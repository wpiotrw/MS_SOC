---
layout: Conceptual
title: Search for and delete chat messages in Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-and-delete-teams-chat-messages
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery (Premium) and the Microsoft Graph Explorer to search for and delete chat messages in Microsoft Teams, and respond to data spillage incidents in Teams.
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
locale: en-us
document_id: ed18701a-c250-7915-fb29-2aadbbeb9976
document_version_independent_id: ed18701a-c250-7915-fb29-2aadbbeb9976
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-and-delete-teams-chat-messages.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-and-delete-teams-chat-messages
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-and-delete-teams-chat-messages.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 56f058aa-52d5-a40e-ad14-19d67aa5901f
---

# Search for and delete chat messages in Teams | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use eDiscovery (Premium) and the Microsoft Graph Explorer to search for and delete chat messages in Microsoft Teams. This feature can help you find and remove sensitive information or inappropriate content. This search and delete workflow will also help you respond to a data spillage incident, when content containing confidential or malicious information is released through Teams chat messages.

Tip

You can also use the purge feature in Data Security Investigations to search for and permanently delete Microsoft Teams items in your organization. Data Security Investigations provides a built-in search and purge workflow with a purge queue dashboard to help you manage and track purge queries. For more information, see [Purge in Data Security Investigations](data-security-investigations-mitigation-actions#purge).

## Before you search and delete chat messages

- To create an eDiscovery (Premium) case and use collections to search for chat messages, you have to be a member of the *eDiscovery Manager* role group in the Microsoft Purview portal. To delete chat messages, you have to be assigned the *Search And Purge* role. This role is assigned to the *Data Investigator* and *Organization Management* role groups by default. For more information, see [Assign eDiscovery permissions](ediscovery-assign-permissions).
- Search and purge are supported for most conversations within your tenant. Search and purge for Teams Connect Chat (External Access or Federation) conversations isn't supported.

    Important

    Chats with yourself (or chats by users with themselves) aren't supported for search and delete.
- A maximum of 100 items per mailbox can be removed at one time. Because the capability to search for and remove chat messages is intended to be an incident-response tool, this limit helps ensure that chat messages are quickly removed.
- Deleting chat messages in federated environments isn't supported.

## Search and delete workflow

Here's the process to search for and delete Teams chat messages:

![Workflow to search for and delete Teams chat messages.](media/teamssearchandpurgeworkflow.png)

## Step 1: Create a case in eDiscovery (Premium)

The first step is to create a case in eDiscovery (Premium) to manage the search and delete process. For information about creating a case, see [Use the new case format](ediscovery-new-case-format).

## Step 2: Create a collection estimate

After you create a case, the next step is to create a collection estimate to search for the Teams chat messages that you want to delete. The delete process you perform is Step 5 deletes all items that are found in the collection estimate (within the 10 item per location limit).

In eDiscovery (Premium), a *collection* is an eDiscovery search of the Teams content locations that contain the chat messages that you want to delete. Create the collection estimate in the case that you created in the previous step. For more information, see [Create a collection estimate](ediscovery-create-draft-collection).

### Data sources for chat messages

Use the following table to determine which data sources to search depending on the type of chat message you need to delete.

| **For this type of chat...** | **Search this data source...** |
| --- | --- |
| Teams 1:1 chats | The mailbox of chat participants. |
| Teams group chats | The mailboxes of chat participants. |
| Teams channels (standard and shared) | The mailbox associated with the parent team. |
| Teams private channels | The mailbox of the private channel members. |

Note

In Step 4, you also have to identify and remove any holds and retention policies assigned to the mailbox that contains the type of chat messages that you want to delete.

### Tips for searching for chat messages

To help ensure the most comprehensive collection of Teams chat conversations (including 1:1 and group chats, and chats from standard, shared, and private chats) use the **Type** condition and select the **Instant messages** option when you build the search query for the collection estimate. We also recommend including a date range or several keywords to narrow the scope of the collection to items relevant to your search a delete investigation.

Here's an example of a sample query using the **Type** and **Date** options:

![Query to collect Teams content.](media/teamsconditionsquerytype.png)

For more information, see [Build search queries for collections](ediscovery-building-search-queries).

## Step 3: Review and verify chat messages to delete

The deletion process in Step 5 deletes the items returned by the collection. It's important that you review the collection estimate results to ensure that the collection only returns the items that you want to delete. To review a sample of items in a collection estimate, see the "Next steps after a collection estimate is complete" section in [Create a collection estimate](ediscovery-create-draft-collection#next-steps-after-a-collection-estimate-is-complete).

Additionally, you can use the collection statistics (specifically the Top Locations statistics) to generate a list of the data sources that contain items returned by the collection. Use this list in the next step to remove hold and retention policies from the data sources that contain search results. For more information, see [Collection statistics and reports](ediscovery-collection-statistics-reports).

## Step 4: Remove all holds and retention policies from data sources

Before you can delete chat messages from a mailbox, you have to remove all organization-wide holds, site holds, or retention policy holds that are assigned to a target mailbox. If not, the chat you're trying to delete is retained.

Use the list of mailboxes that contain the chat messages that you want to delete and determine if there's a hold or retention policy assigned to those mailboxes, and then remove the hold or retention policy. Be sure to identify the hold or retention policy that you remove so that you can reassign to the mailboxes in Step 7.

For instructions about how to identify and remove holds and retention policies, see "Step 3: Remove all holds from the mailbox" in [Delete items in the Recoverable Items folder of cloud-based mailboxes on hold](ediscovery-delete-items-in-the-recoverable-items-folder-of-mailboxes-on-hold#step-3-remove-all-holds-from-the-mailbox).

## Step 5: Delete chat messages from Teams

Note

Because Microsoft Graph Explorer is not available in some US Government clouds (GCC High and DOD), you must use PowerShell to accomplish these tasks. See the Delete chat messages with PowerShell for details.

Now you're ready to actually delete chat messages from Teams. Use the Microsoft Graph Explorer to perform the following three tasks:

1. Get the ID of the eDiscovery (Premium) case that you created in Step 1. This is the case that contains the collection created in Step 2.
2. Get the ID of the collection that you created in Step 2 and verified the search results in Step 3. The search query in this collection returns the chat messages that will be deleted.
3. Delete the chat messages returned by the collection.

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

    In the response, the search query from the collection is displayed in the *contentQuery* property. Items returned by this query is deleted in the next task.
3. Copy the corresponding ID (or copy and paste it to a text file). You'll use this ID in the next task to delete the chat messages.

Tip

Instead of using the previous procedure to obtain the search Id, you can open the case in the Microsoft Purview portal. Open the case and navigate to the Jobs tab. Select the relevant collection and under Support information, find the job ID (the job ID displayed here is the same as the collection ID).

### Delete the chat messages

1. In Graph Explorer, run the following POST request to delete the items returned by the collection that you created in Step 2. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches/{ediscoverySearchID}/purgeData` in the address bar of the request query, where *{ediscoveryCaseID}* and *{ediscoverySearchID}* are the IDs that you obtained in the previous procedures.

    If the POST request is successful, an HTTP response code is displayed in a green banner stating that the request was accepted.

For more information on purgeData, see [sourceCollection: purgeData](/en-us/graph/api/ediscovery-sourcecollection-purgedata).

### Delete chat messages with PowerShell

You can also delete chat messages using PowerShell. For example, to delete messages in the US Government cloud you could use a command similar to:

`Connect-MgGraph -Scopes "ediscovery.ReadWrite.All" -Environment USGov`

`Invoke-MgGraphRequest  -Method POST -Uri '/v1.0/security/cases/ediscoveryCases/<ediscoverySearchID>/searches/<search ID>/purgeData' `

For more information on using PowerShell to delete chat messages, see [ediscoverySearch: purgeData](/en-us/graph/api/security-ediscoverysearch-purgedata?view=graph-rest-1.0).

## Step 6: Verify chat messages are deleted

After you run the POST request to delete chat messages, these messages are removed from the Teams client and replaced with an automatically generated stating that an admin has removed the message. For an example of this message, see the End-user experience section in this article.

If you need to confirm a chat message has been removed and don't have access to the end-user message in Teams, re-run the search and verify if any matching messages are found. If there aren't any results for the message, the message has been removed.

Deleted chat messages are moved to the *SubstrateHolds* folder, which is a hidden mailbox folder. Deleted chat messages are stored there for at least 1 day, and then are permanently deleted the next time the timer job runs (typically between 1-7 days). For more information, see [Learn about retention for Microsoft Teams](retention-policies-teams).

Note

Because Microsoft Graph Explorer is not available in the US Government cloud (GCC, GCC High, and DOD), you must use PowerShell to accomplish these tasks.

## Step 7: Reapply holds and retention policies to data sources

After you verify that chat messages are deleted and removed from the Teams client, you can reapply the holds and retention policies that you removed in Step 4.

## End-user experience

For deleted chat messages, users see an automatically generated message stating "This message was deleted by an admin".

![View of deleted chat message in Teams client.](media/teamspurgetombstone.png)

The message in the previous screenshot replaces the chat message that was deleted.

Note

If you're an end-user and a chat message was deleted, contact your admin for more information.