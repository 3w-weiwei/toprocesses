# STEP CAD MCP Evidence Contract

本文档定义 `only_viewer` MCP 工具返回信息在装配序列规划中的证据分层。目标是让上层 Agent 明确区分：

- **事实证据**：由 STEP 缓存、OCCT/网格解析、装配树、零件/面几何、渲染文件直接给出的信息。
- **启发式证据**：由当前算法估计或排序得到的信息，可作为推理依据，但不能当作精确 CAD 求解结果。
- **视觉证据**：由 viewer 截图、剖切、多视角、移动预览等产生的可追溯图像证据。
- **推理结论**：由 Agent 或工艺知识规则在证据基础上生成，不属于 MCP 原始事实。

## 证据等级

| 等级 | 名称 | 含义 | 可用于 |
|---|---|---|---|
| L0 | Metadata Fact | 项目、解析模式、单位、能力标记、统计数量等元信息 | 判断数据可用性、报告范围 |
| L1 | Geometry Fact | 装配树、零件 ID、名称、bbox、face、normal、area、颜色、拓扑统计 | 零件识别、几何关系、候选装配特征 |
| L2 | Visual Artifact | `image_path`、`has_image`、多视角截图、剖切图、移动预览图 | 给装配步骤提供可审计视觉依据 |
| L3 | Heuristic Candidate | 接触候选、接触零件对、清障方向、拆卸方向、blocker、confidence、method | 生成约束候选、排序候选方案 |
| L4 | Agent Inference | 装配类型、前置依赖、子装配、装夹策略、最终序列 | 最终报告和规划输出 |

Agent 输出中必须把 L0-L3 的证据引用和 L4 的推理结论分开描述。

## 工具分组与证据类型

### 模型与几何事实工具

| 工具 | 主要返回 | 证据类型 | 注意事项 |
|---|---|---|---|
| `cad_get_model_summary` | `project`、`capabilities`、`stats`、`bounds`、`view_state` | L0/L1 | `has_exact_contact_solver=false`、`has_exact_motion_planner=false` 表示后续接触和运动分析均非精确求解 |
| `cad_get_assembly_tree` | `root_id`、`nodes`、`parent_id`、`children`、`bbox`、`face_count` | L1 | 可作为装配层级事实，不代表工艺装配层级 |
| `cad_get_parts` | `parts`、`compactPart` 字段、可选 `contact_preview` | L1，`contact_preview` 为 L3 | 零件名称只能作为弱线索，不能单独作为功能判断 |
| `cad_get_part_faces` | `part`、`faces`、`truncated` | L1 | `truncated=true` 时不应声称已完整检查所有面 |
| `cad_get_face_detail` | `part`、`face`、可选 `contact_candidates` | L1，候选接触为 L3 | 面级几何是事实，局部接触候选是启发式 |

### 接触与可拆卸启发式工具

| 工具 | 主要返回 | 证据类型 | 注意事项 |
|---|---|---|---|
| `cad_get_contact_candidates` | `method`、`contact_candidates`、`confidence`、`face_pairs` | L3 | 方法为 `bbox_normal_area_heuristic`，不是精确接触判定 |
| `cad_get_contact_pairs` | `method`、`contact_pairs`、`relation_type`、`top_face_pairs` | L3 | 建议先用 `compact=true` 获取候选，再对关键 pair 做视觉验证 |
| `cad_find_clearance_directions` | `directions`、排序结果、blocker/clearance 指标 | L3 | 只能说明候选直线方向，不代表完整路径规划 |
| `cad_analyze_removal_directions` | `analyses` | L3 | 用于拆卸优先推理，需结合视觉证据和工艺规则降级/确认 |

### 视觉证据工具

| 工具 | 主要返回 | 证据类型 | 注意事项 |
|---|---|---|---|
| `cad_render_view` | `evidence.image_path`、`view_state` | L2 | 单视角证据，适合概览或已明确状态的截图 |
| `cad_render_section_view` | `section`、`evidence.image_path` | L2 | 用于内部结构，但单剖面不能代表完整空间关系 |
| `cad_render_target_section` | 自动剖切目标面/接触对 | L2/L3 | 自动选择剖面是启发式，图片本身是视觉证据 |
| `cad_render_part_multiview` | 单零件多视角图片与增强 `compactPart` | L1/L2 | 适合零件特征、装夹候选面分析 |
| `cad_render_contact_pair_multiview` | 接触对多视角、红色候选接触面 | L2/L3 | 接触候选是启发式，红色高亮图是可审计视觉证据 |
| `cad_render_move_preview` | 指定方向移动后的截图、`analysis` | L2/L3 | 图像支持方向可视化，`analysis` 仍是启发式 |
| `cad_render_disassembly_exploded_view` | 爆炸图、`plan`、`strategy` | L2/L3 | 可用于整体关系理解，不应直接当作最终拆卸序列 |
| `cad_collect_visual_evidence` | 多视角、剖切 sweep、爆炸证据集合 | L2/L3 | 适合复杂或遮挡关系的稳健取证 |

### 视图状态工具

| 工具 | 主要返回 | 证据类型 | 注意事项 |
|---|---|---|---|
| `cad_set_color_mode` | `success`、`color_mode`、viewer 状态 | 状态控制 | 不是装配证据本身 |
| `cad_reset_view_state` | 重置状态，可选截图 | 状态控制/L2 | 建议在独立视觉调查之间调用 |
| `cad_set_transparency` | 透明度状态，可选截图 | 状态控制/L2 | 若返回图片，可作为视觉证据 |
| `cad_highlight_faces` | 高亮状态 | 状态控制 | 高亮后的截图才是可引用视觉证据 |
| `cad_set_exploded_view` | 爆炸状态，可选截图 | 状态控制/L2/L3 | 爆炸位移通常是启发式布局 |

## Agent 引用要求

每个装配步骤至少包含：

1. **数据证据**：工具名、关键字段、是否为事实或启发式。
2. **视觉证据**：`image_path` 或 `views[].image_path`，以及为什么该图能支持该步骤。
3. **推理结论**：装配动作、装配类型、方向、前置依赖、置信度。
4. **不确定性**：缺少材料、紧固意图、真实公差、装配力、柔性变形、完整运动规划时必须明示。

## 推荐输出中的证据引用格式

```json
{
  "evidence_id": "ev-contact-node-2-node-4-front",
  "source_tool": "cad_render_contact_pair_multiview",
  "evidence_level": "L2_visual_artifact",
  "artifact_path": "project-data/<project_id>/evidence/...",
  "supports": ["constraint:c-node-2-before-node-4"],
  "limitations": ["contact faces are heuristic candidates, not exact CAD contacts"]
}
```

## 严禁混淆

- 不要把 `confidence` 写成事实，只能写成工具启发式评分。
- 不要把接触候选写成确定配合关系，除非有额外证据或人工标注。
- 不要把拆卸方向候选写成完整机器人路径。
- 不要从视觉外观直接断言材料、磁性、弹性、过盈、螺纹标准、扭矩、焊接、胶接。
- 不要在缺少图片路径时把渲染 JSON 当作视觉证据。
