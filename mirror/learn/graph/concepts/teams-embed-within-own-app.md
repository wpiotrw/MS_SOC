---
layout: Conceptual
title: Embed Microsoft Teams in your app - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/teams-embed-within-own-app
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: erichui-ms
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: teams
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Learn how to embed the Microsoft Teams experience within your own application.
ms.localizationpriority: high
ms.date: 2026-09-22T00:00:00.0000000Z
locale: en-us
document_id: 89a8e17a-5d2d-0f8b-f76b-dceba425c56a
document_version_independent_id: 89a8e17a-5d2d-0f8b-f76b-dceba425c56a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/teams-embed-within-own-app.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: teams-embed-within-own-app
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/teams-embed-within-own-app.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 9eb342b6-b27f-5ceb-f572-520d51c0e8a1
---

# Embed Microsoft Teams in your app - Microsoft Graph | Microsoft Learn

This article describes how to embed the Microsoft Teams experience within your application. When you embed Teams in your app, your users can read and send Teams messages directly from your app, without having to switch between your app and Teams.

To improve your app's response time and help lower costs, you'll want to minimize the number of times a message is read from Microsoft Graph. This article explains how to retrieve messages once and cache them, and then use change notifications to get only the subsequent messages.

## Step 1: Design and set up architecture

The following diagram shows the suggested high-level architecture for an app that integrates with Teams.

![Diagram showing Teams integration with an application UI](images/teams-embed-within-own-app-system-diagram.png)

The architecture includes three components:

- A **chat UI** that gets user inputs and displays messages. The chat UI makes API requests (such as `POST`/`GET` chats, `POST`/`GET` messages) to Teams APIs. It also gets new messages in real time from the server component.
- A **server component** that subscribes to change notifications in real time to get new messages from Teams APIs. When Teams APIs send change notifications, a webhook URL is required to listen to the change notifications, and your UI, such as the users' mobile phone, might not have a webhook URL. The server component, however, has a stable webhook URL. The new messages are then pushed from the server component to the chat UI, using communication methods such as ASP.NET [SignalR](/en-us/aspnet/signalr/overview/getting-started/introduction-to-signalr).

    Note

    You might also choose to have the server component, instead of the chat UI, make all the API requests to Teams APIs, and cache all the messages. For example, if you have another backend system component that also needs to make API requests, such as for compliance and auditing, you might choose to centralize the API requests and caching on the server component instead.
- A **cache** that persists messages. Store messages in the cache to minimize repeated reads and improve your application's response time. To learn how to set up a cache, see [Add caching to improve performance in Azure API Management](/en-us/azure/api-management/api-management-howto-cache).

After you set up these components, you can start using Teams APIs.

## Step 2: Create a new chat

Before sending a new [chatMessage](/en-us/graph/api/resources/chatmessage), you must create a [chat](/en-us/graph/api/resources/chat) by assigning [members](/en-us/graph/api/resources/conversationmember). The following example shows how to create a group chat. For more examples that show how to create different chat types, see [Create chat](/en-us/graph/api/chat-post).

### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/chats
Content-Type: application/json

{
    "chatType": "group",
    "members": [
        {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [
                "owner"
            ],
            "user@odata.bind": "https://graph.microsoft.com/v1.0/users('adams@contoso.com')"
        },
        {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [
                "owner"
            ],
            "user@odata.bind": "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')"
        },
        {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [
                "owner"
            ],
            "user@odata.bind": "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')"
        }
    ]
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

var requestBody = new Chat
{ChatType = ChatType.Group,Members = new List<ConversationMember>{	new AadUserConversationMember	{		OdataType = "#microsoft.graph.aadUserConversationMember",		Roles = new List<string>		{			"owner",		},		AdditionalData = new Dictionary<string, object>		{			{				"user@odata.bind" , "https://graph.microsoft.com/v1.0/users('adams@contoso.com')"			},		},	},	new AadUserConversationMember	{		OdataType = "#microsoft.graph.aadUserConversationMember",		Roles = new List<string>		{			"owner",		},		AdditionalData = new Dictionary<string, object>		{			{				"user@odata.bind" , "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')"			},		},	},	new AadUserConversationMember	{		OdataType = "#microsoft.graph.aadUserConversationMember",		Roles = new List<string>		{			"owner",		},		AdditionalData = new Dictionary<string, object>		{			{				"user@odata.bind" , "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')"			},		},	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Chats.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewChat()
chatType := graphmodels.GROUP_CHATTYPE 
requestBody.SetChatType(&chatType) 

conversationMember := graphmodels.NewAadUserConversationMember()
roles := []string {"owner",
}
conversationMember.SetRoles(roles)
additionalData := map[string]interface{}{"user@odata.bind" : "https://graph.microsoft.com/v1.0/users('adams@contoso.com')", 
}
conversationMember.SetAdditionalData(additionalData)
conversationMember1 := graphmodels.NewAadUserConversationMember()
roles := []string {"owner",
}
conversationMember1.SetRoles(roles)
additionalData := map[string]interface{}{"user@odata.bind" : "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')", 
}
conversationMember1.SetAdditionalData(additionalData)
conversationMember2 := graphmodels.NewAadUserConversationMember()
roles := []string {"owner",
}
conversationMember2.SetRoles(roles)
additionalData := map[string]interface{}{"user@odata.bind" : "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')", 
}
conversationMember2.SetAdditionalData(additionalData)

members := []graphmodels.ConversationMemberable {conversationMember,conversationMember1,conversationMember2,
}
requestBody.SetMembers(members)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
chats, err := graphClient.Chats().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Chat chat = new Chat();
chat.setChatType(ChatType.Group);
LinkedList<ConversationMember> members = new LinkedList<ConversationMember>();
AadUserConversationMember conversationMember = new AadUserConversationMember();
conversationMember.setOdataType("#microsoft.graph.aadUserConversationMember");
LinkedList<String> roles = new LinkedList<String>();
roles.add("owner");
conversationMember.setRoles(roles);
HashMap<String, Object> additionalData = new HashMap<String, Object>();
additionalData.put("user@odata.bind", "https://graph.microsoft.com/v1.0/users('adams@contoso.com')");
conversationMember.setAdditionalData(additionalData);
members.add(conversationMember);
AadUserConversationMember conversationMember1 = new AadUserConversationMember();
conversationMember1.setOdataType("#microsoft.graph.aadUserConversationMember");
LinkedList<String> roles1 = new LinkedList<String>();
roles1.add("owner");
conversationMember1.setRoles(roles1);
HashMap<String, Object> additionalData1 = new HashMap<String, Object>();
additionalData1.put("user@odata.bind", "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')");
conversationMember1.setAdditionalData(additionalData1);
members.add(conversationMember1);
AadUserConversationMember conversationMember2 = new AadUserConversationMember();
conversationMember2.setOdataType("#microsoft.graph.aadUserConversationMember");
LinkedList<String> roles2 = new LinkedList<String>();
roles2.add("owner");
conversationMember2.setRoles(roles2);
HashMap<String, Object> additionalData2 = new HashMap<String, Object>();
additionalData2.put("user@odata.bind", "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')");
conversationMember2.setAdditionalData(additionalData2);
members.add(conversationMember2);
chat.setMembers(members);
Chat result = graphClient.chats().post(chat);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const chat = {
    chatType: 'group',
    members: [
        {
            '@odata.type': '#microsoft.graph.aadUserConversationMember',
            roles: [
                'owner'
            ],
            'user@odata.bind': 'https://graph.microsoft.com/v1.0/users(\'adams@contoso.com\')'
        },
        {
            '@odata.type': '#microsoft.graph.aadUserConversationMember',
            roles: [
                'owner'
            ],
            'user@odata.bind': 'https://graph.microsoft.com/v1.0/users(\'gradyA@contoso.com\')'
        },
        {
            '@odata.type': '#microsoft.graph.aadUserConversationMember',
            roles: [
                'owner'
            ],
            'user@odata.bind': 'https://graph.microsoft.com/v1.0/users(\'4562bcc8-c436-4f95-b7c0-4f8ce89dca5e\')'
        }
    ]
};

await client.api('/chats').post(chat);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Models\Chat;
use Microsoft\Graph\Generated\Models\ChatType;
use Microsoft\Graph\Generated\Models\ConversationMember;
use Microsoft\Graph\Generated\Models\AadUserConversationMember;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new Chat();
$requestBody->setChatType(new ChatType('group'));
$membersConversationMember1 = new AadUserConversationMember();
$membersConversationMember1->setOdataType('#microsoft.graph.aadUserConversationMember');
$membersConversationMember1->setRoles(['owner', 	]);
$additionalData = ['user@odata.bind' => 'https://graph.microsoft.com/v1.0/users(\'adams@contoso.com\')',
];
$membersConversationMember1->setAdditionalData($additionalData);
$membersArray []= $membersConversationMember1;
$membersConversationMember2 = new AadUserConversationMember();
$membersConversationMember2->setOdataType('#microsoft.graph.aadUserConversationMember');
$membersConversationMember2->setRoles(['owner', 	]);
$additionalData = ['user@odata.bind' => 'https://graph.microsoft.com/v1.0/users(\'gradyA@contoso.com\')',
];
$membersConversationMember2->setAdditionalData($additionalData);
$membersArray []= $membersConversationMember2;
$membersConversationMember3 = new AadUserConversationMember();
$membersConversationMember3->setOdataType('#microsoft.graph.aadUserConversationMember');
$membersConversationMember3->setRoles(['owner', 	]);
$additionalData = ['user@odata.bind' => 'https://graph.microsoft.com/v1.0/users(\'4562bcc8-c436-4f95-b7c0-4f8ce89dca5e\')',
];
$membersConversationMember3->setAdditionalData($additionalData);
$membersArray []= $membersConversationMember3;
$requestBody->setMembers($membersArray);

$result = $graphServiceClient->chats()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{chatType = "group"members = @(	@{		"@odata.type" = "#microsoft.graph.aadUserConversationMember"		roles = @(		"owner"	)	"user@odata.bind" = "https://graph.microsoft.com/v1.0/users('adams@contoso.com')"}@{	"@odata.type" = "#microsoft.graph.aadUserConversationMember"	roles = @(	"owner")"user@odata.bind" = "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')"
}
@{"@odata.type" = "#microsoft.graph.aadUserConversationMember"roles = @("owner"
)
"user@odata.bind" = "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')"
}
)
}

New-MgChat -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.chat import Chat
from msgraph.generated.models.chat_type import ChatType
from msgraph.generated.models.conversation_member import ConversationMember
from msgraph.generated.models.aad_user_conversation_member import AadUserConversationMember
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = Chat(chat_type = ChatType.Group,members = [	AadUserConversationMember(		odata_type = "#microsoft.graph.aadUserConversationMember",		roles = [			"owner",		],		additional_data = {				"user@odata_bind" : "https://graph.microsoft.com/v1.0/users('adams@contoso.com')",		}	),	AadUserConversationMember(		odata_type = "#microsoft.graph.aadUserConversationMember",		roles = [			"owner",		],		additional_data = {				"user@odata_bind" : "https://graph.microsoft.com/v1.0/users('gradyA@contoso.com')",		}	),	AadUserConversationMember(		odata_type = "#microsoft.graph.aadUserConversationMember",		roles = [			"owner",		],		additional_data = {				"user@odata_bind" : "https://graph.microsoft.com/v1.0/users('4562bcc8-c436-4f95-b7c0-4f8ce89dca5e')",		}	),],
)

result = await graph_client.chats.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#chats/$entity",
    "id": "19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2",
    "topic": null,
    "createdDateTime": "2023-01-11T01:34:18.929Z",
    "lastUpdatedDateTime": "2023-01-11T01:34:18.929Z",
    "chatType": "group",
    "webUrl": "https://teams.microsoft.com/l/chat/19%3Ab1234aaa12345a123aa12aa12aaaa1a9%40thread.v2/0?tenantId=4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1",
    "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1",
    "viewpoint": null,
    "onlineMeetingInfo": null
}
```

## Step 3: Send a message in the chat

Members within the chat can send messages to each other. The following example shows how to send a simple message. For more examples, including sending other media such as file attachments and adaptive cards, see [Send chatMessage](/en-us/graph/api/chatmessage-post).

### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2/messages
Content-type: application/json

{
  "body": {
    "content": "Hello World"
  }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

var requestBody = new ChatMessage
{Body = new ItemBody{	Content = "Hello World",},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Chats["{chat-id}"].Messages.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewChatMessage()
body := graphmodels.NewItemBody()
content := "Hello World"
body.SetContent(&content) 
requestBody.SetBody(body)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Chats().ByChatId("chat-id").Messages().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

ChatMessage chatMessage = new ChatMessage();
ItemBody body = new ItemBody();
body.setContent("Hello World");
chatMessage.setBody(body);
ChatMessage result = graphClient.chats().byChatId("{chat-id}").messages().post(chatMessage);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const chatMessage = {
  body: {
    content: 'Hello World'
  }
};

await client.api('/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2/messages').post(chatMessage);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Models\ChatMessage;
use Microsoft\Graph\Generated\Models\ItemBody;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new ChatMessage();
$body = new ItemBody();
$body->setContent('Hello World');
$requestBody->setBody($body);

$result = $graphServiceClient->chats()->byChatId('chat-id')->messages()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{body = @{	content = "Hello World"}
}

New-MgChatMessage -ChatId $chatId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.chat_message import ChatMessage
from msgraph.generated.models.item_body import ItemBody
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = ChatMessage(body = ItemBody(	content = "Hello World",),
)

result = await graph_client.chats.by_chat_id('chat-id').messages.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#chats('19:b1234aaa12345a123aa12aa12aaaa1a9%40thread.v2')/messages/$entity",
    "id": "1673482643198",
    "replyToId": null,
    "etag": "1673482643198",
    "messageType": "message",
    "createdDateTime": "2023-01-12T00:17:23.198Z",
    "lastModifiedDateTime": "2023-01-12T00:17:23.198Z",
    "lastEditedDateTime": null,
    "deletedDateTime": null,
    "subject": null,
    "summary": null,
    "chatId": "19:b1234aaa12345a123aa12aa12aaaa1a@thread.v2",
    "importance": "normal",
    "locale": "en-us",
    "webUrl": null,
    "channelIdentity": null,
    "policyViolation": null,
    "eventDetail": null,
    "from": {
        "application": null,
        "device": null,
        "user": {
            "id": "87d349ed-44d7-43e1-9a83-5f2406dee5bd",
            "displayName": "John Smith",
            "userIdentityType": "aadUser"
        }
    },
    "body": {
        "contentType": "text",
        "content": "Hello world"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
}
```

## Step 4: Retrieve messages

Use the `GET` HTTP method on the [chatMessages](/en-us/graph/api/resources/chatmessage) resource to retrieve messages.

To improve the response time for your application, to minimize throttling, and to potentially lower the costs for you, minimize reading the same message multiple times. Use the `GET` HTTP method as a one-time export, or when the change notifications have expired and you want to sync the messages again. Otherwise, rely on your cache and change notifications.

Microsoft Graph provides several ways to retrieve chat messages:

- [Get all messages from all chats](/en-us/graph/api/chats-getallmessages) (across all chats): `GET /users/{user-id | user-principal-name}/chats/getAllMessages`
- [List messages in a chat](/en-us/graph/api/chat-list-messages) (per chat): `GET /chats/{chat-id}/messages`

By using `/getAllMessages`, you can get messages across all chats for a user. This API is designed for backend applications, such as audit and compliance applications, which often get messages across all chats at once. It supports [application](/en-us/graph/auth/auth-concepts) permissions only.

By using `/messages`, you can make API calls from the UI using [delegated](/en-us/graph/auth/auth-concepts) permissions, as described in Step 1.

Different APIs have different [throttling limits](/en-us/graph/throttling-limits#microsoft-teams-service-limits). For example, the per-chat `/messages` API has a limit of 30 requests per second (rps) per app per tenant. If a tenant has 50 users and each user has 15 chats on average, and you want to retrieve messages for all users and all chats at the start of your system, you would need at least 50 users x 15 chat requests/user = 750 requests. In this case, it's best to spread the requests over at least 750 requests / 30 rps = 25 seconds. Because there is a limit (maximum `$top=50`) to the number of messages that are returned in a response, you might need to make multiple requests to get all the messages.

The following example shows how to use the per-chat `/messages` API. By default, the returned list of messages is sorted by `lastModifiedDateTime`. This example sorts by [createdDateTime](/en-us/graph/api/chat-list-messages?#example-3-list-chat-messages-sorted-by-creation-date). The sorting is specified via the `orderBy` query parameter in the request.

Typical interactive messaging apps display only the most recent messages by default, and users can then load older messages by paging, scrolling, or clicking. To retrieve only the messages that you need, both APIs above also support filtering (for example, `$top=10`, `$filter=lastModifiedDateTime gt 2019-03-17T07:13:28.000z`).

### Request

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2/messages?$top=2&$filter=lastModifiedDateTime gt 2021-03-17T07:13:28.000z&$orderby=createdDateTime desc
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Chats["{chat-id}"].Messages.GetAsync((requestConfiguration) =>
{requestConfiguration.QueryParameters.Top = 2;requestConfiguration.QueryParameters.Filter = "lastModifiedDateTime gt 2021-03-17T07:13:28.000z";requestConfiguration.QueryParameters.Orderby = new string []{ "createdDateTime desc" };
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

requestTop := int32(2)
requestFilter := "lastModifiedDateTime gt 2021-03-17T07:13:28.000z"

requestParameters := &graphusers.ItemChatsItemMessagesRequestBuilderGetQueryParameters{Top: &requestTop,Filter: &requestFilter,Orderby: [] string {"createdDateTime desc"},
}
configuration := &graphusers.ItemChatsItemMessagesRequestBuilderGetRequestConfiguration{QueryParameters: requestParameters,
}

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
messages, err := graphClient.Users().ByUserId("user-id").Chats().ByChatId("chat-id").Messages().Get(context.Background(), configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

ChatMessageCollectionResponse result = graphClient.users().byUserId("{user-id}").chats().byChatId("{chat-id}").messages().get(requestConfiguration -> {requestConfiguration.queryParameters.top = 2;requestConfiguration.queryParameters.filter = "lastModifiedDateTime gt 2021-03-17T07:13:28.000z";requestConfiguration.queryParameters.orderby = new String []{"createdDateTime desc"};
});

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let messages = await client.api('/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2/messages').filter('lastModifiedDateTime gt 2021-03-17T07:13:28.000z').orderby('createdDateTime desc').top(2).get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Users\Item\Chats\Item\Messages\MessagesRequestBuilderGetRequestConfiguration;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestConfiguration = new MessagesRequestBuilderGetRequestConfiguration();
$queryParameters = MessagesRequestBuilderGetRequestConfiguration::createQueryParameters();
$queryParameters->top = 2;
$queryParameters->filter = "lastModifiedDateTime gt 2021-03-17T07:13:28.000z";
$queryParameters->orderby = ["createdDateTime desc"];
$requestConfiguration->queryParameters = $queryParameters;

$result = $graphServiceClient->users()->byUserId('user-id')->chats()->byChatId('chat-id')->messages()->get($requestConfiguration)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

Get-MgAllUserChatMessage -UserId $userId -ChatId $chatId -Top 2 -Filter "lastModifiedDateTime gt 2021-03-17T07:13:28.000z" -Sort "createdDateTime desc" 

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.users.item.chats.item.messages.messages_request_builder import MessagesRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(	top = 2,	filter = "lastModifiedDateTime gt 2021-03-17T07:13:28.000z",	orderby = ["createdDateTime desc"],
)

request_configuration = RequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.users.by_user_id('user-id').chats.by_chat_id('chat-id').messages.get(request_configuration = request_configuration)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('87d349ed-44d7-43e1-9a83-5f2406dee5bd')/chats('19%3Ab1234aaa12345a123aa12aa12aaaa1a9%40thread.v2')/messages",
    "@odata.count": 2,
    "@odata.nextLink": "https://graph.microsoft.com/v1.0/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2/messages?$top=2&$filter=lastModifiedDateTime+gt+2021-03-17T07%3a13%3a28.000z&$orderby=createdDateTime+desc&$skiptoken=A111wwAwAA1ww1AwA1wwA1Aww111AA1wAwAAwAAwAAAwA1w1AAAwAAwww1Aww1AwAAwwAAA1AA1wAwAAw111wA11AAAww11Aw1wwww1wAwwwAAwwAwAwAAw1",
    "value": [
        {
            "id": "1673543687527",
            "replyToId": null,
            "etag": "1673543687527",
            "messageType": "message",
            "createdDateTime": "2023-01-12T17:14:47.527Z",
            "lastModifiedDateTime": "2023-01-12T17:14:47.527Z",
            "lastEditedDateTime": null,
            "deletedDateTime": null,
            "subject": null,
            "summary": null,
            "chatId": "19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2",
            "importance": "normal",
            "locale": "en-us",
            "webUrl": null,
            "channelIdentity": null,
            "policyViolation": null,
            "eventDetail": null,
            "from": {
                "application": null,
                "device": null,
                "user": {
                    "id": "6789f158-72b1-4a63-9959-1f006381132b",
                    "displayName": "Adele Vance",
                    "userIdentityType": "aadUser",
                    "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1"
                }
            },
            "body": {
                "contentType": "html",
                "content": "<p>Good morning, world!</p>"
            },
            "attachments": [],
            "mentions": [],
            "reactions": []
        },
        {
            "id": "1673482643198",
            "replyToId": null,
            "etag": "1673482643198",
            "messageType": "message",
            "createdDateTime": "2023-01-12T00:17:23.198Z",
            "lastModifiedDateTime": "2023-01-12T00:17:23.198Z",
            "lastEditedDateTime": null,
            "deletedDateTime": null,
            "subject": null,
            "summary": null,
            "chatId": "19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2",
            "importance": "normal",
            "locale": "en-us",
            "webUrl": null,
            "channelIdentity": null,
            "policyViolation": null,
            "eventDetail": null,
            "from": {
                "application": null,
                "device": null,
                "user": {
                    "id": "87d349ed-44d7-43e1-9a83-5f2406dee5bd",
                    "displayName": "John Smith",
                    "userIdentityType": "aadUser",
                    "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1"
                }
            },
            "body": {
                "contentType": "text",
                "content": "Hello world"
            },
            "attachments": [],
            "mentions": [],
            "reactions": []
        }
    ]
}
```

In this example, the **contentType** can be either `text` or `html`; make sure that your application can display both.

To get images embedded in the chat message, make a second call to retrieve [chatMessageHostedContent](/en-us/graph/api/resources/chatmessagehostedcontent). For details, see [Get chatMessageHostedContent](/en-us/graph/api/chatmessagehostedcontent-get).

We recommend that your app monitors to the [chatMessage.policyViolation.dlpAction](/en-us/graph/api/resources/chatmessagepolicyviolation) field, watches for change notifications to this field, and hides or flags the messages according to the data loss prevention (DLP) or similar rules defined by your organization. The valid values are `None`, `NotifySender`, and `BlockAccess`. Currently, Teams ignores `BlockAccessExternal`. For details about these values, see [chatMessagePolicyViolation resource type](/en-us/graph/api/resources/chatmessagepolicyviolation).

Some messages are [system messages](/en-us/graph/system-messages). For example, the following system message shows that a new member joined the chat.

```json
{
  "id": "1616883610266",
  "replyToId": null,
  "etag": "1616883610266",
  "messageType": "systemEventMessage",
  "createdDateTime": "2021-03-28T03:50:10.266Z",
  "lastModifiedDateTime": "2021-03-28T03:50:10.266Z",
  "lastEditedDateTime": null,
  "deletedDateTime": null,
  "subject": null,
  "summary": null,
  "chatId": null,
  "importance": "normal",
  "locale": "en-us",
  "webUrl": "https://teams.microsoft.com/l/message/19%3A4a95f7d8db4c4e7fae857bcebe0623e6%40thread.tacv2/1616883610266?groupId=fbe2bf47-16c8-47cf-b4a5-4b9b187c508b&tenantId=2432b57b-0abd-43db-aa7b-16eadd115d34&createdTime=1616883610266&parentMessageId=1616883610266",
  "policyViolation": null,
  "from": null,
  "body": {
    "contentType": "html",
    "content": "<systemEventMessage/>"
  },
  "channelIdentity": {
    "teamId": "fbe2bf47-16c8-47cf-b4a5-4b9b187c508b",
    "channelId": "19:4a95f7d8db4c4e7fae857bcebe0623e6@thread.tacv2"
  },
  "onBehalfOf": null,
  "attachments": [],
  "mentions": [],
  "reactions": [],
  "eventDetail": {
    "@odata.type": "#microsoft.graph.membersAddedEventMessageDetail",
    "visibleHistoryStartDateTime": "0001-01-01T00:00:00Z",
    "members": [{
        "id": "06a5b888-ad96-455e-88ef-c059ec4e4cf0",
        "displayName": null,
        "userIdentityType": "aadUser"
      },
      {
        "id": "1fb8890f-423e-4154-8fbf-db6809bc8756",
        "displayName": null,
        "userIdentityType": "aadUser"
      }
    ],
    "initiator": {
      "application": null,
      "device": null,
      "user": {
        "id": "9ee3dc1b-6a70-4582-8bc5-5dd35336b6c3",
        "displayName": null,
        "userIdentityType": "aadUser"
      }
    }
  }
}
```

## Step 5: Cache messages

To minimize reading the same message multiple times from [getAllMessages](/en-us/microsoftteams/export-teams-content#how-to-access-teams-export-apis) or [change notification](/en-us/graph/api/resources/changenotificationcollection), cache messages for at least a few hours. Caching allows users to quickly reopen recent chats. Don't cache messages longer than permitted by your organization's retention policies.

In Step 6, you will decide whether the cache is per-user or not.

## Step 6: Subscribe to change notifications

Microsoft Graph offers several kinds of [change notifications for messages](/en-us/graph/teams-change-notification-in-microsoft-teams-overview), as specified by the corresponding **resource** properties:

- Per chat: `"resource": "/chats/{id}/messages"`
- Per user, across all chats: `"resource": "/users/{id}/chats/getAllMessages"`
- Per tenant, across all chats: `"resource": "/chats/getAllMessages"`
- Per app, across all chats in a tenant where the app is installed: `"resource": "/appCatalogs/teamsApps/{id}/installedToChats/getAllMessages"`

If you want to track only specific chats, `/messages` is an option, but you should consider how many different chats you need to track. There's a [limit](/en-us/graph/change-notifications-overview#teams-resource-limitations) on the number of per-chat change notifications. Instead, consider subscribing to one of the three `/getAllMessages` options, which get messages across all chats of a user, tenant, or app.

All four options are called by your backend server component. Because they all support [application](/en-us/graph/auth/auth-concepts) permissions, pay attention to the access control logic to show and hide chats accordingly as users join or leave. The per-user option, which also supports [delegated](/en-us/graph/auth/auth-concepts) permissions, might be easier to implement, because the change notifications are already user specific; however, this it might be more expensive in the long run because the same message would trigger multiple change notifications, one for each subscribed user, and you might need a bigger cache to store the duplicated messages. For more details about permissions and licensing requirements for the different subscribed resources, see [Create subscription](/en-us/graph/api/subscription-post-subscriptions).

When creating the subscription, make sure that the **includeResourceData** property is set to `true`, and that you have specified the **encryptionCertificate** and **encryptionCertificateId** properties. Otherwise, the encrypted content won't be returned in the change notifications. For details, see [Set up change notifications that include resource data](/en-us/graph/change-notifications-overview#notification-endpoint-validation).

The following example shows how to get all messages per user. Before you use this example, the subscription notification endpoint specified in the **notificationUrl** property must be able to respond to a validation request, as described in [Set up notifications for changes in user data](/en-us/graph/change-notifications-overview#notification-endpoint-validation). If the validation fails, the request to create the subscription returns a `400 Bad Request` error.

For more details about this example, see [Create subscription](/en-us/graph/api/subscription-post-subscriptions).

### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/subscriptions
Content-type: application/json

{
  "changeType": "created,updated,deleted",
  "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
  "resource": "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages",
  "expirationDateTime": "2023-01-10T18:56:49.112603+00:00",
  "clientState": "ClientSecret",
  "includeResourceData": true,
  "encryptionCertificate": "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==",
  "encryptionCertificateId": "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

var requestBody = new Subscription
{ChangeType = "created,updated,deleted",NotificationUrl = "https://webhook.azurewebsites.net/api/send/myNotifyClient",Resource = "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages",ExpirationDateTime = DateTimeOffset.Parse("2023-01-10T18:56:49.112603+00:00"),ClientState = "ClientSecret",IncludeResourceData = true,EncryptionCertificate = "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==",EncryptionCertificateId = "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4",
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Subscriptions.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  "time"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewSubscription()
changeType := "created,updated,deleted"
requestBody.SetChangeType(&changeType) 
notificationUrl := "https://webhook.azurewebsites.net/api/send/myNotifyClient"
requestBody.SetNotificationUrl(&notificationUrl) 
resource := "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages"
requestBody.SetResource(&resource) 
expirationDateTime , err := time.Parse(time.RFC3339, "2023-01-10T18:56:49.112603+00:00")
requestBody.SetExpirationDateTime(&expirationDateTime) 
clientState := "ClientSecret"
requestBody.SetClientState(&clientState) 
includeResourceData := true
requestBody.SetIncludeResourceData(&includeResourceData) 
encryptionCertificate := "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s=="
requestBody.SetEncryptionCertificate(&encryptionCertificate) 
encryptionCertificateId := "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4"
requestBody.SetEncryptionCertificateId(&encryptionCertificateId) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
subscriptions, err := graphClient.Subscriptions().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Subscription subscription = new Subscription();
subscription.setChangeType("created,updated,deleted");
subscription.setNotificationUrl("https://webhook.azurewebsites.net/api/send/myNotifyClient");
subscription.setResource("/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages");
OffsetDateTime expirationDateTime = OffsetDateTime.parse("2023-01-10T18:56:49.112603+00:00");
subscription.setExpirationDateTime(expirationDateTime);
subscription.setClientState("ClientSecret");
subscription.setIncludeResourceData(true);
subscription.setEncryptionCertificate("MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==");
subscription.setEncryptionCertificateId("44M4444M4444M4M44MM4444MM4444MMMM44MM4M4");
Subscription result = graphClient.subscriptions().post(subscription);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const subscription = {
  changeType: 'created,updated,deleted',
  notificationUrl: 'https://webhook.azurewebsites.net/api/send/myNotifyClient',
  resource: '/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages',
  expirationDateTime: '2023-01-10T18:56:49.112603+00:00',
  clientState: 'ClientSecret',
  includeResourceData: true,
  encryptionCertificate: 'MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==',
  encryptionCertificateId: '44M4444M4444M4M44MM4444MM4444MMMM44MM4M4'
};

await client.api('/subscriptions').post(subscription);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Models\Subscription;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new Subscription();
$requestBody->setChangeType('created,updated,deleted');
$requestBody->setNotificationUrl('https://webhook.azurewebsites.net/api/send/myNotifyClient');
$requestBody->setResource('/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages');
$requestBody->setExpirationDateTime(new \DateTime('2023-01-10T18:56:49.112603+00:00'));
$requestBody->setClientState('ClientSecret');
$requestBody->setIncludeResourceData(true);
$requestBody->setEncryptionCertificate('MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==');
$requestBody->setEncryptionCertificateId('44M4444M4444M4M44MM4444MM4444MMMM44MM4M4');

$result = $graphServiceClient->subscriptions()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.ChangeNotifications

$params = @{changeType = "created,updated,deleted"notificationUrl = "https://webhook.azurewebsites.net/api/send/myNotifyClient"resource = "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages"expirationDateTime = [System.DateTime]::Parse("2023-01-10T18:56:49.112603+00:00")clientState = "ClientSecret"includeResourceData = $trueencryptionCertificate = "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s=="encryptionCertificateId = "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4"
}

New-MgSubscription -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.subscription import Subscription
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = Subscription(change_type = "created,updated,deleted",notification_url = "https://webhook.azurewebsites.net/api/send/myNotifyClient",resource = "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages",expiration_date_time = "2023-01-10T18:56:49.112603+00:00",client_state = "ClientSecret",include_resource_data = True,encryption_certificate = "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsM4ssMsMsMMMss4ssMMMssss...s4sMMMMsM444ssM4MMsssMMMMsM4MMM4sMsM4MMsM44MMM4ssss4Ms4sMM4MMMMM4MMs+ss4MsMssMss4s==",encryption_certificate_id = "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4",
)

result = await graph_client.subscriptions.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 201 Created
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
  "id": "88aa8a88-88a8-88a8-8888-88a8aa88a88a",
  "resource": "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages",
  "applicationId": "aa8aaaa8-8aa8-88a8-888a-aaaa8a8aa88a",
  "changeType": "created,updated,deleted",
  "clientState": "ClientSecret",
  "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
  "notificationQueryOptions": null,
  "lifecycleNotificationUrl": null,
  "expirationDateTime": "2023-01-10T18:56:49.112603Z",
  "creatorId": "8888a8a8-8a88-888a-88aa-8a888a88888a",
  "includeResourceData": true,
  "latestSupportedTlsVersion": "v1_2",
  "encryptionCertificate": "MMMM/sMMMsssMsMMMsMMsMMMs4sMMsMMs...sssMssMsMsMMss4MMM4sMsM4sMss4s==",
  "encryptionCertificateId": "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4",
  "notificationUrlAppId": null
}
```

## Step 7: Receive and decrypt change notifications

Whenever there is a change to the subscribed resource, a [change notification](/en-us/graph/api/resources/changenotificationcollection) is sent to the **notificationUrl**. For security reasons, the content is encrypted. To decrypt the content, see [Decrypting resource data from change notifications](/en-us/graph/change-notifications-with-resource-data#decrypting-resource-data-from-change-notifications).

When you create the subscription, make sure that the **includeResourceData** property is set to `true`, and that you have specified the **encryptionCertificate** and **encryptionCertificateId** properties. Otherwise, the encrypted content won't be returned in the change notifications. For details, see [Notification endpoint validation](/en-us/graph/api/subscription-post-subscriptions#notification-endpoint-validation).

### Request (sent by Microsoft Graph)

```http
POST https://webhook.azurewebsites.net/api/send/myNotifyClient
Content-type: application/json

{
  "value": [
    {
      "subscriptionId": "88aa8a88-88a8-88a8-8888-88a8aa88a88a",
      "changeType": "created",
      "clientState": "ClientSecret",
      "subscriptionExpirationDateTime": "2023-01-10T11:03:37.0068432-08:00",
      "resource": "chats('19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2')/messages('1677774058888')",
      "resourceData": {
        "id": "1677774058888",
        "@odata.type": "#Microsoft.Graph.chatMessage",
        "@odata.id": "chats('19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2')/messages('1677774058888')"
      },
      "encryptedContent": {
        "data": "sMMsMsMM+3MMMs8MMsMMsss5M+M0+8sMMsM96MM/8MMMsM4MM12sMsssMMsssMsMMssMs8Mss6sssMMsM2ssssssssMss7sssMs4s35ssMs+0ss1sssMsMssMMMMsssss5MsMssssss+sMsMMMM8s4M3MMsMssM54s1ssssMs4ssMsss3MMM8M4sM+3MMss7MM8sMsMMMs3sssss5MssMss6s+Ms7sMssMMssMsMMss1sMs2sM6sss6sMssssMss7s1MMs7/Msssss5M9M7sMsMMMsMs+MMs+MsMMsMsMMMMsMMMss1M2ssMM8M3sMMMsMss2MMMMsM+ss0M+sssMM4M+sMsM69sMs+sMsssM+MMsMsMM/ssssMMMMMss/s6/47Ms0s5Ms6MsssM2sss4MMMMMMsMsMMM+s8MssMsMMssMMs+MMMM56ss0sMM+sssMsss1ssMsMs21s3MssM9ssMsss9M2+MM3sMMMMMM7MM770MMM2MMsssM11MsssMssMsMsMM2sM1s+84MMs6sss8MsMMsMMsMM3MMssMss1MssMsMsMMMMsMsssMMsssM1sssssM9MMM6s4MMss524sMMMssMs4ss3/+ssssss8MMs2ssMMs2MsMsMMssM8MMMMsMM0sss4MMs/sMsMMs0sMMsssss135sssss9+sssMsMMsMsssMsMsMsMsMM7Ms+MssMsMM1sMssss5s64sMss6sMs6sM0MMs3s29MMssM62ssMsMMssMsM0ssssssss+sM1MsM3sMM9sssssMMMsssMMsMsMsssMssssssMsMssMMMsM8Ms5MsssMM9ss/4MssMs3s5M81sMMssssMMMssMMs7Ms2M9M+7MsssMss6sM0sssM7M0ssMssssMMsMMs9s4MsMsMM6MMsMMssMMssM+Mss6MM8MMM6MM1s75MsssMMsM+MMMs2s9M1MMMsMMs1MssMsssssssMs8MsMsMMMMMM7sMsss0MssMsMMssMMM/sM0M01s2M7MsssssMs37MMs140sMMM0ssMMM/ssMMs3sMsM+Ms+sMMsM3MMssMssMsssss6MMssMMMs1MMMMMsssMs0sM9sMMMss+sssss2sssMssMsMMM1MssMMMs8MMMssssMM99ssMsssMssss2Ms5sMs1/5MMssssMsMM3MMMMM1MsMsMsMMsMMssMsMMsssssMs9Mss6Mss+sM+73Msss0ssMsss8sMssMssssssssssMM9MMMMsMMMMMMMM5MMMM27sM+ssMG",
        "dataSignature": "sMM+sss2sMssMMsMMMMMMMM6ssMs93MssMMM8sMMMMM=",
        "dataKey": "MMsMMMMMss7sssM34sMMsMMsMssMss7MssMssss+MM+4sMsssMss6Msss9sMssMssMsssMM0+MMsss0sMs8MMsMssss2MMMMsMsssMMsMsM3MssMs9ss5sssMMsMssMsMMM6MMssMsM1M+MMMMsMss3MMsssMs9s0ssMs/1sM6ssMMssM+Ms9MsssMMM8MMssssMMs2s94MsMssMMM92/MMMs4Ms8/ssssssMs5+0s+Ms2M7sMMMMsMMsMsMs+5MMM3sssMsMMMsM8sMss+MssssMsMs/MMsMM5ssssM8M0s0MM06sssMMsMM4MsssMMsMssMM9M9MsMMMMM7sMsMM==",
        "encryptionCertificateId": "44M4444M4444M4M44MM4444MM4444MMMM44MM4M4",
        "encryptionCertificateThumbprint": "07M3411M4904M3M78MM8211MM4589MMMM47MM7M6"
      },
      "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1"
    }
  ],
  "validationTokens": [
    "ssM0sMMsMsMMM1MsMMMssMssMsMMMsM1MsMsMss1sMM6Ms1MMMMMMM5MMsssMs9ssM1sMs9MsMMMMsssssMsMsssMMM6Ms1MMMMMMM5MMsssMs9ssM1sMs9MsMMMMsssssM9.ssMssMMsMsMsMsssMMMsMs04M2M2MMM1MMMsMMs4MM1sM2MsMMM5MsM3MsMsMMMss3MsMsMssMMsssssM3M0ss53sM5ss3ssMs5ssM8sMMMsMsM3Ms0sMMMsMMMsMMMsMMM3Ms0sMsMsMMMsMMMsMsMsMssssMM0MsssMsssMsssMsMsMMMsMsMsMsM2MsMsMsM3MMMsMsM4sMM6MMM3MsM2MMM1MMssMMssMsssMMMsM1sMssM5MMs4ssMsMMssMMMMM2MsMMMsMMsMMM0sMMMssMMsMMM6MsMsMsMsMsMsMMMsMMMsMMssMs05MMssMMMsMMssMMM0MMM4MsMsMsMssMssMMMsMsssMsMsMssssMM6Mss0sMMsMs8ss3MsMsssssMss3MsssM0MsM0MsMsMMssMMMsMsMsMMMsMs1sMMssMMM2MMMsMMMsMMMsMM8sMMMssMMsMsMsMsMsMsMsMM1sMsssMMMsMMMsMsssMM1sMMMsMMM0M2M2MMssMMMssMM6MsMsMMMsMMM3MMsMMMMMMsMMsMM4MsMsMsMsMssMsMMsMMMsM05MsMssMMssMMM5sMsMMMMMMsMsMsM1MsM6MsMsMsMsMsM1MMM3MMMsMMM5Ms1sM2M1MMMsMMM0MMMsMsM1MsMsMsMsMMM6MsM0MsMsMMssMMMsMsMsMMMsMs1sMMssMMM2MMMsMMMsMMMsMMMsMsM0sMM6MssMMs1sMMMssMsMMMMMssMMss16MMMsMMM2MMMsMsMsMsMssM.s16ssMMM97sM_MMs_ss8s8s3MMs95ssMMM8M6ss4M4Ms3sMMMs-M_7ss80MMMsss6ssM0sMM20MsMMs15sMM_ssMsssMMMs9ssM0M_sss5sMssMsMss4s-M-8Ms1ssM8sMsMMss9sMsMsMMMMMMMsMs6MMss2MMMsMMss0MMssMMssMssMMMMMMMMsMs817ssssssMss8MMMssMMMMsss0sMs1ssM0sM1ssMMMs6MMMMss6ss_sMMss3M4MM3sMss45s4s8MMss6s75ssMsM5sssMM0MMMMMM_1ssMMMMsMMMssMs44sMs4MssM5s-__ss5MMs6sMM_MMss5MsMMMM"
  ]
}
```

### Decrypted content

```json
{
  "@odata.context": "https://graph.microsoft.com/$metadata#chats('19%3Ab1234aaa12345a123aa12aa12aaaa1a9%40thread.v2')/messages/$entity",
  "id": "1677774058888",
  "replyToId": null,
  "etag": "1677774058888",
  "messageType": "message",
  "createdDateTime": "2023-01-10T18:07:30.302Z",
  "lastModifiedDateTime": "2023-01-10T18:07:30.302Z",
  "lastEditedDateTime": null,
  "deletedDateTime": null,
  "subject": "",
  "summary": null,
  "chatId": "19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2",
  "importance": "normal",
  "locale": "en-us",
  "webUrl": null,
  "from": {
    "application": null,
    "device": null,
    "user": {
      "userIdentityType": "aadUser",
      "id": "87d349ed-44d7-43e1-9a83-5f2406dee5bd",
      "displayName": "John Smith",
      "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1"
    }
  },
  "body": {
    "contentType": "html",
    "content": "<p>Hello world</p>"
  },
  "channelIdentity": null,
  "attachments": [
    
  ],
  "mentions": [
    
  ],
  "onBehalfOf": null,
  "policyViolation": null,
  "reactions": [
    
  ],
  "messageHistory": [
    
  ],
  "replies": [
    
  ],
  "hostedContents": [
    
  ],
  "eventDetail": null
}
```

Change notifications are sometimes delivered out of order, because they are asynchronous. If your application requires the resources to be sorted in a particular order, make sure that you sort the decrypted content by the appropriate property. For example, if the messages should be displayed in chronological order in your chat application, sort the decrypted [chatMessages](/en-us/graph/api/resources/chatmessage) by **createdDateTime**.

When a chat message is edited, a change notification is sent for the edit, with an updated `lastEditedDateTime`. Your chat application should display the edited message instead of the original message, if the intent is to display the latest version of messages.

The notes about **contentType**, images, data loss prevention (DLP), and retention policies in Step 4: Retrieve messages apply to the decrypted messages as well.

## Step 8: Renew change notification subscriptions

For security reasons, subscriptions for [chatMessage](/en-us/graph/api/resources/chatmessage) expire in 60 minutes. We recommend that you renew every 30 minutes to allow for some buffer. Lifecycle notifications for expiring subscriptions are not currently available; therefore, you have to keep track of the subscriptions and renew them before they expire by updating the **expirationDateTime** property, as described in [Update subscription](/en-us/graph/api/subscription-update?#example). Because renewing thousands of subscriptions takes time, this is a reason to avoid per-chat change notifications.

If a subscription expires before it gets renewed, some change notifications might be missed. Resync the messages by repeating Step 4: Retrieve messages.

The following example shows how to renew a subscription.

### Request

# [HTTP](#tab/http)
```http
PATCH https://graph.microsoft.com/v1.0/subscriptions/88aa8a88-88a8-88a8-8888-88a8aa88a88a
Content-type: application/json

{
   "expirationDateTime":"2023-01-12T18:23:45.9356913Z"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Models;

var requestBody = new Subscription
{ExpirationDateTime = DateTimeOffset.Parse("2023-01-12T18:23:45.9356913Z"),
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Subscriptions["{subscription-id}"].PatchAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  "time"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewSubscription()
expirationDateTime , err := time.Parse(time.RFC3339, "2023-01-12T18:23:45.9356913Z")
requestBody.SetExpirationDateTime(&expirationDateTime) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
subscriptions, err := graphClient.Subscriptions().BySubscriptionId("subscription-id").Patch(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Subscription subscription = new Subscription();
OffsetDateTime expirationDateTime = OffsetDateTime.parse("2023-01-12T18:23:45.9356913Z");
subscription.setExpirationDateTime(expirationDateTime);
Subscription result = graphClient.subscriptions().bySubscriptionId("{subscription-id}").patch(subscription);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const subscription = {
   expirationDateTime: '2023-01-12T18:23:45.9356913Z'
};

await client.api('/subscriptions/88aa8a88-88a8-88a8-8888-88a8aa88a88a').update(subscription);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Models\Subscription;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new Subscription();
$requestBody->setExpirationDateTime(new \DateTime('2023-01-12T18:23:45.9356913Z'));

$result = $graphServiceClient->subscriptions()->bySubscriptionId('subscription-id')->patch($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.ChangeNotifications

$params = @{expirationDateTime = [System.DateTime]::Parse("2023-01-12T18:23:45.9356913Z")
}

Update-MgSubscription -SubscriptionId $subscriptionId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.subscription import Subscription
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = Subscription(expiration_date_time = "2023-01-12T18:23:45.9356913Z",
)

result = await graph_client.subscriptions.by_subscription_id('subscription-id').patch(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
    "id": "88aa8a88-88a8-88a8-8888-88a8aa88a88a",
    "resource": "/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/getAllMessages",
    "applicationId": "aa8aaaa8-8aa8-88a8-888a-aaaa8a8aa88a",
    "changeType": "created",
    "clientState": null,
    "notificationUrl": "https://function-ms-teams-subscription-webhook-z2a2ig2bfq-uc.a.run.app",
    "notificationQueryOptions": null,
    "lifecycleNotificationUrl": null,
    "expirationDateTime": "2023-01-12T18:23:45.9356913Z",
    "creatorId": "8888a8a8-8a88-888a-88aa-8a888a88888a",
    "includeResourceData": null,
    "latestSupportedTlsVersion": "v1_2",
    "encryptionCertificate": null,
    "encryptionCertificateId": null,
    "notificationUrlAppId": null
}
```

## Step 9: Get and set viewpoints

A [viewpoint](/en-us/graph/api/resources/chatviewpoint) in a chat marks the timestamp at which the chat was last read by users, so that users can see that any messages under the viewpoint are unread.

To get the viewpoint of a chat, use the `GET` HTTP method on the [chats](/en-us/graph/api/chat-get) resource, as shown in the following example.

### Request

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/v1.0/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Chats["{chat-id}"].GetAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
chats, err := graphClient.Users().ByUserId("user-id").Chats().ByChatId("chat-id").Get(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Chat result = graphClient.users().byUserId("{user-id}").chats().byChatId("{chat-id}").get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let chat = await client.api('/users/87d349ed-44d7-43e1-9a83-5f2406dee5bd/chats/19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->users()->byUserId('user-id')->chats()->byChatId('chat-id')->get()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

Get-MgUserChat -UserId $userId -ChatId $chatId

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.users.by_user_id('user-id').chats.by_chat_id('chat-id').get()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

### Response

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#chats/$entity",
    "id": "19:b1234aaa12345a123aa12aa12aaaa1a9@thread.v2",
    "topic": null,
    "createdDateTime": "2023-01-11T01:34:18.929Z",
    "lastUpdatedDateTime": "2023-01-11T01:34:18.929Z",
    "chatType": "group",
    "webUrl": "https://teams.microsoft.com/l/chat/19%3Ab1234aaa12345a123aa12aa12aaaa1a9%40thread.v2/0?tenantId=4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1",
    "tenantId": "4dc1fe35-8ac6-4f0d-904a-7ebcd364bea1",
    "onlineMeetingInfo": null,
    "viewpoint": {
        "isHidden": false,
        "lastMessageReadDateTime": "2021-05-27T22:13:01.577Z"
    }
}
```

The viewpoint of a chat for a user is updated whenever the user [marks the chat as read](/en-us/graph/api/chat-markchatreadforuser), [marks the chat as unread](/en-us/graph/api/chat-markchatunreadforuser), [hides the chat](/en-us/graph/api/chat-hideforuser), or [unhides the chat](/en-us/graph/api/chat-unhideforuser).

## Cost estimation

Currently, retrieving messages per-user, per-chat (Step 4) does not involve consumptions charges (but has throttling limits).