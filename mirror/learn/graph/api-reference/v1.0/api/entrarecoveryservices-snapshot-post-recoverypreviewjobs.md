---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: Create recoveryPreviewJob - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/entrarecoveryservices-snapshot-post-recoverypreviewjobs?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: yuhko-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Create a new preview job to enumerate changes required to restore to a snapshot's state.
ms.date: 2026-06-05T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 70737993-2029-a664-a86e-1d015ebc2b01
document_version_independent_id: acdf3d71-056d-fd7d-948c-0eb226c67d19
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/entrarecoveryservices-snapshot-post-recoverypreviewjobs.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/entrarecoveryservices-snapshot-post-recoverypreviewjobs
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/entrarecoveryservices-snapshot-post-recoverypreviewjobs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: d05bfebc-25a0-a82d-b9ad-e36ca116f448
---

# Create recoveryPreviewJob - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.entraRecoveryServices

Create a new [recoveryPreviewJob](resources/entrarecoveryservices-recoverypreviewjob) object to preview changes required to restore the tenant to a specific snapshot state. This operation follows the resource-based long running operation (RELO) pattern and returns a `202 Accepted` response with a `Location` header pointing to the job resource.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | EntraBackup.ReadWrite.Preview | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Entra Backup Administrator* is the least privileged role supported for this operation.

## HTTP request

```http
POST /directory/recovery/snapshots/{snapshot-id}/recoveryPreviewJobs
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, optionally supply a JSON representation with the following property.

| Property | Type | Description |
| --- | --- | --- |
| filteringCriteria | [microsoft.graph.entraRecoveryServices.recoveryJobFilteringCriteriaBase](resources/entrarecoveryservices-recoveryjobfilteringcriteriabase) | Optional. Filtering criteria to scope the job to specific entity types or entity IDs. If not specified, all supported entities are included. Use `@odata.type` to specify the derived type: `#microsoft.graph.entraRecoveryServices.recoveryJobEntityNamesFilter` or `#microsoft.graph.entraRecoveryServices.recoveryJobEntityNameAndIdsFilter`. |

## Response

If successful, this method returns a `202 Accepted` response code with a `Location` header pointing to the created job resource.

## Examples

### Example 1: Create a preview job without filtering

The following example creates a preview job for all changes.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs
```

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

await client.api('/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs').post();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

```http
HTTP/1.1 202 Accepted
Location: https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs/d3f8e7e8-7e87-4a7f-9d2c-c1c2d7e8e1f1
```

### Example 2: Create a preview job filtered by entity types

The following example creates a preview job for only user entity changes.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs
Content-Type: application/json

{
  "filteringCriteria": {
    "@odata.type": "#microsoft.graph.entraRecoveryServices.recoveryJobEntityNamesFilter",
    "entityTypes": [
      "user"
    ]
  }
}
```

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const recoveryPreviewJob = {
  filteringCriteria: {
    '@odata.type': '#microsoft.graph.entraRecoveryServices.recoveryJobEntityNamesFilter',
    entityTypes: [
      'user'
    ]
  }
};

await client.api('/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs').post(recoveryPreviewJob);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

```http
HTTP/1.1 202 Accepted
Location: https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs/d3f8e7e8-7e87-4a7f-9d2c-c1c2d7e8e1f1
```

### Example 3: Create a preview job filtered by specific entity IDs

The following example creates a preview job for specific users and groups.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs
Content-Type: application/json

{
  "filteringCriteria": {
    "@odata.type": "#microsoft.graph.entraRecoveryServices.recoveryJobEntityNameAndIdsFilter",
    "filterValues": [
      {
        "entityType": "user",
        "entityIds": [
          "52330fde-895a-4a99-ae59-1c35c2a263e9",
          "0c503c02-5554-4d59-9fcc-69736618fb8f"
        ]
      },
      {
        "entityType": "group",
        "entityIds": [
          "04181a71-a18d-4eee-94da-a77e7eb6520b",
          "2c888900-a7e8-4a01-ada5-17c04b29e8ec"
        ]
      }
    ]
  }
}
```

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const recoveryPreviewJob = {
  filteringCriteria: {
    '@odata.type': '#microsoft.graph.entraRecoveryServices.recoveryJobEntityNameAndIdsFilter',
    filterValues: [
      {
        entityType: 'user',
        entityIds: [
          '52330fde-895a-4a99-ae59-1c35c2a263e9',
          '0c503c02-5554-4d59-9fcc-69736618fb8f'
        ]
      },
      {
        entityType: 'group',
        entityIds: [
          '04181a71-a18d-4eee-94da-a77e7eb6520b',
          '2c888900-a7e8-4a01-ada5-17c04b29e8ec'
        ]
      }
    ]
  }
};

await client.api('/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs').post(recoveryPreviewJob);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

```http
HTTP/1.1 202 Accepted
Location: https://graph.microsoft.com/v1.0/directory/recovery/snapshots/MjAyNC0wOC0yNlQwMjozMDowMFo=/recoveryPreviewJobs/fa0f72f4-68e8-4625-846f-38865c49a086
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/entrarecoveryservices-snapshot-post-recoverypreviewjobs?view=graph-rest-beta&accept=text/markdown)
