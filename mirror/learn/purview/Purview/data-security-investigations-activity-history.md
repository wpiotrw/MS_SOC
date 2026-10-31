---
layout: Conceptual
title: Use the Activity history in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-activity-history
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Activity history in Data Security Investigations to track searches, scopes, AI analysis, and mitigation activities for better insights.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
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
locale: en-us
document_id: 37c26f9a-42d1-9672-3f32-b4ecd14e1d43
document_version_independent_id: 37c26f9a-42d1-9672-3f32-b4ecd14e1d43
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-activity-history.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-activity-history
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-activity-history.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 2e5539b2-d5d5-86c2-11ac-9de98c741fd1
---

# Use the Activity history in Data Security Investigations | Microsoft Learn

The Activity history for Data Security Investigations shows information about activities you perform in each area of your investigation. It includes activities associated with searches, investigation scopes, AI analysis, and mitigation activities.

Each time you create or request an activity in a workflow area, the system automatically starts and logs specific activities in the Activity history. For example, if you search for data and select **Estimate scope** in an investigation, the **Generate statistics** and **Generate sample** activities appear in the Activity history list for the investigation.

To view and manage activities, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select the **Activities** tab.

## Activity history dashboard

The Activity history dashboard lists all the activities for an investigation and shows the following information for each activity:

- **Activity type**: The type of activity.
- **Status**: The status of the activity.
- **Export name**: The name of the export. For non-export activity types, this value is blank.
- **Created**: The date and time the activity was created.
- **Completed**: The date and time the activity was completed.
- **Duration**: The duration of the activity.
- **Created by**: The user that created the activity.

To customize the columns display for the Activity history, select **Customize columns** to choose the columns to display or drag and drop the columns in the list to reorder. To download the list of activities and the column information, select **Download list** to create a .csv file containing this information.

## Group activities

When you view a large list of activities for an area, it's often helpful to group activities. Select **Group** to group review sets by the following parameters:

- **None**: Activities are ungrouped in the Activity history.
- **Activity type**: Activities grouped by the *Activity type* values.
- **Created by**: Activities grouped by the *Created by* values.

## Activity details

Select an activity listed in the Activity history for more information in the following areas:

- **Overview** tab: Lists a summary of information for the activity. Includes a calculation for the time remaining to completion for in-progress activities. Select **Download report** to combine all **Overview** information into a single .zip file.
- **Settings** tab: Summarizes the **Statistics view** setting options selected for the investigation.

## Progress bar

When you select an activity in the Activity history, a progress bar appears that shows details about the current state of the activity. For long-running activities, the progress bar has three phases:

- **Assessment phase**: In this phase, the progress bar submits the progress and backend services assess the scope of the activity. This activity includes examining the input conditions based on data sources, query, and relevant activity settings. The service analyzes the scope of the work and identifies the number of locations and number of items for activities. During this phase, a completion estimate isn't available and a flashing progress bar is displayed. The progress bar displays the status of the assessment while the scope is calculated. When all locations and items are identified, the activity transitions to the next phase.
- **In progress phase**: In this phase, the progress bar displays the current status, number of locations, and number of items for the activity. An estimated completion and current elapsed time are displayed in hours, minutes, and seconds.
- **Catch-up phase (optional)**: If there are locations or items with errors, activities are retried. The progress of any retries is displayed.

## Download activity list

To download a .csv file of the activity items on the Activity history dashboard, select **Download list** on the dashboard command bar.

## Activity types and descriptions

These activities start when users take actions to use and manage searches, investigation scopes, AI activities, and more.

| Activity type | Area | Description |
| --- | --- | --- |
| Add to scope | Investigation scope | A user adds search results to an investigation scope. The process copies the items to an Azure Storage location and then reindexes those items in the Azure Storage location. This new index enables querying and analyzing items in the data set. |
| Audit search | Search | A user submits an [audit search](data-security-investigations-search#audit-search) to query the unified audit log for content-associated activities. This activity queries the audit log and identifies content items associated with the specified activities. |
| Categorize | AI analysis | A user [categorizes](data-security-investigations-ai-analysis#use-categorization) items in an investigation scope. |
| Examine | AI analysis | A user analyzes data in an investigation scope by running AI examination and recommendation tools, such as [Credentials](data-security-investigations-credentials), [Mitigation](data-security-investigations-mitigation), [Risks](data-security-investigations-risks). |
| Generate sample | Search | After a user creates and runs a new search (or reruns an existing search), the search tool prepares a [sample](data-security-investigations-search#samples-dashboard) subset of items that match the search query for preview. Previewing search results helps you determine the effectiveness of the search. |
| Generate scope | Search | After a user creates and runs or reruns a search, the search tool searches the index for items that match the search query and prepares a [scope](data-security-investigations-search#scope-dashboard) estimate that includes the number and total size of all items by the search, the number of data sources searched, and other relevant pattern to the search hits like keywords, sensitive information types, and more. |

Note

When an [audit search](data-security-investigations-search#audit-search) is submitted, query chunking creates an *Add to scope* activity and multiple additional activities to process the results. Seeing multiple *Add to scope* activities after an audit search is expected behavior.

## Activity status

The following table describes the different status states for activities:

| **Status** | **Description** |
| --- | --- |
| Abandoned | The system automatically stops the activity. This stoppage might occur due to excessive activities time or other reasons. |
| Canceled | The user cancels the activity. |
| Complete | The activity successfully completes. |
| Failed | The activity encounters an error and fails to complete. This error might be caused by a wrongly formatted query. |
| In progress | The activity is in progress. You can monitor the progress of the activity in the progress bar in the applicable area. |

Note

In addition to tracking activities on this page, Data Security Investigations sends notifications through the Microsoft Purview Notification Center and email when setup completes and investigations are ready to use. For more information, see [Email and portal notifications](data-security-investigations-workflow#email-and-portal-notifications).