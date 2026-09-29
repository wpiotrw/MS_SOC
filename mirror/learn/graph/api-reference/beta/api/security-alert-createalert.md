---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: 'alert: createAlert - Microsoft Graph beta | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-alert-createalert?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: a-merberg
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Create a Microsoft 365 Defender alert by invoking a bound action on the alerts_v2 collection.
ms.date: 2026-08-04T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: ea6293d3-b072-2b55-056d-d436a8770e5e
document_version_independent_id: bbdb267a-4a02-4072-1b6c-21090c29fe86
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/security-alert-createalert.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-alert-createalert
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/security-alert-createalert.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 33bb65b4-aab3-00e6-fdf9-013e9b977cfc
---

# alert: createAlert - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Create a Microsoft 365 Defender alert by invoking a bound action on the `alerts_v2` collection and returning the created [alert](resources/security-alert) resource. The action accepts a [createAlertInput](resources/security-createalertinput) complex type that combines alert metadata and creation-specific options in one request object.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | SecurityAlert.Create.All | SecurityAlert.ReadWrite.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | SecurityAlert.Create.All | SecurityAlert.ReadWrite.All |

## HTTP request

```http
POST /security/alerts_v2/createAlert
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, supply a JSON representation of the parameters.

The following table lists the parameters that are required when you call this action.

| Parameter | Type | Description |
| --- | --- | --- |
| createAlertInput | [microsoft.graph.security.createAlertInput](resources/security-createalertinput) | Required. The input containing alert properties, incident-linking options, workspace routing, and inline entity definitions. |

## Response

If successful, this action returns a `201 Created` response code and an [alert](resources/security-alert) object in the response body.

## Examples

### Example 1: Create an alert linked to an existing incident

#### Request

The following example shows a request that creates an alert and links it to incident 42.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/beta/security/alerts_v2/createAlert
Content-Type: application/json

{
  "createAlertInput": {
    "title": "Suspicious PowerShell activity",
    "severity": "medium",
    "description": "PowerShell script execution was identified during analyst triage.",
    "category": "Execution",
    "recommendedActions": "Review the script contents and isolate the affected device.",
    "mitreTechniques": ["T1059.001"],
    "linkToIncident": 42,
    "isExcludedFromCorrelation": false,
    "entityDefinitions": [
      {
        "entityType": "device",
        "entityIdentifier": "deviceId",
        "identifierValue": "d1234567-abcd-4f01-8abc-890123456789",
        "role": "impacted"
      }
    ]
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Beta.Security.Alerts_v2.MicrosoftGraphSecurityCreateAlert;
using Microsoft.Graph.Beta.Models.Security;

var requestBody = new CreateAlertPostRequestBody
{CreateAlertInput = new CreateAlertInput{	Title = "Suspicious PowerShell activity",	Severity = AlertSeverity.Medium,	Description = "PowerShell script execution was identified during analyst triage.",	Category = "Execution",	RecommendedActions = "Review the script contents and isolate the affected device.",	MitreTechniques = new List<string>	{		"T1059.001",	},	LinkToIncident = 42L,	IsExcludedFromCorrelation = false,	EntityDefinitions = new List<EntityDefinition>	{		new EntityDefinition		{			EntityType = ManualAlertEntityType.Device,			EntityIdentifier = "deviceId",			IdentifierValue = "d1234567-abcd-4f01-8abc-890123456789",			Role = EntityDefinitionInputRole.Impacted,		},	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Security.Alerts_v2.MicrosoftGraphSecurityCreateAlert.PostAsync(requestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  graphsecurity "github.com/microsoftgraph/msgraph-beta-sdk-go/security"  graphmodelssecurity "github.com/microsoftgraph/msgraph-beta-sdk-go/models/security"  //other-imports
)

requestBody := graphsecurity.NewCreateAlertPostRequestBody()
createAlertInput := graphmodelssecurity.NewCreateAlertInput()
title := "Suspicious PowerShell activity"
createAlertInput.SetTitle(&title) 
severity := graphmodels.MEDIUM_ALERTSEVERITY 
createAlertInput.SetSeverity(&severity) 
description := "PowerShell script execution was identified during analyst triage."
createAlertInput.SetDescription(&description) 
category := "Execution"
createAlertInput.SetCategory(&category) 
recommendedActions := "Review the script contents and isolate the affected device."
createAlertInput.SetRecommendedActions(&recommendedActions) 
mitreTechniques := []string {"T1059.001",
}
createAlertInput.SetMitreTechniques(mitreTechniques)
linkToIncident := int64(42)
createAlertInput.SetLinkToIncident(&linkToIncident) 
isExcludedFromCorrelation := false
createAlertInput.SetIsExcludedFromCorrelation(&isExcludedFromCorrelation) 

entityDefinition := graphmodelssecurity.NewEntityDefinition()
entityType := graphmodels.DEVICE_MANUALALERTENTITYTYPE 
entityDefinition.SetEntityType(&entityType) 
entityIdentifier := "deviceId"
entityDefinition.SetEntityIdentifier(&entityIdentifier) 
identifierValue := "d1234567-abcd-4f01-8abc-890123456789"
entityDefinition.SetIdentifierValue(&identifierValue) 
role := graphmodels.IMPACTED_ENTITYDEFINITIONINPUTROLE 
entityDefinition.SetRole(&role) 

entityDefinitions := []graphmodelssecurity.EntityDefinitionable {entityDefinition,
}
createAlertInput.SetEntityDefinitions(entityDefinitions)
requestBody.SetCreateAlertInput(createAlertInput)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
microsoftGraphSecurityCreateAlert, err := graphClient.Security().Alerts_v2().MicrosoftGraphSecurityCreateAlert().Post(context.Background(), requestBody, nil)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.beta.security.alerts_v2.microsoftgraphsecuritycreatealert.CreateAlertPostRequestBody createAlertPostRequestBody = new com.microsoft.graph.beta.security.alerts_v2.microsoftgraphsecuritycreatealert.CreateAlertPostRequestBody();
com.microsoft.graph.beta.models.security.CreateAlertInput createAlertInput = new com.microsoft.graph.beta.models.security.CreateAlertInput();
createAlertInput.setTitle("Suspicious PowerShell activity");
createAlertInput.setSeverity(com.microsoft.graph.beta.models.security.AlertSeverity.Medium);
createAlertInput.setDescription("PowerShell script execution was identified during analyst triage.");
createAlertInput.setCategory("Execution");
createAlertInput.setRecommendedActions("Review the script contents and isolate the affected device.");
LinkedList<String> mitreTechniques = new LinkedList<String>();
mitreTechniques.add("T1059.001");
createAlertInput.setMitreTechniques(mitreTechniques);
createAlertInput.setLinkToIncident(42L);
createAlertInput.setIsExcludedFromCorrelation(false);
LinkedList<com.microsoft.graph.beta.models.security.EntityDefinition> entityDefinitions = new LinkedList<com.microsoft.graph.beta.models.security.EntityDefinition>();
com.microsoft.graph.beta.models.security.EntityDefinition entityDefinition = new com.microsoft.graph.beta.models.security.EntityDefinition();
entityDefinition.setEntityType(com.microsoft.graph.beta.models.security.ManualAlertEntityType.Device);
entityDefinition.setEntityIdentifier("deviceId");
entityDefinition.setIdentifierValue("d1234567-abcd-4f01-8abc-890123456789");
entityDefinition.setRole(com.microsoft.graph.beta.models.security.EntityDefinitionInputRole.Impacted);
entityDefinitions.add(entityDefinition);
createAlertInput.setEntityDefinitions(entityDefinitions);
createAlertPostRequestBody.setCreateAlertInput(createAlertInput);
var result = graphClient.security().alertsV2().microsoftGraphSecurityCreateAlert().post(createAlertPostRequestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const alert = {
  createAlertInput: {
    title: 'Suspicious PowerShell activity',
    severity: 'medium',
    description: 'PowerShell script execution was identified during analyst triage.',
    category: 'Execution',
    recommendedActions: 'Review the script contents and isolate the affected device.',
    mitreTechniques: ['T1059.001'],
    linkToIncident: 42,
    isExcludedFromCorrelation: false,
    entityDefinitions: [
      {
        entityType: 'device',
        entityIdentifier: 'deviceId',
        identifierValue: 'd1234567-abcd-4f01-8abc-890123456789',
        role: 'impacted'
      }
    ]
  }
};

await client.api('/security/alerts_v2/createAlert').version('beta').post(alert);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;
use Microsoft\Graph\Beta\Generated\Security\Alerts_v2\MicrosoftGraphSecurityCreateAlert\CreateAlertPostRequestBody;
use Microsoft\Graph\Beta\Generated\Models\Security\CreateAlertInput;
use Microsoft\Graph\Beta\Generated\Models\Security\AlertSeverity;
use Microsoft\Graph\Beta\Generated\Models\Security\EntityDefinition;
use Microsoft\Graph\Beta\Generated\Models\Security\ManualAlertEntityType;
use Microsoft\Graph\Beta\Generated\Models\Security\EntityDefinitionInputRole;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new CreateAlertPostRequestBody();
$createAlertInput = new CreateAlertInput();
$createAlertInput->setTitle('Suspicious PowerShell activity');
$createAlertInput->setSeverity(new AlertSeverity('medium'));
$createAlertInput->setDescription('PowerShell script execution was identified during analyst triage.');
$createAlertInput->setCategory('Execution');
$createAlertInput->setRecommendedActions('Review the script contents and isolate the affected device.');
$createAlertInput->setMitreTechniques(['T1059.001', 	]);
$createAlertInput->setLinkToIncident(42);
$createAlertInput->setIsExcludedFromCorrelation(false);
$entityDefinitionsEntityDefinition1 = new EntityDefinition();
$entityDefinitionsEntityDefinition1->setEntityType(new ManualAlertEntityType('device'));
$entityDefinitionsEntityDefinition1->setEntityIdentifier('deviceId');
$entityDefinitionsEntityDefinition1->setIdentifierValue('d1234567-abcd-4f01-8abc-890123456789');
$entityDefinitionsEntityDefinition1->setRole(new EntityDefinitionInputRole('impacted'));
$entityDefinitionsArray []= $entityDefinitionsEntityDefinition1;
$createAlertInput->setEntityDefinitions($entityDefinitionsArray);

$requestBody->setCreateAlertInput($createAlertInput);

$result = $graphServiceClient->security()->alerts_v2()->microsoftGraphSecurityCreateAlert()->post($requestBody)->wait();

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.security.alerts_v2.microsoft_graph_security_create_alert.create_alert_post_request_body import CreateAlertPostRequestBody
from msgraph_beta.generated.models.security.create_alert_input import CreateAlertInput
from msgraph_beta.generated.models.alert_severity import AlertSeverity
from msgraph_beta.generated.models.security.entity_definition import EntityDefinition
from msgraph_beta.generated.models.manual_alert_entity_type import ManualAlertEntityType
from msgraph_beta.generated.models.entity_definition_input_role import EntityDefinitionInputRole
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = CreateAlertPostRequestBody(create_alert_input = CreateAlertInput(	title = "Suspicious PowerShell activity",	severity = AlertSeverity.Medium,	description = "PowerShell script execution was identified during analyst triage.",	category = "Execution",	recommended_actions = "Review the script contents and isolate the affected device.",	mitre_techniques = [		"T1059.001",	],	link_to_incident = 42,	is_excluded_from_correlation = False,	entity_definitions = [		EntityDefinition(			entity_type = ManualAlertEntityType.Device,			entity_identifier = "deviceId",			identifier_value = "d1234567-abcd-4f01-8abc-890123456789",			role = EntityDefinitionInputRole.Impacted,		),	],),
)

result = await graph_client.security.alerts_v2.microsoft_graph_security_create_alert.post(request_body)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.security.alert",
  "id": "ea2c5e5341-c60a-42fc-953f-3da427c85e2d_aml",
  "providerAlertId": "manual_ea2c5e5341-c60a-42fc-953f-3da427c85e2d",
  "incidentId": "42",
  "title": "Suspicious PowerShell activity",
  "description": "PowerShell script execution was identified during analyst triage.",
  "severity": "medium",
  "status": "new",
  "classification": "unknown",
  "determination": "unknown",
  "category": "Execution",
  "serviceSource": "microsoft365Defender",
  "detectionSource": "manual",
  "createdDateTime": "2026-07-27T11:00:00Z",
  "lastUpdateDateTime": "2026-07-27T11:00:00Z",
  "recommendedActions": "Review the script contents and isolate the affected device.",
  "mitreTechniques": ["T1059.001"],
  "alertWebUrl": "https://security.microsoft.com/alerts/ea2c5e5341-c60a-42fc-953f-3da427c85e2d_aml"
}
```

### Example 2: Create an alert with a new incident

#### Request

The following example shows a request that creates an alert without specifying an incident, causing the backend to create a new incident.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/beta/security/alerts_v2/createAlert
Content-Type: application/json

{
  "createAlertInput": {
    "title": "Unauthorized access attempt",
    "severity": "high",
    "description": "Multiple failed login attempts from an unusual location.",
    "category": "InitialAccess",
    "mitreTechniques": ["T1078"],
    "isExcludedFromCorrelation": false,
    "entityDefinitions": [
      {
        "entityType": "user",
        "entityIdentifier": "userPrincipalName",
        "identifierValue": "admin@contoso.com",
        "role": "impacted"
      },
      {
        "entityType": "ip",
        "entityIdentifier": "address",
        "identifierValue": "198.51.100.42",
        "role": "related"
      }
    ]
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Beta.Security.Alerts_v2.MicrosoftGraphSecurityCreateAlert;
using Microsoft.Graph.Beta.Models.Security;

var requestBody = new CreateAlertPostRequestBody
{CreateAlertInput = new CreateAlertInput{	Title = "Unauthorized access attempt",	Severity = AlertSeverity.High,	Description = "Multiple failed login attempts from an unusual location.",	Category = "InitialAccess",	MitreTechniques = new List<string>	{		"T1078",	},	IsExcludedFromCorrelation = false,	EntityDefinitions = new List<EntityDefinition>	{		new EntityDefinition		{			EntityType = ManualAlertEntityType.User,			EntityIdentifier = "userPrincipalName",			IdentifierValue = "admin@contoso.com",			Role = EntityDefinitionInputRole.Impacted,		},		new EntityDefinition		{			EntityType = ManualAlertEntityType.Ip,			EntityIdentifier = "address",			IdentifierValue = "198.51.100.42",			Role = EntityDefinitionInputRole.Related,		},	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Security.Alerts_v2.MicrosoftGraphSecurityCreateAlert.PostAsync(requestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  graphsecurity "github.com/microsoftgraph/msgraph-beta-sdk-go/security"  graphmodelssecurity "github.com/microsoftgraph/msgraph-beta-sdk-go/models/security"  //other-imports
)

requestBody := graphsecurity.NewCreateAlertPostRequestBody()
createAlertInput := graphmodelssecurity.NewCreateAlertInput()
title := "Unauthorized access attempt"
createAlertInput.SetTitle(&title) 
severity := graphmodels.HIGH_ALERTSEVERITY 
createAlertInput.SetSeverity(&severity) 
description := "Multiple failed login attempts from an unusual location."
createAlertInput.SetDescription(&description) 
category := "InitialAccess"
createAlertInput.SetCategory(&category) 
mitreTechniques := []string {"T1078",
}
createAlertInput.SetMitreTechniques(mitreTechniques)
isExcludedFromCorrelation := false
createAlertInput.SetIsExcludedFromCorrelation(&isExcludedFromCorrelation) 

entityDefinition := graphmodelssecurity.NewEntityDefinition()
entityType := graphmodels.USER_MANUALALERTENTITYTYPE 
entityDefinition.SetEntityType(&entityType) 
entityIdentifier := "userPrincipalName"
entityDefinition.SetEntityIdentifier(&entityIdentifier) 
identifierValue := "admin@contoso.com"
entityDefinition.SetIdentifierValue(&identifierValue) 
role := graphmodels.IMPACTED_ENTITYDEFINITIONINPUTROLE 
entityDefinition.SetRole(&role) 
entityDefinition1 := graphmodelssecurity.NewEntityDefinition()
entityType := graphmodels.IP_MANUALALERTENTITYTYPE 
entityDefinition1.SetEntityType(&entityType) 
entityIdentifier := "address"
entityDefinition1.SetEntityIdentifier(&entityIdentifier) 
identifierValue := "198.51.100.42"
entityDefinition1.SetIdentifierValue(&identifierValue) 
role := graphmodels.RELATED_ENTITYDEFINITIONINPUTROLE 
entityDefinition1.SetRole(&role) 

entityDefinitions := []graphmodelssecurity.EntityDefinitionable {entityDefinition,entityDefinition1,
}
createAlertInput.SetEntityDefinitions(entityDefinitions)
requestBody.SetCreateAlertInput(createAlertInput)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
microsoftGraphSecurityCreateAlert, err := graphClient.Security().Alerts_v2().MicrosoftGraphSecurityCreateAlert().Post(context.Background(), requestBody, nil)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.beta.security.alerts_v2.microsoftgraphsecuritycreatealert.CreateAlertPostRequestBody createAlertPostRequestBody = new com.microsoft.graph.beta.security.alerts_v2.microsoftgraphsecuritycreatealert.CreateAlertPostRequestBody();
com.microsoft.graph.beta.models.security.CreateAlertInput createAlertInput = new com.microsoft.graph.beta.models.security.CreateAlertInput();
createAlertInput.setTitle("Unauthorized access attempt");
createAlertInput.setSeverity(com.microsoft.graph.beta.models.security.AlertSeverity.High);
createAlertInput.setDescription("Multiple failed login attempts from an unusual location.");
createAlertInput.setCategory("InitialAccess");
LinkedList<String> mitreTechniques = new LinkedList<String>();
mitreTechniques.add("T1078");
createAlertInput.setMitreTechniques(mitreTechniques);
createAlertInput.setIsExcludedFromCorrelation(false);
LinkedList<com.microsoft.graph.beta.models.security.EntityDefinition> entityDefinitions = new LinkedList<com.microsoft.graph.beta.models.security.EntityDefinition>();
com.microsoft.graph.beta.models.security.EntityDefinition entityDefinition = new com.microsoft.graph.beta.models.security.EntityDefinition();
entityDefinition.setEntityType(com.microsoft.graph.beta.models.security.ManualAlertEntityType.User);
entityDefinition.setEntityIdentifier("userPrincipalName");
entityDefinition.setIdentifierValue("admin@contoso.com");
entityDefinition.setRole(com.microsoft.graph.beta.models.security.EntityDefinitionInputRole.Impacted);
entityDefinitions.add(entityDefinition);
com.microsoft.graph.beta.models.security.EntityDefinition entityDefinition1 = new com.microsoft.graph.beta.models.security.EntityDefinition();
entityDefinition1.setEntityType(com.microsoft.graph.beta.models.security.ManualAlertEntityType.Ip);
entityDefinition1.setEntityIdentifier("address");
entityDefinition1.setIdentifierValue("198.51.100.42");
entityDefinition1.setRole(com.microsoft.graph.beta.models.security.EntityDefinitionInputRole.Related);
entityDefinitions.add(entityDefinition1);
createAlertInput.setEntityDefinitions(entityDefinitions);
createAlertPostRequestBody.setCreateAlertInput(createAlertInput);
var result = graphClient.security().alertsV2().microsoftGraphSecurityCreateAlert().post(createAlertPostRequestBody);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const alert = {
  createAlertInput: {
    title: 'Unauthorized access attempt',
    severity: 'high',
    description: 'Multiple failed login attempts from an unusual location.',
    category: 'InitialAccess',
    mitreTechniques: ['T1078'],
    isExcludedFromCorrelation: false,
    entityDefinitions: [
      {
        entityType: 'user',
        entityIdentifier: 'userPrincipalName',
        identifierValue: 'admin@contoso.com',
        role: 'impacted'
      },
      {
        entityType: 'ip',
        entityIdentifier: 'address',
        identifierValue: '198.51.100.42',
        role: 'related'
      }
    ]
  }
};

await client.api('/security/alerts_v2/createAlert').version('beta').post(alert);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;
use Microsoft\Graph\Beta\Generated\Security\Alerts_v2\MicrosoftGraphSecurityCreateAlert\CreateAlertPostRequestBody;
use Microsoft\Graph\Beta\Generated\Models\Security\CreateAlertInput;
use Microsoft\Graph\Beta\Generated\Models\Security\AlertSeverity;
use Microsoft\Graph\Beta\Generated\Models\Security\EntityDefinition;
use Microsoft\Graph\Beta\Generated\Models\Security\ManualAlertEntityType;
use Microsoft\Graph\Beta\Generated\Models\Security\EntityDefinitionInputRole;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new CreateAlertPostRequestBody();
$createAlertInput = new CreateAlertInput();
$createAlertInput->setTitle('Unauthorized access attempt');
$createAlertInput->setSeverity(new AlertSeverity('high'));
$createAlertInput->setDescription('Multiple failed login attempts from an unusual location.');
$createAlertInput->setCategory('InitialAccess');
$createAlertInput->setMitreTechniques(['T1078', 	]);
$createAlertInput->setIsExcludedFromCorrelation(false);
$entityDefinitionsEntityDefinition1 = new EntityDefinition();
$entityDefinitionsEntityDefinition1->setEntityType(new ManualAlertEntityType('user'));
$entityDefinitionsEntityDefinition1->setEntityIdentifier('userPrincipalName');
$entityDefinitionsEntityDefinition1->setIdentifierValue('admin@contoso.com');
$entityDefinitionsEntityDefinition1->setRole(new EntityDefinitionInputRole('impacted'));
$entityDefinitionsArray []= $entityDefinitionsEntityDefinition1;
$entityDefinitionsEntityDefinition2 = new EntityDefinition();
$entityDefinitionsEntityDefinition2->setEntityType(new ManualAlertEntityType('ip'));
$entityDefinitionsEntityDefinition2->setEntityIdentifier('address');
$entityDefinitionsEntityDefinition2->setIdentifierValue('198.51.100.42');
$entityDefinitionsEntityDefinition2->setRole(new EntityDefinitionInputRole('related'));
$entityDefinitionsArray []= $entityDefinitionsEntityDefinition2;
$createAlertInput->setEntityDefinitions($entityDefinitionsArray);

$requestBody->setCreateAlertInput($createAlertInput);

$result = $graphServiceClient->security()->alerts_v2()->microsoftGraphSecurityCreateAlert()->post($requestBody)->wait();

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.security.alerts_v2.microsoft_graph_security_create_alert.create_alert_post_request_body import CreateAlertPostRequestBody
from msgraph_beta.generated.models.security.create_alert_input import CreateAlertInput
from msgraph_beta.generated.models.alert_severity import AlertSeverity
from msgraph_beta.generated.models.security.entity_definition import EntityDefinition
from msgraph_beta.generated.models.manual_alert_entity_type import ManualAlertEntityType
from msgraph_beta.generated.models.entity_definition_input_role import EntityDefinitionInputRole
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = CreateAlertPostRequestBody(create_alert_input = CreateAlertInput(	title = "Unauthorized access attempt",	severity = AlertSeverity.High,	description = "Multiple failed login attempts from an unusual location.",	category = "InitialAccess",	mitre_techniques = [		"T1078",	],	is_excluded_from_correlation = False,	entity_definitions = [		EntityDefinition(			entity_type = ManualAlertEntityType.User,			entity_identifier = "userPrincipalName",			identifier_value = "admin@contoso.com",			role = EntityDefinitionInputRole.Impacted,		),		EntityDefinition(			entity_type = ManualAlertEntityType.Ip,			entity_identifier = "address",			identifier_value = "198.51.100.42",			role = EntityDefinitionInputRole.Related,		),	],),
)

result = await graph_client.security.alerts_v2.microsoft_graph_security_create_alert.post(request_body)

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.security.alert",
  "id": "bf3c9e7812-a45b-44dc-8e2f-1a2b3c4d5e6f_aml",
  "providerAlertId": "manual_bf3c9e7812-a45b-44dc-8e2f-1a2b3c4d5e6f",
  "incidentId": "128",
  "title": "Unauthorized access attempt",
  "severity": "high",
  "status": "new",
  "category": "InitialAccess",
  "serviceSource": "microsoft365Defender",
  "detectionSource": "manual",
  "createdDateTime": "2026-07-27T12:30:00Z",
  "lastUpdateDateTime": "2026-07-27T12:30:00Z",
  "alertWebUrl": "https://security.microsoft.com/alerts/bf3c9e7812-a45b-44dc-8e2f-1a2b3c4d5e6f_aml"
}
```