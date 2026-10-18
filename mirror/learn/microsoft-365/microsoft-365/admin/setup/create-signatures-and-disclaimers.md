---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create Organization-wide Email Signatures and Disclaimers - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/create-signatures-and-disclaimers?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2026-05-07T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- must-keep
- operations-pod
ms.custom:
- VSBFY23
- TRN_M365B
- OKR_SMB_Videos
- seo-marvel-may2020
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- adminvideo
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 2d75860f-c527-4352-a7f6-73eba54c0c72
description: Create organization-wide email signatures in Microsoft 365 to add company branding and legal disclaimers to all outgoing messages. Step-by-step guide for admins.
locale: en-us
document_id: 3a984a46-1f7b-6ef1-71f3-c5df6c142c01
document_version_independent_id: 4fab7da3-c9ae-0136-c693-ae99c1090f40
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/create-signatures-and-disclaimers.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/create-signatures-and-disclaimers
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/create-signatures-and-disclaimers.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 3b168c0c-0e9c-871f-dd07-c5cf18a89572
---

# Create Organization-wide Email Signatures and Disclaimers - Microsoft 365 admin | Microsoft Learn

Create organization-wide email signatures in Microsoft 365 to ensure consistent branding and legal compliance across all outgoing messages. You can set up email signatures to apply to all messages or specific messages based on conditions like recipient or content patterns. This guide shows you how to create and manage these signatures using the Exchange admin center.

## Create a signature that applies to all messages

To learn how to [Create a company-wide email signature](https://go.microsoft.com/fwlink/?linkid=2198031), watch the following video.

Organization-wide signatures are called **disclaimers**, regardless of what they include. For example, they can just be a signature, or they can also include your address, legal disclaimer, or other information.

To create a signature that applies to all messages, follow these steps:

1. Sign in to the [Exchange admin center](https://admin.exchange.microsoft.com/#/).

    Tip

    You can also get to the Exchange admin center from the Microsoft 365 admin center. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/) and then from the left navigation bar, select **… Show all**. Under **Admin centers**, select **Exchange**.
2. From the left navigation bar, select **Mail flow** to expand it.
3. Under **Mail flow**, select **Rules**.
4. In the **Rules** page, select **+ Add a rule**, and then select **Apply disclaimers**.
5. In the **Select rule conditions** page in the **New transport rule** pane:

    1. In the **Name** field, enter a name for the rule.
    2. Select the **Apply this rule** drop-down menu and then select **Apply to all messages**.
    3. Select the **Do the following** drop-down menus and select **Apply a disclaimer to the message** in the left menu and **append a disclaimer** in the right menu.
    4. Under the **Do the following** drop-down menu:

        1. Select the **Enter text** link. In the **specify disclaimer text** pane that opens, enter the text of your disclaimer, and then select **Save**.
        2. Select the **Select one** link. In the **specify fallback option** pane that opens, select **Wrap**, and then select **Save**. This option only applies if the disclaimer can't be added because of encryption or other mail setting that blocks the signature. When **Wrap** is selected, the signature is wrapped in a message envelope.
    5. If desired, select the **Except if** drop-down menus, and then choose whether you want an exception for one of the listed items in the left menu and the condition in the right menu.
    6. Select **Next**.
6. In the **Set rule settings** page in the **New transport rule** pane:

    1. Under **Rule mode**, select **Enforce** to turn on the disclaimer immediately. To test the disclaimer first, select either **Test with Policy Tips** or **Test without Policy Tips** instead.
    2. Select a severity level in the **Severity** drop-down menu.
    3. Select **Activate this rule on** and specify a date to activate the rule.
    4. If desired, select **Deactivate this rule on** and specify a date to deactivate the rule.
    5. If desired, select **Stop processing more rules**. Select this check box to avoid applying additional rules after this rule processes a message.
    6. If desired, select **Defer the message if rule processing doesn't complete**. Select this check box to resubmit the message for processing. By default, the rule is ignored, and delivery of the message continues as normal.
    7. For the **Match sender address in message** drop-down menu, leave it at the default of **Header**. This option isn't relevant in this scenario since the rule applies to all messages.
    8. Select **Next**.
7. In the **Review and finish** page in the **New transport rule** pane, review the settings for the new rule, and then select **Finish**.
8. When the rule finishes saving, select **Done**.

## Limitations of organization-wide email signatures

The following limitations are limitations when managing email signatures in Microsoft 365:

- You can't insert the signature directly under the latest email reply or forward.
- Users can't see server-side email signatures in their **Sent Items** folders.
- You can't embed images in email signatures.
- Rules skip lines that contain variables they can't update. For example, if you use a variable for a user's phone number but the phone number isn't provided for a user, the system skips the line containing the variable.

Tip

Some of these limitations can be overcome by using non-Microsoft tools. To find tools that add capabilities and help manage email signatures and disclaimers, search for `email signature software`. Several of these tools are from Microsoft Gold Partners.