---
layout: Conceptual
title: Take mitigation actions in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-mitigation-actions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to resolve data security incidents effectively using the Mitigation Plan in Data Security Investigations. Track, prioritize, and act on risks.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
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
document_id: 124e5380-8fda-e251-79a1-8fed7a2cfd3a
document_version_independent_id: 124e5380-8fda-e251-79a1-8fed7a2cfd3a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-mitigation-actions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-mitigation-actions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-mitigation-actions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 2eed2d90-93e6-2af7-a321-bc6a93f6df19
---

# Take mitigation actions in Data Security Investigations | Microsoft Learn

Data Security Investigations provides several features to help you quickly mitigate the impact of data security incidents in your organization.

## Mitigation plan

The mitigation plan helps you connect analysis to specific mitigation actions from examination tools and analyst reviews. Use the mitigation plan like a to-do list to manage and track data risk mitigation actions in your investigation. This plan helps analysts centralize all items that require attention or action to mitigate risks associated with the investigation and data security incident.

Using the mitigation plan, take the following actions:

- **Prioritize by risk level**: Immediately address anything that might lead to an active security breach if you don't fix it.
- **Mark items for follow-up**: Use the mitigation plan to track follow-up activities.
- **Consult or involve relevant stakeholders**: Make sure your plan addresses responsibilities for the following areas:

    - **Credentials**: Identify who resets credentials and by when.
    - **Data exposure**: Identify who removes external sharing links or moves files to a secure location.
    - **User education or enforcement**: Identify who follows up with training or disciplinary measures.
    - **Further investigation**: Identify who is responsible for any item that suggests a larger security issue in your organization.

### Mitigation plan dashboard

The **Mitigation plan** displays all items you add to the mitigation plan in your investigation. By using this view, you can quickly see all the items that need action in your investigation, the status for each item, and other important information about each item in the plan.

- **Name**: The subject or title of the data item.
- **Type**: The file type of the data item.
- **Description**: The description of the data item.
- **Status**: The current status of the data item. Values include *In-progress* or *Complete*.
- **Last modified by**: The name of the analyst or investigator that last updated information about the data item.
- **Last updated (UTC)**: The date and time in Coordinated Universal Time (UTC) that the data item was last updated.

Select **Customize columns** to customize the displayed columns and the order of the columns in the mitigation plan. Choose the columns to display or hide. Select **Add filter** and choose an available filter to filter items in the mitigation plan.

Select **Download list** to create a .csv file containing the list of data items and the column information in the mitigation plan.

### Item detailed view

Analysts can view details about each data item included in the mitigation plan as part of the review and evaluation process. After you select a data item, you see an item summary and [viewers](data-security-investigations-scope-views) to view metadata, source, and other information.

### Update item status

As you review data items and work to mitigate risks for each data item, manage the current status for each item. Update the status for individual items or bulk update the status for multiple data items.

To update the status for a data item, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select the **Data Security Investigations** solution card, then select **Investigations** in the left navigation.
3. Select an investigation, then select **Mitigation**.
4. Select one or more data items in the mitigation plan.
5. Select **Update status**, then select the applicable status.

You can also change the status of a data item from the item detail view. From the detailed view for an item, select **Complete** to change the status of the data item.

### Implement the mitigation plan

To implement your mitigation plan, work through the following mitigation steps:

- **Revoke or change credentials immediately**: For each exposed password or secret, ensure the responsible owner resets it. This action might involve forcing password resets for user accounts, deleting or regenerating access keys, or changing service account credentials.
- **Contain data exposure**: If files were accessible publicly or to too many people, lock down permissions immediately. Remove external guest access on SharePoint sites if a sensitive file was shared. If an email with secrets was sent externally, reach out to the recipient to delete it (if appropriate) or use message recall if possible.
- **Remediate documents**: For files that shouldn't contain certain information, decide whether to delete them, redact them, or secure them. Often, removing the sensitive content from the source is advised (or encrypting it). Consider applying [sensitivity labels](sensitivity-labels) or [Data Loss Prevention policies](dlp-learn-about-dlp) to prevent files from being shared again.
- **Track activities and insights**: Use the activity timeline for items. This information might identify related user activities. Check if any risky user behavior is ongoing and if further investigation of that user might be warranted.
- **Document every action**: In the [activity history](data-security-investigations-activity-history), every search, analysis, and mitigation action is logged. This information is useful for audit and post-incident review. Ensure the log shows that all risky items are addressed.
- **Communicate and resolve the incident**: Update all stakeholders on the following information:

    - Confirm that critical holes (credentials, public links, and other vulnerabilities) are closed.
    - If necessary, prepare any external notifications. For example, informing customers of a data breach and informing applicable regulators.
    - Conduct a debrief with all stakeholders. The insights and lessons learned can be used to improve policies and prevent future incidents.

## Purge

Data Security Investigations includes purge features to help you identify and remove Exchange mailbox and Microsoft Teams items in your organization. This need might include identifying items associated with highly confidential or sensitive information about financial, marketing, or sales projects, or other proprietary property. By using the built-in search capability for investigations, you can quickly create a new search query and save it as a purge query that you can review and run whenever needed. The *Data Security Investigation Admin* or *Data Security Investigation Investigator* role groups are required to purge content from Data Security Investigations.

Tip

Use soft purge as the default purge method for most investigation-driven workflows. Soft purge lets you quickly remove sensitive content from a user's view while preserving the ability to restore items if needed. Reserve hard purge for scenarios where you have high confidence that permanent deletion is required and items are correctly identified.

Data Security Investigations supports the following purge options:

- **Soft purge**: Items are moved to the recoverable items folder and retained based on your retention settings. Soft purge is only supported for Exchange mailbox items. Teams messages and OneDrive and SharePoint files aren't supported for soft purge.
- **Hard purge**: Items are permanently deleted from their data sources. This action can't be undone and search queries can't be edited after the purge is complete.

Warning

Hard purge permanently deletes items with no recovery path. Only use hard purge when you have high confidence that the items are correctly identified and permanent deletion is explicitly required.

Soft purge is useful for scenarios such as user terminations or active data-leak containment, where you need to quickly remove sensitive content from a user's view while preserving the ability to restore items if the investigation scope changes or the content is needed for further evidence review.

Both soft purge and hard purge respect [litigation holds](edisc-hold-types-mailboxes), [eDiscovery holds](edisc-hold-create), and [retention policies](retention). If items are subject to a hold or retention policy, purged items are preserved in the recoverable items folder and can't be permanently deleted until the hold is removed or the retention period expires. For more information, see [The principles of retention, or what takes precedence?](retention#the-principles-of-retention-or-what-takes-precedence).

Important

Purging removes items from their original source locations but doesn't remove items from the investigation scope in Data Security Investigations. To remove all items from Data Security Investigations, [delete the investigation](data-security-investigations-settings-investigation).

You pay for the processing needed to purge the volume of data resulting from your search query and uses the new Data Security Investigations compute unit. For more information about the compute unit, see [Billing in Data Security Investigations](data-security-investigations-billing).

### Purge queue dashboard

The **Purge queue** displays all the saved purge queries in your investigation. By using this view, you can quickly see all the purge queries in your investigation, the status for each query, and other important information about each query in the queue.

- **Name**: The name of the purge query.
- **Status**: The current status of the purge query. Values include *Not started*, *In-progress*, *Failed*, or *Complete*.
- **Added by**: The name of the investigator that added the purge query.
- **Added date (UTC)**: The date and time in Coordinated Universal Time (UTC) that the purge query was added to the purge queue.

Select **Customize columns** to customize the displayed columns and the order of the columns in the purge queue. Choose the columns to display or hide. Select **Add filter** and choose an available filter to filter items in the purge queue.

Select **Download list** to create a .csv file containing the list of data items and the column information in the purge queue.

### Choose a purge method

Use the following table to determine the best purge method for your scenario:

| Consideration | Soft purge | Hard purge |
| --- | --- | --- |
| **Action** | Moves items to the recoverable items folder | Permanently deletes items from data sources |
| **Recoverable** | Yes, based on retention settings. | No, action can't be undone. |
| **Supported data sources** | Exchange mailbox items only. | Exchange mailbox items and Teams messages. |
| **Risk level** | Lower risk - items can be restored if needed. | High risk - irreversible, no recovery path. |
| **Recommended use** | Default for most investigation-driven purges, bulk or search-based purges, and scenarios where query scope might be broad. | Only when you have high confidence that items are correctly identified and permanent deletion is required. |
| **Example scenarios** | User terminations, active data-leak containment, removing sensitive content while preserving evidence. | Confirmed malicious content, prohibited material with no compliance retention requirement. |

### Purge items with a search query

To purge specific items in your organization, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation or select **Create investigation** to create a new investigation.
4. On the **Search** tab, select the data sources that contain the items you want to purge.

    Important

    Only items in Exchange mailboxes and Microsoft Teams currently support purge. Selecting SharePoint sites or OneDrive accounts disables purge actions. Soft purge is only supported for Exchange mailbox items. If the search query includes Teams messages or OneDrive and SharePoint files, the soft purge option isn't available.
5. Create a search to identify the items you want to purge, and then select **Review for purge**.

    Important

    *FileID* isn't available for purged items not added to a review set or when exported. Use *ImmutableID* if needed.
6. On the **Review for purge** page, verify that the items returned in the estimates align with the items you want to purge. You can purge up to [10,000 items per search](data-security-investigations-ref-limits#purge-limits).

    If you need to edit the search, select **Search** and update the conditions of the search. To view details for search matches, select the ellipsis and **View samples** or select **Add to scope**.

    Important

    If you add items to an investigation scope, a copy of the items is added to the Azure storage account associated with Data Security Investigations in your organization. Running the purge query in the **Purge queue** removes items from all their current source locations, but not from the investigation scope in Data Security Investigations. To remove all items from Data Security Investigations, delete the investigation.
7. Select **Save for purge** and enter a unique name for the purge query in the **Query name** field.
8. Select **Save** to save the query and add the query to the purge queue. This step only saves the query as a purge query and doesn't purge any items.

    Warning

    The item count displayed during review for purge is an *estimate* based on the search results at the time of review. If you don't run the purge query immediately, the items matching the query can change significantly over time. Running a saved purge query at a later date could result in purging substantially more items than originally estimated, including items you didn't intend to delete. To avoid unintended data loss, always review for purge again immediately before running the purge query.
9. On the **Mitigation** tab for the investigation, you're automatically directed to the **Purge queue** dashboard.
10. Select the purge query you want to run.
11. On the purge query details page, review the query details and select **Run**.
12. On the purge confirmation dialog, select the purge method for the query:

    - **Soft purge**: Moves items to the recoverable items folder and retains them based on your retention settings. This option isn't supported for Teams messages and OneDrive and SharePoint files. If the search query includes unsupported items, the soft purge option isn't available.
    - **Hard purge**: Permanently deletes items from their data sources. This action can't be undone.

    Note

    If items are under a [litigation hold](edisc-hold-types-mailboxes), [eDiscovery hold](edisc-hold-create), or [retention policy](retention), the purge process preserves the items and can't permanently delete them until the hold is removed or the retention period expires.
13. Select **Confirm purge**.
14. To view the status of the purge query, select the **Activities** tab.

After the purge is complete, you can download a report as a .zip file that includes item, location, settings, and summary information about the purged items.

### Purge a single item

To purge a single item from an investigation, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis** to access the investigation scope.
4. Select the item you want to purge from the investigation scope.
5. Select **Add to mitigation**, and then select **Mitigation** to see the Mitigation list.
6. Select the item from the Mitigation list.
7. Select **Add to purge queue**, then select **Purge queue** to view the Purge queue.
8. Select the item from the Purge queue, then select **Purge**.
9. Select the purge method for the item:

    - **Soft purge**: Moves the item to the recoverable items folder and retains it based on your retention settings. This option is only available for Exchange mailbox items.
    - **Hard purge**: Permanently deletes the item from its data source. This action can't be undone.

    Note

    If items are under a [litigation hold](edisc-hold-types-mailboxes), [eDiscovery hold](edisc-hold-create), or [retention policy](retention), the purge process preserves the items and can't permanently delete them until the hold is removed or the retention period expires.
10. Select **Confirm purge**.
11. To view the status of the purge, select the **Activities** tab.