---
layout: Conceptual
title: Pricing guidelines for classic Microsoft Purview data governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-pricing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-07-09T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand pricing for the classic data governance components of Microsoft Purview (formerly Azure Purview) in the classic governance portal.
locale: en-us
document_id: 62623200-fd9c-eb7b-59c2-2549d8e690f7
document_version_independent_id: 62623200-fd9c-eb7b-59c2-2549d8e690f7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-pricing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-pricing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-pricing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: c944e12e-fdf5-79df-21e1-97cf9e845f69
---

# Pricing guidelines for classic Microsoft Purview data governance | Microsoft Learn

Classic data governance solutions in Microsoft Purview in the classic governance portal provided a single pane of glass for managing data governance by enabling automated scanning and classifying data.

Tip

For specific price details for governance in the classic portal, see the [Microsoft Purview (formerly Azure Purview) pricing page](https://azure.microsoft.com/pricing/details/purview/). This article will guide you through the features and factors that will affect pricing.

## Why do you need to understand the components of pricing?

- While the pricing for classic data governance solutions in Microsoft Purview is on a subscription-based **Pay-As-You-Go** model, there are various dimensions that you can consider while budgeting
- This guideline is intended to help you plan the budgeting for classic data governance solutions by providing a view on the control factors that impact the budget

## Factors impacting Azure Pricing

There are **direct** and **indirect** costs that need to be considered while planning budgeting and cost management.

Direct costs impacting Microsoft Purview pricing are based on these applications:

- [The Microsoft Purview Data Map](data-gov-classic-pricing-data-map)
- [Data Estate Insights](concept-guidelines-pricing-data-estate-insights)

## Indirect costs

Indirect costs impacting classic data governance solutions in Microsoft Purview pricing are:

- [Managed resources](https://azure.microsoft.com/pricing/details/azure-purview/)

    - An Event Hubs namespace can be [configured at creation](create-microsoft-purview-portal#create-an-account) or enabled in the [Azure portal](https://portal.azure.com) on the Kafka configuration page of the account to enable monitoring with [*Atlas Kafka* topics events](data-map-kafta-send-receive-events). [The Event Hubs will be charged separately](https://azure.microsoft.com/pricing/details/event-hubs/).
- [Azure private endpoint](data-gov-classic-private-link)

    - Azure private end points are used for classic data governance solutions in Microsoft Purview, where it's required for users on a virtual network (virtual network) to securely access the catalog over a private link
    - The [prerequisites](data-gov-classic-private-link#prerequisites) for setting up private endpoints could result in extra costs, for example, [costs if you deploy a virtual network](https://azure.microsoft.com/pricing/details/virtual-network/).
- [Self-hosted integration runtime related costs](data-map-integration-runtime-self-hosted)

    - Self-hosted integration runtime requires infrastructure, which results in extra costs
    - It's required to deploy and register Self-hosted integration runtime (SHIR) inside the same virtual network where Microsoft Purview ingestion private endpoints are deployed
    - [Other memory requirements for scanning](register-scan-sapecc-source#create-and-run-scan)
        - Certain data sources such as SAP require more memory on the SHIR machine for scanning
- [Virtual Machine Sizing](/en-us/azure/virtual-machines/sizes)

    - Plan virtual machine sizing in order to distribute the scanning workload across VMs to optimize the v-cores utilized while running scans
- [Microsoft 365 license](data-map-sensitivity-labels)

    - Microsoft Purview Information Protection sensitivity labels can be automatically applied to your Azure assets in the Microsoft Purview Data Map.
    - Microsoft Purview Information Protection sensitivity labels are created and managed in the Microsoft Purview portal.
    - To create sensitivity labels for use in Microsoft Purview, you must have an active Microsoft 365 license, which offers the benefit of automatic labeling. For the full list of licenses, see the Sensitivity labels in Microsoft Purview FAQ.
- [Azure Alerts](/en-us/azure/azure-monitor/alerts/alerts-overview)

    - Azure Alerts can notify customers of issues found with infrastructure or applications using the monitoring data in Azure Monitor
    - The pricing for Azure Alerts is available [here](https://azure.microsoft.com/pricing/details/monitor/)
- [Cost Management Budgets & Alerts](/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending)

    - Automatically generated cost alerts are used in Azure to monitor Azure usage and spending based on when Azure resources are consumed
    - Azure allows you to create and manage Azure budgets. Refer [tutorial](/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- Multicloud egress charges

    - Consider the egress charges (minimal charges added as a part of the multicloud subscription) associated with scanning multicloud (for example AWS, Google) data sources running native services excepting the S3 and RDS sources