---
layout: Conceptual
title: Manage VM Applications on Arc-enabled servers (preview) - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/manage-vm-app-on-arc
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to manage VM Applications on Azure Arc-enabled servers.
ms.date: 2026-10-26T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-generated
locale: en-us
document_id: 19e3a607-a560-e42d-f841-a4ce1e13192a
document_version_independent_id: b906f6c1-9324-d5b4-2c5c-9c5e645f957f
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/manage-vm-app-on-arc.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/manage-vm-app-on-arc
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/manage-vm-app-on-arc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3928677-9b71-43a6-875f-004dc4f98b65
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6bbc70ca-58b2-4c69-8249-28ec92c08029
platformId: a6b84561-1fed-0ce7-b0b1-60d5f3f63a92
---

# Manage VM Applications on Arc-enabled servers (preview) - Azure Arc | Microsoft Learn

Manage your VM Applications throughout their lifecycle, from published versions in Azure Compute Gallery to applications deployed to your Arc-enabled servers. This article explains how to manage gallery resources, how to view deployment status, review logs, update application versions, and remove deployed applications.

## Manage VM applications published in Azure Compute Gallery

Azure Compute Gallery stores your VM Application definitions and versions. Each version references an application package and the commands used to install, update, and remove it. Managing these published resources is separate from managing the applications deployed to your Arc-enabled servers.

Use the following guidance to manage your gallery resources:

- **View applications and versions.** Review application definitions, available versions, and publishing details. See [View published VM Applications](/en-us/azure/virtual-machines/vm-applications-manage#view-published-vm-applications).
- **Query applications across galleries.** Use Azure Resource Graph to inventory published applications and versions across your subscriptions. See [View published VM applications using Azure Resource Graph](/en-us/azure/virtual-machines/vm-applications-manage#view-published-vm-applications-using-azure-resource-graph).
- **Update published resources.** Change supported properties of an application or version. Not all properties can be updated. See [Update published VM Application](/en-us/azure/virtual-machines/vm-applications-manage#update-published-vm-application).
- **Delete applications and versions.** Delete all versions before deleting an application definition. Deleting a version removes its gallery replicas but doesn't delete the source application blob in your storage account. See [Delete published VM Application from Azure Compute Gallery](/en-us/azure/virtual-machines/vm-applications-manage#delete-published-vm-application-from-azure-compute-gallery).

## Manage VM applications deployed to Azure Arc-enabled servers

Refer to the following sections to manage VM Applications deployed to your Arc-enabled servers, including viewing installed applications, monitoring their status, updating versions, and removing applications.

### View deployed VM applications and their state

Retrieve details for a specific application or list all deployed applications on an Arc-enabled server.

#### Get details of a single application

Use one of the following methods to view a specific VM Application deployed to your Arc-enabled server.

# [Azure portal](#tab/view-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. Find your application in the list to review its version, install order, gallery, and provisioning state.

# [Azure CLI](#tab/view-azure-cli)
```azurecli
az connectedmachine application get-instance-view \
  --name "{application-resource-name}" \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}"
```

# [REST](#tab/view-rest)
```rest
GET 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications/{application-resource-name}/instanceView?api-version=2026-09-01
```

# [Azure Resource Graph](#tab/view-arg)
```kusto
resources
| where type =~ "microsoft.hybridcompute/machines/applications"
| where resourceGroup =~ "{resource-group}"
| extend machineName = tostring(split(id, "/")[8])
| where machineName =~ "{arc-machine-name}" and name =~ "{application-resource-name}"
| project subscriptionId, resourceGroup, location, machineName,
          applicationName = name,
          provisioningState = tostring(properties.provisioningState),
          packageReferenceId = tostring(properties.packageReferenceId),
          id
```

Note

Azure Resource Graph doesn't provide an instance view. To retrieve an instance view, use Azure CLI or REST.

---

#### List all applications on your Arc-enabled server

Use one of the following methods to view all VM applications deployed to an Arc-enabled server.

# [Azure portal](#tab/list-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. Review the list of deployed applications.

# [Azure CLI](#tab/list-azure-cli)
```azurecli
az connectedmachine application list \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}"
```

To retrieve instance view for a listed application, use `az connectedmachine application get-instance-view` with its name, as shown in Get details of a single application.

# [REST](#tab/list-rest)
```rest
GET 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications?api-version=2026-09-01
```

To retrieve the instance view for a listed application, use its `/instanceView` endpoint, as shown in Get details of a single application.

# [Azure Resource Graph](#tab/list-arg)
```kusto
resources
| where type =~ "microsoft.hybridcompute/machines/applications"
| where resourceGroup =~ "{resource-group}"
| extend machineName = tostring(split(id, "/")[8])
| where machineName =~ "{arc-machine-name}"
| project subscriptionId, resourceGroup, location, machineName,
          applicationName = name,
          provisioningState = tostring(properties.provisioningState),
          packageReferenceId = tostring(properties.packageReferenceId),
          id
```

Note

Azure Resource Graph doesn't provide an instance view. To retrieve an instance view, use Azure CLI or REST.

---

### Update a deployed VM application

Update a deployed VM application on your Arc-enabled server to a newer version by using one of the following methods.

Before you begin, [create a new application version in Azure Compute Gallery](/en-us/azure/virtual-machines/vm-applications-how-to#create-the-vm-application) and replicate it to the region where your Arc-enabled server is connected.

# [Azure portal](#tab/update-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. Confirm that the **Update available** column shows an update for your application.
5. Select the application's checkbox, and then on the toolbar, select **Manual update**.

# [Azure CLI](#tab/update-azure-cli)
```azurecli
az connectedmachine application update \
  --name "{application-resource-name}" \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}" \
  --package-reference-id "{package-reference-id}"
```

# [REST](#tab/update-rest)
```rest
PATCH 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications/{application-resource-name}?api-version=2026-09-01
Content-Type: application/json

{
  "properties": {
    "packageReferenceId": "/subscriptions/{subscription-id}/resourceGroups/{gallery-resource-group}/providers/Microsoft.Compute/galleries/{gallery-name}/applications/{application-name}/versions/{version}",
    "order": {order},
    "treatFailureAsDeploymentFailure": false
  }
}
```

---

### Remove a deployed VM application

Remove a deployed VM Application from your Arc-enabled server by using one of the following methods.

# [Azure portal](#tab/remove-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. Select the checkbox for the application you want to remove.
5. On the toolbar, select **Delete**, and then confirm the deletion.

# [Azure CLI](#tab/remove-azure-cli)
```azurecli
az connectedmachine application delete \
  --name "{application-resource-name}" \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}"
```

# [REST](#tab/remove-rest)
```rest
DELETE 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications/{application-resource-name}?api-version=2026-09-01
```

---