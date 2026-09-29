---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: Overview of Microsoft Entra Backup and Recovery APIs - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: FaithOmbongi
ms.author: ombongifaith
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: overview
description: Learn how to use Microsoft Entra Backup and Recovery APIs as part of your Business Continuity strategy to programmatically back up, preview, and restore directory objects.
ms.reviewer: yuhko-msft, yuhko-msft
ms.localizationpriority: medium
doc_type: conceptualPageType
ms.date: 2026-06-05T00:00:00.0000000Z
locale: en-us
document_id: ff34d613-bcf3-2acb-6f3d-bd0695cde69b
document_version_independent_id: 98547963-55c2-7012-891d-af21eb510d18
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/entrarecoveryservices-backup-recovery-overview.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/entrarecoveryservices-backup-recovery-overview
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/entrarecoveryservices-backup-recovery-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 42178bd4-c6a2-19ad-0be0-803ec6e7e504
---

# Overview of Microsoft Entra Backup and Recovery APIs - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.entraRecoveryServices

The [Microsoft Entra Backup and Recovery](/en-us/entra/backup/overview) APIs in Microsoft Graph enable you to programmatically back up and restore critical directory objects to a previously known good state. These APIs help IT administrators recover from accidental changes or security compromises by viewing available backups, previewing restoration changes, executing recovery operations, and monitoring job progress.

## Supported directory objects

The backup and recovery APIs support the following Microsoft Entra directory objects. For each object type, only a subset of properties and relationships are tracked and supported in the backup and recovery process.

- [Users](user)
- [Groups - Microsoft 365 and security groups](group)
- [Applications](application)
- [Service principals](serviceprincipal)
- [Conditional Access policies](conditionalaccesspolicy)
- [Named location policies](namedlocation)
- [Authentication method policies](authenticationmethodspolicy)
- [Authorization policies](authorizationpolicy)
- [OAuth2 permission grants](oauth2permissiongrant)
- [App role assignments](approleassignment)

Agent identities associated with users, applications, or service principals are also supported.

For more information, see [Supported objects and recoverable properties in Microsoft Entra Backup and Recovery](/en-us/entra/backup/scope-supported-objects-limitations).

Note

Hard-deleted objects can't be recovered. Only objects that were modified, soft-deleted, or newly created since the backup can be addressed by a recovery operation. On-premises Active Directory-synced objects with the source of authority on-premises can't be recovered, but changes are visible in the snapshots.

## Key API concepts

### Snapshots

A [snapshot](entrarecoveryservices-snapshot) represents a point-in-time backup of the tenant's directory data. Each snapshot has a unique identifier (base64-encoded timestamp) and tracks the total count of changed objects. Use snapshots as the starting point for both preview and recovery operations.

Microsoft Entra automatically creates one backup snapshot per day and retains up to five days of snapshot history. Snapshots are non-editable and can't be deleted or disabled by any user or application.

### Jobs

The backup and recovery process revolves around two types of jobs: preview jobs and recovery jobs, represented by the [recoveryPreviewJob](entrarecoveryservices-recoverypreviewjob) and [recoveryJob](entrarecoveryservices-recoveryjob) resource types, respectively.

You can scope both preview and recovery jobs to specific subsets of data using filtering criteria:

- Limit the scope to specific entity types (for example, only users, or only users and groups).
- Limit the scope to specific objects identified by entity type and object ID.

Jobs are long-running operations. When you create a job, the response includes a `Location` header with the URL of the created job resource. Poll this resource to check the job status until it completes.

- A successful preview job provides a comprehensive list of objects that would be affected by a recovery operation, along with the specific property changes.
- A successful recovery job applies the necessary changes to restore the tenant's directory objects to the snapshot state. After completion, you can review any failed changes that couldn't be applied.

Only one job (preview or recovery) can run at a time per tenant. Wait for a running job to complete or cancel it before starting a new one.

#### Recovery preview jobs

A [recoveryPreviewJob](entrarecoveryservices-recoverypreviewjob) is a "dry run" that calculates the differences between the current tenant state and a selected snapshot. Preview jobs don't modify any data.

A preview job can be successfully completed, failed, or abandoned (canceled).

- After a preview job completes, call the [getChanges](../entrarecoveryservices-recoverypreviewjob-getchanges) function to enumerate the objects that would be affected, along with the specific property changes.
- To cancel a preview job, call the [cancel](../entrarecoveryservices-recoveryjobbase-cancel) action. No results are available for an abandoned job.

Each changed object returned by `getChanges` or `getFailedChanges` includes a **recoveryAction** property indicating what the recovery operation does to that object:

| Action | Description |
| --- | --- |
| `update` | The object's properties are updated to match the snapshot state. |
| `softDelete` | The object is soft-deleted because it didn't exist in the snapshot or was deleted in the snapshot. |
| `restore` | The object is restored from a soft-deleted state because it existed in the snapshot. |

#### Recovery jobs

Unlike a preview job, a [recoveryJob](entrarecoveryservices-recoveryjob) executes the actual restoration of directory objects to the selected snapshot state. After a recovery job completes, call the [getFailedChanges](../entrarecoveryservices-recoveryjob-getfailedchanges) function to review any changes that couldn't be applied.

## Typical workflow

The following diagram illustrates the typical end-to-end workflow for using the backup and recovery APIs:

**Step 1: List available snapshots** Retrieve the available backups to identify the snapshot you want to restore to.

```http
GET /directory/recovery/snapshots
```

**Step 2: Create a preview job** Create a preview job to calculate the differences between the current tenant state and the selected snapshot. Optionally, include filtering criteria to limit the scope.

```http
POST /directory/recovery/snapshots/{snapshot-id}/recoveryPreviewJobs
```

**Step 3: Poll the preview job status** The preview job is a long-running operation that returns a `202 Accepted` response with a `Location` header that points to the created job resource. Poll its status until it completes. When the job completes (`successful`, `failed`, or `abandoned` status), retrieve the results.

```http
GET /directory/recovery/snapshots/{snapshot-id}/recoveryPreviewJobs/{job-id}
```

**Step 4: Review the changes** After the preview job completes successfully, retrieve the list of objects that would be affected.

```http
GET /directory/recovery/snapshots/{snapshot-id}/recoveryPreviewJobs/{job-id}/microsoft.graph.entraRecoveryServices.getChanges
```

**Step 5: Create a recovery job** After reviewing the preview, create a recovery job to apply the changes. You can use the same filtering criteria as the preview.

```http
POST /directory/recovery/snapshots/{snapshot-id}/recoveryJobs
```

**Step 6: Monitor the recovery job** The recovery job is a long-running operation that returns a `202 Accepted` response with a `Location` header that points to the created job resource. Poll its status to track progress, including the number of objects and links modified. When the job completes (`successful`, `failed`, or `abandoned` status), retrieve the results.

```http
GET /directory/recovery/snapshots/{snapshot-id}/recoveryJobs/{job-id}
```

**Step 7: Review failed changes (if any)** If the recovery job reports failed changes, retrieve the details to understand what couldn't be applied and why.

```http
GET /directory/recovery/snapshots/{snapshot-id}/recoveryJobs/{job-id}/microsoft.graph.entraRecoveryServices.getFailedChanges
```

Tip

You can cancel a running preview or recovery job at any time by calling the [cancel](../entrarecoveryservices-recoveryjobbase-cancel) action. Canceling a job updates its status to `abandoned`.

## Audit logs

All operations performed through the backup and recovery APIs are logged in the Microsoft Entra [audit logs](directoryaudit) with the category "Backup and Recovery". You can use these logs to track when snapshots were created, when preview and recovery jobs were initiated, and their outcomes.

## Permissions and privileges

The backup and recovery APIs support both delegated and application permissions. For more information about permissions required to call these APIs, see the individual API reference topics for each operation.

In addition to Microsoft Graph permissions, the signed-in user must be assigned one of the following [Microsoft Entra roles](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json):

- **Microsoft Entra Backup Reader** — For read operations (listing snapshots, viewing jobs, retrieving changes).
- **Microsoft Entra Backup Administrator** — For write operations (creating preview jobs, creating recovery jobs, canceling jobs).

## Limitations

- This feature isn't supported for Entra External ID and Azure AD B2C tenants.
- Backup snapshots are created automatically once per day and retained for five days. You can't create, modify, delete, or export snapshots.
- Not all attributes and linked attributes of the supported object types can be recovered.
- On-premises Active Directory-synced objects can't be recovered through these APIs, though changes are visible in snapshots.
- Job completion time depends on the volume of data and processing complexity. Allow at least 1 hour to complete.
- Recovery to another tenant isn't supported.
- Recovery operations don't generate change notifications through [subscriptions](/en-us/graph/api/resources/subscription) or delta records for [change tracking](/en-us/graph/delta-query-overview). Applications that rely on these mechanisms aren't notified of changes made by recovery jobs.

## Throttling

The backup and recovery APIs follow standard [Microsoft Graph service-specific throttling limits](/en-us/graph/throttling-limits). Monitor `429 Too Many Requests` responses and implement retry logic using the `Retry-After` header.

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-beta&accept=text/markdown)
