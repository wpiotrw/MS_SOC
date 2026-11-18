---
layout: Conceptual
title: Configure app role settings in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/app-roles-settings
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: kenwith
ms.author: kenwith
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to configure activation, assignment, approval, and notification settings for app roles in Microsoft Entra Privileged Identity Management.
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.custom: pim, msecd-doc-authoring-1031
ai-usage: ai-generated
locale: en-us
document_id: 6cd6f6da-fcf2-b8df-2d4b-c983b1ea7374
document_version_independent_id: 6cd6f6da-fcf2-b8df-2d4b-c983b1ea7374
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/app-roles-settings.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/app-roles-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/app-roles-settings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 2f8236ac-84c5-ad67-deb2-f6e6ed9f0679
---

# Configure app role settings in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn

In Privileged Identity Management (PIM) in Microsoft Entra ID, which is part of Microsoft Entra, role settings define role assignment properties. These properties include multifactor authentication and approval requirements for activation, assignment maximum duration, and notification settings. This article shows you how to configure role settings and set up the approval workflow to specify who can approve or deny requests to elevate privilege.

## Prerequisites

To modify app role settings, you need PIM AdminReadWrite permissions. The `microsoft.directory/servicePrincipals/appRoleAssignedTo/update` permission grants this access. Each of the administrative roles listed in [Role assignment conditions](app-roles-assign#permissions) provides the required permission.

PIM role settings are also known as PIM policies.

## Open role settings

To open the settings for an app role:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**.
3. Select the application for which you want to configure role settings. Use the application and object IDs in the application list to identify the intended application.
4. Under **Manage**, select **Settings**. View the list of roles and the **Modified**, **Last updated**, and **Last updated by** columns.
5. Select the role that you want to configure to open **Role setting details**.
6. Review the current role settings.
7. Select **Edit** to update role settings.
8. Configure the **Activation**, **Assignment**, and **Notification** tabs as described in Role settings. Use the tab names or the **Next: Assignment**, **Next: Notification**, **Prev: Activation**, and **Prev: Assignment** buttons to move between sections.
9. Select **Update** to save your changes.
10. Review the notification. PIM shows **Updating role settings** while processing the change and **Role setting update succeeded** when it succeeds.
11. Return to **Settings** and reopen the role to confirm that **Role setting details** reflects your changes. The **Settings** list also shows **Modified**, **Last updated**, and **Last updated by**.

## Role settings

For background on eligible and active app role assignments, see [PIM for app roles (preview)](concept-pim-for-app-roles).

### Activation maximum duration

On the **Activation** tab, use the **Activation maximum duration (hours)** slider or numeric field to set the maximum activation duration. This duration concerns activation of an eligible assignment, rather than the lifetime of the eligible assignment itself.

### On activation, require multifactor authentication

You can require users who are eligible for a role to prove who they are by using multifactor authentication (MFA) before they can activate. On the **Activation** tab, **On activation, require** offers **None**, **Azure MFA**, and **Microsoft Entra Conditional Access authentication context**.

Select **Azure MFA** to configure the MFA requirement. The authentication-context option is also present, but its additional configuration isn't shown in the supplied editor views.

### Require justification on activation

On the **Activation** tab, select **Require justification on activation** to require users to enter a business justification when they activate an eligible assignment.

### Require ticket information on activation

On the **Activation** tab, select **Require ticket information on activation** to require users to enter ticket information when they activate an eligible assignment.

### Require approval to activate

You can require approval for activation of an eligible assignment. On the **Activation** tab:

1. Select **Require approval to activate**.
2. Open **Select approver(s)**.
3. In **Select a member**, use **Search** or the **All**, **Users**, and **Groups** tabs to find the intended approvers.
4. Select the checkboxes for the intended entries, and then select **Select**.
5. Review **Selected approvers**. Use **Remove** to remove an entry you don't want.

The **Activation** tab also includes **Require pre-approval custom extension to activate (Preview)** and **Require post-approval custom extension to activate (Preview)**.

To learn more about approvals, see [Approve or deny app role requests in PIM (preview)](app-roles-approval-workflow).

### Assignment duration

When you configure settings for a role, you can choose assignment duration options for each assignment type: *eligible* and *active*.

On the **Assignment** tab, configure the permanent-assignment checkboxes and the corresponding expire-after dropdowns. The expiry dropdowns are disabled in the supplied configuration while permanent assignments are allowed.

You can choose from these eligible assignment duration settings.

| Setting | Description |
| --- | --- |
| **Allow permanent eligible assignment** | Allows eligible assignments without an end date. |
| **Expire eligible assignments after** | Sets the expiration period for eligible assignments. |

You can also choose from these active assignment duration settings.

| Setting | Description |
| --- | --- |
| **Allow permanent active assignment** | Allows active assignments without an end date. |
| **Expire active assignments after** | Sets the expiration period for active assignments. |

Permanent eligibility doesn't remove the need to activate the role before use. Review the activation settings separately from the assignment duration settings.

For information about creating assignments, see [Assign app roles in PIM (preview)](app-roles-assign). For information about changing an assignment's end date, see [Extend or renew app role assignments in PIM (preview)](app-roles-renew-extend).

### Require multifactor authentication on active assignment

You can require users who are eligible for a role to prove who they are by using the multifactor authentication feature in Microsoft Entra ID before they can activate. Multifactor authentication helps safeguard access to data and applications. It provides another layer of security by using a second form of authentication.

Users might not be prompted for multifactor authentication if they authenticated with strong credentials or provided multifactor authentication earlier in this session.

If your goal is to ensure that users must provide authentication during activation, you can use [On activation, require Microsoft Entra Conditional Access authentication context](pim-how-to-change-default-settings#on-activation-require-azure-ad-conditional-access-authentication-context) together with [Authentication Strengths](../../identity/authentication/concept-authentication-strengths). These options require users to authenticate during activation by using methods different from the one they used to sign in to the machine.

For example, if users sign in to the machine by using Windows Hello for Business, you can use **On activation, require Microsoft Entra Conditional Access authentication context** and **Authentication Strengths** to require users to do passwordless sign-in with Microsoft Authenticator when they activate the role.

After the user provides passwordless sign-in with Microsoft Authenticator once in this example, they can do their next activation in this session without another authentication. Passwordless sign-in with Microsoft Authenticator is already part of their token.

Enable the multifactor authentication feature of Microsoft Entra ID for all users. For more information, see [Plan a Microsoft Entra multifactor authentication deployment](../../identity/authentication/howto-mfa-getstarted).

### Require justification on active assignment

You can require the person creating an active (as opposed to eligible) assignment to enter a business justification.

When justification is required, the assignment creator enters it in **Enter justification** on the assignment wizard's **Setting** tab. The form shows required-field validation if the justification is missing.

On the **Assignment** tab, use **Require justification on active assignment** to configure this requirement.

### Notifications

Privileged Identity Management enables granular control over who receives notifications and which notifications they receive. The app-role notification summary includes eligible assignment, active assignment, and activation rows, with default recipients, additional recipients, and a critical-emails-only option.

On the **Notification** tab, configure each notification's **Default recipients**, **Additional recipients**, and **Critical emails only** controls. Notifications are grouped into eligible assignments, active assignments, and eligible-member activations.

For rows that accept additional recipients, enter email addresses separated by semicolons.

The editor shows these recipient categories:

| Notification group | Notification | Recipient category shown |
| --- | --- | --- |
| Eligible or active assignments | Role assignment alert | Admin. |
| Eligible or active assignments | Notification to the assigned user (assignee) | Assignee. |
| Eligible or active assignments | Request to approve a role assignment renewal/extension | Approver. |
| Eligible-member activation | Role activation alert | Admin. |
| Eligible-member activation | Notification to activated user (requestor) | Requestor. |
| Eligible-member activation | Request to approve an activation | Approver. |

Use the controls as follows:

- **Turn off an email**: Clear its default-recipient checkbox and remove any editable additional recipients.
- **Limit emails to specified email addresses**: For a row that accepts additional recipients, clear its default-recipient checkbox and enter the intended addresses.
- **Send emails to both default recipients and additional recipients**: Keep the default-recipient checkbox selected and add the intended addresses.
- **Critical emails only**: Select this checkbox to limit the notification to critical emails.

For **Request to approve an activation**, the additional-recipient field is disabled and states **Only designated approvers can receive this email**. Configure those recipients through **Select approver(s)** on the **Activation** tab, not by adding arbitrary email addresses.