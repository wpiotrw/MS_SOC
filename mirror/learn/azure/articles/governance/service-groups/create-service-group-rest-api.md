---
layout: Conceptual
title: 'Quickstart: Create a service group with REST API - Azure Governance | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/service-groups/create-service-group-rest-api
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
author: kenieva
learn_banner_products:
- azure
ms.author: kenieva
ms.service: azure-policy
description: In this quickstart, you use REST API to create a service group to organize your resources.
ms.topic: quickstart
ms.date: 2025-05-19T00:00:00.0000000Z
ms.custom:
- build-2025
locale: en-us
document_id: e099e11a-adc0-a61c-3a41-0f282b77b417
document_version_independent_id: 2d9a4dc4-7f25-07c5-384a-70f9fad16710
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/service-groups/create-service-group-rest-api.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/service-groups/create-service-group-rest-api
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/service-groups/create-service-group-rest-api.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8574c148-4774-3c66-ab61-f9d680f0a1cd
---

# Quickstart: Create a service group with REST API - Azure Governance | Microsoft Learn

By using Azure Service Groups, you can create low-privilege-based groupings of resources across subscriptions. They provide a way to manage resources with minimal permissions, ensuring that you can group and manage resources without granting excessive access. Service Groups complement existing organizational structures like Resource Groups, Subscriptions, and Management Groups by offering a flexible and secure way to aggregate resources for specific purposes. For more information about service groups, see [Getting started with Service Groups](overview).

## Prerequisites

- If you don't have an Azure subscription, create a [free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) account before you begin.
- If you haven't already, install [ARMClient](https://github.com/projectkudu/ARMClient). It's a tool that sends HTTP requests to Azure Resource Manager-based REST APIs.

## Create in REST API

In this example, the service group **groupId** is *Contoso*.

- REST API URI

    ```http
    PUT https://management.azure.com/providers/Microsoft.Management/serviceGroups/Contoso?api-version=2026-08-01
    ```
- Request Body

The **groupId** is a unique identifier being created. This ID is used by other commands to reference this group and it can't be changed later.

If you want the service group to show a different name within the Azure portal, add the **properties.displayName** property in the request body. For example, to create a service group with the **groupId** of *Contoso* and the display name of *Contoso Group*, use the following endpoint and request body:

```json
{
  "properties": {
    "displayName": "_Contoso Group_",
    "parent": {
      "resourceId": "/providers/Microsoft.Management/serviceGroups/[tenantId]"
    }
  }
}
```

In the preceding examples, the new service group is created under the root service group. To specify a different service group as the parent, use the **properties.parent.resourceId** property.

- REST API URI

    ```http
    PUT https://management.azure.com/providers/Microsoft.Management/serviceGroups/Contoso?api-version=2026-08-01
    ```
- Request Body

    ```json
    {
      "properties": {
        "displayName": "Contoso Group",
        "parent": {
          "resourceId": "/providers/Microsoft.Management/serviceGroups/HoldingGroup"
        }
      }
    }
    ```

### Optional properties

Starting with API version `2026-08-01`, you can set the following optional properties when you create a service group:

| Property | Type | Description |
| --- | --- | --- |
| `tags` | Object | Resource tags as a dictionary of string keys and string values. |
| `kind` | String | The kind of the service group. |
| `properties.attributes.criticality` | Integer | The criticality designation of the service group. Valid values range from 0 through 4. |

The following example creates a service group with tags and a criticality value:

```http
PUT https://management.azure.com/providers/Microsoft.Management/serviceGroups/Contoso?api-version=2026-08-01
```

```json
{
  "tags": {
    "environment": "production"
  },
  "properties": {
    "displayName": "Contoso Group",
    "parent": {
      "resourceId": "/providers/Microsoft.Management/serviceGroups/[tenantId]"
    },
    "attributes": {
      "criticality": 2
    }
  }
}
```

## Verify your Service Group was created

Service Groups PUT or create call is an Asynchronous call which means that the response to the initial create call is that it was accepted. This response doesn't mean the service group was successfully created, only that the Azure successfully received the request to create the service group.

To check the operation was successful, you should do a GET call on the value returned in the **azure-asyncoperation** header. The URL provides the status of the created operation.

Note

To avoid issues within scripts or templates, the automation should poll this provided URL before moving to the next step. If the automation moves to the next step before the operation has responded successfully, the next operation will fail as the service group has not been created.

## Clean up resources

To remove the service group created in this document, use the Service Group Delete endpoint:

- REST API URI

    ```http
    DELETE https://management.azure.com/providers/Microsoft.Management/serviceGroups/Contoso?api-version=2026-08-01
    ```
- No Request Body

A `202 Accepted` response means the delete request was accepted, not that the deletion is complete. Follow the operation status header in the response to confirm completion.