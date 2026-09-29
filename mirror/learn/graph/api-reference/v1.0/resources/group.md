---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: group resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: yuhko-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-groups
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: 'Represents a Microsoft Entra group, which can be a Microsoft 365 group, or a security group. '
ms.localizationpriority: high
ms.reviewer: mbhargav, khotzteam, aadgroupssg
doc_type: resourcePageType
ms.date: 2026-05-26T00:00:00.0000000Z
locale: en-us
document_id: ae6b4ebd-685c-0854-6793-2f900cadc554
document_version_independent_id: 953200ad-c9af-a80d-7bc2-836a25ddc273
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/group.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/group
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/group.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: c60f15de-72ee-f6a1-5490-b6f97d6428f8
---

# group resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a Microsoft Entra group, a Microsoft 365 group, or a security group. This resource is an open type that allows additional properties beyond those documented here.

Inherits from [directoryObject](directoryobject).

For performance reasons, the [create](../group-post-groups), [get](../group-get), and [list](../group-list) operations return only a subset of more commonly used properties by default. These *default* properties are noted in the Properties section. To get any of the properties not returned by default, specify them in a `$select` OData query option.

This resource supports:

- Adding your data to custom properties as [extensions](/en-us/graph/extensibility-overview).
- Subscribing to [change notifications](/en-us/graph/change-notifications-overview).
- Using [delta query](/en-us/graph/delta-query-overview) to track incremental additions, deletions, and updates, by providing a [delta](../group-delta) function.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../group-list) | [group](group) collection | List group objects and their properties. |
| [Create](../group-post-groups) | [group](group) | Create a new group. It can be a Microsoft 365 group, dynamic group, or security group. |
| [Get](../group-get) | [group](group) | Read properties of a group object. |
| [Update](../group-update) | None | Update the properties of a group object. |
| [Upsert](../group-upsert) | [group](group) | Create a new group if it doesn't exist, or update the properties of an existing group. |
| [Delete](../group-delete) | None | Delete group object. |
| [Get delta](../group-delta) | group collection | Get incremental changes for groups. |
| **Group management** |  |  |
| [List members](../group-list-members) | [directoryObject](directoryobject) collection | Get the direct members of this group from the **members** navigation property. |
| [Add members](../group-post-members) | None | Add a member to this group by posting to the **members** navigation property (supported for security groups and Microsoft 365 groups only). |
| [Remove member](../group-delete-members) | None | Remove a member from a Microsoft 365 group or a security group through the **members** navigation property. |
| [List owners](../group-list-owners) | [directoryObject](directoryobject) collection | Get the owners of the group from the **owners** navigation property. |
| [Add owners](../group-post-owners) | None | Add a new owner for the group by posting to the **owners** navigation property (supported for security groups and Microsoft 365 groups only). |
| [Remove owner](../group-delete-owners) | None | Remove an owner from a Microsoft 365 group or a security group through the **owners** navigation property. |
| [List memberships](../group-list-memberof) | [directoryObject](directoryobject) collection | Get the groups, admin roles, and and administrative units that this group is a direct member of from the memberOf navigation property. |
| [List transitive members](../group-list-transitivemembers) | [directoryObject](directoryobject) collection | Get the users, groups, and devices that are members, including nested members of this group. |
| [List transitive memberships](../group-list-transitivememberof) | [directoryObject](directoryobject) collection | List the groups that this group is a member of. This operation is transitive and includes the groups that this group is a nested member of. |
| [List group lifecycle policies](../group-list-grouplifecyclepolicies) | [groupLifecyclePolicy](grouplifecyclepolicy) collection | List group lifecycle policies. |
| [Assign license](../group-assignlicense) | [group](group) | Add or remove subscriptions for the group. You can also enable and disable specific plans associated with a subscription. |
| [Renew](../group-renew) | Boolean | Renews a group's expiration. Renewing extends the group expiration by the number of days defined in the policy. |
| [Validate properties](../group-validateproperties) | JSON | Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. |
| **App role assignments** |  |  |
| [List](../group-list-approleassignments) | [appRoleAssignment](approleassignment) collection | Get the apps and app roles assigned to this group. |
| [Add](../group-post-approleassignments) | [appRoleAssignment](approleassignment) | Assign an app role to this group. |
| [Remove](../group-delete-approleassignments) | None. | Remove an app role assignment from this group. |
| **Calendar** |  |  |
| [Get calendar](../calendar-get) | [calendar](calendar) | Get the group's calendar. |
| [Update calendar](../calendar-update) | None | Update the group's calendar. |
| [List events](../group-list-events) | [event](event) collection | Get an event object collection. |
| [Create event](../group-post-events) | [event](event) | Create a new event by posting to the events collection. |
| [Get event](../group-get-event) | [event](event) | Read properties of an event object. |
| [Update event](../group-update-event) | None | Update the properties of an event object. |
| [Delete event](../group-delete-event) | None | Delete event object. |
| [List calendar view](../group-list-calendarview) | [event](event) collection | Get a collection of events in a specified time window. |
| **Conversations** |  |  |
| [List conversations](../group-list-conversations) | [conversation](conversation) collection | Get a conversation object collection. |
| [Create conversation](../group-post-conversations) | [conversation](conversation) | Create a new conversation by posting to the conversations collection. |
| [Get conversation](../group-get-conversation) | [conversation](conversation) | Read properties of a conversation object. |
| [Delete conversation](../group-delete-conversation) | None | Delete conversation object. |
| [List threads](../group-list-threads) | [conversationThread](conversationthread) collection | Get all the threads of a group. |
| [Create thread](../group-post-threads) | [conversationThread](conversationthread) | Create a new conversation thread. |
| [Get thread](../group-get-thread) | [conversationThread](conversationthread) | Read properties of a thread object. |
| [Update thread](../group-update-thread) | None | Update properties of a thread object. |
| [Delete thread](../group-delete-thread) | None | Delete thread object. |
| [List accepted senders](../group-list-acceptedsenders) | [directoryObject](directoryobject) collection | Get a list of users or groups that are in the accepted-senders list for this group. |
| [Add accepted sender](../group-post-acceptedsenders) | [directoryObject](directoryobject) | Add a User or Group to the acceptSenders collection. |
| [Remove accepted sender](../group-delete-acceptedsenders) | [directoryObject](directoryobject) | Remove a User or Group from the acceptedSenders collection. |
| [List rejected senders](../group-list-rejectedsenders) | [directoryObject](directoryobject) collection | Get a list of users or groups that are in the rejected-senders list for this group. |
| [Add rejected sender](../group-post-rejectedsenders) | [directoryObject](directoryobject) | Add a new User or Group to the rejectedSenders collection. |
| [Remove rejected sender](../group-delete-rejectedsenders) | [directoryObject](directoryobject) | Remove new User or Group from the rejectedSenders collection. |
| **Directory objects** |  |  |
| [List deleted items](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve the groups deleted in the tenant in the last 30 days. |
| [Get deleted item](../directory-deleteditems-get) | [directoryObject](directoryobject) collection | Retrieve a deleted group by ID. |
| [Restore deleted item](../directory-deleteditems-restore) | [directoryObject](directoryobject) collection | Restore a group deleted in the tenant in the last 30 days. |
| [Permanently delete item](../directory-deleteditems-delete) | [directoryObject](directoryobject) collection | Permanently delete a deleted group from the tenant. |
| [List deleted items owned by user](../directory-deleteditems-getuserownedobjects) | [directoryObject](directoryobject) collection | Retrieve the user's groups deleted in the tenant in the last 30 days. |
| [Check member groups](../directoryobject-checkmembergroups) | String collection | Check for membership in a list of groups. The function is transitive. |
| [Get member groups](../directoryobject-getmembergroups) | String collection | Return all the groups that the group is a member of. The function is transitive. |
| [Check member objects](../directoryobject-checkmemberobjects) | String collection | Check for membership in a list of group, directory role, or administrative unit objects. The function is transitive. |
| [Get member objects](../directoryobject-getmemberobjects) | String collection | Return all of the groups and administrative units that the group is a member of. The function is transitive. |
| **Drive** |  |  |
| [Get drive](../drive-get) | [drive](drive) | Retrieve the properties and relationships of a Drive resource. |
| [List children](../driveitem-list-children) | [DriveItems](driveitem) | Return a collection of DriveItems in the children relationship of a DriveItem. |
| **Group settings** |  |  |
| [List](../group-list-settings) | [groupSetting](groupsetting) collection | List properties of all setting objects. |
| [Create](../group-post-settings) | [groupSetting](groupsetting) | Create a setting object based on a groupSettingTemplate. The POST request must provide settingValues for all the settings defined in the template. Only groups specific templates can be used for this operation. |
| [Get](../groupsetting-get) | [groupSetting](groupsetting) | Read properties of a specific setting object. |
| [Update](../groupsetting-update) | None | Update a setting object. |
| [Delete](../groupsetting-delete) | None | Delete a setting object. |
| [List setting template](../groupsettingtemplate-list) | None | List properties of all setting templates. |
| [Get setting template](../groupsettingtemplate-get) | None | Read properties of a setting template. |
| **Notes** |  |  |
| [List notebooks](../onenote-list-notebooks) | [notebook](notebook) collection | Retrieve a list of notebook objects. |
| [Create notebook](../onenote-post-notebooks) | [notebook](notebook) | Create a new OneNote notebook. |
| **Profile photo** |  |  |
| [Get](../profilephoto-get) | [profilePhoto](profilephoto) | Get the specified profilePhoto or its metadata (profilePhoto properties). |
| [Update](../profilephoto-update) | None | Update the photo for any user in the tenant including the signed-in user, or the specified group or contact. |
| [Delete](../profilephoto-delete) | None | Delete the photo for any user in the tenant including the signed-in user or the specified group. |
| **Planner** |  |  |
| [List plans](../plannergroup-list-plans) | [plannerPlan](plannerplan) collection | Get plans assigned to the group. |
| **Posts** |  |  |
| [List](../conversationthread-list-posts) | [post](post) collection | Get posts in a conversation thread. |
| [Get](../post-get) | [post](post) | Get a specific post. |
| [Reply to post](../post-reply) | None | Reply to a post. |
| [Forward post](../post-forward) | None | Forward a post. |
| **Other group resources** |  |  |
| [List permission grants](../group-list-permissiongrants) | [resourceSpecificPermissionGrant](resourcespecificpermissiongrant) collection | List permissions that are granted to apps to access the group. |
| **User settings** |  |  |
| [Add favorite](../group-addfavorite) | None | Add the group to the list of the signed-in user's favorite groups. Supported for only Microsoft 365 groups. |
| [Remove favorite](../group-removefavorite) | None | Remove the group from the list of the signed-in user's favorite groups. Supported for only Microsoft 365 groups. |
| [List member of](../group-list-memberof) | [directoryObject](directoryobject) collection | Get the groups and administrative units that this user is a direct member of, from the **memberOf** navigation property. |
| [List joined teams](../user-list-joinedteams) | [group](group) collection | Get the Microsoft Teams that the user is a direct member of. |
| [List associated teams](../associatedteaminfo-list) | [associatedTeamInfo](associatedteaminfo) collection | Get the list of [associatedTeamInfo](associatedteaminfo) objects in Microsoft Teams that a [user](user) is associated with. |
| [Subscribe by mail](../group-subscribebymail) | None | Set the isSubscribedByMail property to `true`. Enabling the signed-in user to receive email conversations. Supported for only Microsoft 365 groups. |
| [Unsubscribe by mail](../group-unsubscribebymail) | None | Set the isSubscribedByMail property to `false`. Disabling the signed-in user from receive email conversations. Supported for only Microsoft 365 groups. |
| [Reset unseen count](../group-resetunseencount) | None | Reset the unseenCount to 0 of all the posts that the signed-in user hasn't seen since their last visit. Supported for only Microsoft 365 groups. |

## Properties

Important

Specific usage of `$filter` and the `$search` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#group-properties).

| Property | Type | Description |
| --- | --- | --- |
| accessType | [groupAccessType](groupaccesstype) | Indicates the type of access to the group. The possible values are: `none`, `private`, `secret`, `public`, `unknownFutureValue`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| allowExternalSenders | Boolean | Indicates if people external to the organization can send messages to the group. The default value is `false`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| assignedLabels | [assignedLabel](assignedlabel) collection | The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group or a cloud security group. Requires a Microsoft Entra ID P1 license. Requires `$select` to retrieve. This property can be specified during group creation or update. However, for cloud security groups, it's immutable once set. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and [a supported administrator role](/en-us/purview/get-started-with-sensitivity-labels#permissions-required-to-create-and-manage-sensitivity-labels). See [Key differences from Microsoft 365 group labeling](/en-us/entra/identity/users/groups-sensitivity-labels#key-differences-from-microsoft-365-group-labeling) to learn more about managing this property for Microsoft 365 vs. cloud security groups. |
| assignedLicenses | [assignedLicense](assignedlicense) collection | The licenses that are assigned to the group. Requires `$select` to retrieve. Supports `$filter` (`eq`). Read-only. |
| autoSubscribeNewMembers | Boolean | Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is `false`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| classification | String | Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList [setting](groupsetting) value, based on the [template definition](groupsettingtemplate).Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`). |
| createdDateTime | DateTimeOffset | Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is `2014-01-01T00:00:00Z`. Returned by default. Read-only. |
| deletedDateTime | DateTimeOffset | For some Microsoft Entra objects (user, group, application), if the object is deleted, it's first logically deleted, and this property is updated with the date and time when the object was deleted. Otherwise this property is `null`. If the object is restored, this property is updated to `null`. Inherited from [directoryObject](directoryobject). |
| description | String | An optional description for the group. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`) and `$search`. |
| displayName | String | The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values), `$search`, and `$orderby`. |
| expirationDateTime | DateTimeOffset | Timestamp of when the group is set to expire. It's `null` for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the [groupLifecyclePolicy](grouplifecyclepolicy). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is `2014-01-01T00:00:00Z`. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`). Read-only. |
| groupTypes | String collection | Specifies the group type and its membership. If the collection contains `Unified`, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see [groups overview](groups-overview).If the collection includes `DynamicMembership`, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports `$filter` (`eq`, `not`). |
| hasMembersWithLicenseErrors | Boolean | Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an [example](../group-list). Supports `$filter` (`eq`). |
| hideFromAddressLists | Boolean | True if the group isn't displayed in certain parts of the Outlook UI: the **Address Book**, address lists for selecting message recipients, and the **Browse Groups** dialog for searching groups; otherwise, false. The default value is `false`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| hideFromOutlookClients | Boolean | True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is `false`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| id | String | The unique identifier for the group. Returned by default. Inherited from [directoryObject](directoryobject). Key. Not nullable. Read-only.Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| isArchived | Boolean | When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the `/group/{groupId}/team` endpoint or the [Get team](../team-get) API. To update this property, use the [archiveTeam](../team-archive) and [unarchiveTeam](../team-unarchive) APIs. |
| isAssignableToRole | Boolean | Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to `true`, the **securityEnabled** property must also be set to `true`, **visibility** must be `Hidden`, and the group can't be a dynamic group (that is, **groupTypes** can't contain `DynamicMembership`). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the *RoleManagement.ReadWrite.Directory* permission to set this property or update the membership of such groups. For more, see [Using a group to manage Microsoft Entra role assignments](https://go.microsoft.com/fwlink/?linkid=2103037)Using this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports `$filter` (`eq`, `ne`, `not`). |
| isFavorite | Boolean | Indicates whether the user marked the group as favorite. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| isManagementRestricted | Boolean | Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is `null` and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires `$select` to retrieve. |
| isSubscribedByMail | Boolean | Indicates whether the signed-in user is subscribed to receive email conversations. The default value is `true`. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| licenseProcessingState | String | Indicates the status of the group license assignment to all group members. The default value is `false`. Read-only. Possible values: `QueuedForProcessing`, `ProcessingInProgress`, and `ProcessingComplete`.Requires `$select` to retrieve. Read-only. |
| mail | String | The SMTP address for the group, for example, "serviceadmins@contoso.com". Returned by default. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values). |
| mailEnabled | Boolean | Specifies whether the group is mail-enabled. Required. Returned by default. Supports `$filter` (`eq`, `ne`, `not`). |
| mailNickname | String | The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the [ASCII character set 0 - 127](/en-us/office/vba/language/reference/user-interface-help/character-set-0127) except the following characters: ` @ () \ [] " ; : <> , SPACE`. Required. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values). |
| membershipRule | String | The rule that determines members for this group if the group is a dynamic group (groupTypes contains `DynamicMembership`). For more information about the syntax of the membership rule, see [Membership Rules syntax](/en-us/azure/active-directory/users-groups-roles/groups-dynamic-membership). Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`). |
| membershipRuleProcessingState | String | Indicates whether the dynamic membership processing is on or paused. Possible values are `On` or `Paused`. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| onPremisesDomainName | String | Contains the on-premises **domain FQDN**, also called **dnsDomainName** synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only. |
| onPremisesExtensionAttributes | [onPremisesExtensionAttributes](onpremisesextensionattributes) | Complex type containing extension attributes 1-15 for the group, synchronized from on-premises Active Directory. Returned only on `$select`. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| onPremisesLastSyncDateTime | DateTimeOffset | Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is `2014-01-01T00:00:00Z`. Returned by default. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`). |
| onPremisesNetBiosName | String | Contains the on-premises **netBios name** synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only. |
| onPremisesProvisioningErrors | [onPremisesProvisioningError](onpremisesprovisioningerror) collection | Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports `$filter` (`eq`, `not`). |
| onPremisesSamAccountName | String | Contains the on-premises **SAM account name** synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`). Read-only. |
| onPremisesSecurityIdentifier | String | Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports `$filter` (`eq` including on `null` values). |
| onPremisesSyncEnabled | Boolean | `true` if this group is synced from an on-premises directory; `false` if this group was originally synced from an on-premises directory but is no longer synced; **null** if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`, and `eq` on `null` values). |
| preferredDataLocation | String | The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the *Directory.ReadWrite.All* permission and the user be assigned at least one of the following [Microsoft Entra roles](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json): <br>User Account Administrator- Directory Writer<br>- Exchange Administrator<br>- SharePoint Administrator<br><br> For more information about this property, see [OneDrive Online Multi-Geo](/en-us/sharepoint/dev/solution-guidance/multigeo-introduction). Nullable. Returned by default. |
| preferredLanguage | String | The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, `en-US`. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values). |
| proxyAddresses | String collection | Email addresses for the group that direct to the same group mailbox. For example: `["SMTP: bob@contoso.com", "smtp: bob@sales.contoso.com"]`. The **any** operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`, `endsWith`, `/$count eq 0`, `/$count ne 0`). |
| renewedDateTime | DateTimeOffset | Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the [renew service action](../group-renew). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is `2014-01-01T00:00:00Z`. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`). Read-only. |
| resourceBehaviorOptions | String collection | Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This property can be set only as part of creation (POST). For the list of possible values, see [Microsoft 365 group behaviors and provisioning options](/en-us/graph/group-set-options). |
| resourceProvisioningOptions | String collection | Specifies the group resources that are associated with the Microsoft 365 group. The possible value is `Team`. For more information, see [Microsoft 365 group behaviors and provisioning options](/en-us/graph/group-set-options). Returned by default. Supports `$filter` (`eq`, `not`, `startsWith`). |
| securityEnabled | Boolean | Specifies whether the group is a security group. Required. Returned by default. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| securityIdentifier | String | Security identifier of the group, used in Windows scenarios. Read-only. Returned by default. |
| serviceProvisioningErrors | [serviceProvisioningError](serviceprovisioningerror) collection | Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports `$filter` (`eq`, `not`, for isResolved and serviceInstance). |
| theme | string | Specifies a Microsoft 365 group's color theme. Possible values are `Teal`, `Purple`, `Green`, `Blue`, `Pink`, `Orange`, or `Red`. Returned by default. |
| uniqueName | String | The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only. |
| unseenConversationsCount | Int32 | Count of conversations that have had one or more new posts delivered since the signed-in user's last visit to the group. This property is the same as **unseenCount**. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| unseenCount | Int32 | Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as **unseenConversationsCount**.Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| unseenMessagesCount | Int32 | Count of new posts that have been delivered to the group's conversations since the signed-in user's last visit to the group. Requires `$select` to retrieve. Supported only on the Get group API (`GET /groups/{ID}`). |
| visibility | String | Specifies the group join policy and group content visibility for groups. The possible values are: `Private`, `Public`, or `HiddenMembership`. `HiddenMembership` can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as `Private` by default, and the Microsoft 365 group is `Public`. Groups assignable to roles are always `Private`. To learn more, see group visibility options. Returned by default. Nullable. |

### Group visibility options

| Value | Description |
| --- | --- |
| Public | Anyone can join the group without needing owner permission.Anyone can view the attributes of the group.Anyone can see the members of the group. |
| Private | Owner permission is needed to join the group.Anyone can view the attributes of the group.Anyone can see the members of the group. |
| HiddenMembership | Owner permission is needed to join the group.Guests can't view the attributes of the group.Nonmembers can't see the members of the group. This setting doesn't affect visibility of group owners. Administrators (global, company, user, and helpdesk) can view the membership of the group.The group appears in the global address book (GAL). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| acceptedSenders | [directoryObject](directoryobject) collection | The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post. |
| appRoleAssignments | [appRoleAssignment](approleassignment) collection | Represents the app roles granted to a group for an application. Supports `$expand`. |
| calendar | [calendar](calendar) | The group's calendar. Read-only. |
| calendarView | [event](event) collection | The calendar view for the calendar. Read-only. |
| conversations | [conversation](conversation) collection | The group's conversations. |
| createdOnBehalfOf | [directoryObject](directoryobject) | The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only. |
| drive | [drive](drive) | The group's default drive. Read-only. |
| drives | [drive](drive) collection | The group's drives. Read-only. |
| events | [event](event) collection | The group's calendar events. |
| extensions | [extension](extension) collection | The collection of open extensions defined for the group. Read-only. Nullable. |
| groupLifecyclePolicies | [groupLifecyclePolicy](grouplifecyclepolicy) collection | The collection of lifecycle policies for this group. Read-only. Nullable. |
| memberOf | [directoryObject](directoryobject) collection | Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports `$expand`. |
| members | [directoryObject](directoryobject) collection | The members of this group, who can be users, devices, other groups, or service principals. Supports the [List members](../group-list-members), [Add member](../group-post-members), and [Remove member](../group-delete-members) operations. Nullable. Supports `$expand` including nested `$select`. For example, `/groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName)`. |
| membersWithLicenseErrors | [User](user) collection | A list of group members with license errors from this group-based license assignment. Read-only. |
| onenote | [Onenote](onenote) | Read-only. |
| owners | [directoryObject](directoryobject) collection | The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. - If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner.<br>- A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related [known issue](/en-us/graph/known-issues#non-admin-user-cant-add-self-as-group-owner-during-group-creation-or-update).<br>- For security groups, the admin user isn't automatically added to this collection. For more information, see the related [known issue](/en-us/graph/known-issues#non-admin-user-cant-add-self-as-group-owner-during-group-creation-or-update). Supports `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`); Supports `$expand` including nested `$select`. For example, `/groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName)`. |
| photo | [profilePhoto](profilephoto) | The group's profile photo |
| photos | [profilePhoto](profilephoto) collection | The profile photos owned by the group. Read-only. Nullable. |
| planner | [plannerGroup](plannergroup) | Entry-point to Planner resource that might exist for a Unified Group. |
| rejectedSenders | [directoryObject](directoryobject) collection | The list of users or groups not allowed to create posts or calendar events in this group. Nullable |
| settings | [groupSetting](groupsetting) collection | Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable. |
| sites | [site](site) collection | The list of SharePoint sites in this group. Access the default site with /sites/root. |
| team | [channel](channel) collection | The team associated with this group. |
| threads | [conversationThread](conversationthread) collection | The group's conversation threads. Nullable. |
| transitiveMemberOf | [directoryObject](directoryobject) collection | The groups that a group is a member of, either directly or through nested membership. Nullable. |
| transitiveMembers | [directoryObject](directoryobject) collection | The direct and transitive members of a group. Nullable. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "accessType": "String",
  "allowExternalSenders": "Boolean",
  "acceptedSenders": [{ "@odata.type": "microsoft.graph.directoryObject" }],
  "assignedLicenses": [{ "@odata.type": "microsoft.graph.assignedLicense" }],
  "autoSubscribeNewMembers": "Boolean",
  "calendar": { "@odata.type": "microsoft.graph.calendar" },
  "calendarView": [{ "@odata.type": "microsoft.graph.event" }],
  "classification": "String",
  "conversations": [{ "@odata.type": "microsoft.graph.conversation" }],
  "createdDateTime": "String (timestamp)",
  "createdOnBehalfOf": { "@odata.type": "microsoft.graph.directoryObject" },
  "deletedDateTime":  "String (timestamp)",
  "description": "String",
  "displayName": "String",
  "drive": { "@odata.type": "microsoft.graph.drive" },
  "events": [{ "@odata.type": "microsoft.graph.event" }],
  "groupTypes": ["String"],
  "hasMembersWithLicenseErrors": "Boolean",
  "hideFromAddressLists": "Boolean",
  "hideFromOutlookClients": "Boolean",
  "id": "String (identifier)",
  "isAssignableToRole": "Boolean",
  "isFavorite": "Boolean",
  "isManagementRestricted": "Boolean",
  "isSubscribedByMail": "Boolean",
  "licenseProcessingState": "String",
  "mail": "String",
  "mailEnabled": "Boolean",
  "mailNickname": "String",
  "memberOf": [{ "@odata.type": "microsoft.graph.directoryObject" }],
  "members": [{ "@odata.type": "microsoft.graph.directoryObject" }],
  "membersWithLicenseErrors": [{ "@odata.type": "microsoft.graph.user" }],
  "onPremisesDomainName": "String",
  "onPremisesExtensionAttributes": { "@odata.type": "microsoft.graph.onPremisesExtensionAttributes" },
  "onPremisesLastSyncDateTime": "String (timestamp)",
  "onPremisesNetBiosName": "String",
  "onPremisesProvisioningErrors": [
    { "@odata.type": "microsoft.graph.onPremisesProvisioningError" }
  ],
  "onPremisesSecurityIdentifier": "String",
  "onPremisesSyncEnabled": "Boolean",
  "owners": [{ "@odata.type": "microsoft.graph.directoryObject" }],
  "preferredDataLocation": "String",
  "proxyAddresses": ["String"],
  "photo": { "@odata.type": "microsoft.graph.profilePhoto" },
  "photos": [{ "@odata.type": "microsoft.graph.profilePhoto" }],
  "rejectedSenders": [{ "@odata.type": "microsoft.graph.directoryObject" }],
  "renewedDateTime": "String (timestamp)",
  "resourceBehaviorOptions": ["String"],
  "resourceProvisioningOptions": ["String"],
  "securityEnabled": "Boolean",
  "securityIdentifier": "String",
  "serviceProvisioningErrors": [
    { "@odata.type": "microsoft.graph.serviceProvisioningXmlError" }
  ],
  "sites": [{ "@odata.type": "microsoft.graph.site" }],
  "threads": [{ "@odata.type": "microsoft.graph.conversationThread" }],
  "uniqueName": "String",
  "unseenConversationsCount": "Int32",
  "unseenCount": "Int32",
  "unseenMessagesCount": "Int32",
  "visibility": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-beta&accept=text/markdown)
