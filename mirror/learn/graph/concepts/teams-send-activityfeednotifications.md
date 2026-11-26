---
layout: Conceptual
title: Send activity feed notifications to users in Microsoft Teams - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/teams-send-activityfeednotifications
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: RamjotSingh
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: teams
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Use the Microsoft Teams activity feed notification APIs in Microsoft Graph to help keep users up to date with changes in the tools and workflows they use.
ms.localizationpriority: medium
ms.date: 2026-11-19T00:00:00.0000000Z
locale: en-us
document_id: aef120b3-03b9-cca1-9479-05720e6fd9ef
document_version_independent_id: 0cf32a73-043a-6b34-f71c-a8d3bd410bf7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/teams-send-activityfeednotifications.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: teams-send-activityfeednotifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/teams-send-activityfeednotifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: 6581017f-683f-f8e2-1959-943dd4b41477
---

# Send activity feed notifications to users in Microsoft Teams - Microsoft Graph | Microsoft Learn

The Microsoft Teams activity feed notifies users of changes to enable them to triage items that require attention. Activity feed notifications in Teams include the following features:

- Native integration with Teams that brings the user seamlessly into the Tab app and provides additional user engagement from the Teams **Activity** pane to your app.
- Operating system notifications in Teams desktop and mobile clients that include a pop-up and sound.
- Customizable notification content that enables you to show more or less preview content to the user.
- Ability to deep link your tab, personal app, bot message, or Adaptive Card to a notification to increase user engagement with your app.
- Ability to send activity feed notifications to multiple recipients, such as batch notifications to a group of users.

You can use the activity feed notification APIs in Microsoft Graph to extend this functionality to your apps. In this way, you can provide richer experiences and engage users by helping them stay up to date with changes in the tools and workflows they use.

The activity feed notification APIs in Microsoft Graph enable the following use cases:

- **News** - Keep users updated with the latest information, such as new assignments or new posts.
- **Collaboration** - Show users a preview in the notification banner when someone shares a file or @ mentions them in a comment.
- **Reminders** - Send notifications to users about events or tasks.
- **Alerts** - Send notifications that require urgent or immediate attention, such as a past due date or high priority work item.

You can use activity feed notifications to do the following:

- Notify individuals about customized content that requires their attention.
- Show rich content in a Tab app or URL​.
- Support complex user interactions​.
- Send delegated notifications from the user who initiated a notification​.

Teams handles localization of system-provided notification text. Localize app-provided labels, such as the `activity type displayName`, through the app manifest localization mechanism.

## Components of activity feed notifications

Activity feed notifications in Teams are comprised of multiple pieces of information displayed together, as shown in the following image.

![Image showing the components of an activity feed notification, including actor, reason, time stamp, preview, and topic.](images/teams-activityfeednotifications/notificationtemplate.png)

The following table describes the components.

| Component | Description |
| --- | --- |
| **Avatar** | Shows who initiated the activity. |
| **App icon or custom icon** | The type of activity. For app notifications, shows the source (app icon) or type of the notification (custom icon). |
| **Title: Actor + reason** | *Actor* is the name of the user or app that initiated the activity. *Reason* describes the activity. |
| **Timestamp** | Shows when the activity happened. |
| **Text preview** | Shows a truncated line from the start of the notification. |
| **Topic** | Associated resource or the text value of the topic from the request body. |

The following image shows an example of an activity feed notification in Teams. In this example, a user shared a post in an app.

![An image of a Yammer activity feed notification](images/teams-activityfeednotifications/examplefeednotification.png)

### Types of activity feed notification cards

The following tabs show the types of activity feed notification cards that you can display. For app-generated notifications, the user logo is replaced with the app logo.

# [Desktop](#tab/desktop)
**Teams custom**

![Screenshot that shows activity feed notifications in a desktop Teams custom.](images/teams-custom.png)

**Windows**

![Screenshot that shows activity feed notifications in a Windows desktop Teams.](images/windows.png)

**Mac**

![Screenshot that shows activity feed notifications in a Mac desktop Teams.](images/mac.png)

# [Mobile](#tab/mobile)
**Android**

![Screenshot shows the activity feed notifications in a Andriod.](images/android.png)

**iOS**

![Screenshot shows the activity feed notifications in a iOS.](images/ios-notification.png)

---

## Requirements for using the activity feed notification APIs

Activity feed APIs work with a [Teams app](/en-us/microsoftteams/platform/overview). The following are the requirements for sending activity feed notifications:

- The Teams app manifest must have the Microsoft Entra app ID added to the `webApplicationInfo` section. For more information, see the [manifest schema](/en-us/microsoftteams/platform/resources/schema/manifest-schema).
- Activity notifications can be sent with or without activity types declared in the app manifest.
    - By default, you can use the activity notification APIs without declaring the `activities` section in the manifest. The `systemDefault` activity type is reserved, allowing you to provide free-form text in the `Actor+Reason` line of the activity feed notification. For more information, see Send customizable activity feed notifications.
    - If you want to send a templated notification in the traditional mode, activity types must be declared in the Activities section. For more information, see [Manifest schema](/en-us/microsoftteams/platform/resources/schema/manifest-schema).
- The Teams app must be installed for the recipient, either personally or in a [team](/en-us/graph/api/resources/team) or [chat](/en-us/graph/api/resources/chat) they're part of. For more information, see [Teams app installation](/en-us/graph/api/resources/teamsappinstallation).

### Permissions

You can use delegated or application permissions to send activity notifications. When you use application permissions, we recommend that you use [resource-specific consent (RSC)](/en-us/microsoftteams/platform/graph-api/rsc/resource-specific-consent) because the `TeamsActivity.Send.User` permission allows the user to consent to send activity notifications. You must declare RSC permissions in your Teams app [manifest schema](/en-us/microsoftteams/platform/resources/schema/manifest-schema).

### Teams app manifest updates

This section describes the changes that you need to make to the Teams app manifest to implement activity feed notifications. You need to use the [Teams app manifest](/en-us/microsoftteams/platform/resources/schema/manifest-schema) version `1.7` or greater.

```json
"$schema": "https://developer.microsoft.com/json-schemas/teams/v1.7/MicrosoftTeams.schema.json",
"manifestVersion": "1.7",
```

#### webApplicationInfo update

You must update Microsoft Entra **id** and **resource** information in your app manifest **webApplicationInfo** property.

```json
"webApplicationInfo":
{
    "id": "a3111f15-658e-457c-9689-fd20fe907330",
    "resource": "https://contosoapp.com"
}
```

| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Microsoft Entra (client ID). |
| resource | string | Resource associated with the Azure AD app. It is also known as a reply or redirect URI in the Microsoft Entra admin center app registration overview. |

Note

You might get an error if multiple Teams apps in the same scope (team, chat, or user) use the same Microsoft Entra app. Make sure that you're using unique Microsoft Entra apps.

#### Activities update

You must define the **activities** property in your app manifest to post a user activity feed.

```json
"activities":
{
  "activityTypes": [
    {
      "type": "weeklyDigest",
      "displayName": "Weekly digest",
      "description": "Your weekly digest is ready",
      "templateText": "Your weekly digest is ready"
    },
    {
      "type": "approvalRequired",
      "description": "Deployment requires your approval",
      "templateText": "{actor} created a new deployment {deploymentId}"
    }
  ]
}
```

| Parameter | Type | Description |
| --- | --- | --- |
| displayName | string | Optional. A localized label for the activity type, such as `Weekly digest`. The value must be 1 to 128 characters and contain at least one non-whitespace character. Specify a standalone category name without a host command, such as `Turn off`, or end punctuation. Preserve the casing of the resolved label. The **type** property remains the identifier. |
| description | string | Human-readable short description. The description is visible on the Microsoft Teams client. |
| templateText | string | Template text for the activity notification. You can declare your parameters by encapsulating parameters in curly brackets `{}`. |
| type | string | The type needs to be unique in a specific manifest. |

Note

- `actor` is a special parameter that always takes the caller's name. In delegated calls, `actor` is the user's name. In application-only calls, it takes the name of the Teams app.
- The reserved `systemDefault` activity type should not be provided in the `activities` section of the manifest. The reserved activity type can provide free-form text in the `Actor+Reason` line of the activity feed notification. For more information, see Send customizable activity feed notifications.
- Localize **displayName** by using the existing app manifest localization mechanism. For example, the localization key for the first activity type is `activities.activityTypes[0].displayName`. Teams adds the localized action text around the activity type label.

#### Authorization update

```json
"authorization": 
{ 
  "permissions": { 
    "resourceSpecific": [ 
      {
        "type": "Application", 
         "name": "TeamsActivity.Send.User" 
      }, 
      { 
        "type": "Application",
        "name": "TeamsActivity.Send.Group"
      }, 
      { 
        "type": "Application", 
        "name": "TeamsActivity.Send.Chat" 
      } 
    ] 
  }
} 

```

| Parameter | Type | Description |
| --- | --- | --- |
| name | string | The name of the RSC permission. For more information, see [Supported RSC permissions](/en-us/microsoftteams/platform/graph-api/rsc/resource-specific-consent#supported-rsc-permissions) |
| type | string | The resource-specific consent (RSC) permission type. |

### Install the Teams app

Teams apps can be installed in a team, a chat, or for a user personally, and can be distributed in multiple ways. For details, see [Teams app distribution methods](/en-us/microsoftteams/platform/concepts/deploy-and-publish/overview). Typically, [sideloading](/en-us/microsoftteams/platform/concepts/deploy-and-publish/apps-upload) is preferred for development purposes. After development, you can choose the right distribution method based on whether you want to distribute to one tenant or all tenants.

You can also use [Teams app installation](/en-us/graph/api/resources/teamsappinstallation) APIs to manage Teams app installations.

## Send activity feed notifications to users

Note

To show activity feed notifications on iOS and Android clients, the app must be included in the allow list. Only third-party apps are supported.

Because a Teams app can be installed for a user, in a team, or in a chat, the notifications can be sent in three contexts. For details about how to send notifications in each context, see the following topics:

- [Send notification to user in a team](/en-us/graph/api/team-sendactivitynotification)
- [Send notification to user](/en-us/graph/api/userteamwork-sendactivitynotification)
- [Send notification to user in a chat](/en-us/graph/api/chat-sendactivitynotification)

In addition, notifications can be sent in bulk to up to 100 users at a time. For details, see the following topic:

- [Send notifications to multiple users in bulk](/en-us/graph/api/teamwork-sendactivitynotificationtorecipients)

For details about what topics are supported for each scenario, see the specific APIs. Custom text-based topics are supported for all scenarios.

Note

The activity icon is based on the context in which the request is made. If the request is made with delegated permissions, the user's photo appears as the avatar, while the Teams app icon appears as the activity icon. In an application-only context, the Teams app icon is used as the avatar, and the activity icon is omitted.

## Custom activity icons in activity feed notifications

You can use custom activity icons in activity feed notifications to help users easily identify the source and intent of the notification. A notification with a custom activity icon adds a unique and Teams-native feel, enhancing user engagement with your app. The following screenshot shows an activity feed notification with a custom activity icon.

[![The screenshot shows activity feed notifications with custom activity icons.](images/custom-icon-notification-activity-feed.png)](images/custom-icon-notification-activity-feed.png#lightbox)

### Add custom activity icons in activity feed notifications

The following steps show how to add custom activity icons in activity feed notifications sent to a user:

1. Add the custom activity icons in the Teams app package. The following screenshot shows an example.

    [![The screenshot shows a Teams app package with custom activity icons for activity feed notifications.](images/teams-app-package-custom-icon.png)](images/teams-app-package-custom-icon.png#lightbox)
2. Under *manifest.json*, set **manifestVersion** to `devPreview`.
3. Under **activityTypes**, declare a list of **allowedIconIds** for the activity type you want to use custom icons.
4. Declare a list of icons under **activityIcons**. Each icon must be defined with an **id** and **iconFile**. The following example shows a code snippet.

    ```json
    "activities": {
      "activityTypes": [
        {
          "type": "announcementPosted",
          "description": "Announcement Created Activity",
          "templateText": "Alex Wilbur posted an announcement",
          "allowedIconIds": [
            "announcementCreated"
          ]
        },
        {
         "type": "reaction",
         "description": "reaction Activity",
         "templateText": "Adele Vance reacted to your post in channel",
         "allowedIconIds" : [
            "likeReaction",
            "smileReaction"
          ]
        }
      ],
      "activityIcons": [
        {
          "id": "announcementCreated",
          "iconFile": "announcement.png"
        },
        {
          "id": "likeReaction",
          "iconFile": "likeReaction.png"
        },
        {
          "id": "smileReaction",
          "iconFile": "smileReaction.png"
        }
      ]
    }
    ```

    Note

    You can't declare more than 50 icons under each activity type.

    For more information about **allowedIconIds** and **activityIcons**, see [Teams public developer preview app manifest schema](/en-us/microsoftteams/platform/resources/schema/manifest-schema-dev-preview#activitiesactivitytypes).
5. Call the notifications API beta endpoint and include the **iconId** attribute in the payload. The value of the **iconId** must match one of the icon IDs in the **allowedIconIds** for the specified activity type.

    ```http
    POST https://graph.microsoft.com/beta/users/0000000-0000-0000-0000-000000000000/teamwork/sendactivitynotification
    
    {
      "topic": {
        "source": "text",
        "value": "Loop thread",
        "webUrl": "https://teams.microsoft.com/l/loopthread/00:000000000000000000000000000.v2"
      },
      "activityType": "announcementPosted",
      "previewText": {
        "content": "new announcement posted"
      },
      "iconId" : "announcementCreated"
    }
    ```

For custom activity icon design guidelines, see [Teams Store validation guidelines for custom icons](/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/teams-store-validation-guidelines#custom-activity-icons).

To try out custom activity icons in activity feed notifications in Teams, see [Microsoft Graph activity feed sample app for JavaScript](https://github.com/OfficeDev/Microsoft-Teams-Samples/tree/main/samples/graph-activity-feed/nodejs) or [Microsoft Graph activity feed sample app for C#](https://github.com/OfficeDev/Microsoft-Teams-Samples/tree/main/samples/graph-activity-feed/csharp).

## Examples

### Example 1: Notify a user about a task created in a chat

The following example shows how you can send an activity feed notification for a new task created in a chat. In this case, the Teams app must be installed in a chat with ID `chatId` and user `569363e2-4e49-4661-87f2-16f245c5d66a` must also be part of the chat.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/chats/{chatId}/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "entityUrl",
        "value": "https://graph.microsoft.com/v1.0/chats/{chatId}"
    },
    "activityType": "taskCreated",
    "previewText": {
        "content": "New Task Created"
    },
    "recipient": {
        "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
        "userId": "569363e2-4e49-4661-87f2-16f245c5d66a"
    },
    "templateParameters": [
        {
            "name": "taskId",
            "value": "12322"
        }
    ]
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Chats.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.EntityUrl,	Value = "https://graph.microsoft.com/v1.0/chats/{chatId}",},ActivityType = "taskCreated",PreviewText = new ItemBody{	Content = "New Task Created",},Recipient = new AadUserNotificationRecipient{	OdataType = "microsoft.graph.aadUserNotificationRecipient",	UserId = "569363e2-4e49-4661-87f2-16f245c5d66a",},TemplateParameters = new List<KeyValuePair>{	new KeyValuePair	{		Name = "taskId",		Value = "12322",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Chats["{chat-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphchats "github.com/microsoftgraph/msgraph-sdk-go/chats"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphchats.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.ENTITYURL_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "https://graph.microsoft.com/v1.0/chats/{chatId}"
topic.SetValue(&value) 
requestBody.SetTopic(topic)
activityType := "taskCreated"
requestBody.SetActivityType(&activityType) 
previewText := graphmodels.NewItemBody()
content := "New Task Created"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
recipient := graphmodels.NewAadUserNotificationRecipient()
userId := "569363e2-4e49-4661-87f2-16f245c5d66a"
recipient.SetUserId(&userId) 
requestBody.SetRecipient(recipient)

keyValuePair := graphmodels.NewKeyValuePair()
name := "taskId"
keyValuePair.SetName(&name) 
value := "12322"
keyValuePair.SetValue(&value) 

templateParameters := []graphmodels.KeyValuePairable {keyValuePair,
}
requestBody.SetTemplateParameters(templateParameters)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Chats().ByChatId("chat-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.chats.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.chats.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.EntityUrl);
topic.setValue("https://graph.microsoft.com/v1.0/chats/{chatId}");
sendActivityNotificationPostRequestBody.setTopic(topic);
sendActivityNotificationPostRequestBody.setActivityType("taskCreated");
ItemBody previewText = new ItemBody();
previewText.setContent("New Task Created");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
AadUserNotificationRecipient recipient = new AadUserNotificationRecipient();
recipient.setOdataType("microsoft.graph.aadUserNotificationRecipient");
recipient.setUserId("569363e2-4e49-4661-87f2-16f245c5d66a");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
LinkedList<KeyValuePair> templateParameters = new LinkedList<KeyValuePair>();
KeyValuePair keyValuePair = new KeyValuePair();
keyValuePair.setName("taskId");
keyValuePair.setValue("12322");
templateParameters.add(keyValuePair);
sendActivityNotificationPostRequestBody.setTemplateParameters(templateParameters);
graphClient.chats().byChatId("{chat-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'entityUrl',
        value: 'https://graph.microsoft.com/v1.0/chats/{chatId}'
    },
    activityType: 'taskCreated',
    previewText: {
        content: 'New Task Created'
    },
    recipient: {
        '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
        userId: '569363e2-4e49-4661-87f2-16f245c5d66a'
    },
    templateParameters: [
        {
            name: 'taskId',
            value: '12322'
        }
    ]
};

await client.api('/chats/{chatId}/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Chats\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\AadUserNotificationRecipient;
use Microsoft\Graph\Generated\Models\KeyValuePair;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('entityUrl'));
$topic->setValue('https://graph.microsoft.com/v1.0/chats/{chatId}');
$requestBody->setTopic($topic);
$requestBody->setActivityType('taskCreated');
$previewText = new ItemBody();
$previewText->setContent('New Task Created');
$requestBody->setPreviewText($previewText);
$recipient = new AadUserNotificationRecipient();
$recipient->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipient->setUserId('569363e2-4e49-4661-87f2-16f245c5d66a');
$requestBody->setRecipient($recipient);
$templateParametersKeyValuePair1 = new KeyValuePair();
$templateParametersKeyValuePair1->setName('taskId');
$templateParametersKeyValuePair1->setValue('12322');
$templateParametersArray []= $templateParametersKeyValuePair1;
$requestBody->setTemplateParameters($templateParametersArray);

$graphServiceClient->chats()->byChatId('chat-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "entityUrl"	value = "https://graph.microsoft.com/v1.0/chats/{chatId}"}activityType = "taskCreated"previewText = @{	content = "New Task Created"}recipient = @{	"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"	userId = "569363e2-4e49-4661-87f2-16f245c5d66a"}templateParameters = @(	@{		name = "taskId"		value = "12322"	})
}

Send-MgChatActivityNotification -ChatId $chatId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.chats.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.aad_user_notification_recipient import AadUserNotificationRecipient
from msgraph.generated.models.key_value_pair import KeyValuePair
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.EntityUrl,	value = "https://graph.microsoft.com/v1.0/chats/{chatId}",),activity_type = "taskCreated",preview_text = ItemBody(	content = "New Task Created",),recipient = AadUserNotificationRecipient(	odata_type = "microsoft.graph.aadUserNotificationRecipient",	user_id = "569363e2-4e49-4661-87f2-16f245c5d66a",),template_parameters = [	KeyValuePair(		name = "taskId",		value = "12322",	),],
)

await graph_client.chats.by_chat_id('chat-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 2: Notify a user about a task created in a team

The following example shows how you can send an activity feed notification for a team. This example notifies the team owner about a new task created that requires their attention.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teams/{teamId}/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "entityUrl",
        "value": "https://graph.microsoft.com/v1.0/teams/{teamId}"
    },
    "activityType": "taskCreated",
    "previewText": {
        "content": "New Task Created"
    },
    "recipient": {
        "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
        "userId": "569363e2-4e49-4661-87f2-16f245c5d66a"
    },
    "templateParameters": [
        {
            "name": "taskId",
            "value": "12322"
        }
    ]
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teams.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.EntityUrl,	Value = "https://graph.microsoft.com/v1.0/teams/{teamId}",},ActivityType = "taskCreated",PreviewText = new ItemBody{	Content = "New Task Created",},Recipient = new AadUserNotificationRecipient{	OdataType = "microsoft.graph.aadUserNotificationRecipient",	UserId = "569363e2-4e49-4661-87f2-16f245c5d66a",},TemplateParameters = new List<KeyValuePair>{	new KeyValuePair	{		Name = "taskId",		Value = "12322",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teams["{team-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteams "github.com/microsoftgraph/msgraph-sdk-go/teams"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteams.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.ENTITYURL_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "https://graph.microsoft.com/v1.0/teams/{teamId}"
topic.SetValue(&value) 
requestBody.SetTopic(topic)
activityType := "taskCreated"
requestBody.SetActivityType(&activityType) 
previewText := graphmodels.NewItemBody()
content := "New Task Created"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
recipient := graphmodels.NewAadUserNotificationRecipient()
userId := "569363e2-4e49-4661-87f2-16f245c5d66a"
recipient.SetUserId(&userId) 
requestBody.SetRecipient(recipient)

keyValuePair := graphmodels.NewKeyValuePair()
name := "taskId"
keyValuePair.SetName(&name) 
value := "12322"
keyValuePair.SetValue(&value) 

templateParameters := []graphmodels.KeyValuePairable {keyValuePair,
}
requestBody.SetTemplateParameters(templateParameters)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teams().ByTeamId("team-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.EntityUrl);
topic.setValue("https://graph.microsoft.com/v1.0/teams/{teamId}");
sendActivityNotificationPostRequestBody.setTopic(topic);
sendActivityNotificationPostRequestBody.setActivityType("taskCreated");
ItemBody previewText = new ItemBody();
previewText.setContent("New Task Created");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
AadUserNotificationRecipient recipient = new AadUserNotificationRecipient();
recipient.setOdataType("microsoft.graph.aadUserNotificationRecipient");
recipient.setUserId("569363e2-4e49-4661-87f2-16f245c5d66a");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
LinkedList<KeyValuePair> templateParameters = new LinkedList<KeyValuePair>();
KeyValuePair keyValuePair = new KeyValuePair();
keyValuePair.setName("taskId");
keyValuePair.setValue("12322");
templateParameters.add(keyValuePair);
sendActivityNotificationPostRequestBody.setTemplateParameters(templateParameters);
graphClient.teams().byTeamId("{team-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'entityUrl',
        value: 'https://graph.microsoft.com/v1.0/teams/{teamId}'
    },
    activityType: 'taskCreated',
    previewText: {
        content: 'New Task Created'
    },
    recipient: {
        '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
        userId: '569363e2-4e49-4661-87f2-16f245c5d66a'
    },
    templateParameters: [
        {
            name: 'taskId',
            value: '12322'
        }
    ]
};

await client.api('/teams/{teamId}/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teams\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\AadUserNotificationRecipient;
use Microsoft\Graph\Generated\Models\KeyValuePair;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('entityUrl'));
$topic->setValue('https://graph.microsoft.com/v1.0/teams/{teamId}');
$requestBody->setTopic($topic);
$requestBody->setActivityType('taskCreated');
$previewText = new ItemBody();
$previewText->setContent('New Task Created');
$requestBody->setPreviewText($previewText);
$recipient = new AadUserNotificationRecipient();
$recipient->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipient->setUserId('569363e2-4e49-4661-87f2-16f245c5d66a');
$requestBody->setRecipient($recipient);
$templateParametersKeyValuePair1 = new KeyValuePair();
$templateParametersKeyValuePair1->setName('taskId');
$templateParametersKeyValuePair1->setValue('12322');
$templateParametersArray []= $templateParametersKeyValuePair1;
$requestBody->setTemplateParameters($templateParametersArray);

$graphServiceClient->teams()->byTeamId('team-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "entityUrl"	value = "https://graph.microsoft.com/v1.0/teams/{teamId}"}activityType = "taskCreated"previewText = @{	content = "New Task Created"}recipient = @{	"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"	userId = "569363e2-4e49-4661-87f2-16f245c5d66a"}templateParameters = @(	@{		name = "taskId"		value = "12322"	})
}

Send-MgTeamActivityNotification -TeamId $teamId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teams.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.aad_user_notification_recipient import AadUserNotificationRecipient
from msgraph.generated.models.key_value_pair import KeyValuePair
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.EntityUrl,	value = "https://graph.microsoft.com/v1.0/teams/{teamId}",),activity_type = "taskCreated",preview_text = ItemBody(	content = "New Task Created",),recipient = AadUserNotificationRecipient(	odata_type = "microsoft.graph.aadUserNotificationRecipient",	user_id = "569363e2-4e49-4661-87f2-16f245c5d66a",),template_parameters = [	KeyValuePair(		name = "taskId",		value = "12322",	),],
)

await graph_client.teams.by_team_id('team-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 3: Notify a user about an event using a custom topic

As the previous examples show, you can link to different team or chat aspects. However, if you want to link to an aspect that isn't part of the team or Microsoft Graph doesn't represent it, or if you want to customize the name, you can set the source of the **topic** to `text` and pass in a custom value for it. Additionally, **webUrl** is required when you use **topic** source as `text`.

The Yammer notification example shown earlier uses a custom topic because Microsoft Graph doesn't support Yammer's resources.

Note

The **webUrl** must start with the Microsoft Teams domain (`teams.microsoft.com`, for example).

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teams/{teamId}/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "text",
        "value": "Deployment Approvals Channel",
        "webUrl": "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
    },
    "activityType": "approvalRequired",
    "previewText": {
        "content": "New deployment requires your approval"
    },
    "recipient": {
        "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
        "userId": "569363e2-4e49-4661-87f2-16f245c5d66a"
    },
    "templateParameters": [
        {
            "name": "deploymentId",
            "value": "6788662"
        }
    ]
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teams.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.Text,	Value = "Deployment Approvals Channel",	WebUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",},ActivityType = "approvalRequired",PreviewText = new ItemBody{	Content = "New deployment requires your approval",},Recipient = new AadUserNotificationRecipient{	OdataType = "microsoft.graph.aadUserNotificationRecipient",	UserId = "569363e2-4e49-4661-87f2-16f245c5d66a",},TemplateParameters = new List<KeyValuePair>{	new KeyValuePair	{		Name = "deploymentId",		Value = "6788662",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teams["{team-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteams "github.com/microsoftgraph/msgraph-sdk-go/teams"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteams.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.TEXT_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "Deployment Approvals Channel"
topic.SetValue(&value) 
webUrl := "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
topic.SetWebUrl(&webUrl) 
requestBody.SetTopic(topic)
activityType := "approvalRequired"
requestBody.SetActivityType(&activityType) 
previewText := graphmodels.NewItemBody()
content := "New deployment requires your approval"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
recipient := graphmodels.NewAadUserNotificationRecipient()
userId := "569363e2-4e49-4661-87f2-16f245c5d66a"
recipient.SetUserId(&userId) 
requestBody.SetRecipient(recipient)

keyValuePair := graphmodels.NewKeyValuePair()
name := "deploymentId"
keyValuePair.SetName(&name) 
value := "6788662"
keyValuePair.SetValue(&value) 

templateParameters := []graphmodels.KeyValuePairable {keyValuePair,
}
requestBody.SetTemplateParameters(templateParameters)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teams().ByTeamId("team-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.Text);
topic.setValue("Deployment Approvals Channel");
topic.setWebUrl("https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000");
sendActivityNotificationPostRequestBody.setTopic(topic);
sendActivityNotificationPostRequestBody.setActivityType("approvalRequired");
ItemBody previewText = new ItemBody();
previewText.setContent("New deployment requires your approval");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
AadUserNotificationRecipient recipient = new AadUserNotificationRecipient();
recipient.setOdataType("microsoft.graph.aadUserNotificationRecipient");
recipient.setUserId("569363e2-4e49-4661-87f2-16f245c5d66a");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
LinkedList<KeyValuePair> templateParameters = new LinkedList<KeyValuePair>();
KeyValuePair keyValuePair = new KeyValuePair();
keyValuePair.setName("deploymentId");
keyValuePair.setValue("6788662");
templateParameters.add(keyValuePair);
sendActivityNotificationPostRequestBody.setTemplateParameters(templateParameters);
graphClient.teams().byTeamId("{team-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'text',
        value: 'Deployment Approvals Channel',
        webUrl: 'https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000'
    },
    activityType: 'approvalRequired',
    previewText: {
        content: 'New deployment requires your approval'
    },
    recipient: {
        '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
        userId: '569363e2-4e49-4661-87f2-16f245c5d66a'
    },
    templateParameters: [
        {
            name: 'deploymentId',
            value: '6788662'
        }
    ]
};

await client.api('/teams/{teamId}/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teams\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\AadUserNotificationRecipient;
use Microsoft\Graph\Generated\Models\KeyValuePair;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('text'));
$topic->setValue('Deployment Approvals Channel');
$topic->setWebUrl('https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000');
$requestBody->setTopic($topic);
$requestBody->setActivityType('approvalRequired');
$previewText = new ItemBody();
$previewText->setContent('New deployment requires your approval');
$requestBody->setPreviewText($previewText);
$recipient = new AadUserNotificationRecipient();
$recipient->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipient->setUserId('569363e2-4e49-4661-87f2-16f245c5d66a');
$requestBody->setRecipient($recipient);
$templateParametersKeyValuePair1 = new KeyValuePair();
$templateParametersKeyValuePair1->setName('deploymentId');
$templateParametersKeyValuePair1->setValue('6788662');
$templateParametersArray []= $templateParametersKeyValuePair1;
$requestBody->setTemplateParameters($templateParametersArray);

$graphServiceClient->teams()->byTeamId('team-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "text"	value = "Deployment Approvals Channel"	webUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"}activityType = "approvalRequired"previewText = @{	content = "New deployment requires your approval"}recipient = @{	"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"	userId = "569363e2-4e49-4661-87f2-16f245c5d66a"}templateParameters = @(	@{		name = "deploymentId"		value = "6788662"	})
}

Send-MgTeamActivityNotification -TeamId $teamId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teams.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.aad_user_notification_recipient import AadUserNotificationRecipient
from msgraph.generated.models.key_value_pair import KeyValuePair
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.Text,	value = "Deployment Approvals Channel",	web_url = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",),activity_type = "approvalRequired",preview_text = ItemBody(	content = "New deployment requires your approval",),recipient = AadUserNotificationRecipient(	odata_type = "microsoft.graph.aadUserNotificationRecipient",	user_id = "569363e2-4e49-4661-87f2-16f245c5d66a",),template_parameters = [	KeyValuePair(		name = "deploymentId",		value = "6788662",	),],
)

await graph_client.teams.by_team_id('team-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 4: Notify the team members about an event

The following example shows how you can send an activity feed notification to all team members. This example notifies the team members about a new event.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teams/7155e3c8-175e-4311-97ef-572edc3aa3db/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "text",
        "value": "Weekly Virtual Social",
        "webUrl": "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
    },
    "previewText": {
        "content": "It will be fun!"
    },
    "activityType": "eventCreated",
    "recipient": {
        "@odata.type": "microsoft.graph.teamMembersNotificationRecipient",
        "teamId": "7155e3c8-175e-4311-97ef-572edc3aa3db"
    }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teams.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.Text,	Value = "Weekly Virtual Social",	WebUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",},PreviewText = new ItemBody{	Content = "It will be fun!",},ActivityType = "eventCreated",Recipient = new TeamMembersNotificationRecipient{	OdataType = "microsoft.graph.teamMembersNotificationRecipient",	TeamId = "7155e3c8-175e-4311-97ef-572edc3aa3db",},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teams["{team-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteams "github.com/microsoftgraph/msgraph-sdk-go/teams"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteams.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.TEXT_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "Weekly Virtual Social"
topic.SetValue(&value) 
webUrl := "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
topic.SetWebUrl(&webUrl) 
requestBody.SetTopic(topic)
previewText := graphmodels.NewItemBody()
content := "It will be fun!"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
activityType := "eventCreated"
requestBody.SetActivityType(&activityType) 
recipient := graphmodels.NewTeamMembersNotificationRecipient()
teamId := "7155e3c8-175e-4311-97ef-572edc3aa3db"
recipient.SetTeamId(&teamId) 
requestBody.SetRecipient(recipient)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teams().ByTeamId("team-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.Text);
topic.setValue("Weekly Virtual Social");
topic.setWebUrl("https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000");
sendActivityNotificationPostRequestBody.setTopic(topic);
ItemBody previewText = new ItemBody();
previewText.setContent("It will be fun!");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
sendActivityNotificationPostRequestBody.setActivityType("eventCreated");
TeamMembersNotificationRecipient recipient = new TeamMembersNotificationRecipient();
recipient.setOdataType("microsoft.graph.teamMembersNotificationRecipient");
recipient.setTeamId("7155e3c8-175e-4311-97ef-572edc3aa3db");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
graphClient.teams().byTeamId("{team-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'text',
        value: 'Weekly Virtual Social',
        webUrl: 'https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000'
    },
    previewText: {
        content: 'It will be fun!'
    },
    activityType: 'eventCreated',
    recipient: {
        '@odata.type': 'microsoft.graph.teamMembersNotificationRecipient',
        teamId: '7155e3c8-175e-4311-97ef-572edc3aa3db'
    }
};

await client.api('/teams/7155e3c8-175e-4311-97ef-572edc3aa3db/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teams\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\TeamMembersNotificationRecipient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('text'));
$topic->setValue('Weekly Virtual Social');
$topic->setWebUrl('https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000');
$requestBody->setTopic($topic);
$previewText = new ItemBody();
$previewText->setContent('It will be fun!');
$requestBody->setPreviewText($previewText);
$requestBody->setActivityType('eventCreated');
$recipient = new TeamMembersNotificationRecipient();
$recipient->setOdataType('microsoft.graph.teamMembersNotificationRecipient');
$recipient->setTeamId('7155e3c8-175e-4311-97ef-572edc3aa3db');
$requestBody->setRecipient($recipient);

$graphServiceClient->teams()->byTeamId('team-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "text"	value = "Weekly Virtual Social"	webUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"}previewText = @{	content = "It will be fun!"}activityType = "eventCreated"recipient = @{	"@odata.type" = "microsoft.graph.teamMembersNotificationRecipient"	teamId = "7155e3c8-175e-4311-97ef-572edc3aa3db"}
}

Send-MgTeamActivityNotification -TeamId $teamId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teams.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.team_members_notification_recipient import TeamMembersNotificationRecipient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.Text,	value = "Weekly Virtual Social",	web_url = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",),preview_text = ItemBody(	content = "It will be fun!",),activity_type = "eventCreated",recipient = TeamMembersNotificationRecipient(	odata_type = "microsoft.graph.teamMembersNotificationRecipient",	team_id = "7155e3c8-175e-4311-97ef-572edc3aa3db",),
)

await graph_client.teams.by_team_id('team-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 5: Notify the channel members about an event

The following example shows how you can send an activity feed notification to all channel members. This example notifies the channel members about a new event.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teams/7155e3c8-175e-4311-97ef-572edc3aa3db/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "text",
        "value": "Weekly Virtual Social",
        "webUrl": "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
    },
    "previewText": {
        "content": "It will be fun!"
    },
    "activityType": "eventCreated",
    "recipient": {
        "@odata.type": "microsoft.graph.channelMembersNotificationRecipient",
        "teamId": "7155e3c8-175e-4311-97ef-572edc3aa3db",
        "channelId": "19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2"
    }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teams.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.Text,	Value = "Weekly Virtual Social",	WebUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",},PreviewText = new ItemBody{	Content = "It will be fun!",},ActivityType = "eventCreated",Recipient = new ChannelMembersNotificationRecipient{	OdataType = "microsoft.graph.channelMembersNotificationRecipient",	TeamId = "7155e3c8-175e-4311-97ef-572edc3aa3db",	ChannelId = "19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2",},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teams["{team-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteams "github.com/microsoftgraph/msgraph-sdk-go/teams"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteams.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.TEXT_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "Weekly Virtual Social"
topic.SetValue(&value) 
webUrl := "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
topic.SetWebUrl(&webUrl) 
requestBody.SetTopic(topic)
previewText := graphmodels.NewItemBody()
content := "It will be fun!"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
activityType := "eventCreated"
requestBody.SetActivityType(&activityType) 
recipient := graphmodels.NewChannelMembersNotificationRecipient()
teamId := "7155e3c8-175e-4311-97ef-572edc3aa3db"
recipient.SetTeamId(&teamId) 
channelId := "19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2"
recipient.SetChannelId(&channelId) 
requestBody.SetRecipient(recipient)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teams().ByTeamId("team-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.Text);
topic.setValue("Weekly Virtual Social");
topic.setWebUrl("https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000");
sendActivityNotificationPostRequestBody.setTopic(topic);
ItemBody previewText = new ItemBody();
previewText.setContent("It will be fun!");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
sendActivityNotificationPostRequestBody.setActivityType("eventCreated");
ChannelMembersNotificationRecipient recipient = new ChannelMembersNotificationRecipient();
recipient.setOdataType("microsoft.graph.channelMembersNotificationRecipient");
recipient.setTeamId("7155e3c8-175e-4311-97ef-572edc3aa3db");
recipient.setChannelId("19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
graphClient.teams().byTeamId("{team-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'text',
        value: 'Weekly Virtual Social',
        webUrl: 'https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000'
    },
    previewText: {
        content: 'It will be fun!'
    },
    activityType: 'eventCreated',
    recipient: {
        '@odata.type': 'microsoft.graph.channelMembersNotificationRecipient',
        teamId: '7155e3c8-175e-4311-97ef-572edc3aa3db',
        channelId: '19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2'
    }
};

await client.api('/teams/7155e3c8-175e-4311-97ef-572edc3aa3db/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teams\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\ChannelMembersNotificationRecipient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('text'));
$topic->setValue('Weekly Virtual Social');
$topic->setWebUrl('https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000');
$requestBody->setTopic($topic);
$previewText = new ItemBody();
$previewText->setContent('It will be fun!');
$requestBody->setPreviewText($previewText);
$requestBody->setActivityType('eventCreated');
$recipient = new ChannelMembersNotificationRecipient();
$recipient->setOdataType('microsoft.graph.channelMembersNotificationRecipient');
$recipient->setTeamId('7155e3c8-175e-4311-97ef-572edc3aa3db');
$recipient->setChannelId('19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2');
$requestBody->setRecipient($recipient);

$graphServiceClient->teams()->byTeamId('team-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "text"	value = "Weekly Virtual Social"	webUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"}previewText = @{	content = "It will be fun!"}activityType = "eventCreated"recipient = @{	"@odata.type" = "microsoft.graph.channelMembersNotificationRecipient"	teamId = "7155e3c8-175e-4311-97ef-572edc3aa3db"	channelId = "19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2"}
}

Send-MgTeamActivityNotification -TeamId $teamId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teams.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.channel_members_notification_recipient import ChannelMembersNotificationRecipient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.Text,	value = "Weekly Virtual Social",	web_url = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",),preview_text = ItemBody(	content = "It will be fun!",),activity_type = "eventCreated",recipient = ChannelMembersNotificationRecipient(	odata_type = "microsoft.graph.channelMembersNotificationRecipient",	team_id = "7155e3c8-175e-4311-97ef-572edc3aa3db",	channel_id = "19:0ea5de04de4743bcb4cd20cb99235d99@thread.tacv2",),
)

await graph_client.teams.by_team_id('team-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 6: Notify the chat members about an event

The following example shows how you can send an activity feed notification to all chat members. This example notifies the chat members about a new event.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/chats/19:d65713bc498c4a428c71ef9353e6ce20@thread.v2/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "text",
        "value": "Weekly Virtual Social",
        "webUrl": "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
    },
    "previewText": {
        "content": "It will be fun!"
    },
    "activityType": "eventCreated",
    "recipient": {
        "@odata.type": "microsoft.graph.chatMembersNotificationRecipient",
        "chatId": "19:d65713bc498c4a428c71ef9353e6ce20@thread.v2"
    }
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Chats.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.Text,	Value = "Weekly Virtual Social",	WebUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",},PreviewText = new ItemBody{	Content = "It will be fun!",},ActivityType = "eventCreated",Recipient = new ChatMembersNotificationRecipient{	OdataType = "microsoft.graph.chatMembersNotificationRecipient",	ChatId = "19:d65713bc498c4a428c71ef9353e6ce20@thread.v2",},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Chats["{chat-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphchats "github.com/microsoftgraph/msgraph-sdk-go/chats"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphchats.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.TEXT_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "Weekly Virtual Social"
topic.SetValue(&value) 
webUrl := "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"
topic.SetWebUrl(&webUrl) 
requestBody.SetTopic(topic)
previewText := graphmodels.NewItemBody()
content := "It will be fun!"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
activityType := "eventCreated"
requestBody.SetActivityType(&activityType) 
recipient := graphmodels.NewChatMembersNotificationRecipient()
chatId := "19:d65713bc498c4a428c71ef9353e6ce20@thread.v2"
recipient.SetChatId(&chatId) 
requestBody.SetRecipient(recipient)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Chats().ByChatId("chat-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.chats.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.chats.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.Text);
topic.setValue("Weekly Virtual Social");
topic.setWebUrl("https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000");
sendActivityNotificationPostRequestBody.setTopic(topic);
ItemBody previewText = new ItemBody();
previewText.setContent("It will be fun!");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
sendActivityNotificationPostRequestBody.setActivityType("eventCreated");
ChatMembersNotificationRecipient recipient = new ChatMembersNotificationRecipient();
recipient.setOdataType("microsoft.graph.chatMembersNotificationRecipient");
recipient.setChatId("19:d65713bc498c4a428c71ef9353e6ce20@thread.v2");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
graphClient.chats().byChatId("{chat-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'text',
        value: 'Weekly Virtual Social',
        webUrl: 'https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000'
    },
    previewText: {
        content: 'It will be fun!'
    },
    activityType: 'eventCreated',
    recipient: {
        '@odata.type': 'microsoft.graph.chatMembersNotificationRecipient',
        chatId: '19:d65713bc498c4a428c71ef9353e6ce20@thread.v2'
    }
};

await client.api('/chats/19:d65713bc498c4a428c71ef9353e6ce20@thread.v2/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Chats\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\ChatMembersNotificationRecipient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('text'));
$topic->setValue('Weekly Virtual Social');
$topic->setWebUrl('https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000');
$requestBody->setTopic($topic);
$previewText = new ItemBody();
$previewText->setContent('It will be fun!');
$requestBody->setPreviewText($previewText);
$requestBody->setActivityType('eventCreated');
$recipient = new ChatMembersNotificationRecipient();
$recipient->setOdataType('microsoft.graph.chatMembersNotificationRecipient');
$recipient->setChatId('19:d65713bc498c4a428c71ef9353e6ce20@thread.v2');
$requestBody->setRecipient($recipient);

$graphServiceClient->chats()->byChatId('chat-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "text"	value = "Weekly Virtual Social"	webUrl = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000"}previewText = @{	content = "It will be fun!"}activityType = "eventCreated"recipient = @{	"@odata.type" = "microsoft.graph.chatMembersNotificationRecipient"	chatId = "19:d65713bc498c4a428c71ef9353e6ce20@thread.v2"}
}

Send-MgChatActivityNotification -ChatId $chatId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.chats.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.chat_members_notification_recipient import ChatMembersNotificationRecipient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.Text,	value = "Weekly Virtual Social",	web_url = "https://teams.microsoft.com/l/message/19:448cfd2ac2a7490a9084a9ed14cttr78c@thread.skype/1605223780000?tenantId=c8b1bf45-3834-4ecf-971a-b4c755ee677d&groupId=d4c2a937-f097-435a-bc91-5c1683ca7245&parentMessageId=1605223771864&teamName=Approvals&channelName=Azure%20DevOps&createdTime=1605223780000",),preview_text = ItemBody(	content = "It will be fun!",),activity_type = "eventCreated",recipient = ChatMembersNotificationRecipient(	odata_type = "microsoft.graph.chatMembersNotificationRecipient",	chat_id = "19:d65713bc498c4a428c71ef9353e6ce20@thread.v2",),
)

await graph_client.chats.by_chat_id('chat-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

### Example 7: Notify multiple users about pending finance approval requests

The following example shows how to send an activity feed notification to multiple users in bulk. This example notifies multiple stakeholders about pending finance approval requests.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teamwork/sendActivityNotificationToRecipients
Content-Type: application/json

{
    "topic": {
        "source": "entityUrl",
        "value": "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}"
    },
    "activityType": "pendingFinanceApprovalRequests",
    "previewText": {
        "content": "Internal spending team has a pending finance approval requests"
    },
    "recipients": [
        {
            "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
            "userId": "569363e2-4e49-4661-87f2-16f245c5d66a"
        },
        {
            "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
            "userId": "ab88234e-0874-477c-9638-d144296ed04f"
        },
        {
            "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
            "userId": "01c64f53-69aa-42c7-9b7f-9f75195d6bfc"
        }
    ],
    "templateParameters": [
        {
            "name": "pendingRequestCount",
            "value": "5"
        }
    ] 
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teamwork.SendActivityNotificationToRecipients;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationToRecipientsPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.EntityUrl,	Value = "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}",},ActivityType = "pendingFinanceApprovalRequests",PreviewText = new ItemBody{	Content = "Internal spending team has a pending finance approval requests",},Recipients = new List<TeamworkNotificationRecipient>{	new AadUserNotificationRecipient	{		OdataType = "microsoft.graph.aadUserNotificationRecipient",		UserId = "569363e2-4e49-4661-87f2-16f245c5d66a",	},	new AadUserNotificationRecipient	{		OdataType = "microsoft.graph.aadUserNotificationRecipient",		UserId = "ab88234e-0874-477c-9638-d144296ed04f",	},	new AadUserNotificationRecipient	{		OdataType = "microsoft.graph.aadUserNotificationRecipient",		UserId = "01c64f53-69aa-42c7-9b7f-9f75195d6bfc",	},},TemplateParameters = new List<KeyValuePair>{	new KeyValuePair	{		Name = "pendingRequestCount",		Value = "5",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teamwork.SendActivityNotificationToRecipients.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteamwork "github.com/microsoftgraph/msgraph-sdk-go/teamwork"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteamwork.NewSendActivityNotificationToRecipientsPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.ENTITYURL_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}"
topic.SetValue(&value) 
requestBody.SetTopic(topic)
activityType := "pendingFinanceApprovalRequests"
requestBody.SetActivityType(&activityType) 
previewText := graphmodels.NewItemBody()
content := "Internal spending team has a pending finance approval requests"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)

teamworkNotificationRecipient := graphmodels.NewAadUserNotificationRecipient()
userId := "569363e2-4e49-4661-87f2-16f245c5d66a"
teamworkNotificationRecipient.SetUserId(&userId) 
teamworkNotificationRecipient1 := graphmodels.NewAadUserNotificationRecipient()
userId := "ab88234e-0874-477c-9638-d144296ed04f"
teamworkNotificationRecipient1.SetUserId(&userId) 
teamworkNotificationRecipient2 := graphmodels.NewAadUserNotificationRecipient()
userId := "01c64f53-69aa-42c7-9b7f-9f75195d6bfc"
teamworkNotificationRecipient2.SetUserId(&userId) 

recipients := []graphmodels.TeamworkNotificationRecipientable {teamworkNotificationRecipient,teamworkNotificationRecipient1,teamworkNotificationRecipient2,
}
requestBody.SetRecipients(recipients)

keyValuePair := graphmodels.NewKeyValuePair()
name := "pendingRequestCount"
keyValuePair.SetName(&name) 
value := "5"
keyValuePair.SetValue(&value) 

templateParameters := []graphmodels.KeyValuePairable {keyValuePair,
}
requestBody.SetTemplateParameters(templateParameters)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teamwork().SendActivityNotificationToRecipients().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teamwork.sendactivitynotificationtorecipients.SendActivityNotificationToRecipientsPostRequestBody sendActivityNotificationToRecipientsPostRequestBody = new com.microsoft.graph.teamwork.sendactivitynotificationtorecipients.SendActivityNotificationToRecipientsPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.EntityUrl);
topic.setValue("https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}");
sendActivityNotificationToRecipientsPostRequestBody.setTopic(topic);
sendActivityNotificationToRecipientsPostRequestBody.setActivityType("pendingFinanceApprovalRequests");
ItemBody previewText = new ItemBody();
previewText.setContent("Internal spending team has a pending finance approval requests");
sendActivityNotificationToRecipientsPostRequestBody.setPreviewText(previewText);
LinkedList<TeamworkNotificationRecipient> recipients = new LinkedList<TeamworkNotificationRecipient>();
AadUserNotificationRecipient teamworkNotificationRecipient = new AadUserNotificationRecipient();
teamworkNotificationRecipient.setOdataType("microsoft.graph.aadUserNotificationRecipient");
teamworkNotificationRecipient.setUserId("569363e2-4e49-4661-87f2-16f245c5d66a");
recipients.add(teamworkNotificationRecipient);
AadUserNotificationRecipient teamworkNotificationRecipient1 = new AadUserNotificationRecipient();
teamworkNotificationRecipient1.setOdataType("microsoft.graph.aadUserNotificationRecipient");
teamworkNotificationRecipient1.setUserId("ab88234e-0874-477c-9638-d144296ed04f");
recipients.add(teamworkNotificationRecipient1);
AadUserNotificationRecipient teamworkNotificationRecipient2 = new AadUserNotificationRecipient();
teamworkNotificationRecipient2.setOdataType("microsoft.graph.aadUserNotificationRecipient");
teamworkNotificationRecipient2.setUserId("01c64f53-69aa-42c7-9b7f-9f75195d6bfc");
recipients.add(teamworkNotificationRecipient2);
sendActivityNotificationToRecipientsPostRequestBody.setRecipients(recipients);
LinkedList<KeyValuePair> templateParameters = new LinkedList<KeyValuePair>();
KeyValuePair keyValuePair = new KeyValuePair();
keyValuePair.setName("pendingRequestCount");
keyValuePair.setValue("5");
templateParameters.add(keyValuePair);
sendActivityNotificationToRecipientsPostRequestBody.setTemplateParameters(templateParameters);
graphClient.teamwork().sendActivityNotificationToRecipients().post(sendActivityNotificationToRecipientsPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotificationToRecipients = {
    topic: {
        source: 'entityUrl',
        value: 'https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}'
    },
    activityType: 'pendingFinanceApprovalRequests',
    previewText: {
        content: 'Internal spending team has a pending finance approval requests'
    },
    recipients: [
        {
            '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
            userId: '569363e2-4e49-4661-87f2-16f245c5d66a'
        },
        {
            '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
            userId: 'ab88234e-0874-477c-9638-d144296ed04f'
        },
        {
            '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
            userId: '01c64f53-69aa-42c7-9b7f-9f75195d6bfc'
        }
    ],
    templateParameters: [
        {
            name: 'pendingRequestCount',
            value: '5'
        }
    ] 
};

await client.api('/teamwork/sendActivityNotificationToRecipients').post(sendActivityNotificationToRecipients);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teamwork\SendActivityNotificationToRecipients\SendActivityNotificationToRecipientsPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\TeamworkNotificationRecipient;
use Microsoft\Graph\Generated\Models\AadUserNotificationRecipient;
use Microsoft\Graph\Generated\Models\KeyValuePair;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationToRecipientsPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('entityUrl'));
$topic->setValue('https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}');
$requestBody->setTopic($topic);
$requestBody->setActivityType('pendingFinanceApprovalRequests');
$previewText = new ItemBody();
$previewText->setContent('Internal spending team has a pending finance approval requests');
$requestBody->setPreviewText($previewText);
$recipientsTeamworkNotificationRecipient1 = new AadUserNotificationRecipient();
$recipientsTeamworkNotificationRecipient1->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipientsTeamworkNotificationRecipient1->setUserId('569363e2-4e49-4661-87f2-16f245c5d66a');
$recipientsArray []= $recipientsTeamworkNotificationRecipient1;
$recipientsTeamworkNotificationRecipient2 = new AadUserNotificationRecipient();
$recipientsTeamworkNotificationRecipient2->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipientsTeamworkNotificationRecipient2->setUserId('ab88234e-0874-477c-9638-d144296ed04f');
$recipientsArray []= $recipientsTeamworkNotificationRecipient2;
$recipientsTeamworkNotificationRecipient3 = new AadUserNotificationRecipient();
$recipientsTeamworkNotificationRecipient3->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipientsTeamworkNotificationRecipient3->setUserId('01c64f53-69aa-42c7-9b7f-9f75195d6bfc');
$recipientsArray []= $recipientsTeamworkNotificationRecipient3;
$requestBody->setRecipients($recipientsArray);

$templateParametersKeyValuePair1 = new KeyValuePair();
$templateParametersKeyValuePair1->setName('pendingRequestCount');
$templateParametersKeyValuePair1->setValue('5');
$templateParametersArray []= $templateParametersKeyValuePair1;
$requestBody->setTemplateParameters($templateParametersArray);

$graphServiceClient->teamwork()->sendActivityNotificationToRecipients()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "entityUrl"	value = "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}"}activityType = "pendingFinanceApprovalRequests"previewText = @{	content = "Internal spending team has a pending finance approval requests"}recipients = @(	@{		"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"		userId = "569363e2-4e49-4661-87f2-16f245c5d66a"	}	@{		"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"		userId = "ab88234e-0874-477c-9638-d144296ed04f"	}	@{		"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"		userId = "01c64f53-69aa-42c7-9b7f-9f75195d6bfc"	})templateParameters = @(	@{		name = "pendingRequestCount"		value = "5"	})
}

Send-MgTeamworkActivityNotificationToRecipient -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teamwork.send_activity_notification_to_recipients.send_activity_notification_to_recipients_post_request_body import SendActivityNotificationToRecipientsPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.teamwork_notification_recipient import TeamworkNotificationRecipient
from msgraph.generated.models.aad_user_notification_recipient import AadUserNotificationRecipient
from msgraph.generated.models.key_value_pair import KeyValuePair
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationToRecipientsPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.EntityUrl,	value = "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/{teamsAppId}",),activity_type = "pendingFinanceApprovalRequests",preview_text = ItemBody(	content = "Internal spending team has a pending finance approval requests",),recipients = [	AadUserNotificationRecipient(		odata_type = "microsoft.graph.aadUserNotificationRecipient",		user_id = "569363e2-4e49-4661-87f2-16f245c5d66a",	),	AadUserNotificationRecipient(		odata_type = "microsoft.graph.aadUserNotificationRecipient",		user_id = "ab88234e-0874-477c-9638-d144296ed04f",	),	AadUserNotificationRecipient(		odata_type = "microsoft.graph.aadUserNotificationRecipient",		user_id = "01c64f53-69aa-42c7-9b7f-9f75195d6bfc",	),],template_parameters = [	KeyValuePair(		name = "pendingRequestCount",		value = "5",	),],
)

await graph_client.teamwork.send_activity_notification_to_recipients.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 202 Accepted
```

### Example 8: Send a notification to a user using the systemDefault activity type

The following example shows how you can send an activity notification for a team without activity types defined in the manifest. You have the flexibility to provide free-form text here. For more information, see Reserved activity types.

This example notifies the team owner to take a short break. Modify the **value** in **templateParameters** to customize the notification for various scenarios.

#### Request

# [HTTP](#tab/http)
```http
POST https://graph.microsoft.com/v1.0/teams/{teamId}/sendActivityNotification
Content-Type: application/json

{
    "topic": {
        "source": "entityUrl",
        "value": "https://graph.microsoft.com/v1.0/teams/{teamId}"
    },
    "activityType": "systemDefault",
    "previewText": {
        "content": "Take a break"
    },
    "recipient": {
        "@odata.type": "microsoft.graph.aadUserNotificationRecipient",
        "userId": "569363e2-4e49-4661-87f2-16f245c5d66a"
    },
    "templateParameters": [
        {
            "name": "systemDefaultText",
            "value": "You need to take a short break"
        }
    ]
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Teams.Item.SendActivityNotification;
using Microsoft.Graph.Models;

var requestBody = new SendActivityNotificationPostRequestBody
{Topic = new TeamworkActivityTopic{	Source = TeamworkActivityTopicSource.EntityUrl,	Value = "https://graph.microsoft.com/v1.0/teams/{teamId}",},ActivityType = "systemDefault",PreviewText = new ItemBody{	Content = "Take a break",},Recipient = new AadUserNotificationRecipient{	OdataType = "microsoft.graph.aadUserNotificationRecipient",	UserId = "569363e2-4e49-4661-87f2-16f245c5d66a",},TemplateParameters = new List<KeyValuePair>{	new KeyValuePair	{		Name = "systemDefaultText",		Value = "You need to take a short break",	},},
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Teams["{team-id}"].SendActivityNotification.PostAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v1.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-sdk-go"  graphteams "github.com/microsoftgraph/msgraph-sdk-go/teams"  graphmodels "github.com/microsoftgraph/msgraph-sdk-go/models"  //other-imports
)

requestBody := graphteams.NewSendActivityNotificationPostRequestBody()
topic := graphmodels.NewTeamworkActivityTopic()
source := graphmodels.ENTITYURL_TEAMWORKACTIVITYTOPICSOURCE 
topic.SetSource(&source) 
value := "https://graph.microsoft.com/v1.0/teams/{teamId}"
topic.SetValue(&value) 
requestBody.SetTopic(topic)
activityType := "systemDefault"
requestBody.SetActivityType(&activityType) 
previewText := graphmodels.NewItemBody()
content := "Take a break"
previewText.SetContent(&content) 
requestBody.SetPreviewText(previewText)
recipient := graphmodels.NewAadUserNotificationRecipient()
userId := "569363e2-4e49-4661-87f2-16f245c5d66a"
recipient.SetUserId(&userId) 
requestBody.SetRecipient(recipient)

keyValuePair := graphmodels.NewKeyValuePair()
name := "systemDefaultText"
keyValuePair.SetName(&name) 
value := "You need to take a short break"
keyValuePair.SetValue(&value) 

templateParameters := []graphmodels.KeyValuePairable {keyValuePair,
}
requestBody.SetTemplateParameters(templateParameters)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Teams().ByTeamId("team-id").SendActivityNotification().Post(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody sendActivityNotificationPostRequestBody = new com.microsoft.graph.teams.item.sendactivitynotification.SendActivityNotificationPostRequestBody();
TeamworkActivityTopic topic = new TeamworkActivityTopic();
topic.setSource(TeamworkActivityTopicSource.EntityUrl);
topic.setValue("https://graph.microsoft.com/v1.0/teams/{teamId}");
sendActivityNotificationPostRequestBody.setTopic(topic);
sendActivityNotificationPostRequestBody.setActivityType("systemDefault");
ItemBody previewText = new ItemBody();
previewText.setContent("Take a break");
sendActivityNotificationPostRequestBody.setPreviewText(previewText);
AadUserNotificationRecipient recipient = new AadUserNotificationRecipient();
recipient.setOdataType("microsoft.graph.aadUserNotificationRecipient");
recipient.setUserId("569363e2-4e49-4661-87f2-16f245c5d66a");
sendActivityNotificationPostRequestBody.setRecipient(recipient);
LinkedList<KeyValuePair> templateParameters = new LinkedList<KeyValuePair>();
KeyValuePair keyValuePair = new KeyValuePair();
keyValuePair.setName("systemDefaultText");
keyValuePair.setValue("You need to take a short break");
templateParameters.add(keyValuePair);
sendActivityNotificationPostRequestBody.setTemplateParameters(templateParameters);
graphClient.teams().byTeamId("{team-id}").sendActivityNotification().post(sendActivityNotificationPostRequestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const sendActivityNotification = {
    topic: {
        source: 'entityUrl',
        value: 'https://graph.microsoft.com/v1.0/teams/{teamId}'
    },
    activityType: 'systemDefault',
    previewText: {
        content: 'Take a break'
    },
    recipient: {
        '@odata.type': 'microsoft.graph.aadUserNotificationRecipient',
        userId: '569363e2-4e49-4661-87f2-16f245c5d66a'
    },
    templateParameters: [
        {
            name: 'systemDefaultText',
            value: 'You need to take a short break'
        }
    ]
};

await client.api('/teams/{teamId}/sendActivityNotification').post(sendActivityNotification);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\GraphServiceClient;
use Microsoft\Graph\Generated\Teams\Item\SendActivityNotification\SendActivityNotificationPostRequestBody;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopic;
use Microsoft\Graph\Generated\Models\TeamworkActivityTopicSource;
use Microsoft\Graph\Generated\Models\ItemBody;
use Microsoft\Graph\Generated\Models\AadUserNotificationRecipient;
use Microsoft\Graph\Generated\Models\KeyValuePair;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new SendActivityNotificationPostRequestBody();
$topic = new TeamworkActivityTopic();
$topic->setSource(new TeamworkActivityTopicSource('entityUrl'));
$topic->setValue('https://graph.microsoft.com/v1.0/teams/{teamId}');
$requestBody->setTopic($topic);
$requestBody->setActivityType('systemDefault');
$previewText = new ItemBody();
$previewText->setContent('Take a break');
$requestBody->setPreviewText($previewText);
$recipient = new AadUserNotificationRecipient();
$recipient->setOdataType('microsoft.graph.aadUserNotificationRecipient');
$recipient->setUserId('569363e2-4e49-4661-87f2-16f245c5d66a');
$requestBody->setRecipient($recipient);
$templateParametersKeyValuePair1 = new KeyValuePair();
$templateParametersKeyValuePair1->setName('systemDefaultText');
$templateParametersKeyValuePair1->setValue('You need to take a short break');
$templateParametersArray []= $templateParametersKeyValuePair1;
$requestBody->setTemplateParameters($templateParametersArray);

$graphServiceClient->teams()->byTeamId('team-id')->sendActivityNotification()->post($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Teams

$params = @{topic = @{	source = "entityUrl"	value = "https://graph.microsoft.com/v1.0/teams/{teamId}"}activityType = "systemDefault"previewText = @{	content = "Take a break"}recipient = @{	"@odata.type" = "microsoft.graph.aadUserNotificationRecipient"	userId = "569363e2-4e49-4661-87f2-16f245c5d66a"}templateParameters = @(	@{		name = "systemDefaultText"		value = "You need to take a short break"	})
}

Send-MgTeamActivityNotification -TeamId $teamId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.teams.item.send_activity_notification.send_activity_notification_post_request_body import SendActivityNotificationPostRequestBody
from msgraph.generated.models.teamwork_activity_topic import TeamworkActivityTopic
from msgraph.generated.models.teamwork_activity_topic_source import TeamworkActivityTopicSource
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.aad_user_notification_recipient import AadUserNotificationRecipient
from msgraph.generated.models.key_value_pair import KeyValuePair
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = SendActivityNotificationPostRequestBody(topic = TeamworkActivityTopic(	source = TeamworkActivityTopicSource.EntityUrl,	value = "https://graph.microsoft.com/v1.0/teams/{teamId}",),activity_type = "systemDefault",preview_text = ItemBody(	content = "Take a break",),recipient = AadUserNotificationRecipient(	odata_type = "microsoft.graph.aadUserNotificationRecipient",	user_id = "569363e2-4e49-4661-87f2-16f245c5d66a",),template_parameters = [	KeyValuePair(		name = "systemDefaultText",		value = "You need to take a short break",	),],
)

await graph_client.teams.by_team_id('team-id').send_activity_notification.post(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

#### Response

```http
HTTP/1.1 204 No Content
```

## Reserved activity types

The `systemDefault` activity type is reserved and can't be used in the manifest while declaring Activities. You can use the `systemDefault` activity type to:

- Easily test new scenarios and/or quickly try the activity feed notification APIs without defining activity types in your app manifest.
- For Store apps, save time and streamline the process because you don't need to constantly adjust activity types in your app manifest. The `systemDefault` activity type is ready to use from the get-go.

Keep in mind that with the `systemDefault` activity type, you can't:

- Utilize the built-in localization features provided by manifests.
- Rely on sending customizable notifications with the `systemDefault` activity type. Users can turn off all notifications from your app with a toggle in the Microsoft Teams client settings, which can hinder communication between your app and its users.

We still recommend templated notifications for recurring and large batches of notifications because they require activity templates in the manifest.

The `systemDefault` reserved activity type remains available, regardless of the activity types listed in your app's manifest.

## Customize activity feed notifications

Users can customize how they receive activity feed notifications from apps in Teams. Depending on their notification settings, notifications can appear in the activity feed or as banners.

![Screenshot of the Notifications settings in Teams, with the Custom option highlighted](images/teams-activityfeednotifications/notificationsettings.png)

To manage notifications for an app, users can go to their notification settings in Teams and select **Edit** next to the app, as shown in the following example. Notification settings become available after the app sends its first notification. The **description** field in the Teams app manifest is displayed in the notification settings.

![Screenshot showing notifications customized to Banner and feed for a Teams app](images/teams-activityfeednotifications/applevelnotificationsettings.png)

## FAQs

### Who needs to install the Teams app?

The target user must have the Teams app that is sending notifications installed.

### Can a user send notifications to themselves?

No, a user can't send notifications to themselves. For this scenario, use application permissions.

### Can a Teams app control how the notifications are shown to the user?

No, only users are allowed to change notification settings.

### I installed my app; why don't I see notification settings under the user account?

The settings appear after the Teams app sends the first notification. This reduces the number of settings that users see.

### I started getting a 409 (conflict) error; how do I resolve it?

`Conflict` errors primarily occur when multiple Teams apps installed in the same scope (team, chat, user, and so on) have the same Microsoft Entra appId in the `webApplicationInfo` section of the manifest. When this happens, you get an error like `Found multiple applications with the same Microsoft Entra App ID 'Your Microsoft Entra AppId'.`. Make sure that you use unique Microsoft Entra apps for unique Teams apps. You can install the same Teams app in multiple scopes (team + user, for example).