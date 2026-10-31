---
layout: Conceptual
title: Onboard and offboard macOS devices into Purview solutions using Jamf Pro for Microsoft Defender for Endpoint customers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro-mde
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Learn how to onboard and offboard macOS devices into Microsoft Purview solutions using Jamf Pro for Microsoft Defender for Endpoint customers
locale: en-us
document_id: 67f74048-da00-ac3e-14d0-8e74bbaabe2b
document_version_independent_id: 67f74048-da00-ac3e-14d0-8e74bbaabe2b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-offboarding-macos-jamfpro-mde.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-offboarding-macos-jamfpro-mde
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-offboarding-macos-jamfpro-mde.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- Power
- Azure
- M365
platformId: 7b3e4721-b4df-5e8d-45ea-457a0a237875
---

# Onboard and offboard macOS devices into Purview solutions using Jamf Pro for Microsoft Defender for Endpoint customers | Microsoft Learn

You can use Jamf Pro to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure ***if you have*** deployed Microsoft Defender for Endpoint (MDE) to your macOS devices

**Applies to:**

- Customers who have MDE deployed to their macOS devices.
- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

## Before you begin

- Make sure your [macOS devices are managed through Jamf pro](https://www.jamf.com/resources/product-documentation/jamf-pro-installation-guide-for-mac/) and are associated with an identity (Microsoft Entra joined UPN) through Jamf Connect.
- OPTIONAL: Install the v95+ Edge browser on your macOS devices to have native Endpoint DLP support on Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using Jamf Pro

Onboarding a macOS device into Purview solutions is a multi-phase process.

1. Update the existing MDE Preference domain profile using the Jamf Pro console
2. Enable full-disk access
3. Enable accessibility access to Microsoft Purview data loss prevention
4. Check the macOS device

### Prerequisites

Download the following files:

| File | Description |
| --- | --- |
| [accessibility.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/profiles/accessibility.mobileconfig) | Accessibility |
| [fulldisk.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/profiles/fulldisk.mobileconfig) | Full disk access (FDA) |
| [schema.json](https://github.com/microsoft/mdatp-xplat/blob/master/macos/schema/schema.json) | MDE preference |

If any of these individual files are updated, you must download the updated bundled file and redeploy as described.

Tip

We recommend downloading the bundled [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) file, rather than the [individual](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles)*.mobileconfig* files. The bundled file includes the following required files:

- accessibility.mobileconfig
- fulldisk.mobileconfig
- netfilter.mobileconfig
- sysext.mobileconfig

If any of these files are updated, you need to either download the updated bundle, or download each updated file individually.

### Update the existing MDE Preference domain profile using the Jamf Pro console

For information about how to replace the *schema.json* file in the MDE deployment with the updated version, and configure the settings in the Jamf Pro console, refer to the [Jamf Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

### Enable full-disk access

To update the existing full disk access profile with the `fulldisk.mobileconfig` file, upload `fulldisk.mobileconfig` to Jamf. For more information, refer to [Set up the Microsoft Defender for Endpoint on macOS policies in Jamf Pro](/en-us/defender-endpoint/mac-jamfpro-policies).

### Enable accessibility access to Microsoft Purview data loss prevention

To grant accessibility access to DLP, upload the `accessibility.mobileconfig` file you downloaded previously to Jamf, as described in [Deploy system configuration profiles](device-onboarding-offboarding-macos-jamfpro#deploy-system-configuration-profiles).

### Check the macOS device

1. Restart the macOS device.
2. Verify that the following profiles are listed under Profiles in System Settings:
    - Accessibility
    - MAU
    - MDATP Onboarding
    - MDE Preferences
    - Management profile
    - Network filter
    - Notifications
    - System extension profile

## Offboard macOS devices using Jamf Pro

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

For information about how to offboard a macOS device using Jamf Pro, refer to the [Jamf Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).