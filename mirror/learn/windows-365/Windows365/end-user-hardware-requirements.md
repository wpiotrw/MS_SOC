---
layout: Conceptual
title: End-user hardware requirements in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/end-user-hardware-requirements
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about the hardware requirements for end-users to access their Cloud PC.
keywords: 
author: ErikjeMS
ms.author: erikje
manager: dougeby
ms.date: 2025-01-06T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: 
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: alcort
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier1
locale: en-us
document_id: 3dd6e190-ad57-82c3-a365-a18bdb4d55cc
document_version_independent_id: 3dd6e190-ad57-82c3-a365-a18bdb4d55cc
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/end-user-hardware-requirements.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: end-user-hardware-requirements
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/end-user-hardware-requirements.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: b8d7bfdd-9812-b87b-f9c5-f6acce9a4a74
---

# End-user hardware requirements in Windows 365 | Microsoft Learn

To access their Cloud PC, an end-user's hardware must meet certain requirements. These requirements vary depending on which Microsoft Remote Desktop client the end-user installs.

## Windows App

For more information about the requirements of running and using Windows App, see [Get started with Windows App](/en-us/windows-app/get-started-connect-devices-desktops-apps).

## Microsoft Remote Desktop client for Windows

Downloads available for:

- [Windows 64-bit](https://go.microsoft.com/fwlink/?linkid=2068602)
- [Windows 32-bit](https://go.microsoft.com/fwlink/?linkid=2098960)

Hardware requirements:

- **Operating systems**: Windows 10/11, Windows 8.1, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2
- **CPU**: 1vCPU with 1 GHz or faster processor
- **RAM**: 1024 MB
- **Hard drive**: 100 MB or more
- **.NET Framework version**: 4.6.1 or later
- **Video**: DirectX 9 or later with WDDM 1.0 driver

If you'll be using Microsoft Teams on the Cloud PCs, the Windows device requirements increase to:

- **CPU**: At least 2vCPU with Minimum 1.6 GHz or faster processor. For higher video/screen share resolution and frame rate, a four-core processor or better is recommended.
- **RAM**: 4096 MB
- **Hard drive**: 3 GB or more
- **.NET Framework version**: 4.6.1 or later
- **Video**: DirectX 9 or later with WDDM 1.0 driver. Background video effects require Windows 10/11 or a processor with AVX2 instruction set. Also, Teams audio and video offloading on a Cloud PC benefits from a dedicated Graphics Processing Unit (GPU) within the device.

## Microsoft Remote Desktop client for Windows from the Microsoft Store

Download from the [Microsoft Store](https://www.microsoft.com/store/p/microsoft-remote-desktop/9wzdncrfj3ps).

Hardware requirements:

- **Operating systems**: Windows 10 1703 or later
- **CPU**: 1 GHz or faster processor
- **RAM**: 1024 MB
- **Hard drive**: 100 MB or more
- **Video**: DirectX 9 or later with WDDM 1.0 driver. Teams audio and video offloading on Cloud PC benefits from a dedicated Graphics Processing Unit (GPU) within your physical endpoint device.

## macOS, iOS/iPadOS, and Android

You can install the client and find requirements for other platforms here:

- [macOS](https://itunes.apple.com/app/microsoft-remote-desktop/id1295203466?mt=12)
- [iOS/iPadOS](https://aka.ms/rdios)
- [Android](https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx)

## Linux

You can access Windows 365 Cloud PCs from your Linux OS devices by using:

- The web client available at windows365.microsoft.com.
- Third-party clients to connect to Azure Virtual Desktop, including:

    - [Dell](https://www.dell.com/en-us/lp/dell-thinos)
    - [HP](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=c07051097)
    - [IGEL](https://www.igel.com/igel-solution-family/)

    Third-party Linux client solutions can't be managed by using Microsoft Intune. The partner provides a separate management tool for Linux devices.