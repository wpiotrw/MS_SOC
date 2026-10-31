---
layout: Conceptual
title: Search for eDiscovery activities in the audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides guidance about eDiscovery activities that are logged in the Microsoft Purview audit log.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: fe7ffe56-2bc9-47e0-3b9d-e17de21ca3a3
document_version_independent_id: fe7ffe56-2bc9-47e0-3b9d-e17de21ca3a3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-audit-log.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-audit-log
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-audit-log.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 8c583689-9717-7a75-3d21-f9ef4c626d6c
---

# Search for eDiscovery activities in the audit log | Microsoft Learn

The audit log records eDiscovery activities that you perform in Microsoft Purview portal or in PowerShell. Events are logged when administrators, eDiscovery managers, or any user assigned [eDiscovery permissions](edisc-permissions) perform the following tasks:

- Creating and managing [eDiscovery cases](edisc-cases-manage).
- Creating and editing [eDiscovery searches](edisc-search-query) in cases.
- Performing search actions, such as generating statistics, sample, and exporting from search.
- Creating, editing, and removing [eDiscovery holds](edisc-hold-create) from cases.
- Creating [eDiscovery review sets](edisc-review-set-manage) and performing review activities in cases.

For more information about searching the audit log, the permissions that are required, and exporting search results, see [Search the audit log](audit-search).

## How to search for and view eDiscovery activities

Perform the following steps to search for and view eDiscovery activities in the audit log.

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **Audit** solution card.
3. On the **Search** page, complete the following steps:

    1. In the **Activities - friendly names** drop-down list, under **eDiscovery activities**, select one or more eDiscovery activities to search for. For a complete list of all eDiscovery activities, see [Audit log activities](audit-log-activities#ediscovery-activities).

    Note

    The **Activities - friendly names** drop-down list also includes a group of activities named **eDiscovery cmdlet activities** that returns records from the cmdlet audit log.

    1. Select a date and time range to display eDiscovery events that occurred within that period.
    2. In the **Users** box, select one or more users to display search results for. Leave this box blank to return entries for all users.
    3. Select **Search** to run the search using your search criteria.

After the search results are displayed, you can select **Filter results** to filter or sort the resulting activity records. To view details about an activity, select the activity record in the list of search results. A **Details** flyout page is displayed that contains the detailed properties from the event record.

To display additional details, select **More information**. You can export the audit log search results to a .csv file, and then use the Excel Power Query feature to format and filter these records. For more information, see [Export, configure, and view audit log records](audit-log-export-records).

A client **IP Address** field is available for all activities performed in eDiscovery. If the **IP Address** column is blank for an activity, the activity was performed in the legacy eDiscovery experience. All eDiscovery activities performed in eDiscovery include an IP address in the **IP Address** column.

## Audit activities logged for eDiscovery

For a complete listing of all eDiscovery detailed properties and activities included in the audit log, see [Audit log activities](audit-log-activities#ediscovery-activities).