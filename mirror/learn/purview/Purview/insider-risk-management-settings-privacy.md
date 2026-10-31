---
layout: Conceptual
title: Manage username privacy in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using the Privacy setting in Microsoft Purview Insider Risk Management to manage visibility of usernames.
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
document_id: d976df02-2c00-1f4f-240d-b7863e2259c8
document_version_independent_id: d976df02-2c00-1f4f-240d-b7863e2259c8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-privacy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-privacy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-privacy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 11017136-bb29-20cf-c9a5-605764e85522
---

# Manage username privacy in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Protecting the privacy of users that have policy matches in Microsoft Purview Insider Risk Management is important. It helps promote objectivity in data investigation and analysis reviews for insider risk alerts. For users with an insider risk policy match, choose one of the following settings:

Important

With the anonymized versions of usernames setting enabled, you cannot use [data risk graph](insider-risk-management-data-risk-graph).

- **Show anonymized versions of usernames**: The solution anonymizes the names of users to prevent admins, data investigators, and reviewers from seeing who is associated with policy alerts. For example, a user 'Grace Taylor' appears with a randomized pseudonym such as 'AnonIS8-988' in all areas of the Insider Risk Management experience. Choosing this setting anonymizes all users with current and past policy matches and applies to all policies.

    Important

    If you're using the [Triage Agent for Insider Risk Management](copilot-in-purview-agents-overview), user names in prioritized alerts aren't anonymized in the [Triage Agent dashboard](insider-risk-management-activities#triage-agent-in-insider-risk-management-dashboard) if **Show anonymized versions of usernames** is enabled.

    User profile information in the insider risk alert and case details won't be available when this option is chosen. However, names of users that appear in the metadata of an activity, in the metadata of files in Content explorer, and within content of files in Content explorer **aren't anonymized**. Usernames are displayed when adding new users to existing policies or when assigning users to new policies. If you choose to turn off this setting, usernames are displayed for all users that have current or past policy matches.

    Important

    To maintain referential integrity for users who have insider risk alerts or cases in Microsoft 365 or other systems, anonymization of usernames isn't preserved for exported alerts when using the exporting API or when exporting to [Microsoft Purview eDiscovery solutions](ediscovery). Exported alerts display usernames for each alert in this case. If you export to CSV files from alerts or cases, anonymization *is* preserved.
- **Do not show anonymized versions of usernames**: Usernames are displayed for all current and past policy matches for alerts and cases. User profile information (the name, title, alias, and organization or department) is displayed for the user for all Insider Risk Management alerts and cases.

## Change the privacy setting

Perform the following steps to change the privacy setting for displayed usernames:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Privacy**.
5. Select the option you want, to show anonymized names or not.