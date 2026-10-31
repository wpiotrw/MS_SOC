---
layout: Conceptual
title: Onboard and offboard macOS devices into Microsoft Purview solutions using JAMF Pro | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro
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
description: Learn how to onboard and offboard macOS devices into Microsoft Purview solutions using JAMF Pro
locale: en-us
document_id: 33655f25-94a2-7da6-ce4a-a1ef2bcff000
document_version_independent_id: 33655f25-94a2-7da6-ce4a-a1ef2bcff000
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-offboarding-macos-jamfpro.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-offboarding-macos-jamfpro
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-offboarding-macos-jamfpro.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
2PlusCloud:
- Power
- Azure
- M365
platformId: faf7f0c3-6a9e-8465-ed24-bb661a6018b2
---

# Onboard and offboard macOS devices into Microsoft Purview solutions using JAMF Pro | Microsoft Learn

You can use JAMF Pro to onboard macOS devices into Microsoft Purview solutions such as Endpoint data loss prevention (DLP).

Important

Use this procedure if you ***do not*** have Microsoft Defender for Endpoint (MDE) deployed to your macOS devices.

**Applies to:**

- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

## Before you begin

- Make sure your [macOS devices are managed through JAMF pro](https://www.jamf.com/resources/product-documentation/jamf-pro-installation-guide-for-mac/) and are associated with an identity (Microsoft Entra joined UPN) through [JAMF Connect](https://www.jamf.com/products/jamf-connect).
- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices for native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using JAMF Pro

### Prerequisites

Download the following files.

| File | Description |
| --- | --- |
| [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) | This is the bundled file. |
| [schema.json](https://github.com/microsoft/mdatp-xplat/blob/master/macos/settings/data_loss_prevention/schema.json) | This is the MDE preference file. |

Tip

We recommend downloading the bundled [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) file, rather than the [individual](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles)*.mobileconfig* files. The bundled file includes the following required files:

- accessibility.mobileconfig
- fulldisk.mobileconfig
- netfilter.mobileconfig
- sysext.mobileconfig

If any of these files are updated, you need to either download the updated bundle, or download each updated file individually.

### Get the device onboarding and installation packages

[![Screenshot of the Microsoft Intune Configuration settings tab with all fields populated.](media/device-macos-dnld-install-package-inline.png)](media/device-macos-dnld-install-package-expanded.png#lightbox)

1. In the Purview portal, open **Settings** &gt; **Device Onboarding** and then choose **Onboarding**.
2. For the **Select operating system to start onboarding process** value, choose **macOS**.
3. For **Deployment method**, choose **Mobile Device Management/Microsoft Intune**.
4. Choose **Download onboarding package** and then extract the contents of the device onboarding package. the *DeviceComplianceOnboarding.plist* file is downloaded to the JAMF folder.
5. Choose **Download installation package**.

### Deploy onboarding packages

Create a new configuration profile in JAMF Pro. Use the following values:

- **Name:***MDATP onboarding for macOS*
- **Description:** \**MDATP EDR onboarding for macOS*
- **Category:***none*
- **Distribution method:** \*`*install automatically*
- **Level:***computer level*

For help with performing steps within the Jamf Pro console, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

### Configure application preferences

Important

You must use *com.microsoft.wdav* as the **Preference Domain** value. Microsoft Defender for Endpoint uses this name and *com.microsoft.wdav.ext* to load the managed settings.

For information about how to create a new configuration profile in JAMF Pro, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/). Or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

Use these values:

- **Name:***MDATP MDAV configuration settings*
- **Description:***Leave this blank*
- **Category:***none*
- **Distribution method:***install automatically*
- **Level:***computer level*

### Deploy system configuration profiles

For information about how to deploy system configuration profiles in JAMF Pro, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

## Offboard macOS devices using JAMF Pro

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

1. If you aren't using MDE, uninstall the application. See the **Package Deployment** section in the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/).
2. Restart the macOS device. (Some applications may lose printing functionality until they're restarted.)