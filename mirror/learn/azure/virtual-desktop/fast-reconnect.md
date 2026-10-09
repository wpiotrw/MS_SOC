---
layout: Conceptual
title: Session Auto-Reconnect - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/fast-reconnect
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: ridalwan
manager: eliotgra
ms.author: ridalwan
ms.service: azure-virtual-desktop
description: 'Reimagining Session Auto-Reconnect  in Azure Virtual Desktop '
ms.topic: feature-guide
ms.date: 2026-07-29T00:00:00.0000000Z
locale: en-us
document_id: 9f07ff46-3d1f-482a-8016-15adfbb76d63
document_version_independent_id: 9f07ff46-3d1f-482a-8016-15adfbb76d63
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/fast-reconnect.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: fast-reconnect
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/fast-reconnect.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: fb0cfbd3-e701-a4ed-cd58-7f5ce010b797
---

# Session Auto-Reconnect - Azure Virtual Desktop | Microsoft Learn

Auto-Reconnect helps maintain user productivity during temporary network interruptions by automatically restoring an existing remote session when connectivity returns. Instead of requiring users to sign in again, Auto-Reconnect preserves the session state, open applications, and in-memory work so users can continue where they left off.

### Current Auto-Reconnect behavior

Today, Auto-Reconnect uses a retry-based recovery model that starts after the client detects a connection loss.

[![Screenshot that shows Current Auto-Reconnect Behavior.](media/fast-reconnect/current-auto-reconnect.png)](media/fast-reconnect/current-auto-reconnect.png#lightbox)

When a disruption occurs, the client first detects transport failure through signals such as a TCP disconnect, keep-alive timeout, or loss of the underlying network interface. If the device has no active network connectivity, the client waits until the operating system indicates that connectivity has been restored. Once the network becomes available, the client enters a reconnect loop where it repeatedly attempts to re-establish the session.

Each reconnect attempt is a full end-to-end operation that can include broker orchestration to acquire a new connection token, gateway selection, TLS negotiation, transport re-establishment, and remote user logon. Because of this, every attempt incurs non-trivial latency.

The retry behavior follows an exponential backoff algorithm with jitter, where the delay between attempts increases (starting from approximately one second and doubling with each attempt, up to a capped maximum). This reconnect process continues for an overall window of approximately 30 seconds. If the client is unable to restore the connection within this window, the reconnect attempt is considered unsuccessful and the user is prompted to either retry or cancel the session.

From a user experience perspective, the screen is effectively frozen during this process. A modal “Reconnecting” dialog is displayed, user input is blocked, and the session appears unresponsive until reconnection succeeds or the retry window expires. This can result in noticeable disruption and recovery times ranging from several seconds to longer depending on network conditions.

### Modern Auto-Reconnect behavior

Important

Modern Auto-Reconnect is being introduced through a quality-driven, phased rollout. Availability will expand gradually as the rollout progresses, and customers may see the updated experience at different times. No additional action is required beyond meeting the feature prerequisites.

Modern Auto-Reconnect replaces the retry-driven model with a connection preservation model that avoids repeated reconnect attempts and instead focuses on quickly restoring connectivity as soon as any viable network path becomes available.

[![Screenshot that shows Modern Auto-Reconnect behavior.](media/fast-reconnect/image.png)](media/fast-reconnect/image.png#lightbox)

When a network interruption occurs, the client enters a **connection paused** state instead of repeatedly reconnecting. The session remains active on the host while the client waits for network connectivity to be restored.

This experience is enabled by RDP Multipath, which maintains multiple transport paths and allows the connection to recover without rebuilding the entire connection state.

As soon as a network path becomes available, the client resumes the existing session. Because the connection context is preserved, recovery is significantly faster and can often occur almost immediately after connectivity is restored.

If connectivity isn't restored within the allowed waiting period, the user is prompted to continue waiting or close the session.

### User experience improvements

Modern Auto-Reconnect provides a more resilient and less disruptive experience during temporary network interruptions.

Compared to the current reconnect model, users benefit from:

- Faster recovery after connectivity is restored
- Fewer visible interruptions during network transitions
- Preservation of session state and application context
- Reduced dependence on repeated reconnect attempts
- Improved experience when switching between networks or recovering from brief connectivity drops

Instead of displaying a blocking reconnect experience, the client shows a lightweight **Connection paused** notification that indicates the session is temporarily waiting for connectivity to return.

In many scenarios, such as moving between wireless networks or recovering from a brief loss of connectivity, the interruption is short enough that users may experience little or no disruption.

### Availability and Requirements

Modern Auto-Reconnect requires support for the updated connection model and RDP Multipath. To use this experience, install Windows App for Windows version 2.0.1314.0 or later.

Important

Modern Auto-Reconnect is being deployed through a quality-driven, phased rollout. Availability will expand gradually across Azure Virtual Desktop deployments as the rollout progresses.