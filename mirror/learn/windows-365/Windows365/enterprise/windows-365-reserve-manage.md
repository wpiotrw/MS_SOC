---
layout: Conceptual
title: Managing Windows 365 Reserve | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-365-reserve-manage
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to set up and manage Windows 365 Reserve for temporary Cloud PC access.
author: losillim
ms.author: losillim
ms.service: windows-365
ms.topic: get-started
ms.date: 2026-09-16T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 64a1df45-669b-5c70-f477-3e0c1e8b23d5
document_version_independent_id: 64a1df45-669b-5c70-f477-3e0c1e8b23d5
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-365-reserve-manage.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-365-reserve-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-365-reserve-manage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: edbb0907-cecb-e502-b00a-f57531b0f501
---

# Managing Windows 365 Reserve | Microsoft Learn

This guide is for IT administrators who need to deploy and manage Windows 365 Reserve. 

The content is organized into two main areas: 

- **Set up**: Initial tasks to complete before deployment.
- **Manage**: Ongoing actions for operations.

## Set up Windows 365 Reserve

### Prerequisites

#### User licensing

- Each user requires a **Windows 365 Reserve license**.
- Licenses allow up to **10 days of Cloud PC access per year for one user**.
- Users must also have:
    - Windows 11 Enterprise or Windows 10 Enterprise
    - Microsoft Intune
    - Microsoft Entra ID P1

For details, see [Windows 365 Reserve licensing](windows-365-reserve-license)

Note

Windows 365 Reserve doesn't require Azure AD DS or on-premises domains. Windows 365 Reserve Cloud PCs are always Microsoft Entra-joined on the Microsoft Hosted Network. 

#### Role-based access control

To manage Windows 365 Reserve, assign these roles to admins in Microsoft Entra ID and Intune: 

- Required: Windows 365 administrator
- Recommended:
    - Intune administrator (for managing reports and other Intune features)
    - User administrator (for managing Microsoft Entra security groups)

For details, see [Role-based access control](role-based-access). 

### Environment setup

- **Microsoft Intune**: Apply user-targeted policies and apps for a consistent experience. For details, see [Apply features and settings on your devices using device profiles in Microsoft Intune](/en-us/intune/intune-service/configuration/device-profiles)
- **Network**: Ensure corporate firewalls aren't blocking the Windows 365 Service. For details, see [Windows 365 network requirements](requirements-network)
- **Microsoft Entra Join**: Confirm readiness for Microsoft Entra join endpoints. [Plan your Microsoft Entra join implementation](/en-us/entra/identity/devices/device-join-plan)
- **Microsoft Entra Group**: Create or use an existing group for provisioning policy assignment. [Manage Microsoft Entra groups and group membership](/en-us/entra/fundamentals/how-to-manage-groups)

### Create a Reserve provisioning policy

Provisioning policies define Cloud PC settings, such as geography, language, and image type. 

Important

To allocate Windows 365 Reserve licenses, assign a Microsoft Entra Group to a Reserve provisioning policy. You can provision a user's Cloud PCs starting seven days after assigning that user a license. Plan ahead by creating and assigning policies well before you need to provision Cloud PCs. 

#### Steps

1. In Intune, go to **Devices** &gt; **Provision Cloud PCs** and select **Create policy**.
2. Under **Basics**, enter a name and description.
3. [Only for Windows 365 Enterprise and Windows 365 Flex customers] Under **Experience**, select **Access a full Cloud PC**. Under **License type**, select **Reserve**.
4. Choose **Geography** for Reserve Cloud PCs.
5. [Optional] Change the gallery image.
6. [Optional] Configure Device Preparation Policy

    1. Note: Autopilot Device Preparation (DPP) is now generally available for Windows 365 Reserve provisioning policies. When enabled, required applications and configurations are applied during provisioning before users can connect to the Cloud PC. Cloud PCs using DPP will show a Preparing status while setup is in progress.
7. [Optional] Adjust language, region, and naming settings.
8. [Optional] Add scope tags.
9. Under **Assignments**, add user groups.
10. Review settings and select **Create**.

## Configure Windows 365 Settings for Reserve

### Windows App setting: Enable users to provision new Cloud PC instances

User-initiated provisioning is an optional capability in Windows 365 Reserve that enables faster recovery and continuity for users. When turned on, users can initiate Cloud PC provisioning directly from the Windows App, without waiting for IT to take action, allowing them to get back to work as quickly as possible.

This feature is off by default and fully governed by IT. Administrators control availability through Windows App settings for Windows 365 in Microsoft Intune, where the setting can be enabled and scoped to specific Microsoft Entra ID user groups. These controls allow organizations to provide additional flexibility to selected users while maintaining centralized governance and security boundaries.

#### Admin steps

1. In Intune, go to **Devices &gt; Windows 365 &gt; Settings** and select **Create &gt; Windows App settings**.
2. Under **Basics**, enter a name and description.
3. Under **Configuration settings**, toggle **Enable users to provision new Cloud PC instances** to **Enabled**. Note: this setting applies only to user groups assigned to Reserve provisioning policies & licensed for Reserve.
4. Add scope tags (optional).
5. Under Assignments, add user groups.
6. Review settings and select Create.

### Resulting experience

Once the setting is applied, eligible users see the option to provision a Cloud PC in the Windows App and can start the provisioning process themselves. IT retains the ability to provision Cloud PCs as before; user-initiated provisioning simply extends that capability to end users when permitted, reducing dependency on support workflows without changing existing administrative ownership or management responsibilities.

#### User steps

1. In the Windows App or web, users log in with credentials.
2. When their Reserve Cloud PC is not provisioned, users will see a new device card that says Set up my Cloud PC and select it.
3. Users will see a consent prompt and must confirm they wish to create their Reserve Cloud PC.
4. Confirmation kicks off provisioning, and the Device card will change to show the provisioning status.

## Manage Windows 365 Reserve

### Manage provisioning policies

Navigate to **Devices** &gt; **Provision Cloud PCs** in Intune. Use filters or search to locate your Windows 365 Reserve provisioning policy link. 

### Provision a Reserve Cloud PC from Intune

Reserve Cloud PCs are provisioned manually.

Important

**The 10-day access period starts when the Cloud PC is provisioned**. Provision on-demand when needed to avoid unnecessary license consumption.

#### Steps

1. In Intune, open the provisioning policy and select **Cloud PC Users**.
2. Select one or more users and choose **Provision**.
3. Confirm in the dialog box. 

    Bulk provisioning: Verify the selected users, then select **Create** in the Bulk device action wizard. Bulk provisioning now supports up to 1,000 devices per request (in Public Preview).
4. Monitor status changes from **Not Provisioned** to **Provisioned**.

### Deprovision a Reserve Cloud PC

Important

**Deprovisioning pauses the 10-day access period and deletes the Cloud PC and all non-backed-up data.** Admins can deprovision from Intune and users can deprovision (Return) their Cloud PC in the Windows App. Both actions require confirmation through a second consent prompt and require admin action to provision the Cloud PC again. There are no snapshots taken or grace periods when admins or users deprovision; so, ensure users back up important data before deprovisioning.

Deprovision as soon as the device is no longer needed to conserve remaining days of access for later in the license term. 

#### Steps

1. Go to **Cloud PC Users** under your policy.
2. Select one or more Cloud PCs and choose **Deprovision** now.
3. Confirm in the dialog box.

Bulk deprovisioning: Verify the selected users, then complete the steps on the Bulk device action wizard. Bulk deprovisioning now supports up to 1,000 devices per request (in Public Preview).

1. Monitor to ensure status changes from **Provisioned** to **Not provisioned**.

Note

Alternatively, bulk provisioning and deprovisioning of Reserve Cloud PCs can also be initiated from the Bulk device action wizard under All Devices.

### Monitor and manage Reserve Cloud PCs

- **Provisioning policies**: Filter by License Type = Reserve.
- **Reports**:
    - Windows 365 Reserve licensing
    - **All Cloud PCs**: Filter License Type = Reserve.

## End Users: Connect to Windows 365 Reserve Cloud PC

1. Open the Windows App or web client on any supported device.
2. Sign in with organization credentials.
3. Filter by **Windows 365** to find the Reserve Cloud PC once it's provisioned.
4. From the device card, launch the Cloud PC and access actions like restart or reset.
5. Check the **Reserve** tag to see the date your access expires.

## Related links

- [What is Windows 365 Reserve?](introduction-windows-365-reserve)
- [Windows 365 Reserve licensing](windows-365-reserve-license)
- [Windows 365 Reserve FAQ](windows-365-reserve-faq)