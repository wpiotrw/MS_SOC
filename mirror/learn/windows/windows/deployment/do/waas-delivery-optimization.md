---
layout: Conceptual
title: What is Delivery Optimization? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/deployment/do/waas-delivery-optimization
recommendations: true
adobe-target: true
ms.collection:
- tier3
- highpri
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
description: This article provides information about Delivery Optimization, a peer-to-peer distribution method in Windows 10 and Windows 11.
ms.service: windows-client
ms.subservice: itpro-updates
ms.topic: overview
author: cmknox
ms.author: carmenf
manager: bpardi
ms.localizationpriority: medium
ms.date: 2026-05-12T00:00:00.0000000Z
locale: en-us
document_id: dbd18083-5f38-c913-2304-a42742ea38f6
document_version_independent_id: dbd18083-5f38-c913-2304-a42742ea38f6
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/deployment/do/waas-delivery-optimization.md
site_name: Docs
depot_name: TechNet.win-deployment
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-deployment/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: do/waas-delivery-optimization
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/deployment/do/waas-delivery-optimization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: eee92821-2190-f4ca-2476-ed269449c590
---

# What is Delivery Optimization? | Microsoft Learn

> 
> **Looking for Group Policy objects?** See [Delivery Optimization reference](waas-delivery-optimization-reference) or the master spreadsheet available at the Download Center [for Windows 11](https://www.microsoft.com/en-us/download/details.aspx?id=104594) or [for Windows 10](https://www.microsoft.com/en-us/download/details.aspx?id=104678).

Windows updates, upgrades, and applications can contain packages with large files. Downloading and distributing updates can consume quite a bit of network resources on the devices receiving them. Delivery Optimization is a reliable HTTP downloader with a cloud-managed solution that allows Windows devices to download those packages from alternate sources if desired (such as other devices on the network and/or a dedicated cache server) in addition to the traditional internet-based servers (referred to as 'HTTP sources' throughout Delivery Optimization documents). You can use Delivery Optimization to reduce bandwidth consumption by sharing the work of downloading these packages among multiple devices in your deployment however, the use of peer-to-peer is optional.

To use either the peer-to-peer functionality or the Microsoft Connected Cache features, devices must have access to the Internet and Delivery Optimization cloud services. When Delivery Optimization is configured to use peers and Microsoft Connected Cache, to achieve the best possible content delivery experience, the client connects to Connected Cache and peers in parallel. If the desired content can't be obtained from Connected Cache or peers, Delivery Optimization seamlessly falls back to the HTTP source to get the requested content.

You can use Delivery Optimization with Windows Update, Windows Server Update Services (WSUS), Microsoft Intune/Windows Update client policies, or Microsoft Configuration Manager (when installation of Express Updates is enabled).

For information about setting up Delivery Optimization, including tips for the best settings in different scenarios, see [Set up Delivery Optimization](delivery-optimization-configure). For a comprehensive list of all Delivery Optimization settings, see [Delivery Optimization reference](waas-delivery-optimization-reference).

Note

WSUS can also use [BranchCache](../update/waas-branchcache) for content sharing and caching. If Delivery Optimization is enabled on devices that use BranchCache, Delivery Optimization is used instead.

## Requirements

The following table lists the minimum Windows 10 version that supports Delivery Optimization:

| Device type | Minimum Windows version |
| --- | --- |
| Computers running Windows 10 or later | Windows 10 1511 |
| Windows Server 2019 or later (Server Core included) | Windows Server 2019 |
| Windows IoT devices | Windows 10 1803 |

### Types of download content supported by Delivery Optimization

#### Windows Client and Server

Note

Delivery Optimization behaves slightly different on Windows Server. Windows Server 2019 (version 1809) or later is required, and the default DownloadMode (0) is used rather than the Windows client default of DownloadMode (1).

| Windows Client | Minimum Windows version | HTTP Downloader | Peer to Peer | Microsoft Connected Cache |
| --- | --- | --- | --- | --- |
| Windows Update ([feature updates, quality updates, language packs, drivers](../update/get-started-updates-channels-tools#types-of-updates)) | Windows 10 1511, Windows 11 | ✔️ | ✔️ | ✔️ |
| Windows 10/11 UWP Store apps | Windows 10 1511, Windows 11 | ✔️ | ✔️ | ✔️ |
| Windows 11 Win32 Store apps | Windows 11 | ✔️ |  |  |
| Windows Defender definition updates | Windows 10 1511, Windows 11 | ✔️ | ✔️ | ✔️ |
| Intune Win32 apps [Learn more](/en-us/intune/fundamentals/government-service) | Windows 10 1709, Windows 11 | ✔️ | ✔️\* | ✔️\* |
| Microsoft 365 apps and updates | Windows 10 1709, Windows 11 | ✔️ | ✔️ (excluding SAC Extended channel) | ✔️ |
| Edge browser updates | Windows 10 1809, Windows 11 | ✔️ | ✔️ | ✔️ |
| Configuration Manager Express updates | Windows 10 1709 + Configuration Manager version 1711, Windows 11 | ✔️ | ✔️ | ✔️ |
| Dynamic updates | Windows 10 1903, Windows 11 | ✔️ | ✔️ | ✔️ |
| MDM Agent | Windows 11 | ✔️ |  |  |
| Xbox Game Pass (PC) | Windows 10 1809, Windows 11 | ✔️ |  | ✔️ |
| Windows Package Manager | Windows 10 1809, Windows 11 | ✔️ |  |  |
| MSIX Installer | Windows 10 2004, Windows 11 | ✔️ |  |  |
| Teams updates | Windows 10 2004, Windows 11 | ✔️ | ✔️ (starting with version 25122.1415.3698.6812) | ✔️ (only over HTTPS) |

\* Supported in public cloud environments

#### Linux (Public Preview)

| Linux ([Public Preview](https://github.com/microsoft/do-client)) | Linux versions | HTTP Downloader | Peer to Peer | Microsoft Connected Cache |
| --- | --- | --- | --- | --- |
| Device Update for IoT Hub | Ubuntu 18.04, 20.04 / Debian 9, 10 | ✔️ |  | ✔️ |

Note

Starting with Configuration Manager version 1910, you can use Delivery Optimization for the distribution of all Windows update content for clients running Windows 10 version 1709 or newer, not just express installation files. For more, see [Delivery Optimization starting in version 1910](/en-us/mem/configmgr/sum/deploy-use/optimize-windows-10-update-delivery#bkmk_DO-1910).

In Windows client Enterprise, Professional, and Education editions, Delivery Optimization is enabled by default for peer-to-peer sharing on the local network (NAT). Specifically, all of the devices must be behind the same NAT (which includes either Ethernet or WiFi), but you can configure it differently in Group Policy and mobile device management (MDM) solutions such as Microsoft Intune. For more information on [Download mode](waas-delivery-optimization-reference#download-mode) options.

## How Microsoft uses Delivery Optimization

At Microsoft, to help ensure that ongoing deployments weren't affecting our network and taking away bandwidth for other services, Microsoft IT used a couple of different bandwidth management strategies. Delivery Optimization, peer-to-peer caching enabled through Group Policy, was piloted and then deployed to all managed devices using Group Policy. Based on recommendations from the Delivery Optimization team, we used the "group" configuration to limit sharing of content to only the devices that are members of the same Active Directory domain. The content is cached for 24 hours. More than 76 percent of content came from peer devices versus the Internet.

## Using a proxy with Delivery Optimization

If a proxy is being used in your environment, see [Using a proxy with Delivery Optimization](delivery-optimization-proxy) to understand the proxy settings needed to properly using Delivery Optimization.

## How Delivery Optimization works

To gain a deeper understanding of the Delivery Optimization workflow, see [How Delivery Optimization works](delivery-optimization-workflow).

## Set up Delivery Optimization for Windows

[Learn more](delivery-optimization-configure) about the Delivery Optimization settings to ensure proper setup in your environment.

## Delivery Optimization reference

For a complete list of Delivery Optimization settings, see [Delivery Optimization reference](waas-delivery-optimization-reference).

## New in Windows 10, version 20H2 and Windows 11

See [What's new in Delivery Optimization](whats-new-do)