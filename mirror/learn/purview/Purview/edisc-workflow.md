---
layout: Conceptual
title: Learn about the eDiscovery workflow | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-workflow
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the eDiscovery workflow in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: b41ce67a-e04c-2433-189f-cb504bc029a6
document_version_independent_id: b41ce67a-e04c-2433-189f-cb504bc029a6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-workflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-workflow.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 5f2736c4-bfbe-e672-5200-e490735f4248
---

# Learn about the eDiscovery workflow | Microsoft Learn

The eDiscovery workflow helps you quickly identify, investigate, and take action on electronically stored information (ESI) in your organization. Identifying and taking action on ESI items by using eDiscovery uses the following improved workflow:

![eDiscovery workflow diagram.](media/ediscovery-workflow.png)

## Step 1: Escalate from trigger event

Trigger events are activities that escalate in your organization and start the creation of a new case in eDiscovery. These events can be requests from internal or external partners, integrated events associated with alerts in other Microsoft Purview solutions (for example, [Insider Risk Management cases](insider-risk-management-cases)), or any other activity that might benefit from the search, investigation, and mitigation actions included with eDiscovery.

## Step 2: Create and manage cases

A [case](edisc-cases-manage) in eDiscovery contains all searches, holds, and review sets related to a specific investigation. Cases might include responding to regulatory, investigation, and litigation requests. You can also assign members to a case to control who can access the case and view the contents of the case. eDiscovery also supports new case creation integration with Microsoft Purview Insider Risk Management cases.

## Step 3: Search, evaluate results, and refine

After you create a case, use the built-in search tools in eDiscovery to [search the content locations](edisc-search-query) in your organization. You can create and run different searches that are associated with the case. Use conditions (such as keywords) to build multiple search queries that return search results with the data that's most likely relevant to the case. You can also:

- View search statistics that might help you refine a search query to narrow the results.
- Preview the search results to quickly verify whether the relevant data is being found.
- Revise queries and rerun searches.

## Step 4a: Actions from search results

- **Export search results**: After a search in an eDiscovery case successfully completes, you can [export the search results](edisc-search-export). When you export search results, mailbox items are downloaded in PST files or as individual messages. When you export content from SharePoint and OneDrive sites, copies of native Office documents and other documents are exported. Search exports expire 14 days after creation, so download the export packages before they're automatically deleted.
- **Create review sets**: A [review set](edisc-review-set-manage) is a secure, Microsoft-provided Azure Storage location in the Microsoft cloud. When you [add data to a review set](edisc-search-add-to-review-set), the collected items are copied from their original content location to the review set. You can add all search results or [configure sampling](edisc-search-add-to-review-set#create-or-add-results-to-a-review-set) to add a representative subset. Review sets provide a static, known set of content that you can search, filter, tag, and analyze. You can also track and report on what content gets added to the review set.

## Step 4b: Create holds

To preserve and protect data that's relevant to an investigation, [place an eDiscovery hold](edisc-hold-create) on the data sources associated with a case. After creating a case, you can immediately place a hold on the content locations of the people of interest in your investigation. You can also create query-based holds if needed. Content locations include Exchange mailboxes, SharePoint sites, OneDrive accounts, and mailboxes and sites associated with Microsoft Teams and Microsoft 365 Groups. While placing a hold is optional, creating a hold preserves content that might be relevant to the case during the investigation.

When you create a hold, you can preserve all content in specific content locations or you can create a query-based hold to preserve only the content that matches a hold query. In addition to preserving content, another good reason to create holds is to quickly search the content locations on hold (instead of having to select each location to search) when you create and run searches in the next step. After you complete your investigation, you can release any hold that you created. For more information, see [Manage holds in eDiscovery](edisc-hold-manage).

## Step 5: Review and take action from review sets

- **Search for content**: In most cases, it's useful to dig deeper into the content in a review set and organize it to facilitate a more efficient review. Using [filters and queries](edisc-review-set-search) in a review set helps you focus on a subset of documents that meet the criteria of your review.
- **Run KQL queries (preview)**: Use the [Advanced review set explorer (preview)](edisc-review-set-explorer) to run Kusto Query Language (KQL) queries directly against review set data for advanced filtering, aggregation, pattern matching, and data visualization.
- **Run analytics**: eDiscovery provides an integrated analytics tool that helps you further cull data from the review set that you determine isn't relevant to the investigation. In addition to reducing the volume of relevant data, eDiscovery also helps you save legal review costs by letting you organize content to make the review process easier and more efficient. For more information, see [Analyze data in a review set in eDiscovery](edisc-review-set-analytics).
- **Tag items**: Organizing content in a review set is important to complete various workflows in the eDiscovery process. This organization often includes identifying relevant content, culling unnecessary content, and identifying content that needs review by an expert or attorney. When experts, attorneys, or other users review content in a review set, they can capture their opinions related to the content by using tags. Tags provide structure and organization to items included in an investigation. For more information, see [Tag documents in a review set in eDiscovery](edisc-review-set-tagging).
- **Create a Query report (preview)**: Generate and download a [consolidated report](edisc-review-set-query-report) on multiple queries for a review set. This report lets you quickly see the total count and volume of filtered items on a particular keyword search or multiple compound KeyQL queries.
- **Add items from the review set to another review set**: In some cases, it might be necessary to select documents from one review set and work with them individually in [another review set](edisc-review-set-add-to-other-review-set).
- **Export items**: After you search for and find data that's relevant to your investigation, you can export it out of your Microsoft 365 organization for review by people outside of the investigation team. In addition to the exported data files, the export package contains an export report, a summary report, and an error report. For more information, see [Export documents from a review set in eDiscovery](edisc-review-set-export).

Throughout the workflow, eDiscovery administrators can use [Process reports](edisc-process-report) to track activities that count towards concurrency and daily limits, and [Process managers](edisc-process-managers) to view process information scoped to cases, searches, review sets, and holds.

## Ready to get started?

- [Learn more about eDiscovery features and components](edisc-features-components)
- [Get started with eDiscovery](edisc-get-started)