---
layout: Conceptual
title: Microsoft Entra Backup and Recovery Premium pricing (preview) - Microsoft Entra | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/backup/backup-recovery-premium-pricing
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: tazkiaafra
ms.author: tazkiaafra
ms.service: entra-id
manager: dougeby
description: Learn how Microsoft Entra Backup and Recovery Premium pricing works and estimate monthly costs based on the number of protected objects.
ms.date: 2026-11-16T00:00:00.0000000Z
ms.topic: concept-article
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: 4ab46e66-a892-1bfe-8e6a-6b5e9c81dbd5
document_version_independent_id: 4ab46e66-a892-1bfe-8e6a-6b5e9c81dbd5
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/backup/backup-recovery-premium-pricing.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: backup/backup-recovery-premium-pricing
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/backup/backup-recovery-premium-pricing.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 29718ff1-63c6-13ff-89b2-3f78d24946e5
---

# Microsoft Entra Backup and Recovery Premium pricing (preview) - Microsoft Entra | Microsoft Learn

Microsoft Entra Backup and Recovery Premium uses consumption-based pricing. The price is $0.025 USD per protected Microsoft Entra object per month.

Use the pricing formula and example in this article to estimate your monthly cost. The estimate helps with planning, but your actual charges depend on billed usage.

Note

The Premium plan is in preview and must be turned on in the Microsoft 365 admin center. To get started, see [Set up Microsoft 365 Backup](/en-us/microsoft-365/backup/backup-setup?view=o365-worldwide).

## Pricing model

Estimate the monthly cost by multiplying the number of protected Microsoft Entra objects by the monthly price per object:

`Estimated monthly cost = number of protected objects × $0.025 USD`

The estimate uses the number of protected objects as its input.

## Pricing example

The following examples estimate the cost for a full month when the protected-object count remains constant.

| Protected objects | Calculation | Estimated monthly cost |
| --- | --- | --- |
| **10,000** | 10,000 × $0.025 USD | $250 USD |
| **50,000** | 50,000 × $0.025 USD | $1,250 USD |
| **100,000** | 100,000 × $0.025 USD | $2,500 USD |
| **500,000** | 500,000 × $0.025 USD | $12,500 USD |
| **1,000,000** | 1,000,000 × $0.025 USD | $25,000 USD |

## Billing through Microsoft 365 Backup

Billing for Premium is processed through Microsoft 365 Backup. For commerce billing, protected-object usage is represented as GB-based billing units. These units don't indicate the amount of backup storage consumed. For details, see the [Microsoft 365 Backup pricing model](/en-us/microsoft-365/backup/backup-pricing?view=o365-worldwide).