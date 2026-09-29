---
layout: Conceptual
title: Known issues with Microsoft Graph APIs - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/known-issues
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: OmbongiFaith
ms.author: ombongifaith
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: concept-article
description: Learn about known issues with and limitations of Microsoft Graph APIs.
ms.localizationpriority: high
ms.date: 2026-04-10T00:00:00.0000000Z
locale: en-us
document_id: 4ab98f77-bf6f-4ce6-c189-dec2444a1bac
document_version_independent_id: ec5464a8-4def-9074-6e50-0b737b41b631
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/known-issues.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: known-issues
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/known-issues.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 8f5aac20-aac1-8237-0bef-a7c55230383a
---

# Known issues with Microsoft Graph APIs - Microsoft Graph | Microsoft Learn

This article provides information about known issues related to Microsoft Graph APIs.

## Authentication

### Publisher message of "unverified" occurs during PowerShell and CLI app consent

The consent page shows that the command-line app that caters to PowerShell and CLI is from an unverified publisher.

#### Workaround

To remove the "unverified" message, you can do an app registration of your own, on which you can set yourself as the verified publisher. You need to go through the publisher verification process, and use the app ID on the Microsoft Graph PowerShell SDK, as follows:

```powershell
Connect-MgGraph -AppId "{your-own-app-id}" -Scopes "scope"
```

### Pre-consent for CSP apps doesn't work in some customer tenants

Under certain circumstances, pre-consent for cloud solution provider (CSP) apps may not work for some of your customer tenants.

For apps using delegated permissions, when using the app for the first time with a new customer tenant, you might receive this error after sign-in: `AADSTS50000: There was an error issuing a token`.

For apps using application permissions, your app can acquire a token, but unexpectedly gets an access denied message when calling Microsoft Graph.

We're working to fix this issue, so that preconsent works for all CSP customer tenants.

#### Workaround

To unblock development and testing, you can use the following workaround.

Note

This isn't a permanent solution and is only intended to unblock development. This workaround won't be required once the issue is fixed. This workaround doesn't need to be undone after the fix is in place.

1. Open an Azure AD v2 PowerShell session and connect to your customer tenant by entering your admin credentials into the sign-in window. You can download and install Azure AD PowerShell V2 from [here](https://www.powershellgallery.com/packages/AzureAD).

    ```powershell
    Connect-AzureAd -TenantId {customerTenantIdOrDomainName}
    ```
2. Create the Microsoft Graph service principal.

    ```powershell
    New-AzureADServicePrincipal -AppId 00000003-0000-0000-c000-000000000000
    ```

### Azure AD v2.0 endpoint isn't supported for CSP apps

Cloud solution provider (CSP) apps must acquire tokens from the Azure AD (v1) endpoints to successfully call Microsoft Graph in their partner-managed customers. Currently, acquiring a token through the newer Azure AD v2.0 endpoint isn't supported.

## Calendar

### Error attaching large files to events

An app with delegated permissions returns `HTTP 403 Forbidden` when attempting to attach large files to an Outlook message or event that is in a shared or delegated mailbox. With delegated permissions, [createUploadSession](/en-us/graph/api/attachment-createuploadsession) succeeds only if the message or event is in the signed-in user's mailbox.

## Change notifications

### Upgrade events for Teams app installation change notifications in chat scope aren't delivered

When a subscription for a Teams app installation change notification is created, if the scope is specific to or includes chats, upgrade events/notifications aren't delivered to the subscriber.

For example: If a customer subscribes to `/appCatalogs/teamsApps/{teams-app-id}/installations?$filter=(scopeInfo/scope eq 'groupChat')`, they won't receive notifications for upgrade/update events. However, they receive other notifications regarding installations and deletions.

Another example: If a customer subscribes to `/appCatalogs/teamsApps/{teams-app-id}/installations`, they won't receive notifications for upgrade/update events occurring specifically within chats. However, they receive all other forms of notifications in teams and user's personal scope. But, in chats, they only receive installation and deletion notifications.

#### Workaround

Currently no workaround for this issue is available.

## Customer booking

### Error when querying bookingBusinesses

Getting the list of **bookingBusinesses** fails with the following error code when an organization has several Bookings businesses and the account making the request is not an administrator:

```json
{
  "error": {
    "code": "ErrorExceededFindCountLimit",
    "message": "The GetBookingMailboxes request returned too many results. Please specify a query to limit the results."
  }
}
```

#### Workaround

You can limit the set of businesses returned by the request by including a query parameter, for example:

```http
GET https://graph.microsoft.com/beta/bookingBusinesses?query=Fabrikam
```

## Delta query

### OData context is returned incorrectly

OData context is sometimes returned incorrectly when tracking changes to relationships.

## Device and app management

### Accessing and updating deployment audiences is not supported

Accessing and updating deployment audiences on deployment resources created via Intune is not currently supported.

- Listing deployment audience members and listing deployment audience exclusions returns `404 Not Found`.
- Updating deployment audience members and exclusions or updating by ID returns `202 Accepted` but the audience is not updated.

## Groups

### Nonadmin user can't add self as group owner during group creation or update

When a nonadmin user calls the [Create group](/en-us/graph/api/group-post-groups) API, [Update group](/en-us/graph/api/group-update) API, or [Upsert group](/en-us/graph/api/group-upsert) API and adds their user ID in the request body in the **owners@odata.bind** collection, the request fails with a `400 Bad Request` error code with the message "Request contains a property with duplicate values." A nonadmin user can't explicitly add themselves as the group owner.

#### Workaround

There's no workaround for this error.

By default, a nonadmin user who is creating a security or Microsoft 365 group through the [Create group](/en-us/graph/api/group-post-groups) API or [Upsert group](/en-us/graph/api/group-upsert) API is automatically added to the **owners** collection of the group, if they don't specify any group owners. If they specify others as group owners, the nonadmin group creator is still automatically added to the **owners** collection of the security group, but not for the Microsoft 365 group. The user still can't add themselves to the **owners** collection during group update.

### GET /groups/{id}/members doesn't return service principals in v1.0

The [List group members](/en-us/graph/api/group-list-members) API operation on the v1.0 endpoint currently doesn't return any service principals that might be members of the queried group.

#### Workaround

As a workaround, use one of the following options:

- Use the [List group members](/en-us/graph/api/group-list-members?view=graph-rest-beta&amp;preserve-view=true) API operation on the beta endpoint.
- Use the `/groups/{id}?$expand=members` API operation.

## Identity and access

### Use of specific query parameters on /subscribedSkus and /domains doesn't return the expected results

The following usage of query parameters that target **subscribedSkus** and **domain** entities might not return the expected results:

- Use of `$search` on both **subscribedSkus** or **domain** entities
- Use of `$top` and `$filter` on the **domain** entity

Currently, these parameters are effectively ignored, and the queries don't return the expected results.

#### Workaround

To prevent any disruption to your business processes, we recommend that you modify your application code to remove usage of these query parameters from queries that target the **subscribedSkus** or **domain** entities and run the search, top, and filter on the client side.

### Configuring federated domains in delegated scenarios requires Directory.AccessAsUser.All permission

The [Create internalDomainFederation](/en-us/graph/api/domain-post-federationconfiguration), [Update internalDomainFederation](/en-us/graph/api/internaldomainfederation-update), and [Delete internalDomainFederation](/en-us/graph/api/internaldomainfederation-delete) might require you to grant consent to the *Directory.AccessAsUser.All* permission. This requirement is a temporary workaround till we provide a more granular delegated permission for managing federated domains.

### Claims mapping policy might require consent to additional permissions

The [claimsMappingPolicy](/en-us/graph/api/resources/claimsmappingpolicy) API might require consent to both the *Policy.Read.All* and *Policy.ReadWrite.ConditionalAccess* permissions for the `LIST /policies/claimsMappingPolicies` and `GET /policies/claimsMappingPolicies/{id}` methods, as follows:

- If no **claimsMappingPolicy** objects are available to retrieve in a LIST operation, either permission is sufficient to call this method.
- If there are **claimsMappingPolicy** objects to retrieve, your app must consent to both permissions. If not, a `403 Forbidden` error is returned.

In the future, either permission will be sufficient to call both methods.

### Conditional access policy requires consent to additional permission

The [conditionalAccessPolicy](/en-us/graph/api/resources/conditionalaccesspolicy) API currently requires consent to the *Policy.Read.All* permission to call the POST and PATCH methods. In the future, the *Policy.ReadWrite.ConditionalAccess* permission will enable you to read policies from the directory.

### Provisioning of pre-registred passkeys not supported

The FIDO2 provisioning API supports adding passkeys that are active upon creation. Provisioning, where passkeys are pre-registered with Microsoft Entra ID during device manufacturing or distribution and kept disabled until an administrator enables them, aren't supported in the current v1.0 release.

### FIDO2 provisioning API requires self-service setup to be enabled

To use the FIDO2 provisioning API ([Create fido2AuthenticationMethod](/en-us/graph/api/authentication-post-fido2methods)), administrators must enable **Allow self-service setup** in the FIDO2 authentication method policy. In v1.0, this setting also enables end-user FIDO2 registration through My sign-ins. Enabling API-based provisioning independently of self-service registration is currently not supported.

**Microsoft Entra External ID:** External users don't have access to My sign-ins, so enabling this setting doesn't affect self-service registration for external users. Administrators must still enable the setting to use the provisioning API.

## JSON batching

### Request dependencies are limited

Individual requests can depend on other individual requests. Currently, requests can only depend on a single other request, and must follow one of these three patterns:

- **Parallel** - no individual request states a dependency in the **dependsOn** property.
- **Serial** - all individual requests depend on the previous individual request.
- **Same** - all individual requests that state a dependency in the **dependsOn** property, state the same dependency. Note: Requests made using this pattern will run sequentially.

As JSON batching matures, these limitations will be removed.

## Mail

### Delta calls to the messages API using immutable Ids

When you make `/delta` calls to the messages API using immutable Ids in some cases (for example when a message moves out of a folder and is then moved back in), you might miss some change notifications.

### The comment parameter for creating a draft isn't part of the message body

The **comment** parameter for creating a reply or forward draft ([createReply](/en-us/graph/api/message-createreply), [createReplyAll](/en-us/graph/api/message-createreplyall), [createForward](/en-us/graph/api/message-createforward)) isn't part of the body of the response message draft.

## Query parameters

### $search for directory objects fails for encoded ampersand (&) character

As per RFC 3986 and as described in [Encoding query parameters](/en-us/graph/query-parameters#encoding-query-parameters), reserved characters in query strings must be percent-encoded. For example, the syntax for `$search` on a group name like "Hiking&Recreation" is as follows:

```http
GET https://graph.microsoft.com/v1.0/groups?$search="displayName:Hiking%26Recreation group"
```

Microsoft Graph currently returns a `400 Bad Request` error code on the v1.0 endpoint on searches that include encoded ampersand (&) characters, with the following error message: `Unrecognized query argument specified: ''.`. The same request succeeds on the beta endpoint.

Some apps have implemented double-percent encoding on the v1.0 endpoint as a workaround. For example, the double-percent encoded request becomes `/users?$search="displayName:Hiking%2526Recreation group"`. However, this isn't the officially recommended workaround.

#### Workaround

**Workaround 1:**

On the v1.0 endpoint, when using the proper percent-encoding, include the `Prefer` request header set to `legacySearch=false`. For example:

```http
GET https://graph.microsoft.com/v1.0/groups?$search="displayName:Hiking%26Recreation group"
ConsistencyLevel: eventual
Prefer: legacySearch=false
```

In the future, the behavior on the v1.0 endpoint will be corrected, and you won't need to include this header.

**Workaround 2:**

When the behavior on the v1.0 endpoint is corrected, apps with dependency on the double-percent encoding may experience breaking changes unless they're opted-in to maintain their implementation by including the `Prefer` request header set to `legacySearch=true`. For example:

```http
GET https://graph.microsoft.com/v1.0/groups?$search="displayName:Hiking%2526Recreation group"
ConsistencyLevel: eventual
Prefer: legacySearch=true
```

### Some limitations apply to query parameters

The following limitations apply to query parameters:

- Multiple namespaces aren't supported.
- GET requests on `$ref` and casting aren't supported on users, groups, devices, service principals, and applications.
- `@odata.bind` isn't supported. This means that you can't properly set the **acceptedSenders** or **rejectedSenders** navigation property on a group.
- `@odata.id` isn't present on noncontainment navigations (like messages) when using minimal metadata.
- `$expand`on relationships of directory objects:
    - Returns a maximum of 20 objects except for `/users?$expand=registeredDevices`, which returns up to 100 objects.
    - No support for `@odata.nextLink`.
    - No support for more than one level of expand.
    - No support for nesting other query parameters such as `$filter` and `$select` inside an `$expand` query.
- `$filter`:
    - `/attachments` endpoint doesn't support filters. If present, the `$filter` parameter is ignored.
    - Cross-workload filtering isn't supported.
    - When using the `in` operator, the request is limited to 15 expressions in the filter clause by default OR a URL length of 2,048 characters when using advanced query capabilities.
    - When filtering using the `eq` operator, the maximum limit of the value to match is 120 characters. That is, `$filter=displayName eq 'value-to-match-max-120-char'`. This limitation applies even for properties like **displayName** on directory objects that can be up to 256 characters. When using advanced queries, the limit is applied on the URL length at 2,048 characters instead of the matched value.
- `$search`:
    - Full-text search is only available for a subset of entities, such as messages.
    - Cross-workload searching isn't supported.
    - Searching isn't supported in Azure AD B2C tenants.
- `$count`:
    - Not supported in Azure AD B2C tenants.
    - When using the `$count=true` query string when querying against directory resources, the `@odata.count` property is present only on the first page of the paged data.
- Query parameters specified in a request might fail silently. This can be true for unsupported query parameters and for unsupported combinations of query parameters.

## Search

### Creating an externalConnection with a broken adaptive card returns a 503 Service Unavailable response followed by a 409 Conflict error

When you use Microsoft Graph APIs to create an external connection with a broken adaptive card for the result layout, the first call fails with a `503 Service Unavailable` error. Then the second call fails with `409 Conflict` error that indicates that a connection with the same name already exists.

Although the first request failed with a 503 response, the connection was still created. However, the adaptive card template was not registered because it is broken.

## Sites and lists

### Follow/unfollow sites aren't in sync with SharePoint following

When querying followed sites through Microsoft Graph, the response might have incorrect results and those results might not match the results from following content in SharePoint.

#### Workaround

Use the [following people and content](/en-us/sharepoint/dev/general-development/following-people-and-content-rest-api-reference-for-sharepoint) REST API.

## Teamwork and communications

### Listing callRecords participant\_v2 might not return all participants

In some edge cases, a request to list **participants\_v2** for a **callRecord** might return an incomplete list.

#### Workaround

You can utilize the existing **participants** property of a **callRecord** for a complete list of participants.

### Communications Calling SDK: Inconsistent recorded participant number shown on teams client when bot grouping is enabled

When recording bot applications enable Bot Grouping, the number of participants shown by the Teams client as being recorded isn't accurate. Because the participants are grouped, the displayed number of participants being recorded is lower than the actual number.

#### Workaround

Disable bot grouping to show an accurate count.

### callRecords API represents application participants as users in communicationsIdentitySet

In the **callRecord** participant resource, application/bot participants are currently represented by the [communicationsUserIdentity](/en-us/graph/api/resources/communicationsuseridentity) instead of [communicationsApplicationIdentity](/en-us/graph/api/resources/communicationsapplicationidentity).

#### Workaround

Use the user agent **headerValue** on the [participantEndpoint](/en-us/graph/api/resources/callrecords-participantendpoint) resource in a **callRecord** session to identify application participants and see additional details on the application identity.

### Communication Calling SDK: Support for multi-endpoint use case in delta roster notification mode is missing

When the same application or user is joining the same meeting using multiple endpoints, and the roster notification mode is delta roster, the participant roster updates provided by Communications SDK might not capture the additional endpoints added to the ongoing call.

#### Workaround

Legacy mode for roster supports the multi-endpoint use case. Use the SDK version 1.2.0.7270 or earlier.

### Communication Calling SDK: Webhook message processing exception: System.Security.Cryptography.CryptographicException

The release of the KBs introduced an issue with applications developed with the Communication Calling SDKs.

The Microsoft Graph `AnswerAsync` method throws an exception when the bot tries to answer incoming calls. This is related to the following Windows updates:

- Wk22 - KB5038282
- Wk19 - KB5038283

For details, see [SHA256 ComputeHash started throwing - Microsoft Community](https://techcommunity.microsoft.com/t5/windows-server-for-it-pro/sha256-computehash-started-throwing/m-p/4159498).

#### Workaround

Roll back the KBs pending an updated release of the SDK.

### Change tracking requests for APIs that export online meeting artifacts return items that are already synced

Change tracking (`/delta`) requests to [getAllTranscripts](/en-us/graph/api/callrecording-delta) or [getAllRecordings](/en-us/graph/api/calltranscript-delta) might return items that were already synced in earlier requests.

This happens when the meeting had other non-related updates, such as adding participants, notes, or files.

#### Workaround

For every item in the response, check the **createdDateTime** of the recording or transcript and compare it with the previous sync timestamp. If the **createdDateTime** is before the last sync timestamp, the item is already synced and can be ignored.

### APIs that export online meeting artifacts don't return recordings for meetings without transcriptions enabled

The [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings) API does not return recordings for meetings that don't have transcription enabled.

### APIs that export online meeting artifacts might not return nextLink when the request uses the $top query parameter

When you call the [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings) or [getAllTranscripts](/en-us/graph/api/onlinemeeting-getalltranscripts) APIs, passing the `$top` filter might not return the `@odata.nextLink`, even when there are more items to export.

#### Workaround

Do not pass `$top` query parameter until the issue is fixed.

### APIs that export online meeting artifacts may return duplicate items during service update

During a planned service update that is expected to be completed by August 31, 2026, paginated requests to the [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings) or [getAllTranscripts](/en-us/graph/api/onlinemeeting-getalltranscripts) APIs may experience an automatic pagination token reset. A request can return a `200 OK` response with an empty collection and an `@odata.nextLink`. Pagination then restarts and can return recording or transcript items that were returned previously.

#### Workaround

Continue following `@odata.nextLink` even when the collection is empty. De-duplicate subsequent items by tracking the **id** property of each recording or transcript.

When using delta queries with these methods, follow the returned delta link without appending or reapplying filters. The token retains the filter from the initial request. Supplying a filter with the token returns a `400 Bad Request` response with `DeltaFilterNotAllowed` as the `innerError.code` value.

### List team members API fails with 401 errors in newly created tenants

When a newly created tenant sends a [list members of team](/en-us/graph/api/team-list-members) request using advanced Azure AD query capabilities, an HTTP 401 error occurs.

#### Workaround

1. Call the [list teams](/en-us/graph/api/teams-list) API and wait for a few seconds.
2. Call `/teams/{id}/members` and check for a successful response.

### Clone team method does not include all owners of the source team in the cloned team

When you call the [clone team](/en-us/graph/api/team-clone) method, if the source team contains more than one owner, only one owner is preserved in the cloned team. The other owners become members of the new cloned team. It is not possible to choose or configure which owner is retained as the owner of the new team.

#### Workaround

Use the [Add members](/en-us/graph/api/team-post-members) method after you clone the team to update the original owners from members back to owners.

### Create channel can return an error response

When you create a channel, if you use special characters in your channel name, the [Get filesFolder](/en-us/graph/api/channel-get-filesfolder) API will return a `400 Bad Request` error response. When you create a channel, make sure that the **displayName** for the channel does not:

- Include any of the following special characters: `~ # % & * { } + / \ : < > ? | ' "`.
- Start with an underscore (`_`) or period (`.`), or end with a period (`.`).

### Unable to access a cross-tenant shared channel when the request URL contains tenants/{cross-tenant-id}

The API calls for `teams/{team-id}/incomingChannels` and `teams/{team-id}/allChannels` return the `@odata.id` property which you can use to access the channel and run other operations on the channel object. If you call the URL returned from the `@odata.id` property, the request fails with the following error when it tries to access the cross-tenant shared channel:

```http
GET /tenants/{tenant-id}/teams/{team-id}/channels/{channel-id}
```

```json
{
    "error": {
        "code": "BadRequest",
        "message": "TenantId in the optional tenants/{tenantId} segment should match the tenantId(tid) in the token used to call Graph.",
        "innerError": {
            "date": "2022-03-08T07:33:50",
            "request-id": "dff19596-b5b2-421d-97d3-8d4b023263f3",
            "client-request-id": "32ee2cbd-27f8-2441-e3be-477dbe0cedfa"
        }
    }
}
```

#### Workaround

Remove the `/tenants/{tenant-id}` part from the URL before you call the API to access the cross-tenant shared channel.

### Requests to filter team members by role require a parameter

All the requests to filter team members by roles expect either a **skipToken** parameter or a **top** parameter in the request, but not both. If both the parameters are passed in the request, the **top** parameter will be ignored.

### Unable to filter team members by roles

Role query filters along with other filters `GET /teams/team-id/members?$filter=roles/any(r:r eq 'owner') and displayName eq 'dummy'` might not work. The server might respond with a `BAD REQUEST`.

### View meeting details menu is not available on Microsoft Teams client

The Microsoft Teams client does not show the **View Meeting details** menu for channel meetings created via the cloud communications API.

### Sensitivity label does not show up in the Teams UI

Sensitivity Labels that are applied to Teams at times do not show up in the Teams UI, even though it can clearly be seen in both the underlying SharePoint site and in the Admin Center.

### Some properties for chat members might be missing in the response to a GET request

In certain instances, the **tenantId**/**email**/**displayName** property for the individual members of a chat might not be populated on a `GET /chats/chat-id/members` or `GET /chats/chat-id/members/membership-id` request.

### Get chats limit updated for expand members

This API works differently in one or more national clouds. For details, see [Implementation differences in national clouds](/en-us/graph/teamwork-national-cloud-differences). When `$expand=members` is included, this API returns a maximum of 25 items, even if a larger `$top` value is specified.

### layoutType property returns `null` when listing all channels

The **layoutType** property returns `null` when listing all channels. To get the layout type of a specific channel, use the [Get channel](/en-us/graph/api/channel-get) API.

## Users

### APIs that export online meeting artifacts might return transcript URLs that don't contain any content

The [getAllTranscripts](/en-us/graph/api/onlinemeeting-getalltranscripts) API might return transcript content URLs for some meetings that don't have any transcribed words. Calls to the content URL for those meetings will return an error.

#### Workaround

Verify that the meeting has been transcribed and if there's valid content. If there is, report it for further investigation. Otherwise, ignore the content URL.

### showInAddressList property is out of sync with Microsoft Exchange

When querying users through Microsoft Graph, the **showInAddressList** property may not indicate the same status shown in Microsoft Exchange. We recommend you manage this functionality directly with Microsoft Exchange through the Microsoft 365 admin center and not to use this property in Microsoft Graph.

### Access to a user's profile photo is limited

Reading and updating a user's profile photo is only possible if the user has a mailbox. Failure to read or update a photo, in this case, results in the following error:

```json
{
  "error": {
    "code": "ErrorNonExistentMailbox",
    "message": "The SMTP address has no mailbox associated with it."
  }
}
```

Any photos that may have been previously stored using the **thumbnailPhoto** property (using the Azure AD Graph API (currently in its retirement cycle) or through AD Connect synchronization) are no longer accessible through the Microsoft Graph **photo** property of the [user](/en-us/graph/api/resources/user) resource.

Managing users' photos through the [profilePhoto](/en-us/graph/api/resources/profilephoto) resource of the Microsoft Graph API is currently not supported in Azure AD B2C tenants.