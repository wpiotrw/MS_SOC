---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'incident: mergeIncidents - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-incident-mergeincidents?view=graph-rest-1.0
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
description: Merge multiple incidents into a single incident.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-05-06T00:00:00.0000000Z
locale: en-us
document_id: de6aa078-3f78-781e-cbf8-04ee21ad09dc
document_version_independent_id: 405cde42-2158-8c70-ce4e-c02a0e25e70f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/security-incident-mergeincidents.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-incident-mergeincidents
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/security-incident-mergeincidents.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: e183aefa-1208-d3bb-fd6e-3294a1d5a627
---

# incident: mergeIncidents - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Merge multiple [incident](resources/security-incident) resources into a single incident.

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
POST /security/incidents/mergeIncidents
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
| incidentIds | String collection | Required. The IDs of the [incidents](resources/security-incident) to merge. |
| incidentComment | String | Optional. A comment to add to the merged incident. |
| mergeReasons | [microsoft.graph.security.correlationReason](resources/security-correlationreason) | Optional. The correlation reasons for merging the incidents. This object is a flags enum that allows multiple values to be specified. |

## Response

If successful, this action returns a `200 OK` response code and a [microsoft.graph.security.mergeResponse](resources/security-mergeresponse) object in the response body.

## Examples

### Example 1: Merge incidents

#### Request

The following example merges two incidents.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/security/incidents/mergeIncidents
Content-Type: application/json

{
  "incidentIds": [
    "2972395",
    "2972396"
  ],
  "incidentComment": "Merging related incidents from the same campaign",
  "mergeReasons": "sameCampaign, sameActor"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Security.Incidents.MicrosoftGraphSecurityMergeIncidents;
using Microsoft.Graph.Models.Security;

var requestBody = new MergeIncidentsPostRequestBody
{IncidentIds = new List<string>{	"2972395",	"2972396",},IncidentComment = "Merging related incidents from the same campaign",MergeReasons = CorrelationReason.SameCampaign | CorrelationReason.SameActor,
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Security.Incidents.MicrosoftGraphSecurityMergeIncidents.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphsecurity "github.com/microsoftgraph/msgraph-sdk-go/security"  graphmodelssecurity "github.com/microsoftgraph/msgraph-sdk-go/models/security"  //other-imports
)

requestBody := graphsecurity.NewMergeIncidentsPostRequestBody()
incidentIds := []string {"2972395","2972396",
}
requestBody.SetIncidentIds(incidentIds)
incidentComment := "Merging related incidents from the same campaign"
requestBody.SetIncidentComment(&incidentComment) 
mergeReasons := graphmodels.SAMECAMPAIGN, SAMEACTOR_CORRELATIONREASON 
requestBody.SetMergeReasons(&mergeReasons) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
microsoftGraphSecurityMergeIncidents, err := graphClient.Security().Incidents().MicrosoftGraphSecurityMergeIncidents().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.security.incidents.microsoftgraphsecuritymergeincidents.MergeIncidentsPostRequestBody mergeIncidentsPostRequestBody = new com.microsoft.graph.security.incidents.microsoftgraphsecuritymergeincidents.MergeIncidentsPostRequestBody();
LinkedList<String> incidentIds = new LinkedList<String>();
incidentIds.add("2972395");
incidentIds.add("2972396");
mergeIncidentsPostRequestBody.setIncidentIds(incidentIds);
mergeIncidentsPostRequestBody.setIncidentComment("Merging related incidents from the same campaign");
mergeIncidentsPostRequestBody.setMergeReasons(EnumSet.of(com.microsoft.graph.models.security.CorrelationReason.SameCampaign, com.microsoft.graph.models.security.CorrelationReason.SameActor));
var result = graphClient.security().incidents().microsoftGraphSecurityMergeIncidents().post(mergeIncidentsPostRequestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const mergeResponse = {
  incidentIds: [
    '2972395',
    '2972396'
  ],
  incidentComment: 'Merging related incidents from the same campaign',
  mergeReasons: 'sameCampaign, sameActor'
};

await client.api('/security/incidents/mergeIncidents').post(mergeResponse);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Security\Incidents\MicrosoftGraphSecurityMergeIncidents\MergeIncidentsPostRequestBody;
use Microsoft\Graph\Generated\Models\Security\CorrelationReason;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new MergeIncidentsPostRequestBody();
$requestBody->setIncidentIds(['2972395', '2972396', 	]);
$requestBody->setIncidentComment('Merging related incidents from the same campaign');
$requestBody->setMergeReasons(new CorrelationReason('sameCampaign, sameActor'));

$result = $graphServiceClient->security()->incidents()->microsoftGraphSecurityMergeIncidents()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Security

$params = @{incidentIds = @("2972395"
"2972396"
)
incidentComment = "Merging related incidents from the same campaign"
mergeReasons = "sameCampaign, sameActor"
}

Merge-MgSecurityIncident -BodyParameter $params

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.security.incidents.microsoft_graph_security_merge_incidents.merge_incidents_post_request_body import MergeIncidentsPostRequestBody
from msgraph.generated.models.correlation_reason import CorrelationReason
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = MergeIncidentsPostRequestBody(incident_ids = [	"2972395",	"2972396",],incident_comment = "Merging related incidents from the same campaign",merge_reasons = CorrelationReason.SameCampaign | CorrelationReason.SameActor,
)

result = await graph_client.security.incidents.microsoft_graph_security_merge_incidents.post(request_body)

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

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/security-incident-mergeincidents?view=graph-rest-beta&accept=text/markdown)
