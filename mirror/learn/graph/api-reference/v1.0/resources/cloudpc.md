---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: cloudPC resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/cloudpc?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: xhhzuikeaiya
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: cloud-pc
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a cloud-managed virtual desktop.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-10-18T00:00:00.0000000Z
locale: en-us
document_id: c223802d-e32a-0dc4-9cb1-a61dff8ad2c7
document_version_independent_id: 92741d1d-1a26-bec3-63e4-650c861e80b9
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/cloudpc.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/cloudpc
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/cloudpc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 5d1bdf6e-37be-7825-df31-17bc515f5c92
---

# cloudPC resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a cloud-managed virtual desktop. This Cloud PC is also enrolled into Intune and managed through the Microsoft Endpoint Manager portal, so the Cloud PC also has a corresponding Intune managed device ID.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../virtualendpoint-list-cloudpcs) | [cloudPC](cloudpc) collection | List the [cloudPC](cloudpc) devices in a tenant. |
| [Get](../cloudpc-get) | [cloudPC](cloudpc) | Read the properties and relationships of a specific [cloudPC](cloudpc) object. |
| [End grace period](../cloudpc-endgraceperiod) | None | End the grace period for a specific [cloudPC](cloudpc) object. |
| [Reboot](../cloudpc-reboot) | None | Reboot a specific [cloudPC](cloudpc) object. |
| [Rename](../cloudpc-rename) | None | Rename a specific [cloudPC](cloudpc) object. |
| [Reprovision](../cloudpc-reprovision) | None | Reprovision a specific [Cloud PC](cloudpc). |
| [Resize](../cloudpc-resize) | None | Upgrade or downgrade an existing [Cloud PC](cloudpc) to a configuration with a new virtual CPU (vCPU) and storage size. |
| [Restore](../cloudpc-restore) | None | Restore a specific [cloudPC](cloudpc) object to a previous state from a snapshot. |
| [Troubleshoot](../cloudpc-troubleshoot) | None | Troubleshoot a specific [cloudPC](cloudpc) object. |
| [List for user](../user-list-cloudpcs) | [cloudPC](cloudpc) collection | List the [cloudPC](cloudpc) devices that are attributed to the signed-in user. |
| [Retrieve launch detail](../cloudpc-retrievecloudpclaunchdetail) | [cloudPcLaunchDetail](cloudpclaunchdetail) | Get the [cloudPcLaunchDetail](cloudpclaunchdetail) for a specific Cloud PC that belongs to the current signed-in user. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| aadDeviceId | String | The Microsoft Entra device ID for the Cloud PC, also known as the Azure Active Directory (Azure AD) device ID, that consists of 32 characters in a GUID format. Generated on a VM joined to Microsoft Entra ID. Read-only. |
| displayName | String | The display name for the Cloud PC. Maximum length is 64 characters. Read-only. You can use the [cloudPC: rename](../cloudpc-rename) API to modify the Cloud PC name. |
| gracePeriodEndDateTime | DateTimeOffset | The date and time when the grace period ends and reprovisioning or deprovisioning happen. Required only if the status is `inGracePeriod`. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. |
| id | String | The unique identifier of the customer-facing Cloud PC entity that consists of 32 characters in a GUID format. Read-only. Inherited from [entity](entity). |
| imageDisplayName | String | The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. Only letters (A-Z, a-z), numbers (0-9), and special characters (-,\_,.) are allowed for this property. The property value can't begin or end with an underscore. Read-only. |
| lastModifiedDateTime | DateTimeOffset | The last modified date and time of the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. |
| managedDeviceId | String | The Intune enrolled device ID for the Cloud PC that consists of 32 characters in a GUID format. The **managedDeviceId** property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only. |
| managedDeviceName | String | The Intune enrolled device name for the Cloud PC. The **managedDeviceName** property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only. |
| onPremisesConnectionName | String | The on-premises connection that applied during the provisioning of Cloud PCs. Read-only. |
| provisioningPolicyId | String | The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. Read-only. |
| provisioningPolicyName | String | The provisioning policy that applied during the provisioning of Cloud PCs. Maximum length is 120 characters. Read-only. |
| provisioningType | cloudPcProvisioningType | The type of licenses to be used when provisioning Cloud PCs using this policy. The possible values are: `dedicated`, `shared`, `unknownFutureValue`. The default value is `dedicated`. |
| servicePlanId | String | The service plan ID for the Cloud PC that consists of 32 characters in a GUID format. For more information about service plans, see [Product names and service plan identifiers for licensing](/en-us/entra/identity/users/licensing-service-plan-reference). Read-only. |
| servicePlanName | String | The service plan name for the customer-facing Cloud PC entity. Read-only. |
| userPrincipalName | String | The user principal name (UPN) of the user assigned to the Cloud PC. Maximum length is 113 characters. For more information on username policies, see [Password policies and account restrictions in Microsoft Entra ID](/en-us/entra/identity/authentication/concept-sspr-policy#username-policies). Read-only. |

### cloudPcProvisioningType values

| Member | Description |
| --- | --- |
| dedicated | Indicates that a dedicated license is used for provisioning Cloud PCs. Default value. |
| shared | Indicates that a shared license is used for provisioning Cloud PCs. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.cloudPC",
  "aadDeviceId": "String",
  "displayName": "String",
  "gracePeriodEndDateTime": "String (timestamp)",
  "id": "String (identifier)",
  "imageDisplayName": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "managedDeviceId": "String",
  "managedDeviceName": "String",
  "onPremisesConnectionName": "String",
  "provisioningPolicyId": "String",
  "provisioningPolicyName": "String",
  "provisioningType": "String",
  "servicePlanId": "String",
  "servicePlanName": "String",
  "userPrincipalName": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/cloudpc?view=graph-rest-beta&accept=text/markdown)
