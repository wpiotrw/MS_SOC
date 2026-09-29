---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: Update communicationConfiguration - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/agentidentity-update-communicationconfiguration?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: sthapliyal
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: teams
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Replace the communication configuration of an agent identity.
ms.date: 2026-07-28T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: e68b9a30-9e97-ac93-b619-d8d785e82923
document_version_independent_id: 208496cd-676a-df27-662f-7bffc308f703
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/agentidentity-update-communicationconfiguration.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/agentidentity-update-communicationconfiguration
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/agentidentity-update-communicationconfiguration.md
platformId: 14902199-2aa2-38c7-5e06-21118c616545
---

# Update communicationConfiguration - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Replace the [agentCommunicationConfiguration](resources/agentcommunicationconfiguration) of an [agentIdentity](resources/agentidentity). This operation is a full replace: the request replaces the entire configuration object with the supplied body. An agent identity can override the configuration only when the source blueprint sets **isOverridableAtAgentIdLevel** to `true`.

Note

When you set the **endpointConfiguration**, we recommend that you use the `apiBased`[agentEndpointConfigurationType](resources/enums#agentendpointconfigurationtype-values) rather than `botBased`.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permission | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | AgentCommunicationConfiguration.ReadWrite | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | AgentCommunicationConfiguration.ReadWrite.All | Not available. |

## HTTP request

```http
PUT /servicePrincipals/microsoft.graph.agentIdentity/{agentIdentityId}/communicationConfiguration
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, supply a full JSON representation of the [agentCommunicationConfiguration](resources/agentcommunicationconfiguration) object. Because this operation is a full replace, include all properties you want to persist; properties that are omitted are cleared.

| Property | Type | Description |
| --- | --- | --- |
| isOverridableAtAgentIdLevel | Boolean | Indicates whether individual agent instances created from this blueprint can override the **endpointConfiguration**. Optional. |
| endpointConfiguration | [agentEndpointConfiguration](resources/agentendpointconfiguration) | The endpoint binding (bot ID or callback URI) that the agent uses to receive messages. Optional. |
| teamworkConfiguration | [agentTeamworkConfiguration](resources/agentteamworkconfiguration) | The per-conversation-context message notification settings that agents use. Optional. |

## Response

If successful, this method returns a `200 OK` response code and an updated [agentCommunicationConfiguration](resources/agentcommunicationconfiguration) object in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)
```http
PUT https://graph.microsoft.com/beta/servicePrincipals/microsoft.graph.agentIdentity/1f554dbf-8c7a-42dc-8f92-1a3b4c5d6e7f/communicationConfiguration
Content-Type: application/json

{
  "isOverridableAtAgentIdLevel": false,
  "endpointConfiguration": {
    "configurationType": "apiBased",
    "apiBased": {
      "callbackUri": "https://agent.contoso.com/api/messages"
    }
  },
  "teamworkConfiguration": {
    "groupChatConfiguration": {
      "messageNotificationMode": "atMentionedMessagesOnly"
    },
    "channelConfiguration": {
      "messageNotificationMode": "allMessages"
    },
    "oneOnOneChatConfiguration": {
      "messageNotificationMode": "allMessages"
    },
    "meetingChatConfiguration": {
      "messageNotificationMode": "atMentionedMessagesOnly"
    }
  }
}
```

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const agentCommunicationConfiguration = {
  isOverridableAtAgentIdLevel: false,
  endpointConfiguration: {
    configurationType: 'apiBased',
    apiBased: {
      callbackUri: 'https://agent.contoso.com/api/messages'
    }
  },
  teamworkConfiguration: {
    groupChatConfiguration: {
      messageNotificationMode: 'atMentionedMessagesOnly'
    },
    channelConfiguration: {
      messageNotificationMode: 'allMessages'
    },
    oneOnOneChatConfiguration: {
      messageNotificationMode: 'allMessages'
    },
    meetingChatConfiguration: {
      messageNotificationMode: 'atMentionedMessagesOnly'
    }
  }
};

await client.api('/servicePrincipals/microsoft.graph.agentIdentity/1f554dbf-8c7a-42dc-8f92-1a3b4c5d6e7f/communicationConfiguration').version('beta').put(agentCommunicationConfiguration);

```

Important

Microsoft Graph SDKs use the v1.0 version of the API by default, and do not support all the types, properties, and APIs available in the beta version. For details about accessing the beta API with the SDK, see [Use the Microsoft Graph SDKs with the beta API](/en-us/graph/sdks/use-beta).

For details about how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance, see the [SDK documentation](/en-us/graph/sdks/sdks-overview).

---

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#servicePrincipals/microsoft.graph.agentIdentity/communicationConfiguration/$entity",
  "isOverridableAtAgentIdLevel": false,
  "endpointConfiguration": {
    "configurationType": "apiBased",
    "apiBased": {
      "callbackUri": "https://agent.contoso.com/api/messages"
    },
    "botBased": null
  },
  "teamworkConfiguration": {
    "groupChatConfiguration": {
      "messageNotificationMode": "atMentionedMessagesOnly"
    },
    "channelConfiguration": {
      "messageNotificationMode": "allMessages"
    },
    "oneOnOneChatConfiguration": {
      "messageNotificationMode": "allMessages"
    },
    "meetingChatConfiguration": {
      "messageNotificationMode": "atMentionedMessagesOnly"
    }
  }
}
```