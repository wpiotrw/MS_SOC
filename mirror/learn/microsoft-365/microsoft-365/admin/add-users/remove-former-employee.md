---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Remove a former employee - Overview - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-06-15T00:00:00.0000000Z
audience: Admin
ms.topic: solution-overview
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
- SPO_Content
- m365solution-overview
ms.custom:
- has-azure-ad-ps-ref
- azure-ad-ref-level-one-done
- adminvideo
- MSStore_Link
- TRN_M365B
- OKR_SMB_Videos
- AdminSurgePortfolio
- AdminTemplateSet
- m365solution-removeemployee
- business_assist
- user-accounts
description: Block access to Microsoft 365 so a former employee can't sign in, secure organization data, and allow other employees to access their email and OneDrive data.
locale: en-us
document_id: 4e366b9c-0d35-83c6-f509-1774dd351504
document_version_independent_id: 702f2dc1-46f8-508a-68bc-b5d033c56a9a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 398cb6c7-59e3-bc4b-5878-0303434a56a3
---

# Remove a former employee - Overview - Microsoft 365 admin | Microsoft Learn

If an employee leaves your organization, you might be wondering what you should do to secure data and prevent unauthorized access. This article series explains how to block access to Microsoft 365 so former employees can't sign in to your organization's Microsoft 365 subscription, the steps you should take to secure your organization's data, and how to allow other employees to access a former employee's email and OneDrive content.

## Before you begin

To complete the steps in this series, you use these Microsoft 365 capabilities and features.

| Product or component | Capability or feature |
| --- | --- |
| Microsoft 365 admin center | Convert mailbox, forward email, revoke access, or remove user |
| Exchange admin center | Block user, block access to email, or wipe device |
| OneDrive and SharePoint | Give access to other users |
| Outlook | Import pst files, add mailbox |
| Active Directory | Remove users in hybrid environments |
| Purview eDiscovery | Apply legal holds to departing employees to retain their data for legal or compliance purposes |

## Solution: Remove a former employee

![Screenshot: Steps for removing a former employee from your organization.](../../media/delete-user-account.png)

| Step | Why do this step |
| --- | --- |
| [Step 1: Prevent a former employee from signing in to your organization's Microsoft 365 services](remove-former-employee-step-1) | Prevent former employees from accessing your Microsoft 365 services and organization's data. |
| [Step 2: Save the contents of a former employee's mailbox](remove-former-employee-step-2) | If someone is taking over the former employee's work, it's helpful for them to access this information. Or, if there's a legal requirement or important need to save the former employee's data, you want to complete this step. |
| [Step 3: Wipe and block a former employee's mobile device](remove-former-employee-step-3) | Removes your organization's data from the former employee's phone or tablet. |
| [Step 4: Forward a former employee's email to another employee or convert to a shared mailbox](remove-former-employee-step-4) | You can keep the former employee's email address active in case you have customers or partners sending email to the former employee's address. Setting up email forwarding makes sure messages get to the next person taking over the work. |
| [Step 5: Give another employee access to OneDrive and Outlook data](remove-former-employee-step-5) | If you only remove a user's license but don't delete the account, the content in the user's OneDrive remains accessible to you even after 30 days.  Before you delete the account, consider granting access of the former employee's OneDrive and Outlook content to another user. After you delete an employee's account, the content in their OneDrive and Outlook is retained for **30** days. During that 30 days, you can restore the user's account, and gain access to their content. If you restore a user's account, their OneDrive and Outlook content remains accessible to you, even after 30 days. |
| [Step 6 - Remove and delete the Microsoft 365 license from a former employee](remove-former-employee-step-6) | When you remove a license, you can assign it to someone else. Or, you can delete the license if you don't need it.  When you remove or delete a license, the former employee's email, contacts, and calendar are retained for **30 days**, and are then deleted permanently. If you remove or delete a license but don't delete the account, the content in the user's OneDrive remains accessible to you even after 30 days. |
| [Step 7 - Delete a former employee's user account](remove-former-employee-step-7) | Deleting a former employee's account stops email messages sent to that account from being received. |

## Watch: Delete a user overview

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198203).

## Does your organization use Active Directory?

If your organization synchronizes user accounts to Microsoft 365 from a local Active Directory environment, you must delete and restore those user accounts in your local Active Directory service. You can't delete or restore them in Microsoft 365.

To delete and restore a user account in Active Directory (on premises), see [Delete a User Account](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753730%28v=ws.11%29).

If you're using Microsoft Entra ID, see the [Remove-MgUser](/en-us/powershell/module/microsoft.graph.users/remove-mguser) PowerShell cmdlet.