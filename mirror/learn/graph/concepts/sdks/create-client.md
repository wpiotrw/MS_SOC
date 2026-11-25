---
layout: Conceptual
title: Create a Microsoft Graph client - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/sdks/create-client
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: MIchaelMainer
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: article
description: Describes how to create a client to use to make calls to Microsoft Graph. Includes how to set up authentication and select a sovereign cloud.
ms.localizationpriority: medium
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: aef52833-8b23-b9cd-4337-73eec3c34f4d
document_version_independent_id: 9b012e4f-93b3-bda8-0e35-1c9c6326295c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/sdks/create-client.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sdks/create-client
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/sdks/create-client.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 34dd5d38-9bdd-ba8b-935f-5aed91a03cd6
---

# Create a Microsoft Graph client - Microsoft Graph | Microsoft Learn

The Microsoft Graph client is designed to make it simple to make calls to Microsoft Graph. You can use a single client instance for the lifetime of the application. For information about how to add and install the Microsoft Graph client package into your project, see [Install the SDK](sdk-installation).

The following code examples show how to create an instance of a Microsoft Graph client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application.

Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](choose-authentication-providers).

The client ID is the app registration ID that is generated when you [register your app in the Azure portal](/en-us/graph/auth-register-app-v2).

# [C#](#tab/csharp)
```csharp
var scopes = new[] { "User.Read" };

// Multi-tenant apps can use "common",
// single-tenant apps must use the tenant ID from the Azure portal
var tenantId = "common";

// Value from app registration
var clientId = "YOUR_CLIENT_ID";

// using Azure.Identity;
var options = new DeviceCodeCredentialOptions
{
    AuthorityHost = AzureAuthorityHosts.AzurePublicCloud,
    ClientId = clientId,
    TenantId = tenantId,
    // Callback function that receives the user prompt
    // Prompt contains the generated device code that user must
    // enter during the auth process in the browser
    DeviceCodeCallback = (code, cancellation) =>
    {
        Console.WriteLine(code.Message);
        return Task.FromResult(0);
    },
};

// https://learn.microsoft.com/dotnet/api/azure.identity.devicecodecredential
var deviceCodeCredential = new DeviceCodeCredential(options);

var graphClient = new GraphServiceClient(deviceCodeCredential, scopes);
```

> 
> Include `using` statements for `Azure.Identity` and `Microsoft.Graph` to run this code.

# [Go](#tab/go)
```go
cred, _ := azidentity.NewDeviceCodeCredential(&azidentity.DeviceCodeCredentialOptions{
    TenantID: "TENANT_ID",
    ClientID: "CLIENT_ID",
    UserPrompt: func(ctx context.Context, message azidentity.DeviceCodeMessage) error {
        fmt.Println(message.Message)
        return nil
    },
})

graphClient, _ := graph.NewGraphServiceClientWithCredentials(
    cred, []string{"User.Read"})
```

> 
> Include `"github.com/Azure/azure-sdk-for-go/sdk/azidentity"` and `graph "github.com/microsoftgraph/msgraph-sdk-go"` in your import block to run this code.

# [Java](#tab/java)
```java
final String clientId = "YOUR_CLIENT_ID";
final String tenantId = "YOUR_TENANT_ID"; // or "common" for multi-tenant apps
final String[] scopes = new String[] {"User.Read"};

final DeviceCodeCredential credential = new DeviceCodeCredentialBuilder()
    .clientId(clientId).tenantId(tenantId).challengeConsumer(challenge -> {
        // Display challenge to the user
        System.out.println(challenge.getMessage());
    }).build();

if (null == scopes || null == credential) {
    throw new Exception("Unexpected error");
}

final GraphServiceClient graphClient = new GraphServiceClient(credential, scopes);
```

> 
> Include `import` statements for `com.azure.identity.DeviceCodeCredential`, `com.azure.identity.DeviceCodeCredentialBuilder`, and `com.microsoft.graph.serviceclient.GraphServiceClient` to run this code.

# [PHP](#tab/php)
```php
$scopes = ['User.Read'];

// Multi-tenant apps can use "common",
// single-tenant apps must use the tenant ID from the Azure portal
$tenantId = 'common';

// Values from app registration
$clientId = 'YOUR_CLIENT_ID';
$clientSecret = 'YOUR_CLIENT_SECRET';
$redirectUri = 'YOUR_REDIRECT_URI';

// For authorization code flow, the user signs into the Microsoft
// identity platform, and the browser is redirected back to your app
// with an authorization code in the query parameters
$authorizationCode = 'AUTH_CODE_FROM_REDIRECT';

// Microsoft\Kiota\Authentication\Oauth\AuthorizationCodeContext
$tokenContext = new AuthorizationCodeContext(
    $tenantId,
    $clientId,
    $clientSecret,
    $authorizationCode,
    $redirectUri);

$graphClient = new GraphServiceClient($tokenContext, $scopes);
```

> 
> Include `use` statements for `Microsoft\Graph\GraphRequestAdapter`, `Microsoft\Graph\GraphServiceClient`, and `Microsoft\Kiota\Abstractions\Authentication\BaseBearerTokenAuthenticationProvider` to run this code.

# [Python](#tab/python)
```python
scopes = ['User.Read']

# Multi-tenant apps can use "common",
# single-tenant apps must use the tenant ID from the Azure portal
tenant_id = 'common'

# Values from app registration
client_id = 'YOUR_CLIENT_ID'

# azure.identity
credential = DeviceCodeCredential(
    tenant_id=tenant_id,
    client_id=client_id)

graph_client = GraphServiceClient(credential, scopes)
```

> 
> Include `import` statements for `DeviceCodeCredential` from `azure.identity` and `GraphServiceClient` from `msgraph.graph_service_client` to run this code.

# [TypeScript](#tab/typescript)
```typescript
// @azure/identity
const credential = new DeviceCodeCredential({
  tenantId: 'YOUR_TENANT_ID',
  clientId: 'YOUR_CLIENT_ID',
  userPromptCallback: (info) => {
    console.log(info.message);
  },
});

// @microsoft/microsoft-graph-client/authProviders/azureTokenCredentials
const authProvider = new TokenCredentialAuthenticationProvider(credential, {
  scopes: ['User.Read'],
});

const graphClient = Client.initWithMiddleware({ authProvider: authProvider });
```

> 
> Include `import` statements for `DeviceCodeCredential` from `@azure/identity`, `Client` from `@microsoft/microsoft-graph-client`, and `TokenCredentialAuthenticationProvider` from `@microsoft/microsoft-graph-client/authProviders/azureTokenCredentials` to run this code.

---