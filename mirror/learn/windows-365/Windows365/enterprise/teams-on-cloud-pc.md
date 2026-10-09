---
layout: Conceptual
title: Microsoft Teams on Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/teams-on-cloud-pc
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about using Microsoft Teams on a Cloud PC.
keywords: 
author: ErikjeMS
ms.author: pavithir
manager: dougeby
ms.date: 2024-07-01T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: spatnaik
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: a9ff2fbe-211b-8ef3-b04e-d10e11891bf8
document_version_independent_id: a9ff2fbe-211b-8ef3-b04e-d10e11891bf8
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/teams-on-cloud-pc.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/teams-on-cloud-pc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/teams-on-cloud-pc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 6dd0ad2a-2370-53bd-beb6-f174704e29b7
---

# Microsoft Teams on Cloud PCs | Microsoft Learn

Microsoft Teams is one of the core Microsoft 365 applications used with Windows 365. The [Windows 10/11 images optimized for Microsoft 365 apps](device-images#gallery-images) available in the Windows 365 image gallery support Teams chat, presence, calling, and meeting optimizations. Gallery images use the new [Microsoft Teams](/en-us/microsoftteams/new-teams-desktop-admin).

Using Microsoft Teams on a Cloud PC is different from using it on a physical PC. You'll need to do the following to provide the best Teams experiences from Cloud PCs:

- Read the [requirements and limitations](/en-us/MicrosoftTeams/vdi-2) for using Microsoft Teams in virtualized environments.
- [Prepare your network](/en-us/microsoftteams/prepare-network/) for Microsoft Teams.
- Confirm that [required components](/en-us/azure/virtual-desktop/teams-on-avd) for Microsoft Teams optimizations are installed.
- Conform to [Cloud PCs sizing requirements](cloud-pc-size-recommendations) for Microsoft Teams.
- Conform to [End-user hardware requirements](../end-user-hardware-requirements) for Microsoft Teams.

## Teams optimizations

The [Windows 10/11 images](device-images#gallery-images) in the gallery are pre-configured with required optimization components. When you install and use new Microsoft Teams in your cloud PC, you get an optimized experience. These optimization components enable peer-to-peer audio and video calls from your physical endpoint to the other person's endpoint. This situation creates the same experience as you would have on a physical endpoint running Microsoft Teams.

Some of the key benefits of the optimizations are:

- High-performance peer-to-peer streaming facilitated by WebRTC and rendered directly on the endpoint.
- Devices are redirected as the same hardware device, resulting in better hardware redirection support.
- Windows 10/11 and macOS endpoints get all the benefits of the modern media stack, including HW video decoding.
- Teams optimization VDI 2.0 is currently supported, in preview, for macOS.

### Supported endpoints

Media optimization for Microsoft Teams is available on the following endpoints:

- [Windows App for Windows](/en-us/azure/virtual-desktop/teams-on-avd) via the Microsoft Store (ideally the latest version).
- Windows App for Windows, version 1.2.1026.0 or later.
- Windows App for macOS, version [11.13.2 MAU client](https://go.microsoft.com/fwlink/?linkid=868963) or later.
- Windows App for iOS and iPadOS, version 11.2.5 or later.
- Windows App for Android version 11.0.0.78 or later.

Note

Microsoft Teams installs during the first sign in to the Cloud PC. Installation can take a couple of minutes. Make sure to restart Teams to activate the AV optimizations that redirect audio and video. You can also sign out and in again to your Cloud PC to gain the same result.

## Collect Teams logs for Microsoft support

If you encounter issues with the Teams desktop app in your Windows 365 environment, collect client logs on the Cloud PC under

```
%appdata%\Microsoft\Teams\logs.txt
```

If you encounter issues with calls and meetings, collect Teams Web client logs with the key combination Ctrl + Alt + Shift + 1. Logs will be written on the Cloud PC to

```
%userprofile%\Downloads\MSTeams Diagnostics Log DATE_TIME.txt
```

### Contact Microsoft Teams support

For information on contacting Microsoft Teams support, see [Microsoft 365 admin center](/en-us/microsoft-365/admin/contact-support-for-business-products).