---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: activityLogBase resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/activitylogbase?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: Vassu05
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: m365-backup-storage
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an activity log and its properties.
ms.date: 2026-02-12T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: d8374a39-9fb4-2d4b-a213-5450676b14a0
document_version_independent_id: f532ba4a-daf1-dec2-08aa-d3644f1376bc
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/activitylogbase.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/activitylogbase
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/activitylogbase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: ca24ce5d-4e3b-cd10-aecb-87cdb882ca67
---

# activityLogBase resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an activity log record that contains information about any admin activity on backup and restore resources.

Base type for [backupPolicyActivityLog](backuppolicyactivitylog), [dynamicRuleActivityLog](dynamicruleactivitylog), [offboardingActivityLog](offboardingactivitylog), and [restoreTaskActivityLog](restoretaskactivitylog).

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../backuprestoreroot-list-activitylogs) | [activityLogBase](activitylogbase) collection | Get a list of [activityLogBase](activitylogbase) objects and their properties. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| activityType | [activityLogOperationType](enums#activitylogoperationtype-values) | The type of activity performed. The possible values are: `backupPolicyCreated`, `backupPolicyActivated`, `backupPolicyModified`, `backupPolicyPaused`, `backupPolicyRenamed`, `dynamicRuleExecution`, `dynamicRuleDeletion`, `protectionUnitLevelOffboarding`, `policyLevelOffboarding`, `restoreTaskCreated`, `restoreTaskCompleted`, `unknownFutureValue`. |
| error | [publicError](publicerror) | Contains error details if an error occurred while processing this activity. |
| eventDateTime | DateTimeOffset | Timestamp of activity completion. |
| id | String | The unique identifier of the activityLog. |
| performedBy | String | The identity of the person who performed the activity. |
| resultStatus | [activityLogResultStatus](enums#activitylogresultstatus-values) | Indicates the outcome status of the activity. The possible values are: `succeeded`, `failed`, `partiallySucceeded`, `unknownFutureValue`. |
| serviceType | [serviceType](enums#servicetype-values) | Represents the service type. The possible values are: `unknown`, `sharepoint`, `exchange`, `oneDriveForBusiness`, `unknownFutureValue`. |
| severity | [activityLogSeverity](enums#activitylogseverity-values) | Indicates the severity of the activity. The possible values are: `high`, `medium`, `low`, `unknownFutureValue`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.activityLogBase",
  "id": "String (identifier)",
  "eventDateTime": "String (timestamp)",
  "activityType": "String",
  "resultStatus": "String",
  "serviceType": "String",
  "severity": "String",
  "performedBy": "String",
  "error": {
    "@odata.type": "microsoft.graph.publicError"
  }
}
```