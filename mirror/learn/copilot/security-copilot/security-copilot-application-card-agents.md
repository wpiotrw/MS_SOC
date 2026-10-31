---
layout: Conceptual
title: Application card for Microsoft Security Copilot agents | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how Microsoft Security Copilot agent works, including its intended uses, limitations, evaluations, and safety mitigations.
ms.date: 2026-08-09T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: responsible-ai-transparency​, msecd-doc-authoring-1023
ms.reviewer: spunukol
ai-usage: ai-assisted
search.audiencetype: Admin
locale: en-us
document_id: 39317292-a6ce-b141-a461-36026c401778
document_version_independent_id: 39317292-a6ce-b141-a461-36026c401778
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/security-copilot-application-card-agents.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: security-copilot-application-card-agents
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/security-copilot-application-card-agents.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 81875239-1002-03cf-b187-9572b11bb8e6
---

# Application card for Microsoft Security Copilot agents | Microsoft Learn

## What is an Application or Platform card?

Microsoft's Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to [six core principles](https://www.microsoft.com/ai/principles-and-approach/): fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. These principles are embedded in the [Responsible AI Standard](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf), which guides teams in designing, building, and testing AI applications. Application and Platform cards play a key role in operationalizing these principles by offering transparency around capabilities, intended uses, and limitations. For further insight, readers are encouraged to explore Microsoft's [Responsible AI Transparency Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Responsible-AI-Transparency-Report-2025.pdf) and the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct), which outlines how to engage with AI responsibly.

## Overview

Microsoft Security Copilot is a generative AI-powered security solution that helps increase the efficiency and capabilities of defenders to improve security outcomes at machine speed and scale. Security Copilot provides a natural language, assistive copilot experience that helps security professionals and IT administrators handle a wide range of end-to-end scenarios, including incident response, threat hunting, intelligence gathering, and posture management.

Security Copilot is designed with integration in mind and offers an immersive standalone experience at https://securitycopilot.microsoft.com. The platform seamlessly integrates with products in the Microsoft security portfolio, such as Microsoft Defender XDR, Microsoft Sentinel, Microsoft Intune, Microsoft Entra, and Microsoft Purview and supported third-party services.

A Security Copilot agent generates outputs and can perform actions based on configured logic, permissions, and triggers defined by the customer. Customers can use autonomous Security Copilot agents to automate security workflows, accelerate response times, prioritize risks, and reduce manual workloads, all while retaining full control. Agent autonomy refers to an agent’s ability to take actions independently within defined boundaries.

An administrator (Security Copilot owner) discovers and deploys agents through the Security Copilot portal and Security Store, with some agents also surfaced in embedded Microsoft security product experiences. The administrator sets the agent’s identity and configures role-based access control (RBAC) for the agent.

The intended users include SOC analysts, IT administrators, data security and identity administrators, compliance analysts, and security leaders such as Chief Information Security Officers (CISOs).

Security Copilot holds ISO 42001 certification, which confirms that an independent third party reviewed Microsoft's application of the necessary framework and capabilities to effectively manage risks and opportunities associated with the continuous development, deployment, and operation of Microsoft AI systems.

For more information, see [What is Microsoft Security Copilot?](microsoft-security-copilot), [Microsoft Security Copilot experiences](experiences-security-copilot), and [Application card for Security Copilot](/en-us/copilot/security/security-copilot-application-card).

## Key terms

The following table provides a glossary of key terms related to Microsoft Security Copilot agents.

| Term | Definition |
| --- | --- |
| Agent | A Security Copilot agent processes signals from the customer environment through integrated data sources and plugins, analyzes over data, and generates recommendations. Agents may also perform scoped actions within configured permissions when prompted, which require an appropriate user or administrator approval. Agents can range from simple prompt-and-response experiences to more automated, semi-autonomous workflows with human oversight. |
| Agent action | An operation executed by an agent, such as retrieving data, generating outputs, or modifying configurations, based on permissions. |
| Agent manifest | A configuration file that defines an agent's capabilities, tools, and behavior. It controls how the agent operates within the Security Copilot and is represented in a YAML file format. |
| Embedded experience | Accessing Security Copilot capabilities from within another Microsoft security product, such as Microsoft Defender XDR or Microsoft Sentinel. The Security Copilot sidecar panel surfaces AI assistance directly in the context of that product. |
| Grounding | The process of providing contextual input sources to the large language model related to a user's prompt. By enabling Security Copilot to access organizational data through plugins and Microsoft security products, Security Copilot can deliver more accurate and contextually relevant responses. |
| Large language model (LLM) | AI models trained on large amounts of text data to predict words in sequences. LLMs are capable of performing various tasks such as text generation, summarization, translation, classification, and more. |
| Partner-built agent | An agent published by Microsoft partners and made available through the Security Store to address specific security use cases. |
| Plugin | A collection of related tools that extends Security Copilot's capabilities by giving it access to resources from Microsoft and non-Microsoft services and public websites through APIs. Plugins add more context to the responses and outputs that Security Copilot generates. |
| Post-processing | The set of actions Security Copilot performs to refine and prepare the LLM response before returning it to the user. This post-processing includes additional grounding calls through plugins, responsible AI checks, security, compliance, and privacy checks. |
| Prompt | The natural language text a user sends to Security Copilot to execute a specific task or obtain information. For example, *Summarize this incident and suggest remediation steps.* |
| Promptbook | A series of prompts that run in sequence, building on previous responses, to accomplish specific security-related tasks. Promptbooks can be used from the library or built and shared by users. |
| Red team testing | Techniques used by experts to assess the limitations and vulnerabilities of a system and to test the effectiveness of planned mitigations. Red team testing is used to identify potential risks and is distinct from systematic measurement of risks. |
| Responsible AI | Microsoft's policy, research, and engineering practices that are grounded in its AI principles and operationalized through the [Responsible AI standard](https://www.microsoft.com/ai/responsible-ai). For more information, see the [Fluent RAI guidance](https://fluent2.microsoft.design/responsible-AI/). |
| Security Compute Unit (SCU) | SCUs are the units of compute capacity used to run Security Copilot workloads and deliver consistent performance across its experiences. Security Copilot capacity is measured in SCUs and can be consumed through provisioned or overage capacity models. For more information, see [Understand SCUs](/en-us/copilot/security/security-compute-units-capacity). |
| Security Operations Center (SOC) | A dedicated security team or facility focused on continuous monitoring, analysis, and response to cybersecurity incidents within an organization. SOC analysts are among the primary intended users of Security Copilot. |
| Standalone experience | The immersive Security Copilot portal experience accessed directly at https://securitycopilot.microsoft.com. |
| Tenant | The organizational boundary in Microsoft Entra ID that isolates identity, access, and data for Security Copilot. The tenant governs all workspaces, users, and interactions through tenant-level permissions and security controls. |
| Trigger | An event or condition that tells an agent to start executing its workflow. Triggers can be time-based (for example, a weekly schedule for the Threat Intelligence Briefing Agent) or manual (run on demand by a user or administrator). The trigger is configured during agent setup. |

## Key features or capabilities

The key features and capabilities in the following table describe what Microsoft Security Copilot is designed to do and how it performs across supported tasks.

| Feature or capability | Description |
| --- | --- |
| Incident investigation and response | Security Copilot helps security professionals triage and investigate incidents by generating summaries of complex security alerts, correlating signals across Microsoft Defender XDR, Microsoft Sentinel, and other integrated products, and providing step-by-step remediation guidance. |
| Threat intelligence | Security Copilot can search across Microsoft Defender threat intelligence articles and profiles, threat analytics reports, and vulnerability disclosure publications to surface relevant intelligence aligned to a prompt. |
| Security Alert Triage | Security Copilot includes the Security Alert Triage Agent to help security teams triage alerts at scale by identifying real attacks and false positives, enabling analysts to focus on investigating real threats with transparent, step-by-step reasoning to support every decision. |
| Script analysis and KQL query generation | Security Copilot can analyze suspicious scripts or malware and translate natural language into KQL queries, enabling team members at all skill levels to perform advanced hunting and technical analysis tasks. |
| Security posture management | Security Copilot helps users understand prioritized risks across their environment and identify opportunities to improve posture through integration with Microsoft Defender XDR, Microsoft Entra, and Microsoft Intune. |
| Security policy creation and management | Users can define new policies, cross-reference them with existing policies for conflicts, and summarize policies in plain language to manage complex organizational context. |
| Stakeholder reporting | Security Copilot can generate reports that summarize context, open issues, and protective measures tailored to the intended audience, such as executives or security teams. |
| Promptbooks | Promptbooks are sequences of prompts that run in order to accomplish specific security tasks. Users can run promptbooks from a shared library or create and share their own. |
| Agents | Security Copilot supports agents that automate and assist with security and IT operations tasks within the permissions granted by administrators. An agent takes actions through configured identities, access controls, and triggers, and operate with human oversight as part of security workflows.  Microsoft-built agents span the security product portfolio, covering SOC operations, threat hunting, threat intelligence, identity management, endpoint management, and data security. Administrators configure each agent’s identity, permissions, and trigger during setup. Users can review an agent’s triggers, data access, identity, and action permissions (such as read or write) to understand how the agent operates within its defined scope. For details on specific agents and their use cases, see Intended uses. |
| Multi-language support | Security Copilot supports prompting and responses in multiple languages. For more information, see [Supported languages](supported-languages). |

Security Copilot is an AI-powered security solution that operates both assistively and as an autonomous agentic system. To understand agent autonomy, consider:

- **Activation triggers** – what conditions or user actions cause the agent to run
- **Access permissions** – what data, systems, or resources the agent can use
- **Action rights** – what actions the agent is authorized to take on its own

The following sections describe the core agentic capabilities that underpin how agents reason, plan, remember, adapt, and extend their reach.

### Reasoning

Security Copilot agents use the underlying large language model to analyze available context, evaluate signals, and determine the most appropriate course of action. For example, the Phishing Triage Agent assesses email content, sender reputation, and behavioral signals to produce a classification verdict with a natural language rationale. Agents surface their reasoning transparently so that analysts can review, validate, or override conclusions before acting on them.

### Planning

Agents operate against defined triggers that instruct the agentic system to initiate a structured sequence of actions toward a goal. Agents can be configured to:

- Run automatically on a schedule (for example, the Threat Intelligence Briefing Agent runs every seven days).
- Run manually on demand when needed.

This design gives agents a goal-directed execution model where the system analyzes when and how to act to complete its task.

### Memory

Security Copilot agents can retain information over time, referred to as memory. Memory allows an agent to incorporate past inputs into future behavior, depending on how the agent is designed and configured.

Memory can include feedback provided by users. Agents can use this feedback to adjust their responses or actions in subsequent interactions.

### Adaptability

Security Copilot agents are designed to adapt based on user feedback and operational context, while continuing to operate within the scope defined by their configured identity, permissions, and triggers.

- **Feedback loop**: Security Copilot Owners and Contributors can provide feedback on an agent’s responses. This feedback is stored in the agent’s memory and can influence future outputs, depending on the agent design and configuration.
- **Contextual grounding**: During prompt processing, Security Copilot enriches prompts using grounding. This process incorporates relevant organizational data, enabled plugins, and threat intelligence so that responses reflect the current context.
- **Configurable identity and permissions**: Agents can be updated after setup to modify identity, triggers, and parameters. This enables agents to align with evolving workflows and requirements.

### Extensibility

- **Plugins**: Agents use plugins to reach external services via APIs, including reputation lookups, threat intelligence, and endpoint data. Both Microsoft-built and partner-built plugins are supported. For more information, see [Plugins overview](plugin-overview).
- **Connectors**: Logic Apps and Copilot Studio connectors wrap the Security Copilot API, enabling developers and users to call into the platform from external automation workflows. For more information, see [Connectors overview](connectors-overview).
- **Custom agents**: Developers can build custom agents tailored to specific use cases and add them to the Security Copilot ecosystem via the developer platform. For more information, see [Develop custom agents](/en-us/copilot/security/developer/custom-agent-overview).
- **Security Store**: Prebuilt Microsoft and partner agents can be discovered and deployed from the built-in agent library and Security Store.
- **Embedded experiences**: Agents operate not only in the Security Copilot standalone portal but are also embedded across the broader Microsoft security ecosystem, including Microsoft Defender XDR, Microsoft Sentinel, Microsoft Intune, Microsoft Entra, and Microsoft Purview.

## Intended uses

Microsoft Security Copilot agents are designed for security professionals and IT administrators to support security workflows, such as intelligence gathering and correlation. Agents can operate within administrator-defined permissions, and help streamline tasks that might otherwise require significant manual effort, while keeping humans in control. Some examples of intended agent use cases include:

- **Threat intelligence briefing**: The **Threat Intelligence Briefing Agent** generates timely, detailed threat intelligence reports by correlating Microsoft Defender Threat Intelligence data, Defender External Attack Surface Management (EASM) signals, and real-time customer context. Security analysts can use this agent to replace hours or days of manual intelligence gathering and correlation with a report generated in minutes.
- **Security data analysis (Microsoft Defender XDR)**: The **Security Analyst Agent** helps security analysts quickly identify, assess, and prioritize risks across large volumes of security data. The agent performs both basic analysis tasks such as pattern analysis, trend analysis, and visualization, and advanced tasks such as anomaly detection, clustering, risk scoring, and predictive modeling. It integrates data from Microsoft Defender XDR, Microsoft Sentinel Log Analytics, Microsoft Sentinel Data Lake, and uploaded CSV files, generating prioritized insights with a full evidence trail in an interactive, code-free chat experience.
- **Security operations and incident response (Microsoft Defender XDR)**:

    - The **Phishing Triage Agent** evaluates user-reported phishing emails as they're submitted, classifies verdicts with transparent reasoning, and incorporates analyst feedback over time. The **Security Alert Triage Agent (Preview)** extends the same triage approach beyond phishing to a subset of identity alerts and cloud container alerts.
    - The **Dynamic Threat Detection Agent** runs continuously in the background to uncover hidden threats and gaps across Defender and Microsoft Sentinel environments by correlating alerts, events, anomalies, and threat intelligence.
- **Threat hunting (Microsoft Defender XDR)**: The **Threat Hunting Assistant** enables end-to-end threat hunting using natural language. It generates KQL queries, interprets results, surfaces insights, and guides analysts through full hunting sessions to find threats faster and with greater confidence.
- **Identity and access management (Microsoft Entra)**:

    - The **Conditional Access Optimization Agent** analyzes conditional access policies and recommends improvements based on Microsoft best practices and Zero Trust principles.
    - The **Identity Risk Management Agent** helps identity administrators investigate potential risks and take action to protect critical assets.
- **Endpoint management (Microsoft Intune)**:

    - The **Vulnerability Remediation Agent** uses Defender data to monitor vulnerabilities and prioritize remediation with AI-driven risk assessments.
    - The **Policy Configuration Agent** lets administrators import documents or write plain-language instructions to find matching settings in the Intune settings catalog and create policies.
    - The **Change Review Agent** evaluates the effect of approval requests in Intune and makes recommendations for actions administrators can take.
- **Data security investigation (Microsoft Purview)**:

    - The **Triage Agent in Insider Risk Management** evaluates alerts based on user, file, and activity risk, automatically sorting them into prioritized categories to help security teams focus on the highest-risk cases.
    - The **Purview Triage Agent in Data Loss Prevention** evaluates DLP alerts based on sensitivity risk, exfiltration risk, and policy risk, helping data security administrators act on the most critical incidents.
- **Custom agentic workflows**: Developers can build and deploy custom agents using natural language processing, uploading the agent manifest, or using the MCP tools tailored to their organization's specific security use cases, extending agent capabilities through plugins and connectors to Microsoft and non-Microsoft services. For more information, see [Custom agents](/en-us/copilot/security/developer/custom-agent-overview).

    You can also build an interactive chat agent when agents and users need to collaborate for a guided experience to solve something. For more information, see [Interactive Agent](/en-us/copilot/security/developer/interactive-agents-overview).

## Models and training data

Microsoft Security Copilot uses Azure OpenAI large language models (LLMs) from Foundry Models sold by Azure to power natural language experiences. These models aren't trained on Security Copilot Customer Data. Model capabilities vary in reasoning, speed, limitations, and supported scenarios.

Security Copilot also incorporates security-specific knowledge and context through plugins and grounding, which provide the LLM with relevant organizational data, threat intelligence, and authoritative content at inference time rather than through model training.

## Performance

Security Copilot is designed to operate in enterprise security environments where large volumes of real-time security signals are generated across Microsoft Security products and other data sources configured by the organization. It integrates signals from these sources, combining real-time processing of structured log data with investigative reasoning. This is designed to help detect, analyze, and trace the source and impact of security incidents across multiple data sources.

Security Copilot runs on Microsoft’s hyperscale infrastructure and a security-specific orchestration layer, which are intended to support scalable, resilient performance across repeated threat detection and investigation scenarios.

Agents extend Security Copilot’s ability to act on security signals by executing defined security tasks through administrator-configured permissions. Agents reason over available signals, plan and execute structured actions, and produce outputs such as triage decisions, intelligence reports, and remediation guidance grounded in real-time organizational and threat intelligence data. Agent execution is transparent through step-by-step node maps, allowing analysts to review generated steps (not an in-depth summary of the specific actions taken at each node) and validate outcomes across runs.

Performance reliability is further supported through preconfigured Microsoft-built agents, which are tested against representative workflows, and custom agents, where a manifest YAML file can help promote more consistent behavior by specifying capabilities, tools, triggers, and operational boundaries. When manifest instructions are clearly defined, the agent may be better able to interpret its task, select appropriate actions, and operate within its intended scope. For more information, see [Custom agents](/en-us/copilot/security/developer/custom-agent-overview).

For interactive agents, performance is shaped primarily through the iterative exchange between the agent and the user. The agent produces an initial response, and the user refines context through follow-up prompts based on what the agent surfaces. This back-and-forth interaction allows the user to incrementally guide the agent toward more accurate and targeted outcomes than a single autonomous run would produce. For more information, see [Interactive agents](/en-us/copilot/security/developer/interactive-agents-overview).

## Limitations

Understanding Security Copilot's limitations are important to ensure it's used within safe and effective boundaries. While customers are encouraged to use Security Copilot in their security workflows, it's important to note that Security Copilot wasn't designed for every possible scenario. Refer to the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct) as well as the following considerations when choosing a use case:

- **Public preview status**: Some agents are in public preview and may be substantially modified before general availability. Microsoft makes no warranties, express or implied, with respect to these capabilities. As with any AI output, customers must review the decision making of the agent prior to acting upon its outputs.
- **Accuracy and completeness**: Like any AI-powered technology, Security Copilot doesn't get everything right. Responses may be inaccurate, incomplete, or outdated, particularly if the relevant plugins aren't enabled or if the most current data isn't available through user input or organizational context. Users should always exercise human judgment and verify critical outputs rather than relying solely on AI-generated response.
- **Domain-specific scope**: Security Copilot is designed to respond to prompts related to the security domain, such as incident investigation and threat intelligence. Prompts outside the scope of security may result in responses that lack accuracy and comprehensiveness.
- **Script and code generation**: Security Copilot may generate code or include code in responses. Responses may appear valid but might not be semantically or syntactically correct, or might not accurately reflect the intent of the requester. Generated code shouldn't be deployed into production environments without appropriate validation, testing, and review procedures. Users must also verify that any parameters used by the generated code align with the original request. For example, if an agent operates on alerts within a specific time range, confirm that the time range in the generated code matches the time range specified in the natural language prompt.
- **Prompt-length constraints**: The system may not be able to process long prompts, such as those containing hundreds of thousands of characters. The underlying LLM has a token limit, and overly verbose queries or extended sessions can overflow the token space. When this scenario happens, Security Copilot attempts to apply mitigations to ensure an output is always available, even if the content isn't optimal; however, those mitigations are not always effective, and it might be necessary to try a different prompt or plugin.
- **Usage limits and latency**: Use of the platform may be subject to usage limits or capacity throttling. Generating responses, including making API calls through plugins and checking responses before displaying them, can take time and require high GPU capacity. Organizations should monitor their SCU consumption and adjust provisioned capacity as needed to avoid unexpected service interruptions.
- **Bias, stereotyping, and ungrounded content**: Despite the implementation of responsible AI controls on both user prompts and LLM outputs, AI services are fallible and probabilistic. This makes it challenging to comprehensively block all inappropriate content, which may lead to potential biases, stereotypes, or ungrounded content in AI-generated output.
- **Government and Microsoft Sovereign Public/Private Cloud**: Security Copilot isn't supported in these environments at this time.
- **Task-specific agent boundaries**: The agents are suitable only for the specific task they're designed to perform. For more information, see the intended use cases section. They aren't suitable for any other task and shouldn't be repurposed beyond their defined scope.
- **Node map detail**: The agent node map provides a high-level view of the steps performed during an agent workflow. Each node represents a step in the process and displays the title of the skill used, along with basic metadata such as completion status, duration, and timestamp. The node map is designed to show the sequence of actions, but it doesn't provide detailed information about the specific operations or decisions made within each step. Because the node map presents only summarized information, it may not fully capture the context or complexity of each action.
- **Agent feedback and memory transparency**: When users submit feedback to an agent for storage in memory, the agent doesn't provide a summary of its interpretation of the feedback. To increase accuracy of future outputs, users should provide feedback that's clear, concise, and specific. Feedback submitted to an agent may be stored and used to influence future outputs. However, visibility into this stored feedback can vary depending on the agent experience and user role. For more information, see [Provide feedback](agents-manage#provide-feedback).

## Evaluations

Performance and safety evaluations assess whether AI applications are operating reliably and securely by examining factors like groundedness, relevance, and coherence while identifying the risks of generating harmful content. The following evaluations were conducted with safety components already in place, which are also described in Safety Components and Mitigations.

### Evaluation data for quality and safety

Our evaluation data is custom-built to assess AI application performance across key areas of safety and quality, simulating real-world scenarios, and risks. We begin by identifying relevant evaluation aspects of concern based on multi-disciplinary research and expert input. These concerns are translated into targeted evaluation objectives and guide formulation of evaluation metrics.

For safety, we create adversarial prompts to elicit undesirable or edge-case responses, which are then scored using AI-assisted annotators trained to assess alignment with Microsoft’s safety standards. For quality, we craft rubric-based prompts relevant to scenarios including evaluating retrieval-augmented generation (RAG) applications and agents.

Datasets are curated from diverse sources including synthetic and public datasets to simulate real-world user scenarios. Using the curated datasets, both evaluations undergo iterative refinement and human alignment to improve metric efficacy and reliability. This methodology forms the foundation of repeatable, rigorous assessments that reflect how customers use evaluations to build better and safer AI.

### Custom evaluations

Custom evaluations were conducted to validate model performance across grounding, adversarial robustness, and harmful content scenarios using regression testing, curated prompt datasets, and production-aligned examples. The evaluation compared outputs between GPT models, using internal tools to assess **groundedness** and **Azure OpenAI content filtering** to validate protections against **jailbreak**, **prompt injection**, and **intellectual property violations**. Results show consistent or improved performance, including strong protection rates across adversarial scenarios and improved grounding accuracy.

Harmful content handling remains consistent across models and operates in annotation mode to support security-focused use cases, with additional large-scale testing confirming high protection rates across categories. Regression tests are conducted to verify that the content, which isn't harmful isn’t getting classified as harmful.

Security Copilot agents were evaluated by its product and research team with use cases and design inputs from customers. The security of the agent system was also assessed through a dedicated red teaming exercise. Microsoft also completed penetration testing on the Security Copilot service to validate protection against unauthorized access.

Now that Security Copilot is released, user feedback is critical in helping Microsoft improve the system. Users have the option of providing feedback on the agent response from Security Copilot. This feedback goes directly to Microsoft and is used to improve the platform's performance through ongoing iterative refinement. For more information, see [Provide feedback](agents-manage#provide-feedback).

## Safety components and mitigations

As we identified potential risks and misuse through processes like red team testing and measured them, we developed mitigations to reduce the potential for harm. We'll continue to evaluate the Microsoft Security Copilot experience to improve product performance and mitigations. The following list describes some of those mitigations:

- **Harmful content filtering and guardrails**: Security Copilot integrates Microsoft-developed guardrails (content filters) and abuse detection models as part of the [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai/) foundation. These neural classification models detect and filter harmful content across categories including hate, sexual, violence, and self-harm at multiple severity levels. Optional classification models also detect jailbreak risks, known text or code material, and indirect prompt injection attacks. These layered controls help prevent the AI from producing responses that violate Microsoft's safety standards.
- **Designed to minimize irreversible actions**: Microsoft-designed agent scenarios are intended to minimize irreversible actions and keep users in control of critical decisions. For custom agents, non-Microsoft designed agents the agent developers can modify agent behavior to ensure irreversible actions are minimized.
- **Safety system design**: Microsoft developed a safety system for Security Copilot that is designed to mitigate failures and prevent misuse, including harmful content annotation, operational monitoring, and other safeguards. The Azure OpenAI Service Responsible AI Mitigation Requirements don't apply to Security Copilot customers directly because Security Copilot implements these mitigations on the customer's behalf.
- **User feedback loop**: After an agent returns a response, users can provide feedback. Depending on the configuration, users may also submit additional written feedback to provide context on their experience. Submitted feedback is collected and used by Microsoft to improve product quality, identify issues, and prioritize enhancements to Security Copilot experiences.
- **Agent identity governance and Role-based access control (RBAC)**: Each Security Copilot agent runs under either a managed identity or a user account, enabling the administrator to govern the data it has access to. Each agent has RBAC controls, and the agents may be further restricted as to what data they process. By confining each agent's permissions, the system mitigates risks of unauthorized data exposure and ensures all automated actions are auditable and traceable.
- **Data encryption and access protection**: Customer data handled by Security Copilot is encrypted both in transit and at rest as described in the Microsoft Products and Services Data Protection Addendum. By default, no human users have access to the database and network access is restricted to the private network where the Security Copilot application is deployed; if human access is needed (for incident response), elevated access and network access must be approved by authorized Microsoft employees. See [Compliance](/en-us/copilot/security/faq-data-compliance).
- **Phased deployment approach**: Security Copilot releases features through an invite-only early access program, allowing Microsoft to gather feedback and refine features before broader availability.

Our approach to mapping, measuring, and managing risks continue to evolve as we learn more, and make improvements based on feedback received from customers.

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

## Learn more about Security Copilot agents

For more information on the responsible use of Microsoft Security Copilot, see the following documentation:

- [What is Microsoft Security Copilot?](microsoft-security-copilot)
- [Build custom agents](/en-us/copilot/security/developer/custom-agent-overview)
- [Privacy and data security in Microsoft Security Copilot](privacy-data-security)

### Learn more about responsible AI

- [Microsoft AI principles](https://fluent2.microsoft.design/responsible-AI/)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/tools-practices)
- [Microsoft Azure Learning courses on responsible AI](/en-us/ai)
- [AI Literacy](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)