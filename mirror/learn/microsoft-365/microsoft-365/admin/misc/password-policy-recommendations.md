---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Password policy recommendations - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-04-08T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: security
ms.localizationpriority: high
ms.collection:
- Tier1
- ContentEngagementFY23
- scotvorg
- highpri
- Adm_O365
- Adm_NonTOC
- must-keep
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- user-accounts
description: Make your organization more secure against password attacks, and ban common passwords and enable risk-based multifactor authentication.
locale: en-us
document_id: 523758d0-17ea-7061-d9ce-8f5a31a76b4c
document_version_independent_id: 545fd950-8ef0-837b-8839-8aa21da0c6eb
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/misc/password-policy-recommendations.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/misc/password-policy-recommendations
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/misc/password-policy-recommendations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8e8ddda8-f708-d492-3835-b448b5062f3d
---

# Password policy recommendations - Microsoft 365 admin | Microsoft Learn

As a Microsoft 365 administrator, you're responsible for setting the password policy for users in your organization. Setting the password policy can be complicated and confusing, and this article provides recommendations to make your organization more secure against password attacks.

Microsoft cloud-only accounts have a predefined password policy that can't be changed. The only items you can change are the number of days until a password expires and whether or not passwords expire at all.

Microsoft's latest guidance discourages password expiration policies for cloud-only accounts. The recommended setting is for passwords to never expire.

For more information on using Entra ID for help with passwords, see [Eliminate bad passwords using Microsoft Entra Password Protection.](/en-us/entra/identity/authentication/concept-password-ban-bad)

## Understanding password recommendations

Good password practices fall into a few broad categories:

- **Resisting common attacks**: This practice involves choosing where users enter passwords (known and trusted devices with good malware detection, validated sites), and the what passwords to use (length and uniqueness).
- **Containing successful attacks**: Containing successful hacker attacks is about limiting exposure to a specific service, or preventing that damage altogether, if a user's password gets stolen. For example, ensuring that a breach of your social networking credentials doesn't make your bank account vulnerable, or not letting a poorly guarded account accept reset links for an important account.
- **Understanding human nature**: Many valid password practices fail in the face of natural human behaviors. Understanding human nature is critical because research shows that almost every rule you impose on your users results in a weakening of password quality. Length requirements, special character requirements, and password change requirements all result in normalization of passwords, which makes it easier for attackers to guess or crack passwords.

## Password guidelines for administrators

The primary goal of a more secure password system is password diversity. You want your password policy to contain lots of different and hard-to-guess passwords. Here are a few recommendations for keeping your organization as secure as possible.

- Maintain a 14-character minimum length requirement. (Even though Microsoft 365 requires at least eight characters, for stronger security, we recommend a minimum of 14 characters.)
- Don't use easy-to-guess passwords like `abcdefg` or `password`
- Educate users to not reuse their organization passwords for nonwork purposes
- Enforce registration for [multifactor authentication](../security-and-compliance/set-up-multi-factor-authentication)
- Enable identity protection risk policies
- Configure password resets paired with an authentication app.

## Password guidance for users

Here's some password guidance for users in your organization. Make sure to let your users know about these recommendations and enforce the recommended password policies at the organizational level.

- Don't use a password that is the same or similar to one you use on any other websites
- Don't use a single word, for example, `password`, or a commonly used phrase like `Iloveyou`
- Set passwords that are hard to guess, even by people who know a lot about you. Examples include using names and birthdays of your friends and family, your favorite bands, and phrases you like to use

### Ban easy-to-guess passwords

The most important password requirement you should put on your users when creating passwords is to ban the use of easy-to-guess passwords that make your organization vulnerable to brute-force password attacks. Examples include:

- `abcdefg`
- `password`
- `monkey`
- `123456`

### Educate users to not reuse organization passwords anywhere else

One of the most important messages to get across to users in your organization is to not reuse their organization password anywhere else. The use of organization passwords in external websites greatly increases the likelihood that cybercriminals can compromise these passwords.

### Enforce multifactor authentication registration

Make sure your users update contact and security information, like an alternate email address, phone number, or a device registered for push notifications, so they can respond to security challenges and be notified of security events. Updated contact and security information helps users verify their identity if they ever forget their password, or if someone else tries to take over their account. It also provides an out of band notification channel for security events such as sign-in attempts or changed passwords.

To learn more, see [Set up multifactor authentication](../security-and-compliance/set-up-multi-factor-authentication).

### Enable risk based multifactor authentication

Risk-based multifactor authentication ensures that when our system detects suspicious activity, it can challenge the user to ensure that they're the legitimate account owner.