---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: contentManagementRepository resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-contentmanagement-contentmanagementrepository?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: AlexBrohshtut
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a connected source-control repository that delivers security content as code in the caller's tenant.
ms.date: 2026-10-29T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: f24f36b2-c34a-2c42-3ae2-612a9ff52e1e
document_version_independent_id: e56185fc-2572-78e0-e108-57e78430ce02
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-contentmanagement-contentmanagementrepository.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-contentmanagement-contentmanagementrepository
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-contentmanagement-contentmanagementrepository.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ca37a3e8-3e9c-b9ea-031c-3ef838ef88a4
---

# contentManagementRepository resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.contentManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a connected source-control repository that delivers security content as code in the caller's tenant.

Inherits from [microsoft.graph.entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List repositories](../contentmanagementroot-list-repositories) | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) collection | List connected repositories. |
| [Get contentManagementRepository](../security-contentmanagement-contentmanagementrepository-get) | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) | Get one connection by its identifier. |
| [contentManagementRepository: connect](../security-contentmanagement-contentmanagementrepository-connect) | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) | Connect a source-control repository. |
| [contentManagementRepository: discoverAvailableRepositories](../security-contentmanagement-contentmanagementrepository-discoveravailablerepositories) | [microsoft.graph.security.contentManagement.discoveredRepository](security-contentmanagement-discoveredrepository) collection | Discover up to 200 accessible candidate repositories. |
| [contentManagementRepository: modify](../security-contentmanagement-contentmanagementrepository-modify) | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) | Modify a connected repository. |
| [contentManagementRepository: disconnect](../security-contentmanagement-contentmanagementrepository-disconnect) | [microsoft.graph.security.contentManagement.repositoryDisconnectResult](security-contentmanagement-repositorydisconnectresult) | Disconnect and report any cleanup warning. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| contentTypes | [microsoft.graph.security.contentManagement.repositoryContentType](enums-security-contentmanagement#repositorycontenttype-values) collection | Content kinds this repository is configured to deploy. The possible values are: `customDetection`, `unknownFutureValue`, `defenderWorkbook`. Use the `Prefer: include-unknown-enum-members` request header to get `defenderWorkbook`. |
| deploymentIdentity | [microsoft.graph.security.contentManagement.deploymentIdentity](security-contentmanagement-deploymentidentity) | Bring-your-own deployment identity used for deployment. Optional; when omitted the platform-managed identity path is used. Provide a service principal or a managed identity. Immutable after connecting. |
| deploymentScope | [microsoft.graph.security.contentManagement.deploymentScope](security-contentmanagement-deploymentscope) | Optional Azure deployment scope, immutable after connecting the repository. |
| description | String | Optional description of the connection. |
| displayName | String | Human-readable name of the connection. Supports `$filter` (`eq`, `ne`) and `$orderby`. |
| id | String | A unique identifier for this resource. Inherited from [entity](entity). Supports `$filter` (`eq`, `ne`). |
| lastDeploymentInfo | [microsoft.graph.security.contentManagement.repositoryDeploymentInfo](security-contentmanagement-repositorydeploymentinfo) | Status of the most recent deployment from this repository. Read-only. |
| pullRequest | [microsoft.graph.security.contentManagement.repositoryPullRequest](security-contentmanagement-repositorypullrequest) | The setup pull request opened for this connection, when applicable. Read-only. |
| repoType | [microsoft.graph.security.contentManagement.repositoryType](enums-security-contentmanagement#repositorytype-values) | Source-control provider for this repository. Immutable after connecting. Supports `$filter` (`eq`, `ne`). The possible values are: `gitHub`, `azureDevOps`, `unknownFutureValue`. |
| servicePrincipal | [microsoft.graph.security.contentManagement.repositoryServicePrincipal](security-contentmanagement-repositoryserviceprincipal) | Service principal / managed identity used by the connection. Read-only. |
| sourceLocation | [microsoft.graph.security.contentManagement.repositorySettings](security-contentmanagement-repositorysettings) | Location of the source repository (URL and branch). |
| systemData | [microsoft.graph.security.contentManagement.systemData](security-contentmanagement-systemdata) | Creation and last modification provenance. Read-only. |
| workloadIdentityFederation | [microsoft.graph.security.contentManagement.repositoryWorkloadIdentityFederation](security-contentmanagement-repositoryworkloadidentityfederation) | Workload identity federation details for the connection, when configured. Read-only. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.contentManagement.contentManagementRepository",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "repoType": "String",
  "contentTypes": [
    "String"
  ],
  "sourceLocation": {
    "@odata.type": "microsoft.graph.security.contentManagement.repositorySettings"
  },
  "deploymentScope": {
    "@odata.type": "microsoft.graph.security.contentManagement.deploymentScope"
  },
  "deploymentIdentity": {
    "@odata.type": "microsoft.graph.security.contentManagement.deploymentIdentity"
  },
  "servicePrincipal": {
    "@odata.type": "microsoft.graph.security.contentManagement.repositoryServicePrincipal"
  },
  "workloadIdentityFederation": {
    "@odata.type": "microsoft.graph.security.contentManagement.repositoryWorkloadIdentityFederation"
  },
  "lastDeploymentInfo": {
    "@odata.type": "microsoft.graph.security.contentManagement.repositoryDeploymentInfo"
  },
  "pullRequest": {
    "@odata.type": "microsoft.graph.security.contentManagement.repositoryPullRequest"
  },
  "systemData": {
    "@odata.type": "microsoft.graph.security.contentManagement.systemData"
  }
}
```