architecture_rules = {
"Security": [
    {
        "article": "Article 15 – Accuracy, robustness and cybersecurity",
        "link": "https://artificialintelligenceact.eu/article/15/",
        "quote": (
            "High-risk AI systems shall be designed and developed in such a way, including with appropriate levels "
            "of accuracy, robustness and cybersecurity, that they achieve, in the light of their intended purpose, "
            "an appropriate level of accuracy, robustness and cybersecurity, and perform consistently for their "
            "intended purpose. They shall be resilient as regards errors, faults or inconsistencies that may occur "
            "within the system or due to interaction with natural persons or other systems. High-risk AI systems shall "
            "be protected against attempts by unauthorized third parties to alter their use, performance or functionality "
            "by exploiting the system vulnerabilities and against data poisoning. Appropriate measures shall be taken to "
            "prevent and control for those risks through technical redundancy, fail-safe and fallback plans."
        ),
        "advice": (
            "Implement a defense-in-depth architecture. Use strong authentication and authorization mechanisms to ensure "
            "only legitimate actors access the AI system. Validate and sanitize all inputs (e.g. user data, model inputs) "
            "to thwart data-poisoning or injection attacks. Encrypt sensitive data in transit and at rest to protect "
            "confidentiality. Incorporate continuous monitoring and intrusion detection, and maintain an audit trail of "
            "system access and actions. These measures collectively address the AI Act’s cybersecurity mandate (Art. 15) "
            "by hardening the system against unauthorized manipulation and ensuring integrity under attack."
        ),
        "tactics": [
            "Input Validation and Sanitization",
            "Role-Based Access Control (RBAC)",
            "Transport Layer Security (TLS)",
            "Audit Trail for Access Logs",
            "Intrusion Detection Systems (IDS)"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 27001:2022",
                "name": "Information security management systems – Requirements",
                "link": "https://www.iso.org/standard/27001.html",
                "clauses": "8.1–8.3 (operational planning, risk assessment & treatment); Annex A (controls A.5–A.18)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001.html",
                "clauses": "8.2 & 8.3 (AI risk assessment & treatment); Annex B.6 (AI life-cycle controls); Annex B.6 (implementation guidance)"
            },
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "8.2 (AI-specific security threats); 9.7 (reliability, resilience & robustness); 9.10 (testing & evaluation)"
            }
        ]
    }
],



"Availability": [
    {
        "article": "Article 9 – Risk management system",
        "link": "https://artificialintelligenceact.eu/article/9/",
        "quote": (
            "A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. "
            "It shall consist of a continuous, iterative process run throughout the entire lifecycle of a high-risk AI system, requiring regular "
            "systematic updating. That process shall ensure that the high-risk AI system performs consistently for its intended purpose and under "
            "reasonably foreseeable conditions of use, and shall include appropriate measures to identify, estimate, evaluate and handle risks."
        ),
        "advice": (
            "Design for fault tolerance and continuous operation. Apply redundancy tactics such as failover servers or replicated services so that if one "
            "component fails, a backup can seamlessly take over. Use active-passive redundancy (hot/warm spares) or load-balanced clusters to eliminate single "
            "points of failure. Include health monitoring and automatic restart/recovery mechanisms. In line with risk management best practices, plan for "
            "graceful degradation—if the AI system encounters a fault, it should continue providing partial service rather than shutting down."
        ),
        "tactics": [
            "Failover Clustering",
            "Active-Passive Redundancy",
            "Service Replication",
            "Health Monitoring",
            "Graceful Degradation"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "6.4–6.6 (risk assessment, treatment, monitoring); 6.7 (recording & reporting); Annex A.7 & A.10"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "8.2–8.3 (AI risk assessment & treatment); 9.1 (monitoring / measurement); Annex B.6 (AI system life cycle)"
            },
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.7 (reliability, resilience, robustness); 9.8 (mitigating hardware faults)"
            }
        ]
    },
    {
        "article": "Article 15 – Accuracy, robustness and cybersecurity",
        "link": "https://artificialintelligenceact.eu/article/15/",
        "quote": (
            "High-risk AI systems shall perform consistently for their intended purpose throughout their lifecycle. Appropriate levels of accuracy, robustness "
            "and cybersecurity shall be ensured, taking into account the generally acknowledged state of the art."
        ),
        "advice": (
            "Availability engineering should anticipate infrastructure-level failures and implement redundancy at data, compute, and network levels. "
            "Failover strategies and service replication help preserve functionality even when partial system failures occur."
        ),
        "tactics": [
            "Hot Standby",
            "Load Redistribution",
            "Latency Minimization",
            "Redundant Compute Nodes",
            "Network Partition Recovery"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.7 (reliability / resilience / robustness); 9.10 (testing & evaluation)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.5 (verification & validation); 8.7 (operation)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "9.1 (monitoring / measurement, analysis & evaluation); Annex B.6"
            }
        ]
    }
],


"Modifiability": [
    {
        "article": "Article 72 – Post-market monitoring system",
        "link": "https://artificialintelligenceact.eu/article/72/",
        "quote": (
            "Providers of high-risk AI systems shall establish a post-market monitoring system in a manner that is proportionate to the nature of the AI system and the risks it may pose. "
            "That system shall collect, document and analyse relevant data provided by users or collected through other sources on the performance of high-risk AI systems throughout their "
            "lifetime, and allow the provider to evaluate continuous compliance with the requirements set out in this Regulation."
        ),
        "advice": (
            "Enable easy adaptation and update of the system. Use a modular architecture where components are decoupled and communicate via stable interfaces, so changes "
            "in one module have minimal impact on others. For instance, separate data ingestion, model logic, and interface into distinct services. Employ information hiding: "
            "encapsulate details likely to change (e.g. model algorithms, data schemas) behind well-defined interfaces. Continuous delivery practices can be adopted to frequently "
            "deploy small improvements."
        ),
        "tactics": [
            "Service-Oriented Architecture",
            "Interface Abstraction",
            "Modular Decomposition",
            "Semantic Versioning",
            "Continuous Integration/Delivery (CI/CD)"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "8.4 (impact assessment); 9.1 (monitoring / measurement); 10.1 (continual improvement)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.7 (operation); 8.8 (example ML process)"
            },
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "6.6 (monitoring & review); 6.7 (recording & reporting)"
            }
        ]
    },
    {
        "article": "Article 73 – Reporting of serious incidents and of malfunctioning",
        "link": "https://artificialintelligenceact.eu/article/73/",
        "quote": (
            "Providers shall immediately report to the market surveillance authorities any serious incident or any malfunctioning of the high-risk AI system which constitutes a breach "
            "of obligations laid down in this Regulation or which poses significant harm to health, safety, or fundamental rights."
        ),
        "advice": (
            "Architectural flexibility is essential to support rapid hotfixes or system rollbacks. Implement built-in hooks for runtime patches and diagnostic interfaces for "
            "root-cause analysis. These enable prompt issue resolution and reduce time-to-repair when malfunctions occur."
        ),
        "tactics": [
            "Dynamic Reconfiguration",
            "Hot-Swapping Components",
            "Rollback Mechanisms",
            "Runtime Diagnostics",
            "Error Isolation Zones"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "10.2 (non-conformity & corrective action); 8.4 (impact assessment)"
            },
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.10 (testing & evaluation); 8.2 (AI-specific security threats)"
            },
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "6.6 (monitoring & review); 6.7 (recording & reporting)"
            }
        ]
    }
],

"Transparency": [
    {
        "article": "Article 13 – Transparency and provision of information to users",
        "link": "https://artificialintelligenceact.eu/article/13/",
        "quote": (
            "High-risk AI systems shall be designed and developed in such a way to ensure that their operation is sufficiently transparent "
            "to enable users to interpret the system’s output and use it appropriately. Instructions for use shall include concise and clear "
            "information that is relevant, accessible and comprehensible to users."
        ),
        "advice": (
            "Embed explainability and disclosure mechanisms into the system. Integrate explainable AI (XAI) components that can provide understandable justifications for "
            "the model’s outputs. For example, use model-agnostic explainers (LIME, SHAP) or built-in feature importance metrics to generate user-facing explanations for "
            "predictions. Provide an “AI Factsheet” or help section that describes the system’s purpose, limitations, and performance to fulfill instruction requirements."
        ),
        "tactics": [
            "Model-Agnostic Explanation APIs",
            "Feature Attribution Visualizations",
            "Public AI Factsheets",
            "Contextual Help UIs",
            "Explanation Logging"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 22989:2022",
                "name": "Artificial intelligence concepts and terminology",
                "link": "https://www.iso.org/standard/74296.html",
                "clauses": "3 (terms & definitions); 5 (AI concepts); 6 (AI life cycle)"
            },
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.2 (transparency); 9.3 (explainability); 9.4 (controllability)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "7.4 (communication); Annex B.8 (information for interested parties)"
            }
        ]
    },
    {
        "article": "Article 50 – Transparency obligations for certain AI systems",
        "link": "https://artificialintelligenceact.eu/article/50/",
        "quote": (
            "Providers shall ensure that AI systems intended to interact with natural persons are designed and developed in such a way that natural persons "
            "are informed that they are interacting with an AI system, unless this is obvious from the context or circumstances. The information shall be "
            "provided at the latest at the time of the first interaction and in a clear and distinguishable manner."
        ),
        "advice": (
            "Ensure the UI includes informational cues that the user is interacting with an AI—e.g. a label or icon indicating AI assistance. "
            "Use visual, auditory, or textual cues to disclose AI presence, and log these disclosures for auditability."
        ),
        "tactics": [
            "AI Disclosure Labels",
            "Voice/Visual AI Cues",
            "System Prompts for Interaction",
            "Disclosure Logging",
            "Branding AI Functionality"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.2 (transparency); 9.3 (explainability)"
            },
            {
                "title": "ISO/IEC TR 24368:2022",
                "name": "Ethical and societal concerns in AI",
                "link": "https://www.iso.org/standard/78507.html",
                "clauses": "7.1 (aligning processes to AI principles); 8.2 (ethical & societal considerations)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "8.4 (impact assessment); 7.4 (communication)"
            }
        ]
    }
],


"Auditability": [
    {
        "article": "Article 12 – Record-keeping",
        "link": "https://artificialintelligenceact.eu/article/12/",
        "quote": (
            "High-risk AI systems shall be designed and developed with capabilities enabling the automatic recording of events ('logs') while the system is operating. "
            "The logging capability shall be appropriate to the intended purpose of the AI system and shall ensure a level of traceability of the AI system’s functioning throughout its lifecycle."
        ),
        "advice": (
            "Build in robust logging and compliance documentation. Establish a comprehensive logging subsystem that automatically records key events: inputs received, decisions made by the AI, "
            "user actions, overrides, and any anomalies. Logs should be tamper-evident (append-only and timestamped). Maintain up-to-date technical documentation (technical file as per Annex IV) "
            "recording the model version, training data, and validation results."
        ),
        "tactics": [
            "Event Sourcing Pattern",
            "Tamper-Proof Log Stores",
            "Secure Time-Stamped Logs",
            "Automated Technical File Generator",
            "User Action and Override Logging"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.2 (transparency / traceability logs); 9.7 (reliability, resilience & robustness)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "7.5 (documented information); 9.2 (internal audit)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.5 (verification & validation); 8.7 (operation)"
            }
        ]
    },
    {
        "article": "Article 16 – Obligations of providers of high-risk AI systems",
        "link": "https://artificialintelligenceact.eu/article/16/",
        "quote": (
            "Providers of high-risk AI systems shall ensure that the systems are designed and developed in such a way to allow for automatic recording of events "
            "during their operation (logging) to ensure traceability of the functioning of the AI systems throughout their lifecycle."
        ),
        "advice": (
            "Centralize logging frameworks and integrate them with audit tools. Design log data storage with secure access controls. Use metadata tagging for log parsing, and "
            "support forensic investigation of failures or complaints."
        ),
        "tactics": [
            "Centralized Logging Infrastructure",
            "Metadata-Enriched Log Entries",
            "Access-Controlled Log Storage",
            "Compliance-Ready Log Formats",
            "Audit Dashboard Integration"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "5.2 (AI policy); 5.3 (roles & responsibilities); 6.1 (actions to address risks)"
            },
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "5 (framework); 6.4–6.5 (risk assessment & treatment)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.5 (verification & validation); 8.7 (operation)"
            }
        ]
    }
],


"Safety": [
    {
        "article": "Article 9 – Risk management system",
        "link": "https://artificialintelligenceact.eu/article/9/",
        "quote": (
            "The risk management system shall identify and evaluate the known and foreseeable risks that are associated with each high-risk AI system, "
            "and define and implement risk mitigation measures. The risk management system shall be documented and kept up to date."
        ),
        "advice": (
            "Incorporate safety-engineering patterns to prevent and contain failures. Perform hazard analysis (e.g. FMEA or FTA) on the architecture to identify points of failure. "
            "Use error containment zones in the design. Implement fail-safe defaults and provide manual override or emergency stop mechanisms. Redundancy (e.g. N-version design) can be used "
            "to detect algorithmic faults and fallback to safety mode."
        ),
        "tactics": [
            "Error Containment Zones",
            "Fail-Safe Defaults",
            "Emergency Stop Interfaces",
            "N-Version Programming",
            "Anomaly Detection and Intervention"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "6.4–6.5 (risk assessment & treatment); 6.6 (monitoring & review); Annex A.10 (safety)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "8.2–8.3 (AI risk assessment & treatment); Annex B.6 (AI life-cycle controls)"
            },
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "7.2 (safety); 9.9 (functional safety)"
            }
        ]
    },
    {
        "article": "Article 15 – Accuracy, robustness and cybersecurity",
        "link": "https://artificialintelligenceact.eu/article/15/",
        "quote": (
            "High-risk AI systems shall be resilient to errors, faults or inconsistencies in the operating environment and in data inputs. "
            "They shall include mechanisms to ensure that system behavior does not lead to unsafe or unintended consequences."
        ),
        "advice": (
            "Design for resilience against adversarial inputs, degraded sensors, or data shifts. Include runtime safety monitors and human-in-the-loop interventions. "
            "Implement isolation of risky functions from core decision-making components."
        ),
        "tactics": [
            "Runtime Safety Monitoring",
            "Adversarial Input Handling",
            "Component Sandboxing",
            "Human-in-the-Loop Fallbacks",
            "Safe Mode Triggers"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.7 (reliability & robustness); 9.9 (functional safety); 9.10 (testing & evaluation)"
            },
            {
                "title": "ISO/IEC TR 24029-1:2021",
                "name": "Robustness of neural networks — Part 1: Overview",
                "link": "https://www.iso.org/standard/77609.html",
                "clauses": "6 (adversarial robustness testing); 7 (fault-injection techniques)"
            },
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "8.4 (AI system impact assessment); Annex B.6 (implementation guidance — life cycle)"
            }
        ]
    }
],

"Performance": [
    {
        "article": "Article 15 – Accuracy, robustness and cybersecurity",
        "link": "https://artificialintelligenceact.eu/article/15/",
        "quote": (
            "High-risk AI systems shall be designed and developed in such a way that they achieve appropriate levels of accuracy, robustness and cybersecurity, "
            "and perform consistently in those respects throughout their lifecycle."
        ),
        "advice": (
            "Architect for consistent performance and accuracy under load. Allocate explicit performance budgets for critical operations—e.g. max response time for predictions—"
            "and design the system to meet them. Use scalable architecture patterns such as load balancers, caching layers, and asynchronous processing to handle high throughput. "
            "Deploy the AI model behind a scaling API so that request volume increases can be met with additional instances. Include profiling and monitoring hooks to track "
            "performance in production and detect degradation over time."
        ),
        "tactics": [
            "Load Balancing",
            "Caching",
            "Asynchronous Queues",
            "Auto-Scaling",
            "Performance Monitoring Dashboards"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC TR 24028:2020",
                "name": "Trustworthiness in AI",
                "link": "https://www.iso.org/standard/77608.html",
                "clauses": "9.7 (reliability & robustness); 9.10 (testing & evaluation)"
            },
            {
                "title": "ISO/IEC 5259-1:2024",
                "name": "Data quality for analytics & ML — Part 1",
                "link": "https://www.iso.org/standard/81088.html",
                "clauses": "5.1–5.3 (data-quality framework & life-cycle)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.5 (verification & validation); 8.6 (model deployment); 8.7 (operation)"
            }
        ]
    },
    {
        "article": "Article 17 – Quality management system",
        "link": "https://artificialintelligenceact.eu/article/17/",
        "quote": (
            "The quality management system shall include, at least, strategies and procedures for the following aspects: examination, test and validation procedures "
            "to be carried out before, during and after development, as well as documentation of those procedures and their results."
        ),
        "advice": (
            "Use continuous integration and testing to validate performance regularly. Apply synthetic workloads to simulate usage and verify that critical functions meet their response thresholds. "
            "Log historical performance metrics to establish trends."
        ),
        "tactics": [
            "Load Testing",
            "Synthetic Workload Simulation",
            "Performance Regression Testing",
            "CI/CD with Metric Alerts",
            "Profiling Tool Integration"
        ],
        "iso_standards": [
            {
                "title": "ISO/IEC 42001:2023",
                "name": "Artificial intelligence management system",
                "link": "https://www.iso.org/standard/42001",
                "clauses": "6.1 (actions to address risks); 9.1 (monitoring & measurement); 10.1 (continual improvement)"
            },
            {
                "title": "ISO/IEC 23053:2022",
                "name": "Framework for AI Systems Using Machine Learning",
                "link": "https://www.iso.org/standard/74438.html",
                "clauses": "8.5 (verification & validation); 8.6 (model deployment); 8.7 (operation)"
            },
            {
                "title": "ISO/IEC 23894:2023",
                "name": "Risk management for AI",
                "link": "https://www.iso.org/standard/77304.html",
                "clauses": "6.6 (monitoring & review); 6.7 (recording & reporting)"
            }
        ]
    }
]
}