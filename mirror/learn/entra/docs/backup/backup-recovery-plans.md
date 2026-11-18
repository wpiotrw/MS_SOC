---
layout: Conceptual
title: Microsoft Entra Backup and Recovery plans - Microsoft Entra | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/backup/backup-recovery-plans
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: tazkiaafra
ms.author: tazkiaafra
ms.service: entra-id
manager: dougeby
description: Compare Microsoft Entra Backup and Recovery Standard and Premium plans, including retention, billing, and performance.
ms.date: 2026-10-19T00:00:00.0000000Z
ms.topic: concept-article
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: cb7530c6-ad7b-c22f-0f4c-7f9444f2e2b7
document_version_independent_id: cb7530c6-ad7b-c22f-0f4c-7f9444f2e2b7
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/backup/backup-recovery-plans.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: backup/backup-recovery-plans
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/backup/backup-recovery-plans.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 502497d2-6f41-dd89-3b2a-172423855c71
---

# Microsoft Entra Backup and Recovery plans - Microsoft Entra | Microsoft Learn

Microsoft Entra Backup and Recovery has Standard and Premium plans for daily backups of supported directory objects. Both plans support the same backup, difference-report, and recovery capabilities. They differ in retention, initial difference-report and recovery performance, licensing, and billing.

Identity administrators can use this comparison to choose the plan that meets their organization's retention and billing needs.

Note

The Premium plan is in preview and must be turned on in the Microsoft 365 admin center. To get started, see [Set up Microsoft 365 Backup](/en-us/microsoft-365/backup/backup-setup?view=o365-worldwide).

## Compare Standard and Premium plans

The following table summarizes the plan differences.

| **Capability** | **Standard plan** | **Premium plan (preview)** |
| --- | --- | --- |
| **Retention** | Up to 7 days of daily backups. | Up to 30 days of daily backups. |
| **Backup frequency** | Once a day. | Once a day. |
| **[Supported objects](scope-supported-objects-limitations)** | All object types supported by Microsoft Entra Backup and Recovery. | The same supported object types as the Standard plan. |
| **Difference reports and recovery** | The first operation against an unloaded backup loads the backup data. Later operations against the same backup reuse the loaded data. | Initial processing skips data loading, allowing faster full difference-report generation or recovery. |
| **Recovery scope** | Recover all supported objects, selected object types, or specific object IDs. | The same recovery scope as the Standard plan. |
| **Licensing prerequisites** | Included with Microsoft Entra ID P1 and P2 licenses. | Microsoft Entra ID P1 and P2 licenses aren't required. The tenant must have at least one SharePoint license or a license that includes SharePoint. |
| **Billing model** | Included with Microsoft Entra ID P1 and P2 licenses. | Consumption-based billing at $0.025 USD per protected object per month. For pricing details, see [Microsoft Entra Backup and Recovery Premium pricing](backup-recovery-premium-pricing). |
| **Default state** | Available automatically for tenants with Microsoft Entra ID P1 or P2 licenses. | Off by default. |

## How Premium retention accumulates

Premium backup history grows after each daily backup cycle until 30 days are available.

For a tenant that already has Standard plan backups:

| **Time after Premium is enabled** | **Available backup history** | **Premium billing** |
| --- | --- | --- |
| **Day 1** | Six Standard backups and one Premium backup. | One day of Premium backup data. |
| **Day 2** | Five Standard backups and two Premium backups. | Two days of Premium backup data. |
| **Day 30** | Thirty Premium backups in a rolling window. | Thirty days of Premium backup data. |

For a tenant without Microsoft Entra ID P1 or P2 licenses, backup history starts with the first Premium backup and grows by one backup after each daily backup cycle.

## How to identify the plan type

To identify your tenant's current plan, go to **Backup and recovery** &gt; **Settings** in the Microsoft Entra admin center. Under **Plan status**, **Current plan** shows **Standard** or **Premium**.

[![Screenshot of the Backup and recovery Settings page showing Premium as the current plan under Plan status.](media/backup-recovery-plans/plan-status.png)](media/backup-recovery-plans/plan-status.png#lightbox)

To identify the plan associated with a specific backup, go to **Backups** and check the **Plan** column. Each backup shows **Standard** or **Premium**. Retained Standard and Premium backups can appear together and are sorted by date.

[![Screenshot of the Backups page showing Standard and Premium values in the Plan column.](media/backup-recovery-plans/backup-plan-column.png)](media/backup-recovery-plans/backup-plan-column.png#lightbox)

## What happens when Premium stops

Premium can stop because an administrator turns it off or because of a billing issue. In either case:

- The service stops creating new Premium backups.
- Existing Premium backups remain available for difference reports and recovery jobs until they expire.
- The **Plan** column continues to identify retained Premium backups.

For tenants with Microsoft Entra ID P1 or P2 licenses, new Standard backups begin accumulating after Premium stops. The backup list can contain retained Premium backups and new Standard backups at the same time.

For tenants without Microsoft Entra ID P1 or P2 licenses, no new Standard backups are created.

If Premium stops because of a billing issue, use the Microsoft 365 admin center to review the billing status.