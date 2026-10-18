---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Automatic Service Health Incident Creation - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-incidents?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
ROBOTS: NOINDEX, NOFOLLOW
search.appverid:
- MET150
description: A feature that creates new ServiceNow incidents when a Microsoft Service Health Incident is published for your Microsoft 365 tenant.
locale: en-us
document_id: 9bceee8f-8de9-727d-9f5d-d479e09a1997
document_version_independent_id: 9bceee8f-8de9-727d-9f5d-d479e09a1997
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/servicenow-incidents.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/servicenow-incidents
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/servicenow-incidents.md
platformId: 3f68ab74-9fb4-2425-608c-493820fd56ac
---

# Automatic Service Health Incident Creation - Microsoft 365 admin | Microsoft Learn

Important

Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

The Microsoft 365 support integration app enables you to create ServiceNow incidents when a Microsoft Service Health Incident is published for your tenant. To use this feature, you must use version 2.1.0 or later. This feature helps IT teams by automatically creating incidents in ServiceNow when Microsoft publishes new service health incidents.

![image of Microsoft 365 servicehealth dashboard.](../../media/servicenowincident1.png)

Note

This article was partially generated using Azure OpenAI Service. Before publishing, an author reviewed and revised the content as needed. See [Our principles for using AI-generated content in Microsoft Learn](https://aka.ms/ai-content-principles).

When a Microsoft Service Health Incident is updated, the app posts the same updates to the ServiceNow incident. You can choose to have the app automatically close the ServiceNow incident when the Microsoft service health incident is resolved, or you can close it manually.

The properties on the Microsoft service health incident map to properties on the ServiceNow incident.

| Microsoft Service Health | ServiceNow Incident |
| --- | --- |
| Title | Short Description |
| Issue type | Impact |
| Status | Urgency |
| All other fields | Description |

## Configuration

To enable automatic creation of ServiceNow incidents, navigate to **Microsoft 365 Support** &gt; **Service Health** in your ServiceNow instance.

Select **Enable the Microsoft 365 support integration app to create ServiceNow incidents for each Microsoft 365 service health incident**.

![image of servicenow copied incident from service health dashboard.](../../media/servicenowincident2.png)

To automatically close ServiceNow incidents, select **Automatically resolve ServiceNow incident when the Microsoft service health is resolved**.

If the ServiceNow incident is manually closed and this setting is enabled, the app stops posting updates to that incident.

If the ServiceNow incident is automatically resolved, the app stops posting updates to that incident. The ServiceNow incident is resolved with the following settings:

- Resolution code: **Closed/Resolved by Caller**
- Resolution note: **The Microsoft service health incident was resolved on &lt;date\_time&gt;. Please refer to the incident details in the Microsoft 365 Support tab for more information.**

To automatically create ServiceNow incidents, configure the **Assignment group** and **Category** for the app. The **Assigned to** and **Subcategory** aren't required. Setting those values improves routing and reporting.