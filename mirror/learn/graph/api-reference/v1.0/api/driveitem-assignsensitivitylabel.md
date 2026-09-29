---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'driveItem: assignSensitivityLabel - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: abhishek-microsoft-2021
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: onedrive
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Asynchronously assign a sensitivity label to a driveItem.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-04-09T00:00:00.0000000Z
locale: en-us
document_id: d2d40aa4-a0ce-5535-aba4-0be24fdf9cde
document_version_independent_id: 9f0b40b0-ef81-00e4-78f4-cc2a1834e068
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/driveitem-assignsensitivitylabel.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/driveitem-assignsensitivitylabel
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/driveitem-assignsensitivitylabel.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 025bbed2-97a9-c4f6-72d5-60c1e9b668d3
---

# driveItem: assignSensitivityLabel - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Asynchronously assign a sensitivity label to a [driveItem](resources/driveitem).

This API is part of the Microsoft SharePoint and OneDrive APIs that perform advanced premium administrative functions, and is considered as protected. Protected APIs require you to have more validations, beyond permission and consent, before you can use them.

For more information about sensitivity labels from an administrator's perspective, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](/en-us/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files?view=o365-worldwide&amp;preserve-view=true).

Note

This is a metered API and some charges for use may apply. For details, see [Overview of metered Microsoft 365 APIs in Microsoft Graph](/en-us/graph/metered-api-overview). Before you call this API, you must [Enable metered APIs and services in Microsoft Graph](/en-us/graph/metered-api-setup?tabs=azurecloudshell).

This API applies sensitivity labels to files at rest. Office clients don't apply watermarks, headers, or footers to files that contain the label information. For more information about sensitivity labels from an administrator's perspective, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](/en-us/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files?view=o365-worldwide&amp;preserve-view=true).

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | Files.ReadWrite.All | Sites.ReadWrite.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Files.ReadWrite.All | Sites.ReadWrite.All |

Note

For Microsoft SharePoint Embedded containers, application-only requests require the `appliedByUser` parameter.

## HTTP request

```http
POST /drives/{drive-id}/items/{item-id}/assignSensitivityLabel
POST /drives/{drive-id}/root:/{item-path}:/assignSensitivityLabel
POST /groups/{group-id}/drive/items/{item-id}/assignSensitivityLabel
POST /groups/{group-id}/drive/root:/{item-path}:/assignSensitivityLabel
POST /me/drive/items/{item-id}/assignSensitivityLabel
POST /me/drive/root:/{item-path}:/assignSensitivityLabel
POST /sites/{site-id}/drive/items/{item-id}/assignSensitivityLabel
POST /sites/{site-id}/drive/root:/{item-path}:/assignSensitivityLabel
POST /users/{user-id}/drive/items/{item-id}/assignSensitivityLabel
POST /users/{user-id}/drive/root:/{item-path}:/assignSensitivityLabel
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

In the request body, provide the ID for the sensitivity label that is to be assigned to a given file. The following table lists the required and optional input parameters.

| Name | Value | Description |
| --- | --- | --- |
| sensitivityLabelId | String | Required. ID of the sensitivity label to be assigned, or empty string to remove the sensitivity label. |
| assignmentMethod | [sensitivityLabelAssignmentMethod](/en-us/graph/api/resources/sensitivitylabelassignment?view=graph-rest-1.0&amp;preserve-view=true#sensitivitylabelassignmentmethod-values) | Optional. The assignment method of the label on the document. Indicates whether the assignment of the label was done automatically, standard, or as a privileged operation (the equivalent of an administrator operation). |
| justificationText | String | Optional. Justification text for audit purposes. Required when downgrading or removing a label. |
| appliedByUser | [userIdentity](/en-us/graph/api/resources/useridentity?view=graph-rest-1.0&amp;preserve-view=true) | Optional. The identity of the user on whose behalf the label is applied. Supported only in application (app-only) context. Specify either `id` (Microsoft Entra object ID) or `userPrincipalName`. |

## Response

If successful, the API returns a `202 Accepted` HTTP response code with an empty response body. The `Location` header provides the URL to get operation details. For more information about how to monitor the progress of an assignSensitivityLabel operation, see [monitoring long-running operations](/en-us/graph/long-running-actions-overview).

In addition to general errors that apply to Microsoft Graph, this API returns the `423 Locked` response code, which indicates that the file being accessed is locked. In such cases, the **code** property of the response object indicates the error type that blocks the operation. Also, some IRM Protected sensitivity labels can't be updated in app-only mode and need delegated user access to validate if the user has proper rights, and for these scenarios the API returns a `Not Supported` response code.

The following table lists the possible values for the error types.

| Value | Description |
| --- | --- |
| fileDoubleKeyEncrypted | Indicates that the file is protected via double key encryption; therefore, it can't be opened. |
| fileDecryptionNotSupported | Indicates that the encrypted file has specific properties that don't allow these files to be opened by SharePoint. |
| fileDecryptionDeferred | Indicates that the file is being processed for decryption; therefore, it can't be opened. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

## Examples

### Example 1: Assign a sensitivity label

#### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/drive/root/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel
Content-Type: application/json

{
  "sensitivityLabelId": "5feba255-812e-446a-ac59-a7044ef827b5",
  "assignmentMethod": "standard",
  "justificationText": "test_justification"
}
```

# [C#](#tab/csharp)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const assignSensitivityLabel = {
  sensitivityLabelId: '5feba255-812e-446a-ac59-a7044ef827b5',
  assignmentMethod: 'standard',
  justificationText: 'test_justification'
};

await client.api('/drive/root/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel').post(assignSensitivityLabel);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```
Snippet not available
```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

```http
HTTP/1.1 202 Accepted
Location: https://contoso.sharepoint.com/_api/v2.0/monitor/QXNzaWduU2Vuc2l0aXZpdHlMYWJlbCxiMzc3ODY3OS04OWQ3LTRkYmYtYjg0MC1jYWM1NzRhY2FlNmE?tempAuth=eyJ0eXAiOiJKV1QiLCJhb....
```

The value of the `Location` header provides a URL for a service that returns the current state of the assignSensitivityLabel operation. You can use this information to [determine when the assignSensitivityLabel operation finishes](/en-us/graph/long-running-actions-overview).

### Example 2: Assign a sensitivity label on behalf of a user (app-only)

#### Request

The following example shows an app-only request that assigns a label on behalf of a specific user, identified by Microsoft Entra object ID.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/drives/{drive-id}/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel
Content-Type: application/json

{
  "sensitivityLabelId": "5feba255-812e-446a-ac59-a7044ef827b5",
  "assignmentMethod": "standard",
  "justificationText": "test_justification",
  "appliedByUser": {
    "id": "4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b"
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Drives.Item.Items.Item.AssignSensitivityLabel;
using Microsoft.Graph.Models;
using Microsoft.Kiota.Abstractions.Serialization;

var requestBody = new AssignSensitivityLabelPostRequestBody
{SensitivityLabelId = "5feba255-812e-446a-ac59-a7044ef827b5",AssignmentMethod = SensitivityLabelAssignmentMethod.Standard,JustificationText = "test_justification",AdditionalData = new Dictionary<string, object>{	{		"appliedByUser" , new UntypedObject(new Dictionary<string, UntypedNode>		{			{				"id", new UntypedString("4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b")			},		})	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Drives["{drive-id}"].Items["{driveItem-id}"].AssignSensitivityLabel.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphdrives "github.com/microsoftgraph/msgraph-sdk-go/drives"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphdrives.NewAssignSensitivityLabelPostRequestBody()
sensitivityLabelId := "5feba255-812e-446a-ac59-a7044ef827b5"
requestBody.SetSensitivityLabelId(&sensitivityLabelId) 
assignmentMethod := graphmodels.STANDARD_SENSITIVITYLABELASSIGNMENTMETHOD 
requestBody.SetAssignmentMethod(&assignmentMethod) 
justificationText := "test_justification"
requestBody.SetJustificationText(&justificationText) 
additionalData := map[string]interface{}{
appliedByUser := graph.New()
id := "4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b"
appliedByUser.SetId(&id) requestBody.SetAppliedByUser(appliedByUser)
}
requestBody.SetAdditionalData(additionalData)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Drives().ByDriveId("drive-id").Items().ByDriveItemId("driveItem-id").AssignSensitivityLabel().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.drives.item.items.item.assignsensitivitylabel.AssignSensitivityLabelPostRequestBody assignSensitivityLabelPostRequestBody = new com.microsoft.graph.drives.item.items.item.assignsensitivitylabel.AssignSensitivityLabelPostRequestBody();
assignSensitivityLabelPostRequestBody.setSensitivityLabelId("5feba255-812e-446a-ac59-a7044ef827b5");
assignSensitivityLabelPostRequestBody.setAssignmentMethod(SensitivityLabelAssignmentMethod.Standard);
assignSensitivityLabelPostRequestBody.setJustificationText("test_justification");
HashMap<String, Object> additionalData = new HashMap<String, Object>();
 appliedByUser = new ();
appliedByUser.setId("4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b");
additionalData.put("appliedByUser", appliedByUser);
assignSensitivityLabelPostRequestBody.setAdditionalData(additionalData);
graphClient.drives().byDriveId("{drive-id}").items().byDriveItemId("{driveItem-id}").assignSensitivityLabel().post(assignSensitivityLabelPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const assignSensitivityLabel = {
  sensitivityLabelId: '5feba255-812e-446a-ac59-a7044ef827b5',
  assignmentMethod: 'standard',
  justificationText: 'test_justification',
  appliedByUser: {
    id: '4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b'
  }
};

await client.api('/drives/{drive-id}/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel').post(assignSensitivityLabel);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Drives\Item\Items\Item\AssignSensitivityLabel\AssignSensitivityLabelPostRequestBody;
use Microsoft\Graph\Generated\Models\SensitivityLabelAssignmentMethod;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new AssignSensitivityLabelPostRequestBody();
$requestBody->setSensitivityLabelId('5feba255-812e-446a-ac59-a7044ef827b5');
$requestBody->setAssignmentMethod(new SensitivityLabelAssignmentMethod('standard'));
$requestBody->setJustificationText('test_justification');
$additionalData = ['appliedByUser' => [	'id' => '4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b',],
];
$requestBody->setAdditionalData($additionalData);

$graphServiceClient->drives()->byDriveId('drive-id')->items()->byDriveItemId('driveItem-id')->assignSensitivityLabel()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Files

$params = @{sensitivityLabelId = "5feba255-812e-446a-ac59-a7044ef827b5"assignmentMethod = "standard"justificationText = "test_justification"appliedByUser = @{	id = "4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b"}
}

Set-MgDriveItemSensitivityLabel -DriveId $driveId -DriveItemId $driveItemId -BodyParameter $params

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.drives.item.items.item.assign_sensitivity_label.assign_sensitivity_label_post_request_body import AssignSensitivityLabelPostRequestBody
from msgraph.generated.models.sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = AssignSensitivityLabelPostRequestBody(sensitivity_label_id = "5feba255-812e-446a-ac59-a7044ef827b5",assignment_method = SensitivityLabelAssignmentMethod.Standard,justification_text = "test_justification",additional_data = {		"applied_by_user" : {				"id" : "4a2ec3c4-1b2d-3e4f-5a6b-7c8d9e0f1a2b",		},}
)

await graph_client.drives.by_drive_id('drive-id').items.by_drive_item_id('driveItem-id').assign_sensitivity_label.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

```http
HTTP/1.1 202 Accepted
Location: https://contoso.sharepoint.com/_api/v2.0/monitor/QXNzaWduU2Vuc2l0aXZpdHlMYWJlbCxiMzc3ODY3OS04OWQ3LTRkYmYtYjg0MC1jYWM1NzRhY2FlNmE?tempAuth=******
```

### Example 3: Assign a sensitivity label on behalf of a user using a user principal name (app-only)

#### Request

The following example shows an app-only request that identifies the user by their user principal name.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/drives/{drive-id}/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel
Content-Type: application/json

{
  "sensitivityLabelId": "5feba255-812e-446a-ac59-a7044ef827b5",
  "assignmentMethod": "standard",
  "justificationText": "test_justification",
  "appliedByUser": {
    "userPrincipalName": "adelev@contoso.com"
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Drives.Item.Items.Item.AssignSensitivityLabel;
using Microsoft.Graph.Models;
using Microsoft.Kiota.Abstractions.Serialization;

var requestBody = new AssignSensitivityLabelPostRequestBody
{SensitivityLabelId = "5feba255-812e-446a-ac59-a7044ef827b5",AssignmentMethod = SensitivityLabelAssignmentMethod.Standard,JustificationText = "test_justification",AdditionalData = new Dictionary<string, object>{	{		"appliedByUser" , new UntypedObject(new Dictionary<string, UntypedNode>		{			{				"userPrincipalName", new UntypedString("adelev@contoso.com")			},		})	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Drives["{drive-id}"].Items["{driveItem-id}"].AssignSensitivityLabel.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphdrives "github.com/microsoftgraph/msgraph-sdk-go/drives"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphdrives.NewAssignSensitivityLabelPostRequestBody()
sensitivityLabelId := "5feba255-812e-446a-ac59-a7044ef827b5"
requestBody.SetSensitivityLabelId(&sensitivityLabelId) 
assignmentMethod := graphmodels.STANDARD_SENSITIVITYLABELASSIGNMENTMETHOD 
requestBody.SetAssignmentMethod(&assignmentMethod) 
justificationText := "test_justification"
requestBody.SetJustificationText(&justificationText) 
additionalData := map[string]interface{}{
appliedByUser := graph.New()
userPrincipalName := "adelev@contoso.com"
appliedByUser.SetUserPrincipalName(&userPrincipalName) requestBody.SetAppliedByUser(appliedByUser)
}
requestBody.SetAdditionalData(additionalData)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Drives().ByDriveId("drive-id").Items().ByDriveItemId("driveItem-id").AssignSensitivityLabel().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.drives.item.items.item.assignsensitivitylabel.AssignSensitivityLabelPostRequestBody assignSensitivityLabelPostRequestBody = new com.microsoft.graph.drives.item.items.item.assignsensitivitylabel.AssignSensitivityLabelPostRequestBody();
assignSensitivityLabelPostRequestBody.setSensitivityLabelId("5feba255-812e-446a-ac59-a7044ef827b5");
assignSensitivityLabelPostRequestBody.setAssignmentMethod(SensitivityLabelAssignmentMethod.Standard);
assignSensitivityLabelPostRequestBody.setJustificationText("test_justification");
HashMap<String, Object> additionalData = new HashMap<String, Object>();
 appliedByUser = new ();
appliedByUser.setUserPrincipalName("adelev@contoso.com");
additionalData.put("appliedByUser", appliedByUser);
assignSensitivityLabelPostRequestBody.setAdditionalData(additionalData);
graphClient.drives().byDriveId("{drive-id}").items().byDriveItemId("{driveItem-id}").assignSensitivityLabel().post(assignSensitivityLabelPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const assignSensitivityLabel = {
  sensitivityLabelId: '5feba255-812e-446a-ac59-a7044ef827b5',
  assignmentMethod: 'standard',
  justificationText: 'test_justification',
  appliedByUser: {
    userPrincipalName: 'adelev@contoso.com'
  }
};

await client.api('/drives/{drive-id}/items/016GVDAP3RCQS5VBQHORFIVU2ZMOSBL25U/assignSensitivityLabel').post(assignSensitivityLabel);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Drives\Item\Items\Item\AssignSensitivityLabel\AssignSensitivityLabelPostRequestBody;
use Microsoft\Graph\Generated\Models\SensitivityLabelAssignmentMethod;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new AssignSensitivityLabelPostRequestBody();
$requestBody->setSensitivityLabelId('5feba255-812e-446a-ac59-a7044ef827b5');
$requestBody->setAssignmentMethod(new SensitivityLabelAssignmentMethod('standard'));
$requestBody->setJustificationText('test_justification');
$additionalData = ['appliedByUser' => [	'userPrincipalName' => 'adelev@contoso.com',],
];
$requestBody->setAdditionalData($additionalData);

$graphServiceClient->drives()->byDriveId('drive-id')->items()->byDriveItemId('driveItem-id')->assignSensitivityLabel()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Files

$params = @{sensitivityLabelId = "5feba255-812e-446a-ac59-a7044ef827b5"assignmentMethod = "standard"justificationText = "test_justification"appliedByUser = @{	userPrincipalName = "adelev@contoso.com"}
}

Set-MgDriveItemSensitivityLabel -DriveId $driveId -DriveItemId $driveItemId -BodyParameter $params

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.drives.item.items.item.assign_sensitivity_label.assign_sensitivity_label_post_request_body import AssignSensitivityLabelPostRequestBody
from msgraph.generated.models.sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = AssignSensitivityLabelPostRequestBody(sensitivity_label_id = "5feba255-812e-446a-ac59-a7044ef827b5",assignment_method = SensitivityLabelAssignmentMethod.Standard,justification_text = "test_justification",additional_data = {		"applied_by_user" : {				"user_principal_name" : "adelev@contoso.com",		},}
)

await graph_client.drives.by_drive_id('drive-id').items.by_drive_item_id('driveItem-id').assign_sensitivity_label.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

```http
HTTP/1.1 202 Accepted
Location: https://contoso.sharepoint.com/_api/v2.0/monitor/QXNzaWduU2Vuc2l0aXZpdHlMYWJlbCxiMzc3ODY3OS04OWQ3LTRkYmYtYjg0MC1jYWM1NzRhY2FlNmE?tempAuth=******
```

### Remarks

The response from the API only indicates that the assignSensitivityLabel operation was accepted or rejected. The operation might be rejected, for example, if the file type isn't supported, or the file is double encrypted. Audit events for both success and failure cases are logged. For more information, see [Audit log activities](/en-us/purview/audit-log-activities#sensitivity-label-activities).

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-beta&accept=text/markdown)
