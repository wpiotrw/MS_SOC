---
layout: Conceptual
title: Any mobile device management tool for customers without Microsoft Defender for Endpoint | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-any-mdm-no-mde
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-05-05T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Learn how to onboard and offboard macOS devices into Microsoft Purview solutions using any MDM, no MDE
locale: en-us
document_id: 6347a69a-6e11-3379-02ed-bd4ac71ec69c
document_version_independent_id: 6347a69a-6e11-3379-02ed-bd4ac71ec69c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-offboarding-any-mdm-no-mde.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-offboarding-any-mdm-no-mde
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-offboarding-any-mdm-no-mde.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2510b867-e001-3056-10d1-3aae06f05e8b
---

# Any mobile device management tool for customers without Microsoft Defender for Endpoint | Microsoft Learn

You can use any mobile device management (MDM) solution to onboard macOS devices into Microsoft Purview solutions such as Endpoint data loss prevention (DLP).

Important

Use this procedure if you ***do not*** have Microsoft Defender for Endpoint (MDE) deployed to your macOS devices.

**Applies to:**

- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)

## Before you begin

- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices for native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using any MDM

### Prerequisites

- You must have Microsoft Defender Antimalware client version 101.25012.0005 or newer installed on the device.
- Download the following files.

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

1. In the Microsoft Purview portal, open **Settings** &gt; **Device Onboarding** and then choose **Onboarding**.
2. For the **Select operating system to start onboarding process** value, choose **macOS**.
3. For **Deployment method**, choose **Mobile Device Management/Microsoft Intune**.
4. Choose **Download onboarding package** and then extract the contents of the device onboarding package. the *DeviceComplianceOnboarding.plist* file is downloaded to the JAMF folder.
5. Choose **Download installation package**.

### Deploy onboarding packages

1. Create a new configuration profile in your MDM. Use the following values (if applicable):

- **Name:***MDATP onboarding for macOS*
- **Description:** \**MDATP EDR onboarding for macOS*
- **Category:***none*
- **Distribution method:** \*`*install automatically*
- **Level:***computer level*

1. Upload *DeviceComplianceOnboarding.plist* as a custom settings
2. Enter `com.microsoft.wdav.atp` as the **Preference Domain**,
3. Choose **Save**. Refer to your MDM documentation on creating configuration profile.

### Configure application preferences

Important

You must use *com.microsoft.wdav* as the **Preference Domain** value. Microsoft Defender for Endpoint uses this name and *com.microsoft.wdav.ext* to load the managed settings.

For information about how to create a new configuration profile, refer to your MDM documentation.

1. Create a new configuration profile. Use these values (if applicable):

- **Name:***MDATP MDAV configuration settings*
- **Description:***Leave this blank*
- **Category:***none*
- **Distribution method:***install automatically*
- **Level:***computer level*

1. Add the `schema.json` as a custom schema in the configuration profile.
2. Under **Preference Domain Properties**, locate **Data Loss Prevention** and select `enabled`.
3. Save the profile after adjusting other MDE settings (if necessary).

### Deploy system configuration profiles

For information about how to deploy system configuration profiles, refer to your MDM documentation.

1. Create a new configuration profile by uploading the `mdatp.mobileconfig` file into your MDM.

### Register Identity

Depending on your configuration, you register the Microsoft Entra identity of the using one of these two methods.

#### Method 1: Register without the Microsoft Intune Company Portal

1. Install any Microsoft application such as Microsoft Office, or Teams, or Microsoft Edge. When the user logs in using valid Microsoft Entra account, that account is registered as the UPN for DLP policy evaluation. Personal Microsoft accounts aren't considered as valid. The device may need to restart to complete the registration.

#### Method 2: Register with the Microsoft Intune Company Portal

This method is for users whose macOS devices don't use Microsoft apps.

You can [Get the Microsoft Intune Company Portal](/en-us/intune/intune-service/user-help/sign-in-to-the-company-portal) if you don't already have it.

1. Deploy [Microsoft Enterprise SSO plug-in for Apple devices](/en-us/entra/identity-platform/apple-sso-plugin) to their managed macOS devices using your MDM solution. The Microsoft Intune Company Portal for macOS provides the SSO plugin for smooth user experience. So, the Microsoft Intune Company Portal must be installed on the macOS device, but the user doesn't need to be signed into the Intune Company portal. When the user signs-in to any non-Microsoft Authentication Library (MSAL) application, like Safari browser, the SSO plugin is enabled to register the UPN. The device may need to restart to complete the registration.

For information on troubleshooting the Microsoft Enterprise SSO Extension, go to [Troubleshooting the Microsoft Enterprise SSO Extension plugin on Apple devices](/en-us/entra/identity/devices/troubleshoot-mac-sso-extension-plugin?tabs=flowchart-ios).

## Offboard macOS devices using any MDM

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

1. If you aren't using MDE, uninstall the application. Refer to your MDM documentation for any MDM specific instructions for uninstallation.
2. Restart the macOS device. (Some applications may lose printing functionality until they're restarted.)