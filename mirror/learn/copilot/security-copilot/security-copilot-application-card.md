---
layout: Conceptual
title: Application card - Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how Microsoft Security Copilot works, including its intended uses, limitations, evaluations, and safety mitigations.
ms.date: 2026-06-22T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: responsible-ai-transparency​
ms.reviewer: spunukol
ai-usage: ai-assisted
search.audiencetype: Admin
locale: en-us
document_id: fdd043a2-d3f7-71a0-e360-1250a4bbd05e
document_version_independent_id: fdd043a2-d3f7-71a0-e360-1250a4bbd05e
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/security-copilot-application-card.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: security-copilot-application-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/security-copilot-application-card.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 4ab07735-29ae-50d9-c389-eed4937e8b5d
---

# Application card - Microsoft Security Copilot | Microsoft Learn

## What is an Application or Platform card?

Microsoft's Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to [six core principles](https://www.microsoft.com/ai/principles-and-approach/): fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. These principles are embedded in the [Responsible AI Standard](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf), which guides teams in designing, building, and testing AI applications. Application and Platform cards play a key role in operationalizing these principles by offering transparency around capabilities, intended uses, and limitations. For further insight, readers are encouraged to explore Microsoft's [Responsible AI Transparency Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Responsible-AI-Transparency-Report-2025.pdf) and the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct), which outlines how to engage with AI responsibly.

## Overview

Microsoft Security Copilot is a generative AI-powered security solution that helps increase the efficiency and capabilities of defenders to improve security outcomes at machine speed and scale. It provides a natural language, assistive copilot experience that helps security professionals and IT administrators handle a wide range of end-to-end scenarios, including incident response, threat hunting, intelligence gathering, and posture management.

Security Copilot is designed with integration in mind. It offers an immersive standalone experience at https://securitycopilot.microsoft.com and integrates with Microsoft security products including Microsoft Defender XDR, Microsoft Sentinel, Microsoft Intune, Microsoft Entra, and Microsoft Purview, as well as supported third-party services.

The intended users include SOC analysts, IT administrators, data security and identity administrators, compliance analysts, and security leaders such as Chief Information Security Officers (CISOs).

Security Copilot has earned the ISO 42001 certification that confirms that an independent third party reviewed Microsoft's application of the necessary framework and capabilities to effectively manage risks and opportunities associated with the continuous development, deployment, and operation of Microsoft AI systems.

For more information, see [What is Microsoft Security Copilot?](microsoft-security-copilot), [Microsoft Security Copilot experiences](experiences-security-copilot), and [Application card for Security Copilot agents](/en-us/copilot/security/security-copilot-application-card-agents).

## Key terms

The following table provides a glossary of key terms related to Microsoft Security Copilot.

| Term | Definition |
| --- | --- |
| Agent | A Security Copilot agent processes signals from the customer environment through integrated data sources and plugins, analyzes over data, and generates recommendations. Agents may also perform scoped actions within configured permissions when prompted, which require an appropriate user or administrator approval. Agents can range from simple prompt-and-response experiences to more automated, semi-autonomous workflows with human oversight. For example, the Phishing Triage Agent and the Vulnerability Remediation Agent. |
| Agent identity | The credential an agent uses to authenticate with Microsoft services and access the data it needs to perform its tasks. During setup, an administrator chooses either to create a dedicated identity (using Microsoft Entra Agent ID) or to let the agent inherit the credentials of the configuring user. The choice of identity governs what data the agent can access. |
| Data source | Structured or unstructured data accessed through plugins or integrations to ground responses. |
| Embedded experience | Accessing Security Copilot capabilities from within another Microsoft security product, such as Microsoft Defender XDR or Microsoft Sentinel. The Security Copilot sidecar panel surfaces AI assistance directly in the context of that product. |
| Grounding | The process of providing contextual input sources to the large language model related to a user's prompt. By enabling Security Copilot to access organizational data through plugins and Microsoft security products, Security Copilot can deliver more accurate and contextually relevant responses. |
| Large language model (LLM) | AI models trained on large amounts of text data to predict words in sequences. LLMs are capable of performing various tasks such as text generation, summarization, translation, classification, and more. |
| Plugin | A collection of related tools that extends Security Copilot's capabilities by giving it access to resources from Microsoft and non-Microsoft services and public websites through APIs. Plugins add more context to the responses and outputs that Security Copilot generates. |
| Post-processing | The set of actions Security Copilot performs to refine and prepare the LLM response before returning it to the user. This post-processing includes additional grounding calls through plugins, responsible AI checks, security, compliance, and privacy checks. |
| Prompt | The natural language text a user sends to Security Copilot to execute a specific task or obtain information. For example, *Summarize this incident and suggest remediation steps.* |
| Promptbook | A series of prompts that run in sequence, building on previous responses, to accomplish specific security-related tasks. Promptbooks can be used from the library or built and shared by users. |
| Red team testing | Techniques used by experts to assess the limitations and vulnerabilities of a system and to test the effectiveness of planned mitigations. Red team testing is used to identify potential risks and is distinct from systematic measurement of risks. |
| Responsible AI | Microsoft's policy, research, and engineering practices that are grounded in its AI principles and operationalized through the [Responsible AI standard](https://www.microsoft.com/ai/responsible-ai). For more information, see the [Fluent RAI guidance](https://fluent2.microsoft.design/responsible-AI/). |
| Security Compute Unit (SCU) | SCUs are the units of compute capacity used to run Security Copilot workloads and deliver consistent performance across its experiences. Security Copilot capacity is measured in SCUs and can be consumed through provisioned or overage capacity models. For more information, see [Understand SCUs](/en-us/copilot/security/security-compute-units-capacity). |
| Security Copilot response | The AI-generated output returned to a user prompt, including summaries, recommendations, or actions that may include code and visuals. |
| Security Operations Center (SOC) | A dedicated security team or facility focused on continuous monitoring, analysis, and response to cybersecurity incidents within an organization. SOC analysts are among the primary intended users of Security Copilot. |
| Security Store | A marketplace-like experience where users can discover and enable partner-built agents and extensions for Security Copilot. |
| Session | A bounded interaction context that includes prompts, responses, and associated data used to generate outputs. Session context is isolated and isn’t shared across sessions. Access to session data is governed by user permissions and workspace roles, and prompts and responses are treated as Customer Data that isn’t used to train foundation models. |
| Standalone experience | The immersive Security Copilot portal experience accessed directly at https://securitycopilot.microsoft.com. |
| Tenant | The organizational boundary in Microsoft Entra ID that isolates identity, access, and data for Security Copilot. All workspaces, users, and interactions operate within this boundary and are governed by tenant-level permissions and security controls. |

## Key features or capabilities

The key features and capabilities in the following table describe what Microsoft Security Copilot is designed to do and how it performs across supported tasks.

| Feature or capability | Description |
| --- | --- |
| Incident investigation and response | Security Copilot helps security professionals triage and investigate incidents by generating summaries of complex security alerts, correlating signals across Microsoft Defender XDR, Microsoft Sentinel, and other integrated products, and providing step-by-step remediation guidance. |
| Threat intelligence | Security Copilot can search across Microsoft Defender threat intelligence articles and profiles, threat analytics reports, and vulnerability disclosure publications to surface relevant intelligence aligned to a prompt. |
| Security Alert Triage | Security Copilot includes the Security Alert Triage Agent to help security teams triage alerts at scale by identifying real attacks and false positives, enabling analysts to focus on investigating real threats. |
| Script analysis and KQL query generation | Security Copilot can analyze suspicious scripts or malware and translate natural language into KQL queries, enabling team members at all skill levels to perform advanced hunting and technical analysis tasks. |
| Security posture management | Security Copilot helps users understand prioritized risks across their environment and identify opportunities to improve posture through integration with Microsoft Defender XDR, Microsoft Entra, and Microsoft Intune. |
| Security policy creation and management | Users can define new policies, cross-reference them with existing policies for conflicts, and summarize policies in plain language to manage complex organizational context. |
| Promptbooks | Promptbooks are sequences of prompts that run in order to accomplish specific security tasks. Users can run promptbooks from a shared library or create and share their own. |
| Agents | Security Copilot supports agents that can automate and assist with security and IT operations tasks within the permissions granted by administrators. Agent actions are governed by configured identities, access controls, and triggers, and are designed to operate with human oversight as part of security workflows. Microsoft-built agents span the security product portfolio, covering SOC operations, threat hunting, threat intelligence, identity management, endpoint management, and data security. Administrators configure each agent’s identity, permissions, and trigger. For details on specific agents and their use cases, see [Intended uses](security-copilot-application-card-agents#intended-uses). |
| File upload | Users can upload files directly into Security Copilot sessions, allowing Copilot to analyze, summarize, or cross-reference uploaded content when generating responses. |
| Multi-language support | Security Copilot supports prompting and responses in multiple languages. For more information, see [Supported languages](supported-languages). |

## Intended uses

Microsoft Security Copilot is designed for use by security professionals and IT administrators who need AI-assisted support across a broad range of security and IT operations tasks. The assistive copilot experience helps users work more efficiently by surfacing relevant context, generating actionable guidance, and reducing the time spent on manual analysis. Some examples of intended use cases include:

- **Incident investigation and response**: Generates summaries of complex alerts, correlates signals across integrated security products such as Microsoft Defender XDR and Microsoft Sentinel, and provides step-by-step remediation guidance. Analysts can ask follow-up questions to progressively refine their investigation.
- **Threat intelligence gathering**: Surfaces relevant intelligence about threat actors, malware, and vulnerabilities based on natural language prompts, consolidating information into tailored summaries.
- **Script analysis and reverse engineering**: Explains suspicious scripts or command-line activity in plain language, identifies malicious behaviors, and highlights indicators of compromise.
- **KQL query generation**: Translates natural language prompts into ready-to-run KQL queries for advanced hunting and log analysis.
- **Security posture management**: Identifies prioritized risks and recommends actions to improve organizational security posture.
- **Security policy creation and management**: Assists in drafting, reviewing, and summarizing policies, and identifying gaps or conflicts.
- **Stakeholder reporting**: Generates reports tailored to different audiences, including technical summaries and executive briefings.
- **Promptbooks for repeatable security workflows**: Enables users to run or create multi-step workflows to standardize recurring security tasks.

## Models and training data

Microsoft Security Copilot uses Azure OpenAI large language models (LLMs) from Foundry Models sold by Azure to power natural language experiences. These models aren't trained on Security Copilot Customer Data. Model capabilities vary in reasoning, speed, limitations, and supported scenarios.

Security Copilot also incorporates security-specific knowledge and context through plugins and grounding, which provide the LLM with relevant organizational data, threat intelligence, and authoritative content at inference time rather than through model training.

## Performance

Security Copilot is designed to operate in enterprise security environments where large volumes of real-time security signals are generated across Microsoft Security products and other data sources configured by the organization.

Unlike general-purpose LLMs, Security Copilot provides:

- Real-time signal processing across structured security data
- Investigative reasoning that correlates multiple data sources
- Evidence-backed outputs grounded in customer data
- Continuous data collection for ongoing visibility

Users interact with Security Copilot using natural language prompts. The system processes these inputs through active plugins, data sources, and LLMs to generate responses.

Outputs are primarily textual including summary explanations, recommended actions, step-by-step guidance, code snippets (such as KQL queries), and formatted reports tailored to stakeholders. As the system generates a response, it displays intermediate steps in a process log, providing opportunities to double-check its processes and sources. Users can cancel, edit, rerun, or delete a prompt at any time, and responses can be pinned, shared, and exported to facilitate collaboration.

## Limitations

Understanding the limitations of Microsoft Security Copilot is important to ensure it is used effectively and responsibly. While Security Copilot enhances security workflows, it isn’t designed for every scenario. Refer to the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct) as well as the following considerations when choosing a use case:

- **Accuracy and completeness**: Security Copilot can produce responses that are inaccurate, incomplete, or outdated. Output quality depends on available data sources, enabled integrations, and user-provided context. Users should apply human judgment and validate critical outputs.
- **Bias, stereotyping, and ungrounded content**: Despite safeguards, outputs may contain bias, stereotypes, or unsupported conclusions due to the probabilistic nature of large language models. Users should critically evaluate responses, especially in sensitive or high-impact scenarios.
- **Domain-specific scope**: Security Copilot is optimized for security-related tasks such as incident investigation and threat analysis. Prompts outside this domain may result in less accurate or less relevant responses.
- **Usage limits and latency**: Use of Security Copilot may be subject to capacity constraints and performance considerations. Generating responses, including executing integrations and applying safety checks, may introduce latency. Organizations should monitor their usage (SCUs) to maintain consistent performance.
- **Preview status**: Some Security Copilot capabilities may be in preview. Preview features should be treated as prerelease functionality, and outputs should be reviewed before taking action.
- **Prompt and context constraints**: Security Copilot operates within token and context limits inherent to large language models. Long prompts or extended interactions may exceed these limits, resulting in truncated or less optimal responses. Reframing or simplifying prompts may improve outcomes.
- **Dependence on data sources and configuration**: Responses are grounded in available data, including connected Microsoft services, third-party integrations, and user input. If relevant data sources aren’t available, enabled, or current, results may lack completeness or accuracy.
- **Script and code generation**: Security Copilot may generate code or include code in responses. Responses may appear valid but might not be semantically or syntactically correct, or might not accurately reflect the intent of the requester. Generated code shouldn't be deployed into production environments without appropriate validation, testing, and review procedures. Users must also verify that any parameters used by the generated code align with the original request. For example, if an agent operates on alerts within a specific time range, confirm that the time range in the generated code matches the time range specified in the natural language prompt.
- **Data access and permission boundaries**: Security Copilot operates within existing organizational permissions and data access controls. Responses are limited to the data a user is authorized to access. Misconfigured permissions in underlying systems may affect the relevance or completeness of results.
- **Government cloud environments**: Security Copilot isn’t currently designed for use in certain government cloud environments.

## Evaluations

Performance and safety evaluations assess whether AI applications are operating reliably and securely by examining factors like groundedness, relevance, and coherence while identifying the risks of generating harmful content. The following evaluations were conducted with safety components already in place, which are also described in Safety Components and Mitigations.

### Evaluation data for quality and safety

Our evaluation data is custom-built to assess AI application performance across key areas of safety and quality, simulating real-world scenarios, and risks. We begin by identifying relevant evaluation aspects of concern based on multi-disciplinary research and expert input. These concerns are translated into targeted evaluation objectives and guide formulation of evaluation metrics.

For safety, we create adversarial prompts to elicit undesirable or edge-case responses, which are then scored using AI-assisted annotators trained to assess alignment with Microsoft’s safety standards. For quality, we craft rubric-based prompts relevant to scenarios including evaluating retrieval-augmented generation (RAG) applications and agents.

Datasets are curated from diverse sources including synthetic and public datasets to simulate real-world user scenarios. Using the curated datasets, both evaluations undergo iterative refinement and human alignment to improve metric efficacy and reliability. This methodology forms the foundation of repeatable, rigorous assessments that reflect how customers use evaluations to build better and safer AI.

### Custom evaluations

Custom evaluations were conducted to validate model performance across grounding, adversarial robustness, and harmful content scenarios using regression testing, curated prompt datasets, and production-aligned examples. The evaluation compared outputs between GPT models, using internal tools to assess **groundedness** and **Azure OpenAI content filtering** to validate protections against **jailbreak**, **prompt injection**, and **intellectual property violations**. Results show consistent or improved performance, including strong protection rates across adversarial scenarios and improved grounding accuracy.

Harmful content handling remains consistent across models and operates in annotation mode to support security-focused use cases, with additional large-scale testing confirming high protection rates across categories. Regression tests are conducted to verify that the content, which is not harmful isn’t getting classified as harmful.

User feedback is critical to improving Security Copilot. Users can provide feedback using: **Needs improvement**, **Inappropriate** or the **Looks right** options. This feedback goes directly to Microsoft and is used to improve the platform's performance through ongoing iterative refinement.

## Safety components and mitigations

As we identified potential risks and misuse through processes like red team testing and measured them, we developed mitigations to reduce the potential for harm. In the following list, we describe some of those mitigations. We will continue to evaluate the Microsoft Security Copilot experience to improve product performance and mitigations.

- **Harmful content filtering and guardrails**: Security Copilot integrates Microsoft-developed guardrails (content filters) and abuse detection models as part of the [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai/) foundation. These neural classification models detect and filter harmful content across categories including hate, sexual, violence, and self-harm at multiple severity levels. Optional classification models also detect jailbreak risks, known text or code material, and indirect prompt injection attacks. These layered controls help prevent the AI from producing responses that violate Microsoft's safety standards.
- **Safety system design**: Microsoft developed a safety system for Security Copilot that is designed to mitigate failures and prevent misuse, including harmful content annotation, operational monitoring, and other safeguards. The Azure OpenAI Service Responsible AI Mitigation Requirements do not apply to Security Copilot customers directly because Security Copilot implements these mitigations on the customer's behalf.
- **User feedback loop**: The platform provides built-in feedback mechanisms: **Needs improvement**, **Inappropriate**, and **Looks right** options that allow users to report problematic and useful outputs directly to Microsoft. This feedback drives continuous improvement cycles, enabling rapid fixes and model adjustments when errors or misalignments are discovered.
- **Data encryption and access protection**: Customer data handled by Security Copilot is encrypted both in transit and at rest as described in the Microsoft Products and Services Data Protection Addendum. By default, no human users have access to the database and network access is restricted to the private network where the Security Copilot application is deployed; if human access is needed (for incident response), elevated access and network access must be approved by authorized Microsoft employees. See [Compliance](/en-us/copilot/security/faq-data-compliance).
- **Phased deployment approach**: Security Copilot releases features through an invite-only early access program, allowing Microsoft to gather feedback and refine features before broader availability.

Our approach to mapping, measuring, and managing risks will continue to evolve as we learn more, and we're already making improvements based on feedback received from customers.

## Best practices for deploying and adopting Microsoft Security Copilot

Responsible AI is a shared commitment between Microsoft and its customers. While Microsoft builds AI systems with safety, fairness, and transparency at the core, customers play a critical role in deploying and using these technologies responsibly within their own contexts.

Security Copilot agents are designed to augment human expertise, not replace. Customers remain responsible for reviewing outputs, validating decisions, and ensuring compliance with applicable laws, regulations, and organizational policies.

Deployers and end users should:

- **Exercise caution and evaluate outcomes when using Security Copilot for consequential decisions or in sensitive domains**: Consequential decisions are those that may have a legal or significant impact on a person's access to employment, legal services, healthcare, or that could result in physical, psychological, or financial harm. Sensitive domains such as financial services, healthcare, and legal require particular care due to the potential for disproportionate impact on different groups of people. When using AI for decisions in these areas, customers should ensure that impacted stakeholders can understand how decisions are made, appeal decisions, and update any relevant input data.
- **Evaluate legal and regulatory considerations**: Customers need to evaluate potential specific legal and regulatory obligations when using any AI services and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI services or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.
- **Enable and maintain relevant plugins**: The quality and accuracy of Security Copilot responses depend significantly on the plugins that are enabled. Administrators should ensure that appropriate Microsoft and third-party plugins are configured and maintained so that users receive grounded, contextually relevant responses.

End users should:

- **Write effective prompts**: Writing clear, specific prompts is key to getting better outcomes with Security Copilot. Include relevant context such as incident IDs, asset names, or time ranges. Iterate and regenerate prompts as needed, and always review and verify AI-generated responses. For more information, see [Prompting tips for Security Copilot](prompting-tips).
- **Exercise human oversight when appropriate**: Human oversight is an important safeguard when interacting with AI systems. While we continuously improve Security Copilot, AI systems may make mistakes. The output generated may be inaccurate, incomplete, biased, or not fully aligned with your intended goals due to ambiguity in inputs or limitations of the underlying models. Users should review the responses generated by Security Copilot and verify that they match their expectations and requirements before taking action.
- **Be aware of the risk of overreliance**: Overreliance on AI occurs when users accept incorrect or incomplete AI outputs, mainly because mistakes in AI outputs may be hard to detect. For security professionals, overreliance could result in missed threats, incorrect incident conclusions, or policy changes based on flawed recommendations. Security Copilot includes AI disclosure and cites source materials to help mitigate this risk, but users should still make sure to verify the accuracy of responses. Users can review the agent node map that provides a high-level view of the steps performed during an agent's workflow.
- **Exercise caution when deploying or designing agentic AI in sensitive domains**: Users must implement appropriate human oversight, when configuring and deploying agentic AI systems in domains where agent actions are irreversible or highly consequential. Additional precautions should be taken when creating autonomous agentic AI as described in the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct).

Deployers should:

- **Configure RBAC and agent permissions carefully**: Administrators are responsible for configuring role-based access controls for both users and agents. Permissions should follow the principle of least privilege. Agents should only be granted access to the data and actions necessary for their designated task.
- **Monitor usage and review activity**: Administrators (owners) can use the Security Copilot usage monitoring dashboard to review session-level data such as usage over time, session initiators, and plugins used during sessions. This visibility helps organizations understand how Security Copilot is used across prompts, promptbooks, and agents. For more information, see [Manage usage](manage-usage).
- **Manage data sharing settings**: Owners can configure Customer Data sharing preferences at any time and must review and update these settings in accordance with their organization's privacy and compliance requirements. For more information, see [Privacy and data security in Microsoft Security Copilot](privacy-data-security).
- **Educate users on capabilities and limitations**: Effective and responsible use of Security Copilot requires users to understand what the system can and cannot do. Deployers should provide training and guidance to help users interact with Security Copilot effectively, including the importance of verifying AI-generated outputs before taking action.

## Learn more about Security Copilot

For additional guidance on the responsible use of Microsoft Security Copilot, see the following documentation:

- [What is Microsoft Security Copilot?](microsoft-security-copilot)
- [Privacy and data security in Microsoft Security Copilot](privacy-data-security)

### Learn more about responsible AI

- [Microsoft AI principles](https://fluent2.microsoft.design/responsible-AI/)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/tools-practices)
- [Microsoft Azure Learning courses on responsible AI](/en-us/ai)
- [AI Literacy](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)