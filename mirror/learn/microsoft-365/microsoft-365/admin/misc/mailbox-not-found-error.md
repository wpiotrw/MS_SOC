---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Getting a mailbox not found error in Outlook on the web - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/mailbox-not-found-error?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: kwekua
author: kwekuako
manager: scotv
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: high
ms.date: 2025-03-18T00:00:00.0000000Z
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- operations-pod
ms.custom:
- AdminTemplateSet
- admindeeplinkMAC
- user-accounts
ROBOTS: NOINDEX, NOFOLLOW
search.appverid:
- MET150
ms.assetid: 7e453a40-66df-44ab-92a1-96786cb7fb34
description: A **Mailbox couldn't be found for** error means the account you used to connect to Outlook on the web doesn't have an Exchange Online license.
locale: en-us
document_id: 00421a8e-42cf-c393-f91d-da1b7d7cc7da
document_version_independent_id: de00b816-762d-2171-eb7f-1ce6a55ec189
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/misc/mailbox-not-found-error.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/misc/mailbox-not-found-error
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/misc/mailbox-not-found-error.md
platformId: aef1349b-b44f-aaed-743c-7eb57cddd9a5
---

# Getting a mailbox not found error in Outlook on the web - Microsoft 365 admin | Microsoft Learn

If you're using Outlook on the web and you get a **Mailbox couldn't be found for** error, the account that you used to connect to Outlook on the web doesn't have an Exchange Online license and therefore, no mailbox is associated with the account.

## Assign a license to your account

Your admin can assign a license to your account by following these steps:

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). In the left nav pane, in the **Users** section, select **Active users**, and then select the user who is seeing the error.
2. In the user page that opens, go to the **Licenses and Apps** section, select the appropriate **Location** value, and assign a license that contains Exchange Online (expand **Apps** to see its details).
3. When you're finished, click **Save changes**.