---
layout: Conceptual
title: View and query machine inventory - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/how-to/machine-inventory/view-and-query-machine-inventory
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
description: Learn how to browse machine inventory and query applications, certificates, services, accounts, and server roles with Azure Resource Graph.
ms.date: 2026-11-07T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: 6e4cb520-6148-a1d2-a1e7-23827bd18503
document_version_independent_id: c7d071b2-3566-5670-8a3b-b44a9e77e4af
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/how-to/machine-inventory/view-and-query-machine-inventory.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/how-to/machine-inventory/view-and-query-machine-inventory
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/how-to/machine-inventory/view-and-query-machine-inventory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3928677-9b71-43a6-875f-004dc4f98b65
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6bbc70ca-58b2-4c69-8249-28ec92c08029
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 9e08c338-e6d6-884b-db7b-7d28524d9e0d
---

# View and query machine inventory - Azure Machine Configuration | Microsoft Learn

Use machine inventory in the Azure portal to explore collected inventory, or use Azure Resource Graph to answer questions across machines. The examples in this article query inventory records without changing machine configuration.

## Prerequisites

- [Enable machine inventory](enable-machine-inventory) or [Microsoft Configuration Manager Connected Inventory](configuration-manager-connected-inventory).
- Permissions to view inventory and the associated machine resources in your query scope.

## Browse inventory in the Azure portal

1. Open the **Machine Configuration** page in Azure Portal.
2. Go to **machine inventory (preview)** in the left-hand table of contents.

    [![Screenshot of the machine inventory overview in the Azure portal.](machine-inventory-overview.png)](machine-inventory-overview.png#lightbox)
3. Use the filters to select specific subscription or resource group scopes you want to review.
4. Currently, inventory category tables are available for the following categories: **Applications**, **Certificates**, **Services**, **Users**, **Groups**, and **Windows roles**.
5. Select **See all** on any tile to review the inventory records and their associated machines.

## Run an Azure Resource Graph query

1. In the Azure portal, open **Resource Graph Explorer**.
2. Select the subscriptions you want to query.
3. Paste one of the following queries into the query editor.
4. Replace any placeholder values, and select **Run query**.

The queries use `guestconfigurationresources`. Each example includes the machine resource ID so that similarly named machines can be distinguished.

```kusto
guestconfigurationresources
| where id startswith '<machine-resource-id>/'
| where type in~ (
    'microsoft.guestconfiguration/applications',
    'microsoft.guestconfiguration/services',
    'microsoft.guestconfiguration/users',
    'microsoft.guestconfiguration/groups',
    'microsoft.guestconfiguration/certificates',
    'microsoft.guestconfiguration/windowsroles',
    'microsoft.guestconfiguration/daemons',
    'microsoft.guestconfiguration/softwares')
| summarize records = count() by type
| order by type asc
```

The result counts inventory records by resource type, not machines. A category with no records doesn't appear in the result.

### List Windows applications

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/applications'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, application = name,
    version = tostring(properties.version),
    publisher = tostring(properties.publisher),
    installedDate = todatetime(properties.installDate),
    resourceGroup, subscriptionId
| order by machineResourceId asc, application asc
```

To find a particular application, add a filter such as `| where name contains 'Contoso'` before `project`.

### Find expired certificates or certificates expiring within 30 days

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/certificates'
| extend expirationDate = todatetime(properties.notAfter)
| where expirationDate <= now() + 30d
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, certificate = name,
    subject = tostring(properties.subject),
    issuer = tostring(properties.issuer),
    expirationDate,
    keySize = toint(properties.keySize),
    resourceGroup, subscriptionId
| order by expirationDate asc
```

This query includes already-expired certificates. To return only certificates that haven't yet expired, add `| where expirationDate > now()` before `project`.

### Review Windows service state and service accounts

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/services'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, service = name,
    displayName = tostring(properties.displayName),
    state = tostring(properties.state),
    status = tostring(properties.status),
    startType = tostring(properties.startType),
    userName = tostring(properties.userName),
    resourceGroup, subscriptionId
| order by machineResourceId asc, service asc
```

### Review local users

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/users'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, user = name,
    domain = tostring(properties.domain),
    enabled = tobool(properties.enabled),
    description = tostring(properties.description),
    resourceGroup, subscriptionId
| order by machineResourceId asc, user asc
```

### Review groups and membership

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/groups'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, group = name,
    groupId = tostring(properties.groupId),
    members = properties.members,
    memberCount = array_length(properties.members),
    resourceGroup, subscriptionId
| order by machineResourceId asc, group asc
```

### Review Windows Server roles

```kusto
guestconfigurationresources
| where type =~ 'microsoft.guestconfiguration/windowsroles'
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, role = name,
    installedState = tostring(properties.installedState),
    path = tostring(properties.path),
    displayName = tostring(properties.displayName),
    description = tostring(properties.description),
    parentRole = tostring(properties.parentRole),
    resourceGroup, subscriptionId
| order by machineResourceId asc, path asc
```

### Explore Linux inventory

Use the raw properties to inspect Linux software and daemon records without assuming that their schema matches Windows applications or services.

```kusto
guestconfigurationresources
| where type in~ (
    'microsoft.guestconfiguration/daemons',
    'microsoft.guestconfiguration/softwares')
| extend machineResourceId = tostring(split(tolower(id), '/providers/microsoft.guestconfiguration/')[0])
| project machineResourceId, type, name, properties, resourceGroup, subscriptionId
| order by machineResourceId asc, type asc, name asc
```

## Interpret results

Inventory queries return records within the selected Azure scope and your access permissions. Check both before treating the output as a fleet-wide result.

Inventory reflects collected data rather than a live inspection of a machine. Missing categories or records can indicate an unsupported category, a collection issue, or a reporting delay. Verify that the machine is enabled for inventory before concluding that a resource is absent.