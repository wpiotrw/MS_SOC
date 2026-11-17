---
layout: Conceptual
title: Manage dynamic permissions settings for a catalog - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/dynamic-permissions-manage-catalog-settings
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: OWinfreyATL
ms.author: owinfrey
ms.service: entra-id-governance
manager: dougeby
description: Learn how to enable or disable dynamic permissions remediation for a catalog in Microsoft Entra ID Governance using the Microsoft Entra admin center.
ms.topic: how-to
ms.date: 2026-11-16T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: e2c81aea-75a5-8d2d-7004-326ea67bb2f8
document_version_independent_id: e2c81aea-75a5-8d2d-7004-326ea67bb2f8
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/dynamic-permissions-manage-catalog-settings.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/dynamic-permissions-manage-catalog-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/dynamic-permissions-manage-catalog-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 320bfeed-74bb-b2b0-6a0b-d0da5842552a
---

# Manage dynamic permissions settings for a catalog - Microsoft Entra ID Governance | Microsoft Learn

As an Identity Governance Administrator, you can enable or disable dynamic permissions remediation for a catalog in Microsoft Entra ID Governance. This article describes how to change the **Permission remediation** setting in the Microsoft Entra admin center.

For more information about dynamic permissions and its permission remediation capabilities, see [What is dynamic permissions?](dynamic-permissions-overview).

Permission remediation is available for specific resources in a catalog. If you're getting started, see [Tutorial: Mitigate permission risk of agents in Snowflake with Microsoft Entra dynamic permissions](tutorial-dynamic-permissions-prevent-excessive-permissions).

## Prerequisites

Dynamic permissions is in preview and capabilities are subject to change. Licensing requirements for dynamic permissions have not yet been announced. During preview, dynamic permissions for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite.

## Enable dynamic permissions remediation for a catalog

Important

Each application has its own 90-day reporting period, starting when permission remediation is configured for the application in a catalog with permission remediation enabled. During this period, dynamic permissions reports detections and planned remediation actions without automatically applying them.

Microsoft is developing a capability to approve exceptions for individual detections, preventing remediation for those detections. Automatic transitions from reporting to remediation won't begin until this capability is available.

To enable permission remediation for a catalog, complete the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)**.
3. Select **Resources**, and then select **Enable dynamic permissions**.

    [![Screenshot of the Dynamic permissions Resources page with the Enable dynamic permissions button highlighted.](media/dynamic-permissions-manage-catalog-settings/enable-dynamic-permissions.png)](media/dynamic-permissions-manage-catalog-settings/enable-dynamic-permissions.png#lightbox)
4. Select the catalog for which you want to enable permission remediation.
5. Confirm the catalog has the correct resources, and set **Permission remediation** to **Enabled**.
6. Select **Enable dynamic permissions**.

    [![Screenshot of permission remediation enabled for a catalog with the final Enable dynamic permissions button highlighted.](media/dynamic-permissions-manage-catalog-settings/confirm-enable-dynamic-permissions.png)](media/dynamic-permissions-manage-catalog-settings/confirm-enable-dynamic-permissions.png#lightbox)

## Disable dynamic permissions remediation for a catalog

To disable permission remediation for a catalog, complete the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Entitlement management**.
3. Select **Catalogs**.
4. Select the catalog for which you want to disable dynamic permissions capabilities.
5. Select **Edit**.
6. Change **Permission remediation** from **Enabled** to **Disabled**.

    [![Screenshot of catalog settings with the Permission remediation setting highlighted in the Disabled state.](media/dynamic-permissions-manage-catalog-settings/disable-permission-remediation.png)](media/dynamic-permissions-manage-catalog-settings/disable-permission-remediation.png#lightbox)
7. Select **Save**.