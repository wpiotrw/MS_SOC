---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: Create externalOriginResourceConnector - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/entitlementmanagement-post-externaloriginresourceconnectors?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vikama-microsoft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Create a new externalOriginResourceConnector object.
ms.date: 2026-07-22T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 39569237-0f32-1b6f-5fbe-e58c2447537b
document_version_independent_id: 8092ca11-5b9a-97c4-522e-faea04586337
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/entitlementmanagement-post-externaloriginresourceconnectors.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/entitlementmanagement-post-externaloriginresourceconnectors
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/entitlementmanagement-post-externaloriginresourceconnectors.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: b3f35b83-1a49-e04c-b39a-731e0b222347
---

# Create externalOriginResourceConnector - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Creates a new [externalOriginResourceConnector](resources/externaloriginresourceconnector) object.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | EntitlementManagement.ReadWrite.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | EntitlementManagement.ReadWrite.All | Not available. |

## HTTP request

```http
POST /identityGovernance/entitlementManagement/externalOriginResourceConnectors
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, supply a JSON representation of the [externalOriginResourceConnector](resources/externaloriginresourceconnector) object.

You can specify the following properties when creating an **externalOriginResourceConnector**.

| Property | Type | Description |
| --- | --- | --- |
| connectionInfo | [connectionInfo](resources/connectioninfo) | The connection information for the external origin resource connector. Required. |
| connectorType | connectorType | The type of connector. The possible values are: `sapIag`, `unknownFutureValue`. Required. |
| description | String | The description of the external origin resource connector. Required. |
| displayName | String | The display name of the external origin resource connector. Required. |

## Response

If successful, this method returns a `201 Created` response code and an [externalOriginResourceConnector](resources/externaloriginresourceconnector) object in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/identityGovernance/entitlementManagement/externalOriginResourceConnectors
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.externalOriginResourceConnector",
  "displayName": "SAP IAG Connector",
  "description": "This connector helps integrate Microsoft Entra with SAP IAG",
  "connectorType": "sapIag",
  "connectionInfo": {
    "@odata.type": "microsoft.graph.externalTokenBasedSapIagConnectionInfo",
    "url": "https://contoso.example.com",
    "accessTokenUrl": "https://contoso.example.com/oauth/token",
    "clientId": "e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29",
    "keyVaultName": "Keyvault",
    "secretName": "clientSecret",
    "subscriptionId": "5ee98b73-d9df-43a7-8a92-36855054bdee",
    "resourceGroup": "SAP IAG Group"
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

var requestBody = new ExternalOriginResourceConnector
{OdataType = "#microsoft.graph.externalOriginResourceConnector",DisplayName = "SAP IAG Connector",Description = "This connector helps integrate Microsoft Entra with SAP IAG",ConnectorType = ConnectorType.SapIag,ConnectionInfo = new ExternalTokenBasedSapIagConnectionInfo{	OdataType = "microsoft.graph.externalTokenBasedSapIagConnectionInfo",	Url = "https://contoso.example.com",	AccessTokenUrl = "https://contoso.example.com/oauth/token",	ClientId = "e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29",	KeyVaultName = "Keyvault",	SecretName = "clientSecret",	SubscriptionId = "5ee98b73-d9df-43a7-8a92-36855054bdee",	ResourceGroup = "SAP IAG Group",},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.IdentityGovernance.EntitlementManagement.ExternalOriginResourceConnectors.PostAsync(requestBody);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewExternalOriginResourceConnector()
displayName := "SAP IAG Connector"
requestBody.SetDisplayName(&displayName) 
description := "This connector helps integrate Microsoft Entra with SAP IAG"
requestBody.SetDescription(&description) 
connectorType := graphmodels.SAPIAG_CONNECTORTYPE 
requestBody.SetConnectorType(&connectorType) 
connectionInfo := graphmodels.NewExternalTokenBasedSapIagConnectionInfo()
url := "https://contoso.example.com"
connectionInfo.SetUrl(&url) 
accessTokenUrl := "https://contoso.example.com/oauth/token"
connectionInfo.SetAccessTokenUrl(&accessTokenUrl) 
clientId := "e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29"
connectionInfo.SetClientId(&clientId) 
keyVaultName := "Keyvault"
connectionInfo.SetKeyVaultName(&keyVaultName) 
secretName := "clientSecret"
connectionInfo.SetSecretName(&secretName) 
subscriptionId := "5ee98b73-d9df-43a7-8a92-36855054bdee"
connectionInfo.SetSubscriptionId(&subscriptionId) 
resourceGroup := "SAP IAG Group"
connectionInfo.SetResourceGroup(&resourceGroup) 
requestBody.SetConnectionInfo(connectionInfo)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
externalOriginResourceConnectors, err := graphClient.IdentityGovernance().EntitlementManagement().ExternalOriginResourceConnectors().Post(context.Background(), requestBody, nil)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

ExternalOriginResourceConnector externalOriginResourceConnector = new ExternalOriginResourceConnector();
externalOriginResourceConnector.setOdataType("#microsoft.graph.externalOriginResourceConnector");
externalOriginResourceConnector.setDisplayName("SAP IAG Connector");
externalOriginResourceConnector.setDescription("This connector helps integrate Microsoft Entra with SAP IAG");
externalOriginResourceConnector.setConnectorType(ConnectorType.SapIag);
ExternalTokenBasedSapIagConnectionInfo connectionInfo = new ExternalTokenBasedSapIagConnectionInfo();
connectionInfo.setOdataType("microsoft.graph.externalTokenBasedSapIagConnectionInfo");
connectionInfo.setUrl("https://contoso.example.com");
connectionInfo.setAccessTokenUrl("https://contoso.example.com/oauth/token");
connectionInfo.setClientId("e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29");
connectionInfo.setKeyVaultName("Keyvault");
connectionInfo.setSecretName("clientSecret");
connectionInfo.setSubscriptionId("5ee98b73-d9df-43a7-8a92-36855054bdee");
connectionInfo.setResourceGroup("SAP IAG Group");
externalOriginResourceConnector.setConnectionInfo(connectionInfo);
ExternalOriginResourceConnector result = graphClient.identityGovernance().entitlementManagement().externalOriginResourceConnectors().post(externalOriginResourceConnector);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const externalOriginResourceConnector = {
  '@odata.type': '#microsoft.graph.externalOriginResourceConnector',
  displayName: 'SAP IAG Connector',
  description: 'This connector helps integrate Microsoft Entra with SAP IAG',
  connectorType: 'sapIag',
  connectionInfo: {
    '@odata.type': 'microsoft.graph.externalTokenBasedSapIagConnectionInfo',
    url: 'https://contoso.example.com',
    accessTokenUrl: 'https://contoso.example.com/oauth/token',
    clientId: 'e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29',
    keyVaultName: 'Keyvault',
    secretName: 'clientSecret',
    subscriptionId: '5ee98b73-d9df-43a7-8a92-36855054bdee',
    resourceGroup: 'SAP IAG Group'
  }
};

await client.api('/identityGovernance/entitlementManagement/externalOriginResourceConnectors').post(externalOriginResourceConnector);

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Models\ExternalOriginResourceConnector;
use Microsoft\Graph\Generated\Models\ConnectorType;
use Microsoft\Graph\Generated\Models\ExternalTokenBasedSapIagConnectionInfo;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new ExternalOriginResourceConnector();
$requestBody->setOdataType('#microsoft.graph.externalOriginResourceConnector');
$requestBody->setDisplayName('SAP IAG Connector');
$requestBody->setDescription('This connector helps integrate Microsoft Entra with SAP IAG');
$requestBody->setConnectorType(new ConnectorType('sapIag'));
$connectionInfo = new ExternalTokenBasedSapIagConnectionInfo();
$connectionInfo->setOdataType('microsoft.graph.externalTokenBasedSapIagConnectionInfo');
$connectionInfo->setUrl('https://contoso.example.com');
$connectionInfo->setAccessTokenUrl('https://contoso.example.com/oauth/token');
$connectionInfo->setClientId('e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29');
$connectionInfo->setKeyVaultName('Keyvault');
$connectionInfo->setSecretName('clientSecret');
$connectionInfo->setSubscriptionId('5ee98b73-d9df-43a7-8a92-36855054bdee');
$connectionInfo->setResourceGroup('SAP IAG Group');
$requestBody->setConnectionInfo($connectionInfo);

$result = $graphServiceClient->identityGovernance()->entitlementManagement()->externalOriginResourceConnectors()->post($requestBody)->wait();

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.external_origin_resource_connector import ExternalOriginResourceConnector
from msgraph.generated.models.connector_type import ConnectorType
from msgraph.generated.models.external_token_based_sap_iag_connection_info import ExternalTokenBasedSapIagConnectionInfo
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = ExternalOriginResourceConnector(odata_type = "#microsoft.graph.externalOriginResourceConnector",display_name = "SAP IAG Connector",description = "This connector helps integrate Microsoft Entra with SAP IAG",connector_type = ConnectorType.SapIag,connection_info = ExternalTokenBasedSapIagConnectionInfo(	odata_type = "microsoft.graph.externalTokenBasedSapIagConnectionInfo",	url = "https://contoso.example.com",	access_token_url = "https://contoso.example.com/oauth/token",	client_id = "e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29",	key_vault_name = "Keyvault",	secret_name = "clientSecret",	subscription_id = "5ee98b73-d9df-43a7-8a92-36855054bdee",	resource_group = "SAP IAG Group",),
)

result = await graph_client.identity_governance.entitlement_management.external_origin_resource_connectors.post(request_body)

```

> 
> For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.externalOriginResourceConnector",
  "id": "ea32a820-9c92-428d-ba21-a33b0c00cfb2",
  "displayName": "SAP IAG Connector",
  "description": "This connector helps integrate Microsoft Entra with SAP IAG",
  "connectorType": "sapIag",
  "connectionInfo": {
    "@odata.type": "microsoft.graph.externalTokenBasedSapIagConnectionInfo",
    "url": "https://contoso.example.com",
    "accessTokenUrl": "https://contoso.example.com/oauth/token",
    "clientId": "e9ad8b1d-959c-4e86-8ba2-2cbf4d14bc29",
    "keyVaultName": "Keyvault",
    "secretName": "clientSecret",
    "subscriptionId": "5ee98b73-d9df-43a7-8a92-36855054bdee",
    "resourceGroup": "SAP IAG Group"
  },
  "createdBy": "admin@contoso.com",
  "createdDateTime": "2026-02-23T10:15:30Z",
  "modifiedBy": null,
  "modifiedDateTime": null
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/entitlementmanagement-post-externaloriginresourceconnectors?view=graph-rest-beta&accept=text/markdown)
