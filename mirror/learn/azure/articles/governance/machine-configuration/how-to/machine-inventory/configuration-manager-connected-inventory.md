---
layout: Conceptual
title: Enable Microsoft Configuration Manager Connected Inventory - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/how-to/machine-inventory/configuration-manager-connected-inventory
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
description: Learn how to enable Connected Inventory for Microsoft Configuration Manager device collections and review their inventory in Azure.
ms.date: 2026-11-07T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: 30f55945-0726-2891-fd59-4b8a9d06fe14
document_version_independent_id: aa3e6be1-1a27-0375-0ea4-0955b8b70da5
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/how-to/machine-inventory/configuration-manager-connected-inventory.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/how-to/machine-inventory/configuration-manager-connected-inventory
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/how-to/machine-inventory/configuration-manager-connected-inventory.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4c50f262-d533-4ba4-9d4a-08899ec3a3d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/6a8c83be-f1de-4e90-bde0-bd097999a60c
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: c00dad4c-da72-0fe5-c0a2-d01d5c443ea4
---

# Enable Microsoft Configuration Manager Connected Inventory - Azure Machine Configuration | Microsoft Learn

Microsoft Configuration Manager Connected Inventory makes existing inventory from Configuration Manager-managed servers available in Azure. You select device collections in the Configuration Manager console and review their inventory through the Azure portal and Azure Resource Graph.

Connected Inventory creates read-only Azure representations of the selected servers. It uses inventory already collected by Configuration Manager and doesn't install agents on each managed server.

## Prerequisites

- A Configuration Manager site with managed servers and device collections.
- The Azure Arc connector configured for the site.
- The required Configuration Manager console extension installed.
- Access to the Azure tenant, subscription, resource group, and region configured for the connection.
- Permissions to configure the connection and view the resulting Azure resources.

## Enable Connected Inventory for a collection

1. Open the **Microsoft Configuration Manager console**.
2. Expand **Cloud Services**, and select **Azure Arc Devices**.
3. Select **Arc Connected Device** to open the **Azure Arc setup** wizard.
4. On **Connected Inventory**, verify the site and the **Connected to Azure Arc** destination information, and then select **Next**.
5. On **Choose collections**, select the device collection whose inventory you want to publish, and then select **Next**.
6. On **Review**, verify the Azure destination and the collection changes, and then select **Apply**.
7. Wait for **Apply changes** to complete, and review **Results**.
8. Return to **Azure Arc Devices** and verify that the selected machines show **Enabled** in **Connected Inventory**.

## Review inventory in Azure

1. In the Azure portal, open the relevant Azure Arc **On-premises connector**.
2. Open **Devices**, and select a synchronized server.
3. Open **machine inventory (preview)**.
4. Review the available inventory for that server.

Inventory refreshes daily and can take up to 24 hours to appear after enablement.

## Query device-collection membership

In **Resource Graph Explorer**, select the subscription containing the synchronized servers and run the following query. Replace `<subscription-id>` with your subscription ID.

```kusto
guestconfigurationresources
| where subscriptionId == '<subscription-id>'
| where type =~ 'microsoft.guestconfiguration/devicecollections'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, deviceCollection = name,
    properties, resourceGroup, subscriptionId
| order by machineResourceId asc, deviceCollection asc
```

Use the results to verify that collection membership records are available for synchronized machines.

## Troubleshoot Connected Inventory

| Symptom | What to check |
| --- | --- |
| Machines remain disabled | Confirm that you selected the correct collection. Review the wizard's Results page for validation or synchronization errors. |
| Devices don't appear in Azure | Verify the Azure destination, selected subscription, and portal filters. Allow up to 24 hours after enablement. |
| A category is empty or data appears stale | Verify that Configuration Manager collected the expected inventory and that synchronization is functioning. Check whether the category is supported for this collection path. |
| Collection membership is missing | Query `microsoft.guestconfiguration/devicecollections` in the destination subscription and compare the results with the selected collection. |