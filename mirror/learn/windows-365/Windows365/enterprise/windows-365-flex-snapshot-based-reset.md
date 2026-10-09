---
layout: Conceptual
title: Snapshot-based reset for Windows 365 Flex in Shared mode (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-365-flex-snapshot-based-reset
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about snapshot-based reset for Windows 365 Flex in Shared mode.
keywords: 
author: anushareddy
ms.author: anushareddy
manager: satulim
ms.date: 2026-04-24T00:00:00.0000000Z
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
document_id: 5b32d791-143b-0954-c667-b6bcc7e6c102
document_version_independent_id: 5b32d791-143b-0954-c667-b6bcc7e6c102
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-365-flex-snapshot-based-reset.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-365-flex-snapshot-based-reset
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-365-flex-snapshot-based-reset.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 36c2317c-859e-5fb2-1b53-bffbae78c682
---

# Snapshot-based reset for Windows 365 Flex in Shared mode (Preview) | Microsoft Learn

Important

Snapshot-based reset for Windows 365 Flex shared Cloud PCs is currently available in Public Preview.

The snapshot-based reset feature for Windows 365 Flex shared Cloud PCs restores Cloud PCs after each user session. When a user signs out, the Cloud PC automatically resets to a clean state, ensuring no personal data or changes persist across sessions. This design simplifies management, enhances security, and supports the shared licensing model for Windows 365 Flex.

This feature helps organizations:

- Ensure each user session starts with a clean Cloud PC.
- Prevent data carryover between users.

[![Diagram showing the snapshot-based reset flow for Windows 365 Flex in Shared mode.](media/snapshot-based-reset/snapshot-based-reset.png)](media/snapshot-based-reset/snapshot-based-reset.png#lightbox)

**Set time limit for active but idle Remote Desktop Services sessions** controls how long an active session can remain idle before it’s disconnected (idle → disconnect). The default value for Windows 365 Flex shared Cloud PCs is 15 minutes. For more information, see [ADMX_TerminalServer Policy CSP | Microsoft Learn](/en-us/windows/client-management/mdm/policy-csp-admx-terminalserver?WT.mc_id=Portal-Microsoft_Intune_Workflows#ts_sessions_idle_limit_2).

**Set time limit for disconnected sessions** controls how long a disconnected session remains active before the user is signed out (disconnect → sign-out). The default value for Windows 365 Flex shared Cloud PCs is 30 minutes. For more information, see [ADMX_TerminalServer Policy CSP | Microsoft Learn](/en-us/windows/client-management/mdm/policy-csp-admx-terminalserver?WT.mc_id=Portal-Microsoft_Intune_Workflows#ts_sessions_disconnected_timeout_2).

## User experience

Users sign in to a clean Cloud PC for each session. After sign-out, the Cloud PC automatically resets and reverts to a clean state before returning to the shared pool.

### Session behavior

- If a user disconnects instead of signing out (for example, by closing the Windows App), the session times out and triggers the same reset process.
- Without User Experience Settings (UES) enabled, personal settings, files, and app configurations don't persist after reset.

### User Experience Sync

With User Experience Sync enabled:

- Selected user files and app configurations can be retained and restored.
- The Cloud PC itself continues to reset and revert to a clean state between sessions.

This reset process is automatic and doesn't require manual intervention from admins.

## Connectivity and device availability during reset

After a user signs out, the Cloud PC automatically initiates the reset process. During this time, the device is temporarily unavailable for new connections and might appear as **Unavailable (Servicing)** in admin views.

The **Unavailable (Servicing)** status indicates that the Cloud PC is being reverted to a clean state between user sessions. After the reset is complete, the Cloud PC returns to a ready state and becomes available in the shared pool for the next user session.

For more information, see [Connectivity health checks in Windows 365](health-checks-connectivity).

## Get started with Public Preview

Snapshot-based reset for Windows 365 Flex shared Cloud PCs is now available in Public Preview. Try this feature and share your feedback to help refine the experience before general availability.

[Sign up for the Public Preview](https://forms.cloud.microsoft/r/iTyCYfsPy8)

## Frequently asked questions

### When should admins use reprovisioning instead of snapshot-based reset?

Use snapshot-based reset and reprovisioning together—they serve complementary purposes. Snapshot-based reset ensures a clean state between user sessions. Use reprovisioning for major changes such as OS upgrades and image updates. Together, they help maintain consistency over time and reduce configuration drift.

### How often is the snapshot updated? Is it visible to admins? How are Intune deployments affected?

- **Initial snapshot**: A snapshot is captured at Cloud PC provisioning, after the first Intune sync completes and any workloads defined in the Device Provisioning Policy (DPP) have been applied. This ensures the baseline reflects a fully configured, policy-compliant device.
- **Refresh cadence**: Snapshots refresh daily on a rolling 24-hour cycle per Cloud PC, so the timing is staggered based on each device's provisioning time and eligibility window.
- **Intune alignment**: Each refreshed snapshot reflects the latest Intune policies and device-targeted app deployments that have synced and applied prior to capture.
- **Admin visibility**: Admins can't view, download, or manage individual snapshots directly — the system manages them automatically as part of the reset baseline.

### How does snapshot-based reset work with Cloud Apps?

Cloud Apps run normally during a session, but local data and settings are cleared at reset. Users can continue work across sessions by saving data to cloud services or by using [User Experience Sync](windows-365-flex-user-experience-sync).

### How does snapshot-based reset affect user experience during preview?

During the preview, users might observe:

- Reset between users takes approximately 3 minutes.
- After each reset, users sign in within about 50 seconds.

### How do I deploy an updated app version to Cloud PCs that use snapshot-based reset?

Don't rely on runtime Intune app deployment alone. The update is lost at the next reset. Instead:

1. In Intune, target the updated app version to the device group that contains your Cloud PCs.
2. Reprovision the Cloud PCs in the pool.
3. During reprovisioning, the new app version is installed as part of the device build and captured in the next snapshot. From that point on, every reset restores the Cloud PC with the updated app already in place.

### How should I manage Windows updates on Cloud PCs that use snapshot-based reset?

Don't apply Windows quality updates to individual Cloud PCs at runtime. Those updates are reverted on reset. Instead:

1. Turn off Windows Update on the individual Cloud PCs (for example, through an Intune configuration policy).
2. When a new quality update is needed, reprovision the Cloud PCs using the latest Windows 365 gallery image. Custom images are also supported.
3. Reprovisioning rebuilds each Cloud PC from the updated image, and the new OS state is captured in the next snapshot. This keeps every Cloud PC in the pool on a known, consistent Windows version.

### Why reprovision instead of patching in place?

Snapshot-based reset is designed to give every user a clean, identical starting point. Patching individual Cloud PCs after provisioning causes drift between devices in the pool and gets discarded on the next reset. Reprovisioning makes the change part of the baseline, so it persists across resets and applies uniformly to every Cloud PC in the pool.

These workflows are known areas of improvement that are actively being optimized as the feature progresses toward general availability.