---
layout: Conceptual
title: Data Loss Prevention policy tips reference | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-09-03T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-data-loss-prevention
search.appverid:
- SPO160
- MET150
ms.assetid: 6501b5ef-6bf7-43df-b60d-f65781847d6c
ms.collection:
- purview-compliance
- SPO_Content
recommendations: false
description: Learn how to add a policy tip to a data loss prevention (DLP) policy notify a user that they're working with content that conflicts with a DLP policy.
ms.custom: seo-marvel-apr2021
locale: en-us
document_id: df40ebef-197d-85f5-7ef6-53cd6eaf106f
document_version_independent_id: df40ebef-197d-85f5-7ef6-53cd6eaf106f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-policy-tips-reference.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-policy-tips-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-policy-tips-reference.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
2PlusCloud:
- Azure
- M365
- Power
__autotagging_hash:
- 943AD37FB907664940CDE709E4050C0CBFF9CCDB331BE2FD81B851A161BB7925
platformId: 7ce3ff35-0613-61b7-a67e-f2f4b2ad9558
---

# Data Loss Prevention policy tips reference | Microsoft Learn

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## DLP Policy Tips support matrix for Outlook clients highlights

This short table highlights some common DLP support for policy tips across Outlook clients. For complete information, see:

- [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips)
- [Data loss prevention policy tip reference for Outlook on the Web](dlp-owa-policy-tips)
- [Data loss prevention policy tip reference for new Outlook for Windows](dlp-policy-reference-new-outlook)

| Feature | [Outlook for Microsoft 365 (ver. 2105 build 14026.20000 and semi-annual channel ver. 2102 build 13801.20862)](dlp-ol365-win32-policy-tips) | [Outlook On the Web](dlp-owa-policy-tips) | [new Outlook for Windows](dlp-policy-reference-new-outlook) |
| --- | --- | --- | --- |
| Policy tips supported | Yes | Yes | Yes |
| Top 10 conditions - Content is shared from M365- Content contains SITs- Content contains sensitivity label- Subject or Body contains words or phrases- Sender is - Sender is a member of- Sender domain is- Recipient is- Recipient domain is- Recipient is a member of | Yes | Yes | Yes |
| [Default Oversharing Dialog](dlp-ol365-win32-policy-tips#default-oversharing-dialog) | Yes | No | Yes |
| [Customized Oversharing Dialog](dlp-ol365-win32-policy-tips#customized-oversharing-dialog) | Yes | No | Yes |
| [Wait on Send dialog support for Oversharing for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips#wait-on-send-dialog-support-for-oversharing-for-outlook-for-microsoft-365) | Yes | No | Yes |
| [Microsoft provided sensitive information types (SIT)](sit-sensitive-information-type-learn-about) | Yes | Yes | Yes |
| [Custom SITs](sit-create-a-custom-sensitive-information-type) | Yes | Yes | Yes |
| [Exact data match SITs](sit-learn-about-exact-data-match-based-sits) | Yes | Yes | Yes |
| [Custom compliance URL to further educate end users](dlp-policy-reference#policy-tips-and-user-notifications-configuration-options) | Yes | No | No |

## Support Matrix for DLP policy tips across Microsoft apps

| **App and platform** | **DLP policy tip support** | **Sensitive information types supported** | **Conditions and actions supported** | **Comments** |
| --- | --- | --- | --- | --- |
| **Outlook On the Web** | ![](media/rightmrk.png) | Subset. See [Sensitive information types that support policy tips in Outlook on the Web](dlp-owa-policy-tips#sensitive-information-types-that-support-policy-tips-in-outlook-on-the-web) | Subset. See [Conditions that support policy tips in Outlook on the Web](dlp-owa-policy-tips#conditions-that-support-policy-tips-in-outlook-on-the-web) and [Actions that support policy tips in Outlook on the Web](dlp-owa-policy-tips#actions-that-support-policy-tips-in-outlook-on-the-web) | For full details, see [Data loss prevention policy tip reference for Outlook on the Web](dlp-owa-policy-tips) |
| **Outlook for Microsoft 365 (ver. 2105 build 14026.20000 and semi-annual channel ver. 2102 build 13801.20862)** | ![](media/rightmrk.png) | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) |
| **Outlook Mobile (iOS, Android)** | ![](media/rightmrk.png) | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS](dlp-outlook-mobile-policy-tip-ref) |
| **Outlook Mac** | ![](media/rightmrk.png) | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS](dlp-outlook-mobile-policy-tip-ref) |
| **SharePoint/OneDrive Web client** | ![](media/rightmrk.png) | All. | All. | See [Data loss prevention policy tip reference for SharePoint and OneDrive web client](dlp-spo-odbweb-policy-tips) |
| **SharePoint Win32/ OneDrive Win32 client** | ![](media/crsmrk.png) | None | None | DLP policy tips aren't supported on SharePoint or OneDrive desktop client apps |
| **Word, Excel, PowerPoint Web Client** | ![](media/rightmrk.png) | All | All SPO/ODB predicates and actions in DLP | DLP policy tip s are supported if the document is hosted on SharePoint or the OneDrive web app and the DLP policy is already stamped. |
| **Word, Excel, PowerPoint Mobile Client** | ![](media/crsmrk.png) | None | None | DLP policy tips aren't supported in mobile apps for Office. |
| **Teams Web/ Teams Desktop/ Teams Mobile/ Teams Mac** | ![](media/rightmrk.png) | All | All Teams predicates in DLP policy | Policy tips will show when a message is flagged as “This message has been flagged. What can I do?” When clicking the link, the user can review the sensitive info types detected and override or report an issue if allowed by the admin. No policy tips are shown for files. When the recipient tries to access the document, they might get access denied if not allowed. |
| **Win32 Endpoint Devices** | ![](media/rightmrk.png) | Subset | All Endpoint DLP predicates and actions in DLP policy | For more information, see Data Loss Prevention on Endpoint supports policy tips for only some sensitive information types |
| **macOS devices** | ![](media/rightmrk.png) | All | DLP policy tips are supported for all actions that are supported for macOS. | For more information, see [Endpoint DLP Windows 10/11 and macOS support](endpoint-dlp-learn-about#endpoint-dlp-windows-1011-and-macos-support) |
| **3rd party cloud apps** | ![](media/crsmrk.png) | None | None | DLP policy tips aren't supported on third party cloud apps |
| **On-prem** | ![](media/crsmrk.png) | None | None |  |
| **Word, Excel, PowerPoint Win32 Client** | ![](media/crsmrk.png) | Subset | Subset | See [Data loss prevention policy tip reference for Outlook for Microsoft 365](dlp-ol365-win32-policy-tips#data-loss-prevention-policy-tip-reference-for-outlook-for-microsoft-365) for the list of sensitive information types supportedPolicy tips for WXP client apps will work for documents stored on SharePoint or OneDrive Sites for all DLP policies that have exactly the below or a subset of conditions or actions in the DLP policy:<br>- Content contains sensitive information types<br>- Access Scope (Content is shared internally/externally)<br>- Notify User (policy tips/user notifications)<br>- Block everyone<br>- Incident reports<br><br> If any other condition or action is present, the DLP policy tip for that policy won't appear in the desktop apps of Word, Excel or PowerPoint.See [Policy tips in Excel, PowerPoint, and Word](dlp-use-notifications-and-policy-tips#policy-tips-in-excel-powerpoint-and-word) for more details |
| **Fabric and Power BI** | ![](media/rightmrk.png) | - Sensitivity labels - Sensitive information types (excluding exact data match sensitive information types) | Subset | Data loss prevention policies in Power BI and Fabric are generally available.  Policy tips and admin alerts are supported. |

## Data loss prevention on endpoint devices supports policy tips for only some sensitive information types

These sensitive information types (SIT)s can be detected on endpoint devices:

- [ABA routing number](sit-defn-aba-routing)
- [Argentina national identity (DNI) number](sit-defn-argentina-national-identity-numbers)
- [Australia bank account number](sit-defn-australia-bank-account-number)
- [Australia medical account number](sit-defn-australia-medical-account-number)
- [Australia passport number](sit-defn-australia-passport-number)
- [Australia tax file number](sit-defn-australia-tax-file-number)
- [Australia business number](sit-defn-australia-business-number)
- [Australia Company Number](sit-defn-australia-company-number)
- [Austria Driver's License Number](sit-defn-austria-drivers-license-number)
- [Austria Identity Card](sit-defn-austria-identity-card)
- [Austria Passport Number](sit-defn-austria-passport-number)
- [Austria Social Security Number](sit-defn-austria-social-security-number)
- [Austria Tax Identification Number](sit-defn-austria-tax-identification-number)
- [Austria value added tax](sit-defn-austria-value-added-tax)
- [Azure DocumentDB auth key](sit-defn-azure-document-db-auth-key)
- [Azure IAAS database connection string and Azure SQL connection string](sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](sit-defn-azure-iot-connection-string)
- [Azure publish setting password](sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](sit-defn-azure-redis-cache-connection-string)
- [Azure SAS](sit-defn-azure-sas)
- [Azure service bus connection string](sit-defn-azure-service-bus-connection-string)
- [Azure storage account key](sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](sit-defn-azure-storage-account-key-generic)
- [Azure Storage account Shared Access Signature](sit-defn-azure-storage-account-shared-access-signature)
- [Belgium drivers license number](sit-defn-belgium-drivers-license-number)
- [Belgium National Number](sit-defn-belgium-national-number)
- [Belgium passport number](sit-defn-belgium-passport-number)
- [Belgium value added tax number](sit-defn-belgium-value-added-tax-number)
- [Brazil CPF number](sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](sit-defn-brazil-legal-entity-number)
- [Brazil national identification card (RG)](sit-defn-brazil-national-identification-card)
- [Bulgaria drivers license number](sit-defn-bulgaria-drivers-license-number)
- [Bulgaria passport number](sit-defn-bulgaria-passport-number)
- [Bulgaria Uniform Civil Number](sit-defn-bulgaria-uniform-civil-number)
- [Canada bank account number](sit-defn-canada-bank-account-number)
- [Canada drivers license number](sit-defn-canada-drivers-license-number)
- [Canada health service number](sit-defn-canada-health-service-number)
- [Canada Passport Number](sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](sit-defn-canada-personal-health-identification-number)
- [Canada Social Insurance Number](sit-defn-canada-social-insurance-number)
- [Chile Identity Card Number](sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](sit-defn-china-resident-identity-card-number)
- [Credit Card Number](sit-defn-credit-card-number)
- [Croatia Driver's License Number](sit-defn-croatia-drivers-license-number)
- [Croatia Identity Card Number](sit-defn-croatia-identity-card-number)
- [Croatia Passport Number](sit-defn-croatia-passport-number)
- [Croatia Personal Identification (OIB) Number](sit-defn-croatia-personal-identification-number)
- [General Symmetric Key](sit-defn-general-symmetric-key)
- [Cyprus Driver's License Number](sit-defn-cyprus-drivers-license-number)
- [Cyprus Identity Card](sit-defn-cyprus-identity-card)
- [Cyprus Passport Number](sit-defn-cyprus-passport-number)
- [Cyprus Tax Identification Number](sit-defn-cyprus-tax-identification-number)
- [Czech drivers license number](sit-defn-czech-drivers-license-number)
- [Czech Personal Identity Number](sit-defn-czech-personal-identity-number)
- [Czech passport number](sit-defn-czech-passport-number)
- [Denmark Driver's License Number](sit-defn-denmark-drivers-license-number)
- [Denmark Passport Number](sit-defn-denmark-passport-number)
- [Denmark Personal Identification Number](sit-defn-denmark-personal-identification-number)
- [Drug Enforcement Agency (DEA) number](sit-defn-drug-enforcement-agency-number)
- [Estonia drivers license number](sit-defn-estonia-drivers-license-number#estonia-drivers-license-number)
- [Estonia Passport Number](sit-defn-estonia-passport-number)
- [Estonia Personal Identification Code](sit-defn-estonia-personal-identification-code)
- [EU Debit Card Number](sit-defn-eu-debit-card-number)
- [EU Driver's License Number](sit-defn-eu-drivers-license-number)
- [EU National Identification Number](sit-defn-eu-national-identification-number)
- [EU Passport Number](sit-defn-eu-passport-number)
- [EU Social Security Number (SSN) or Equivalent ID](sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax Identification Number (TIN)](sit-defn-eu-tax-identification-number)
- [Finland Driver's License Number](sit-defn-finland-drivers-license-number)
- [Finland European Health Insurance Number](sit-defn-finland-european-health-insurance-number)
- [Finland National ID](sit-defn-finland-national-id)
- [Finland Passport Number](sit-defn-finland-passport-number)
- [France Driver's License Number](sit-defn-france-drivers-license-number)
- [France Health Insurance Number](sit-defn-france-health-insurance-number)
- [France National ID Card (CNI)](sit-defn-france-national-id-card)
- [France Passport Number](sit-defn-france-passport-number)
- [France Social Security Number (INSEE)](sit-defn-france-social-security-number)
- [France Tax Identification Number (numéro SPI.)](sit-defn-france-tax-identification-number)
- [France Value Added Tax Number](sit-defn-france-value-added-tax-number)
- [German Driver's License Number](sit-defn-germany-drivers-license-number)
- [German Passport Number](sit-defn-germany-passport-number)
- [German Identity Card Number](sit-defn-germany-identity-card-number)
- [German Tax Identification Number](sit-defn-germany-tax-identification-number)
- [German Value Added Tax Number](sit-defn-germany-value-added-tax-number)
- [Greece Driver's License Number](sit-defn-greece-drivers-license-number)
- [Greece National ID Card](sit-defn-greece-national-id-card)
- [Greece Passport Number](sit-defn-greece-passport-number)
- [Greece Social Security Number (AMKA)](sit-defn-greece-social-security-number)
- [Greek Tax identification Number](sit-defn-greece-tax-identification-number)
- [Hong Kong Identity Card (HKID) Number](sit-defn-hong-kong-identity-card-number)
- [Hungary Social Security Number (TAJ)](sit-defn-hungary-social-security-number)
- [Hungary Value Added Tax Number](sit-defn-hungary-value-added-tax-number)
- [Hungary Driver's License Number](sit-defn-hungary-drivers-license-number)
- [Hungary Passport Number](sit-defn-hungary-passport-number)
- [Hungary Personal Identification Number](sit-defn-hungary-personal-identification-number)
- [Hungary Tax identification Number](sit-defn-hungary-tax-identification-number)
- [India Permanent Account Number (PAN)](sit-defn-india-permanent-account-number)
- [India Unique Identification (Aadhaar) Number](sit-defn-india-unique-identification-number)
- [Indonesia Identity Card (KTP) Number](sit-defn-indonesia-identity-card-number)
- [International Banking Account Number (IBAN)](sit-defn-international-banking-account-number)
- [International Classification of Diseases (ICD-10-CM)](sit-defn-international-classification-of-diseases-icd-10-cm)
- [International Classification of Diseases (ICD-9-CM)](sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP Address](sit-defn-ip-address)
- [Ireland Driver's License Number](sit-defn-ireland-drivers-license-number)
- [Ireland Passport Number](sit-defn-ireland-passport-number)
- [Ireland Personal Public Service (PPS) Number](sit-defn-ireland-personal-public-service-number)
- [Israel Bank Account Number](sit-defn-israel-bank-account-number)
- [Israel National ID](sit-defn-israel-national-identification-number)
- [Italy Driver's License Number](sit-defn-italy-drivers-license-number)
- [Italy Fiscal Code](sit-defn-italy-fiscal-code)
- [Italy Passport Number](sit-defn-italy-passport-number)
- [Italy Value Added Tax Number](sit-defn-italy-value-added-tax-number)
- [Japan Bank Account Number](sit-defn-japan-bank-account-number)
- [Japan Driver's License Number](sit-defn-japan-drivers-license-number)
- [Japan Passport Number](sit-defn-japan-passport-number)
- [Japan Resident Registration Number](sit-defn-japan-resident-registration-number)
- [Japan Social Insurance Number (SIN)](sit-defn-japan-social-insurance-number)
- [Japan My Number Corporate](sit-defn-japan-my-number-corporate)
- [Japan My Number Personal](sit-defn-japan-my-number-personal)
- [Japan Residence Card Number](sit-defn-japan-residence-card-number)
- [Latvia Driver's License Number](sit-defn-latvia-drivers-license-number)
- [Latvia Passport Number](sit-defn-latvia-passport-number)
- [Latvia Personal Code](sit-defn-latvia-personal-code)
- [Lithuania Driver's License Number](sit-defn-lithuania-drivers-license-number)
- [Lithuania Passport Number](sit-defn-lithuania-passport-number)
- [Lithuania Personal Code](sit-defn-lithuania-personal-code)
- [Luxemburg drivers license number](sit-defn-luxemburg-drivers-license-number)
- [Luxemburg national identification number (natural persons)](sit-defn-luxemburg-national-identification-number-natural-persons)
- [Luxemburg national identification number (non-natural persons)](sit-defn-luxemburg-national-identification-number-non-natural-persons)
- [Luxemburg passport number](sit-defn-luxemburg-passport-number)
- [Malaysia Identity Card Number](sit-defn-malaysia-identification-card-number)
- [Malta Driver's License Number](sit-defn-malta-drivers-license-number)
- [Malta Identity Card Number](sit-defn-malta-identity-card-number)
- [Malta Passport Number](sit-defn-malta-passport-number)
- [Malta Tax ID Number](sit-defn-malta-tax-identification-number)
- [Netherlands Citizen's Service (BSN) Number](sit-defn-netherlands-citizens-service-number)
- [Netherlands Driver's License Number](sit-defn-netherlands-drivers-license-number)
- [Netherlands Passport Number](sit-defn-netherlands-passport-number)
- [Netherlands Tax Identification Number](sit-defn-netherlands-tax-identification-number)
- [Netherlands Value Added Tax Number](sit-defn-netherlands-value-added-tax-number)
- [New Zealand bank account Number](sit-defn-new-zealand-bank-account-number)
- [New Zealand Driver License Number](sit-defn-new-zealand-drivers-license-number)
- [New Zealand Inland Revenue Number](sit-defn-new-zealand-inland-revenue-number)
- [New Zealand Ministry of Health Number](sit-defn-new-zealand-ministry-of-health-number)
- [New Zealand Social Welfare Number](sit-defn-new-zealand-social-welfare-number)
- [Norway Identity Number](sit-defn-norway-identification-number)
- [Philippines Unified Multi-Purpose ID Number](sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland Driver's License Number](sit-defn-poland-drivers-license-number)
- [Poland Identity Card](sit-defn-poland-identity-card)
- [Poland National ID (PESEL)](sit-defn-poland-national-id)
- [Poland Passport](sit-defn-poland-passport-number)
- [Poland Tax Identification Number](sit-defn-poland-tax-identification-number)
- [Polish REGON Number](sit-defn-poland-regon-number)
- [Portugal Citizen Card Number](sit-defn-portugal-citizen-card-number)
- [Portugal Driver's License Number](sit-defn-portugal-drivers-license-number)
- [Portugal Passport Number](sit-defn-portugal-passport-number)
- [Portugal Tax Identification Number](sit-defn-portugal-tax-identification-number)
- [Romania Driver's License Number](sit-defn-romania-drivers-license-number)
- [Romania Passport Number](sit-defn-romania-passport-number)
- [Romania Personal Numerical Code (CNP)](sit-defn-romania-personal-numeric-code)
- [Russian Passport Number (Domestic)](sit-defn-russia-passport-number-domestic)
- [Russian Passport Number (International)](sit-defn-russia-passport-number-international)
- [Saudi Arabia National ID](sit-defn-saudi-arabia-national-id)
- [Singapore national registration identity card (NRIC) number](sit-defn-singapore-national-registration-identity-card-number)
- [Slovakia Driver's License Number](sit-defn-slovakia-drivers-license-number)
- [Slovakia Passport Number](sit-defn-slovakia-passport-number)
- [Slovakia Personal Number](sit-defn-slovakia-personal-number)
- [Slovenia Driver's License Number](sit-defn-slovenia-drivers-license-number)
- [Slovenia Passport Number](sit-defn-slovenia-passport-number)
- [Slovenia Tax Identification Number](sit-defn-slovenia-tax-identification-number)
- [Slovenia Unique Master Citizen Number](sit-defn-slovenia-unique-master-citizen-number)
- [South Africa Identification Number](sit-defn-south-africa-identification-number)
- [South Korea Resident Registration Number](sit-defn-south-korea-resident-registration-number)
- [Spain DNI](sit-defn-spain-dni)
- [Spain Driver's License Number](sit-defn-spain-drivers-license-number)
- [Spain Passport Number](sit-defn-spain-passport-number)
- [Spain Social Security Number (SSN)](sit-defn-spain-social-security-number)
- [Spain Tax Identification Number](sit-defn-spain-tax-identification-number)
- [SQL Server Connection String](sit-defn-sql-server-connection-string)
- [Sweden Driver's License Number](sit-defn-sweden-drivers-license-number)
- [Sweden National ID](sit-defn-sweden-national-id)
- [Sweden Passport Number](sit-defn-sweden-passport-number)
- [Sweden Tax Identification Number](sit-defn-sweden-tax-identification-number)
- [SWIFT Code](sit-defn-swift-code)
- [Swiss Social Security Number AHV](sit-defn-switzerland-ssn-ahv-number)
- [Taiwan National ID](sit-defn-taiwan-national-identification-number)
- [Taiwan Passport Number](sit-defn-taiwan-passport-number)
- [Taiwan Resident Certificate (ARC/TARC)](sit-defn-taiwan-resident-certificate-number)
- [Thai Population Identification Code](sit-defn-thai-population-identification-code)
- [Turkish National Identification number](sit-defn-turkey-national-identification-number)
- [U.K. Driver's License Number](sit-defn-uk-drivers-license-number)
- [U.K. Electoral Roll Number](sit-defn-uk-electoral-roll-number)
- [U.K. National Health Service Number](sit-defn-uk-national-health-service-number)
- [U.K. National Insurance Number (NINO)](sit-defn-uk-national-insurance-number)
- [U.K. Unique Taxpayer Reference Number](sit-defn-uk-unique-taxpayer-reference-number)
- [U.S./U.K. passport number](sit-defn-us-uk-passport-number)
- [U.S. bank account number](sit-defn-us-bank-account-number)
- [U.S. drivers license number](sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](sit-defn-us-individual-taxpayer-identification-number)
- [U.S. social security number (SSN)](sit-defn-us-social-security-number)
- [Ukraine passport domestic](sit-defn-ukraine-passport-domestic)
- [Ukraine passport international](sit-defn-ukraine-passport-international)

Custom sensitive information types will also be detected in addition to the above out-of-the-box sensitive information types.