---
layout: Conceptual
title: Windows update management methodologies for session hosts - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/windows-update-management-methodologies-session-hosts
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: NeoCai
manager: eliotgra
ms.author: neocai
ms.service: azure-virtual-desktop
description: Learn the supported methods to update and service Azure Virtual Desktop session hosts, including monthly updates, feature updates, and OS version upgrades.
ms.topic: overview
ms.reviewer: sugopina
ms.date: 2026-08-28T00:00:00.0000000Z
locale: en-us
document_id: 7e2aff78-bddd-6540-c8a8-6d5e908c7319
document_version_independent_id: 7e2aff78-bddd-6540-c8a8-6d5e908c7319
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/windows-update-management-methodologies-session-hosts.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: windows-update-management-methodologies-session-hosts
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/windows-update-management-methodologies-session-hosts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: 99463b6d-7fc9-c32b-bbff-e4379ac01dca
---

# Windows update management methodologies for session hosts - Azure Virtual Desktop | Microsoft Learn

Azure Virtual Desktop (AVD) supports multiple session host operating systems and servicing approaches. The right update strategy depends on several factors:

- The session host operating system: Windows client Enterprise, Windows client multi-session, or Windows Server.
- The type of update: monthly security and quality updates, feature updates, or OS version upgrades.
- The servicing model: patch in-place or image-based servicing.

This article gives an overview of the supported update methods for AVD session hosts. The following table explains what each recommendation marker means.

| Marker | Meaning |
| --- | --- |
| Recommended | Supported and the preferred method for this operating system. |
| Supported | Works and is an acceptable choice. It's not the single preferred method for this operating system. |
| Not recommended | Works, but discouraged for this operating system. A better option is available. |
| Not supported | Shouldn't be used for, or doesn't apply to, this operating system. |

## Supported session host operating systems

The first step in choosing a servicing approach is to identify the session host operating system and host pool type.

| Host pool type | Windows client Enterprise^1^ | Windows client multi-session | Windows Server |
| --- | --- | --- | --- |
| Personal | Supported | Not supported | Supported |
| Pooled | Not recommended^2^ | Supported | Supported |

^1. Also known as Windows client single-session.^^2. Session density set to 1 (session limit).^

## Monthly security and quality updates

Monthly updates include security updates, quality updates, and the latest cumulative updates (LCUs). The recommended delivery method depends on the session host operating system.

| Delivery method | Windows client Enterprise | Windows client multi-session | Windows Server |
| --- | --- | --- | --- |
| Windows Update | Recommended | Not recommended | Supported |
| Windows Autopatch (WUfB) | Recommended | Not recommended | Not supported |
| Configuration Manager | Supported | Supported | Supported |
| Azure Update Manager | Not supported | Not supported | Recommended |
| Automatic guest patching | Not supported | Not supported | Recommended |
| Session host update | Not supported | Recommended | Not recommended |
| Azure Compute Gallery | Not recommended | Recommended | Not recommended |

### Hotpatch considerations for monthly updates

Hotpatching applies eligible monthly security updates without requiring a reboot. It's supported on Windows Server Azure Edition and on Windows 11 Enterprise, version 24H2 or later, when virtualization-based security (VBS) is enabled and updates are managed through Windows Autopatch and Microsoft Intune.

| Operating system | Hotpatch support |
| --- | --- |
| Windows client Enterprise | Supported on Windows 11 Enterprise, version 24H2 or later, with VBS enabled. |
| Windows client multi-session | Supported. |
| Windows Server | Supported on Azure Edition only. |

## Feature updates

Feature updates, including enablement package (eKB) updates, introduce new Windows features. For example, moving from Windows 11, version 24H2 to Windows 11, version 25H2. Feature updates don't apply to Windows Server.

| Delivery method | Windows client Enterprise | Windows client multi-session | Windows Server |
| --- | --- | --- | --- |
| Windows Update | Recommended | Not recommended | Not supported |
| Windows Autopatch (WUfB) | Recommended | Not recommended | Not supported |
| Configuration Manager | Supported | Supported | Supported |
| Windows Server Update Services (WSUS) | Not supported | Not recommended | Not recommended |
| Session host update | Not supported | Recommended | Not recommended |
| Azure Compute Gallery | Not recommended | Recommended | Not supported |
| In-place (Setup.exe or ISO) | Not recommended | Not supported | Not supported |

## OS version upgrades

An OS version upgrade moves a session host to a new operating system version. For example, Windows Server 2022 to Windows Server 2025, or Windows 10 to Windows 11.

The recommended method is to deploy new virtual machines (VMs) that use an image for the target OS version. For more information about in-place upgrades, see [Perform an in-place upgrade of a Windows VM in Azure](/en-us/troubleshoot/azure/virtual-machines/windows/in-place-system-upgrade).

| Delivery method | Windows client Enterprise | Windows client multi-session | Windows Server |
| --- | --- | --- | --- |
| In-place (Setup.exe or ISO) | Not supported | Not supported | Not supported |
| New VM deployment from a new image (Azure Compute Gallery) | Recommended | Recommended, using session host update | Recommended |

## Choose the right servicing model

Each delivery method maps to one of two servicing models: patch in-place or image-based servicing.

| Delivery method | Servicing model |
| --- | --- |
| Windows Update or Windows Autopatch (WUfB) | Patch in-place |
| Microsoft Intune | Patch in-place |
| Microsoft Configuration Manager | Patch in-place |
| Azure Update Manager | Patch in-place |
| Automatic guest patching | Patch in-place |
| WSUS | Patch in-place |
| Setup.exe or ISO | Patch in-place |
| Session host update | Image-based servicing |
| Azure Compute Gallery or new VM deployment from a new image | Image-based servicing |

### Patch in-place

Patch in-place updates the existing session host VM without replacing it. It's typically used for monthly cumulative updates, security updates, and Windows Server patching. Common, recommended technologies include Windows Update, Windows Autopatch (WUfB), Microsoft Intune, Azure Update Manager, automatic guest patching, WSUS, and Microsoft Configuration Manager.

### Image-based servicing

Image-based servicing creates a new image version and deploys updated session hosts. The typical workflow is to update the base image, validate applications and configurations, publish a new Azure Compute Gallery image version, deploy new session hosts, then drain and remove the old session hosts. When a session host is updated through image-based servicing, user data and local storage isn't saved.

Image-based servicing through [session host update](session-host-update) is recommended for pooled AVD environments because it provides consistent host configuration, easier rollback, and reduced impact to active user sessions.