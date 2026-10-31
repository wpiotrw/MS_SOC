---
layout: Conceptual
title: Use Process managers in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-process-managers
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to review and manage processes with the Process managers in eDiscovery.
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
document_id: ef957dcf-b267-9d44-2747-5885fbd375ed
document_version_independent_id: ef957dcf-b267-9d44-2747-5885fbd375ed
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-process-managers.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-process-managers
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-process-managers.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 06317d70-ccc9-d0da-f902-0cc8e5f0a6fe
---

# Use Process managers in eDiscovery | Microsoft Learn

Each primary area in eDiscovery includes a process manager. These managers let you view processes and related information for a specific area. You can access process managers by selecting **Process manager** in each of the following areas:

- [Cases](edisc-cases-manage)
- [Searches](edisc-search-query)
- [Review sets](edisc-review-set-manage)
- [Holds](edisc-hold-create)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Process manager information

Each area's process manager shows information about processes performed in that area. For example, if you export data from the review set, an *Export* process item appears in the process manager list for the review set, but not in the process manager lists for searches and holds. Each process manager contains the following information for its area:

- **Process type**: The type of process.
- **Status**: The status of the process.
- **Export name**: The name of the export. For nonexport process types, this value is blank.
- **Created**: The date and time the process was created.
- **Completed**: The date and time the process was completed.
- **Duration**: The duration of the process.
- **Created by**: The user that created the process.

To customize the columns display for the process manager, select **Customize columns** to choose the columns to display or drag and drop the columns in the list to reorder. To download the list of processes and the column information, select **Download list** to create a .csv file containing this information.

## Grouping processes

When you view a large list of processes for an area, it's often helpful to group processes. Select **Group** to group review sets by the following parameters:

- **None**: Processes are ungrouped in the Process manager.
- **Process type**: Processes grouped by the *Process type* values.
- **Created by**: Processes grouped by the *Created by* values.

## Process details

Select a process listed in the process manager for more information in the following areas:

- **Overview** tab: Lists a summary of information for the process. Includes a calculation for the time remaining to completion for in-progress processes. Select **Download report** to combine all **Overview** information into a single .zip file. This file contains the files included in the [Download report](edisc-process-report-use#download-report) guidance.
- **Settings** tab: Summarizes the **Search & analytics** setting options selected for the case.

## Progress bar

When you select a process in the Process manager, a progress bar appears that shows details about the current state of the process. For long-running processes, there are three phases:

- **Assessment phase**: In this phase, the progress is submitted and backend services assess the scope of the process. This assessment includes examining the input conditions based on data sources, query, and relevant process settings. The service analyzes the scope of the work and identifies the number of locations and number of items for processing. During this phase, a completion estimate isn't available and a flashing progress bar is displayed. The progress bar displays the status of the assessment while the scope is calculated. When all locations and items are identified, the process transitions to the next phase.
- **In progress phase**: In this phase, the progress bar displays the current status, number of locations, and number of items for the process. An estimated completion and current elapsed time are displayed in hours, minutes, and seconds.
- **Catch-up phase (optional)**: If there are locations or items with errors, processing is retried. The progress of the retries is displayed.