---
layout: FAQ
title: Microsoft Purview Data Governance Billing FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-billing-faq
summary: >
  <div class="IMPORTANT">

  <p>Important</p>

  <p>Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the <a href="https://aka.ms/DG-Deprecation">Microsoft Purview data governance retirement announcement</a>.</p>

  </div>
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
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
search.appverid:
- MOE150
- MET150
description: Find answers to frequently asked questions about billing for Microsoft Purview data governance solutions, including Unified Catalog.
locale: en-us
document_id: d84ea5b5-57db-40e7-dfe9-a02bbe6e52d7
document_version_independent_id: d84ea5b5-57db-40e7-dfe9-a02bbe6e52d7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-billing-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-billing-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-billing-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 55bb7d09-e88a-a5dc-c002-9560e9058aa9
---

# Microsoft Purview Data Governance Billing FAQ | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

## When did the new pricing model go into effect?

The new pricing model took effect on January 6, 2025.

## Is the asset counting done at a monthly level or daily level?

Assets are counted on a daily basis. Each day, unique governed assets are counted. If you ungovern any assets mid-month, the right asset count is picked for the day and multiplied by unique governed assets per day.

## I have a single data product with three data assets attached. Am I charged for each data asset for 30 days?

Yes. When attaching three data assets to a data product, you're charged for each data asset each day.

## I have the same data asset attached to both a data product and a critical data element. How am I charged?

You aren't charged for a data asset attached to both a data product and a critical data element. You're charged for a data asset once.

## How am I charged if I scanned 10 data assets and only three are attached to data products?

You're charged for the three data assets attached to the data product. You aren't charged for the remaining seven data assets in Data Map.

## If I use the classic glossary in Data Map and attach classic glossary terms to a data asset, am I charged?

No. Assets with classic glossary terms attached to them aren't charged.

## If I attach a SQL server with 200 tables in it to a data product, how many governed assets am I charged for?

You're charged for a single asset as governed asset for a SQL server with many tables. Children won't be counted since the intent is to govern the server as a whole. We recommend putting an individual table or a selected group of tables in a data product, so the experience is more curated and meaningful. If the data product is data consumer facing, then limited data consumers would want access to a data product with 200 tables.

## If I attach a Power BI semantic model into a data product that has 200 tables, and then I intentionally hand-pick 10 tables to be part of the data product, how many assets do I get charged for?

If the semantic model is still attached to the data product, we charge it as a single asset. If you have picked five tables to be attached to the data product, removing the semantic model we charge for the five tables only.

## Can I run data quality rules on a database or its individual tables and columns?

Data quality runs are set on columns of tables. Running data quality on a data asset's columns or tables turns that data asset into a governed asset.

## What type of billing transparency will I be able to see?

[Usage monitoring (preview) in Unified Catalog settings](data-governance-admin-experience#usage-monitoring-preview) provides Data Governance Administrators with a view of governed assets and data governance processing unit (DGPU) consumption across governance domains. Based on the processing units, you can decide if you're over-using, under-using, or if there are opportunities to optimize data quality rules. You can also charge back costs to the different governance domains using the consumption details.

## Are there tools and guidance to help estimate costs with new pricing model?

Yes. You can find complete pricing information and a pricing calculator on the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

## Is there a volume discount?

No, but based on usage at scale, we can work on volume-based pricing for future releases.

## What cost reporting will be available, and where can I view this?

Costs can be viewed from January 6, 2025, in the Cost management section of the subscription tied to your Microsoft Purview tenant (in the Microsoft Purview portal, go to **Settings** &gt; **Account** &gt; **Account overview**). Data Governance Admininisrators can also view the [usage monitoring (preview)](data-governance-admin-experience#usage-monitoring-preview) report.

## What meters are zeroed out from classic to Microsoft Purview Unified Catalog?

The following meters are zeroed out from classic to Microsoft Purview Unified Catalog in the following areas:

- Data Map population - Scanning including SHIR
- Data Map enrichment - Insights Generation, Data Map capacity units
- Data Map consumption - including insights consumption

## Does the advanced resource set meter zero out for me?

The advanced resource set isn't offered as part of Microsoft Purview, so the meter is ineffective.