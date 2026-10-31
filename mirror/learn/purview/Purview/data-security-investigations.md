---
layout: Conceptual
title: Learn about Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Understand Microsoft Purview Data Security Investigations, how it uses AI to analyze incidents, and how to get started.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 10b9c17a-ad78-2f1b-452f-86b2a772354a
document_version_independent_id: 10b9c17a-ad78-2f1b-452f-86b2a772354a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 62c32804-c528-d6f6-1646-482090027993
---

# Learn about Data Security Investigations | Microsoft Learn

Microsoft Purview Data Security Investigations helps cybersecurity teams in your organization use generative artificial intelligence (AI) to analyze and respond to data security incidents, risky insiders, and data breaches. Investigations help you quickly identify risks from sensitive data exposure and more effectively collaborate with your partner teams to remediate the issues. It simplifies tasks that traditionally are time consuming and complex. 

Analysts in your organization can use Data Security Investigations features to:

- Quickly and efficiently search, discover, and identify impacted data.
- Use deep content AI analysis to discover exact data risks hidden in data.
- Take action to reduce the impact of data security incidents and quickly mitigate ongoing risks.
- Collaborate with internal and external stakeholders on investigation details.
- Receive notifications through the Microsoft Purview Notification Center and email when setup completes and investigations are ready to use.

For more information about how Data Security Investigations can help you respond to data security incidents, watch the following videos:

- [Data Security Investigations in Microsoft Purview](https://www.youtube.com/watch?v=tgnY65zHd8g)
- [Enhance data security investigations with Microsoft Purview](https://www.youtube.com/watch?v=SKQyfHBfvpY)
- [Introducing Microsoft Purview Data Security Investigations](https://www.youtube.com/watch?v=nGXgxy-6FPY)
- [Unlock the Power of Data Security Investigations with Microsoft Purview](https://www.youtube.com/watch?v=_uu_6LSZQqs)
- [Microsoft Purview Data Security Investigations Ask Me Anything](https://www.youtube.com/watch?v=D7TT5B-DTu0)

## AI integration

Data Security Investigations uses generative AI to conduct deep content analysis and uncover key security and sensitive data risks for data included in investigations. AI helps analysts quickly analyze large volumes of data with high accuracy, saving critical time for triage, review, and mitigation actions.

There are three main AI-related investigative capabilities:

- **Vector search**: Vector-based semantic search enables similarity-based information retrieval and understands user intent beyond literal words. Analysts query impacted data to find all assets related to a particular subject, even if keywords are missing.
- **Categorization**: To get an initial understanding of incident severity, analysts can use **Standard** or **Advanced** AI options to categorize impacted data, narrowing focus to high-risk assets. Data Security Investigations automatically sorts data into default, custom, or AI-suggested categories. Categorized items also include grouping by subject matter and risk level.
- **Examination**: Data Security Investigations enables analysts to easily address the number one priority for most data security incidents - finding security risks buried within impacted data. By examining impacted data for security risks, analysts can find compromised credentials, network risks, [personal data exposure](data-security-investigations-personal-data), or evidence of threat actor discussions associated with security incidents.

For more information about AI integration and these tools, see [Learn about AI analysis in Data Security Investigations](data-security-investigations-ai).

## Common data breach actions

Most organizations are concerned with the increasing risks and impact related to internal and external data security breaches. Your cybersecurity team is responsible for identifying impacted data during a data breach scenario and reducing the time required to mitigate the risk associated with vulnerabilities exposed within a data breach scenario. When a data breach occurs, you must respond quickly and effectively to mitigate risks and protect sensitive information.

Your cybersecurity team needs to:

- **Assess the data breach**: Analysts must understand the scope and impact of the data breach. This understanding includes identifying all affected systems, the data impacted, and any external and internal users associated with the data breach.
- **Containment and communication**: Analysts must isolate affected systems to minimize and prevent further damage. Additionally, internal stakeholders and departments in your organization (IT, Legal, Executive Management) need notification and the details about the data breach.
- **Forensics and evidence preservation**: Analysts might need support when engaging with data forensics experts. System and status details must be retained (logs, system snapshots, network traffic) for potential legal and regulatory requirements.
- **Risk assessment and mitigation**: Analysts must evaluate potential risks and prioritize mitigation actions based on risk severity. This information helps with implementing configuration and policy updates, including implementing applicable security patches.
- **Data purge and protection**: Analysts might need to remove unnecessary or compromised data and delete redundant copies. Data Security Investigations supports [soft purge and hard purge](data-security-investigations-mitigation-actions#purge) options to remove or permanently delete items from data sources. Other tasks might include strengthening access controls, data encryption, and monitoring.
- **Reporting and compliance**: Depending on the nature of the data involved and the jurisdictions affected, analysts might need to comply with regulatory requirements for [breach notification](data-security-investigations-personal-data). These requirements might include informing affected individuals, regulatory bodies, and other stakeholders about the nature of the breach and the steps taken to address it.

## Common scenarios

### Investigate a data breach

After a data security incident, it can be difficult to understand the impact of sensitive data exposure. As part of your mitigation strategy, you need to identify the intellectual property, [personal data](data-security-investigations-personal-data), and financial information that might be compromised. Additionally, some organizations build and maintain custom tools to investigate these issues.

When you use [Microsoft Defender XDR](/en-us/defender-xdr?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) to investigate data security incidents, you might discover a document containing unfiled patents. When you create an investigation from the incident in Data Security Investigations, further analysis shows which users downloaded the document and if it was accessed from a risky IP address. This information gives you critical context to take mitigation steps, such as protecting or purging the sensitive document from your organization.

### Investigate a potential data leak from a risky insider

When you use [Insider Risk Management](insider-risk-management) to investigate data leak alerts for a risky user in your organization, you might learn that the user shared emails and files with an external storage solution. With built-in integration, you can create a new investigation in Data Security Investigations from the Insider Risk Management case to quickly review preliminary insights about the shared content. Before committing any additional compute resources or charges, you can decide if this content needs further analysis.

If you add the shared items to the scope of the investigation, processing automatically starts so you can dig further into the details of the content. When processing completes, all the data is categorized and assessed for risk severity. Analysts can quickly review the highest severity items and identify the items needing a closer look. Details about usernames, passwords, documentation content, and source code are all available for review as applicable. Analysts can then work with other stakeholders in your organization to take action on the most critical items to mitigate ongoing risks from the data leak.

### Confidential data leak

In scenarios where confidential, sensitive, or protected information is intentionally or unintentionally exposed outside its intended environment, you can use Data Security Investigations to further investigate a potential data leak, better understand incident impact, and take necessary next steps.

### Proactive data security assessment

You can also use Data Security Investigations to proactively assess your data estate for data risk. You can analyze a sample of high-value data sources and users for data risk or run proactive scans of specific high-value data sources or a broader organization-wide scope. The assessment helps to identify opportunities for refining policies or organizational changes to strengthen security practices and potentially prevent or reduce the impact of future data security incidents.

When you enable [proactive AI insights from Data Security Posture Management (preview)](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm), Data Security Investigations automatically analyzes recently exfiltrated sensitive data across five risk categories, providing continuous visibility into data exposure without manual investigation creation.

## Integration with other Microsoft platforms and solutions

Data Security Investigations is a unified, purpose-built solution that's tightly integrated with other Microsoft security services. Integrated with the Microsoft Graph-enabled approach to security, Data Security Investigations draws correlations between impacted data, users, and activities. This integration helps you quickly identify impacted data, investigate incidents using generative AI, and securely collaborate with other members of your security team to mitigate risk.

### Microsoft Defender XDR

[Microsoft Defender XDR](/en-us/defender-xdr?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks. With built-in integration with Data Security Investigations, you can extend the analysis of threat signals and dive deeper into data associated with attacks and security incidents.

Using the Microsoft Defender portal, you can assess alerts and quickly open an investigation in Data Security Investigations for deeper insights about the data and users associated with the incident. The investigation helps you analyze the alert details, understand what they mean, and collect and examine data for deeper review and mitigation efforts.

For more information about Microsoft Defender XDR features, see [Get started with Microsoft Defender XDR](/en-us/defender-xdr/get-started?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

### Microsoft Purview Insider Risk Management

By combining the integration and investigative capabilities of Data Security Investigations with the proactive risk management features of [Microsoft Purview Insider Risk Management](insider-risk-management), your organization has a holistic view of potential risks and the ability to take timely actions to protect sensitive data. Insider Risk Management investigators might not have important insights into the content contained in files associated with risky alerts. This gap might lead to the mishandling of alerts and ultimately hinder your effectiveness at mitigating insider threats.

The integration between Data Security Investigations and Insider Risk Management enables seamless collaboration between your cybersecurity and risk management teams. This collaboration allows for more efficient identification and a quicker mitigation of insider threats. For more information about Insider Risk Management features, see the following articles:

- [Get started with Insider Risk Management](insider-risk-management-configure)
- [Create and manage Insider Risk Management policies](insider-risk-management-policies)
- [Investigate insider risk activities](insider-risk-management-activities)
- [Take action on insider risk cases](insider-risk-management-cases)

### Microsoft Purview Data Security Posture Management

If you're using [Microsoft Purview Data Security Posture Management (DSPM)](data-security-posture-management-learn-about), you can escalate potential data exfiltration findings to Data Security Investigations for deeper, AI-powered content analysis. You can [manually create an investigation](data-security-investigations-investigation#create-a-manual-investigation-from-dspm) from a DSPM (preview) insight, or [enable proactive AI insights](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm) that automatically create and refresh an investigation for your tenant every 24 hours. Investigations created from DSPM are automatically scoped to all sensitive data recently exfiltrated from your organization, allowing your team to quickly understand what was exposed, assess its sensitivity, and take informed remediation actions.

### Unified audit log

[Microsoft Purview auditing solutions](audit-solutions-overview) provide an integrated solution to help organizations effectively respond to security events, forensic investigations, internal investigations, and compliance obligations. Your organization's unified audit log captures, records, and retains thousands of user and admin operations performed in dozens of Microsoft services and solutions.

Data Security Investigations integrates with the unified audit log in two ways:

- **Audit search**: Use [audit search](data-security-investigations-search#audit-search) to identify and collect content based on user activities recorded in the unified audit log. Audit search queries the unified audit log for content-associated activities, such as file access, downloads, and sensitivity label changes, and adds the related content directly to your investigation scope.
- **Activity logging**: Data Security Investigations provides powerful investigation tools that might require the ability to audit activities taken to ensure secure and approved use of the solution. To meet these requirements, Data Security Investigations activities are automatically logged in the unified audit log.

For more information about these activities, see the [Data Security Investigations activities](audit-log-activities#data-security-investigations-activities) section in the Audit log activities [article](audit-log-activities).

### Microsoft Purview Endpoint Data Loss Prevention

[Microsoft Purview Endpoint Data Loss Prevention (DLP)](endpoint-dlp-learn-about) monitors and protects sensitive items on onboarded Windows and macOS devices. For a general overview of DLP capabilities, see [Learn about data loss prevention](dlp-learn-about-dlp). When endpoint DLP policies are configured with [evidence collection for file activities on devices](dlp-copy-matched-items-learn), copies of files that match policies are captured and stored for review.

Data Security Investigations integrates with endpoint DLP evidence collection, allowing investigators to query captured endpoint data and add it to an investigation scope for AI-powered analysis. Instead of triaging individual endpoint DLP alerts one by one, investigators can aggregate endpoint events and analyze them collectively to detect patterns such as mass exfiltration or coordinated data theft.

For more information about using endpoint DLP data in investigations, see [Endpoint DLP evidence collection](data-security-investigations-search#endpoint-dlp-evidence-collection-preview).

## Billing models

Data Security Investigations helps you identify data risks for breached content by using large language models (LLMs) and Microsoft Copilot for Security. Because Data Security Investigations provides on-demand AI analysis and integrates with other Microsoft Purview solutions, it uses pay-as-you-go and capacity billing models. This billing structure means you pay for the storage and AI capacity features you use in the solution. However, you don't need a dedicated enterprise [plan or license](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) to use Data Security Investigations.

If you enable [proactive AI insights from DSPM](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm), storage and AI capacity costs are incurred continuously while the toggle remains enabled, as the auto-created investigation refreshes every 24 hours.

For more information about billing, see [Billing models in Data Security Investigations](data-security-investigations-billing).

## Ready to get started?

- [Learn about the Data Security Investigations workflow](data-security-investigations-workflow)
- [Get started with Data Security Investigations](data-security-investigations-get-started)