---
layout: Conceptual
title: Learn about Insider Risk Management forensic evidence | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Insider Risk Management forensic evidence in Microsoft Purview. Forensic evidence is an investigative tool for viewing captured user activity to help determine whether the user's actions pose a risk and might lead to a security incident.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: itpro
ms.collection: m365-security-compliance
locale: en-us
document_id: bc09d5ad-27ad-d245-5c00-12e12a2000b1
document_version_independent_id: bc09d5ad-27ad-d245-5c00-12e12a2000b1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-forensic-evidence.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-forensic-evidence
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-forensic-evidence.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: b336c402-b98d-5bcd-2f53-5e8bad243c4c
---

# Learn about Insider Risk Management forensic evidence | Microsoft Learn

Important

Forensic evidence is an opt-in add-on feature in [Microsoft Purview Insider Risk Management](insider-risk-management) that gives security teams visual insights into potential insider data security incidents, with user privacy built in. Forensic evidence includes customizable event triggers and built-in user privacy protection controls, enabling security teams to better investigate, understand and respond to potential insider data risks like unauthorized data exfiltration of sensitive data.

Organizations set the right policies for themselves, including what risky events are highest priority for capturing forensic evidence and what data is most sensitive. Forensic evidence is off by default, policy creation requires dual authorization and usernames can be masked with pseudonymization (which is on by default for Insider Risk Management). Setting up policies and reviewing security alerts within Insider Risk Management leverages strong role-based access controls (RBAC), ensuring that the designated individuals in the organization are taking the right actions with additional auditing capabilities.

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Visual context is crucial for security teams during forensic investigations to get better insights into potentially risky security-related user activities. With customizable event triggers and built-in user privacy protection controls, forensic evidence enables customizable visual activity capturing across devices to help your organization better mitigate, understand, and respond to potential data risks like unauthorized data exfiltration of sensitive data. You set the right policies for your organization, including what risky events are the highest priority for capturing forensic evidence, what data is most sensitive, and whether users are notified when forensic capturing is activated. Forensic evidence capturing is off by default and policy creation requires dual authorization.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Feature capabilities

- **Visual capturing** enables your organization to capture clips of key security-related user activities, so you can have more secure or compliant visibility that meets your organizational needs.
- **Include or exclude desktop applications and websites** to configure a recording policy that focuses on the applications and websites that present the most risk. This approach preserves storage space and user privacy. For example, you can exclude personal email and social media accounts.
- **Enhanced phishing protection (preview)** enables your organization to capture clips related to Enhanced Phishing Protection in Microsoft Defender SmartScreen. For example, you can capture when a user enters the Microsoft password they used to sign into their Windows 11 device on a phishing site or application connecting to a phishing site. [Learn more about Enhanced Phishing Protection in Microsoft Defender SmartScreen](/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/enhanced-phishing-protection)
- **Protected user privacy** through multiple levels of approval for the activation of the capturing feature.
- **Customizable triggers and capturing options** mean that security teams can set up forensic evidence to meet their needs, whether it be based on incidents (for example, *Capture 5 min before and 10 min after a user has downloaded 'SecretResearchPlans.docx'*), or based on continuous capturing needs.
- **User-centric policy targeting** means that security and compliance teams can focus on activity by user, not device, for better contextual insights.
- **Strong role-based access controls (RBAC)** mean that the ability to set up and review forensic clips is tightly controlled and only available to individuals in the organization with the right permissions.
- **Deep integration with current Insider Risk Management features**, making for easier onboarding and more familiar workflows for Insider Risk Management administrators and a trusted single-platform approach.
- **Trial capacity (up to 20 GB)** for captured clips, with quick access to capacity utilization and the ability to purchase additional capacity.

## Device and configuration requirements

The following tables include the supported minimum requirements for utilizing Insider Risk Management forensic evidence.

### Supported platforms

| Operating system | SKU | Processor |
| --- | --- | --- |
| Windows 10 (including [Windows 365](/en-us/windows-365/enterprise/forensic-evidence-set-up)) | Enterprise | 64-bit (Intel or AMD) |
| Windows 11 (including [Windows 365](/en-us/windows-365/enterprise/forensic-evidence-set-up)) | Enterprise | 64-bit (Intel or AMD) |

### Physical devices

| Hardware | Minimum requirement |
| --- | --- |
| RAM | Minimum of 8 GB (at least 2 GB should be available for client usage) |
| CPU processor | Intel i5 or higher and AMD Ryzen 5 or higher |
| Graphics card | Compatible with DirectX 11 or later, with a WDDM 1.0 driver or later. Only integrated graphics cards are currently supported; discrete GPUs, including NVIDIA RTX PRO series, are not supported |
| Disk space | Minimum of 10 GB of disk storage |
| Display | Minimum screen resolution of 1920 x 1080 |

### Hyper-V and virtual machines

| Hardware | Minimum requirement |
| --- | --- |
| RAM | Minimum of 16 GB (at least 2 GB should be available for client usage) |
| CPU processor | Minimum of eight vCPU processors or equivalent |
| Disk space | Minimum of 10 GB of disk storage |
| Display | Minimum screen resolution of 1920 x 1080 |

Important

If you don't meet the minimum requirements, you might run into Microsoft Purview client issues and the quality of forensic captures might not be reliable.

## Capturing options

[Triggering events, global indicators, and policy indicators](insider-risk-management-settings-policy-indicators) play an important role in all Insider Risk Management policies, including forensic evidence policies. Triggering events are user actions that determine if users are brought into scope for evaluation in Insider Risk Management policies. Global settings indicators determine what activities Insider Risk Management collects. Policy indicators determine a risk score for an in-scope user.

Depending on how your organization decides to configure forensic evidence, you can choose from two capturing options:

- **Specific activities**: This policy option captures activity only when a triggering event brings an approved user into scope for the forensic evidence policy and when the conditions for a policy indicator are detected for the user. For example, a user approved for forensic evidence capturing is brought in-scope to the forensic evidence policy and the user copies data to personal cloud storage services or portable storage devices. Capturing is scoped only to the configured time frame when the user is copying the data to the personal cloud storage service or portable storage device. You can review captures for this option on the **Forensic evidence** tab on the **Alerts** dashboard.
- **All activities**: This policy option captures any activity performed by users. For example, your organization has a time-sensitive need for capturing activities for an approved user that is actively involved in potentially risky activities that might lead to a security incident. Policy indicators might not have reached the threshold for an alert to be generated by the policy and the potentially risky activity might not be documented. Continuous capturing help prevents the potentially risky activity from being missed or going undetected. You can review captures for this option on the **Forensic evidence** tab on the **User activity reports (preview)** dashboard.

Important

Forensic evidence clips are deleted 120 days after they're captured or at the end of the preview period, whichever is sooner. You can download or transfer forensic evidence clips before they're deleted.

## Workflow

The overall workflow for detecting, investigating, and remediating alerts that contain clip capturing follows the [same basic steps](insider-risk-management#workflow) as other Insider Risk Management policies. However, some notable differences exist for forensic evidence when configured in your organization:

- **Users subject to capturing must have explicit capturing requests and approvals**: This extra process isn't included as a part of configuring other Insider Risk Management policies. Users assigned to the *Insider Risk Management* or *Insider Risk Management Admins* role groups must submit a request to users assigned to the *Insider Risk Management Approvers* role group before any user in your organization is eligible for any clip capturing options. For example, this requirement helps support organizational scenarios where your Insider Risk Management admins must get explicit approval from your designated legal or human resources personnel before capturing for any user is enabled.
- **Devices must be onboarded and have the Microsoft Purview client installed**: Before forensic evidence can collect and store clips captured for eligible users, their devices must be onboarded to the Microsoft Purview portal. Additionally, each device must have the Microsoft Purview Client installed. These prerequisites enable support for both online and offline device capturing.

## Ready to get started?

- For step-by-step guidance to configure forensic evidence capturing in your organization, see [Get started with Insider Risk Management forensic evidence](insider-risk-management-forensic-evidence-configure).
- To configure prerequisites, create policies, and start receiving alerts, see [Get started with Insider Risk Management](insider-risk-management-configure).