---
layout: Conceptual
title: View detections and remediations (Preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/dynamic-permissions-review-detections-remediations
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: OWinfreyATL
ms.author: owinfrey
ms.service: entra-id-governance
manager: dougeby
description: Learn how to see the dynamic permissions detection results and remediation details for non-human identities in catalog resources in Microsoft Entra ID Governance.
ms.topic: how-to
ms.date: 2026-11-14T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: 1c1ff0f4-6ae6-a78e-e209-66fa4d7c8d29
document_version_independent_id: 1c1ff0f4-6ae6-a78e-e209-66fa4d7c8d29
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/dynamic-permissions-review-detections-remediations.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/dynamic-permissions-review-detections-remediations
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/dynamic-permissions-review-detections-remediations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
platformId: 56c2cee6-e5c8-bb4f-54c3-025b18bfc065
---

# View detections and remediations (Preview) - Microsoft Entra ID Governance | Microsoft Learn

As an Identity Governance Administrator, you can see results of dynamic permission detection of non-human identities across resources in a catalog in Microsoft Entra ID Governance. You can then select an identity to view more detection details, including the planned remediation action and remediation status.

This feature focuses on overpermissioned non-human identities. For viewing the discovered users and groups in applications, see [Discover identities in target applications with account discovery](../identity/app-provisioning/how-to-account-discovery).

## Prerequisites

### Licensing

Dynamic permissions is in preview and capabilities are subject to change. Licensing requirements for dynamic permissions have not yet been announced. During preview, dynamic permissions for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite.

### Resource setup

Before viewing detections, you will need to

- Have one or more resource in the catalog already set up for permission remediation.
- Optionally, configured [separation of duties rules for non-human identities](dynamic-permissions-manage-separation-duties).

If you're getting started, see [Tutorial: Mitigate permission risk of agents in Snowflake with Microsoft Entra dynamic permissions](tutorial-dynamic-permissions-prevent-excessive-permissions).

## View detections and remediations

To see detections and remediation details for the resources in a catalog, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](../identity/role-based-access-control/permissions-reference#identity-governance-administrator).
2. Browse to **ID Governance** &gt; **Dynamic permissions (preview)**.
3. Select **Detections**.
4. Select a catalog which has the desired resources:

    - If you're visiting **Detections** for the first time, select a catalog when prompted.
    - If you've already selected a catalog and want to see the detections from another catalog, select **Change catalog**, and then select the other catalog.
5. The detections are shown for each identity in a resource impacted by a rule. Select an identity to view the detection details, including the planned remediation action and remediation status, if configured.

    [![Screenshot of the Detections page showing an identity's risk categories, resource, and remediation status.](media/dynamic-permissions-review-detections-remediations/view-detections.png)](media/dynamic-permissions-review-detections-remediations/view-detections-expanded.png#lightbox)