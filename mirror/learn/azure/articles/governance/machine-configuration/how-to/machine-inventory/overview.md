---
layout: Conceptual
title: Machine Inventory overview - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/how-to/machine-inventory/overview
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: mgreenegit
learn_banner_products:
- azure
ms.author: migreene
ms.service: azure-machine-configuration
description: Learn how machine inventory provides visibility into software, services, certificates, accounts, and server roles across your machines.
ms.date: 2026-11-07T00:00:00.0000000Z
ms.topic: overview
locale: en-us
document_id: dc04d8a8-dd23-32b9-5a45-aeaab9950f11
document_version_independent_id: 35551ed6-8973-71c9-21b1-febc87a7b659
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/how-to/machine-inventory/overview.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/how-to/machine-inventory/overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/how-to/machine-inventory/overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4c50f262-d533-4ba4-9d4a-08899ec3a3d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/6a8c83be-f1de-4e90-bde0-bd097999a60c
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 754caef4-40bf-5879-ec58-ef43ddeb3d9c
---

# Machine Inventory overview - Azure Machine Configuration | Microsoft Learn

The machine inventory feature provides read-only visibility into guest-level resources on your machines. Use it to review installed software, inspect services, identify expiring certificates, and understand local users and group membership. You can browse inventory in the Azure portal or query it across machines by using Azure Resource Graph.

The machine inventory feature supports inventory collected from Windows and Linux Azure virtual machines (VMs) and Azure Arc-enabled servers. Microsoft Configuration Manager Connected Inventory provides a separate collection path for servers managed through Configuration Manager.

Choose the collection path that matches how you manage your machines.

| Collection path | How data reaches Azure | Get started |
| --- | --- | --- |
| Agent-based inventory | Azure Policy enables inventory collection through Machine Configuration on Azure VMs and Arc-enabled servers. Collected inventory is available in Azure Resource Graph. | [Enable machine inventory](enable-machine-inventory) |
| Configuration Manager Connected Inventory | An Azure Arc connector publishes existing Configuration Manager inventory for selected device collections. This path doesn't install the Azure Connected Machine agent on each managed server. | [Enable Connected Inventory](configuration-manager-connected-inventory) |

## Prerequisites

Before you begin, ensure you have:

- An Azure subscription and a resource group for the machines or synchronized server resources.
- Permissions to view the machines and their inventory in the Azure scope you want to explore.
- The prerequisites for your collection path:

| Collection path | Required setup |
| --- | --- |
| Agent-based inventory | Windows or Linux Azure VMs, or servers connected through Azure Arc; the applicable [Machine Configuration prerequisites](../../overview/02-setup-prerequisites); and permissions to assign Azure policies at the target scope. For Azure VMs, assign the prerequisite initiative described in [Enable machine inventory](enable-machine-inventory) before assigning inventory policies. |
| Configuration Manager Connected Inventory | A Configuration Manager site with managed servers and device collections, a configured Azure Arc connector, the required Configuration Manager console extension, and permissions to configure the connection and access its Azure destination. See [Connected Inventory prerequisites](configuration-manager-connected-inventory#prerequisites). |

## Getting started

1. **Choose and enable a collection path.** For Azure VMs and Azure Arc-enabled servers, follow [Enable machine inventory](enable-machine-inventory) to assign the prerequisites and the inventory policies that match your machines' operating systems. For servers managed through Configuration Manager, follow [Enable Configuration Manager Connected Inventory](configuration-manager-connected-inventory) to select the device collections to publish to Azure.
2. **Verify that inventory is available.** For agent-based inventory, check the policy assignments and Machine Configuration health, and then open **machine inventory (preview)** in the Azure portal and select the target subscription and resource group. For Connected Inventory, open a synchronized server from the connector's **Devices** page and select **machine inventory (preview)**. Connected Inventory can take up to 24 hours to appear after enablement.
3. **Explore your inventory.** Review a category available for your machines, such as applications or certificates on Windows, and use filters to narrow the results. To browse records or run Azure Resource Graph queries across machines, see [View and query machine inventory](view-and-query-machine-inventory).

## Inventory categories

You can view the following inventory resource types in the `guestconfigurationresources` table in Azure Resource Graph.

| Platform | Inventory category | Resource type |
| --- | --- | --- |
| Windows | Applications | `microsoft.guestconfiguration/applications` |
| Windows | Services | `microsoft.guestconfiguration/services` |
| Windows | Users | `microsoft.guestconfiguration/users` |
| Windows | Groups | `microsoft.guestconfiguration/groups` |
| Windows | Certificates | `microsoft.guestconfiguration/certificates` |
| Windows | Windows Server roles | `microsoft.guestconfiguration/windowsroles` |
| Linux | Daemons | `microsoft.guestconfiguration/daemons` |
| Linux | Software | `microsoft.guestconfiguration/softwares` |

Configuration Manager Connected Inventory also exposes device-collection membership as `microsoft.guestconfiguration/devicecollections`.

## Considerations

- Inventory is a read-only view. Reviewing an application, account, certificate, or service doesn't change its configuration.
- Inventory availability and category coverage depend on the machine's platform and collection path.
- Configuration Manager Connected Inventory refreshes daily, and inventory can take up to 24 hours to appear after enablement.