---
layout: Conceptual
title: Get started with DLP file quarantine for SharePoint and OneDrive | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-spo-odb-quarantine-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
- SPO_Content
search.appverid:
- MET150
description: Learn the prerequisites, permissions, and configuration steps for using the DLP file quarantine action for SharePoint and OneDrive.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: fbac11ec-4776-8727-181d-c9d694c7523b
document_version_independent_id: fbac11ec-4776-8727-181d-c9d694c7523b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-spo-odb-quarantine-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-spo-odb-quarantine-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-spo-odb-quarantine-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8e04492e-9353-1f1d-d351-749184a8173f
---

# Get started with DLP file quarantine for SharePoint and OneDrive | Microsoft Learn

Note

The features described in this article are in preview. This article walks you through the prerequisites and configuration for using the DLP file quarantine action for SharePoint and OneDrive locations.

## Before you begin

### Licensing

For information on licensing, see:

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

DLP file quarantine for SharePoint and OneDrive is only available for E5 licenses.

### Permissions

To configure and manage DLP file quarantine, you need one of the following Microsoft Entra ID roles:

- Compliance administrator
- Security administrator
- Compliance data administrator

#### Recommended permissions for quarantine site management

Because the quarantine site contains highly sensitive files, the administrator who manages it should also have the following data classification permissions:

- **Data Classification List Viewer** — Allows viewing items listed in Data Explorer.
- **Data Classification Content Viewer** — Allows viewing the actual contents of items in Data Explorer.

> 
> ![CAUTION] These permissions aren't technically required to configure or use file quarantine. However, you should use the same criteria when selecting accounts for administering this feature as you do for selecting accounts to be members of the **Data Classification List Viewer** and **Data Classification Content Viewer** roles. You should apply the same account-selection criteria because the quarantine site can contain files with sensitive content that the admin might need to inspect before deciding whether to restore or delete them. To learn more, see [Get started with Data Explorer](data-classification-activity-explorer).

#### Roles and role groups

Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

## Deploy a DLP policy with the quarantine action

For step-by-step instructions on how to configure quarantine settings and create and deploy a policy see, [Create a DLP policy to quarantine files in SharePoint and OneDrive](dlp-create-policy-spo-odb-quarantine).

## View quarantine alerts

Use the following steps to view alerts for quarantined files:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data loss prevention** &gt; **Alerts**.
2. Review alerts for policies that use the quarantine action. DLP alerts and DLP rule match events include:

    - The quarantine file location.
    - The file owner.
    - The original file path.
3. For more information, see [Get started with the data loss prevention alerts dashboard](dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](/en-us/defender-xdr/dlp-investigate-alerts-defender).

## View quarantine activity in Data Explorer

Use Activity explorer to review quarantine-related DLP events:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data classification** &gt; **Activity explorer**.
2. Filter for DLP policy rule match events related to your quarantine policy.
3. For more information, see [Get started with Activity explorer](data-classification-activity-explorer).

## Restore a quarantined file

File restore is a manual process.

Important

After restore, original sharing permissions aren't restored. Only the latest file version is preserved. The same DLP rule won't re-quarantine the restored file, even if the file or policy is modified. Other DLP rules continue to apply.

To restore a quarantined file:

1. Locate the quarantined file in the quarantine site.
2. Identify the original file path by using audit logs or the DLP alert details.
3. Move the file from the quarantine site back to the original location.
4. Delete the tombstone text file from the original location.