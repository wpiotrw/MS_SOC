---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: userAccount resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-useraccount?view=graph-rest-1.0
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
description: Represents common properties for a user account.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-05-10T00:00:00.0000000Z
locale: en-us
document_id: ca5e4b79-9f20-b138-264c-4af43f973eac
document_version_independent_id: 6e0a9223-38a8-ded6-848a-f0dc86a33d76
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-useraccount.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-useraccount
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-useraccount.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/37da4cc9-0cfc-42a9-ba5e-805706b01ef8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3661fb96-d414-4a4e-b7ad-9370637790dd
platformId: e93ae9ae-18ea-6c15-562a-e93cb629b0f9
---

# userAccount resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents common properties for a user account.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| accountName | String | The displayed name of the user account. |
| activeDirectoryObjectGuid | Guid | The unique user identifier assigned by the on-premises Active Directory. |
| azureAdUserId | String | The user object identifier in Microsoft Entra ID. |
| displayName | String | The user display name in Microsoft Entra ID. |
| domainName | String | The name of the Active Directory domain of which the user is a member. |
| resourceAccessEvents | [microsoft.graph.security.resourceAccessEvent](security-resourceaccessevent) collection | Information on resource access attempts made by the user account. |
| tenantId | String | The Microsoft Entra tenant ID of the user account. |
| userPrincipalName | String | The user principal name of the account in Microsoft Entra ID. |
| userSid | String | The local security identifier of the user account. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.userAccount",
  "accountName": "String",
  "activeDirectoryObjectGuid": "Guid",
  "azureAdUserId": "String",
  "tenantId": "String",
  "displayName": "String",
  "domainName": "String",
  "resourceAccessEvents": [{  "@odata.type": "microsoft.graph.security.resourceAccessEvent"}
  ],
  "userPrincipalName": "String",
  "userSid": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-useraccount?view=graph-rest-beta&accept=text/markdown)
