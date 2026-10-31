---
layout: Conceptual
title: Data risk graph in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-data-risk-graph
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Explore the data risk graph in Data Security Investigations to uncover relationships between users, files, and activities for enhanced incident resolution.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
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
ms.custom:
- sfi-ga-nochange
- sfi-image-nochange
locale: en-us
document_id: 38debe0c-36cb-cb96-1449-320bb50369d3
document_version_independent_id: 38debe0c-36cb-cb96-1449-320bb50369d3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-data-risk-graph.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-data-risk-graph
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-data-risk-graph.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/8f37329d-5c2f-4d50-b9b8-aa5cf54dbffe
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://authoring-docs-microsoft.poolparty.biz/devrel/e13db295-3de6-46d5-bcdf-8785a76e3843
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: f0a6f267-1697-0840-5ef1-d344248c2473
---

# Data risk graph in Data Security Investigations | Microsoft Learn

Important

We are retiring Data risk graph (Explore insights) in Microsoft Purview Data Security Investigations (DSI). **Beginning September 30, 2026**, organizations will no longer be able to configure Data risk graph. The feature will be fully retired and no longer available after **November 30, 2026**.

Data risk graphs in [Data Security Investigations](data-security-investigations) provide a visual investigation experience that combines asset and activity data into a single view. Powered by Microsoft Sentinel integration, it summarizes the previous 30 days of activity for any file scoped in your investigation. It helps you identify risky user accounts that interacted with content of interest and analyze the sequence of events leading up to recent incidents. By enriching analysis with activity insights, data risk graphs can help you resolve your data security incidents faster and with greater confidence.

For more information about Microsoft Sentinel integration, see [Learn about Microsoft Sentinel in Microsoft Purview](purview-sentinel).

Note

[Admin units](purview-admin-units) aren't supported in the data risk graph. If you're scoped to an admin unit, data doesn't appear in data risk graphs.

## Supported activities in data risk graph

The data risk graph currently supports the following exfiltration activities:

- Anonymous links created in SharePoint or OneDrive
- Anonymous links used via SharePoint or OneDrive
- Company links created in SharePoint or OneDrive
- File downloads from SharePoint and OneDrive
- Files renamed in SharePoint and OneDrive

## Before you begin

Before you can use data risk graphs in Data Security Investigations, complete the following steps:

- Learn about [pay-as-you-go billing](/en-us/azure/sentinel/billing) in Microsoft Sentinel for your organization.
- Configure the [prerequisites for Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding#prerequisites).
- Review the [changes made when onboarding to Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding).
- [Create an investigation](data-security-investigations-investigation) in Data Security Investigations.

## Configure data risk graph

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

After you complete the prerequisites, complete the following steps to configure data risk graph in Data Security Investigations:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal with an account assigned the *Global Administrator* or *Security Administrator* role.
2. Select **Overview** in the left navigation.
3. In the **Setup tasks** section, select **Set up data lake and data risk graph**.

    If you don't have the correct permissions to set up the data lake, a notification appears to contact a global or billing administrator in your organization.
4. On the **Setup** tab on **Set up data lake & risk graph (preview)**, configure the following settings:

    1. **Subscription**: Enter the Azure subscription you want to use. Your selected subscription must be valid and accessible. You must be a subscription owner.
    2. **Resource group**: Enter the resource group you want to use. Your selected resource group must be valid and accessible.

    Important

    After the data lake is provisioned for a specific Azure subscription and resource group, you can't migrate it to a different subscription or resource group.
5. Select **Setup**.

Important

When the data risk graph is first created, it includes the most recent seven days of data. As the data risk graph refreshes over time, the look-back window expands up to a maximum of 30 days. It might take some time for the data risk graph to reach the full 30-day window, so expect gradual growth after initial setup.

The set up process begins and onboarding might take up to 60 minutes to complete. You can close the setup panel while the process is running. After the onboarding process completes, you see *Complete* on **Set up data lake & risk graph (preview)**. The data risk graph shows events that occur after your Microsoft Sentinel data lake was created or onboarded.

Initial processing of data and data risk graph availability for an investigation might take 24-48 hours.

Important

You always have one data lake. If you already onboarded to the data lake with another Microsoft service, your existing data lake is used. If you never onboarded to the data lake, onboarding in Data Security Investigations enables Microsoft Sentinel data lake and graph in the Defender portal.

## Use data risk graph

Data risk graph in Data Security Investigations uniquely visualizes correlations between impacted data, users, and their activities. It provides critical context to guide mitigation and next steps. For example, upon uncovering a highly sensitive document, data risk graphs give you visibility into which users downloaded it or if they accessed it from a risky IP address. This visibility lets you uncover new nodes to a data security incident, like additional users or new content that requires investigation.

To view the data risk graph for an investigation, you must be assigned to at least one built-in Data Security Investigations role group:

- *Data Security Investigations Admins*
- *Data Security Investigations Investigators*
- *Data Security Investigations Reviewers*

For more information about role groups, see [Assign permissions in Data Security Investigations](data-security-investigations-permissions).

![Data Security Investigations data risk graph example.](media/data-security-investigations-data-risk-graph.png)

To use the data risk graph in Data Security Investigations, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal with an account assigned to a Data Security Investigations role group.
2. Select **Investigations** in the left navigation.
3. Select an investigation to review, then select one of the following options:

    1. On **Summary**, select **Manage scope** on the **Investigation scope** card.
    2. Select the **Analysis** tab to list items included in the **Investigation scope**.
4. Select items (up to 100) included in the scope, and then select **Explore insights**.

    Note

    **Explore insights** isn't available unless you configure Data Security Investigations for Microsoft Sentinel data lake and graph.
5. Filter the time as applicable and select individual data risk graph nodes for more information about each connection during triage.
6. Expand relationships in the graph by selecting the + icon on users or assets.

The data risk graph contains several nodes. Selecting a node shows details about the node:

- **User details**: Shows information about users associated with the investigation. This information includes organization information for each user, including User Principal Name (UPN), labels, location, job title, and more.
- **Relationships**: Shows information about starting and ending connections between nodes. This information includes starting and last connection dates, relationship types, and more.
- **IP addresses**: Shows information about each IP address node.
- **Data details**: Shows information about files and sites. This information includes the object location, type, labels, and more.

You can view data risk graph information for users based on the last 30 days of activity. This duration is fixed and can't be extended.