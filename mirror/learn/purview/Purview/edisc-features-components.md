---
layout: Conceptual
title: Learn about eDiscovery features and components | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-features-components
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Explore Microsoft Purview eDiscovery features and components, including cases, data sources, searches, holds, review sets, and exports.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-19T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1028
locale: en-us
document_id: 17072ac0-e872-3a51-5fde-6422a106dee0
document_version_independent_id: 17072ac0-e872-3a51-5fde-6422a106dee0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-features-components.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-features-components
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-features-components.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: fca97184-84f5-e5bb-c98a-f676b1c04ea0
---

# Learn about eDiscovery features and components | Microsoft Learn

This article provides a summary of the key features and components in Microsoft Purview eDiscovery. Use this article to learn about what each feature and component does and to find links to more detailed guidance. For information about the overall eDiscovery workflow, see [Learn about the eDiscovery workflow](edisc-workflow).

## Auditing

eDiscovery activities performed by admins, compliance officers, and other users are logged in the audit log. You can search for and review these activities to track actions taken across cases, searches, holds, and review sets. For more information, see [Search for eDiscovery activities in the audit log](edisc-ref-audit-log). For a complete list of logged eDiscovery activities, see [eDiscovery activities](audit-log-activities#ediscovery-activities).

## Cases

A [case](edisc-cases-manage) contains all searches, holds, and review sets related to a specific investigation. This investigation might include responding to regulatory and litigation requests. You can also assign members to a case to control who can access the case and view the contents of the case. eDiscovery also supports new case creation integration with [Microsoft Purview Insider Risk Management](insider-risk-management-cases) cases.

Two general types of cases exist in eDiscovery:

- Cases you create in eDiscovery by using **Create case** on the **Cases** dashboard
- A single Content Search case you create in eDiscovery by using **Create case** on the **Content Search** dashboard.

## Content Search case

All content searches are contained in a single eDiscovery case named *Content search*. The **Content Search** option in the eDiscovery (classic) experience in the Microsoft Purview portal is retired.

The new **Content Search** option in the new eDiscovery experience displays a set of all existing content searches in your organization and contains any new content searches that you create in the Microsoft Purview portal.

## Cloud attachments

[Cloud attachments](edisc-cloud-attachments) are links to documents and files shared in Microsoft Teams messages, Outlook emails, and other Microsoft 365 services. Instead of attaching a traditional copy of a file, users share a link to the file stored in SharePoint or OneDrive. eDiscovery can collect these cloud attachments and include them in search results and review sets, ensuring that shared content is preserved and available for review.

## Data sources

In eDiscovery, the concept of *data sources* streamlines the process of identifying and managing data across Microsoft 365 platforms. eDiscovery users select a user, group, or bulk add list of SMTP addresses or URLs, which creates [data sources](edisc-data-sources) and eDiscovery automatically identifies and organizes relevant data stored across platforms. The data source gathers locations related to the user or group (mailboxes, OneDrive sites, SharePoint sites) and adds the locations in the data source hierarchy. eDiscovery users refine the scope by selecting or excluding specific locations as needed.

SharePoint Embedded container support in eDiscovery (preview) lets data sources include supported user-owned and tenant-owned containers. You can discover relevant containers for a selected user, filter the containers by application, add a known container URL, or bulk import supported container URLs.

Group-owned and app-owned SharePoint Embedded containers aren't currently supported. For details, including the compliance boundary limitation, see [Data sources in eDiscovery](edisc-data-sources#sharepoint-embedded-application-content).

## Decryption

eDiscovery supports [decryption](edisc-decryption) of content protected with Microsoft encryption technologies. When you add email messages and attachments encrypted with Microsoft Purview Message Encryption, and documents protected with sensitivity labels or Azure Rights Management, to search results or review sets, the system automatically decrypts them. This capability ensures that protected content is available for review and analysis without requiring manual decryption steps.

## Exports and downloads

After a search associated with an eDiscovery case runs successfully, you can [export the search results](edisc-search-export). When you export search results, mailbox items are downloaded in PST files or as individual messages. When you export content from SharePoint and OneDrive sites, you export copies of native Office documents and other documents. Search export packages expire 14 days after creation and must be downloaded before they're automatically deleted.

If you add search results to a review set from a case, you can also [export review set content](edisc-review-set-export) to a download package. This package is configurable and includes options to export selected documents only, all filtered documents, or all documents in the review set.

## Holds and hold policies

Use an eDiscovery case to create [hold policies](edisc-hold-create) that preserve content relevant to the investigation by applying an eDiscovery hold. Place a hold on the Exchange mailboxes and OneDrive accounts of people you're investigating in the case. You can also place a hold on the mailboxes and sites associated with Microsoft Teams, Microsoft 365 groups, and Viva Engage Groups. When you place content locations on hold, you preserve content until you remove the content location from the hold or delete the hold. Use the [hold management](edisc-hold-manage) dashboard to view hold status, modify holds, and track hold policies across cases. You can also use the [hold report](edisc-hold-report) to view information about holds associated with all eDiscovery cases in your organization.

If needed, you can also place a mailbox on [Litigation Hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) to preserve all mailbox content, including deleted items and original versions of modified items. When you place a mailbox on Litigation Hold, the user's archive mailbox (if it's enabled) is also placed on hold.

## Permissions and licensing

To use any of the eDiscovery-related features in the Microsoft Purview portal, assign the appropriate [permissions](edisc-permissions). The easiest way to assign roles is to add the person to the appropriate role group on the **Role groups** page in the Microsoft Purview portal.

Both admins and users working with eDiscovery cases require a Microsoft 365 Enterprise E3 or E5 license. If an admin account doesn't also have a Microsoft SharePoint E3 license, some SharePoint capabilities might be limited. License both admins and users appropriately. Some eDiscovery capabilities also require [pay-as-you-go billing](edisc-billing) configuration. Additionally, if the admin account has any conditional access Entra policy some operations might be restricted, see [Troubleshoot sign-in problems with Conditional Access](/en-us/entra/identity/conditional-access/troubleshoot-conditional-access?toc=%2Fentra%2Fidentity%2Fconditional-access%2Fmonitoring-health%2Ftoc.json&amp;bc=%2Fentra%2Fidentity%2Fconditional-access%2Fmonitoring-health%2Fbreadcrumb%2FTOC.json) to troubleshoot policy issues.

Tip

You can view your own permissions on the eDiscovery overview page in the Microsoft Purview portal. You must have at least one role assigned for your permissions to be displayed.

## Processes

eDiscovery includes a [Process report](edisc-process-report) that lists all activities that count towards case concurrency and daily limits in eDiscovery for a defined time period. Processes in eDiscovery (preview) are activities associated with specific tasks that support cases, searches, and review sets. User actions trigger processes when using these components.

*eDiscovery administrators* and *eDiscovery Managers* (preview) can access this report. [Process managers](edisc-process-managers) help you view information that is automatically scoped to cases, searches, review sets, and holds.

## Review sets

A [review set](edisc-review-set-manage) is a secure, Microsoft-provided Azure Storage location in the Microsoft cloud. When you add data to a review set, the collected items are copied from their original content location to the review set. Review sets provide a static, known set of content that you can search, filter, tag, analyze, and predict relevancy using predictive coding models. You can also track and report on what content gets added to the review set.

Key review set capabilities include:

- [Search and filter content](edisc-review-set-search) using the query condition builder to focus on specific subsets of documents.
- Use the [Advanced review set explorer (preview)](edisc-review-set-explorer) to run Kusto Query Language (KQL) queries directly against review set data for advanced filtering, aggregation, and visualization.
- [Group and view items](edisc-review-set-view) using different grouping options and specialized viewers to examine item details.
- [Tag items](edisc-review-set-tagging) to organize content, identify relevant documents, and track review progress using customizable tag structures.
- [Run analytics](edisc-review-set-analytics) to identify near-duplicate documents, email threads, and themes, helping reduce the volume of content to review.
- [Export items](edisc-review-set-export) from a review set to a download package for use outside of eDiscovery.

## Searches

Use [search](edisc-search-query) to quickly find content relevant to a case. Searches find content across [Exchange mailboxes](edisc-search-mailboxes), [SharePoint sites and OneDrive locations](edisc-search-sites), [Microsoft Teams](edisc-search-teams) conversations, and [Copilot and AI application data](edisc-search-copilot-data).

Create and run different searches that are associated with the case. Build search queries using the [condition builder](edisc-condition-builder) for a guided experience, or use [Keyword Query Language (KQL)](edisc-keyword-query-language) for advanced query syntax with autocompletion support.

You can also:

- View [search statistics](edisc-search-results#statistics-dashboard) for insights on data volume, content locations, and query hit counts to help you refine your search.
- View [search samples](edisc-search-results#sample-dashboard) to examine a representative set of items returned by the search criteria.
- Preview the search results to quickly verify whether the relevant data is being found.
- Revise a query and rerun the search.
- [Export the search results](edisc-search-export) or [add the search results to a review set](edisc-search-add-to-review-set).

## Trigger events

Trigger events are activities that escalate in your organization and start the creation of a new case in eDiscovery. These events can be requests from internal or external partners, integrated events associated with alerts in other Microsoft Purview solutions (for example, [Insider Risk Management cases](insider-risk-management-cases)), or any other activity that might benefit from the search, investigation, and mitigation actions included with eDiscovery. For more information, see [Learn about the eDiscovery workflow](edisc-workflow).

## Ready to get started?

- [Get started with eDiscovery](edisc-get-started)
- [Learn about the eDiscovery workflow](edisc-workflow)