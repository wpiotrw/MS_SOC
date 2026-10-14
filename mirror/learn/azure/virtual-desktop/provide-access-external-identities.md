---
layout: Conceptual
title: Provide host pool access to external identities - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/provide-access-external-identities
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: ChristianMontoya
manager: eliotgra
ms.author: chrimo
ms.service: azure-virtual-desktop
description: Learn how to configure a host pool and create sessions hosts for external identities.
ms.topic: how-to
ms.date: 2025-11-06T00:00:00.0000000Z
locale: en-us
document_id: 14b5e1cf-b74c-71da-135e-d93009b763ea
document_version_independent_id: 14b5e1cf-b74c-71da-135e-d93009b763ea
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/provide-access-external-identities.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: provide-access-external-identities
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/provide-access-external-identities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 4f88600b-b280-decb-cd62-f689f19280b8
---

# Provide host pool access to external identities - Azure Virtual Desktop | Microsoft Learn

This article explains the process of providing host pool access to external identities.

## Prerequisites

Before providing host pool access, review the [requirements and limitations for external identities](authentication#external-identity).

## Provide host pool access for external identities

To provide host pool access for external identities:

1. Follow the steps to [Configure single sign-on for Azure Virtual Desktop using Microsoft Entra authentication](configure-single-sign-on) to:

    1. Ensure that single sign-on is enabled in your tenant.
    2. (Optional) Hide the consent prompt.
2. Follow the steps to [Deploy Microsoft Entra joined VMs](azure-ad-joined-session-hosts#deploy-microsoft-entra-joined-vms) with the following considerations:

    1. You can deploy Entra joined VMs to a new or existing host pool.
    2. Use an OS image running a supported OS (defined in the [requirements and limitations for external identities](authentication#external-identity)).
    3. Ensure you make the following assignments with the Microsoft Entra user group containing the external identities:
        1. Assign the group to the application group.
        2. Assign the group either the **Virtual Machine User Login** or **Virtual Machine Administrator Login** Azure role-based access control (RBAC) role for each session host VM in the host pool. If you're using a [session host configuration](host-pool-management-approaches#session-host-configuration), this assignment isn't required.
3. [Configure the host pool to enable single sign-on](configure-single-sign-on#configure-your-host-pool-to-enable-single-sign-on).

    Note

    You must enable single sign-on external identities to connect. Connection attempts using legacy authentication protocols will fail.

## Connect to Azure Virtual Desktop resources with an external identity

Follow the steps to [Manage user accounts in Windows App](/en-us/windows-app/user-account-settings-add-remove-manage) to sign in to a supported Windows App client with an external identity and connect to Azure Virtual Desktop resources.