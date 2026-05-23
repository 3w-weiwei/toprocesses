"""
Schema for the visual evidence selection subagent.
"""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


Confidence = Literal["High", "Medium", "Low", "Unknown"]

TargetType = Literal[
    "overview",
    "evidence_scout",
    "part",
    "contact_pair",
    "removal_direction",
    "hidden_interface",
    "subassembly",
    "unknown",
]

VisualToolName = Literal[
    "cad_render_view",
    "cad_render_part_multiview",
    "cad_render_contact_pair_multiview",
    "cad_render_move_preview",
    "cad_render_target_section",
    "cad_render_section_view",
    "cad_collect_visual_evidence",
    "unknown",
]


class VisualEvidenceCandidate(BaseModel):
    candidate_id: str
    source_tool: VisualToolName
    image_path: Optional[str] = None
    view_name: Optional[str] = None
    target_parts_visible: Literal["yes", "partial", "no", "unknown"] = "unknown"
    target_faces_visible: Literal["yes", "partial", "no", "unknown"] = "unknown"
    direction_visible: Literal["yes", "partial", "no", "unknown"] = "unknown"
    occlusion_level: Literal["low", "medium", "high", "unknown"] = "unknown"
    framing_quality: Literal["good", "usable", "poor", "unknown"] = "unknown"
    state_hygiene: Literal["clean", "uncertain", "poor"] = "uncertain"
    supports_claim: Literal["yes", "partial", "no", "unknown"] = "unknown"
    rationale: str = ""
    limitations: List[str] = Field(default_factory=list)


class VisualEvidenceSelectionResult(BaseModel):
    schema_version: Literal["step-to-process/visual-evidence/v1"] = (
        "step-to-process/visual-evidence/v1"
    )
    project_id: str
    target_type: TargetType = "unknown"
    intended_claim: str = Field(
        ...,
        description="The statement this evidence is supposed to support.",
    )
    part_ids: List[str] = Field(default_factory=list)
    face_ids: List[str] = Field(default_factory=list)
    pair_id: Optional[str] = None
    selected_evidence_id: Optional[str] = None
    selected_image_path: Optional[str] = None
    selected_source_tool: VisualToolName = "unknown"
    candidates: List[VisualEvidenceCandidate] = Field(default_factory=list)
    evidence_quality: Confidence = "Unknown"
    selection_reason: str = ""
    recapture_recommendation: Optional[str] = Field(
        default=None,
        description="What to try next if the best evidence is insufficient.",
    )
    final_note: str = ""


__all__ = [
    "Confidence",
    "TargetType",
    "VisualEvidenceCandidate",
    "VisualEvidenceSelectionResult",
    "VisualToolName",
]
