---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: List Microsoft 365 capabilities for default policy - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: lasharma
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Get a list of Microsoft 365 cross-tenant capabilities configured for the default cross-tenant access policy.
ms.date: 2026-08-07T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
toc.title: List Microsoft 365 capabilities
locale: en-us
document_id: f80d805a-521c-c603-4171-f492f039cdd0
document_version_independent_id: c2317eeb-6a4b-bc93-d368-066f59c585f8
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 175e99fb-2ffc-47b2-b9c6-4bb7fbb3cbfb
---

# List Microsoft 365 capabilities for default policy - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Get a list of Microsoft 365 cross-tenant capabilities configured for the [default cross-tenant access policy](resources/crosstenantaccesspolicyconfigurationdefault). The returned collection is a heterogeneous collection of derived types of [m365CapabilityBase](resources/m365capabilitybase), differentiated by their **@odata.type** property.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | Policy.Read.All | Policy.ReadWrite.CrossTenantCapability |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Policy.Read.All | Policy.ReadWrite.CrossTenantCapability |

Important

For delegated access using work or school accounts where the signed-in user is acting on another user, they must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. Managing Microsoft 365 cross-tenant capabilities affects the entire cross-tenant access policy, so no lower-privileged built-in role covers all capabilities. This operation supports the following built-in roles:

- Global Administrator - required for all capabilities, because managing the cross-tenant access policy requires directory-wide privileges.
- Exchange Administrator - supported only for the MailTips, Calendar Sharing, and Free/Busy capabilities.

## HTTP request

```http
GET /policies/crossTenantAccessPolicy/default/m365Capabilities
```

## Optional query parameters

This method supports the `$select`, `$filter`, `$top`, `$skip`, and `$count`[OData query parameters](/en-us/graph/query-parameters) to help customize the response.

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [m365CapabilityBase](resources/m365capabilitybase) objects in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
GET https://graph.microsoft.com/v1.0/policies/crossTenantAccessPolicy/default/m365Capabilities
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Policies.CrossTenantAccessPolicy.Default.M365Capabilities.GetAsync();

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
m365Capabilities, err := graphClient.Policies().CrossTenantAccessPolicy().Default().M365Capabilities().Get(context.Background(), nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

M365CapabilityBaseCollectionResponse result = graphClient.policies().crossTenantAccessPolicy().defaultEscaped().m365Capabilities().get();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let m365Capabilities = await client.api('/policies/crossTenantAccessPolicy/default/m365Capabilities').get();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->policies()->crossTenantAccessPolicy()->escapedDefault()->m365Capabilities()->get()->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.policies.cross_tenant_access_policy.default.m365_capabilities.get()

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "@odata.type": "#microsoft.graph.crossTenantOpenProfileCard",
      "name": "crossTenantOpenProfileCard",
      "lastModifiedDateTime": "2026-01-15T10:04:11.4531504Z",
      "inboundAccess": {
        "isAllowed": true,
        "resourceScopes": {
          "included": [
            {
              "resourceId": "ad4fc698-74dc-4f62-9e71-ba9b591e8e74",
              "resourceType": "group"
            }
          ],
          "excluded": []
        }
      }
    },
    {
      "@odata.type": "#microsoft.graph.crossTenantMigration",
      "name": "crossTenantMigration",
      "lastModifiedDateTime": "2026-01-15T10:08:08.8321956Z",
      "inboundAccess": {
        "isAllowed": false,
        "resourceScopes": {
          "included": [],
          "excluded": []
        }
      }
    }
  ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities?view=graph-rest-beta&accept=text/markdown)
