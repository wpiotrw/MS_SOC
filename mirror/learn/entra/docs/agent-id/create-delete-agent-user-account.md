---
layout: Conceptual
title: Create and delete an agent's user account - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/create-delete-agent-user-account
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Learn how to create and delete an agent's user account using the Microsoft Graph API.
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.reviewer: dastrock
locale: en-us
document_id: bee02d36-53ff-8a9b-5be0-5cf108bd86ca
document_version_independent_id: bee02d36-53ff-8a9b-5be0-5cf108bd86ca
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/create-delete-agent-user-account.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/create-delete-agent-user-account
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/create-delete-agent-user-account.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7f9e78ef-5930-b2a7-7c8e-2a4356ee13a2
---

# Create and delete an agent's user account - Microsoft Entra Agent ID | Microsoft Learn

An agent's user account is a specialized identity that lets an agent act as a digital worker—appearing to other systems as a user identity rather than a service principal. Agent user accounts aren't created automatically. You must explicitly create one and associate it with a specific agent identity.

For background on what an agent's user account is and when to use one, see [The agent's user account in Microsoft Entra Agent ID](agent-users).

Note

Creating an agent's user account through the Microsoft Graph API establishes the identity in Microsoft Entra but doesn't provision Microsoft 365 capabilities such as a mailbox or Teams presence. To provision a full digital worker with Microsoft 365 capabilities, create the agent through Microsoft Teams using the Agent 365 SDK.

## Prerequisites

- An [agent identity blueprint](create-blueprint) and at least one [agent identity](create-delete-agent-identities) created from it. Record the agent identity's object ID.
- The blueprint app registration must have the `AgentIdUser.ReadWrite.IdentityParentedBy` application permission granted with admin consent. See Grant the blueprint permission to create agent user accounts.
- An access token for the blueprint app registration with `https://graph.microsoft.com/.default` scope. The blueprint authenticates to Microsoft Graph to create and delete agent user accounts on behalf of the agent identity it parents.

The `identityParentId` value is the agent identity's object ID. The agent user's separate `id` is used to delete the user account. For identifier meanings, see [Record the identifiers for your scenario](key-concepts#record-the-identifiers-for-your-scenario).

## Grant the blueprint permission to create agent user accounts

The blueprint app registration doesn't have permission to create agent user accounts by default. Add the `AgentIdUser.ReadWrite.IdentityParentedBy` application permission and grant admin consent before calling the creation API.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **Entra ID** &gt; **App registrations** and open the blueprint app registration.
3. Select **API permissions** &gt; **Add a permission** &gt; **Microsoft Graph** &gt; **Application permissions**.
4. Search for and select `AgentIdUser.ReadWrite.IdentityParentedBy`.
5. Select **Add permissions**, then select **Grant admin consent**.

## Create an agent's user account

Create the agent's user account and associate it with an agent identity in a single call. The `identityParentId` property establishes the immutable 1:1 relationship between the user account and its parent agent identity.

```http
POST https://graph.microsoft.com/v1.0/users/microsoft.graph.agentUser
Content-Type: application/json
Authorization: Bearer <blueprint-access-token>

{
  "accountEnabled": true,
  "displayName": "Sales Agent",
  "mailNickname": "SalesAgent",
  "userPrincipalName": "salesagent@contoso.com",
  "identityParentId": "<agent-identity-object-id>"
}
```

| Property | Description |
| --- | --- |
| `accountEnabled` | Set to `true` to enable the account immediately. |
| `displayName` | Display name shown in the directory. |
| `mailNickname` | Alias used when provisioning a mailbox. Must be unique in the tenant. |
| `userPrincipalName` | Sign-in name in `user@domain` format. Must use a verified domain in the tenant. |
| `identityParentId` | Object ID of the agent identity that owns this user account. This value is immutable after creation. |

A successful request returns `201 Created` with the new agent user object:

```json
{
  "@odata.type": "#microsoft.graph.agentUser",
  "id": "87d349ed-44d7-43e1-9a83-5f2406dee5bd",
  "displayName": "Sales Agent",
  "mailNickname": "SalesAgent",
  "userPrincipalName": "salesagent@contoso.com",
  "identityParentId": "<agent-identity-object-id>"
}
```

Record the `id` value. You need it to configure the agent's user account flow in your agent and to delete the account later.

## Delete an agent's user account

When the agent is decommissioned, delete the user account to remove it from the directory.

```http
DELETE https://graph.microsoft.com/v1.0/users/microsoft.graph.agentUser/<agent-user-id>
Authorization: Bearer <blueprint-access-token>
```

A successful request returns `204 No Content`. The agent identity itself is not deleted by this call. To also remove the agent identity, see [Create and delete agent identities](create-delete-agent-identities).