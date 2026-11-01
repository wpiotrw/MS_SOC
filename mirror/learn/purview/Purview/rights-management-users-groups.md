---
layout: Conceptual
title: Understand how user accounts and groups use the Azure Rights Management service | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/rights-management-users-groups
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2025-08-26T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: How user accounts and groups work with the Azure Rights Management encryption service from Microsoft Purview Information Protection.
locale: en-us
document_id: 8fb0aa2f-d5d1-3cbb-6a06-7fbd5dba98e6
document_version_independent_id: 8fb0aa2f-d5d1-3cbb-6a06-7fbd5dba98e6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/rights-management-users-groups.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: rights-management-users-groups
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/rights-management-users-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: aa11b84c-5dc7-ccf4-1faf-56ea0c8c4a70
---

# Understand how user accounts and groups use the Azure Rights Management service | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Before you use [the Azure Rights Management service](azure-rights-management-learn-about) to encrypt content for your organization, understand how the service works with accounts for users and groups in Microsoft Entra ID.

There are different ways to create these accounts for users and groups, which include:

- You create the users in the Microsoft 365 admin center, and the groups in the Exchange Online admin center.
- You create the users and groups in the Azure portal.
- You create the users and group by using PowerShell cmdlets.
- You create the users and groups in your on-premises Active Directory and synchronize them to Microsoft Entra ID.
- You create the users and groups in another directory and synchronize them to Microsoft Entra ID.

When you create users and groups by using the first three methods from this list, with one exception, they're automatically created in Microsoft Entra ID, and the Azure Rights Management service can use these accounts directly. However, some enterprise networks use an on-premises directory to create and manage users and groups. The Azure Rights Management service can't use these accounts directly; you must synchronize them to Microsoft Entra ID.

The exception referred to in the previous paragraph is dynamic distribution lists that you can create for Exchange Online. Unlike static distribution lists, these groups aren't replicated to Microsoft Entra ID and so can't be used by the Azure Rights Management service.

## How users and groups are used by the Azure Rights Management service

There are two scenarios for using users and groups with the Azure Rights Management service:

**For encryption settings** when you use the Azure Rights Management service to encrypt documents and emails. Administrators and users can select users and groups that can open the encrypted content, and additionally:

- Usage rights that determine how they can use the content. For example, whether they can only read it, or read and print it, or read and edit it.
- Access controls include an expiry date and whether a connection to the internet is required for access.

**For configuring the Azure Rights Management service** to support specific scenarios, and therefore only administrators select these groups. Examples include configuring the following:

- Super users, so that designated services or people can open encrypted content if required for eDiscovery or data recovery.
- Delegated administration of the Azure Rights Management service.
- Onboarding controls to support a phased deployment.

## Azure Rights Management service requirements for user accounts

For encryption settings, and configuring the Azure Rights Management service:

- To authorize users, two attributes in Microsoft Entra ID are used: **proxyAddresses** and **userPrincipalName**.
- The **Microsoft Entra proxyAddresses** attribute stores all email addresses for an account and can be populated in different ways. For example, a user in Microsoft 365 that has an Exchange Online mailbox automatically has an email address that is stored in this attribute. If you assign an alternative email address for a Microsoft 365 user, it is also saved in this attribute. It can also be populated by the email addresses that are synchronized from on-premises accounts.

    The Azure Rights Management service can use any value in this Microsoft Entra proxyAddresses attribute, providing the domain has been added to your tenant (a "verified domain"). For more information about verifying domains:

    - For Microsoft Entra ID: [Add a custom domain name to Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/add-custom-domain)
    - For Microsoft 365: [Add a domain to Microsoft 365](/en-us/office365/admin/setup/add-domain)
- The **Microsoft Entra userPrincipalName** attribute is used only when an account in your tenant doesn't have values in the Microsoft Entra proxyAddresses attribute. For example, you create a user in the Azure portal, or create a user for Microsoft 365 that doesn't have a mailbox.

### Encryption settings for external users

In addition to using the Microsoft Entra proxyAddresses and Microsoft Entra userPrincipalName for users in your tenant, the Azure Rights Management service also uses these attributes in the same way to authorize users from another tenant.

Other authorization methods:

- For email addresses that aren't in Microsoft Entra ID, the Azure Rights Management service can authorize these when they're authenticated with a Microsoft account. However, not all applications can open encrypted content when a Microsoft account is used for authentication.
- When an email is sent by using Microsoft Purview Message Encryption to a user who doesn't have an account in Microsoft Entra ID, the user is first authenticated by using federation with a social identity provider or by using a one-time passcode. Then the email address specified in the protected email is used to authorize the user.

## Azure Rights Management service requirements for group accounts

For assigning usage rights and access controls:

- You can use any type of group in Microsoft Entra ID that has an email address that contains a verified domain for the user's tenant. A group that has an email address is often referred to as a mail-enabled group.

For configuring the Azure Rights Management service:

- You can use any type of group in Microsoft Entra ID that has an email address from a verified domain in your tenant, with one exception. That exception is when you configure onboarding controls to use a group, which must be a security group in Microsoft Entra ID for your tenant.
- You can use any group in Microsoft Entra ID (with or without an email address) from a verified domain in your tenant for delegated administration of the Azure Rights Management service.

### Encryption settings for external groups

In addition to using the Microsoft Entra proxyAddresses for groups in your tenant, the Azure Rights Management service also uses this attribute in the same way to authorize groups from another tenant.

## Using accounts from Active Directory on-premises

If you have accounts that are managed on-premises that you want to use with the Azure Rights Management service, you must synchronize these to Microsoft Entra ID. For ease of deployment, we recommend that you use [Microsoft Entra Connect](/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect). However, you can use any directory synchronization method that achieves the same result.

When you synchronize your accounts, you don't need to synchronize all attributes. For a list of the attributes that must be synchronized, see the [Azure RMS section](/en-us/azure/active-directory/connect/active-directory-aadconnectsync-attributes-synchronized#azure-rms) from the Microsoft Entra documentation.

From the attributes list for Azure Rights Management, you see that for users, the on-premises AD attributes of **mail**, **proxyAddresses**, and **userPrincipalName** are required for synchronization. Values for **mail** and **proxyAddresses** are synchronized to the Microsoft Entra proxyAddresses attribute. For more information, see [How the proxyAddresses attribute is populated in Microsoft Entra ID](https://support.microsoft.com/help/3190357/how-the-proxyaddresses-attribute-is-populated-in-azure-ad)

## Considerations if email addresses change

If you change the email address of a user or group, we recommend that you add the old email address as a second email address (also known as a proxy address, alias, or alternate email address) to the user or group. When you do this, the old email address is added to the Microsoft Entra proxyAddresses attribute. This account administration ensures business continuity for any usage rights or other configurations there were saved when the old email address was in use.

If you can't do this, the user or group with the new email address risks being denied access to documents and emails that were previously protected with the old email address. In this case, you must repeat the protection configuration to save the new email address. For example, if the user or group was granted usage rights in templates or labels, edit those templates or labels and specify the new email address with same usage rights as you granted to the old email address.

Note that it's rare for a group to change its email address and if you assign usage rights to a group rather to than individual users, it doesn't matter if the user's email address changes. In this scenario, the usage rights are assigned to the group email address and not individual user email addresses. This is the most likely (and recommended) method for an administrator to configure usage rights that protect documents and emails. However, users might more typically assign custom permissions for individual users. Because you can't always know whether a user account or group has been used to grant access, it's safest to always add the old email address as a second email address.

## Group membership caching

For performance reasons, the Azure Rights Management service caches group membership. This caching means that any changes to group membership in Microsoft Entra ID can take up to three hours to take effect when these groups are used by the Azure Rights Management service and this time period is subject to change.

Remember to factor this delay into any changes or testing that you do when you use groups for granting usage rights or configuring the Azure Rights Management service.