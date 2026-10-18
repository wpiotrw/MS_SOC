---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Cancel Google Workspace (and keep your domain) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/moveto-microsoft-365/cancel-google?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: heidip
author: MicrosoftHeidi
manager: dansimp
ms.date: 2026-09-25T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection:
- Tier2
- highpri
- M365-subscription-management
- Adm_O365
- operations-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- adminvideo
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to cancel Google Workspace subscription but keep your domain.
ai-usage: ai-assisted
locale: en-us
document_id: 173fae7e-7f5e-0fad-c1da-2d432e3da45e
document_version_independent_id: 173fae7e-7f5e-0fad-c1da-2d432e3da45e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/moveto-microsoft-365/cancel-google.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/moveto-microsoft-365/cancel-google
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/moveto-microsoft-365/cancel-google.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7bb87418-fc90-dc6a-3df0-b237b3fe3387
---

# Cancel Google Workspace (and keep your domain) - Microsoft 365 admin | Microsoft Learn

This procedure is for a domain-verified Google Workspace organization that uses Gmail. Review Google's [cancellation guidance](https://knowledge.workspace.google.com/admin/billing/cancel-google-workspace) for your subscription's data and billing requirements, including any Cloud Identity exceptions.

Important

When you cancel your subscription, it's canceled immediately and you can't undo this action. Download the data you need before canceling; deleted Google Workspace data can't be restored.

If you purchased Google Workspace through a reseller, follow the reseller's cancellation process instead of the Google Admin procedure below.

1. Sign in to [Google Admin](https://admin.google.com/) and go to **Billing** &gt; **Subscriptions**.
2. Choose your Google Workspace subscription and select **Cancel subscription**. If that option isn't shown, select **More** first.
3. Review the cancellation terms for your subscription, and confirm cancellation.

Note

- Canceling Google Workspace doesn't cancel a domain registration managed by a separate registrar or DNS host. Continue paying the registrar and preserve access to the registrar account.
- Deleting your organization's Google Account is a separate, optional action. Before deleting it, make sure you can sign in to your registrar, including Squarespace if applicable, without the Google Workspace identity.