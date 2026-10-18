---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Overview of people relationships in Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/people-relationships-m365?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: People relationships in Microsoft 365 enable rich organizational context across profile cards and Copilot. Learn which relationship types are supported and how to bring your data into Microsoft 365.
ms.date: 2026-07-22T00:00:00.0000000Z
author: Sameergupta-2019
ms.author: samegupt
ms.reviewer: ellenwehrle
ms.topic: overview
manager: rampo
ms.service: microsoft-365-admin
ms.collection: not-ai
locale: en-us
document_id: b57a4a59-5c50-91a6-23fe-7eb9ce19f2d7
document_version_independent_id: b57a4a59-5c50-91a6-23fe-7eb9ce19f2d7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/people-relationships-m365.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/people-relationships-m365
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/people-relationships-m365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 95f3d7a0-465a-b7fc-9ef0-894f298679e9
---

# Overview of people relationships in Microsoft 365 - Microsoft 365 admin | Microsoft Learn

When Microsoft 365 has people relationship data, it can show up in people experiences such as [Profile card](https://support.microsoft.com/Outlook/profile-cards-in-microsoft-365), [Org explorer](https://support.microsoft.com/topic/org-explorer-40c65909-b12d-4ab9-8d6c-a1592789dc8e), and Microsoft Copilot to help users understand organizational context. The experiences and visualizations that are available depend on the relationship type and the data available for the person.

Microsoft 365 experiences and Copilot can surface the following types of key formal people relationships when the relevant data is available:

- Manager
- Assistant
- Dotted-Line manager
- Other custom relationships

## Manager

A **direct manager** or simply **manager** represents a person's primary reporting relationship within an organization. This relationship helps users understand organizational hierarchy and reporting structure. When manager data is available, Microsoft 365 People experiences and Microsoft Copilot can surface this relationship.

## Assistant

An **Assistant** relationship helps users identify people who provide administrative or operational support to another employee. [Learn more.](https://support.microsoft.com/office/add-an-assistant-on-your-profile-in-microsoft-365-66080b84-e98b-40bb-baa6-f5acdca2b28f)

## Dotted-Line manager

A **Dotted-Line manager** represents a reporting relationship in addition to a person’s direct manager. Organizations commonly use dotted-Line manager relationships when work spans teams, projects, regions, or functions. Some organizations might use a different label for this relationship in their HR systems, such as *People Lead* or *Capability Manager*. If Dotted-Line manager and the related relationship label data is available for a person, Microsoft Copilot uses this data to surface rich responses to organization hierarchy related queries.

## Other custom relationships

Organizations often maintain relationship types that are specific to their operating model, business processes, or organizational structure. Examples include relationships such as Mentor or Business Partner when those relationship types are defined in the organization's source systems. Microsoft Copilot can surface these custom people relationships when the relationship data is available through supported people data connectors.

## How organizations bring people relationship data into Microsoft 365

Organizations can bring supported people relationship data into Microsoft 365 through Microsoft 365 Copilot connectors for people data.

For more information, see:

- [Organizational Data in Microsoft 365 | Microsoft Learn](/en-us/viva/organizational-data)
- [Organizational Data in Microsoft 365 - Attribute reference | Microsoft Learn](/en-us/viva/orgdata-attributes)