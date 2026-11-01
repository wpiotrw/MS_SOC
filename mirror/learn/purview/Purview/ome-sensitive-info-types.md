---
layout: Conceptual
title: Create a sensitive information type policy using Microsoft Purview Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome-sensitive-info-types
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
- Strat_O365_Enterprise
description: Learn how to create a sensitive information type policy for your organization using message encryption.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, admindeeplinkEXCHANGE, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: a9d6a0b5-4c39-a245-8319-627536beea39
document_version_independent_id: a9d6a0b5-4c39-a245-8319-627536beea39
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome-sensitive-info-types.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome-sensitive-info-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome-sensitive-info-types.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c36216dc-26e5-ff32-6692-4c25d3069f78
---

# Create a sensitive information type policy using Microsoft Purview Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

You can use either Exchange mail flow rules or Microsoft Purview Data Loss Prevention (DLP) to create a sensitive information type policy with Microsoft Purview Message Encryption. To create an Exchange mail flow rule, you can use either the [Exchange admin center (EAC)](https://go.microsoft.com/fwlink/p/?linkid=2059104) or Exchange PowerShell.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## To create the policy by using mail flow rules in the EAC

Sign in to the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) and go to **Mail flow** &gt; **Rules**. On the Rules page, create a rule that applies Message Encryption. You can create a rule based on conditions such as the presence of certain keywords or sensitive information types in the message or attachment.

### To create the policy by using mail flow rules in Exchange PowerShell

Use a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell). Use the `Set-IRMConfiguration` and `New-TransportRule` cmdlets to create the policy.

## Example mail flow rule created with Exchange PowerShell

Run the following commands in PowerShell to create an Exchange mail flow rule that automatically encrypts emails sent outside your organization with the encrypt-only option if the emails or their attachments contain the following sensitive information types:

- ABA routing number
- Credit card number
- Drug Enforcement Agency (DEA) number
- U.S. or U.K. passport number
- U.S. bank account number
- U.S. Individual Taxpayer Identification Number (ITIN)
- U.S. Social Security Number (SSN)

```powershell
Set-IRMConfiguration -DecryptAttachmentForEncryptOnly $true
New-TransportRule -Name "Encrypt outbound sensitive emails (out of box rule)" -SentToScope  NotInOrganization  -ApplyRightsProtectionTemplate "Encrypt" -MessageContainsDataClassifications @(@{Name="ABA Routing Number"; minCount="1"},@{Name="Credit Card Number"; minCount="1"},@{Name="Drug Enforcement Agency (DEA) Number"; minCount="1"},@{Name="U.S. / U.K. Passport Number"; minCount="1"},@{Name="U.S. Bank Account Number"; minCount="1"},@{Name="U.S. Individual Taxpayer Identification Number (ITIN)"; minCount="1"},@{Name="U.S. Social Security Number (SSN)"; minCount="1"}) -SenderNotificationType "NotifyOnly"
```

For cmdlet syntax and parameter details, see [Set-IRMConfiguration](/en-us/powershell/module/exchange/set-irmconfiguration) and [New-TransportRule](/en-us/powershell/module/exchange/new-transportrule).

## How recipients access attachments

After Microsoft encrypts a message, recipients have unrestricted access to attachments when they access and open their encrypted email.

## To prepare for automatic encryption of outbound sensitive emails

You may want to update any applicable end-user documentation and training materials to prepare people in your organization for the automatic encryption of outbound messages containing sensitive information. Share these message encryption resources with your users as appropriate:

- [Send, view, and reply to encrypted messages in Outlook for PC](https://support.microsoft.com/office/send-view-and-reply-to-encrypted-messages-in-outlook-for-pc-eaa43495-9bbb-4fca-922a-df90dee51980)
- [Microsoft 365 Essentials Video: Message Encryption](https://youtu.be/CQR0cG_iEUc)

## View these changes in the audit log

Microsoft 365 audits the creation of the mail flow rule and makes the audit record available to administrators. The operation is 'New-TransportRule' and a snippet of a sample audit entry from the Audit Log Search in the Microsoft Purview portal is as follows:

```text
*{"CreationTime":"2018-11-28T23:35:01","Id":"a1b2c3d4-daa0-4c4f-a019-03a1234a1b0c","Operation":"New-TransportRule","OrganizationId":"123456-221d-12345 ","RecordType":1,"ResultStatus":"True","UserKey":"Microsoft Operator","UserType":3,"Version":1,"Workload":"Exchange","ClientIP":"123.456.147.68:17584","ObjectId":"","UserId":"Microsoft Operator","ExternalAccess":true,"OrganizationName":"contoso.onmicrosoft.com","OriginatingServer":"CY4PR13MBXXXX (15.20.1382.008)","Parameters": {"Name":"Organization","Value":"123456-221d-12346"{"Name":"ApplyRightsProtectionTemplate","Value":"Encrypt"},{"Name":"Name","Value":"Encrypt outbound sensitive emails (out of box rule)"},{"Name":"MessageContainsDataClassifications"...etc.*
```

## To disable or customize the sensitive information types policy

Once you've created the Exchange mail flow rule, you can [disable or edit the rule](/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules#enable-or-disable-a-mail-flow-rule) by going to **Mail flow** &gt; **Rules** in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) and disabling the rule "*Encrypt outbound sensitive emails (out of box rule)*".