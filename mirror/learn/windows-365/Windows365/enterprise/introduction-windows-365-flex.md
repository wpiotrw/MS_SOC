---
layout: Conceptual
title: What is Windows 365 Flex? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/introduction-windows-365-flex
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about Windows 365 Flex.
keywords: 
author: msft-jasonparker
ms.author: japarker
manager: stulimat
ms.date: 2026-09-24T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: stulimat, scottduf
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
ai-usage: ai-assisted
locale: en-us
document_id: 0940bd07-fd5a-d6bd-d220-322bb9a71aea
document_version_independent_id: 0940bd07-fd5a-d6bd-d220-322bb9a71aea
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/introduction-windows-365-flex.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/introduction-windows-365-flex
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/introduction-windows-365-flex.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 05d3b13a-6130-03f4-ebe8-d190fb86c32a
---

# What is Windows 365 Flex? | Microsoft Learn

Windows 365 Flex is a version of [Windows 365](../overview) that helps organizations save costs by letting them provision a Cloud PC that can be used by multiple users with a single [license](windows-365-flex-license). Windows 365 Flex has two different modes: Dedicated mode and Shared mode. Windows 365 Flex licenses can be applied to either mode.

## Windows 365 Flex in Dedicated mode

A single license:

- Lets you provision up to three Cloud PCs that can be used nonconcurrently, each assigned to a single user.
- Provides one concurrent session.

Windows 365 Flex Dedicated mode is designed specifically for workers who need a dedicated Cloud PC but don't need 24/7 access. This system better supports organizations that are more elastic and distributed, working across various devices. Windows 365 Flex Cloud PCs in Dedicated mode can be helpful for users who are:

- On a rotation schedule.
- Working across time zones and regions.
- Part-time workers.
- Contingent staff.

The maximum number of active Windows 365 Flex Cloud PC sessions in your organization is equal to the number of Windows 365 Flex licenses that you purchased. For example, if you purchase 10 licenses, up to 30 Cloud PCs can be provisioned in Dedicated mode, but only 10 of those Cloud PCs can be active at a given time. The active sessions are managed automatically. When a user signs off from their Cloud PC, the session is released for another user to start using their Cloud PC. A concurrency buffer exists to exceed the maximum a limited number of times per day. For more information, see [Concurrency buffer](concurrency-buffer).

Note

Windows 365 Flex Cloud PCs in Dedicated mode automatically powers off after the user signs off from the Cloud PC, and is powered on when the user attempts to connect. It may take more time for the user to connect when the Cloud PC is being powered on. This connection time doesn't include executing logon scripts set by organizations. After the user signs off, the Cloud PC remains powered on for two hours. If the user attempts to reconnect while the Cloud PC is powered on, the connection time is the same as Windows 365 Enterprise Cloud PCs.

### Intelligent prestart for Windows 365 Flex in Dedicated mode

Windows 365 Flex Cloud PCs in Dedicated mode can predict when a user connects and prestart their Cloud PC before they sign in every day. This prediction improves startup times for such users' Cloud PCs. For instance, if a user connects to their Cloud PC every day at 9 AM, then the system recognizes that after a few days and will start up that user's Cloud PC around 30 minutes before 9 AM each day and keep it powered on for two hours waiting for the user to connect. Thus, when the user connects at 9 AM, their Cloud PC is already started and they can connect quickly. If the user connects outside their regular startup time, the user must wait for the Cloud PC to start up.

For the prediction to work appropriately, users must connect to their Cloud PCs for at least three days in the past 30 days. If the user doesn't have a pattern of connecting, then the prediction might not be accurate, and the prestart does not behave as expected.

Prestarted Cloud PCs don’t consume the license for session connection until the user connection is complete. If the user doesn’t connect within two hours, the Cloud PC automatically shuts down.

### Session State Retention for Windows 365 Flex dedicated Cloud PCs

Today, when a user disconnects from a Windows 365 Flex dedicated Cloud PC, it powers off, closing open apps and risking unsaved work.

With Session State Retention, eligible Flex dedicated Cloud PCs preserve the user's active session while idle. Users reconnect and return to their open apps and work exactly where they left off.

### How it works

When a user disconnects, an eligible Cloud PC hibernates after a set idle period (default: two hours) instead of powering off. On the next connection, it resumes from the saved state with apps and windows intact. Cloud PCs that aren't hibernation-eligible continue to power off.

### Considerations and limitations

- Available only on hibernation-eligible Flex dedicated Cloud PCs; others power off instead.
- Resizing to a size that doesn't support hibernation makes a Cloud PC ineligible.
- Some events, such as Windows Updates that require a reboot, start a Cloud PC fresh, so the previous session isn't preserved.

## Windows 365 Flex in Shared mode

A single license:

- Lets you provision one Cloud PC that can be shared nonconcurrently among a group of users.
- Provides one concurrent session.

Windows 365 Flex in Shared mode is designed specifically for workers who

- Require access to a Cloud PC to perform specialized tasks for a short time during their work day.
- Don't require data persistence.

Windows 365 Flex Cloud PCs in Shared mode can be helpful for users who are:

- Customer-facing workers.
- External contractors.

The maximum number of active Windows 365 Flex Cloud PC sessions in your organization is equal to the number of Windows 365 Flex licenses that you set up for a specific group. For example, if you assign 10 Windows 365 Flex shared licenses, 10 Cloud PCs can be provisioned for the group. Only a single user can connect to a shared Cloud PC at a given time. When a user signs out from the Cloud PC, all user data is deleted and the Cloud PC is released for another user to start using. Concurrency buffer doesn't exist for a Windows 365 Flex Cloud PC in Shared mode.

With Windows 365 Flex Cloud PCs in Shared mode, you can also provide [Cloud Apps](cloud-apps) to users instead of the full Cloud PC desktop experience.

Note

Windows 365 Flex Cloud PCs in Dedicated mode are prioritized over Shared mode in the case where you already have provisioning policies created and later add licenses.

## Monitor the concurrency buffer

You can monitor the use of concurrency buffer with the Windows 365 Flex connection hourly report. You can use the Windows 365 Flex concurrency alert to receive alerts each time the concurrency buffer is activated. The concurrency buffer doesn't apply to GPU-enabled Cloud PCs and Windows 365 Flex Cloud PCs in Shared mode.

## Microsoft Purview Customer Key

Supported for Windows 365 Flex Cloud PCs in both **Dedicated** and **Shared** modes. Newly provisioned Cloud PCs are encrypted using Customer Key once the capability is enabled in Microsoft Purview.

Learn more about [Microsoft Purview Customer Key](purview-customer-key) support in Windows 365.

## Compare planning factors for dedicated and Shared modes

Use the following table to compare key planning factors for dedicated and Shared modes when sizing a Windows 365 Flex deployment.

| Planning factor | Dedicated mode | Shared mode |
| --- | --- | --- |
| License provisions | Up to three Cloud PCs, each dedicated to a specific user | One Cloud PC shared non-concurrently by a group of users |
| Cloud PCs per license | Up to 3 | 1 |
| Active (concurrent) sessions per license | 1 | 1 |
| User assignment | Each Cloud PC is assigned to a single user through a Microsoft Entra ID user group | Any user in the assigned Microsoft Entra ID user group can use the shared Cloud PC |
| Data persistence | User data persists between sessions | User data is deleted after each session. When UES (User Experience Sync) is enabled, user-specific app data and Windows settings are stored in the cloud. |
| Maximum active sessions are limited by | The total number of Windows 365 Flex licenses purchased for the tenant, excluding licenses used for Shared mode Cloud PCs | The number of Windows 365 Flex licenses allocated to the group |

## Considerations when planning

- If the Microsoft Entra ID user group assigned to a Dedicated mode provisioning policy has more users than available Cloud PCs for the selected size, some users might not receive a Cloud PC.
- When a tenant has both Dedicated mode and Shared mode provisioning policies and additional licenses are added, Dedicated mode Cloud PCs are provisioned first.
- The concurrency buffer is available for Dedicated mode only. Shared mode does not include a concurrency buffer. GPU-enabled Cloud PCs are also excluded from the concurrency buffer.

## Features not yet supported Windows 365 Flex

The following features aren't yet supported for Windows 365 Flex.

- Resize a Cloud PC remote action
- Cross region disaster recovery

Windows 365 Flex in Shared mode is currently only available for Azure Global Cloud.

[Learn more](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2Cent#supported-azure-regions-for-cloud-pc-provisioning) about which regions support provisioning Windows 365 Flex in Shared mode.