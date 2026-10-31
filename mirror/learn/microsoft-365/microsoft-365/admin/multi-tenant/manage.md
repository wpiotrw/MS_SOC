---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage Multiple Tenants in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/multi-tenant/manage?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to manage multiple Microsoft 365 tenants from a single location using tenant switcher and multitenant views. Streamline admin tasks across tenants efficiently.
customer-intent: As a Microsoft 365 administrator, I want to manage multiple tenants from a single location so that I can streamline administration tasks.
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-01-06T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: tenant
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_NonTOC
- Adm_TOC
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
- multi-tenant
locale: en-us
document_id: 7b378de4-ca71-a16b-6669-369e3e3ff9d4
document_version_independent_id: 1a1a6ec6-8c04-2172-7afa-49d268191687
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/multi-tenant/manage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/multi-tenant/manage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/multi-tenant/manage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/c4c18c0c-090d-4c28-a4be-9e6214a0c4fb
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b22d517c-92cf-4ee3-8dca-36c6cd062217
platformId: 4227c7b3-37b7-0ec0-291a-c9cf9acd1023
---

# Manage Multiple Tenants in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

[Multitenant management](/en-us/entra/identity/multi-tenant-organizations/overview) in the Microsoft 365 admin center offers a unified approach that allows partner administrators to manage all their tenants in a single location. This streamlined solution helps partners with [delegated administrator](/en-us/entra/identity/users/directory-delegated-administration-primer) roles efficiently manage multiple Microsoft 365 tenants. If you're a partner managing multiple tenants, you can:

- Move quickly between tenants you manage
- Assess service health, products, and billing across multiple tenants
- On the **All tenants** page, quickly see the health of all your tenants' services, any open service requests, your products and billing, and the number of users in that tenant

## Before you begin

You must have the [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role assigned to perform this task.

Important

Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use another role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Move between tenants

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), select a tenant name.

    ![Screenshot of Microsoft 365 admin center showing the multitenant switcher interface for managing multiple tenants.](../../media/macorgswitcher.png)
2. Using the **Tenant switcher**, you can move quickly between tenants you manage.

    ![Screenshot of tenant switcher displaying list of managed tenants with search functionality in Microsoft 365 admin center.](../../media/yourtenantslist.png)

## View the All tenants page

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the navigation pane, select **All tenants**.
2. On the **All tenants** page, take one or more of the following steps:

    - Assess service health
    - Review license usage
    - Search for or select the tenant you want to manage
    - Pin your most often visited tenant to the top of the list.

If you mark a tenant as a favorite, the list automatically expands the tenant. Then you can immediately view the status details.

## View service health for all tenants

The service health view shows you if any incidents or advisories are affecting the tenants. It also tells you how many of your managed tenants are affected.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the multitenant view, select **Service Health**.
2. On the **Service health** page aggregated view, you can also see the total number of incidents, the total number of advisories affecting any of the managed tenants, and the number of services with active incidents. You can also see if any incidents and advisories affect your tenants.

    - You can use the filter option to view issues by issue type or by service.
    - You can review issues under **All services** or **All issues** tabs.

    ![Screenshot of multitenant service health page displaying incident summary and affected services across managed tenants.](../../media/multitenant-servicehealth.png)
3. Select an incident on the **All services** or **All issues** tab to get more information about any incident on the **Overview** tab. Select the **Tenants affected** tab to get a list of the affected tenants.

    ![Screenshot of tenants affected tab showing detailed list of tenants impacted by service health issue.](../../media/tenantsaffected.png)

    You can export the list of affected tenants to CSV format so that admins can share it with support teams.

## View a single tenant in the Microsoft 365 admin center

You can return to the Microsoft 365 admin center for any of the tenants from the **All tenants** page.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the navigation pane, select **All tenants**.
2. Select the tenant name for which you want to view the Microsoft 365 admin center.

    The admin center opens for that tenant.