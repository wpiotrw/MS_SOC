---
layout: Conceptual
title: Share Insider Risk Management data with other solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to export Insider Risk Management alert information to SIEM solutions or share Insider Risk Management user risk levels with Microsoft Defender XDR and DLP alerts.
keywords: Microsoft 365, Microsoft Purview, Microsoft Defender XDR, insider risk, risk management, compliance, DLP, data loss prevention
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: f328a855-c27a-c319-7cab-9d07be668ea9
document_version_independent_id: f328a855-c27a-c319-7cab-9d07be668ea9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-share-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-share-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-share-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
platformId: f68b2f3e-fc07-0fea-5bb1-bc1d43c9a99f
---

# Share Insider Risk Management data with other solutions | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

You can share data from Insider Risk Management in the following ways:

- Export alert information to SIEM solutions.
- Share alerts and user risk severity levels with Microsoft Defender XDR.
- Share user risk severity levels with data loss prevention (DLP) alerts.

## Export alert information to SIEM solutions

You can export Microsoft Purview Insider Risk Management alert information to security information and event management (SIEM) and security orchestration automated response (SOAR) solutions by using the [Office 365 Management Activity API schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#security-and-compliance-alerts-schema). Use the Office 365 Management Activity APIs to export alert information to other applications your organization uses to manage or aggregate insider risk information. Alert information is exported and available every 60 minutes through the Office 365 Management Activity APIs.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

If your organization uses Microsoft Sentinel, you can also use the out-of-the-box Insider Risk Management data connector to import insider risk alert information to Microsoft Sentinel. For more information, see [Insider Risk Management](/en-us/azure/sentinel/data-connectors-reference#microsoft-365-insider-risk-management-irm-preview) in the Microsoft Sentinel article.

Important

To maintain referential integrity for users who have insider risk alerts or cases in Microsoft 365 or other systems, anonymization of usernames isn't preserved for exported alerts when using the exporting API or when exporting to [Microsoft Purview eDiscovery solutions](ediscovery). Exported alerts display usernames for each alert in this case. If you export to CSV files from alerts or cases, anonymization *is* preserved.

### Use the APIs to review insider risk alert information

Use the following steps to enable alert export by using the APIs:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Export alerts**. By default, this setting is disabled for your Microsoft 365 organization.
5. Turn the setting **On**.
6. Filter the common Office 365 audit activities by *SecurityComplianceAlerts*.
7. Filter *SecurityComplianceAlerts* by the *InsiderRiskManagement* category.

Alert information contains information from the Office 365 Management Activity API [Security and Compliance Alerts schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#security-and-compliance-alerts-schema) and [common schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#common-schema). The following fields and values are exported for Insider Risk Management alerts for the common schema:

- CreationTime
- ID
- Operation
- OrganizationId
- RecordType
- UserId
- UserKey
- UserType

## Share alert severity levels with other Microsoft security solutions

You can share alert severity levels from Insider Risk Management to bring unique user context to alert investigation experiences in the following Microsoft security solutions:

- [Microsoft Defender XDR](/en-us/defender-xdr/irm-investigate-alerts-defender)
- [Microsoft Purview Communication Compliance](communication-compliance)
- [Microsoft Purview Data Loss Prevention (DLP)](dlp-learn-about-dlp)

Insider Risk Management analyzes user activities over a period of 90 to 120 days and looks for anomalous behavior over that period. Adding this data to other security solutions enhances the data available in those solutions to help analysts prioritize alerts.

Tip

*Alert severity levels* in Insider Risk Management are different from *insider risk levels* that are defined in Adaptive Protection.

- Alert severity levels (Low, Medium, or High) are assigned to users based on activity detected in Insider Risk Management policies. The system calculates these levels from alert risk scores assigned to all active alerts associated with the user. These levels help insider risk analysts and investigators prioritize and respond to user activity accordingly.
- Insider risk levels (Elevated, Moderate, or Minor) in Adaptive Protection measure risk determined by admin-defined conditions such as the number of exfiltration activities users perform in a day or whether their activity generated a high-severity insider risk alert.

### Prerequisites

To share Insider Risk Management user risk levels with other Microsoft security solutions, the user must meet the following conditions:

- Be part of an Insider Risk Management policy.
- Perform exfiltration activities that bring the user into the scope of the policy.
- **For sharing with DLP**: Have [DLP alert permissions](dlp-alerts-dashboard-get-started#roles-and-role-groups). After the **Data sharing** setting is turned on, users with DLP alert permissions can access Insider Risk Management context for DLP alert investigation and for the Microsoft Defender XDR Users page. Users with Insider Risk Management permissions can also access this data.
- **For sharing with Communication Compliance**: Be assigned either the *Communication Compliance Analyst* or *Communication Compliance Investigator* roles to view user risk severity levels and activity history in Communication Compliance.

Tip

If you have access to DLP alerts in Microsoft Purview and/or Microsoft Defender, you can view user context from Insider Risk Management shared with those solutions.

### Share data with other Microsoft security solutions

You can share Insider Risk Management alert severity levels with other Microsoft security solutions by turning on a single setting.

1. In Insider Risk Management settings, select the **Data sharing** setting.
2. Under the **Sharing data with other Microsoft security solutions** section, turn on the setting.

Note

If you don't turn on this setting, the value displayed in the DLP alerts **Insider risk severity** column is "User data isn't available" and is displayed as "Insider Risk Activity not available" in Communication Compliance.

### What happens when you share Insider Risk Management alert severity levels?

When you turn on data sharing, Insider Risk Management severity information becomes available in the following Microsoft security experiences:

#### In Microsoft Defender XDR

Sharing alert data in the [Microsoft Defender portal](/en-us/defender-xdr/microsoft-365-defender-portal) is vital for protecting your organization's sensitive information and maintaining security. Security operations center (SOC) analysts can:

- Investigate Insider Risk Management alerts in the Microsoft Defender alert queue.
- Investigate Insider Risk Management alerts correlated with alerts from other detection sources such as Data Loss Prevention, Microsoft Defender for Identity, Microsoft Defender for Office, and more in the Microsoft Defender XDR incident queue.
- Run [Advanced Hunting queries](/en-us/defender-xdr/irm-investigate-alerts-defender) on two new tables containing Insider Risk Management alert data.
- Export rich Insider Risk Management alert data through [Microsoft Graph API](/en-us/defender-xdr/irm-investigate-alerts-defender#integrate-insider-risk-management-data-with-microsoft-graph-security-api).
- View Insider Risk Management severity for a user during your alert triage. An **Insider risk severity** field is added to the **Users** page for users that have a **High**, **Medium**, or **Low** risk level in Insider Risk Management. This data is available for any users with an active Insider Risk Management alert. An insider risk activity summary and activity timeline for that user appears on the right side of the **Users** page.

##### Migrating from Office 365 management activity APIs to Microsoft Graph APIs

You can access Insider Risk Management alert metadata through [Office 365 management activity API](/en-us/defender-xdr/streaming-api). However, Graph API provides richer metadata and bi-directional support. We recommend migrating to Graph API to integrate Insider Risk Management data with your enterprise systems.

The following table summarizes the most common Office 365 management activity API parameters and the equivalent Microsoft Graph API parameter:

| Office 365 management activity API parameter | Microsoft Graph API parameter |
| --- | --- |
| Alert parameter | No equivalent parameter |
| AlertId | ID |
| Category | ServiceSource |
| Comments | No equivalent parameter |
| Data | Evidence.useraccount.userPrincipalName(along with suffix) |
| Name | AlertPolicyName |
| PolicyId | AlertPolicyId |
| Severity | Severity |
| Source | DetectionSource |
| Status | Status |
| Version | No equivalent parameter |

For detailed schema mapping, see the Defender XDR schema in the [Office 365 management activity API](/en-us/defender-xdr/streaming-api) and [Microsoft Graph API](/en-us/defender-xdr/irm-investigate-alerts-defender).

##### Integrating Insider Risk Management with ServiceNow Security Operations

ServiceNow provides integrations to connect with Microsoft security technologies using Microsoft Graph. These solutions include Microsoft Sentinel, Microsoft Defender Advanced Threat Protection, and Azure Advanced Threat Protection. The ServiceNow Microsoft Graph integration allows you to access valuable insights from Microsoft products and helps you efficiently manage and respond to security incidents centrally using the ServiceNow platform. Insider Risk Management alert data is accessed outside the Microsoft Purview environment through the [Microsoft Graph security API](/en-us/graph/security-concept-overview).

To share Insider Risk Management alert data with ServiceNow, complete the following steps:

1. Get the [Microsoft Graph Security API Alert Ingestion Integration For Security Operations](https://store.servicenow.com/sn_appstore_store.do#!/store/application/92712ec3c7000010c20eb5a827c26059/10.4.8?referer=%2Fstore%2Fsearch%3Flistingtype%3Dallintegrations%25253Bancillary_app%25253Bcertified_apps%25253Bcontent%25253Bindustry_solution%25253Boem%25253Butility%25253Btemplate%25253Bgenerative_ai%25253Bsnow_solution%26q%3Dmicrosoft%2520graph%2520api&amp;sl=sh)
2. Follow the [ServiceNow documentation](https://docs.servicenow.com/bundle/xanadu-security-management/page/product/secops-integration-sir/secops-integration-ms-graph/concept/ms-graph-about.html) to set up or create a profile for the Microsoft Graph Security API alert ingestion integration.

For more information, see [Investigate insider risk threats in the Microsoft Defender portal](/en-us/defender-xdr/irm-investigate-alerts-defender).

#### In Communication Compliance alerts

For every [Communication Compliance](communication-compliance-policies) policy match, you can view the user risk severity associated with the sender. View this information on the **User activity** tab in communication for the alert. This view provides risk profile, policy matches, and user activities captured by [Insider Risk Management](insider-risk-management) and Communication Compliance.

The severity levels are categorized as *High*, *Medium*, *Low*, or *None*.

For risk severity levels of *None*, the reason might be for any of the following scenarios:

- The user isn't included in an insider risk policy.
- The user's activities aren't assigned a risk score, meaning the user isn't in the active scope for the policy.
- The user is included in an Insider Risk Management policy, but didn't engage in any risky activity.
- The organization doesn't have an active Insider Risk Management policy.

If the user risk severity isn't available, data sharing isn't enabled from Insider Risk Management.

You can view insider risk activities for up to 120 days in the **View Details** section on the **User history** tab in Insider Risk Management. Currently, the user activity summary in Communication Compliance shows only data from [exfiltration indicators](insider-risk-management-settings-policy-indicators).

#### In DLP alerts

In DLP alerts, shared Insider Risk Management data appears in the following ways:

- For the Insider Risk Management policy associated with the DLP alert, the DLP alerts queue includes an **Insider risk severity** column with values of *High*, *Medium*, *Low*, or *None*. If multiple users have activities that match the policy, the queue displays the user with the highest insider risk level.

    A value of **None** can mean either of the following:

    - The user isn't part of any Insider Risk Management policy.
    - The user is part of an Insider Risk Management policy, but they didn't perform risky activities that bring them into the scope of the policy (there's no exfiltration data).
- You can select the insider risk level in the DLP alerts queue to access the **User activity summary** tab, which shows a timeline of all exfiltration activities for that user for the past 90-120 days. Like the DLP alerts queue, the **User activity summary** tab shows the user with the highest insider risk level. This deep context into what a user did over the past 90 to 120 days provides a wider view of the risks presented by that user.

    Only data from exfiltration indicators appear in the user activity summary. Data from other sensitive indicators, such as HR, browsing, and so on, don't share with DLP alerts.
- An **Actor details** section is added to the DLP Alert details page. You can use this page to see *all* users involved in the specific DLP alert. For each user involved in the DLP alert, you can view all the exfiltration activities for the past 90 to 120 days.
- If you select **Get a summary from Security Copilot** in a DLP alert, the alert summary provided by Microsoft Security Copilot includes the Insider Risk Management severity level in addition to the DLP summary info, if the user is in scope of an Insider Risk Management policy.

    Tip

    You can also use [Security Copilot](/en-us/security-copilot/microsoft-security-copilot) to investigate DLP alerts. If the Insider Risk Management **Data sharing** setting is turned on, you can then do a combined DLP/Insider Risk Management investigation. For example, you might want to start by asking Copilot to summarize a DLP alert, then ask Copilot to show the insider risk level associated with the user flagged in the alert. Or you might want to ask why the user is considered a high-risk user. The user risk information in this case comes from Insider Risk Management. Security Copilot seamlessly integrates Insider Risk Management with DLP to assist with investigations. [Learn more about using the standalone version of Copilot for combined DLP/Insider Risk Management investigations](copilot-in-purview-promptbooks).