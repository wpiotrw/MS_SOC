---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: List activitylogs - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/backuprestoreroot-list-activitylogs?view=graph-rest-beta
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
description: Get a list of activityLogBase objects and their properties.
ms.date: 2026-02-12T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 8c763453-723b-067f-0d7d-f6230ef6ce33
document_version_independent_id: 2c990292-9872-e96b-63ac-b9092a48b4bd
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/backuprestoreroot-list-activitylogs.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/backuprestoreroot-list-activitylogs
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/backuprestoreroot-list-activitylogs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c8d4e54f-1a00-8b0b-02d9-51b63558da56
---

# List activitylogs - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Get a list of [activityLogBase](resources/activitylogbase) objects and their properties.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permission | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | BackupRestore-Monitor.Read.All | Not supported. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | BackupRestore-Monitor.Read.All | Not supported. |

## HTTP request

```http
GET /solutions/backupRestore/activityLogs
```

## Optional query parameters

This method supports some of the OData query parameters to help customize the response. For general information, see [OData query parameters](/en-us/graph/query-parameters).

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [activityLogBase](resources/activitylogbase) objects in the response body.

## Examples

### Request

The following example shows a request.

```http
GET https://graph.microsoft.com/beta/solutions/backupRestore/activityLogs
```

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#solutions/backupRestore/activityLogs",
  "value": [
    {
      "@odata.type": "#microsoft.graph.backupPolicyActivityLog",
      "id": "5618d002-be47-80be-21ec-10a03b2807b2",
      "eventDateTime": "2026-02-11T10:30:00Z",
      "activityType": "backupPolicyCreated",
      "resultStatus": "succeeded",
      "serviceType": "exchange",
      "severity": "low",
      "performedBy": "admin@contoso.com",
      "error": null,
      "policyId": "a1234567-b890-1234-c567-d89012345678",
      "policyName": "Exchange Daily Backup Policy",
      "policyStatus": "active",
      "oldPolicyName": null,
      "protectionUnitDetails": {
        "requestedToAddCount": 50,
        "requestedToRemoveCount": 0,
        "addedCount": 50,
        "removedCount": 0,
        "failedCount": 0,
        "backupConfigurationType": "Manual Selection"
      },
      "retentionPeriod": "P30D"
    },
    {
      "@odata.type": "#microsoft.graph.dynamicRuleActivityLog",
      "id": "7829e003-cf58-91cf-32f9-55ea1e334d93",
      "eventDateTime": "2026-02-11T11:00:00Z",
      "activityType": "dynamicRuleExecution",
      "resultStatus": "succeeded",
      "serviceType": "oneDriveForBusiness",
      "severity": "low",
      "performedBy": "system",
      "error": null,
      "policyId": "b2345678-c901-2345-d678-e90123456789",
      "policyName": "OneDrive Protection Policy",
      "policyStatus": "active",
      "protectionUnitDetails": {
        "requestedToAddCount": 15,
        "requestedToRemoveCount": 5,
        "addedCount": 15,
        "removedCount": 5,
        "failedCount": 0,
        "backupConfigurationType": "dynamic"
      }
    },
    {
      "@odata.type": "#microsoft.graph.restoreTaskActivityLog",
      "id": "8930f114-dg69-02dg-43g0-66fb2f445e04",
      "eventDateTime": "2026-02-11T12:15:00Z",
      "activityType": "restoreTaskCompleted",
      "resultStatus": "succeeded",
      "serviceType": "sharepoint",
      "severity": "medium",
      "performedBy": "admin@contoso.com",
      "error": null,
      "restoreSessionId": "c3456789-d012-3456-e789-f01234567890",
      "restoreSessionStatus": "completed",
      "destinationType": "inPlace",
      "tags": "fastRestore",
      "restoreArtifactDetails": {
        "totalArtifactsCount": 100,
        "restoredCount": 100,
        "failedCount": 0
      },
      "restoreCompletionDateTime": "2026-02-11T12:15:00Z"
    },
    {
      "@odata.type": "#microsoft.graph.offboardingActivityLog",
      "id": "9041g225-eh70-13eh-54h1-77gc3g556f15",
      "eventDateTime": "2026-02-11T13:30:00Z",
      "activityType": "protectionUnitLevelOffboarding",
      "resultStatus": "succeeded",
      "serviceType": "exchange",
      "severity": "high",
      "performedBy": "admin@contoso.com",
      "error": null,
      "policyId": "d4567890-e123-4567-f890-012345678901",
      "policyName": "Exchange Protection Policy",
      "policyStatus": "active",
      "offboardingDetails": {
        "totalRequestedCount": 25,
        "offboardedCount": 25,
        "failedCount": 0,
        "cancelledCount": 0,
        "offboardStartDateTime": "2026-02-11T13:20:00Z",
        "offboardEndDateTime": "2026-02-11T13:30:00Z",
        "offboardingStatus": "completed"
      }
    },
    {
      "@odata.type": "#microsoft.graph.backupPolicyActivityLog",
      "id": "a152h336-fi81-24fi-65i2-88hd4h667g26",
      "eventDateTime": "2026-02-11T14:00:00Z",
      "activityType": "backupPolicyActivated",
      "resultStatus": "failed",
      "serviceType": "sharepoint",
      "severity": "high",
      "performedBy": "admin@contoso.com",
      "error": {
        "code": "PolicyActivationFailed",
        "message": "Failed to activate backup policy due to insufficient permissions on target protection units.",
        "innerError": {
          "code": "InsufficientPermissions",
          "message": "The service principal does not have the required permissions to access 10 SharePoint sites."
        }
      },
      "policyId": "e5678901-f234-5678-g901-123456789012",
      "policyName": "SharePoint Protection Policy",
      "policyStatus": "inactive",
      "oldPolicyName": null,
      "protectionUnitDetails": {
        "requestedToAddCount": 30,
        "requestedToRemoveCount": 0,
        "addedCount": 20,
        "removedCount": 0,
        "failedCount": 10,
        "backupConfigurationType": "Manual Selection"
      },
      "retentionPeriod": "P90D"
    }
  ]
}
```