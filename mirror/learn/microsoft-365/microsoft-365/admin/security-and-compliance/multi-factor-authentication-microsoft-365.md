---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Multifactor authentication for Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/multi-factor-authentication-microsoft-365?view=o365-worldwide
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
ms.date: 2026-06-16T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-security
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- admindeeplinkMAC
ROBOTS: NOINDEX, NOFOLLOW
description: Learn about the options for multi-factor authentication in Microsoft 365 (also known as MFA, two-factor authentication, or 2FA).
locale: en-us
document_id: 4f7ee91e-a312-e712-e8e3-60cfe433c8e2
document_version_independent_id: 4f7ee91e-a312-e712-e8e3-60cfe433c8e2
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/multi-factor-authentication-microsoft-365.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/multi-factor-authentication-microsoft-365
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/multi-factor-authentication-microsoft-365.md
platformId: a4bdaa0d-048d-120e-fe6d-6178f51783cf
---

# Multifactor authentication for Microsoft 365 - Microsoft 365 admin | Microsoft Learn

Passwords are the most common method of authenticating users, but they're also the most vulnerable. People often use weak, easy to guess passwords, and use the same credentials at different services.

To provide an extra level of security, multifactor authentication (also known as MFA, two-factor authentication, or 2FA) requires a second verification method for user sign-ins based on:

- Something a user has that isn't easily duplicated. For example, a smart phone.
- Something unique to the user. For example, a fingerprint or other biometric attributes.

The extra verification method is used only after the password is verified. Even if a strong user password is compromised, the attacker doesn't have the user's smart phone or fingerprints to complete the sign-in.

The available methods to enable MFA in Microsoft 365 organizations, including Microsoft 365 for business organizations, are described in the following sections.

For configuration instructions, see [Set up MFA for Microsoft 365](set-up-multi-factor-authentication).

## Security defaults

Security defaults is a set of unmodifiable policies in all Microsoft 365 organizations via Microsoft Entra ID Free.

Security defaults include the following security features:

- Require all users and admins to register for Microsoft Entra multifactor authentication (MFA) using the [Microsoft Authenticator app](/en-us/entra/identity/authentication/concept-authentication-authenticator-app) or any non-Microsoft authentication app that supports [OATH TOTP](/en-us/entra/identity/authentication/concept-authentication-oath-tokens#oath-software-tokens).
- Require MFA for administrator accounts at every sign in.
- Require MFA for users when necessary (for example, on new devices).
- Block legacy authentication protocols (for example, POP3 and IMAP4 in old email clients).
- Require MFA for users and admins accessing Azure Resource Manager services (for example, the Microsoft Azure portal).

Security defaults is either on or off in an organization. Microsoft 365 organizations created after October 2019 have security defaults (hence, MFA) turned on by default, **so you don't need to do anything to enable security defaults or MFA in a new organization**. For many organizations, security defaults offer a good, baseline level of sign-in security.

For more information about security defaults and the policies enforced, see [Enforced security policies in security defaults](/en-us/entra/fundamentals/security-defaults#enforced-security-policies).

To configure security defaults, see [Manage security defaults](set-up-multi-factor-authentication#manage-security-defaults).

## Conditional Access policies

As an alternative to using security defaults, Conditional Access policies are available for organizations who have Microsoft Entra ID P1 or P2. Examples include:

- Microsoft 365 Business Premium (Microsoft Entra ID P1)
- Microsoft 365 E3 (Microsoft Entra ID P1)
- Microsoft 365 E5 (Microsoft Entra ID P2)
- An add-on subscription

Tip

Organizations with Microsoft Entra ID P2 also have access to Microsoft Entra ID Protection. You can create a Conditional Access policy to [require multifactor authentication for elevated sign-in risk](/en-us/entra/identity/conditional-access/policy-risk-based-sign-in). For more information, see [What is Microsoft Entra ID Protection?](/en-us/entra/id-protection/overview-identity-protection).

You create Conditional Access policies that react to sign-in events before a user is granted access to an application or service. If your organization has complex security requirements or you need granular control over security policies, you can use Conditional Access policies instead of security defaults.

Important

Organizations can use security defaults or Conditional Access policies, but not both at the same time. Conditional Access policies require security defaults to be turned off, so it's important to recreate the policies from security defaults in Conditional Access policies as a baseline for all users.

For more information about Conditional Access policies, see [What is Conditional Access?](/en-us/entra/identity/conditional-access/overview).

To configure Conditional Access policies, see [Manage Conditional Access policies](set-up-multi-factor-authentication#manage-conditional-access-policies).

## Legacy per-user MFA (not recommended)

If you can't use security defaults or Conditional Access for business reasons, your last option is using legacy MFA for individual Microsoft Entra ID accounts. This option is available with the Microsoft Entra ID Free plan. We strongly recommend MFA for accounts with administrator roles, especially the Global Administrator role.

For configuration instructions, see [Enable per-user Microsoft Entra multifactor authentication to secure sign-in events](/en-us/entra/identity/authentication/howto-mfa-userstates).

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Comparing MFA methods

The following table shows the results of enabling MFA with security defaults, Conditional Access policies, or per-user account settings.

| Method | Method enabled | Method disabled | Available authentication methods |
| --- | --- | --- | --- |
| **Security defaults** | If security defaults is turned on, you can create new Conditional Access policies, but you can't turn them on. | After you turn off security defaults, you can turn on Conditional Access policies. | [Microsoft Authenticator app](/en-us/entra/identity/authentication/concept-authentication-authenticator-app) or any non-Microsoft authentication app that supports [OATH TOTP](/en-us/entra/identity/authentication/concept-authentication-oath-tokens#oath-software-tokens). |
| **Conditional Access policies** | If one or more Conditional Access policies exist in any state (**Off**, **On**, or **Report only**), you can't turn on security defaults. | If there are no Conditional Access policies, you can enable security defaults. | [Microsoft Authenticator app](/en-us/entra/identity/authentication/concept-authentication-authenticator-app) or any non-Microsoft authentication app that supports [OATH TOTP](/en-us/entra/identity/authentication/concept-authentication-oath-tokens#oath-software-tokens). Other authentication methods might also be available, depending on the configured [authentication strength](/en-us/compliance/anz/e8-mfa-configure-authentication-strengths). |
| **Legacy per-user MFA (not recommended)** | Overrides security defaults and Conditional Access policies requiring MFA at each sign-in. | Overridden by security defaults or Conditional Access policies | User-specified during MFA registration |