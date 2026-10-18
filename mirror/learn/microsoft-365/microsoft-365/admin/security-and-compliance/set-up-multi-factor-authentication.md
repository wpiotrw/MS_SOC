---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set up multifactor authentication for users - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: deniseb
author: denisebmsft
manager: dansimp
ms.date: 2025-12-10T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: microsoft-365-admin
ms.localizationpriority: high
ms.collection:
- Tier1
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- adminvideo
- business_assist
- security
description: Learn how to set up multifactor authentication (also known as MFA, two-factor authentication, or 2FA) in your Microsoft 365 organization.
customer-intent: As an administrator, I want to know about MFA and how to set it up.
locale: en-us
document_id: be1e6c9a-9644-6d86-3962-d36bf1efd656
document_version_independent_id: 96142d6c-71de-6ea9-0361-dbec82647b15
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/set-up-multi-factor-authentication
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: c1d34021-5160-da18-a872-4bfe0acbeb68
---

# Set up multifactor authentication for users - Microsoft 365 admin | Microsoft Learn

Multifactor authentication (also known as MFA, two-factor authentication, or 2FA) requires a second verification method for user sign-ins and improves account security.

This article contains instructions to set up MFA using the available options:

- Security defaults: Available in all Microsoft 365 organizations via Microsoft Entra ID Free.
- Conditional Access policies: Available in Microsoft 365 organizations with Microsoft Entra ID P1 or P2.
- Legacy per-user MFA (not recommended): Available in all Microsoft 365 organizations via Microsoft Entra ID Free.

For information about the different options for MFA in Microsoft 365, see [Multifactor authentication in Microsoft 365](multi-factor-authentication-microsoft-365)

## What do you need to know before you begin?

- You must have appropriate permissions assigned before you can complete the procedures in this article. Here are some options:

    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal):

        - Turn on or turn off security defaults: Membership in the **Global Administrator** or **Security Administrator** roles.
        - Create and manage Conditional Access policies: Membership in the **Global Administrator** or **Conditional Access Administrator** roles.

        Important

        Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
- To use security defaults or Conditional Access, you need to turn off legacy per-user MFA for users in your organization. If your organization's subscription was started after 2019, legacy per-user MFA is most likely not turned on. For more information, see [Enable per-user Microsoft Entra multifactor authentication to secure sign-in events](/en-us/entra/identity/authentication/howto-mfa-userstates).

Note

If you have non-Microsoft directory services with Active Directory Federation Services (AD FS) configured before July 2019, set up the Azure MFA Server. For more information, see [Advanced scenarios with Microsoft Entra multifactor authentication and non-Microsoft VPN solutions](/en-us/previous-versions/entra/identity/authentication/howto-mfaserver-nps-vpn).

## Manage security defaults

Microsoft 365 tenants created after October 2019 have security defaults turned on by default. To view or change the current status of security defaults in your organization, follow these steps:

1. In the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity** &gt; **Overview**. Or, to go directly to the [Microsoft Entra overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView).
2. On the overview page, select the **Properties** tab, and the go to the **Security defaults** section at the bottom of the tab.

    Depending on the current status of security defaults, one of the following experiences is available:

    - **Security defaults is on**: The following text is shown and **Manage security defaults** is available:

> 
> Your organization is protected by security defaults.
    - **One or more Conditional Access policies exist in Microsoft Entra ID P1 or P2**: The following text is shown and **Manage security defaults** isn't available:

> 
> Your organization is currently using Conditional Access policies which prevents you from enabling security defaults. You can use Conditional Access to configure custom policies that enable the same behavior provided by security defaults.

        **Manage Conditional Access** takes you to the [Policies page](https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/PoliciesList.ReactView) where you can manage Conditional Access policies. To switch between security defaults and Conditional Access policies, see the Revert to security defaults from Conditional Access policies section in this article.
    - **Security defaults is off**: The following text is shown and **Manage security defaults** is available:

> 
> Your organization is not protected by security defaults.
3. If **Manage security defaults** is available, select it to turn on or turn off security defaults.

    In the **Security defaults** flyout that opens, do one of the following:

    - **Turn on security defaults**: In the **Security defaults** dropdown list, select **Enabled**, and then select **Save**.
    - **Turn off security defaults**: In the **Security defaults** dropdown list, select **Disabled**. In the **Reason for disabling** section, select **My organization is planning to use Conditional Access**.

    When you're finished in the **Security defaults** flyout, select **Save**

Caution

Don't turn off security defaults unless you're switching to Conditional Access policies in Microsoft Entra ID P1 or P2.

## Manage Conditional Access policies

If your Microsoft 365 organization includes Microsoft Entra ID P1 or later, you can use Conditional Access instead of security defaults for a higher security posture and more granular control. For example:

- Microsoft 365 Business Premium (Microsoft Entra ID P1)
- Microsoft 365 E3 (Microsoft Entra ID P1)
- Microsoft 365 E5 (Microsoft Entra ID P2)
- An add-on subscription

For more information, see [Plan a Conditional Access deployment](/en-us/entra/identity/conditional-access/plan-conditional-access).

Switching from security defaults to Conditional Access policies requires the following basic steps:

1. Turn off security defaults.
2. Create baseline Conditional Access policies to recreate the security policies in security defaults.
3. Adjust MFA exclusions.
4. Create new Conditional Access policies.

Tip

If security defaults are turned on, you can create new Conditional Access policies, but you can't turn them on. After you turn off security defaults, you can turn on Conditional Access policies.

### Step 1: Turn off security defaults

Security defaults and Conditional Access policies can't be turned on at the same time, so the first thing you need to do is turn off security defaults.

For instructions, see the previous Manage security defaults section in this article.

### Step 2: Create baseline Conditional Access policies to recreate the policies in security defaults

The policies in security defaults are the Microsoft-recommended baseline for all organizations, so it's important to recreate these policies in Conditional Access before you create other Conditional Access policies.

The following templates in Conditional Access recreate the policies in security defaults:

- [Require MFA for all users](/en-us/entra/identity/conditional-access/howto-conditional-access-policy-all-users-mfa)
- [Require MFA for administrators](/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin) (To improve your security posture, see [Require phishing-resistant MFA for administrators](/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa))
- [Block legacy authentication](/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-legacy)
- [Require MFA for Azure management](/en-us/entra/identity/conditional-access/howto-conditional-access-policy-azure-management)

To create Conditional Access policies using these templates, follow these steps:

1. In the Microsoft Entra admin center, go to the [Conditional Access | Policies page](https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/%7E/Policies).
2. On the **Conditional Access | Policies** page, select ![](../../media/m365-cc-sc-create-icon.png)**New policy from template**.
3. On the **New policy from template** page, verify the **Select a template** tab is selected. On the **Select a template** tab, verify the **Secure foundation** tab is selected.
4. On the **Secure foundation** tab, select one of the required templates (for example, **Require multifactor authentication for all users**), and then select **Review + Create**.

    Tip

    To find and select the **Require phishing-resistant multifactor authentication for admins** template, use the ![](../../media/m365-cc-sc-search-icon.png)**Search** box.
5. On the **Review + Create** tab, view or configure the following settings:

    - **Basics** section:

        - **Policy name**: Accept the default name or customize it.
        - **Policy state**: Select **On**
    - **Assignments** section: In the **Users and groups** section, notice the **Excluded users** value is **Current user** and you can't change it. Only [emergency access accounts](/en-us/entra/identity/role-based-access-control/security-emergency-access) should be excluded from MFA requirements. For more information, see the next step.

    When you're finished on the **Review + Create** tab, select **Create**.

    The policy you created is shown on the **Conditional Access | Policies** page.
6. Repeat the previous steps for the remaining templates.

#### Step 3: Adjust MFA exclusions

By default, the Conditional Access policies you created in the previous step contains exclusions for the account you were signed in as, and you can't modify exclusions during policy creation.

We recommend at least two [emergency access admin accounts](/en-us/entra/identity/role-based-access-control/security-emergency-access) in every organization that aren't assigned to specific individuals and are only used in emergencies. These accounts need to be excluded from MFA requirements.

You might need to remove the current account exclusions and/or add emergency access account exclusions to the following policies:

- [Require MFA for all users](/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength#create-a-conditional-access-policy)
- [Require MFA for administrators](/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin) or [Require phishing-resistant MFA for administrators](/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa#create-a-conditional-access-policy)
- [Require MFA for Azure management](/en-us/entra/identity/conditional-access/policy-old-require-mfa-azure-mgmt#create-a-conditional-access-policy)

Before you create custom Conditional Access policies, create your emergency access accounts and then use the following steps to adjust the exclusions for MFA-related policies:

1. On the [Conditional Access | Policies page](https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/%7E/Policies), select one of the MFA-related policies that you created in the previous step (for example, **Require multifactor authentication for Azure management**).
2. On the policy details page that opens, select **All users included and specific users excluded** in the **Assignments** &gt; **Users** section.
3. In the information that appears, select the **Exclude** tab.
4. On the **Exclude** tab, the following settings are configured:

    - **Select the users and groups to exempt from the policy**: The value **Users and groups** is selected.
    - **Select excluded users and groups**: The value **1 user** is shown, and the user account that was used to create the policy is shown.

        - To remove the current account from the excluded users list, select ![](../../media/m365-cc-sc-more-actions-icon.png) &gt; ![](../../media/m365-cc-sc-delete-icon.png)**Remove**.

        The value changes to **0 users and groups selected** and the warning text **Select at least one user or group** appears.

        - To add emergency access accounts to the excluded users list, select **0 users and groups selected**. In the **Select excluded users and groups** flyout that opens, find and select the emergency access accounts to exclude. The selected users are shown in the **Selected** pane. When you're finished, select **Select**.

        Back on the policy details page, select **Save**.
5. Repeat the previous steps for the remaining MFA-related policies.

Tip

The [Block legacy authentication](/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-legacy) policy probably needs no exclusions, so you can use the previous steps to remove the existing exclusion. Just uncheck **Users and groups** in Step 4.

For more information about user exclusions in Conditional Access policies, see [User exclusions](/en-us/entra/identity/conditional-access/plan-conditional-access#user-exclusions).

### Step 4: Create new Conditional Access policies

Now you can create Conditional Access policies that meet your business needs. For more information, see [Plan a Conditional Access deployment](/en-us/entra/identity/conditional-access/plan-conditional-access).

### Revert to security defaults from Conditional Access policies

Security defaults are turned off when you're using Conditional Access policies. If one or more Conditional Access policies exist in any state (**Off**, **On**, or **Report only**), you can't turn on security defaults. You need to delete all existing Conditional Access policies before you can turn on security defaults.

Caution

Before you delete any Conditional Access policies, be sure to record their settings.

To delete Conditional Access policies, use the following steps:

1. On the [Conditional Access | Policies page](https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/%7E/Policies), select the policy that you want to delete.
2. In the details page that opens, select ![](../../media/m365-cc-sc-delete-icon.png)**Delete** at the top of the page.
3. In the **Are you sure?** dialog that opens, select **Yes**.

After you delete all Conditional Access policies, you can turn on security defaults as described in Manage security defaults.

## Manage legacy per-user MFA

We strongly recommend using security defaults or Conditional Access for MFA in Microsoft 365. If you can't, your last option is MFA for individual Microsoft Entra ID accounts via Microsoft Entra ID Free.

For instructions, see [Enable per-user Microsoft Entra multifactor authentication to secure sign-in events](/en-us/entra/identity/authentication/howto-mfa-userstates).