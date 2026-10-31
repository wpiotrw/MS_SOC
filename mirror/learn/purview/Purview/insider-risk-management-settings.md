---
layout: Conceptual
title: Learn about Insider Risk Management settings | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Insider Risk Management settings in Microsoft Purview.
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
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: bdc12255-799b-2436-56ce-bd90284dc074
document_version_independent_id: bdc12255-799b-2436-56ce-bd90284dc074
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 3b9388a6-b685-b857-a4db-c5eec628bdcc
---

# Learn about Insider Risk Management settings | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Before you get started with Insider Risk Management policies, understand and choose the Insider Risk Management settings that best meet the compliance needs for your organization. Insider Risk Management settings apply to all Insider Risk Management policies, regardless of the template you choose when creating a policy.

Note

Use **Settings** at the top of any Insider Risk Management page to make settings changes.

The following table describes each Insider Risk Management setting and provides a link to learn more about the setting.

| Setting | Description |
| --- | --- |
| [Admin notifications](insider-risk-management-settings-admin-notifications) | Use the **Admin notifications** setting to automatically send an email notification to selectable Insider Risk Management role groups. You can:- Send a notification email when the first alert is generated for a new policy- Send a daily email when new high-severity alerts are generated- Send a weekly email summarizing policies that have unresolved warnings |
| [Analytics](insider-risk-management-settings-analytics) | Insider risk analytics enables you to conduct an evaluation of potential insider risks in your organization without configuring any insider risk policies. This evaluation can help your organization identify potential areas of higher user risk and help determine the type and scope of Insider Risk Management policies you might consider configuring. |
| [Data sharing](insider-risk-management-settings-share-data) | Use the **Data sharing** setting to do either of the following: 1) Export Insider Risk Management alert information to SIEM solutions by using the Office 365 Management Activity API schema; 2) Share Insider Risk Management user risk levels with Microsoft Defender and DLP alerts. |
| [Detection groups](insider-risk-management-settings-detection-groups) | Use the **Detection groups** setting to create variants of built-in indicators if you want to tailor detections for different sets of users. Creating detection groups helps to reduce false positives. |
| [Export alerts](insider-risk-management-settings-alerts) | Insider Risk Management alert information is exportable to security information and event management (SIEM) and security orchestration automated response (SOAR) solutions by using the Office 365 Management Activity API schema. You can use the Office 365 Management Activity APIs to export alert information to other applications your organization might use to manage or aggregate insider risk information. |
| [Global exclusions](insider-risk-management-settings-global-exclusions) | Use the **Global exclusions** setting to specify global exclusions that won't be scored by your Insider Risk Management policies. |
| [Inline alert customization](insider-risk-management-settings-inline-alert-customization) | Inline alert customization allows you to quickly tune an Insider Risk Management policy directly from the **Alerts dashboard** while reviewing the alert. Alerts are generated when a risk management activity meets the thresholds configured in the related policy. To reduce the number of alerts you get from this type of activity, you can change the thresholds or remove the risk management activity from the policy altogether. |
| [Intelligent detections](insider-risk-management-settings-intelligent-detections) | Use the **Intelligent detections** setting to boost the score for unusual download activity, control alert volume, import and filter Microsoft Defender for Endpoint alerts, and specify unallowed and third-party domains for risk scoring. |
| [Microsoft Teams (preview)](insider-risk-management-settings-teams) | You can enable Microsoft Teams support so that compliance analysts and investigators can use Teams to collaborate on Insider Risk Management cases. Use Teams to: - Coordinate and review response activities for cases in private Teams channels- Securely share and store files and evidence related to individual cases- Detect and review response activities by analysts and investigators |
| [Policy indicators](insider-risk-management-settings-policy-indicators) | Each Insider Risk Management policy template is based on specific indicators that correspond to specific triggers and risk activities. All global indicators are disabled by default; **you must select one or more indicators to configure an Insider Risk Management policy**. Indicator level settings help you control how the number of occurrences of risk events in your organization affect the risk score. |
| [Policy timeframes](insider-risk-management-settings-policy-timeframes) | The **Policy timeframes** setting allows you to define past and future review periods that are triggered after policy matches based on events and activities for the Insider Risk Management policy templates. |
| [Power Automate flows (preview)](insider-risk-management-settings-power-automate) | Microsoft Power Automate is a workflow service that automates actions across applications and services. By using flows from templates or created manually, you can automate common tasks associated with these applications and services. When you enable Power Automate flows for Insider Risk Management, you can automate important tasks for cases and users. You can configure Power Automate flows to retrieve user, alert, and case information and share this information with stakeholders and other applications, as well as automate actions in Insider Risk Management, such as posting to case notes. Power Automate flows are applicable for cases and any user in scope for a policy. |
| [Priority physical assets (preview)](insider-risk-management-settings-priority-physical-assets) | Identifying access to priority physical assets and correlating access activity to user events is an important component of your compliance infrastructure. These physical assets represent priority locations in your organization, such as company buildings, data centers, or server rooms. Insider risk activities might be associated with users working unusual hours, attempting to access these unauthorized sensitive or secure areas, and requests for access to high-level areas without legitimate needs. |
| [Priority user groups](insider-risk-management-settings-priority-user-groups) | Users in your organization might have different levels of risk depending on their position, level of access to sensitive information, or risk history. Prioritizing the examination and scoring of the activities of these users can help alert you to potential risks that might have higher consequences for your organization. Use the **Priority user groups** setting to define the users in your organization that need closer inspection and more sensitive risk scoring. |
| [Privacy](insider-risk-management-settings-privacy) | Choose whether to display usernames or anonymized versions of usernames for all current and past policy matches for alerts and cases. |