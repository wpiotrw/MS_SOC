---
layout: Conceptual
title: Programmatically deploy and manage Azure Arc Extended Security Updates licenses - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/api-extended-security-updates
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
zone_pivot_group_filename: zone-pivots/azure-management/zone-pivot-groups.json
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to programmatically deploy and manage Azure Arc Extended Security Updates licenses for Windows Server 2012 and Windows Server 2016.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
zone_pivot_groups: extended-security-updates-windows-server
locale: en-us
document_id: 9bdf88f1-3ffc-654e-a922-3ad02c309d99
document_version_independent_id: 861b0149-b2e4-d8aa-32c1-bb7f4dcff183
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/api-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/api-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/api-extended-security-updates.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 246043f8-e168-b6c3-2d75-a28c8300ede8
---

# Programmatically deploy and manage Azure Arc Extended Security Updates licenses - Azure Arc | Microsoft Learn

This article provides instructions to programmatically provision and manage Windows Server Extended Security Updates lifecycle operations through the Azure Arc ESU ARM APIs. The instructions apply to Windows Server 2012/2012 R2 and Windows Server 2016. Use the selector at the top of the article to choose the operating system version you're licensing.

For each of the API commands explained in this article, enter accurate parameter information for location, state, edition, type, and processors depending on your particular scenario. Set the `target` property to the operating system you're licensing:

::: zone pivot="windows-server-2012"

- `Windows Server 2012`
- `Windows Server 2012 R2`

Important

The Windows Server 2012 and Windows Server 2012 R2 ESU period ends on October 13, 2026. At midnight Coordinated Universal Time (UTC) on October 14, 2026, ESU licenses enabled by Azure Arc are deactivated and stop providing update eligibility. Deactivated license resources remain available to query, but they can't provide eligibility for security updates released after October 13, 2026.

::: zone-end

::: zone pivot="windows-server-2016"

- `Windows Server 2016`

::: zone-end

Note

You need to create a service principal to use the Azure API to manage ESUs. See [Connect hybrid machines to Azure at scale](onboard-service-principal) and [Azure REST API reference](/en-us/rest/api/azure/) for more information.

## Provision a license

To provision a license, run the following command:

::: zone pivot="windows-server-2012"

```http
PUT  
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/licenses/LICENSE_NAME?api-version=2023-06-20-preview 
{  
    "location": "ENTER-REGION",  
    "properties": {  
        "licenseDetails": {  
            "state": "Activated",  
            "target": "Windows Server 2012",  
            "Edition": "Datacenter",  
            "Type": "pCore",  
            "Processors": 12  
        }  
    }  
}
```

::: zone-end

::: zone pivot="windows-server-2016"

```http
PUT  
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/licenses/LICENSE_NAME?api-version=2023-06-20-preview 
{  
    "location": "ENTER-REGION",  
    "properties": {  
        "licenseDetails": {  
            "state": "Activated",  
            "target": "Windows Server 2016",  
            "Edition": "Datacenter",  
            "Type": "pCore",  
            "Processors": 12  
        }  
    }  
}
```

::: zone-end

::: zone pivot="windows-server-2012"

The `--volume-license-details` parameter applies only to the transition from Year 1 Volume Licensing entitlements. This transition period has ended. The command syntax retains the parameter for compatibility with existing automation:

```azurecli
az connectedmachine license create --license-name
                                   --resource-group
                                   [--edition {Datacenter, Standard}]
                                   [--license-type {ESU}]
                                   [--location]
                                   [--no-wait {0, 1, f, false, n, no, t, true, y, yes}]
                                   [--processors]
                                   [--state {Activated, Deactivated}]
                                   [--tags]
                                   [--target {Windows Server 2012, Windows Server 2012 R2}]
                                   [--tenant-id]
                                   [--type {pCore, vCore}]
                                   [--volume-license-details]
```

::: zone-end

::: zone pivot="windows-server-2016"

### Transition from volume licensing

Transitioning from Volume Licensing isn't supported for Windows Server 2016 ESUs enabled by Azure Arc.

::: zone-end

## Link a license

To link a license, run the following command:

```http
PUT  
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/machines/MACHINE_NAME/licenseProfiles/default?api-version=2023-06-20-preview 
{
   "location": "SAME_REGION_AS_MACHINE",
   "properties": {
      "esuProfile": {
         "assignedLicense": "RESOURCE_ID_OF_LICENSE"
      }
   }
}
```

## Unlink a license

To unlink a license, run the following command:

```http
PUT 
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/machines/MACHINE_NAME/licenseProfiles/default?api-version=2023-06-20-preview
{
  "location": "SAME_REGION_AS_MACHINE",
  "properties": {
    "esuProfile": {
    }
  }
}
```

## Modify a license

To modify a license, run the following command:

::: zone pivot="windows-server-2012"

```http
PUT/PATCH 
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/licenses/LICENSE_NAME?api-version=2023-06-20-preview 
{  
    "location": "ENTER-REGION",  
    "properties": {  
        "licenseDetails": {  
            "state": "Activated",  
            "target": "Windows Server 2012",  
            "Edition": "Datacenter",  
            "Type": "pCore",  
            "Processors": 12  
        }  
    }  
}
```

::: zone-end

::: zone pivot="windows-server-2016"

```http
PUT/PATCH 
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/licenses/LICENSE_NAME?api-version=2023-06-20-preview 
{  
    "location": "ENTER-REGION",  
    "properties": {  
        "licenseDetails": {  
            "state": "Activated",  
            "target": "Windows Server 2016",  
            "Edition": "Datacenter",  
            "Type": "pCore",  
            "Processors": 12  
        }  
    }  
}
```

::: zone-end

To delete a license, run the following command:

```http
DELETE  
https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME/providers/Microsoft.HybridCompute/licenses/LICENSE_NAME?api-version=2023-06-20-preview
```