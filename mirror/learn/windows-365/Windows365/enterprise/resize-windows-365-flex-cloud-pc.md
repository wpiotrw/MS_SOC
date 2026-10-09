---
layout: Conceptual
title: Resize Windows 365 Flex Cloud PCs in Dedicated mode | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/resize-windows-365-flex-cloud-pc
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to resize Windows 365 Flex Cloud PCs in Dedicated mode.
keywords: 
author: ErikjeMS
ms.author: abpineda
manager: dougeby
ms.date: 2025-03-06T00:00:00.0000000Z
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
ai-usage: ai-assisted
locale: en-us
document_id: 9e37f294-2bea-f94d-8312-5bf449aa321b
document_version_independent_id: 9e37f294-2bea-f94d-8312-5bf449aa321b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/resize-windows-365-flex-cloud-pc.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/resize-windows-365-flex-cloud-pc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/resize-windows-365-flex-cloud-pc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 5f3c0a05-af44-bdc3-e1ef-0910ae6cd98e
---

# Resize Windows 365 Flex Cloud PCs in Dedicated mode | Microsoft Learn

You can use a provisioning policy to resize Windows 365 Flex Cloud PCs in Dedicated mode.

Windows 365 Flex Cloud PCs in Shared mode can't be resized.

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

## Use a provisioning policy to resize Windows 365 Flex Cloud PCs in Dedicated mode

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Windows 365** &gt; **Provisioning policies**.
2. Select a provisioning policy that includes an assignment with the Windows 365 Flex Cloud PCs in Dedicated mode that you want to resize.
3. On the policy page, select **Edit** next to **Assignments**.
4. On the **Assignments** tab, in the **Cloud PC size** column, select the Windows 365 Cloud PC Flex entry that you want to resize. All Cloud PCs in the assignment will be resized.
5. In the **Select Cloud PC size** pane, under **Available sizes**, select the new Cloud PC size &gt; **Next**.
6. On the **Assignments** page, select **Next**.
7. On the **Review + save** tab, select **Update** to initiate the resize.

You can monitor the progress of the resize on the **All Cloud PCs** page and the [**Cloud PC actions** report](report-cloud-pc-actions).