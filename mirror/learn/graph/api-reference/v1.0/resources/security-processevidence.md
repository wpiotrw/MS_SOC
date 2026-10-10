---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: processEvidence resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-processevidence?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: BenAlfasi
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a process that is reported in the alert as evidence.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: 23b9511d-6733-03fc-afd5-93066acab566
document_version_independent_id: c3590eb7-4a0b-111f-de0a-fcab79d92a4b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-processevidence.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-processevidence
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-processevidence.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
platformId: 9064abc6-6c39-e9a9-0c47-97eed3bfb9d1
---

# processEvidence resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents a process that is reported in the alert as evidence.

Inherits from [alertEvidence](security-alertevidence).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| detectionStatus | microsoft.graph.security.detectionStatus | The status of the detection.The possible values are: `detected`, `blocked`, `prevented`, `unknownFutureValue`. |
| imageFile | [microsoft.graph.security.fileDetails](security-filedetails) | Image file details. |
| mdeDeviceId | String | A unique identifier assigned to a device by Microsoft Defender for Endpoint. |
| parentProcessCreationDateTime | DateTimeOffset | Date and time when the parent of the process was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. |
| parentProcessId | Int64 | Process ID (PID) of the parent process that spawned the process. |
| parentProcessImageFile | [microsoft.graph.security.fileDetails](security-filedetails) | Parent process image file details. |
| processCommandLine | String | Command line used to create the new process. |
| processCreationDateTime | DateTimeOffset | Date and time when the process was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. |
| processId | Int64 | Process ID (PID) of the newly created process. |
| userAccount | [microsoft.graph.security.userAccount](security-useraccount) | User details of the user that ran the process. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.processEvidence",
  "createdDateTime": "String (timestamp)",
  "detectionStatus": "String",
  "imageFile": {"@odata.type": "microsoft.graph.security.fileDetails"},
  "mdeDeviceId": "String",
  "parentProcessCreationDateTime": "String (timestamp)",
  "parentProcessId": "Int64",
  "parentProcessImageFile": {"@odata.type": "microsoft.graph.security.fileDetails"},
  "processCommandLine": "String",
  "processCreationDateTime": "String (timestamp)",
  "processId": "Int64",
  "remediationStatus": "String",
  "remediationStatusDetails": "String",
  "roles": ["String"],
  "tags": ["String"],
  "userAccount": {"@odata.type": "microsoft.graph.security.userAccount"},
  "verdict": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-processevidence?view=graph-rest-beta&accept=text/markdown)
