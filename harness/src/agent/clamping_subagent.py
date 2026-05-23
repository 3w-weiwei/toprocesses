"""
Part feature and clamping strategy subagent.

The exported builder keeps the old function name build_clamping_subagent for
compatibility, but the subagent exposed to deepagents is now named
part-feature-analyzer.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

from src.agent.part_feature_schema import PartFeatureAnalysisResult


_RENDER_TOOL_NAME = "cad_render_part_multiview"

_SCHEMA_JSON = json.dumps(
    PartFeatureAnalysisResult.model_json_schema(),
    indent=2,
    ensure_ascii=False,
)


_PART_FEATURE_SUBAGENT_PROMPT = f"""你是机械装配体的单零件装配特征分析子智能体。

你的职责不是输出装配序列，而是对一个 part_id 做稳定、可追溯的 PartFeatureAnalysisResult JSON。

强制流程：
1. 收到 project_id 和 part_id 后，只调用一次 `{_RENDER_TOOL_NAME}`。
2. 调用参数：project_id、part_id、size=256。
3. 不要调用其他 MCP 工具，不要并发调用视觉工具。
4. 工具会返回 8 视角图片，以及增强 compactPart 几何统计。

分析内容：
- 识别几何类别：plate、disk、shaft、block、ring、fastener_like、spring_like、seal_like、freeform、mixed、unknown。
- 提取装配相关特征：hole、through_hole、blind_hole、shaft、cylindrical_surface、planar_surface、thread_like、slot、notch、boss、step、keyway_like、pin_like、thin_wall、cover_like、orientation_feature。
- 分析对称性和方向性：axisymmetric、rotational、mirror、bilateral、asymmetric、unknown；记录缺口、偏心孔、键槽、非对称凸台等定向特征。
- 区分候选装夹面、候选装配面、候选支撑面、需避免接触的面。
- 在 clamping_strategy 中给出装夹策略推断，但必须把它视为工艺推断，而非几何事实。

证据规则：
- 视觉上可见的内容写入 visual_evidence_paths 和 evidence_summary。
- compactPart 中的 plane/cylinder/freeform 面统计、max_plane_area、max_cylinder_length/radius、has_main_axis 等只能作为 mesh_heuristic。
- 不得仅凭图片断言材料、磁性、刚度、公差、装配力、表面粗糙度、禁夹区或真实螺纹标准。
- 磁吸、低刚度、装配力、禁夹面等没有外部工艺输入时，必须写入 uncertain_information。
- 如果图片或几何统计不足，使用 unknown 并降低 confidence。

输出要求：
- 只输出一个合法 JSON 对象。
- 不要 Markdown，不要解释性正文。
- 字段必须符合以下 JSON Schema：

{_SCHEMA_JSON}
"""


_SUBAGENT_DESCRIPTION = (
    "对单个零件进行装配特征提取和装夹策略初步推断。"
    "输入必须包含 project_id 和 part_id。"
    f"子智能体只调用 `{_RENDER_TOOL_NAME}` 获取 8 视角图片和 compactPart 几何统计，"
    "输出 PartFeatureAnalysisResult JSON。"
)


def _find_tool(mcp_tools: List[Any], tool_name: str) -> Any:
    tool = next((t for t in mcp_tools if getattr(t, "name", None) == tool_name), None)
    if tool is None:
        available = [getattr(t, "name", "<unnamed>") for t in mcp_tools]
        raise ValueError(f"未在 MCP 工具中找到 `{tool_name}`。当前可用工具: {available}")
    return tool


def build_part_feature_subagent(mcp_tools: List[Any]) -> Dict[str, Any]:
    render_tool = _find_tool(mcp_tools, _RENDER_TOOL_NAME)
    return {
        "name": "part-feature-analyzer",
        "description": _SUBAGENT_DESCRIPTION,
        "system_prompt": _PART_FEATURE_SUBAGENT_PROMPT,
        "tools": [render_tool],
    }


def build_clamping_subagent(mcp_tools: List[Any]) -> Dict[str, Any]:
    """Backward-compatible builder for older imports."""

    return build_part_feature_subagent(mcp_tools)
