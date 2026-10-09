---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'alert: moveAlerts - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-alert-movealerts?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: hareldamti
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Move one or more alerts to an incident.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-05-06T00:00:00.0000000Z
locale: en-us
document_id: b81b59ed-cd8c-e330-984e-68ff15a6b059
document_version_independent_id: 5a31c80e-938f-322d-ea77-11668660b6da
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/security-alert-movealerts.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-alert-movealerts
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/security-alert-movealerts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 545653c1-449f-363b-9f00-3dcd6f10aa38
---

# alert: moveAlerts - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Move one or more [alert](resources/security-alert) resources to a new or existing [incident](resources/security-incident).

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | SecurityData.Manage.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | SecurityData.Manage.All | Not available. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:

- *Security Operator*. Can manage alerts and view, investigate, and respond to security alerts in the Microsoft 365 Defender portal. **This is the least privileged role for this operation.**
- *Security Administrator*. Has permissions to manage security-related features in the Microsoft 365 Defender portal, including managing security threats and alerts.

## HTTP request

```http
POST /security/alerts_v2/moveAlerts
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, provide a JSON object with the following parameters.

| Parameter | Type | Description |
| --- | --- | --- |
| alertIds | String collection | Required. The IDs of the [alerts](resources/security-alert) to move. |
| incidentId | String | Optional. The ID of the target [incident](resources/security-incident). A request with `null` creates a new incident. |
| alertComment | String | Optional. A comment to add when moving the alerts. |
| newCorrelationReasons | [microsoft.graph.security.correlationReason](resources/security-correlationreason) | Optional. The correlation reasons to associate with the move operation. This object is a flags enum that allows multiple values to be specified. |

## Response

If successful, this action returns a `200 OK` response code and a [microsoft.graph.security.mergeResponse](resources/security-mergeresponse) object in the response body.

## Examples

### Example 1: Move alerts to an incident

#### Request

The following example moves two alerts to an existing incident.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/security/alerts_v2/moveAlerts
Content-Type: application/json

{
  "alertIds": [
    "da637551227677560813_-961444813",
    "da637551227677560813_-961444814"
  ],
  "incidentId": "2972395",
  "alertComment": "Moving alerts for investigation consolidation",
  "newCorrelationReasons": "sameAsset, temporalProximity"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Security.Alerts_v2.MicrosoftGraphSecurityMoveAlerts;
using Microsoft.Graph.Models.Security;

var requestBody = new MoveAlertsPostRequestBody
{AlertIds = new List<string>{	"da637551227677560813_-961444813",	"da637551227677560813_-961444814",},IncidentId = "2972395",AlertComment = "Moving alerts for investigation consolidation",NewCorrelationReasons = CorrelationReason.SameAsset | CorrelationReason.TemporalProximity,
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Security.Alerts_v2.MicrosoftGraphSecurityMoveAlerts.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphsecurity "github.com/microsoftgraph/msgraph-sdk-go/security"  graphmodelssecurity "github.com/microsoftgraph/msgraph-sdk-go/models/security"  //other-imports
)

requestBody := graphsecurity.NewMoveAlertsPostRequestBody()
alertIds := []string {"da637551227677560813_-961444813","da637551227677560813_-961444814",
}
requestBody.SetAlertIds(alertIds)
incidentId := "2972395"
requestBody.SetIncidentId(&incidentId) 
alertComment := "Moving alerts for investigation consolidation"
requestBody.SetAlertComment(&alertComment) 
newCorrelationReasons := graphmodels.SAMEASSET, TEMPORALPROXIMITY_CORRELATIONREASON 
requestBody.SetNewCorrelationReasons(&newCorrelationReasons) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
microsoftGraphSecurityMoveAlerts, err := graphClient.Security().Alerts_v2().MicrosoftGraphSecurityMoveAlerts().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.security.alerts_v2.microsoftgraphsecuritymovealerts.MoveAlertsPostRequestBody moveAlertsPostRequestBody = new com.microsoft.graph.security.alerts_v2.microsoftgraphsecuritymovealerts.MoveAlertsPostRequestBody();
LinkedList<String> alertIds = new LinkedList<String>();
alertIds.add("da637551227677560813_-961444813");
alertIds.add("da637551227677560813_-961444814");
moveAlertsPostRequestBody.setAlertIds(alertIds);
moveAlertsPostRequestBody.setIncidentId("2972395");
moveAlertsPostRequestBody.setAlertComment("Moving alerts for investigation consolidation");
moveAlertsPostRequestBody.setNewCorrelationReasons(EnumSet.of(com.microsoft.graph.models.security.CorrelationReason.SameAsset, com.microsoft.graph.models.security.CorrelationReason.TemporalProximity));
var result = graphClient.security().alertsV2().microsoftGraphSecurityMoveAlerts().post(moveAlertsPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const mergeResponse = {
  alertIds: [
    'da637551227677560813_-961444813',
    'da637551227677560813_-961444814'
  ],
  incidentId: '2972395',
  alertComment: 'Moving alerts for investigation consolidation',
  newCorrelationReasons: 'sameAsset, temporalProximity'
};

await client.api('/security/alerts_v2/moveAlerts').post(mergeResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Security\Alerts_v2\MicrosoftGraphSecurityMoveAlerts\MoveAlertsPostRequestBody;
use Microsoft\Graph\Generated\Models\Security\CorrelationReason;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new MoveAlertsPostRequestBody();
$requestBody->setAlertIds(['da637551227677560813_-961444813', 'da637551227677560813_-961444814', 	]);
$requestBody->setIncidentId('2972395');
$requestBody->setAlertComment('Moving alerts for investigation consolidation');
$requestBody->setNewCorrelationReasons(new CorrelationReason('sameAsset, temporalProximity'));

$result = $graphServiceClient->security()->alerts_v2()->microsoftGraphSecurityMoveAlerts()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Security

$params = @{alertIds = @("da637551227677560813_-961444813"
"da637551227677560813_-961444814"
)
incidentId = "2972395"
alertComment = "Moving alerts for investigation consolidation"
newCorrelationReasons = "sameAsset, temporalProximity"
}

Move-MgSecurityAlert -BodyParameter $params

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.security.alerts_v2.microsoft_graph_security_move_alerts.move_alerts_post_request_body import MoveAlertsPostRequestBody
from msgraph.generated.models.correlation_reason import CorrelationReason
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = MoveAlertsPostRequestBody(alert_ids = [	"da637551227677560813_-961444813",	"da637551227677560813_-961444814",],incident_id = "2972395",alert_comment = "Moving alerts for investigation consolidation",new_correlation_reasons = CorrelationReason.SameAsset | CorrelationReason.TemporalProximity,
)

result = await graph_client.security.alerts_v2.microsoft_graph_security_move_alerts.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "targetIncidentId": "2972395"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/security-alert-movealerts?view=graph-rest-beta&accept=text/markdown)
