---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure Microsoft 365 Clutter for Your Organization - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-clutter?view=o365-worldwide
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
ms.date: 2026-06-05T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- user-accounts
description: Enable or disable Microsoft 365 Clutter for all or selected users by using Exchange PowerShell. Configure settings now by following these steps.
locale: en-us
document_id: 122fb260-6533-c67b-0d9c-5282a73989c0
document_version_independent_id: 33bb5e77-e3cd-976e-f333-1d80e1475caa
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/configure-clutter.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/configure-clutter
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/configure-clutter.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 1612d5a3-02d6-2111-f31d-9a340042132a
---

# Configure Microsoft 365 Clutter for Your Organization - Microsoft 365 admin | Microsoft Learn

As an admin, you might need to manage the Clutter feature in Microsoft 365. To turn the Clutter feature on or off for users in your organization, use Exchange PowerShell. (Individuals can turn it on or off by using these instructions: [Turn off/on Clutter in Outlook](https://support.microsoft.com/office/a9c72a77-1bc4-40e6-ba6d-103c1d1aba4c)).

For details on using Exchange PowerShell, see [Using PowerShell with Exchange Online](/en-us/powershell/exchange/exchange-online-powershell) and [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell). You need an account that has at least the [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) role and the ability to connect to Exchange Online by using PowerShell.

## Turn on Clutter by using Exchange PowerShell

You can enable Clutter manually for a mailbox by running the [Set-Clutter](/en-us/powershell/module/exchangepowershell/set-clutter) cmdlet. You can also view Clutter settings for mailboxes in your organization by running the [Get-Clutter](/en-us/powershell/module/exchangepowershell/get-clutter) cmdlet.

Turn on Clutter for a single user named Allie Bellew:

`Set-Clutter -Identity "Allie Bellew" -Enable $true`

## Turn Clutter off by using Exchange PowerShell

You can disable Clutter manually for a mailbox by running the [Set-Clutter](/en-us/powershell/module/exchangepowershell/set-clutter) cmdlet. You can also view **Clutter** settings for mailboxes in your organization by running the [Get-Clutter](/en-us/powershell/module/exchangepowershell/get-clutter) cmdlet. For example, to turn off Clutter for a single user named Allie Bellew, run the following PowerShellcommand:

```PowerShell
Set-Clutter -Identity "Allie Bellew" -Enable $false`
```

If you use PowerShell to bulk create your users, run [Set-Clutter](/en-us/powershell/module/exchangepowershell/set-clutter) against each user's mailbox to manage Clutter.

## How Clutter appears in Outlook on the web

As an admin, you can re-enable Clutter by using Exchange PowerShell. Focused Inbox is turned off and Clutter is active again.

### If you're using Outlook on the web with a Microsoft 365 Business Premium subscription

- If you currently have Clutter enabled:

    - Clutter settings appear.
- If you currently have Focused Inbox enabled:

    - Clutter settings don't appear.
- If Clutter and Focused Inbox are both disabled:

    - Both Clutter and Focused Inbox appear as options in your Mail Settings.

### If you're using Outlook.com

- If you currently have Clutter enabled:

    - Clutter settings appear.
- If you currently have Focused Inbox enabled:

    - Clutter settings don't appear.
- If Clutter and Focused Inbox are both disabled:

    - Both Clutter and Focused Inbox appear as options in your Mail Settings.