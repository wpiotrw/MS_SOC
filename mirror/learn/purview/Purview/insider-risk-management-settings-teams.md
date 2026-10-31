---
layout: Conceptual
title: Enable Microsoft Teams for collaborating on Insider Risk Management cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about enabling Microsoft Teams for collaborating on Microsoft Purview Insider Risk Management cases.
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
document_id: 4b5aaf31-ecf1-1ee4-63c9-c3209fffc987
document_version_independent_id: 4b5aaf31-ecf1-1ee4-63c9-c3209fffc987
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-teams.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-teams
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-teams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: d6b5ed78-0254-b092-14ef-82b46b3aae47
---

# Enable Microsoft Teams for collaborating on Insider Risk Management cases | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Compliance analysts and investigators can use Microsoft Teams to collaborate on Microsoft Purview Insider Risk Management cases. They can communicate with other stakeholders on Teams to:

- Coordinate and review response activities for cases in private Teams channels
- Securely share and store files and evidence related to individual cases
- Detect and review response activities by analysts and investigators

When you enable Teams for Insider Risk Management, the solution creates a dedicated team every time you confirm an alert and create a case. By default, the team automatically includes all members of the *Insider Risk Management*, *Insider Risk Management Analysts*, and *Insider Risk Management Investigators* role groups (up to 100 initial users). You can add additional organization contributors to the team after it's created and as appropriate.

For existing cases created before enabling Teams, analysts and investigators can choose to create a new team when working on a case, if needed. When you resolve the Insider Risk Management case linked to that team, the solution automatically archives the team (moves to hidden and read-only).

Learn more: [Overview of teams and channels in Microsoft Teams](/en-us/MicrosoftTeams/teams-channels-overview).

## Enable Teams support

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Microsoft Teams (preview)**.
5. Turn the setting on.
6. Select **Save**.

## Create a team for existing cases

If you enable Teams support for Insider Risk Management after you have existing cases, you need to manually create a team for each case, as needed. Users need permission to create Microsoft 365 Groups in your organization to create a team from a case. For more information about managing permissions for Microsoft 365 Groups, see [Manage who can create Microsoft 365 Groups](/en-us/microsoft-365/solutions/manage-creation-of-groups).

Note

After enabling Teams support in Insider Risk Management settings, when you create a new case, the system automatically creates a new team.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation, then select an existing case.
4. On the case action menu, select **Create Microsoft Team**.
5. In the **Team name** field, enter a name for the new Microsoft Teams team.
6. Select **Create Microsoft team**, then select **Close**.

Depending on the number of users assigned to Insider Risk Management role groups, it might take 15 minutes for all investigators and analysts to be added to the newly created Microsoft Teams team for the case.