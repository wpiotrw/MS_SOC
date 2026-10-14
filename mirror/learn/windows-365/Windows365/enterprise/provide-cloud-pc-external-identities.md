---
layout: Conceptual
title: Provision Cloud PCs for external identities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/provide-cloud-pc-external-identities
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: How to provision Cloud PCs for external identities
keywords: 
author: ChristianMontoya
ms.author: chrimo
manager: pratikshah
ms.date: 2025-11-06T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: davidbel
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 362459e3-dc11-6334-ec3b-7c361c29b6ae
document_version_independent_id: 362459e3-dc11-6334-ec3b-7c361c29b6ae
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/provide-cloud-pc-external-identities.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/provide-cloud-pc-external-identities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/provide-cloud-pc-external-identities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
platformId: f2963abe-0a03-914d-2a4d-e95b176419aa
---

# Provision Cloud PCs for external identities | Microsoft Learn

This article explains the process of providing Cloud PCs to external identities.

## Prerequisites

Before provisioning Cloud PCs, review the [requirements and limitations for external identities](identity-authentication#external-identity).

## Provision Cloud PCs for external identities

To provision Cloud PCs for external identities:

1. Follow the steps to [Configure single sign-on for Windows 365 using Microsoft Entra authentication](configure-single-sign-on)to:
    1. Ensure that single sign-on is enabled in your tenant.
    2. (Optional) Hide the consent prompt.
2. Follow the steps to [Create provisioning policies](create-provisioning-policy), with the following configurations:
    1. On the General page, select **Microsoft Entra Join** as the join type.
    2. On the General page, check the box to **Use Microsoft Entra single sign-on**.
    3. On the Image page, select an image running a supported OS (defined in the [requirements and limitations for external identities](identity-authentication#external-identity)).
    4. On the Assignments page, select a Microsoft Entra user group containing the external identities.

## Connect to Cloud PCs with an external identity

Follow the steps to [Manage user accounts in Windows App](/en-us/windows-app/user-account-settings-add-remove-manage) to sign in to a supported Windows App client with an external identity and connect to a Cloud PC.