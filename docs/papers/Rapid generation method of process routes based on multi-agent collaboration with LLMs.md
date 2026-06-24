Full length article 

# Rapid generation method of process routes based on multi-agent collaboration with LLMs☆

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/7c4f212c33d8ebc35a997405f4d74dc2e5886eeeded485ad6384b20aeabff87f.jpg)


Yanling Xie a , Jihong Liu a , Ruiwen Wang b , Zuoxu Wang a,* , Kai Yu a , Ziming Song 

a School of Mechanical Engineering and Automation, Beihang University, Beijing 100191, China 

b School of Public Order, People’s Public Security University of China, Beijing 100038, China 

## A R T I C L E I N F O

Keywords: 

Manufacturing process design 

Multi-agent 

Generative AI 

Knowledge graph 

Smart manufacturing 

## A B S T R A C T

In the process of process design for manufacturing, issues such as high reliance on personal experience and knowledge, along with long design cycles, are common. This paper proposes a rapid method for generating machining process routes based on Large Language Models (LLMs) and multi-agent collaboration. The complex task of generating process routes is broken down into four subtasks: machining feature recognition, machining feature sorting, machining feature process chain and resource selection, and process route merging and optimization. Each subtask is assigned to an agent fine-tuned with LLMs, equipped with different specialized tools such as STP file parsing and process knowledge base querying, to endow each agent with distinct expertise. The agents collaborate by exchanging information to achieve the rapid, automated generation of machining process routes, offering heuristic ideas for process designers. The TOPSIS evaluation method integrating quantitative and qualitative indicators based on actual production data and expert scores is used to compare the final generated processing route with typical ones, showing that it achieves a higher closeness degree. This demonstrates the advantages of multi-agent collaboration in complex tasks, providing a new solution for the automation and intelligence of process design in intelligent manufacturing systems. 

## 1. Introduction

Intelligent manufacturing integrates advanced manufacturing tech nologies and information technologies with the goal of improving product quality, increasing production efficiency, and reducing production costs. It spans across all stages of the entire lifecycle, including design, production, and service [1]. As a bridge between design and manufacturing, process design still heavily relies on human–machine interaction [2–4], fundamentally depending on human intelligence rather than machine intelligence. It is highly dependent on individual knowledge and long-accumulated project experience, which is both time-consuming and labor-intensive, leading to prolonged process preparation times and rising labor costs [5]. 

With the rapid development of large language models (LLMs), they have achieved remarkable results in various generative design tasks. These models not only demonstrate powerful capabilities in traditional fields such as text generation, language translation, and sentiment analysis, but also show tremendous potential in cross-domain applications, especially in the field of industrial intelligent manufacturing, where the empowerment of LLMs is bringing about a new revolution. Although LLMs, through techniques such as pre-training and finetuning, can correctly understand and generate contextually relevant high-quality text, and even simulate human reasoning and decisionmaking processes to some extent, their inherent limitations pose challenges [6]. When handling complex, dynamic, and highly specialized industrial scenarios, LLMs are prone to generating what is known as “hallucinations”—information that seems plausible but is actually incorrect or imprecise. Due to these limitations, applying LLMs to domain-specific tasks still faces many challenges, such as ensuring the reliability and accuracy of generated content, integrating domain knowledge graphs for enhanced reasoning, and avoiding misjudgments or biases in domain-specific applications. While LLMs hold great promise in industrial fields, fully unlocking their potential requires overcoming these critical challenges. 

Agent technology refers to the approach where multiple intelligent agents collaborate to complete a task. LLMs have shown remarkable potential in achieving human-level reasoning and planning capabilities. This ability aligns perfectly with human expectations of autonomous agents—entities that can perceive their environment, make decisions, and take actions [7]. Leveraging the reasoning capabilities of LLMs can significantly enhance the effectiveness of agent-assisted reasoning. In industrial complex tasks such as process design, a single LLMs, although possessing powerful language understanding and generation abilities, may fall short due to its single perspective and inherent limitations. Multi-agent technology draws on the concept of problem-solving within human teams, where multiple agents with different capabilities collaborate, discuss, and make decisions. By decomposing complex tasks into multiple component tasks and facilitating information flow, it enables the handling of specialized, complex tasks such as process route design. By leveraging the extensive knowledge of LLM-Agent across different domains, the potential for solving specialized computational tasks can be enhanced [8]. However, emerging research indicates that using LLMs-based multi-agent systems to solve various tasks, such as software development [9], Multi-Robot System [10,11], Social Simulation [12,13], Game Simulation [14,15] may lead to complications. Since the academic research in this field is still in its early stages, it has attracted a diverse range of explorers, extending to artificial intelligence experts, including those from disciplines such as social sciences, psychology, and policy studies. 

To address the challenge of time-consuming and human-dependent process route generation, this paper proposes a rapid process route generation method based on multi-agent collaboration with LLMs. The complex task of process route generation is decomposed into multiple component tasks (Machining feature recognition, machining feature sorting, machining feature process chain and resource selection, and process route merging and optimization), with each task assigned to a different agent. By equipping each agent with specific tools to enable them to specialize in completing their assigned tasks, the method improves the efficiency and quality of each component task, enabling the rapid generation of high-quality and feasible process routes. This provides heuristic design support for process designers, optimizing the process flow and efficiently accomplishing the complex task of process route planning. 

The main contributions of this paper are as follows: 

1. A multi-agent collaboration framework for process route generation based on LLMs is proposed. The innovative introduction of the multiagent collaboration mechanism uses LLMs as the ’brain’ of the agents. Through prompt-based fine-tuning of LLMs and equipping personalized tools to adapt different agents to various sub-tasks, efficient and rapid processing of four sub-tasks—Machining feature recognition, machining feature sorting, machining feature process chain and resource selection, and process route merging and optimization—is achieved. This framework enables the rapid recommendation of process routes for part manufacturing to process designers. 

2. The combination of LLMs and a process knowledge graph is utilized to enhance the accuracy of the content generated by agents in the field of process design and reduce hallucinations. By integrating the process knowledge graph, agents are provided with domain-specific knowledge support, enabling the accurate and efficient generation of sub-task content for process routes. This reduces the hallucination issue commonly encountered in professional tasks with large language models, thereby improving the reliability and accuracy of the generated results. 

3. Using the typical process route of the part as a reference, the TOPSIS analysis method is applied to evaluate the generated machining process route. A comprehensive comparison of the scoring results shows that the machining process route generated by multiple agents has a higher overall score than the typical process route. 

The rest of this paper is organized as follow. Section 2 summarizes the current research status on process design, large language models (LLMs), and LLM-Agent. The proposed rapid generation method of process routes based on multi-agent collaboration with LLMs is elaborated in Section 3. Section 4 demonstrates the practical application effectiveness of the proposed method through a case study involving aerospace precision parts. Finally, Section 5 concludes the paper, summarizing the contributions, limitations, and future research directions. 

## 2. Related work

## 2.1. Process design

As an important component of the advanced manufacturing tech nology system and a critical link in the manufacturing system, Computer Aided Process Planning (CAPP) plays a key role in achieving the integration of Computer Aided Design (CAD) and Computer Aided Manufacturing (CAM) within a computer-integrated manufacturing environment. Among its various challenges, process route decisionmaking is one of the key difficulties of CAPP, playing a crucial role in optimizing production processes, improving efficiency, and reducing costs [16,17]. 

Traditional process design methods primarily rely on expert knowledge and long-accumulated experience, typically involving manual or semi-automated approaches to plan process routes [18]. However, these methods have several limitations. First, the manual operation process is time-consuming and struggles to meet the high demand for rapid response in modern manufacturing. Second, the transfer of expert knowledge is limited, and reliance on individual experience often leads to inconsistent design quality, affecting the standardization and consistency of process design. As manufacturing technologies advance, the complexity of process design also increases. Relying solely on human effort makes it difficult to comprehensively cover all details, which can lead to design flaws and oversights. 

To address issues such as the low degree of automation in process design, researchers have proposed various improvement methods. Learning-based approaches, particularly neural network technologies, have been applied to various tasks, including machining feature recognition, process parameter planning [19], process route planning [5,20], tool condition monitoring [21,22], and intelligent diagnostics [23]. By integrating process planning, process modelling, and machining simulation into commercial software systems, a model of the entire process is established by linking manufacturing features with manufacturing resources, enabling overall planning of machining processes, logistics processes, and production line operations. 

To address issues such as the low degree of knowledge reuse in process design, some scholars have constructed knowledge repositories by mining various modal forms of process data to facilitate knowledge reuse, Using Knowledge-Based Systems to provide solutions for manufacturing problems [24]. For example, CHANG ZY [25] and others proposed a process knowledge reuse method that enhances the subjective initiative of process engineers. Some researchers have considered the representation of knowledge. In addition to incorporating knowledge graphs [26–28] into process knowledge reuse, they have also studied techniques such as the construction, retrieval, and visualization of knowledge graphs. 

By introducing computer technology, the automation level and design quality of process design have been improved. However, existing systems still have certain limitations, particularly when dealing with complex and dynamic manufacturing environments. The traditional CAPP research and development, primarily focused on automation, has led to growing skepticism about the effectiveness of such systems [29]. Researchers are gradually recognizing that high automation is not a requirement for an effective CAPP system, and have begun to emphasize assistance rather than full automation [30]. The survival and development of manufacturing enterprises still largely rely on individuals who possess information and knowledge, creativity, and collaborative skills. Human decision-making, creative inspiration, and innovation abilities remain irreplaceable. In this context, the rapid development of the manufacturing industry urgently demands the introduction of standardized and feasible processes for intelligent, rapid generation of process routes, to assist process designers in more efficiently handling complex design tasks. This not only standardizes the design process and improves design quality, but also provides heuristic support to help designers make more optimized decisions in the face of a complex and ever-changing production environment. 

## 2.2. Large language models

With LLM’s powerful natural language processing and data analysis capabilities, LLMs are becoming an indispensable component of intelligent manufacturing systems and have been applied in various aspects of the field. In design, increasing research focuses on LLMs’s capabilities in executing various engineering design tasks, such as design descriptions, concept selection, material selection, engineering drawing analysis, CAD generation, CFD interpretation, topology optimization, and manufacturability assessment [31,32]. In production and assembly optimization [33,34], LLMs utilize their natural language features to provide operators with a natural language interface, enabling the creation of recommendation execution systems. In quality inspection and prediction [35–37], LLMs have relevant applications in quality forecasting and fault analysis, among others. 

To further enhance the application effectiveness of LLMs in intelligent manufacturing, researchers have proposed various optimization methods. First, Prompt Engineering significantly improves the output quality of models in engineering design tasks by designing efficient prompts to guide LLMs in generating more accurate responses [38–42]. Second, Retrieval-Augmented Generation (RAG) enhances the knowledge coverage and reasoning capabilities of LLMs in specialized fields by integrating external knowledge bases (e.g., knowledge graphs), thereby enabling superior performance in interpreting complex design specifications and optimizing manufacturing processes [43–47]. Finally, Finetuning enables LLMs to better adapt to high-precision and specialized engineering requirements through training on domain-specific data [48–51]. These optimization methods provide crucial support for the deeper integration of LLMs in intelligent manufacturing. 

With the rapid advancement of large language models, the evaluation of model-generated content has become increasingly critical. Traditional evaluation standards and methods are often constrained by human subjectivity. Existing automatic evaluation metrics, such as BLEU and ROUGE, primarily rely on surface-level text matching and fail to capture higher-level human expectations, such as semantic depth [52] and emotional resonance [53]. Recent research on LLM evaluation indicates a notable shift from model-centric assessment towards human-–AI collaborative evaluation paradigms. In the medical domain, the QUEST framework has been proposed, encompassing five dimensions: information quality, reasoning ability, safety risk, trustworthiness, and user perception. This framework systematically reviewed 142 studies involving human factor evaluations and highlighted issues related to reliability and generalizability [54]. Within the human–computer interaction community, Ibrahim et al. extended this direction by proposing a three-phase Human-Interaction Evaluations (HIE) process, which emphasizes assessing overreliance and persuasive risk in realworld tasks to bridge the “socio-technical gap” between offline model testing and practical deployment [55]. Zhou et al [56] further reviewed LLM-enabled agent models and simulations, underscoring the importance of incorporating social feedback, long-term adaptability, and behavioral safety as essential dimensions for evaluating agent-based systems. In parallel, a security-focused survey published in IEEE Transactions on Automation Science and Engineering (IEEE JAS) advocates evaluating the controllability of LLM agents from both attack surfaces and defense mechanisms, offering methodological guidance for the design of system-level risk control indicators [57]. As a result, the evaluation paradigm for LLMs has evolved from conventional offline textual metrics to a comprehensive framework that simultaneously addresses model performance, human-centered interaction experience, and system-level safety. This multidimensional perspective lays a robust methodological foundation for the objective validation of collaborative multi-agent systems in future intelligent applications. 

Although LLMs have made some progress in intelligent manufacturing and their applications across various stages of the product lifecycle are gradually being validated, there are still several challenges to overcome. First, LLMs face limitations in handling deep technical issues in specific professional fields due to insufficient data and knowledge accumulation. This can result in less-than-ideal application outcomes in high-precision and specialized engineering design and production tasks [58]. Second, the application of LLMs in critical manufacturing processes, such as process design and optimization of machining details, remains relatively limited [59]. Their explanatory capabilities and understanding of complex design specifications still require improvement. 

## 2.3. LLM-agent

LLMs-based agents combine the powerful natural language processing capabilities of LLMs with the autonomous decision-making and collaboration abilities of agents. These agents can understand human natural language commands and perform routine tasks [60,61], making it possible to improve task efficiency, reduce user workload, and facilitate access to a broader user base. 

In task-oriented deployment, agents follow high-level instructions from users, undertaking tasks such as goal decomposition [62], sub-goal sequence planning [63,64], and environmental interaction exploration [65,66], until the final objective is achieved. LLMs-based agents have made significant progress in fields such as gaming [67,68]and healthcare [69]. Notably, a critical form of multi-agent collaboration lies in systematically decomposing complex tasks into subtasks that can be processed sequentially or in parallel, and achieving efficient division of labor through dynamic coordination mechanisms [10,70,71]. This collaborative paradigm demonstrates significant advantages in specialized domains or complex tasks (e.g., process design), enhancing the precision and robustness of overall solutions. 

However, the application of LLMs-based agents in process design tasks is still in the exploratory stage, with numerous challenges remaining, such as how to effectively decompose process tasks, integrate knowledge and data analysis technologies, and ensure reliability and stability. 

## 3. Methodology

## 3.1. Overview

In this paper, a rapid generation method for part processing routes based on LLMs and multi-agent collaboration is proposed (see Fig. 1). The machining process route task is refined into four sub-tasks, each assigned to an agent fine-tuned with LLMs, responsible for handling specific sub-tasks: 

1. Feature Extraction Agent (FEA): Parse the input part STP file and multi-view images of the part, which undergo pre-processing steps such as data de-sensitization, encryption, and intellectual property isolation before being processed, to accurately extract machining features and provide a comprehensive description of the part. This process achieves multi-modal information parsing and transfer, enhancing the completeness of the information and the accuracy of feature extraction, thereby providing comprehensive and systematic support for subsequent machining processes. 

2. Macro Process Planning Agent (MPPA): Based on the machining features extracted from the FEA analysis and the overall description of the part, focus on the part’s overall structure, taking into account the division of machining stages and key processes. This ensures the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/3c60f7dee51047d238ad398c2bf11b8b28a3cda58199ea29173748ccb0e1fad3.jpg)



Fig. 1. Framework for rapid process route generation based on multi-agent collaboration with LLMs.


proper sequencing and arrangement of machining features, guaranteeing the feasibility of the machining route for sequential processing of features without process merging or optimization, while maintaining coordination within the production process. 

3. Specific Process Planning Agent (SPPA): Based on the machining feature information extracted from the FEA analysis, the transmitted machining requirements of the part, and the machining sequence of features planned by the MPPA, by accessing the knowledge resources from the process knowledge graph database as external resources to implement Retrieval-Augmented Generation (RAG), this approach performs the selection of typical machining feature process chains and retrieves machining resources for each process in the chain based on the part’s machining precision requirements. This enhances the quality and professionalism of generated content, thereby achieving optimal matching of feature machining solutions and optimized resource allocation. 

4. Process Optimization and Evaluation Agent (POEA): Based on the macro process route information generated by the MPPA and the detailed process route information generated by the SPPA, the ’rough first, fine later’ principle is followed to merge the machining processes. The generated merged process routes are then evaluated, and the process route with the highest optimization score is output to the process design personnel, thereby achieving the recommendation of the part’s machining process route. 

To achieve the objectives of the respective sub-tasks, each Agent is equipped with specialized tools, which are crucial for the realization of their primary functions. Table 1 provides a detailed overview of how each Agent integrates with the design tools, automating the invocation of the Agent’s tools to ensure a seamless transition from input data to design output throughout the entire process. This integration significantly enhances design efficiency, reduces human intervention, and optimizes the design solutions. 


Table 1 Information integration for agent design tools.


<table><tr><td>Agent</td><td>Tool</td><td>Data interface</td><td>Input format</td><td>Output format</td></tr><tr><td rowspan="3">FEA</td><td>STP File Analysis Tool</td><td>Function Interface</td><td>STP Standard Format File</td><td>Face/Vertex Feature Text Information</td></tr><tr><td>JPG Image Analysis Tool</td><td>GLM-4 V API Interface</td><td>JPG/PNG Part 3D Image Files</td><td>Image Text Information</td></tr><tr><td>General Tool</td><td>GPT-4o API Interface</td><td>Natural Language</td><td>Natural Language</td></tr><tr><td>MPPA</td><td>General Tool</td><td>GPT-4o API Interface</td><td>Natural Language</td><td>Natural Language</td></tr><tr><td rowspan="2">SPPA</td><td>General Tool Process Knowledge Graph Query Tool</td><td>Neo4j API Interface</td><td>Process Query</td><td>Relevant Process Triplets</td></tr><tr><td>General Tool</td><td>GPT-4o API Interface</td><td>Natural Language</td><td>Natural Language</td></tr><tr><td rowspan="2">POEA</td><td>Decision Evaluation and Analysis Tool</td><td>Function Interface</td><td>Machine Tool Switches and Tool Switches</td><td>Comprehensive Efficiency Score</td></tr><tr><td>General Tool</td><td>GPT-4o API Interface</td><td>Natural Language</td><td>Natural Language</td></tr></table>

## 3.2. Agent construction process

## 3.2.1. Agent definition based on Langchain framework

Agents constructed based on the Langchain framework [72] (see Fig. 2) are designed to perform specific tasks. The operational flow begins when a requirement is captured (Step 1), and the controller code calls the Agent module interface via the Langchain API. Internally, the system interacts with the LLMs (Step 2), which either directly generates an answer by understanding the problem or, depending on the task, dynamically selects appropriate tools to break down the task and execute it (Step 3). Agents defined within the Langchain framework are capable of self-reflection and iterative improvement through promptbased interactions and multi-turn conversations. This process allows the Agent to continuously refine and optimize its responses or actions, thereby enhancing the overall quality of its output. The four Agents in this study, each responsible for executing specific tasks, are all constructed based on this approach. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/d592ba0e50b93c7e5a5fc38f8ce92fa907749d590212a85847f1a6375e23fe32.jpg)



Fig. 2. Task execution process of agents defined based on the langchain framework.


## 3.2.2. Three-stage prompt tuning for professional task agents

Prompt tuning aims to guide the LLMs to generate more accurate and contextually relevant responses for specific tasks by adjusting the input prompts. Through task requirement analysis, example-based guidance, and other methods, prompt tuning helps the model quickly adapt to specific domains or tasks, enabling the LLMs to better recognize and apply domain knowledge in complex tasks, thereby achieving more precise generation outcomes. 

By introducing LLMs (GPT-4) as the brain of the Agent, the performance of the Agent in specific tasks is enhanced through three-Stage prompt-based fine-tuning. The three-stage prompt design method achieves task-driven execution and logical guidance through a structured framework. Firstly, at the role positioning level, specific professional identities such as professional engineers or senior process planners are assigned according to task requirements, clarifying the knowledge system and capability boundaries of task-executing subjects to define the executor’s expertise, thereby restricting the model to generate content strictly within the designated professional domain and, at the source, reducing knowledge drift and hallucinations that arise from ambiguous role definition.. Secondly, in the task basis and input information module, multi-source data and tool resources are systematically integrated to specify the key elements covered by input data and clearly define the required tools and their functions, ensuring a complete data and tool foundation for task execution, thereby providing the model with robust contextual support, preventing hallucinations caused by missing information, and effectively constraining the generated content from deviating from factual evidence. Finally, in the specific task requirements stage, a progressive logical approach is used to construct the task system and clarify the task output format; through task summarization and example descriptions, the consistency in output format and logical rigor of the Agent are ensured, while preventing the model from exhibiting logical breaks and content divergence during complex reasoning, thereby further mitigating hallucinations. The three-stage prompt design forms a closed-loop task execution guidance system through logical stratification and task progression, thereby enhancing the method’s operability and execution effectiveness. 

Based on the design of the three-Stage prompt framework and incorporating various prompt engineering techniques, four agents constructed with differentiated prompts for different processing links in manufacturing process route generation tasks collaborate to ultimately achieve the efficient completion of manufacturing process route generation tasks. 

In this paper, the complete prompts used for the four Agents incorporate several key prompt engineering techniques: Example-Guided Prompting involves providing a series of examples within the prompt to guide the model in generating similar outputs, showcasing the desired output format and reducing generation errors. Contextual Prompting, on the other hand, supplies the background or context of the task, allowing the model to incorporate this information when generating content, thus responding more accurately to user needs. For instance, specifying the task’s scenario or objectives within the prompt makes the generated content more targeted. Instructional Prompting designs the prompt as clear instructions or questions, directly guiding the model to produce the required content. Lastly, Chain-of-Thought Prompting encourages the model to express a step-by-step reasoning process in the prompt, making the generated results more logical and showing the reasoning steps, which is particularly useful for tasks that require multi-step calculations or reasoning. 

During the prompt fine-tuning process for the Agent, prompt engineering techniques are employed to achieve efficient adjustment of each Agent in the manufacturing process route generation task. The finetuned prompts ultimately guide the Agent to focus its attention on key points of the task, enabling it to maintain high-quality output in multiturn dialogues and complex tasks. Additionally, the Agent becomes more capable of understanding and utilizing domain-specific terminology, enhancing the professionalism and consistency of the content within the specific field. This task-specific fine-tuning helps optimize the system’s computational resource utilization, reducing the time and resource consumption spent processing irrelevant information. 

## 3.2.3. Expert review and validation mechanism for multi-agent process outputs

To comprehensively evaluate the effectiveness and reliability of the proposed multi-agent collaborative process planning approach, an expert review mechanism was established for the core outputs of each agent. This mechanism refines the evaluation dimensions and key assessment criteria for the outputs of individual agents at critical stages, including part feature extraction, process planning, process chain selection and resource allocation, and process route optimization. The aim is to ensure a high degree of accuracy, rationality, and engineering applicability in real-world implementations of the multi-agent system. By organizing independent reviews by domain experts, potential shortcomings within the system can be promptly identified and addressed, thereby enhancing the scientific rigor and practical value of the overall solution. The specific evaluation criteria for each agent are detailed in the following Table 2. 

## 3.3. Feature extraction agent

The FEA implements the sub-task of processing feature recognition, which is the first step in the manufacturing process route generation task. It directly handles the raw file information, extracts the machining features of the part, and generates an overall description of the part in conjunction with the view information. This serves as the foundation for subsequent tasks, and the accuracy of its information processing has a significant impact on the precision of the tasks that follow. The task can be described as shown in Eq. (1): 


Table 2 Expert review evaluation elements table.


<table><tr><td>Agent</td><td>Expert review criteria</td></tr><tr><td>FEA</td><td>1. Accuracy and completeness of feature extraction2. Rationality and consistency of multimodal information analysis3. Standardization and readability of the overall part description4.Comprehensiveness and effectiveness of information provided for downstream process planning</td></tr><tr><td>MPPA</td><td>1. Rationality of process route stage division2. Scientific sequencing of machining features3. Feasibility and production coordination of the proposed solution4. Effective utilization of input information5. Standardization and completeness of output description</td></tr><tr><td>SPPA</td><td>1. Rationality and pertinence of process chain selection2. Optimization of machining resource allocation3. Accuracy and timeliness of process knowledge graph retrieval4. Consistency of interface with upstream and downstream information5. Practicality and safety of the proposed solution</td></tr><tr><td>POEA</td><td>1. Logical soundness of process route merging and adherence to the “rough-to-fine” principle2. Scientific basis and transparency of evaluation indicators and scoring methods3. Degree of achievement of optimization objectives (e.g., efficiency, cost, reduction of steps, etc.)4. Feasibility, innovativeness, and inspiration of the recommended solution</td></tr></table>

$$
\operatorname{FEA}: (S, I) \rightarrow (F, D) \tag {1}
$$

where S denotes the set of 3D geometric information from the STP file, I denotes the set of 3D geometric information from the JPG image, F denotes the set of machining features, and D denotes the overall description of the part. 

FEA receives the initial part STP file and part view file provided by the user and processes them. First, based on the feature extraction identity set by the Agent, the overall goal of machining feature extraction is decomposed into sub-tasks, including STP file analysis, view file analysis, and part machining feature summary description. These subtasks are automatically assigned to the STP File Analysis Tool, JPG Image Analysis Tool, and General Tool. After the STP File Analysis Tool and JPG Image Analysis Tool complete their tasks, the results are unified and passed to the General Tool for summarize and output. Ultimately, FEA produces two outputs: the machining feature set and the overall part description. 

(1) STP File Analysis Tool: Parse and extract 3D model data from the STP file, supporting the automatic processing of complex model data and the extraction of machining features. 

The tool, based on a deep learning graph neural network model, can simultaneously perform tasks such as semantic segmentation, instance segmentation, and bottom-face segmentation to identify machining features, the faces associated with these features, and their bottom faces, it outputs information about points, faces, and normal vectors. 

(2) JPG Image Analysis Tool: Extract and analyse image information from JPG format images to support the recognition and understanding of model structures, enhancing the system’s ability to process visual modality data. 

The tool is based on the advanced multi-modal large-scale language model GLM-4 V, which transcends the limitations of single-modal models, enabling the conversion of image information into textual descriptions and helping to extract structural layout information of parts from image modality data. 

(3) General Tool: Address and answer questions based on the capabilities of the LLMs itself. 

The tool, based on LLMs (GPT-4o), addresses problems in the extraction of machining process features that cannot be resolved by the other two tools, enabling seamless integration and unified output of information. 

## 3.4. Macro process planning agent

MPPA (as shown in the figure) completes the macro process route task planning, i.e., the sorting of machining features, which is the second step of the overall task. Existing machining feature process planning methods mainly focus on the information of individual machining features, lacking a comprehensive consideration of the overall part information [73]. This deficiency leads to a reduced effectiveness of the process design results and limited direct applicability. Therefore, this step plays a pivotal role in bridging the previous and subsequent stages, as it receives the parsed information of the part output from the FEA and the macro process route output directly impacts the rationality of the final process route generation. It takes the parsed information from FEA as input, and the output of the macro process route is crucial to the rationality of the final process route generation. The task can be described as shown in $\operatorname { E q . }$ (2): 

$$
M P P A: (F, D) \rightarrow R \tag {2}
$$

where F represents the machining feature information, D represents the part description $\mathbf { \mathbf { \mathbf { \mathbf { R } } } } = \{ \mathbf { \mathbf { r } } _ { 1 } , \mathbf { r } _ { 2 } , . . . , \mathbf { r } _ { \mathbf { \mathbf { k } } } \} , \mathbf { \mathbf { r } _ { i } }$ represents the i-th machining feature. 

MPPA receives the machining feature information and overall feature structure description generated by FEA. Adopting the role of a high-level process planner, it analyses the part from a professional perspective, considering the types and descriptions of machining features. The task is decomposed into three parts: modality information integration, overall part morphology analysis, and macro process route generation. By leveraging the powerful comprehension capabilities of LLMs in the General Tool, the final summary output is produced. Based on factors such as processing cost and ease of machining, the machining feature processing sequence constraints are comprehensively assessed to determine the order of machining features. 

## 3.5. Specific process planning agent

SPPA completes the selection of machining feature process chains and the processing resources for each operation within the process chain. It plays a central supporting role in the entire process route generation task. Through the precise matching of knowledge resources, it ensures that the processing requirements of each operation are met, laying a solid foundation for the realization of high-quality, continuous process flows. The task can be described as shown in Eq. (3): 

$$
\mathrm{SPPA}: (\mathrm{F}, \mathrm{R} _ {\mathrm{M}}, \mathrm{RE}) \rightarrow R _ {S} \tag {3}
$$

where F represents the machining feature information, ${ \sf R } _ { \sf M } = \{ { \bf r } _ { 1 } , { \bf r } _ { 2 } , . . . ,$ $\mathbf { r } _ { \mathrm { k } } \}$ represents the macro process route planning content, including the sequence of machining features, RE represents the part machining requirements, and $\mathtt { R } _ { \mathtt { S } }$ represents the detailed process route planning content. 

SPPA receives the machining feature information generated by FEA, the macro machining feature sequence information generated by MPPA, and part machining requirements such as machining precision. It first decomposes the machining feature sequencing information, then combines the part’s machining requirements and the detailed information of each machining feature to generate Neo4j query statements for the knowledge graph. Using the Process Knowledge Graph Query Tool, it queries the knowledge base to match the machining features with their typical process chains and machining resources. Finally, based on the macro machining feature sequence information and the retrieved knowledge, it summarizes the output. This process supplements detailed process chains and resource information based on the macro process route content, resulting in a feasible part machining process route, see Fig. 3. 

Two tools equipped with SPPA and their technical principles are as follows: 

(1) Process Knowledge Graph Query Tool: Retrieving process knowledge from the knowledge graph, extracting relevant process information to provide data support and knowledge assistance for the system, thereby enhancing the intelligent processing capability of the manufacturing process. 

This tool primarily performs knowledge retrieval tasks. It contains an embedded knowledge graph database of typical feature processing chains and associated processing resources. 

The directed graph representation of the process knowledge graph (PKG) for typical features is as shown in Eq. (4): 

$$
\mathrm{PKG} = (\mathrm{V}, \mathrm{E}) \tag {4}
$$

where V represents the set of process feature nodes, and E represents the relationships between the nodes. 

$$
\mathrm{V} = \text { MainProcessFeature } \cup \text { ProcessChain } \cup \text { ProcessX } \cup \text { Machine }
$$

∪ Cutter 

where MainProcessFeature represents the set of process feature nodes, ProcessChain represents the set of process chain nodes, ProcessX represents the set of operation nodes, Machine represents the set of machine tool nodes, and Cutter represents the set of tool nodes. 

The attribute set of ProcessChain can be described as: 

$$
\text { Attr(PC) } = \{\text { Ra,   Dimensional\_accuracy,   Materials,   Describe } \}
$$

where Ra represents the surface roughness range, Dimensional accuracy represents the dimensional accuracy range, Materials represents the applicable materials, and Describe represents the application scenarios of the process chain. 

$$
\mathrm{E} = \left\{\left(\mathrm{v} _ {\mathrm{i}}, \mathrm{v} _ {\mathrm{j}}\right) \mid \mathrm{v} _ {\mathrm{i}}, \mathrm{v} _ {\mathrm{j}} \in \mathrm{V} \text {   and   there   exists   a   specific   relationship } \right\}
$$

where $\mathbf { v _ { i } }$ and $\mathbf { v } _ { \mathrm { j } }$ represent two distinct nodes. 

The final constructed Process Knowledge Graph ontology model is shown in the Fig. 4. 

(2) General Tool: Address and answer questions based on the capabilities of the LLMs itself. 

This tool, based on LLMs (GPT-4o), performs tasks beyond knowledge querying, achieving information integration and unified output. 

## 3.6. Process optimization and evaluation agent

POEA completes the final step of the machining process route generation task: process route optimization and evaluation. By optimizing and evaluating the feasible process route plans based on the sequence of machining features generated by SPPA, a machining process route that is both economical and reasonable, and meets the part’s machining requirements, is ultimately generated. This provides heuristic inspiration for professional process designers. The task can be described as shown in Eq. (5): 

$$
\mathrm{POEA}: \left(\mathrm{R} _ {\mathrm{M}}, \mathrm{R} _ {\mathrm{S}}\right)\rightarrow R ^ {*} \tag {5}
$$

where $\mathrm { R } _ { \mathrm { M } }$ represents the macro-level machining process route planning content, which includes the sequence of machining features; $\mathtt { R } _ { \mathtt { S } }$ represents the detailed machining process route planning content, including process chains and machining resources; and $R ^ { * }$ represents the final output machining process route. 

POEA receives the macro-level process route generated by MPPA and the detailed process route generated by SPPA. With the identity of a senior process planner, POEA analyses the constraints on the machining feature sequence based on the macro-level process route and analyses the machining accuracy and resources for each process based on the detailed process route. By considering the ’rough-first, fine-later’ principle, POEA utilizes the General Tool to generate optimized process route solutions by merging process steps. The Decision Evaluation and Analysis Tool is then employed to evaluate the process route based on a mathematical function that analyses the frequency of machining resource switching, considering economic factors. The best process route is selected, and General Tool is used to supplement and refine the process steps before outputting the final optimized process route plan. 

The two tools equipped with POEA and their technical principles are as follows: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/329a1d2f0a9c984d7a1534866ea01983049af3235957467bb84f6b4aa7ca596e.jpg)



Fig. 3. Knowledge graph-Based detailed process content generation mechanism for SPPA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/90d45579a56ded771a848fc088da13bd6837133b7abf45e7557f295aee86f54f.jpg)



Fig. 4. Ontology model of the process knowledge graph for PKG.


(1) Decision Evaluation and Analysis Tool: Evaluate and score a single process route plan based on economic considerations. 

The tool incorporates a simplified mathematical model for the evaluation of process route schemes. By assigning appropriate weights to the time delays and economic costs associated with machine changes and tool changes, an efficiency evaluation model driven by key variables is established. This enables the quantitative characterization and comparison of process route schemes in terms of execution efficiency, thereby providing data-driven support and a robust modelling foundation for multi-scheme screening and optimization. 

Let a denote the number of machine changes and b denote the number of tool changes during the machining process. Each type of change introduces varying degrees of production delay and economic expenditure. To objectively reflect their relative impacts on overall efficiency, a weighted linear model is introduced as shown in Eq. (6): 

$$
\mathrm{Y} = \mathrm{Y} _ {0} - \alpha \mathrm{a} - \beta \mathrm{b} \tag {6}
$$

Here, Y represents the overall efficiency score of the process route, where a higher value indicates greater efficiency; ${ \mathrm { Y } } _ { 0 }$ is the baseline score, reflecting the ideal efficiency in the absence of machine and tool changes; α and β are the weighting parameters for machine changes and tool changes, respectively; a and b denote the number of machine changes and tool changes, respectively. 

To ensure the objectivity of the weighting parameters, α and β are determined by constructing a linear combination model based on the average time consumption and average cost of switching operations derived from historical production data, as shown in the Eqs. (7) and (8). 

$$
\alpha = \omega_ {1} t _ {\mathrm{a}} + \omega_ {2} C _ {\mathrm{a}} \tag {7}
$$

$$
\beta = \omega_ {1} t _ {b} + \omega_ {2} C _ {b} \tag {8}
$$

here, $\mathbf { t _ { a } }$ and $\mathbf { t _ { \mathrm { b } } }$ represent the average time required for each unit switch; $\mathrm { C _ { a } }$ and $\mathrm { C _ { b } }$ denote the average economic cost per unit switch; ${ \bf { \omega } } _ { \bf { { u } } }$ and ω2 are the weighting coefficients for time and cost, respectively, and can be set according to specific preferences. 

Based on actual data from a manufacturing enterprise, let $\mathbf { t _ { a = 1 0 , t _ { b = 3 } } }$ $\mathrm { C _ { a } } = 6 , \mathrm { C _ { b } } = 4 , \mathrm { \ : \omega _ { 0 1 } } = 7 , \mathrm { \omega _ { 0 2 } } = 3 ;$ thus, the parameters are determined as shown in the Eq. (9): 

$$
\frac {\alpha}{\beta} = \frac {8}{3} \tag {9}
$$

Let $\mathrm { Y } _ { 0 } = 1 0 0$ serve as the baseline score. The final mathematical model for the overall efficiency score is thus expressed as shown in the Eq. (10): 

$$
\mathrm{Y} = 1 0 0 - 8 \mathrm{a} - 3 \mathrm{b} \tag {10}
$$

The selection of weighting parameters is guided by empirical analysis and experimental validation based on actual production scenarios, thereby reflecting the relative impact of each factor on production efficiency. The weighting parameters can be flexibly adjusted according to specific circumstances to accommodate the requirements of different process routes. The use of a simple linear mathematical function offers the advantages of computational simplicity, efficiency, intuitiveness, and ease of interpretation and dissemination. By employing a weighted sum of a limited number of key variables, this approach enables rapid evaluation of process route schemes, significantly reducing complexity and computational cost. It is particularly well suited for applications where data are limited or rapid decision-making is required. 

(2) General Tool: Address and answer questions based on the capabilities of the LLMs itself. 

In POEA, the General Tool primarily utilizes the powerful reasoning and decision-making capabilities of LLMs (GPT-4o) to analyze the incoming process route content. It performs tasks such as merging process routes based on the ’rough first, fine later’ principle, optimizing the process route by adding auxiliary operations, and integrating and unifying the output of information. 

## 4. Case study

This section presents a component from an aerospace device as a case study to illustrate the proposed process planning workflow; the generated route is benchmarked against the component’s conventional route through qualitative and quantitative TOPSIS analysis, demonstrating the method’s effectiveness and practicality and underscoring its strong potential for engineering application and broader adoption. 

## 4.1. Part process analysis

A component in an aerospace precision device (as shown in the Fig. 5a) is used in a medium-precision assembly system to ensure the stability of other parts. Based on the 3D model analysis, the machining feature locations of the part (as shown in the Fig. 5b, c and d) include a rectangular channel for sliding fit during assembly, a rectangular groove for fixing, a through hole as a positioning reference, and a flat surface that ensures tight integration with other components. The part is designed for mass production with low cost and uses chromiummolybdenum alloy steel (15CrMo) as the blank material. The machining process aims to meet the roughness requirement of Ra = 0.8–1.6 μm and tolerance grade IT7–IT8. The accuracy and dimensional requirements of the part are directly related to the smoothness of the assembly and long-term stability. A reasonable machining process route is critical to the overall system’s reliability. 

Based on the company’s machining experience and the standards from the mechanical processing technology manuals, a typical machining process route for square-shaped parts is obtained, as shown in the Table 3 below: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/2d29566e0565e47f73854963248940287e2a43d2d134f67db0cf5f525ad6b25e.jpg)



（a）3DModelofthe Part


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/405077e14c124f177a0d16fc98e2ff3bbe95705237669d5fa5eeaa8f733a828d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/4d5e2543bef85927598260943b89999edf5dfb661cd7728eeba3ea382f9a9707.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/66e9d574156e70e26633632e22279dc4b2ee4faed2ac1a21aaf632b4f9619fd0.jpg)



(d）rectangular_pocket


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/0a1c8e19a47a94f29680071feacff2a0ca279d98229dc2d1a09bc2bea80e4472.jpg)



（b）through_hole


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/cff1deb5d316ebe7feb57628483df652c49f85c112a57b77d492f22faeacf86e.jpg)



(c）rectangular_through_slot



Fig. 5. A part in a certain aerospace precision device.


## 4.2. Construction of the process knowledge graph

Based on the experience of process engineers and the knowledge from machining process handbooks, this study summarizes the commonly used process chains for machining features of parts in precision aerospace equipment (for example, taking typical machining features such as holes as a case, as shown in Table 4). The goal is to establish a knowledge storage system for these process chains to support the knowledge query capability of SPPA. 

Different manufacturing companies and tool manufacturers classify tools in various ways. By integrating the existing machining resources and manufacturing experience of a specific machining enterprise, this study aims to allocate resources for each process in the hole machining process chain, and establish a knowledge storage system for machining resources (see Table 5). 

Based on the existing machining resources of a specific enterprise and knowledge from the Machining Process Handbook, with the Machining Process Handbook serving as the general knowledge baseline, a knowledge graph comprising tens of thousands of nodes has been constructed. This graph covers 82 % of the core entities and 79 % of the key relationships outlined in the handbook. Additionally, leveraging the enterprise’s existing machining resources and historical data, proprietary knowledge nodes have been specifically supplemented, further expanding the graph to include knowledge related to machining features identified through FEA analysis. The complete process knowledge graph, as shown in ${ \mathrm { F i g . ~ } } 6 ,$ ultimately encompasses machining process chains for typical machining features, along with the machining resources for each process step. 


Table 3 Typical processing route for square parts.


<table><tr><td>Operation</td><td>Operation Name</td><td>Processing Resources</td></tr><tr><td>1</td><td>Cutting</td><td></td></tr><tr><td>2</td><td>Blank Manufacturing</td><td>Forging</td></tr><tr><td>3</td><td>Heat Treatment</td><td>Quenching Furnace</td></tr><tr><td>4</td><td>Finishing Reference Surface</td><td>Precision Milling Machine</td></tr><tr><td>5</td><td>Through Hole Processing</td><td>Drilling Machine, Boring Machine, Reamer</td></tr><tr><td>6</td><td>Rectangular Channel Processing</td><td>CNC Milling Machine</td></tr><tr><td>7</td><td>Rectangular Groove Processing</td><td>CNC Milling Machine</td></tr><tr><td>8</td><td>Flat Surface Finishing</td><td>Precision Milling Machine</td></tr><tr><td>9</td><td>Deburring and Surface Treatment</td><td>Manual Deburring, Oil Coating Equipment</td></tr><tr><td>10</td><td>Packaging and Storage</td><td></td></tr></table>


Table 4 Hole feature processing chain.


<table><tr><td>Serial Number</td><td>Process Chain</td><td>Dimensional Accuracy</td><td>Surface Roughness</td><td>Applicable Range</td></tr><tr><td>1</td><td>drilling</td><td>IT11-IT12</td><td>6.3–25</td><td rowspan="4">Machining of small cylindrical holes and tapered holes in ferrous and non-ferrous metals</td></tr><tr><td>2</td><td>drilling –reaming</td><td>IT9-IT10</td><td>6.3–12.5</td></tr><tr><td>3</td><td>drilling –reaming –honing</td><td>IT8-IT9</td><td>3.2–6.3</td></tr><tr><td>4</td><td>drilling –reaming –rough honing –finish honing</td><td>IT7-IT8</td><td>0.8–3.2</td></tr><tr><td>5</td><td>drilling (reaming) –rough honing –finish honing –lapping</td><td>IT6-IT7</td><td>0.2–0.8</td><td>Machining of small cylindrical holes in ferrous metals</td></tr><tr><td>6</td><td>drilling (reaming) –fine boring</td><td>IT7-IT8</td><td>0.8–3.2</td><td>Small cylindrical holes in ferrous or non-ferrous metals</td></tr><tr><td>......</td><td>......</td><td>......</td><td>......</td><td>......</td></tr><tr><td>......</td><td>rough boring –semi-finishboring – finishboring –carbide boring</td><td>IT6-IT7</td><td>0.2–0.8</td><td>Large cylindrical holes in non-ferrous metals</td></tr></table>

To further validate the accuracy of the knowledge graph, domain experts were invited to review the graph. The focus of the evaluation was on the rationality of the process chains and the accuracy of the entity relationships. The expert evaluation results revealed that 86 % of the entity definitions and 80 % of the relationship logic received ratings of 4 or higher (on a scale of 5). The Kendall’s coefficient of concordance $( \mathsf { W } = 0 . 7 8 , \mathsf { p } < 0 . 0 1 )$ indicates a high degree of agreement among the experts, thereby demonstrating that the quality of the knowledge graph construction is relatively high. 

## 4.3. Part machining process route generation

The machining requirements of the aerospace precision equipment part, along with the part’s STP file and multi-view image file (see Fig. 7), are transmitted into the multi-agent collaborative framework for rapid machining process route generation. Through the multi-agent collabo ration method based on LLMs, and the information exchange between Agents, a feasible and reasonable machining process route for the part is quickly generated. 


Table 5 Resource allocation for each process in the feature hole processing chain.


<table><tr><td>Serial Number</td><td>1</td><td>Machining Resources</td><td>2</td><td>Machining Resources</td><td>3</td><td>...</td></tr><tr><td>1</td><td>drilling</td><td>Twist Drill: Sandvik R840-5 | Vertical Drilling Machine: Z3040</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>drilling</td><td>Twist Drill: Kyocera KSD35 Radial Drilling Machine: Z3041</td><td>Reaming</td><td>Reamer: Mitsubishi MWE080 Vertical Drilling Machine: Z5140</td><td></td><td></td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>...</td><td>Rough Boring</td><td>Carbide Rough Boring Tool: Sandvik CoroBore BR20 Boring Machine: TPX6111B</td><td>Semi- finish Boring</td><td>High-speed Steel Semi- finish Boring Tool: Mitsubishi BORING Boring Machine: TPX6117B</td><td>Finish Boring</td><td>...</td></tr></table>

The detailed definition of the prompt is shown in Fig. 8. In the aspect of role definition, FEA is endowed with the role of a professional engineer specializing in file parsing and data analysis, whose knowledge system covers the fields of STP file parsing and image analysis; MPPA is positioned as a “senior process planner” focusing on macro-processing route decision-making based on multi-source data; SPPA is positioned as a “senior process planner” emphasizing the generation of detailed process plans based on tools and multi-dimensional information; POEA, as a “senior process planner”, completes the merging, evaluation, and optimization of process routes based on macro and detailed route information. Through the clearly defined role positioning by prompts, each Agent constructs a complete knowledge capability boundary from data parsing to solution optimization. In terms of task basis and input information, FEA takes the provided STP files and multi-view images as inputs to perform parsing tasks for points, surfaces, normal vectors, and machining features; MPPA carries out macro-manufacturing process route planning based on the multi-view analysis information output by 

FEA and the STP file analysis information; SPPA utilizes the STP file analysis information, part processing requirements, and the macroprocess route generated by MPPA to complete the detailed process route design; finally, POEA integrates the macro-process route and detailed process route, combines tool resource information, and completes the full-process optimization of the process route. In terms of specific task requirements, each Agent follows the task content and output format specified by prompts. FEA completes three parsing tasks as instructed; MPPA outputs the processing sequence of each machining feature and decision basis in the specified format; SPPA structurally presents the process chain and machining resources with reference to the Cypher query example; POEA completes route merging, evaluation, and optimization as required, and outputs the final process route, ensuring that the entire execution process maintains strict consistency with the prompt design. 

FEA not only generates the multi-view image analysis information of the part, describing the overall shape and distribution of machining feature structures, including details such as location and colour, but also produces detailed information about points, surfaces, normal vectors, and machining feature recognition, as shown in Fig. 9. Verified by process design experts, the generated machining feature descriptions are accurate, with all features correctly identified and no omissions detected. 

MPPA generates the machining sequence for each machining feature and provides detailed justifications for the sequence arrangement, reducing errors in information transfer, as shown in Fig. 10. Verified by process design experts, the generated machining sequence of the features constitutes a feasible process route. 

SPPA, based on the knowledge graph, matches the process chain and machining resources for each machining feature and generates more detailed machining process information in a specified format, building upon the macro machining process route of the part, as shown in Fig. 11. Verified by process design experts, the selected machining resources, including machines and cutting tools, align with resource allocation based on daily production experience. 

POEA, after comprehensively considering machining equipment, machining resources, and the ’rough first, then finish’ process principle, generates the final machining process route for the part by merging processes. The resulting machining process route, organized and merged in the sequence of ’rough milling − semi-finish milling − finish milling − drilling − boring,’ serves as the final output of the framework method presented in this paper, providing process designers with valuable insights, as shown in Fig. 12. Verified by process design experts, the final generated process route is feasible, with resource allocation consistent with daily experience and adhering to the machining principle of “roughing before finishing. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/aa5f8ca546518eadbe12514dc64eeaf36bf1484e7f1536363338cfd786c81723.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/d26d3711e30935b704f55f0fb4fee9538cebf49381b715bd51341e3e48a20056.jpg)



Fig. 6. Process knowledge graph.


<table><tr><td>ISO-10303-21;
HEADER;
FILE_DESCRIPTION((&#x27;Open CASCADE Model&#x27;),&#x27;2;1&#x27;);
FILE_NAME(&#x27;Open CASCADE Shape Model&#x27;,&#x27;2023-01-13T12:43:40&#x27;,&#x27;Author&#x27;),
    (&#x27;Open CASCADE&#x27;), &#x27;Open CASCADE STEP processor 7.5&#x27;, &#x27;Open CASCADE 7.5&#x27;
        ,&#x27;Unknown&#x27;);
FILE_SCHEMA((&#x27;AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }&#x27;)); 
ENDSEC;
DATA;
#1 = APPLICATION_PROTOCOL_DEFINITION(&#x27;international standard&#x27;,
    &#x27;automotive_design&#x27;,2000,#2);
#2 = APPLICATION_CONTEXT(
    &#x27;core data for automotive mechanical design processes&#x27;);
#3 = SHAPE_DEFINITION_REPRESENTATION(#4,#10);
#4 = PRODUCT_DEFINITION_SHAPE(&quot;, #5);
#5 = PRODUCT_DEFINITION(&#x27;design&#x27;,&quot;, #6,#9);
#6 = PRODUCT_DEFINITION_FORMATION(&quot;, #7);
#7 = PRODUCT(&#x27;Open CASCADE STEP translator 7.5 1&#x27;,
    &#x27;Open CASCADE STEP translator 7.5 1&#x27;,&quot;, (#8));
#8 = PRODUCT_CONTEXT(&quot;, #2,&#x27;mechanical&#x27;);
#9 = PRODUCT_DEFINITION_CONTEXT(&#x27;part definition&#x27;, #2,&#x27;design&#x27;);
#10 = ADVANCED_BREP_SHAPE_REPRESENTATION(&quot;, (#11,#15), #2393);</td></tr><tr><td>...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......</td></tr></table>


(a) Content of the Part's STP File



(b)Part's Multi-view Image



Fig. 7. Input of the process routes generation framework.


<table><tr><td>FEA
You are a professional engineer specializing in file parsing and data analysis, with expertise in parsing STP files and analyzing images. Using the provided tools, please complete the following three tasks:
(1) Parse the part&#x27;s STP file and provide information on the points, surfaces, normal vectors, and identified machining features of the part.
(2) Analyze the part&#x27;s multi-view images and describe both the overall structure and specific details, forming a comprehensive textual description.</td><td>MPPA
You are a senior process planner. Based on two sets of information for a given part: {Multi-view analysis information of the part} and {STP file analysis information}, please reasonably plan the macro machining process route for the part (i.e., the machining sequence of each feature). Consider the part&#x27;s shape characteristics, machining cost, machining convenience, and the number of tool changes to determine the machining sequence for each feature. Provide the reasoning for each step of the machining sequence.
Output format should follow the structure below:
1.Machining Feature XX
Reason: ......
2.Machining Feature XX
Reason: ......
3. .... .... .... ....</td><td>SPPA
You are a senior process planner. Using the tools and the following information: {STP file analysis information}, {Part machining requirements}, and {Macro process route}, generate a detailed machining process route for the part. The route should include the process chain for each machining feature and the machining machine tools and cutting tools used in each step. Be as detailed as possible.
The final output must follow the machining feature sequence in the macro process route and include the process chain for each machining feature (the process chain must be explicitly shown). Additionally, for each operation in the feature&#x27;s process chain, specify the machine tool and cutting tool used.
Note: An example Cypher query for retrieving the process chain of a machining feature is as follows: MATCH (mf:MF {name: &#x27;through hole&#x27;})-[:have]-&gt;(pc:process chain)
OPTIONAL MATCH (process chain)-[:have]-&gt;(pcx) .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... ...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Supports</td><td colspan="2">Supports</td><td colspan="2">Supports</td><td colspan="2">Supports</td></tr><tr><td>Example-Guided Prompting</td><td>Contextual Prompting</td><td>Instructional Prompting</td><td>Chain-of-Thought Prompting</td><td colspan="4">......</td></tr></table>


Fig. 8. Detailed design of multi-agent prompts in the process route generation task.


## 4.4. Evaluation of manufacturing process routes based on TOPSIS

To scientifically and objectively evaluate the advantages and disad vantages of the newly generated process route by multi-agent collaboration compared with the historical typical process route, this study establishes a comprehensive evaluation index system integrating both qualitative and quantitative factors, and conducts scheme evaluation based on the TOPSIS method. Specifically, three key quantitative indicators derived from actual production, namely production time, manufacturing cost, and energy consumption, are selected to comprehensively reflect the operational efficiency, economic performance, and resource utilization of the process routes. In addition, three qualitative indicators (process feasibility, process flexibility, and equipment utilization) are incorporated. Each indicator is rated by multiple domain experts on a three-level scale of high, medium, and low. The high level corresponds to scores from 4.0 to 5.0, where “very high” equals 5.0 and “relatively high” equals 4.0 to 4.5. The medium level corresponds to scores from 2.5 to 3.5, where “upper medium” equals 3.0 to 3.5 and “medium” equals 2.5 to 3.0. The low level corresponds to scores from 1.0 to 2.0, where “relatively low” equals 2.0 and “very low” equals 1.0 to 1.5. Incorporating these qualitative assessments helps mitigate the limitations of relying solely on quantitative data when characterizing 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/f8a3a2c840c764132ec298c1d3a0778d3c39a120963180e2c48ea825bc6b68dd.jpg)


## FEA

The part is madeofwhite plasticandhasanoverallrectangular shape.Itfeatures several characteristics anddetails,incluing: 

General Shape:Rectangular 

Feature Description: 

Twothroughholes:Locatedalongthecentralaxisoftheshortsides,symmetricallypositionedonbothsidesofthecentralaxis. 

Tworectangular channels:Located on both sidesof thecentral axisof the long sides,symmetrically placed. 

Fourrectangular grooves:Positioned atthe rightangle formed bythe intersectionof the tworectangular channels. 

Surface Treatment:Matte 

Color:White 

Other Features:Rounded corners,chamfers,etc. 

Part description 

Face0:Ae(e( (66847,552048000),(668473852,00）,(68473852,000),(66847,00)] 

Fae 66656,0)] 

Fe2: （23248,0,60）,(48,00）,(0,00) 

Face3: 50000),(46205,21922,50000),(46205,0,50000)] 

Face29:e 55204,30000)] 

Thispart has 32 faces. 

t 6,23,24,25})3. 

Fivefeatures,withthefollowingdata:featurename,facesinvolved,andthebasefaceof thefeature: 

through_hole[11][] 

through_hole[10][] 

rectangular_through_slot[13,14,15][14] 

rectangularpocket[16,17,18,19,20,21,26,27,28,29,30,31][18,19,28,29] 

rectangular_through_slot[4,5,6,23,24,25][5,4] 

Machining feature information 


Fig. 9. FEA output.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/a116ca4ea93b44303aaa9f8bc77968213f278e6d34648cbe9b5bd7f5202b9a7e.jpg)


## MPPA

1.**Basic Shape of the Machining Blank**: 

**Reason**:First, machining therectangular block shape provides areference surface for subsequent processing, ensuring the stability and accuracy of the part's positioning. 

2.**Machining Two Through Holes (Features:through_hole[1O] and[11])**： 

**Reason**:Through holes are generallysimpler features in machining,and can be performed immediately after the basic shape iscompleted.Machining through holes canuse thesame drillbit,reducing tool change times。 

3.**MachiningTwoRectangularSlots (Features:rectangular_through_slot[4,5,6,23,24,25]and[13,14,5])**： 

**Reason**:Rectangularslots are features thatpassthrough the entire part,typically machinedafter the through holes. While differentillingutesmaybeed,othsmmetcalotsabeproessdieseupducingter setups required.。 

4.**MachiningFourRectangularPockets (Features: rectangular_pocket[16,17,18,19,20,21,26,27,28,29,30,31])**： 

**Reason**:Pocket machining typically requires more precise milling operations,whichcan be done after machining theslots.Sincethepocketsarelocatedattheright-angleintersectionsoftheslots,machiningtheslotsfirstprovidesa reference for the pockets.。 

5.**Surface Treatment**: 

**Reason**:Surface treatment should be done after all features are machined to ensure the appearance and consistency of the part.。 

6.**Chamferingand Fillet Treatment**： 

Fig. 10. MPPA output. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/101a612c7d7973ecd256bdb0b330b17159680fd0c6e23ad5227a8c84242b9b91.jpg)


## SPPA

<table><tr><td colspan="3">1. **Processing the Basic Shape of the Workpiece**:</td></tr><tr><td colspan="3">- Process Chain 3:</td></tr><tr><td>- Step 1: Rough Milling</td><td>- Machine: Gantry Milling Machine (Doosan BM2045)</td><td>- Tool: Carbide End Mill (Kyocera PR1535)</td></tr><tr><td>- Step 2: Semi-Finishing Milling</td><td>- Machine: Horizontal Milling Machine (OKUMA MB-5000H)</td><td>- Tool: High-Speed Steel End Mill (Kennametal KSEM)</td></tr><tr><td>- Step 3: Finishing Milling</td><td>- Machine: CNC Milling Machine (DMG MORI NHX 5000)</td><td>- Tool: Tungsten Carbide End Mill (Sandvik CoroMill 316)</td></tr><tr><td colspan="3">2. **Processing Two Through Holes**:</td></tr><tr><td colspan="3">- Process Chain 6:</td></tr><tr><td>-Step 1: Drilling (Reaming)</td><td>- Machine: Radial Drill (Z3040)</td><td>- Tool: Drill Bit (Kyocera KSD30)</td></tr><tr><td>-Step 2: Precision Boring</td><td>- Machine: Boring Machine (TPX6111B)</td><td>- Tool: Carbide Precision Boring Tool (Mitsubishi BORING)</td></tr><tr><td colspan="3">3. **Processing Two Rectangular Slots**:</td></tr><tr><td colspan="3">- Process Chain 1:</td></tr><tr><td>- Step 1: Rough Milling</td><td>- Machine: Gantry Milling Machine (Doosan BM2740)</td><td>- Tool: Carbide End Mill (Mitsubishi APX4000)</td></tr><tr><td>- Step 2: Semi-Finishing Milling</td><td>- Machine: Horizontal Milling Machine (OKUMA MB-5000H)</td><td>- Tool: High-Speed Steel End Mill (Kyocera MEGACOAT)</td></tr><tr><td>- Step 3: Finishing Milling</td><td>- Machine: CNC Milling Machine (DMG MORI NHX 5000)</td><td>- Tool: Tungsten Carbide End Mill (Sandvik CoroMill 316)</td></tr><tr><td>- Step 4: Ultra-Fine Milling</td><td>- Machine: Ultra-Precision CNC Milling Machine (Makino F5)</td><td>- Tool: Ceramic Tool (Kyocera PV720)</td></tr><tr><td colspan="3">4. **Processing Four Rectangular Pockets**:</td></tr><tr><td colspan="3">- Process Chain 1:</td></tr><tr><td>- Step 1: Rough Milling</td><td>- Machine: Gantry Milling Machine (Doosan BM2740)</td><td>- Tool: Carbide End Mill (Mitsubishi APX4000)</td></tr><tr><td>- Step 2: Semi-Finishing Milling</td><td>- Machine: Horizontal Milling Machine (OKUMA MB-5000H)</td><td>- Tool: High-Speed Steel End Mill (Kyocera MEGACOAT)</td></tr><tr><td>- Step 3: Finishing Milling</td><td>- Machine: CNC Milling Machine (DMG MORI NHX 5000)</td><td>- Tool: Tungsten Carbide End Mill (Sandvik CoroMill 316)</td></tr><tr><td>- Step 4: Ultra-Fine Milling</td><td>- Machine: Ultra-Precision CNC Milling Machine (Makino F5)</td><td>-Tool: Ceramic Tool (Kyocera PV720)</td></tr><tr><td colspan="3">5. **Surface Treatment**:</td></tr><tr><td colspan="3">- Since surface treatment typically does not involve specific machines or tools, it is not detailed here.</td></tr><tr><td colspan="3">6. **Chamfering and Rounding**:</td></tr><tr><td colspan="3">- Since chamfering and rounding typically do not involve specific machines or tools, they are not detailed here..</td></tr></table>


Fig. 11. SPPA output.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/0767641fe5046ceb25f8fa2993f608c196c82b30ff4b6662065fae4380ab3f78.jpg)


## POEA

The evaluationscore for Process RouteMergingMethod1 is42,the evaluationscore for ProcessRoute Merging Method2 is -2,and the evaluationscore for theoriginalprocessrouteis-10.Therefore,ProcessRouteMergingMethod1hasthehighestevaluationscore. 

### Improved Process Route Merging Method 1: 

1.**Processing the Basic Shape of the Workpiece-Rough Milling** (Doosan BM2045,Kyocera PR1535) 

2.**Processing Two RectangularChannels-Rough Milling**(Doosan BM2740,Mitsubishi APX4000) 

3.**ProcessingFourRectangularPockets-RoughMilling(DoosanBM2740,itsubishiAX4000) 

4.Deburing-Ensurenoburrs remain onthe surface after rough milling 

5.Processing the Basic Shape oftheWorkpiece-Semi-FinishingMilling(OKUMAMB-50o0H,Kennametal KSEM) 

6.ProcessingTwoRectangularChannels-Semi-FinishingMiling(OKUMAMB-50ooH,KyoceraMEGACOAT) 

7.ProcessingFourRectangularPockets-Semi-FinishingMilling(OKUMAMB-50ooH,KyoceraMEGACOAT) 

8.Cleaning-Removechipsandcoolantresidue generated during the machining process 

9.Processing theBasicShape ofthe Workpiece-FinishingMiling(DMGMORINHX 50oo,Sandvik CoroMill316) 

10.ProcessingTwoRectangularChannels-FinishingMilling(DMGMORINHX500o,SandvikCoroMill316) 

11.ProcessingFourRectangularPockets-FinishingMilling(DMGMORINHX50oo,SandvikCoroMill316) 

12.Processing Two ThroughHoles-Drilling(Reaming) (Z3040,KyoceraKSD30) 

13.Processing Two Through Holes-PrecisionBoring(TPX611iB,MitsubishiBORING) 

14.Final Inspection-Checkall dimensionsand surface qualityto ensure they meet therequirements 

Byaddingauxiliary processes suchasdeburring,cleaning,andfinal inspection,the integrityofthe machining processandproduct qualityareensured." 

Fig. 12. POEA output. 

process flexibility and innovation capability. The specific definitions of each evaluation indicator and their data acquisition methods are presented in the Table 6. 

The quantitative indicator data for each process route scheme were collected from actual production statistics or enterprise databases, while the qualitative indicators were independently scored by three to five experts. The arithmetic mean of these expert scores was then incorporated into the decision matrix. To eliminate the effects of differing units and magnitudes among the indicators, a min–max normalization method was employed. The normalization formula is as shown in the Eq. (11): 

$$
x _ {i j} ^ {\prime} = \frac {x _ {i j} - \min (x _ {j})}{\max (x _ {j}) - \min (x _ {j})} \tag {11}
$$

here, x denotes the original score of the ith scheme under the jth evaluation indicator; min(xj) represent the minimum and maximum values, respectively, of the jth indicator across all schemes; $\mathbf { X } _ { \mathrm { i j } } ^ { ' }$ is the normalized value for the ith scheme under the jth indicator, where a higher value indicates better performance. 

The original indicator data for both the multi-agent collaboratively generated process route and the historical typical process route are presented in the Table 7. After normalization and weighting, the final TOPSIS-based closeness coefficients are summarized in the Table 8. 

According to the comprehensive TOPSIS evaluation, the process route generated by the proposed multi-agent collaboration approach exhibits a higher closeness coefficient than the historical typical scheme. This evaluation result demonstrates the effectiveness of the proposed method in multi-criteria decision-making scenarios. In summary, the multi-agent collaboration-based approach for rapid generation of manufacturing process routes enhances overall production performance, thereby exhibiting significant potential for engineering application and broader adoption 


Table 6 Evaluation Indicators Information Table.


<table><tr><td>Indicator</td><td>Type</td><td>Unit</td><td>Trend</td><td>Data source</td></tr><tr><td>Production Time</td><td>Numerical</td><td>H</td><td>The smaller, the better</td><td>Production Statistics</td></tr><tr><td>Manufacturing Cost</td><td>Numerical</td><td>RMB</td><td>The smaller, the better</td><td>Financial System</td></tr><tr><td>Energy Consumption</td><td>Numerical</td><td>kWh</td><td>The smaller, the better</td><td>Energy Monitoring</td></tr><tr><td>Process Feasibility</td><td>Rating</td><td>score (1 - 5)</td><td>The larger, the better</td><td>Expert Evaluation</td></tr><tr><td>Flexibility</td><td>Rating</td><td>score (1 - 5)</td><td>The larger, the better</td><td>Expert Evaluation</td></tr><tr><td>Equipment Utilization</td><td>Rating</td><td>score (1 - 5)</td><td>The larger, the better</td><td>Expert Evaluation</td></tr></table>


Table 7 Original Index Data Table.


<table><tr><td>Indicator</td><td>Typical process route</td><td>Multi-agent generated process route</td></tr><tr><td>Production Time (H)</td><td>16.5</td><td>14.8</td></tr><tr><td>Manufacturing Cost (RMB)</td><td>1280</td><td>1325</td></tr><tr><td>Energy Consumption (kWh)</td><td>235</td><td>193</td></tr><tr><td>Process Feasibility</td><td>4.5</td><td>3.25</td></tr><tr><td>Flexibility</td><td>3.2</td><td>4.3</td></tr><tr><td>Equipment Utilization</td><td>3.7</td><td>4.25</td></tr></table>


Table 8 Closeness Coefficient Comparison Table.


<table><tr><td>Scheme</td><td>Distance to positive ideal solution</td><td>Distance to negative ideal solution</td><td>Closeness coefficient</td></tr><tr><td>Typical Process Route</td><td>0.33</td><td>0.24</td><td>0.414</td></tr><tr><td>Multi-agent Generated Process Route</td><td>0.24</td><td>0.33</td><td>0.586</td></tr></table>

The results show that the machining process route generated by the multi-agent approach has a higher composite score compared to the typical machining process route. After the task of process merging based on the ’rough first, then finish’ principle, the multi-agent generated process route demonstrates advantages in machining cost and machining cycle. In the rough machining stage, it can quickly remove material, reducing machining time and cycle, while still meeting the requirements for machining quality and process feasibility, exhibiting favourable characteristics. 

According to the comprehensive TOPSIS evaluation, the process route generated by the proposed multi-agent collaboration approach exhibits a higher closeness coefficient than the historical typical scheme. This evaluation result demonstrates the effectiveness of the proposed method in multi-criteria decision-making scenarios. In summary, the multi-agent collaboration-based approach for rapid generation of manufacturing process routes enhances overall production performance, thereby exhibiting significant potential for engineering application and broader adoption. 

## 4.5. Discussion

## 4.5.1. Multi-agent collaboration and single-agent task completion capability

The multi-agent collaboration method proposed in this paper decomposes the process route generation task into multiple sub-tasks, which are completed through collaboration among multiple Agents, with each Agent responsible for different task modules. In the experimental design, the single-agent baseline was strictly configured to possess exactly the same task tools and resources as the multi-agent process route generation method. Specifically, in the single-agent scenario, the prompt used was constructed by integrating all prompt contents from the individual process route generation agents in the multiagent collaborative scheme, thereby consolidating prompts originally targeted at different task modules into a comprehensive input. All knowledge bases and auxiliary tools available for process route generation were equally provided to the single agent, allowing it to autonomously invoke these resources according to its own reasoning and planning capabilities to accomplish the task. Furthermore, the input for the single-agent was kept fully consistent with that of the multi-agent system, and no artificial constraints, functional limitations, or procedural simplifications were imposed during task execution. This ensured that the single agent had equivalent operational privileges and access to information as in the multi-agent collaborative environment, thereby enabling it to independently complete the generation and decisionmaking tasks for complex process routes under identical knowledge and information conditions. The single Agent’s prompts and output results are shown in the Fig. 13. 

Comparing the final process route generation results obtained by POEA, the single-agent approach faces limitations when dealing with complex tasks due to factors such as long prompts, excessive task focus, and constraints on computational power, knowledge scope, and task handling efficiency. The excessive number of tools assigned to the single Agent is not fully utilized, resulting in a rough outcome with inaccurate information. In contrast, by employing multi-agent collaboration, tasks can be divided and processed in parallel, with each Agent efficiently collaborating based on its specific expertise or task module. This accelerates the process route generation speed and improves the optimization of the solution. This approach fully leverages the advantages of individual Agents, overcoming bottlenecks when faced with complex tasks, making full use of the various tools at hand, and ensuring the processing and transfer of information. The generated process route is accurate, refined, and exhibits better characteristics. In addition to an evaluation of visual quality, two fundamental quantitative metrics—planning time and information-extraction error rate—were measured. The results indicate that the multi-agent approach reduced planning time by approximately 25 % and lowered the informationextraction error rate by nearly 52 % compared with the single-agent baseline, thereby quantitatively confirming its superior efficiency and quality. 

In engineering applications, the approach of a single-agent independently completing tasks is applicable, especially when the tasks are relatively simple, resources are limited, or there is a need to quickly obtain preliminary solutions. This method can reduce the communication and coordination costs between multi-agents by centralizing the processing. However, for complex engineering tasks, such as process route generation, the tasks themselves often involve higher complexity and more diverse requirements. In such scenarios, multi-agent collaboration holds promise in improving the overall system efficiency, flexibility, and accuracy through mechanisms like task decomposition, resource sharing, and decision-making coordination. 

Although the multi-agent collaboration method has demonstrated certain advantages in process route generation tasks, several issues still require further exploration and optimization. First, the coordination mechanism between Agents needs to be further deepened. While the existing collaboration methods can decompose tasks and improve efficiency through parallel processing, ensuring effective information 

## Prompt ED

You are a senior process planner.Based on the part's STP file and multi-view images,combined withthe requirement that'thepart's blank material is black metal,and the final machiningachievesa surface roughness grade of O.8-3.2and dimensional accuracy ofIT7-IT8,' generatea detailed machining process route for the part. The detailed process route should include the machines and tools used in each operation.Organize the process route following the'rough first,then finish' principle.Please provide the final answer inthe following format: 

1. **Machining XX feature -Process X** (Machine model XX, Tool model XX) 

2.**Machining XX feature -Process X** (Machine model XX, Tool model XX) 

3.**Machining XX feature -ProcessX**(Machine model XX,Tool model XX) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/c33f7cb4-8639-4172-8b7d-3227679aa567/93eca1536efee7e29d9cef43cd8ee999037d31965f195b250ef0dc79ed8c6152.jpg)


## Output

Basedontherelevant informationandrequirements ofte part,te following is the machining process route for the part: 

1.**Machining the blank shape -Rough machining** (Milling Machine,e.g., Mazak VTC 800,Rough End Mill,e.g.,φ25mm Hss End Mill) 

2.**Machining through hole feature -Rough machining**(CNC Milling Machine, e.g.,Haas VF-2,DrillBit,e.g.,10mm Tungsten CarbideDril Bit) 

3.**Machining the blank shape -Fine machining**(CNC Milling Machine,e.g., Mazak VTC 800, PrecisionEndMill,e.g., 12mm CarbdeEnd Mill) 

4.**Machining through holefeature-Fine machining** (CNC Milig Machine,e.g., Haas VF-2,Precision DrillBit, e.g., φ8mmCarbide Drill Bit) 

Fig. 13. Comparison of multi-agent and single-agent output results. 

sharing and communication between Agents, particularly in complex and information-dense tasks, remains a key challenge. Second, optimizing task decomposition and module division is another important issue in multi-agent collaboration. How to reasonably decompose complex specialized tasks into multiple sub-tasks, and allocate them to different Agents based on task complexity and requirements, is crucial for improving collaboration efficiency. Tasks that are too simple may lead to under-utilization of some Agents’ capabilities, while overly complex tasks may result in excessive workload, which could impact efficiency and the quality of the final results. Therefore, future research should consider more dynamic task allocation and optimization methods to achieve the optimal collaboration outcomes. While this section has made efforts to ensure fairness in the comparison of singleagent and multi-agent approaches in terms of experimental conditions and resource allocation, the performance of the single-agent baseline may still improve with algorithmic optimizations (such as better prompts, memory mechanisms, etc.). In the future, further refinement of the single-agent baseline can be pursued, and additional benchmarks and evaluation methods can be introduced to achieve a more comprehensive and rigorous comparative analysis. 

4.5.2. Enhancement of agent expertise through external knowledge bases In this paper, an external knowledge base in the form of a knowledge graph is introduced during the construction of SPPA. By integrating external knowledge as a knowledge retrieval tool with the Agent, the professional capability of the Agent is enhanced when handling complex tasks. Without changing the overall prompts of SPPA, when the knowledge graph retrieval tool is removed, the output of the detailed machining process route generation task is shown in the Fig. 14. Although the generated results are output in the format defined by the prompts, the granularity of the machining feature process chain varies, which does not align with the traditional representation of process chains. Additionally, the machining resources such as tools and machines provided are rough and inadequate. 

With the integration of the knowledge graph external knowledge base, the accuracy, rationality, and optimization of the machining process route generated by SPPA have significantly improved compared to when the external knowledge base is not integrated. The quality of the content generated in the field of process expertise has greatly increased. Specifically, the Agent with access to the external knowledge base can quickly acquire and integrate a richer pool of domain knowledge, enabling more precise matching and decision-making during the process route generation. Additionally, based on actual production conditions, the knowledge base provides detailed information about machining resources such as machine tools and cutting tools, further enhancing the feasibility and practicality of the generated route. This approach 

## Output

Here is the detailed machining process chain for the part based on the macro processroute and the query results of the processchain, including the machine tools and cutting tools for each step: 

1.**Machining the basic shape of the blank**: 

Rough machining: Use a lathe for turning with rough turning tools. 

Finishing:Use a milling machine for milling with fine milling tools. 

Machine Tools and Cutting Tools: Lathe (rough turning tools),Milling machine (fine milling tools). 

2.**Machining two through holes **: 

Positioning and clamping: Use a drilling machine with fixture for clamping. 

Center drilling: Usea center drill. 

Driling: Use anappropriate diameter twist drill. 

Deburring: Use manual deburring tools. 

Machine Tools and Cutting Tools: Drilling machine (center drill, twist drill). 

3.**Machining two rectangular slots ** 

Rough machining:Use a vertical milling machine with a rough milling cutter. 

Finishing: Use a vertical milling machine with a fine milling cutter. 

Machine Tools and Cutting Tools: Vertical milling machine (rough milling cuter, fine milling cutter). 

6.**Chamfering and rounding**: 

Chamfering:Use a chamfering machine with chamfering tools. 

Rounding: Use manual tools with rounding tools. 

Machine Tools and Cutting Tools: Chamfering machine (chamfering tools), Manual tools (rounding tools). 

The above process chain ensures that the part's machining meets the requirements for black metal materials, witha roughness gradeof 0.8-3.2 and dimensional accuracy ofIT7-IT8.s 

Fig. 14. Output of SPPA without support from a knowledge graph. 

effectively prevents the need for re-planning the process route due to improper resource selection, thereby improving overall production efficiency and optimizing the solution. 

Although the introduction of the external knowledge base has brought significant benefits, it has also exposed some challenges. The semantic matching and reasoning capabilities during the knowledge base query process represent a pressing issue. While the knowledge graph provides a vast amount of structured knowledge, how to efficiently and accurately retrieve relevant knowledge based on the Agent’s actual needs and the problem context, and perform reasonable reasoning and inference, remains a significant technical challenge. 



[5] Y. Zhang, S. Zhang, R. Huang, B. Huang, J. Liang, H. Zhang, Z. Wang, Combining deep learning with knowledge graph for macro process planning, Comput. Ind. 140 (2022) 103668. 





[64] S. Pateria, B. Subagdja, A.H. Tan, C. Quek, Value-based subgoal discovery and path planning for reaching long-horizon goals, IEEE Trans. Neural Networks Learn. Syst. 35 (2024) 10288–10300. 



## 5. Conclusion



[6] Z. Wang, X. Liang, M. Li, S. Li, J. Liu, L. Zheng, Towards cognitive intelligenceenabled product design: the evolution, state-of-the-art, and future of AI-enabled product design, J. Ind. Inf. Integr. 43 (2025) 100759. 





[65] Multimodal Web Navigation with Instruction-Finetuned Foundation Models, (2024). 



To overcome the limitations of traditional process design, which heavily relies on individual experience and knowledge and has long design cycles, a method for the rapid generation of process routes based on a multi-agent collaboration using LLMs is proposed. This method involves the construction of four agents: FEA (Feature Recognition Agent), MPPA (Feature Sorting Agent), SPPA (Resource Selection Agent), and POEA (Process Route Optimization and Merging Agent). Each agent performs one of the four sub-tasks: recognition of machining features, sorting of machining features, selection of machining resources, and optimization of the process route. The input to the method consists of a part’s STP file and multi-view images, while the output is a feasible process route with certain economic benefits, generated by POEA. This method can quickly recommend a suitable machining process route for professionals in the field, facilitating heuristic design by process engineers. This study proposes an LLM-based multi-agent collaborative method for rapid generation of process routes, opening up a new path for heuristic recommendation design in process planning. By modularly decomposing the task flow and assigning specialized division of labour to Agents, the advantages of multi-agent collaboration in task decomposition, knowledge integration, and dynamic content generation are fully leveraged. Based on the design of general prompt words and tool-based integration of advanced technologies, this method can be adapted to process planning for complex products in multiple fields such as aerospace, automotive, and equipment manufacturing, providing support for innovative design and knowledge reuse in enterprises. The innovations of this study are summarised as follows: 



[7] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang, J. Wang, S. Jin, E. Zhou, R. Zheng, X. Fan, X. Wang, L. Xiong, Y. Zhou, W. Wang, C. Jiang, Y. Zou, X. Liu, Z. Yin, S. Dou, R. Weng, W. Qin, Y. Zheng, X. Qiu, X. Huang, Q. Zhang, T. Gui, The rise and potential of large language model based agents: a survey, SCIENCE CHINA Inf. Sci. 68 (2025) 121101. 





[66] Z. Wang, Z. Yan, S. Li, J. Liu, IndVisSGG: VLM-based scene graph generation for industrial spatial intelligence, Adv. Eng. Inf. 65 (2025) 103107. 





[8] T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N.V. Chawla, O. Wiest, X. Zhang, Large language model based multi-agents: a survey of progress and challenges. Proceedings of the Thirty-Third International Joint Conference on Artificial IntelligenceJeju, 2024. 





[67] R. Gallotta, G. Todd, M. Zammit, S. Earle, A. Liapis, J. Togelius, G.N. Yannakakis, Large language models and games: a survey and roadmap, IEEE Trans. Games (2024) 1–18. 



(1) This work is the first to apply an LLM-driven multi-agent collaborative division of labour to machining process planning. Prompt-tuned large language models act as the “brains” of the agents, enabling rapid completion of feature recognition, operation selection and route optimisation. Compared with traditional approaches that depend on explicit rules and expert knowledge, the proposed method markedly lowers the knowledge barrier and enhances generation efficiency. 



[9] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, W.X. Zhao, Z. Wei, J. Wen, A survey on large language model based autonomous agents, Front. Comp. Sci. 18 (2024) 186345. 





[68] S. Hu, T. Huang, F. Ilhan, S.F. Tekin, G. Liu, R.R. Kompella, L. Liu, A Survey on Large Language Model-Based Game Agents, ArXiv, abs/2404.02039 (2024). 



(2) An agent capability system integrating a multimodal toolchain is developed. By combining a process knowledge graph, CAD or visual parsers and numerical-analysis utilities, the system supplies the LLM with structured domain knowledge and real data, thereby improving the accuracy of knowledge acquisition and utilisation while alleviating hallucination issues frequently observed in LLM outputs. 



[10] S. Gronauer, K. Diepold, Multi-agent deep reinforcement learning: a survey, Artif. Intell. Rev. 55 (2022) 895–943. 





[69] M.C. Schubert, W. Wick, V. Venkataramani, (2023). 



Although the proposed method has certain contributions, it also has some limitations: 



[11] D. Lee, N. He, P. Kamalaruban, V. Cevher, Optimization for reinforcement learning: from a single agent to cooperative agents, IEEE Signal Process Mag. 37 (2020) 123–135. 





[12] J.S. Park, J. O’Brien, C.J. Cai, M.R. Morris, P. Liang, M.S. Bernstein, Generative agents: interactive simulacra of human behaviour, in: Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, Association for Computing Machinery, San Francisco, CA, USA, 2023, p. 2.. 





[70] E. Fast, B. Chen, J. Mendelsohn, J. Bassen, M.S. Bernstein, Iris: A Conversational Agent for Complex Tasks, Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, Association for Computing Machinery, Montreal QC, Canada, 2018, pp. Paper 473. 



(1) This research relies on the quality of LLMs and various tools. In practical applications, the performance of the LLMs and the accuracy and comprehensiveness of the tools will directly affect the effectiveness of process route generation. 



[13] J.S. Park, L. Popowski, C. Cai, M.R. Morris, P. Liang, M.S. Bernstein, Social Simulacra: Creating Populated Prototypes for Social Computing Systems, in: Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology, Association for Computing Machinery, Bend, OR, USA, 2022, p. 74. 





[71] T.T. Nguyen, N.D. Nguyen, S. Nahavandi, Deep reinforcement learning for multiagent systems: a review of challenges, solutions, and applications, IEEE Trans. Cybern. 50 (2020) 3826–3839. 



(2) For complex parts, issues such as inaccurate recognition of machining features and unreasonable process route generation 



[14] Y. Liu, W. Wang, Y. Hu, J. Hao, X. Chen, Y. Gao, Multi-agent game abstraction via graph attention neural network, in: Proceedings of the AAAI Conference on Artificial Intelligence, 2020, pp. 7211–7218. 





[72] O. Topsakal, T.C. Akinci, Creating large language model applications utilizing langchain: a primer on developing LLM apps fast, Int. Conf. Appl. Eng. Nat. Sci. 1 (2023) 1050–1056. 



may arise, limiting the heuristic design ideas that can be provided to process designers. 



[15] M. Taub, R. Sawyer, A. Smith, J. Rowe, R. Azevedo, J. Lester, The agency effect: the impact of student agency on learning, emotions, and problem-solving behaviours in a game-based learning environment, Comput. Educ. 147 (2020) 103781. 





[73] Z. Wang, S. Zhang, H. Zhang, Y. Zhang, J. Liang, R. Huang, B. Huang, Machining feature process route planning based on a graph convolutional neural network, Adv. Eng. Inf. 59 (2024) 102249. 



(3) The proposed method has been validated only on a single aerospace component and has not yet undergone systematic evaluation across multiple industries, diverse part types, or varied machining scenarios; consequently, its generalization capability and applicability still require further verification. 



[16] X. Zhang, H. Zhang, Z. Jiang, Y. Wang, An integrated model for remanufacturing process route decision, Int. J. Comput. Integr. Manuf. 28 (2015) 451–459. 



Future work will continue to explore methods and techniques to enhance the generative capabilities of LLMs, refine knowledge graphs and associated tools, and investigate more efficient and rational collaboration mechanisms across different organisational and functional levels among agents, with the aim of extending applications to diverse industries and engineering domains of varying complexity. At the same time, we will further integrate enterprise security protocols to develop adaptive technical solutions, ensuring the effectiveness of data desensitization, encryption, and intellectual property isolation measures for real industrial data. 



[17] C. Li, R. Mo, Z. Chang, D. Zhang, Y. Xiang, Decision-making of process route considering process planning experience and manufacturing stability, J. Computer-Aided Design Comp. Graph. 27 (2015) 2384–2392. 



## CRediT authorship contribution statement



[18] Z. Xu, Y. Dang, Solution knowledge mining and recommendation for quality problem-solving, Comput. Ind. Eng. 159 (2021) 107313. 



Yanling Xie: Writing – original draft, Methodology, Formal analysis, Conceptualization. Jihong Liu: Writing – review & editing, Methodology, Investigation, Funding acquisition, Conceptualization. Ruiwen Wang: Writing – review & editing, Validation, Project administration, Methodology, Conceptualization. Zuoxu Wang: Writing – review & editing, Project administration, Investigation, Funding acquisition. Kai Yu: Writing – review & editing. Ziming Song: Writing – review & editing, Conceptualization. 



[19] W. Li, S. He, X. Mao, B. Li, C. Qiu, J. Yu, F. Peng, X. Tan, Multi-agent evolution reinforcement learning method for machining parameters optimization based on bootstrap aggregating graph attention network simulated environment, J. Manuf. Syst. 67 (2023) 424–438. 



## Declaration of competing interest



[20] Z. Han, R. Huang, B. Huang, J. Jiang, X. Li, Data-driven and knowledge-guided approach for NC machining process planning, Comput. Aided Des. 162 (2023) 103562. 



The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 



[21] X. Li, C. Yue, X. Liu, J. Zhou, L. Wang, ACWGAN-GP for milling tool breakage monitoring with imbalanced data, Rob. Comput. Integr. Manuf. 85 (2024) 102624. 



## Acknowledgments



[22] C. Hao, X. Mao, T. Ma, S. He, B. Li, H. Liu, F. Peng, L. Zhang, A novel deep learning method with partly explainable: Intelligent milling tool wear prediction model based on transformer informed physics, Adv. Eng. Inf. 57 (2023) 102106. 



Research funded by the grant from the National Key Research and Development Program of China, China (Grant No. 2024YFB3311801) under the project titled “Digital-intelligent foundation for the integration of product design, manufacturing, and service” and the National Key Research and Development Program of China, China (Grant No. 2020YFB1711400) under the project titled “Key Technologies and System Development for Visualized Intelligent Design and Simulation Verification of Customized Products. It is also supported by the Ministry of Industry and Information Technology (MIIT) Key Laboratory of Intelligent Manufacturing for High-end Aerospace Products, and the Beijing Key Laboratory of Digital Design and Manufacturing. 



[23] X. Huang, X. Zhang, Y. Xiong, F. Dai, Y. Zhang, Intelligent fault diagnosis of turbine blade cracks via multiscale sparse filtering and multi-kernel support vector machine for information fusion, Adv. Eng. Inf. 56 (2023) 101979. 



## Data availability



[24] S.P. Leo Kumar, State of the art-intense review on artificial intelligence systems application in process planning and manufacturing, Eng. Appl. Artif. Intell. 65 (2017) 294–329. 



Data will be made available on request. 



[25] Z. Chang, The measure and search method of process knowledge element based on machining intent, J. Mech. Eng. 54 (2018) 160. 



## References



[26] L. Guo, F. Yan, T. Li, T. Yang, Y. Lu, An automatic method for constructing machining process knowledge base from knowledge graph, Rob. Comput. Integr. Manuf. 73 (2022) 102222. 





[27] Y. Xiao, S. Zheng, J. Shi, X. Du, J. Hong, Knowledge graph-based manufacturing process planning: a state-of-the-art review, J. Manuf. Syst. 70 (2023) 417–435. 





[1] Y.Q. Lu, X. Xu, L.H. Wang, Smart manufacturing process and system automation - a critical review of the standards and envisioned scenarios, J. Manuf. Syst. 56 (2020) 312–325. 





[28] Z. Chen, Y. Wang, B. Zhao, J. Cheng, X. Zhao, Z. Duan, Knowledge graph completion: a review, IEEE Access 8 (2020) 192435–192456. 





[2] C.-S. Lee, J.-H. Lee, D.-S. Kim, E.-Y. Heo, D.-W. Kim, A hole-machining process planning system for marine engines, J. Manuf. Syst. 32 (2013) 114–123. 





[29] D. Kiritsis, A review of knowledge-based expert systems for process planning, Methods Problems, Int. J. Adv. Manuf. Technol. 10 (1995) 240–262. 





[3] Y. Ye, T. Hu, C. Zhang, W. Luo, Design and development of a CNC machining process knowledge base using cloud technology, Int. J. Adv. Manuf. Technol. 94 (2018) 3413–3425. 





[30] A.M. Luscombe, D.J. Toncich, A geometrical approach to computer-aided process planning for computer-controlled machine tools, Int. J. Adv. Manuf. Technol. 11 (1996) 83–90. 





[4] X. Fu, D. Peddireddy, V. Aggarwal, M.B.G. Jun, Improved dexel representation: a 3- D CNN geometry descriptor for manufacturing CAD, IEEE Trans. Ind. Inf. 18 (2022) 5882–5892. 





[31] C. Picard, K.M. Edwards, A.C. Doris, B. Man, G. Giannone, M.F. Alam, F. Ahmed, From concept to manufacturing: evaluating vision-language models for engineering design, ArXiv (2023) abs/2311.12668. 





[32] Y. Tian, A. Liu, Y. Dai, K. Nagato, M. Nakao, Systematic synthesis of design prompts for large language models in conceptual design, CIRP Ann. 73 (2024) 85–88. 





[33] S. Colabianchi, F. Costantino, N. Sabetta, Assessment of a large language model based digital intelligent assistant in assembly manufacturing, Comput. Ind. 162 (2024) 104129. 





[34] C. Gkournelos, C. Konstantinou, S. Makris, An LLM-based approach for enabling seamless Human-Robot collaboration in assembly, CIRP Ann. 73 (2024) 9–12. 





[35] Y. Zhang, Large language model in SD-WAN intelligent operations and maintenance, in: Research Briefs on Information and Communication Technology Evolution, 2023, pp. 178–188. 





[36] L. Vidyaratne, X.Y. Lee, A. Kumar, T. Watanabe, A. Farahat, C. Gupta, Generating troubleshooting trees for industrial equipment using large language models (LLM), IEEE Int. Conf. Prog. Health Manag. (ICPHM) 2024 (2024) 116–125. 





[37] P.Y. Abijith, P. Patidar, G. Nair, R. Pandya, Large Language Models Trained on Equipment Maintenance Text, ADIPEC, 2023, pp. D021S065R003. 





[38] D. Federiakin, D. Molerov, O. Zlatkin-Troitschanskaia, A. Maur, Prompt engineering as a new 21st century skill, Front. Edu. 9 (2024). 





[39] G. Marvin, N. Hellen, D. Jjingo, J. Nakatumba-Nabende, Prompt engineering in large language models, in: I.J. Jacob, S. Piramuthu, P. Falkowski-Gilski (Eds.), Data Intelligence and Cognitive Informatics, Springer Nature Singapore, Singapore, 2024, pp. 387–402. 





[40] E. Balcı, M. Sarıgül, B. Ata, Prompting large language models for aerial navigation, in: 2024 9th International Conference on Computer Science and Engineering (UBMK), 2024, pp. 304–309. 





[41] S. Tiwari, N. Mihindukulasooriya, F. Osborne, D. Kontokostas, J. D’Souza, M. Kejriwal, F. Polat, I. Tiddi, P. Groth, Testing prompt engineering methods for knowledge extraction from text, Semantic Web 16 (2025) SW-243719. 





[42] J. Bode, B. Patzold, ¨ R. Memmesheimer, S. Behnke, A comparison of prompt engineering techniques for task planning and execution in service robotics, in: 2024 IEEE-RAS 23rd International Conference on Humanoid Robots (humanoids), 2024, pp. 309–314. 





[43] P. Ardimento, M.L. Bernardi, M. Cimitile, Teaching UML using a RAG-based LLM, Int. Joint Conf. Neural Netw. (IJCNN) 2024 (2024) 1–8. 





[44] A. Mansurova, A. Mansurova, A. Nugumanova, QA-RAG: exploring LLM reliance on external knowledge. Big Data and Cognitive Computing, 2024. 





[45] Z. Wang, Z. Liu, W. Lu, L. Jia, Improving knowledge management in building engineering with hybrid retrieval-augmented generation framework, J. Build. Eng. (2025) 112189. 





[46] L. Siddharth, J. Luo, Retrieval augmented generation using engineering design knowledge, Knowl.-Based Syst. 303 (2024) 112410. 





[47] V. Zolfaghari, N. Petrovic, F. Pan, K. Lebioda, A. Knoll, Adopting RAG for LLMaided future vehicle design, in: 2024 2nd International Conference on Foundation and Large Language Models (FLLM), 2024, pp. 437–442. 





[48] F. Wu, Z. Li, Y. Li, B. Ding, J. Gao, FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model, Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, Barcelona, Spain, 2024, pp. 3345–3355. 





[49] J.C.d.S. Junior, R. Hu, R. Song, Y. Bai, Domain-Driven LLM Development: Insights into RAG and Fine-Tuning Practices, Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, Barcelona, Spain, 2024, pp. 6416–6417. 





[50] D.M. Anisuzzaman, J.G. Malins, P.A. Friedman, Z.I. Attia, Fine-tuning large language models for specialized use cases, Mayo Clinic Proceedings: Digital Health 3 (2025) 100184. 





[51] R. Rosati, F. Antonini, N. Muralikrishna, F. Tonetto, A. Mancini, Improving Industrial Question Answering Chatbots with Domain-Specific LLMs Fine-Tuning, 2024 20th IEEE/ASME International Conference on Mechatronic and Embedded Systems and Applications (MESA), 2024, pp. 1-7. 





[52] N.R.a.R.H. Desai, The Two Word Test: A Semantic Benchmark for Large Language Models, arXiv, abs/2306.04610(2023). 





[53] Z.T.a.Z.J.a.X.B.a.H.Z.a.Y.F.a.J.L.a.W. Hu, EvEval: A Comprehensive Evaluation of Event Semantics for Large Language Models, arXiv, abs/2305.15268(2023). 





[54] T.Y.C. Tam, S. Sivarajkumar, S. Kapoor, A.V. Stolyar, K. Polanska, K.R. McCarthy, H. Osterhoudt, X. Wu, S. Visweswaran, S. Fu, P. Mathur, G.E. Cacciamani, C. Sun, Y. Peng, Y. Wang, A framework for human evaluation of large language models in healthcare derived from literature review, npj Digital Med. 7 (2024) 258. 





[55] L.I.a.S.H.a.L.A.a.M. Anderljung, Beyond static AI evaluations: advancing human interaction evaluations for LLM harms and risks, arXiv, abs/2405.10632(2024). 





[56] C.G.a.X.L.a.N.L.a.Y.Y.a.J.D.a.Z.Z.a.F.X.a.Y. Li, Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, arXiv, abs/ 2306.04610(2023). 





[57] -.W. Zhou, -.X. Zhu, -.Q.-L. Han, -.L. Li, -.X. Chen, -.S. Wen, -.Y. Xiang, - The Security of Using Large Language Models: A Survey With Emphasis on ChatGPT, - IEEE/CAA Journal of Automatica Sinica, - 12 (2025) - 1. 





[58] J.A. Heredia Alvaro, ´ J.G. Barreda, An advanced retrieval-augmented generation system for manufacturing quality control, Adv. Eng. Inf. 64 (2025) 103007. 





[59] Q. Xu, G. Zhou, C. Zhang, F. Chang, Y. Cao, D. Zhao, Generative AI and DT integrated intelligent process planning: a conceptual framework, Int. J. Adv. Manuf. Technol. 133 (2024) 2461–2485. 





[60] R. Schumann, W. Zhu, W. Feng, T.-J. Fu, S. Riezler, W.Y. Wang, VELMA: verbalization embodiment of LLM agents for vision and language navigation in street view, in: Proceedings of the AAAI Conference on Artificial Intelligence, 2024, pp. 18924–18933. 





[61] J. Wang, T. Wang, W. Cai, L. Xu, C. Sun, Boosting efficient reinforcement learning for vision-and-language navigation with open-sourced LLM, IEEE Rob. Autom. Lett. 10 (2025) 612–619. 





[62] C. Sun, W. Liu, L. Dong, Reinforcement learning with task decomposition for cooperative multiagent systems, IEEE Trans. Neural Networks Learn. Syst. 32 (2021) 2054–2065. 





[63] E. Ephrati, J.S. Rosenschein, A heuristic technique for multi-agent planning, Ann. Math. Artif. Intell. 20 (1997) 13–67. 

