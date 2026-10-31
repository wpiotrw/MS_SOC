---
layout: Conceptual
title: Overview of Content search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-content-search-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the Content search eDiscovery tool in the Microsoft Purview portal to quickly find email in Exchange mailboxes, documents in SharePoint sites and OneDrive locations, and instant messaging conversations in Skype for Business.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- highpri
- purview-compliance
- content-search
locale: en-us
document_id: 11bdfe6f-2e5f-8a33-2580-83e548918ec0
document_version_independent_id: 11bdfe6f-2e5f-8a33-2580-83e548918ec0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-content-search-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-content-search-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-content-search-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: fbc9fab0-1643-7ea4-5c51-63275094c155
---

# Overview of Content search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Use the Content search tool in the Microsoft Purview portal to quickly find email in Exchange mailboxes, documents in SharePoint sites and OneDrive locations, and instant messaging conversations in Skype for Business. You can use the content search tool to search for email, documents, and instant messaging conversations in collaboration tools such as Microsoft Teams and Microsoft 365 Groups.

## Search for content

The first step is to starting using the Content search tool to choose content locations to search and configure a keyword query to search for specific items. Or, you can just leave the query blank and return all items in the target locations.

- [Create and run](ediscovery-content-search) a Content search.
- [Build search queries and use conditions](ediscovery-keyword-queries-and-search-conditions) to narrow your search.
- [Feature reference](ediscovery-content-search-reference) for Content search.
- [Configure search permissions filtering](ediscovery-permissions-filtering-for-content-search) so that an eDiscovery manager can only search subset of mailboxes or sites in your organization.
- [Search cloud-based mailboxes](ediscovery-search-cloud-based-mailboxes-for-on-premises-users) for on-premises users in Microsoft 365.
- [View keyword statistics](ediscovery-view-keyword-statistics-for-content-search) for the results of a search and then refine the query if necessary.
- [Search for third-party data](use-content-search-to-search-third-party-data-that-was-imported) that your organization has imported to Microsoft 365.
- [Preserve Bcc recipients](/en-us/exchange/policy-and-compliance/holds/preserve-bcc-recipients-and-group-members) so you can search for them.
- [Search for Microsoft 365 Copilot and Microsoft 365 Copilot Chat data](/en-us/purview/ai-microsoft-purview) (user prompts and Copilot responses) stored in custodian mailboxes.

## Perform actions on content you find

After you run a search and refine it as necessary, the next step is to do something with the results returned by the search. You can export and download the results to your local computer or in the case of an email attack on your organization, you can delete the results of a search from user mailboxes.

- [Export the results of a content search](ediscovery-export-search-results) and download them to your local computer..
- [Search for and delete email messages](ediscovery-search-for-and-delete-email-messages), such as messages that content a virus, dangerous attachments, or phishing messages.

## Learn more about content search

Content search is easy to use, but it's also a powerful tool. Behind-the-scenes, there's a lot going on. The more you know about it and understand its behavior and its limitations, the more successful you'll be using it for your organization's search and investigation needs.

- [Estimated and actual search results](ediscovery-differences-between-estimated-and-actual-search-results) and the reasons why there might be differences between them when you export and download search results.
- [Partially indexed items in Exchange and SharePoint](ediscovery-partially-indexed-items-in-content-search) and how to include or exclude them when you export and download search results.
- [Investigate partially indexed items](ediscovery-investigating-partially-indexed-items) and determine your organization's exposure to them.

## Use scripts for advanced scenarios

Sometimes you have to perform more advanced, complex, and repetitive content search tasks. In these cases, it's easier and faster to use commands in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell).

To help make this easier, we've created several Security & Compliance PowerShell scripts to help you complete complex content search-related tasks.

- [Search specific mailbox and site folders](ediscovery-use-content-search-for-targeted-collections) (called a *targeted* collection) when you're confident that items responsive to a case are located in that folder.
- [Search the mailbox and OneDrive location](ediscovery-search-mailboxes-and-onedrive-for-users) for a list of users.
- [Create, report on, and delete multiple searches](ediscovery-create-reports-and-delete-multiple-content-searches) to quickly and efficiently identify and cull search data.
- [Clone a content search](ediscovery-clone-a-content-search) and quickly compare the results of different keyword search queries run on the same content locations; or use the script to save time by not having to re-enter a large number of content locations when you create a new search.