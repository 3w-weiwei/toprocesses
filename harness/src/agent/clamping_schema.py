"""
Compatibility exports for the old clamping analyzer.

The original clamping schema mixed visible part features with fixture strategy.
New code should import from part_feature_schema.py directly.  These aliases keep
existing imports working while the subagent is renamed to part-feature-analyzer.
"""

from __future__ import annotations

from src.agent.part_feature_schema import (
    CandidateSurface,
    ClampingStrategyInference,
    DimensionalHeuristicSummary,
    ObservedAssemblyFeature,
    PartFeatureAnalysisResult,
    SymmetryAndOrientationAnalysis,
)


ClampingAnalysisResult = PartFeatureAnalysisResult
VisibleGraspingSurfaces = CandidateSurface
ClampingClassification = ClampingStrategyInference
VlmRequiredObservation = PartFeatureAnalysisResult
OverallGeometry = PartFeatureAnalysisResult
EndFaceFeatures = ObservedAssemblyFeature
CylindricalFeatures = ObservedAssemblyFeature
LocalStructureFeatures = ObservedAssemblyFeature
SymmetryAndOrientation = SymmetryAndOrientationAnalysis
DeformablePartFeatures = ObservedAssemblyFeature
SmallFastenerFeatures = ObservedAssemblyFeature


__all__ = [
    "CandidateSurface",
    "ClampingAnalysisResult",
    "ClampingClassification",
    "ClampingStrategyInference",
    "CylindricalFeatures",
    "DeformablePartFeatures",
    "DimensionalHeuristicSummary",
    "EndFaceFeatures",
    "LocalStructureFeatures",
    "ObservedAssemblyFeature",
    "OverallGeometry",
    "PartFeatureAnalysisResult",
    "SmallFastenerFeatures",
    "SymmetryAndOrientation",
    "VlmRequiredObservation",
    "VisibleGraspingSurfaces",
]
