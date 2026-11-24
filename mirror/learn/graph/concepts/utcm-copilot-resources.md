---
layout: Conceptual
title: Supported Copilot resources for Tenant Configuration Management (preview) - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/utcm-copilot-resources
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
description: Learn about the supported Copilot resource types, properties, and permissions for monitoring and snapshots in Tenant Configuration Management.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.localizationpriority: medium
locale: en-us
document_id: 65d64d1e-93d6-dfcd-caca-d92f5b40a093
document_version_independent_id: 65d64d1e-93d6-dfcd-caca-d92f5b40a093
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/utcm-copilot-resources.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: utcm-copilot-resources
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/utcm-copilot-resources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: a7aabdce-bd5f-5fb0-1d4e-f4050f4be31a
---

# Supported Copilot resources for Tenant Configuration Management (preview) - Microsoft Graph | Microsoft Learn

This article lists the Copilot resource types supported in preview for monitoring and snapshots through the Tenant Configuration Management (TCM) APIs in Microsoft Graph beta. These resources also support [remediation and applyOnce](utcm-remediation-applyonce-resources#microsoft-copilot-resources).

All resources on this page use `resourceVersion: 1` and are singletons. They don't have a key property because each tenant has only one instance of each setting. Use the property names, data types, and allowed values documented for each resource when creating a baseline. The `value` property is a string, not a Boolean or a number. Its meaning varies by setting.

## Prerequisites and permissions

Important

The 20 Copilot resources are Office Cloud Policy Service (OCPS) settings. TCM supports these settings only in tenant-level policies in the Microsoft 365 Apps admin center. Before using TCM, ensure that the target setting isn't configured in any group-level policy in that admin center. If it is, monitoring, snapshots, remediation, and `applyOnce` fail for that resource. This restriction doesn't apply to Agent resources.

For monitoring and snapshots, grant the TCM service principal the `CopilotPolicySettings.Read`**application** permission on Microsoft Graph. For remediation and `applyOnce`, grant it the `CopilotPolicySettings.ReadWrite`**delegated** permission. **AI Administrator** is the least-privileged role for the signed-in user for remediation and `applyOnce`; don't assign that user-role requirement to the service principal.

These workload permissions are separate from the permissions required by the app that calls the TCM APIs. See [Set up authentication](utcm-authentication-setup).

## allowconnectedofficeexperiences resource type

### Description

Controls whether connected experiences are available to users in Office. These include experiences that analyze content, download online content, support document coauthoring and online storage, and provide additional optional connected experiences.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Makes connected Office experiences available or unavailable to users. `0` disables the setting; `1` enables the setting. When unavailable, limited Office functionality and essential services such as licensing remain available. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow connected Office experiences",
  "resourceType": "microsoft.copilot.allowconnectedofficeexperiences",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowfeedback resource type

### Description

Controls whether users can provide feedback to Microsoft about their product experiences with Microsoft 365 products.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents users from submitting feedback to Microsoft about their Microsoft 365 product experiences. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow feedback",
  "resourceType": "microsoft.copilot.allowfeedback",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowfileupload resource type

### Description

Controls whether users can upload files to Copilot.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Controls file uploads. `0` allows uploads in both Microsoft 365 Copilot and Microsoft 365 Copilot Chat. `1` prevents uploads in both. `2` disables uploads in Microsoft 365 Copilot Web mode and Microsoft 365 Copilot Chat while allowing uploads in Microsoft 365 Copilot Work mode. | `0`, `1`, `2` |

### Sample baseline resource

```json
{
  "displayName": "Allow file upload",
  "resourceType": "microsoft.copilot.allowfileupload",
  "resourceVersion": 1,
  "properties": {
    "value": "0"
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

## allowinadmincenters resource type

### Description

Controls whether tenant admins can access and use Admin Copilot in the Microsoft 365 admin center.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents tenant admins from accessing Admin Copilot in the Microsoft 365 admin center. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow Copilot in admin centers",
  "resourceType": "microsoft.copilot.allowinadmincenters",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowlogsinfeedback resource type

### Description

Controls whether users see an option to include additional log files and relevant content samples when they submit feedback to Microsoft.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Shows or hides the option to include additional log files and relevant content samples with feedback submitted to Microsoft. `0` disables the setting; `1` enables the setting. This setting has no effect when users aren't allowed to submit feedback to Microsoft. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow logs in feedback",
  "resourceType": "microsoft.copilot.allowlogsinfeedback",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowofficeexperiencesanalyzingcontent resource type

### Description

Controls whether connected experiences that analyze content are available to users in Office. PowerPoint Designer and Editor in Word are examples of these experiences.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Makes connected Office experiences that analyze content available or unavailable to users. `0` disables the setting; `1` enables the setting. These experiences remain unavailable when the broader connected-experiences-in-Office policy is disabled. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow Office experiences that analyze content",
  "resourceType": "microsoft.copilot.allowofficeexperiencesanalyzingcontent",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowoptionalconnectedexperiences resource type

### Description

Controls whether additional optional connected experiences are available to users in Office. These experiences are offered directly by Microsoft and are governed by terms other than the organization's commercial agreement with Microsoft. Examples include inserting an online video into PowerPoint and using 3D Maps in Excel.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Makes additional optional connected experiences available or unavailable to users. `0` disables the setting; `1` enables the setting. Users can turn off these experiences as a group when they are available. They remain unavailable when the broader connected-experiences-in-Office policy is disabled. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Allow optional connected experiences",
  "resourceType": "microsoft.copilot.allowoptionalconnectedexperiences",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## allowwebsearch resource type

### Description

Controls web search availability in Microsoft 365 Copilot and Microsoft 365 Copilot Chat. Web search data is handled under Bing consumer terms, separately from Microsoft 365 data handling and processing terms.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Controls web search. `0` enables it in Microsoft 365 Copilot and Microsoft 365 Copilot Chat. `1` disables it in both. `2` disables it in Microsoft 365 Copilot Work mode while enabling it in Microsoft 365 Copilot Web mode and Microsoft 365 Copilot Chat. When web search is available, users can turn it off for themselves. Web search can be enabled independently of the optional connected experiences policy. | `0`, `1`, `2` |

### Sample baseline resource

```json
{
  "displayName": "Allow web search",
  "resourceType": "microsoft.copilot.allowwebsearch",
  "resourceVersion": 1,
  "properties": {
    "value": "0"
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

## blockaccesstocamerasharing resource type

### Description

Controls camera sharing for Vision in Microsoft Copilot. Turning off camera sharing doesn't turn off voice.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents camera sharing for Vision in Microsoft Copilot. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Block access to camera sharing",
  "resourceType": "microsoft.copilot.blockaccesstocamerasharing",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## blockaccesstoopenfiles resource type

### Description

Controls whether users can ask Copilot questions about the file currently open in an eligible Microsoft 365 app, such as requesting summaries, key action items, or rewrites. This policy applies only to users without a Microsoft 365 Copilot license.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents Copilot from accessing the currently open file when responding to prompts. `0` disables the setting; `1` enables the setting. In Outlook, blocking access also blocks all entry points to Copilot Chat. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Block access to open files",
  "resourceType": "microsoft.copilot.blockaccesstoopenfiles",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## blockaccesstoscreensharing resource type

### Description

Controls screen sharing for Vision in Microsoft Copilot. Turning off screen sharing doesn't turn off voice.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents screen sharing for Vision in Microsoft Copilot. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Block access to screen sharing",
  "resourceType": "microsoft.copilot.blockaccesstoscreensharing",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## copilotchatpinning resource type

### Description

Controls whether Microsoft 365 Copilot Chat is pinned to the navigation bar in Microsoft 365 apps.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Pins or unpins Microsoft 365 Copilot Chat in Microsoft 365 apps. `0` disables the setting; `1` enables the setting. As of January 20, 2026, this setting no longer governs the Microsoft 365 Copilot app. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Copilot Chat pinning",
  "resourceType": "microsoft.copilot.copilotchatpinning",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## copilotchatsidepane resource type

### Description

Controls whether users without a Microsoft 365 Copilot license can access Microsoft 365 Copilot Chat from Microsoft 365 apps.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Shows or hides Microsoft 365 Copilot Chat entry points in Microsoft 365 apps for users without a Microsoft 365 Copilot license. `0` disables the setting; `1` enables the setting. This policy doesn't apply to licensed users. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Copilot Chat side pane",
  "resourceType": "microsoft.copilot.copilotchatsidepane",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## copilotpagesnotebooks resource type

### Description

Controls whether users can create and view Copilot Pages and Copilot Notebooks through Microsoft 365 Copilot Chat and Copilot Actions.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents creating and viewing Copilot Pages and Copilot Notebooks through Microsoft 365 Copilot Chat and Copilot Actions. `0` disables the setting; `1` enables the setting. When disabled, Copilot Chat doesn't provide live access to view or edit shared Loop files, and Copilot Actions email and Teams notifications are disabled. This policy is separate from the policy for creating and viewing Loop files in supported Microsoft apps. Copilot Notebooks also require a Microsoft 365 Copilot license. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Copilot Pages and Notebooks",
  "resourceType": "microsoft.copilot.copilotpagesnotebooks",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## frontier resource type

### Description

Controls whether users can access experimental Frontier features in Microsoft 365 web apps.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents access to experimental, unsupported Frontier features in Microsoft 365 web apps. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Copilot Frontier",
  "resourceType": "microsoft.copilot.frontier",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## harmfulcontentprotections resource type

### Description

Controls whether users can adjust harmful-content protection options in Microsoft 365 Copilot Chat.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Controls whether users can adjust harmful-content protection. `0` provides users with the option to adjust harmful-content protection. `1` doesn't provide users with the option to adjust harmful-content protection. This policy applies only to Microsoft 365 Copilot Chat. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Harmful content protections",
  "resourceType": "microsoft.copilot.harmfulcontentprotections",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## imagegeneration resource type

### Description

Controls tenant access to Designer Image Generation in AppChat, BizChat, Copilot Visual Creator, and compliant web Copilot experiences.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Blocks or retains tenant access to Designer Image Generation. `0` disables the setting; `1` enables the setting. Enabling the setting blocks access; disabling or not configuring it retains access. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Image generation",
  "resourceType": "microsoft.copilot.imagegeneration",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## multipleaccountaccess resource type

### Description

Controls whether users can use Copilot in Microsoft 365 apps on work documents with a Copilot license from outside the organization.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Allows or prevents users from using an external or personal Copilot license on work documents. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Multiple account access",
  "resourceType": "microsoft.copilot.multipleaccountaccess",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## powerpointdesigner resource type

### Description

Controls whether PowerPoint Designer is available in Microsoft PowerPoint on Windows.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Enables or disables PowerPoint Designer. `0` disables the setting; `1` enables the setting. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "PowerPoint Designer",
  "resourceType": "microsoft.copilot.powerpointdesigner",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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

## videogeneration resource type

### Description

Deprecated. The generative-AI video creation feature previously powered by Sora is unavailable, and this policy no longer applies.

### Parameters

| Parameter | Attribute | DataType | Description | Allowed Values |
| --- | --- | --- | --- | --- |
| value | Write | String | Formerly controlled access to generative-AI video creation in Video Creator and Microsoft 365 apps. `0` disables the setting; `1` enables the setting. Enabling the setting blocked access. This setting is deprecated and no longer applies. | `0`, `1` |

### Sample baseline resource

```json
{
  "displayName": "Deprecated - Copilot video generation",
  "resourceType": "microsoft.copilot.videogeneration",
  "resourceVersion": 1,
  "properties": {
    "value": "1"
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