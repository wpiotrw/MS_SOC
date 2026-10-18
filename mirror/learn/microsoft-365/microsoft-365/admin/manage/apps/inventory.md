---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: View and oversee apps in Microsoft Copilot Managed Runtime across your tenant (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/inventory?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how the All apps page in the Microsoft 365 admin center gives admins a centralized view to discover, monitor, and govern apps in Copilot Managed Runtime.
ms.date: 2026-09-25T00:00:00.0000000Z
author: mikferland-msft
ms.author: miferlan
manager: zoraz
ms.reviewer: mkaur
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: 90429e18-98d2-3ab1-7e6b-94a243626be7
document_version_independent_id: 90429e18-98d2-3ab1-7e6b-94a243626be7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/inventory.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/inventory
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/inventory.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c78390cd-0c27-4b41-6790-cb4953b17c88
---

# View and oversee apps in Microsoft Copilot Managed Runtime across your tenant (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

Copilot Managed Runtime lets people across your organization build and ship solutions quickly, but that growth can leave administrators without a clear view of what exists, who owns it, and whether it's healthy. The **All apps** page in the Microsoft 365 admin center closes that gap, giving tenant administrators a single, centralized view of every app built with Copilot Managed Runtime across the organization. Instead of chasing down app owners or piecing together information from multiple tools, admins get the full picture in one table and can act on it immediately.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

By using the **All apps** page, you can:

- **Discover every app built with Copilot Managed Runtime**: See who built each app, what it connects to, and where it runs, all without leaving the admin center.
- **Keep your estate healthy**: Monitor app open success, session counts, and latency, and set alert rules to catch problems before users feel them.
- **Enforce compliance standards**: Spot apps running in nonapproved regions or outside expected environment groups so you can keep your tenant in policy.
- **Act with confidence**: Block apps under investigation or delete abandoned and duplicate apps directly from the inventory.

## Where to find it

In the Microsoft 365 admin center, go to **Apps** &gt; **All apps**.

## What's included

The **All apps** page always shows apps built with **Copilot Managed Runtime** in the tenant. Other app types are managed elsewhere, as summarized in the following table.

| App type | In All apps? | Notes |
| --- | --- | --- |
| **Copilot Managed Runtime apps** | Yes | Always shown. |
| **Integrated apps** | Yes | Appears on a separate **Integrated apps** tab. Integrated apps still appear in **Settings** &gt; **Integrated apps** as usual. See [Manage integrated apps in the Microsoft 365 admin center](/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center). |
| **Canvas / Model-Driven / Code / Vibe apps** | No | Governed in the Power Platform admin center (PPAC). |

When your tenant opts in to Copilot Managed Runtime, an **Integrated apps** tab appears next to the **Copilot Managed Runtime** tab so you can see both in one place. This tab is an added view only. It doesn't change how integrated apps are governed or who can access that experience. Integrated apps still appear in **Settings** &gt; **Integrated apps** as usual. When your tenant isn't opted in, integrated apps don't appear on the **All apps** page and stay in their single location under **Settings** &gt; **Integrated apps**.

## Required roles

Entra role assignments control access to the **All apps** page in the Microsoft 365 admin center. Access is per tab: the **Copilot Managed Runtime** and **Integrated apps** tabs each use their own roles, and a tab appears only if your role grants access to it.

| Role | Copilot Managed Runtime | Integrated apps tab |
| --- | --- | --- |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | Full: view, delete, block | Full: all integrated app types |
| [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | Full: view, delete, block | Not shown |
| [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) | Read-only | Copilot agents only |
| [AI Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader) | Read-only | Not shown |
| [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | Read-only | Read-only: all types |
| [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) | Not shown | Outlook and Office add-ins they deployed |

Read-only roles can view apps but can't take actions like delete or block. The **Integrated apps** tab respects the same roles integrated apps use today, so a role that can't manage integrated apps today still can't here.

## App inventory

The **All apps** page shows a table of every app built with Copilot Managed Runtime in the tenant. Created, updated, or deleted apps appear within 15 minutes. The default columns are:

| Column | Description |
| --- | --- |
| **Name** | The display name of the app |
| **Owner** | Current owner of the app (might differ from the original creator) |
| **Status** | Current status of the app (for example, Active or Blocked) |
| **Location** | Region where the app is hosted |
| **Environment group** | The environment group governing this app |
| **Created on** | Date the app was created |

You can add more columns, such as **Created by**, **Last modified on**, **Last modified by**, **App ID**, **Owner ID**, and more through **Choose columns**.

### Summary cards

Two summary cards above the table give admins a quick overview:

- **Total apps**: The total number of apps built with Copilot Managed Runtime in the tenant.
- **Blocked apps**: The number of apps that an admin blocks.

## App detail panel

Select an app to open its detail panel. The panel has four tabs:

- **Details**: Core metadata for the app. In addition to the columns available in the table, the panel surfaces **Owner ID** and **Copilot Managed Runtime ID**.
- **Usage**: Usage metrics for the app. Metrics data appears here once usage increases.
- **Monitor**: Health and reliability metrics for the app, including App open success rate, App session count, Time to interactive (P75), Data requests success rate, and Data requests latency (P75). Admins can create alert rules from this tab. (Currently in preview; alerts can be configured with a data review period of 1 hour or 24 hours.)
- **Data & tools**: How the app is built, including connectors, data sources, and dependencies.

## Actions

You can access all actions from both the **table** (via the three-dot context menu on a row) and the **detail panel**. Admins who already know what they need can act directly from the table without opening the detail panel.

### Delete

Permanently remove an app. A confirmation dialog summarizes what the deletion affects before confirming. This action is useful for cleaning up abandoned, test, or duplicate apps.

### Block

Immediately block end-user access to the app while preserving the app and its data. A blocked app shows a blocked status to users who try to launch it. Admins can unblock later if the issue is resolved. This action is useful when an app needs investigation (for example, flagged for non-compliance, suspicious behavior, or a security concern) but shouldn't be deleted yet.

## Working with the table

The table supports filtering, sorting, searching, column customization, and export.

### Filter

Filter pills above the table let admins narrow results by **Owner**, **Status**, **Location**, and **Environment group**. Filters are cumulative: stacking multiple filters progressively narrows results. The count above the table updates to reflect matching results (for example, "Showing 111 of 303 total apps").

### Sort

Select any column header to sort ascending or descending.

### Search

Use the **Search by keyword** field to search across the entire app inventory.

### Choose columns

Select **Choose columns** to add or remove columns and tailor the view to your needs.

### Export

Select **Export** to download the current view as a CSV file for offline analysis or reporting. Exporting can take some time depending on the number of apps in the tenant.

### Refresh

Select **Refresh** to reload the app inventory with the latest data.