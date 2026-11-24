---
layout: Conceptual
title: Supported Agent resources for Tenant Configuration Management (preview) - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/utcm-agent-resources
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Anusree-stack
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: tenant-configuration-management
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: article
description: Learn about the supported Agent resource types, properties, and permissions for monitoring and snapshots in Tenant Configuration Management.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.localizationpriority: medium
locale: en-us
document_id: db249a65-1dde-5200-3a7d-6cdbd30fabe0
document_version_independent_id: db249a65-1dde-5200-3a7d-6cdbd30fabe0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/utcm-agent-resources.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: utcm-agent-resources
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/utcm-agent-resources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/d56bfe0c-ecd5-4d90-854f-35482bbb1314
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/02e99b71-5808-477b-9387-4c6efa24e46b
platformId: 7b152eb3-7b9a-ff58-a2f8-11edd58fd2b8
---

# Supported Agent resources for Tenant Configuration Management (preview) - Microsoft Graph | Microsoft Learn

This article lists the Agent resource types supported in preview for monitoring and snapshots through the Tenant Configuration Management (TCM) APIs in Microsoft Graph beta. These resources also support [remediation and applyOnce](utcm-remediation-applyonce-resources#microsoft-agent-resources).

All resources on this page use `resourceVersion: 1` and are singletons. They don't have a key property because each tenant has only one instance of each setting. Use the nested `valueObject` properties documented for each resource when creating a baseline.

## Permissions

For monitoring and snapshots, grant the TCM service principal the `CopilotPolicySettings.Read`**application** permission on Microsoft Graph. For remediation and `applyOnce`, grant it the `CopilotPolicySettings.ReadWrite`**delegated** permission. **AI Administrator** is the least-privileged role for the signed-in user for remediation and `applyOnce`; don't assign that user-role requirement to the service principal.

These workload permissions are separate from the permissions required by the app that calls the TCM APIs. See [Set up authentication](utcm-authentication-setup).

The [Copilot group-level policy restriction](utcm-copilot-resources#prerequisites-and-permissions) doesn't apply to the Agent resources on this page.

## allowedagenttypes resource type

### Description

Controls which types of apps, agents, and plugins users can see in their store and install. The author of an app, agent, or plugin determines its type.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| valueObject | Write | AllowedAgentTypesValueObject | Configures which types of apps, agents, and plugins users can see and install. | - |

#### AllowedAgentTypesValueObject

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| areISVAppsAllowed | Write | Boolean | Indicates whether apps, agents, and plugins built by external publishers are allowed. | - |
| areMicrosoftAppsAllowed | Write | Boolean | Indicates whether apps, agents, and plugins built by Microsoft are allowed. | - |
| areMicrosoftCertifiedThirdPartyAppsAllowed | Write | Boolean | Indicates whether only apps, agents, and plugins from certified external publishers are allowed when external publishers are enabled. | - |
| areTenantScopedAppsAllowed | Write | Boolean | Indicates whether apps, agents, and plugins built by the organization are allowed. | - |

### Sample baseline resource

```json
{
  "displayName": "Allowed agent types",
  "resourceType": "microsoft.agent.allowedagenttypes",
  "resourceVersion": 1,
  "properties": {
    "valueObject": {
      "areMicrosoftAppsAllowed": true,
      "areTenantScopedAppsAllowed": true,
      "areISVAppsAllowed": false,
      "areMicrosoftCertifiedThirdPartyAppsAllowed": true
    }
  }
}
```

### Permissions

#### Microsoft Entra ID roles

For remediation and `applyOnce`, **AI Administrator** is the least-privileged [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference) for the signed-in user. This role requirement applies to the user, not to the TCM service principal.

#### Microsoft Graph

Grant the following Microsoft Graph permissions to the TCM service principal. For setup instructions, see [Set up authentication](/en-us/graph/utcm-authentication-setup).

##### Application permissions

| Operation | Supported permissions |
| --- | --- |
| Monitoring and snapshots | CopilotPolicySettings.Read |

##### Delegated permissions

| Operation | Supported permissions |
| --- | --- |
| Remediation and applyOnce | CopilotPolicySettings.ReadWrite |

## sharing resource type

### Description

Controls who can share agents with anyone in the organization. This setting applies to agents built with Microsoft 365 Copilot Agent Builder. Users who can't share with everyone in the organization can still share their agents with individual users and security groups.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| valueObject | Write | AgentSharingValueObject | Configures who can share Agent Builder agents with anyone in the organization. | - |

#### AgentSharingValueObject

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| organizationWideSharingAssignment | Write | UserAssignment | Configures which users can share agents with everyone in the organization. | - |

#### UserAssignment

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| userAssignmentCategory | Write | String | Specifies whether all users or no users can share agents with everyone in the organization. | `everyone`, `noOne` |

### Sample baseline resource

```json
{
  "displayName": "Agent sharing",
  "resourceType": "microsoft.agent.sharing",
  "resourceVersion": 1,
  "properties": {
    "valueObject": {
      "organizationWideSharingAssignment": {
        "userAssignmentCategory": "everyone"
      }
    }
  }
}
```

### Permissions

#### Microsoft Entra ID roles

For remediation and `applyOnce`, **AI Administrator** is the least-privileged [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference) for the signed-in user. This role requirement applies to the user, not to the TCM service principal.

#### Microsoft Graph

Grant the following Microsoft Graph permissions to the TCM service principal. For setup instructions, see [Set up authentication](/en-us/graph/utcm-authentication-setup).

##### Application permissions

| Operation | Supported permissions |
| --- | --- |
| Monitoring and snapshots | CopilotPolicySettings.Read |

##### Delegated permissions

| Operation | Supported permissions |
| --- | --- |
| Remediation and applyOnce | CopilotPolicySettings.ReadWrite |

## useraccess resource type

### Description

Controls which users or groups can use agents built by Microsoft and the organization, including plugins within agents. Some agents require additional permissions or licenses. In pay-as-you-go deployments, allowing access to agents can increase costs.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| valueObject | Write | AgentUserAccessValueObject | Configures who can access agents and plugins. | - |

#### AgentUserAccessValueObject

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| userAssignmentCategory | Write | String | Specifies whether all users or no users can access agents and plugins. | `everyone`, `noOne` |

### Sample baseline resource

```json
{
  "displayName": "Agent user access",
  "resourceType": "microsoft.agent.useraccess",
  "resourceVersion": 1,
  "properties": {
    "valueObject": {
      "userAssignmentCategory": "everyone"
    }
  }
}
```

### Permissions

#### Microsoft Entra ID roles

For remediation and `applyOnce`, **AI Administrator** is the least-privileged [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference) for the signed-in user. This role requirement applies to the user, not to the TCM service principal.

#### Microsoft Graph

Grant the following Microsoft Graph permissions to the TCM service principal. For setup instructions, see [Set up authentication](/en-us/graph/utcm-authentication-setup).

##### Application permissions

| Operation | Supported permissions |
| --- | --- |
| Monitoring and snapshots | CopilotPolicySettings.Read |

##### Delegated permissions

| Operation | Supported permissions |
| --- | --- |
| Remediation and applyOnce | CopilotPolicySettings.ReadWrite |