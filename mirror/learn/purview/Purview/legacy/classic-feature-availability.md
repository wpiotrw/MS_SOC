---
layout: Conceptual
title: Feature availability for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/classic-feature-availability
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Feature availability Microsoft Purview across sovereign clouds.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: references_regions, msecd-doc-authoring-1030
locale: en-us
document_id: 253d444e-a3bb-10d9-f488-0a790197309c
document_version_independent_id: 253d444e-a3bb-10d9-f488-0a790197309c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/classic-feature-availability.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/classic-feature-availability
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/classic-feature-availability.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: de65c90e-67b5-06f6-a013-141dee68af37
---

# Feature availability for Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Learn what which Microsoft Purview features are partially available or unavailable in Azure Government and Azure China 21Vianet regions.

In the list of global Azure regions, there are several regions that serve specific markets in addition to the public cloud regions. Microsoft Purview is deployed into the following regions.

- Azure China 21Vianet region: China North 3.
- Azure Government regions: US GOV Virginia

The information in the rest of this document provides information on the feature availability for Microsoft Purview. To see more detailed information about a feature's regional support, select the link to that feature.

## Azure China 21Vianet cloud

Feature support is represented by the following symbols:

| Symbol | Meaning | Description |
| --- | --- | --- |
| ❌ | Unsupported | Unsupported means that the feature isn't available in that particular region. |
| ✅ | Supported | Supported means that the feature is available in that particular region and in no way differs from the public cloud offering. |
| ⚠ | Partial support | Partial support indicates that the feature offered for the public cloud is available, but with perhaps some modifications. See the guidance and recommended sections for more information about partially supported features. |

| Feature | Subfeature | Public cloud status | CH-North-3 |
| --- | --- | --- | --- |
| [Microsoft Purview Data Map](../governance-solutions-overview#data-map) |  | GA | ⚠ |
|  | [Register and scan Azure Sources](../data-map-data-sources-register-manage) | GA | ✅ |
|  | [Register and scan on-premises Sources](../data-map-data-sources-register-manage) | GA | ✅ |
|  | [Register and scan multicloud sources](../data-map-data-sources-register-manage) | GA | ⚠ |
|  | [Metamodel](../concept-metamodel) | Public preview | ✅ |
| [Microsoft Purview Data Catalog](../governance-solutions-overview#classic-data-catalog) |  | GA | ⚠ |
|  | [Search and browse](../unified-catalog-data-assets-search) | GA | ✅ |
|  | [Bulk edit](../how-to-bulk-edit-assets) | GA | ✅ |
|  | [Asset Certification](../how-to-certify-assets) | GA | ✅ |
|  | [Managed attributes](how-to-managed-attributes) | Public preview | ❌ |
|  | [Business glossary](../how-to-create-manage-glossary) | GA | ✅ |
|  | [Lineage](../data-gov-classic-lineage-user-guide) | GA | ✅ |
|  | [Classifications](../data-map-classification-apply-auto) | GA | ✅ |
|  | [Labeling](../data-map-sensitivity-labels) | Public preview | ❌ |
|  | [Workflows](../concept-workflow) | Public preview | ✅ |
| [Data sharing](../concept-data-share) |  | Public preview | ❌ |
| [Microsoft Purview Data Estate Insights](../concept-insights) |  | GA | ⚠ |
| [Microsoft Purview Data Policies](../governance-solutions-overview#data-policy) |  | GA | ✅ |
|  | [DevOps policies](../concept-policies-devops) | GA | ✅ |
|  | [Self Service policies](../concept-self-service-data-access-policy) | Public preview | ✅ |
|  | [Data owner policies](../concept-policies-data-owner) | Public preview | ✅ |

### Azure China guidance and recommendations

#### Microsoft Purview Data Map

The Microsoft Purview Data Map is fully supported, except for some multicloud sources.

Sources that are **NOT** supported in Azure China are:

| Category | Source |
| --- | --- |
| Microsoft | [Azure Data Lake Store Gen 1](../register-scan-adls-gen1) |
|  | [Azure Machine Learning](../register-scan-azure-machine-learning) |
| Database | [Amazon RDS](../register-scan-amazon-rds) |
|  | [SQL Server on Azure-Arc](../register-scan-azure-arc-enabled-sql-server) |
| File | [Amazon S3](../register-scan-amazon-s3) |
| Services and apps | [Looker](../register-scan-looker-source) |

For lineage, [Azure Synapse Analytics pipeline lineage](../data-map-lineage-azure-synapse-analytics) is not supported.

#### Microsoft Purview Data Estate Insights

Data Estate Insights is fully available [except for sensitivity label insights](../unified-catalog-reports-classic-sensitivity-labels), as sensitivity labels aren't supported.

#### Microsoft Purview Workflows

Workflows are available in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include other legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

#### Microsoft Purview Data policies

Only policies for Azure SQL Database are currently supported.

## Azure Government

Feature support is represented by the following symbols:

| Symbol | Meaning | Description |
| --- | --- | --- |
| ❌ | Unsupported | Unsupported means that the feature isn't available in that particular region. |
| ✅ | Supported | Supported means that the feature is available in that particular region and in no way differs from the public cloud offering. |
| ⚠ | Partial support | Partial support indicates that the feature offered for the public cloud is available, but with perhaps some modifications. See the guidance and recommended sections for more information about partially supported features. |

| Feature | Subfeature | Public cloud status | US Gov Virginia |
| --- | --- | --- | --- |
| [Microsoft Purview Data Map](../governance-solutions-overview#data-map) |  | GA | ⚠ |
|  | [Register and scan Azure Sources](../data-map-data-sources-register-manage) | GA | ✅ |
|  | [Register and scan on-premises Sources](../data-map-data-sources-register-manage) | GA | ✅ |
|  | [Register and scan multicloud sources](../data-map-data-sources-register-manage) | GA | ⚠ |
|  | [Metamodel](../concept-metamodel) | Public preview | ✅ |
| [Microsoft Purview Data Catalog](../governance-solutions-overview#classic-data-catalog) |  | GA | ⚠ |
|  | [Search and browse](../unified-catalog-data-assets-search) | GA | ✅ |
|  | [Bulk edit](../how-to-bulk-edit-assets) | GA | ✅ |
|  | [Asset Certification](../how-to-certify-assets) | GA | ✅ |
|  | [Managed attributes](how-to-managed-attributes) | Public preview | ❌ |
|  | [Business glossary](../how-to-create-manage-glossary) | GA | ✅ |
|  | [Lineage](../data-gov-classic-lineage-user-guide) | GA | ✅ |
|  | [Classifications](../data-map-classification-apply-auto) | GA | ✅ |
|  | [Labeling](../data-map-sensitivity-labels) | Public preview | ❌ |
|  | [Workflows](../concept-workflow) | Public preview | ✅ |
| [Data sharing](../concept-data-share) |  | Public preview | ❌ |
| [Microsoft Purview Data Estate Insights](../concept-insights) |  | GA | ⚠ |
| [Microsoft Purview Data Policies](../governance-solutions-overview#data-policy) |  | GA | ✅ |
|  | [DevOps policies](../concept-policies-devops) | GA | ✅ |
|  | [Self Service policies](../concept-self-service-data-access-policy) | Public preview | ✅ |
|  | [Data owner policies](../concept-policies-data-owner) | Public preview | ✅ |

### Azure Government guidance and recommendations

#### Microsoft Purview Data Map

The Microsoft Purview Data Map is fully supported, except for some multicloud sources.

Sources that are **NOT** supported in Azure Government are:

| Category | Source |
| --- | --- |
| Microsoft | [Power BI](../register-scan-power-bi-tenant) (Though [Power BI GCC](/en-us/power-bi/enterprise/service-govus-overview)**is** supported.) |
| Database | [Amazon RDS](../register-scan-amazon-rds) |
| File | [Amazon S3](../register-scan-amazon-s3) |

Note

Any sources that are in preview are not supported. For lineage, [Azure Synapse Analytics pipeline lineage](../data-map-lineage-azure-synapse-analytics) is not supported.

#### Microsoft Purview Data Estate Insights

Data Estate Insights is fully available [except for sensitivity label insights](../unified-catalog-reports-classic-sensitivity-labels), as sensitivity labels aren't supported.

#### Microsoft Purview Workflows

Workflows are available in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include other legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

#### Microsoft Purview Data policies

Only policies for Azure SQL Database are currently supported.