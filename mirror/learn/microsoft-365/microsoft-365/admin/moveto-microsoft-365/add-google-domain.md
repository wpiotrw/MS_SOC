---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Add your Google Workspace domain - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/moveto-microsoft-365/add-google-domain?view=o365-worldwide
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
- admindeeplinkMAC
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to add and verify your Google Workspace domain in Microsoft 365 for business.
ai-usage: ai-assisted
locale: en-us
document_id: 70316d67-8007-acc2-675a-c5371491a114
document_version_independent_id: 70316d67-8007-acc2-675a-c5371491a114
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/moveto-microsoft-365/add-google-domain.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/moveto-microsoft-365/add-google-domain
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/moveto-microsoft-365/add-google-domain.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
platformId: b3a81f29-4a60-8f22-7b28-d75fa9864cb3
---

# Add your Google Workspace domain - Microsoft 365 admin | Microsoft Learn

## Watch: Add Google Workspace domain

Watch this video and find more on the [Microsoft 365 small business YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198105).

Add your Google Workspace domain to Microsoft 365 for business so you can keep using your business email address.

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the Microsoft 365 admin center, in the left nav, select **Show all** &gt; **Settings** &gt; [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).
3. Choose **Add domain**, enter your domain name, and then select **Use this domain**.
4. Choose **Add a TXT record to the domain's DNS records**, select **Continue**, and copy the TXT value.
5. Identify the DNS hosting provider used by your domain's authoritative nameservers, and sign in to that provider.

    If your Google Domains registration migrated to Squarespace, use the [Squarespace Domains dashboard](https://domains.squarespace.com) to check the nameservers. With custom nameservers, add the record at that DNS provider, not in Squarespace's DNS records. See [Squarespace nameserver guidance](https://support.squarespace.com/hc/en-us/articles/4404183898125-Change-or-reset-your-domain-s-nameservers). Don't change nameservers or transfer the domain just to verify ownership.
6. At the authoritative DNS host, add the **TXT** record using the name and value supplied by Microsoft 365, and then save it. The update usually takes effect within a few minutes but might take up to 48 hours.
7. Return to the [admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), select **Verify**, and then **Close**. Adding the TXT record verifies domain ownership. It doesn't transfer domain registration or DNS hosting, and it doesn't redirect email to Microsoft 365.

## Update users' email addresses

Use the verified business domain when [preparing new email migration accounts](migrate-email#prepare-mail-user-accounts).

For existing users who need a username and primary-email change:

1. In the left nav, select **Users** &gt; [**Active users**](https://go.microsoft.com/fwlink/p/?linkid=834822).
2. Choose a user, select **Manage username and email**, **Edit**, select your domain from the dropdown, then select **Done** and **Save changes**.
3. Repeat for the other users who need the change.

Next, [prepare and migrate email](migrate-email). Change the production MX records after completing the migration batches, as described in [Connect your domain](connect-domain-tom365).