---
layout: Conceptual
title: Resize multiple Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/resize-cloud-pc-bulk
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to resize multiple Cloud PCs by using Microsoft Intune.
keywords: 
author: ErikjeMS
ms.author: abpineda
manager: dougeby
ms.date: 2025-04-28T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: abpineda
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: f1bca889-d00d-8c12-8956-56bb84e7be00
document_version_independent_id: f1bca889-d00d-8c12-8956-56bb84e7be00
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/resize-cloud-pc-bulk.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/resize-cloud-pc-bulk
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/resize-cloud-pc-bulk.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 5f978dfc-396d-eb90-a144-582c60be6399
---

# Resize multiple Cloud PCs | Microsoft Learn

You can resize Cloud PCs in bulk using Microsoft Intune.

Resizing in bulk can have large scale impact. Before resizing a large group of Cloud PCs, try resizing a small group. This step helps familiarize you with the process.

Up to 5,000 Cloud PCs can be resized at a time.

For more information about resizing a single Cloud PC, see [Resize a single Cloud PC](resize-cloud-pc-single).

For more information about resizing, see [Cloud PC resizing overview](resize-cloud-pc).

## Requirements

### Role requirements

To resize a Cloud PC, the admin must have certain built-in Microsoft Entra roles.

- For a Cloud PC provisioned with a direct assigned license, at least one of the following roles
    - Intune Service Administrator
    - Intune Reader + Cloud PC Admin roles
    - Intune Reader + Windows 365 Administrator
- For a Cloud PC provisioned with a group-based license, at least one of the following roles
    - Intune Service Administrator
    - Intune Reader + Windows 365 Administrator
    - In addition to one of the previous three roles, a role with Microsoft Entra group read/write membership and licensing permissions, like the Windows 365 Admin role.

Alternatively, you can assign a custom role that includes the permissions of these built-in roles.

### IP address requirements

When you resize a Microsoft Entra hybrid join bring-your-own-network Cloud PC, a second IP address must be available in the subnet for the Cloud PC to be resized.

During the resizing operation, a second IP address is used when moving to the new size. This precaution makes sure that the Cloud PC can be rolled back to the original should an issue occur.

To account for this precaution, you can:

- Make sure that adequate IP addresses are available in the vNET for all Cloud PCs to be resized, or
- Stagger your resize operations to make sure that the address scope is maintained.

If inadequate addresses are available, resize failures can occur.

### Other requirements

In order to use **Resize** there must be available licenses in the inventory for the resized Cloud PC configuration.

To **Resize** a Cloud PC, it must have a status of **Provisioned** in the Windows 365 provisioning node.

Important

Before triggering a resize for Windows 365 Enterprise Cloud PCs, ensure that you are following best license assignment practices. Resizing Cloud PCs is simpler when using discrete Entra groups for licensing that are different from the Entra groups used for provisioning policy targeting. For more information, follow [Provisioning in Windows 365 | Microsoft Learn](/en-us/windows-365/enterprise/provisioning)

## Bulk resize Cloud PCs originally provisioned with directly assigned licenses

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **All Devices** &gt; **Bulk device actions** &gt; **OS (Windows)** &gt; **Select device type (Cloud PCs)** &gt; **Device action (Resize)**.
2. On the **Basics** page, select the **Source size** for the Cloud PCs to be resized.
3. Select the **Target size** for the resized Cloud PCs &gt; **Next**.
4. On the **Devices** page, choose **Select individual devices across your environment** &gt; **Next**.
5. Under **Select devices**, choose the devices that you want to resize &gt; **Next**.
6. On the **Review + create** page, select **Create**.

## Bulk resize Cloud PCs originally provisioned with group-based licenses

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **All Devices** &gt; **Bulk device actions** &gt; **OS (Windows)** &gt; **Select device type (Cloud PCs)** &gt; **Device action (Resize)**.
2. On the **Basics** page, select the **Source size** for the Cloud PCs to be resized.
3. Select the **Target size** for the resized Cloud PCs &gt; **Next**.
4. On the **Devices** page, choose **Apply this action to the devices registered to its group members** &gt; **Next**.
5. Under **Select groups to include**, choose the groups containing the users who own the devices that you want to resize &gt; **Next**.
6. On the **Review + create** page, select **Create**. The user’s Cloud PC is placed in the **Resize pending license** state as can be seen in the Windows 365 provisioning blade.
7. Select **Groups** &gt; select the group that you're changing &gt; **Licenses** &gt; select the old license &gt; **Remove license** &gt; **Yes** &gt; **Save**. Repeat this step for each group that you want to change.
8. Select **Assignments** &gt; select the license that you want to resize the Cloud PCs to &gt; **Save**. The users' Cloud PC starts resizing, which you can check in the Windows 365 provisioning blade.

## Bulk resize a subset of Cloud PCs originally provisioned using group-based licenses

1. Create a new target Microsoft Entra group. Add the users from the source Microsoft Entra group that you want to resize. Alternately, you can use existing Microsoft Entra groups if you're mapping the groups to individual Windows 365 license types.
2. Assign the existing provisioning policy targeting the original source Microsoft Entra group to the new target Microsoft Entra group. You only need to do this step if you don't have a discrete Microsoft Entra group for your provisioning policy assignment. If you have discrete Microsoft Entra groups to manage your provisioning policy assignments, you can omit this step.
3. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **All Devices** &gt; **Bulk device actions** &gt; **OS (Windows)** &gt; **Select device type (Cloud PCs)** &gt; **Device action (Resize)**.
4. On the **Basics** page, select the **Source size** for the Cloud PCs to be resized.
5. Select the **Target size** for the resized Cloud PCs &gt; **Next**.
6. On the **Devices** page, choose **Apply this action to the devices registered to its group members** &gt; **Next**.
7. Under **Select groups to include**, choose the groups containing the users who own the devices that you want to resize &gt; **Next**.
8. On the **Review + create** page, select **Create**. The user’s Cloud PC is placed in the **Resize pending license** state as can be seen in the Windows 365 provisioning blade.
9. To complete the resize, the following two licensing actions must be completed:

    - The original (source) license must be removed.
    - The new (target) license must be assigned. The order in which these licensing actions occur **does not matter**. The resize begins only after both conditions are satisfied.
10. To retrieve the original license, remove the users from the original source Microsoft Entra group.

    - If the original license is removed but the target license isn’t assigned within **48 hours**, the Cloud PCs go into a **grace period**.
    - If the original license isn’t removed and the target license isn’t assigned within **48 hours**, the Cloud PCs return to the **Provisioned** state.
    - When using Microsoft Entra ID hybrid in your environment, after removing users from the original group, you must wait until Microsoft Entra Connect synchronizes your on‑premises Active Directory with Microsoft Entra ID. This synchronization can take up to **30 minutes**. After synchronization completes, you can add the users to the new target group.

    1. Assign the target license by adding the users to the new target Microsoft Entra group. Once both the source license is removed and the target license is assigned, the resizing process begins.
    2. If the wrong target license is assigned, the Cloud PCs are provisioned matching the configuration of that license.