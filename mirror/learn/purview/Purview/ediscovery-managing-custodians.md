---
layout: Conceptual
title: Work with custodians in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-managing-custodians
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the custodian management tool in eDiscovery (Premium) to manage data for a legal case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.assetid: 
ms.custom:
- seo-marvel-apr2020
locale: en-us
document_id: 59160de9-4e51-2c25-816b-dcb208da3ec4
document_version_independent_id: 59160de9-4e51-2c25-816b-dcb208da3ec4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-managing-custodians.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-managing-custodians
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-managing-custodians.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 762c2e24-591d-bb6a-f2d4-c0e66124327c
---

# Work with custodians in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When an organization responds to a legal investigation, the workflow around identifying, preserving, and collecting potentially relevant content is based on the people in the organization who are the custodians of relevant data. In eDiscovery, these individuals are called *data custodians* (or just *custodians*) and are defined as "persons having administrative control of a document or electronic file." For example, the custodian of an email message could be the owner of the mailbox that contains the relevant message.

Additionally, there might be content located in mailboxes and sites that aren't associated with a custodian but that's relevant to the case. Content locations where case custodians don't have administrative control but might be owners of relevant data, are known as *non-custodial data sources*.

In an eDiscovery (Premium) case, legal teams can add individuals in their organization as custodians, and identify and preserve custodial data sources such as Exchange mailboxes, OneDrive accounts, and SharePoint and Teams sites. They can also identify and preserve non-custodial data sources. By using the built-in custodian and data source management tool in eDiscovery (Premium), organizations can secure electronically stored information from inadvertent (or intentional) deletion. This tool lets you eliminate the time-consuming and error-prone process of manually having to perform the legal hold processes.

For more information about working with custodians, see the following articles:

- [Add custodians to a case](ediscovery-add-custodians-to-case)
- [Bulk-add custodians to a case](ediscovery-bulk-add-custodians)
- [Manage custodians in a case](ediscovery-manage-new-custodians)
- [View custodian activity](ediscovery-view-custodian-activity)
- [Add non-custodial data sources to a case](ediscovery-non-custodial-data-sources)