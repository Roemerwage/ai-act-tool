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
            "Adopt a defence-in-depth stance: validate every input, authenticate every actor and monitor every interaction. "
            "Layer controls so attempted tampering, poisoning or privilege-escalation is detected swiftly and contained "
            "before it alters system behaviour."
        ),
        "tactics": [
            "Input validation and sanitization",
            "Role-based access controls(RBAC)",
            "Transport layer security (TLS)",
            "Audit trail for access logs",
            "Intrusion detection systems (IDS)"
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
            "Architect the solution so that risks surfaced at any stage can be detected early and contained locally. "
            "Embed redundancy, health supervision and graceful-degradation paths so that foreseeable faults or data shifts never cascade into total service failure. "
            "Keep the mitigation loop continuous by feeding runtime signals back into the design and deployment pipeline."
        ),
        "tactics": [
            "Failover clustering",
            "Active-passive redundancy",
            "Service replication",
            "Health monitoring",
            "Graceful degradation"
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
                "Treat robustness as a service-level obligation. "
                "Distribute workload, keep hot-standby instances ready and rebalance traffic automatically, "
                "so capacity and response times stay within target even when nodes, links or whole zones fail."
        ),
        "tactics": [
                "Failover clustering",
                "Service replication",
                "Health monitoring",
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
            "Architect for low-friction evolution driven by operational insight. "
            "Expose health and usage telemetry, version APIs semantically and automate deployment so fixes and enhancements ship promptly as monitoring uncovers issues."

        ),
        "advice": (
            "Enable easy adaptation and update of the system. Use a modular architecture where components are decoupled and communicate via stable interfaces, so changes "
            "in one module have minimal impact on others. For instance, separate data ingestion, model logic, and interface into distinct services. Employ information hiding: "
            "encapsulate details likely to change (e.g. model algorithms, data schemas) behind well-defined interfaces. Continuous delivery practices can be adopted to frequently "
            "deploy small improvements."
        ),
        "tactics": [
                "Encapsulate",
                "Restrict dependencies",
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
            "Enable rapid containment and rollback when faults emerge. "
            "Provide dynamic re-configuration hooks, fine-grained diagnostics and isolation zones that confine defective components while a patched version is prepared and deployed."

        ),
        "tactics": [
            "Component replacement",
            "Configuration-time binding",
            "Use an intermediary"
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
            "Surface explanations and usage guidance at the points where users rely on the model. "
            "Combine plain-language rationales, visual cues and contextual help so people can evaluate outcomes, limitations and next steps without consulting external documentation."
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
            "Make the AI presence unmistakable and auditable. "
            "Display clear visual or auditory cues, log the disclosure event and align the notification style with the product’s branding to maintain user trust without confusion."
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
            "Guarantee an immutable, time-sequenced account of the system’s behaviour. "
            "Capture inputs, outputs and control actions as append-only events, preserve integrity with cryptographic checks, and store them where auditors can replay any decision path on demand."
        ),
        "tactics": [
                "Event sourcing pattern",
                "Tamper-proof log stores",
                "Secure time-stamped logs",
                "Comprehensive event capture"
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
            "Centralise and enrich lifecycle logs so incidents can be reconstructed across versions and components. "
            "Protect the evidence chain with role-based access and metadata tagging, enabling auditors to trace any anomaly end-to-end without compromising data protection."
        ),
        "tactics": [
                "Event sourcing pattern",
                "Access-controlled log storage",
                "Comprehensive event capture"
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
            "Harden the design with safety-engineering defaults. "
            "Partition components into error-containment zones, provide manual override paths and fail-safe modes so that any hazardous condition is isolated and neutralised before it causes harm."
        ),
        "tactics": [
            "Error containment zones",
            "Fail-safe defaults",
            "Emergency stop interfaces",
            "N-version programming"
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
            "Continuously supervise runtime behaviour for unsafe states and shift to a controlled safe-mode when thresholds are crossed. "
            "Sandbox risky components and include human fallback loops for irreversible actions so that errors or adversarial inputs cannot propagate harm."
        ),
        "tactics": [
            "Runtime safety monitoring",
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
            "Design for elastic throughput and predictable latency. "
            "Define performance budgets, instrument end-to-end metrics and scale horizontally or shed non-critical load before response-time targets are breached."
        ),
        "tactics": [
            "Introduce concurrency",
            "Maintain multiple copies of computations",
            "Maintain multiple copies of data",
            "Schedule resources",
            "Bound queue sizes"
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
            "Embed performance-and-accuracy gates into CI/CD. "
            "Re-run regression suites and synthetic workloads on every build, block releases on KPI drift, and archive the evidence so validation remains demonstrable throughout the lifecycle."
        ),
        "tactics": [
            "Introduce concurrency",
            "Maintain multiple copies of computations",
            "Maintain multiple copies of data",
            "Schedule resources",
            "Bound queue sizes"
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