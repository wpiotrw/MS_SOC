---
layout: Conceptual
title: Create provisioning policies for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/create-provisioning-policy
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to create provisioning policies for Windows 365.
keywords: 
author: ErikjeMS
ms.author: scottduf
manager: scottduf
ms.date: 2026-03-20T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: sezhen
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
- essentials-manage
locale: en-us
document_id: 34eb1b03-5e4e-b511-4542-ce1dff71d3cc
document_version_independent_id: 34eb1b03-5e4e-b511-4542-ce1dff71d3cc
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/create-provisioning-policy.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/create-provisioning-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/create-provisioning-policy.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 90c2b7e6-518a-5814-ab1b-ad92cd04dba3
---

# Create provisioning policies for Windows 365 | Microsoft Learn

Important

Windows 365 Frontline is now **Windows 365 Flex**. The product name in the Microsoft Intune admin center is being updated and may still appear as **Frontline** in some places. This article reflects those existing references where updates are still in progress. For more information about the rebrand, see [Expanding access to Windows 365](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-365-and-azure-virtual-desktop-expanding-access/4515931).

Cloud PCs are created and assigned to users based on provisioning policies. These policies hold key provisioning rules and settings that let the Windows 365 service set up and configure the right Cloud PCs for your users. After provisioning policies are created and assigned to the Microsoft Entra user security groups or Microsoft 365 Groups, the Windows 365 service:

1. Checks for appropriate licensing.
2. Configures the Cloud PCs accordingly.

To learn more about Windows 365 provisioning concepts, see [Provisioning](provisioning).

A few things to keep in mind:

- Windows 365 Enterprise

    - If a user in an assigned group doesn’t have a Cloud PC license assigned, Windows 365 won’t provision their Cloud PC.
    - For each Cloud PC license assigned to a user, only one provisioning policy is used to set up and configure the Cloud PC. The Windows 365 service always uses the first assigned policy to provision the Cloud PC.
- Windows 365 Flex in Dedicated mode

    - If you have more users in your Microsoft Entra user group than the number of Cloud PCs available for the selected size, some users might not receive their Cloud PC.
    - If you remove users from your Microsoft Entra user group, their Cloud PC is automatically moved into a [grace period](device-management-overview#column-details).
- Windows 365 Flex in Shared mode

    - If you remove users from your Microsoft Entra user group, the user loses access to the Cloud PC.
    - If you remove the Microsoft Entra user group from the assignment, the Cloud PCs are automatically deprovisioned without moving into grace period.
- Windows 365 Reserve

    - Cloud PCs are provisioned through the "Provision" device action, not automatically when the provisioning policy is created.
    - If you have more users in your Microsoft Entra user group than the number of licenses available in the tenant, some users might not receive their license assignment.
    - For each Cloud PC license assigned to a user, only one provisioning policy is used to set up and configure the Cloud PC. The Windows 365 service always uses the first assigned policy to provision the Cloud PC.

## Provide general information

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Provision Cloud PCs** &gt; **Provisioning policies** &gt; **Create policy**.
2. On the **General** page, enter a **Name** and **Description** (optional) for the new policy.

    Tip

    Your provisioning policy name can't contain the following characters: &lt; &gt; & | " ^
3. Choose **Experience type:**

    - Access a full Cloud PC desktop: Users connect to a full Windows desktop experience. This option is available for all Windows 365 license types.
    - Access only apps which run on a Cloud PC: Users connect to [Cloud Apps](cloud-apps). This option is only available for Windows 365 Flex in Shared mode.
4. Choose a **License type**:

    - **Enterprise**: Provision Cloud PCs for Windows 365 Enterprise.
    - **Windows 365 Frontline**: Provision Cloud PCs for [Windows 365 Flex](introduction-windows-365-flex). You must have Windows 365 Flex licenses to create a provisioning policy for Windows 365 Flex Cloud PCs. A warning is shown if you lack such licenses when you choose this option.
    - **Reserve**: Provision Cloud PCs for [Windows 365 Reserve](introduction-windows-365-reserve).
5. If you choose **Windows 365 Frontline**, you must also select a **Windows 365 Frontline type**:

    - **Dedicated**: Provision Cloud PCs in [dedicated mode](introduction-windows-365-flex#windows-365-flex-in-dedicated-mode).
    - **Shared**: Provision Cloud PCs in [shared mode](introduction-windows-365-flex#windows-365-flex-in-shared-mode).
6. If you choose **Windows 365 Enterprise** or **Windows 365 Frontline**, then you need to select a **Join type**.

    - **Microsoft Entra Join**: You have three options for **Network**:
        - **Microsoft hosted network**: Select a **Geography** where you want your Cloud PCs provisioned. Then, for **[Region](requirements#supported-azure-regions-for-cloud-pc-provisioning)**, you can select:
            - **[Recommended] All default regions within the geography** (not supported for Windows 365 Flex in Shared mode): You maximize resiliency and provisioning success. Microsoft strongly recommends option to ensure Cloud PCs are distributed across the maximum number of regions with similar latency experience. Learn more about the [resiliency benefits](enhanced-resiliency-mhn) due to this option.
            - **A single region group:** If you want your Cloud PCs to reside within a specific country or region group, select only that region group. This ensures Cloud PCs are distributed across its regions, providing maximum resiliency at the region-group level.
            - **A specific region:** This option makes sure that your Cloud PCs are only provisioned in the region that you choose. You can also choose regions across multiple region groups.
            - **Auto opt-in:** You can enable the auto opt-in checkbox to automatically include any future regions or region groups as they become available, ensuring your Cloud PC deployment always benefits from the latest Azure expansion without manual updates.
        - **Azure network connection**: Select an Azure network connection (ANC) to use for this policy.
    - **Hybrid Microsoft Entra join**: You must select an ANC to use for this policy.
7. Lastly, on the **General** page, you can check the box so that your users **Use Microsoft Entra single sign-on**.

Tip

For Windows 365 Flex in Shared mode, if you want to make sure that users aren't prompted each time they connect, then [Hide consent prompt dialog](/en-us/azure/virtual-desktop/configure-single-sign-on#hide-the-consent-prompt-dialog).

### Select an ANC

You must select an [ANC](azure-network-connections) for your provisioning policy if you selected either of these two options in the previous section:

- **Join type** = **Hybrid Microsoft Entra Join**
- **Join type** = **Microsoft Entra join** and **Network** = **Azure network connection**

To select an ANC, follow these steps:

1. On the **General** page, for **Azure network connection**, select one or more ANCs. For more information about using multiple ANCs, see [Alternate ANCs](azure-network-connections#alternate-ancs).
2. If you select more than one ANC, you can set the priority order for those ANCs. To do so, hover over an ANC &gt; select and drag on the three dots &gt; drag the ANC to a different position in the list.

As long as the first ANC in the list is **Healthy**, it's always used for provisioning Cloud PCs using this policy. If the first ANC isn't healthy, the policy uses the next ANC in the list that is healthy.

Note

For Windows 365 Flex in Shared mode, the ANC must be in the same region.

## Select an image

1. On the **Image** page, for **Image type**, select one of the following options:

    - **Gallery image**: Choose **Select** &gt; select an image from the gallery &gt; **Select**. Gallery images are default images provided for your use.
        - For Reserve, the default gallery image is Automatic, where Windows 365 selects the latest image.
    - **Custom image**: Choose **Select** &gt; select an image from the list &gt; **Select**. The page displays the list of images that you uploaded using the [Add device images](add-device-images) workflow.
    - Optional. If you selected **Access only apps** for **Experience** in the previous step, then you can view applications that are discovered in the image and will be available to publish as **Cloud Apps** after the provisioning policy is created.
2. Select **Next**.

## Select configurations

1. On the **Configuration** page, under **Windows settings**, choose a **Language & Region**. The selected language pack is installed on Cloud PCs provisioned with this policy.
2. Optional. Select **Apply device name template** to create a Cloud PC naming template to use when naming all Cloud PCs that are provisioned with this policy. This naming template updates the NETBIOS name and doesn't affect the display name of the Cloud PC. When creating the template, follow these rules:

    - Names must be between 5 and 15 characters.
    - Names can contain letters, numbers, and hyphens.
    - Names can't include blank spaces or underscores.
    - Prefixes must be 10 or less characters.
    - Optional. use the %USERNAME:X% macro to add the first X letters of the username for Windows 365 Enterprise and Windows 365 Flex Dedicated devices.
    - Required. Use the %RAND:Y% macro to add a random string of characters, where Y equals the number of characters to add. Y must be 5 or more. Names must contain a randomized string.

    Example of a custom naming template:

    - ABCDEF-%RAND:8%
3. Optional. Under **Additional services**, choose a service to be installed on Cloud PCs provisioned with this policy:

    - **Windows Autopatch** is a cloud service that automates updates for Windows, Microsoft 365 Apps for enterprise, Microsoft Edge, and Microsoft Teams on both physical and virtual devices. For more information, see [What is Windows Autopatch?](/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-overview) and the [Windows Autopatch FAQ](https://go.microsoft.com/fwlink/?linkid=2200228). The Windows Autopatch option isn't available for Windows 365 Flex in Shared mode.

        - If you already have Windows Autopatch configured to manage your Cloud PCs, this option replaces the existing policy. This replacement might disrupt any dynamic distribution that is already configured in Autopatch.
        - When **Windows Autopatch** is selected, the system assigns devices to a new ring as the last ring of the Autopatch group.
        - To manually enable dynamic distribution for your Cloud PCs, modify your Autopatch Groups dynamic distribution list to include the Entra ID group to which your Cloud PCs are being added.
        - **None**. Manage and update Cloud PCs manually.
        - The Autopatch option is not available for Windows 365 Flex devices in Shared mode, however it is possible for Windows 365 Flex devices in Shared mode to be enrolled in Autopatch and receive Windows update policies.
    - **Windows Autopilot (Preview)** is a cloud service that ensures Intune applications and scripts are installed during initial enrollment and setup. Choose a Device Preparation Profile from the list, or create a new one. Learn more about [Autopilot Device Preparation for Cloud PCs](autopilot-device-preparation).
    - **User Experience Sync** can be enabled for Windows 365 Flex Cloud PCs in Shared mode. If enabled, Windows 365 stores user-specific Windows and app experience data in central cloud storage and reconnects it whenever the user signs in to the cloud PCs in this provisioning policy. User storage limits are based on Windows 365 Flex license type and are pooled across all users assigned. Learn more about [User Experience Sync](windows-365-flex-user-experience-sync).
4. Select **Next**.

## Create scope tags

1. Optional. You can create [scope tags](/en-us/intune/intune-service/fundamentals/scope-tags) for your provisioning policy.
2. Select **Next**.

## Create assignments

1. On the **Assignments** page, choose **Select groups** &gt; choose the groups you want this policy assigned to &gt; **Select**. Nested groups aren't currently supported.

    - For Windows 365 Flex in Dedicated mode, you must also select a Cloud PC size for each group in the policy. Choose **Select one** &gt; select a size under **Available sizes** &gt; **Select**.

        - Optional. You can create an assignment to reserve licenses for the group members by following these steps:
            1. Under **Assignment**, enter an **Assignment name**.
            2. For **Number of licenses**, enter the number of licenses that you want to reserve for the group. You can also see the number of unassigned licenses.
    - For Windows 365 Flex in Shared mode you must:

        1. Choose **Select one** &gt; select a size under **Available sizes** &gt; **Select**.
        2. Type in a **Friendly name** &gt; select a **Cloud PC number** &gt; **Next**. The **Friendly name** shows up in the end user's Windows app.
2. Select **Next**.

## Review and create

On the **Review + create** page, select **Create**. If you used Microsoft Entra hybrid join as the join type, it can take up to 60 minutes for the policy creation process to complete. The time depends on when the Microsoft Entra Connect sync last happened.

After the provisioning policy is created and assigned, Windows 365 automatically starts to provision Cloud PCs.