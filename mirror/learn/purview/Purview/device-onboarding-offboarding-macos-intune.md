---
layout: Conceptual
title: Onboard and offboard macOS devices into Microsoft Purview solutions using Microsoft Intune | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-intune
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
description: Learn how to onboard and offboard macOS devices into Microsoft Purview solutions using Microsoft Intune
locale: en-us
document_id: 9e7f5109-87c7-ed10-c699-22d2d3850ef6
document_version_independent_id: 9e7f5109-87c7-ed10-c699-22d2d3850ef6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-offboarding-macos-intune.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-offboarding-macos-intune
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-offboarding-macos-intune.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
platformId: 899cea45-1a43-3920-aa84-177c022e7ed4
---

# Onboard and offboard macOS devices into Microsoft Purview solutions using Microsoft Intune | Microsoft Learn

You can use Microsoft Intune to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure if you ***do not*** have Microsoft Defender for Endpoint (MDE) deployed to your macOS devices

**Applies to:**

- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

## Before you begin

- Make sure your [macOS devices are onboarded into Intune](/en-us/mem/intune/fundamentals/deployment-guide-platform-macos) and are enrolled in the [Company Portal app](/en-us/mem/intune/user-help/enroll-your-device-in-intune-macos-cp).
- Make sure you have access to the [Microsoft Intune admin center](https://endpoint.microsoft.com/#home).
- Create the user groups that you're going to assign the configuration updates to.
- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices to have native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard macOS devices into Microsoft Purview solutions using Microsoft Intune

Onboarding a macOS device into Purvoiew solutions is a multi-phase process.

1. Get the device onboarding package
2. Deploy the mobileconfig and onboarding packages
3. Publish the application

### Prerequisites

Download the following files:

| File | Description |
| --- | --- |
| [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) | System mobile config file |
| [com.microsoft.wdav.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/settings/data_loss_prevention/com.microsoft.wdav.mobileconfig). | MDE preferences |

Tip

We recommend downloading the bundled [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) file, rather than the [individual](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles)*.mobileconfig* files. The bundled file includes the following required files:

- accessibility.mobileconfig
- fulldisk.mobileconfig
- netfilter.mobileconfig
- sysext.mobileconfig

If any of these files are updated, you need to either download the updated bundle, or download each updated file individually.

### Get the device onboarding package

[![Screenshot of the Microsoft Intune Configuration settings tab with all fields populated.](media/device-macos-dnld-onboarding-package-intune-inline.png)](media/device-macos-dnld-onboarding-package-intune-expanded.png#lightbox)

1. In the **Microsoft Purview portal** open **Settings** &gt; **Device Onboarding** and then choose **Onboarding**.
2. For the **Select operating system to start onboarding process** option, choose **macOS**.
3. For **Deployment method**, choose **Mobile Device Management/Microsoft Intune**.
4. Choose **Download onboarding package**.
5. Extract the .ZIP file and open the *Intune* folder. This contains the onboarding code in the *DeviceComplianceOnboarding.xml* file.

### Deploy the mobileconfig and onboarding packages

1. Open the **Microsoft Intune admin center** and navigate to **Devices** &gt; **macOS** &gt; **Configuration**.
2. Choose: **+ Create** and then choose **New policy**.
3. Select the following values:

    1. **Platform** = macOS
    2. **Profile type** = Templates
    3. **Template name** = Custom
4. Choose **Create**.
5. On the **Basics** page, Enter a name for the profile, such as *Microsoft Purview System MobileConfig*, and then Choose **Next**.
6. On the **Configuration settings** page, Choose the `mdatp.mobileconfig` file that you downloaded in the pre-requisites section as the configuration profile file.
7. Choose **Next**.
8. On the **Assignments** tab, add the group you want to deploy these configurations to and then choose **Next**.
9. Review your settings and then choose **Create** to deploy the configuration.
10. Repeat steps 2-9 to create profiles for the:

    1. **DeviceComplianceOnboarding.xml** file. Name it *Microsoft Purview Device Onboarding Package*
    2. **com.microsoft.wdav.mobileconfig** file. Name it *Microsoft Endpoint Device Preferences*
11. In the macOS **Configuration policies** page, the policies you created now display. Select **Refresh** if your changes don't show up right away.
12. Choose the profile that you just created. Next, view the **Device and user check-in status** report of the configuration policy.

### Publish the application

Microsoft Endpoint data loss protection is installed as a component of Microsoft Defender for Endpoint on macOS. This procedure applies to onboarding devices into Microsoft Purview solutions

1. In the [Microsoft Intune admin center](https://endpoint.microsoft.com/), open **Apps**.
2. Select **macOS**.
3. On the **macOS** &gt; **macOS apps** page, select **Create**.
4. On the **Select app type** &gt; **Create app** slider, select the App type drop-down and then **macOS** under **Microsoft Defender for Endpoint**.
5. Choose the **Select** button.
6. On the **App Information** tab, keep the default values and then choose **Next**.
7. On the **Assignments** tab, add assignments and then choose **Next**.
8. You can visit **Apps** &gt; **macOS** to see the new application listed.

## Offboard macOS devices using Intune

Note

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including reference to any alerts it has had, will be retained for up to six months.

1. In the **Microsoft Intune admin center**, open **Devices** &gt; **macOS** &gt; **Configuration**. The policies you created are listed.
2. Select **Microsoft Endpoint Device Preferences** policy.
3. Under **Properties** &gt; **Assignments,** choose **Edit**.
4. Remove the group from the assignment. This will uninstall the com.microsoft.wdav.mobileconfig configuration profile file and offboard the macOS device from Purview solutions.