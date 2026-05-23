"""
Structured output schema for evidence-based STEP assembly planning.

The schema is intentionally separated from clamping_schema.py.  Clamping analysis
describes one part's grasping needs; this module describes the whole assembly
planning result: part analyses, evidence traces, precedence DAG, sequence steps,
risks, and review notes.
"""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field


Confidence = Literal["High", "Medium", "Low", "Unknown"]

EvidenceLevel = Literal[
    "L0_metadata_fact",
    "L1_geometry_fact",
    "L2_visual_artifact",
    "L3_heuristic_candidate",
    "L4_agent_inference",
]

AssemblyType = Literal[
    "base_placement",
    "insertion",
    "stacking",
    "fastening_like",
    "closure",
    "subassembly_join",
    "adjustment_orientation",
    "retention",
    "inspection",
    "unknown",
]

ProcessPrimitiveType = Literal[
    "planar_mating",
    "cylindrical_insertion",
    "shaft_hole_insertion",
    "threaded_fastening",
    "pin_insertion",
    "stacking",
    "cover_closure",
    "snap_or_retention",
    "orientation_alignment",
    "subassembly_merge",
    "inspection",
    "unknown",
]

GripperType = Literal[
    "vacuum_pad",
    "parallel_jaw",
    "soft_parallel_jaw",
    "v_block",
    "three_jaw_chuck",
    "magnetic_driver",
    "inner_expansion",
    "custom_fixture",
    "manual_or_unknown",
    "unknown",
]

PartRole = Literal[
    "base",
    "moving",
    "support",
    "fastener_like",
    "held_by_fixture",
    "held_by_robot",
    "unknown",
]

DependencyType = Literal[
    "spatial_prerequisite",
    "mating_sequence",
    "access_preservation",
    "blocker_precedence",
    "enclosure_precedence",
    "subassembly_merge",
    "closure_sequence",
    "fastening_prerequisite",
    "tooling_prerequisite",
    "human_review_required",
    "unknown",
]


class EvidenceReference(BaseModel):
    """A traceable fact, heuristic result, or visual artifact used by the plan."""

    evidence_id: str = Field(..., description="Stable local identifier for citing this evidence.")
    source_tool: str = Field(..., description="MCP tool or agent/subagent that produced the evidence.")
    evidence_level: EvidenceLevel
    summary: str = Field(..., description="Short statement of what the evidence says.")
    project_id: Optional[str] = None
    part_ids: List[str] = Field(default_factory=list)
    face_ids: List[str] = Field(default_factory=list)
    pair_ids: List[str] = Field(default_factory=list)
    artifact_path: Optional[str] = Field(
        default=None,
        description="image_path or other saved artifact path when available.",
    )
    raw_ref: Optional[str] = Field(
        default=None,
        description="Optional compact pointer to the raw tool call/result, e.g. call id or file path.",
    )
    confidence: Confidence = "Unknown"
    method: Optional[str] = Field(
        default=None,
        description="Algorithm/method metadata from the tool, especially for heuristic evidence.",
    )
    limitations: List[str] = Field(default_factory=list)


class DirectionCandidate(BaseModel):
    direction: List[float] = Field(
        ...,
        min_length=3,
        max_length=3,
        description="Normalized or tool-returned direction vector [x, y, z].",
    )
    label: Optional[str] = Field(default=None, description="Human-readable label such as +X or custom-1.")
    blockers: List[str] = Field(default_factory=list)
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"
    notes: Optional[str] = None


class SurfaceReference(BaseModel):
    """A lightweight reference to a grasping, assembly, support, or alignment surface."""

    surface_id: Optional[str] = Field(
        default=None,
        description="Known face_id or local surface label when available.",
    )
    part_id: str
    role: Literal[
        "grasp_surface",
        "assembly_surface",
        "support_surface",
        "alignment_surface",
        "avoid_contact_surface",
        "unknown",
    ] = "unknown"
    geometry_type: Literal["planar", "cylindrical", "conical", "thread_like", "freeform", "unknown"] = "unknown"
    description: str = ""
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class PoseRequirement(BaseModel):
    """Pose/orientation information needed by downstream workstation planning."""

    approach_direction: Optional[List[float]] = Field(default=None, min_length=3, max_length=3)
    insertion_axis: Optional[List[float]] = Field(default=None, min_length=3, max_length=3)
    rotation_axis: Optional[List[float]] = Field(default=None, min_length=3, max_length=3)
    required_rotation: Optional[str] = Field(
        default=None,
        description="Qualitative rotation requirement, e.g. align notch, rotate about Z, threaded rotation unknown turns.",
    )
    orientation_constraints: List[str] = Field(default_factory=list)
    pose_confidence: Confidence = "Unknown"
    evidence_ids: List[str] = Field(default_factory=list)


class ToolingRequirement(BaseModel):
    """Fixture and gripper intent, not a final robot end-effector command."""

    gripper_type: GripperType = "unknown"
    fixture_type: Optional[str] = None
    grasp_surfaces: List[SurfaceReference] = Field(default_factory=list)
    keep_clear_surfaces: List[SurfaceReference] = Field(default_factory=list)
    required_capabilities: List[str] = Field(
        default_factory=list,
        description="Examples: axial insertion, rotation, compliant grasp, force control, vision alignment.",
    )
    missing_inputs: List[str] = Field(
        default_factory=list,
        description="Material, stiffness, mass, force, tolerance, friction, or forbidden surfaces needed later.",
    )
    confidence: Confidence = "Unknown"


class PartRoleAssignment(BaseModel):
    part_id: str
    role: PartRole = "unknown"
    reason: str = ""
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class AssemblyInterfaceSpec(BaseModel):
    """Process-intent description for a node/step interface."""

    process_primitive: ProcessPrimitiveType = "unknown"
    base_part_ids: List[str] = Field(default_factory=list)
    moving_part_ids: List[str] = Field(default_factory=list)
    role_assignments: List[PartRoleAssignment] = Field(default_factory=list)
    assembly_surfaces: List[SurfaceReference] = Field(default_factory=list)
    pose_requirement: PoseRequirement = Field(default_factory=PoseRequirement)
    tooling_requirement: ToolingRequirement = Field(default_factory=ToolingRequirement)
    expected_contact_or_mate: Optional[str] = Field(
        default=None,
        description="Cautious interface description such as planar mate candidate or shaft-hole insertion candidate.",
    )
    verification_need: List[str] = Field(default_factory=list)
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class ContactRelation(BaseModel):
    related_part_id: str
    relation_type: str = Field(default="unknown")
    contact_face_ids: List[str] = Field(default_factory=list)
    pair_id: Optional[str] = None
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"
    is_heuristic: bool = Field(
        default=True,
        description="True unless confirmed by exact CAD solver or human annotation.",
    )


class PartAssemblyFeatureAnalysis(BaseModel):
    part_id: str
    name: Optional[str] = None
    basic_features: List[str] = Field(
        default_factory=list,
        description="Evidence-supported features, e.g. hole-like, shaft-like, planar-mate.",
    )
    geometry_summary: str = ""
    contact_relations: List[ContactRelation] = Field(default_factory=list)
    removal_directions: List[DirectionCandidate] = Field(default_factory=list)
    install_directions: List[DirectionCandidate] = Field(default_factory=list)
    clamping_category: Optional[str] = Field(
        default=None,
        description="Optional clamping strategy category from part-feature-analyzer.",
    )
    candidate_grasp_surfaces: List[str] = Field(default_factory=list)
    process_accessibility: Literal[
        "accessible",
        "blocked",
        "requires_prior_subassembly",
        "requires_human_review",
        "unknown",
    ] = "unknown"
    evidence_ids: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class ConstraintNode(BaseModel):
    node_id: str
    label: str
    parts: List[str] = Field(default_factory=list)
    subassembly_id: Optional[str] = None
    assembly_type: AssemblyType = "unknown"
    interface_spec: AssemblyInterfaceSpec = Field(default_factory=AssemblyInterfaceSpec)
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class ConstraintEdge(BaseModel):
    edge_id: str
    source: str = Field(..., description="Predecessor node id.")
    target: str = Field(..., description="Successor node id.")
    dependency_type: DependencyType
    rationale: str
    evidence_ids: List[str] = Field(default_factory=list)
    is_hard_constraint: bool = Field(
        default=False,
        description="True for constraints strongly supported by geometry or explicit process input.",
    )
    confidence: Confidence = "Unknown"


class ConstraintDAG(BaseModel):
    nodes: List[ConstraintNode] = Field(default_factory=list)
    edges: List[ConstraintEdge] = Field(default_factory=list)
    unresolved_cycles: List[str] = Field(
        default_factory=list,
        description="Describe any cycle or contradictory dependency that requires review.",
    )


class AssemblyStep(BaseModel):
    step_id: str
    label: str
    parts: List[str] = Field(default_factory=list)
    subassembly_id: Optional[str] = None
    assembly_type: AssemblyType = "unknown"
    process_primitive: ProcessPrimitiveType = "unknown"
    operation: str
    interface_spec: AssemblyInterfaceSpec = Field(default_factory=AssemblyInterfaceSpec)
    direction: Optional[List[float]] = Field(default=None, min_length=3, max_length=3)
    prerequisites: List[str] = Field(default_factory=list)
    blockers_resolved: List[str] = Field(default_factory=list)
    data_evidence_ids: List[str] = Field(default_factory=list)
    visual_evidence_ids: List[str] = Field(default_factory=list)
    best_visual_evidence_id: Optional[str] = None
    assumptions: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class SubassemblyPlan(BaseModel):
    subassembly_id: str
    label: str
    parts: List[str]
    internal_step_ids: List[str] = Field(default_factory=list)
    merge_step_id: Optional[str] = None
    rationale: str = ""
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: Confidence = "Unknown"


class OpenRisk(BaseModel):
    risk_id: str
    description: str
    affected_parts: List[str] = Field(default_factory=list)
    affected_steps: List[str] = Field(default_factory=list)
    evidence_ids: List[str] = Field(default_factory=list)
    severity: Literal["High", "Medium", "Low"] = "Medium"
    recommended_review: str = ""


class AssemblyPlanningResult(BaseModel):
    schema_version: Literal["step-to-process/assembly-plan/v1"] = "step-to-process/assembly-plan/v1"
    project_id: str
    model_summary: str = ""
    part_analyses: List[PartAssemblyFeatureAnalysis] = Field(default_factory=list)
    evidence_trace: List[EvidenceReference] = Field(default_factory=list)
    constraint_dag: ConstraintDAG = Field(default_factory=ConstraintDAG)
    sequence_steps: List[AssemblyStep] = Field(default_factory=list)
    subassemblies: List[SubassemblyPlan] = Field(default_factory=list)
    open_risks: List[OpenRisk] = Field(default_factory=list)
    global_assumptions: List[str] = Field(default_factory=list)
    human_review_items: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


def get_assembly_plan_json_schema() -> Dict[str, Any]:
    """Return the JSON schema used to constrain the assembly planning result."""

    return AssemblyPlanningResult.model_json_schema()


def create_empty_assembly_plan(project_id: str, model_summary: str = "") -> AssemblyPlanningResult:
    """Create a valid empty planning result as a scaffold for agent output."""

    return AssemblyPlanningResult(project_id=project_id, model_summary=model_summary)


__all__ = [
    "AssemblyPlanningResult",
    "AssemblyStep",
    "AssemblyType",
    "Confidence",
    "ConstraintDAG",
    "ConstraintEdge",
    "ConstraintNode",
    "ContactRelation",
    "DependencyType",
    "DirectionCandidate",
    "EvidenceLevel",
    "EvidenceReference",
    "AssemblyInterfaceSpec",
    "OpenRisk",
    "PartAssemblyFeatureAnalysis",
    "PartRole",
    "PartRoleAssignment",
    "PoseRequirement",
    "ProcessPrimitiveType",
    "GripperType",
    "SurfaceReference",
    "SubassemblyPlan",
    "ToolingRequirement",
    "create_empty_assembly_plan",
    "get_assembly_plan_json_schema",
]
