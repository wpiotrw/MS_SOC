---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Admin account security in Microsoft 365 for business - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-security
ms.date: 2026-01-06T00:00:00.0000000Z
ms.localizationpriority: medium
ms.collection:
- M365-Campaigns
- m365solution-smb
- highpri
- tier2
- trust-pod
ms.custom:
- MiniMaven
- security
search.appverid:
- BCS160
- MET150
description: Learn how to set up and protect your administrator accounts in Microsoft 365 Business Basic, Microsoft 365 Business Standard, and Microsoft 365 Business Premium.
locale: en-us
document_id: fca68d2b-5ba9-91af-e4f5-a2ffd47ae3b1
document_version_independent_id: fca68d2b-5ba9-91af-e4f5-a2ffd47ae3b1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-account-security-admins.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-account-security-admins
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-account-security-admins.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: c67be9b3-8ecf-9285-9cdf-5ef148ef8208
---

# Admin account security in Microsoft 365 for business - Microsoft 365 admin | Microsoft Learn

Although multifactor authentication (MFA) is [turned on by default for all accounts in Microsoft 365 for business organizations](multi-factor-authentication-microsoft-365#security-defaults), administrator or admin accounts require extra security considerations unrelated to MFA. Admin accounts have elevated privileges and are valuable targets for attackers. At the same time, admin accounts are fundamental to the operation and management of your organization.

The account you used to enroll in Microsoft 365 for business is automatically a Global Administrator (also known as a *global admin*). Global admins have ultimate control over user accounts and all the other settings in the Microsoft admin center (https://admin.microsoft.com). But there are many different kinds of admin capabilities with varying levels of access. For more information, see [About admin roles in the Microsoft 365 admin center](../add-users/about-admin-roles).

Use the following guidance to make the most of admin accounts while protecting your organization from attackers:

- **Be sure to have more than one admin account**: We recommend at least two admin [emergency access accounts](/en-us/entra/identity/role-based-access-control/security-emergency-access) in every organization that aren't assigned to specific individuals and are only used in emergencies. These accounts also need to be [excluded from MFA requirements](set-up-multi-factor-authentication#step-3-adjust-mfa-exclusions) and therefore should have long, complex passwords (16 or more characters). These accounts are also known as "break glass accounts."

    For admin account creation instructions, see [Add an administrator](../add-users/assign-admin-roles#add-an-administrator).

    Important

    Limit the number of admin accounts your organization. Too many admin accounts provide attackers with more opportunities to compromise your organization.

    Use the concept *least privilege*, which means you give users only the permissions required to do their jobs. For example, if a user needs to create user accounts, don't add them to the Global Administrator role; add them to the User Administrator role instead. For more information, see the following articles:

    - [Enhance security with the principle of least privilege](/en-us/entra/identity-platform/secure-least-privileged-access)
    - [About admin roles in the Microsoft 365 admin center](../add-users/about-admin-roles)
- **Use ordinary user accounts for regular work tasks**: Admins should use non-admin accounts as primary accounts to sign in to their computers and do regular tasks like checking email and using Microsoft 365 Apps. Use your admin account only as needed.

    - Before using admin accounts, close all unrelated browser sessions and apps, including personal email accounts. You can also use InPrivate, Incognito, or Private browsing mode for admin tasks.
    - After completing admin tasks, be sure to sign out of the browser session.

    For account creation instructions, see [Add users and assign licenses at the same time](../add-users/add-users).

    Tip

    Ordinary user accounts need Microsoft 365 for business licenses, but you don't need to license admin only accounts.

    Use a naming convention that doesn't advertise the fact that an account has admin privileges. For example, your regular user account is `alice.chavez@contoso.onmicrosoft.com`, and your admin account is `alicec@contoso.onmicrosoft.com`.
- **Use passwordless authentication for admin accounts**: For more information, see [Enable passwordless sign-in with Authenticator](/en-us/entra/identity/authentication/howto-authentication-passwordless-phone).

    - Microsoft 365 Business Basic and Microsoft 365 Business Standard organizations support the following passwordless authentication options via Microsoft Entra ID Free:
        - The [Microsoft Authenticator](/en-us/entra/identity/authentication/concept-authentication-passwordless#microsoft-authenticator) app with push notifications and biometric or PIN verification.
        - [Passkeys (FIDO2)](/en-us/entra/identity/authentication/concept-authentication-passwordless#passkeys-fido2)
        - [Windows Hello for Business](/en-us/entra/identity/authentication/concept-authentication-passwordless#windows-hello-for-business)
    - Microsoft 365 Business Premium via Microsoft Entra ID P1 also allows you to *require* passwordless authentication and authentication strength for admin accounts using Conditional Access. For more information, see [Conditional Access authentication strength](/en-us/entra/identity/authentication/concept-authentication-strengths).