---
layout: Conceptual
title: Deprovision or end grace period for Cloud PCs in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/end-grace-period
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to end the grace period for Cloud PCs in Windows 365.
author: ErikjeMS
ms.author: mmoyaaceves
manager: dougeby
ms.date: 2026-09-27T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.reviewer: mattsha
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: c6062542-4500-4c95-c649-a64dd7a4ad83
document_version_independent_id: c6062542-4500-4c95-c649-a64dd7a4ad83
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/end-grace-period.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/end-grace-period
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/end-grace-period.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: d1ec829a-595c-d41b-00cb-3ceba5be7f80
---

# Deprovision or end grace period for Cloud PCs in Windows 365 | Microsoft Learn

When a Cloud PC is in a grace period, the user can continue using the Cloud PC for seven days. After the seven-day grace period expires, the user is logged off the Cloud PC. They’ll lose access and the Cloud PC will be [deprovisioned](lifecycle#deprovision).

There may be situations where you don't want to wait seven days for the grace period to end normally. In this case, you can use the **End grace period** option to immediately end the grace period.

## End grace period

1. Ending the grace period is a destructive action. Before ending the grace period, notify your users to be sure that they're fully aware of the impact.
2. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **All Cloud PCs**.
3. In the **Status** column of the list, select **In grace period** &gt; **Deprovision now** &gt; **Yes**.

    Important

    This is a destructive act. It will delete the operating system and data. The Cloud PC will no longer be available.

    After you select **Yes**, the following steps will happen automatically:

    1. The Cloud PC will start deprovisioning.
    2. The user loses access to the Cloud PC.
    3. The operating system and data are deleted from the Cloud PC. The Cloud PC is no longer available.
    4. If the original provisioning policy was replaced with a different policy, the Cloud PC will be reprovisioned with the settings in the new policy.

## Bulk deprovision

Windows 365 Enterprise Cloud PCs and Flex Cloud PCs created in Dedicated mode that are in grace period can be deprovisioned in bulk. Any data saved to individual Cloud PCs is removed and the user is no longer able to access the Cloud PC. There are two ways to initiate bulk deprovisioning. One is through the provisioning policy view and the other is through Intune's Bulk Action Wizard.

Tip

Ensure all Cloud PCs you select are in grace period. The **Deprovision** action may be blocked if a provisioned Cloud PC is selected. This does not apply for Reserve Cloud PCs. For further details see [Manage W365 Reserve](/en-us/windows-365/enterprise/windows-365-reserve-manage).

#### Provisioning Policy View

1. Deprovisioning is a destructive action. Before deprovisioning, notify your users to be sure that they're fully aware of the impact.
2. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; scroll down to **Manage W365 Cloud PCs** section &gt; select **Provision Cloud PCs**.
3. Search or select an Enterprise of Flex Dedicated provisioning policy &gt;head to the **Devices** tab &gt; select Cloud PCs in grace period.
4. Click **Deprovision** from the actions bar above. If you select multiple Cloud PCs, it will automatically redirect you to the Bulk Action Wizard.
5. Select **Next** to view the devices you have selected to deprovision &gt; then click **Next** to view the Review + Create tab.
6. Once the **Create** button is pressed, the Cloud PCs will be deprovisioned, all data will be lost and the action cannot be undone.

#### Intune Bulk Action Wizard

1. Deprovisioning is a destructive action. Before deprovisioning, notify your users to be sure that they're fully aware of the impact.
2. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; select **All devices** section &gt; click **Bulk device actions**.
3. In the Basics tab, select **Windows** as the OS, **Cloud PCs** as Device type, and **Deprovision** as your action.
4. After clicking **Next**, you may select individual devices or devices targeted to a specific user group. Click **Add devices** to begin selecting. Note only Enterprise or Flex Dedicated Cloud PCs **in grace period** and Reserve Cloud PCs will appear.
5. Select **Next** to view the devices you have selected to deprovision &gt; then click **Next** to view the Review + Create tab.
6. Once the **Create** button is pressed, the Cloud PCs will be deprovisioned, all data will be lost and the action cannot be undone.