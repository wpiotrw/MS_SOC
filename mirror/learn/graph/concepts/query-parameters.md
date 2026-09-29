---
layout: Conceptual
title: Customize Microsoft Graph Responses with Query Parameters - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/query-parameters
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: FaithOmbongi
ms.author: ombongifaith
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: concept-article
description: Discover how to use query parameters with Microsoft Graph APIs to control data retrieval and efficiently customize API responses and improve performance.
ms.reviewer: Luca.Spolidoro
ms.localizationpriority: high
ms.date: 2025-07-02T00:00:00.0000000Z
locale: en-us
document_id: 44f6304a-ab90-8543-39c7-2afd61197ffb
document_version_independent_id: 9ca019b5-063f-33a2-3cb9-3ab6baafe9d4
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/query-parameters.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query-parameters
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/query-parameters.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/86a4b315-a9f1-4577-b985-6fb0e0e67420
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/96ac410d-d052-4707-8007-df31dd0fe041
platformId: a849de8d-ebab-e3d7-8ef7-29c4181a60cc
---

# Customize Microsoft Graph Responses with Query Parameters - Microsoft Graph | Microsoft Learn

Query parameters help you optimize Microsoft Graph API responses by controlling exactly what data is returned. Instead of retrieving all available properties and data, you can use query parameters to:

- Filter results to get only the records you need
- Select specific properties to reduce response size and improve performance
- Sort and paginate data for better user experiences
- Expand related resources to get connected data in a single request

This article explains how to use [OData system query options](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html#_Toc31360955) and other Microsoft Graph query parameters effectively. You learn the syntax, see practical examples, and discover best practices for building efficient queries that enhance your application's performance.

Support for specific query parameters varies between API operations and can differ between the *v1.0* and *beta* endpoints.

Tip

On the *beta* endpoint, the `$` prefix is optional. For example, you can use `filter` instead of `$filter`. On the *v1.0* endpoint, the `$` prefix is optional for only a subset of APIs. **For simplicity, always include `$` across all versions**.

## OData system query options

A Microsoft Graph API operation might support one or more of the following OData system query options. These query options are compatible with the [OData V4 query language](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356) and are supported only in *GET* operations.

Select the examples to try them in [Graph Explorer](https://developer.microsoft.com/graph/graph-explorer).

| Name | Description | Example |
| --- | --- | --- |
| $count | Returns the total count of matching resources. | [`/me/messages?$top=2&$count=true`](https://developer.microsoft.com/graph/graph-explorer?request=me/messages?$top=2%26$count=true&amp;method=GET&amp;version=v1.0) |
| $expand | Returns related resources. | [`/groups?$expand=members`](https://developer.microsoft.com/graph/graph-explorer?request=groups?$expand=members&amp;method=GET&amp;version=v1.0) |
| $filter | Filters results (rows). | [`/users?$filter=startswith(givenName,'J')`](https://developer.microsoft.com/graph/graph-explorer?request=users?$filter=startswith%28givenName,%27J%27%29&amp;method=GET&amp;version=v1.0) |
| $format | Returns results in the specified media format. | [`/users?$format=json`](https://developer.microsoft.com/graph/graph-explorer?request=users?$format=json&amp;method=GET&amp;version=v1.0) |
| $orderby | Orders results. | [`/users?$orderby=displayName desc`](https://developer.microsoft.com/graph/graph-explorer?request=users?$orderby=displayName%20DESC&amp;method=GET&amp;version=v1.0) |
| $search | Returns results based on search criteria. | [`/me/messages?$search=pizza`](https://developer.microsoft.com/graph/graph-explorer?request=me/messages?$search=pizza&amp;method=GET&amp;version=v1.0) |
| $select | Filters properties (columns). | [`/users?$select=givenName,surname`](https://developer.microsoft.com/graph/graph-explorer?request=users?$select=givenName,surname&amp;method=GET&amp;version=v1.0) |
| $skip | Skips items in a result set. Also used by some APIs to implement paging and can be used with `$top` to manually page results. | [`/me/messages?$skip=11`](https://developer.microsoft.com/graph/graph-explorer?request=me/messages?$skip=11&amp;method=GET&amp;version=v1.0) |
|  | Sets the page size of results. | [`/users?$top=2`](https://developer.microsoft.com/graph/graph-explorer?request=users?$top=2&amp;method=GET&amp;version=v1.0) |

To find the OData system query options that an API and its properties support, see the "Properties" table in the resource page and the "Optional query parameters" section of the LIST and GET operations for the API.

## Other query parameters

| Name | Description | Example |
| --- | --- | --- |
| $skipToken | Returns the next page of results from result sets that span multiple pages. (Some APIs use `$skip` instead.) | `/users?$skiptoken=X%274453707402000100000017...` |

## Other OData URL capabilities

The following OData 4.0 capabilities are URL segments, not query parameters.

| Name | Description | Example |
| --- | --- | --- |
| $count | Returns the integer total of the collection. | `GET /users/$count``GET /groups/{id}/members/$count`[Get a count of users](/en-us/graph/api/user-list#example-3-get-only-a-count-of-users) |
| $ref | Updates entities membership to a collection. | `POST /groups/{id}/members/$ref`[Add a member to a group](/en-us/graph/api/group-post-members) |
| $value | Returns or updates the binary value of an item. | `GET /me/photo/$value`[Get the photo for a user, group, or team](/en-us/graph/api/profilephoto-get) |
| $batch | Combines multiple HTTP requests into a batch request. | `POST /$batch`[JSON batching](/en-us/graph/json-batching) |

## Encoding query parameters

Percent-encode query parameter values according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986#section-2.2). All reserved characters in query strings must be percent-encoded. Many HTTP clients, browsers, and tools (such as the [Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)) handle this encoding automatically. If a query fails, a possible cause is failure to encode the query parameter values appropriately. Sometimes, you need to double-encode values.

Note

There's a known issue with encoding ampersand (&) symbols in `$search` expressions on the *v1.0* endpoint. For more information about the issue and the recommended workaround, see [Known issue: $search for directory objects fails for encoded ampersand (&) character](/en-us/graph/known-issues#search-for-directory-objects-fails-for-encoded-ampersand-character).

For example, an unencoded URL looks like this:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users?$filter=startswith(givenName, 'J')
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFilter := "startswith(givenName, 'J')"

requestParameters := &graphusers.UsersRequestBuilderGetQueryParameters{Filter: &requestFilter,
}
configuration := &graphusers.UsersRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
users, err := graphClient.Users().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

UserCollectionResponse result = graphClient.users().get(requestConfiguration -> {requestConfiguration.queryParameters.filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let users = await client.api('/users').filter('startswith(givenName, \'J\')').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\UsersRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new UsersRequestBuilderGetRequestConfiguration();
$queryParameters = UsersRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->filter = "startswith(givenName, 'J')";
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Users

Get-MgUser -Filter "startswith(givenName, 'J')" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(	filter = "startswith(givenName, 'J')",
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

The properly percent-encoded URL looks like this:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users?$filter=startswith(givenName%2C+'J')
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFilter := "startswith(givenName, 'J')"

requestParameters := &graphusers.UsersRequestBuilderGetQueryParameters{Filter: &requestFilter,
}
configuration := &graphusers.UsersRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
users, err := graphClient.Users().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

UserCollectionResponse result = graphClient.users().get(requestConfiguration -> {requestConfiguration.queryParameters.filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let users = await client.api('/users').filter('startswith(givenName, \'J\')').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\UsersRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new UsersRequestBuilderGetRequestConfiguration();
$queryParameters = UsersRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->filter = "startswith(givenName, 'J')";
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Users

Get-MgUser -Filter "startswith(givenName, 'J')" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(	filter = "startswith(givenName, 'J')",
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

The double-encoded URL looks like this:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users?$filter=startswith%28givenName%2C%20%27J%27%29
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFilter := "startswith(givenName, 'J')"

requestParameters := &graphusers.UsersRequestBuilderGetQueryParameters{Filter: &requestFilter,
}
configuration := &graphusers.UsersRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
users, err := graphClient.Users().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

UserCollectionResponse result = graphClient.users().get(requestConfiguration -> {requestConfiguration.queryParameters.filter = "startswith(givenName, 'J')";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let users = await client.api('/users').filter('startswith(givenName, \'J\')').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\UsersRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new UsersRequestBuilderGetRequestConfiguration();
$queryParameters = UsersRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->filter = "startswith(givenName, 'J')";
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Users

Get-MgUser -Filter "startswith(givenName, 'J')" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(	filter = "startswith(givenName, 'J')",
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Escaping single quotes

For requests that use single quotes, if any parameter values also contain single quotes, they should be double escaped; otherwise, the request fails because of invalid syntax. In the example, the string value `let''s meet for lunch?` has the single quote escaped.

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/messages?$filter=subject eq 'let''s meet for lunch?'
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Filter = "subject eq 'let''s meet for lunch?'";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFilter := "subject eq 'let''s meet for lunch?'"

requestParameters := &graphusers.ItemMessagesRequestBuilderGetQueryParameters{Filter: &requestFilter,
}
configuration := &graphusers.ItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().messages().get(requestConfiguration -> {requestConfiguration.queryParameters.filter = "subject eq 'let''s meet for lunch?'";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/messages').filter('subject eq \'let\'\'s meet for lunch?\'').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->filter = "subject eq 'let''s meet for lunch?'";
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMessage -UserId $userId -Filter "subject eq 'let''s meet for lunch?'" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	filter = "subject eq 'let''s meet for lunch?'",
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

## Count

Use the `$count` query parameter to get the count of the total number of items in a collection or matching an expression. You can use `$count` in the following ways:

1. As a query string parameter with the syntax `$count=true` to include a count of the total number of items in a collection alongside the page of data values returned from Microsoft Graph. For example, `users?$count=true`.
2. As a URL segment to get only the integer total of the collection. For example, `users/$count`.
3. In a `$filter` expression with equality operators to get a collection of data where the filtered property is an empty collection. See [Use the $filter query parameter to filter a collection of objects](/en-us/graph/filter-query-parameter).

Note

1. On resources that derive from [directoryObject](/en-us/graph/api/resources/directoryobject), `$count` is only supported in an advanced query. See [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries).
2. Use of `$count` isn't supported in Azure AD B2C tenants.

For example, the following request returns both the **contact** collection of the current user and the number of items in the **contact** collection in an **@odata.count** property.

# [HTTP](#tab/http)
```msgraph
GET  https://graph.microsoft.com/v1.0/me/contacts?$count=true
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Contacts.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Count = true;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestCount := true

requestParameters := &graphusers.ItemContactsRequestBuilderGetQueryParameters{Count: &requestCount,
}
configuration := &graphusers.ItemContactsRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
contacts, err := graphClient.Me().Contacts().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

ContactCollectionResponse result = graphClient.me().contacts().get(requestConfiguration -> {requestConfiguration.queryParameters.count = true;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let contacts = await client.api('/me/contacts').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Contacts\ContactsRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new ContactsRequestBuilderGetRequestConfiguration();
$queryParameters = ContactsRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->count = true;
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->contacts()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.PersonalContacts

# A UPN can also be used as -UserId.
Get-MgUserContact -UserId $userId -CountVariable CountVar 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.contacts.contacts_request_builder import ContactsRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = ContactsRequestBuilder.ContactsRequestBuilderGetQueryParameters(	count = True,
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.contacts.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

For directory objects, that is, resources that derive from [directoryObject](/en-us/graph/api/resources/directoryobject), the `$count` query parameter is only supported in [advanced queries](/en-us/graph/aad-advanced-queries).

## Expand

Many Microsoft Graph resources expose both declared properties of the resource and its relationships with other resources. These relationships are also called reference properties or navigation properties, and they can reference either a single resource or a collection of resources. For example, the mail folders, manager, and direct reports of a user are all exposed as relationships.

You can use the `$expand` query string parameter to include the expanded resource or collection referenced by a single relationship (navigation property) in your results. For some APIs, only one relationship can be expanded in a single request.

The following example gets root drive information along with the top-level child items in a drive:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/drive/root?$expand=children
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Drives["{drive-id}"].Root.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Expand = new string []{ "children" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphdrives "github.com/microsoftgraph/msgraph-sdk-go/drives"  //other-imports
)

requestParameters := &graphdrives.ItemRootRequestBuilderGetQueryParameters{Expand: [] string {"children"},
}
configuration := &graphdrives.ItemRootRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
root, err := graphClient.Drives().ByDriveId("drive-id").Root().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

DriveItem result = graphClient.drives().byDriveId("{drive-id}").root().get(requestConfiguration -> {requestConfiguration.queryParameters.expand = new String []{"children"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let driveItem = await client.api('/me/drive/root').expand('children').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Drives\Item\Root\RootRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new RootRequestBuilderGetRequestConfiguration();
$queryParameters = RootRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->expand = ["children"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->drives()->byDriveId('drive-id')->root()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Files

Get-MgDriveRoot -DriveId $driveId -ExpandProperty "children" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.drives.item.root.root_request_builder import RootRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = RootRequestBuilder.RootRequestBuilderGetQueryParameters(	expand = ["children"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.drives.by_drive_id('drive-id').root.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

With some resource collections, you can also specify the properties to be returned in the expanded resources by adding a `$select` parameter. The following example performs the same query as the previous example but uses a `$select` statement to limit the properties returned for the expanded child items to the **id** and **name** properties.

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/drive/root?$expand=children($select=id,name)
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Drives["{drive-id}"].Root.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Expand = new string []{ "children($select=id,name)" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphdrives "github.com/microsoftgraph/msgraph-sdk-go/drives"  //other-imports
)

requestParameters := &graphdrives.ItemRootRequestBuilderGetQueryParameters{Expand: [] string {"children($select=id,name)"},
}
configuration := &graphdrives.ItemRootRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
root, err := graphClient.Drives().ByDriveId("drive-id").Root().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

DriveItem result = graphClient.drives().byDriveId("{drive-id}").root().get(requestConfiguration -> {requestConfiguration.queryParameters.expand = new String []{"children($select=id,name)"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let driveItem = await client.api('/me/drive/root').expand('children($select=id,name)').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Drives\Item\Root\RootRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new RootRequestBuilderGetRequestConfiguration();
$queryParameters = RootRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->expand = ["children(\$select=id,name)"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->drives()->byDriveId('drive-id')->root()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Files

Get-MgDriveRoot -DriveId $driveId -ExpandProperty "children(`$select=id,name)" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.drives.item.root.root_request_builder import RootRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = RootRequestBuilder.RootRequestBuilderGetQueryParameters(	expand = ["children($select=id,name)"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.drives.by_drive_id('drive-id').root.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Note

- Not all relationships and resources support the `$expand` query parameter. For example, you can expand the **directReports**, **manager**, and **memberOf** relationships on a user, but you can't expand its **events**, **messages**, or **photo** relationships. Not all resources or relationships support using `$select` on expanded items.
- With Microsoft Entra resources that derive from [directoryObject](/en-us/graph/api/resources/directoryobject), like [user](/en-us/graph/api/resources/user) and [group](/en-us/graph/api/resources/group), `$expand` typically returns a maximum of 20 items for the expanded relationship and has no [@odata.nextLink](paging). For details, see [query parameter limitations](/en-us/graph/known-issues#some-limitations-apply-to-query-parameters).
- `$expand` isn't currently supported with [advanced queries](/en-us/graph/aad-advanced-queries).

## Filter

Use the `$filter` query parameter to get just a subset of a collection. For guidance on using `$filter`, see [Use the $filter query parameter to filter a collection of objects](/en-us/graph/filter-query-parameter).

## Format

Use the `$format` query parameter to specify the media format of the items returned from Microsoft Graph.

For example, the following request returns the users in the organization in JSON format:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users?$format=json
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Format = "json";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFormat := "json"

requestParameters := &graphusers.UsersRequestBuilderGetQueryParameters{Format: &requestFormat,
}
configuration := &graphusers.UsersRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
users, err := graphClient.Users().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

UserCollectionResponse result = graphClient.users().get(requestConfiguration -> {requestConfiguration.queryParameters.format = "json";
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let users = await client.api('/users').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\UsersRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new UsersRequestBuilderGetRequestConfiguration();
$queryParameters = UsersRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->format = "json";
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Users

Get-MgUser -Format "json" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(	format = "json",
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Note

The `$format` query parameter supports many formats (for example, `atom`, `xml`, and `json`) but results might not be returned in all formats.

## OrderBy

Use the `$orderby` query parameter to specify the sort order of the items returned from Microsoft Graph. The default order is ascending.

For example, the following request returns users in the organization ordered by their display name in ascending order:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users?$orderby=displayName
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Orderby = new string []{ "displayName" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestParameters := &graphusers.UsersRequestBuilderGetQueryParameters{Orderby: [] string {"displayName"},
}
configuration := &graphusers.UsersRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
users, err := graphClient.Users().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

UserCollectionResponse result = graphClient.users().get(requestConfiguration -> {requestConfiguration.queryParameters.orderby = new String []{"displayName"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let users = await client.api('/users').orderby('displayName').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\UsersRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new UsersRequestBuilderGetRequestConfiguration();
$queryParameters = UsersRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->orderby = ["displayName"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Users

Get-MgUser -Sort "displayName" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(	orderby = ["displayName"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Some APIs support sorting by complex type entities. The following request gets messages and sorts them by the **address** field of the **from** property, which is of the complex type **emailAddress**:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/messages?$orderby=from/emailAddress/address
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Orderby = new string []{ "from/emailAddress/address" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestParameters := &graphusers.ItemMessagesRequestBuilderGetQueryParameters{Orderby: [] string {"from/emailAddress/address"},
}
configuration := &graphusers.ItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().messages().get(requestConfiguration -> {requestConfiguration.queryParameters.orderby = new String []{"from/emailAddress/address"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/messages').orderby('from/emailAddress/address').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->orderby = ["from/emailAddress/address"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMessage -UserId $userId -Sort "from/emailAddress/address" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	orderby = ["from/emailAddress/address"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

To sort results in ascending or descending order, append either `asc` or `desc` to the field name, separated by a space; for example, `?$orderby=name desc` (unencoded), `?$orderby=name%20desc` (URL encoded). If you don't specify the sort order, ascending order is inferred.

With some APIs, you can order results on multiple properties. For example, the following request orders the messages in the user's Inbox, first by the name of the person who sent it in descending order (Z to A), and then by subject in ascending order (default).

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages?$orderby=from/emailAddress/name desc,subject
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.MailFolders["{mailFolder-id}"].Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Orderby = new string []{ "from/emailAddress/name desc","subject" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestParameters := &graphusers.MailFoldersItemMessagesRequestBuilderGetQueryParameters{Orderby: [] string {"from/emailAddress/name desc","subject"},
}
configuration := &graphusers.MailFoldersItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().MailFolders().ByMailFolderId("mailFolder-id").Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().mailFolders().byMailFolderId("{mailFolder-id}").messages().get(requestConfiguration -> {requestConfiguration.queryParameters.orderby = new String []{"from/emailAddress/name desc", "subject"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/mailFolders/Inbox/messages').orderby('from/emailAddress/name desc,subject').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\MailFolders\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->orderby = ["from/emailAddress/name desc","subject"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->mailFolders()->byMailFolderId('mailFolder-id')->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMailFolderMessage -UserId $userId -MailFolderId $mailFolderId -Sort "from/emailAddress/name desc,subject" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.mail_folders.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	orderby = ["from/emailAddress/name desc","subject"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.mail_folders.by_mail_folder_id('mailFolder-id').messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Note

When you specify `$filter`, the service infers a sort order for the results. If you use both `$orderby` and `$filter` to get messages, because the server always infers a sort order for the results of a `$filter`, you must [specify properties in certain ways](/en-us/graph/api/user-list-messages#using-filter-and-orderby-in-the-same-query).

The following example shows a query filtered by the **subject** and **importance** properties, and then sorted by the **subject**, **importance**, and **receivedDateTime** properties in descending order.

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/messages?$filter=Subject eq 'welcome' and importance eq 'normal'&$orderby=subject,importance,receivedDateTime desc
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Filter = "Subject eq 'welcome' and importance eq 'normal'";requestConfiguration.QueryParameters.Orderby = new string []{ "subject","importance","receivedDateTime desc" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestFilter := "Subject eq 'welcome' and importance eq 'normal'"

requestParameters := &graphusers.ItemMessagesRequestBuilderGetQueryParameters{Filter: &requestFilter,Orderby: [] string {"subject","importance","receivedDateTime desc"},
}
configuration := &graphusers.ItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().messages().get(requestConfiguration -> {requestConfiguration.queryParameters.filter = "Subject eq 'welcome' and importance eq 'normal'";requestConfiguration.queryParameters.orderby = new String []{"subject", "importance", "receivedDateTime desc"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/messages').filter('Subject eq \'welcome\' and importance eq \'normal\'').orderby('subject,importance,receivedDateTime desc').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->filter = "Subject eq 'welcome' and importance eq 'normal'";
$queryParameters->orderby = ["subject","importance","receivedDateTime desc"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMessage -UserId $userId -Filter "Subject eq 'welcome' and importance eq 'normal'" -Sort "subject,importance,receivedDateTime desc" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	filter = "Subject eq 'welcome' and importance eq 'normal'",	orderby = ["subject","importance","receivedDateTime desc"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Note

Combining `$orderby` and `$filter` query parameters is supported for directory objects. See [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries).

## Search

Use the `$search` query parameter to restrict request results to match a search criterion. Its syntax and behavior varies across different resources. For more information, see [Use the $search query parameter to match a search criterion](/en-us/graph/search-query-parameter).

## Select

Use the `$select` query parameter to return a subset of properties for a resource. With `$select`, you can specify a subset or a superset of the default properties.

When you make a GET request without using `$select` to limit the property data, Microsoft Graph includes a **@microsoft.graph.tips** property that provides a best practice recommendation for using `$select` similar to the following message:

```html
"@microsoft.graph.tips": "Use $select to choose only the properties your app needs, as this can lead to performance improvements. For example: GET groups?$select=appMetadata,assignedLabels",
```

For example, when getting the messages of the signed-in user, you can specify that only the **from** and **subject** properties be returned:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/messages?$select=from,subject
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Select = new string []{ "from","subject" };
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestParameters := &graphusers.ItemMessagesRequestBuilderGetQueryParameters{Select: [] string {"from","subject"},
}
configuration := &graphusers.ItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().messages().get(requestConfiguration -> {requestConfiguration.queryParameters.select = new String []{"from", "subject"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/messages').select('from,subject').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->select = ["from","subject"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMessage -UserId $userId -Property "from,subject" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	select = ["from","subject"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Important

We recommend that you use `$select` to limit the properties returned by a query to those needed by your app. This is especially true for queries that might potentially return a large result set. Limiting the properties returned in each row reduces network load and improves your app's performance.

In *v1.0*, some Microsoft Entra resources that derive from [directoryObject](/en-us/graph/api/resources/directoryobject), like [user](/en-us/graph/api/resources/user) and [group](/en-us/graph/api/resources/group), return a limited, default subset of properties on reads. For these resources, you must use `$select` to return properties outside of the default set.

## Skip

Use the `$skip` query parameter to set the number of items to skip at the start of a collection. For example, the following request returns events for the user sorted by date created, starting with the 21st event in the collection:

# [HTTP](#tab/http)
```msgraph
GET  https://graph.microsoft.com/v1.0/me/events?$orderby=createdDateTime&$skip=20
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Events.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Orderby = new string []{ "createdDateTime" };requestConfiguration.QueryParameters.Skip = 20;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestSkip := int32(20)

requestParameters := &graphusers.ItemEventsRequestBuilderGetQueryParameters{Orderby: [] string {"createdDateTime"},Skip: &requestSkip,
}
configuration := &graphusers.ItemEventsRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
events, err := graphClient.Me().Events().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

EventCollectionResponse result = graphClient.me().events().get(requestConfiguration -> {requestConfiguration.queryParameters.orderby = new String []{"createdDateTime"};requestConfiguration.queryParameters.skip = 20;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let events = await client.api('/me/events').orderby('createdDateTime').skip(20).get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Events\EventsRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new EventsRequestBuilderGetRequestConfiguration();
$queryParameters = EventsRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->orderby = ["createdDateTime"];
$queryParameters->skip = 20;
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->events()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Calendar

# A UPN can also be used as -UserId.
Get-MgUserEvent -UserId $userId -Sort "createdDateTime" -Skip 20 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.events.events_request_builder import EventsRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = EventsRequestBuilder.EventsRequestBuilderGetQueryParameters(	orderby = ["createdDateTime"],	skip = 20,
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.events.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Some Microsoft Graph APIs, like Outlook Mail and Calendars (**message**, **event**, and **calendar**), use `$skip` to implement paging. When query results span multiple pages, these APIs return an **@odata.nextLink** property with a URL that contains a `$skip` parameter. You can use this URL to return the next page of results. To learn more, see [Paging](paging).

[Directory objects](/en-us/graph/api/resources/directoryobject) such as **user**, **group**, and **application** don't support `$skip`.

## SkipToken

Some requests return multiple pages of data, either due to server-side paging or due to using the  parameter to limit the page size of the response. Many Microsoft Graph APIs use the `skipToken` query parameter to reference subsequent pages of the result. This parameter contains an opaque token that references the next page of results and is returned in the URL provided in the **@odata.nextLink** property in the response. To learn more, see [Paging](paging).

Note

If you're using OData Count (adding `$count=true` in the query string) for queries against directory objects, the `@odata.count` property is present only in the first page.

The **ConsistencyLevel** header required for advanced queries against directory objects isn't included by default in subsequent page requests. It must be set explicitly in subsequent pages.

## Top

Use the `$top` query parameter to specify the number of items to be included in the result.

If more items remain in the result set, the response body contains an **@odata.nextLink** parameter. This parameter contains a URL that you can use to get the next page of results. To learn more, see [Paging](paging).

The minimum value of $top is 1 and the maximum depends on the corresponding API.

For example, the following [list messages](/en-us/graph/api/user-list-messages) request returns the first five messages in the user's mailbox:

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/me/messages?$top=5
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Me.Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Top = 5;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphusers "github.com/microsoftgraph/msgraph-sdk-go/users"  //other-imports
)

requestTop := int32(5)

requestParameters := &graphusers.ItemMessagesRequestBuilderGetQueryParameters{Top: &requestTop,
}
configuration := &graphusers.ItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Me().Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MessageCollectionResponse result = graphClient.me().messages().get(requestConfiguration -> {requestConfiguration.queryParameters.top = 5;
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/me/messages').top(5).get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->top = 5;
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->me()->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Mail

# A UPN can also be used as -UserId.
Get-MgUserMessage -UserId $userId -Top 5 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	top = 5,
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

Note

The **ConsistencyLevel** header required for advanced queries against directory objects isn't included by default in subsequent page requests. It must be set explicitly in subsequent pages.

## Error handling for query parameters

Some requests return an error message if a specified query parameter isn't supported. For example, you can't use `$expand` on the `user/photo` relationship.

```http
https://graph.microsoft.com/v1.0/me?$expand=photo
```

```json
{
    "error":{
        "code":"ExpandNotSupported",
        "message":"Expand is not allowed for property 'Photo' according to the entity schema.",
        "innerError":{
            "request-id":"1653fefd-bc31-484b-bb10-8dc33cb853ec",
            "date":"2017-07-31T20:55:01"
        }
    }
}
```

However, sometimes query parameters specified in a request fail silently. For example, for unsupported query parameters and for unsupported combinations of query parameters. In these cases, examine the data returned by the request to determine whether the query parameters you specified had the desired effect.