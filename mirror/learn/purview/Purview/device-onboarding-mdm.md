---
layout: Conceptual
title: Onboard Windows 10 and Windows 11 devices using Mobile Device Management tools | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-mdm
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-04-03T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Use Mobile Device Management tools to deploy the configuration package on devices so that they're onboarded to the service.
locale: en-us
document_id: c9885af1-3172-1789-9395-6d575755c223
document_version_independent_id: c9885af1-3172-1789-9395-6d575755c223
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-mdm.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-mdm
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-mdm.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: 6a786e93-3bc4-e4df-56aa-8919f65a0681
---

# Onboard Windows 10 and Windows 11 devices using Mobile Device Management tools | Microsoft Learn

**Applies to:**

- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

You can use mobile device management (MDM) solutions to configure devices. Microsoft 365 information protection supports MDM solutions by providing OMA-URIs to create policies to manage devices.

## Before you begin

If you're using Microsoft Intune, the device must be enrolled in MDM.

For more information on enabling MDM with Microsoft Intune, see [Device enrollment (Microsoft Intune)](/en-us/mem/intune/enrollment/device-enrollment).

## Onboard devices using Microsoft Intune

Follow the instructions from [Intune](/en-us/mem/intune/protect/advanced-threat-protection-configure).

Note

The **Health Status for onboarded devices** policy uses read-only properties and can't be remediated.

## Offboard and monitor devices using Mobile Device Management tools

For security reasons, the package used to offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When you download an offboarding package, you're notified of the package's expiry date. The expiry date is also included in the package name.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time. If they are, unpredictable collisions result.

1. Get the offboarding package from the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149).
2. In the navigation pane, select **Settings** &gt; **Device onboarding** &gt; **Offboarding**.
3. In the **Deployment method** field, select **Mobile Device Management / Microsoft Intune**.
4. Select **Download package**, and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the network administrators who deploy the package. You should have a file named *DeviceCompliance\_valid\_until\_YYYY-MM-DD.offboarding*.
6. Use the Microsoft Intune custom configuration policy to deploy the following supported OMA-URI settings.

    ```console
    OMA-URI: ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Offboarding
    Date type: String
    Value: [Copy and paste the value from the content of the DeviceCompliance_valid_until_YYYY-MM-DD.offboarding file]
    ```

    Note

    If Microsoft Defender for Endpoint is already configured, you can **Turn on device onboarding**. If you do this, step 6 isn't required.

Note

The **Health Status for offboarded devices** policy uses read-only properties and can't be remediated.

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including reference to any alerts received, will be retained for up to six months.