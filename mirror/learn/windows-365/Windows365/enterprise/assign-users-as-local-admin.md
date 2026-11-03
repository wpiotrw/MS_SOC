---
layout: Conceptual
title: User settings in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/assign-users-as-local-admin
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about user settings in Windows 365.
author: maddiecarr22
ms.author: madelinecarr
ms.date: 2026-11-02T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
locale: en-us
document_id: bae741a8-2ff2-6901-29a9-2b07ded3f9ee
document_version_independent_id: bae741a8-2ff2-6901-29a9-2b07ded3f9ee
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/assign-users-as-local-admin.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/assign-users-as-local-admin
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/assign-users-as-local-admin.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: ff7ce36c-ceef-b6e5-23cb-ddd2809105ce
---

# User settings in Windows 365 | Microsoft Learn

Note

New policies can no longer be created through **User** **settings (legacy), but existing policies can still be edited and will continue to apply.** We recommend using [Cloud PC configurations](/en-us/windows-365/enterprise/cloud-pc-configurations) or [Windows App settings](/en-us/windows-365/enterprise/windows-app-settings) for new policies and encourage admins to recreate their existing configurations in these experiences before editing is disabled.

We recommend using **Cloud PC configurations** when creating new policies for Enable local admin, Point-in-time restore, Cross-Region Disaster Recovery, and Disaster Recovery Plus. Similarly, we recommend using **Windows App settings** when creating new policies for Enable users to reset their Cloud PC and Allow users to initiate a restore.

The **User settings** page lets IT administrators manage the following settings for the user:

- **Enable local admin**: If enabled, each user in the assigned groups is elevated to a local administrator of each of their own Cloud PCs. These permissions apply at the user level.
- **Enable users to reset their Cloud PCs**: If enabled, a **Reset** option is shown in the Windows App and portal for users in the assigned groups. Resetting wipes and reprovisions the Cloud PC, deleting all user data and apps.
- **Allow user to initiate restore service**: If enabled, each user in the assigned groups can restore their own Cloud PCs to any available backup version.
- **Cross region disaster recovery configuration (optional)**: Lets you protect Cloud PCs during regional outages. For more information, see [Cross region disaster recovery](cross-region-disaster-recovery).

When managing settings, keep the following points in mind:

- The settings can be applied before or after a Cloud PC is assigned.
- Changes to the settings take effect when the user logs on. If the user is currently logged on, they must sign out and then sign in again to see the change.
- User settings don't apply to Windows 365 Flex Cloud PCs in Shared mode.

## Add a new setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Select **Create**, and choose "**User settings (legacy)".**
3. Under **Settings**, enter a **Name** for the setting.
4. Select the boxes for the settings that you want to enable for the users.

- If you selected **Allow user to initiate restore service**, also select an option for **Frequency of restore-point service**.

1. Select **Next**.
2. Under **Assignments**, choose **Add Groups**.
3. Under **Select groups to include**, choose a group of users to get the settings &gt; **Select**.
4. Select **Next**.
5. On the **Review + save** page, select **Create**.

![Screenshot that shows User settings in Intune.](media/assign-users-as-local-admin/screenshot-that-shows-user-settings-in-intune.png)

## Edit a user setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. The **Cloud PC Settings** page shows the current settings.
3. Select the user setting that you want to edit.
4. To change the name of the policy or to turn settings on or off, select **Edit** next to **Settings**.
5. Under **Settings**, make any changes you want, and then select **Next**.
6. On the **Review + Save** page, select **Update**.
7. To edit assignments, select **Edit** next to **Assignments** &gt; **Add Groups** to add another group. To remove existing groups, select the ellipses (**…**) &gt; **Remove**.
8. Select **Next**.
9. On the **Review + Save** page, select **Update**.

## Delete a user setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. On the **Cloud PC settings** page, you can view the created settings.
3. Select the ellipses (**…**) in the row of the setting you want to delete &gt; **Delete**.
4. Select **Yes** on the confirmation pop up to delete the setting permanently.

## Conflict Resolution for Local Admin

Because user setting policies are assigned to user groups, there’s a possibility of overlap for groups/users. If a user is assigned to more than one user setting policy, user settings from the most-recently created policy are used and all others are ignored. The last time a policy was updated doesn't affect this priority. To make sure user settings are consistent and clear, avoid any policy targeting overlaps. If **Enable Local admin** isn't checked, local admin rights are removed from users in these user groups. This can affect custom solutions/scripts that add users to the local administrator group.