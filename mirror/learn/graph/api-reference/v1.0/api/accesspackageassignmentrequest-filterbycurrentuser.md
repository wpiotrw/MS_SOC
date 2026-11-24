---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'accessPackageAssignmentRequest: filterByCurrentUser - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/accesspackageassignmentrequest-filterbycurrentuser?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: AlexFilipin
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Retrieve a list of accesspackageassignmentrequest objects filtered on the signed-in user.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2024-04-04T00:00:00.0000000Z
locale: en-us
document_id: f077ba5c-0952-7302-5f6b-d10c69c61943
document_version_independent_id: eef1a869-4ffa-e5fd-4044-cd3ba1a51c3e
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/accesspackageassignmentrequest-filterbycurrentuser.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/accesspackageassignmentrequest-filterbycurrentuser
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/accesspackageassignmentrequest-filterbycurrentuser.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 80a02994-b487-9274-e31d-da97ddd2220c
---

# accessPackageAssignmentRequest: filterByCurrentUser - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

In [Microsoft Entra Entitlement Management](resources/entitlementmanagement-overview), retrieve a list of [accessPackageAssignmentRequest](resources/accesspackageassignmentrequest) objects filtered on the signed-in user.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ✅ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | EntitlementMgmt-SubjectAccess.ReadWrite | EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

## HTTP request

```http
GET /identityGovernance/entitlementManagement/assignmentRequests/filterByCurrentUser(on='parameterValue')
```

## Function parameters

The following table shows the parameters that can be used with this function.

| Parameter | Type | Description |
| --- | --- | --- |
| on | [accessPackageAssignmentRequestFilterByCurrentUserOptions](resources/accesspackageassignmentrequestfilterbycurrentuseroptions) | The list of user options that can be used to filter on the access package assignment requests list. |

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [accessPackageAssignmentRequest](resources/accesspackageassignmentrequest) collection in the response body.

## Examples

### Request

# [HTTP](#tab/http)
```http
GET https://graph.microsoft.com/v1.0/identityGovernance/entitlementManagement/assignmentRequests/filterByCurrentUser(on='target')
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.IdentityGovernance.EntitlementManagement.AssignmentRequests.FilterByCurrentUserWithOn("target").GetAsFilterByCurrentUserWithOnGetResponseAsync();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
on := "target"
filterByCurrentUser, err := graphClient.IdentityGovernance().EntitlementManagement().AssignmentRequests().FilterByCurrentUserWithOn(&on).GetAsFilterByCurrentUserWithOnGetResponse(context.Background(), nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

var result = graphClient.identityGovernance().entitlementManagement().assignmentRequests().filterByCurrentUserWithOn("target").get();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let filterByCurrentUser = await client.api('/identityGovernance/entitlementManagement/assignmentRequests/filterByCurrentUser(on='target')').get();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->identityGovernance()->entitlementManagement()->assignmentRequests()->filterByCurrentUserWithOn('target', )->get()->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Invoke-MgFilterEntitlementManagementAssignmentRequestByCurrentUser -On $onId 

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.identity_governance.entitlement_management.assignment_requests.filter_by_current_user_with_on("target").get()

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "id": "46c1410d-ef96-44c5-ae9c-a577d014fe0e",
      "requestType": "adminAdd",
      "state": "delivered",
      "status": "Delivered",
      "createdDateTime": "2021-01-19T20:02:23.907Z",
      "completedDateTime": "2021-01-19T20:02:40.97Z",
      "schedule": {
        "@odata.type": "microsoft.graph.entitlementManagementSchedule"
      }
    }
  ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/accesspackageassignmentrequest-filterbycurrentuser?view=graph-rest-beta&accept=text/markdown)
