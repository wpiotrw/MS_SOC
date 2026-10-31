---
layout: Conceptual
title: Onboard and offboard macOS devices into Purview solutions using Microsoft Intune for Microsoft Defender for Endpoint customers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-intune-mde
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-01-14T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Learn how to onboard and offboard macOS devices into Microsoft Purview solutions using Microsoft Intune for MDE customers
locale: en-us
document_id: 9b821712-53f4-dd74-afe3-2167978759ec
document_version_independent_id: 9b821712-53f4-dd74-afe3-2167978759ec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-offboarding-macos-intune-mde.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-offboarding-macos-intune-mde
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-offboarding-macos-intune-mde.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a2b3676c-ff6e-3412-9306-67cfde00c351
---

# Onboard and offboard macOS devices into Purview solutions using Microsoft Intune for Microsoft Defender for Endpoint customers | Microsoft Learn

You can use Microsoft Intune to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure ***if you have already deployed*** Microsoft Defender for Endpoint (MDE) to your macOS devices.

**Applies to:**

- Customers who have MDE deployed to their macOS devices.
- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

## Before you begin

- Make sure your [macOS devices are onboarded to Intune](/en-us/mem/intune/fundamentals/deployment-guide-platform-macos) and enrolled in the [Company Portal app](/en-us/mem/intune/user-help/enroll-your-device-in-intune-macos-cp).
- Make sure you have access to the [Microsoft Intune admin center](https://endpoint.microsoft.com/#home).
- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices.

Note

The three most recent major releases of macOS are supported.

## Onboard macOS devices into Microsoft Purview solutions using Microsoft Intune

Given that Microsoft Defender for Endpoints (MDE) has already been deployed to your macOS devices, you can still onboard the devices into Purview solutions by competing the following steps:

1. Validate existing FDA system configuration profile
2. Update MDE Preferences

### Validate existing system configuration profile

1. A full disk access (FDA) configuration profile should have been created and deployed previously for MDE. (For details, see [Intune-based deployment for Microsoft Defender for Endpoint on Mac](/en-us/defender-endpoint/mac-install-with-intune#step-3-full-disk-access)).
2. Endpoint data loss prevention (DLP) *requires additional FDA permission* for the new application (`com.microsoft.dlp.daemon`). Validate that the `com.microsoft.dlp.daemon` is in the fulldisk.mobileconfig file

### Update MDE Preferences

1. Find the existing **MDE Preferences** configuration profile. See [Intune-based deployment for Microsoft Defender for Endpoint on Mac](/en-us/defender-endpoint/mac-install-with-intune#step-9-microsoft-defender-for-endpoint-configuration-settings) for details.
2. Add the following key to the `com.microsoft.wdav` configuration profile file, then save the file.

    ```xml
    <key>features</key> 
    <dict> 
      <key>dataLossPrevention</key> 
      <string>enabled</string> 
    </dict> 
    ```

## Offboard macOS devices using Microsoft Intune

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data received from the device, including references to any alerts it has had, will be retained for up to six months.

1. In the **Microsoft Intune admin center**, open **Devices** &gt; **Configuration**. The policies you created display.
2. Choose the **MDE Preferences** policy.
3. Under **Properties &gt;** **Configuration Settings**, choose **Edit**
4. Remove these settings:

    ```xml
     <key>features</key>
     <dict>
         <key>dataLossPrevention</key>
         <string>enabled</string>
     </dict>
    ```
5. Choose \*\*Review+\*\***Save**. This will offboard the macOS devices from Purview solutions while not changing the macOS device enrollment in MDE.