---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create Room and Equipment Mailboxes - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/room-and-equipment-mailboxes?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: twerner
author: twernermsft
manager: scotv
ms.date: 2026-04-08T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- must-keep
- operations-pod
ms.custom:
- Lean
- MSStore_Link
- AdminSurgePortfolio
- admindeeplinkMAC
search.appverid:
- MET150
- MOE150
ms.assetid: 9f518a6d-1e2c-4d44-93f3-e19013a1552b
description: Create room and equipment mailboxes to help your organization reserve shared resources for meetings and events. Set up and manage these resources in Microsoft 365 today.
locale: en-us
document_id: 8c6a9c81-eca7-9f41-8872-93da50e2ebe0
document_version_independent_id: a2a6044c-8c52-e4d2-e0ff-939a07af21a7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/room-and-equipment-mailboxes.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/room-and-equipment-mailboxes
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/room-and-equipment-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 946a3eda-2d0a-e8c5-9e96-92367697f5be
---

# Create Room and Equipment Mailboxes - Microsoft 365 admin | Microsoft Learn

If you have a conference room or equipment that your users need to access, you need a way to make those resources reservable to everyone. Creating a room or equipment mailbox in Microsoft 365 is the best way to allow users to easily reserve these resources. With room and equipment mailboxes, your organization can efficiently reserve shared resources for meetings and events. You might create one for your first floor conference room, media equipment, or a moving truck.

Once you create a room or equipment mailbox, everyone in your organization can reserve shared resources for meetings or events using Outlook. This article explains how to:

- Use room and equipment mailboxes.
- Set up room and equipment mailboxes in the Microsoft 365 admin center.

## Access and use room and equipment mailboxes

To use room or equipment mailboxes, follow these steps to reserve the resource for a meeting or event:

1. Open **Outlook** or **Outlook on the web** on your computer.
2. On the **Home** tab, choose **New items**, and then select **Meeting** from the drop-down list. Alternatively, you can also select **New Meeting** from the **Calendar** ribbon.

    [![Screenshot of scheduling a meeting in Outlook by selecting New Items and then Meeting on the Home tab to reserve a room or equipment mailbox.](../../media/ffd575a8-1036-4d67-b839-73941fc60276.png)](../../media/ffd575a8-1036-4d67-b839-73941fc60276.png#lightbox)
3. In the **Required** field, enter the name of the conference room or equipment you want to reserve in addition to any attendees you want to invite. Alternatively, select **Required** and then double-click the conference room or equipment from the list. Once the conference room or equipment is displayed next to **Required**, select **OK**.

    [![Screenshot of reserving a room or equipment mailbox in Outlook by adding it to the Required field in a meeting invitation.](../../media/4588c806-9fb9-46c9-b2d8-34caa943e28e.png)](../../media/4588c806-9fb9-46c9-b2d8-34caa943e28e.png#lightbox)
4. In the **Title** line, type the purpose of the reservation or meeting.
5. Change the **Location** value or accept the default.
6. Change the **Start time** and **End time** or select **All day**. To make the meeting or reservation repeat, select **Recurrence** at the top.

    [![Screenshot of reserving a room or equipment mailbox meeting time in Outlook by setting start and end times and recurrence options.](../../media/4b72a0a6-4da2-449e-909e-85ea79f78e2c.png)](../../media/4b72a0a6-4da2-449e-909e-85ea79f78e2c.png#lightbox)
7. Type a message describing the purpose and attach any files if needed.
8. To allow others to join online or call in to the meeting, select **Microsoft Teams Meeting** at the top.
9. To make sure the room, equipment, and people you invited are available, select **Scheduling Assistant** from the menu bar. Then select an available time in the calendar.

    [![Screenshot of checking if a room or equipment mailbox is available in Outlook using the Scheduling Assistant to view the availability calendar.](../../media/eb0097c6-4263-4b63-bfca-f7c03ad99b4f.png)](../../media/eb0097c6-4263-4b63-bfca-f7c03ad99b4f.png#lightbox)

    Tip

    In the scheduling calendar, blue means the room or equipment is reserved, or busy. Select the white, or free, area on the calendar.
10. When finished, select **Send**.

## Set up room and equipment mailboxes

To set up a room or equipment mailbox, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with an account that has the proper permissions.
2. From the left navigation bar, select **... Show all**, and then select **Resources** to expand it.
3. Under **Resources**, select [**Rooms & equipment**](https://go.microsoft.com/fwlink/p/?linkid=2067334).
4. In the **Rooms & equipment** page, select **+ Add resource**.
5. In the **Add resource** pane, fill out the room or equipment fields:

    - **Room** or **Equipment**: The type of mailbox you want to create.
    - **Name**: A friendly name or short description.
    - **Email**: The email alias of the room or equipment. You need an email address to send a meeting request to the room or equipment.
    - **Capacity**: The number of people who can fit in the room or use the equipment at the same time.
    - **Location**: The room number or location of the room in a building or region.
    - **Phone number**: The phone number of the room itself. This phone number is different from the meeting phone number generated when using Microsoft Teams.

    [![Screenshot of adding a room or equipment mailbox in the Microsoft 365 admin center by filling in resource details like name, email, and capacity.](../../media/114d49e3-976e-40ef-b0af-2b0f5c85f15e.png)](../../media/114d49e3-976e-40ef-b0af-2b0f5c85f15e.png#lightbox)
6. Select **Save**.

Tip

To keep your room and equipment mailboxes secure, block sign-in to these mailboxes. For more information, see [Block sign-in for the shared mailbox account](/en-us/office365/admin/email/create-a-shared-mailbox#block-sign-in-for-the-shared-mailbox-account).

## Frequently asked questions (FAQs) about room and equipment mailboxes

For answers to common questions about managing room and equipment mailboxes, see [Room and Equipment Mailboxes FAQ](room-equipment-mailboxes-faq).