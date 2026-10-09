---
layout: Conceptual
title: What is Windows 365 Reserve? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/introduction-windows-365-reserve
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Windows 365 Reserve provides organizations with short-term Cloud PC access to maintain productivity during unexpected disruptions. Learn how this offering supports business continuity by enabling quick, secure access to pre-configured Cloud PCs when physical devices are unavailable.
author: losillim
ms.author: losillim
ms.service: windows-365
ms.topic: overview
ms.date: 2026-07-09T00:00:00.0000000Z
locale: en-us
document_id: 1f733387-54fd-66a0-a75c-a3971fa2b524
document_version_independent_id: 1f733387-54fd-66a0-a75c-a3971fa2b524
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/introduction-windows-365-reserve.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/introduction-windows-365-reserve
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/introduction-windows-365-reserve.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: aba2be3d-2dfc-099f-d336-7d70bab0758f
---

# What is Windows 365 Reserve? | Microsoft Learn

Windows 365 Reserve is a version of [Windows 365](overview) designed for users who primarily work on physical PCs. It provides organizations with flexible, short-term Cloud PC access to keep employees productive during unexpected disruptions. This offering supports business continuity by enabling quick, secure access to Cloud PCs when physical devices are unavailable. 

## Overview

Windows 365 Reserve allows organizations to assign employees licenses with an annual term that grants up to **10 days of Cloud PC access per user, per year**. Reserve Cloud PCs are provisioned when needed, reducing costs and operational complexity compared to providing physical loaner devices or full-usage Cloud PC licenses. 

## Common scenarios

- Device loss, theft, or damage
- Delays in hardware shipments
- Outages or cyber incidents
- Short-term staffing needs
- Trials or testing environments

## Licensing

- Each user requires a Windows 365 Reserve license.
- Each license allows up to 10 days of Cloud PC access per year for one user.

For prerequisites and more licensing information, see [Windows 365 Reserve licensing](windows-365-reserve-license). 

## How it works

### For IT administrators

Windows 365 Reserve management is integrated with Microsoft Intune. 

- **Set up**:

    - Create provisioning policies, user assignments, and settings in advance to ensure Windows 365 Reserve is ready for fast Cloud PC deployment when you need it.
    - Create or use existing Microsoft Intune policies so that Windows 365 Reserve automatically pre-loads Cloud PCs with your organization's apps, settings, and security policies.
    - Optionally, configure Windows 365 Windows App Settings to allow users to provision Reserve Cloud PCs directly from the Windows App.
- **Deploy**: When users need Windows 365 Reserve Cloud PCs, provision them from Intune or enable the Windows App setting that allows users to initiate provisioning from the Windows App.
- **Monitor and manage**: Track licensing and usage in Intune. Deprovision Cloud PCs that are no longer needed to preserve remaining access days for later in the license term.

### For users

Windows 365 Reserve can be accessed from any device and is designed for a seamless experience. 

- **Connect**: After provisioning, users sign in with work credentials to the Windows App or web portal on any device (Windows, Mac, iOS, Android) and click to connect.
- **Monitor and manage**: Users can view a description of their Windows 365 Reserve Cloud PC, view available access time, and take limited actions, such as Restarting, Resetting, or Returning (deprovisioning) the Cloud PC on their device card in the Windows App or web portal.

## Key benefits

### Quickly restore end-user productivity

When a user’s primary device is unavailable, their productivity can stall for days while their device is repaired or replaced. Windows 365 Reserve enables organizations restore productivity fast by providing secure, short-term access to a Cloud PC so users can keep working while waiting for their main device to be available.

With Windows 365 Reserve admins can:

- Provision Cloud PCs when needed from Microsoft Intune to minimize downtime or allow users to provision themselves to reduce IT load.
- Prepare Cloud PCs with preconfigured apps and policies using Microsoft Intune
- Provide a consistent experience from any device via the Windows App, backed by reliable Windows Cloud performance

### Centralized IT management

IT admins can manage physical and Cloud PCs together in Microsoft Intune, streamlining oversight and reducing complexity.

Windows 365 Reserve offers:

- Simple setup; no specialized cloud or virtualization expertise required
- Lower operational overhead through policy-based management

### Secure by design

Security is a top priority for organizations. Windows 365 Reserve provides secure short-term access to corporate data and apps from any device. Sensitive data stays in the cloud, reducing risk even when users connect from outside the corporate network.

Managing Cloud PCs through Microsoft Intune helps admins:

- Consistently apply corporate security policies to physical devices and Cloud PCs
- Enable safe connections from unmanaged devices with security settings like conditional access policies

### Microsoft Purview Customer Key

Supported for Windows 365 Reserve Cloud PCs. Newly provisioned Cloud PCs are encrypted using Customer Key once the capability is enabled in Microsoft Purview.

Learn more about [Microsoft Purview Customer Key setup and support for Windows 365](/en-us/windows-365/enterprise/purview-customer-key).