---
layout: Conceptual
title: Create a DLP Policy Using Device Scoping | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-device-scoping
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE
ai-usage: ai-assisted
search.appverid:
- MET150
description: Learn how to create a Microsoft Purview DLP policy scoped to specific device groups so you can enforce different data protection rules.
locale: en-us
document_id: e02de5d6-1ee4-21eb-b215-162248ade467
document_version_independent_id: e02de5d6-1ee4-21eb-b215-162248ade467
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-create-policy-device-scoping.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-create-policy-device-scoping
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-create-policy-device-scoping.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
platformId: 6ae556fe-4217-5844-244e-c8c7c02a3322
---

# Create a DLP Policy Using Device Scoping | Microsoft Learn

This scenario shows how to scope a Microsoft Purview Endpoint DLP policy to specific device groups. For example, you can enforce a policy only when Finance users access data from Windows devices while excluding macOS devices. Device groups are commonly defined using dynamic device groups in Microsoft Entra ID.

This scenario is for an unrestricted admin creating a full directory policy.

This scenario requires that you already have devices onboarded and reporting into activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started).

## Prerequisites and assumptions

This article uses the process you learned in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [Deploy a DLP policy](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

You've created a dynamic device group.

## Policy intent statement and mapping

*An organization wants to enforce a DLP policy that blocks copying sensitive items with credit card data to USB devices when Finance users access data from Windows devices, and does not apply when the same users work from macOS devices.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “An organization wants to enforce a DLP policy that blocks copying sensitive items with credit card data to USB devices..." | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/Finance Windows Devices group |
| “when Finance users access data from Windows devices…” | - Condition: **Content contains** = **Credit Card Number** |
| “…and does not apply when the same users work from macOS devices…” | - Action: **Audit or restrict activities on devices**- Activity type: **File activities on all apps**- Restriction model: **Apply restrictions to specific activity**- **Copy to a removable USB device** = **Block** |

## Create a device group

If you're unfamiliar with dynamic device groups, see:

- [Create or update a dynamic membership group in Microsoft Entra ID](/en-us/entra/identity/users/groups-create-rule)
- [Manage rules for dynamic membership groups in Microsoft Entra ID](/en-us/entra/identity/users/groups-dynamic-membership).

To create the device group for this scenario:

1. Create a new dynamic device group named **Finance Windows Device** for the Windows devices that the finance team uses.

## Create a policy scoped to the dynamic device group

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **policies**.
2. Select **Create policy**.
3. Select **Enterprise applications & devices**.
4. Select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**. Select **Next**.
5. Give your new policy a **Name** and **Description**.
6. Accept the default **Full directory** under **Admin units**.
7. Scope the location to only the **Devices** location.
8. Select **Edit** on the **Devices** location.
9. Accept the default **All users, groups, and adaptive scopes**
10. Select **Specific devices and device groups** and add the **Finance Windows Device** that you created.
11. Create a rule with the following values:

    - **Condition**: **Content contains** = **Sensitive Info types** = **Credit Card Number**
    - **Action**: **Audit or restrict activities on devices** &gt; **File activities for all apps** &gt; **Apply restrictions to specific activity** &gt; **Copy to a removable USB device** = **Block**.
12. Select **Save** and then **Next**.
13. Accept the default **Run the policy in simulation mode** value and choose **Show policy tips while in simulation mode**. Choose **Next**.
14. Review your settings and choose **Submit**.

The new DLP policy appears in the policy list.