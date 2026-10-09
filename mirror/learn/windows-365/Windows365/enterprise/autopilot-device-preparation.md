---
layout: Conceptual
title: Use Autopilot device preparation with Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/autopilot-device-preparation
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to use Autopilot device preparation with Cloud PCs.
keywords: 
author: ErikjeMS
ms.author: khyatishah
ms.date: 2025-04-02T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: ericor
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: a0ad0644-9fba-b0d6-3f41-f0ccfe315232
document_version_independent_id: a0ad0644-9fba-b0d6-3f41-f0ccfe315232
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/autopilot-device-preparation.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/autopilot-device-preparation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/autopilot-device-preparation.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4b132a0c-342a-42eb-91ff-8159e1ed413d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f2b71146-ce8e-46a8-9965-8aa8b3aa8235
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: a8c4c949-edcd-7fd0-3bd3-ffeaaf2bb18c
---

# Use Autopilot device preparation with Cloud PCs | Microsoft Learn

When provisioning Cloud PCs, you can optionally link [Autopilot device preparation](/en-us/autopilot/device-preparation/overview) to help make sure Windows 365 Cloud PCs for Enterprise, Windows 365 Flex in Shared mode, and Windows 365 Flex in Dedicated mode are provisioned with important Intune apps and scripts. Additionally, you can now use Intune Autopilot device preparation to publish Intune apps as Windows 365 Cloud Apps.

This feature is in [public preview](../public-preview) for Windows 365 Reserve licenses.

## Link device preparation policies to Cloud PCs

1. Meet the [Windows Autopilot device preparation requirements](/en-us/autopilot/device-preparation/requirements).
2. When [creating a new](create-provisioning-policy) or [editing an existing](edit-provisioning-policy) Windows 365 provisioning policy also complete the following steps:

    1. On the **Configuration** tab, for **Autopilot device preparation policy**, select a policy.
    2. For **Minutes allowed before device preparation fails**, enter a value that allows adequate time to install the apps and scripts defined in your policy. If the apps and scripts aren't finished installing by this time, the device preparation fails (but the provisioning continues).
    3. Optionally, you can select **Prevent users from connection to Cloud PC upon installation failure or time-out** option to force the provisioning result to **Failed** if there's a time-out or failure. If selected, Cloud PCs that fail to complete device preparation policy installation are marked as **Failed**. In this case, users can't connect to them. If not selected, Cloud PCs are marked as **Provisioned with warnings** and users can connect to their Cloud PCs.
3. Complete the remaining steps to [create a new](create-provisioning-policy) or [edit an existing](edit-provisioning-policy) Windows 365 provisioning policy.

    Windows 365 completes the provisioning process after:

    - The apps and scripts are successfully installed.
    - The time-out value expires.

Note

Windows 365 supports both Entra join and Hybrid Entra join during provisioning. Device Preparation can be used in provisioning policies with these features enabled.

## Monitor status of device preparation on Cloud PCs

To see the status of device preparation for Cloud PC provisioning, go to **Devices** &gt; **Enrollment** &gt; **Monitor** &gt; **Windows Autopilot device preparation deployment status**.