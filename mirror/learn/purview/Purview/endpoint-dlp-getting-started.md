---
layout: Conceptual
title: Get started with endpoint data loss prevention | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-20T00:00:00.0000000Z
audience: ITPro
ms.topic: get-started
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MET150
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1023
description: Set up Endpoint data loss prevention to monitor file activities and implement protective actions for those files to endpoints.
ai-usage: ai-assisted
locale: en-us
document_id: 9c73a306-88b0-c1c3-8427-b1e5966b3c02
document_version_independent_id: 9c73a306-88b0-c1c3-8427-b1e5966b3c02
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-getting-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-getting-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-getting-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 84c3b14b-52c5-3d2c-4332-834319f69851
---

# Get started with endpoint data loss prevention | Microsoft Learn

Endpoint data loss prevention (Endpoint DLP) is part of the Microsoft Purview Data Loss Prevention (DLP) suite of features you can use to discover and protect sensitive items across Microsoft 365 services. For more information about all of Microsoft's DLP offerings, see [Learn about data loss prevention](dlp-learn-about-dlp). To learn more about Endpoint DLP, see [Learn about Endpoint data loss prevention](endpoint-dlp-learn-about)

Microsoft Endpoint DLP allows you to monitor [onboarded Windows 10, and Windows 11](device-onboarding-overview) and [onboarded macOS devices](device-onboarding-macos-overview) running any of the three latest released versions. Once a device is onboarded, DLP detects when sensitive items are used and shared. This gives you the visibility and control you need to ensure that they're used and protected properly, and to help prevent risky behavior that might compromise them.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you begin

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

Important

Endpoint DLP policy targeting can be configured using a combination of users and devices. If a policy is scoped to devices where the signed-in users do not meet the [required criteria](device-onboarding-overview#before-you-begin), ensure those users or devices or both are explicitly excluded from the policy. Failure to do so may lead to unintended policy enforcement behavior.

### Configure proxy on the Windows 10 or Windows 11 device

If you're onboarding Windows 10 or Windows 11 devices, check to make sure that the device can communicate with the cloud DLP service. For more information, see, [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp).

## Windows 10 and Windows 11 Onboarding procedures

For a general introduction to onboarding Windows devices, see:

- [Onboard Windows devices into Microsoft 365 overview](device-onboarding-overview#onboard-windows-devices-into-microsoft-365-overview)

For specific guidance to onboarding Windows devices, see:

| Article | Description |
| --- | --- |
| [Onboard Windows 10 or 11 devices using Group Policy](device-onboarding-gp) | Use Group Policy to deploy the configuration package on devices. |
| [Onboard Windows 10 or 11 devices using Microsoft Endpoint Configuration Manager](device-onboarding-sccm) | You can use either use Microsoft Endpoint Configuration Manager (current branch) version 1606 or Microsoft Endpoint Configuration Manager (current branch) version 1602 or earlier to deploy the configuration package on devices. |
| [Onboard Windows 10 or 11 devices using Microsoft Intune](device-onboarding-mdm) | Use Microsoft Intune to deploy the configuration package on device. |
| [Onboard Windows 10 or 11 devices using a local script](device-onboarding-script) | Learn how to use the local script to deploy the configuration package on endpoints. |
| [Onboard non-persistent virtual desktop infrastructure (VDI) devices](device-onboarding-vdi) | Learn how to use the configuration package to configure VDI devices. |

### Endpoint DLP support for virtualized environments

You can onboard virtual machines as monitored devices in Microsoft Purview portal. There's no change to the onboarding procedures listed above.

The table that follows lists the virtual operating systems that are supported by virtualization environments.

| Virtualizationplatform | Windows 10 | Windows 11 | Windows Server 2019 | Windows Server 202221H2, 22H2, Data Center |
| --- | --- | --- | --- | --- |
| Azure virtual desktop (AVD) | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | Single session and Multi session supported. | Supported |
| Windows 365 | - Supported for 21H2, 22H2 | - Supported for 21H2, 22H2 | Not applicable | Not applicable |
| Citrix Virtual Apps and Desktops 7 (2209 and higher) | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | Supported | Supported |
| Amazon workspaces | - Single session supported for 21H2, 22H2 | Not applicable | - Windows 10 powered by Windows Server 2019 | Not applicable |
| Hyper-V | - Single session supported for 21H2, 22H2<br>- Multi session with Hybrid AD join supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session with Hybrid AD join supported for 21H2, 22H2 | Supported with Hybrid AD join | Supported with Hybrid AD join |

#### Known issues

1. You can't monitor **Copy to Clipboard** and **Enforcing Endpoint DLP** on Azure Virtual Desktop environments via browsers. However, the same egress operation will be monitored by **Endpoint DLP for actions via Remote Desktop Session (RDP)**.
2. Citrix XenApp doesn't support access by restricted app monitoring.

#### Limitations

1. Handling of USBs in virtualized environments: USB storage devices are treated as network shares. You need to include the **Copy to network share** activity to monitor **Copy to a USB device**. All activity explorer events for virtual devices and incident alerts show the **Copy to a network share** activity for all copy to USB events.

## macOS onboarding procedures

For a general introduction to onboarding macOS devices, see:

- [Onboard macOS devices into Microsoft Purview](device-onboarding-macos-overview)

For specific guidance to onboarding macOS devices, see:

Important

There are important permission changes for Microsoft Purview Endpoint DLP in macOS 27. If you're onboarding or upgrading devices that run macOS 27, review the updated guidance before deployment. For more information, see [Microsoft Purview Endpoint DLP on macOS 27 (Preview)](endpoint-dlp-macos-27-changes).

| Article | Description |
| --- | --- |
| [Intune](device-onboarding-offboarding-macos-intune) | For macOS devices that are managed through Intune |
| [Intune for Microsoft Defender for Endpoint customers](device-onboarding-offboarding-macos-intune-mde) | For macOS devices that are managed through Intune and that have Microsoft Defender for Endpoint (MDE) deployed to them |
| [JAMF Pro)](device-onboarding-offboarding-macos-jamfpro) | For macOS devices that are managed through JAMF Pro |
| [JAMF Pro for Microsoft Defender for Endpoint customers)](device-onboarding-offboarding-macos-jamfpro-mde) | For macOS devices that are managed through JAMF Pro and that have Microsoft Defender for Endpoint (MDE) deployed to them |

Once a device is onboarded, it should be visible in the devices list, and should start reporting audit activity to Activity explorer.