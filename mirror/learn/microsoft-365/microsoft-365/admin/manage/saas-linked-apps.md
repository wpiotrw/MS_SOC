---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: SaaS linked apps - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/saas-linked-apps?view=o365-worldwide
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
ms.date: 2025-08-26T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- integrated-apps
search.appverid: MET150
ROBOTS: NOINDEX, NOFOLLOW
description: Gives an overview of software as a service (SaaS) linked apps.
locale: en-us
document_id: a9ca7ddb-ddad-e51d-562e-7a35fcb761f7
document_version_independent_id: a9ca7ddb-ddad-e51d-562e-7a35fcb761f7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/saas-linked-apps.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/saas-linked-apps
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/saas-linked-apps.md
platformId: 55d34b5c-ef4d-eff9-bafc-642f6d9d560a
---

# SaaS linked apps - Microsoft 365 admin | Microsoft Learn

The Microsoft 365 admin center gives you the flexibility to deploy single store apps, custom business line of apps, and bundled apps - also called **SaaS linked apps** - from a single location. We invited our independent software vendor (ISV) partners to link their SaaS offer with related free apps, such as apps for Microsoft 365, Teams apps, Office add-ins, and SharePoint Framework solutions. For more information on how partners create these apps, see [How to plan a SaaS offer for the commercial marketplace](https://go.microsoft.com/fwlink/?linkid=2158277).

We help our admins discover these linked apps with the SaaS offer and manage them all at once from the integrated apps portal. The UX on the integrated apps portal allows the admin to apply the same gesture across all the apps at once.

An admin can choose not to deploy an app that is linked to an SaaS offer. In the integrated apps portal, admins then find the status of **More apps available** in the Deployed Apps list view. This status is to inform the admins that there are more integrations from the ISVs that aren't deployed.

## Unsupported scenarios

There are some scenarios when SaaS linked apps can't be managed from the integrated apps portal. You aren't able to deploy a single store add-in from the integrated apps portal for the following scenarios:

- The same add-in is linked to more than one SaaS offer.
- The SaaS offer is linked to add-ins, but it doesn't integrate with Microsoft Graph and no Microsoft Entra App ID is provided.
- The SaaS offer is linked to add-ins, but Microsoft Entra App ID provided for Microsoft Graph integration is shared across multiple SaaS offers.