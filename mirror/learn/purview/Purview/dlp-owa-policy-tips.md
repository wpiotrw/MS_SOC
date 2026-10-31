---
layout: Conceptual
title: Data loss prevention policy tip reference for Outlook on the Web | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-08T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
recommendations: false
description: DLP policy tip reference for Outlook on the web.
locale: en-us
document_id: cff6a5e6-aa07-7cab-85e3-4d385577fa80
document_version_independent_id: cff6a5e6-aa07-7cab-85e3-4d385577fa80
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-owa-policy-tips.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-owa-policy-tips
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-owa-policy-tips.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: c19604a8-0242-c435-fd4a-b42aec1242b8
---

# Data loss prevention policy tip reference for Outlook on the Web | Microsoft Learn

Mailboxes must be hosted in Exchange Online. For more information, see: [Learn about data loss prevention](dlp-learn-about-dlp).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## DLP policy tips supported

Yes.

## Email notification supported for Outlook on the Web

Yes.

## Conditions that support policy tips in Outlook on the Web

- Content contains (SITs, sensitivity labels)
- Content is shared from M365
- Sender is a member of
- Recipient Domain Is
- Recipient is
- Subject Contains Words or phrases
- Sender is
- Sender domain is
- File extension is
- Subject matches patterns
- Subject or Body contains words or phrases
- Doc or Attachment is password protected
- Document name contains words or phrases
- Sender address contains words
- Document size equals or is greater than
- Subject or Body matches patterns
- Recipient address contains words
- Sender address matches patterns
- Document name matches patterns
- Recipient address matches patterns
- Message importance is
- Document property is
- Content is not labeled

## Actions that support policy tips in Outlook on the Web

- Restrict access or encrypt the content in Microsoft 365 locations
- Set headers
- Remove header
- Redirect the message to specific users
- Forward the message for approval to sender's manager
- Forward the message for approval to specific approvers
- Add recipient to the To box
- Add recipient to the Cc box
- Add recipient to the Bcc box
- Add the sender's manager as recipient
- Removed O365 Message Encryption and rights protection
- Prepend Email Subject
- Add HTML Disclaimer
- Modify Email Subject
- Deliver the message to the hosted quarantine

## Sensitive information types that support policy tips in Outlook on the Web

These preconfigured sensitive information types (SITs) support policy tips in Outlook on the Web.

- [ABA routing number](sit-defn-aba-routing)
- [Argentina national identity (DNI) number](sit-defn-argentina-national-identity-numbers)
- [Australia bank account number](sit-defn-australia-bank-account-number)
- [Australia medical account number](sit-defn-australia-medical-account-number)
- [Australia passport number](sit-defn-australia-passport-number)
- [Australia tax file number](sit-defn-australia-tax-file-number)
- [Azure DocumentDB auth key](sit-defn-azure-document-db-auth-key)
- [Azure IAAS database connection string and Azure SQL connection string](sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](sit-defn-azure-iot-connection-string)
- [Azure publish setting password](sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](sit-defn-azure-redis-cache-connection-string)
- [Azure SAS](sit-defn-azure-sas)
- [Azure service bus connection string](sit-defn-azure-service-bus-connection-string)
- [Azure storage account key](sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](sit-defn-azure-storage-account-key-generic)
- [Belgium national number](sit-defn-belgium-national-number)
- [Brazil CPF number](sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](sit-defn-brazil-legal-entity-number)
- [Brazil national identification card (RG)](sit-defn-brazil-national-identification-card)
- [Canada bank account number](sit-defn-canada-bank-account-number)
- [Canada driver's license number](sit-defn-canada-drivers-license-number)
- [Canada health service number](sit-defn-canada-health-service-number)
- [Canada passport number](sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](sit-defn-canada-personal-health-identification-number)
- [Canada social insurance number](sit-defn-canada-social-insurance-number)
- [Chile identity card number](sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](sit-defn-china-resident-identity-card-number)
- [Credit card number](sit-defn-credit-card-number)
- [Croatia identity card number](sit-defn-croatia-identity-card-number)
- [Croatia personal identification (OIB) number](sit-defn-croatia-personal-identification-number)
- [Czech personal identity number](sit-defn-czech-personal-identity-number)
- [Denmark personal identification number](sit-defn-denmark-personal-identification-number)
- [Drug Enforcement Agency (DEA) number](sit-defn-drug-enforcement-agency-number)
- [EU debit card number](sit-defn-eu-debit-card-number)
- [EU driver's license number](sit-defn-eu-drivers-license-number)
- [EU national identification number](sit-defn-eu-national-identification-number)
- [EU passport number](sit-defn-eu-passport-number)
- [EU social security number or equivalent identification](sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax identification number](sit-defn-eu-tax-identification-number)
- [Finland national ID](sit-defn-finland-national-id)
- [Finland passport number](sit-defn-finland-passport-number)
- [France driver's license number](sit-defn-france-drivers-license-number)
- [France national id card (CNI)](sit-defn-france-national-id-card)
- [France passport number](sit-defn-france-passport-number)
- [France social security number (INSEE)](sit-defn-france-social-security-number)
- [Germany driver's license number](sit-defn-germany-drivers-license-number)
- [Germany passport number](sit-defn-germany-passport-number)
- [Germany identity card number](sit-defn-germany-identity-card-number)
- [Greece national ID card](sit-defn-greece-national-id-card)
- [Hong Kong identity card (HKID) number](sit-defn-hong-kong-identity-card-number)
- [India permanent account number (PAN)](sit-defn-india-permanent-account-number)
- [India unique identification (Aadhaar) number](sit-defn-india-unique-identification-number)
- [Indonesia identity card (KTP) number](sit-defn-indonesia-identity-card-number)
- [International banking account number (IBAN)](sit-defn-international-banking-account-number)
- [International classification of diseases (ICD-10-CM)](sit-defn-international-classification-of-diseases-icd-10-cm)
- [International classification of diseases (ICD-9-CM)](sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP address](sit-defn-ip-address)
- [IP Address v4](sit-defn-ip-address-v4#ip-address-v4)
- [IP Address v6](sit-defn-ip-address-v6#ip-address-v6)
- [Ireland personal public service (PPS) number](sit-defn-ireland-personal-public-service-number)
- [Israel bank account number](sit-defn-israel-bank-account-number)
- [Israel national identification number](sit-defn-israel-national-identification-number)
- [Italy driver's license number](sit-defn-italy-drivers-license-number)
- [Japan bank account number](sit-defn-japan-bank-account-number)
- [Japan driver's license number](sit-defn-japan-drivers-license-number)
- [Japan passport number](sit-defn-japan-passport-number)
- [Japan resident registration number](sit-defn-japan-resident-registration-number)
- [Japan social insurance number (SIN)](sit-defn-japan-social-insurance-number)
- [Japan residence card number](sit-defn-japan-residence-card-number)
- [Malaysia identification card number](sit-defn-malaysia-identification-card-number)
- [Netherlands citizens service (BSN) number](sit-defn-netherlands-citizens-service-number)
- [New Zealand ministry of health number](sit-defn-new-zealand-ministry-of-health-number)
- [Norway identification number](sit-defn-norway-identification-number)
- [Philippines unified multi-purpose identification number](sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland identity card](sit-defn-poland-identity-card)
- [Poland national ID (PESEL)](sit-defn-poland-national-id)
- [Poland passport number](sit-defn-poland-passport-number)
- [Portugal citizen card number](sit-defn-portugal-citizen-card-number)
- [Saudi Arabia National ID](sit-defn-saudi-arabia-national-id)
- [Singapore national registration identity card (NRIC) number](sit-defn-singapore-national-registration-identity-card-number)
- [South Africa identification number](sit-defn-south-africa-identification-number)
- [South Korea resident registration number](sit-defn-south-korea-resident-registration-number)
- [Spain social security number (SSN)](sit-defn-spain-social-security-number)
- [SQL Server connection string](sit-defn-sql-server-connection-string)
- [Sweden national ID](sit-defn-sweden-national-id)
- [Sweden passport number](sit-defn-sweden-passport-number)
- [SWIFT code](sit-defn-swift-code)
- [Taiwan national identification number](sit-defn-taiwan-national-identification-number)
- [Taiwan passport number](sit-defn-taiwan-passport-number)
- [Taiwan-resident certificate (ARC/TARC) number](sit-defn-taiwan-resident-certificate-number)
- [Thai population identification code](sit-defn-thai-population-identification-code)
- [Turkey national identification number](sit-defn-turkey-national-identification-number)
- [U.K. drivers license number](sit-defn-uk-drivers-license-number)
- [U.K. electoral roll number](sit-defn-uk-electoral-roll-number)
- [U.K. national health service number](sit-defn-uk-national-health-service-number)
- [U.K. national insurance number (NINO)](sit-defn-uk-national-insurance-number)
- [U.S./U.K. passport number](sit-defn-us-uk-passport-number)
- [U.S. bank account number](sit-defn-us-bank-account-number)
- [U.S. driver's license number](sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](sit-defn-us-individual-taxpayer-identification-number)
- [U.S. social security number (SSN)](sit-defn-us-social-security-number)

## Exact data match sensitive information types support for policy tips in Outlook on the Web

Yes.

All exact data match sensitive information types are custom created. For more information, see [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits).

## Custom sensitive information types support for policy tips in Outlook on the Web

Yes.

Custom sensitive information types that use REGEX, functions, keyword lists, and keyword dictionaries support policy tips in Outlook on the Web. For more information, see [Create custom sensitive information types](sit-create-a-custom-sensitive-information-type) and [Create a custom sensitive information type using PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell).

## Sensitivity labels support for policy tips in Outlook on the Web

Yes.

## Retention labels support for policy tips in Outlook on the Web

No.

## Trainable classifiers support for policy tips in Outlook on the Web

No.

## Important information

- When emails are encrypted with Microsoft Purview Message Encryption and the policy used to detect them uses the *detect encryption* condition, policy tips will not appear.
- Administrators can use the DlpViaDcsEnabled parameter to enable exact same features and conditions that New Outlook does, see: [Learn about Organisation configuration](/en-us/powershell/module/exchangepowershell/set-organizationconfig?view=exchange-ps&amp;source=docs).