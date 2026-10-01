---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: device resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/device?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: SanDeo-MSFT
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a device registered in the organization.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-10-25T00:00:00.0000000Z
locale: en-us
document_id: 2b855b67-0f09-bf85-782f-7fb68a24ee7c
document_version_independent_id: 500e299b-6f0f-f0b6-f89b-ae60f77f9332
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/device.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/device
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/device.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 8efce5b9-1d01-4170-d14d-33eb6c6dafbf
---

# device resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a device registered in the organization. Devices are created in the cloud using the Device Registration Service or by Intune. They're used by conditional access policies for multi-factor authentication. These devices can range from desktop and laptop machines to phones and tablets. Inherits from [directoryObject](directoryobject).

This resource is an open type that allows additional properties beyond those documented here.

This resource supports:

- Adding your own data to custom properties as [extensions](/en-us/graph/extensibility-overview).
- Using [delta query](/en-us/graph/delta-query-overview) to track incremental additions, deletions, and updates, by providing a [delta](../user-delta) function.
- [OData query capabilities](/en-us/graph/query-parameters) including `$select`, `$filter`, `$search`, and `$top`. Specific usages are supported only with [Advanced query capabilities](/en-us/graph/aad-advanced-queries#group-properties).

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../device-list) | [device](device) collection | Retrieve a list of devices registered in the directory. |
| [Create](../device-post-devices) | [device](device) | Register a new device in the directory. |
| [Get](../device-get) | [device](device) | Read properties and relationships of a device object. |
| [Update](../device-update) | [device](device) | Update the properties of a device object. |
| [Delete](../device-delete) | None | Delete a device object. |
| [device: provision](../device-provision) | [provisionResponse](provisionresponse) | Provision a device on behalf of an approved Virtual Desktop Infrastructure (VDI) provider. |
| [Get delta](../device-delta) | [device](device) collection | Get incremental changes for devices. |
| [List member of](../device-list-memberof) | [directoryObject](directoryobject) collection | List the groups and administrative units that the device is a direct member of. |
| [List transitive member of](../device-list-transitivememberof) | [directoryObject](directoryobject) collection | List the groups and administrative units that the device is a member of. This operation is transitive. |
| [List registered owners](../device-list-registeredowners) | [directoryObject](directoryobject) collection | Get the users that are registered owners of the device from the registeredOwners navigation property. |
| [Add registered owners](../device-post-registeredowners) | [directoryObject](directoryobject) collection | Add registered owners of the device. |
| [Remove registered owners](../device-delete-registeredowners) | [directoryObject](directoryobject) collection | Delete registered owners from the device. |
| [List registered users](../device-list-registeredusers) | [directoryObject](directoryobject) collection | Get the registered users of the device from the registeredUsers navigation property. |
| [Add registered users](../device-post-registeredusers) | [directoryObject](directoryobject) collection | Add registered users of the device . |
| [Remove registered users](../device-delete-registeredusers) | [directoryObject](directoryobject) collection | Remove registered users from the device . |
| [Check member objects](../directoryobject-checkmemberobjects) | String collection | Check for membership in a list of groups, directory role, or administrative unit objects. |
| [Get member objects](../directoryobject-checkmemberobjects) | String collection | Return all groups, administrative units, and directory roles that the device is a member of. The check is transitive. |

## Properties

Important

Specific usage of `$filter` and the `$search` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#device-properties).

| Property | Type | Description |
| --- | --- | --- |
| accountEnabled | Boolean | `true` if the account is enabled; otherwise, `false`. Required. Default is `true`.  Supports `$filter` (`eq`, `ne`, `not`, `in`). Only callers with at least the Cloud Device Administrator role can set this property. |
| alternativeSecurityIds | [alternativeSecurityId](alternativesecurityid) collection | For internal use only. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`). |
| approximateLastSignInDateTime | DateTimeOffset | The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, and `eq` on `null` values) and `$orderby`. |
| complianceExpirationDateTime | DateTimeOffset | The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
| deviceCategory | String | User-defined property set by Intune to automatically add devices to groups and simplify managing devices. |
| deviceId | String | Unique identifier set by Azure Device Registration Service at the time of registration. This alternate key can be used to reference the device object. Supports `$filter` (`eq`, `ne`, `not`, `startsWith`). |
| deviceMetadata | String | For internal use only. Set to `null`. |
| deviceOwnership | String | Ownership of the device. Intune sets this property. The possible values are: `unknown`, `company`, `personal`. |
| deviceVersion | Int32 | For internal use only. |
| displayName | String | The display name for the device. Maximum length is 256 characters. Required. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values), `$search`, and `$orderby`. |
| enrollmentProfileName | String | Enrollment profile applied to the device. For example, `Apple Device Enrollment Profile`, `Device enrollment - Corporate device identifiers`, or `Windows Autopilot profile name`. This property is set by Intune. |
| enrollmentType | String | Enrollment type of the device. Intune sets this property. The possible values are: `unknown`, `userEnrollment`, `deviceEnrollmentManager`, `appleBulkWithUser`, `appleBulkWithoutUser`, `windowsAzureADJoin`, `windowsBulkUserless`, `windowsAutoEnrollment`, `windowsBulkAzureDomainJoin`, `windowsCoManagement`, `windowsAzureADJoinUsingDeviceAuth`,`appleUserEnrollment`, `appleUserEnrollmentWithServiceAccount`. **NOTE:** This property might return other values apart from those listed. |
| extensionAttributes | [onPremisesExtensionAttributes](onpremisesextensionattributes) | Contains extension attributes 1-15 for the device. The individual extension attributes aren't selectable. These properties are mastered in the cloud and can be set during creation or update of a device object in Microsoft Entra ID. Supports `$filter` (`eq`, `not`, `startsWith`, and `eq` on `null` values). |
| id | String | The unique identifier for the device. Inherited from [directoryObject](directoryobject). Key, Not nullable. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| isCompliant | Boolean | `true` if the device complies with Mobile Device Management (MDM) policies; otherwise, `false`. Read-only. This can only be updated by Intune for any device OS type or by an [approved MDM app](/en-us/windows/client-management/mdm/azure-active-directory-integration-with-mdm) for Windows OS devices. Supports `$filter` (`eq`, `ne`, `not`). |
| isManaged | Boolean | `true` if the device is managed by a Mobile Device Management (MDM) app; otherwise, `false`. This can only be updated by Intune for any device OS type or by an [approved MDM app](/en-us/windows/client-management/mdm/azure-active-directory-integration-with-mdm) for Windows OS devices. Supports `$filter` (`eq`, `ne`, `not`). |
| isManagementRestricted | Boolean | Indicates whether the device is a member of a restricted management administrative unit. If not set, the default value is `null` and the default behavior is false. Read-only.  To manage a device that's a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires `$select` to retrieve. |
| isRooted | Boolean | `true` if the device is rooted or jail-broken. This property can only be updated by Intune. |
| managementType | String | The management channel of the device. This property is set by Intune. The possible values are: `eas`, `mdm`, `easMdm`, `intuneClient`, `easIntuneClient`, `configurationManagerClient`, `configurationManagerClientMdm`, `configurationManagerClientMdmEas`, `unknown`, `jamf`, `googleCloudDevicePolicyController`. |
| manufacturer | String | Manufacturer of the device. Read-only. |
| mdmAppId | String | Application identifier used to register device into MDM. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `startsWith`). |
| model | String | Model of the device. Read-only. |
| onPremisesLastSyncDateTime | DateTimeOffset | The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z` Read-only. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`). |
| onPremisesSecurityIdentifier | String | The on-premises security identifier (SID) for the user who was synchronized from on-premises to the cloud. Read-only. Requires `$select` to retrieve. Supports `$filter` (`eq`). |
| onPremisesSyncEnabled | Boolean | `true` if this object is synced from an on-premises directory; `false` if this object was originally synced from an on-premises directory but is no longer synced; `null` if this object has never been synced from an on-premises directory (default). Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`, and `eq` on `null` values). |
| operatingSystem | String | The type of operating system on the device. Required. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`, and `eq` on `null` values). |
| operatingSystemVersion | String | The version of the operating system on the device. Required. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`, and `eq` on `null` values). |
| physicalIds | String collection | For internal use only. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`,`/$count eq 0`, `/$count ne 0`). |
| profileType | deviceProfileType | The profile type of the device. Possible values: `RegisteredDevice` (default), `SecureVM`, `Printer`, `Shared`, `IoT`. |
| registrationDateTime | DateTimeOffset | Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
| systemLabels | String collection | List of labels applied to the device by the system. Supports `$filter` (`/$count eq 0`, `/$count ne 0`). |
| trustType | String | Type of trust for the joined device. Read-only. Possible values: `Workplace` (indicates *bring your own personal devices*), `AzureAd` (Cloud-only joined devices), `ServerAd` (on-premises domain joined devices joined to Microsoft Entra ID). For more information, see [Introduction to device management in Microsoft Entra ID](/en-us/azure/active-directory/device-management-introduction). Supports `$filter` (`eq`, `ne`, `not`, `in`). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| extensions | [extension](extension) collection | The collection of open extensions defined for the device. Read-only. Nullable. |
| memberOf | [directoryObject](directoryobject) collection | Groups and administrative units that this device is a member of. Read-only. Nullable. Supports `$expand`. |
| registeredOwners | [directoryObject](directoryobject) collection | The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Read-only. Nullable. Supports `$expand`. |
| registeredUsers | [directoryObject](directoryobject) collection | Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports `$expand`. |
| transitiveMemberOf | [directoryObject](directoryobject) collection | Groups and administrative units that the device is a member of. This operation is transitive. Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "accountEnabled": "Boolean",
  "alternativeSecurityIds": [{"@odata.type": "microsoft.graph.alternativeSecurityId"}],
  "approximateLastSignInDateTime": "String (timestamp)",
  "complianceExpirationDateTime": "String (timestamp)",
  "deviceCategory": "String",
  "deviceId": "String",
  "deviceMetadata": "String",
  "deviceOwnership": "String",
  "deviceVersion": "Int32",
  "displayName": "String",
  "enrollmentProfileName": "String",
  "enrollmentType": "String",
  "extensionAttributes": {"@odata.type": "microsoft.graph.onPremisesExtensionAttributes"},
  "id": "String (identifier)",
  "isCompliant": "Boolean",
  "isManaged": "Boolean",
  "isManagementRestricted": "Boolean",
  "isRooted": "Boolean",
  "managementType": "String",
  "manufacturer": "String",
  "mdmAppId": "String",
  "model": "String",
  "onPremisesLastSyncDateTime": "String (timestamp)",
  "onPremisesSecurityIdentifier": "String",
  "onPremisesSyncEnabled": "Boolean",
  "operatingSystem": "String",
  "operatingSystemVersion": "String",
  "physicalIds": ["String"],
  "profileType": "String",
  "registrationDateTime": "String (timestamp)",
  "systemLabels": ["String"],
  "trustType": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/device?view=graph-rest-beta&accept=text/markdown)
