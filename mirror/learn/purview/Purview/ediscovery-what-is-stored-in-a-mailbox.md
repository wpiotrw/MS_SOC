---
layout: Conceptual
title: Content stored in Exchange Online mailboxes for eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-what-is-stored-in-a-mailbox
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Content produced by cloud-based apps in Microsoft 365 is stored or associated with a user's Exchange Online mailbox. This content is searchable using Microsoft eDiscovery tools.
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
- MED150
- MET150
locale: en-us
document_id: 6a42ddb3-dbe0-396f-0a2e-f66101722229
document_version_independent_id: 6a42ddb3-dbe0-396f-0a2e-f66101722229
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-what-is-stored-in-a-mailbox.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-what-is-stored-in-a-mailbox
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-what-is-stored-in-a-mailbox.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 50027e48-aa4c-38cd-f73e-6797fe3ffe35
---

# Content stored in Exchange Online mailboxes for eDiscovery | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

A mailbox in Exchange Online is primarily used to store email-related items such as messages, calendar items, tasks, and notes. But that's changing as more cloud-based apps also store their data in a user's mailbox. One advantage of storing data in a mailbox is that you can use the search tools in content search, Microsoft Purview eDiscovery (Standard), and Microsoft Purview eDiscovery (Premium) to find, view, and export the data from these cloud-based apps.

The data from some of these apps is stored in hidden folders located in a non-interpersonal message (non-IPM) subtree in the mailbox. Data from other cloud-based apps might not be stored *in* the mailbox, but it's *associated with* the mailbox, and is returned in searches (if that data matches the search query). Regardless of whether cloud-based data is stored in or associated with a user mailbox, the data is typically not visible in an email client when a user opens their mailbox.

The following table lists the apps that either stores or associates data with a cloud-based mailbox. The table also describes the type of content that each app produces.

| Microsoft 365 app | Description |
| --- | --- |
| Forms^\*^ | Forms and responses to a form are stored in files that are attached to email messages and stored in a hidden folder in the mailbox of the user who created the form. Forms created before April 2020 are stored as a PDF file. Forms created after 2020 are stored as a JSON file. Responses to a form are stored in a CSV file. When you export content from Forms in a PST file, this data is located in the **ApplicationDataRoot** folder in a subfolder named with the following globally unique identified (GUID): **c9a559d2-7aab-4f13-a6ed-e7e9c52aec87**. |
| Microsoft 365 Groups | Email messages, calendar items, contacts (People), notes, and tasks are stored in the mailbox that's associated with a Microsoft 365 group. |
| Microsoft 365 Copilot and Microsoft 365 Copilot Chat | All Copilot activity data (user prompts and Copilot responses) generated in supported Microsoft 365 apps and services is stored in custodian mailboxes. |
| Outlook/Exchange Online | Email messages, calendar items, contacts (People), notes, and tasks are stored in a user's mailbox. |
| People | Contacts in the People app (which are the same contacts as the ones accessible in Outlook) are stored in a user's mailbox. |
| Class Schedule | Plans created in Class Schedule are stored in the mailbox of the corresponding Microsoft 365 Group that is provisioned when a new plan is created. The alias for the group mailbox is the name of the plan. |
| Skype for Business | Conversations in Skype for Business are stored in the Conversation History folder in a user's mailbox. If the mailbox of a participant of a Skype meeting is placed on Litigation Hold or assigned to a retention policy, files attached to a meeting are retained in the participants mailbox. |
| Sway^\*^ | Sways are stored as an HTML file that is attached to an email message and stored in a hidden folder in the mailbox of the user who created the sway. When you export content from Sway in a PST file, this data is located in the **ApplicationDataRoot** folder in a subfolder named with the following GUID: **905fcf26-4eb7-48a0-9ff0-8dcc7194b5ba**. |
| Tasks | Tasks in the Tasks app (which are the same tasks as the ones accessible in Outlook) are stored in a user's mailbox. |
| Teams | Conversations that are part of a Teams channel are associated with the Teams mailbox. Conversations that are part of the Chat list in Teams (also called *1 x N chats*) are associated with the mailbox of the users who participate in the chat. Also, summary information for meetings and calls in a Teams channel are associated with mailboxes of users who dialed into the meeting or call. So when searching for Teams content, you would search the Teams mailbox for content in channel conversations and search user mailboxes for content in 1 x N chats. |
| To-Do | Tasks (called *to-dos*, which are saved in to-do lists) in the To-Do app are stored in a user's mailbox. |
| Viva Engage | Conversations and comments within a Viva Engage community are associated with the Microsoft 365 group mailbox, as well as the user mailbox of the author and any named recipients (@ mentioned or Cc'ed users). Private messages sent outside of a Viva Engage community are stored in the mailbox of the users who participate in the private message. |
|  |  |

Note

^\*^ At this time, if a hold is placed on a mailbox (by using holds in eDiscovery (Standard) or eDiscovery (Premium) cases), content from this app will not be preserved by the hold.