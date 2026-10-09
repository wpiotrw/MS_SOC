---
layout: Conceptual
title: Enable Business Continuity and Disaster Recovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/business-continuity-disaster-recovery-setup
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Explains how to set up BCDR features (Point-in-Restore, Cross-region Disaster Recovery, Disaster Recovery Plus) in Cloud PC Settings.
author: golipreethi
ms.author: golipreethi
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.topic: how-to
ms.date: 2026-07-20T00:00:00.0000000Z
locale: en-us
document_id: e651dd76-cd81-d39a-02c5-e0147aa77155
document_version_independent_id: e651dd76-cd81-d39a-02c5-e0147aa77155
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/business-continuity-disaster-recovery-setup.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/business-continuity-disaster-recovery-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/business-continuity-disaster-recovery-setup.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 4af9d446-757c-9b7f-71f3-00447fad3636
---

# Enable Business Continuity and Disaster Recovery | Microsoft Learn

This article explains how to configure Business Continuity and Disaster Recovery (BCDR) features for Windows 365 Cloud PCs. BCDR features help protect Cloud PCs and support recovery during service interruptions.

## Prerequisites

Before you configure BCDR features, review the following articles:

- [Point-in-time Restore](/en-us/windows-365/enterprise/restore-overview)
- [Cross-region Disaster Recovery in Windows 365](/en-us/windows-365/enterprise/cross-region-disaster-recovery)
- [Disaster Recovery Plus](/en-us/windows-365/enterprise/disaster-recovery-plus)

Ensure that all licensing and service requirements described in those articles are met before proceeding.

## Configure BCDR settings

Important

Creating a new Cloud PC configuration to replace an existing User Setting doesn't result in the loss of existing backup copies, provided that the restore-point frequency and backup region remain unchanged.

1. In Microsoft Intune admin center, select the **Devices** tab.
2. Under **Manage Windows 365 Cloud PCs,** select **Cloud PC Settings.**
3. Select the **Create** button.
4. Select the **Cloud PC configurations** option from the dropdown.
5. Add a **Name** and **Description** (optional).
6. On the Configuration settings tab, navigate to **Business continuity and disaster recovery**.

    1. To configure **Point-in-time Restore**, select **Enable**. For Frequency of restore-point service, choose an interval for how often restore points will be created.
    2. To configure **Cross-Region Disaster Recovery** and/or **Disaster Recovery Plus**, select **Enable**. For Network type, select an option:

        1. **Microsoft-hosted network (MHN)**: Select the Geography and Region where your Cloud PC backups are created. Change the selection of regions as needed.
        2. **Azure network connection (ANC**): Your selected ANC determines where the Cloud PC backups are created. You must configure your ANC for your backup region to support the restored Cloud PC.
    3. Select an appropriate Geography. Select **Change selection** to update specific region groups and regions as needed. When configuring a backup location, consider things like data sovereignty and geographic distance between the user and the Cloud PC backup location. The greater the distance between your backup location and users, the greater the potential impact to latency and user experience.
7. Follow on-screen prompts until you reach the **Assignments** tab. Add the groups containing users that you want this Cloud PC Configuration applied to. All Cloud PCs associated with a user share the same BCDR setting.
8. Proceed to the **Review + create** tab and select **Create**.
9. Within the Cloud PC Settings tab, confirm that Cloud PC Configuration has been appropriately created.
10. Wait up to 24 hours before activating BCDR services.

Important

Devices that are actively in a temporary backup region will not receive the new Cloud PC Configuration until they return back to the primary region.

## Configure Disaster Recovery Plus control for end users

To allow or disallow end users to activate and deactivate DR Plus themselves, configure a Windows App setting.

1. In Microsoft Intune admin center, select the **Devices** tab.
2. Under **Manage Windows 365 Cloud PCs,** select **Cloud PC Settings.**
3. Select the **Create** button.
4. Select the **Windows App settings** option from the dropdown.
5. Add a **Name** and **Description** (optional).
6. For **Allow users to initiate Disaster Recovery Plus service**, select **Enable**.
7. Follow on-screen prompts until you reach the **Assignments** tab. Add the groups containing users that you want this Cloud PC Configuration applied to. All Cloud PCs associated with a user share the same DR Plus setting.
8. Proceed to the **Review + create** tab and select **Create**.
9. Within the Cloud PC Settings tab, confirm that the Windows App setting has been appropriately created.

## Activate and use BCDR features

The process for using each BCDR feature depends on the selected recovery option:

- To restore a Cloud PC to a previous state, see [Restore a single Cloud PC to a previous state](/en-us/windows-365/enterprise/restore-single-cloud-pc).
- To move users to a temporary backup region during a regional outage using Cross-region Disaster Recovery, see [Activate or deactivate Cross-region Disaster Recovery in Windows 365](/en-us/windows-365/enterprise/cross-region-disaster-recovery).
- To move users to a temporary backup region during a regional outage using Disaster Recovery Plus, see [Activate or deactivate Windows 365 Disaster Recovery Plus](/en-us/windows-365/enterprise/disaster-recovery-plus).