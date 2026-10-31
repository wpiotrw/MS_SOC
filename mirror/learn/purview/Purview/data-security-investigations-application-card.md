---
layout: Conceptual
title: Application card for Microsoft Purview Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-application-card
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: tanneruzzell
ms.date: 2026-06-17T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
- msec-ai-copilot
ms.custom: responsible-ai-transparency
description: Learn how Microsoft Purview Data Security Investigations uses AI to analyze incidents, identify sensitive data risks, and support mitigation with human oversight.
locale: en-us
document_id: 5a97bfb4-3137-3dbc-4a27-4b576e419d8f
document_version_independent_id: 5a97bfb4-3137-3dbc-4a27-4b576e419d8f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-application-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-application-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-application-card.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 11096e6d-fd70-d330-b06b-cf1afb57237d
---

# Application card for Microsoft Purview Data Security Investigations | Microsoft Learn

## What is an Application or Platform Card?

Microsoft’s Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to six core principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. These principles are embedded in the Responsible AI Standard, which guides teams in designing, building, and testing AI applications. Application and Platform Cards play a key role in operationalizing these principles by offering transparency around capabilities, intended uses, and limitations. For further insight, readers are encouraged to explore Microsoft’s Responsible AI Transparency Report and Code of Conduct, which outline how enterprise customers and individuals can engage with AI responsibly.

## Overview

Microsoft Purview Data Security Investigations is an AI-enabled investigation application for cybersecurity and data security teams. It helps organizations analyze data associated with potential breaches, insider incidents, and exfiltration events by combining search, AI analysis, and mitigation planning in one workflow. The application uses generative AI to identify sensitive content risks, prioritize high-impact items, and produce recommendations that support containment and remediation.

The application is designed to reduce time and complexity in post-breach and high-risk investigations. Instead of manually reviewing very large sets of files, emails, and messages, analysts can use vector search, categorization, and examination tools to focus on the most relevant and risky content first. This improves triage efficiency, supports cross-team coordination, and helps organizations take timely actions such as investigation-driven mitigation planning and purge operations.

Data Security Investigations is intended for enterprise customers and downstream users such as security analysts, incident responders, threat investigators, and data protection teams. Key documentation includes [Learn about Data Security Investigations](data-security-investigations) amd [Learn about AI analysis in Data Security Investigations](data-security-investigations-ai).

## Key terms

The following list provides a glossary of key terms related to Microsoft Purview Data Security Investigations:

- **Categorization**: An AI capability that groups scoped investigation content into default, custom, or AI-suggested categories to speed prioritization. Standard and Advanced processing options help analysts move from broad triage to deeper topic-level clustering.
- **Examination**: An AI analysis mode that performs focused item-level review for areas such as credentials, risk, and mitigation guidance. Examination outputs help investigators understand severity and recommended next actions.
- **Investigation scope**: The set of content items selected for review and analysis in an investigation.
- **Mitigation plan**: A structured set of actions for items identified as high priority during investigation. It helps analysts track and execute remediation and risk-reduction tasks.
- **Purge (soft/hard)**: A mitigation action to remove risky items identified in an investigation. Soft purge moves items to recoverable locations, while hard purge permanently deletes items.
- **Risk score**: A score generated during examination that helps analysts prioritize content based on potential security impact. It supports triage and escalation decisions.
- **AI Search (preview)**: A retrieval-augmented search experience that combines semantic retrieval with AI-generated summaries and citations. It helps analysts assess whether search results match investigative intent.
- **Vector search**: A semantic search method that uses embeddings to retrieve contextually relevant content, even when exact keywords are missing. It supports intent-aware queries and relevance-based ranking.

## Key features or capabilities

The key features and capabilities outlined here describe what Microsoft Purview Data Security Investigations is designed to do and how it performs across supported tasks.

- **Integrated incident-to-investigation workflow**: The application supports investigation creation from Microsoft Defender XDR incidents, Insider Risk Management cases, Data Security Posture Management (preview) insights, or manual draft mode. This helps security teams move from alerting to data-focused analysis without switching tools. It also improves collaboration between cybersecurity, compliance, and risk teams.
- **AI-powered semantic retrieval**: Vector search enables intent-aware retrieval across scoped, text-based content. Analysts can find relevant items even when content does not contain exact query terms. This improves recall and reduces manual keyword trial-and-error.
- **AI-assisted prioritization through categorization**: Categorization organizes data into default, custom, and AI-suggested categories so analysts can quickly focus on higher-risk areas. Advanced categorization provides additional topic-level organization for deeper review. This reduces review effort in large investigations by surfacing prioritized content instead of requiring full manual review first.
- **Targeted risk and credential examination**: Examination tools extract credentials, assess item risk, and generate mitigation-oriented outputs for selected content. Analysts get a faster understanding of what might be exposed and what to do next. This supports quicker containment and remediation in active incidents.
- **Mitigation and purge actions**: Investigators can convert findings into concrete actions through mitigation plans and purge workflows. This ties analysis outputs directly to risk-reduction execution. Teams can track progress and status of mitigation decisions within the investigation lifecycle.
- **Audit and ecosystem integration**: The solution integrates with Microsoft Purview audit workflows and Microsoft security solutions, helping teams preserve evidence context and align response actions. It also supports investigation activity logging in the unified audit log to strengthen operational accountability.

## Intended uses

Microsoft Purview Data Security Investigations can be used in multiple scenarios. Some examples of use cases include:

- **Breach response from a Defender XDR incident**: An analyst can create new Data Security Investigation directly from a Defender XDR incident to assess the blast radius of a compromised user. AI-powered examination surfaces credentials, sensitive documents, and communications the attacker could have accessed, with regulated and customer-impacting data prioritized first. Mitigation actions are taken within the same investigation, producing a documented response for audit and follow-up.
- **Tracing employee data exfiltration through the audit log**: When an employee is suspected of exfiltrating a large volume of data, an investigator queries the Unified Audit Log through Data Security Investigations to trace files downloaded and accessed. AI categorization separates routine activity from suspicious content and focuses attention on the highest-risk data. AI enriched findings are handed off to legal and privacy teams for further actions.
- **Hunting sensitive data in an overexposed SharePoint site**: After learning that a SharePoint site containing sensitive content is broadly overshared, an investigator scopes an investigation to that site and runs AI analysis to identify what is actually at risk. Vector search and categorization surface concentrations of sensitive content that would be impractical to review manually.
- **Reviewing risky AI interactions**: An investigator scopes a DSI investigation to AI prompts and responses involving sensitive data, whether from Microsoft Copilot or third-party AI tools. Examinations identify where regulated content, credentials, or PII appeared in interactions, and categorization highlights recurring patterns of risky use. Findings inform both immediate remediation on exposed content and broader follow-up with the users and tools involved.

## Models and training data

Microsoft Purview Data Security Investigations leverages a variety of AI models to power the experience that users see. Some examples include Azure OpenAI Service models and Microsoft Security Copilot platform capabilities used for vector embeddings, categorization, and examination-related AI outputs. To learn more about the data used to train the foundation models behind Microsoft Purview Data Security Investigations, refer to the linked model cards to find the relevant data cards.

- [Transparency note for Azure OpenAI](/en-us/azure/foundry/responsible-ai/openai/transparency-note)
- [Privacy and data security in Microsoft Security Copilot](/en-us/copilot/security/privacy-data-security)
- [Responsible AI practices at Microsoft](https://www.microsoft.com/ai/responsible-ai)

## Performance

Microsoft Purview Data Security Investigations is designed to perform reliably in enterprise post-breach and data risk investigation workflows where investigation scope is properly defined and users are assigned the required role groups. In these conditions, analysts can iteratively refine search results, prioritize data through categorization, and run examination on selected items to support mitigation decisions.

The intended inputs are primarily enterprise content and investigator prompts. Inputs include files, emails, and messages scoped from supported Microsoft 365 data sources; metadata and audit-linked context; and natural language or keyword queries used in vector search and Search with AI (preview). The expected outputs include relevance-ranked search results, category groupings, risk and credential examination outputs, and mitigation-oriented recommendations.

The primary evaluated and documented AI interaction modality is text. Vectorization and semantic retrieval depend on text-bearing content. Some content types that do not include usable text are excluded from vectorization workflows, so investigators should account for this during scope planning.

Performance and usefulness are influenced by investigation setup quality, including scope precision, category selection, and iterative human review. In large datasets, categorization returns prioritized subsets rather than exhaustive coverage for each category. For comprehensive item-level analysis, teams should combine categorization with examination and investigator validation.

## Limitations

Understanding Microsoft Purview Data Security Investigations’s limitations is crucial to determine if it is used within safe and effective boundaries. While we encourage customers to leverage Microsoft Purview Data Security Investigations in their innovative solutions or applications, it’s important to note that Microsoft Purview Data Security Investigations was not designed for every possible scenario. We encourage users to refer to either the Microsoft Enterprise AI Services Code of Conduct (for organizations) or the Code Conduct section in the Microsoft Services Agreement (for individuals) as well as the following considerations when choosing a use case:

- **AI output reliability constraints**: Results generated by generative AI might not always be fully accurate or complete. This limitation is important because investigators may otherwise overestimate confidence and miss context that changes incident severity. Users should validate critical findings, especially before legal, compliance, or irreversible technical actions. Human judgment remains required in final decisions.
- **Text-content dependency for semantic tooling**: Vector search and related semantic workflows require text-bearing content. Certain content types, such as image-only items or content without extractable text, may be excluded from vectorization and therefore from some AI-assisted retrieval workflows. Teams should evaluate whether key evidence might require additional review methods outside semantic search. This helps avoid false assumptions about complete coverage.
- **Prioritized-not-exhaustive categorization behavior**: Categorization is optimized to surface high-relevance content for selected categories, not to guarantee full review of every item in scope per category. In large datasets, relevant lower-scoring items might not appear in category outputs. Users should use examination for comprehensive item-level analysis where complete coverage is required. This is especially important in high-impact investigations.
- **Operational limits and capacity boundaries**: Investigation and feature limits apply, including limits on total documents, total file size per investigation, and limits in audit search and purge workflows. These constraints can affect how teams segment work and sequence large investigations. Users should plan scope and processing strategy around published limits to avoid delays. Capacity-aware planning improves both cost control and investigative continuity.
- **Not intended for unsupported scenarios or prohibited use**: Data Security Investigations is intended for data security incident investigation and mitigation contexts. Using it as a sole decision-maker, outside governance and security workflows, or in ways prohibited by terms and code-of-conduct requirements can create safety and compliance risk. Organizations should keep the tool within intended operational boundaries and apply layered controls. This includes legal and policy review before high-consequence actions.

## Evaluations

Performance and safety evaluations assess whether AI applications are operating reliably and securely by examining factors like groundedness, relevance, and coherence while identifying the risks of generating harmful content. The following evaluations were conducted with safety components already in place, which are also described in 9. Safety Components and Mitigations.

### Performance and quality evaluations

Performance and quality evaluations for AI features in Microsoft Purview Data Security Investigations focus on practical investigation outcomes, including vector search relevance, categorization accuracy, and examination output usefulness. Based on product documentation, evaluation activities include pre-release testing and scenario-based validation to assess whether AI-assisted discovery, prioritization, and analysis features help investigators act on identified risks.

For current AI experiences, the primary evaluated modality is text. Ideal outcomes are accurate, relevant findings that help analysts quickly identify high-risk items and take informed investigative actions. Suboptimal outcomes include results that are incomplete, irrelevant, or require substantial additional analysis and validation.

### Risk and safety evaluations

Our evaluation data is custom-built to assess AI application performance across key areas of safety and quality, simulating real-world scenarios and risks. We begin by identifying relevant evaluation aspects of concern based on multi-disciplinary research and expert input. These concerns are translated into targeted evaluation objectives and guide formulation of evaluation metrics. For safety, we create adversarial prompts to elicit undesirable or edge-case responses, which are then scored using AI-assisted annotators trained to assess alignment with Microsoft’s safety standards. For quality, we craft rubric-based prompts relevant to scenarios including evaluating retrieval-augmented generation (RAG) applications and agents. Datasets are curated from diverse sources including synthetic and public datasets to simulate real-world user scenarios. Using the curated datasets, both evaluations undergo iterative refinement and human alignment to improve metric efficacy and reliability. This methodology forms the foundation of repeatable, rigorous assessments that reflect how customers use evaluations to build better and safer AI.

### Custom evaluations

Data Security Investigations was evaluated using multiple quality and reliability indicators, including AI accuracy, result relevance, and output clarity. Based on documented practices, evaluations use a combination of manual red teaming and human grading to test whether AI-assisted outputs are useful and dependable for incident investigation workflows. The primary evaluated modality for current AI experiences is text.

Evaluation scenarios include semantic retrieval, categorization relevance, and examination outputs used to prioritize and mitigate risk. Ideal results are contextually relevant findings that help analysts quickly identify high-risk items and take informed next actions. Suboptimal results include incomplete, unclear, or less relevant outputs that require additional iteration and validation by investigators.

Operational feedback is also used to improve performance over time. The product collects selected quality-focused metrics about AI inputs and outputs to help tune relevance and usefulness, while documented privacy controls describe what content is and is not collected. This continuous loop supports ongoing quality improvements after release.

## Safety components & mitigations

- **Role-based access controls**: Data Security Investigations uses dedicated role groups (Admins, Investigators, Reviewers) to control feature access and responsibilities. This helps limit who can run sensitive activities such as purge and administrative configuration. Clear separation of duties reduces misuse risk and strengthens accountability in investigation workflows.
- **Human-in-the-loop decision making**: AI outputs are designed to assist analysts, not replace investigator judgment. Teams are expected to validate high-impact findings and mitigation recommendations before taking consequential action. This mitigates overreliance and reduces the chance of acting on incomplete AI output.
- **Scope refinement and exclusion controls**: Investigators can iteratively narrow investigation scope and exclude irrelevant items before advanced AI analysis. This improves relevance, reduces noise, and lowers exposure to unnecessary content processing. Focused scope management also supports cost control and faster incident response.
- **Audit logging and evidentiary traceability**: Investigation-related activities are logged through integrated auditing workflows. Logging supports forensic traceability, operational review, and compliance accountability. This is a key mitigation for governance and post-incident validation requirements.
- **Privacy and data handling safeguards**: Documented controls describe tenant-isolated investigation storage and privacy protections for AI processing. Data sharing, logging, and scanning controls in integrated processing paths are documented as off by default for specific Copilot processing contexts. These safeguards help reduce privacy risk and support enterprise compliance expectations.

## Best practices for deploying and adopting Microsoft Purview Data Security Investigations

Responsible AI is a shared commitment between Microsoft and its customers. While Microsoft builds AI applications with safety, fairness, and transparency at the core, customers play a critical role in deploying and using these technologies responsibly within their own contexts. To support this partnership, we offer the following best practices for deployers and end users to help customers implement responsible AI effectively. Deployers and end-users (admins) should:

- Exercise caution and evaluate outcomes when using Microsoft Purview Data Security Investigations for consequential decisions or in sensitive domains: Consequential decisions are those that may have a legal or significant impact on a person’s access to education, employment, financial platforms, government benefits, healthcare, housing, insurance, legal platforms, or that could result in physical, psychological, or financial harm. Sensitive domains—such as financial platforms, healthcare, and housing—require particular care due to the potential for disproportionate impact on different groups of people. When using AI for decisions in these areas, make sure that impacted stakeholders can understand how decisions are made, appeal decisions, and update any relevant input data.
- Evaluate legal and regulatory considerations: Customers need to evaluate potential specific legal and regulatory obligations when using any AI platforms and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI platforms or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.
- **Plan investigations for iterative analysis**: Data Security Investigations workflows are intentionally iterative, especially for search refinement, scope tuning, and AI-assisted triage. Teams should define repeatable checkpoints for when to run vector search, categorization, and examination. This improves consistency, reduces unnecessary compute use, and strengthens investigation quality.
- **Coordinate cross-functional response early**: Security incidents often involve security, IT, legal, compliance, and business owners. Bring these stakeholders into the investigation process as soon as high-risk findings are identified. Early coordination improves containment speed and reduces downstream remediation friction.

End-users should:

- **Use clear and focused investigation prompts**: For vector search and Search with AI (preview), prompts should include context, subject, and intent (for example, credentials in a named project or access-risk content for a specific incident). Clear prompts produce more relevant retrieval and reduce investigative noise. Users should iterate and compare outputs before drawing conclusions.
- **Validate AI findings with supporting evidence**: Review citations, item details, and activity context before escalating or mitigating. AI outputs can accelerate triage but may miss edge cases or include lower-confidence results. Cross-checking with search, scope views, and stakeholder input reduces error risk.
- Exercise human oversight when appropriate: Human oversight is an important safeguard when interacting with AI applications. While we continuously improve our AI applications, AI might still make mistakes. The outputs generated may be inaccurate, incomplete, biased, misaligned, or irrelevant to your intended goals. This could happen due to various reasons, such as ambiguity in the inputs or limitations of the underlying models. As such, users should review the responses generated by Microsoft Purview Data Security Investigations and verify that they match their expectations and requirements.
- Be aware of the risk of overreliance: Overreliance on AI happens when users accept incorrect or incomplete AI outputs, mainly because mistakes in AI outputs may be hard to detect. For the end-user, overreliance could result in decreased productivity, loss of trust, application abandonment, financial loss, psychological harm, physical harm, among others. (e.g. a doctor accepts an incorrect AI output).
- Exercise caution when designing agentic AI in sensitive domains: Users should exercise caution when designing and/or deploying agentic AI applications in sensitive domains where agent actions are irreversible or highly consequential.
- Additional precautions should also be taken when creating autonomous agentic AI as described further in either the Microsoft Enterprise AI Services Code of Conduct (for organizations) or the Code Conduct section in the Microsoft Services Agreement (for individuals).

Deployers should:

- **Configure permissions and ownership model upfront**: Assign Data Security Investigations role groups based on least privilege and operational responsibility before incidents occur. Include backup admins and clear role coverage to avoid response delays. This reduces risk from overbroad access and strengthens continuity during active incidents.
- **Design for limits, costs, and throughput**: Investigation, audit search, and purge limits should inform how teams segment large incidents. Teams should also monitor capacity usage and stage AI processing to align with urgency and budget. This avoids bottlenecks and supports predictable response performance.
- **Test mitigation workflows and escalation paths**: Run tabletop or pilot investigations using representative data to validate query patterns, categorization strategy, and mitigation handoffs. Pre-tested workflows reduce confusion during real incidents and improve time to action. Include checks for legal and compliance notification requirements as part of this testing.

## Learn more about Microsoft Purview Data Security Investigations

For additional guidance or to learn more about the responsible use of Microsoft Purview Data Security Investigations, we recommend reviewing the following documentation:

- [Learn about Data Security Investigations](data-security-investigations)
- [Get started with Data Security Investigations](data-security-investigations-get-started)
- [Learn about AI analysis in Data Security Investigations](data-security-investigations-ai)
- [Use AI analysis in Data Security Investigations](data-security-investigations-ai-analysis)
- [Learn about the Data Security Investigations workflow](data-security-investigations-workflow)
- [Assign permissions in Data Security Investigations](data-security-investigations-permissions)
- [Limits in Data Security Investigations](data-security-investigations-ref-limits)
- [Privacy FAQ for Data Security Investigations](data-security-investigations-privacy-faq)
- [Microsoft Purview privacy statement](https://www.microsoft.com/privacy/privacystatement)
- [Microsoft Trust Center](https://www.microsoft.com/trust-center)

### Learn more about responsible AI

- [Microsoft AI principles](https://www.microsoft.com/ai/responsible-ai)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/responsible-ai-resources)
- [Microsoft Azure Learning courses on responsible AI](/en-us/training/browse/?products=azure&amp;subjects=artificial-intelligence)