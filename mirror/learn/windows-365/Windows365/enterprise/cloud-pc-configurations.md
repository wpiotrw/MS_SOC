---
layout: Conceptual
title: Cloud PC configurations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/cloud-pc-configurations
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: This article will provide information about Cloud PC configurations in Intune.
author: maddiecarr22
ms.author: madelinecarr
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-09-08T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: db88c9bf-6717-f497-9c94-45f438b5b41b
document_version_independent_id: db88c9bf-6717-f497-9c94-45f438b5b41b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/cloud-pc-configurations.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/cloud-pc-configurations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/cloud-pc-configurations.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 5c01110c-b65e-0c73-5a59-d79f9060cfc2
---

# Cloud PC configurations | Microsoft Learn

Cloud PC configurations encompass settings that affect Cloud PCs, specifically addressing configurations that can be enabled or disabled after initial provisioning. Cloud PC configurations support targeting to user groups or all users.

The **Cloud PC configurations** page lets IT administrators manage the following settings for the user: 

- **AI-enabled features (Frontier preview):** The hybrid compute framework will be installed and allow end user’s device to use AI-enabled features.
- **Enable local admin (preview):** If enabled, each user in the assigned groups is elevated to a local administrator of each of their own Cloud PCs. These permissions apply at the user level.
- **Business continuity and disaster recovery features:** These features help protect Cloud PCs and support recovery during service interruptions. To learn more, see [Business continuity and disaster recovery](/en-us/windows-365/enterprise/business-continuity-disaster-recovery-setup).

Note

We recommend using **Cloud PC configurations** when configuring the **Enable local admin (preview)** setting. Existing configurations of **Enable local admin (preview)** in **User Settings** can continue to be managed there for now. Over time, we recommend moving these configurations to **Cloud PC configurations** as support through **User Settings** is phased out.

Note

Applicable only to devices with specs of 8vCPU/32GB/256GB and higher.

## **Add a new setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Click on **Create** and select **Cloud PC configurations** from the dropdown.
3. Enter a **Name** for the setting and include a **Description** (optional).
4. On the **Configuration settings** tab, select **Enable** or **Disable** for any of the settings you would like to configure. For any setting you don't want to configure, you can leave them as their default state of **Not configured**.
5. Add any **Scope tags** you would like to configure. To learn more about scope tags, go [here](/en-us/intune/intune-service/fundamentals/scope-tags).
6. Under **Assignments**, choose **Add groups** or **Add all users**.
7. Under **Select groups to include**, choose a group of users to get the settings &gt; **Select**.
8. Select **Next**.
9. On the **Review + save** page, select **Create**. 

    ![Screenshot that shows Cloud PC configurations in Intune.](media/cloud-pc-configurations/cloud-pc-configurations.png)

## **Edit a setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. Select the **Cloud PC configurations** policy that you want to edit.
3. To change the name of the policy or to turn settings on or off, select **Edit** next to **Settings**.
4. Make any changes you want.
5. On the **Review + Save** page, select **Update**.
6. To edit assignments, select **Edit** next to **Assignments** &gt; **Add** **groups** to add another user group, or select **Add all users** to assign the configuration to all users. To remove existing groups, select the ellipses (**…**) &gt; **Remove**.
7. Select **Next**.
8. On the **Review + Save** page, select **Update**.

## **Delete a setting**

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Cloud PC Settings** (under **Manage Windows 365 Cloud PCs**).
2. On the **Cloud PC Settings** page, you can view the created settings.
3. Select the ellipses (**…**) in the row of the setting you want to delete &gt; **Delete**.
4. Select **Yes** on the confirmation pop up to delete the setting permanently.