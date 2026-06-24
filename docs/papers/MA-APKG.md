Technical paper 

# MA-APKG: A multi-agent LLM-based method for construction aviation product assembly process knowledge graph

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/07618a45d82f2c2eb9affec9730b62e0546a1b2e20b36a041657c86635403702.jpg)


Jun Pu , Yu Guo , Shaohua Huang , ChenXin Zhou , JiaJun Tian , Lijun Ma 

College of Mechanical and Electrical Engineering, Nanjing University of Aeronautics and Astronautics, China 

## A R T I C L E I N F O

Keywords: 

Large language models 

Multi-agent systems 

Knowledge graph 

Complex aviation products 

Assembly process knowledge 

## A B S T R A C T

To address the characteristics of complex aviation assembly process knowledge, including diverse knowledge types, complex hierarchical structures, strong semantic correlations, and continuous evolution, a top-down construction method for an assembly process knowledge graph (KG) is proposed. First, a multi-level assembly process ontology is developed to provide unified and standardized modeling of product information, assembly process knowledge, tools and equipment, historical cases, and their cross-level relationships, enabling structured knowledge representation and semantic consistency enforcement. Second, to cope with the semantic complexity of assembly process texts, a large language model (LLM)-based multi-agent collaborative triple information extraction method is proposed. By integrating ontology constraints and a self-consistency chain-of-thought (CoT) mechanism, the stability, accuracy, and interpretability of extraction results are significantly improved. Finally, a semantic embedding-based dynamic KG update strategy is adopted to maintain entity uniqueness and semantic consistency during continuous knowledge evolution. Experimental results demonstrate the effectiveness and applicability of the proposed method in complex aviation assembly process scenarios. 

## 1. Introduction

The assembly workload of complex aviation products usually accounts for 50–60% of the total manufacturing workload [1]. Assembly process planning integrates and matches product design information, assembly process knowledge, and assembly resources to generate executable assembly process plans, serving as a critical bridge between product design and manufacturing [2]. As the primary data source for all assembly activities, the quality and efficiency of assembly process planning directly affect both the in-service performance of the product and the development cycle [3]. The production of complex aviation products exhibits several distinctive characteristics. On the one hand, the highly complex product structures and extremely high levels of system integration require customized designs for different models and even for different production batches of the same model [4,5]. On the other hand, niche market demands and customer-specific configuration requirements result in a typical order-driven production mode [6]. In addition, considering the substantial R&D investment, rapid technological evolution, and the close relevance to national security strategies, small-batch and incremental production approaches have become an inevitable choice for risk reduction and optimized resource allocation [7]. Under this background, investigating knowledge-driven assembly process planning methods for complex aviation products is of great significance for improving product development efficiency and manufacturing capability. 

The assembly process of complex aviation products differs significantly from that of general mechanical products, as it imposes extremely stringent requirements on aerodynamic profiles and assembly accuracy [8]. Aviation products are characterized by highly complex structures and confined assembly spaces, involving a large number of parts and fasteners, many of which exhibit large dimensions, low stiffness, and susceptibility to deformation [9]. To ensure assembly accuracy, a wide variety of complex fixtures and tooling jigs must be employed during the assembly process [10]. Meanwhile, to meet the comprehensive requirements of aviation products in terms of lightweight design, structural strength, fatigue resistance, and sealing performance [11], riveted joints are extensively adopted in assembly operations [12], along with the widespread application of advanced materials, such as composite materials and aviation aluminum alloys [13]. Under these assembly characteristics and technical constraints, assembly process planning for complex aviation products involves multiple critical decision-making tasks, including assembly partitioning, datum selection, process compensation design, assembly sequence planning, and the selection of tools and equipment [14]. Consequently, assembly process planning knowledge encompasses not only conventional process decision knowledge, but also three-dimensional product model information as well as resource information related to tools, fixtures, and equipment. Such knowledge and data are primarily derived from industry standards, historical process documents, tooling and equipment, and product 3D models, exhibiting characteristics of multi-source heterogeneity, implicitness, and dispersion [15]. Traditional document- based or database-based management approaches struggle to effectively represent semantic relationships among knowledge elements and are not well suited for knowledge reuse or intelligent reasoning. Therefore, investigating an efficient and accurate knowledge modeling approach to systematically organize, uniformly manage, and effectively utilize assembly process knowledge is of great significance. 

KG model fragmented process knowledge in the form of “entities–relations–attributes” using a graph structure, which not only enables unified representation and associative management of complex process knowledge, but also provides fundamental support for intelligent retrieval, reasoning and analysis, as well as knowledge-enhanced applications based on LLMs. Moreover, with the continuous advancement of aviation assembly technologies, new processes, equipment, and materials are constantly being introduced, leading to the dynamic evolution of assembly process planning knowledge [10]. How to update newly emerging elements into the knowledge base and analyze the dynamic evolution mechanisms of the KG is crucial for ensuring the timeliness and reliability of the process knowledge base. To address these challenges, this study proposes an LLM-based KG construction method for aviation product assembly processes, along with a bidirectionally driven data update mechanism, to ensure the real-time availability and reliability of assembly process knowledge for complex aviation products. The main contributions of this paper are summarized as follows: 

(1) A multi-level ontology model for assembly process KG is developed to address the diversity, hierarchical complexity, and strong interconnections of assembly knowledge, enhancing its organization and semantic consistency. 

(2) The traditional end-to-end triple extraction pipeline is decom posed into multiple agents with clearly defined roles (e.g., preprocessing, entity recognition, relation generation, and verification). With ontology constraints and feedback mechanisms, semantic ambiguity and structural conflicts are reduced. 

(3) A multi-path CoT generation and consistency evaluation mechanism is introduced to stabilize LLM reasoning, improving the accuracy, robustness, and interpretability of triple extraction. 

(4) KG dynamic updates are modeled as time-evolving triples, with mechanisms for entity similarity assessment and conflict resolution to ensure entity uniqueness and semantic consistency during evolution. 

The remainder of this paper is organized as follows. Section 2 reviews the related work. Section 3 introduces a top-down KG construction method for complex aviation assembly processes. Section 4 describes the ontology construction of the assembly process knowledge base for complex aviation products. Section 5 presents a multi-agentbased approach for triple information extraction. Section 6 provides the experimental results and corresponding analysis. Section 7 gives conclusions and future works. 

## 2. Related work

With the continuous increase in the complexity and knowledge intensity of aviation product assembly processes, the systematic modeling, automated acquisition, and dynamic evolution of assembly process knowledge have become prominent research topics in the fields of intelligent manufacturing and knowledge engineering. Focusing on the representation of assembly process knowledge and the construction of $\begin{array} { r } { \operatorname { K G } , } \end{array}$ researchers both domestically and internationally have conducted extensive studies, resulting in a variety of representative technical approaches. 

## 2.1. Assembly process knowledge representation and storage methods

In terms of assembly process knowledge representation, early studies mainly adopted rule-based and case-based approaches, in which assembly experience, process constraints, and operational rules were explicitly encoded in the form of if-then rules or case libraries to support assembly process decision-making and planning [16]. Gui et al. [17] proposed an integrated function-behavior-structure design object model, in which predicate logic and knowledge reasoning rules were embedded to automatically generate mechanical system assembly sequences, and successfully applied it to assemblability analysis and assembly planning of typical automotive mechanical products. Su et al. [18] developed an assembly sequence planning method based on case-based reasoning combined with genetic algorithms, where automatic assembly sequence generation was achieved through similar case retrieval and intelligent reasoning, significantly improving the efficiency and quality of assembly planning. However, when dealing with complex assembly relationships, multi-source heterogeneous knowledge, and dynamic evolution requirements, such approaches generally suffer from limited knowledge reusability and insufficient scalability. 

To enhance the level of knowledge structuring and semantic expressiveness, researchers gradually introduced ontology theory for modeling assembly process knowledge. Ontology-based methods achieve semantic normalization of assembly objects, assembly resources, process parameters, and constraint conditions by defining unified concept hierarchies, properties, and relationships, thereby providing fundamental support for cross-system knowledge sharing and reasoning [19–22]. Kang et al. [23] proposed an ontology-based modeling and reasoning-rule-driven method for manufacturing process selection and sequencing, which enables automatic reasoning, rational ordering, and cross-system reuse of manufacturing processes by jointly considering feature accuracy requirements and process capabilities. Qiao et al. [24] presented an ontology modeling and rule reasoning framework integrating geometric information for assembly sequence planning. By explicitly representing assembly semantics and combining ontology web language description logics and semantic web rule language reasoning mechanisms, the framework effectively supports intelligent decision-making for complex product assembly sequences. Owing to their advantages in process planning consistency, knowledge reusability, and interpretability, ontology-based assembly process knowledge models have been widely applied in aviation assembly and complex product manufacturing scenarios [15,25,26]. 

In recent years, with the rapid development of semantic web and big data technologies, KG have gradually become a mainstream approach for assembly process knowledge representation and storage [27,28]. By organizing assembly process knowledge in the form of triples, KG are capable of capturing complex relationships among assembly elements while supporting the integrated storage and updating of multi-source heterogeneous data [29]. Jiang et al. [30] proposed an automatic generation method for helicopter component assembly instructions. This method integrated $\operatorname { K G } ,$ assembly instruction reuse algorithms, and deep learning models, which effectively reduced the cost of instruction preparation and improved the intelligence level of assembly process design. Wu et al. [31] developed an intelligent manufacturing process instruction generation method that integrates $\operatorname { K G } ,$ large-scale pre-- trained language models, and multiple reasoning mechanisms, significantly enhancing the accuracy and automation of process element identification and process parameter decision-making, thereby providing an effective solution for intelligent process planning in manufacturing. 

## 2.2. Triple information extraction

Research on triple information extraction for KG construction has undergone a remarkable evolution, transitioning from manual ruledriven approaches to data-driven methods, and more recently to pretrained LLM-driven paradigms [32]. Early studies primarily relied on domain experts to manually design rules or templates for matching and extracting entities and relations from structured or semi-structured texts [33,34]. Heist et al. [35] proposed a descriptive rule mining approach that derives extraction rules from list contexts to identify relationships between list topic entities and their surrounding contexts. Wang et al. [36] constructed domain-specific rules to reduce noise in entity relations and facilitate the extraction of latent relations. Gotti et al. [37] introduced a rule acquisition method for open information extraction, in which rules are learned based on token sequence patterns connecting two named entities within a sentence. Although such methods achieve high precision in documents with well-defined formats and fixed terminology, they typically suffer from high manual costs, limited portability, and poor adaptability to complex natural language expressions. 

With the advancement of statistical learning, researchers introduced machine learning models to enable automatic entity and relation extraction through feature engineering. Kumar et al. [38] employed a BiLSTM-CRF model to identify entities from manufacturing science literature and achieved high accuracy. Guo et al. [39] developed a BERT-BiLSTM-CRF framework for automatic knowledge extraction from process-related texts, significantly outperforming traditional sequence labeling models. Guan et al. [40] proposed triple extraction algorithms based on BiLSTM with attention and CR-CNN models, achieving competitive macro-averaged performance. Salman et al. [41] introduced an enhanced Doc-KG model that leverages syntactic information to accurately extract triples from unstructured text, demonstrating strong performance in both triple extraction and KG completion tasks. 

Pre-trained language models such as BERT and T5, which acquire general semantic representations through large-scale corpus training, have been widely adopted for fine-tuning in downstream KG construction tasks. These approaches typically define target tasks-such as named entity recognition, relation classification, and triple classification—and fine-tune pre-trained models on annotated datasets to improve their adaptability to specific domains or tasks [42,43]. Lin et al. [44] proposed a multi-layer KG completion model integrating KG-BERT, graph attention networks, which significantly enhanced the completion performance of KG in the high-speed railway turnout equipment domain, providing effective support for railway operation, maintenance, and preventive decision-making. Zhang et al. [45] developed a domain KG-based modeling and extraction framework for power systems by combining BERT-BiLSTM-CRF and BERT-BiLSTM-Attention models to extract entities and relations. Meng et al. [46] proposed an entity and relation extraction model integrating BERT, BiLSTM, and CRF, enabling high-precision triple extraction from Chinese power equipment fault literature and the construction of power equipment fault KG, thereby improving KG quality and supporting intelligent fault diagnosis and question-answering applications. 

With the rapid advancement of large generative language models such as GPT, an increasing number of studies have explored direct triple generation from text, bypassing traditional extractors and extensive data annotation pipelines. Unlike fine-tuning-based methods, LLMs can perform entity and relation identification through prompt engineering, few-shot learning, or zero-shot learning, and directly output normalized triples [47–49]. Li et al. [50] proposed a rapid KG construction method for relay protection operation and management based on prompt engineering and LLMs, which efficiently extracts key information from unstructured texts, significantly reducing construction time while maintaining high accuracy, thus supporting intelligent power grid operation and decision-making. Guo et al. [51] presented an LLM-driven KG construction framework integrating prompt engineering and few-shot learning, achieving high-precision entity and relation extraction with low manual cost and improving the efficiency and reliability of knowledge base construction in task-oriented semantic communication systems. Gu et al. [52] proposed a KG construction method for customer service business processes based on multimodal LLMs and prompt-guided extraction, enabling automatic recognition and knowledge extraction of natural gas customer service workflows, thereby providing high-quality knowledge support for intelligent customer service systems and effectively enhancing service efficiency, intelligence, and standardization. Ma et al. [53] proposed a hybrid aerospace process planning KG construction method that integrates LLMs and small language model (SLM). By leveraging multi-agent pre-annotation and high-quality dataset training, the method achieves high-precision extraction of process knowledge and has been successfully applied in intelligent process planning for commercial aircraft manufacturing. Xu et al. [54] presented an LLM-driven machining process KG construction approach. Through an LLM-based pre-- annotation and validation mechanism, the method significantly reduces manual annotation costs and accelerates construction efficiency, and its comprehensive advantages in performance, time, and cost have been validated in enterprise-level process planning applications. Tang et al. [55] proposed a collaborative relation extraction framework, SLCoLM, which combines SLMs and LLMs. By adopting a “train–guide–predict” strategy, the framework effectively alleviates the long-tail data problem in relation extraction and significantly improves extraction performance for few-shot and long-tail relation types. Xu et al. [56] developed a hybrid named entity recognition (NER) method that integrates LLMs and SLM. By lightly fine-tuning the LLMs and introducing its guidance capability in low-confidence scenarios, the approach effectively improves overall performance on Chinese NER tasks, particularly in complex contexts and for unseen entities. 

Han et al. [57] proposed a time-aware retrieval-augmented generation method, TG-RAG, which constructs a dual-layer temporal graph structure to support temporal knowledge modeling, incremental updates, and temporal subgraph retrieval, thereby significantly enhancing the ability of RAG systems to handle dynamically evolving knowledge. Garijo et al. [58] introduced the UpSHACL method, which enables efficient SHACL constraint validation in dynamic update scenarios by identifying update-affected subgraphs and performing localized validation. He et al. [59] proposed a KG update method that combines deep learning, graph convolutional networks, and zero-shot learning. By incorporating semantic embeddings and unknown class detection, the method improves the iterative update capability and generalization performance of KG in the construction domain. Wang et al. [60] proposed the AIR framework, which achieves efficient updates and quality maintenance of dynamic KG embeddings by adaptively selecting important triples affected by new knowledge events and integrating embedding propagation techniques. Zhang et al. [61] proposed a dynamically updated process KG construction method for CAPP. By integrating knowledge representations from design and manufacturing data with a learning–forgetting model, the method enables continuous KG evolution and improves process design efficiency and accuracy. 

## 2.3. Literature summary

Although existing studies have made significant progress in knowledge management and triple information extraction, several limitations remain in the domain of complex aviation assembly processes: 

(1) Most existing research adopts ontology-based approaches to semantically model assembly objects, process resources, and constraints, achieving certain effectiveness in process planning consistency and knowledge sharing. However, the majority of these works focus on a single level or local process elements, and systematic modeling of cross-level and multi-type knowledge associations in complex aviation assembly is still insufficient. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/b4c27fe057088d3fa2974dc2feb2a237aa165fc181e7688c42b093aac7371f62.jpg)



Fig. 1. Overall Workflow of Aviation Assembly Process Design.


(2) LLMs are capable of performing entity recognition and relation identification under zero-shot or few-shot settings, substantially reducing the cost of manual annotation and demonstrating strong domain adaptability. Nevertheless, their generative processes are inherently stochastic, leading to insufficient stability in reasoning paths and output results, which in turn affects the consistency and reliability of triple extraction outcomes. 

(3) With respect to the continuous evolution of assembly process knowledge, existing studies pay limited attention to dynamic KG updating, entity uniqueness identification, and relation conflict resolution. There is a lack of unified evolution modeling and consistency maintenance mechanisms, making it difficult to ensure the semantic consistency and usability of KG during longterm updates. 

To address the above issues, this paper proposes a top-down construction method for KG of complex aviation assembly processes. First, a multi-level assembly process knowledge ontology is established. Then, an LLM-based multi-agent approach for triple information extraction is proposed, in which a self-consistency-aware CoT construction strategy is introduced to improve the accuracy and stability of triple extraction. Finally, a semantic embedding-based KG update strategy is adopted to enable and validate the dynamic evolution of the KG. 

## 3. Top-down assembly process KG construction framework for complex aviation products

The assembly process design of complex aviation products spans the entire lifecycle of product design, process preparation, and development-oriented production, and its specific workflow is illustrated in Fig. 1. During the product design stage, process planners work collaboratively with product designers to make key process decisions—such as assembly datums, assembly compensation strategies, and positioning methods-in accordance with assembly accuracy requirements, functional requirements of components, and interchangeability constraints. In the process preparation stage, process engineers compile a large number of assembly process documents based on the process schemes determined during the design stage. During the development and production stage, these process documents are revised according to trial manufacturing and assembly implementation feedback. Meanwhile, by introducing new processes and equipment, assembly efficiency and overall process capability are continuously improved. 

By first constructing a unified and standardized domain ontology and conceptual system, the semantic consistency and professional correctness of knowledge can be effectively ensured, enabling a clear representation of multi-level and strongly coupled knowledge structures in complex domains. Meanwhile, this approach provides stable semantic constraints for multi-source heterogeneous data integration, incremental knowledge updating, and long-term knowledge evolution. It also facilitates the integration of rule-based reasoning and expert experience, thereby supporting highly reliable and interpretable knowledge services and decision-making. 

The top-down framework for assembly process KG construction of complex aviation products, along with its key contributions, is illustrated in Fig. 2. Specifically, (a) depicts the data sources of the assembly process knowledge base, including forward-driven domain knowledge and backward-driven update knowledge. (b) illustrates the hierarchical structure of the knowledge base and their relationships, comprising the process knowledge layer, component information layer, equipment and resource layer, assembly process decision rules layer, and historical case layer, as well as the inter-layer associations. (c) represents the knowledge update mechanism. (d) shows the LLM-based triple information extraction module. (e) presents the assembly process knowledge base constructed using Neo4j. and (f) illustrates the application layer of the knowledge base, including knowledge-based question answering, knowledge management, and process information reasoning. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/950d91f51da0f7844189004d680b5b5db0e6ca2d032f31ffe73d6fa18e347eb5.jpg)



Fig. 2. Top-Down KG Construction Method.


The construction workflow of the knowledge base mainly consists of the following steps: 

Step 1: Analyze knowledge in the aviation product assembly domain to identify entity attributes and inter-entity relationships, and construct a multi-level assembly process knowledge base ontology using Prot´eg´e. 

Step 2: Extract 〈head entity, relation, tail entity〉 triples from existing domain knowledge using LLMs, and instantiate the assembly process KG ontology. The assembly process KG is then constructed using Neo4j. 

Step 3: For dynamic process knowledge such as new materials, new equipment, personnel feedback, and measurement data, update the assembly process knowledge base through a knowledge updating mechanism to ensure its timeliness. 

Step 4: Based on the constructed assembly process knowledge base, enable assembly knowledge management, process information reasoning, and process-oriented question answering. 

## 4. Ontology construction of the assembly process KG for complex aviation products

This section elaborates on the ontology construction details of the Aviation Product Assembly Process Knowledge Base (APAPKB) from three aspects: entities, relations, and attributes. The APAPKB consists of the product information layer, process knowledge layer, tool equipment resource layer, historical case layer, and assembly process decision rule layer. Accordingly, the APAPKB can be formally represented as: 

$$
A P A P K B = P I L \cup P K L \cup E R L \cup H C L \cup K H R \tag {1}
$$

Where PIL denotes the Product Information Layer, PKL represents the Process Knowledge Layer, ERL refers to the Tool Equipment Resource Layer, HCL denotes the Historical Case Layer, and KHR represents the Assembly Process Decision Rules. The associative relationships among different layers illustrated in Fig. 3 and summarized in Table 1. 

## 4.1. Product information knowledge layer construction

The product information knowledge layer provides a detailed description of the structural information, geometric positioning information, performance requirements, production characteristics, and product annotation information of complex aviation products. It serves as an essential data input for knowledge-driven assembly process planning of complex aviation products and can be represented as follows: 

$$
P I L = (E, R, A) \tag {2}
$$

where, $E , R ,$ A denote the sets of entities, relations, and attributes in the product information layer respectively. 

## 4.1.1. Construction of Entities and Attributes in the Product Information Layer

The organizational structure of entities and attributes in the product information layer is illustrated in Fig. 4. The hierarchical structure of an aviation product is typically represented in a product-assemblycomponent-part manner. In addition to basic attributes such as name, identification code, and type, assemblies and components also contain functional requirements, accuracy requirements, and interchangeability requirements. Functional requirements mainly describe constraints related to weight, center of gravity, cleanliness, sealing performance, contact resistance, and surface protection. Accuracy requirements include aerodynamic contour accuracy, relative positional accuracy, positional accuracy of internal structural components, and fitting accuracy between structural components. Interchangeability requirements cover in-plant interchangeability, inter-factory interchangeability, and international interchangeability. Parts, besides basic information such as name and identification code, further include attributes such as geometric configuration, general notes, technical specifications, heat treatment, surface protection, material, hole diameter, and thickness. These attributes play an important role in subsequent machining tool selection and process decision-making. In addition, the production nature attribute indicates whether the product is in the development stage or in mass production. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/e4947425d43ceeb0ff6c965664386ecff6d26bf4ea40c7082716cd79761497ce.jpg)



Fig. 3. Relationships among different knowledge layers.



Table 1 Meaning of inter-layer relationships.


<table><tr><td>Layer</td><td>Layer</td><td>Relation</td></tr><tr><td>PIL</td><td>KHR</td><td>Product information layer provides data inputs for the assembly process decision-making layer.</td></tr><tr><td>PIL</td><td>ERL</td><td>Product information layer provides data inputs for the tool and equipment resource layer.</td></tr><tr><td>PIL</td><td>HCL</td><td>Historical case layer stores historical product information.</td></tr><tr><td>KHR</td><td>PKL</td><td>Assembly process decision-making layer selects assembly process methods based on product information.</td></tr><tr><td>KHR</td><td>ERL</td><td>Assembly process decision-making layer selects tools and equipment based on product information.</td></tr><tr><td>KHR</td><td>HCL</td><td>Historical case layer stores historical decision-making results.</td></tr><tr><td>PKL</td><td>ERL</td><td>Assembly process knowledge layer provides the types of tools and equipment required by specific process methods.</td></tr><tr><td>PKL</td><td>HCL</td><td>Historical case layer stores typical assembly process knowledge.</td></tr><tr><td>ERL</td><td>HCL</td><td>Historical case layer records historical information on tool and equipment resources.</td></tr></table>

4.1.2. Construction of relationships in the product information layer In addition to the hierarchical structure of product-assemblycomponent-part, the relationships in the product information layer also include assembly constraint relationships among components in complex aviation products. These relationships are used to explicitly describe the structural dependencies and assembly constraints between different components. The main relationship types include contain, priority, datum, and aggregation, as summarized in Table 2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/7a5b61d727fdb3cf62a6925d7353c12a2f38adedf79094808ad0f4a0a9324963.jpg)



Fig. 4. Product information layer ontology.



Table 2 Relationships in the product information layer.


<table><tr><td>Number</td><td>Head entity</td><td>Relationship</td><td>Tail entity</td></tr><tr><td>1</td><td>Product</td><td>Contain</td><td>Assembly</td></tr><tr><td>2</td><td>Assembly</td><td>Contain</td><td>Component</td></tr><tr><td>3</td><td>Component</td><td>Contain</td><td>Part</td></tr><tr><td>4</td><td>Component</td><td>Priority</td><td>Component</td></tr><tr><td></td><td>Part</td><td></td><td>Part</td></tr><tr><td>5</td><td>Assembly</td><td>Priority</td><td>Assembly</td></tr><tr><td>6</td><td>Component</td><td>Datum</td><td>Component</td></tr><tr><td></td><td>Part</td><td></td><td>Part</td></tr><tr><td>7</td><td>Assembly</td><td>Datum</td><td>Assembly</td></tr><tr><td>8</td><td>Component</td><td>Aggregation</td><td>Component</td></tr><tr><td></td><td>Part</td><td></td><td>Part</td></tr><tr><td>9</td><td>Assembly</td><td>Aggregation</td><td>Assembly</td></tr></table>

In Table 2, the contain relationship represents the hierarchical containment structure among product-assembly-component-part. The priority relationship describes the assembly sequence precedence among components during the assembly process. For example, components that need to be positioned on fixtures at the initial stage of assembly are assigned the highest priority. If component A provides structural support for component B, or if B has a coaxiality requirement with respect to A, then component A should be assembled prior to component B. In addition, the assembly of complex aviation products generally follows fundamental principles such as frame-before-beam, inside-before-outside, and bottom-before-top. The aggregation relationship denotes a group of homogeneous parts that are installed together but do not form a closed spatial structure after assembly. The datum relationship represents the assembly locating datum between components. If component A serves as the assembly datum for component B, the relationship can be expressed as A→datum→B. 

## 4.2. Process knowledge layer construction

The process knowledge layer of complex aviation product assembly includes assembly process decision knowledge involved in the process planning stage, such as positioning methods, assembly datums, and assembly compensation. The process knowledge layer can be represented as follows: 

$$
P K L = (E, R, A) \tag {3}
$$

where E, R, A denote the sets of entities, relations, and attributes in the process knowledge layer, respectively. 

## 4.2.1. Construction of entity attributes in the process knowledge layer

The entities and attributes of the process knowledge layer are illustrated in Fig. 5. Assembly process knowledge can be classified into rulebased decision knowledge and heuristic experiential knowledge. Rulebased knowledge refers to process knowledge that can be explicitly selected once specific conditions are satisfied, such as positioning method selection and assembly datum selection. In contrast, heuristic knowledge is mainly derived from expert experience and is difficult to describe exhaustively using explicit rules. For example, assembly sequence planning commonly follows principles such as inside before outside and bottom before top. The process knowledge base also contains management-related metadata, including the name, model, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/6792587c20968da157123e36656b23fcbcbec9cc8674721a071ca3e7e2e47c32.jpg)



Fig. 5. Process knowledge layer ontology.



Table 3 Relationships in the process knowledge layer.


<table><tr><td>Number</td><td>Head entity</td><td>Relationship</td><td>Tail entity</td></tr><tr><td>1</td><td>Process Knowledge Base</td><td>Has</td><td>Rule-based Process KnowledgeEmpirical Process Knowledge</td></tr><tr><td>2</td><td>Rule-based Process Knowledge</td><td>Has</td><td>Benchmark Knowledge Assembly Compensation KnowledgePositioning Knowledge Connective knowledge</td></tr><tr><td>3</td><td>Empirical Process Knowledge</td><td>Has</td><td>Sequence Planning KnowledgeJoint Knowledge</td></tr></table>

version, administrator, modification time, data volume, and data source. Specific process knowledge is described in terms of its name, selection basis, selection principles, and application scope, among which the selection basis, selection principles, and application scope constitute the primary criteria for deciding whether a given process method should be adopted. These data are mainly derived from the product information layer. 

## 4.2.2. Construction of relationships in the process knowledge layer

The internal relationships of the assembly process knowledge layer for complex aviation products are presented in Table 3. 

## 4.3. Construction of the tool equipment resource layer

The tool and equipment resource layer stores all information related to tools, fixtures, and equipment used during the assembly stage of complex aviation products. It serves as an important information source for the preparation of assembly process instructions. By matching component information with tool and equipment data, optimal tools and equipment for assembly operations can be determined. The tool equipment resource layer can be represented as follows: 

$$
P K L = (E, R, A) \tag {4}
$$

where E, R, A denote the sets of entities, relations, and attributes in the tool equipment resource layer, respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/b80baf262274fa050d3462e1e5bf6a46266c942e23dcdc9e95eda5318cd6e280.jpg)



Fig. 6. Tool Equipment Resource Layer Ontology.



Table 4 Relationships in the Tool Equipment Resource Layer.


<table><tr><td>Number</td><td>Head entity</td><td>Relationship</td><td>Tail entity</td></tr><tr><td>1</td><td>Assembly Resource</td><td>Has</td><td>Connected Device, Sealing Equipment, Measuring Equipment, Tooling Equipment.</td></tr><tr><td>2</td><td>Connected Device</td><td>Has</td><td>Bit Tool, Riveting Gun, Drilling Tool, Screw Connection Tool.</td></tr><tr><td>3</td><td>Sealing Equipment</td><td>Has</td><td>Deburring Tool, Glue Gun.</td></tr><tr><td>4</td><td>Measuring Equipment</td><td>Has</td><td>Fixed Force Tool, Weight Measurement tool, Roughness Measurement tool, Aperture Measurement tool, Angle Measurement tool.</td></tr></table>

## 4.3.1. Construction of entity attributes in the tool equipment resource layer

The entities and attributes of the tool equipment resource layer are illustrated in Fig. 6. This layer includes fastening equipment, sealing equipment, measurement equipment, and tooling and fixture equipment. Each piece of equipment is described by a set of attributes such as name, model, and application scope. For example, a riveting gun is characterized by attributes including model, diameter, operating pressure, impact frequency, impact energy, and weight. 

## 4.3.2. Construction of Relationships in the Tool Equipment Resource Layer

The relationships within the tool and equipment resource layer are presented in Table 4. 

## 4.4. Construction of the Historical Case Layer

The historical case layer stores assembly process documents of aviation products that have already been developed and manufactured. For derivative or improved aviation models, rapid assembly process planning can be achieved by reusing the assembly processes of the original models. In addition, the historical case layer can be used to verify the accuracy of the assembly process knowledge base, thereby ensuring its validity and reliability. The historical case layer can be represented as follows: 

$$
P K L = (E, R, A) \tag {5}
$$

where E, R, A denote the sets of entities, relations, and attributes in the historical case layer, respectively. 

## 4.4.1. Construction of entity attributes in the historical case layer

The entities and attributes in the historical case layer include typical component assembly schemes and historical case schemes. Typical component assembly schemes describe the assembly process plans for representative components, such as planar components, singlecurvature panels, and double-curvature panels. Historical case schemes record assembly operation instructions and the corresponding assembly process documents.(Fig. 7). 

## 4.5. Construction of the assembly process decision rule layer

The different layers of the assembly process knowledge base are interconnected through complex semantic relationships. To enable interpretable and traceable logical reasoning for tasks in the assembly domain of complex aviation products, a graph rule-based reasoning (GRBR) construction method using KG is proposed. This method realizes the formal embedding of logical rules into a KG and supports efficient and interpretable graph-based reasoning. 

Traditional RBR rules can be formally expressed as: 

$$
R _ {i}: \text { IF } \underset {k = 1} {\overset {m} {\wedge}} C _ {i k} \text { THENA } _ {i} (w _ {i}) \tag {6}
$$

whereRidenotes thei − thrule,Cikrepresents thek − thcondition in the rule antecedent,Aidenotes the conclusion inferred by the rule, andω ∈ [0, 1]is the confidence of the rule. 

To transform the above rule structure into a graph-based 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/e9a14842c0b7d5673c3f90905a5e6950f3627e588d7e299a1a0251e647199e49.jpg)



Fig. 7. Historical Case Layer Ontology.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/42f5f89dfc89cbd61d3dfd0500e3a513ed09f82b2f6527cec8cb7b21b98c6d0b.jpg)



Fig. 8. Assembly process decision rule ontology.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/2ed5b4163a4d298683bbddf8165c4cfddbcaff0a4c0f65d5c8aeb76706d20c76.jpg)



Fig. 9. Application example of the assembly process decision rule layer.


representation, the following semantic mapping framework is adopted: Rule node: 

$$
R _ {i} \rightarrow : \text { Rule } (i d, \text { name }, \text { confidence } = \omega_ {i}) \tag {7}
$$

Antecedent pattern node: 

$$
P _ {i} = \left\{C _ {i 1}, C _ {i 2}, \dots , C _ {i m} \right\}\rightarrow : \text { Pattern } \tag {8}
$$

Condition node: each condition is represented in a structured form as 

$$
C _ {i k} = (s, p, o) _ {i k} \rightarrow : \text { Condition } (\text { subject } = s, \text { predicate } = p, \text { object } = o) \tag {9}
$$

Conclusion node: 

$$
A _ {i} = \left(s ^ {\prime}, p ^ {\prime}, o ^ {\prime}\right) _ {i} \rightarrow : \text { Conclusion } (\text { subject } = s ^ {\prime}, \text { predicate } = p ^ {\prime}, \text { object } = o ^ {\prime}) \tag {10}
$$

Accordingly, the logical implication relationship defined in Eq. (6) can be modeled as semantic relations in the $\operatorname { K G } ,$ as shown in Fig. 8. 

First, a rule ontology is constructed to describe concepts such as rules, patterns, conditions, and conclusions. Let the rule set be defined as： 

$$
R = \left\{R _ {1}, R _ {2}, \dots , R _ {n} \right\} \tag {11}
$$

Each ruleR is formalized as a triple-based structure: 

$$
R _ {i} = \left\langle P _ {\mathrm{i}}, C _ {\mathrm{i}}, A _ {\mathrm{i}} \right\rangle \tag {12}
$$

whereP denotes the antecedent pattern,C represents the set of conditions, andA denotes the conclusion or action. The definition of the rule ontology is illustrated in Fig. 9. 

## 5. LLM-based multi-agent triple information extraction

## 5.1. Problem description

The triple information extraction problem based on LLMs can be formulated as the following mathematical model. Given a text segmentT, an LLMs is employed to extract the following three categories of structured information: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/2a1144f663ae0bfe990ef3184e7b6461eb5306fb862affd00eddb99c63495533.jpg)



Fig. 10. Multi-agent triplet extraction.


a) Entity set $\boldsymbol \varepsilon = \{ \mathbf e _ { 1 } , \mathbf e _ { 2 } , \dots \}$ , where each entity consists of: 

➣ Name: a unique identifier of the entity; 

➣ Type: selected from the entity type set of the aviation assembly process knowledge ontology $\tau = \{ t _ { 1 } , t _ { 2 } , \dots \}$ },specified by the variable {entity_types}; 

➣ Attributes: attribute fields dynamically determined according to the entity type, drawn from the variable {entity_attributes}. 

b) Entity relationship set $\mathfrak { R } = \{ r _ { 1 } , r _ { 2 } , \ldots \}$ , selected from the predefined relationship type set specified by the variable {relationship_types}; 

c) Triple ${ \sf s e t } \vartheta = \big ( \{ e _ { i } = ( n a m e _ { i } , t y p e _ { i } , a _ { i } , c _ { i } ) \} , \{ ( e _ { i } , r _ { i j } , e _ { j } , s _ { i j } ) \} \big ) _ { : }$ , wherea denotes the entity attributes,c represents entity confidence, $\mathrm { a n d } s _ { i j } \in [ 0 ,$ 1]denotes relationship strength. 

## 5.2. Multi-agent collaborative information extraction method based on LLM

To address the challenges of knowledge extraction from complex aviation product assembly process texts, including high extraction difficulty, long semantic spans, and strongly implicit rules, a multi-agent collaborative triple extraction method based on LLMs is proposed. In this approach, the LLMs is encapsulated into multiple intelligent agents with distinct functional roles, enabling task decomposition, crossvalidation, and mutual supervision under a unified objective, thereby forming a high-precision and high-consistency knowledge extraction framework. The proposed method consists of three core agent groups: the document processing agent group, the information extraction agent group, and the knowledge fusion agent group. All agents are instantiated based on the same family of LLMs and achieve autonomous decisionmaking and collaborative reasoning through role prompting, chain-ofagents invocation, and an agent cooperation protocol. The overall multi-agent framework is illustrated in Fig. 10. The Central Control Agent (CCA) serves as the core scheduling and control unit of the multiagent framework, responsible for task interpretation, decomposition, and process management in assembly process knowledge extraction. Based on the type and structural characteristics of the input texts, the CCA decomposes the overall task into subtasks, including document preprocessing, information extraction, and knowledge fusion, and dispatches them to the document processing agent group, information extraction agent group, and conflict resolution agent according to predefined collaboration strategies. During execution, the CCA continuously monitors the status and intermediate outputs of each agent to ensure coordinated operation and global consistency. After structural parsing, semantic segmentation, and format normalization, the document processing agent group stores standardized intermediate results in the Knowledge Memory Agent (KMA), which are then forwarded by the CCA to the information extraction agents. These agents perform entity recognition, relation extraction, and candidate triple generation based on contextual semantics, and subsequently feed the results back to the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/75702ff3deb22d073eb6b718b2f50714217816a98a63d5921ee7c3da26d1ad84.jpg)



Fig. 11. KG update mechanism.


KMA. The CCA then aggregates multi-source outputs and forwards them to the conflict resolution agent to produce the final structured knowledge. The KMA acts as the unified memory and state management module of the system, responsible for storing and maintaining key information throughout the process. It records task instructions, intermediate reasoning results, confidence scores, and final triples. During collaboration, agents can access the KMA on demand to retrieve contextual states and historical records, thereby ensuring consistent memory support for verification and conflict resolution. 

## 5.2.1. Document preprocessing agent group

Let the raw document collection be defined as: 

$$
D = \left\{d _ {1}, d _ {2}, \dots , d _ {n} \right\} \tag {13}
$$

Each raw document D may contain various types of noise, such as disordered formatting, OCR errors, duplicated paragraphs, embedded tables or images, and mixed languages. The objective of the document cleaning agent is to transform the raw documents into structured, clean representations that can be directly used by downstream extraction modules. The document cleaning agent is defined as an LLM-driven function: 

$$
T = \mathrm{LLM} _ {\text { org }} (D | \theta , P _ {\text { org }}) \tag {14}
$$

where θ denotes the parameters of the LLM, and $P _ { o r g }$ represents the set of high-level instructions. 

The output text T is then processed by the document segmentation agent, which divides the document into a set of semantic units based on document structure and semantic similarity, while ensuring semantic coherence within each segment: 

$$
Y = \mathrm{LLM} _ {\text {seg}} (T | \theta , P _ {\text {seg}}) \tag {15}
$$

where θ denotes the LLM parameters and $P _ { s e g }$ represents the segmentation instruction set. 

Finally, the document summarization agent reads and summarizes the segmented text units to generate a document summary: 

$$
s _ {i} = \mathrm{LLM} _ {\text { sum }} (y _ {i} | \theta , P _ {\text { sum }}) \tag {16}
$$

where θ denotes the LLM parameters and $P _ { s u m }$ represents the document summarization instruction set. 

## 5.2.2. Information extraction agent group

Based on the document preprocessing agent group, the information extraction agents perform the extraction of entities, attributes, relationships, and rules from text segments. Rule knowledge is often implicitly embedded in long textual descriptions. The rule extraction agent identifies rule patterns through pattern reconstruction and logical analysis, as expressed in Eq. (17), 

$$
R _ {i} = \mathrm{LLM} _ {\text { rule }} (y _ {i}, s _ {i} | \theta , P _ {\text { rule }}) \tag {17}
$$

where $y _ { i }$ denotes the processed text segment, θ represents the parameters of the LLM, sidenotes the summary of the text segment, and $P _ { r u l e }$ represents the set of rule extraction instructions. 

The entity extraction agent leverages the semantic recognition capability of the LLM to extract a set of entities and their attributes from each text segment. In Eq. (18), 

$$
E (y _ {i}) = \mathrm{LLM} _ {\text {ent}} (y _ {i} | \theta , s _ {i}, P _ {\text {ent}}) \odot O _ {E} \tag {18}
$$

where $y _ { i }$ denotes the processed text segment, θ represents the LLM parameters, $s _ { i }$ denotes the text segment summary, $P _ { e n t }$ denotes the set of entity extraction instructions, and ⊙OE represents ontology-based entity filtering. Each entity is represented as $\boldsymbol { e } _ { i } = ( n a m e _ { i } , t y p \boldsymbol { e } _ { i } , a t t \boldsymbol { r } _ { i } )$ , where nameis the entity name, typeis the entity type, and attris the set of entity attributes: 

Based on the extracted entity set, the relationship extraction agent generates a set of relational triples by exploiting the LLM’s ability to locate textual evidence and analyze entity relationship semantics. In Eq. (19), 

$$
\mathrm{p} \left(\mathrm{r} \mid \mathrm{e} _ {\mathrm{i}}, \mathrm{e} _ {\mathrm{j}}, \mathrm{s} _ {\mathrm{j}}\right) = \mathrm{LLM} _ {\text { rel }} \left(\mathrm{e} _ {\mathrm{i}}, \mathrm{e} _ {\mathrm{j}}, \mathrm{s} _ {\mathrm{j}}, P _ {\text { rel }}\right) \odot O _ {R} \tag {19}
$$

where p(r|⋅) denotes the probability distribution over candidate relationships, $\odot O _ { R }$ represents ontology-based relationship filtering, and $P _ { r e l }$ denotes the set of relationship extraction instructions. The relationship with the highest probability is selected to form a triple. 

## 5.2.3. Conflict resolution agent

Newly extracted triples may conflict with previously stored triples. Let $t = ( e _ { h } , r , e _ { t } )$ denote an existing triple, and $\boldsymbol { t } ^ { \prime } = ( e _ { h } , r ^ { \prime } , e _ { t } )$ denote a newly extracted triple, whererand rʹare logically contradictory. The conflict relationship is defined as: 

$$
\operatorname{conflict} (t, G) = \left\{ \begin{array}{l l} 1 & , \quad \text { if } \exists t ^ {\prime} \text { that   contradictst } \\ 0 & , \quad \text { otherwise } \end{array} \right. \tag {20}
$$

The conflict resolution agent resolves such conflicts using conflict resolution prompt templates: 

$$
\mathrm{LLM} _ {C R A} (t, t ^ {\prime}) \rightarrow \{\text { Agree }, \text { Contradict } \} \tag {21}
$$

If the conflict resolution agent determines the relationship to be Contradict, the newly extracted triple tʹ is discarded or retained based on expert judgment, depending on the associated relationship confidence. 

## 5.2.4. KG update strategy based on semantic embeddings

To enable the dynamic evolution and continuous updating of assembly process knowledge for complex aviation products, an incremental KG update strategy is proposed. At time $t ,$ the KG is represented as a set of triples $G _ { \mathrm { t } } = \{ ( h , r , t ) \}$ }, where h,t ∈ εdenote the head entity and tail entity, respectively, andr ∈ ℜrepresents the relationship between entities. New knowledge from external data sources is introduced in the form of incremental triples $\Delta G _ { \mathrm { t + 1 } }$ , and the update process can be formally expressed as: 

$$
G _ {t + 1} = G _ {t} \otimes \Delta G _ {t + 1} \tag {22}
$$

where ⊗ denotes the KG update operation, including entity alignment, conflict resolution, and new knowledge insertion. The overall KG update strategy is illustrated in Fig. 11. The incremental update process of the assembly process KG begins by receiving new process knowledge input and converting it into entity–relationship–entity (triple) form through triple extraction. Subsequently, the system performs checks and processing on the extracted entities: if the entity ID already exists in the KG, conflict resolution is executed; if the ID does not match but the entity similarity exceeds a predefined threshold, entity alignment is performed; otherwise, the entity is added as a new node in the graph. Relationship information is updated directly according to the identifiers of new entities, or conflict resolution is applied when necessary. Throughout the entire process, all operations are recorded in an update log to ensure that the dynamic maintenance of the KG remains traceable and verifiable. 

For newly extracted triples, the update type is first determined. If the update corresponds to an entity attribute update, the attribute value is selected based on timestamps or confidence scores. If the update involves a relationship update, the conflict resolution procedure described in Section 4.2.3 is triggered to update the corresponding relational triple. If the update represents new knowledge insertion, the new triple is directly added to the KG. 

To achieve entity disambiguation, an entity similarity function sim(e, $e \prime )$ is defined. If the computed similarity exceeds a predefined threshold $\theta ,$ the incremental entity eʹ is considered equivalent to an existing entity e. The entity similarity function is defined as follows: 

$$
\operatorname{sim} \left(e, e ^ {\prime}\right) = \prod_ {i = 1} ^ {n} \operatorname{sim} _ {\text { num }} \left(v _ {1 i}, v _ {2 i}\right) \cdot \frac {1}{m} \sum_ {j = 1} ^ {m} \lambda_ {j} \operatorname{sim} _ {\text { text }} \left(v _ {1 j}, v _ {2 j}\right) \tag {23}
$$

$$
\operatorname{sim} _ {n u m} (v _ {1}, v _ {2}) = \left\{ \begin{array}{l} 1, i f (v _ {1} = v _ {2}) \\ 0, o t h e r w i s e \end{array} \right. \tag {24}
$$

$$
\operatorname{sim} _ {\text { text }} \left(v _ {1}, v _ {2}\right) = \frac {\mathrm{LLM} _ {\text { emb }} \left(v _ {1}\right) \cdot \mathrm{LLM} _ {\text { emb }} \left(v _ {2}\right)}{\left| \left| \mathrm{LLM} _ {\text { emb }} \left(v _ {1}\right) \right| \right| \cdot \left| \left| \mathrm{LLM} _ {\text { emb }} \left(v _ {2}\right) \right| \right|} \tag {25}
$$

## 5.3. CoT construction of LLM with self-consistency

To enhance the comprehension and reasoning capabilities of LLMs in the aviation manufacturing domain, and to improve the accuracy and stability of triplet information extraction, this study proposes a structured CoT construction method. This approach introduces elements such as Role, Goals, Workflow, OutputFormat, Variables, Constraints, and Examples to systematically constrain task definition, reasoning processes, and output formats. Specifically, Role defines the model’s identity and task boundaries; Goals adopt a result-oriented description to clarify the objectives to be achieved; Workflow decomposes complex tasks into a sequence of executable reasoning steps; OutputFormat enforces strict output structures, such as specifying JSON array formats and field naming conventions; Variables reserve dynamically fillable input parameters to enable reuse of the CoT; Constraints regulate model outputs through mandatory and prohibitive rules; and Examples provide sample outputs that conform to the required formats, which is particu larly beneficial for tasks with high demands on structural consistency. 

The prediction objective of a LLM is typically formulated as: 

$$
\widehat {\mathbf {y}} = \underset {y} {\operatorname{argmax}} \mathrm{LLM} _ {\theta} (y | x) \tag {26}
$$

where x denotes the input, θ represents the model parameters, y denotes the output, and $\widehat { \boldsymbol { y } }$ is the most probable output predicted by the model. 

After introducing the CoT technique, the model’s prediction objective becomes: 

$$
\widehat {\mathbf {y}} = \underset {y} {\operatorname{argmax}} \sum_ {z \in R} \mathrm{LLM} _ {\theta} (y, z | x) \tag {27}
$$

wherez $\mathbf { \xi } = ( z _ { 1 } , z _ { 2 } , \ldots , z _ { k } )$ denotes the reasoning path. The probability can be decomposed in a chain-wise manner as follows: 

$$
\operatorname{LLM} _ {\theta} (y, z | x) = \operatorname{LLM} _ {\theta} \left(z _ {1} | x\right) \times \prod_ {i = 2} ^ {k} \operatorname{LLM} _ {\theta} \left(z _ {i} \mid x, z _ {1: i - 1}\right) \times \operatorname{LLM} _ {\theta} (y \mid x, z _ {1: k}) \tag {28}
$$

When self-consistency is considered and multiple CoT are introduced, the model objective is further reformulated as: 

$$
\mathrm{LLM} _ {\theta} (y | x) = \sum_ {z} \mathrm{LLM} _ {\theta} (y | z, x) \cdot \mathrm{LLM} _ {\theta} (z | x) \tag {29}
$$

where z denotes a reasoning chain generated by the model, which may include processes such as task understanding and entity type identification, word-by-word or phrase-level reasoning, contextual verification, and final integration and output generation. $\mathbf { L L M } _ { \theta } ( z | x )$ represents the probability of generating the reasoning chain z given the input $x ,$ and $\mathbf { L L M } _ { \theta } ( y | z , x )$ denotes the probability of producing the final output conditioned on the reasoning chain z. Since a single input text may admit multiple plausible reasoning paths, relying on a single CoT is prone to randomness or local reasoning bias, thereby reducing the stability of the results. To address this issue, this study introduces a selfconsistency mechanism, whose core idea is to enhance reliability through multi-path reasoning. Specifically, given an input $x ,$ the model generates K reasoning chains ${ \mathfrak { z } } ^ { ( 1 ) } , { \mathfrak { z } } ^ { ( 2 ) } , . . . , { \mathfrak { z } } ^ { ( k ) }$ and each chain produces a corresponding output $y ^ { ( 1 ) } , y ^ { ( 2 ) } , . . . , y ^ { ( k ) }$ . Subsequently, a majority voting strategy is applied to select the final result, choosing either the most frequently occurring output or the one with the highest aggregated probability among the candidate outputs. By integrating multiple independent reasoning paths, the self-consistency mechanism effectively reduces random errors arising from single-pass generation and improves stability and robustness in complex semantic understanding and structured information extraction tasks. The construction of CoT reasoning with self-consistency for LLM is illustrated in Fig. 12. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/74eddaffac458bf61b744d62ddffd252a1630053587836a922104f2e6a4ad060.jpg)



Fig. 12. Schematic diagram of CoT construction of LLM with self-consistency.


$$
\widehat {y} = \operatorname{mod} \left\{y ^ {(1)}, y ^ {(2)}, \dots , y ^ {(k)} \right\} \tag {30}
$$

## 6. Case study

## 6.1. Experimental dataset and environment

## 6.1.1. Experimental dataset

To verify the effectiveness of the proposed KG construction method in the domain of complex aviation assembly processes, this study constructs an aviation product assembly process dataset. The dataset is collected from the real technical document repository of an aviation manufacturing enterprise. It contains approximately 61 assemblyrelated technical documents and two 3D models of product components, covering aviation manufacturing manuals, assembly process instructions, tool and equipment lists, and industry standards, and involving diverse types of assembly process knowledge. Overall, the dataset covers product structural information, process knowledge, and resource configuration information, and can comprehensively reflect the characteristics of complex aviation product assembly process knowledge. According to data structure characteristics, the experimental dataset can be divided into three categories. Sample experimental data are shown in Fig. 13, the detailed composition is listed in Table 5, and the distribution ratios of different data types are illustrated in Fig. 14. 

The preprocessing workflow of the experimental data is illustrated in Fig. 15. The workflow first receives user-input files and determines their types. If the input is a CATIA 3D model file, triple information is directly extracted based on the CATIA Application Architecture (CAA)framework. If the input corresponds to document-based data, its format is further identified: Word documents or other parsable files are directly converted into Markdown format, whereas scanned PDF files are first processed using OCR and then converted into Markdown format. The Markdown text is shown in Fig. 16, where the number of `#` symbols is used to distinguish section hierarchies, and tables in the text are converted into HTML-format tables to facilitate subsequent input to LLMs. Subsequently, the uniformly formatted text is fed into an LLM-based multi-agent triple information extraction module to complete knowl edge extraction and structured representation. Finally, triple information is generated as output, enabling unified processing and structured knowledge representation from multi-source heterogeneous data. 

CAA is the official secondary development framework provided by Dassault Syst`emes for the CATIA platform, which allows developers to access and manipulate 3D model data, assembly structures, and design parameters through standardized interfaces. By leveraging CAA interfaces, geometric feature retrieval, assembly relationship parsing, and automatic extraction of engineering data can be efficiently realized. Scanned PDF files refer to PDF documents generated from scanned images, which do not contain extractable text layers. In this study, scanned PDFs are processed using PDFelement for OCR recognition, while textbased PDF and Word files are converted into Markdown format using MinerU. 

To objectively evaluate the effectiveness and generalization capability of the proposed triple information extraction method, a validation dataset is constructed through manual annotation. To enhance annotation quality and consistency, a dual-annotator independent labeling strategy combined with cross-review is adopted. Samples with annotation discrepancies are resolved through expert discussions to reach a unified standard, and the annotation results are further normalized. Ultimately, a high-quality validation dataset is obtained to assess the model’s performance in entity recognition, relation extraction, and complete triple generation, providing a reliable benchmark for subsequent experimental comparisons and model optimization. 

## 6.1.2. Experimental environment

All experiments in this study were conducted under a unified software and hardware environment to ensure the fairness and reproducibility of the experimental results. The hardware configuration is as follows: an Intel Xeon Platinum 8352 V CPU @ 2.10 GHz, 512 GB of RAM, and four NVIDIA GeForce RTX 4090 GPUs. The evaluated models include Deepseek-r1 (1.5B, 7B, 14B, 32B, and 70B), Llama3.2 (1B and 3B), Llama3 (8B and 70B), Gemma3 (1B, 4B, 12B, and 27B), and Qwen3 (1.7B, 4B, 8B, 14B, 30B, and 32B). These open-source LLMs were deployed and invoked locally using the Ollama framework. In addition, GPT-4o and Deepseek-v3 were accessed via API-based inference, with UIUIAPI serving as the API proxy platform. The construction and management of the KG were implemented using Neo4j Desktop. 

## 6.2. KG ontology construction

The ontology model of the assembly process KG was constructed using the ontology development tool Prot´eg´e 5.6.4, as shown in Figs. 17 and 18. Prot´eg´e is an open-source ontology editing and knowledge modeling tool developed by Stanford University in the United States. It is widely used in the fields of knowledge representation, semantic 

4.4 Selection of Assembly Process References 

A reference (datum) refers to certain points,lines,or planes used to determine the relative positions of structural components. Product design requires the cstablishment of such references, such as the aireraft horizontal reference line,symmetry axis, wing chord plane, chord line, beam axis,longeronaxis, frame axis,ribaxis, etc.,collectively referred to as design datums. 

Design datums generally do not exist physically on the structure,and therefore cannot be directly used in production. Consequently, assembly process datums must be established during the assembly process. These are points,lines,or planes that exist on the structural components and can be used to determine their assembly positions. 

Abroad, a common practice is to mark design datums (which do not physically exist on the structure) onto the structure using markers. This method not only makes the datums usable during assembly but also ensures they can be preserved long-term. For example, the aireraft horizontal reference line and aircraft symmetry axis can be marked on the structure using this method. 

4.4.1 Classification of Assembly Process Datums 

(1) Classification by function 

1.Positioning datum: used to determine the relative position ofstructural components on equipment or tooling. 

2.Assembly datum: used to determine the relative positions between structural components. 

3.Measurement datum: usedasa starting point for measuring the positional dimensions of assembled components. 

Hybrid datum—K-hole: With the application of digital coordination technology, inorder to reduce accumulated errors,efforts are made to unify the positioning, assembly, and measurement datums. As a result, K-holes are widely used as shared datums in both part manufacturing and assembly processes. K-holes are jointly determined by process engineers and designers during the concurrent design phase of the aireraft and are explicitly defined in the product's mathematical model or manufacturing dataset (for datum holes on process tabs). 

(2)Two assemblydatums forensuring component shape accuracy 


(a)Aviation manufacturing engineering handbook


<table><tr><td rowspan="2" colspan="3"></td><td rowspan="2" colspan="3">(AO) Assembly Order (Universal)</td><td colspan="3">Order No.</td><td colspan="2">Issue</td></tr><tr><td colspan="3">FA0G-FC533G4300051</td><td colspan="2">F</td></tr><tr><td colspan="2">Process</td><td>75</td><td colspan="3">Process Name</td><td>Platform Plate Positioning</td><td colspan="2">Process Characteristic</td><td colspan="2">S</td></tr><tr><td rowspan="2"></td><td rowspan="2" colspan="5"></td><td colspan="5">Parts and Standard Parts</td></tr><tr><td colspan="5">cp, FC533G432201, Platform Plate, 1 pc</td></tr><tr><td rowspan="9" colspan="4"></td><td rowspan="9" colspan="2">(AO) Assembly Order (Universal)</td><td colspan="3">Order No.</td><td colspan="2">Issue</td></tr><tr><td rowspan="3" colspan="3">FA0G-FC533G4300051</td><td rowspan="3" colspan="2">F</td></tr><tr></tr><tr></tr><tr><td colspan="2">Assembly of Long Chord and Platform via Assembly Holes</td><td>Process Characteristic</td><td colspan="2">S</td></tr><tr><td colspan="5">Parts and Standard Parts</td></tr><tr><td colspan="5"></td></tr><tr><td colspan="5"></td></tr><tr><td colspan="5"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>


(b)Assembly process instructions


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/d51baa8640d507c62661685c75383c6b4bee07b83467a4f24b0f0f0576cd5f75.jpg)



(c) Mid-fuselage central section 3D model



Fig. 13. Example screenshot of the experimental dataset.


modeling, and KG construction. The tool supports ontology creation based on Semantic Web standards such as OWL (Web Ontology Language), including the definition of classes and properties, relationship modeling, and the specification of reasoning rules, enabling researchers to build structured knowledge systems and facilitate knowledge sharing and reuse. 

6.3. KG triple information extraction experiments 

6.3.1. Experimental setup and evaluation metrics 

To comprehensively verify the effectiveness and stability of the proposed triple information extraction method in the domain of complex aviation assembly processes, a series of comparative experiments were designed from three progressive perspectives: baseline model capability, multi-agent collaboration mechanisms, and self-consistency CoT construction. The experiments are organized in a hierarchical manner. First, the baseline extraction capability of mainstream LLMs in the aviation assembly domain is evaluated. Next, the performance improvement brought by the multi-agent framework for triple extraction is verified. Finally, the impact of introducing a self-consistency CoT mechanism on extraction consistency and stability is analyzed. The specific experimental design is summarized in Table 6. 


Table 5 Raw experimental data.


<table><tr><td>Data Type</td><td>Document Name</td><td>Document Content</td><td>Data Scale</td></tr><tr><td rowspan="2">Structured Data</td><td>Product 3D Models</td><td>Store geometric structure information of assembly objects, part hierarchy relationships, assembly constraint relationships, and attribute information, providing basic data support for assembly process planning.</td><td>Include two product component 3D models, specifically the mid-fuselage section and the lower front fuselage structure of a certain helicopter model, containing 1159 parts.</td></tr><tr><td>Tool and Equipment Lists</td><td>Contain information on tools and equipment involved in assembly process planning in an aviation manufacturing enterprise, including equipment types, functional purposes, applicable processes, specification parameters, and usage constraints, supporting process planning and resource matching.</td><td>Specifically include four Excel tables: cutting tool list, tool list, fixture list, and reference document list, covering approximately 301 types of tools and equipment.</td></tr><tr><td>Semi-Structured Data</td><td>Historical Assembly Process Instructions</td><td>Store assembly process instructions for existing helicopter models, including operation names, operational steps and requirements, tools and fixtures, and reference documents, providing references for knowledge reuse.</td><td>Include 51 assembly process instruction documents for the mid-fuselage section of a certain helicopter model.</td></tr><tr><td rowspan="2">Unstructured Data</td><td>Aviation Manufacturing Engineering Handbook, Part II (Aircraft Component Assembly)</td><td>Provides detailed descriptions of aviation component assembly process knowledge, including assembly workflow and sequence planning, assembly coordination scheme design, selection of process datum and positioning methods, determination of assembly states, error compensation design, as well as the classification characteristics and selection criteria of riveting, bolting, and sealing technologies.</td><td>Specifically refers to Part II of the Aviation Manufacturing Manual (Aircraft Component Assembly), comprising five chapters.</td></tr><tr><td>Aviation Industry Standards (HB)</td><td>Systematically specify key process methods and technical requirements in the aircraft assembly domain, focusing on the process classification, applicable conditions, operating specifications, and quality standards of riveting, bolting, and sealing technologies, providing standardized guidance for process design.</td><td>Specifically include five industry standard documents covering riveting, bolting, and sealing technologies.</td></tr></table>

Precision, Recall, and F1-score are adopted as the evaluation metrics for triple information extraction performance. All metrics are calculated at the triple level, and their formulations are given as follows: 

$$
P r e c i s i o n = \frac {T P}{T P + F P} \tag {31}
$$

$$
\text { Recall } = \frac {T P}{T P + F N} \tag {32}
$$

$$
F 1 = \frac {2 \times \text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }} \tag {33}
$$

where TP denotes the number of triples correctly extracted by the model, FP denotes the number of incorrectly extracted triples, and FN denotes the number of ground-truth triples that were not successfully identified by the model. 

## 6.3.2. Experiments on triple information extraction based on LLMs

To systematically evaluate the performance differences among LLMs of varying scales and architectures in the task of triple information extraction for assembly process knowledge, this study conducts comparative experiments on the Deepseek-r1 series, Llama3 series, Gemma3 series, Qwen3 series, as well as large-scale models Deepseek-v3 and GPT-4o. A comprehensive analysis is carried out based on three evaluation metrics: Recall, Precision, and F1-score. In this experiment, all models adopt a single-agent architecture and utilize the same prompt template for triple information extraction, thereby eliminating the influence of prompt design and framework differences on the experimental results. An example of the prompt template is shown in the appendix. The comparative performance of different models under the single-model setting is presented in Table 7. 

## (1) Analysis of the Relationship Between Model Scale and Performance

The overall experimental results demonstrate a significant positive correlation between model scale and triple extraction performance. As shown in Fig. 19, as the number of parameters increases, all model series exhibit consistent improvements in Recall, Precision, and F1-score. Taking the Deepseek-R1 series as an example, the 1.5B model failed to effectively complete the triple extraction task (F1 = 0), indicating that small-scale models struggle to comprehend complex process-related semantic structures. When the parameter scale increased to 7B, 14B, and 32B, the F1-score improved from 0.154 to 0.580. Further scaling to 70B resulted in an F1-score of 0.664, demonstrating strong information extraction capability. A similar trend can be observed in the Gemma3 and Qwen3 series. For instance, as Gemma3 increased from 4B to 27B, the F1-score rose from 0.310 to 0.601; similarly, when Qwen3 expanded from 8B to 32B, the F1-score improved from 0.380 to 0.589. These results indicate that for triple extraction tasks involving complex domain knowledge and multi-layered semantic relationships, large-parameter models possess clear advantages, particularly in capturing long-range dependencies and implicit semantic structures. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/e2be6a4a2b293a4102886f1341a0543d173a68681e4c6cfe327ac4a85ce8f2cd.jpg)



Fig. 14. Dataset distribution.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/5eac8fbe66b18ec05fcc587d6cc5ea1699ac4cbc7d406dfea98c0d30d85c27ba.jpg)



Fig. 15. Data preprocessing workflow.


## (2) Performance Bottleneck of Small-Scale Models

It is noteworthy that most 1B–4B scale models (e.g., Llama3.2:1B, Gemma3:1B, Qwen3:1.7B) achieved zero Recall and 

Precision in the experiments, indicating that they failed to generate valid triples. This phenomenon can be attributed to several factors: insufficient parameter scale leading to limited semantic understanding of complex process texts; weak adherence to structured output formats; and inadequate domain knowledge or reasoning capability, making it difficult to accurately identify relationships between entities. These findings suggest that in industrial KG construction scenarios, ultra-small models exhibit significant limitations when directly applied to structured information extraction tasks. 

## (3) Horizontal Comparison of Different Model Architectures

Even under similar parameter scales, performance differences are observed across model architectures. Deepseek-R1 demonstrates relatively significant improvements in Recall at comparable parameter levels, indicating an advantage in relation discovery capability. The Qwen3 series achieves relatively high Precision (e.g., Qwen3:8B with Precision = 0.567), suggesting more conservative generation behavior with fewer incorrect relations. Llama3:70B shows stable performance, achieving an F1- score of 0.647, which is close to Deepseek-R1:70B (0.664), indicating that mainstream open-source models have developed strong structured extraction capabilities at large parameter scales. In addition, Gemma3 exhibits notable performance gains at medium scales (12B–27B), reflecting its potential advantages in structured tasks. 

## (4) Performance Analysis of Ultra-Large-Scale Models

Among all evaluated models, Deepseek-v3 and GPT-4o achieved the best performance, with F1-scores of 0.774 and 0.751, respectively, significantly outperforming other open-source models. This indicates that ultra-large-scale models possess stronger capabilities in complex semantic modeling, demonstrate higher stability and generalization in multi-entity and multi-relation structured extraction tasks, and achieve a better balance between Recall and Precision. Specifically, Deepseek-v3 achieves a Recall of 0.824, reflecting stronger coverage of potential triples, while GPT-4o maintains a more balanced trade-off between 

##4.4 Selectionof Assembly Process References 

###4.4.1Classification of Assembly Process Datums 

## Heading level

Megeyrsuent detgu. assembled components. 

4.Hybrid datum K-hole:With the application of digital coordination technology,in order to reduce accumulated errors，efforts are made to unify the positioning,assembly，and measurement datums. As a result， K-holes are widely used as shareddatums in both part manufacturing and assembly processes.K-holes are jointlydetermined by process engineers and designers during the concurrent design phaseof the aircraft and are explicitly defined in the products mathematical model ormanufacturing dataset (for datum holes on process tabs). 

(2) Two assembly datums for ensuring component shape accuracy 

To ensure the accuracy of component shapes, two types of assembly datums areused: 

skeleton-based datums and skin-based datums.A comparison of these twoassembly datums is shown inTable4-2. Table 

<table><tr><td>Category</td><td>skeleton-based Datum</td><td>skin-based Datum</td></ tr><tr><td>Structural Characteristics</td><td>Ribs,bulkheads，frames,and other skeletal components form an integrated structure with no external shims.</td><td>1.Ribs and bulkheads are composed of upper and lower halves，connected with overlapping shims. 

2.Wing surface components are generally separated at chord planes;upper and lower ribs are usually not connected. 

3.There are no shims between ribs，bulkheads， frames，and the skin.</td></tr><tr><td>Assembly Process</td><td>First position the skeleton, then attach the skin to the skeleton and press with force (P)，performing fitting between skin and skeleton.</td><td>1.Structure without shims:Position the skin according to the jig，install the half ribs under pressing force (Q), and fit with the skin,aligning upper and lower ribs. 

2.Structure with shims:Position the rib panel (or frame)，attach the skin using the jig with additional force to fit the panel, install shims to connect skin and rib panel (or frame). Shims can also be mounted on the wall panel to connect with ribs (or frames)after positioning </td></tr><tr><td>Assembly Error Accumulation</td><td>Assembly errors accumulate from inside tooutside",and errors are reflected in the component's external shape.</td><td>Assembly errors accumulate from outside to inside,and errors are eliminated through structural shims </td></tr><tr><td>Composition of Shape Errors</td><td>1.Shape errors of skeletal components. 2.Assembly errors of the skeleton. 

3.Skin thickness errors. 

4.Fit gaps between skin and skeleton, 

5.Deformation during assembly.</td><td>1. Shape errors of panels. 

2.Fit gaps between skin and panels. 

3.Deformation during assembly.</td></tr><tr><td>Features</td><td>Accumulated errors are reflected inthe component's external shape,reducing its accuracy.To improve the shape accuracy of the component，it is necessary to improve both the shape accuracy of the skeletal< td><td>Using shims can achieve higher shape accuracy of components.</td></tr><tr><td></ td><td>components and the accuracy of skeleton assembly and positioning.</td><td></td></ tr><tr><td>Applicable Scope</td><td>1.Components with lower shape accuracy requirements.2. Wing types with smaller height，not suitable for using structural shims.</td><td>Components 

2. Assembly datum: used to determine the relative positions between structuralcomponents. 

3. Measurement datum: used as a starting point for measuring the positionaldimensions of assembled components. 

4. Hybrid datum 一 K-hole: With the application of digital coordination technology,in order to reduceaccumulated errors, efforts are made to unify the positioning,assembly, and measurement datums. As aresult, K-holes are widely used as shareddatums in both part manufacturing and assembly processes. K-holes are jointlydetermined by process engineers and designers during the concurrent design phaseof theaircraft and are explicitly defined in the product's mathematical model ormanufacturing dataset (for datumholes on process tabs). (2) Two assembly datums for ensuring component shape accuracy To ensure theaccuracy of component shapes, two types of assembly datums areused: skeleton-based datums and skin-based datums. A comparison of these twoassembly datums is shown in Table 4-2. Table 4-2 Comparison ofthe Two Assembly Datums

<table><tr><td>Category</td><td>Skeleton-based Datum</td><td>Skin-based Datum</td></tr><tr><td>Structural Characteristics</td><td>Ribs, bulkheads, frames, and other skeletal components form an integrated structure with no external shims.</td><td>1. Ribs and bulkheads are composed of upper and lower halves, connected with overlapping shims. 2. Wing surface components are generally separated at chord planes; upper and lower ribs are usually not connected. 3. There are no shims between ribs, bulkheads, frames, and the skin.</td></tr><tr><td>Assembly Process</td><td>First position the skeleton, then attach the skin to the skeleton and press with force (P), performing fitting between skin and skeleton.</td><td>1. Structure without shims: Position the skin according to the jig, install the half ribs under pressing force (Q), and fit with the skin, aligning upper and lower ribs. 2. Structure with shims: Position the rib panel (or frame), attach the skin using the jig with additional force to fit the panel, install shims to connect skin and rib panel (or frame). Shims can also be mounted on the wall panel to connect with ribs (or frames) after positioning.</td></tr><tr><td>Assembly Error Accumulation</td><td>Assembly errors accumulate “from inside to outside”, and errors are reflected in the component&#x27;s external shape.</td><td>Assembly errors accumulate “from outside to inside”, and errors are eliminated through structural shims.</td></tr><tr><td>Composition of Shape Errors</td><td>1. Shape errors of skeletal components. 2. Assembly errors of the skeleton. 3. Skin thickness errors. 4. Fit gaps between skin and rib plate. 5. Deformation</td><td>1. Shape errors of panels. 2. Fit gaps between skin and panels. 3. Deformation during assembly.</td></tr></table>


Fig. 16. Example of markdown-formatted text.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/99780cfc4c10b9b75280cd2458f0229e08c29ccd369080adedb6442ea851fb62.jpg)



Entity Definition


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/89b552444be45f32855fd377a32c21e73111b09405e969732eef07d9db5b3216.jpg)



Relationship Definition


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/ea518f760b16baff52aaa558a3fc468bde4f22d6ee0e8c3c8e35fe9ceb0437ec.jpg)



Attribute Definition



Fig. 17. Entity attributes of the process KG.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/eb70f91f0e0ab4939324436f93fcdededb7ca6c5f369b842f83940595c246a5b.jpg)



Fig. 18. Ontological relationships of the process KG.


Precision and Recall. 

Building upon the aforementioned base model selection experiments, this study further introduces a multi-agent collaborative mech anism to Deepseek-r1:70B, Llama3:70B, Gemma3:27B, Qwen3:32B, Deepseek-v3, and GPT-4o, in order to validate the effectiveness of the proposed multi-agent framework for triple information extraction in the aviation assembly process domain. Specifically, the triple extraction procedure is decomposed into three stages: document preprocessing, information extraction, and knowledge fusion, each handled by agents with distinct functional roles. The prompt designs for each agent are provided in the Appendix. All agents collaborate under shared aviation assembly process ontology constraints. To evaluate the impact of the multi-agent collaboration mechanism on triple extraction performance, this study compares single-agent and multi-agent configurations under the same model backbone. Overall, the multi-agent architecture demonstrates consistent performance improvements across all evaluated models. Recall, Precision, and F1-score all show measurable gains compared to the single-agent setting, indicating that task decomposition, role specialization, and multi-round reasoning effectively enhance structured information extraction capability. For example, under the 


Table 6 Experimental design overview.


<table><tr><td>Experiment</td><td>Experimental Content</td><td>Experimental Objective</td></tr><tr><td>Experiment 1</td><td>Baseline LLMs selection</td><td>Compare the performance of mainstream LLMs on aviation assembly process triple extraction tasks and select the model with superior baseline extraction capability as the reference model for subsequent experiments</td></tr><tr><td>Experiment 2</td><td>Effectiveness of the multi-agent framework</td><td>Under the same base model, compare single-model extraction with multi-agent collaborative extraction to validate the improvement in precision and recall brought by the multi-agent framework</td></tr><tr><td>Experiment 3</td><td>Effectiveness of the self-consistency CoT</td><td>Introduce a self-consistency CoT mechanism on top of the multi-agent framework and verify its enhancement of stability and reliability in triple extraction through multi-path reasoning result consistency filtering</td></tr></table>


Table 7 Triple Extraction Performance of Different Models under the Single-Agent Setting.


<table><tr><td>Model</td><td>Size</td><td>Context</td><td>Recall</td><td>Precision</td><td>F1</td></tr><tr><td>Deepseek-r1:1.5b</td><td>1.1 GB</td><td>128 K</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Deepseek-r1:7b</td><td>4.7 GB</td><td>128 K</td><td>0.119</td><td>0.217</td><td>0.154</td></tr><tr><td>Deepseek-r1:14b</td><td>9.0 GB</td><td>128 K</td><td>0.381</td><td>0.642</td><td>0.478</td></tr><tr><td>Deepseek-r1:32b</td><td>20 GB</td><td>128 K</td><td>0.510</td><td>0.672</td><td>0.580</td></tr><tr><td>Deepseek-r1:70b</td><td>43 GB</td><td>128 K</td><td>0.705</td><td>0.627</td><td>0.664</td></tr><tr><td>Llama3.2:1b</td><td>1.3 GB</td><td>128 K</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Llama3.2:3b</td><td>2 GB</td><td>128 K</td><td>0.238</td><td>0.417</td><td>0.303</td></tr><tr><td>Llama3:8b</td><td>4.7 GB</td><td>8 K</td><td>0.400</td><td>0.348</td><td>0.372</td></tr><tr><td>Llama3:70b</td><td>40 GB</td><td>8 K</td><td>0.621</td><td>0.675</td><td>0.647</td></tr><tr><td>Gemma3:1b</td><td>815MB</td><td>32 K</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Gemma3:4b</td><td>3.3 GB</td><td>128 K</td><td>0.214</td><td>0.563</td><td>0.310</td></tr><tr><td>Gemma3:12b</td><td>8.1 GB</td><td>128 K</td><td>0.426</td><td>0.577</td><td>0.490</td></tr><tr><td>Gemma3:27b</td><td>17 GB</td><td>128 K</td><td>0.557</td><td>0.652</td><td>0.601</td></tr><tr><td>Qwen3:1.7b</td><td>1.4 GB</td><td>40 K</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Qwen3:4b</td><td>2.5 GB</td><td>256 K</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Qwen3:8b</td><td>5.2 GB</td><td>40 K</td><td>0.286</td><td>0.567</td><td>0.380</td></tr><tr><td>Qwen3:14b</td><td>9.3 GB</td><td>40 K</td><td>0.510</td><td>0.629</td><td>0.563</td></tr><tr><td>Qwen3:30b</td><td>19 GB</td><td>256 K</td><td>0.541</td><td>0.635</td><td>0.584</td></tr><tr><td>Qwen3:32b</td><td>20 GB</td><td>40 K</td><td>0.555</td><td>0.627</td><td>0.589</td></tr><tr><td>Deepseek-v3</td><td>404 GB</td><td>160 K</td><td>0.824</td><td>0.730</td><td>0.774</td></tr><tr><td>Gpt-4o</td><td></td><td>128k</td><td>0.801</td><td>0.706</td><td>0.751</td></tr></table>

multi-agent configuration, the F1-score of Deepseek-r1:70B increases from 0.664 to 0.703, Llama3:70B improves from 0.647 to 0.695, while Gemma3:27B and Qwen3:32B rise to 0.619 and 0.632, respectively. These results suggest that the multi-agent mechanism provides architecture-agnostic performance enhancement. From the perspective of metric variation, the improvement in Recall is particularly notable. Deepseek-v3 achieves an increase in Recall from 0.824 to 0.891, and GPT-4o improves from 0.801 to 0.869. This indicates that multi-agent collaboration is capable of uncovering more latent triple relationships and reducing omission rates. Meanwhile, Precision also improves concurrently, demonstrating that the incorporation of multi-role verification and feedback mechanisms does not sacrifice accuracy for higher recall, but rather enhances overall extraction quality. In summary, the multi-agent architecture strengthens the model’s ability to understand and validate complex semantic relationships through task specialization and interactive reasoning. It exhibits clear advantages in complex domain knowledge extraction tasks, with more pronounced improvements observed in large-scale models. These findings validate the effectiveness and scalability of the proposed multi-agent approach for automated KG construction.(Table 8). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/8dbb853fa3152a57e679d822680d0310f5b2743397c67374121d104a6bf85ad8.jpg)



Fig. 19. Scaling Trends of Model Size and Performance.


## 6.3.3. Effectiveness experiment of self-consistency CoT construction

To verify the effectiveness of the self-consistency CoT mechanism in triple information extraction, this study introduces multiple reasoning paths and a consistency voting strategy on top of the multi-agent collaborative framework. Specifically, for the same input assembly process text, 1, 3, and 5 reasoning chains are generated (denoted as CoT-1, CoT-3, and CoT-5), respectively. The extraction results corresponding to multiple reasoning chains are then filtered through a consistency selection mechanism to obtain the final set of triples. To comprehensively evaluate the impact of the self-consistency mechanism on extraction performance and stability, comparative experiments are conducted on Deepseek-r1:70B, Llama3:70B, Gemma3:27B, Qwen3:32B, Deepseek-v3, and GPT-4o. The F1-score is adopted as the evaluation metric, and box plots are used to illustrate the performance distribution under different numbers of reasoning chains, as shown in Fig. 20. 

The experimental results demonstrate that as the number of reasoning chains increases, both the overall performance and stability of triple extraction improve significantly. For Deepseek-v3, the F1 distribution under the CoT-1 setting exhibits noticeable dispersion and fluctuation. When the number of reasoning chains increases to three, the median and upper quartile of F1 rise substantially, and the distribution range becomes more concentrated. Under the CoT-5 setting, the overall F1 further improves and shows the smallest dispersion, indicating that the self-consistency filtering mechanism effectively suppresses the randomness introduced by single-pass inference. A similar trend is observed for GPT-4o. Compared with CoT-1, both CoT-3 and CoT-5 show an upward shift in overall F1 distribution, while the occurrence of extremely low values is significantly reduced, demonstrating that multi-chain consistency voting effectively filters unstable or sporadic erroneous extraction results. Deepseek-r1:70B and Llama3:70B also exhibit clear performance improvements, although the magnitude is slightly smaller than that of ultra-large models, suggesting a synergistic relationship between model scale and reasoning capability—larger models can more effectively leverage the CoT reasoning mechanism. For medium-scale models such as Gemma3:27B and Qwen3:32B, the introduction of CoT also leads to steady improvements, particularly from CoT-1 to CoT-3, indicating that multi-step reasoning partially compensates for limitations in semantic understanding caused by smaller parameter scales. Although numerical distributions vary across models, the overall trend remains consistent, validating the general applicability of the self-consistency CoT mechanism across different LLMs. 


Table 8 Performance Comparison between Single-Agent and Multi-Agent Settings.


<table><tr><td>Model Configuration</td><td>Recall</td><td>Precision</td><td>F1</td></tr><tr><td>Deepseek-r1:70b(Single Agent)</td><td>0.705</td><td>0.627</td><td>0.664</td></tr><tr><td>Deepseek-r1:70b(Multi-Agent)</td><td>0.754</td><td>0.658</td><td>0.703</td></tr><tr><td>Llama3:70b(Single Agent)</td><td>0.621</td><td>0.675</td><td>0.647</td></tr><tr><td>Llama3:70b(Multi-Agent)</td><td>0.689</td><td>0.701</td><td>0.695</td></tr><tr><td>Gemma3:27b(Single Agent)</td><td>0.557</td><td>0.652</td><td>0.601</td></tr><tr><td>Gemma3:27b(Multi-Agent)</td><td>0.589</td><td>0.6532</td><td>0.619</td></tr><tr><td>Qwen3:32b(Single Agent)</td><td>0.555</td><td>0.627</td><td>0.589</td></tr><tr><td>Qwen3:32b (Multi-Agent)</td><td>0.613</td><td>0.652</td><td>0.632</td></tr><tr><td>Deepseek-v3(Single Agent)</td><td>0.824</td><td>0.73</td><td>0.774</td></tr><tr><td>Deepseek-v3(Multi-Agent)</td><td>0.891</td><td>0.797</td><td>0.841</td></tr><tr><td>Gpt-4o(Single Agent)</td><td>0.801</td><td>0.706</td><td>0.751</td></tr><tr><td>Gpt-4o(Multi-Agent)</td><td>0.869</td><td>0.774</td><td>0.819</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/0f6c36f0daecf7f28c02804153204f80cd48c5e1149446cdb095d1a5dd8fd490.jpg)



Fig. 20. Distribution of triple extraction performance under different numbers of chains of thought.



Table 9 Comparison of KG Update Methods.


<table><tr><td>Method</td><td>Update Logic</td></tr><tr><td>Full-Rebuild</td><td>Rebuilds the entire KG from scratch at each time slice</td></tr><tr><td>No-Alignment</td><td>Introduces new entities directly without performing entity similarity computation</td></tr><tr><td>No-Conflict</td><td>Does not perform relation conflict resolution</td></tr><tr><td>Similarity-Merge</td><td>Align entities based on string similarity</td></tr><tr><td>Ours</td><td>Complete incremental update method</td></tr></table>

From a mechanism perspective, the self-consistency CoT strategy introduces multiple independent reasoning paths and selects results based on cross-path agreement, ensuring that final triples are more likely to originate from consistent judgments across different reasoning trajectories. This “multi-path generation–consistency constraint” 

approach effectively reduces the impact of occasional misjudgments in single reasoning chains. It is particularly beneficial for complex aviation assembly process texts, where it enhances accuracy and stability while maintaining high recall. In summary, the self-consistency CoT mechanism further strengthens the robustness of triple extraction within the multi-agent collaborative framework, providing an effective means of improving stability in KG construction for complex engineering domains. 

BERT-BiLSTM-CRF is a classical deep learning architecture widely applied in named entity recognition (NER) and triple information extraction tasks. By combining pretrained language models with sequence labeling structures, it effectively models domain-specific texts such as assembly process documents and aviation manufacturing knowledge. Therefore, to comprehensively evaluate the performance of the proposed method in assembly process knowledge extraction, this study adopts BERT-BiLSTM-CRF as a traditional supervised learning baseline for comparison. As shown in the figure, the extraction performance of BERT-BiLSTM-CRF, indicated by the red dashed line, serves as the baseline. The performance distributions of Deepseek-v3 and GPT-4o under different CoT settings consistently lie above the baseline. Among them, CoT-5 achieves the best results, with both the median and mean F1-scores significantly exceeding those of BERT-BiLSTM-CRF, and with a more concentrated box distribution, indicating not only improved overall extraction performance but also enhanced stability. In contrast, other models, constrained by parameter scale and reasoning capacity, perform slightly below the best models but still demonstrate gradual improvement as CoT depth increases. Furthermore, unlike BERT-BiLSTM-CRF, which requires large amounts of annotated data for supervised training, the proposed method achieves competitive performance without relying on extensive domain-specific fine-tuning. This highlights the strong generalization capability and practical advantages of LLMs in complex domain knowledge extraction tasks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/a1491facc0687cee935b67757144a1f0c8b1edcb87ea4961a7af8f56cf2bec28.jpg)



Fig. 21. Impact of threshold on update accuracy.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/8f4f74f85737b93486ef107f58bbd0baca5f37136118dfece133bdf36e9f0a1a.jpg)



Fig. 22. Comparison of update performance across different methods.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/c4cc51d6647aa6b351c1ea15fc05b445a8d8b21891fd5d2f5ab3bf9f32b8e1e4.jpg)



Fig. 23. Overall construction results of the KG.


## 6.4. Dynamic KG updating

## 6.4.1. Experimental setup and evaluation metrics

To verify the effectiveness of the proposed incremental KG updating method based on entity alignment and conflict resolution, a series of experiments were designed and implemented on the Neo4j graph database platform. The KG was initialized using the triples extracted in Section 5.2, comprising approximately 3552 entities and 5674 relations. To simulate the dynamic evolution of the KG, three batches of incremental triple sets were constructed, containing 2530, 1820, and 1324 triples, respectively. The comparative experimental settings are summarized as follows:(Table 9). 

The experimental evaluation metric adopts triple update accuracy $A c c _ { u p d a t e } ,$ , and its calculation formula is given as follows: 

$$
A c c _ {u p d a t e} = \frac {\left| G _ {t + 1} ^ {p r e d} \cap G _ {t + 1} ^ {g t} \right|}{\left| G _ {t + 1} ^ {g t} \right|} \tag {34}
$$

The metric $A c c _ { u p d a t e }$ measures the degree of consistency between the KG $G _ { \mathrm { t + 1 } } ^ { \mathrm { p r e d } }$ obtained at time slice t +1 through the incremental update operation ⊙ and the manually annotated ground-truth KG $G _ { { \mathrm { t } } + 1 } ^ { g t }$ . To evaluate the impact of the entity similarity threshold 

θ on the performance of the proposed incremental update method, a threshold sensitivity experiment was further conducted. On the validation set, θ was varied across a given range with a step size of 0.01, and the changes in performance metrics under different threshold values were calculated. This allowed for an analysis of the model’s sensitivity to the threshold parameter and its effect on the overall update performance. 

## 6.4.2. Experimental results and analysis

The variation of metric $A c c _ { u p d a t e }$ with respect to the entity similarity threshold θ is shown in the Fig. 21. The results indicate that θ has a significant impact on update performance and exhibits a clear phased trend: In the lower threshold range (θ<0.7), the average update accuracy is relatively low and highly volatile. This is primarily due to the loose similarity criterion, which causes semantically similar but actually distinct entities to be incorrectly merged, increasing the proportion of erroneous updates and reducing overall accuracy. As the threshold gradually increases to the medium range (0.7 ≤θ≤0.85), the update accuracy steadily rises, indicating that stricter similarity constraints effectively reduce mismatches and improve entity disambiguation quality. However, some boundary cases still exist, suggesting that the threshold has not yet reached the optimal balance. $\mathrm { A t } ~ \theta { = } 0 . 9 1$ , the accuracy reaches a peak of 0.916, showing an effective balance between the precision and coverage of entity matching. This avoids the erroneous merges associated with low thresholds while maintaining a high recall for correct matches. When the threshold is further increased, the 

## 4.5.1 Classification and Characteristics of Positioning Methods

In aircraft assembly, commonly used positioning methods mainly include the layout marking method, datum-based positioning, assembly-hole positioning, and asembly frame positioning, each of which has distinct characteristics and applicable scenarios. 

The layout marking method determines the position of components through techniques such as scribing with general measuring tools, the use of dedicated templates, or photo-exposed gelatin layout lines. This method is simple and easy to implement and requires relatively low tooling costs; however, it offers limited assembly accuracy and low efficiency. It is typically applied during the new aircraft development stage or for assemblies with low accuracy requirements, and it may also serve as an auxiliary means in combination with other positioning methods. 

The datum-based positioning method relies on existing points, lines, and surfaces on the product structure to locate the components to be assembled. It features simple operation and good coordination, but places high demands on the stiffness and accuracy of the datum components.This method is mainly used for the assembly of parts with mating relationships or identical geometries. 

The assembly-hole positioning method achieves positioning by means of pre-manufactured corresponding holes in the connected components. It enables rapid positioning and requires relatively simple tooling, with accuracy lying between that of layout marking and jig-based positioning. This method is suitable for the assembly positioning of single-curvature or smoothly double-curvature panels, internal stiffeners, and planar assemblies. 

The assembly frame positioning method uses dedicated jigs to determine the position of components, providing high positioning accuracy, effectively controlling assembly deformation,and ensuring interchangeability and coordination. However, it requires a relatively long production preparation cycle. This method is widely applied to various structural components with high assembly accuracy requirements. 


Fig. 24. Background knowledge of aviation assembly positioning methods.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/4a0816013ce0f9f3f7efc6cd455171a08588a1188e871a8745a2da2c9df363ea.jpg)



Fig. 25. KG construction results with ontology constraints.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/be2e93c4b4b0c5ddae2194057e8e0b71fc76ae964cde3c7d079982460d282c3c.jpg)



Fig. 26. KG construction results without ontology constraints.


accuracy begins to decline. This is because overly strict similarity constraints prevent some genuinely identical entities from being recognized as matches, negatively affecting the KG update. 

The average update accuracy of different methods across consecutive time slices is shown in the Fig. 22. The results demonstrate that the choice of update strategy has a significant effect on performance: Full-Rebuild achieves the highest accuracy (0.922), indicating that full reconstruction can maximally avoid cumulative historical errors. However, this method requires reprocessing all data, incurring high computational cost and making it impractical for real-time incremental updates in actual aviation manufacturing scenarios. Its results therefore serve mainly as a reference upper bound. No-Alignment yields the lowest accuracy (0.841), showing that without entity similarity alignment, synonymous or variably expressed entities in incremental data are repeatedly created, leading to entity redundancy and fragmented relationships, which substantially reduces structural consistency. This underscores the necessity of an entity alignment module in dynamic updates. No-Conflict achieves 0.883, lower than the complete method, indicating that unhandled relationship conflicts during incremental updates directly affect knowledge consistency and reasoning reliability, highlighting the importance of the conflict resolution mechanism. Similarity-Merge (0.89) performs better than No-Alignment but remains lower than the proposed method, suggesting that relying solely on simple string similarity is insufficient to handle the complex semantic expressions typical in aviation manufacturing. The proposed Ours method achieves an average update accuracy of 0.916, approaching the performance upper bound of Full-Rebuild while significantly outperforming simplified strategies. This demonstrates that a KG update strategy based on semantic embeddings can maintain high accuracy while avoiding the computational cost of full reconstruction, achieving an effective balance between efficiency and performance. 

## 6.5. KG construction performance analysis

The overall construction performance of the KG is illustrated in Fig. 23. Text-based assembly process knowledge is automatically constructed using the triplet information extraction method proposed in this study. And the 3D model–related knowledge of the product is obtained through secondary development based on the CAA framework by parsing 3D models to extract the hierarchical structure of components and their associated relationships. 

Fig. 24 presents the original text segment from the background knowledge describing aircraft assembly positioning methods. This segment details the classification of positioning methods, the characteristics of each type, and the criteria for selecting them during actual assembly processes, serving as a critical knowledge source for positioning method selection in assembly process planning. Fig. 26 shows the KG constructed by directly applying the proposed multi-agent LLMbased triple extraction method to this text without introducing ontology constraints. As observed, the model extracted relations such as “USES_TECHNIQUE,” “AFFECTED_BY,” and “APPLICABLE_TO,” along with entities and attributes like “Internal Stiffeners,” “Operability,” and “Positioning_speed.” Although these extracted entities and relations carry some importance in the text, not all of them are practically necessary or directly applicable in production and assembly process operations. Some information appears only in the textual context and may be irrelevant to specific process workflows, operational guidance, or decision support. This can result in a knowledge base containing a large amount of redundant data. Redundant information not only increases the complexity of knowledge management and retrieval but can also introduce semantic confusion, leading to unclear entity type distinctions and relation semantics, ultimately reducing the accuracy and usability of the KG for subsequent process planning, intelligent reasoning, and decision support. Particularly in cross-level, complex assembly scenarios, unconstrained extraction results may fail to maintain hierarchical logic consistency and domain compliance, further diminishing the practical value of the knowledge representation. Fig. 25 illustrates the KG constructed with multi-level assembly process ontology constraints. The comparison shows that ontology constraints standardize entity types and relation semantics while providing clear guidance for hierarchical structure organization. This significantly reduces semantic redundancy and structural ambiguity, enhances the completeness and consistency of the KG, and ensures that the representation aligns more closely with domain cognition, making it more suitable for subsequent process planning, decision-making, and intelligent reasoning applications. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/fba7a75d3d59d13119eebd8f4f017e54571bf5a537aa2f366c2edac3e25ea2f2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-14/3cc9d61e-a330-46c8-b295-b9ba33aa2cbd/5ce3e815c6abe83447580eab08bf4a0c9de0f466af0049ba70f3d686f6617e2f.jpg)



Fig. 27. Construction results of the product information layer.


In addition, Fig. 27 presents the product information layer KG constructed from product 3D models. This layer takes components as the core entities and explicitly represents product structural hierarchies and assembly relationships, thereby providing a reliable data foundation for subsequent reasoning and association of assembly process knowledge. 

## 7. Conclusion

In view of the characteristics of complex aviation assembly process knowledge-such as diverse knowledge types, complex hierarchical structures, tight semantic correlations, and continuous knowledge evolution-this paper focuses on the systematic modeling, automatic acquisition, and dynamic updating of assembly process knowledge, and proposes a top-down construction method for KG of complex aviation assembly processes. First, starting from the business logic of assembly process planning and the requirements of knowledge organization, a multi-level assembly process knowledge ontology model is constructed. This model provides unified and standardized semantic representations of product information, assembly process knowledge, tools and equipment, historical cases, and their cross-level relationships, laying a solid foundation for the structured representation and semantic consistency of assembly process knowledge. Second, to address the semantic complexity and structural diversity of assembly process texts, a LLMbased multi-agent collaborative triple information extraction method is proposed. By incorporating domain ontology constraints, this approach effectively reduces semantic ambiguity and structural conflicts during the extraction process. Furthermore, to tackle the instability of reasoning paths in LLMs, a self-consistency–constrained CoT construction method is introduced. Through multi-path CoT generation and consistency evaluation mechanisms, the processes of entity recognition, relation determination, and triple construction are jointly constrained, significantly improving the stability, accuracy, and interpretability of triple extraction results. Finally, to meet the requirements of continuous evolution of assembly process knowledge, a semantic embedding–based dynamic KG update strategy is proposed. By integrating entity similarity assessment, relation conflict detection, and attribute disambiguation mechanisms, this strategy ensures entity uniqueness and semantic consistency of the KG during incremental updates. The experimental results demonstrate that, under the support of advanced large-scale models, the proposed method achieves an average F1-score of 92.74% in triple information extraction, representing an improvement of 13.1% over traditional deep learning approaches. In the KG update experiments, the proposed method attains an average update accuracy of 0.916, approaching the upper performance bound of the Full-Rebuild method 0.922. These results indicate that the proposed approach exhibits strong effectiveness and applicability in complex aviation assembly process scenarios. It provides reliable knowledge support for assembly process knowledge management, process planning decision-making, and intelligent reasoning applications. 

Although the proposed method has achieved certain results in the construction and application of KG for complex aviation assembly processes, several issues remain for further investigation and optimization. On the one hand, as the hierarchical structures and semantic relationships of assembly process knowledge become increasingly complex, ontology construction still largely relies on domain experts, posing significant challenges in terms of modeling efficiency and scalability. How to achieve automatic or semi-automatic construction of assembly process KG ontologies while ensuring semantic accuracy remains an open research problem. On the other hand, existing ontology structures are mainly defined by static specifications during knowledge updating and expansion, and do not sufficiently consider adaptive adjustments of the ontology structure when new processes, equipment, or rules are introduced. Future research may combine the conceptual abstraction capabilities of LLMs with structural learning methods to explore dynamic ontology evolution and continuous optimization mechanisms, thereby further enhancing the flexibility and sustainability of assembly process KG in long-term applications. 



[23] Kang M, Kim G, Lee T, Jung CH, Eum K, Park MW, et al. Selection and sequencing of machining processes for prismatic parts using process ontology model. Int J Precis Eng Manuf 2016;17:387–94. https://doi.org/10.1007/s12541-016-0048-2. 



## CRediT authorship contribution statement



[24] Qiao L, Qie Y, Zhu Z, Zhu Y, Zaman UKU, Anwer N. An ontology-based modelling and reasoning framework for assembly sequence planning. Int J Adv Manuf Technol 2018;94:4187–97. https://doi.org/10.1007/s00170-017-1077-4. 



Jun Pu: Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project admin istration, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Yu Guo: Supervision, Project administration, Methodology, Funding acquisition. Shaohua Huang: Supervision, Methodology, Funding acquisition, Formal analysis, Conceptualization. ChenXin Zhou: Writing – original draft, Visualization, Validation, Formal analysis. JiaJun Tian: Visualization, Software, Data curation. Lijun Ma: Writing – original draft, Visualization, Validation, Software. 



[25] He Y, Hao C, Wang Y, Li Y, Wang Y, Huang L, et al. An ontology-based method of knowledge modelling for remanufacturing process planning. J Clean Prod 2020; 258:120952. https://doi.org/10.1016/j.jclepro.2020.120952. 



## Declaration of Competing Interest



[26] Song D, Ye X, Wu W, Zhang Z, Saren Q, Qian J, et al. Ontology-based assembly knowledge representation and process file generation. MATEC Web Conf 2022; 355:02028. https://doi.org/10.1051/matecconf/202235502028. 



The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 



[27] Shen X, Li X, Zhou B, Jiang Y, Bao J. Dynamic knowledge modeling and fusion method for custom apparel production process based on knowledge graph. Adv Eng Inf 2023;55:101880. https://doi.org/10.1016/j.aei.2023.101880. 



## Acknowledgment



[28] Bao Q, Zheng P, Dai S. Hierarchical construction and application of machining domain knowledge graph based on as-fabricated information model. Adv Eng Inf 2024;62:102638. https://doi.org/10.1016/j.aei.2024.102638. 



This research was supported by National Key Science and Technology Projects (Grant No. 2025ZD1603000). 



[29] Guo L, Yan F, Lu Y, Zhou M, Yang T. An automatic machining process decisionmaking system based on knowledge graph. Int J Comput Integr Manuf 2021;34: 1348–69. https://doi.org/10.1080/0951192X.2021.1972461. 



## References



[30] Jiang M, Guo Y, Huang S, Pu J. Generating the assembly instructions of helicopter subassemblies using the hierarchical pruning strategy and large language model. J Ind Inf Integr 2024;42:100723. https://doi.org/10.1016/j.jii.2024.100723. 





[31] Wu T, Guo Y, Huang S, Fang W, Long Z, Qian W. Intelligent process instruction generation method: combining large-scale pre-trained language model and multireasoning. Appl Softw. Comput 2025;185:114038. https://doi.org/10.1016/j. asoc.2025.114038. 





[1] Liu Z, Liu J, Zhuang C, Wan F. Multi-objective complex product assembly scheduling problem considering parallel team and worker skills. J Manuf Syst 2022;63:454–70. https://doi.org/10.1016/j.jmsy.2022.05.003. 





[32] Goyal A, Gupta V, Kumar M. Recent named entity recognition and classification techniques: a systematic review. Comput Sci Rev 2018;29:21–43. https://doi.org/ 10.1016/j.cosrev.2018.06.001. 





[2] Xiao Y, Zheng S, Shi J, Du X, Hong J. Knowledge graph-based manufacturing process planning: a state-of-the-art review. J Manuf Syst 2023;70:417–35. https:// doi.org/10.1016/j.jmsy.2023.08.006. 





[33] Zhao X, Xing Z, Kabir MA, Sawada N, Li J, Lin S-W. HDSKG: Harvesting Domain Specific Knowledge Graph from Content of Webpages. In: Pinzger M, Bavota G, Marcus A, editors. Ieee 24th International Conference on Software Analysis, Evolution, and Reengineering (saner), 2017. New York: IEEE; 2017. p. 56–67. 





[3] Wang L, Keshavarzmanesh S, Feng H-Y, Buchal RO. Assembly process planning and its future in collaborative manufacturing: a review. Int J Adv Manuf Technol 2009; 41:132–44. https://doi.org/10.1007/s00170-008-1458-9. 





[34] Chen T, Lu Y, Xu T. Chinese Book Information Extraction Based on Bert and Rule Matching. In: Gan J, Pan Y, Zhou J, Liu D, Song X, Lu Z, editors. Computer Science and Educational Informatization, 1899. Singapore: Springer Nature Singapore; 2024. p. 65–75. https://doi.org/10.1007/978-981-99-9499-1_6. 





[4] Arista R, Mas F, Morales-Palma D, Vallellano C. Industrial resources in the design of reconfigurable manufacturing systems for aerospace: a systematic literature review. Comput Ind 2022;142:103719. https://doi.org/10.1016/j. compind.2022.103719. 





[35] Heist N, Paulheim H. Information Extraction From Co-Occurring Similar Entities. Proceedings of the World Wide Web Conference 2021 (www 2021). New York: Assoc Computing Machinery; 2021. p. 3999–4009. https://doi.org/10.1145/ 3442381.3449836. 





[5] Liu Q, Zhang H, Leng J, Chen X. Digital twin-driven rapid individualised designing of automated flow-shop manufacturing system. Int J Prod Res 2019;57:3903–19. https://doi.org/10.1080/00207543.2018.1471243. 





[36] Wang X, Li J, Zheng Z, Chang Y, Zhu M. Entity and relation extraction with ruleguided dictionary as domain knowledge. Front Eng Manag 2022;9:610–22. https:// doi.org/10.1007/s42524-022-0226-0. 





[6] Buergin J, Belkadi F, Hupays C, Gupta RK, Bitte F, Lanza G, et al. A modular-based approach for Just-In-Time Specification of customer orders in the aircraft manufacturing industry. CIRP J Manuf Sci Technol 2018;21:61–74. https://doi. org/10.1016/j.cirpj.2018.01.003. 





[37] Gotti F, Langlais P. Weakly supervised, data-driven acquisition of rules for open information extraction. In: Meurs MJ, Rudzicz F, editors. Advances in Artificial Intelligence, 11489. Cham: Springer International Publishing Ag; 2019. p. 16–28. https://doi.org/10.1007/978-3-030-18305-9_2. 





[7] Zhang X, Qiu K, Niu B, Chen L, Xi J. A sample average approximation approach for aircraft product configuration optimization with customer order uncertainty. Aerospace 2025;12:199. https://doi.org/10.3390/aerospace12030199. 





[38] Kumar A, Starly B. FabNER: information extraction from manufacturing process science domain literature using named entity recognition. J Intell Manuf 2022;33: 2393–407. https://doi.org/10.1007/s10845-021-01807-x. 





[8] Li J, Zhao G, Wei J, Hu Z, Zhang W, Zhang P. Assembly simulation and optimization method for underconstrained frame structures of aerospace vehicles. Aerospace 2024;11:689. https://doi.org/10.3390/aerospace11080689. 





[39] Guo L, Yan F, Li T, Yang T, Lu Y. An automatic method for constructing machining process knowledge base from knowledge graph. Robot Comput-Integr Manuf 2022; 73:102222. https://doi.org/10.1016/j.rcim.2021.102222. 





[9] Sun H, Zhao J, Zheng Z, Jiang Y, Jin X, Deng S, et al. A review of the deformation mechanism and control of low stiffness thin-walled parts. CIRP J Manuf Sci Technol 2025;60:322–55. https://doi.org/10.1016/j.cirpj.2025.05.007. 





[40] Guan K, Du L, Yang X. Relationship extraction and processing for knowledge graph of welding manufacturing. IEEE Access 2022;10:103089–98. https://doi.org/ 10.1109/ACCESS.2022.3209066. 





[10] Zhang X, Meng S, Wang B, Zheng L, Zhang R, Li X. Integrated assembly, measurement, and adjustment method of reconfigurable flexible fixture for aircraft panels based on augmented reality and human-computer interaction. J Manuf Syst 2025;79:117–33. https://doi.org/10.1016/j.jmsy.2025.01.003. 





[41] Salman M, Haller A, Mendez SJR, Naseem U. Doc-KG: unstructured documents to knowledge graph construction, identification and validation with Wikidata. Expert Syst 2024;41. https://doi.org/10.1111/exsy.13617. 





[11] Zhao G, Shi J, Xu W, Sun N, Zeng J, Yang G, et al. A study on the failure behavior and force transmission of composite skin-stringer structures under a compressive load. Materials 2025;18:1380. https://doi.org/10.3390/ma18061380. 





[42] Shi X, Tian X, Ma L, Wu X, Gu J. A knowledge graph-based structured representation of assembly process planning combined with deep learning. Int J Adv Manuf Technol 2024;133:1807–21. https://doi.org/10.1007/s00170-024- 13785-4. 





[12] Papuga J, Stejskal J. Effect of some riveting process parameters on the fatigue life of double-shear lap joints. Eng Fail Anal 2022;134:106008. https://doi.org/ 10.1016/j.engfailanal.2021.106008. 





[43] He Z, Wang H, Zhang X. Multi-task learning model based on BERT and knowledge graph for aspect-based sentiment analysis. Electronics 2023;12:737. https://doi. org/10.3390/electronics12030737. 





[13] Korba P, Al-Rabeei S, Hovanec M, Sekelov I, Kale U. Structural design and material comparison for aircraft wing box beam panel. Heliyon 2024;10:e27403. https:// doi.org/10.1016/j.heliyon.2024.e27403. 





[14] Andolfatto L, Thiebaut F, Lartigue C, Douilly M. Quality- and cost-driven assembly technique selection and geometrical tolerance allocation for mechanical structure assembly. J Manuf Syst 2014;33:103–15. https://doi.org/10.1016/j. jmsy.2013.03.003. 





[44] Lin H, Bao J, Hu N, Zhao Z, Bai W, Li D. Knowledge graph completion for highspeed railway turnout switch machine maintenance based on the multi-level KBGC model. Actuators 2024;13:410. https://doi.org/10.3390/act13100410. 





[15] Zhu D, Zhang Z, Shi L, Qian J, Qimuge S, Song D. A hierarchical assembly knowledge representation framework and microdevice assembly ontology. Adv Eng Inf 2022;53:101705. https://doi.org/10.1016/j.aei.2022.101705. 





[45] Zhang B, Chen X, Ouyang Y, Gan Y, Lyu B, Liu H, et al. A construction Method of Knowledge Graph for Electric Power Field. 2022 5th International Conference on Advanced Electronic Materials, Computers and Software Engineering (AEMCSE). Wuhan, China: IEEE; 2022. p. 444–8. https://doi.org/10.1109/ AEMCSE55572.2022.00094. 





[16] Kumar SPL. Knowledge-based expert system in manufacturing planning: state-ofthe-art review. Int J Prod Res 2019;57:4766–90. https://doi.org/10.1080/ 00207543.2018.1424372. 





[46] Meng F, Yang S, Wang J, Xia L, Liu H. Creating knowledge graph of electric power equipment faults based on BERT-BiLSTM-CRF model. J Electr Eng Technol 2022; 17:2507–16. https://doi.org/10.1007/s42835-022-01032-3. 





[17] Gui JK. A function-behaviour-structure machine design model and its use in assembly sequence planning. J Eng Des 1990;1:239–59. https://doi.org/10.1080/ 09544829008901655. 





[47] Geng Y, Chen J, Zeng Y, Chen Z, Zhang W, Pan JZ, et al. Prompting disentangled embeddings for knowledge graph completion with pre-trained language model. Expert Syst Appl 2025;268:126175. https://doi.org/10.1016/j.eswa.2024.126175. 





[18] Su Q. Applying case-based reasoning in assembly sequence planning. Int J Prod Res 2007;45:29–47. https://doi.org/10.1080/00207540600632182. 





[48] Shi F, Chen L, Zhou M, Zhao Y. A stepwise intelligence generative method for structured maintenance guidance documents based on knowledge graph augmented LLM. Adv Eng Inf 2025;67:103523. https://doi.org/10.1016/j. aei.2025.103523. 





[19] Zhang Y, Luo X, Zhang H, Sutherland JW. A knowledge representation for unit manufacturing processes. Int J Adv Manuf Technol 2014;73:1011–31. https://doi. org/10.1007/s00170-014-5864-x. 





[49] Ma Y, Zheng S, Yang Z, Zheng P, Leng J, Hong J. Leveraging large language models in next generation intelligent manufacturing: retrospect and prospect. J Manuf Syst 2025;82:809–40. https://doi.org/10.1016/j.jmsy.2025.07.019. 





[20] Zhu B, Roy U. Ontology-based disassembly information system for enhancing disassembly planning and design. Int J Adv Manuf Technol 2015;78:1595–608. https://doi.org/10.1007/s00170-014-6704-8. 





[50] Li Y, Zheng M, Gu Y, Zhang M, Jiang W, Tang W, et al. A rapid construction method for a knowledge graph of relay protection operation management based on prompt engineering. 2025 6th International Conference on Artificial Intelligence and Electromechanical Automation (AIEA). Hefei, China: IEEE; 2025. p. 73–7. https:// doi.org/10.1109/AIEA66061.2025.11160578. 





[21] Guo L, Hu T, Dong L, Ma S. Ontology and production rules-based dynamic knowledge base construction methodology for machining process. J Manuf Syst 2024;77:1027–44. https://doi.org/10.1016/j.jmsy.2024.11.006. 





[51] Guo C, Liu J, Gao W, Lu Z, Li Y, Wang C, et al. A large language model driven knowledge graph construction scheme for semantic communication. Appl Sci-Basel 2025;15:4575. https://doi.org/10.3390/app15084575. 





[22] Leng J, Jiang P, Ding K. Implementing of a three-phase integrated decision support model for parts machining outsourcing. Int J Prod Res 2014;52:3614–36. https:// doi.org/10.1080/00207543.2013.879344. 





[52] Gu S., Qi Y. Knowledge graph construction method for business process instructed by prompts. In: Yue Y, editor. International Conference on Optics, Electronics, and Communication Engineering (OECE 2024), Wuhan, China: SPIE; 2024, p. 98. https ://doi.org/10.1117/12.3049117. 





[53] Ma Y, Zheng S, Yang Z, Zheng P, Leng J, Hong J. Aircraft assembly process planning based on knowledge graph constructed by integrating LLMs and SLMs. J Manuf Syst 2026;84:1–19. https://doi.org/10.1016/j.jmsy.2025.11.016. 





[54] Xu Q, Qiu F, Zhou G, Zhang C, Ding K, Chang F, et al. A large language modelenabled machining process knowledge graph construction method for intelligent process planning. Adv Eng Inform 2025;65:103244. https://doi.org/10.1016/j. aei.2025.103244. 





[55] Tang X, Wang J. Small language models as effective guides for large language models in chinese relation extraction. arXivOrg 2024. 〈https://arxiv.org/abs/ 2402.14373v2〉 (accessed February 4, 2026). 





[56] Xu W, Dang R, Huang S. LLM’s Weakness in NER Doesn’t Stop It from Enhancing a Stronger SLM. In: Anderson A, Gordin S, Li B, Liu Y, Passarotti MC, editors. Sprugnoli R, editors. Proceedings of the Second Workshop on Ancient Language Processing, The Albuquerque Convention Center. Laguna: Association for Computational Linguistics; 2025. p. 170–5. https://doi.org/10.18653/v1/2025. alp-1.21. 





[57] RAG Meets Temporal Graphs: Time-Sensitive Modeling and Retrieval for Evolving Knowledge-All Databases n.d. 〈https://www.webofscience.com/wos/alldb/full-rec ord/INSPEC:27517099〉 (accessed February 5, 2026). 





[58] Zacouris Z, Ke J, Acosta M. UpSHACL: Targeted Constraint Validation for Updates over Knowledge Graphs. In: Garijo D, Kirrane S, Salatino A, Shimizu C, Acosta M, Nuzzolese AG, et al., editors. The Semantic Web – ISWC 2025, 16140. Nature Switzerland: Cham: Springer; 2026. p. 122–39. https://doi.org/10.1007/978-3- 032-09527-5_7. 





[59] He L, Hu X. The application of GCN algorithm in Building Construction Knowledge Graph updating under the combination of artificial intelligence and knowledge management. Int J Cogn Comput Eng 2025;6:65–73. https://doi.org/10.1016/j. ijcce.2024.11.001. 





[60] Jia Z, Li H, Chen L. AIR: Adaptive incremental embedding updating for dynamic knowledge graphs. In: Wang X, Sapino ML, Han W-S, El Abbadi A, Dobbie G, Feng Z, et al., editors. Database Systems for Advanced Applications, 13944. Nature Switzerland: Cham: Springer; 2023. p. 606–21. https://doi.org/10.1007/978-3- 031-30672-3_41. 





[61] Zhang E, Zhang S-W, Jia J-L. A dynamically updatable knowledge graph construction method for computer-aided process planning and design. J Eng Des 2025;36:1551–84. https://doi.org/10.1080/09544828.2025.2450762. 

