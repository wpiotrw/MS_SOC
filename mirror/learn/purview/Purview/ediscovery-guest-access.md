---
layout: Conceptual
title: Guest access in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-guest-access
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about guest access in eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: swethaiyer
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: b10e799a-b8bd-c6c9-7acc-1b0767f751b5
document_version_independent_id: b10e799a-b8bd-c6c9-7acc-1b0767f751b5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-guest-access.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-guest-access
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-guest-access.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: c6443440-04e5-ae68-5a41-bde258a14ec7
---

# Guest access in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

With guest access, you can provide access to an eDiscovery Premium case to people outside your organization. You can invite guests users to eDiscovery (Premium) cases just like you can invite guests into your Teams environment.

A guest is someone who doesn't have a work or school account with your organization. For example, guests may include external partners, vendors, suppliers, or consultants. Anyone who isn't part of your organization can be added as guest for an eDiscovery (Premium) case. This access means that anyone with a Microsoft Entra account or personal email account (Outlook, Gmail, or others) can participate as a guest in eDiscovery and have access to specific eDiscovery (Premium) cases.

Guest access in eDiscovery uses [Azure B2B technology](/en-us/azure/active-directory/external-identities/what-is-b2b), which depends on an organization-wide Azure collaboration setting. When you invite a guest to eDiscovery, a guest account is created for them in Microsoft Entra ID. They're covered by the same compliance and auditing protection as other Microsoft 365 users. Guest access is subject to Microsoft Entra ID and Microsoft 365 service limits.

Note

eDiscovery guests are currently limited to *Reviewer* role group permission only. For more information about the reviewer role, see [Assign eDiscovery permissions in the Microsoft Purview portal](ediscovery-assign-permissions#rbac-roles-related-to-ediscovery).

## Set up guest access

Setting up guest access in eDiscovery requires configuring other settings in Microsoft Entra ID. To enable access to invite guests to eDiscovery cases, complete the following steps:

1. Check the [B2B external collaboration settings](/en-us/microsoft-365/solutions/collaborate-as-team#azure-external-collaboration-settings) to ensure that collaboration with guests isn't blocked. If the **Guest invite settings** is set to *No one in the organization can invite guest users including admins* then inviting guest into eDiscovery won't work. Contact your system administrator to ensure [this setting is properly configured](/en-us/azure/active-directory/external-identities/external-collaboration-settings-configure). You can view and update the collaboration setting using the *Authorization Policy*[API](/en-us/graph/api/resources/authorizationpolicy).
2. Depending on the specific configuration in Step 1, eDiscovery administrators may or may not need additional roles to approval a guest access request submitted from the eDiscovery user.

    - If the *Anyone in the organization can invite guest users including guests and non-admins (most inclusive)* or *Member users and users assigned to specific admin roles can invite guest users including guests with member permission* options are selected, then eDiscovery administrators can approve invitation requests without additional roles.
    - If *Only users assigned to specific admin roles can invite guest users* is selected, then the eDiscovery administrator who would approve the invitation request requires the *Invite guest* role to approve and trigger the invitation email to the guest. See the [Assign Microsoft Entra roles to users](/en-us/azure/active-directory/roles/manage-roles-portal) article for guidance on how to add the *Guest Inviter* role to users. If you prefer to use PowerShell to add this role, see [Assign the Guest Inviter role to a user](/en-us/azure/active-directory/external-identities/external-collaboration-settings-configure#assign-the-guest-inviter-role-to-a-user).
3. To enable collaboration with guest reviewers from other Microsoft 365 cloud environments, including if you're a Microsoft Azure Government organization, both your organization and the guest user’s organization must enable specific connection settings. For detailed configuration guidance, see [Collaborate with guests from other Microsoft 365 cloud environments](/en-us/microsoft-365/solutions/collaborate-guests-cross-cloud).

## Enable guest access in eDiscovery (Premium)

eDiscovery admins must enable guest access in eDiscovery (Premium) before they can invite users as guests.

To enable guest access for guests in eDiscovery (Premium), complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), navigate to **eDiscovery** &gt; **Premium** &gt; **eDiscovery (Premium) settings** &gt; **Guest users**.
2. Toggle **Guest access** to *On*.

Now eDiscovery managers and admins can initiate the guest invitation process within any eDiscovery (Premium) case.

## Invite guests to an eDiscovery (Premium) case

To invite guests to an eDiscovery (Premium) case, complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), navigate to **eDiscovery** &gt; **Premium** &gt; **eDiscovery (Premium) cases** and select the case you want to invite guests to.
2. In the selected case, select the **Settings** tab and then select **Access & permissions**.
3. In the **Guest users** section, select **Add**.
4. On the **Invite guest** flyout pane, complete the following fields:

    - **Full name**: Enter the full name of the guest you want to invite.
    - **Email address**: Enter the email address of the guest you want to invite.
    - **Organization**: Enter the organization of the guest you want to invite.
    - **Guest role**: Select the role you want to assign to the guest. The guest is currently limited to *Reviewer* role group permission only.
    - **Justification**: Explain why this person needs access to the case.
5. Select **Invite** to submit the invitation request for review and approval by an eDiscovery admin.

## Approve guest access requests

After guest invitations are submitted, eDiscovery admins must approve the requests before the guest can access the case. eDiscovery admins must have the *Role Management* role assigned to approve guest access requests.

To approve guest access requests, eDiscovery managers must complete the following steps:

1. eDiscovery managers are notified of pending invitation requests on the **Overview** tab in eDiscovery (Premium).
2. To review and approve or deny the request, navigate to **eDiscovery** &gt; **Premium** &gt; **eDsicovery (Premium) settings** &gt; **Guest users**. Select the guest request and select **Create account** or **Deny**.
3. If the guest is being added to the tenant for the first time, eDiscovery admins need to perform a two-step approval process. They first need to approve creation of an account, which may take up to 24 hours. After 24 hours, eDiscovery admins can approve guest access to the case. For future access requests for access to other cases for the same guest, only one-step approval is required.

In you encounter an error when approving the guest access to a case, check the following:

- The guest's email isn't disabled, blocked or deleted by the tenant admin.
- If there are any members in the *Reviewer* role group whose Microsoft Entra account has been deleted. Currently, an error occurs when adding a new member to a role group that has any deleted users. If the *Reviewer* role group has any deleted users, [remove them from the role group](purview-permissions#remove-users-or-groups-from-a-microsoft-purview-built-in-role-group) and retry the guest approval.

## Accepting guest invitations

After the request is approved by the eDiscovery admin, the guest receives a welcome email from *Microsoft Invitations*. This email contains information about the eDiscovery invitation and a link where the guest can accept the invite and sign in. The guest must select the unique link provided in the email or copy/paste the link in a browser to log into the specific eDiscovery organization.

![Email invitation for guest access to an eDiscovery (Premium case).](media/ediscovery-guest-user-invite-email.png)

Guests that have a work or school account in Microsoft Entra ID can accept the invitation and authenticate immediately. Other users are sent a one-time passcode to validate their identity. You must ensure that the [one-time passcode setting](/en-us/azure/active-directory/external-identities/one-time-passcode) is enabled in your organization.

Note

If the guest is logged into another eDiscovery organization in their browser, they need to sign out from the organization and clear their browser cache before selecting the link in the invitation email.

After accepting the invitation and authenticating, the guest can participate in the eDiscovery case like an internal reviewer of the case and perform review activities such as querying, filtering, tagging, redaction, downloading single items for review, and more.

## Removing guest access

An eDiscovery admin can remove a guest’s access to a case from eDiscovery Premium settings page. To remove guest access for a user, eDiscovery admins must complete the following steps:

1. To review and approve or deny the request, navigate to **eDiscovery** &gt; **Premium** &gt; **eDsicovery (Premium) settings** &gt; **Guest users**.
2. Select the guest and select **Remove** from the flyout pane.

The guest continues to have access to other cases that they have been added to. When a guest is removed from the last case they have access to, they're removed from the *Reviewer* role group and won't have access to any cases in eDiscovery (Premium).

The guest continues to have a Microsoft Entra guest account in the organization. A regular review and clean-up of guest accounts from Microsoft Entra ID is recommended.