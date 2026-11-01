---
layout: Conceptual
title: Learn about Microsoft Sentinel in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-sentinel
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Microsoft Sentinel integration for data risk graphs in Microsoft Purview.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-08-27T00:00:00.0000000Z
ms.service: purview
audience: Admin
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-manage
ms.custom:
- admindeeplinkCOMPLIANCE
- admindeeplinkEXCHANGE
- sfi-image-nochange
- msecd-doc-authoring-1024
ai-usage: ai-assisted
locale: en-us
document_id: edc96460-9cfb-2d1e-5ae1-d9de7eb1cdaf
document_version_independent_id: edc96460-9cfb-2d1e-5ae1-d9de7eb1cdaf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-sentinel.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-sentinel
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-sentinel.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/8f37329d-5c2f-4d50-b9b8-aa5cf54dbffe
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://authoring-docs-microsoft.poolparty.biz/devrel/e13db295-3de6-46d5-bcdf-8785a76e3843
platformId: 09cd8b6f-1f7e-0674-a3da-2522cf109f96
---

# Learn about Microsoft Sentinel in Microsoft Purview | Microsoft Learn

[Microsoft Sentinel](/en-us/azure/sentinel/overview) is a scalable, cloud-native security information and event management (SIEM) solution that delivers cost-efficient security across multicloud and multiplatform environments with built-in AI, automation, threat intelligence, and a modern data lake and graph architecture. The Microsoft Sentinel [data lake](/en-us/azure/sentinel/datalake/sentinel-lake-overview) and [graph](/en-us/azure/sentinel/datalake/sentinel-graph-overview) are tenant-wide repositories for collecting, storing, and managing large volumes of security-related data from various sources. These solutions integrate with Microsoft Purview solutions and support data risk graphs.

Important

**Data risk graph is being deprecated.** The data risk graph in Microsoft Purview Insider Risk Management will be retired on **November 24, 2026**. After that date, the data risk graph experience will no longer be available.

Data risk graph capabilities are available in the following Microsoft Purview solutions:

- [Microsoft Purview Data Security Investigations (preview)](data-security-investigations)
- [Microsoft Purview Insider Risk Management](insider-risk-management)

Partner integrations are available in the following Microsoft Purview solution:

- [Microsoft Purview Data Security Posture Management](data-security-posture-management-learn-about)

## Data risk graph

Powered by Microsoft Sentinel graph, data risk graphs in Microsoft Purview solutions allow you to view connections between impacted assets, users, and their activities in an interactive graph experience. Microsoft Sentinel graph is a unified graph analytics capability within Microsoft Sentinel that powers graph-based experiences across Microsoft Purview solutions. For more information about Microsoft Sentinel graph, see [What is Microsoft Sentinel graph?](/en-us/azure/sentinel/datalake/sentinel-graph-overview)

Data risk graphs natively represent the real-world web of users, devices, cloud resources, data flows, activities, and attacker actions associated with activities identified in Microsoft Purview solutions. By connecting activities to assets, analysts can:

- **Understand context**: View a user's role and file locations to assess whether behavior is typical or suspicious.
- **Assess impact**: Visualize which assets might be impacted by tracing activity paths within sensitive sites.
- **Collaborate effectively**: Use the data risk graph to communicate findings with stakeholders by showing connections between users, actions, and assets.

![Screenshot of a data risk graph in Microsoft Purview showing connected nodes for users, sites, files, and activities with relationship badges.](media/purview-data-risk-graph.png)

### Data risk graph controls

Data risk graphs in Microsoft Purview solutions have the following controls to help you discover and work with information about item relationships and connected nodes:

- **Movable nodes**: Change the presentation of the graph by moving nodes to customize the view of nodes, relationships, and connections.
- **Layers**: The **Vulnerability** layer is presented as the default **Insights layer** in a data risk graph. To change layers, select the **Layers** control in the lower-left corner of a graph.
- **Maximize the graph view**: To quickly maximize a graph, select the **Zoom to fit** control in the lower-left corner of a graph.
- **Scale the graph to any size**: To enlarge or reduce the size of the graph, select the **+** or **-** controls in the lower-left corner of a graph. Select the **Settings** control in the lower-left corner of a graph to enable or disable the **Zoom slider** control.

### Data risk graph features

Data risk graphs in Microsoft Purview solutions include the following features to help you discover and work with information about item relationships and connected nodes:

- **Nodes**: Nodes include users, sites, files, and IP addresses associated with each other.
- **Relationships**: Connections between nodes describing how they interact with each other. Badges on each relationship describe actions and meanings. For example, badges might include *Signed in from*, *Downloaded*, *Uploaded*, and more.

## Prerequisites and onboarding changes

To use the data risk graph in supported Microsoft Purview solutions, you must onboard to the Microsoft Sentinel data lake and graph and meet specific requirements. Additionally, when you onboard to data lake and graph, the onboarding process makes changes in several areas and services in your organization. The onboarding process includes changes to your existing data lake, primary and other connected workspaces in Microsoft Defender, and more.

Data risk graphs use a pay-as-you-go billing model to ingest and store data, but data risk graph usage doesn't incur any extra charges. If data needed to populate the data risk graph is already enabled or stored, you don't incur any extra charges.

For step-by-step guidance for all prerequisites, billing information, and changes made in your onboarding process, see the following articles:

- [Prerequisites for Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding#prerequisites)
- [Changes made when onboarding to Microsoft Sentinel data lake and Microsoft Sentinel graph](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding)

## Configure data risk graph

After you meet the prerequisites for Microsoft Sentinel data lake and Microsoft Sentinel graph and understand the changes made during the onboarding process, you're ready to configure data risk graph in Microsoft Purview solutions. The data lake for your organization stores all activity and asset data from Microsoft Purview data risk graphs.

To configure data risk graph in Microsoft Purview solutions, see the following articles:

- [Configure data risk graph in Data Security Investigations (preview)](data-security-investigations-data-risk-graph)
- [Configure data risk graph in Insider Risk Management](insider-risk-management-data-risk-graph)

## Partner integrations

Set up Microsoft Sentinel data lake to integrate partner solutions and centralize security posture monitoring across all data sources. To see the available partner solutions and then select one from Data Security Posture Management, you must first [connect to the Microsoft Sentinel content hub](/en-us/azure/sentinel/sentinel-solutions-deploy?tabs=defender-portal#prerequisites). The Microsoft Sentinel content hub is the centralized catalog where you discover and deploy partner solutions. Initial partners include Cyera (for Snowflake), BigID (for Databricks), OneTrust (for Google Cloud Platform), and Varonis (for Salesforce).