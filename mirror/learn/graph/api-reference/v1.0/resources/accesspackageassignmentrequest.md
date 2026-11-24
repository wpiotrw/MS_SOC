---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessPackageAssignmentRequest resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accesspackageassignmentrequest?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: markwahl-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: An access package assignment request created by a user who wants to obtain an access package assignment.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-10-14T00:00:00.0000000Z
locale: en-us
document_id: 58329c0d-50b2-2b69-b968-e36e4d7c6ad9
document_version_independent_id: 0369ad98-97b9-c193-eff8-3bc1aec1c267
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accesspackageassignmentrequest.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accesspackageassignmentrequest
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accesspackageassignmentrequest.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: a1a2469a-5e9a-012d-cc6a-234914215b9a
---

# accessPackageAssignmentRequest resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

In [Microsoft Entra Entitlement Management](entitlementmanagement-overview), an access package assignment request is created by or on behalf of a user who wants to obtain an access package assignment. If the request is successful, with any necessary approvals, the user receives an access package assignment, and is the subject of that resulting access package assignment. Microsoft Entra ID also creates access package assignment requests automatically for tracking access removal.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../entitlementmanagement-list-assignmentrequests) | [accessPackageAssignmentRequest](accesspackageassignmentrequest) collection | Retrieve a list of **accesspackageassignmentrequest** objects. |
| [Create](../entitlementmanagement-post-assignmentrequests) | [accessPackageAssignmentRequest](accesspackageassignmentrequest) | Creates a new **accessPackageAssignmentRequest** object. |
| [Get](../accesspackageassignmentrequest-get) | [accessPackageAssignmentRequest](accesspackageassignmentrequest) | Read properties and relationships of an **accessPackageAssignmentRequest** object. |
| [Delete](../accesspackageassignmentrequest-delete) | None | Delete an **accessPackageAssignmentRequest**. |
| [Cancel](../accesspackageassignmentrequest-cancel) | [accessPackageAssignmentRequest](accesspackageassignmentrequest) collection | Cancel an **accessPackageAssignmentRequest** object that is in a cancelable state. |
| [Filter by current user](../accesspackageassignmentrequest-filterbycurrentuser) | [accessPackageAssignmentRequest](accesspackageassignmentrequest) collection | Retrieve the list of **accessPackageAssignmentRequest** objects filtered on the signed-in user. |
| [Reprocess](../accesspackageassignmentrequest-reprocess) | None | Automatically retry a user’s request for access to an access package. |
| [Resume](../accesspackageassignmentrequest-resume) | None | Resume a user's access package request after waiting for a callback from a custom extension. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| answers | [accessPackageAnswer](accesspackageanswer) collection | Answers provided by the requestor to [accessPackageQuestions](accesspackagequestion) asked of them at the time of request. |
| completedDateTime | DateTimeOffset | The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
| customExtensionCalloutInstances | [customExtensionCalloutInstance](customextensioncalloutinstance) collection | Information about all the custom extension calls that were made during the access package assignment workflow. |
| createdDateTime | DateTimeOffset | The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Supports `$filter`. |
| id | String | Read-only. |
| justification | String | The requestor's supplied justification. |
| parameters | [accessPackageAssignmentRequestParameters](accesspackageassignmentrequestparameters) | Additional parameters that control how the request is processed, such as bypassing the approval requirement configured on the access package policy. |
| requestType | accessPackageRequestType | The type of the request. The possible values are: `notSpecified`, `userAdd`, `userUpdate`, `userRemove`, `adminAdd`, `adminUpdate`, `adminRemove`, `systemAdd`, `systemUpdate`, `systemRemove`, `onBehalfAdd` (not supported), `unknownFutureValue`. Use the `Prefer: include-unknown-enum-members` request header to get the following values in this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `approverRemove`. Requests from the user have a **requestType** of `userAdd`, `userUpdate`, or `userRemove`. This property can't be changed once set. |
| schedule | [entitlementManagementSchedule](entitlementmanagementschedule) | The range of dates that access is to be assigned to the requestor. This property can't be changed once set, but a new schedule for an assignment can be included in another `userUpdate` or `adminUpdate` assignment request. |
| state | accessPackageRequestState | The state of the request. The possible values are: `submitted`, `pendingApproval`, `delivering`, `delivered`, `deliveryFailed`, `denied`, `scheduled`, `canceled`, `partiallyDelivered`, `unknownFutureValue`. Read-only. Supports `$filter` (`eq`). |
| status | String | More information on the request processing status. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| accessPackage | [accessPackage](accesspackage) | The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports `$expand`. |
| assignment | [accessPackageAssignment](accesspackageassignment) | For a **requestType** of `userAdd` or `adminAdd`, this is an access package assignment requested to be created. For a **requestType** of `userRemove`, `adminRemove`, `approverRemove`, or `systemRemove`, this has the `id` property of an existing assignment to be removed.  Supports `$expand`. |
| requestor | [accessPackageSubject](accesspackagesubject) | The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessPackageAssignmentRequest",
  "completedDateTime": "String (timestamp)",
  "createdDateTime": "String (timestamp)",
  "id": "String (identifier)",
  "requestType": "String",
  "justification": "String",
  "parameters": {"@odata.type": "microsoft.graph.accessPackageAssignmentRequestParameters"},
  "schedule": {
    "@odata.type": "microsoft.graph.entitlementManagementSchedule"
  },
  "state": "String",
  "status": "String",
  "answers": [
    {
      "@odata.type": "microsoft.graph.accessPackageAnswerString"
    }
  ]

}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accesspackageassignmentrequest?view=graph-rest-beta&accept=text/markdown)
