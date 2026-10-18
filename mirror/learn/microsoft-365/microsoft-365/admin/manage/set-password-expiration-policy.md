---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set the password expiration policy for your organization - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/set-password-expiration-policy?view=o365-worldwide
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
ms.date: 2026-03-13T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: high
ms.collection:
- Tier1
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- must-keep
- operations-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- admindeeplinkMAC
- business_assist
- has-azure-ad-ps-ref
- azure-ad-ref-level-one-done
- user-accounts
description: Learn how to set a password expiration policy for your organization in the Microsoft 365 admin center. Configure passwords to expire or never expire and improve security.
locale: en-us
document_id: d322ca91-2125-7486-887f-7c313f2fbcf9
document_version_independent_id: a139620d-3330-a687-709a-35bb270101e4
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/set-password-expiration-policy.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/set-password-expiration-policy
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/set-password-expiration-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 74bf0ca7-58d9-ec07-709e-617de3539c57
---

# Set the password expiration policy for your organization - Microsoft 365 admin | Microsoft Learn

This article is for people who set password expiration policies for organizations, such as a business, school, or nonprofit organization, using Microsoft 365 for business.

As a user administrator, you can make user passwords expire after a certain number of days, or set passwords to never expire. **By default, passwords never expire for your organization**.

To avoid security risks associated with users setting weak passwords or reusing old passwords, enable [multifactor authentication](../security-and-compliance/set-up-multi-factor-authentication). See [Password policy recommendations](../misc/password-policy-recommendations).

## Before you begin

You must be a [user administrator](../add-users/about-admin-roles) to perform these steps.

## Set password expiration policy

To set user passwords to expire after a set amount of time, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org Settings**](https://go.microsoft.com/fwlink/p/?linkid=2053743).

    If you don't have an appropriate role assigned, you won't see the **Org Settings** option. In this case, [Check administrator roles in your organization](../add-users/assign-admin-roles#check-administrator-roles-in-your-organization).
4. In the **Org Settings** page, select the [**Security and Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) tab.
5. In the **Security and Privacy** tab, select **Password expiration policy**.
6. In the **Password expiration policy** pane, clear the check box **Set passwords to never expire (recommended)**.
7. In the **Days before passwords expire** text box, enter how often passwords should expire. Choose a number of days from **14 to 730**, and then select **Save**.

Important

The Microsoft 365 admin center and Microsoft 365 productivity apps no longer support password expiration notifications.

## Important things you need to know about the password expiration feature

People who only use the Outlook app aren't forced to reset their Microsoft 365 password until it expires in the cache. This process can take days after the actual expiration date. There's no workaround for this configuration at the admin level.

## Prevent last password from being used again

To prevent users from recycling old passwords, enforce password history in Active Directory (AD). For more information, see [Create a custom password policy](/en-us/azure/active-directory-domain-services/password-policy#create-a-custom-password-policy).

In Microsoft Entra ID, users can't reuse their last password when they change a password. This password policy applies to all user accounts that you create and manage directly in Entra ID, and it can't be modified. For more information, see [Microsoft Entra password policies](/en-us/azure/active-directory/authentication/concept-sspr-policy#password-policies-that-only-apply-to-cloud-user-accounts).

## New and federated domains

Set password policies for each managed domain in your organization. If you add a new domain or convert a domain from *federated* to *managed*, re-enable the organization password policy to update all domains. Otherwise, the new or converted domain keeps the default policy.

## Synchronize user password hashes from on-premises Active Directory to Microsoft Entra ID

This article explains how to set the expiration policy for cloud-only users (Microsoft Entra ID). It doesn't apply to hybrid identity users who use password hash sync, pass-through authentication, or on-premises federation like Active Directory Federation Services (ADFS).

To learn how to synchronize user password hashes from an on-premises Active Directory to Microsoft Entra ID, see [Implement password hash synchronization with Microsoft Entra Connect Sync](/en-us/azure/active-directory/hybrid/how-to-connect-password-hash-synchronization).

## Password policies and account restrictions in Microsoft Entra ID

You can set more password policies and restrictions in Microsoft Entra ID. For more information, see [Password policies and account restrictions in Microsoft Entra ID](/en-us/azure/active-directory/authentication/concept-sspr-policy).

## Update password policy using PowerShell

The `Update-MgDomain` cmdlet updates the password policy of a specified domain or tenant and indicates the length of time that a password remains valid before it must be changed.

To learn how to update password policy for a specific domain or tenant, see [Update-MgDomain](/en-us/powershell/module/microsoft.graph.identity.directorymanagement/update-mgdomain).