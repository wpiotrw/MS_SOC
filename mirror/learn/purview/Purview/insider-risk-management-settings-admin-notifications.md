---
layout: Conceptual
title: Enable admin notifications in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-admin-notifications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Enable admin notifications in Microsoft Purview Insider Risk Management to send email alerts for first-time policy matches, daily high-severity alerts, weekly unresolved warnings, and analytics insights.
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
document_id: c73182a2-d8e2-fa07-03d3-1260b1939d02
document_version_independent_id: c73182a2-d8e2-fa07-03d3-1260b1939d02
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-admin-notifications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-admin-notifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-admin-notifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 313b2ca6-b851-f1b1-8b19-8fbc922b995b
---

# Enable admin notifications in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

## Admin notifications

When you turn on the **Admin notifications** setting in Microsoft Purview Insider Risk Management, the system automatically sends email notifications to selected role groups. You can send email notifications for the following scenarios:

- Send a notification email when the first alert is generated for a new policy. The system checks policies every 24 hours for first-time alerts and doesn't send notifications on subsequent alerts for the policy.
- Send a daily email when new high-severity alerts are generated. The system checks policies every 24 hours for high severity alerts.
- Send a weekly email summarizing policies that have unresolved warnings.

If you enable Insider Risk Management analytics for your organization, members of the *Insider Risk Management Admins* role group automatically receive an email notification for initial analytics insights for data leaks, theft, and exfiltration activities.

Note

Add individuals to the role group to receive notifications. Email notifications don't support Admin Units, Priority Users Groups, or Entra ID Security Groups.

## Disable admin and analytics notifications

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, and then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Admin notifications**.
4. Clear the check boxes for the following options, as applicable:

    - **Send a notification email when the first alert is generated for a new policy**
    - **Send an email when an analytics scan detects an insight for the first time**
    - **Send an email when analytics is turned off for your organization**
5. Select **Save**.