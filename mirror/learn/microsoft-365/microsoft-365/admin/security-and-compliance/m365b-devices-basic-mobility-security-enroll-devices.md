---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Enroll devices in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-enroll-devices?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: security
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
- basic-mobility-security
search.appverid:
- MET150
description: Before you can use Microsoft 365 services with your device, you might need to first enroll it in Basic Mobility and Security for Microsoft 365.
locale: en-us
document_id: 2bf00838-c5af-2155-90dd-84518a2b6e56
document_version_independent_id: 2bf00838-c5af-2155-90dd-84518a2b6e56
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-enroll-devices.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-enroll-devices
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-enroll-devices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7e943c2b-9f1e-d41e-e8eb-17a435af82da
---

# Enroll devices in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn

After an admin [sets up Basic Mobility and Security](m365b-devices-basic-mobility-security-set-up) and [configures policies](m365b-devices-basic-mobility-security-policies-configure), users need to enroll their [supported devices](m365b-devices-basic-mobility-security-overview#supported-device-platforms-in-basic-mobility-and-security) in Basic Mobility and Security to access Microsoft 365 company data using [supported apps](m365b-devices-basic-mobility-security-overview#apps-that-prompt-users-to-enroll-in-basic-mobility-and-security).

The rest of this article explains how users can enroll their supported devices in Basic Mobility and Security.

Important

Basic Mobility and Security is a mobile device management (MDM) solution, which means your Microsoft 365 organization controls the enrolled device, not just company data on the device. For example, admins can configure policies that require complex passwords, block access to specific features, and remotely wipe devices. For information about information that's visible to admins on enrolled devices, see [What information can my organization see when I enroll my device?](/en-us/intune/intune-service/user-help/what-info-can-your-company-see-when-you-enroll-your-device-in-intune).

## Enroll iOS/iPadOS devices in Basic Mobility and Security

Tip

You can't send and receive Microsoft 365 email until you complete this step.

1. In the Apple App Store, find and install the [Intune Company Portal app](https://apps.apple.com/us/app/intune-company-portal/id719171358) on the device.
2. Open the Company Portal app and sign in with the Microsoft 365 work or school account of the device user.

The rest of the instructions are described in [Microsoft Intune - iOS/iPadOS device enrollment with the Company Portal app](/en-us/intune/intune-service/user-help/enroll-your-device-in-intune-ios#device-enrollment-with-company-portal-app).

### Enroll Android devices in Basic Mobility and Security

Tip

You can't send and receive Microsoft 365 email until you complete this step.

1. In the Google Play Store, find and install the [Intune Company Portal app](https://play.google.com/store/apps/details?id=com.microsoft.windowsintune.companyportal) on the device.
2. Open the Company Portal app and sign in with the Microsoft 365 work or school account of the device user.

The rest of the instructions are described in [Microsoft Intune - Enroll Android devices with the Company Portal app](/en-us/intune/intune-service/user-help/enroll-device-android-company-portal#enroll-device).

### Enroll Windows devices in Basic Mobility and Security

1. In the Microsoft Store, find and install the [Intune Company Portal app](https://go.microsoft.com/fwlink/p/?linkid=2141417).
2. Open the Company Portal app and sign in with the Microsoft 365 work or school account of the device user.

To connect and configure your Windows phone or PC with the Company portal to Microsoft 365, see [Enroll Windows 10/11 devices in Intune](/en-us/intune/intune-service/user-help/enroll-windows-10-device).