---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Transfer a domain from Microsoft to another host - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/transfer-a-domain-from-microsoft-to-another-host?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: frankroj
author: frankroj
manager: dansimp
ms.date: 2026-06-16T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.subservice: m365-domains
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- Adm_O365_Setup
- operations-pod
ms.custom:
- AdminSurgePortfolio
- domains
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
description: Transfer a domain from Microsoft to another host with this step-by-step guide. Learn how to unlock your domain, get an authorization code, and complete the transfer.
locale: en-us
document_id: f82907a2-5f0a-b909-0e15-f7b90768664b
document_version_independent_id: 33c36d45-0ec6-3225-9ad2-f3d040406d2d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/get-help-with-domains/transfer-a-domain-from-microsoft-to-another-host.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/get-help-with-domains/transfer-a-domain-from-microsoft-to-another-host
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/get-help-with-domains/transfer-a-domain-from-microsoft-to-another-host.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: b35e3206-22c0-27da-7758-a601003fe065
---

# Transfer a domain from Microsoft to another host - Microsoft 365 admin | Microsoft Learn

You can't transfer a Microsoft 365 domain to another registrar for 60 days after you purchase the domain from Microsoft.

Note

A *Whois* query shows a Microsoft purchased domain registrar as **Wild West Domains LLC**. However, only Microsoft should be contacted about your Microsoft 365 purchased domain.

Sign in with an account with appropriate permissions, follow these steps to get a code at Microsoft 365, and then go to the other domain registrar website to transfer your domain name to the new registrar.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Transfer a domain

1. In the admin center, go to **Settings** &gt; **Domains**.
2. On the **Domains** page, select the Microsoft 365 domain that you want to transfer to another domain registrar, and then select **Check health**.
3. At the top of the page, select **Transfer domain**.
4. On the **Choose where to transfer your domain** page, select **A different registrar**, and then select **Next**.
5. On the **Unlock domain transfer** page, select **Unlock transfer for *&lt;your domain&gt;***, and then select **Next**.
6. Check your domain transfer contact information, and then select **Next**.
7. Copy the authorization code and wait about 30 minutes for your domain transfer status to change to **Unlocked for transfer** on the **Registration** tab before you continue with next steps.
8. Go to the website of the domain registrar you want to manage your domain name going forward. Follow directions for transferring a domain. If you need assistance, search for help on their website. Transferring a domain usually means paying transfer fees and giving the Authcode to the new registrar so they can start the transfer. Microsoft emails you to confirm the transfer request is received. The domain then transfers within five days.

    You can find the authorization code on the **Registration** tab on the **Domains** page in Microsoft 365.

    Tip

    `.uk` domains require a different procedure. Select an IPS tag from the drop-down menu of UK domain registrars to update your **IPS Tags** to match the registrar you want to manage your domain going forward. Once the tag changes, the domain immediately transfers to the new registrar. To complete the transfer, work with the new registrar. This process most likely involves paying transfer fees and adding the transferred domain to your account with your new registrar.
9. After the transfer is complete, you'll renew your domain at the new domain registrar.
10. To finish the process, go back to the **Domains** page in the admin center, and then select **Complete domain transfer**. This action marks the domain not purchased from Microsoft 365 and disables the domain subscription. It doesn't remove the domain from the tenant and doesn't affect existing users and mailboxes on the domain.

Note

Microsoft 365 purchased domains aren't eligible for nameserver changes or transferring the domain between Microsoft 365 organizations. If either of these procedures are required, the domain registration must be transferred to another registrar.

## Support

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).