---
layout: Conceptual
title: Cost Management dataset schema index - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/dataset-schema/schema-index
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/748a4eaa-0e25-ec11-b6e6-000d3a4f07b8
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn about the dataset schemas available in Cost Management.
author: vikramdesai01
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: common
ms.topic: reference
ms.date: 2026-11-16T00:00:00.0000000Z
ms.author: vikdesai
locale: en-us
document_id: d67b4b0e-eb11-d96a-de92-75b50402ffc5
document_version_independent_id: 9d63fbee-9db8-c4cb-d54f-0612771c0de4
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/dataset-schema/schema-index.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../costs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/dataset-schema/schema-index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/dataset-schema/schema-index.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: dee558a4-9153-1bdf-dfbd-dc68a357cc99
---

# Cost Management dataset schema index - Microsoft Cost Management | Microsoft Learn

This article lists all dataset schemas available in Microsoft Cost Management. The schema files list and describe all of the data fields found in various data files.

## Dataset schema files

The following sections list of all dataset schema files available in Cost Management. The dataset name is the name of the file that contains the data. The contract is the agreement type of Azure subscription that the data is associated with. The dataset version is the version of the dataset schema. The mapped API version is the version of the API that the dataset schema maps to.

The latest version of each dataset is based on the agreement type and scope, where applicable. It includes:

- Enterprise Agreement (EA)
- Microsoft Customer Agreement (MCA)
- Microsoft Partner Agreement (MPA)
- Cloud Solution Provider (CSP)
- Microsoft Online Services Agreement (MOSA), also known as pay-as-you-go

For for more information about each agreement type and what's included, see [Supported Microsoft Azure offers](../costs/understand-cost-mgt-data#supported-microsoft-azure-offers).

## Latest dataset schema files

Note

Exports let you select a dataset version, and the 2026-10-01 versions are available only in exports. Usage files and price sheets that you download from the Azure portal, or by using the download APIs, don't use version 2026-10-01. Instead, the new `priceFactors` and `supplementalChargeDetails` columns are added at the end of the file. For more information, see [Understand price factors and supplemental charge details](../automate/understand-price-factors-supplemental-charge-details).

| Dataset | Contract | Dataset version |
| --- | --- | --- |
| Cost and usage details | Enterprise Agreement (EA) | [2026-10-01](cost-usage-details-ea) |
| Cost and usage details | Microsoft Customer Agreement (MCA) | [2026-10-01](cost-usage-details-mca) |
| Cost and usage details | Microsoft Partner Agreement (MPA) | [2026-10-01](cost-usage-details-mca-partner) |
| Cost and usage details | Cloud Service Provider (CSP) subscription | [2026-10-01](cost-usage-details-mca-partner-subscription) |
| Cost and usage details | Pay-as-you-go (MOSA) | [2019-11-01](cost-usage-details-pay-as-you-go) |
| Cost and usage details (FOCUS) | EA and MCA | [1.2-preview](cost-usage-details-focus) |
| Price sheet | EA | [2026-10-01](price-sheet-ea) |
| Price sheet | MCA | [2026-10-01](price-sheet-mca) |
| Reservation details | EA | [2023-03-01](reservation-details-ea) |
| Reservation details | MCA | [2023-03-01](reservation-details-mca) |
| Reservation recommendations | EA | [2023-05-01](reservation-recommendations-ea) |
| Reservation recommendations | MCA | [2023-05-01](reservation-recommendations-mca) |
| Reservation transactions | EA | [2023-05-01](reservation-transactions-ea) |
| Reservation transactions | MCA | [2023-05-01](reservation-transactions-mca) |

## Older versions of dataset schema files

| Dataset | Contract | Returned byAPI Versions | Dataset version |
| --- | --- | --- | --- |
| Cost and usage details | EA | 2023-12-01-preview | [2023-12-01-preview](cost-usage-details-ea#version-2023-12-01-preview) |
| Cost and usage details | MCA | 2023-12-01-preview | [2023-12-01-preview](cost-usage-details-mca#version-2023-12-01-preview) |
| Cost and usage details | EA | 2021-01-012021-04-01-preview2021-05-01 | [2021-01-01](cost-usage-details-ea#version-2021-01-01) |
| Cost and usage details | Cloud Service Provider (CSP) subscription | 2023-12-01-preview | [2023-12-01-preview](cost-usage-details-mca-partner-subscription#version-2023-12-01-preview) |
| Cost and usage details | Microsoft Partner Agreement (MPA) | 2023-12-01-preview | [2023-12-01-preview](cost-usage-details-mca-partner#version-2023-12-01-preview) |
| Cost and usage details | MCA | 2021-01-012021-04-01-preview2021-05-012020-05-01-preview | [2021-01-01](cost-usage-details-mca#version-2021-01-01) |
| Cost and usage details | EA | 2020-01-012020-08-01-preview2020-12-01-preview | [2020-01-01](cost-usage-details-ea#version-2020-01-01) |
| Cost and usage details | Cloud Service Provider (CSP) subscription | 2021-01-012021-04-01-preview2021-05-012020-05-01-preview | [2021-01-01](cost-usage-details-mca-partner-subscription#version-2021-01-01) |
| Cost and usage details | Microsoft Partner Agreement (MPA) | 2021-01-012021-04-01-preview2021-05-012020-05-01-preview | [2021-01-01](cost-usage-details-mca-partner#version-2021-01-01) |
| Cost and usage details | MCA | 2019-11-01 | [2019-11-01](cost-usage-details-mca#version-2019-11-01) |
| Cost and usage details | EA | 2018-05-312018-06-302018-08-312018-10-01-preview2019-01-01-preview2018-10-012018-07-312018-08-312018-08-01-preview2018-11-01-preview2018-12-01-preview2019-01-01-preview2019-01-012019-03-01-preview2019-04-01-preview2019-05-01-preview2019-05-012018-08-01-preview2019-10-012019-11-01 | [2019-10-01](cost-usage-details-ea#version-2019-10-01) |
| Cost and usage details | Cloud Service Provider (CSP) subscription | 2018-05-312018-06-302018-08-312018-10-01-preview2019-01-01-preview2018-10-012018-07-312018-08-312018-08-01-preview2018-11-01-preview2018-12-01-preview2019-01-01-preview2019-01-012019-03-01-preview2019-04-01-preview2019-05-01-preview2019-05-012018-08-01-preview2019-11-01 | [2019-11-01](cost-usage-details-mca-partner-subscription#version-2019-11-01) |
| Cost and usage details | Microsoft Partner Agreement (MPA) | 2018-05-312018-06-302018-08-312018-10-01-preview2019-01-01-preview2018-10-012018-07-312018-08-312018-08-01-preview2018-11-01-preview2018-12-01-preview2019-01-01-preview2019-01-012019-03-01-preview2019-04-01-preview2019-05-01-preview2019-05-012019-10-012018-08-01-preview2019-11-01 | [2019-11-01](cost-usage-details-mca-partner#version-2019-11-01) |
| Cost and usage details | MCA | 2018-05-312018-06-302018-08-312018-10-01-preview2019-01-01-preview2018-10-012018-07-312018-08-312018-08-01-preview2018-11-01-preview2018-12-01-preview2019-01-01-preview2019-01-012019-03-01-preview2019-04-01-preview2019-05-01-preview2019-05-012019-10-012018-08-01-preview | [2019-10-01](cost-usage-details-mca#version-2019-10-01) |