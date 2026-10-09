---
layout: Conceptual
title: Windows 365 Cloud Apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/cloud-apps
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about Windows 365 Cloud Apps.
author: serenaz
ms.author: sezhen
ms.service: windows-365
ms.topic: concept-article
ms.date: 2026-07-12T00:00:00.0000000Z
locale: en-us
document_id: 78025fdd-95e0-e8ca-3e98-ec4d961ebe11
document_version_independent_id: 78025fdd-95e0-e8ca-3e98-ec4d961ebe11
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/cloud-apps.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/cloud-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/cloud-apps.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 516d66ee-7808-8fb2-e7e8-99d27c7b2451
---

# Windows 365 Cloud Apps | Microsoft Learn

Important

Windows 365 Frontline is now **Windows 365 Flex**. The product name in the Microsoft Intune admin center is being updated and may still appear as **Frontline** in some places. This article reflects those existing references where updates are still in progress. For more information about the rebrand, see [Expanding access to Windows 365](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-365-and-azure-virtual-desktop-expanding-access/4515931).

Windows 365 Cloud Apps allow administrators to give users secure access to individual apps hosted on a Cloud PC, without requiring a dedicated Cloud PC for every user. Windows 365 Cloud Apps run on Windows 365 Flex Cloud PCs in Shared mode, so [Windows 365 Flex licenses](/en-us/windows-365/enterprise/windows-365-flex-license) are required to use Cloud Apps.

## Prerequisites

To create Cloud Apps, you need a [Windows 365 Flex license](/en-us/windows-365/enterprise/windows-365-flex-license).

If you'd like to create Cloud Apps from custom applications (that is, applications that aren't preinstalled in [Windows 365 gallery images](/en-us/windows-365/enterprise/device-images)), then you can either:

- Add a [custom image](/en-us/windows-365/enterprise/add-device-images)

    - When you upload a [custom image](/en-us/windows-365/enterprise/add-device-images), Windows 365 Cloud Apps uses a PowerShell script to scan the Start Menu for apps. However, if your tenant imposes security policies requiring extra authentication for PowerShell, then we can't discover apps. Additionally, if your custom image isn't supported, then we can't discover apps.
- Create an [Autopilot Device Preparation Policy](/en-us/windows-365/enterprise/autopilot-device-preparation)

    - Windows 365 Cloud App support for Autopilot Device Preparation is in [public preview](/en-us/windows-365/public-preview).

## Create Cloud Apps

1. First, [create a new](/en-us/windows-365/enterprise/create-provisioning-policy) Windows 365 provisioning policy, and complete the following steps:

    1. On the **General** tab, for **Experience**, select "Access only apps." This selection defaults the License type to Frontline and Shared mode.
    2. In the **Image** tab, you can view the apps available on the image that you can publish after provisioning.
    3. In the **Configuration** tab, if you select an [Autopilot Device Preparation Policy](/en-us/windows-365/enterprise/autopilot-device-preparation), then make sure to check the box to "Prevent users from connection to Cloud PC upon installation failure or timeout." You can also enable User Experience Sync so that app settings and data are saved and applied between user sessions.
2. Once the policy is created, the Windows 365 Flex Cloud PCs in Shared mode with experience type "Cloud App" begin provisioning in **All Cloud PCs**, and a row with status "Preparing" appears in **All Cloud Apps**. After the first Cloud PC is provisioned, the apps discovered on the Cloud PC's Start Menu will show as "Ready to publish" in **All Cloud Apps.**

Note

Cloud Apps support for APPX and MSIX applications in existing Cloud Apps provisioning policies requires reprovisioning. This will enable the discovery of APPX and MSIX applications. Preview of apps in image during policy creation does not currently include APPX/MSIX applications. The application will be ready to publish in the All Cloud Apps blade. 

## Publish and edit Cloud Apps

In **All Cloud Apps**, you can publish, edit, reset, and unpublish Cloud Apps.

- Publish - When you publish Cloud Apps, the app status changes from "Ready to publish" to "Publishing" to "Published." Publishing an app makes it available in Windows App to all users assigned to the provisioning policy. If the app status is "Failed," then try unpublishing and republishing again.
- Edit - You can edit individual Cloud App details, including display name, description, command line, icon path, and icon index. The Cloud App's scope tags and assignment are inherited from the provisioning policy. The edits are published immediately to Windows App.
- Reset - You can reset the Cloud App's details to its original discovered state.
- Unpublish - When you unpublish Cloud Apps, the app status changes from "Published" to "Ready to publish," and the app is no longer available in Windows App. App details are also reset.

## Add Cloud Apps from file path

In **All Cloud Apps**, you can manually add Cloud Apps by specifying a file path.

- Add from file path - When you add a Cloud App from file path, you can enter the file path, app name, display name, description, command-line parameters, icon path, and icon index of an application that exists on your Cloud PCs. This lets you publish apps that are not discovered automatically from the Start Menu, including legacy apps, and apps that require custom launch parameters.
- Validate - If the file path or the icon path is invalid, a failed status is shown on the Cloud App so you can correct the app details and republish.
- Edit - You can edit Cloud Apps added from file path, including the file path, app name, display name, description, command line, icon path, and icon index. After editing, review and publish the Cloud App so the updated details are available to users.
- Delete - You can delete Cloud Apps added from file path. When deleted, the app is removed from All Cloud Apps and is no longer available for publishing or launching in Windows App. Published apps will disappear from the Windows App.

If Cloud PCs from a provisioning policy are reprovisioned, all the apps will be re-discovered and republished. For Cloud Apps added from file path, they will also be re-validated and republished.

## Delete Cloud Apps

To delete Cloud Apps, you need to delete the Cloud App provisioning policy assignment or the user group assigned to the policy.

## Manage Cloud Apps and Cloud PCs

Since Cloud Apps run on [Windows 365 Flex Cloud PCs in Shared mode](/en-us/windows-365/enterprise/introduction-windows-365-flex), the same management and end-user experiences that apply to Windows 365 Flex shared Cloud PCs also apply to Cloud Apps. For example:

- The maximum number of active Windows 365 Cloud App sessions for a provisioning policy is equal to the number of Windows 365 Flex licenses that you assign to that specific policy. You can monitor concurrency in the [Connected Windows 365 Flex Cloud PCs report](/en-us/windows-365/enterprise/report-connected-windows-365-flex-cloud-pcs).
- All settings applied to the underlying Windows 365 Flex Cloud PCs, such as [redirections](/en-us/windows-365/enterprise/manage-rdp-device-redirections) or [idle timeout settings](/en-us/windows-365/enterprise/windows-365-flex-cloud-pc-session-time-limits), also apply to Cloud Apps.

## Connect to Cloud Apps

End-users access published apps through [Windows App](/en-us/windows-365/end-user-access-cloud-pc). Published apps can also open other apps that are on the Cloud PC. For example, Microsoft Outlook as a Cloud App can launch Microsoft Edge via embedded links in emails, even if Microsoft Edge isn't published as a Cloud App. To fully control access to apps, use [Application Control for Windows](/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol).

If Cloud PCs are running supported versions of Windows (Windows 11 Enterprise, version 24H2, or version 22H2 or 23H2 with the [2024-07 Cumulative Update for Windows 11 (KB5040442)](https://support.microsoft.com/kb/KB5040442) or later installed.), then Cloud Apps automatically launch OneDrive.

## Enable enhanced user experiences in Cloud Apps (preview)

Enhanced user experiences for Cloud Apps is in [public preview](/en-us/windows-365/public-preview). Enhancements include improved support for Windows Snap and full-screen mode, better DPI handling, and refined visuals like borders, shadows, and theme integration in Windows OS. To learn how to enable for Cloud Apps, see [RemoteApp enhancements (preview)](/en-us/azure/virtual-desktop/remoteapp-enhancements).

## Troubleshooting

- If Cloud PCs fail to provision, then see [Troubleshoot provisioning errors](/en-us/troubleshoot/windows-365/provisioning-errors).
- If Autopilot device preparation fails to install applications, then see [Autopilot device preparation monitoring](/en-us/autopilot/device-preparation/tutorial/automatic/automatic-monitor) or [Autopilot device preparation known issues](/en-us/autopilot/device-preparation/known-issues).
- If Cloud PCs provision successfully and Autopilot device preparation succeeds, but Intune apps don't appear in Cloud Apps, then make sure the policy configuration option "Prevent users from connection to Cloud PC upon installation failure or timeout" is selected.
- If Cloud PCs provision successfully, but Cloud App status is stuck in "Preparing," then try bulk reprovisioning the policy. Alternatively, if that doesn't work, then try deleting and re-creating the Cloud App policy assignment.