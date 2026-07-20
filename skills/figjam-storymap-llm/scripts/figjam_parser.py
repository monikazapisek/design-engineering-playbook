"""
figjam_parser.py
================
Parser FigJam Story Map (Jeff Patton methodology) → Markdown / JSON.

Czyta tablicę FigJam przez Figma REST API, grupuje sticky/shape w sekcje,
mapuje User Stories do Tasks algorytmicznie po osi X, renderuje ustrukturyzowany
backlog gotowy do Notion / Linear / Jira lub jako kontekst dla agenta kodującego.

Usage:
    python figjam_parser.py --file-key {FILE_KEY} --token $FIGMA_TOKEN > story-map.md
    python figjam_parser.py --file-key {FILE_KEY} --token $FIGMA_TOKEN --format json > story-map.json

Requirements:
    pip install requests

License: MIT
Author: Monika Zapisek (product-handoff-lab)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import requests


FIGMA_API_BASE = "https://api.figma.com/v1/files/{file_key}"

# Sekcje kanoniczne (kolejność ma znaczenie dla renderu)
SECTION_ROOT = "[STORY_MAP]"
SECTION_AI_README = "[00_SECTION_AI_Readme]"
SECTION_PERSONA = "[USER_SEGMENT_or_PERSONA]"
SECTION_BACKBONE_ACTIVITIES = "[01_SECTION_BACKBONE_Activities]"
SECTION_BACKBONE_TASKS = "[02_SECTION_BACKBONE_User_Tasks]"
RELEASE_SECTION_PREFIX = "[0"  # [03_..., [04_..., [05_... — releases

# Tagi taksonomii na kartkach
TAG_STORY = "[STORY]"
TAG_ACT = "[ACT_"
TAG_TASK = "[TASK_"
TAG_RELEASE = re.compile(r"\[V([123])\]")
TAG_PRIORITY = re.compile(r"\[P([123])\]")
TAG_OWNER = re.compile(r"@(UX|DEV|PM|BIZ|QA)", re.IGNORECASE)


@dataclass
class StickyItem:
    """Jedna kartka na kanwie FigJam (STICKY lub SHAPE_WITH_TEXT)."""

    id: str
    text: str
    x: float
    y: float
    width: float
    height: float
    color: Optional[str] = None
    section_id: Optional[str] = None
    section_name: Optional[str] = None
    # Pola wynikowe (po mapowaniu)
    release: Optional[str] = None
    priority: Optional[str] = None
    owner: Optional[str] = None
    acceptance_criteria: List[str] = field(default_factory=list)
    story_sentence: Optional[str] = None
    mapped_task_id: Optional[str] = None
    mapped_activity_id: Optional[str] = None

    @property
    def center_x(self) -> float:
        return self.x + self.width / 2


@dataclass
class TaskItem:
    """[TASK_XX] z backbone — definiuje kolumnę na osi X."""

    id: str
    name: str
    x: float
    width: float
    activity_id: Optional[str] = None

    def contains_x(self, x: float) -> bool:
        return self.x <= x <= self.x + self.width

    def distance_to_center(self, x: float) -> float:
        center = self.x + self.width / 2
        return abs(x - center)


@dataclass
class ActivityItem:
    """[ACT_XX] z backbone — User Activity (główny cel)."""

    id: str
    name: str


@dataclass
class Connector:
    """Relacja między kartkami przez natywny Connector FigJam."""

    from_id: Optional[str]
    to_id: Optional[str]
    label: str = "CONNECTS_TO"


def fetch_figjam(file_key: str, token: str) -> Dict[str, Any]:
    """Pobiera drzewo obiektów FigJam przez Figma REST API."""
    url = FIGMA_API_BASE.format(file_key=file_key)
    headers = {"X-Figma-Token": token}
    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


def get_bbox(node: Dict[str, Any]) -> Tuple[float, float, float, float]:
    """Wyciąga (x, y, width, height) z absoluteBoundingBox lub layout.locationRelativeToParent."""
    bbox = node.get("absoluteBoundingBox") or {}
    if bbox:
        return (
            float(bbox.get("x", 0)),
            float(bbox.get("y", 0)),
            float(bbox.get("width", 0)),
            float(bbox.get("height", 0)),
        )
    layout = node.get("layout") or {}
    loc = layout.get("locationRelativeToParent") or {}
    dims = layout.get("dimensions") or {}
    return (
        float(loc.get("x", 0)),
        float(loc.get("y", 0)),
        float(dims.get("width", 0)),
        float(dims.get("height", 0)),
    )


def get_text(node: Dict[str, Any]) -> str:
    """Wyciąga tekst z pola `characters`."""
    return (node.get("characters") or "").strip()


def get_color(node: Dict[str, Any]) -> Optional[str]:
    """Wyciąga pierwszy kolor fill."""
    fills = node.get("fills") or []
    if fills and isinstance(fills, list):
        first = fills[0]
        if isinstance(first, str):
            return first
        if isinstance(first, dict) and "color" not in first:
            return None
    return None


def is_release_section(name: str) -> bool:
    """Czy sekcja to Release (V1/V2/V3)?"""
    return name.startswith("[03_") or name.startswith("[04_") or name.startswith("[05_")


def parse_release_from_section(name: str) -> Optional[str]:
    """Parsuje V1/V2/V3 z nazwy sekcji release."""
    match = re.search(r"\[V([123])\]", name) or re.search(r"Release\s*([123])", name, re.IGNORECASE)
    if match:
        return f"V{match.group(1)}"
    if name.startswith("[03_"):
        return "V1"
    if name.startswith("[04_"):
        return "V2"
    if name.startswith("[05_"):
        return "V3"
    return None


def parse_story_text(text: str) -> Dict[str, Any]:
    """Parsuje treść kartki [STORY] na komponenty."""
    result: Dict[str, Any] = {
        "release": None,
        "priority": None,
        "owner": None,
        "story_sentence": None,
        "acceptance_criteria": [],
    }

    if not text:
        return result

    release_match = TAG_RELEASE.search(text)
    if release_match:
        result["release"] = f"V{release_match.group(1)}"

    priority_match = TAG_PRIORITY.search(text)
    if priority_match:
        result["priority"] = f"P{priority_match.group(1)}"

    owner_match = TAG_OWNER.search(text)
    if owner_match:
        result["owner"] = owner_match.group(0).upper()

    # Split na sekcję AC (po "AC:" lub po podwójnym newline)
    ac_split = re.split(r"\n\s*AC\s*:?\s*\n", text, maxsplit=1)
    main_part = ac_split[0]
    ac_part = ac_split[1] if len(ac_split) > 1 else ""

    # Usuń tagi z głównego zdania
    sentence = re.sub(r"\[(STORY|V[123]|P[123])\]", "", main_part)
    sentence = re.sub(r"@(UX|DEV|PM|BIZ|QA)", "", sentence, flags=re.IGNORECASE)
    sentence = re.sub(r"\s+", " ", sentence).strip()
    result["story_sentence"] = sentence or None

    if ac_part:
        # AC jako linie po myślniku lub newline
        lines = [ln.strip().lstrip("-").strip() for ln in re.split(r"\n", ac_part) if ln.strip()]
        result["acceptance_criteria"] = [ln for ln in lines if ln]

    return result


def traverse(
    node: Dict[str, Any],
    current_section_id: Optional[str],
    current_section_name: Optional[str],
    sections: Dict[str, Dict[str, Any]],
    stickies: List[StickyItem],
    tasks: List[TaskItem],
    activities: List[ActivityItem],
    connectors: List[Connector],
) -> None:
    """Rekurencyjne przejście drzewa węzłów FigJam."""
    node_type = node.get("type")
    node_id = node.get("id", "")
    node_name = node.get("name", "")

    if node_type == "SECTION":
        current_section_id = node_id
        current_section_name = node_name
        sections[node_id] = {
            "name": node_name,
            "parent_id": None,
            "children_section_ids": [],
            "stickies": [],
        }

    elif node_type in ("STICKY", "SHAPE_WITH_TEXT"):
        text = get_text(node)
        x, y, w, h = get_bbox(node)
        color = get_color(node)
        sticky = StickyItem(
            id=node_id,
            text=text,
            x=x,
            y=y,
            width=w,
            height=h,
            color=color,
            section_id=current_section_id,
            section_name=current_section_name,
        )

        # Identyfikuj backbone
        if text.startswith(TAG_TASK) or TAG_TASK in text:
            t_id = re.search(r"\[TASK_\d+\]", text)
            tasks.append(
                TaskItem(
                    id=node_id,
                    name=text,
                    x=x,
                    width=w,
                )
            )
        elif text.startswith(TAG_ACT) or TAG_ACT in text:
            activities.append(
                ActivityItem(
                    id=node_id,
                    name=text,
                )
            )
        elif text.startswith(TAG_STORY) or TAG_STORY in text:
            parsed = parse_story_text(text)
            sticky.release = parsed["release"]
            sticky.priority = parsed["priority"]
            sticky.owner = parsed["owner"]
            sticky.story_sentence = parsed["story_sentence"]
            sticky.acceptance_criteria = parsed["acceptance_criteria"]
            stickies.append(sticky)
        else:
            # Inne kartki (legenda, persona) — zapisz jako sticky bez parsowania
            stickies.append(sticky)

    elif node_type == "CONNECTOR":
        cstart = node.get("connectorStart") or {}
        cend = node.get("connectorEnd") or {}
        label = get_text(node) or "CONNECTS_TO"
        connectors.append(
            Connector(
                from_id=cstart.get("endpointNodeId"),
                to_id=cend.get("endpointNodeId"),
                label=label,
            )
        )

    # Rekurencja
    for child in node.get("children") or []:
        traverse(
            child,
            current_section_id,
            current_section_name,
            sections,
            stickies,
            tasks,
            activities,
            connectors,
        )


def map_stories_to_tasks(stickies: List[StickyItem], tasks: List[TaskItem]) -> None:
    """Mapuje [STORY] do [TASK] algorytmicznie po osi X.

    Algorytm:
    1. Dla każdej story bierz środek X (center_x).
    2. Znajdź task, którego range X zawiera center story.
    3. Fallback: najbliższy środek taska.
    """
    if not tasks:
        return

    for sticky in stickies:
        if not sticky.text.startswith(TAG_STORY) and TAG_STORY not in sticky.text:
            continue
        cx = sticky.center_x
        # Range match
        candidate = None
        for t in tasks:
            if t.contains_x(cx):
                candidate = t
                break
        # Nearest center fallback
        if candidate is None:
            candidate = min(tasks, key=lambda t: t.distance_to_center(cx))
        sticky.mapped_task_id = candidate.id


def map_tasks_to_activities(tasks: List[TaskItem], activities: List[ActivityItem]) -> None:
    """Mapuje [TASK] do [ACT] — w prostej wersji: pozycja Y (activity nad task)."""
    # W FigJam template: activities leżą nad tasks w tej samej kolumnie X.
    # Mapowanie przez overlap X (prosty nearest).
    if not activities:
        return
    for t in tasks:
        # Tu można rozszerzyć o pozycje activities — na razie zostawiamy puste
        t.activity_id = None


def group_stickies_by_section(stickies: List[StickyItem]) -> Dict[str, List[StickyItem]]:
    """Grupuje stickies po section_name."""
    groups: Dict[str, List[StickyItem]] = {}
    for s in stickies:
        key = s.section_name or "(unsectioned)"
        groups.setdefault(key, []).append(s)
    return groups


def render_markdown(
    sections: Dict[str, Dict[str, Any]],
    stickies: List[StickyItem],
    tasks: List[TaskItem],
    activities: List[ActivityItem],
    connectors: List[Connector],
) -> str:
    """Renderuje ustrukturyzowany Markdown z hierarchią Release → Activity → Task → Story."""
    out: List[str] = ["# Story Map — parsed backlog\n"]
    out.append("_Source: FigJam, parsed by `figjam-storymap-llm` skill._\n")

    # Sekcja AI Readme (legenda)
    readme_items = [s for s in stickies if s.section_name and "00_" in s.section_name]
    if readme_items:
        out.append("## 00. AI ReadMe (legenda)\n")
        for s in readme_items:
            if s.text:
                out.append(f"```\n{s.text}\n```\n")

    # Persona
    persona_items = [s for s in stickies if s.section_name and "USER_SEGMENT" in s.section_name.upper()]
    if persona_items:
        out.append("## Persona / User Segment\n")
        for s in persona_items:
            if s.text:
                out.append(f"- {s.text}\n")
        out.append("")

    # Backbone — Activities
    out.append("## 01. Backbone — Activities\n")
    for a in activities:
        out.append(f"- **{a.id}** — {a.name}")
    out.append("")

    # Backbone — Tasks
    out.append("## 02. Backbone — Tasks\n")
    for t in tasks:
        out.append(f"- **{t.id}** — {t.name} (x={t.x:.0f}, w={t.width:.0f})")
    out.append("")

    # Releases (po kolei V1, V2, V3)
    releases: Dict[str, List[StickyItem]] = {"V1": [], "V2": [], "V3": []}
    for s in stickies:
        if not (s.text.startswith(TAG_STORY) or TAG_STORY in s.text):
            continue
        if s.release:
            releases.setdefault(s.release, []).append(s)
        elif s.section_name and is_release_section(s.section_name):
            r = parse_release_from_section(s.section_name)
            if r:
                s.release = r
                releases.setdefault(r, []).append(s)

    for release_key in ["V1", "V2", "V3"]:
        items = releases.get(release_key, [])
        if not items:
            continue
        out.append(f"## {release_key} — Release {release_key[1]}\n")
        # Grupuj po mapped_task_id
        by_task: Dict[Optional[str], List[StickyItem]] = {}
        for s in items:
            by_task.setdefault(s.mapped_task_id, []).append(s)

        for task_id, stories in by_task.items():
            task_name = next((t.name for t in tasks if t.id == task_id), None)
            if task_id:
                out.append(f"### Task: {task_name or task_id}\n")
            else:
                out.append(f"### Task: (unassigned — outside any column)\n")
            for s in stories:
                line = f"- [STORY] "
                if s.release:
                    line += f"[{s.release}] "
                if s.priority:
                    line += f"[{s.priority}] "
                if s.story_sentence:
                    line += s.story_sentence
                if s.owner:
                    line += f" {s.owner}"
                out.append(line)
                if s.acceptance_criteria:
                    out.append("  - **AC:**")
                    for ac in s.acceptance_criteria:
                        out.append(f"    - {ac}")
            out.append("")

    # Connectors
    if connectors:
        out.append("## Connector relations\n")
        for c in connectors:
            out.append(f"- `{c.from_id}` --[{c.label}]--> `{c.to_id}`")
        out.append("")

    # Unsectioned warnings
    unsectioned = [s for s in stickies if not s.section_id]
    if unsectioned:
        out.append("## ⚠ Unsectioned items (poza `[STORY_MAP]` root)\n")
        for s in unsectioned:
            out.append(f"- {s.id}: {s.text[:80]}")
        out.append("")

    return "\n".join(out)


def render_json(
    stickies: List[StickyItem],
    tasks: List[TaskItem],
    activities: List[ActivityItem],
    connectors: List[Connector],
) -> str:
    """Renderuje JSON dla PM toolingu."""
    payload = {
        "activities": [{"id": a.id, "name": a.name} for a in activities],
        "tasks": [
            {"id": t.id, "name": t.name, "x": t.x, "width": t.width, "activity_id": t.activity_id}
            for t in tasks
        ],
        "stories": [
            {
                "id": s.id,
                "release": s.release,
                "priority": s.priority,
                "owner": s.owner,
                "story_sentence": s.story_sentence,
                "acceptance_criteria": s.acceptance_criteria,
                "mapped_task_id": s.mapped_task_id,
                "section_name": s.section_name,
                "raw_text": s.text,
            }
            for s in stickies
            if s.text.startswith(TAG_STORY) or TAG_STORY in s.text
        ],
        "connectors": [
            {"from": c.from_id, "to": c.to_id, "label": c.label} for c in connectors
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="FigJam Story Map parser → Markdown/JSON (Patton methodology, LLM-ready)."
    )
    parser.add_argument("--file-key", required=True, help="Figma file key z URL: figma.com/board/{key}/...")
    parser.add_argument(
        "--token",
        default=os.getenv("FIGMA_TOKEN", ""),
        help="Figma personal access token (lub env FIGMA_TOKEN).",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Format wyjścia.",
    )
    parser.add_argument("--input", help="Opcjonalnie: ścieżka do zapisanego JSON FigJam (zamiast API).")

    args = parser.parse_args()

    if not args.token and not args.input:
        print("ERROR: brak FIGMA_TOKEN. Ustaw env lub podaj --token.", file=sys.stderr)
        return 2

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = fetch_figjam(args.file_key, args.token)

    document = data.get("document") or data  # wsparcie /files i /nodes
    if "nodes" in data and not document:
        # /nodes zwraca {nodes: {id: {document: ...}}}
        first_node = next(iter(data["nodes"].values()), {})
        document = first_node.get("document", {})

    sections: Dict[str, Dict[str, Any]] = {}
    stickies: List[StickyItem] = []
    tasks: List[TaskItem] = []
    activities: List[ActivityItem] = []
    connectors: List[Connector] = []

    traverse(document, None, None, sections, stickies, tasks, activities, connectors)

    map_stories_to_tasks(stickies, tasks)
    map_tasks_to_activities(tasks, activities)

    if args.format == "json":
        print(render_json(stickies, tasks, activities, connectors))
    else:
        print(render_markdown(sections, stickies, tasks, activities, connectors))

    return 0


if __name__ == "__main__":
    sys.exit(main())