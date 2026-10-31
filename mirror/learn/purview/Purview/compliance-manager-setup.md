---
layout: Conceptual
title: Get started with Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-setup
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-11-27T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
- highpri
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-ga-blocked
search.appverid:
- MOE150
- MET150
description: Set up user permissions and roles, and set up automated testing, for Microsoft Purview Compliance Manager.
locale: en-us
document_id: ddcc77a8-14c1-dc0f-e67d-53f76a5b8d55
document_version_independent_id: ddcc77a8-14c1-dc0f-e67d-53f76a5b8d55
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-setup.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-setup.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: c3b92ca1-f505-be46-8e90-31559375d8ea
---

# Get started with Microsoft Purview Compliance Manager | Microsoft Learn

## Who can access Compliance Manager

Compliance Manager is available to organizations with Office 365 and Microsoft 365 licenses, and to US Government Community Cloud (GCC) Moderate, GCC High, and Department of Defense (DoD) customers. Assessment availability and management capabilities depend on your licensing agreement. [View service description details](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).

## Sign in

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for an admin account in your Microsoft 365 organization:
2. Select **Compliance Manager** on the left navigation pane. You arrive at your Compliance Manager dashboard.

## Set user permissions and assign roles

Compliance Manager uses a role-based access control (RBAC) permission model. Only users who are assigned a role can access Compliance Manager, and the actions allowed by each user are restricted by role type. Our RBAC model also allows you to grant user access to individual assessments. See role-based access to assessments below to learn more.

The person holding the Global Administrator role or Compliance Manager Administrator role for your organization can set user permissions for Compliance Manager. Permissions can be set in one of the following places:

- [Permissions in the Microsoft Purview portal](purview-permissions)
- [Permissions in Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-assign-role-azure-portal)

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Note

- Users with Microsoft Entra identities who don't have Office 365 or Microsoft 365 subscriptions won't be able to access Compliance Manager in the Microsoft Purview portal. To seek assistance in accessing Compliance Manager, contact cmresearch@microsoft.com.
- Customers in US Government Community (GCC) High and Department of Defense (DoD) environments can only set user permissions and roles for Compliance Manager in Microsoft Entra ID. See the Microsoft Entra permissions instructions and role type definitions.

### Role types

The table below shows the functions allowed by each role in Compliance Manager. The table also shows how each [Microsoft Entra role](/en-us/azure/active-directory/roles/permissions-reference) maps to Compliance Manager roles. Users need at least the Compliance Manager reader role, or Microsoft Entra global reader role, to access Compliance Manager.

A user can only hold one role at a time. Any change in a user's role overrides their previous role.

| User can: | Compliance Manager role | Microsoft Entra role |
| --- | --- | --- |
| **Read but not edit data** | Compliance Manager Reader | Microsoft Entra Global reader, Security reader |
| **Edit data and create assessments - for example, can edit improvement action status, enter notes, upload evidence; can create assessments** | Compliance Manager Contribution | Compliance Administrator |
| **Edit data only - can't create assessments** | Compliance Manager Assessor | Compliance Administrator |
| **Manage assessments, regulatory templates, and tenant data; assign improvement actions** | Compliance Manager Administration | Compliance Administrator, Compliance Data Administrator, Security Administrator |

### Role-based access to assessments and regulations

You can assign roles to users in order to grant access to specific assessments, or all assessments based on the regulation. Granting user access in these ways is useful when you need to ensure that only the people working on certain regulatory requirements have access to that data.

These four roles provide access to assessments:

- Compliance Manager Reader
- Compliance Manager Contribution
- Compliance Manager Assessor
- Compliance Manager Administration

What you can do with each assessment remains restricted based on which activities the role allows.

To grant users access to an assessment or all assessments for a regulation, open its details page and select **Manage users access** to add users by role. If a user has a role assigned to them in the Microsoft Purview portal for overall access to Compliance Manager, any role you assign them for a specific assessment applies only to that assessment.

**More information**:

- See [Grant user access to assessments](compliance-manager-assessments#grant-user-access-to-individual-assessments) for more detailed instructions.
- See [Grant user access to regulations](compliance-manager-regulations#grant-user-access-to-regulations) for more detailed instructions.
- Learn more about managing all users' access to assessments in Compliance Manager settings.

## Start a premium assessments trial

The Compliance Manager premium assessments trial is a great way to quickly create assessments that are most relevant to your organization. Our library of over 360 regulatory templates correspond to governmental regulations and industry standards around the world. Learn more about the [premium assessments trial](compliance-easy-trials-compliance-manager-assessments).

## Compliance Manager settings

To locate Compliance Manager settings in the [Microsoft Purview portal](https://purview.microsoft.com), select the **Settings** icon at the top of the page, then select **Compliance Manager**.

The types of settings for Compliance Manager include:

- Testing source: Allows you to turn off or on the automatic testing of improvement actions.
- Manage user history: Allows you to manage the data of users associated to improvement actions, including the ability to reassign improvement actions to a different user.
- User access: Allows you to view and manage user roles for access to assessments or assessment templates.
- [Connectors](compliance-manager-connectors): Allows you to activate and manage connectors for non-Microsoft services. Get details about [accessing connectors](compliance-manager-connectors#step-2-activate-the-connector-in-compliance-manager) in the portal.

Compliance Manager settings are accessible by users who hold a Compliance Manager Administrator role or Global Administrator role.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Testing source for automated testing

Compliance Manager detects various signals to provide automated testing and monitoring of improvement actions. This automation derives from three primary sources: built-in, Microsoft Secure Score, and Microsoft Defender for Cloud ([get details about automated testing sources](compliance-manager-improvement-actions#automated-testing-and-monitoring)). Compliance Manager also detects signals from Microsoft Priva (this capability is in preview; [learn more](/en-us/privacy/priva/priva-overview#how-priva-works-with-microsoft-purview-risk-and-compliance-solutions)). When an improvement action is successfully tested and implemented, you receive the maximum possible points for that action, which gets credited to your overall compliance score.

#### Initial settings

While automated testing helps maximize efficiency in your compliance activities, you have full control over whether to apply automated testing. Here's what's initially set up by Compliance Manager and how you can make changes:

- The first time you use Compliance Manager, automatic testing is turned on by default for all actions that can be automatically tested. It takes approximately seven days to fully collect data and factor that data into your compliance score.
- You can turn off automatic testing for all actions, which disables all automated activity on improvement actions by Compliance Manager. You can also select individual improvement actions for automatic testing. See Manage automated testing settings for instructions.

#### How to tell which actions are tested automatically

On an improvement action’s details page, the **Testing type** status in the top information bar shows how the action is tested. If the value is listed as **Automatic**, then the action is automatically tested. If the value is **Manual**, then the action is tested by your organization. Get details about [improvement action testing type](compliance-manager-improvement-actions#testing-type).

#### When actions are added or updated

When automation becomes available for existing improvement actions, or when new automated improvement actions are added, the default behavior depends on your current settings and whether or not you've [brought data into an improvement action](compliance-manager-update-actions). When you add your own testing data or evidence into an improvement action, automatic testing is turned off for that action to ensure that Compliance Manager doesn't overwrite any of your data.

If you've added data to an existing improvement action:

- Automated testing remains **off** by default for the action. You can choose to turn it back on.

If you haven't added data to an improvement action, or when new automated actions are added to Compliance Manager, the testing behavior follows your current settings:

- Automated testing is **on** if your setting is **on** for **all actions** or **per action**.
- Automated testing is **off** if your setting is **off for all actions**.

#### Manage automated testing settings

The Compliance Manager Administrator and the Global Administrator for your organization can change the settings for automated testing at any time. You can turn off automated testing for common improvement actions, or turn it on for individual actions. Follow the instructions below to change your automated testing settings. When you change a setting, it will be reflected in the audit log. Learn more about [Compliance Manager activities in the audit log](audit-log-activities#compliance-manager-activities).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. In Compliance Manager, select **Compliance Manager settings** in top right corner of the page.
2. Select **Testing source** from the left navigation.
3. Select your desired option for testing improvement actions:

    1. Turn on automatic testing for all actions.
    2. Turn off automatic testing for all actions.
    3. Turn on automatic testing per action.
4. If you select **Turn on per improvement action**, a list displays all the improvement actions that are eligible for testing. All actions are checked by default, so you need to uncheck the actions you **don't** want to be automatically tested.
5. Select **Save** to save your settings. You receive a confirmation message at the top of your screen that your selection was saved. If you receive a failure notice, try again.

## Manage user history

The **Manage user history** settings help you quickly identify which users have worked with improvement actions in Compliance Manager. The identifiable user data associated with improvement actions includes the status of the improvement actions and documents they uploaded. Understanding and retrieving this type of data might be necessary for your organization’s own compliance needs.

The user history settings also allow you to reassign all improvement actions from one user to another.

**To find the user history settings:**

1. In Compliance Manager, select **Compliance Manager settings** in the top right corner of the page.
2. Select **Manage user history** from the left navigation.

The **Manage user history** page shows a list of all users by email address who are assigned to an improvement action. Use the **Search** button to quickly find a specific user by typing in their email address.

To the right of each user’s email address, the **Select** drop-down menu provides options to export a report, reassign improvement actions, or delete history. See each section below for details about each option.

#### Export a report of user history data

You can export an Excel file containing a list of improvement actions currently assigned to a user. The report also lists any evidence files uploaded by that user. This information can help you reassign open improvement actions.

The report reflects the improvement action’s status as of its creation date. It’s not a historical report of all previous changes to its status or assignment (learn how to [export a report from your improvement actions page](compliance-manager-improvement-actions#export-a-report-of-all-improvement-actions)).

**Follow the steps below to export a report by user:**

1. In Compliance Manager, select **Compliance Manager settings** in top right part of the page.
2. Select **Manage user history** from the left navigation.
3. Find your intended user by searching the list email addresses, or by selecting **Search** and entering the user’s email address.
4. From the **Select** drop-down menu, choose **Export report**.
5. Once the Excel file of your report is generated, you can open it and save it to your local machine.

#### Reassign improvement actions to another user

You can reassign ownership of improvement actions from one user to another. When you reassign an action, the evidence upload history doesn't change, but the name of the user who originally uploaded evidence no longer appears within the improvement action.

**Follow the steps below to reassign improvement actions to another user:**

1. In Compliance Manager, select **Compliance Manager settings** in top right corner of the page.
2. Select **Manage user history** from the left navigation.
3. Find a user by searching the list email addresses, or by selecting **Search** and entering that user’s email address.
4. From the **Select** drop-down menu, choose **Reassign improvement actions**. The **Reassign improvement actions** flyout pane appears.
5. In the **Search users** field, enter the name or email address of the user to whom you're assigning the improvement actions.
6. When you see the name of your intended user under **Improvement actions will be assigned to**, select the user, then select **Assign actions**.
7. When the reassignment is complete, you see a confirmation message in the flyout pane confirming that all improvement actions from the previous user have been reassigned to the new user. If you receive a reassignment failure notice, close the window and try again. To close the flyout pane, select **Done**.

The new owner receives an email that they've been assigned to an improvement action. The email contains a direct link into the improvement action's details page.

Note

If you reassign an action that has a pending update, the direct link to the action in the reassignment email will break if the update is accepted after reassignment. You can fix this by re-assigning the action to the user after the update is accepted. Learn more about [updates to improvement actions](compliance-manager-improvement-actions#accepting-updates-to-improvement-actions).

#### Delete user history

Deleting a user’s history removes them as an owner of improvement actions and removes their name from all other fields in Compliance Manager. When you delete a user’s history, the improvement actions they owned won't display an **Assigned to** value until a new user is assigned. Evidence uploaded to the improvement action shows **User removed** in place of the deleted user’s name. Deleting user history is permanent.

To delete a user’s history, follow the steps below:

1. In Compliance Manager, select **Compliance Manager settings** in top right corner of the page.
2. Select **Manage user history** from the left navigation.
3. Find a user by searching the list email addresses on the page, or by selecting **Search** and entering that user’s email address.
4. From the **Select** drop-down menu, choose **Delete history**.
5. A window asks you to confirm the permanent deletion of the user’s history. To continue with deletion, select **Delete history**. To leave without deleting the history, select **Cancel**.

You arrive back at the **Manage user history** page with a confirmation message at the top that the history for the user was deleted.

## User access

The **User access** section of **Settings** displays a list of all users who have a role that allows access to one or more assessments. From this page, you can make changes to role assignments. When you change a setting, it will be reflected in the audit log. Learn more about [Compliance Manager activities in the audit log](audit-log-activities#compliance-manager-activities).

- When you grant a user access to an **assessment**: The user has access to just that one assessment.
- When you grant a user access to a **regulation**: The user will have access to any assessment created with that regulation, including existing assessments and any assessments created in the future.

To add or remove user access roles for assessments and regulations, follow the steps below:

1. In Compliance Manager, select **Compliance Manager settings** in top right part of the page.
2. Select **User access** from the left navigation.
3. Select the checkbox next to the name of one or more users whose role you want to edit.
4. Depending on whether you're editing roles for assessments or regulations: From the **Edit assessment roles** or **Edit regulation roles** dropdown menu above the list of names, select **Add assessment/regulation permissions** or **Remove assessment/regulation permissions**.
5. **For adding a role**: From the flyout pane, go to the tab that corresponds to the role you want to add (Reader, Assessor, or Contributor), then select **Add assessments/regulations**. On the next flyout pane, choose the checkbox next to the assessments/regulations and select **Apply**, then select **Save**.
6. **For removing a role**: From the flyout pane, go to the tab that corresponds to the role you want to remove (Reader, Assessor, or Contributor). Select the button next to the assessments/regulations for which you want to remove access, and select the X mark in the **Remove** column.

    1. A **Remove access?** confirmation box appears. Select **Confirm** to remove the user's role, or select **Cancel** to cancel. The name of the assessments will now be removed from the role tab.
    2. Select **Save** on the flyout pane. The role removal won't be completed until you select the **Save** button. Selecting **Close** will cancel out of the process without saving the role removal.

The user list on the **User access** page will now reflect the changes you made.

Note

Admins whose permissions for Compliance Manager were set in Microsoft Entra ID won't appear on the **User access** page. This means that if a user has access to one or more assessments, and their role is Global Administrator, Compliance Administrator, Compliance Data Administrator, or Security Administrator, they won't appear on this page. Learn more about setting Compliance Manager permissions.

**More information**:

- [Visit these instructions](compliance-manager-assessments#grant-user-access-to-individual-assessments) for assigning user roles from an assessment's details page.

## Understand the Compliance Manager dashboard

The Compliance Manager dashboard is designed to provide you an at-a-glance view of your current compliance posture.

## Overview page

### Your compliance score

Your compliance score is featured prominently at the top of the **Overview** page. The score is a percentage based on points achievable for completing improvement actions that address key data protection standards and regulations. Points from [Microsoft actions](compliance-manager-assessments#microsoft-actions-tab), which are managed my Microsoft, also count toward your compliance score.

When you come to Compliance Manager for the first time, your initial score is based on the [Microsoft 365 data protection baseline](compliance-manager-assessments#data-protection-baseline-default-assessment). This baseline assessment, which is available to all organizations, is a set of controls that includes common industry regulations and standards. Compliance Manager checks your existing Microsoft 365 solutions and gives you an initial assessment based on your current privacy and security settings. As you add assessments that are relevant to your organization, your score becomes more meaningful for you.

**Learn more:**[Understand how your compliance score is calculated](compliance-score-calculation).

### Key improvement actions

This section lists the top improvement actions you can take right now to make the largest positive impact on your overall compliance score. Select **View all improvement actions** to go to your improvement actions page.

### Solutions that affect your score

This section highlights solutions containing improvement actions that can positively impact your score, and the number of outstanding improvement actions in those solutions. Select **View all solutions** to visit your solutions page.

### Compliance score breakdown

This section gives you a more detailed view of your score in two different ways:

- **Categories**: shows the percentage of your overall score within data protection categories, such as "protect information" or "manage devices."
- **Assessments**: shows the percentage of your progress in managing assessments for particular compliance and data protection standards, regulations, or laws, such as GDPR or NIST 800-53.

### Filtering your dashboard view

You can filter your dashboard view to see only the items related to particular regulations and standards, solutions, type of action, assessment groups, or data protection categories. Filtering your view in this way will also filter the score on your dashboard, showing how many points you've achieved out of total possible points based on your filter criteria.

To apply filters:

1. Select **Filter** on the upper-right side of the dashboard.
2. Select your filter criteria from the **Filters** flyout pane, then select **Apply**.

After you apply a filter, you’ll see your score adjusted in real time. The compliance score percentage and breakdown information, and the improvement actions and solutions, now only pertain to data covered by your filter criteria. If you sign out of Compliance Manager, your filtered view remains when you sign back in.

To remove filters:

- At the **Applied filters** heading above your compliance score, select the **X** next to the individual filter you want to remove; or
- Select **Filter** on the upper-right side of your dashboard, then on the **Filters** flyout pane, select **Clear filters**.

## Improvement actions page

[Improvement actions](compliance-manager-improvement-actions) are recommended actions that can help to centralize your compliance activities and align with data protection regulations and standards. Each improvement action gives detailed implementation guidance and a link to launch you into the appropriate solution. Improvement actions can be assigned to users in your organization to perform implementation and testing work. You can also store evidence, notes, and record status updates within the improvement action.

## Solutions page

The **Solutions** page shows the share of earned and potential points as organized by solution. Viewing your remaining points and improvement actions from this view helps you understand which solutions need more immediate attention.

Find the solutions page by selecting the **Solutions** tab on your Compliance Manager dashboard. You can also select **View all solutions** underneath **Solutions that affect your score** in the upper-right section of your dashboard. To filter your view of solutions:

1. Select **Filter** at the top-left corner of your assessments list.
2. On the **Filters** flyout pane, place a check next to the desired criteria (regulations, solutions, action types, groups, categories).
3. Select the **Apply** button. The filter pane closes and you see your filtered view.

You can also modify your view to see assessments by group, product, or regulation by selecting the type of grouping from the **Group** drop-down menu above your assessments list.

#### Taking action from the solution page

The **Solutions** page displays your organization’s solutions that are connected to improvement actions. The table lists each solution’s contribution to your overall score, the points achieved and possible within that solution, and the remaining number of improvement actions grouped in that solution that can increase your score.

There are two ways you can take action from this screen:

1. On the row of your intended solution, under the **Remaining actions** column, select the hyperlinked number. You see a filtered view of the improvement actions screen showing untested improvement actions for that solution.
2. On the row of your intended solution, under the **Open solution** column, select **Open**. You arrive at the solution's location in the Microsoft Purview portal, Microsoft Defender portal, or its admin center, where you can take the recommended action.

## Assessments page

The **Assessments** page lists all the assessments you set up for your organization. Your compliance score denominator is determined by all your tracked assessments. As you add more assessments, you see more improvement actions listed on your improvement actions page, and your compliance score denominator increases. See [Build and manage assessments](compliance-manager-assessments) to learn about assessment status and how to create new assessments.

## Regulations page

A regulatory template is a framework for creating an assessment in Compliance Manager. The **Regulations** page displays a list of regulatory templates and key details. The **Free regulation licenses used/Purchased regulation licenses used** counter near the top of the page shows the number of active regulations currently in use out of the total number available for your organization to use. See [Regulation availability and licensing](compliance-manager-regulations#regulation-availability-and-licensing) for more information.

## Policies page

The **Policies** page lists policies you set up to alert you to key changes within Compliance Manager that affect your compliance score. Visit [Compliance Manager alerts and alert policies](compliance-manager-alert-policies) to learn more.

## Alerts page

The **Alerts** page lists alerts generated by policies you set up to track changes within Compliance Manager that affect your compliance score. Visit [Compliance Manager alerts and alert policies](compliance-manager-alert-policies) to learn more.

## Reports page

The **Reports** page displays a history report of activities in Compliance Manager within the previous seven days. You can look up data from the previous six months by adjusting filters.

The **Reports** page displays your compliance score and a chart representing your organization's overall compliance posture. Select **View detailed report** to bring up a detailed history report page. A table lists improvement actions that have had a score change within the last month. It takes about 24 hours for changes in an action to be reflected in the report.

Select an improvement action from its row on the table to see a details pane that explains the action, the related regulation, associated assessments, and score update. You can launch into the action by selecting **Go to action**. Select the **History** tab on the pane to view the score history for the action.

##### Filter by date range, regulation, and service

On the history report page, you can adjust the filters to broaden or refine the view of actions that appear in the table. Select the **Date range** filter to select a range that can retrieve data up to six months prior. Select **Add filter** to apply other filters that apply to actions based on regulation or by cloud service.