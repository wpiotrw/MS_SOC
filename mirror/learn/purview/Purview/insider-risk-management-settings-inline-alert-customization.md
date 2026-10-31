---
layout: Conceptual
title: Configure inline alert customization in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-inline-alert-customization
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Enable inline alert customization to allow Insider Risk Management analysts and investigators to adjust policy thresholds or disable indicators directly from the Alert dashboard.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
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
document_id: 5777d16c-42fc-79b3-2d57-de52891d7cd6
document_version_independent_id: 5777d16c-42fc-79b3-2d57-de52891d7cd6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-inline-alert-customization.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-inline-alert-customization
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-inline-alert-customization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 82186fa2-8e15-57b6-a59b-32b174b2998d
---

# Configure inline alert customization in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Inline alert customization in Microsoft Purview Insider Risk Management enables you to quickly tune an Insider Risk Management policy directly from the **Alert dashboard** while reviewing the alert. Alerts are generated when a risk management activity meets the thresholds configured in the related policy. To reduce the number of alerts you get from the risk management activity associated with the alert, you can change the thresholds or remove the risk management activity from the policy altogether.

You can enable inline alert customization to allow users assigned to the *Insider Risk Management Analysts* and *Insider Risk Management Investigators* role groups to edit policy thresholds and to disable specific indicators. If you don't enable inline alert customization, only users assigned to the *Insider Risk Management Admins* or *Insider Risk Management* role groups can edit these policy conditions. Inline alert customization supports alerts regardless of the current alert status, so analysts and investigators can update policies for *Dismissed* and *Resolved* alerts if needed.

When enabled, analysts and investigators can select **Reduce alerts for this activity** for an alert on the **Alert dashboard** and view details about the risk management activity and indicators associated with the alert. The portal displays the current policy thresholds for the number of events used to create low, medium, and high severity alerts. If you select **Reduce alerts for this activity** and a previous policy edit changes the threshold or removes the associated indicator, you see a notification message detailing previous changes to the policy.

Analysts and investigators can choose from the following options on the **Reduce alerts for this activity** pane to quickly edit the policy that created the alert:

- **Reduce alerts using Microsoft's recommended thresholds**: This option automatically increases the thresholds in the policy for you. You can review the new recommended threshold settings before changing the policy.
- **Reduce alerts by choosing your own thresholds**: This option lets you manually increase the thresholds for the risk management activity associated with the alert for the current and future alerts. You can review the current threshold settings and configure the new threshold settings before changing the policy.
- **Stop getting alerts for this activity**: This option removes the indicator associated with the selected alert from the policy and the risk management activity is no longer detected by the policy. This option applies to all indicators, regardless of whether the indicator is threshold-based.

After choosing an option, analysts and investigators can choose two options to update the policy:

- **Save and dismiss alert**: Saves the changes to the policy and updates the alert status to *Resolved*.
- **Save only**: Saves the changes to the policy, but the alert status remains the same.

## Enable inline alert customization

Perform the following steps to enable inline alert customization:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Under **Insider risk settings**, select **Inline alert customization**, and then turn on the setting.
5. Select **Save**.

    Note

    After turning on the **Inline alert customization** setting, it takes approximately one hour before inline alert customization is available in new and existing policy alerts.