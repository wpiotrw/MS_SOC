---
layout: Conceptual
title: Find and delete Microsoft Teams chat messages in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-teams-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery and the Microsoft Graph Explorer to search for and delete chat messages in Microsoft Teams.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 9b34568e-2dd5-4562-3d8f-ce2e02268774
document_version_independent_id: 9b34568e-2dd5-4562-3d8f-ce2e02268774
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-teams-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-teams-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-teams-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 3cf18f35-5274-25f8-b744-f4037b1e3468
---

# Find and delete Microsoft Teams chat messages in eDiscovery | Microsoft Learn

Tip

You can also use the purge feature in Data Security Investigations to search for and permanently delete Microsoft Teams items in your organization. Data Security Investigations provides a built-in search and purge workflow with a purge queue dashboard to help you manage and track purge queries. For more information, see [Purge in Data Security Investigations](data-security-investigations-mitigation-actions#purge).

You can use eDiscovery and the Microsoft Graph Explorer to search for and delete chat messages in Microsoft Teams. This feature helps you find and remove sensitive information or inappropriate content. This search and delete workflow helps you respond to a data spillage event, when content containing confidential or malicious information is released through Teams chat messages.

Microsoft Teams chat data is stored in separate copies, one for compliance purposes (used by tools like eDiscovery) and one for user access.

- **Soft delete or hard delete operations** remove the user copy permanently and can't be recovered for user use.
- **Cmdlet-based purges** of Teams messages can remove the compliance copy of Teams messages, but the user copy remains visible. After the compliance copy is deleted, eDiscovery can no longer remove the user-visible message. Verify Teams messages carefully before purging and avoid using cmdlets to purge Teams messages (the user copy isn't deleted).

    - If you use cmdlets, review the export report and exclude Teams items. Deletes are only performed on the compliance copy and don't remove copies from user viewing. Deleting only the compliance copy also prevents any future deletion when using Microsoft Graph APIs.
    - If you use Microsoft Graph to review the report and ensure Teams items being deleted are intentional, there's no recovery of the items after the deletion is complete.

To ensure complete removal of items, plan your purge strategy carefully and understand which copy each deletion method targets.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you search and delete chat messages

Important

Carefully review the following guidance before starting the search and purge steps for Teams chat messages.

- Depending on the eDiscovery subscription for your organization, cases can either be enabled for premium features or not. Verify the level of feature support for the case to determine if the search and purge should be conducted using PowerShell or Microsoft Graph. Cases not configured for premium features can only use [PowerShell to search and delete email messages](edisc-search-mailbox-data) and cases configured for premium features can use PowerShell or Microsoft Graph to search and delete email messages. Don't use a combination of PowerShell and Microsoft Graph to purge email messages and chats.
- After data is permanently deleted, it isn't recoverable. Follow the guidance in this article carefully and validate the scope of the search before issuing the purge command. After you run the purge command, you can't undo it and email messages and chats can't be restored.
- Run an export report to review all items that match your search criteria before the purge. Using the search and export experience in the Microsoft Purview portal and [exporting the results in report-only format](edisc-search-export) allows you to examine detailed metadata before deletion. This approach helps refine your search scope and ensures a more targeted and accurate purge.
- To create an eDiscovery case and search for chat messages, you need to be a member of the *eDiscovery Manager* role group in the Microsoft Purview portal. To delete chat messages, you need to be assigned the *Search And Purge* role. This role is assigned to the *Data Investigator* and *Organization Management* role groups by default. For more information, see [Assign eDiscovery permissions](edisc-permissions).
- Search and purge are supported for most conversations within your organization. Search and purge for Teams Connect Chat (External Access or Federation) conversations isn't supported.

    Important

    Chats with yourself (or chats by users with themselves) aren't supported for search and delete.
- You can remove up to 100 items per mailbox at one time. Because the capability to search for and remove chat messages is intended to be an event-response tool, this limit helps ensure that chat messages are quickly removed.

## Step 1: Create a case in eDiscovery

The first step is to [create a case](edisc-cases-manage) in eDiscovery to manage the search and delete process.

## Step 2: Create a search query

After you create a case, you need to [search for the Teams chat messages](edisc-search-teams) that you want to delete. The delete process deletes all items that are found in the search (within the 10 item per location limit).

### Data sources for chat messages

Use the following table to determine which data sources to search depending on the type of chat message you need to delete.

| For this type of chat... | Search this data source... |
| --- | --- |
| Teams 1:1 chats | The mailbox of chat participants. |
| Teams group chats | The mailboxes of chat participants. |
| Teams channels (standard and shared) | The mailbox associated with the parent team. |
| Teams private channels | A dedicated mailbox for each private channel. |

Note

Before deleting messages, you also need to identify and remove any holds and retention policies assigned to the mailbox that contains the type of chat messages you want to delete.

### Tips for searching for chat messages

To help ensure the most comprehensive identification of Teams chat conversations (including 1:1 and group chats, and chats from standard, shared, and private chats), use the **Type** condition and select the **Instant messages** option when you build the search query. Include a date range or several keywords to narrow the scope of the search to items relevant to your investigation.

## Step 3: Review and verify chat messages to delete

The deletion process deletes all items returned by the search. It's important that you review the search statistics to ensure that the search only returns the items that you want to delete. Additionally, you can use the search statistics (specifically the *Top Locations* statistics) to generate a list of the data sources that contain items returned by the search. Use this list when removing hold and retention policies from the data sources that contain search results.

## Step 4: Remove all holds and retention policies from data sources

Before you can delete chat messages from a mailbox, you need to remove all organization-wide holds, site holds, or retention policy holds that are assigned to a target mailbox. If you don't remove these holds, the chat messages you're trying to delete are retained.

Use the list of mailboxes that contain the chat messages you want to delete to determine if there's a hold or retention policy assigned to those mailboxes, and then remove the hold or retention policy. Be sure to identify the hold or retention policy that you remove so that you can reassign it to the mailboxes after deletion is complete.

For instructions about how to identify and remove holds and retention policies, see "Step 3: Remove all holds from the mailbox" in [Delete items in the Recoverable Items folder of cloud-based mailboxes on hold](edisc-hold-delete-recoverable-items#step-3-remove-all-holds-from-the-mailbox).

## Step 5: Delete chat messages from Teams

Note

Because Microsoft Graph Explorer isn't available in some US Government clouds (GCC High and DOD), you must use PowerShell to accomplish these tasks. See Delete chat messages with PowerShell for details.

Now you're ready to delete chat messages from Teams. Use the Microsoft Graph Explorer to perform the following tasks:

1. Get the ID of the eDiscovery case that you created in Step 1. This case contains the search results created in Step 2.
2. Get the ID of the search that you created in Step 2 and verified the search results in Step 3. The search query returns the chat messages that you want to delete.
3. Delete the chat messages returned by the search.

For information about using Graph Explorer, see [Use Graph Explorer to try Microsoft Graph APIs](/en-us/graph/graph-explorer/graph-explorer-overview).

Important

To perform these three tasks in Graph Explorer, you might have to consent to the eDiscovery.Read.All and eDiscovery.ReadWrite.All permissions. For more information, see the "Consent to permissions" section in [Working with Graph Explorer](/en-us/graph/graph-explorer/graph-explorer-features#consent-to-permissions).

### Get the case ID

Use Graph Explorer to retrieve the ID of the eDiscovery case you created earlier.

1. Go to https://developer.microsoft.com/graph/graph-explorer and sign in to the Graph Explorer with an account that's assigned the *Search And Purge* role in the Microsoft Purview portal.
2. Run the following GET request to retrieve the ID for the eDiscovery case. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases` in the address bar of the request query. Be sure to select **v1.0** in the API version dropdown list.

    This request returns information about all cases in your organization on the **Response preview** tab.
3. Scroll through the response to locate the eDiscovery case. Use the **displayName** property to identify the case.
4. Copy the corresponding ID (or copy and paste it to a text file). Use this ID in the next task to get the search ID.

Tip

Instead of using the previous procedure to obtain the case ID, you can open the case in the Microsoft Purview portal and copy the case ID from the URL.

### Get the eDiscoverySearchID

Next, retrieve the ID of the search that contains the chat messages you want to purge.

1. In Graph Explorer, run the following GET request to retrieve the ID for the search that you created in Step 2, and contains the items you want to delete. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches` in the address bar of the request query, where *{ediscoveryCaseID}* is the CaseID that you obtained in the previous procedure.
2. Scroll through the response to locate the search that contains the items you want to delete. Use the *displayName* property to identify the search that you created and verified earlier.

    In the response, the search query from the search is displayed in the *contentQuery* property. Items returned by this query are deleted in the next task.
3. Copy the corresponding ID (or copy and paste it to a text file). Use this ID in the next task to delete the chat messages.

### Delete the chat messages

After you confirm the correct case and search IDs, use the following request to purge the matching chat messages.

1. In Graph Explorer, run the following POST request to delete the items returned by the search that you created in Step 2. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches/{ediscoverySearchID}/purgeData` in the address bar of the request query, where *{ediscoveryCaseID}* and *{ediscoverySearchID}* are the IDs that you obtained in the previous procedures.

    If the POST request is successful, an HTTP response code is displayed in a green banner stating that the request was accepted.

For more information about purgeData, see [sourceCollection: purgeData](/en-us/graph/api/ediscovery-sourcecollection-purgedata).

### Delete chat messages with PowerShell

You can also delete chat messages by using PowerShell. For example, to delete messages in the US Government cloud, you can use a command similar to the following example:

```powershell
Connect-MgGraph -Scopes "ediscovery.ReadWrite.All" -Environment USGov
```

```powershell
Invoke-MgGraphRequest  -Method POST -Uri '/v1.0/security/cases/ediscoveryCases/<ediscoverySearchID>/searches/<search ID>/purgeData'
```

For more information about using PowerShell to delete chat messages, see [ediscoverySearch: purgeData](/en-us/graph/api/security-ediscoverysearch-purgedata).

## Step 6: Verify chat messages are deleted

When you run the POST request to delete chat messages, the Teams client removes these messages and replaces them with an automatically generated message stating that an admin removed the message. For an example of this message, see the User experience section in this article.

If you need to confirm a chat message is removed but don't have access to the user message in Teams, rerun the search and check if any matching messages appear. If there aren't any results for the message, the message is removed.

When you issue a purge:

- The **user copy** of the message is deleted immediately and can't be recovered by the user.
- The **compliance copy** (stored in the mailbox's *SubstrateHolds* folder) is retained for at least 24 hours before permanent deletion by a background timer job (typically within 1–7 days). If a hold is removed and then re-applied within that 24-hour window, the compliance copy might be preserved by the new hold.

For more information, see [Learn about retention for Microsoft Teams](retention-policies-teams).

Note

Because Microsoft Graph Explorer isn't available in the US Government cloud (GCC, GCC High, and DOD), you must use PowerShell to accomplish these tasks.

## Step 7: Reapply holds and retention policies to data sources

After you verify that chat messages are deleted and removed from the Teams client, reapply the holds and retention policies that you removed in Step 4.

## User experience after Teams chat messages are deleted

For deleted chat messages, users see an automatically generated message stating *This message was deleted by an admin*.

![Screenshot of a deleted chat message as shown in the Teams client.](media/teamspurgetombstone.png)

The message in the previous screenshot replaces the chat message that was deleted.

Note

If you're a user and a chat message was deleted, contact your admin for more information.