---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Share Microsoft 365 Calendars with users outside your organization - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/share-calendars-with-external-users?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-03-16T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- must-keep
- operations-pod
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
description: Enable external calendar sharing in the Microsoft 365 admin center so users can share free/busy times with people outside your organization. Try it now.
locale: en-us
document_id: 2b3bda19-af86-20e8-92c4-ccb0caee7cd2
document_version_independent_id: cc93f793-d8bf-e508-d1c1-ddada942623d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/share-calendars-with-external-users.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/share-calendars-with-external-users
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/share-calendars-with-external-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c1c51f7d-6c23-3488-ea75-272c96c074d2
---

# Share Microsoft 365 Calendars with users outside your organization - Microsoft 365 admin | Microsoft Learn

Your users might need to schedule meetings with people outside your organization. To simplify the process of finding mutually agreeable meeting times, Microsoft 365 enables you to make calendars available to people outside your organization. These people need to see free and busy times for users in your organization, but don't have user accounts for your Microsoft 365 organization.

As the admin, you can enable external calendar sharing for all users in your organization. Once sharing is enabled, users can use Outlook on the web to share their calendars with anyone inside or outside the organization. People inside the organization can view the shared calendar along with their own calendar. People outside the organization are sent a URL that they can use to view the calendar. Users decide when to share, how much to share, and when to keep their calendars private.

Note

If you want to share calendar information with an on-premises Exchange organization, the Exchange administrator must configure an authentication relationship (federation) between the on-premises environment and Exchange Online. Federation requires supported Exchange versions and specific configuration. For more information, see [Sharing](/en-us/exchange/sharing-exchange-2013-help).

## Enable calendar sharing in the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select **Org Settings**.
4. On the **Services** tab of the **Org Settings** page, select **Calendar**.
5. In the **Calendar** pane:

    - To allow your users to share their calendars with external Microsoft 365 or Exchange users, select **Let your users share their calendars with people outside of your organization who have Office 365 or Exchange**.
    - To allow sharing with people who don't sign in, select **Allow anyone to access calendars with an email invitation**. This option only becomes available after you enable sharing with external Microsoft 365 or Exchange users.
    - If you allow anonymous users outside of your organization access to your users' calendars, choose what type of calendar information to make available to your users:

        - **Show calendar free/busy information with time only**.
        - **Show calendar free/busy information with time, subject, and location**.
        - **Show all calendar appointment information**.

## How users share their calendars

After you enable external calendar sharing, users can choose whether to share their own calendars with external people. Users control who they share with, what level of detail they share, and when to stop sharing.

For step-by-step instructions, see [Share your calendar in Outlook on the web](https://support.microsoft.com/office/7ecef8ae-139c-40d9-bae2-a23977ee58d5).