---
layout: Conceptual
title: Host pool management approaches - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/host-pool-management-approaches
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: cmckitterick
manager: eliotgra
ms.author: chmckitt
ms.service: azure-virtual-desktop
description: Learn about the different host pool management approaches of session host configuration management and standard management in Azure Virtual Desktop.
ms.topic: article
ms.reviewer: caineoyuan
ms.date: 2026-07-02T00:00:00.0000000Z
locale: en-us
document_id: cee05535-df81-d67e-149b-216aed48986d
document_version_independent_id: cee05535-df81-d67e-149b-216aed48986d
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/host-pool-management-approaches.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: host-pool-management-approaches
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/host-pool-management-approaches.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: 62c774e6-2a63-8b02-3ae2-2c3eea33eb6a
---

# Host pool management approaches - Azure Virtual Desktop | Microsoft Learn

Host pools are logical groupings of session host virtual machines that have the same configuration and serve the same workload. You can choose one of two host pool management approaches, *standard* and using a *session host configuration*. In this article, you learn about each management approach and the differences between them to help you decide which one to use.

Caution

The host pool management approach is set when you create a host pool and can't be changed later. If you create a host pool without a session host configuration, you can't add one afterwards.

## Session host configuration management approach

Creating, updating, and scaling session hosts in a host pool can require much effort if you don't have existing tools and processes in place. The session host configuration management approach uses a combination of the following native features to provide an integrated and dynamic experience:

- A *session host configuration* specifies **what** the configuration of session hosts should be.
- A *session host management policy* specifies **how** session hosts should be created and updated.
- *[Session host update](session-host-update)* updates session hosts **when** there's an update made to the session host configuration. Session host update ensures that all session hosts in the pool have the same configuration.
- *[Autoscale](autoscale-scenarios)* dynamically scales the number of session hosts up and down based on the actual usage and the schedules defined in the scaling plan.

Important

The session host configuration management approach can be used with pooled host pools only. When using a host pool with a session host configuration, you can't create, update or scale session hosts outside of the Azure Virtual Desktop service using tools designed for host pools with standard management.

### Session host configuration

A session host configuration is a sub-resource of the session host configuration management approach that specifies the configuration of session hosts in the host pool. The session host configuration persists throughout the lifecycle of the host pool and is aligned with the session hosts in the host pool. The session host configuration includes the following properties:

- VM image
- VM name prefix
- VM resource group
- VM size
- OS disk information
- Domain join information
- VM network configuration
- VM location

- VM availability zones
- VM security type
- VM admin credentials
- VM name prefix
- VM boot diagnostics information
- Custom configuration PowerShell script
- VM Tags

Any newly created session hosts are created from the session host configuration for the host pool. To update the session hosts in your host pool, first you must update the session host configuration. After updating the session host configuration, you schedule when you would like that update to be applied to the session hosts in the host pool using the session host update feature. If there are no session hosts in the host pool, any property of the session host configuration can be changed without needing to schedule a session host update.

For a comparison of host pool with a session host configuration and a host pool with standard management, see Compare host pool management approaches.

### Session host management policy

A session host management policy is a sub-resource of a host pool that specifies how session hosts in the host pool should be updated and created. The session host management policy persists throughout the lifetime of the host pool and it's used when updating the session hosts in the host pool or adding new session hosts. Each host pool with a session host configuration only has a single session host management policy, and you can't delete a session host management policy independently of the host pool.

When you use the Azure portal, a default session host management policy is created when you create a host pool with a session host configuration. You can override its values when updating and creating session hosts, or you can also update the session host management policy at any time using PowerShell.

The session host management policy includes the following parameters:

| Parameter | Description | Azure portal default value |
| --- | --- | --- |
| **Time zone** | The time zone to use when scheduling an update of the session hosts in a host pool. | `UTC` |
| **Max VMs removed during update** | The maximum number of session hosts to update concurrently, also known as the *batch size*. | `1` |
| **Logoff delay in minutes** | The amount of time to wait after an update start time for users to be notified to sign out, between 0 and 60 minutes. Users will automatically be signed out after this time elapses. | `2` |
| **Logoff message** | A message to display to users that the session host they're connected to will be updated. | `You will be signed out` |
| **Leave in drain mode** | Determines whether newly created session hosts will be left in drain mode for post-creation actions before users can log in. This parameter doesn't apply for session host update. | `False` |
| **Failed session host cleanup policy** | Determines whether to keep none, some, or all session hosts that encounter an error during session host creation. This parameter doesn't apply for session host update. | `KeepAll` |

## Standard management approach

With the standard host pool management approach, you manage creating, updating, and scaling session hosts in a host pool. If you want to use existing tools and processes, such as automated pipelines, custom scripts, you need to use the standard host pool management type. Existing tooling designed for standard management won't work with a session host configuration. For a comparison of host pool with a session host configuration and a host pool with standard management, see Compare host pool management approaches.

## Compare host pool management approaches

The following table compares the management approach of host pools with a session host configuration and host pools with standard management in different scenarios or when using different features of Azure Virtual Desktop:

| Scenario or feature | Session host configuration | Standard management |
| --- | --- | --- |
| Create session hosts | [Add session hosts](add-session-hosts-host-pool?pivots=host-pool-session-host-configuration) by increasing the host pool size using the Azure portal, ARM template, or PowerShell. You can't retrieve a registration token to add session hosts created outside of Azure Virtual Desktop to a host pool. | [Add session hosts](add-session-hosts-host-pool?pivots=host-pool-standard) using your preferred method, then use a registration token to add them to a host pool. If you use the Azure portal, you need to input the configuration each time. |
| Configure session hosts | The session host configuration ensures the configuration of session hosts is consistent. | You have to ensure the configuration of session hosts in the host pool is consistent. Session host configuration isn't available. |
| Scale session hosts | Use [autoscale](autoscale-scenarios) to turn session hosts on and off or create and delete session hosts based on a schedule and usage. | Use [autoscale](autoscale-scenarios) to turn session hosts on and off based on a schedule and usage. |
| Update session host image | Use [session host update](session-host-update) to update the image and configuration of your session hosts based on the session host management policy and session host configuration. | Use your own existing tools and processes, such as automated pipelines and custom scripts to update the image and configuration of your session hosts. You can't use session host update. |
| Automatically power on session hosts | Use [Start VM on Connect](start-virtual-machine-connect) to enable end users to turn on their session hosts only when they need them. | Use [Start VM on Connect](start-virtual-machine-connect) to enable end users to turn on their session hosts only when they need them. |