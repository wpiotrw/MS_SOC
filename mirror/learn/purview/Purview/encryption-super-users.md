---
layout: Conceptual
title: Configure super users for Azure Rights Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/encryption-super-users
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-09-01T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Configure the super user feature of the Azure Rights Management service from Microsoft Purview Information Protection, so that authorized people and services can always read and inspect ("reason over") your organization's encrypted data.
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: d022b605-7148-2604-5374-fffe41b27fe5
document_version_independent_id: d022b605-7148-2604-5374-fffe41b27fe5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/encryption-super-users.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: encryption-super-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/encryption-super-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9abf1764-80c6-55f6-d3ca-ebc7561768e4
---

# Configure super users for Azure Rights Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The super user feature of the Azure Rights Management service from Microsoft Purview Information Protection ensures that authorized people and services can always read and inspect the data that Azure Rights Management encrypts for your organization. If necessary, the encryption protection can then be removed or changed.

A super user always has the Rights Management Full Control [usage right](rights-management-usage-rights) for documents and emails that have been encrypted by your organization’s tenant. This ability is sometimes referred to as "reasoning over data" and is a crucial element in maintaining control of your organization’s data. For example, you would use this feature for any of the following scenarios:

- An employee leaves the organization and you need to read the files that they encrypted.
- An IT administrator needs to remove the current encryption settings that were configured for files and apply new encryption settings.
- Exchange Server needs to index mailboxes for search operations.
- You have existing IT services for data loss prevention (DLP) solutions, content encryption gateways (CEG), and anti-malware products that need to inspect files that are already encrypted.
- You need to bulk decrypt files for auditing, legal, or other compliance reasons.

## Configuration for the super user feature

By default, the super user feature isn't enabled, and no users are assigned to this role. It's enabled for you automatically if you configure the Rights Management connector for Exchange, and it's not required for standard services that run Exchange Online, Microsoft SharePoint Server, or SharePoint in Microsoft 365.

If you need to manually enable the super user feature, use the PowerShell cmdlet [Enable-AipServiceSuperUserFeature](/en-us/powershell/module/aipservice/enable-aipservicesuperuserfeature), and then assign users (or service accounts) as needed by using the [Add-AipServiceSuperUser](/en-us/powershell/module/aipservice/add-aipservicesuperuser) cmdlet or the [Set-AipServiceSuperUserGroup](/en-us/powershell/module/aipservice/set-aipservicesuperusergroup) cmdlet and add users (or other groups) as needed to this group.

Although using a group for your super users is easier to manage, for performance reasons, the Azure Rights Management service [caches the group membership](rights-management-users-groups#group-membership-caching). So if you need to assign a new user to be a super user to decrypt content immediately, add that user by using Add-AipServiceSuperUser, rather than adding the user to an existing group that you configured by using Set-AipServiceSuperUserGroup.

Note

- When adding a user with the [Add-AipServiceSuperUser](/en-us/powershell/module/aipservice/add-aipservicesuperuser) cmdlet, you must also add the primary mail address or user principal name to the group. Email aliases aren't evaluated.
- If you haven't yet installed the PowerShell module for the Azure Rights Management service, see [Install the AIPService PowerShell module for the Azure Right Management service](/en-us/purview/install-aipservice-powershell).

It doesn't matter when you enable the super user feature or when you add users as super users. For example, if you enable the feature on Thursday and then add a user on Friday, that user can immediately open content that was protected at the very beginning of the week.

## Security best practices for the super user feature

Follow these security best practices when using the super user feature:

- Restrict and monitor the administrators who are assigned a global administrator for your tenant, or who are assigned the GlobalAdministrator role by using the [Add-AipServiceRoleBasedAdministrator](/en-us/powershell/module/aipservice/add-aipservicerolebasedadministrator) cmdlet. These users can enable the super user feature and assign users (and themselves) as super users, and potentially decrypt all files that your organization encrypts.
- To see which users and service accounts are individually assigned as super users, use the [Get-AipServiceSuperUser](/en-us/powershell/module/aipservice/get-aipservicesuperuser) cmdlet.
- To see whether a super user group is configured, use the [Get-AipServiceSuperUserGroup](/en-us/powershell/module/aipservice/get-aipservicesuperusergroup) cmdlet and your standard user management tools to check which users are a member of this group.
- Like all administration actions, enabling or disabling the super feature, and adding or removing super users are logged and can be audited by using the [Get-AipServiceAdminLog](/en-us/powershell/module/aipservice/get-aipserviceadminlog) command. For example, see Example auditing for the super user feature.
- When super users decrypt files, file decryption is logged and can be audited with [usage logging](rights-management-usage-logging).

    Note

    While the logs include details about the decryption, including the user who decrypted the file, they don't detail when the user is a super user.

    Use the logs together with [Get-AipServiceSuperUser](/en-us/powershell/module/aipservice/get-aipservicesuperuser) and [Get-AipServiceSuperUserGroup](/en-us/powershell/module/aipservice/get-aipservicesuperusergroup) to first collect a list of super users that you can identify in the logs.
- If you don't need the super user feature for everyday services, enable the feature only when you need it, and disable it again by using the [Disable-AipServiceSuperUserFeature](/en-us/powershell/module/aipservice/disable-aipservicesuperuserfeature) cmdlet.

### Example auditing for the super user feature

The following log extract shows some example entries from using the [Get-AipServiceAdminLog](/en-us/powershell/module/aipservice/get-aipserviceadminlog) cmdlet.

In this example, the administrator for Contoso Ltd confirms that the super user feature is disabled, adds Richard Simone as a super user, checks that Richard is the only super user configured for the Azure Rights Management service, and then enables the super user feature so that Richard can now decrypt some files that were protected by an employee who has now left the company.

`2015-08-01T18:58:20	admin@contoso.com	GetSuperUserFeatureState	Passed	Disabled`

`2015-08-01T18:59:44	admin@contoso.com	AddSuperUser -id rsimone@contoso.com	Passed	True`

`2015-08-01T19:00:51	admin@contoso.com	GetSuperUser	Passed	rsimone@contoso.com`

`2015-08-01T19:01:45	admin@contoso.com	SetSuperUserFeatureState -state Enabled	Passed	True`

## Scripting options for super users

Often, somebody who is assigned a super user for the Azure Rights Management service needs to remove encryption from multiple files, in multiple locations. While it’s possible to do this task manually, it’s more efficient (and often more reliable) to script this using the [Set-FileLabel](/en-us/powershell/module/purviewinformationprotection/set-filelabel) cmdlet.

You can also use this cmdlet to apply a new label that doesn't apply encryption, or remove the label that applied encryption.

For more information about these cmdlets, see [Use PowerShell with the Microsoft Purview Information Protection client](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#use-powershell-with-the-microsoft-purview-information-protection-client) from the PurviewInformationProtection PowerShell documentation.

Note

The PurviewInformationProtection module is different from and supplements the [AIPService PowerShell module](/en-us/azure/information-protection/administer-powershell) that manages the Azure Rights Management service for Microsoft Purview Information Protection.

### Removing encryption from PST files

To remove encryption from PST files, we recommend that you use [eDiscovery from Microsoft Purview](ediscovery) to search and extract encrypted emails and encrypted attachments in emails.

The super user ability is automatically integrated with Exchange Online so that eDiscovery in the Microsoft Purview portal can search for encrypted items prior to export, or decrypt encrypted email on export.

If you can't use Microsoft Purview eDiscovery, you might have another eDiscovery solution that integrates with the Azure Rights Management service to similarly reason over data.

Or, if your eDiscovery solution can't automatically read and decrypt protected content, you can still use this solution in a multi-step process together with the [Set-FileLabel](/en-us/powershell/module/purviewinformationprotection/set-filelabel) cmdlet:

1. Export the email in question to a PST file from Exchange Online or Exchange Server, or from the workstation where the user stored their email.
2. Import the PST file into your eDiscovery tool. Because the tool can't read encrypted content, expect these items to generate errors.
3. From all the items that the tool couldn't open, generate a new PST file that this time, contains just encrypted items. This second PST file will likely be much smaller than the original PST file.
4. Run [Set-FileLabel](/en-us/powershell/module/purviewinformationprotection/set-filelabel) on this second PST file to decrypt the contents of this much smaller file. From the output, import the now-decrypted PST file into your discovery tool.

For more detailed information and guidance for performing eDiscovery across mailboxes and PST files, see the following blog post: [Azure Information Protection and eDiscovery Processes](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Azure-Information-Protection-and-eDiscovery-Processes/ba-p/270216).