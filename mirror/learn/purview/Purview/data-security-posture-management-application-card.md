---
layout: Conceptual
title: Application card for Microsoft Purview Data Security Posture Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-application-card
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: soqureshi
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.date: 2026-04-16T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection: msec-ai-copilot
ms.custom: responsible-ai-transparency
ai-usage: ai-assisted
description: Application card for Microsoft Purview Data Security Posture Management that describes AI capabilities, intended uses, limitations, evaluations, safety components, and best practices.
locale: en-us
document_id: 43564125-15a2-90ae-d3db-f27a19fde434
document_version_independent_id: 43564125-15a2-90ae-d3db-f27a19fde434
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-application-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-application-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-application-card.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 8159c0ac-2151-bc99-e06e-cedd25360eeb
---

# Application card for Microsoft Purview Data Security Posture Management | Microsoft Learn

## What is an Application or Platform Card?

Microsoft's Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to six core principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. These principles are embedded in the Responsible AI Standard, which guides teams in designing, building, and testing AI applications. Application and Platform Cards play a key role in operationalizing these principles by offering transparency around capabilities, intended uses, and limitations. For further insight, readers are encouraged to explore Microsoft's [Responsible AI Transparency Report](https://www.microsoft.com/ai/responsible-ai) and [Code of Conduct](/en-us/legal/ai-code-of-conduct), which outline how enterprise customers and individuals can engage with AI responsibly.

## Overview

Microsoft Purview Data Security Posture Management is a data security application within the Microsoft Purview portal that helps organizations discover, protect, and investigate sensitive data risks across their digital estate. Rather than focusing on infrastructure or endpoints, Data Security Posture Management centers on the data itself, identifying where it resides, who can access it, how it's used, and whether it's adequately protected. It uses AI to analyze access patterns, sharing behaviors, and policy gaps in order to surface actionable risks and recommend remediation steps.

Data Security Posture Management addresses a growing challenge in today's AI-driven workplaces: the increasing complexity and volume of data makes it difficult for security teams to maintain visibility and control. The application solves this problem by consolidating insights from multiple Microsoft Purview solutions, including data loss prevention (DLP), Insider Risk Management, information protection with sensitivity labels, and Data Security Investigations, into a single view for monitoring data risks, policy coverage, and posture trends. This unified approach replaces the need for multiple tools and manual audits, helping administrators close data security gaps more efficiently.

Data Security Posture Management is designed to perform reliably in enterprise environments where organizations need to monitor and protect sensitive data across multiple locations. The application includes an embedded Microsoft Security Copilot experience that allows these users to ask natural language questions about their data security posture, as well as AI agents from Security Copilot that can take guided remediation actions on detected risks. For an overview introduction, see the Microsoft Mechanics video: [New Data Security Posture Management](https://www.youtube.com/watch?v=NLfoFpFxhrA).

## Key terms

The following list provides a glossary of key terms related to Data Security Posture Management:

**AI observability**: A feature within Data Security Posture Management that provides an inventory of AI apps and agents with recent activity, showing how many are high risk and the total with sensitive interactions, along with a breakdown of individual agents and the policies governing them.

**Collection policy**: A policy that captures prompts and responses from AI interactions for Copilot in Fabric and Security Copilot, and for non-Copilot AI apps, so they can be managed in Microsoft Purview solutions.

**Copilot interactions**: Prompts and responses from Copilots and agents that Microsoft Purview supports for data security and compliance protections. Includes Microsoft 365 Copilot, Security Copilot, Copilot in Fabric, Copilot Studio.

**Data loss prevention (DLP)**: A Microsoft Purview solution that helps prevent users from inappropriately sharing sensitive data by using content analysis techniques including keyword matching, expression evaluation, and machine learning algorithms.

**Data risk assessment**: An automated or custom scan that identifies and helps fix potential data oversharing risks, particularly for SharePoint sites and Fabric workspaces. Default assessments run weekly for the top 100 sites based on usage.

**Data security objectives**: Guided workflows within Data Security Posture Management that each represent a specific security goal, such as preventing data exposure in Copilot interactions or preventing oversharing. Each objective groups together relevant Microsoft Purview solutions and prioritized actions.

**Data Security Posture Agent**: A Microsoft Security Copilot agent exclusive to the current version of Data Security Posture Management that uses natural language search across files in SharePoint, OneDrive, Teams, Exchange, and Copilot interactions. It is designed for pre-investigation checks rather than formal cases.

**Insider Risk Management**: A Microsoft Purview solution that uses built-in service and third-party indicators to help identify, triage, and act on potentially risky activity by users in an organization.

**One-click policy**: A preconfigured policy within Data Security Posture Management that can be activated with a single click to quickly gain insights and protect data, without requiring manual policy configuration.

**Promptbook**: A built-in sequence of prompts for Microsoft Security Copilot that helps users quickly investigate specific data security scenarios, such as risky user behavior or sensitive data protection.

**Security Copilot**: Microsoft Security Copilot and its agents is a generative AI-powered security solution that helps data security professionals investigate and respond to security incidents. Within Data Security Posture Management, it provides an open-ended prompt experience for asking natural language questions about data security.

**Sensitivity label**: A label from Microsoft Purview Information Protection that can be applied to content to define and enforce protection policies for sensitive data across clouds, apps, and devices.

## Key features or capabilities

The key features and capabilities outlined here describe what Data Security Posture Management is designed to do and how it performs across supported tasks.

- **Data security posture dashboard**: The central landing page that provides immediate access to key posture metrics, top objectives to address based on risk, a snapshot of data usage across the data estate, and a 30-day trending graph of the organization's data security posture. Users can interact directly with Security Copilot through suggested prompts on this page.
- **Data security objectives with guided workflows**: Selectable cards that each represent a specific security goal, such as preventing data exposure in Copilot interactions, preventing oversharing of sensitive data, preventing exfiltration to risky locations, and discovering sensitive data. Each objective provides an end-to-end workflow with prioritized actions, one-click policies, and progress tracking, so users can focus on achieving outcomes rather than navigating separate solutions.
- **AI observability**: An inventory of AI apps and agents with activity in the last 30 days, showing how many are high risk and the total with sensitive interactions. Provides a breakdown of individual agents, their activities, and the policies governing them, enabling administrators to monitor risks such as oversharing, exfiltration, and unusual access patterns.
- **Data risk assessments**: Automated and custom scans that identify potential data oversharing risks. Default assessments run weekly for the top 100 SharePoint sites based on usage. Custom assessments can target specific users, sites, or Fabric workspaces. Results include remediation options such as restricting access by label, creating auto-labeling policies, or creating retention policies.
- **Data security recommendations and remediation actions**: Insights and recommendations generated from processed data that help administrators create or refine DLP and Insider Risk Management policies. Includes one-click policies for quick deployment directly from the Data Security Posture Management workflow.
- **Reports and analytics**: Tracks the organization's data security posture over time with reports summarizing sensitivity label usage, DLP policy coverage, risky user behavior, and AI app activity. Enhanced reporting provides advanced filtering, customizable views, and export capabilities to support compliance requirements.
- **Activity explorer**: Provides detailed visibility into content-related activity, including AI interactions (prompts, responses, and sensitive information detected), DLP rule matches, AI website visits, and sensitive information type detections. Supports filtering by workload categories such as Copilot experiences, enterprise AI apps, and other AI apps.
- **Data Security Posture Agent**: An AI-powered agent from Microsoft Security Copilot and that uses natural language search to find sensitive data across SharePoint, OneDrive, Teams, Exchange, and Copilot interactions. It provides item counts, sensitivity label classifications, and risk-level assessments, along with exportable insight reports. This agent is designed for quick, pre-investigation checks.
- **Embedded Security Copilot experience**: An open-ended prompt experience where users can ask natural language questions about their data security posture. Includes built-in promptbooks for risky user investigation and sensitive data protection, as well as a prompt gallery with categorized prompts for alerts, data at risk, risky users, suspicious activity, and sensitive data.
- **AI agent-driven remediation**: Under user guidance, AI agents can take direct action on detected risks, such as removing public sharing links, applying DLP policies, or revoking permissions. AI-driven triage agents review alerts from DLP and Insider Risk Management, filtering noise and highlighting critical threats. All agent actions are audited and subject to user review and approval.

## Intended uses

Data Security Posture Management can be used in multiple scenarios across a variety of industries. Some examples of use cases include:

- **Monitoring data security posture across the enterprise**: A compliance officer at a financial services organization uses Data Security Posture Management to get a unified view of their sensitive data across different locations. The posture dashboard surfaces key metrics and trends, enabling the officer to quickly identify where unprotected sensitive data exists and track improvements over time. This eliminates the need to manually review multiple separate tools and dashboards.
- **Preventing oversharing before deploying Microsoft 365 Copilot**: An IT administrator preparing for a Microsoft 365 Copilot deployment runs data risk assessments to identify SharePoint sites with potentially overshared content. Data Security Posture Management surfaces sites where sensitive files have broad sharing links or lack sensitivity labels, and provides one-click remediation options such as restricting access or creating auto-labeling policies. This helps the organization reduce data exposure before AI tools begin processing that content.
- **Investigating risky user behavior with AI-assisted analysis**: A data security analyst receives an alert about a user performing unusual file-sharing activities. Using the embedded Security Copilot experience, the analyst runs the risky user investigation promptbook, which automatically analyzes the user's sensitive data activities, identifies potential exfiltration patterns, checks for anomalies, and suggests protective actions, all through a sequence of natural language prompts.
- **Governing AI app usage across the organization**: A security team at a healthcare organization uses AI observability to monitor which AI apps and agents employees are interacting with, which of those interactions involve sensitive patient data, and whether appropriate DLP policies are in place. The team uses data security objectives to create targeted policies that prevent sensitive health information from being shared with unauthorized AI applications.
- **Responding to compliance requirements**: A compliance team at a government agency uses Data Security Posture Management reports and activity explorer to demonstrate that sensitive data is appropriately labeled, protected by DLP policies, and monitored for risky activity. The export capabilities and customizable views allow the team to generate audit-ready documentation aligned with their regulatory obligations.
- **Discovering unprotected sensitive data in new environments**: An organization just getting started with Microsoft Purview uses Data Security Posture Management to automatically scan data and user activities, gaining baseline insights and recommendations focused on unprotected data. This helps the organization quickly establish DLP, information protection, and Insider Risk Management policies without conducting deep manual analysis.

Data Security Posture Management is not intended for use as a general-purpose AI assistant, for scenarios unrelated to data security within Microsoft Purview, or for formal legal investigations (which require dedicated solutions such as eDiscovery and Data Security Investigations).

## Models and training data

Data Security Posture Management leverages existing AI agents and AI functionality. As such, it's dependent on any external configuration that these provide. For example, model choice for [Microsoft Security Copilot](/en-us/copilot/security/security-copilot-application-card) for the embedded natural language prompt experience. Data Security Posture Management also uses content analysis within [Data Loss Prevention](dlp-learn-about-dlp) for detecting sensitive information through keyword matching, expression evaluation, and machine learning algorithms. To learn more, refer to the linked application cards and documentation.

## Performance

Data Security Posture Management is designed to perform reliably in enterprise environments where organizations need to monitor and protect sensitive data across multiple locations. The application processes and correlates data from existing Microsoft Purview solutions, including DLP, Insider Risk Management, and information protection, to generate insights, recommendations, and posture metrics. Performance is optimized for organizations using supported Microsoft cloud services, and results improve as more Microsoft Purview solutions are configured and more data is available for analysis.

The application accepts text-based inputs across its features. Users interact with Data Security Posture Management through the Microsoft Purview portal interface, where they can navigate dashboards, configure policies, and run data risk assessments. The embedded Security Copilot experience accepts natural language text prompts and returns text-based responses, including data summaries, risk analysis, and recommended actions. The Data Security Posture Agent accepts natural language search queries and returns structured results, including item counts, sensitivity label classifications, and risk-level assessments, with an option to export reports as Word documents.

Data Security Posture Management supports the languages available in the Microsoft Purview portal interface. The Security Copilot experience is designed and evaluated primarily for English-language prompts and responses. Sensitive information type detection supports multiple languages as documented in the individual sensitive information type definitions. Users should be aware that performance of the natural language prompt and search features may vary when using languages other than English.

After initial setup, Data Security Posture Management requires time to process organizational data. Scanning times vary based on the size of the organization and the amount of data and activities to process, and it may take up to three days for initial processing to complete. New policies require at least 24 hours to collect data before results appear. Data risk assessments require at least 48 hours after completion before updated results are available. The Data Security Posture Agent can search up to 1 GB of content per query, and restricted searches targeting specific users or sites perform significantly faster than tenant-wide searches.

## Limitations

Understanding Data Security Posture Management's limitations is crucial to determine it is used within safe and effective boundaries. While we encourage customers to leverage Data Security Posture Management in their innovative solutions or applications, it's important to note that Data Security Posture Management was not designed for every possible scenario. We encourage users to refer to either the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct) (for organizations) or the Code of Conduct section in the [Microsoft Services Agreement](https://www.microsoft.com/servicesagreement) (for individuals) as well as the following considerations when choosing a use case:

- **Data security scope**: The Security Copilot experience in Data Security Posture Management is designed to answer questions about data security associated with Insider Risk Management, Information Protection, and Data Loss Prevention in Microsoft Purview. All other Purview solutions are currently out of scope for Data Security Posture Management insights. Users should direct questions outside of these areas to the appropriate solution-specific tools.
- **Data coverage**: The asset explorer Standard tab is filtered by Microsoft and non-Microsoft locations. Microsoft locations currently include Microsoft 365 only. Non-Microsoft locations are made possible by integration with partner solutions. Organizations with significant data in environments that aren't included should be aware that visibility through the asset explorer may be limited and should supplement with other tools as needed.
- **Data risk assessment volume limits**: A maximum of 200,000 items per location applies to both custom and default data risk assessments. The reported file count may not be accurate when there are more than 100,000 files per location. Organizations with very large SharePoint sites should consider running multiple targeted assessments. Additionally, OneDrive is not currently supported for item-level scanning, and custom assessments support a maximum of 10 SharePoint sites for item-level scanning.
- **Processing time requirements**: After a custom data risk assessment completes, results require at least 48 hours to become available and do not update after that point. A new assessment is needed to see changes. New policies require at least 24 hours before data appears. Users should plan ahead and avoid expecting real-time results from newly created assessments or policies.
- **Activity explorer data completeness**: The AI interaction event may not always display prompt and response text. In some cases, prompts and responses span consecutive entries. When a user does not have a mailbox hosted in Exchange Online, no prompt or response is displayed. Microsoft Facilitator AI-generated notes may not display prompts or responses. Users should be aware of these gaps when relying on activity explorer for compliance or investigative purposes.
- **Data Security Posture Agent constraints**: The agent supports content searches up to 1 GB of data but does not support metadata-based searches. If no time period is specified, results default to the last 7 days. The agent is designed for pre-investigation checks and is not a replacement for formal investigation tools such as eDiscovery, audit, or Data Security Investigations.
- **Language support**: The Security Copilot experience and the Data Security Posture Agent are designed and evaluated primarily for English-language prompts. Using other languages may result in reduced accuracy or incomplete responses. Users should exercise caution when operating outside the intended language scope.
- **Generative AI response accuracy**: As with all generative AI systems, Security Copilot responses in Data Security Posture Management may occasionally contain inaccurate or incomplete information. Users should verify AI-generated insights against actual data before taking consequential actions based on those responses.

## Evaluations

Performance and safety evaluations assess whether AI applications are operating reliably and securely by examining factors like groundedness, relevance, and coherence while identifying the risks of generating harmful content. The following evaluations were conducted with safety components already in place, which are also described in Safety Components and Mitigations.

Data Security Posture Management was evaluated using custom evaluation methods developed by the product team. The evaluation focused on the accuracy of the embedded Security Copilot experience when responding to natural language questions about data security.

The evaluation data set consisted of relevant prompts identified by the product team and customers, including an expanded test set of prompts based on table schemas and descriptions. Microsoft evaluated performance using an accuracy rate metric: a response is considered accurate if the generated query provides the exact information asked in the prompt. The team tested across a range of data security scenarios covering DLP, information protection, and Insider Risk Management insights to verify that Security Copilot responses are factually supported by the underlying data and contextually appropriate to the user's question.

An ideal result is one where the Security Copilot response returns exactly the information requested, grounded in the organization's actual data, with no fabricated or misleading content. A suboptimal result would be a response that returns inaccurate data, misinterprets the user's question, or provides information outside the scope of the supported data security solutions. The evaluation process is iterative, with the product team refining the prompt sets and accuracy thresholds based on customer feedback and real-world usage patterns.

## Safety components and mitigations

- **Role-based access control**: Data Security Posture Management enforces granular permissions through Microsoft Entra and Microsoft Purview role groups. Different activities require specific roles, such as Compliance Administrator for editing, Data Security Viewer for using Security Copilot, and Content Explorer Content Viewer for viewing AI interaction prompts and responses. This ensures that users can only access data and take actions appropriate to their role, reducing the risk of unauthorized access to sensitive information.
- **Comprehensive audit logging**: All automated actions taken by AI agents in Data Security Posture Management are recorded in audit logs. This includes actions such as removing sharing links, applying policies, and revoking permissions. Audit logs and activity explorer features provide a full trail of interactions with AI apps and agents, supporting compliance investigations, incident response, and accountability.
- **Human review and approval for agent actions**: Users always maintain control over AI agent behavior within Data Security Posture Management. AI-driven triage agents and the Data Security Posture Agent surface recommendations and findings, but users review, approve, or customize all automated actions before they take effect. The "View agent activity" options throughout the interface provide easy access to agent activity for oversight.
- **Opt-in analytics processing**: Data Security Posture Management requires explicit opt-in before processing organizational data. Analytics in both Insider Risk Management and DLP must be enabled before Data Security Posture Management can generate insights. This ensures that organizations make a deliberate decision to share data for analysis and are aware of the processing that takes place.
- **Scoped AI capabilities**: The Security Copilot experience in Data Security Posture Management is deliberately scoped to data security topics associated with Insider Risk Management, Information Protection, and Data Loss Prevention. Questions outside this scope are not answered, reducing the risk of the AI generating responses about topics where it lacks reliable data. The Data Security Posture Agent is similarly scoped to content searches within Microsoft 365 and limited to 1 GB of content per query.
- **Risk-level classification for search results**: The Data Security Posture Agent assigns a risk level to each search result based on how closely the content matches the user's prompt. Results are categorized to help users prioritize and focus on the most relevant findings. When the agent cannot determine the risk level, items are marked as "not categorized," providing transparency about the agent's confidence level.
- **Alert triage and noise reduction**: AI-driven triage agents review DLP and Insider Risk Management alerts and categorize them as "needs attention," "less urgent," or "not categorized." This filtering reduces alert fatigue and helps security analysts focus on genuine threats rather than false positives.
- **Privacy-preserving design**: Insider Risk Management, which feeds data into Data Security Posture Management, includes privacy controls such as pseudonymization and role-based access to ensure user-level privacy while enabling risk analysis. The Security Copilot component follows the data privacy and security practices documented in the [Microsoft Security Copilot privacy and data security documentation](/en-us/copilot/security/privacy-data-security).
- **In-product feedback mechanism**: Users can provide feedback on each Security Copilot response by marking it as "looks right," "needs improvement," or "inappropriate." This feedback loop helps Microsoft continuously improve the quality and safety of AI-generated responses.

## Best practices for deploying and adopting Data Security Posture Management

Responsible AI is a shared commitment between Microsoft and its customers. While Microsoft builds AI applications with safety, fairness, and transparency at the core, customers play a critical role in deploying and using these technologies responsibly within their own contexts. To support this partnership, we offer the following best practices for deployers and end users to help customers implement responsible AI effectively.

Deployers and end-users should:

- **Exercise caution and evaluate outcomes when using Data Security Posture Management for consequential decisions or in sensitive domains**: Consequential decisions are those that may have a legal or significant impact on a person's access to education, employment, financial platforms, government benefits, healthcare, housing, insurance, legal platforms, or that could result in physical, psychological, or financial harm. Sensitive domains—such as financial platforms, healthcare, and housing—require particular care due to the potential for disproportionate impact on different groups of people. When using AI for decisions in these areas, make sure that impacted stakeholders can understand how decisions are made, appeal decisions, and update any relevant input data.
- **Evaluate legal and regulatory considerations**: Customers need to evaluate potential specific legal and regulatory obligations when using any AI platforms and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI platforms or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.

End-users should:

- **Exercise human oversight when appropriate**: Human oversight is an important safeguard when interacting with AI applications. While we continuously improve our AI applications, AI might still make mistakes. The outputs generated may be inaccurate, incomplete, biased, misaligned, or irrelevant to your intended goals. This could happen due to various reasons, such as ambiguity in the inputs or limitations of the underlying models. As such, users should review the responses generated by Data Security Posture Management and verify that they match their expectations and requirements.
- **Be aware of the risk of overreliance**: Overreliance on AI happens when users accept incorrect or incomplete AI outputs, mainly because mistakes in AI outputs may be hard to detect. For the end-user, overreliance could result in decreased productivity, loss of trust, application abandonment, financial loss, psychological harm, physical harm, among others. In the context of Data Security Posture Management, overreliance could mean acting on an inaccurate Security Copilot insight without verifying it against actual data, potentially leading to misguided policy changes or missed security risks.
- **Scope Security Copilot questions to supported areas**: For the best results, ask questions about data security topics associated with Insider Risk Management, Information Protection, and Data Loss Prevention. Questions outside these areas may return incomplete or inaccurate responses because they fall outside the data Data Security Posture Management is designed to analyze.
- **Use specific and targeted prompts**: When using the Security Copilot experience or the Data Security Posture Agent, provide clear and specific prompts that include relevant details such as user names, time periods, and data locations. For example, instead of asking "show me security risks," ask "show all sensitive data activities performed by user@contoso.com in the last 30 days." More specific prompts produce more accurate and actionable results.
- **Provide feedback to improve quality**: Use the in-product feedback option to mark Security Copilot responses as "looks right," "needs improvement," or "inappropriate." This feedback helps Microsoft identify and address quality issues in AI-generated responses.

Deployers should:

- **Configure appropriate permissions before granting access**: Assign the minimum required roles to each user based on their responsibilities. Use the detailed permissions table in the [Data Security Posture Management permissions documentation](data-security-posture-management-permissions) to determine which role groups are needed for each activity. Restricting access reduces the risk of unauthorized users viewing sensitive data or taking unintended actions.
- **Complete all setup tasks before relying on insights**: Ensure that auditing, analytics, and collection policies are properly configured before evaluating Data Security Posture Management insights. Incomplete setup can result in missing data and inaccurate posture metrics. Allow sufficient processing time (up to three days for initial scans, at least 24 hours for new policies) before making decisions based on Data Security Posture Management data.
- **Use restricted searches for efficient processing**: When using the Data Security Posture Agent, configure searches to target specific users, groups, or sites rather than running tenant-wide scans. Restricted searches are significantly faster and more efficient, reducing processing time and producing more focused results.
- **Review and refine one-click policies after deployment**: One-click policies provide a useful starting point, but they should be reviewed and customized based on your organization's specific requirements. After initial deployment, monitor policy results through Data Security Posture Management reports and activity explorer, and adjust policy settings in the corresponding solution (DLP, Insider Risk Management, or Information Protection) to match your organization's risk tolerance and compliance needs.
- **Establish a regular review cadence**: Use Data Security Posture Management posture trends and reports to track your organization's data security posture over time. Establish a regular cadence for reviewing data risk assessments, policy coverage, and AI observability metrics. Regular reviews help identify emerging risks, policy gaps, and changes in user behavior before they become security incidents.
- **Plan for collection policy configuration**: If your organization needs to capture prompts and responses from Copilot in Fabric and Security Copilot, and for non-Copilot AI apps, configure collection policies with the content capture option selected. For apps that use these collection policies, AI interaction events in activity explorer will not display prompt and response text, limiting the usefulness of the data for compliance monitoring.

## Learn more about Data Security Posture Management

For additional guidance or to learn more about the responsible use of Data Security Posture Management, we recommend reviewing the following documentation:

- [Learn about Data Security Posture Management](data-security-posture-management-learn-about)
- [Data Security Posture Management (classic)](data-security-posture-management) - Overview of the previous version
- [Setup tasks for Data Security Posture Management](data-security-posture-management-setup)
- [Considerations for Data Security Posture Management](data-security-posture-management-considerations)
- [Permissions for Data Security Posture Management](data-security-posture-management-permissions)
- [Prevent oversharing with data risk assessments](data-security-posture-management-oversharing)
- [Microsoft Purview data security and compliance protections for generative AI apps](ai-microsoft-purview)
- [Data, privacy, and security for Microsoft Security Copilot](/en-us/copilot/security/privacy-data-security)
- [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)

### Learn more about responsible AI

- [Microsoft AI principles](https://www.microsoft.com/ai/responsible-ai)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/tools-practices)
- [Microsoft Azure Learning courses on responsible AI](/en-us/ai)