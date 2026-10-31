---
layout: Conceptual
title: Manage jobs in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-managing-jobs
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: eDiscovery (Premium) jobs help you track the status of long-running processes related to performing various eDiscovery (Premium) tasks.
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
locale: en-us
document_id: cf847aeb-1db7-9272-d718-748eedefbf6e
document_version_independent_id: cf847aeb-1db7-9272-d718-748eedefbf6e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-managing-jobs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-managing-jobs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-managing-jobs.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7d8a82af-2ea2-0fc7-3096-b49405af6b1c
---

# Manage jobs in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

## Jobs report

eDiscovery (Premium) includes a jobs report that lists all jobs that count towards case jobs concurrency and daily limits in eDiscovery for a defined time period. *eDiscovery administrators* and *eDiscovery Managers* (preview) can access this report on the **Reports** &gt; **Jobs report** tab and can use this report to see the job activities across Content Search activities and eDiscovery (Standard and Premium) cases. *eDiscovery Managers* (preview) can view the jobs usage cards at the top of the report, but the jobs list is limited to the cases to which they're assigned.

Important

Jobs listed on the report can't be deleted or removed. Long-running jobs automatically time out after 7 days.

The job report summarizes the following key information for jobs up to the last 30 days:

- All jobs that are in progress or completed (successfully or with error) in a specified time range across eDiscovery Standard and Premium.
- Insights into how far away your organization is from reaching job-related organization-wide limits.
- Creates a .csv report for the list of jobs.
- Filters for job types, statuses, and for hours/days.
- Quick access to case/job pages by selecting case name links.

The following eDiscovery (Premium) job types currently don't count towards the concurrency/daily limits and aren't shown in the report:

- Prepare for export
- Run analytics
- Tag Items
- Compare load sets
- Convert redacted items to PDF
- Relevance train and Relevance load
- Prepare remediation

Note

Any jobs included in the list view of the report and that have run for more than 24 hours do not contribute towards the concurrency/daily limits for your organization.

The following eDiscovery (Premium) jobs started in classic cases don't contribute to throttling limits and aren't reflected in the report. However, these jobs started for cases in the New case format are included in the report:

- Adding non-Microsoft 365 data to a review set
- Adding remediated data to a review set
- Re-indexing custodian data
- Adding data to a review set
- Adding data to another review set

## Job types and descriptions

Long-running processes are associated with specific jobs that support cases, collections, and reporting in Microsoft Purview eDiscovery (Premium). These jobs are triggered by user actions when using and managing cases and collections.

| Job type | Description |
| --- | --- |
| Add external data | A user uploads non-Microsoft 365 data to a review set. The data is also indexed during this process. For example, files from an on-premises file server or a client computer are uploaded to a review set. For more information, see [Load non-Microsoft 365 data into a review set](ediscovery-load-non-office-365-data-into-a-review-set). |
| Add items to another review set | A user adds documents from one review set to a different review set in the same case. For more information, see [Add data to a review set from another review set](ediscovery-add-data-to-review-set-from-another-review-set). |
| Add items to review set | A user adds a collection to a review set. This job consists of two sub jobs:  - **Export** - A list of items in the collection is generated.  - **Ingestion & Indexing** - The items in the collection that match the search query are copied to an Azure Storage location (in a process called *ingestion*) and then those items in the Azure Storage location are reindexed. This new index is used when querying and analyzing items in the data set.  For more information, see [Add search results to a review set](ediscovery-add-data-to-review-set). |
| Adding remediated items to a review set | Data with processing errors is remediated and loaded back into a review set. For more information, see: <br>- [Error remediation when processing data](ediscovery-error-remediation-when-processing-data)<br>- [Single item error remediation](ediscovery-single-item-error-remediation) |
| Apply holds | A user adds custodial and non-custodial sources on the Data sources page and places them on hold. This triggers an Apply holds job. For more information, see, [Work with custodians in eDiscovery (Premium)](ediscovery-managing-custodians). |
| Compare load sets | A user looks at the differences between different load sets in a review set. A load set is an instance of adding data to a review set. For example, if you add the results of two different searches to the same review set, each would represent a load set. |
| Converting redacted items to PDF | After a user annotates a document in a review set and redacts a portion of it, they can choose to convert the redacted document to a PDF file. This ensures that the redacted portion won't be visible if the document is exported for presentation. For more information, see [View documents in a review set](ediscovery-view-documents-in-review-set). |
| Create conversation PDFs | When a user adds the results of a search to a conversation review set, instant message conversations (also called threaded conversations) in services like Microsoft Teams are reconstructed in a PDF file. This job is also triggered when a user selects **Action** &gt; **Create conversation PDFs in a review set**. For more information, see [Review conversations in eDiscovery (Premium)](ediscovery-conversation-review-sets). |
| Prepare search estimates | After a user creates and runs or reruns a collection estimate, the search tool searches the index for items that match the search query and prepares an estimate that includes the number and total size of all items by the search, and the number of data sources searched. For more information, see [Collect data for a case](ediscovery-collections). |
| Import custodians | User imports multiple custodians at once by uploading a CSV file that contains the information necessary to add them to a case. For more information, see [Import custodians to an eDiscovery (Premium) case](ediscovery-bulk-add-custodians). |
| Preparing for export | A user exports documents from a review set. When the export process is complete, they can download the exported data to a local computer. For more information, see [Export case data](ediscovery-exporting-data). |
| Prepare remediation | When a user selects a file and creates a new error remediation in the Error view on the Processing tab of a case, the first step in the process is to upload the file that has the processing error to an Azure Storage location in the Microsoft cloud. This job tracks the progress of the upload process. For more information about the error remediation workflow, see [Error remediation when processing data](ediscovery-error-remediation-when-processing-data). |
| Prepare search preview | After a user creates and runs a new collection estimate (or reruns an existing collection estimate), the search tool prepares a sample subset of items (that match the search query) that can be previewed. Previewing search results help you determine the effectiveness of the search. For more information, see [Learn about collections in eDiscovery](ediscovery-collections). |
| Purge data | Use eDiscovery (Premium) and the Microsoft Graph Explorer to search for and delete chat messages in Microsoft Teams. This feature can help you find and remove sensitive information or inappropriate content. This search and purge workflow will also help you respond to a data spillage incident, when content containing confidential or malicious information is released through Teams chat messages. |
| Reindex data sources | When you add custodial or non-custodial data sources to a case, all partially indexed items in the selected data source locations are reindexed by a process called *Advanced indexing*. This job is also triggered when you select **Update index** on the **Processing** tab of a case, and when you update the index for a specific data source on the properties flyout page. For more information, see [Advanced indexing of custodian data](ediscovery-indexing-custodian-data). |
| Relevance load | This job is triggered when user starts a "new model" - Review set &gt; Manage predictive coding models (preview). It sets up the machine learning model. After you create a model, the following things occur in the background during the creation and preparation of the model:  - The system calculates the number of items for the control set. This size is based on the number of items in the review set and the settings for the confidence level and the margin of error. Items for the control set are randomly selected and designated as control set items. The system includes 10 items from the control set in the first round of training.  - The system randomly selects 40 items from the review set to be included in the training set for the first round of training. Therefore, the first round of training includes 50 items for labeling: 40 items from the training set and 10 items from the control set. |
| Run analytics | A user analyzes data in a review set by running eDiscovery (Premium) analytics tools such as near duplicate detection, email threading analysis, and themes analysis. For more information, see [Analyze data in a review set](ediscovery-analyzing-data-in-review-set). |
| Tag items | This job is triggered when a user selects **Start tagging job** in the **Tagging panel** when reviewing documents in a review set. A user can start this job after tagging documents in a review set and then bulk-selecting them in the view document panel. For more information, see [Tag documents in a review set](ediscovery-tagging-documents). |

## Job status

The following table describes the different status states for jobs:

| **Status** | **Description** |
| --- | --- |
| Submitted | A new job was created. The date and time that the job was submitted is displayed in the **Created** column on the **Jobs** tab. |
| Submission failed | The job submission failed. You should attempt to rerun the action that triggered the job. |
| In progress | The job is in progress, you can monitor the progress of the job in the **Jobs** tab. |
| Successful/Completed | The job was successfully completed. The date and time that the job completed is displayed in the **Completed** column on the **Jobs** tab. |
| Partially successful | The job was successful. This status is typically returned when the job didn't find any partially indexed data (also called *unindexed data*) in some of the custodian data sources. |
| Failed/Completed with errors | The job failed. You should attempt to rerun the action that triggered the job. If the job fails a second time, we recommend that you contact Microsoft Support and provide the support information from the job. |