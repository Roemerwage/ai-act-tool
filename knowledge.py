# Updated knowledge.py file with 100% QA coverage based on the AI Act PDF
# Each entry includes legal reference, full quote, and architecture advice

architecture_rules = {
    "Security": [
        {
            "article": "Article 15 – Accuracy, robustness and cybersecurity",
            "quote": (
                "High-risk AI systems shall be designed and developed in such a way, including with appropriate levels of accuracy, robustness and cybersecurity, "
                "that they achieve, in the light of their intended purpose, an appropriate level of accuracy, robustness and cybersecurity, and perform consistently "
                "for their intended purpose. They shall be resilient as regards errors, faults or inconsistencies that may occur within the system or due to interaction "
                "with natural persons or other systems. High-risk AI systems shall be protected against attempts by unauthorized third parties to alter their use, "
                "performance or functionality by exploiting the system vulnerabilities and against data poisoning. Appropriate measures shall be taken to prevent and "
                "control for those risks through technical redundancy, fail-safe and fallback plans."
            ),
            "advice": (
                "Design system components to resist data poisoning and adversarial manipulation. Enforce strict authentication, input validation, and secure "
                "model deployment. Apply redundancy and fallback strategies to maintain integrity under stress or compromise."
            )
        }
    ],

    "Availability": [
        {
            "article": "Article 9 – Risk management system",
            "quote": (
                "A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. It shall consist of a "
                "continuous, iterative process run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic updating. That process shall "
                "ensure that the high-risk AI system performs consistently for its intended purpose and under reasonably foreseeable conditions of use, and shall include "
                "appropriate measures to identify, estimate, evaluate and handle risks."
            ),
            "advice": (
                "Implement a risk-oriented design process with stress tests and simulations. Include service uptime goals, fallback behaviors, and failure recovery procedures "
                "to ensure availability under load or failure."
            )
        },
        {
            "article": "Article 15 – Accuracy, robustness and cybersecurity",
            "quote": (
                "High-risk AI systems shall perform consistently for their intended purpose throughout their lifecycle. Appropriate levels of accuracy, robustness and "
                "cybersecurity shall be ensured, taking into account the generally acknowledged state of the art."
            ),
            "advice": (
                "Build lifecycle monitoring into system infrastructure. Apply regression tests, live performance dashboards, and version control to verify continuous availability."
            )
        }
    ],

    "Modifiability": [
        {
            "article": "Article 61 – Post-market monitoring system",
            "quote": (
                "Providers of high-risk AI systems shall establish a post-market monitoring system in a manner that is proportionate to the nature of the AI system and the risks "
                "it may pose. That system shall collect, document and analyse relevant data provided by users or collected through other sources on the performance of high-risk AI systems throughout their lifetime, and allow the provider to evaluate continuous compliance with the requirements set out in this Regulation."
            ),
            "advice": (
                "Ensure modularity and reconfigurability of software components. Enable dynamic updates and compatibility checks to maintain continuous regulatory compliance."
            )
        },
        {
            "article": "Article 62 – Reporting of serious incidents and of malfunctioning",
            "quote": (
                "Providers shall immediately report to the market surveillance authorities any serious incident or any malfunctioning of the high-risk AI system which constitutes a breach of obligations laid down in this Regulation or which poses significant harm to health, safety, or fundamental rights."
            ),
            "advice": (
                "Enable hotfixes, emergency patches, and rollbacks. Include traceable versioning and compliance-aware change deployment mechanisms."
            )
        }
    ],

    "Transparency": [
        {
            "article": "Article 13 – Transparency and provision of information to users",
            "quote": (
                "High-risk AI systems shall be designed and developed in such a way that their operation is sufficiently transparent to enable users to interpret the system’s output "
                "and use it appropriately. Providers shall ensure that high-risk AI systems are accompanied by instructions for use."
            ),
            "advice": (
                "Integrate explainability methods such as rationale explanation, saliency maps, or simplified logic paths. Document all outputs and limitations in accessible language."
            )
        },
        {
            "article": "Article 50 – Transparency obligations for certain AI systems",
            "quote": (
                "Providers shall ensure that natural persons are informed that they are interacting with an AI system, unless this is obvious from the circumstances and the context of use."
            ),
            "advice": (
                "Disclose AI interactions through interface cues, tooltips, or onboarding flows. Design visual indicators or voice prompts where appropriate."
            )
        },
        {
            "article": "Article 52 – Obligations of providers of general-purpose AI models",
            "quote": (
                "The provider of a general-purpose AI model shall draw up and make publicly available a sufficiently detailed summary about the content used for training the model. "
                "That summary shall be formulated in a manner that is comprehensive to providers of AI systems who intend to integrate the general-purpose AI model in their AI systems."
            ),
            "advice": (
                "Compile a public documentation set detailing training sources, development methodology, model capabilities, and known biases or risks."
            )
        }
    ],

    "Auditability": [
        {
            "article": "Article 12 – Record-keeping",
            "quote": (
                "High-risk AI systems shall be designed and developed with capabilities enabling the automatic recording of events (‘logs’) while the system is operating. Logging "
                "shall be ensured to the extent appropriate to the intended purpose of the system and sufficient to facilitate the post-market monitoring obligations."
            ),
            "advice": (
                "Log decisions, model inputs/outputs, user actions, and exceptions. Ensure immutability of logs and design retention policies that support auditing and monitoring."
            )
        },
        {
            "article": "Article 16 – Obligations of providers of high-risk AI systems",
            "quote": (
                "Providers shall ensure that high-risk AI systems are accompanied by the documentation and instructions of use referred to in Article 11 and Article 13(3), and that "
                "they undergo the relevant conformity assessment procedure referred to in Article 43."
            ),
            "advice": (
                "Document system behavior, assumptions, data provenance, and test procedures. Structure documentation to support compliance audits and traceability."
            )
        }
    ],

    "Safety": [
        {
            "article": "Article 9 – Risk management system",
            "quote": (
                "The risk management system shall identify and evaluate the known and foreseeable risks that are associated with each high-risk AI system, and define and implement "
                "risk mitigation measures. The risk management system shall be documented and kept up to date."
            ),
            "advice": (
                "Apply risk analysis frameworks (e.g., FMEA, HARA) and simulation tools. Include safeguards such as user overrides, error containment, and health monitoring."
            )
        },
        {
            "article": "Article 62 – Reporting of serious incidents and of malfunctioning",
            "quote": (
                "Providers shall immediately report to the market surveillance authorities any serious incident or malfunctioning of the high-risk AI system which constitutes a breach of "
                "obligations laid down in this Regulation or which poses significant harm to health, safety, or fundamental rights."
            ),
            "advice": (
                "Add triggers for alerts when serious faults or violations occur. Define a responsible incident response plan including containment and rollback actions."
            )
        }
    ],

    "Performance": [
        {
            "article": "Article 15 – Accuracy, robustness and cybersecurity",
            "quote": (
                "High-risk AI systems shall be designed and developed in such a way, including with appropriate levels of accuracy, robustness and cybersecurity, that they achieve, "
                "in the light of their intended purpose, an appropriate level of accuracy, robustness and cybersecurity and perform consistently for their intended purpose."
            ),
            "advice": (
                "Test model performance on edge cases and long-tail inputs. Benchmark accuracy, latency, and resource efficiency in live-like conditions."
            )
        },
        {
            "article": "Article 17 – Quality management system",
            "quote": (
                "Providers shall ensure that a quality management system is established, implemented and documented. The quality management system shall ensure compliance with this "
                "Regulation and effective monitoring and control of the functioning of the high-risk AI system."
            ),
            "advice": (
                "Set up structured review processes with metrics for performance, robustness, and user impact. Automate tests for drift and anomaly detection."
            )
        }
    ]
}
