---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: Create case activity - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-casemanagement-case-post-activities?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: alfeldsh
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Create a new timeline activity for a security case.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 89136b23-463d-f709-a3e5-2e988cf27363
document_version_independent_id: e2d751e7-fb54-154f-0349-8d6cdc8b9b61
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/security-casemanagement-case-post-activities.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-casemanagement-case-post-activities
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/security-casemanagement-case-post-activities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 48088910-36af-bd43-8595-52719463b2ed
---

# Create case activity - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Create a [comment](resources/security-casemanagement-comment) activity for a [case](resources/security-casemanagement-case).

Note

A case supports a maximum of 100 comments.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | CaseManagement.ReadWrite.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | CaseManagement.ReadWrite.All | Not available. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This API supports the following built-in roles:

- Global Reader
- Security Reader
- Security Operator
- Security Administrator

## HTTP request

```http
POST /security/caseManagement/cases/{caseId}/activities
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, supply a JSON representation of the [microsoft.graph.security.caseManagement.activity](resources/security-casemanagement-activity) object. To create a comment, include `@odata.type` with `#microsoft.graph.security.caseManagement.comment` and the **message** property. Audit log activities are system generated and can't be created by clients.

You can specify the following properties when creating an **activity**.

| Property | Type | Description |
| --- | --- | --- |
| @odata.type | String | The OData type of the concrete activity. To create a comment, use `#microsoft.graph.security.caseManagement.comment`. Required. |
| message | String | The comment body. The maximum length is 1,000 characters for [incident cases](resources/security-casemanagement-incidentcase) and 5,000 characters for [generic cases](resources/security-casemanagement-genericcase). Required. |

## Response

If successful, this method returns a `201 Created` response code and a [microsoft.graph.security.caseManagement.activity](resources/security-casemanagement-activity) object in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/beta/security/caseManagement/cases/{caseId}/activities
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.security.caseManagement.comment",
  "message": "This is a comment for the case."
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Beta.Models.Security.CaseManagement;

var requestBody = new Comment
{OdataType = "#microsoft.graph.security.caseManagement.comment",Message = "This is a comment for the case.",
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Security.CaseManagement.Cases["{case-id}"].Activities.PostAsync(requestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  graphmodelssecuritycasemanagement "github.com/microsoftgraph/msgraph-beta-sdk-go/models/security/casemanagement"  //other-imports
)

requestBody := graphmodelssecuritycasemanagement.NewActivity()
message := "This is a comment for the case."
requestBody.SetMessage(&message) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
activities, err := graphClient.Security().CaseManagement().Cases().ByCaseId("case-id").Activities().Post(context.Background(), requestBody, nil)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.beta.models.security.casemanagement.Comment activity = new com.microsoft.graph.beta.models.security.casemanagement.Comment();
activity.setOdataType("#microsoft.graph.security.caseManagement.comment");
activity.setMessage("This is a comment for the case.");
com.microsoft.graph.models.security.casemanagement.Activity result = graphClient.security().caseManagement().cases().byCaseId("{case-id}").activities().post(activity);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const activity = {
  '@odata.type': '#microsoft.graph.security.caseManagement.comment',
  message: 'This is a comment for the case.'
};

await client.api('/security/caseManagement/cases/{caseId}/activities').version('beta').post(activity);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;
use Microsoft\Graph\Beta\Generated\Models\Security\CaseManagement\Comment;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new Comment();
$requestBody->setOdataType('#microsoft.graph.security.caseManagement.comment');
$requestBody->setMessage('This is a comment for the case.');

$result = $graphServiceClient->security()->caseManagement()->cases()->byCaseId('case-id')->activities()->post($requestBody)->wait();

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Security

$params = @{"@odata.type" = "#microsoft.graph.security.caseManagement.comment"message = "This is a comment for the case."
}

New-MgBetaSecurityCaseManagementCaseActivity -CaseId $caseId -BodyParameter $params

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.models.security.case_management.comment import Comment
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = Comment(odata_type = "#microsoft.graph.security.caseManagement.comment",message = "This is a comment for the case.",
)

result = await graph_client.security.case_management.cases.by_case_id('case-id').activities.post(request_body)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

The following example shows the response.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.security.caseManagement.comment",
  "id": "d2a408d7-9023-4e99-ac69-2e00b36314eb",
  "message": "This is a comment for the case.",
  "createdDateTime": "2026-05-20T11:12:28Z",
  "createdBy": "user@contoso.com",
  "lastModifiedDateTime": "2026-05-20T11:18:45Z",
  "lastModifiedBy": "user@contoso.com"
}
```