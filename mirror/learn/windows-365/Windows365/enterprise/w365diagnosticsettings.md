---
layout: Conceptual
title: Send Windows 365 log data to Azure Storage, Event Hub, or Log Analytics | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/w365diagnosticsettings
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: This article provides documentation on how to send Windows 365 log data from Monitor Cloud PCs to Azure Storage, Event Hub and Log Analytics.
author: rachellelcheung
ms.author: racheun
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.topic: how-to
ms.date: 2026-11-02T00:00:00.0000000Z
locale: en-us
document_id: 64316c08-c89c-a62c-a022-74f9d75a4b68
document_version_independent_id: 64316c08-c89c-a62c-a022-74f9d75a4b68
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/w365diagnosticsettings.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/w365diagnosticsettings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/w365diagnosticsettings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/f0234678-3067-4edc-abf7-8142d54bb7d2
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/b0f4f6b9-28ed-4892-be4e-517310289c68
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
platformId: 31216eac-53bf-e70a-d58e-4a39c157c9e3
---

# Send Windows 365 log data to Azure Storage, Event Hub, or Log Analytics | Microsoft Learn

Important

Windows 365 log data to Azure Storage, Event Hub, or Log Analytics is in public preview. Preview features are tagged with (preview) in the admin user interface and might have restricted or limited functionality. These features are subject to change before general availability (GA) and are fully supported by Microsoft. Preview features are considered unfinished, might not be suitable for production workloads, and should be used with caution.

Microsoft Intune includes [built-in logs](/en-us/intune/governance/integrate-azure-monitor) that provide information about your environment. Specifically for Windows 365, the following logs are available:

- **Windows 365 Audit Logs** show administrative activities and changes made to Windows 365 resources, including who performed each action and when it occurred.
- **Windows 365 Connection Logs** show Cloud PC connection attempts and their outcomes, including the user, device, client platform, session host, gateway, transport type, and IP address.

These logs can also be sent to Azure Monitor services, including storage accounts, Event Hubs, and Log Analytics. Specifically, you can:

- Archive Intune logs to an Azure Storage account to keep the data, or archive for a set time.
- Stream Intune logs to an Azure Event Hubs for analytics using popular Security Information and Event Management (SIEM) tools, such as Splunk and QRadar.
- Integrate Intune logs with your own custom log solutions by streaming them to Event Hubs.
- Send Intune logs to Log Analytics to enable rich visualizations, monitoring, and alerting on the connected data.

These features are part of the **Diagnostics Settings** in Intune.

This article shows you how to use **Diagnostics Settings** to send log data to different services, and answers some common questions. Once you enable this feature, your logs are routed to the Azure Monitor service you choose.

Note

These logs use schemas that may change.

## Prerequisites

In addition to having a Windows 365 subscription and access to Diagnostics settings, you will need the [prerequisites here](/en-us/intune/governance/integrate-azure-monitor).

## Using logs

Follow the instructions below to use the logs:

- [Send logs to Azure Monitor](/en-us/intune/governance/integrate-azure-monitor)
- [Use audit logs throughout Intune](/en-us/intune/governance/integrate-azure-monitor)

### Windows 365 Audit Logs

| Name of data collected | Description | Sample Value |
| --- | --- | --- |
| AuditEventId | Audit event identifier. | abc123-def456-ghi789 |
| auditDisplayName | Audit event display name. | CloudPcOnPremisesConnection |
| componentName | Component/controller that emitted the event. Uses the supplied component name or caller source-file name. | CloudPcOnPremisesConnectionsController |
| actor | Caller identity/application associated with the audit event | { "type": "ItPro", ... } |
| activity | Legacy friendly activity field. | null |
| activityDateTime | UTC time when the audited activity was recorded by GraphApiAuditor. | 2025-01-28T05:21:03.909627Z |
| activityType | Generated operation/activity name. | Create CloudPCOnPremisesConnection |
| activityOperationType | Public operation classification. | Create |
| activityResult | Operation outcome. | Success |
| correlationId | Request/activity correlation identifier. | jkl123-mno456-pqr789 |
| resources | Resources affected by the operation. | [{ "resourceId": "stu-123-vwx-456-yz78", ... }] |
| category | Audit category. | CloudPC |
| actor.type | Caller type. | ItPro |
| actor.userPermissions | Effective app permissions or delegated scopes obtained from the token. | {"ReadWrite.All"} |
| actor.applicationId | Microsoft Entra application/client ID from the caller token. | adf123-ggd34-fgk4545 |
| actor.applicationDisplayName | The application display name. | CloudPCRunner3rdPartyApp |
| actor.userPrincipalName | Caller UPN. | cloudpcadmin@contoso.com |
| actor.servicePrincipalName | Service principal name. | null |
| actor.ipAddress | Caller IP | null |
| actor.userId | Caller Microsoft Entra object ID. | 340df-34fnkk3-dff4-32393fb9u |
| actor.userRoleScopeTags | Role scope tags associated with the caller. | [] |
| actor.remoteTenantId | Delegated partner tenant ID. | null(non-partner) |
| actor.remoteUserId | Delegated partner administrator object ID. | null(non-partner) |
| actor.userRoleScopeTags[].displayName | Role scope tag display name | "" |
| actor.userRoleScopeTags[].roleScopeTagId | Role scope tag ID | ScopeTagId |
| resources[].displayName | Resource display name. | Resource |
| resources[].modifiedProperties | Resource property snapshot/diff. Patch overloads can include old and new values. | [{ "displayName":"DisplayName", "oldValue":"OldName", "newValue":"NewName" }] |
| resources[].resourceType | CLR entity type name. | CloudPcOnPremisesConnection |
| resources[].resourceId | Target entity ID. | 323hih35-sd23g5-dffd33-dgdfg3535hife3 |
| resources[].modifiedProperties[].displayName | Exact modified property name/path. | DeviceManagementAPIVersion |
| resources[].modifiedProperties[].oldValue | Previous value. Normally present from changed fields in patch flows. | OldName(or null) |
| resources[].modifiedProperties[].newValue | New/current value. | NewName |

### Windows 365 Connection Logs

| Name of data collected | Description | Sample Value |
| --- | --- | --- |
| TimeGenerated | The timestamp (UTC) of the event. | 2026-02-25T12:20:07.0000000Z |
| TenantId | The Microsoft Entra (Azure AD) tenant identifier. | abc123-def456-ghi789 |
| CloudPCId | The unique identifier of the Cloud PC. | jkl123-mno456-pqr789 |
| ActivityId | The activity Id for correlating with network, error, and checkpoint data. | stu-123-vwx-456-yz789 |
| ManagedDeviceName | The name of the managed device. | CPC-contoso |
| UserPrincipalName | The user principal name of the user who initiated the connection. | cloudpc@contoso.com |
| State | The state of the connection. | Completed |
| ClientOS | The OS of the client that is connecting (if available). | Linux x86\_64 |
| PlatformName | The platform name of the client application. | Chrome |
| PlatformVersion | The version of the client platform. | 141.0.0.0 |
| SessionHostOSDescription | The OS SKU description of the machine where the user connection was orchestrated. | Windows 10 Enterprise |
| GatewayRegion | The region of the gateway for the server side user connection. | westus |
| TransportType | The type of transport used by the RDP connection: Shortpath, TURN, Websocket. | TCP Websocket |
| ResultType | The result type of the connection. | Success |
| CallerIPAddress | The IP address of the connecting endpoint. | 10.111.22.333 |
| SessionHostSxSStackVersion | The side-by-side (SxS) stack version of the session host. | 1.0.2222.3333 |
| SessionHostOSVersion | The OS version of the session host. | 10.1.22222.3333 |
| SessionHostIPAddress | The IP address of the session host. | 10.1.2.3 |

### Windows 365 Connection Error Logs

| Name of data collected | Description | Sample Value |
| --- | --- | --- |
| TimeGenerated | The timestamp (UTC) of the event. | 2026-02-26T06:40:36.0000000Z |
| TenantId | The Microsoft Entra (Azure AD) tenant identifier. | abc123-def456-ghi789 |
| ActivityId | The activity Id. | stu-123-vwx-456-yz789 |
| CodeSymbolic | The error code symbolic representation (if available). | ObjectFetchFailed |
| Message | The error message. | The user's network connection to their Cloud PC was unexpectedly interrupted. |
| ResultType | The result type of the operation. | In Progress |
| UserName | The user for whom the error happened. | cloudpcuser1 |
| Source | The source of the error. | Client |

### Windows 365 Network Logs

| Name of data collected | Description | Sample Value |
| --- | --- | --- |
| TimeGenerated | The timestamp (UTC) when the network event was generated. | 2026-02-26T06:23:02.0000000Z |
| TenantId | The Microsoft Entra (Azure AD) tenant identifier. | abc123-def456-ghi789 |
| CloudPCId | The unique identifier of the Cloud PC. | jkl123-mno456-pqr789 |
| ActivityId | The activity Id for correlating with connection data. | stu-123-vwx-456-yz789 |
| EstRoundTripTimeInMs | The average of estimated network round trip times (milliseconds) in the last evaluated connection time interval. | 259 |
| EstAvailableBandwidthKBps | The average of estimated network bandwidth (kilobyte per second) in the last evaluated connection time interval. | 10229 |