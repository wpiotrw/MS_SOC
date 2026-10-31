---
layout: Conceptual
title: Search for and delete Copilot data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-and-delete-copilot-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery (Premium) and the Microsoft Graph Explorer to search for and delete Microsoft 365 Copilot and Microsoft 365 Copilot Chat data.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
ms.update-cycle: 180-days
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
- m365copilot
- msec-ai-copilot
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: cbab3dfc-c4d5-39cf-4fe7-f21adb2079f8
document_version_independent_id: cbab3dfc-c4d5-39cf-4fe7-f21adb2079f8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-and-delete-copilot-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-and-delete-copilot-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-and-delete-copilot-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: c26c4fa1-2b89-66a2-9e38-5730f4929f10
---

# Search for and delete Copilot data | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use eDiscovery (Premium) and the Microsoft Graph Explorer to search for and delete user prompts and Microsoft 365 Copilot and Microsoft 365 Copilot Chat responses in supported applications and services. This feature can help you find and remove sensitive information or inappropriate content included in Copilot activities. This search and deletion workflow can also help you respond to a data spillage incident, when content containing confidential or malicious information is released through Copilot-related activity.

## Before you search and delete Copilot data

- To create an eDiscovery (Premium) case and use collections to search for Copilot activity data, you have to be a member of the *eDiscovery Manager* role group in the Microsoft Purview portal. To delete Copilot data, you have to be assigned the *Search And Purge* role. This role is assigned to the *Data Investigator* and *Organization Management* role groups by default. For more information, see [Assign eDiscovery permissions](ediscovery-assign-permissions).
- A maximum of 100 items per mailbox can be removed at one time. Because the capability to search for and remove Copilot data is intended to be an incident-response tool, this limit helps ensure that this data is quickly removed.

## Step 1: Create a case in eDiscovery (Premium)

The first step is to create a case in eDiscovery (Premium) to manage the search and deletion process. For information about creating a case, see [Use the new case format](ediscovery-new-case-format).

## Step 2: Create a collection estimate

After you create a case, the next step is to create a collection estimate to search for the Copilot data that you want to delete. The deletion process you perform is Step 5 deletes all Copilot-related items that are found in the collection estimate (within the 10 item per location limit).

In eDiscovery (Premium), a *collection* is an eDiscovery search of the content locations that contain Copilot data that you want to delete. Create the collection estimate in the case that you created in the previous step. For more information, see [Create a collection estimate](ediscovery-create-draft-collection).

### Data sources for Copilot data

The following table lists the applications and services that are sources for Copilot data. All user prompts to Copilot and responses from Copilot are stored in a user's mailbox.

| For this type of Microsoft Copilot data... | Search this item class... |
| --- | --- |
| Excel | IPM.SkypeTeams.Message.Copilot.Excel |
| Facilitator AI notes | IPM.SkypeTeams.Message.TeamCopilot.AiNotes.Teams |
| Loop | IPM.SkypeTeams.Message.Copilot.Loop |
| Microsoft 365 App | IPM.SkypeTeams.Message.Copilot.M365App |
| Microsoft Copilot for Bing (Microsoft 365 Copilot Chat) | IPM.SkypeTeams.Message.Copilot.BizChat |
| Microsoft Forms | IPM.SkypeTeams.Message.Copilot.Forms |
| OneNote | IPM.SkypeTeams.Message.Copilot.OneNote |
| Outlook | IPM.SkypeTeams.Message.Copilot.Outlook |
| PowerPoint | IPM.SkypeTeams.Message.Copilot.Powerpoint |
| SharePoint | IPM.SkypeTeams.Message.Copilot.SharePoint |
| Teams Channel | IPM.SkypeTeams.Message.Copilot.Teams |
| Teams Chat | IPM.SkypeTeams.Message.Copilot.Teams |
| Teams Copilot Chat (Microsoft 365 Copilot Chat) | IPM.SkypeTeams.Message.Copilot.BizChat |
| Teams Meeting | IPM.SkypeTeams.Message.Copilot.Teams |
| Teams Microsoft 365 Chat (BF) | IPM.SkypeTeams.Message |
| WebChat | IPM.SkypeTeams.Message.Copilot.WebChat |
| Whiteboard | IPM.SkypeTeams.Message.Copilot.Whiteboard |
| Word | IPM.SkypeTeams.Message.Copilot.Word |

Note

In Step 4, you also have to identify and remove any holds and retention policies assigned to the mailbox that contains the type of Copilot data that you want to delete.

### Tips for searching for Copilot data

To help ensure the most comprehensive collection of Copilot data, use the **Type** condition and select the **Copilot activity** option when you build the search query for the collection estimate. We also recommend including a date range or several keywords to narrow the scope of the collection to items relevant to your search and delete investigation.

For more information, see [Build search queries for collections](ediscovery-building-search-queries).

### Identifying web queries in Microsoft 365 Copilot usage

With the web search enabled for Microsoft 365 Copilot or Microsoft Copilot to include the latest data from the web, the web search queries sent to Microsoft Bing are searchable in eDiscovery. For more information about web search, see [Data, privacy, and security for web search in Microsoft 365 Copilot and Microsoft 365 Copilot Chat](/en-us/copilot/microsoft-365/manage-public-web-access).

Complete the following steps for finding these web queries:

1. Using the Condition builder in eDiscovery, search for Copilot activity using the filter *Type*, *Equals any of*, and *Copilot activity*.
2. In the query results, download any single item.
3. Open up the downloaded item in a text editor.
4. Look for *WebSearchQuery*
5. If the Copilot activity is involved in a Bing search query, *WebSearchQuery* is present in the downloaded file. It's followed by the specific query sent in the Microsoft Bing search query.

## Step 3: Review and verify Copilot data to delete

The deletion process in Step 5 will delete the items returned by the collection. It's important that you review the collection estimate results to ensure that the collection only returns the items that you want to delete. To review a sample of items in a collection estimate, see the **Next steps after a collection estimate is complete** section in [Create a collection estimate](ediscovery-create-draft-collection#next-steps-after-a-collection-estimate-is-complete).

Additionally, you can use the collection statistics (specifically the *Top Locations* statistics) to generate a list of the data sources that contain items returned by the collection. Use this list in the next step to remove hold and retention policies from the user mailboxes that contain search results. For more information, see [Collection statistics and reports](ediscovery-collection-statistics-reports).

## Step 4: Remove holds and retention policies from data sources

Before you can delete Copilot data from a mailbox, you have to remove any hold or retention policy that is assigned to a target mailbox. If not, then the data you're trying to delete is retained.

Use the list of mailboxes that contain the Copilot data that you want to delete and determine if there's a hold or retention policy assigned to those mailboxes, and then remove the hold or retention policy. Be sure to identify the hold or retention policy that you remove so that you can reassign to the mailboxes in Step 7.

For instructions about how to identify and remove holds and retention policies, see **Step 3: Remove all holds from the mailbox** in [Delete items in the Recoverable Items folder of cloud-based mailboxes on hold](ediscovery-delete-items-in-the-recoverable-items-folder-of-mailboxes-on-hold#step-3-remove-all-holds-from-the-mailbox).

## Step 5: Delete Copilot data

Note

Because Microsoft Graph Explorer is not available in some US Government clouds (GCC High and DOD), you must use PowerShell to accomplish these tasks. See the Delete Copilot data with PowerShell for details.

Now you're ready to delete Copilot data from user mailboexes. Use the Microsoft Graph Explorer to perform the following three tasks:

1. Get the ID of the eDiscovery (Premium) case that you created in Step 1. This is the case that contains the collection created in Step 2.
2. Get the ID of the collection that you created in Step 2 and verified the search results in Step 3. The search query in this collection returns the Copilot data to be deleted.
3. Delete the Copilot data returned by the collection.

For information about using Graph Explorer, see [Use Graph Explorer to try Microsoft Graph APIs](/en-us/graph/graph-explorer/graph-explorer-overview).

Important

To perform these three tasks in Graph Explorer, you may have to consent to the eDiscovery.Read.All and eDiscovery.ReadWrite.All permissions. For more information, see the "Consent to permissions" section in [Working with Graph Explorer](/en-us/graph/graph-explorer/graph-explorer-features#consent-to-permissions).

### Get the case ID

1. Go to https://developer.microsoft.com/graph/graph-explorer and sign in to the Graph Explorer with an account that's assigned the *Search And Purge* role in the Microsoft Purview portal.
2. Run the following GET request to retrieve the ID for the eDiscovery (Premium) case. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases` in the address bar of the request query. Be sure to select **v1.0** in the API version dropdown list.

    This request returns information about all cases in your organization on the **Response preview** tab.
3. Scroll through the response to locate the eDiscovery (Premium) case. Use the **displayName** property to identify the case.
4. Copy the corresponding ID (or copy and paste it to a text file). You'll use this ID in the next task to get the collection ID.

Tip

Instead of using the previous procedure to obtain the case Id, you can open the case in the Microsoft Purview portal and copy the case Id from the URL.

### Get the eDiscoverySearchID

1. In Graph Explorer, run the following GET request to retrieve the ID for the collection that you created in Step 2, and contains the items you want to delete. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches` in the address bar of the request query, where *{ediscoveryCaseID}* is the CaseID that you obtained in the previous procedure.
2. Scroll through the response to locate the collection that contains the items that you want to delete. Use the *displayName* property to identify the collection that you created in Step 3.

    In the response, the search query from the collection is displayed in the *contentQuery* property. Items returned by this query are deleted in the next task.
3. Copy the corresponding ID (or copy and paste it to a text file). You'll use this ID in the next task to delete Copilot data.

Tip

Instead of using the previous procedure to obtain the search Id, you can open the case in the Microsoft Purview portal. Open the case and navigate to the Jobs tab. Select the relevant collection and under Support information, find the job ID (the job ID displayed here is the same as the collection ID).

### Delete Copilot data

1. In Graph Explorer, run the following POST request to delete the items returned by the collection that you created in Step 2. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches/{ediscoverySearchID}/purgeData` in the address bar of the request query, where *{ediscoveryCaseID}* and *{ediscoverySearchID}* are the IDs that you obtained in the previous procedures.

    If the POST request is successful, an HTTP response code is displayed in a green banner stating that the request was accepted.

For more information on purgeData, see [sourceCollection: purgeData](/en-us/graph/api/ediscovery-sourcecollection-purgedata).

### Delete Copilot data with PowerShell

Note

Because Microsoft Graph Explorer is not available in the US Government cloud (GCC, GCC High, and DOD), you must use PowerShell to accomplish these tasks.

You can also delete Copilot data using PowerShell. For example, to delete Copilot data in the US Government cloud you could use a command similar to:

`Connect-MgGraph -Scopes "ediscovery.ReadWrite.All" -Environment USGov`

`Invoke-MgGraphRequest  -Method POST -Uri '/v1.0/security/cases/ediscoveryCases/<ediscoverySearchID>/searches/<search ID>/purgeData' `

For more information on using PowerShell to delete Copilot data, see [ediscoverySearch: purgeData](/en-us/graph/api/security-ediscoverysearch-purgedata?view=graph-rest-1.0).

## Step 6: Verify Copilot data is deleted

After you run the POST request to delete Copilot data, this data is removed from the user's mailbox. There isn't any visible notification or confirmation for the user that the data has been deleted.

Deleted Copilot data is moved to the *SubstrateHolds* folder, which is a hidden mailbox folder. Deleted Copilot data is stored there for at least 1 day and then are permanently deleted the next time the timer job runs (typically between 1-7 days).

## Step 7: Reapply holds and retention policies to user mailboxes

After you verify that the Copilot data is deleted, you can reapply the holds and retention policies to user mailboxes that you removed in Step 4.