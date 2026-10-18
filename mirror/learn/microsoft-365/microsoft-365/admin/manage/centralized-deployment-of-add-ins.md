---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Requirements to use centralized deployment for Office Add-ins - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-of-add-ins?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2026-03-16T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- integrated-apps
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: b4527d49-4073-4b43-8274-31b7a3166f92
description: Verify your tenant and users meet requirements for centralized deployment of Office Add-ins. Check license, Exchange, and group compatibility to get started.
locale: en-us
document_id: 66ace7ce-d26f-68d0-2206-525acc513322
document_version_independent_id: 19e8d325-8074-2878-b864-cf0802e23cb0
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/centralized-deployment-of-add-ins.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/centralized-deployment-of-add-ins
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/centralized-deployment-of-add-ins.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 9aa31d6a-4eb2-22f4-015a-1554c5e4b61c
---

# Requirements to use centralized deployment for Office Add-ins - Microsoft 365 admin | Microsoft Learn

The [integrated apps portal](test-and-deploy-microsoft-365-apps) is the recommended and most feature-rich way for most customers to centrally deploy Office Add-ins to users and groups within your organization.

However, if the integrated apps portal isn't available to you, or if you're a customer in a sovereign or government cloud (GCC, GCC-H, DoD, AirGap, or Gallatin), use this article as guidance. Use it to determine whether your organization and users meet the requirements for centralized deployment.

Centralized deployment allows admins to deploy Office Add-ins to users and groups within an organization. It provides the following benefits:

- An admin can deploy and assign an add-in directly to a user, to multiple users via a group, or to everyone in the organization (see Admin requirement section for information).
- When the relevant Office application starts, the add-in automatically downloads. If the add-in supports add-in commands, the add-in automatically appears in the ribbon within the Microsoft 365 application.
- Add-ins no longer appear for users if:

    - The admin turns off or deletes the add-in.
    - The user is removed from Microsoft Entra ID or from a group that the add-in is assigned to.

Centralized deployment supports two platforms: Office on Windows and Mac. It also supports Office for the web. For Outlook Mobile Add-ins only, centralized deployment also supports iOS and Android.

Important

After you centrally deploy an add-in, it can take up to 24 hours for the add-in to appear on all users' clients.

## Before you begin

Centralized deployment of add-ins requires that the users have one of the following licenses:

- Microsoft 365 Business (Business Basic, Business Standard, Business Premium).
- Office 365 Enterprise (E1/E3/E5/F3).
- Microsoft 365 Enterprise (E3/E5/F3) (and are signed in Microsoft 365 using their organizational ID).
- Office 365 Education (A1/A3/A5).
- Microsoft 365 Education (A3/A5).
- Office 365 Government (G3/G5).
- Microsoft 365 Government (G3/G5).

Users must also have Exchange Online and active Exchange Online mailboxes. Your subscription directory must either be in or federated to Microsoft Entra ID.

The following are specific requirements for Microsoft 365 and Exchange, or use the Centralized Deployment Compatibility Checker.

Centralized deployment doesn't support the following items:

- Add-ins that target Office MSI versions, except Outlook.
- An on-premises directory service.
- Add-in deployment to an Exchange on-premises Mailbox.
- Add-in deployment to SharePoint.
- [Apps for Microsoft 365](apps-for-microsoft-365-overview) that include more than an add-in (For example, an app for Microsoft 365 that includes a Teams app).
- Deployment of Component Object Model (COM) or Visual Studio Tools for Office (VSTO) add-ins.
- Deployments of Microsoft 365 that don't include Exchange Online such as SKUs: Microsoft 365 Apps for Business and Microsoft 365 Apps for Enterprise.

### Microsoft 365 requirements

For Word, Excel, and PowerPoint add-ins, your users must use one of the following versions:

- On a Windows device, Version 1704 or later of Microsoft 365 Business licenses (Microsoft 365 Business Basic, Microsoft 365 Business Standard, Microsoft 365 Business Premium), Office 365 Enterprise licenses (E1/E3/E5/F3), or Microsoft 365 for enterprise licenses (E3/E5/F3).
- On a Mac, Version 15.34 or later.

For Outlook, your users must use one of the following versions:

| **Product/Platform** | **Minimum version required** | **Add-in in My add-ins** | **Add-in in Outlook ribbon** |
| --- | --- | --- | --- |
| Microsoft 365 Business licenses (Microsoft 365 Business Basic, Microsoft 365 Business Standard, Microsoft 365 Business Premium), Office 365 Enterprise licenses (E1/E3/E5/F3), or Microsoft 365 for enterprise licenses (E3/E5/F3) | Version 1701 or later | ✅ |  |
| Office Professional Plus 2019 or Office Standard 2019 | Version 1808 or later | ✅ |  |
| Office Professional Plus 2016 (MSI) or Office Standard 2016 (MSI)\* | Version 16.0.4494.1000 or later |  | ✅ |
| Office Professional Plus 2013 (MSI) or Office Standard 2013 (MSI)\* | Version 15.0.4937.1000 or later |  | ✅ |
| Office 2016 for Mac | Version 16.0.9318.1000 or later | ✅ |  |
| Outlook mobile for iOS | Version 2.75.0 or later | ✅ |  |
| Outlook mobile for Android | Version 2.2.145 or later | ✅ |  |

### Exchange Online requirements

Microsoft Exchange stores the add-in manifests within your organization's tenant. The admin deploying add-ins and the users receiving those add-ins must be on a version of Exchange Online that supports OAuth authentication.

To find out which configuration is in use, check with your organization's Exchange admin. You can verify OAuth connectivity per user by using the [Test-OAuthConnectivity](/en-us/powershell/module/exchangepowershell/test-oauthconnectivity) PowerShell cmdlet.

### Exchange Online user role requirements

Use the Exchange admin center (EAC) to assign permissions to users. The following steps detail the permissions required to view and modify deployed add-ins.

1. Sign in to the classic EAC with an account with appropriate permissions.
2. Go to **Permissions** and then select **User Roles**.
3. Select an existing role assignment policy or create a new policy.
4. Type a name for the policy if you're creating a new policy.
5. Select the following roles: **My Custom Apps**, **My MarketPlace Apps**, and **My ReadWriteMailbox Apps**.
6. Select **Save**.

Note

These roles are selected by default.

For more information, see [Manage role groups in Exchange Online](/en-us/exchange/permissions-exo/role-groups). For a detailed description of the different roles, see [Role assignment policies in Exchange Online](/en-us/exchange/permissions-exo/role-assignment-policies).

### Check the AppsForOfficeEnabled parameter

If you're deploying Office add-ins and none are showing up, then as a first troubleshooting step, use the `Get-OrganizationConfig | fl AppsForOfficeEnabled` PowerShell command. If the query returns a value of **False**, set this parameter to **True** using the `Set-OrganizationConfig -AppsForOfficeEnabled:$True` command. The add-ins should then appear as expected.

We don't recommend that the **AppsForOfficeEnabled** parameter be set to **False**. A value of **False** overrides all the Administrative and User role settings and prevent any new apps from being activated by any user in the organization.

### Admin requirements

To deploy an add-in through centralized deployment, you need to be an Exchange admin in the organization.

Note

An Exchange admin can deploy an add-in if they add the **Application Administrator** role or set the **App Registrations** property to true in Microsoft Entra admin center, as shown in the following image:

[![Screenshot of the App Registrations property set to true in the Microsoft Entra admin center.](../../media/144516704-8874a10d-b540-41f3-ae9d-c07a8d7e143f.png)](../../media/144516704-8874a10d-b540-41f3-ae9d-c07a8d7e143f.png#lightbox)

### Centralized Deployment Compatibility Checker

By using the Centralized Deployment Compatibility Checker, you can verify whether the users in your tenant are set up to use centralized deployment for Word, Excel, and PowerPoint. The Compatibility Checker isn't required for Outlook support. Download and install the [compatibility checker](https://aka.ms/officeaddindeploymentorgcompatibilitychecker).

Note

The Compatibility Checker currently isn't supported in any of the sovereign or government clouds (GCC, GCC-H, DoD, AirGap, Gallatin).

#### Run the compatibility checker

1. Start an elevated PowerShell.exe window.
2. Run the following command:

    ```powershell
    Import-Module O365CompatibilityChecker
    ```
3. Run the **Invoke-CompatibilityCheck** command:

    ```powershell
    Invoke-CompatibilityCheck
    ```

    This command prompts you for *TenantDomain* (for example, *TailspinToysIncorporated.onmicrosoft.com*) and *TenantAdmin* credentials, and then requests consent.

    Note

    Depending on the number of users in your tenant, the checker can complete in minutes or hours.

When the tool finishes running, it produces an output file in comma-separated (.csv) format. The tool saves the file to **the current working directory** by default. The output file contains the following information:

- User name.
- User ID (User's email address).
- Centralized Deployment ready - If the remaining items are true.
- Microsoft 365 plan - The plan of Office they're licensed for.
- Microsoft 365 Activated - If they activated Microsoft 365.
- Supported Mailbox - If they are on an OAuth-enabled mailbox.

If your Microsoft 365 reports show anonymous user names instead of actual user names, fix this issue by changing the reports setting in Microsoft 365 admin center. For detailed steps, see [Microsoft 365 reports show anonymous user names instead of actual user names](/en-us/office365/troubleshoot/miscellaneous/reports-show-anonymous-user-name).

Note

Multifactor authentication isn't supported when using the Central Deployment PowerShell module. The module only works with Basic authentication.

## User and group assignments

The centralized deployment feature currently supports most groups supported by Microsoft Entra ID, including:

- Microsoft 365 groups.
- Distribution lists.
- Dynamic groups.
- Security groups.

Note

The feature doesn't currently support non-mail-enabled security groups.

Centralized deployment supports assignments to individual users, groups, and everyone in the tenant. Centralized deployment supports users in top-level groups (groups without parent groups), but not users in nested groups (groups that have parent groups).

Take a look at the following example where Sandra, Sheila, and the Sales Department group are assigned to an add-in. Because the West Coast Sales Department is a nested group, Bert and Fred aren't assigned to an add-in.

[![Screenshot of a diagram showing nested group assignments where the West Coast Sales Department nested group isn't assigned to the add-in.](../../media/683094bb-1160-4cce-810d-26ef7264c592.png)](../../media/683094bb-1160-4cce-810d-26ef7264c592.png#lightbox)

### Find out if a group contains nested groups

The easiest way to detect if a group contains nested groups is to view the group contact card within Outlook. If you enter the group name within the **To** field of an email and then select the group name when it resolves, it shows you if it contains users or nested groups. In the following example, the **Members** tab of the Outlook contact card for the Test Group shows no users and only two sub groups.

[![Screenshot of the Members tab of the Outlook contact card showing two sub groups and no users.](../../media/d9db88c4-d752-426c-a480-b11a5b3adcd6.png)](../../media/d9db88c4-d752-426c-a480-b11a5b3adcd6.png#lightbox)

You can do the opposite query by resolving the group to see if it's a member of any group. In the following example, you can see under the **Membership** tab of the Outlook contact card that Sub Group 1 is a member of the Test Group.

[![Screenshot of the Membership tab of the Outlook contact card showing Sub Group 1 as a member of the Test Group.](../../media/a9f9b6ab-9c19-4822-9e3d-414ca068c42f.png)](../../media/a9f9b6ab-9c19-4822-9e3d-414ca068c42f.png#lightbox)

Alternately, you can use the Microsoft Graph API to run queries to find the list of groups within a group. For more information, see [Manage groups in Microsoft Graph](/en-us/graph/api/resources/groups-overview).

### Contact Microsoft for support

If you or your users encounter problems loading the add-in while using centrally deployed Microsoft 365 apps for the web (Word, Excel, etc.), [contact Microsoft support](../../business-video/get-help-support). Provide the following information about your Microsoft 365 environment in the support ticket.

| **Platform** | **Debug information** |
| --- | --- |
| Microsoft 365 | - Charles/Fiddler logs<br>- Tenant ID ([learn how](/en-us/onedrive/find-your-office-365-tenant-id))<br>- CorrelationID: View the source of one of the Office pages and look for the Correlation ID value and send it to support. For example:`<input name=" **wdCorrelationId**" type="hidden" value=" **{BC17079E-505F-3000-C177-26A8E27EB623}**">``<input name="user_id" type="hidden" value="1003bffd96933623"></form>` |
| Rich clients (Windows, Mac) | - Charles/Fiddler logs<br>- Build numbers of the client app (preferably as a screenshot from **File/Account**) |