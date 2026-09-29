---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: authenticationBehaviors resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/authenticationbehaviors?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: medhir
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Authentication behaviors provide applications flexibility in adopting breaking-change behaviors related to token issuance.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-20T00:00:00.0000000Z
locale: en-us
document_id: 094c1b98-2b56-94ec-7ed3-8d8a1a1d4ff8
document_version_independent_id: 7fb0f43d-b062-7b0c-58f5-9214c9530901
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/authenticationbehaviors.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/authenticationbehaviors
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/authenticationbehaviors.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: ddff2a5f-38a5-7096-bc35-a4893332c68e
---

# authenticationBehaviors resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Describes the authentication behaviors set in the context of an [application](application). Authentication behaviors are Boolean flags that provide applications flexibility in adopting breaking-change behaviors related to token issuance. These updated token issuance behaviors can be related to security mitigations, security improvements, or feature deprecations.

Applications can adopt new breaking changes by enabling a behavior (set the behavior to `true`), or continue using preexisting behavior by disabling it (by setting the behavior to `false`). For more information about managing authentication behaviors, see [Manage application authenticationBehaviors](/en-us/graph/applications-authenticationbehaviors).

Note

The **coopEnforcement** property isn't available in national cloud deployments. It's available only for the global service.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| blockAzureADGraphAccess | Boolean | If `false`, allows the app to have extended access to Azure AD Graph until August 31, 2025 when Azure AD Graph is fully retired. For more information on Azure AD retirement updates, see [June 2024 update on Azure AD Graph API retirement](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/june-2024-update-on-azure-ad-graph-api-retirement/ba-p/4094534). |
| coopEnforcement | Boolean | Indicates whether Cross-Origin-Opener-Policy (COOP) headers are enforced on browser-based authentication responses for the application. Set to `true` to enable enforcement, `false` to temporarily suppress enforcement, or `null` to use the service default. For how-to guidance, see [Control Cross-Origin-Opener-Policy enforcement](/en-us/graph/applications-authenticationbehaviors#control-cross-origin-opener-policy-enforcement). |
| removeUnverifiedEmailClaim | Boolean | If `true`, removes the `email` claim from tokens sent to an application when the email address's domain can't be verified. |
| requireClientServicePrincipal | Boolean | If `true`, requires multitenant applications to have a service principal in the resource tenant as part of authorization checks before they're granted access tokens. This property is only modifiable for multitenant resource applications that rely on access from clients without a service principal and had this behavior as set to `false` by Microsoft. Tenant administrators should respond to security advisories sent through Azure Health Service events and the Microsoft 365 message center. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.authenticationBehaviors",
  "blockAzureADGraphAccess": "Boolean",
  "coopEnforcement": "Boolean",
  "removeUnverifiedEmailClaim": "Boolean",
  "requireClientServicePrincipal": "Boolean"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/authenticationbehaviors?view=graph-rest-beta&accept=text/markdown)
