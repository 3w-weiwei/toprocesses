"""
Visual evidence selection subagent.

This subagent hides camera/tool-choice details from the main assembly planner.
It captures a small set of high-value visual candidates and selects the best
evidence path for a stated claim.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

from src.agent.visual_evidence_schema import VisualEvidenceSelectionResult


_VISUAL_TOOL_NAMES = [
    "cad_reset_view_state",
    "cad_render_view",
    "cad_render_part_multiview",
    "cad_render_contact_pair_multiview",
    "cad_render_move_preview",
    "cad_render_target_section",
    "cad_render_section_view",
    "cad_collect_visual_evidence",
]

_SCHEMA_JSON = json.dumps(
    VisualEvidenceSelectionResult.model_json_schema(),
    indent=2,
    ensure_ascii=False,
)


_VISUAL_EVIDENCE_PROMPT = f"""You are the visual evidence selector for STEP assembly analysis.

Your job is not to plan the assembly sequence. Your job is to capture and select
the most informative visual evidence for an intended claim while using as little
context as possible.

Inputs usually include:
- project_id
- target_type: overview / evidence_scout / part / contact_pair / removal_direction / hidden_interface / subassembly
- intended_claim
- optional part_ids, face_ids, pair_id, direction, distance

Tool policy:
1. Start a new visual task with cad_reset_view_state unless the request explicitly asks to keep the current state.
2. Visual tools share viewer state. Never call visual tools in parallel.
3. Keep captures small and selective. Usually 1-3 tool calls are enough.
4. Do not call cad_render_disassembly_exploded_view. It is intentionally excluded because it often produces weak exploded evidence.

Target-type policy:
- overview: use cad_collect_visual_evidence(mode="overview") or cad_render_view.
- evidence_scout: after part features are known, select a compact set of rich overview/contact/section/part-focus images that best explain the assembly. Prefer cad_collect_visual_evidence with overview, part_focus, or section_sweep modes.
- part: use cad_render_part_multiview.
- contact_pair: use cad_render_contact_pair_multiview. If the interface is hidden, add cad_render_target_section or cad_collect_visual_evidence(mode="section_sweep").
- removal_direction: use cad_render_move_preview only when a specific direction is already proposed. The image is evidence for visibility and rough straight-line motion, not proof of a full path.
- hidden_interface: use cad_collect_visual_evidence(mode="section_sweep"), optionally cad_render_target_section.
- subassembly: use cad_collect_visual_evidence(mode="overview" or "part_focus") and choose views that show the subassembly boundary.

Selection criteria:
- target parts are visible
- target/contact faces are visible
- motion or insertion direction is visible when relevant
- occlusion is low
- framing is complete
- viewer state is clean
- the image actually supports intended_claim

Output requirements:
- Output exactly one valid JSON object.
- Do not output Markdown or explanatory prose.
- selected_image_path must come from image_path or views[].image_path returned by a tool.
- If no useful image is available, set selected_image_path to null, evidence_quality to Low, and provide recapture_recommendation.
- Use this JSON Schema:

{_SCHEMA_JSON}
"""


def build_visual_evidence_subagent(mcp_tools: List[Any]) -> Dict[str, Any]:
    tools = [t for t in mcp_tools if getattr(t, "name", None) in _VISUAL_TOOL_NAMES]
    found = {getattr(t, "name", None) for t in tools}
    missing = [name for name in _VISUAL_TOOL_NAMES if name not in found]
    if not tools:
        available = [getattr(t, "name", "<unnamed>") for t in mcp_tools]
        raise ValueError(f"No visual MCP tools were found. Available tools: {available}")

    description = (
        "Selects compact, high-information CAD visual evidence for a stated claim. "
        "Input project_id, target_type, intended_claim, and optional part_ids/pair_id/"
        "face_ids/direction. Outputs VisualEvidenceSelectionResult JSON."
    )
    if missing:
        description += f" Some optional visual tools are unavailable: {missing}."

    return {
        "name": "visual-evidence-selector",
        "description": description,
        "system_prompt": _VISUAL_EVIDENCE_PROMPT,
        "tools": tools,
    }
