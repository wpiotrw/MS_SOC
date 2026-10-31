---
layout: Conceptual
title: Data risk graph in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-data-risk-graph
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about data risk graph in Insider Risk Management in Microsoft Purview.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-27T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1024, admindeeplinkCOMPLIANCE, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: dd03b231-380b-3085-9a46-8ce3884685c6
document_version_independent_id: dd03b231-380b-3085-9a46-8ce3884685c6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-data-risk-graph.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-data-risk-graph
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-data-risk-graph.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8f37329d-5c2f-4d50-b9b8-aa5cf54dbffe
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e13db295-3de6-46d5-bcdf-8785a76e3843
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d1ea7a3e-c435-17e8-7188-c79f141d1017
---

# Data risk graph in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Data risk graphs in [Insider Risk Management](insider-risk-management) provide a visual investigation experience that combines asset and activity data into a single view. Powered by Microsoft Sentinel integration, it summarizes [alert-related activity](insider-risk-management-activities) by a potential insider over the past 30 days, helping analysts triage alerts by revealing hidden contextual connections.

Important

**Data risk graph is being deprecated.** The data risk graph in Microsoft Purview Insider Risk Management will be retired on **November 24, 2026**. After that date, the data risk graph experience will no longer be available.

For more information about Microsoft Sentinel integration, see [Learn about Microsoft Sentinel in Microsoft Purview](purview-sentinel).

Important

You cannot use this feature with the [anonymized usernames privacy setting](insider-risk-management-settings-privacy) enabled. If you have anonymized user names, the graph will not load.

Note

[Admin units](purview-admin-units) aren't supported in the data risk graph. If you're scoped to an admin unit, data doesn't appear in data risk graphs.

## Supported activities in data risk graph

The data risk graph currently supports the following exfiltration activities:

- Anonymous links created in SharePoint or OneDrive
- Anonymous links used via SharePoint or OneDrive
- Company links created in SharePoint or OneDrive
- File downloads from SharePoint and OneDrive
- Files renamed in SharePoint and OneDrive

For more information about exfiltration detection indicators, see [Configure policy indicators in Insider Risk Management](insider-risk-management-settings-policy-indicators).

## Before you begin

Before you can use data risk graphs in Insider Risk Management, complete the following steps:

- Learn about [pay-as-you-go billing](/en-us/azure/sentinel/billing) in Microsoft Sentinel for your organization.
- Configure the [prerequisites for Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding#prerequisites)
- Review the [changes made when onboarding to Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding)
- Configure at least one [Insider Risk Management policy](insider-risk-management-policies) for supported data exfiltration activities.

## Configure data risk graph

Important

You always have one data lake. If you already onboarded to the data lake with another Microsoft service, your existing data lake is used. If you never onboarded to the data lake, onboarding in Insider Risk Management enables Microsoft Sentinel data lake and graph in the Defender portal.

After you complete the [prerequisites and understand the onboarding changes](purview-sentinel) that Microsoft Sentinel data lake and graph make to your organization, complete the following steps to configure data risk graph in Insider Risk Management:

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with an account assigned the *Global Administrator* or *Security Administrator* role.
2. Select the **Insider Risk Management** solution card, then select **Recommended actions** in the left nav.
3. In the **Comprehensive protection** section, select **Set up data lake and data risk graph**.

    If you don't have the correct permissions to set up the data lake, a notification appears to contact a global or billing administrator in your organization.
4. On the **Setup** tab on **Set up data lake & risk graph**, configure the following settings:

    1. **Subscription**: Enter the Azure subscription you want to use. Your selected subscription must be valid and accessible and you must be the subscription owner.
    2. **Resource group**: Enter the resource group you want to use. Your selected resource group must be valid and accessible.

    Important

    After the data lake is provisioned for a specific Azure subscription and resource group, you can't migrate it to a different subscription or resource group.
5. Select **Setup**.

The data lake and data risk graph setup process begins, and onboarding might take up to 60 minutes to complete. You can close the setup panel while the process is running. After the onboarding process completes, you see *Complete* on **Set up data lake & risk graph**. The data risk graph shows events that occur after your Microsoft Sentinel data lake was created or onboarded.

Initial processing of data and data risk graph availability for an investigation can take 24–48 hours.

Important

When the data risk graph is first created, it includes the most recent seven days of data. As the data risk graph refreshes over time, the look-back window expands up to a maximum of 30 days. It might take some time for the data risk graph to reach the full 30-day window, so expect gradual growth after initial setup.

## Use data risk graph

Data risk graph in Insider Risk Management uniquely visualizes correlations between impacted data, users, and their activities. It provides critical context to guide mitigation and next steps. For example, when you uncover an alert related to a highly sensitive document, data risk graphs give you visibility into which users downloaded it or if they accessed it from an IP address flagged as risky by your organization's security signals. This visibility lets you uncover new nodes to a data security incident, like additional users or new content related to an alert.

To view the data risk graph for an alert, you must be assigned the *Insider Risk Management Graph Reader* role. This role is included by default in several Insider Risk Management built-in role groups. For more information, see [Assign permissions in Insider Risk Management](insider-risk-management-permissions).

Important

All user names are visible in data risk graph, even if pseudonymization is enabled in [Insider Risk Management privacy settings](insider-risk-management-settings-privacy).

To use the data risk graph in Insider Risk Management, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with an account assigned the *Insider Risk Management Graph Reader* role.
2. Select the **Insider Risk Management** solution card, then select **Alerts** in the left nav.
3. Select an alert to review, then select the **Data risk graph** tab.
4. Filter the time as applicable and select individual data risk graph nodes for more information about each connection during triage.
5. Expand relationships in the graph by selecting the + icon on users or assets.

The data risk graph contains several nodes. Selecting a node shows details about the node:

- **User details**: Shows information about users associated with the alert. This information includes organization information for each user, including User Principal Name (UPN), labels, location, job title, and more.
- **Data details**: Shows information about files and sites. This information includes the object location, type, labels, and more.

You can view data risk graph information for users based on the last 30 days of activity. This fixed duration isn't extendable.