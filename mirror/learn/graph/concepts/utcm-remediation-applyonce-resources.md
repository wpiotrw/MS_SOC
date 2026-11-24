---
layout: Conceptual
title: Supported resources for remediation and applyOnce (preview) - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/utcm-remediation-applyonce-resources
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
description: Learn about resource support and authorization requirements for Tenant Configuration Management drift remediation and applyOnce monitors.
ms.date: 2026-11-14T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: conceptual
locale: en-us
document_id: 8fb818cc-58c2-9af3-2e69-9d4af8abf5de
document_version_independent_id: 8fb818cc-58c2-9af3-2e69-9d4af8abf5de
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/utcm-remediation-applyonce-resources.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: utcm-remediation-applyonce-resources
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/utcm-remediation-applyonce-resources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 671df850-287d-67cd-a727-95250c828827
---

# Supported resources for remediation and applyOnce (preview) - Microsoft Graph | Microsoft Learn

Tenant Configuration Management (TCM) drift remediation and `applyOnce` monitors change workload configuration on behalf of the signed-in administrator. These capabilities are available in preview through Microsoft Graph beta. TCM is available only in the global service, not in national clouds.

## Resource support

The following resources are currently supported in the preview.

Grant the delegated workload permissions to the TCM service principal. Assign the listed administrative role to the signed-in user, not to the service principal.

### Microsoft Copilot resources

The delegated permission in this table belongs to Microsoft Graph.

Important

The 20 Copilot resources are Office Cloud Policy Service (OCPS) settings. TCM supports these settings only in tenant-level policies in the Microsoft 365 Apps admin center. Before using TCM, ensure that the target setting isn't configured in any group-level policy in that admin center. If it is, monitoring, snapshots, remediation, and `applyOnce` fail for that resource. This restriction doesn't apply to Agent resources.

| Resource | Delegated permission on the TCM service principal | Least-privileged signed-in user role |
| --- | --- | --- |
| [microsoft.copilot.allowconnectedofficeexperiences](utcm-copilot-resources#allowconnectedofficeexperiences-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowfeedback](utcm-copilot-resources#allowfeedback-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowfileupload](utcm-copilot-resources#allowfileupload-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowinadmincenters](utcm-copilot-resources#allowinadmincenters-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowlogsinfeedback](utcm-copilot-resources#allowlogsinfeedback-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowofficeexperiencesanalyzingcontent](utcm-copilot-resources#allowofficeexperiencesanalyzingcontent-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowoptionalconnectedexperiences](utcm-copilot-resources#allowoptionalconnectedexperiences-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.allowwebsearch](utcm-copilot-resources#allowwebsearch-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.blockaccesstocamerasharing](utcm-copilot-resources#blockaccesstocamerasharing-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.blockaccesstoopenfiles](utcm-copilot-resources#blockaccesstoopenfiles-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.blockaccesstoscreensharing](utcm-copilot-resources#blockaccesstoscreensharing-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.copilotchatpinning](utcm-copilot-resources#copilotchatpinning-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.copilotchatsidepane](utcm-copilot-resources#copilotchatsidepane-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.copilotpagesnotebooks](utcm-copilot-resources#copilotpagesnotebooks-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.frontier](utcm-copilot-resources#frontier-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.harmfulcontentprotections](utcm-copilot-resources#harmfulcontentprotections-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.imagegeneration](utcm-copilot-resources#imagegeneration-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.multipleaccountaccess](utcm-copilot-resources#multipleaccountaccess-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.powerpointdesigner](utcm-copilot-resources#powerpointdesigner-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.copilot.videogeneration](utcm-copilot-resources#videogeneration-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |

The `microsoft.copilot.videogeneration` setting is deprecated and no longer applies. See its [resource description](utcm-copilot-resources#videogeneration-resource-type).

### Microsoft Agent resources

The delegated permission in this table belongs to Microsoft Graph.

| Resource | Delegated permission on the TCM service principal | Least-privileged signed-in user role |
| --- | --- | --- |
| [microsoft.agent.allowedagenttypes](utcm-agent-resources#allowedagenttypes-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.agent.sharing](utcm-agent-resources#sharing-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |
| [microsoft.agent.useraccess](utcm-agent-resources#useraccess-resource-type) | `CopilotPolicySettings.ReadWrite` | AI Administrator |

### Microsoft Exchange resources

The delegated permission in this table belongs to Exchange Online, not Microsoft Graph. `Exchange.Manage` doesn't replace the `Exchange.ManageAsApp` application permission used for monitoring and snapshots.

| Resource | Delegated permission on the TCM service principal | Signed-in user's role |
| --- | --- | --- |
| [microsoft.exchange.accepteddomain](utcm-exchange-resources#accepteddomain-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.antiphishpolicy](utcm-exchange-resources#antiphishpolicy-resource-type) | `Exchange.Manage` | Exchange Administrator OR Security Administrator OR Global Administrator |
| [microsoft.exchange.casmailboxplan](utcm-exchange-resources#casmailboxplan-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.hostedcontentfilterpolicy](utcm-exchange-resources#hostedcontentfilterpolicy-resource-type) | `Exchange.Manage` | Security Administrator OR Exchange Administrator |
| [microsoft.exchange.mailboxplan](utcm-exchange-resources#mailboxplan-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.malwarefilterpolicy](utcm-exchange-resources#malwarefilterpolicy-resource-type) | `Exchange.Manage` | Security Administrator OR Exchange Administrator OR Global Administrator |
| [microsoft.exchange.organizationconfig](utcm-exchange-resources#organizationconfig-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.owamailboxpolicy](utcm-exchange-resources#owamailboxpolicy-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.remotedomain](utcm-exchange-resources#remotedomain-resource-type) | `Exchange.Manage` | Exchange Administrator |
| [microsoft.exchange.safeattachmentpolicy](utcm-exchange-resources#safeattachmentpolicy-resource-type) | `Exchange.Manage` | Exchange Administrator OR Security Administrator |
| [microsoft.exchange.safelinkspolicy](utcm-exchange-resources#safelinkspolicy-resource-type) | `Exchange.Manage` | Security Administrator OR Global Administrator |

`OR` indicates alternative roles, not cumulative requirements. For `antiphishpolicy`, `hostedcontentfilterpolicy`, `malwarefilterpolicy`, `safeattachmentpolicy`, and `safelinkspolicy`, the listed alternatives aren't confirmed least-privilege minima.

### Microsoft Entra resources

The delegated permissions in this table belong to Microsoft Graph.

| Resource | Delegated permission on the TCM service principal | Signed-in user's role |
| --- | --- | --- |
| [microsoft.entra.authenticationmethodpolicy](utcm-entra-resources#authenticationmethodpolicy-resource-type) | `Policy.ReadWrite.AuthenticationMethod` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authenticationmethodpolicyemail](utcm-entra-resources#authenticationmethodpolicyemail-resource-type) | `Policy.ReadWrite.AuthenticationMethod`, `Group.Read.All` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authenticationmethodpolicyfido2](utcm-entra-resources#authenticationmethodpolicyfido2-resource-type) | `Policy.ReadWrite.AuthenticationMethod`, `Group.Read.All` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authenticationmethodpolicysms](utcm-entra-resources#authenticationmethodpolicysms-resource-type) | `Policy.ReadWrite.AuthenticationMethod`, `Group.Read.All` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authenticationmethodpolicyvoice](utcm-entra-resources#authenticationmethodpolicyvoice-resource-type) | `Policy.ReadWrite.AuthenticationMethod`, `Group.Read.All` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authenticationmethodpolicyx509](utcm-entra-resources#authenticationmethodpolicyx509-resource-type) | `Policy.ReadWrite.AuthenticationMethod`, `Group.Read.All` | Authentication Policy Administrator OR Global Administrator |
| [microsoft.entra.authorizationpolicy](utcm-entra-resources#authorizationpolicy-resource-type) | `Policy.ReadWrite.Authorization` | Privileged Role Administrator OR Global Administrator |
| [microsoft.entra.conditionalaccesspolicy](utcm-entra-resources#conditionalaccesspolicy-resource-type) | `Policy.Read.All`, `Policy.ReadWrite.ConditionalAccess`, `Agreement.Read.All`, `Application.Read.All`, `Group.Read.All`, `RoleManagement.Read.Directory`, `User.Read.All`, `CustomSecAttributeDefinition.Read.All` | Conditional Access Administrator OR Security Administrator OR Global Administrator |
| [microsoft.entra.crosstenantaccesspolicyconfigurationdefault](utcm-entra-resources#crosstenantaccesspolicyconfigurationdefault-resource-type) | `Policy.ReadWrite.CrossTenantAccess`, `User.Read.All`, `Group.Read.All` | Security Administrator OR Global Administrator |
| [microsoft.entra.crosstenantaccesspolicyconfigurationpartner](utcm-entra-resources#crosstenantaccesspolicyconfigurationpartner-resource-type) | `Policy.ReadWrite.CrossTenantAccess`; see additional lookup permissions. | Security Administrator OR Global Administrator |
| [microsoft.entra.externalidentitypolicy](utcm-entra-resources#externalidentitypolicy-resource-type) | `Policy.ReadWrite.ExternalIdentities` | Global Administrator |
| [microsoft.entra.namedlocationpolicy](utcm-entra-resources#namedlocationpolicy-resource-type) | `Policy.Read.All`, `Policy.ReadWrite.ConditionalAccess` | Conditional Access Administrator OR Security Administrator OR Global Administrator |
| [microsoft.entra.roledefinition](utcm-entra-resources#roledefinition-resource-type) | `RoleManagement.ReadWrite.Directory` | Privileged Role Administrator OR Global Administrator |
| [microsoft.entra.securitydefaults](utcm-entra-resources#securitydefaults-resource-type) | `Policy.ReadWrite.SecurityDefaults` | Security Administrator OR Global Administrator |
| [microsoft.entra.tenantdetails](utcm-entra-resources#tenantdetails-resource-type) | `Organization.ReadWrite.All` | Billing Administrator OR Global Administrator |

`OR` indicates alternative roles, not cumulative requirements. The listed roles are current setup guidance, not confirmed least-privilege minima. Global Administrator is listed alone for `externalidentitypolicy` while a lower-privileged role is being validated. For `tenantdetails`, role requirements depend on the organization properties being changed; don't generalize this role mapping to unrelated properties.

For `conditionalaccesspolicy`, `authenticationmethodpolicyemail`, `authenticationmethodpolicyx509`, `namedlocationpolicy`, and `crosstenantaccesspolicyconfigurationpartner`, end-to-end validation used Global Administrator. The other listed roles are based on Microsoft Graph documentation and the TCM authorization map and haven't been validated end to end.

For `authenticationmethodpolicyx509`, `Group.Read.All` supports lookup of groups referenced in the baseline.

#### Conditional Access policy restrictions

If a `conditionalaccesspolicy` baseline uses application or service principal filters, the signed-in user also needs the Attribute Definition Reader role. This requirement applies even when the user is a Global Administrator; that role doesn't grant Attribute Definition Reader permissions by default.

#### Cross-tenant access partner policy lookup permissions

For `crosstenantaccesspolicyconfigurationpartner`, grant the following additional delegated permissions to the TCM service principal when the baseline requires the corresponding lookups:

| Baseline lookup | Additional delegated permission |
| --- | --- |
| Application | `Application.Read.All` |
| Group | `Group.Read.All` |
| User | `User.Read.All` |

#### Email authentication method policy restrictions

For `authenticationmethodpolicyemail`, only groups and `all_users` are supported as targets. Individual user targets aren't supported.

### Other resources

Support for monitoring and snapshots doesn't imply support for remediation or `applyOnce`. The existing monitoring and snapshot resource documentation remains available:

- [Microsoft Entra resources](utcm-entra-resources)
- [Exchange resources](utcm-exchange-resources)
- [Intune resources](utcm-intune-resources)
- [Security and Compliance resources](utcm-securityandcompliance-resources)
- [Teams resources](utcm-teams-resources)

The linked resource schemas describe monitoring and snapshots. Their application-permission guidance doesn't replace the delegated permissions and user roles in the preceding tables.

## Authorization requirements

For each confirmed target resource, the TCM service principal needs delegated workload permissions, including the permissions to read the resource's current state. The signed-in user must have the workload administrative role required to manage that resource.

These requirements are separate from the calling app's `ConfigurationMonitoring.ReadWrite.All` delegated permission. See [Set up permissions for remediation and applyOnce (preview)](utcm-authentication-setup#set-up-permissions-for-remediation-and-applyonce-preview) for the three-principal model and tenant-wide delegated-grant setup.