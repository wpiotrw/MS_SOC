---
layout: Conceptual
title: Set policy timeframes in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-timeframes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the Policy timeframes settings in Microsoft Purview Insider Risk Management.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-25T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 814e5dca-c2de-65ad-a809-69b803fb3a76
document_version_independent_id: 814e5dca-c2de-65ad-a809-69b803fb3a76
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-policy-timeframes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-policy-timeframes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-policy-timeframes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b657b927-6ea5-56cf-e8bc-7842e020968f
---

# Set policy timeframes in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Policy timeframes in Microsoft Purview Insider Risk Management let you set past and future review periods that start after policy matches events and activities for the Insider Risk Management policy templates. Depending on the policy template you choose, you can set the following policy timeframes:

- **Activation window**: Available for all policy templates, *Activation window* is the number of days that the window activates **after** a triggering event. The window activates for 1 to 30 days after a triggering event occurs for any user assigned to the policy. For example, you configure an Insider Risk Management policy and set *Activation window* to 30 days. Several months pass since you configured the policy, and a triggering event occurs for one of the users included in the policy. The triggering event activates *Activation window* and the policy is active for that user for 30 days after the triggering event occurred.
- **Past activity detection**: Available for all policy templates, *Past activity detection* is the number of days that the window activates **before** a triggering event. For activities in the audit log, the window activates for 0 to 90 days before a triggering event occurs for any user assigned to the policy. For example, you configure an Insider Risk Management policy and set *Past activity detection* to 90 days. Several months pass since you configured the policy, and a triggering event occurs for one of the users included in the policy. The triggering event activates *Past activity detection* and the policy gathers historic activities for that user for 90 days prior to the triggering event.

    Note

    For email activities, the past activity detection period is 10 days.

## Configure policy timeframes

1. In Insider Risk Management settings, select **Policy timeframes**.
2. Move the slider for **Activation window** and **Past activity detection** to the number of days that you want.

    ![Screenshot of the Insider Risk Management policy timeframes settings page showing the Activation window and Past activity detection sliders.](media/insider-risk-settings-timeframes.png)