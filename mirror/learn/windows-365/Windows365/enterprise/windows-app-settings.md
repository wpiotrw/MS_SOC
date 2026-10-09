---
layout: Conceptual
title: Windows App settings (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-app-settings
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: This settings object allows IT administrators the ability to customize options for users of the Windows App.
author: maddiecarr22
ms.author: madelinecarr
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-10-08T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 07ae0825-f24b-03d1-2e5c-d65262a894ff
document_version_independent_id: 07ae0825-f24b-03d1-2e5c-d65262a894ff
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-app-settings.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-app-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-app-settings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c450d479-44e5-4a9c-9b93-e6f9b69dd42d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e273b0-a43e-4cc8-9bf9-67d4d6a1e869
platformId: c6cc6d8d-0705-c41e-2382-a4167e3f357a
---

# Windows App settings (Preview) | Microsoft Learn

This settings object allows IT administrators the ability to customize options for users of the [Windows App](/en-us/windows-app/get-started-connect-devices-desktops-apps?tabs=windows-avd%2Cwindows-w365%2Cwindows-devbox%2Cmacos-rds%2Cmacos-pc&amp;pivots=azure-virtual-desktop). Windows App settings support targeting to user groups or all users.

The **Windows App settings** page lets IT administrators manage the following settings for the user: 

- **Enable users to reset their Cloud PCs:** Enabling this setting will allow targeted users to reprovision their Cloud PC from within the Windows 365 app and web app.

    Note

    Applicable only to user groups assigned to Windows 365 Enterprise, Windows 365 Flex Dedicated, and Windows 365 Reserve provisioning policies.
- **Allow users to initiate a Restore:** Allow user to initiate restore service.

    Note

    Applicable only to user groups assigned to Windows 365 Enterprise and Windows 365 Flex Dedicated provisioning policies.

    Note

    Applicable only to user groups assigned to Reserve provisioning policies & licensed for Reserve.

## **Add a new setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Click on **Create** and select **Windows App settings** from the dropdown.
3. Enter a **Name** for the setting and include a **Description** (optional).
4. On the **Configuration settings** tab, select **Enable** or **Disable** for any of the settings you would like to configure. For any settings you do not want to configure, you can leave them as their default state of **Not configured**.
5. Add any **Scope tags** you would like to configure. To learn more about scope tags, go [here](/en-us/intune/intune-service/fundamentals/scope-tags).
6. Under **Assignments**, choose **Add groups** or **Add all users**.
7. Under **Select groups to include**, choose a group of users to get the settings &gt; **Select**.
8. Select **Next**.
9. On the **Review + save** page, select **Create**.

    ![Screenshot that shows Windows App settings in Intune.](media/windows-app-settings/windows-app-settings.png)

Note

When there's a conflict between **Windows App settings** and **User settings**, the **Windows App settings** will override **User settings**.

## **Edit a setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Select the **Windows App settings** policy that you want to edit.
3. To change the name of the policy or to turn settings on or off, select **Edit** next to **Settings**.
4. Make any changes you want.
5. On the **Review + Save** page, select **Update**.
6. To edit assignments, select **Edit** next to **Assignments** &gt; **Add** **groups** to add another user group, or select **Add all users** to assign the configuration to all users. To remove existing groups, select the ellipses (**…**) &gt; **Remove**.
7. Select **Next**.
8. On the **Review + Save** page, select **Update**.

## **Delete a setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. On the **Settings** page, you can view the created settings.
3. Select the ellipses (**…**) in the row of the setting you want to delete &gt; **Delete**.
4. Select **Yes** on the confirmation pop up to delete the setting permanently.