---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Buy a Domain Name in Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name?view=o365-worldwide
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
ms.date: 2026-05-08T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.subservice: m365-domains
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- Adm_O365_Setup
- operations-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- AdminTemplateSet
- domains
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
ms.assetid: 1561140a-16a9-4a02-822d-a989250e479d
description: Buy a domain name in Microsoft 365 admin center with our step-by-step guide. Explore available top-level domains and start building your brand today.
locale: en-us
document_id: fb572a6e-0bd1-9609-4cbe-021deb497da7
document_version_independent_id: 7f82b19b-d569-c955-2e2d-20ec3112b3ad
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/get-help-with-domains/buy-a-domain-name.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/get-help-with-domains/buy-a-domain-name
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/get-help-with-domains/buy-a-domain-name.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
2PlusCloud:
- Azure
- M365
- Power
platformId: 2c8b438c-4114-c506-55ce-d2697d74b80d
---

# Buy a Domain Name in Microsoft 365 - Microsoft 365 admin | Microsoft Learn

This article explains how to buy a new domain name for your Microsoft 365 organization. It covers where to buy a domain in the Microsoft 365 admin center, including which top-level domains are available.

::: moniker range="o365-21vianet"

Note

If your organization uses Microsoft 365 operated by 21Vianet in China, see How to buy a domain for Microsoft 365 operated by 21Vianet.

::: moniker-end

## Before you start

To add, modify, or remove domains, you must be a **Domain Name Administrator** of a [business or enterprise plan](https://www.microsoft.com/microsoft-365/business) because these changes affect the whole tenant. Administrators without the **Domain Name Administrator** role or regular users can't make these changes.

## Buy a domain name in the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Domains**](https://admin.cloud.microsoft/?#/Domains).
4. In the **Domains** page, select **Buy domain**.
5. Step through the **Domains &gt; Buy domain** wizard to complete the purchase of your domain.

You can choose from the following top-level domains for your domain.

- .biz
- .cloud
- .com
- .info
- .me
- .mobi
- .net
- .org
- .tv
- .co.uk
- .org.uk

## Domain privacy

Microsoft offers a free *Domain Privacy Subscription* when you purchase a domain. This subscription keeps your contact information private when you register your domain with ICANN. For more information, see [ICANN's website](https://whois.icann.org/en/privacy-and-proxy-services).

## Buy a domain from another domain registrar

If you want to buy a domain from a domain registrar, Microsoft recommends using a registrar that supports automatic setup (Domain Connect):

- [GoDaddy](https://www.godaddy.com/)
- [Aruba](https://hosting.aruba.it/)
- [IONOS](https://www.ionos.com/)
- [EuroDNS](https://www.eurodns.com/)
- [Cloudflare](https://www.cloudflare.com/)
- [WordPress.com](https://wordpress.com/)
- [Plesk](https://www.plesk.com/)
- SecureServer or WildWestDomains (GoDaddy resellers that use SecureServer DNS hosting)
    - Examples:
        - [DomainsPricedRight](https://www.domainspricedright.com/products/domain-registration)
        - [DomainNow](https://www.domainnow.com/)

## Transfer your domain to a different domain registrar

If a provider doesn't support all the necessary DNS records, you can transfer your domain to a different registrar. When you transfer your domain, you change who you send payments to in order to renew and keep your domain name.

Request the transfer at the registrar that you want to move your domain to. Look on their website for an option such as **Transfer DNS**. After they make the changes, it can take a few days to update across the Internet.

::: moniker range="o365-21vianet"

## How to buy a domain for Microsoft 365 operated by 21Vianet

If you don't already have your own domain, you can easily buy one online at a domain name registrar, domain reseller, or even at your current Internet provider. When you sign up for Microsoft 365 operated by 21Vianet, you get a domain name, such as contoso.partner.onmschina.cn. But you might want to use a custom domain name, like fourthcoffee.com.

To set up a domain in Microsoft 365, you must own a domain and change some of the DNS records for your domain.

Caution

Some domain registrars or DNS hosting providers don't allow creating all the DNS records required by Microsoft 365. The following list of hosting providers supports all the needed records. If you're thinking of using a different hosting provider, [Service limitations when your hosting provider doesn't support SRV, CNAME, TXT, or redirection](https://support.microsoft.com/topic/dfbb03e3-08c1-4c4e-b2f0-891665b29b77).

After you register your domain (at a domain registrar), sign in to Microsoft 365 as an admin. Then, set up your domain so you can use it with your email address and other services.

### Domain registrars that support all DNS records required for Microsoft 365

- [Oray](https://oray.com/)
- [HiChina](https://www.hichina.com/)
- [east.net](http://www.east.net/)
- [BIZCN](https://www.bizcn.com/)

::: moniker-end

## Support

If you don't find what you're looking for, check the [**Domains FAQ**](../setup/domains-faq).

Tip

Some configuration tasks might be complex to perform. For technical support, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. At the bottom right, select **Help & Support**.
3. In the **Support Assistant** pane that opens, enter your question.
4. Review the results. If you still have questions, select **Contact support**.

To learn about your options for contacting support, see [Get support for Microsoft 365 for business](/en-us/microsoft-365/admin/get-help-support).