# 文献推荐报告 — KG + Agent 装配序列生成

> 生成日期:2026-06-06 · 面向论文:《面向机械装配的知识图谱先验与多智能体证据闭环装配序列生成方法》
>
> **诚信声明**:分两类——✅ 已在检索中确证存在(给出可核实链接);⚠️ 未确证、需二次核对。不为任何一篇编造 DOI。
> **检索局限**:本次为英文公网检索,**中文核心期刊(机械工程学报 / 计算机集成制造系统等)未覆盖**,需另查 CNKI。

---

## 阅读优先级

**先精读这 3 篇(能把 Related Work 从"待核实"升级为"已坐实"):**
1. Xie et al. 2025(方法对标)
2. AssemMate 2025(装配侧对标)
3. Xiao et al. 2023(综述金矿,其参考文献是扩充 Related Work 的矿脉)

---

## 第一梯队:必读必引(✅ 已确证,与本文方法最接近)

### 1. Xie et al. (2025) — 最强方法对标
- **标题**:Rapid generation method of process routes based on multi-agent collaboration with LLMs
- **来源**:*Advanced Engineering Informatics*,ScienceDirect `S1474034625006263` ✅
- **关键词**(已确证):Multi-agent / Generative AI / Knowledge graph / Smart manufacturing
- **关联**:与本文几乎同构(多智能体 + KG + 降幻觉),但对象=机加工艺路线(非装配序列)、无逐步证据溯源。**本文创新性三点差异(对象/输出/机制)全靠与它对比立起来。**
- **读它干什么**:看它如何论证"多智能体降幻觉",借鉴其实验设计;明确划清你与它的边界。

### 2. AssemMate (2025) — 最接近的装配侧对标
- **标题**:AssemMate: Graph-Based LLM for Robotic Assembly Assistance
- **来源**:**arXiv:2509.11617** ✅(标题、摘要已确证)
- **核心**:从装配文档+3D模型构建装配KG,图编码喂LLM做装配问答/任务规划;摘要强调需注入领域知识引导装配。
- **关联**:实证"图结构注入优于纯文档"——这是本文"为什么不用纯GraphRAG"的实锤引证。它做问答/任务规划,本文做序列生成+成套工艺语义+溯源,差异清晰。

### 3. Xiao et al. (2023) — KG用于工艺规划的奠基综述
- **标题**:Knowledge graph-based manufacturing process planning: A state-of-the-art review
- **来源**:*Journal of Manufacturing Systems*, Vol.70, pp.417-435,`S0278612523001577` ✅
- **核心**:综述PKG构建技术路线;专设"装配工艺规划"节与"PKG+LLM结合"节;明确批评传统CAPP"人工干预多、依赖个人经验、难得全局最优"。
- **关联**:本文论断B(经验=预制模型)的正面引证 + KG承载真实经验的综述支撑。**通读全文,其参考文献是扩充 Related Work 的金矿。**

---

## 第二梯队:方法范式支撑(✅ 已确证)

### 4. Shu, Kim & Park (2024) — S2A,学习类ASP代表
- **标题**:Subassembly to Assembly (S2A): Effective Assembly Sequence Planning through Graph-based Reinforcement Learning
- **来源**:**arXiv:2409.13620** ✅(KAUST,作者/摘要已确证)
- **关联**:"学习类方法输出止于顺序、奖励是经验模拟"的代表;可作相关工作对照对象。

### 5. PKG资源复用 (2022) — 装配领域KG应用
- **标题**:Knowledge graph-based assembly resource knowledge reuse towards complex product assembly process
- **来源**:*Sustainability*, 2022(在 Xiao 2023 参考文献中被引 ✅)
- **关联**:KG用于装配资源/经验复用的具体案例,§2.3 支撑。
- ⚠️ 需核对卷期(MDPI直链被拦,但被权威综述引用,存在性可信)。

---

## 第三梯队:理论前提支撑(几何语义不完备性,✅ 概念确证)

### 6. PMI / 语义PMI — 支撑"几何信息不完备性"论断
- **概念源**(已确证):ISO 10303 STEP + PMI 标准;语义PMI定义(PTC / Capvidia / Onshape 行业源)✅
- **学术源**:Bonino et al. *Semantic enrichment approach for low-level CAD models*, *Computers in Industry*, `S0166361521001822` ✅
- **关联**:全文理论支点("工艺意图丢失在几何之外")的支撑。建议:1个PMI概念源(ISO标准或Wikipedia PMI条目) + 1篇Bonino学术文献。

---

## ⚠️ 需二次核实的文献(本次检索未确证,核对后再引用)

| 文献 | 声称出处 | 核对方式 |
|---|---|---|
| HP-KG | NeurIPS 2025 | NeurIPS 2025 proceedings |
| KARMA | arXiv:2502.06472 | arXiv 核对 id |
| Neural Assembler | AAAI 2025 | AAAI 2025 录用列表 |
| Petruzzellis et al. | ICML 2025 | ICML 2025 proceedings |
| GraphRAG (Edge et al.) | arXiv:2404.16130, Microsoft | arXiv 核对(高可信) |
| Wilson & Latombe | Artificial Intelligence 71(2), 1994 | DOI:10.1016/0004-3702(94)90048-5(经典,高可信) |

---

## 待补缺口

1. **中文核心期刊**:CNKI 检索「装配序列规划 知识图谱」「装配工艺 大模型」「智能装配 智能体」——本次英文检索未覆盖。
2. **装配by拆卸经典综述**:如 Bahubalendruni 等的 ASP review,可作背景必引。
3. **本体用于装配规划**:Demoly / Lohse 等早期工作。
4. **焊接/涂胶等具体工艺意图识别**的专门文献,加固论断C。