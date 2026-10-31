---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: slaPolicyDefinition resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-casemanagement-slapolicydefinition?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: msklotz
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a service-level agreement policy for a single case type.
ms.date: 2026-09-06T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 835d6b5c-6160-10e8-706b-0c9e850b1c2a
document_version_independent_id: 025bcc8c-a1f1-1f3f-99e7-938626d5e0dd
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-casemanagement-slapolicydefinition.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-casemanagement-slapolicydefinition
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-casemanagement-slapolicydefinition.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 79f5a4f5-609b-7c0f-7b38-ea42792855da
---

# slaPolicyDefinition resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a service-level agreement (SLA) policy that defines scope criteria and warning and breach timers for a single case type.

Each policy belongs to the **slaPolicies** relationship of a [caseTypeConfiguration](security-casemanagement-casetypeconfiguration). The `caseTypeConfigurations/{caseTypeConfiguration-id}` URL segment determines its owning case type: `incidentCase`, `genericCase`, or `exposureCase`. A policy can't target multiple case types. A tenant can have up to 30 policies across its case types.

Timers are evaluated in **order**, lowest first. The first timer whose **filters** match applies; otherwise, the timer with **isDefault** set to `true` applies. A policy supports up to 15 timers and must have exactly one default timer. Timers aren't independently addressable. Updating **timers** replaces the entire collection.

For request bodies, use the canonical `#microsoft.graph...` form of `@odata.type` on polymorphic condition objects. Service responses can omit `@odata.type` on non-polymorphic objects such as **slaPolicyDefinition**, **slaPolicyTimer**, and **slaPolicyRecalculateCondition**.

Inherits from [caseManagementEntity](security-casemanagement-casemanagemententity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../security-casemanagement-casetypeconfiguration-list-slapolicies) | [microsoft.graph.security.caseManagement.slaPolicyDefinition](security-casemanagement-slapolicydefinition) collection | Get the SLA policies configured for a single case type. |
| [Create](../security-casemanagement-casetypeconfiguration-post-slapolicies) | [microsoft.graph.security.caseManagement.slaPolicyDefinition](security-casemanagement-slapolicydefinition) | Create an SLA policy for a single case type. |
| [Get](../security-casemanagement-slapolicydefinition-get) | [microsoft.graph.security.caseManagement.slaPolicyDefinition](security-casemanagement-slapolicydefinition) | Get an SLA policy, including its criteria and timers. |
| [Update](../security-casemanagement-slapolicydefinition-update) | [microsoft.graph.security.caseManagement.slaPolicyDefinition](security-casemanagement-slapolicydefinition) | Update the properties of an SLA policy. |
| [Delete](../security-casemanagement-casetypeconfiguration-delete-slapolicies) | None | Delete an SLA policy. |

## Properties

For supported query parameters when listing policies, see [List slaPolicies](../security-casemanagement-casetypeconfiguration-list-slapolicies#optional-query-parameters).

| Property | Type | Description |
| --- | --- | --- |
| createdBy | String | The identifier of the identity that created the policy. Read-only. Inherited from **caseManagementEntity**. |
| createdDateTime | DateTimeOffset | The date and time when the policy was created, in ISO 8601 format and UTC. Read-only. Inherited from **caseManagementEntity**. |
| description | String | The description of the policy. Maximum length: 5,000 characters. |
| displayName | String | The display name of the policy. Must be unique across the tenant, using a case-insensitive comparison. Maximum length: 150 characters. |
| exitCriteria | [microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock](security-casemanagement-slapolicycriteriablock) | The condition that removes a case from the policy's scope. |
| id | String | The unique, server-generated identifier of the policy. Read-only. Inherited from **caseManagementEntity**. |
| isActive | Boolean | Whether the policy is actively evaluated. Inactive policies are excluded from new case evaluations. The default value on creation is `true`. |
| lastModifiedBy | String | The identifier of the identity that last modified the policy. Read-only. Inherited from **caseManagementEntity**. |
| lastModifiedDateTime | DateTimeOffset | The date and time when the policy was last modified, in ISO 8601 format and UTC. Read-only. Inherited from **caseManagementEntity**. |
| pauseCriteria | [microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock](security-casemanagement-slapolicycriteriablock) | The condition that pauses the timer while a case matches it. |
| recalculateCondition | [microsoft.graph.security.caseManagement.slaPolicyRecalculateCondition](security-casemanagement-slapolicyrecalculatecondition) | The settings that control whether elapsed time resets when the policy is recalculated. |
| setCriteria | [microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock](security-casemanagement-slapolicycriteriablock) | The condition a case must match to enter the policy's scope. When omitted, the policy applies to all cases of its owning case type. The maximum nesting depth is two. |
| timers | [microsoft.graph.security.caseManagement.slaPolicyTimer](security-casemanagement-slapolicytimer) collection | The embedded warning and breach timers, evaluated in **order**, lowest first. Maximum: 15 timers. Exactly one timer must have **isDefault** set to `true`. Updating this property replaces the entire collection. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyDefinition",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "createdBy": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "lastModifiedBy": "String",
  "displayName": "String",
  "description": "String",
  "setCriteria": {
    "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock"
  },
  "exitCriteria": {
    "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock"
  },
  "pauseCriteria": {
    "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock"
  },
  "recalculateCondition": {
    "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyRecalculateCondition",
    "shouldResetTime": "Boolean"
  },
  "isActive": "Boolean",
  "timers": [
    {
      "policyTimerId": "String",
      "order": "Int32",
      "filters": {
        "@odata.type": "#microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock"
      },
      "isDefault": "Boolean",
      "warningThresholdInMinutes": "Int32",
      "breachThresholdInMinutes": "Int32"
    }
  ]
}
```