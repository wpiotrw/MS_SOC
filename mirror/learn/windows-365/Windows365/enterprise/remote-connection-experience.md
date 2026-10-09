---
layout: Conceptual
title: Remote connection experience | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/remote-connection-experience
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how IT administrators can use Remote Connection Experience settings to customize the remote desktop connection experience for Windows 365 Cloud PC users.
author: maddiecarr22
ms.author: madelinecarr
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-07-16T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
ai-usage: ai-assisted
locale: en-us
document_id: 686ad3d5-aa75-8711-be51-a366d72c25b5
document_version_independent_id: 686ad3d5-aa75-8711-be51-a366d72c25b5
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/remote-connection-experience.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/remote-connection-experience
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/remote-connection-experience.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 7f594d56-8597-7b5c-db07-7b9fcc44e1f0
---

# Remote connection experience | Microsoft Learn

The **Remote Connection Experience** settings apply just in time as a user connects to a targeted Cloud PC. Remote Connection Experience supports targeting to device groups or all devices. 

The **Remote Connection Experience** page lets IT administrators manage the following settings for the device:

- **Context-based redirections (preview):** By using authentication context, admins can define when specific client capabilities should be allowed or restricted based on factors such as user role, device compliance, or network location. [Learn more about context-based redirections](/en-us/windows-365/enterprise/context-based-redirections)
- **Input protection (preview):** Blocks input from local admin like keyboard, pen from entering the remote session. Only input generated within the remote session is accepted, improving isolation and reducing risk of interference.
- **Display settings (preview):** IT admins can configure default display settings (single display or all displays) for Windows 365 Cloud PCs. Users can override admin defaults with their own display preferences via the Windows App client (for Windows and MacOS only).

## Add a new setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Select **Create** and select **Remote Connection Experience** from the dropdown.
3. Enter a **Name** for the setting and include a **Description** (optional).
4. On the **Configuration settings** tab, select **Enable** or **Disable** for any of the settings you would like to configure. For any settings you do not want to configure, you can leave them as their default state of **Not configured**.
5. Add any **Scope tags** you would like to configure. To learn more about scope tags, see [Use role-based access control (RBAC) and scope tags for distributed IT](/en-us/intune/intune-service/fundamentals/scope-tags).
6. Under **Assignments**, choose **Add groups** or **Add all devices**.
7. Under **Select groups to include**, choose a group of devices to get the settings &gt; **Select**.
8. Select **Next**.
9. On the **Review + save** page, select **Create**.

![Screenshot that shows Remote connection experience in Intune.](media/remote-connection-experience/remote-connection-experience.png)

## Edit a setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Select the **Remote Connection Experience** policy that you want to edit.
3. To change the name of the policy or to turn settings on or off, select **Edit** next to **Settings**.
4. Make any changes you want.
5. On the **Review + Save** page, select **Update**.
6. To edit assignments, select **Edit** next to **Assignments** &gt; **Add** **groups** to add another device group, or select **Add all devices** to assign the configuration to all devices. To remove existing groups, select the ellipses (**…**) &gt; **Remove**.
7. Select **Next**.
8. On the **Review + Save** page, select **Update**.

## Delete a setting

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. On the **Settings** page, you can view the created settings.
3. Select the ellipses (**…**) in the row of the setting you want to delete &gt; **Delete**.
4. Select **Yes** on the confirmation pop up to delete the setting permanently.