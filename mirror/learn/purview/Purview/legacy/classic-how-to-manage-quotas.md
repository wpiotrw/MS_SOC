---
layout: Conceptual
title: Manage resources and quotas for classic data governance - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/classic-how-to-manage-quotas
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the quotas and limits on resources for classic Microsoft Purview Data Governance and how to request quota increases.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: limits-and-quotas
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 664f3721-8faa-420e-b6cd-68505c46d8a2
document_version_independent_id: 664f3721-8faa-420e-b6cd-68505c46d8a2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/classic-how-to-manage-quotas.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/classic-how-to-manage-quotas
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/classic-how-to-manage-quotas.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: ae5cc1b1-0c0e-fbcd-e08e-c965776b2a54
---

# Manage resources and quotas for classic data governance - Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article highlights the limits that currently exist in the classic Microsoft Purview Data Governance service. These limits are also known as quotas.

Note

These are limits for the [classic data governance experience](../governance-solutions-overview).

## Classic Microsoft Purview Data Governance limits

| **Resource** | **Default limit** | **Maximum limit** |
| --- | --- | --- |
| Microsoft Purview accounts per region, per tenant (all subscriptions combined) | 3\* ([dependent](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-)) | Contact Support |
| Data Map throughputThere's no default limit on the Data Map metadata storage | 10 capacity units 250 operations per second | 100 capacity units 2,500 operations per second |
| vCores available for scanning, per account\*\* | 160 | 160 |
| Concurrent scans per Purview account. The limit is based on the type of data sources scanned\* | 5 | 10 |
| Maximum time that a scan can run for | 7 days | 7 days |
| Size of assets per account | 100M physical assets | Contact support |
| Maximum size of an asset in a catalog | 2 MB | 2 MB |
| Maximum length of an asset name and classification name | 4 KB | 4 KB |
| Maximum length of asset property name and value | 32 KB | 32 KB |
| Maximum length of classification attribute name and value | 32 KB | 32 KB |
| Maximum number of glossary terms, per glossary | 100K | 100K |
| Maximum number of self-service policies, per account | 3K | 3K |
| Maximum number of collections | 256 | 256 |
| Maximum ingestion of child objects and contacts | Doesn't apply | 20,000 entities |

\* Accounts limit is dependent on your organization. [For full information, see the FAQ.](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-)

\*\* Self-hosted integration runtime scenarios aren't included in the limits defined in the above table.

^ Increasing the Data Map throughput limit also increases the minimum number of capacity units with no usage. TO increase Data Map throughput, you can request a capacity until upgrade. See [Data Map throughput](../data-map) for more info about Data Map in general.

## Request quota increase

Use the following steps to create a new support request from the Azure portal to increase quota for Microsoft Purview. You can create a quota request for Microsoft Purview accounts in a subscription or tenant ([dependent on your organization](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-)), and the Data Map throughput (capacity units) of a specific account.

Caution

Once you have upgraded your Data Map throughput, you can't downgrade.

1. On the [Azure portal](https://portal.azure.com) menu, select **Help + support**.

    ![Screenshot showing how to navigate to help and support](../media/how-to-manage-quotas/help-plus-support.png)
2. In **Help + support**, select **New support request**.

    ![Screenshot showing how to create new support request](../media/how-to-manage-quotas/create-new-support-request.png)
3. For **Issue type**, select **Service and subscription limits (quotas)**.
4. For **Subscription**, select the subscription whose quota you want to increase.
5. For **Quota type**, select Microsoft Purview. Then select **Next**.

    ![Screenshot showing how to enter support information](../media/how-to-manage-quotas/enter-support-details.png)
6. In the **Details** window, select **Enter details** to enter additional information.
7. Choose your **Quota type**, scope (either location or account) and what you wish the new limit to be

    ![Screenshot showing how to enter quota amount for Microsoft Purview accounts per subscription](../media/how-to-manage-quotas/enter-quota-amount.png)
8. Enter the rest of the required support information. Review and create the support request