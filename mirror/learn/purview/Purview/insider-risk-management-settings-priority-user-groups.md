---
layout: Conceptual
title: Prioritize user groups for Insider Risk Management policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-priority-user-groups
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the Priority user groups settings for Microsoft Purview Insider Risk Management.
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
document_id: 6a963ccd-d658-ee99-5710-26d901df9ea4
document_version_independent_id: 6a963ccd-d658-ee99-5710-26d901df9ea4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-priority-user-groups.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-priority-user-groups
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-priority-user-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 60a5bf6d-485f-e9f8-24ca-63c868818ce2
---

# Prioritize user groups for Insider Risk Management policies | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Users in your organization might have different levels of risk depending on their position, level of access to sensitive information, or risk history. Prioritizing the examination and scoring of the activities of these users can help alert you to potential risks that might have higher consequences for your organization. Priority user groups in Microsoft Purview Insider Risk Management help define the users in your organization that need closer inspection and more sensitive risk scoring. Coupled with the *Security policy violations by priority users* and *Data leaks by priority users* policy templates, users you add to a priority user group have an increased likelihood of insider risk alerts and alerts with higher severity levels.

![Screenshot of the Insider Risk Management priority user group settings page showing options for defining and managing priority user groups.](media/insider-risk-settings-priority-users.png)

Instead of being open to review by all analysts and investigators, you might need to restrict review activities for priority user groups to specific users or insider risk role groups. You can assign individual users and role groups to review users, alerts, cases, and reports for each priority user group. You can assign review permissions for priority user groups to the built-in *Insider Risk Management*, *Insider Risk Management Analysts*, and *Insider Risk Management Investigators* role groups, one or more of these role groups, or to a custom selection of users.

For example, you need to protect against data leaks for a highly confidential project where users have access to sensitive information. You choose to create the *Confidential Project Users* priority user group for users in your organization that work on this project. Also, you don't want all the default Insider Risk Management admins, analysts, and investigators to see users, alerts, cases, and reports associated with this priority user group. In settings, you create the *Confidential Project Users* priority user group and assign two users as reviewers that can view data related to the group. Use the policy workflow and the *Data leaks by priority users* policy template to create a new policy and assign the *Confidential Project Users* priority users group to the policy. Activities examined by the policy for members of the *Confidential Project Users* priority user group are more sensitive to risk and activities by these users are more likely to generate alerts and have alerts with higher severity levels.

## Create a priority user group

You must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group to create a priority user group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) as a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Priority user groups**.
5. On the **Priority user groups** page, select **Create priority user group** to start the group creation workflow.
6. On the **Name and describe the priority user group** page, complete the following fields:

    - **Name (required)**: Enter a friendly name for the priority user group. You can't change the name of the priority user group after you complete the workflow.
    - **Description (optional)**: Enter a description for the priority user group.
7. Select **Next** to continue.
8. On the **Choose members** page, select **Choose members** to search and select which mail-enabled user accounts are included in the group or select the **Select all** checkbox to add all users in your organization to the group. Select **Add** to continue.

    Note

    You can add up to 10,000 users to a priority user group.
9. Select **Upload** to add members by uploading a CSV file if needed. The .csv file must have a column titled *user principal name* with the list of users you want to add.
10. Select **Next** to continue.
11. On the **Choose who can view this group** page, you must define who can review users, alerts, cases, and reports for the priority user group. Assign at least one user or Insider Risk Management role group. Select **Choose users and role groups**, and then select the users or Insider Risk Management role groups you want to assign to the priority user group. Select **Add** to assign the selected users or role groups to the group.
12. Select **Next** to continue.
13. On the **Review** page, review the settings you chose for the priority user group. Select the **Edit** links to change any of the group values or select **Submit** to create and activate the priority user group.
14. On the confirmation page, select **Done**.

## Update a priority user group

To update a priority user group, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) as a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Priority user groups**.
5. Select the priority user group you want to edit, then select **Edit group**.
6. On the **Name and describe** page, update the **Description** field if needed. You can't update the name of the priority user group. Select **Next** to continue.
7. On the **Choose members** page, add new members to the group using the **Choose members** control. To remove a user from the group, select the 'X' next to the user you want to remove. Select **Next** to continue.
8. On the **Choose who can view this group** page, add or remove users or role groups that can review users, alerts, cases, and reports for the priority user group.
9. Select **Next** to continue.
10. On the **Review** page, review the update settings for the priority user group. Select the **Edit** links to change any of the group values or select **Submit** to update the priority user group.
11. On the confirmation page, select **Done**.

## Delete a priority user group

Important

Deleting a priority user group removes it from any active policy to which it's assigned. If you delete a priority user group that an active policy uses, the policy has no included users. The policy is idle and doesn't create alerts.

To delete a priority user group, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admin* role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) as a member of the *Insider Risk Management* or *Insider Risk Management Admin* role group.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Priority user groups**.
5. Select the priority user group you want to delete, then select **Delete**.
6. In the **Delete** dialog box, select **Yes**.