"""
Schema for single-part assembly feature extraction.

This schema separates two tasks that were previously mixed together:

1. Part feature extraction: what assembly-relevant geometry is visible or
   supported by CAD statistics.
2. Clamping strategy inference: how the part may be grasped or fixtured for a
   flexible assembly cell.
"""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


Confidence = Literal["High", "Medium", "Low", "Unknown"]

YesNoUnknown = Literal["yes", "no", "unknown"]

GeometricClass = Literal[
    "plate",
    "disk",
    "shaft",
    "block",
    "ring",
    "fastener_like",
    "spring_like",
    "seal_like",
    "freeform",
    "mixed",
    "unknown",
]

AssemblyFeatureType = Literal[
    "hole",
    "through_hole",
    "blind_hole",
    "shaft",
    "cylindrical_surface",
    "planar_surface",
    "thread_like",
    "slot",
    "notch",
    "boss",
    "step",
    "keyway_like",
    "pin_like",
    "thin_wall",
    "cover_like",
    "orientation_feature",
    "unknown",
]

SymmetryType = Literal[
    "axisymmetric",
    "rotational",
    "mirror",
    "bilateral",
    "asymmetric",
    "unknown",
]

SurfaceRole = Literal[
    "candidate_grasp_surface",
    "candidate_assembly_surface",
    "candidate_support_surface",
    "candidate_orientation_surface",
    "avoid_if_possible",
    "unknown",
]

ClampingCategory = Literal[
    "end_face_grasp_side_wall_assembly",
    "slender_shaft",
    "magnetic_adsorption_candidate",
    "complex_freeform",
    "short_thick_shaft",
    "low_stiffness",
    "unknown",
]


class ObservedAssemblyFeature(BaseModel):
    feature_type: AssemblyFeatureType
    description: str
    location_hint: Optional[str] = Field(
        default=None,
        description="Coarse location such as end face, side wall, outer cylinder, inner hole.",
    )
    evidence: List[str] = Field(
        default_factory=list,
        description="Visible or CAD-statistical basis for the feature.",
    )
    confidence: Confidence = "Unknown"


class CandidateSurface(BaseModel):
    surface_label: str = Field(..., description="Human-readable surface name.")
    role: SurfaceRole = "unknown"
    geometry_type: Literal["planar", "cylindrical", "conical", "freeform", "edge_region", "unknown"] = "unknown"
    quality: Literal["good", "usable", "poor", "unknown"] = "unknown"
    reason: str = ""
    risks: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class SymmetryAndOrientationAnalysis(BaseModel):
    symmetry_type: SymmetryType = "unknown"
    main_axis: Optional[List[float]] = Field(default=None, min_length=3, max_length=3)
    has_orientation_feature: YesNoUnknown = "unknown"
    orientation_features: List[str] = Field(default_factory=list)
    front_back_difference: YesNoUnknown = "unknown"
    notes: str = ""
    confidence: Confidence = "Unknown"


class DimensionalHeuristicSummary(BaseModel):
    bbox_aspect: str = Field(default="", description="Qualitative bbox aspect ratio summary.")
    length_to_diameter_ratio: Optional[float] = None
    max_plane_area_hint: Optional[str] = None
    cylindrical_surface_hint: Optional[str] = None
    face_composition_hint: Optional[str] = None
    method: str = "mesh_heuristic"
    limitations: List[str] = Field(default_factory=list)


class ClampingStrategyInference(BaseModel):
    predicted_category: ClampingCategory = "unknown"
    recommended_gripper_or_fixture: List[str] = Field(
        default_factory=list,
        description="Examples: vacuum_pad, v_block, three_jaw_chuck, magnetic_driver, inner_expansion, soft_parallel_gripper.",
    )
    candidate_grasp_surfaces: List[CandidateSurface] = Field(default_factory=list)
    forbidden_or_uncertain_surfaces: List[CandidateSurface] = Field(default_factory=list)
    required_process_inputs: List[str] = Field(
        default_factory=list,
        description="Missing process data needed before final fixture decision.",
    )
    rationale: str = ""
    confidence: Confidence = "Unknown"


class PartFeatureAnalysisResult(BaseModel):
    schema_version: Literal["step-to-process/part-feature/v1"] = "step-to-process/part-feature/v1"
    project_id: str
    part_id: str
    part_name: Optional[str] = None
    geometric_class: GeometricClass = "unknown"
    assembly_features: List[ObservedAssemblyFeature] = Field(default_factory=list)
    candidate_surfaces: List[CandidateSurface] = Field(default_factory=list)
    symmetry_and_orientation: SymmetryAndOrientationAnalysis = Field(
        default_factory=SymmetryAndOrientationAnalysis
    )
    dimensional_heuristics: DimensionalHeuristicSummary = Field(
        default_factory=DimensionalHeuristicSummary
    )
    clamping_strategy: ClampingStrategyInference = Field(
        default_factory=ClampingStrategyInference
    )
    visual_evidence_paths: List[str] = Field(
        default_factory=list,
        description="image_path values returned by cad_render_part_multiview when available.",
    )
    evidence_summary: List[str] = Field(default_factory=list)
    uncertain_information: List[str] = Field(default_factory=list)
    final_note: str = ""
    confidence: Confidence = "Unknown"


def get_part_feature_json_schema():
    return PartFeatureAnalysisResult.model_json_schema()


__all__ = [
    "AssemblyFeatureType",
    "CandidateSurface",
    "ClampingCategory",
    "ClampingStrategyInference",
    "Confidence",
    "DimensionalHeuristicSummary",
    "GeometricClass",
    "ObservedAssemblyFeature",
    "PartFeatureAnalysisResult",
    "SurfaceRole",
    "SymmetryAndOrientationAnalysis",
    "SymmetryType",
    "YesNoUnknown",
    "get_part_feature_json_schema",
]
