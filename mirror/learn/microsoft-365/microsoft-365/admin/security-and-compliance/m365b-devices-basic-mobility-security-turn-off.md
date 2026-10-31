---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Turn off Basic Mobility and Security enforcement - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-turn-off?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords: NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: security
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- AdminSurgePortfolio
- basic-mobility-security
- security
description: Learn how to effectively disable Basic Mobility and Security.
locale: en-us
document_id: e0654f64-9050-19e2-4bf6-c4ead19619ba
document_version_independent_id: e0654f64-9050-19e2-4bf6-c4ead19619ba
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-turn-off.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-turn-off
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-turn-off.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 15fd5e6b-94ab-625e-b849-f6d111cf61fa
---

# Turn off Basic Mobility and Security enforcement - Microsoft 365 admin | Microsoft Learn

You can't completely turn off or disable Basic Mobility and Security in your organization after you [enable](m365b-devices-basic-mobility-security-set-up) and [configure](m365b-devices-basic-mobility-security-policies-configure#create-policies-in-basic-mobility-and-security) it. But you can remove the enforcement of Basic Mobility and Security on devices in your organization by using either of the following methods:

- **Remove security group assignments from all Basic Mobility and Security policies**: This method works up to a certain point, because a policy must be assigned to at least one security group. You have the following options:
    - Create a new security group with no members and assign all policies to that group. For security group creation instructions, see [Create, edit, or delete a security group](../email/create-edit-or-delete-a-security-group).
    - Assign the policy to no one (select **We'll save this policy, but it won't be applied to any devices in your organization**).
- **Remove all Basic Mobility and Security policies**: This option works up to a certain point, because you can't remove the last remaining policy in the organization. You have the following options:
    - Create a new security group with no members and assign the last remaining policy to that group. For security group creation instructions, see [Create, edit, or delete a security group](../email/create-edit-or-delete-a-security-group).
    - Assign the last remaining policy to no one (select **We'll save this policy, but it won't be applied to any devices in your organization**).
    - Create a new policy with no restrictions assigned to no one or an empty security group, and then remove all other policies.

The rest of this article describes how to use these methods to effectively disable Basic Mobility and Security enforcement in an organization.

For more information about Basic Mobility and Security, see [Overview of Basic Mobility and Security in Microsoft 365 for business](m365b-devices-basic-mobility-security-overview).

Important

Be aware of the effect on user devices when you turn off Basic Mobility and Security enforcement. For example, email profiles and cached email might be removed. For more information, see [What happens when you delete a policy or remove a user from a policy?](m365b-devices-basic-mobility-security-policies-configure#what-happens-when-you-delete-a-policy-or-remove-a-user-from-a-policy).

## What do you need to know before you begin?

- You open the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity.
- You need to be assigned permissions before you can do the procedures in this article. You have the following options:

    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**^\*^ or **Compliance Administrator** roles gives users the required permissions *and* permissions for other features in Microsoft 365.

        Important

        ^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).
- Questions? See the [Basic Mobility and Security FAQ](m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Remove security group assignments from all Basic Mobility and Security policies

1. On the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity, select the **Policies** tab.
2. On the **Policies** tab, select a policy by clicking anywhere in the row other than the check box next to the name to open the details flyout for the policy.
3. In the details flyout, select **Edit deployment** in the **Deployment** section.
4. In the **Edit deployment** flyout that opens, make one of the following selections:

    - Remove any existing groups below the **Include these groups** box, start typing the name of the designated security group with no members in the box, and then select it when it appears.
    - Select **We'll save this policy, but it won't be applied to any devices in your organization**

    When you're finished on the **Edit deployment** flyout, select **Save**.
5. Back on the details flyout, select **Close**.

Repeat these steps as many times as necessary.

## Remove all Basic Mobility and Security policies

1. On the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity, select the **Policies** tab.
2. On the **Policies** tab, select the policy to remove by selecting the check box next to the name.
3. Select ![](../../media/m365-cc-sc-more-actions-icon.png)**More actions** &gt; **Delete selected policies**.
4. Select **Yes** in the warning dialog that opens.
5. Repeat the previous steps until only one policy remains, then do one of the following steps:

    - Create a new policy with no restrictions assigned to no one or an empty security group. After you create this policy, remove the last remaining "real" policy. For policy creation instructions, see [Create policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure#create-policies-in-basic-mobility-and-security).
    - Assign the last remaining policy to no one or an empty security group as described in the Remove security group assignments from all Basic Mobility and Security device policies section.