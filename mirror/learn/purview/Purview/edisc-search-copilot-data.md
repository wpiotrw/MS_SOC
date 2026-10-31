---
layout: Conceptual
title: Search for and delete AI application data in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery and the Microsoft Graph Explorer to search for and delete Microsoft Copilot and other AI application activities in user mailboxes.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.update-cycle: 180-days
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
- msec-ai-copilot
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 6bf19e5e-881d-fdfc-0915-b14f978ea062
document_version_independent_id: 6bf19e5e-881d-fdfc-0915-b14f978ea062
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-copilot-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-copilot-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-copilot-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1cad7102-aec6-927b-1f1e-8a98d3e3f555
---

# Search for and delete AI application data in eDiscovery | Microsoft Learn

You can use eDiscovery and the Microsoft Graph Explorer to search for and delete user prompts and Microsoft Copilot and other AI solutions in supported applications and services. This feature can help you find and remove sensitive information or inappropriate content included in Copilot and other AI application activities. The eDiscovery search-and-deletion workflow described in this article can also help you respond to a data spillage event, when content containing confidential or malicious information is released through AI-related activity.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you search and delete AI data

- To create an eDiscovery case and search for AI activity data, you need to be a member of the *eDiscovery Manager* role group. To delete AI activity data, you need to be assigned the *Search And Purge* role. The *Data Investigator* and *Organization Management* role groups have this role by default. For more information, see [Assign eDiscovery permissions](edisc-permissions).
- You can remove up to 10 items per mailbox at one time. Because the search-and-removal capability is intended to be an event-response tool, the 10-item-per-mailbox limit helps ensure that AI activity data is removed quickly.

## Step 1: Create a case in eDiscovery

To begin the search-and-deletion workflow, [create an eDiscovery case](edisc-cases-manage) to manage the process.

## Step 2: Create a search in eDiscovery

After you create a case, [create an eDiscovery search](edisc-search-query) for the AI application data that you want to delete. The deletion process you perform in Step 5 deletes all AI-related items that are found in the search (within the 10 item per location limit).

### Data sources for AI data

The following table lists the application and service sources for Copilot and other AI data. All user prompts and responses from AI applications are stored in a user's mailbox.

| For this type of Microsoft Copilot or other AI data... | Search this item class... |
| --- | --- |
| Microsoft Foundry | `IPM.SkypeTeams.Message.ConnectedAIApp.AzureAI.<AzureResourceName>` |
| ChatGPT Enterprise | - Local machine interactions: `IPM.SkypeTeams.Message.ConnectedAIApp.Connector.<ChatGPTEnterprise>` - Browser-based interactions: `IPM.SkypeTeams.Message.CloudAIApp.SaaS.<AppID>` |
| Copilot in Fabric | `IPM.SkypeTeams.Message.Copilot.Fabric.*` |
| Copilot personalization and memory | `IPM.Contact` For more information, see [Copilot personalization and memory](/en-us/copilot/microsoft-365/copilot-personalization-memory). |
| Copilot Studio | `IPM.SkypeTeams.Message.Copilot.Studio.*` |
| Excel | `IPM.SkypeTeams.Message.Copilot.Excel` |
| Facilitator | `IPM.SkypeTeams.Message` |
| Facilitator AI notes | `IPM.SkypeTeams.Message.TeamCopilot.AiNotes.Teams` |
| Loop | `IPM.SkypeTeams.Message.Copilot.Loop` |
| Microsoft 365 App | `IPM.SkypeTeams.Message.Copilot.M365App` |
| Microsoft 365 Copilot | `IPM.SkypeTeams.Message.Copilot.*` |
| Microsoft Copilot for Bing (Microsoft 365 Copilot Chat) | `IPM.SkypeTeams.Message.Copilot.BizChat` |
| Microsoft Entra apps | `IPM.SkypeTeams.Message.ConnectedAIApp.Entra.<AppID>` |
| Microsoft Forms | `IPM.SkypeTeams.Message.Copilot.Forms` |
| Microsoft Security Copilot | `IPM.SkypeTeams.Message.Copilot.Security.SecurityCopilot` |
| OneNote | `IPM.SkypeTeams.Message.Copilot.OneNote` |
| Other AI apps | - Local machine interactions: `IPM.SkypeTeams.Message.ConnectedAIApp.Connector.<AppName>` - Browser-based interactions: `IPM.SkypeTeams.Message.CloudAIApp.SaaS.<AppID>` |
| Outlook | `IPM.SkypeTeams.Message.Copilot.Outlook` |
| PowerPoint | `IPM.SkypeTeams.Message.Copilot.Powerpoint` |
| SharePoint | `IPM.SkypeTeams.Message.Copilot.SharePoint` |
| Teams AI notes in Chat | `IPM.SkypeTeams.Message.TeamCopilot.AiNotes.Teams` |
| Teams Channel | `IPM.SkypeTeams.Message.Copilot.Teams` |
| Teams Chat | `IPM.SkypeTeams.Message.Copilot.Teams` |
| Teams Copilot Chat (Microsoft 365 Copilot Chat) | `IPM.SkypeTeams.Message.Copilot.BizChat` |
| Teams Meeting | `IPM.SkypeTeams.Message.Copilot.Teams` |
| Teams Microsoft 365 Chat (BF) | `IPM.SkypeTeams.Message` |
| WebChat | `IPM.SkypeTeams.Message.Copilot.WebChat` |
| Whiteboard | `IPM.SkypeTeams.Message.Copilot.Whiteboard` |
| Word | `IPM.SkypeTeams.Message.Copilot.Word` |

Note

In step 4, you also need to identify and remove any holds and retention policies assigned to the mailbox that contains the type of Copilot or AI application data that you want to delete.

### Tips for searching for Copilot and other AI data

To collect the most comprehensive set of AI data, use the *Item class* condition and select the **Copilot activity** option when you build the eDiscovery search query for this deletion workflow. This condition includes all Copilot and other AI application data. Add a date range or several keywords to narrow the scope of the search to items relevant to your search and delete investigation.

For Copilot memory data, consider the following when working in eDiscovery:

- Inferred memories can be deleted along with other mailbox items using [Microsoft Graph](/en-us/graph/api/security-ediscoverysearch-purgedata).
- Copilot memories are stored as the *IPM.Contact* item class and they match as contacts in the eDiscovery [condition builder](edisc-condition-builder).
- Deleting a conversation or message from Microsoft Purview or eDiscovery doesn't delete the associated Copilot memory.

### How Copilot interactions appear in eDiscovery results

Each Microsoft 365 Copilot interaction is stored in the user's Exchange Online mailbox as an individual message-class item (see the Data sources for AI data table). When these items appear in eDiscovery search results, review sets, or exports (PST files, individual messages, or Microsoft Graph), the email-style headers reflect the two participants of the interaction:

| Interaction direction | `From` | `To` |
| --- | --- | --- |
| User prompt to Copilot | The user's primary SMTP address | The Copilot application identity (for example, `Microsoft 365 Chat`, `Microsoft 365 Copilot Chat`, `WebChat`) |
| Copilot response to the user | The Copilot application identity | The user's primary SMTP address |

The Copilot application identity is the service-principal display name of the Copilot app that handled the interaction. For example:

- **Microsoft 365 Chat** for Microsoft 365 Copilot Chat (BizChat) interactions.
- The **host app name** for in-app Copilot in Word, Excel, PowerPoint, Outlook, OneNote, Loop, and Teams.
- **WebChat** for browser-based Copilot WebChat interactions.

This identity isn't a routable mailbox and can't receive mail; it identifies the Copilot application that participated in the interaction. This representation is by design and is consistent across all tenants and across commercial and US Government clouds.

## Step 3: Review and verify Copilot and other AI data to delete in eDiscovery

The deletion process in Step 5 deletes the items returned by the search. Review the search results to ensure that the search only returns the items that you want to delete.

You can use the search statistics (specifically the *Top Locations* statistics) to generate a list of the data sources that contain items returned by the search. Use the list of mailboxes from the Top Locations statistics to remove hold and retention policies from the user mailboxes that contain search results.

## Step 4: Remove holds and retention policies from data sources

Before you can delete Copilot or other AI application data from a mailbox, you have to [remove any hold](edisc-hold-manage) or retention policy that is assigned to a target mailbox. If you don't remove the hold or retention policy, the data you're trying to delete is retained.

Use the list of mailboxes that contain the Copilot and AI data that you want to delete to determine if there's a hold or retention policy assigned to those mailboxes, and then remove the hold or retention policy. Record each hold or retention policy that you remove so that you can reapply that policy to the affected mailboxes after the deletion is complete.

## Step 5: Delete Copilot and other AI data in Microsoft Graph Explorer

Note

Because Microsoft Graph Explorer isn't available in some US Government clouds (GCC High and DOD), you must use PowerShell to accomplish these tasks. For more information, see Delete Copilot and other AI data with PowerShell.

Now you're ready to delete Copilot and other AI data from user mailboxes. Use Microsoft Graph Explorer to perform the following three tasks:

1. Get the ID of the eDiscovery case that you created in Step 1. This case contains the search created in Step 2.
2. Get the ID of the search that you created in Step 2 and verified the search results in Step 3. The query in the selected eDiscovery search returns the AI activity data to delete.
3. Delete the data returned by the search.

For information about using Graph Explorer, see [Use Graph Explorer to try Microsoft Graph APIs](/en-us/graph/graph-explorer/graph-explorer-overview).

Important

To perform these three tasks in Graph Explorer, you might have to consent to the eDiscovery.Read.All and eDiscovery.ReadWrite.All permissions. For more information, see the "Consent to permissions" section in [Working with Graph Explorer](/en-us/graph/graph-explorer/graph-explorer-features#consent-to-permissions).

### Get the case ID in Microsoft Graph Explorer

Perform the following steps to retrieve the eDiscovery case ID in Graph Explorer:

1. Go to https://developer.microsoft.com/graph/graph-explorer and sign in to Graph Explorer with an account that's assigned the *Search And Purge* role in the Microsoft Purview portal.
2. Run the following GET request to retrieve the ID for the eDiscovery case. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases` in the address bar of the request query. Be sure to select **v1.0** in the API version dropdown list. This request returns information about all cases in your organization on the **Response preview** tab.
3. Scroll through the response to locate the eDiscovery case. Use the **displayName** property to identify the case.
4. Copy the corresponding ID (or copy and paste it to a text file). Save the eDiscovery case ID; you need it in the procedure for retrieving the search ID.

Tip

Instead of using Graph Explorer to obtain the case ID, you can open the case in the Microsoft Purview portal and copy the case ID from the URL.

### Get the eDiscoverySearchID in Microsoft Graph Explorer

Perform the following steps to retrieve the eDiscovery search ID in Graph Explorer:

1. In Graph Explorer, run the following GET request to retrieve the ID for the search that you created in Step 2, and contains the items you want to delete. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches` in the address bar of the request query, where *{ediscoveryCaseID}* is the CaseID that you obtained in the previous procedure.
2. Scroll through the response to locate the search that contains the items that you want to delete. Use the *displayName* property to identify the search that you created in Step 3. In the response, the search query from the search is displayed in the *contentQuery* property. The items returned by the selected search query are deleted in the purge request described in the following procedure.
3. Copy the corresponding ID (or copy and paste it to a text file). Save the eDiscovery search ID; you need it in the purge request to delete Copilot and other AI application data.

Tip

Instead of using Graph Explorer to obtain the search ID, you can open the case in the Microsoft Purview portal. Open the case and go to the Jobs tab. Select the relevant search and under Support information, find the job ID (the job ID displayed here's the same as the search ID).

### Delete Copilot and other AI data in Microsoft Graph Explorer

Perform the following step to purge the items returned by the search:

1. In Graph Explorer, run the following POST request to delete the items returned by the search that you created in Step 2. Use the value `https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches/{ediscoverySearchID}/purgeData` in the address bar of the request query, where *{ediscoveryCaseID}* and *{ediscoverySearchID}* are the IDs that you obtained in the previous procedures.

    If the purgeData POST request is successful, Graph Explorer displays an HTTP response code in a green banner stating that the request was accepted.

For more information about purgeData, see [sourceCollection: purgeData](/en-us/graph/api/ediscovery-sourcecollection-purgedata).

### Delete Copilot and other AI data with PowerShell

Note

Because Microsoft Graph Explorer isn't available in the US Government cloud (GCC, GCC High, and DOD), you must use PowerShell to accomplish these tasks.

You can also delete Copilot and other AI data with PowerShell. For example, to delete Copilot data in the US Government cloud, use a command similar to the following example:

```powershell
Connect-MgGraph -Scopes "ediscovery.ReadWrite.All" -Environment USGov
```

```powershell
Invoke-MgGraphRequest  -Method POST -Uri '/v1.0/security/cases/ediscoveryCases/<ediscoverySearchID>/searches/<search ID>/purgeData'
```

For more information about using PowerShell to delete Copilot and other AI data, see [ediscoverySearch: purgeData](/en-us/graph/api/security-ediscoverysearch-purgedata).

## Step 6: Verify Copilot and other AI data is deleted

After you run the purgeData POST request, Microsoft Purview removes the Copilot and other AI data returned by the search from the user's mailbox. The user doesn't receive any visible notification or confirmation that the data is deleted.

Deleted Copilot and other AI data moves to the *SubstrateHolds* folder, which is a hidden mailbox folder. Deleted data stays in the *SubstrateHolds* folder for at least one day. The next time the timer job runs (typically between 1-7 days), the timer job permanently deletes the data.

## Step 7: Reapply holds and retention policies to user mailboxes

After you verify that the Copilot and other AI data is deleted, reapply the holds and retention policies to user mailboxes that you removed in Step 4.