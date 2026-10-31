---
layout: Conceptual
title: Onboard Windows 10 and Windows 11 devices using a local script | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/device-onboarding-script
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-13T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-device-onboarding
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Use a local script to deploy the configuration package on devices so that they are onboarded to the service.
locale: en-us
document_id: 575f1fe6-0f9d-d938-3703-32f5b4b109de
document_version_independent_id: 575f1fe6-0f9d-d938-3703-32f5b4b109de
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/device-onboarding-script.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: device-onboarding-script
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/device-onboarding-script.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3ea63631-d573-6df1-7eaf-46a5b91c496a
---

# Onboard Windows 10 and Windows 11 devices using a local script | Microsoft Learn

**Applies to:**

- [Endpoint data loss prevention (DLP)](endpoint-dlp-learn-about)
- [Insider risk management](insider-risk-management)

You can also manually onboard individual devices to Microsoft 365. You might want to do this first when testing the service before you commit to onboarding all devices in your network.

Important

This script has been optimized for use on up to 10 devices.

To deploy at scale, use [other deployment options](device-onboarding-overview). For example, you can deploy an onboarding script to more than 10 devices in production with the script available in [Onboard Windows 10 devices using Group Policy](device-onboarding-gp).

## Onboard devices

1. Get the configuration package .zip file (*DeviceComplianceOnboardingPackage.zip*) package from [Microsoft Purview portal](https://purview.microsoft.com)
2. In the navigation pane, select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device onboarding**.
3. In the **Deployment method** field, select **Local Script**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the configuration package to a location on the device you want to onboard (for example, the Desktop). You should have a file named *DeviceComplianceLocalOnboardingScript.cmd*.
6. Open an elevated command-line prompt on the device and run the script:
7. Go to **Start** and type **cmd**.
8. Right-click **Command prompt** and select **Run as administrator**.

    ![Window Start menu pointing to Run as administrator.](media/dlp-run-as-admin.png)
9. Type the location of the script file. If you copied the file to the desktop, type: *%userprofile%\Desktop\DeviceComplianceLocalOnboardingScript.cmd*
10. Press the **Enter** key or click **OK**.

For information on how you can manually validate that the device is compliant and correctly reports sensor data see, [Troubleshoot Microsoft Defender Advanced Threat Protection onboarding issues](/en-us/windows/security/threat-protection/microsoft-defender-atp/troubleshoot-onboarding).

## Offboard devices using a local script

For security reasons, the package used to Offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When downloading an offboarding package you will be notified of the packages expiry date and it will also be included in the package name.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time, otherwise this will cause unpredictable collisions.

1. Get the offboarding package from [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149).
2. In the navigation pane, select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device offboarding**.
3. In the **Deployment method** field, select **Local Script**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the devices. You should have a file named *DeviceComplianceOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd*.
6. Open an elevated command-line prompt on the device and run the script:
7. Go to **Start** and type **cmd**.
8. Right-click **Command prompt** and select **Run as administrator**.

    ![Window Start menu pointing to Run as administrator.](media/dlp-run-as-admin.png)
9. Type the location of the script file. If you copied the file to the desktop, type: *%userprofile%\Desktop\WindowsDefenderATPOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd*
10. Press the **Enter** key or click **OK**.

Important

Offboarding causes the device to stop sending sensor data to the portal.

## Monitor device configuration

You can follow the different verification steps in the [Troubleshoot onboarding issues]((/windows/security/threat-protection/microsoft-defender-atp/troubleshoot-onboarding) to verify that the script completed successfully and the agent is running.

Monitoring can also be done directly on the portal, or by using the different deployment tools.

### Monitor devices using the portal

1. Go to [Microsoft Purview portal](https://compliance.microsoft.com).
2. Choose **Settings** &gt; **Device onboarding** &gt; **Devices**.
3. Go to Microsoft Purview portal, and select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device onboarding** &gt; **Devices**.
4. Verify that devices are appearing.