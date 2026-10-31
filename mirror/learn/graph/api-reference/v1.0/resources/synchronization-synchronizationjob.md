---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: synchronizationJob resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/synchronization-synchronizationjob?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: ArvindHarinder1
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-applications
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: 5e49e501-a7b5-2e21-4421-cf9e68df9619
document_version_independent_id: 530f4c89-34e5-6b9d-eacc-15c542800541
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/synchronization-synchronizationjob.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/synchronization-synchronizationjob
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/synchronization-synchronizationjob.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c70296a6-95a1-9927-b2a1-7adca9d5ec7a
---

# synchronizationJob resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory. The synchronization job is always specific to a particular instance of an application in your tenant. As part of the synchronization job setup, you need to give authorization to read and write objects in your target directory, and customize the job's synchronization schema.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../synchronization-synchronization-list-jobs) | [synchronizationJob](synchronization-synchronizationjob) collection | List existing jobs for a given application instance (service principal). |
| [Get](../synchronization-synchronizationjob-get) | [synchronizationJob](synchronization-synchronizationjob) | Read properties and relationships of a synchronizationJob object. |
| [Create](../synchronization-synchronization-post-jobs) | [synchronizationJob](synchronization-synchronizationjob) | Create new job for a given application. |
| [Start](../synchronization-synchronizationjob-start) | None | Start synchronization. If the job is in a paused state, it continues from the point where the job was paused. If the job is in quarantine, the quarantine status is cleared. |
| [Pause](../synchronization-synchronizationjob-pause) | None | Temporarily stop synchronization. All the progress, including job state, is persisted, and the job will continue from where it left off when a [Start](../synchronization-synchronizationjob-start) call is made. |
| [Restart](../synchronization-synchronizationjob-restart) | None | Force the job to start over and re-process all the objects in the directory. |
| [Delete](../synchronization-synchronizationjob-delete) | None | Stop synchronization, and permanently delete all the state associated with the job. |
| [Provision on demand](../synchronization-synchronizationjob-provisionondemand) | [synchronizationJobApplicationParameters](synchronization-synchronizationjobapplicationparameters) collection | Represents the objects that will be provisioned and the synchronization rules executed. The resource is primarily used for on-demand provisioning. |
| [Validate credentials](../synchronization-synchronizationjob-validatecredentials) | None | Test provided credentials against target directory. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | Unique synchronization job identifier. Read-only. |
| schedule | [synchronizationSchedule](synchronization-synchronizationschedule) | Schedule used to run the job. Read-only. |
| status | [synchronizationStatus](synchronization-synchronizationstatus) | Status of the job, which includes when the job was last run, current job state, and errors. |
| synchronizationJobSettings | [keyValuePair](keyvaluepair) | Settings associated with the job. Some settings are inherited from the template. |
| templateId | String | Identifier of the [synchronization template](synchronization-synchronizationtemplate) this job is based on. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| bulkUpload | [bulkUpload](synchronization-bulkupload) | The bulk upload operation for the job. |
| schema | [synchronizationSchema](synchronization-synchronizationschema) | The synchronization schema configured for the job. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "id": "String (identifier)",
  "schedule": {
    "@odata.type": "microsoft.graph.synchronizationSchedule"
  },
  "status": {
    "@odata.type": "microsoft.graph.synchronizationStatus"
  },
  "synchronizationJobSettings": {
    "@odata.type": "microsoft.graph.keyValuePair"
  },
  "templateId": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/synchronization-synchronizationjob?view=graph-rest-beta&accept=text/markdown)
