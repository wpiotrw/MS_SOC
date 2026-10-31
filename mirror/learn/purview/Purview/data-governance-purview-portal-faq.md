---
layout: FAQ
title: Frequently asked questions for data governance in the new Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-purview-portal-faq
summary: ''
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.date: 2025-09-19T00:00:00.0000000Z
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
audience: Admin
ms.topic: faq
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: M365-security-compliance
search.appverid:
- MOE150
- MET150
description: Get answers to common questions about data governance in the new Microsoft Purview portal or upgrading an existing account to the new experience.
locale: en-us
document_id: 9c062307-ba27-2bbf-6baa-bdde4e8b93e3
document_version_independent_id: 9c062307-ba27-2bbf-6baa-bdde4e8b93e3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-purview-portal-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-purview-portal-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-purview-portal-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5c140e45-7365-c3cd-6b04-5528c3574577
---

# Frequently asked questions for data governance in the new Microsoft Purview | Microsoft Learn

## Where is the new portal?

The new [Microsoft Purview portal](purview-portal) is located at https://purview.microsoft.com. The [classic data governance portal](use-microsoft-purview-governance-portal) is located at https://web.purview.azure.com.

## How can I use the new portal experience?

The new portal experience is available to all organizations. If you're using Microsoft Purview for the first time and you use Power BI or Microsoft Fabric, you'll automatically have access. If not, create a new account and you're automatically upgraded to the enterprise version of Microsoft Purview within a few weeks. For existing Microsoft Purview users, learn more about using the new experience if [you have one Microsoft Purview account](data-governance-purview-portal#one-microsoft-purview-account) or if [you have multiple Microsoft Purview accounts](data-governance-purview-portal#multiple-microsoft-purview-accounts).

## Is there a cost to use the enterprise version of Microsoft Purview?

Yes. Learn more about pricing at [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/).

## Can I create new Microsoft Purview accounts in my subscription?

It depends:
- If your organization created an account after August 1, 2023, you can't create more accounts.
- If your organization hasn't created a Microsoft Purview account before, if you create an account it will automatically be reconciled to the [new experience](data-governance-purview-portal), and you can't create more accounts after.
- If your organization has a single Microsoft Purview account that has already been reconciled to the [new experience](data-governance-purview-portal), you can't create more accounts.
- If you're using the free version of Microsoft Purview governance solutions and haven't created a Microsoft Purview account, if you [upgrade to the enterprise version](data-governance-free-version-upgrade-to-enterprise), you can't create more accounts.
- If you're using the free version of Microsoft Purview governance solutions and create an account, the newly created account will be automatically reconciled to the [new experience](data-governance-purview-portal) and you can't create more accounts after that.
- If your organization already has multiple Microsoft Purview accounts, you can create Microsoft Purview accounts up to [the preexisting quota](classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits), even if you have already reconciled an account to the new experience.

## We already had a Microsoft Purview account, and are using the new portal experience. Is our account the free or enterprise version of Microsoft Purview?

If you're already using a Microsoft Purview account that's upgraded to use the new portal experience, your organization is using the enterprise version of Microsoft Purview. You can check your organization's account type in the Microsoft Purview portal by going to **Settings** &gt; **View all settings**.

## When I start using the new Microsoft Purview experience, does it create an account for my organization or just for me?

The new Microsoft Purview experience uses a single, organization-wide instance of Microsoft Purview.

## What does this mean for my existing Microsoft Purview governance portal accounts?

One of your Microsoft Purview governance portal accounts are elevated to be the primary tenant/organization level account with all its current metadata and information. If you have other Microsoft Purview accounts, in the future their information will also be made available in the primary account.

## Can multiple accounts in the same tenant have access to the new experience?

Not currently. The new experience uses a single, primary Microsoft Purview account. If you have multiple accounts, you select a primary account when you [upgrade to the new experience](data-governance-purview-portal). In the future, the information in your other accounts will also be made available in this environment.

## What is the impact of upgrading the production account to the enhanced experience?

There's no impact on upgrading the account to the enhanced experience. Users can navigate the capabilities in the new [Microsoft Purview portal](https://purview.microsoft.com) and [classic governance portal in Azure](https://web.purview.azure.com). If users browse Microsoft Purview portal from the Azure portal, the upgraded account provides two links to browse the portals.

## How long does the upgrade take?

If your account is [eligible](data-governance-purview-portal#how-to-use-the-new-experience), upgrading to the new experience only takes a few minutes.

## What if my organization blocked the new portal endpoints on the firewall?

You can still access Microsoft Purview through the classic portal by launching the old endpoints through https://web.purview.azure.com.

## What should I do if my organization can't use preview features?

Upgrading to enhanced experience doesn't change the status of generally available (GA) features.

## My primary Microsoft Purview instance has private endpoints enabled. Can I upgrade it to enhanced experience?

If your Microsoft Purview account had disabled all public network access and is using private endpoints, you can still upgrade to the new experience. You can continue to use your [*ingestion* private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint) as is, but the new experience also uses a *platform* private endpoint. After upgrading to the new experience, you can follow [this guide to set up platform the private endpoint for governance solutions in the Microsoft Purview portal](data-governance-private-endpoints). For more information, see [what to do if your account has disabled all public network access](data-governance-purview-portal#disabled-all-public-network-access).

## How is access to the Microsoft Purview portal granted if you're a Dynamics 365, Microsoft 365 Enterprise, Microsoft Fabric, Power Apps, or Power BI user?

If your organization uses Dynamics 365, Microsoft 365 Enterprise, Microsoft Fabric, Power Apps, or Power BI, your tenant has the Microsoft Purview Discovery Plan added. Administrators can find this plan under **Your products** in the admin center. This plan has no cost and grants access to the new experience.

## What if I'm not an Azure Enterprise, Dynamics 365, Microsoft 365 Enterprise, Microsoft Fabric, Power Apps, or Power BI customer?

If you're an existing Microsoft Purview customer (your Microsoft Entra tenant already has a Microsoft Purview account), a user holding a [Purview Administrator](data-governance-roles-permissions#tenant-level-role-groups) role can upgrade your instance to the new experience. When that happens, you're prompted to confirm the upgrade. When you confirm, your tenant is added to the Microsoft Purview Discovery Plan. Administrators can find this plan under **Your products** in the admin center. This plan has no cost and grants access to the new experience. If a global or billing admin attempts this upgrade, they receive an error. If you don't have access to the Microsoft 365 role groups to assign [Purview Admins](data-governance-roles-permissions#tenant-level-role-groups), [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview).

## My organization wants to continue using the classic portal. What link can we use to access it?

Access the classic portal at https://web.purview.azure.com.

## If I continue to scan or curate assets in the existing classic portal, will the new or updated assets show up in the new portal?

Yes. The upgraded account is accessible via both portals, and changes in metadata and configurations are visible in the classic and new portals.

## Can I opt out of migration to the new experience?

Existing Microsoft Purview accounts stay the same and remain operational in parallel with the new experience for a time. Eventually users are encouraged to transition to the new experience.

## Should I start the upgrade now?

We recommend all Microsoft Purview customers to start the upgrade as soon as possible. New features and capabilities are only available on the new portal.

## What do I need to prepare before the upgrade and what are some areas of considerations to include in my plan?

**1. Prepare your change request.** Before the upgrade, Microsoft Purview users can navigate to the classic Microsoft Purview governance portal only through legacy endpoints: Portal: `web.purview.azure.com` Endpoint: `https://[accountname].purview.azure.com/` After the upgrade, the upgraded account is accessible via legacy experience and the new experience. To use the new experience, make sure your corporate firewalls allow outbound traffic to new endpoints. Access to classic portal and endpoints: Portal:`web.purview.azure.com` Endpoint - `https://[accountname].purview.azure.com/` Access to new portal and endpoints: Portal: `purview.microsoft.com` Endpoint: `api.purview-service.microsoft.com`**2. Add new endpoints to your corporate firewalls.** Even though the classic portal and endpoints are still available, as part of retiring these endpoints, Microsoft suggests planning to include new URLs and endpoints to your firewall. These updates make sure your users' access and applications aren't impacted when the legacy endpoints are retired.**3. Adjust permissions.** The upgraded account can be accessed by users through Microsoft Purview roles. New roles are also added to your Microsoft Purview account at the tenant level. You can manage these roles in new portal. Learn more about [data governance roles and permissions](data-governance-roles-permissions).

## What if my organization has multiple Microsoft Purview accounts?

You can upgrade your primary account. All other Microsoft Purview accounts in your tenant can still be accessed through the classic portal. Be prepared to merge those accounts with the primary account when the feature becomes available. Microsoft will notify customers who require to perform more steps to merge these accounts.

## We have multiple Microsoft Purview accounts and want to upgrade to use the new portal. Which account should we select as the "primary"?

We suggest you select the production account, the account that is used by most of your end users, or the account that's the most critical to your daily operations. See [our guide to choosing your primary account](data-governance-purview-portal#how-to-choose-a-primary-account).

## If I can't create a new account, what are my other options?

Use [collections](data-gov-best-practices-domains-collections) and assign role-based access on those collections to provide granular access control.

## What can I access in the free version of Microsoft Purview governance solutions?

The free version allows users to explore their Azure and Microsoft Fabric resources. See [what's available in the free version](data-governance-free-version#whats-available-in-the-free-version).

## What region is Microsoft Purview in if we use the free version?

The free version of Microsoft Purview governance solutions uses the same location mappings as Microsoft 365, and maps to a location based on your Microsoft Entra ID home region.

## How does Microsoft Purview choose the region for the enterprise version of Microsoft Purview?

**If your tenant has no Microsoft Purview account:** The free version of Microsoft Purview governance solutions is mapped to the same location as your Microsoft 365 instance. If that's unavailable, then it falls back to using the location geographically closest to your Microsoft Entra ID region. When you upgrade from free to enterprise, the enterprise version uses the same location.

**If your tenant has a Microsoft Purview account**: If your Microsoft Purview account is already upgraded to the new experience, it's using the region it was created in or the region that was selected during upgrade. If you haven't upgraded a Microsoft Purview account to the new experience, if you upgrade an existing account or create a new account to upgrade then the enterprise version will use that account's region.

The Microsoft Purview region is incidental; it doesn't affect your configurations or how you use your data, even if your sources are in another region. Microsoft Purview does all data processing local to your data sources, and doesn't move your data to its own region or store your data. Your data remains securely in its own location, and ingress and egress charges that other Azure products sometimes incur aren't applicable. Regardless of where your data sources are housed, you don't need to change the region your Microsoft Purview account is using to interact with your sources.

If you're trying to upgrade from the free version to enterprise and can't upgrade due to security policy or data residency constraints around Microsoft Purview's mapped region, [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview). Also contact support if you're trying to create a first Microsoft Purview account in the Azure portal and can't create the account in the selected region due to security policy or data residency constraints.

If you're moving because of a security policy, you can only move to another region in your tenant's current [Azure Geography](https://azure.microsoft.com/explore/global-infrastructure/geographies/#geographies). If you need to move to a region outside your tenant's current geography, you need to create a tenant in that geography.

## How can I get more governance capabilities?

All governance features and capabilities are available by [upgrading to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).