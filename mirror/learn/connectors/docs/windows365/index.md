---
layout: Reference
title: Windows 365 - Connectors | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/connectors/windows365/
ms.subservice: connectors
author: miriver
ms.author: miriver
ms.manager: jwarner
ms.service: power-platform
ms.date: 2024-03-01T00:00:00.0000000Z
breadcrumb_path: /connectors/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-PowerPlatform
feedback_system: None
ms.topic: generated-reference
locale: en-us
document_id: 95f481b5-1bed-79de-d248-8544a578ce8e
document_version_independent_id: 95f481b5-1bed-79de-d248-8544a578ce8e
original_content_git_url: https://github.com/MicrosoftDocs/BusinessApplicationPlatform-Connectors/blob/live/docs/windows365/index.yml
site_name: Docs
depot_name: MSDN.businessplatform-connectors
page_type: powerconnector
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: windows365/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/windows365/index.yml
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 47b159a8-11ed-a7be-0940-bd1750351ffb
---

# Windows 365 (Preview)

![](https://conn-afd-prod-endpoint-bmc9bqahasf3grgk.b01.azurefd.net/releases/v1.0.1793/1.0.1793.4581/windows365/icon.png)
Windows 365 is a cloud-based service that automatically creates a new type of Windows virtual machine (Cloud PCs) for your end users. Each Cloud PC is assigned to an individual user as a dedicated Windows device. Windows 365 provides the productivity, security, and collaboration benefits of Microsoft 365.

This connector is available in the following products and regions:

| Service | Class | Regions |
| --- | --- | --- |
| **Copilot Studio** | Premium | All [Power Automate regions](/en-us/flow/regions-overview) except the following:  - US Government (GCC)  - US Government (GCC High)  - China Cloud operated by 21Vianet  - US Department of Defense (DoD) |
| **Logic Apps** | Standard | All [Logic Apps regions](https://azure.microsoft.com/global-infrastructure/services/?products=logic-apps&amp;regions=all) except the following:  - Azure Government regions  - Azure China regions  - US Department of Defense (DoD) |
| **Power Apps** | Premium | All [Power Apps regions](/en-us/powerapps/administrator/regions-overview#what-regions-are-available) except the following:  - US Government (GCC)  - US Government (GCC High)  - China Cloud operated by 21Vianet  - US Department of Defense (DoD) |
| **Power Automate** | Premium | All [Power Automate regions](/en-us/flow/regions-overview) except the following:  - US Government (GCC)  - US Government (GCC High)  - China Cloud operated by 21Vianet  - US Department of Defense (DoD) |

| Contact | - |
| --- | --- |
| Name | Microsoft |
| URL | https://powerautomate.microsoft.com/en-us/support/ |

| Connector Metadata | - |
| --- | --- |
| Publisher | Microsoft |
| Website | https://www.microsoft.com/en-us/windows-365 |
| Privacy policy | https://privacy.microsoft.com/en-us/privacystatement |
| Categories | IT Operations;Productivity |

| **Service** | **Class** | **Regions** |
| --- | --- | --- |
| **Copilot Studio** | Premium | All [Power Automate regions](/en-us/flow/regions-overview) |
| **Logic Apps** | Premium | All [Logic Apps regions](https://azure.microsoft.com/global-infrastructure/services/?products=logic-apps&amp;regions=all) |
| **Power Apps** | Premium | All [Power Apps regions](/en-us/powerapps/administrator/regions-overview#what-regions-are-available) |
| **Power Automate** | Premium | All [Power Automate regions](/en-us/flow/regions-overview) |

| **Contact** | - |
| --- | --- |
| Name | Windows 365 |
| URL | /en-us/connectors/windows365 |
| Email | W365powerplatform@microsoft.com |

## Known issues and limitations

The Windows 365 connector is currently in Public Preview.

Microsoft wants to make sure that a connector is stable before we release it to general availability. Until that time, the connector is in preview. Previews are provided "as is," "with all faults," and "as available". They're excluded from service level agreements (SLAs), but are made available on a preview basis so that you can get early access and provide feedback. [Learn more about preview features and how to enable them](/en-us/power-platform/admin/what-are-preview-features-how-do-i-enable-them). Previews might not be covered by customer support. They might be discontinued at any time without notice and might not be released into general availability.

We encourage you to try out the preview connectors and provide feedback. This will help us stabilize and improve the connectors. You can use the [product forums](https://powerusers.microsoft.com/t5/Using-Connectors/bd-p/ConnectingToData) for sharing issues and feedback. Microsoft support might not be available for preview features, including connectors, but we'll try to provide support on a best-effort basis.

To learn more, please visit the [Connectors in preview FAQ](/en-us/connectors/custom-connectors/preview-connector-faq).

## General limits

1. Capabilities and limitations are consistent with the underlying [Graph API](/en-us/graph/api/resources/cloudpc-api-overview?view=graph-rest-1.0).
2. When needing to call something on the Graph beta endpoint, use the HTTP request action.

## Actions:

### List Cloud PCs

**Operation ID:** ListCloudPCs

This action allows you to list Cloud PCs.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **$select** | No | string | $select allows you to choose which properties are returned from Graph. |
| **$filter** | No | string | $filter allows you to get a just subset of a collection from Graph. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| **aadDeviceId** | String | The Microsoft Entra device ID for the Cloud PC, also known as the Azure Active Directory (Azure AD) device ID, that consists of 32 characters in a GUID format. Generated on a VM joined to Microsoft Entra ID. Read-only. |
| **diskEncryptionState** | String | Shows disk encryption state. |
| **displayName** | String | The display name for the Cloud PC. Maximum length is 64 characters. Read-only. |
| **gracePeriodEndDateTime** | DateTimeOffset | The date and time when the grace period ends and reprovisioning or deprovisioning happen. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. |
| **id** | String | The unique identifier of the customer-facing Cloud PC entity that consists of 32 characters in a GUID format. Read-only. |
| **imageDisplayName** | String | The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. Only letters (A-Z, a-z), numbers (0-9), and special characters (-,\_,.) are allowed for this property. The property value can't begin or end with an underscore. Read-only. |
| **lastModifiedDateTime** | DateTimeOffset | The last modified date and time of the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. |
| **managedDeviceId** | String | The Intune enrolled device ID for the Cloud PC that consists of 32 characters in a GUID format. The **managedDeviceId** property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only. |
| **managedDeviceName** | String | The Intune enrolled device name for the Cloud PC. The **managedDeviceName** property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only. |
| **onPremisesConnectionName** | String | The on-premises connection that applied during the provisioning of Cloud PCs. Read-only. |
| **provisioningPolicyId** | String | The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. Read-only. |
| **provisioningPolicyName** | String | The provisioning policy that applied during the provisioning of Cloud PCs. Maximum length is 120 characters. Read-only. |
| **provisioningType** | String | Shows provisioning type. |
| **servicePlanId** | String | The service plan ID for the Cloud PC that consists of 32 characters in a GUID format. For more information about service plans, see [Product names and service plan identifiers for licensing](/en-us/entra/identity/users/licensing-service-plan-reference). Read-only. |
| **servicePlanName** | String | The service plan name for the customer-facing Cloud PC entity. Read-only. |
| **servicePlanType** | String | Shows plan type. |
| **userPrincipalName** | String | The user principal name (UPN) of the user assigned to the Cloud PC. Maximum length is 113 characters. For more information on username policies, see [Password policies and account restrictions in Microsoft Entra ID](/en-us/entra/identity/authentication/concept-sspr-policy#username-policies). Read-only. |

### Get provisioning policies

**Operation ID:** GetProvisioningPoliciesV1

This action allows you to return information about the provisioning policies.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **$select** | No | String | $select allows you to choose which properties are returned from Graph. |
| **$filter** | No | String | $filter allows you to get a just subset of a collection from Graph. |
| **$expand** | No | String | $expand allows you to return related resources from Graph. |

**Returns**

Use $expand with a value of assignments to see the returned values below:

| Name | Type | Description |
| --- | --- | --- |
| **cloudPCNamingTemplate** | String | The template used to name Cloud PCs provisioned using this policy. The template can contain custom text and replacement tokens, including %USERNAME:x% and %RAND:x%, which represent the user's name and a randomly generated number, respectively. For example, CPC-%USERNAME:4%-%RAND:5% means that the name of the Cloud PC starts with CPC-, followed by a four-character username, a - character, and then five random characters. The total length of the text generated by the template can't exceed 15 characters. |
| **description** | String | The provisioning policy description. |
| **displayName** | String | The display name for the provisioning policy. |
| **domainJoinConfiguration** | [cloudPcDomainJoinConfiguration](/en-us/graph/api/resources/cloudpcdomainjoinconfiguration?view=graph-rest-1.0) collection | Specifies a list ordered by priority on how Cloud PCs join Microsoft Entra ID (Azure AD). |
| **enableSingleSignOn** | Boolean | True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. The default value is false. Windows 365 users can use single sign-on to authenticate to Microsoft Entra ID with passwordless options (for example, FIDO keys) to access their Cloud PC |
| **id** | String | The unique identifier associated with the provisioning policy. This ID is auto populated during the creation of a new provisioning policy. Read-only. |
| **imageDisplayName** | String | The display name of the operating system image that is used for provisioning. For example, Windows 11 Preview + Microsoft 365 Apps 23H2 23H2. |
| **imageId** | String | The unique identifier that represents an operating system image that is used for provisioning new Cloud PCs. The format for a gallery type image is: {publisherName\_offerName\_skuName}. Supported values for each of the parameters are:<br>- publisher: Microsoftwindowsdesktop<br>- offer: windows-ent-cpc<br>- sku: 21h1-ent-cpc-m365, 21h1-ent-cpc-os, 20h2-ent-cpc-m365, 20h2-ent-cpc-os, 20h1-ent-cpc-m365, 20h1-ent-cpc-os, 19h2-ent-cpc-m365, and 19h2-ent-cpc-os |
| **imageType** | [cloudPcProvisioningPolicyImageType](/en-us/graph/api/resources/cloudpcprovisioningpolicy?view=graph-rest-1.0#cloudpcprovisioningpolicyimagetype-values) | The type of operating system image (custom or gallery) that is used for provisioning on Cloud PCs. Possible values are: gallery, custom. The default value is gallery. |

### Get a provisioning policy

**Operation ID:** GetAProvisioningPolicyV1

This action allows you to get the details of a specific provisioning policy.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Provisioning policy ID** | Yes | String | The ID of the provisioning policy. Must be included. |
| **$select** | No | String | $select allows you to choose which properties are returned from Graph. |
| **$filter** | No | String | $filter allows you to get a just subset of a collection from Graph. |

**Returns**

The outputs of this operation are dynamic.

### Create a provisioning policy

**Operation ID:** CreateAProvisioningPolicyV1

This action allows you to create a provisioning policy.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Name** | Yes | String | The provisioning policy that applied during the provisioning of Cloud PCs. Maximum length is 120 characters |
| **Description** | Yes | String | The provisioning policy description. |
| **Domain join configuration** | Yes |  |  |
| **Image ID** | Yes | String | This is the image ID you want to use for provisioning Cloud PCs. |
| **Image display name** | Yes | String | The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. Only letters (A-Z, a-z), numbers (0-9), and special characters (-,\_,.) are allowed for this property. The property value can't begin or end with an underscore. |
| **Image type** | Yes | String | Custom or Gallery. |
| **Provisioning type** | Yes | String | Shared or dedicated. |
| **Windows setting/locale** | Yes | String | Provide the language/locale you’d like to use. Windows 365 provides over 30 such languages/region pairs. |

You can also add other fields from Graph under Advanced parameters.

**Returns**

The outputs of this operation are dynamic.

### Assign a provisioning policy to a group

**Operation ID:** AssignAProvisioningPolicyToAGroupV1

This action allows you to assign a group to a provisioning policy.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Provisioning policy ID** | Yes | String | This is the provisioning policy ID that you would like to assign a group to. |
| **Assignments - ID** |  |  |  |
| **Assignments – Target Group ID** | Yes | String | User group from Entra ID. |

**Returns**

The outputs of this operation are dynamic.

### Update a provisioning policy

**Operation ID:** UpdateAProvisioningPolicyV1

This action allows you to update a provisioning policy.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Provisioning policy ID** | Yes | String | This is the provisioning policy ID of the provisioning policy you want to update. |
| **Description** | No | String | This is what the provisioning policy description will be updated to. |

You can also add other fields from Graph under Advanced parameters.

**Returns**

The outputs of this operation are dynamic.

### Get a provisioning policy

**Operation ID:** GetAProvisioningPolicyV1

This action allows you to get the details of a provisioning policy.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Provisioning policy ID** | Yes | String | The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. |
| **$select** | No | String | $select allows you to choose which properties are returned from Graph. |
| **$expand** | No | String | $expand allows you to return related resources from Graph. |

You can also add other fields from Graph under Advanced parameters.

**Returns**

The outputs of this operation are dynamic.

### Start a remote action

**Operation ID:** RemoteActions

This action allows you to start a remote action on a Cloud PC.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Cloud PC ID** | Yes | String | This allows you to specify which Cloud PC ID you want to target with a remote action. |
| **Remote action** | Yes | String | This allows you to choose when remote action you want to take on a Cloud PC. |
| **Remote action – snapshot ID** | No | String | If you’re choosing to restore a Cloud PC, you must also provide a snapshot ID. |
| **Remote action – Display name** | No | String | If you’re choosing to rename a Cloud PC, you must also provide a display name. |

**Returns**

If successful, this returns a 204 No Content response code.

### Send a Microsoft Graph HTTP request

**Operation ID:** HttpRequest

This action allows you to call Graph directly and customize the call.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **URI** | Yes | String | This allows you to specify which URI to call, for example: `https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/auditEvents` |
| **Method** | Yes | String | This allows you to define the call method. |

You can also add other fields (headers, body, etc.) under Advanced parameters.

**Returns**

The outputs of this operation are dynamic.

## Triggers:

All of the scenarios are part of one trigger, which is selectable in the trigger body itself.

| When a remote action on a Cloud PC is triggered | Allows you to trigger a flow when a remote action is triggered. |
| --- | --- |
| When a remote action on a Cloud PC completes | Allows you to trigger a flow when a remote action on a Cloud PC completes. |
| When a provisioning policy is updated | Allows you to trigger a flow when a provisioning policy is updated |
| When a new provisioning policy is created | Allows you to start a flow when a provisioning policy is created. |
| When a Cloud PC is created | This trigger allows you to start a flow when a Cloud PC is created. |

### When a provisioning policy or Cloud PC is updated

**Operation ID:** Webhook

This trigger fires when a provisioning policy or Cloud PC is updated.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Scenario** | Yes | Dropdown | You can choose between the supported scenarios:<br>1. When a Cloud PC is created<br>2. When a new provisioning policy is created<br>3. When a provisioning policy is updated<br>4. When a remote action on a Cloud PC completes<br>5. When a remote action on a Cloud PC is triggered |

**Returns**

The outputs of this operation are dynamic.

## 9/15 doc updates:

1. Add “deprecated” to title of “**When a provisioning policy or Cloud PC is updated (deprecated)” trigger**
2. Add underneath its section: “This trigger can continue to be used for existing flows, but there will be no new updates to it in the future. We recommend using the new triggers.”
3. Add new docs for new triggers as follows:

### When a new provisioning policy is created

**Operation ID:** WebhookProvisioningPolicyCreated

**Parameters:**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Filter provisioning policy name** | No | String | This allows you to set filters if you want to trigger the flow based on a policy name pattern. For example, if your organization uses provisioning policy name templates and you want to trigger your flow based off of that, you can specify the template here. |
| **Filter provisioning policy ID** | No | String | This allows you to select a single or multiple specific policy IDs on which to trigger this flow. |
| **Filter provisioning type** | No | String | This allows you to select a single or multiple specific provisioning types on which to trigger this flow. For example, you may want to trigger a flow just for Windows 365 Enterprise provisioning policies. |

**Returns**

The outputs of this operation are dynamic.

### When a Cloud PC is created

**Operation ID:** WebhookCloudPcProvisioned

This trigger allows you to trigger a flow based on when a Cloud PC is created.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Filter provisioning type** | No | String | This allows you to specify which Windows 365 edition triggers this flow. You can specify multiple types in the filter in an “OR” relationship. |

**Returns**

The outputs of this operation are dynamic.

### When a provisioning policy is updated

**Operation ID:** WebhookProvisioningPolicyUpdated

This trigger allows you to trigger a flow based on when a provisioning policy is updated.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Filter provisioning policy name** | No | String | This allows you to select a single or multiple specific policy names on which to trigger this flow. |
| **Filter provisioning policy ID** | No | String | This allows you to select a single or multiple specific policy IDs on which to trigger this flow. |
| **Filter provisioning type** | No | String | This allows you to select a single or multiple specific provisioning types on which to trigger this flow. For example, you may want to trigger a flow just for Windows 365 Enterprise provisioning policies. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| **provisioningPolicyId** | String | The provisioning policy ID that was updated. Consists of 32 characters in a GUID format. |
| **provisioningPolicyName** | String | The provisioning policy name that was updated. |

### When a remote action on a Cloud PC is triggered

**Operation ID:** WebhookCloudPcRemoteActionTriggered

This trigger allows you to trigger a flow based on when a remote action on a Cloud PC is triggered.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Filter provisioning type** | No | String | This allows you to select a single or multiple specific provisioning types on which to trigger this flow. For example, you may want to trigger a remote action flow just for Cloud PCs that are related to Windows 365 Enterprise provisioning policies. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| **CloudPcId** | String | The Cloud PC ID that had its remote action complete. |
| **provisioningType** | String | The provisioning type, which shows the Windows 365 Cloud PC edition. |
| **actionType** | String | The type of remote action, for example a restart. |

### When a remote action on a Cloud PC completes

**Operation ID:** Webhook.CloudPC.ActionCompleted

This trigger allows you to trigger a flow based on when a remote action on a Cloud PC completes.

**Parameters**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **Filter provisioning type** | No | String | This allows you to select a single or multiple specific provisioning types on which to trigger this flow. For example, you may want to trigger a remote action flow just for Cloud PCs that are related to Windows 365 Enterprise provisioning policies. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| **CloudPcId** | String | The Cloud PC ID that had its remote action complete. |
| **provisioningType** | String | The provisioning type, which shows the Windows 365 Cloud PC edition. |
| **actionType** | String | The type of remote action, for example a restart. |

## Throttling Limits

| Name | Calls | Renewal Period |
| --- | --- | --- |
| API calls per connection | 100 | 60 seconds |

## Actions

| Assign a provisioning policy to a group | Assign a provisioning policy to a group. |
| --- | --- |
| Create a provisioning policy | Creates a provisioning policy. |
| Delete a provisioning policy | Deletes a provisioning policy. |
| Get a Cloud PC | Gets a Cloud PC |
| Get a provisioning policy | Gets a specific provisioning policy. |
| Get provisioning policies | Gets a list of provisioning policies. |
| List Cloud PCs | List CloudPCs |
| Send a Microsoft Graph HTTP request (Preview) | Construct a Microsoft Graph REST API request |
| Start a remote action | Start a remote action on a Cloud PC. |
| Update a provisioning policy | Updates a provisioning policy. |

### Assign a provisioning policy to a group

- Operation ID:
    - AssignAProvisioningPolicyToAGroupV1

Assign a provisioning policy to a group.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy ID | id | True | string | id |
| Provisioning Policy ID | id |  | string | This is the provisioning policy ID that you would like to assign a group to |
| Group ID | groupId | True | string | groupId |
| servicePlanId | servicePlanId |  | string | Target ServicePlan ID |

#### Returns

### Create a provisioning policy

- Operation ID:
    - CreateAProvisioningPolicyV1

Creates a provisioning policy.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Name | displayName | True | string | displayName |
| Description | description | True | string | description |
| domainJoinType | domainJoinType |  | string |  |
| type | type |  | string |  |
| regionName | regionName |  | string |  |
| onPremisesConnectionId | onPremisesConnectionId |  | string |  |
| regionGroup | regionGroup |  | string |  |
| Other Fields | otherFields |  | object | Other fields |
| Enable single sign-on | enableSingleSignOn |  | boolean | enableSingleSignOn |
| Image ID | imageId | True | string | imageId |
| Image display name | imageDisplayName | True | string | imageDisplayName |
| Image type | imageType | True | string | imageType |
| Provisioning type | provisioningType | True | string | provisioningType |
| Locale | locale | True | string | locale |
| Managed Type | managedType |  | string | managedType |
| Profile | profile |  | string | profile |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
| id | id | string | id |
| Display name | displayName | string | The provisioning policy display name. |
| Description | description | string | The provisioning policy description. |
| Image ID | imageId | string | The ID of the operating system image you want to provision on Cloud PCs. |
| Image display name | imageDisplayName | string | The display name for the OS image you’re provisioning. |
| Image type | imageType | string | The type of OS image (custom or gallery) you want to provision on Cloud PCs. |
| Enable single sign-on | enableSingleSignOn | boolean | Specifies whether the provisioning policy has enabled SSO for Cloud PCs. |
| Cloud PC naming template | cloudPcNamingTemplate | string | The template used to name Cloud PCs provisioned using this policy. |
| Provisioning type | provisioningType | string | Specifies the type of license used when provisioning Cloud PCs using this policy. |
| managedBy | managedBy | string | managedBy |
| scopeIds | scopeIds | array of | scopeIds |
| Autopatch settings | autopatch | string | Indicates the Windows Autopatch settings for Cloud PCs using this provisioning policy. |
| autopilotConfiguration | autopilotConfiguration | string | autopilotConfiguration |
| domainJoinConfigurations | domainJoinConfigurations | array of object | domainJoinConfigurations |
| domainJoinType | domainJoinConfigurations.domainJoinType | string | domainJoinType |
| type | domainJoinConfigurations.type | string | type |
| regionName | domainJoinConfigurations.regionName | string | regionName |
| onPremisesConnectionId | domainJoinConfigurations.onPremisesConnectionId | string | onPremisesConnectionId |
| regionGroup | domainJoinConfigurations.regionGroup | string | regionGroup |
| managedType | microsoftManagedDesktop.managedType | string | managedType |
| type | microsoftManagedDesktop.type | string | type |
| profile | microsoftManagedDesktop.profile | string | profile |
| locale | windowsSetting.locale | string | locale |
| language | windowsSettings.language | string | language |

### Delete a provisioning policy

- Operation ID:
    - DeleteAProvisioningPolicyV1

Deletes a provisioning policy.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy ID | id | True | string | id |

#### Returns

### Get a Cloud PC

- Operation ID:
    - GetACloudPCObject

Gets a Cloud PC

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Cloud PC ID | cloudPcId | True | string | The unique identifier of the Cloud PC. |
| Select | $select |  | string | Select properties to be returned. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
| ID | id | string | The unique identifier of the customer-facing Cloud PC entity that consists of 32 characters in a GUID format. |
| Entra device ID | aadDeviceId | string | The Microsoft Entra device ID for the Cloud PC, also known as the Azure Active Directory (Azure AD) device ID, that consists of 32 characters in a GUID format. Generated on a VM joined to Microsoft Entra ID. Read-only. |
| Display name | displayName | string | The display name for the Cloud PC. Maximum length is 64 characters. Read-only. |
| Image display name | imageDisplayName | string | The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. |
| Provisioning policy ID | provisioningPolicyId | string | The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. |
| Provisioning policy name | provisioningPolicyName | string | The provisioning policy that applied during the provisioning of Cloud PCs. |
| On-premises connection name | onPremisesConnectionName | string | The Azure network connection that applied during the provisioning of Cloud PCs. |
| Service plan ID | servicePlanId | string | The service plan ID for the Cloud PC that consists of 32 characters in a GUID format. |
| Service plan name | servicePlanName | string | The service plan name for the customer-acing Cloud PC entity. |
| status | status | string | status |
| User principal name | userPrincipalName | string | The user principal name (UPN) of the user assigned to the Cloud PC. |
| Last modified date/time | lastModifiedDateTime | string | The last modified date and time of the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. |
| Managed device ID | managedDeviceId | string | The Intune enrolled device ID for the Cloud PC that consists of 32 characters in a GUID format. |
| Managed device name | managedDeviceName | string | The Intune enrolled device name for the Cloud PC. |
| Grace period end date/time | gracePeriodEndDateTime | string | The date and time when the grace period ends and reprovisioning or deprovisioning happen. |
| Disk encryption state | diskEncryptionState | string | Disk encryption state |
| Provisioning type | provisioningType | string | The type of licenses to be used when provisioning Cloud PCs using this policy. |
| Allotment display name | allotmentDisplayName | string | Allotment display name |
| Status detail | statusDetail | string | Status detail |
| Enable single sign-on | connectionSetting.enableSingleSignOn | boolean | Enable single sign-on |
| partnerAgentInstallResults | partnerAgentInstallResults | array of string | partnerAgentInstallResults |

### Get a provisioning policy

- Operation ID:
    - GetAProvisioningPolicyV1

Gets a specific provisioning policy.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy ID | id | True | string | id |
| Select | $select |  | string | Returns default properties if unspecified; first option returns all properties. |
| Expand | $expand |  | string | Expands related entities inline. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
| assignments | assignments | array of object |  |
| items | assignments | object |  |
| Description | description | string | The provisioning policy description. |
| Display name | displayName | string | The provisioning policy display name. |
| Domain join configurations | domainJoinConfigurations | array of object | Specifies a list ordered by priority on how Cloud PCs join Microsoft Entra ID. |
| onPremisesConnectionId | domainJoinConfigurations.onPremisesConnectionId | string | onPremisesConnectionId |
| type | domainJoinConfigurations.type | string | type |
| managedType | microsoftManagedDesktop.managedType | string | managedType |
| profile | microsoftManagedDesktop.profile | string | profile |
| autopatchGroupId | autopatch.autopatchGroupId | string | autopatchGroupId |
| devicePreparationProfileId | autopilotConfiguration.devicePreparationProfileId | string | devicePreparationProfileId |
| applicationTimeoutInMinutes | autopilotConfiguration.applicationTimeoutInMinutes | integer | applicationTimeoutInMinutes |
| onFailureDeviceAccessDenied | autopilotConfiguration.onFailureDeviceAccessDenied | boolean | onFailureDeviceAccessDenied |
| Enable single sign-on | enableSingleSignOn | boolean | Specifies whether the provisioning policy has enabled SSO for Cloud PCs. |
| Id | id | string | id |
| Image display name | imageDisplayName | string | The display name for the OS image you’re provisioning. |
| Image ID | imageId | string | The ID of the operating system image you want to provision on Cloud PCs. |
| Image type | imageType | string | The type of OS image (custom or gallery) you want to provision on Cloud PCs. |
| locale | windowsSetting.locale | string | locale |
| managedBy | managedBy | string | managedBy |
| Provisioning type | provisioningType | string | Specifies the type of license used when provisioning Cloud PCs using this policy. |

### Get provisioning policies

- Operation ID:
    - GetProvisioningPoliciesV1

Gets a list of provisioning policies.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Select | $select |  | string | Returns default properties if unspecified; first option returns all properties. |
| Filter | $filter |  | string | Filter items by property values. |
| Expand | $expand |  | string | Expands related entities inline. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
| value | value | array of object | value |
| assignments | value.assignments | array of object |  |
| items | value.assignments | object |  |
| Description | value.description | string | The provisioning policy description. |
| Display name | value.displayName | string | The provisioning policy display name. |
| Domain join configurations | value.domainJoinConfigurations | array of object | Specifies a list ordered by priority on how Cloud PCs join Microsoft Entra ID. |
| onPremisesConnectionId | value.domainJoinConfigurations.onPremisesConnectionId | string | onPremisesConnectionId |
| type | value.domainJoinConfigurations.type | string | type |
| managedType | value.microsoftManagedDesktop.managedType | string | managedType |
| profile | value.microsoftManagedDesktop.profile | string | profile |
| autopatchGroupId | value.autopatch.autopatchGroupId | string | autopatchGroupId |
| devicePreparationProfileId | value.autopilotConfiguration.devicePreparationProfileId | string | devicePreparationProfileId |
| applicationTimeoutInMinutes | value.autopilotConfiguration.applicationTimeoutInMinutes | integer | applicationTimeoutInMinutes |
| onFailureDeviceAccessDenied | value.autopilotConfiguration.onFailureDeviceAccessDenied | boolean | onFailureDeviceAccessDenied |
| Enable single sign-on | value.enableSingleSignOn | boolean | Specifies whether the provisioning policy has enabled SSO for Cloud PCs. |
| Id | value.id | string | id |
| Image display name | value.imageDisplayName | string | The display name for the OS image you’re provisioning. |
| Image ID | value.imageId | string | The ID of the operating system image you want to provision on Cloud PCs. |
| Image type | value.imageType | string | The type of OS image (custom or gallery) you want to provision on Cloud PCs. |
| locale | value.windowsSetting.locale | string | locale |
| managedBy | value.managedBy | string | managedBy |
| Provisioning type | value.provisioningType | string | Specifies the type of license used when provisioning Cloud PCs using this policy. |

### List Cloud PCs

- Operation ID:
    - ListCloudPCs

List CloudPCs

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Select | $select |  | string | Select properties to be returned. |
| Filter | $filter |  | string | Ex. provisioningPolicyName eq 'XXX' and userPrincipalName eq 'XXX' |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
| ID | id | string | The unique identifier of the customer-facing Cloud PC entity that consists of 32 characters in a GUID format. |
| Entra device ID | aadDeviceId | string | The Microsoft Entra device ID for the Cloud PC, also known as the Azure Active Directory (Azure AD) device ID, that consists of 32 characters in a GUID format. Generated on a VM joined to Microsoft Entra ID. Read-only. |
| Display name | displayName | string | The display name for the Cloud PC. Maximum length is 64 characters. Read-only. |
| Image display name | imageDisplayName | string | The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. |
| Provisioning policy ID | provisioningPolicyId | string | The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. |
| Provisioning policy name | provisioningPolicyName | string | The provisioning policy that applied during the provisioning of Cloud PCs. |
| On-premises connection name | onPremisesConnectionName | string | The Azure network connection that applied during the provisioning of Cloud PCs. |
| Service plan ID | servicePlanId | string | The service plan ID for the Cloud PC that consists of 32 characters in a GUID format. |
| Service plan name | servicePlanName | string | The service plan name for the customer-acing Cloud PC entity. |
| status | status | string | status |
| User principal name | userPrincipalName | string | The user principal name (UPN) of the user assigned to the Cloud PC. |
| Last modified date/time | lastModifiedDateTime | string | The last modified date and time of the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. |
| Managed device ID | managedDeviceId | string | The Intune enrolled device ID for the Cloud PC that consists of 32 characters in a GUID format. |
| Managed device name | managedDeviceName | string | The Intune enrolled device name for the Cloud PC. |
| Grace period end date/time | gracePeriodEndDateTime | string | The date and time when the grace period ends and reprovisioning or deprovisioning happen. |
| Disk encryption state | diskEncryptionState | string | Disk encryption state |
| Provisioning type | provisioningType | string | The type of licenses to be used when provisioning Cloud PCs using this policy. |
| Allotment display name | allotmentDisplayName | string | Allotment display name |
| Status detail | statusDetail | string | Status detail |
| Enable single sign-on | connectionSetting.enableSingleSignOn | boolean | Specifies whether the provisioning policy has enabled SSO for Cloud PCs. |
| partnerAgentInstallResults | partnerAgentInstallResults | array of string | partnerAgentInstallResults |

### Send a Microsoft Graph HTTP request (Preview)

- Operation ID:
    - HttpRequest

Construct a Microsoft Graph REST API request

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| URI | Uri | True | string | The full or relative URI. Example: `https://graph.microsoft.com/{version}/{resource}` |
| Method | Method | True | string | The HTTP method (default is GET) |
| Body | Body |  | binary | The request body content |
| Content-Type | ContentType |  | string | The content-type header for the body (default is application/json) |
| CustomHeader1 | CustomHeader1 |  | string | Custom header 1. Specify in format: header-name: header-value |
| CustomHeader2 | CustomHeader2 |  | string | Custom header 2. Specify in format: header-name: header-value |
| CustomHeader3 | CustomHeader3 |  | string | Custom header 3. Specify in format: header-name: header-value |
| CustomHeader4 | CustomHeader4 |  | string | Custom header 4. Specify in format: header-name: header-value |
| CustomHeader5 | CustomHeader5 |  | string | Custom header 5. Specify in format: header-name: header-value |

#### Returns

- response
    - ObjectWithoutType

### Start a remote action

- Operation ID:
    - RemoteActions

Start a remote action on a Cloud PC.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Cloud PC ID | cloudPcId | True | string | The unique identifier of the Cloud PC. |
| Remote action | remoteAction | True | string | The remote action to perform on the Cloud PC. |
| Cloud PC snapshot Id | cloudPcSnapshotId |  | string | Required for restore |
| Display name | displayName |  | string | Required for rename |

#### Returns

### Update a provisioning policy

- Operation ID:
    - UpdateAProvisioningPolicyV1

Updates a provisioning policy.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy ID | id | True | string | id |
| Group ID | autopatchGroupId |  | string | autopatchGroupId |
| Device preparation profile ID | devicePreparationProfileId |  | string | devicePreparationProfileId |
| Application timeout in minutes | applicationTimeoutInMinutes |  | integer | applicationTimeoutInMinutes |
| On failure device access denied | onFailureDeviceAccessDenied |  | boolean | onFailureDeviceAccessDenied |
| Description | description |  | string | description |
| Display name | displayName |  | string | displayName |
| Domain join type | domainJoinType |  | string | domainJoinType |
| On premises connection ID | onPremisesConnectionId |  | string | onPremisesConnectionId |
| Region group | regionGroup |  | string | regionGroup |
| Region name | regionName |  | string | regionName |
| Type | type |  | string | type |
| Enable single sign on | enableSingleSignOn |  | boolean | enableSingleSignOn |
| Image display name | imageDisplayName |  | string | imageDisplayName |
| Image ID | imageId |  | string | imageId |
| Image type | imageType |  | string | imageType |
| Managed type | managedType |  | string | managedType |
| Profile | profile |  | string | profile |
| Locale | locale |  | string | locale |
| Other Fields | otherFields |  | object | Other fields |

#### Returns

## Triggers

| When a Cloud PC is created | This trigger allows you to start a flow when a Cloud PC is created. |
| --- | --- |
| When a new provisioning policy is created | Allows you to start a flow when a provisioning policy is created. |
| When a provisioning policy is updated | Allows you to trigger a flow when a provisioning policy is updated |
| When a provisioning policy or Cloud PC is updated (deprecated) [DEPRECATED] | When a provisioning policy or Cloud PC is updated (deprecated) |
| When a remote action on a Cloud PC completes | Allows you to trigger a flow when a remote action on a Cloud PC completes. |
| When a remote action on a Cloud PC is triggered | Allows you to trigger a flow when a remote action on a Cloud PC completes. |

### When a Cloud PC is created

- Operation ID:
    - WebhookCloudPcProvisioned

This trigger allows you to start a flow when a Cloud PC is created.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning type | provisioningTypeNames |  | array of string | Select one or more provisioning types. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
|  |  | array of object |  |
| tenantId | data.tenantId | string | tenantId |
| category | data.category | string | category |
| action | data.action | string | action |
| cloudPCId | data.data.cloudPCId | string | cloudPCId |
| policyId | data.data.policyId | string | policyId |

### When a new provisioning policy is created

- Operation ID:
    - WebhookProvisioningPolicyCreated

Allows you to start a flow when a provisioning policy is created.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy name | provisioningPolicyNames |  | array of string | Select a provisioning policy to monitor for updates. |
| Provisioning policy ID | provisioningPolicyIds |  | array of string | Enter one or more provisioning policy IDs. |
| Provisioning type | provisioningTypeNames |  | array of string | Select one or more provisioning types. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
|  |  | array of object |  |
| tenantId | data.tenantId | string | tenantId |
| category | data.category | string | category |
| action | data.action | string | action |
| cloudPCId | data.data.cloudPCId | string | cloudPCId |
| policyId | data.data.policyId | string | policyId |

### When a provisioning policy is updated

- Operation ID:
    - WebhookProvisioningPolicyUpdated

Allows you to trigger a flow when a provisioning policy is updated

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning policy name | provisioningPolicyNames |  | array of string | Select a provisioning policy to monitor for updates. |
| Provisioning policy ID | provisioningPolicyIds |  | array of string | Enter one or more provisioning policy IDs. |
| Provisioning type | provisioningTypeNames |  | array of string | Select one or more provisioning types. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
|  |  | array of object |  |
| tenantId | data.tenantId | string | tenantId |
| category | data.category | string | category |
| action | data.action | string | action |
| cloudPCId | data.data.cloudPCId | string | cloudPCId |
| policyId | data.data.policyId | string | policyId |

### When a provisioning policy or Cloud PC is updated (deprecated) [DEPRECATED]

- Operation ID:
    - Webhook

When a provisioning policy or Cloud PC is updated (deprecated)

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| scenario | scenario | True | string | scenario |

### When a remote action on a Cloud PC completes

- Operation ID:
    - WebhookCloudPcRemoteActionCompleted

Allows you to trigger a flow when a remote action on a Cloud PC completes.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning type | provisioningTypeNames |  | array of string | Select one or more provisioning types. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
|  |  | array of object |  |
| tenantId | data.tenantId | string | tenantId |
| category | data.category | string | category |
| action | data.action | string | action |
| cloudPCId | data.data.cloudPCId | string | cloudPCId |
| policyId | data.data.policyId | string | policyId |

### When a remote action on a Cloud PC is triggered

- Operation ID:
    - WebhookCloudPcRemoteActionTriggered

Allows you to trigger a flow when a remote action on a Cloud PC completes.

#### Parameters

| Name | Key | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Provisioning type | provisioningTypeNames |  | array of string | Select one or more provisioning types. |

#### Returns

| Name | Path | Type | Description |
| --- | --- | --- | --- |
|  |  | array of object |  |
| tenantId | data.tenantId | string | tenantId |
| category | data.category | string | category |
| action | data.action | string | action |
| cloudPCId | data.data.cloudPCId | string | cloudPCId |
| policyId | data.data.policyId | string | policyId |

## Definitions

### ObjectWithoutType