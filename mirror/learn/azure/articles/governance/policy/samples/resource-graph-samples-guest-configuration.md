---
layout: Conceptual
title: Azure Resource Graph sample queries for Azure Policy guest configuration - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/samples/resource-graph-samples-guest-configuration
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
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
ms.service: azure-policy
ms.reviewer: kgremban
description: Sample Azure Resource Graph queries for Azure Policy guest configuration showing use of resource types and tables to access related resources and properties.
ms.date: 2025-02-25T00:00:00.0000000Z
ms.topic: sample
ms.custom: devx-track-azurecli, devx-track-azurepowershell
locale: en-us
document_id: e85a3ab3-171e-f1e3-4686-8a34355a93c7
document_version_independent_id: 89a904b6-fa6c-9e05-1640-76983641f254
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/samples/resource-graph-samples-guest-configuration.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/samples/resource-graph-samples-guest-configuration
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/samples/resource-graph-samples-guest-configuration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3928677-9b71-43a6-875f-004dc4f98b65
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/6bbc70ca-58b2-4c69-8249-28ec92c08029
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: dc544d41-b82d-18fe-a53d-352ea1dbb11f
---

# Azure Resource Graph sample queries for Azure Policy guest configuration - Azure Policy | Microsoft Learn

This page is a collection of [Azure Resource Graph](../../resource-graph/overview) sample queries for Azure Policy guest configuration.

## Azure Policy guest configuration

### Count machines in scope of guest configuration policies

Displays the count of Azure virtual machines and Arc connected servers in scope for [Azure Policy guest configuration](../../machine-configuration/overview) assignments.

```kusto
GuestConfigurationResources
| where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments'
| extend vmid = split(properties.targetResourceId,'/')
| mvexpand properties.latestAssignmentReport.resources
| where properties_latestAssignmentReport_resources.resourceId != 'Invalid assignment package.'
| project machine = tostring(vmid[(-1)]),type = tostring(vmid[(-3)])
| distinct machine, type
| summarize count() by type
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | extend vmid = split(properties.targetResourceId,'/') | mvexpand properties.latestAssignmentReport.resources | where properties_latestAssignmentReport_resources.resourceId != 'Invalid assignment package.' | project machine = tostring(vmid[(-1)]),type = tostring(vmid[(-3)]) | distinct machine, type | summarize count() by type"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | extend vmid = split(properties.targetResourceId,'/') | mvexpand properties.latestAssignmentReport.resources | where properties_latestAssignmentReport_resources.resourceId != 'Invalid assignment package.' | project machine = tostring(vmid[(-1)]),type = tostring(vmid[(-3)]) | distinct machine, type | summarize count() by type"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20extend%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%0a%7c%20mvexpand%20properties.latestAssignmentReport.resources%0a%7c%20where%20properties_latestAssignmentReport_resources.resourceId%20!%3d%20%27Invalid%20assignment%20package.%27%0a%7c%20project%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2ctype%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%0a%7c%20distinct%20machine%2c%20type%0a%7c%20summarize%20count%28%29%20by%20type)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20extend%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%0a%7c%20mvexpand%20properties.latestAssignmentReport.resources%0a%7c%20where%20properties_latestAssignmentReport_resources.resourceId%20!%3d%20%27Invalid%20assignment%20package.%27%0a%7c%20project%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2ctype%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%0a%7c%20distinct%20machine%2c%20type%0a%7c%20summarize%20count%28%29%20by%20type)
- Microsoft Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20extend%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%0a%7c%20mvexpand%20properties.latestAssignmentReport.resources%0a%7c%20where%20properties_latestAssignmentReport_resources.resourceId%20!%3d%20%27Invalid%20assignment%20package.%27%0a%7c%20project%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2ctype%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%0a%7c%20distinct%20machine%2c%20type%0a%7c%20summarize%20count%28%29%20by%20type)

---

### Count of non-compliant guest configuration assignments

Displays a count of non-compliant machines per [guest configuration assignment reason](../how-to/determine-non-compliance#compliance-details-for-guest-configuration). Limits results to first 100 for performance.

```kusto
GuestConfigurationResources
| where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments'
| project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus)
| extend resources = iff(isnull(resources[0]), dynamic([{}]), resources)
| mvexpand resources
| extend reasons = resources.reasons
| extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons)
| mvexpand reasons
| project id, vmid, name, status, resource = tostring(resources.resourceId), reason = reasons.phrase
| summarize count() by resource, name
| order by count_
| limit 100
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | project id, vmid, name, status, resource = tostring(resources.resourceId), reason = reasons.phrase | summarize count() by resource, name | order by count_ | limit 100"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | project id, vmid, name, status, resource = tostring(resources.resourceId), reason = reasons.phrase | summarize count() by resource, name | order by count_ | limit 100"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20tostring%28resources.resourceId%29%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20count%28%29%20by%20resource%2c%20name%0a%7c%20order%20by%20count_%0a%7c%20limit%20100)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20tostring%28resources.resourceId%29%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20count%28%29%20by%20resource%2c%20name%0a%7c%20order%20by%20count_%0a%7c%20limit%20100)
- Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20type%20%3d%7e%20%27microsoft.guestconfiguration%2fguestconfigurationassignments%27%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20tostring%28resources.resourceId%29%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20count%28%29%20by%20resource%2c%20name%0a%7c%20order%20by%20count_%0a%7c%20limit%20100)

---

### Find all reasons a machine is non-compliant for guest configuration assignments

Display all [guest configuration assignment reasons](../how-to/determine-non-compliance#compliance-details-for-guest-configuration) for a specific machine. Replace `MACHINENAME` with a valid machine name.

```kusto
GuestConfigurationResources
| where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments'
| project id, name, resources = properties.latestAssignmentReport.resources, machine = split(properties.targetResourceId,'/')[(-1)]
| extend resources = iff(isnull(resources[0]), dynamic([{}]), resources)
| mv-expand resources
| extend reasons = resources.reasons
| extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons)
| mv-expand reasons
| extend status = iff(resources.complianceStatus == true, 'Compliant', 'NonCompliant')
| where status == 'NonCompliant'
| where machine == 'MACHINENAME'
| project id, machine, name, status, resource = resources.resourceId, reason = reasons.phrase
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | project id, name, resources = properties.latestAssignmentReport.resources, machine = split(properties.targetResourceId,'/')[(-1)] | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mv-expand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mv-expand reasons | extend status = iff(resources.complianceStatus == true, 'Compliant', 'NonCompliant') | where status == 'NonCompliant' | where machine == 'MACHINENAME' | project id, machine, name, status, resource = resources.resourceId, reason = reasons.phrase"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "GuestConfigurationResources | where type =~ 'microsoft.guestconfiguration/guestconfigurationassignments' | project id, name, resources = properties.latestAssignmentReport.resources, machine = split(properties.targetResourceId,'/')[(-1)] | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mv-expand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mv-expand reasons | extend status = iff(resources.complianceStatus == true, 'Compliant', 'NonCompliant') | where status == 'NonCompliant' | where machine == 'MACHINENAME' | project id, machine, name, status, resource = resources.resourceId, reason = reasons.phrase"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0D%0A%7C%20where%20type%20%3D~%20%27microsoft.guestconfiguration%2Fguestconfigurationassignments%27%0D%0A%7C%20project%20id%2C%20name%2C%20resources%20%3D%20properties.latestAssignmentReport.resources%2C%20machine%20%3D%20split%28properties.targetResourceId%2C%27%2F%27%29%5B%28-1%29%5D%0D%0A%7C%20extend%20resources%20%3D%20iff%28isnull%28resources%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20resources%29%0D%0A%7C%20mv-expand%20resources%0D%0A%7C%20extend%20reasons%20%3D%20resources.reasons%0D%0A%7C%20extend%20reasons%20%3D%20iff%28isnull%28reasons%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20reasons%29%0D%0A%7C%20mv-expand%20reasons%0D%0A%7C%20extend%20status%20%3D%20iff%28resources.complianceStatus%20%3D%3D%20true%2C%20%27Compliant%27%2C%20%27NonCompliant%27%29%0D%0A%7C%20where%20status%20%3D%3D%20%27NonCompliant%27%0D%0A%7C%20where%20machine%20%3D%3D%20%27MACHINENAME%27%0D%0A%7C%20project%20id%2C%20machine%2C%20name%2C%20status%2C%20resource%20%3D%20resources.resourceId%2C%20reason%20%3D%20reasons.phrase)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0D%0A%7C%20where%20type%20%3D~%20%27microsoft.guestconfiguration%2Fguestconfigurationassignments%27%0D%0A%7C%20project%20id%2C%20name%2C%20resources%20%3D%20properties.latestAssignmentReport.resources%2C%20machine%20%3D%20split%28properties.targetResourceId%2C%27%2F%27%29%5B%28-1%29%5D%0D%0A%7C%20extend%20resources%20%3D%20iff%28isnull%28resources%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20resources%29%0D%0A%7C%20mv-expand%20resources%0D%0A%7C%20extend%20reasons%20%3D%20resources.reasons%0D%0A%7C%20extend%20reasons%20%3D%20iff%28isnull%28reasons%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20reasons%29%0D%0A%7C%20mv-expand%20reasons%0D%0A%7C%20extend%20status%20%3D%20iff%28resources.complianceStatus%20%3D%3D%20true%2C%20%27Compliant%27%2C%20%27NonCompliant%27%29%0D%0A%7C%20where%20status%20%3D%3D%20%27NonCompliant%27%0D%0A%7C%20where%20machine%20%3D%3D%20%27MACHINENAME%27%0D%0A%7C%20project%20id%2C%20machine%2C%20name%2C%20status%2C%20resource%20%3D%20resources.resourceId%2C%20reason%20%3D%20reasons.phrase)
- Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0D%0A%7C%20where%20type%20%3D~%20%27microsoft.guestconfiguration%2Fguestconfigurationassignments%27%0D%0A%7C%20project%20id%2C%20name%2C%20resources%20%3D%20properties.latestAssignmentReport.resources%2C%20machine%20%3D%20split%28properties.targetResourceId%2C%27%2F%27%29%5B%28-1%29%5D%0D%0A%7C%20extend%20resources%20%3D%20iff%28isnull%28resources%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20resources%29%0D%0A%7C%20mv-expand%20resources%0D%0A%7C%20extend%20reasons%20%3D%20resources.reasons%0D%0A%7C%20extend%20reasons%20%3D%20iff%28isnull%28reasons%5B0%5D%29%2C%20dynamic%28%5B%7B%7D%5D%29%2C%20reasons%29%0D%0A%7C%20mv-expand%20reasons%0D%0A%7C%20extend%20status%20%3D%20iff%28resources.complianceStatus%20%3D%3D%20true%2C%20%27Compliant%27%2C%20%27NonCompliant%27%29%0D%0A%7C%20where%20status%20%3D%3D%20%27NonCompliant%27%0D%0A%7C%20where%20machine%20%3D%3D%20%27MACHINENAME%27%0D%0A%7C%20project%20id%2C%20machine%2C%20name%2C%20status%2C%20resource%20%3D%20resources.resourceId%2C%20reason%20%3D%20reasons.phrase)

---

### List machines and status of pending reboot

Provides a list of machines with configuration details about whether they have a pending reboot.

```kusto
GuestConfigurationResources
| where name in ('WindowsPendingReboot')
| project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/'), status = tostring(properties.complianceStatus)
| extend resources = iff(isnull(resources[0]), dynamic([{}]), resources)
| mvexpand resources
| extend reasons = resources.reasons
| extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons)
| mvexpand reasons
| project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase
| summarize name = any(name), status = any(status), vmid = any(vmid), resources = make_list_if(resource, isnotnull(resource)), reasons = make_list_if(reason, isnotnull(reason)) by id = tolower(id)
| project id, machine = tostring(vmid[(-1)]), type = tostring(vmid[(-3)]), name, status, reasons
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "GuestConfigurationResources | where name in ('WindowsPendingReboot') | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/'), status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase | summarize name = any(name), status = any(status), vmid = any(vmid), resources = make_list_if(resource, isnotnull(resource)), reasons = make_list_if(reason, isnotnull(reason)) by id = tolower(id) | project id, machine = tostring(vmid[(-1)]), type = tostring(vmid[(-3)]), name, status, reasons"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "GuestConfigurationResources | where name in ('WindowsPendingReboot') | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/'), status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase | summarize name = any(name), status = any(status), vmid = any(vmid), resources = make_list_if(resource, isnotnull(resource)), reasons = make_list_if(reason, isnotnull(reason)) by id = tolower(id) | project id, machine = tostring(vmid[(-1)]), type = tostring(vmid[(-3)]), name, status, reasons"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27WindowsPendingReboot%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20name%20%3d%20any%28name%29%2c%20status%20%3d%20any%28status%29%2c%20vmid%20%3d%20any%28vmid%29%2c%20resources%20%3d%20make_list_if%28resource%2c%20isnotnull%28resource%29%29%2c%20reasons%20%3d%20make_list_if%28reason%2c%20isnotnull%28reason%29%29%20by%20id%20%3d%20tolower%28id%29%0a%7c%20project%20id%2c%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2c%20type%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%2c%20name%2c%20status%2c%20reasons)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27WindowsPendingReboot%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20name%20%3d%20any%28name%29%2c%20status%20%3d%20any%28status%29%2c%20vmid%20%3d%20any%28vmid%29%2c%20resources%20%3d%20make_list_if%28resource%2c%20isnotnull%28resource%29%29%2c%20reasons%20%3d%20make_list_if%28reason%2c%20isnotnull%28reason%29%29%20by%20id%20%3d%20tolower%28id%29%0a%7c%20project%20id%2c%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2c%20type%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%2c%20name%2c%20status%2c%20reasons)
- Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27WindowsPendingReboot%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase%0a%7c%20summarize%20name%20%3d%20any%28name%29%2c%20status%20%3d%20any%28status%29%2c%20vmid%20%3d%20any%28vmid%29%2c%20resources%20%3d%20make_list_if%28resource%2c%20isnotnull%28resource%29%29%2c%20reasons%20%3d%20make_list_if%28reason%2c%20isnotnull%28reason%29%29%20by%20id%20%3d%20tolower%28id%29%0a%7c%20project%20id%2c%20machine%20%3d%20tostring%28vmid%5b%28-1%29%5d%29%2c%20type%20%3d%20tostring%28vmid%5b%28-3%29%5d%29%2c%20name%2c%20status%2c%20reasons)

---

### List machines that are not running and the last compliance status

Provides a list of machines that aren't powered on with their configuration assignments and the last reported compliance status.

```kusto
Resources
| where type =~ 'Microsoft.Compute/virtualMachines'
| where properties.extended.instanceView.powerState.code != 'PowerState/running'
| project vmName = name, power = properties.extended.instanceView.powerState.code
| join kind = leftouter (GuestConfigurationResources
  | extend vmName = tostring(split(properties.targetResourceId,'/')[(-1)])
  | project vmName, name, compliance = properties.complianceStatus) on vmName | project-away vmName1
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "Resources | where type =~ 'Microsoft.Compute/virtualMachines' | where properties.extended.instanceView.powerState.code != 'PowerState/running' | project vmName = name, power = properties.extended.instanceView.powerState.code | join kind = leftouter (GuestConfigurationResources | extend vmName = tostring(split(properties.targetResourceId,'/')[(-1)]) | project vmName, name, compliance = properties.complianceStatus) on vmName | project-away vmName1"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "Resources | where type =~ 'Microsoft.Compute/virtualMachines' | where properties.extended.instanceView.powerState.code != 'PowerState/running' | project vmName = name, power = properties.extended.instanceView.powerState.code | join kind = leftouter (GuestConfigurationResources | extend vmName = tostring(split(properties.targetResourceId,'/')[(-1)]) | project vmName, name, compliance = properties.complianceStatus) on vmName | project-away vmName1"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/Resources%0a%7c%20where%20type%20%3d%7e%20%27Microsoft.Compute%2fvirtualMachines%27%0a%7c%20where%20properties.extended.instanceView.powerState.code%20!%3d%20%27PowerState%2frunning%27%0a%7c%20project%20vmName%20%3d%20name%2c%20power%20%3d%20properties.extended.instanceView.powerState.code%0a%7c%20join%20kind%20%3d%20leftouter%20%28GuestConfigurationResources%0a%09%7c%20extend%20vmName%20%3d%20tostring%28split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%29%0a%09%7c%20project%20vmName%2c%20name%2c%20compliance%20%3d%20properties.complianceStatus%29%20on%20vmName%20%7c%20project-away%20vmName1)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/Resources%0a%7c%20where%20type%20%3d%7e%20%27Microsoft.Compute%2fvirtualMachines%27%0a%7c%20where%20properties.extended.instanceView.powerState.code%20!%3d%20%27PowerState%2frunning%27%0a%7c%20project%20vmName%20%3d%20name%2c%20power%20%3d%20properties.extended.instanceView.powerState.code%0a%7c%20join%20kind%20%3d%20leftouter%20%28GuestConfigurationResources%0a%09%7c%20extend%20vmName%20%3d%20tostring%28split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%29%0a%09%7c%20project%20vmName%2c%20name%2c%20compliance%20%3d%20properties.complianceStatus%29%20on%20vmName%20%7c%20project-away%20vmName1)
- Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/Resources%0a%7c%20where%20type%20%3d%7e%20%27Microsoft.Compute%2fvirtualMachines%27%0a%7c%20where%20properties.extended.instanceView.powerState.code%20!%3d%20%27PowerState%2frunning%27%0a%7c%20project%20vmName%20%3d%20name%2c%20power%20%3d%20properties.extended.instanceView.powerState.code%0a%7c%20join%20kind%20%3d%20leftouter%20%28GuestConfigurationResources%0a%09%7c%20extend%20vmName%20%3d%20tostring%28split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%29%0a%09%7c%20project%20vmName%2c%20name%2c%20compliance%20%3d%20properties.complianceStatus%29%20on%20vmName%20%7c%20project-away%20vmName1)

---

### Query details of guest configuration assignment reports

Display report from [guest configuration assignment reason](../how-to/determine-non-compliance#compliance-details-for-guest-configuration) details. In the following example, the query returns only results where the Guest Assignment name is `installed_application_linux` and the output contains the string `Chrome` to list all Linux machines where a package is installed that includes the name **Chrome**.

```kusto
GuestConfigurationResources
| where name in ('installed_application_linux')
| project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus)
| extend resources = iff(isnull(resources[0]), dynamic([{}]), resources)
| mvexpand resources
| extend reasons = resources.reasons
| extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons)
| mvexpand reasons
| where reasons.phrase contains 'chrome'
| project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase
```

# [Azure CLI](#tab/azure-cli)
```azurecli
az graph query -q "GuestConfigurationResources | where name in ('installed_application_linux') | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | where reasons.phrase contains 'chrome' | project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase"
```

# [Azure PowerShell](#tab/azure-powershell)
```azurepowershell
Search-AzGraph -Query "GuestConfigurationResources | where name in ('installed_application_linux') | project id, name, resources = properties.latestAssignmentReport.resources, vmid = split(properties.targetResourceId,'/')[(-1)], status = tostring(properties.complianceStatus) | extend resources = iff(isnull(resources[0]), dynamic([{}]), resources) | mvexpand resources | extend reasons = resources.reasons | extend reasons = iff(isnull(reasons[0]), dynamic([{}]), reasons) | mvexpand reasons | where reasons.phrase contains 'chrome' | project id, vmid, name, status, resource = resources.resourceId, reason = reasons.phrase"
```

# [Portal](#tab/azure-portal)
- Azure portal: [portal.azure.com](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27installed_application_linux%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20where%20reasons.phrase%20contains%20%27chrome%27%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase)
- Azure Government portal: [portal.azure.us](https://portal.azure.us/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27installed_application_linux%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20where%20reasons.phrase%20contains%20%27chrome%27%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase)
- Azure operated by 21Vianet portal: [portal.azure.cn](https://portal.azure.cn/#blade/HubsExtension/ArgQueryBlade/query/GuestConfigurationResources%0a%7c%20where%20name%20in%20%28%27installed_application_linux%27%29%0a%7c%20project%20id%2c%20name%2c%20resources%20%3d%20properties.latestAssignmentReport.resources%2c%20vmid%20%3d%20split%28properties.targetResourceId%2c%27%2f%27%29%5b%28-1%29%5d%2c%20status%20%3d%20tostring%28properties.complianceStatus%29%0a%7c%20extend%20resources%20%3d%20iff%28isnull%28resources%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20resources%29%0a%7c%20mvexpand%20resources%0a%7c%20extend%20reasons%20%3d%20resources.reasons%0a%7c%20extend%20reasons%20%3d%20iff%28isnull%28reasons%5b0%5d%29%2c%20dynamic%28%5b%7b%7d%5d%29%2c%20reasons%29%0a%7c%20mvexpand%20reasons%0a%7c%20where%20reasons.phrase%20contains%20%27chrome%27%0a%7c%20project%20id%2c%20vmid%2c%20name%2c%20status%2c%20resource%20%3d%20resources.resourceId%2c%20reason%20%3d%20reasons.phrase)

---