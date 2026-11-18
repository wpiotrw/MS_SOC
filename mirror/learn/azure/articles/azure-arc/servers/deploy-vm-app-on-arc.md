---
layout: Conceptual
title: Deploy VM applications on Arc-enabled servers (preview) - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/deploy-vm-app-on-arc
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
description: Learn how to deploy VM Applications on Azure Arc-enabled servers.
ms.date: 2026-10-24T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-generated
locale: en-us
document_id: b6386de8-61b5-79ff-d60a-f61a3428068d
document_version_independent_id: d1ec7afd-6776-55c2-89cc-9f4a32b3df1f
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/deploy-vm-app-on-arc.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/deploy-vm-app-on-arc
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/deploy-vm-app-on-arc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: d69b9026-1a48-97e6-80db-3f38f9f6b6da
---

# Deploy VM applications on Arc-enabled servers (preview) - Azure Arc | Microsoft Learn

VM Applications let you deploy versioned application packages from Azure Compute Gallery to your Azure Arc-enabled servers. This article guides you through the deployment process.

Before you begin, [prepare and publish your VM Application](overview-vm-app-on-arc#prepare-and-create-a-vm-application). The preparation and publishing process is the same for Azure VMs and Arc-enabled servers.

## Prerequisites

Before deploying your VM Application to your Azure Arc-enabled server, ensure you have the following prerequisites:

- Ensure the server is Arc-enabled and not expired. For more information, see [Azure Arc-enabled servers overview](overview).
- Ensure the Azure Connected Machine agent is on version 1.69 or later. For more information, see [Manage and maintain the Connected Machine agent](manage-agent).
- For Azure Arc-enabled Linux servers, ensure OpenSSL version 1.1.1 or later is installed.
- Add `*.blob.core.windows.net` to your allow list. For more information, see [Azure Arc network requirements](network-requirements?tabs=azure-cloud#urls).
- Ensure the VM application is replicated to the region to which the Azure Arc-enabled server is connected. For more information, see [Create the VM Application](/en-us/azure/virtual-machines/vm-applications-how-to#create-the-vm-application).

## Get the package reference ID

The deployment references a specific gallery application version. Find its resource ID by using the Azure portal, Azure CLI, or PowerShell.

# [Azure portal](#tab/get-id-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Compute Galleries**.
2. Open the gallery that contains your VM Application.
3. On the gallery's **Overview** page, under **Definitions**, select your VM Application.
4. Select the version you want to deploy.
5. On the version's **Overview** page, select **JSON View** and copy the **Resource ID**. Copy the version's resource ID.

# [Azure CLI](#tab/get-id-cli)
```azurecli
az sig gallery-application version show \
  --subscription "{subscription-id}" \
  --resource-group "{gallery-resource-group}" \
  --gallery-name "{gallery-name}" \
  --application-name "{application-name}" \
  --version-name "{version}" \
  --query id \
  --output tsv
```

# [PowerShell](#tab/get-id-powershell)
```powershell
Get-AzGalleryApplicationVersion `
  -ResourceGroupName "{gallery-resource-group}" `
  -GalleryName "{gallery-name}" `
  -GalleryApplicationName "{application-name}" `
  -Name "{version}" |
  Select-Object -ExpandProperty Id
```

---

Note

Use the full resource ID as the package reference ID when you deploy the application. It has the following format:

```text
/subscriptions/{subscription-id}/resourceGroups/{gallery-resource-group}/providers/Microsoft.Compute/galleries/{gallery-name}/applications/{application-name}/versions/{version}
```

## Deploy the VM application

After you create your VM Application and gather the necessary information, deploy it to your Arc-enabled server. The server downloads the application package and runs the installation command defined for that version.

# [Azure portal](#tab/portal)
### Deploy to a single machine

Deploy a VM application from the Arc-enabled server's resource page.

1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. On the toolbar, select **Add/Create**, and then select **Add application**.
5. Select the application you want to deploy, and then select **Save**.

### Deploy to multiple machines

Deploy one or more VM applications to multiple Arc-enabled servers from the machines list.

1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select the checkboxes for the servers you want to deploy applications to.
3. On the toolbar, select **Add applications**.
4. Confirm the selected machines, and then select **Next: Add applications &gt;**.
5. Select one or more applications, and then select **Next: Review &gt;**.
6. Review your selections, and then select **Review + Add**.

# [Azure CLI](#tab/azure-cli)
```azurecli
az connectedmachine application add \
  --name "{application-resource-name}" \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}" \
  --package-reference-id "{package-reference-id}"
```

# [PowerShell](#tab/azure-powershell)
```powershell
New-AzConnectedMachineApplication `
  -MachineName "{arc-machine-name}" `
  -ResourceGroupName "{resource-group}" `
  -ApplicationName "{application-resource-name}" `
  -PackageReferenceId "{package-reference-id}"
```

# [REST](#tab/rest)
```rest
PUT 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications/{application-resource-name}?api-version=2026-09-01
Content-Type: application/json

{
  "location": "{arc-machine-location}",
  "properties": {
    "packageReferenceId": "{package-reference-id}",
    "order": 1,
    "treatFailureAsDeploymentFailure": false
  }
}
```

# [Template](#tab/arm-template)
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "machineName": { "type": "string" },
    "applicationResourceName": { "type": "string" },
    "location": { "type": "string" },
    "packageReferenceId": { "type": "string" }
  },
  "resources": [
    {
      "type": "Microsoft.HybridCompute/machines/applications",
      "apiVersion": "2026-09-01",
      "name": "[format('{0}/{1}', parameters('machineName'), parameters('applicationResourceName'))]",
      "location": "[parameters('location')]",
      "properties": {
        "packageReferenceId": "[parameters('packageReferenceId')]",
        "order": 1,
        "treatFailureAsDeploymentFailure": false
      }
    }
  ]
}
```

# [Azure Policy](#tab/azure-policy)
Use Azure Policy to deploy and configure VM applications across a subscription or resource group:

- [Deploy a required application to Arc-enabled servers that don't have it and match the selected operating system.](monitor-vm-app-on-arc?tabs=deploy-if-not-exists#define-and-assign-a-policy)
- [Enforce the version, install order, and failure-handling settings of an existing application.](monitor-vm-app-on-arc?tabs=modify#define-and-assign-a-policy)

For identity permissions and remediation requirements, see [Prerequisites and remediation](monitor-vm-app-on-arc#prerequisites-and-remediation).

---

Important

When deploying multiple applications, use the VM Application `order` property to define the installation order. Don't use the ARM template `dependsOn` property as the application installation ordering mechanism.

## Verify the VM application deployment

After deployment, use one of the following methods to retrieve the application resource and check its provisioning state.

# [Azure portal](#tab/verify-portal)
1. In the [Azure portal](https://portal.azure.com), search for and select **Azure Arc**.
2. Select **Machines**, and then select your Arc-enabled server.
3. In the resource menu, select **VM applications**.
4. On the toolbar, select **Refresh**.
5. Find your application in the list and check its **Provisioning state**.

# [Azure CLI](#tab/verify-azure-cli)
```azurecli
az connectedmachine application show \
  --name "{application-resource-name}" \
  --machine-name "{arc-machine-name}" \
  --resource-group "{resource-group}"
```

# [PowerShell](#tab/verify-azure-powershell)
```azurepowershell
Get-AzConnectedMachineApplication `
  -MachineName "{arc-machine-name}" `
  -ResourceGroupName "{resource-group}" `
  -ApplicationName "{application-resource-name}"
```

# [REST](#tab/verify-rest)
```rest
GET 
https://management.azure.com/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.HybridCompute/machines/{arc-machine-name}/applications/{application-resource-name}?api-version=2026-09-01
```

---

Review the returned provisioning state for the status of the Azure resource operation. To check the installed version and the results of operations on the Arc-enabled server, [retrieve the application's instance view](manage-vm-app-on-arc#get-details-of-a-single-application).

## Difference in deployment process between Azure virtual machines and Arc-enabled servers

For Azure virtual machines (VMs) and Virtual Machine Scale Sets (VMSS), the application is added to the `applicationProfile` within the VM or VMSS profile. For Arc-enabled servers, the application is an external resource that's referenced and added to the machine. This enables event tracking and logging through Azure Activity Logs for control plane operations.