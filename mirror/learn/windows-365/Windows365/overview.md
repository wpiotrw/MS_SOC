---
layout: Conceptual
title: What is Windows 365? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: What is Windows 365?
keywords: 
author: cawerner
ms.author: cawerner
ms.date: 2025-04-15T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: 
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: ivivano
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started; intro-hub-or-landing
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 73040313-8778-540a-872d-134ed78e0bff
document_version_independent_id: 73040313-8778-540a-872d-134ed78e0bff
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 0b577a38-99a6-2bdf-2f4c-6ef5032d616d
---

# What is Windows 365? | Microsoft Learn

Windows 365 is a cloud-based software-as-a-service (SaaS) that automatically creates a new type of Windows virtual machine (Cloud PCs) for your end users. The Cloud PC lets users access Windows 10 or 11 from various devices (like Windows, iOS, and Android). Windows 365 offers various solutions to support organizations of all sizes with multiple deployment options tailored to specific roles and needs. Windows 365 provides the productivity, security, and collaboration benefits of Microsoft 365.

Windows 365 is available in multiple editions:

- **Windows 365 Business** simplifies deployment and is made specifically for use in smaller companies (up to 300 seats) who want ready-to-use Cloud PCs with simple management options. For more information, see [Getting started with Windows 365 Business and Cloud PCs](business/get-started-windows-365-business).
- **Windows 365 Enterprise** is for larger companies who want unlimited seats for creating Cloud PCs. It includes options to create custom Cloud PCs based on device images that you create, more management options, and full integration with Microsoft Intune. For more information, see [What is Windows 365 Enterprise?](enterprise/overview)
- **Windows 365 Government** is a service that spans across a regulated US Government Community Cloud (GCC) and a public facing cloud. For more information, see [What is Windows 365 Government?](enterprise/introduction-windows-365-government)
- **Windows 365 Flex** helps organizations save costs by providing a single license to provision up to three Cloud PCs for non-concurrent use. These are meant for cases where the user needs Cloud PC access for a limited time per day. For more information, see [What is Windows 365 Flex?](enterprise/introduction-windows-365-flex)
- **Windows 365 for Agents (preview)** is the compute platform for AI-powered computer-using agents. These Cloud PCs are sandbox environments spun up for user prompted tasks. For more information, see [What is Windows 365 for Agents?](agents/introduction-windows-365-for-agents)

To learn about the differences between the Business and Enterprise versions, see [Compare Windows 365 Business and Enterprise](business-enterprise-comparison).

Windows 365 isn't currently available for individuals.

## Windows 365 Link

Available now in select markets, Microsoft also offers Windows 365 Link, the first Cloud PC device purpose-built to connect users directly to Windows 365. For more information, see [What is Windows 365 Link?](link/overview)

## What is a Cloud PC?

A Cloud PC is a highly available, optimized, and scalable virtual machine that gives end users a rich Windows desktop experience. The Windows 365 service hosts it, and you can access it from anywhere, on any device.

In Windows 365 Enterprise, Business, and Government, end users have a 1:1 relationship with their Cloud PC. It’s their own personal PC in the cloud. With [Windows 365 Flex](/en-us/windows-365/enterprise/introduction-windows-365-flex), multiple users can nonconcurrently access a single Cloud PC.

Users can connect to their Cloud PC by using [windows365.microsoft.com](https://windows365.microsoft.com/). [Browser and app-based access](/en-us/windows-365/end-user-access-cloud-pc) is available for Windows, Mac, iOS, and Android devices. Desk-based users can also use [Windows 365 Link](/en-us/windows-365/link/) to connect securely to your Windows 365 Cloud PC in seconds.

### Creating a Cloud PC

The Windows 365 service automatically creates Cloud PCs when you assign a Windows 365 license to an end user in an appropriate Microsoft Entra user group.

Admins don't manually create Cloud PCs.

## Licensing and how to buy

Before your users can gain access to a Cloud PC, you must purchase Windows 365 licenses. Customers can purchase Windows 365 as a separate license per user for a fixed monthly fee to access and use Cloud PCs. Additional costs may apply based on network usage. After licenses are purchased, you can create provisioning policies to automatically create Cloud PCs for users.

For more information, see [Windows 365 Licensing](https://www.microsoft.com/licensing/product-licensing/windows-365) and [Windows 365 plans and pricing](https://www.microsoft.com/windows-365/all-pricing?rtc=1).

### Licensing for external identities

If you're using Windows 365 with external identities, there may be special considerations for how you license other products and services from Microsoft for those external identities.

Licenses assigned to an external collaborator in their own home tenant generally do not confer entitlements to Windows 365 or other products within your tenant. Therefore, we generally recommend purchasing the same sort of license as you purchase for internal users and assigning it to the external collaborator's identity in your tenant. For example, if you're licensing Microsoft 365 Apps alongside your Windows 365 Cloud PCs, and your external collaborators need the same entitlements, purchase a Microsoft 365 Apps license and assign it to the external collaborator in your tenant.

Similarly, licenses assigned to a user in one tenant of a [multitenant organization](/en-us/entra/identity/multi-tenant-organizations/overview) generally do not confer entitlements to Windows 365 or other products within another tenant of that organization. Therefore, we generally recommend purchasing a license for each user in each tenant in which access rights are required. An exception to this is Entra ID; only one Microsoft Entra ID P1 license is required per employee per multitenant organization.

## Billing

Cloud PCs for human use are billed in a per-user per-month cost model. This model means your organization doesn’t have to manage the variability of compute and storage costs of a traditional hosted desktop model. Cloud PCs for agent use are billed in pay-as-you-go model. This model means your organization only pays for the compute needed by the agent solutions.

## Microsoft 365 Lighthouse

Managed Server Providers (MSPs) can manage Cloud PCs in Microsoft 365 Lighthouse for their customer tenants. For more information, see [Windows 365 (Cloud PCs) page overview](/en-us/microsoft-365/lighthouse/m365-lighthouse-win365-page-overview).