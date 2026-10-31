---
layout: Conceptual
title: Manage custodians in an eDiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-manage-new-custodians
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to view details, edit, and bulk edit the list of custodians in an eDiscovery (Premium) case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 420816ba-4080-b0f1-0dce-88f8521e294a
document_version_independent_id: 420816ba-4080-b0f1-0dce-88f8521e294a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-manage-new-custodians.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-manage-new-custodians
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-manage-new-custodians.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b0b935d8-bf65-a287-d956-5e743c5527ce
---

# Manage custodians in an eDiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The **Data sources** tab in a Microsoft Purview eDiscovery (Premium) case contains a list of all custodians that have been added to the case. After you add custodians to a case, details about each custodian are automatically collected from Microsoft Entra ID and are viewable in eDiscovery (Premium).

## View custodian details

The **Data Sources** list view can be filtered by *Source name*, *Source type* (custodian/data location), *Locations*, *Source status*, *Indexing status*, *Hold status*, and *Index date*. The list view can also be grouped by *Data source*, *Source type*, *Source status*, *Hold status*, and *Indexing status*.

To view the details about a custodian, select the custodian from the list on the **Data sources** tab. A flyout page is displayed with the following tabs and information:

- Summary tab
    - Employee information
    - Statuses
- Locations tab
- Import errors

Additionally, the command bar for the custodian flyout page enables the following actions for the custodian:

- **Edit source**: Opens the **Edit custodian** page where you can add or remove data sources associated with the custodian.
- **Update index**: Updates the index for the custodian's data sources. This action is useful when you want to reindex the custodian's data sources to address partially indexed items.
- **Release**: Releases the custodian from the case. This action releases any holds placed on the custodian's data sources through the default hold policies for custodian/non-custodian sources. Any holds placed on the custodian's data sources in other cases or through manual policies (Query base holds) still apply.
- **View activity**: Opens the **View activity** page where you can search for specific activity for the custodian in the [audit log](/en-us/purview/audit-new-search).
- **Retry hold action**: Retries the hold for the selected custodians and locations. If the hold option was selected while adding/editing the source, the hold is applied again. If the hold option was not selected while adding/editing the source, the hold is removed.

### Summary tab

The **Summary** tab shows the following sections and information about the custodian:

#### Employee information

- **Title**: The custodian's job title.
- **User principal name**: The user principal name (UPN) for the custodian. For example, user1@contoso.onmicrosoft.com.
- **Manager**: The custodian's manager. The designated manager receives any escalation communications for this custodian.
- **Mailbox**: The custodian's primary mailbox.
- **Location**. The office location in the custodian's place of business.
- **City**: The city in which the custodian works.
- **State**: The state in which the custodian works.
- **Country**: The country/region in which the custodian works.
- **Department**: The name for the department in which the custodian works.

Important

If the UPN of a custodian changes after the custodian is added to a case, the custodian information (Title, Manager, Location, etc.) isn't retained and is displayed in the custodian summary pane as *No data to show*.

#### Statuses

- **Hold status**: The hold status of the locations added to the custodian. The hold statuses include:

    - *On hold*: Indicates the custodian and associated locations is successfully placed on hold.
    - *Not on hold*: Indicates the custodian and associated data locations are either not placed on hold or successfully released from hold.
    - *Applying hold*: Indicates the application of hold to the custodian and associated data locations is in progress. Wait until the hold job completes and verify that the hold is placed successfully.
    - *Releasing hold*: Indicates that the release of hold from the custodian and associated data locations is in progress. Wait until the hold job completes and verify if the hold is released successfully.
    - *Partial hold*: Indicates errors for some locations associated with the custodian couldn't be placed on hold.
    - *Partial hold released*: Indicates some locations associated with the custodian weren't released from hold.
    - *Hold failed*: Indicates the hold couldn't be placed on the custodian and any of the associated locations.
    - *Release failed*: Indicates the hold couldn't be released from the custodian and any of the associated locations.

        If the hold couldn't be placed or released successfully, the total count of failed locations with associated error categories and their resolution are displayed in the **Summary** tab. Select **Show locations** to view the full list of failed locations or select **Export list** to download a list of the failed locations by error type. For more information about data source errors, see [Manage hold status and errors](ediscovery-managing-holds#manage-hold-status-errors).

        Note

        The improved hold error details and resolution are available only for newly added custodians. A generic error message is displayed for older custodial locations that had previously failed. Users can get the improved error messaging and resolution information for these custodians by selecting **Retry hold action**. This retries the hold and generates the improved error messaging and resolution if the error persists.
- **Indexing status**: Indicates the indexing state, including the last updated date and time (UTC).

### Locations tab

This tab shows the count and type of data sources (mailboxes, sites, and Teams) and the hold status for each location associated with the custodian and are part of the case.

- Each data location shows its hold status.
- If you don't see a hold status for a data source, check the status of the custodian hold that's listed on the **Hold** tab for the case. The custodian hold identifies the specific data sources place on hold.

### Import errors tab

This tab shows the count and list of locations associated with the custodian that errored during the import custodian process and allows user to remove invalid locations from the sources.

## Edit a custodian

As your case progresses, you may discover that there may be additional data sources relevant to a specific custodian and the case. In other scenarios, you may want to remove certain data sources that have been reviewed and deemed as not relevant.

To update the data sources that are associated with a custodian:

1. Go to **eDiscovery &gt; eDiscovery (Premium)** and open the case.
2. Select the **Data Sources** tab.
3. Select a custodian from the list, and then select **Edit source** on the flyout page command bar.
4. To add or remove the primary mailbox and OneDrive account for the custodian:

    - Expand the custodian to view the primary data locations that have been previously associated with the custodian.
    - Select **Edit** next to **Mailboxes** or **OneDrive** to add the custodian's mailbox or OneDrive location.
    - Select **Clear** next to **Mailboxes** or **OneDrive** to remove the custodian's mailbox or OneDrive account from being associated as a data location for this custodian.
5. To add or remove other mailboxes, sites, Teams, or Viva Engage groups to a specific custodian, select **Edit** next to the service to add a data location.

    - **Exchange**: Use to associate other mailboxes to the custodian. Type into the search box the name or alias (a minimum of three characters) of user mailboxes or distribution groups. Select the mailboxes to assign to the custodian and then select **Add**.
    - **SharePoint**: Use to associate SharePoint sites to the custodian. Select a site in the list or search for a site by typing a URL in the search box. Select the sites to assign to the custodian and then select **Add**.
    - **Teams**: Use to assign the Microsoft Teams the custodian is currently a member of. Select the teams to assign to the custodian and then select **Add**. After you add a team, the system automatically identifies and locates the SharePoint site and group mailbox associated to that team and assigns them to the custodian.
    - **Viva Engage**: Use to assign the Viva Engage groups the custodian is currently a member of. Select the groups to assign to the custodian and then select **Add**. After you add a team, the system automatically identifies and locates the SharePoint site and group mailbox associated to that group and assigns them to the custodian.

    Note

    You can use the **Exchange** and **SharePoint** location pickers to associate any mailbox or site in your organization, including teams or Viva Engage groups that a custodian is not a member of, to a custodian. To do this, you have to add both the mailbox and site associated with each team or Viva Engage group.
6. After editing the data locations for the custodian, select **Next** to go to the **Hold settings** page.
7. On the **Hold settings** page, update the hold settings for the custodian. Select **Next**.
8. On the **Review** page, review the changes and select **Submit** to save the changes.

## Reindex custodian data

In most eDiscovery workflows for legal investigations, a subset of a custodian's data is searched after the custodian is added to a legal case. Because of large file sizes or possible data corruption, some items in the data sources associated with a custodian may be partially indexed. Using the [Advanced indexing](ediscovery-indexing-custodian-data) capability in the eDiscovery (Premium), most partially indexed items can be automatically remediated by reindexing these items on demand.

When a custodian is added to a case, the data located in the data sources associated with the custodian is automatically reindexed (by the Advanced indexing process). This means you can leave the data in-place instead of having to download and remediate it and then search it offline. However, during the lifecycle of a legal case new data sources might be associated with a custodian. In this case, you can reindex the custodian's data by rerunning the Advanced indexing process to remediate any partially indexed items and update the index for the custodian's data.

To trigger the reindexing process to address partially indexed items:

1. Go to **eDiscovery &gt; eDiscovery (Premium)** and open the case.
2. Select the **Data sources** tab.
3. On the **Data sources** page, select a custodian whose data must be reindexed.
4. On the flyout page, select **Update index**.A dialog is displayed to confirm the index update, select **Yes** to continue.

Reindexing custodian data is a long-running process; the corresponding job that's created is named **Re-indexing custodian data**. You can track the progress on the **Jobs** tab or on the **Custodians** tab by monitoring the status in the **Indexing job status** column.

For more information, see:

- [Work with processing errors](ediscovery-processing-data-for-case)
- [Manage jobs](ediscovery-managing-jobs)

## Release a custodian from a case

A custodian is released in situations where a case is closed, the custodian is no longer under obligation to preserve content for a case, or when the custodian is deemed to no longer be relevant to the case.

If you release a custodian after a hold notice was published, a release notice will be sent to the custodian. Additionally, any holds placed on data sources that were associated with the custodian are removed. If the custodian was placed on a *silent hold*, where they weren't issued any legal hold notifications, a release notice won't be sent but any holds placed on data sources that were associated with that custodian are removed.

To release a custodian:

1. Go to **eDiscovery &gt; eDiscovery (Premium)** and open the case.
2. Select the **Data sources** tab.
3. On the **Data sources** page, and then select the custodian who is being released from the case.
4. On the flyout page, select **Release**.

    A warning page is displayed explaining that if a hold is placed on a data source associated with the custodian, the hold is removed, and that any other hold associated with a different eDiscovery (Premium) case still apply. That includes other types of preservation and retention features (such as a Microsoft 365 retention policy).
5. Select **Yes** to confirm that you want to release the custodian.

    The status for this user on the **Custodians** tab is set to **Released** and the **Hold status** on the flyout page is changed to **False**.

Note

A custodian may be simultaneously involved in several legal cases. When a custodian is released from a specific case, the holds and notifications across other cases won't be impacted.