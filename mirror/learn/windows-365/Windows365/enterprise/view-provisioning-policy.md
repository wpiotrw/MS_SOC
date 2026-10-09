---
layout: Conceptual
title: View provisioning policies for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/view-provisioning-policy
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn what configurations and actions are available when you view Windows 365 provisioning policies.
keywords: 
author: sezhen
ms.author: sezhen
ms.date: 2026-06-29T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
locale: en-us
document_id: 3d6e6c1d-80ea-974d-cf0f-912f5ce15e73
document_version_independent_id: 3d6e6c1d-80ea-974d-cf0f-912f5ce15e73
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/view-provisioning-policy.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/view-provisioning-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/view-provisioning-policy.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: b15dc8c0-27fc-26b1-c6d6-88bde3689098
---

# View provisioning policies for Windows 365 | Microsoft Learn

To view a Windows 365 provisioning policy, in the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) &gt; **Devices** &gt; **Provision Cloud PCs**, select a provisioning policy.

- **Overview**shows essential information, including the license type, created time, created by, last modified time, and last modified by.
    - Note that Created time and Created by only show values for provisoining policies created after October 2025.
- Use **Properties** to view and edit the policy properties and assignments. To learn which edits apply immediately and which require you to **Apply Configuration** or **Reprovision**, see [edit a provisioning policy](edit-provisioning-policy).
- **Devices** show the Cloud PCs provisioned from this policy. You can view and filter for provisioning, connectivity, and action statuses. You can also select multiple Cloud PCs to perform [bulk device actions](remotely-manage-cloud-pc).
- **Action Status** shows the status of all device actions for Cloud PCs in the policy. To view action status for all devices, see the [Cloud PC actions report](report-cloud-pc-actions).

For [Windows 365 Flex](introduction-windows-365-flex) in shared mode provisioning policies, there are also additional pivots based on your configuration:

- For policies with experience type [Cloud App](cloud-apps), you can use **Cloud Apps** to publish, edit, and add apps.
- For policies with [User Experience Sync](windows-365-flex-user-experience-sync) enabled, you can use **User storage** to view and manage storage information.

For [Windows 365 Reserve](introduction-windows-365-reserve) provisioning policies, you can provision Cloud PCs in **Cloud PC Users**.