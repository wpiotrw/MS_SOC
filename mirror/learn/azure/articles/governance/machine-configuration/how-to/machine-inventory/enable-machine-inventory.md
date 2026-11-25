---
layout: Conceptual
title: Enable Machine Inventory - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/how-to/machine-inventory/enable-machine-inventory
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
description: Learn how to assign built-in Azure policies to enable machine inventory on Windows and Linux Azure VMs and Arc-enabled servers.
ms.date: 2026-11-07T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: 9d4470ce-187e-51e5-36e3-269a914a428e
document_version_independent_id: 9843126b-2177-1744-bfaf-f647320719ae
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/how-to/machine-inventory/enable-machine-inventory.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/how-to/machine-inventory/enable-machine-inventory
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/how-to/machine-inventory/enable-machine-inventory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
platformId: b583a488-be4a-cdb7-f2eb-1760bb40428e
---

# Enable Machine Inventory - Azure Machine Configuration | Microsoft Learn

Use built-in Azure policies to enable machine inventory on Windows and Linux Azure virtual machines (VMs) and Azure Arc-enabled servers. After collection starts, you can review inventory in the Azure portal and query it by using Azure Resource Graph.

This article describes how to enable inventory on Azure or Arc-enabled machines. For servers managed through Microsoft Configuration Manager, see [Enable Configuration Manager Connected Inventory](configuration-manager-connected-inventory).

## Prerequisites

- An Azure subscription and a resource group containing the machines you want to inventory.
- Windows or Linux Azure VMs, or servers connected to Azure through Azure Arc.
- The applicable [Machine Configuration prerequisites](../../overview/02-setup-prerequisites).
- Permissions to assign the required Azure policies at the target scope and view the machines and their inventory.

## Assign the prerequisite initiative

For Azure VMs, assign the prerequisite initiative before enabling inventory.

1. In the Azure portal, open the **Machine Configuration** page. Search for this page by using the search bar.
2. In the table of contents, under **Solutions**, select **Policy**.
3. Open **Definitions** and find **Deploy prerequisites to enable Guest Configuration policies on virtual machines**.
4. Assign the initiative to the scope containing your target VMs.
5. Review the assignment and create it.
6. Verify that prerequisite deployment succeeds on the target VMs.

[![Screenshot of the prerequisite policy initiative for enabling Guest Configuration on virtual machines.](machine-inventory-prerequisites.png)](machine-inventory-prerequisites.png#lightbox)

## Assign the inventory policies

Assign the policy that matches the operating system of your target machines. For a resource group containing both Windows and Linux machines, assign both policies.

| Operating system | Built-in policy |
| --- | --- |
| Windows | **[Preview]: Windows machines should have Azure inventory enabled** |
| Linux | **[Preview]: Linux machines should have Azure inventory enabled** |

[![Screenshot of the Windows and Linux policies for enabling machine inventory.](machine-inventory-policies.png)](machine-inventory-policies.png#lightbox)

1. In the Azure portal, open the **Machine Configuration** page. Search for this page by using the search bar.
2. In the table of contents, under **Solutions**, select **Policy**. Use the search bar to find the applicable policy for your machine.
3. Select **Assign**.
4. Select the resource group containing your target machines and enter an assignment name.
5. For Azure Arc-enabled servers, set the `IncludeArcMachines` parameter to the lowercase string `"true"` where offered.
6. Review the assignment and create it. It takes 5-15 minutes for Azure to apply these changes.
7. Repeat for the other operating system, if needed.

## Troubleshoot missing inventory

| Symptom | What to check |
| --- | --- |
| No machines appear | Confirm the selected subscription and resource-group filters, and verify that the target machines are within the policy assignment scope. |
| A machine has no inventory records | Check prerequisite deployment, the applicable inventory policy assignment, and Machine Configuration health. Allow collection and reporting to complete. |
| An expected category is empty | Confirm that the category is available for that operating system. Query the corresponding resource type in Azure Resource Graph. |
| Policy deployment fails | Review assignment and deployment errors, including any identity or authorization errors, before troubleshooting inventory presentation. |

An empty result isn't evidence that a machine has no installed software or other guest resources.