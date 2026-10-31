---
layout: Conceptual
title: Data loss prevention policy tip reference for SharePoint in Microsoft 365 and OneDrive for work or school web client | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-spo-odbweb-policy-tips
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-31T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
recommendations: false
description: DLP policy tip reference for SharePoint in Microsoft 365 and OneDrive for work or school web client.
locale: en-us
document_id: 227424be-645d-c16a-5b4f-1949b2846d77
document_version_independent_id: 227424be-645d-c16a-5b4f-1949b2846d77
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-spo-odbweb-policy-tips.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-spo-odbweb-policy-tips
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-spo-odbweb-policy-tips.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 7412f6af-735d-d6a5-8383-67a71d091f2a
---

# Data loss prevention policy tip reference for SharePoint in Microsoft 365 and OneDrive for work or school web client | Microsoft Learn

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## DLP policy tips supported

Yes.

Important

When emails are encrypted with Microsoft Purview Message Encryption and the policy used to detect them uses the detect encryption condition policy tips will not appear.

For more information on blocking and notifications in SharePoint in Microsoft 365 and OneDrive for work or school, see [Blocking and notifications in SharePoint in Microsoft 365 and OneDrive for work or school](dlp-policy-reference#blocking-and-notifications-in-sharepoint-in-microsoft-365-and-onedrive)

## Conditions that support policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

- Content contains
- Content is shared from Microsoft 365
- Document property is
- File extension is
- Document name contains words or phrases
- Document size equals or is greater than
- Document created by
- Document created by member of
- Document is shared (OneDrive for work or school web client only)

## Actions that support policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

- Restrict access or encrypt the content in Microsoft 365 locations

## Sensitive information types that support policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

These preconfigured sensitive information types (SIT) support policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

- [ABA Routing Number](sit-defn-aba-routing)
- [All Credential Types](sit-defn-all-creds)
- [All full names](sit-defn-all-full-names)
- [All medical terms and conditions](sit-defn-all-medical-terms-conditions)
- [All Physical Addresses](sit-defn-all-physical-addresses)
- [Amazon S3 Client Secret Access Key](sit-defn-amazon-s3-client-secret-access-key)
- [Argentina national identity (DNI) number](sit-defn-argentina-national-identity-numbers)
- [Argentina Unique Tax Identification Key (CUIT/CUIL)](sit-defn-argentina-unique-tax-identification-key)
- [ASP.NET machine Key](sit-defn-asp-net-machine-key)
- [Australia bank account number](sit-defn-australia-bank-account-number)
- [Australian Business Number](sit-defn-australia-business-number)
- [Australian Company Number](sit-defn-australia-business-number)
- [Australia Driver's License Number](sit-defn-australia-drivers-license-number)
- [Australia medical account number](sit-defn-australia-medical-account-number)
- [Australia passport number](sit-defn-australia-passport-number)
- [Australia physical addresses](sit-defn-australia-physical-addresses)
- [Australia tax file number](sit-defn-australia-tax-file-number)
- [Austria Driver's License Number](sit-defn-austria-drivers-license-number)
- [Austria identity card](sit-defn-austria-identity-card)
- [Austria passport number](sit-defn-austria-passport-number)
- [Austria physical addresses](sit-defn-austria-physical-addresses)
- [Austria social security number](sit-defn-austria-social-security-number)
- [Austria tax identification number](sit-defn-austria-tax-identification-number)
- [Austria Value Added Tax (VAT) Number](sit-defn-austria-value-added-tax)
- [Azure App Service deployment password](sit-defn-azure-app-service-deployment-password)
- [Azure Batch shared access key](sit-defn-azure-batch-shared-access-key)
- [Azure Bot Framework secret key](sit-defn-azure-bot-framework-secret-key)
- [Azure Bot service app secret](sit-defn-azure-bot-service-app-secret)
- [Azure Cognitive Search API key](sit-defn-azure-cognitive-search-api-key)
- [Azure Cognitive Service key](sit-defn-azure-cognitive-service-key)
- [Azure Container Registry access key](sit-defn-azure-container-registry-access-key)
- [Azure Cosmos DB account access key](sit-defn-azure-cosmos-db-account-access-key)
- [Azure Databricks personal access token](sit-defn-azure-databricks-personal-access-token)
- [Azure DevOps app secret](sit-defn-azure-devops-app-secret)
- [Azure DevOps personal access token](sit-defn-azure-devops-personal-access-token)
- [Azure DocumentDB auth key](sit-defn-azure-document-db-auth-key)
- [Azure EventGrid access key](sit-defn-azure-eventgrid-access-key)
- [Azure Function Master / API key](sit-defn-azure-function-master-api-key)
- [Azure IAAS database connection string and Azure SQL connection string](sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](sit-defn-azure-iot-connection-string)
- [Azure IoT shared access key](sit-defn-azure-iot-shared-access-key)
- [Azure Logic app shared access signature](sit-defn-azure-logic-app-shared-access-signature)
- [Azure Machine Learning web service API key](sit-defn-azure-machine-learning-web-service-api-key)
- [Azure Maps subscription key](sit-defn-azure-maps-subscription-key)
- [Azure publish setting password](sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](sit-defn-azure-redis-cache-connection-string)
- [Azure Redis cache connection string password](sit-defn-azure-redis-cache-connection-string-password)
- [Azure SAS](sit-defn-azure-sas)
- [Azure service bus connection string](sit-defn-azure-service-bus-connection-string)
- [Azure service bus shared access signature](sit-defn-azure-service-bus-shared-access-signature)
- [Azure Shared Access key / Web Hook token](sit-defn-azure-shared-access-key-web-hook-token)
- [Azure SignalR access key](sit-defn-azure-signalr-access-key)
- [Azure SQL connection string](sit-defn-azure-sql-connection-string)
- [Azure storage account access key](sit-defn-azure-storage-account-access-key)
- [Azure storage account key](sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](sit-defn-azure-storage-account-key-generic)
- [Azure Storage account shared access signature](sit-defn-azure-storage-account-shared-access-signature)
- [Azure Storage account shared access signature for high risk resources](sit-defn-azure-storage-account-shared-access-signature-high-risk-resources)
- [Azure subscription management certificate](sit-defn-azure-subscription-management-certificate)
- [Belgium driver's license number](sit-defn-belgium-drivers-license-number)
- [Belgium national number](sit-defn-belgium-national-number)
- [Belgium passport number](sit-defn-belgium-passport-number)
- [Belgium physical addresses](sit-defn-belgium-physical-addresses)
- [Belgium value added tax number](sit-defn-belgium-value-added-tax-number)
- [Blood test terms](sit-defn-blood-test-terms)
- [Brand medication names](sit-defn-brand-medication-names)
- [Brazil CPF number](sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](sit-defn-brazil-legal-entity-number)
- [Brazil National ID Card (RG)](sit-defn-brazil-national-identification-card)
- [Brazil physical addresses](sit-defn-brazil-physical-addresses)
- [Bulgaria driver's license number](sit-defn-bulgaria-drivers-license-number)
- [Bulgaria passport number](sit-defn-bulgaria-passport-number)
- [Bulgaria physical addresses](sit-defn-bulgaria-physical-addresses)
- [Bulgaria uniform civil number](sit-defn-bulgaria-uniform-civil-number)
- [Canada bank account number](sit-defn-canada-bank-account-number)
- [Canada driver's license number](sit-defn-canada-drivers-license-number)
- [Canada health service number](sit-defn-canada-health-service-number)
- [Canada passport number](sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](sit-defn-canada-personal-health-identification-number)
- [Canada physical addresses](sit-defn-canada-physical-addresses)
- [Canada social insurance number](sit-defn-canada-social-insurance-number)
- [Chile identity card number](sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](sit-defn-china-resident-identity-card-number)
- [China physical addresses](sit-defn-china-physical-addresses)
- [Client secret / API key](sit-defn-client-secret-api-key)
- [Credit card number](sit-defn-credit-card-number)
- [Colombia national ID](sit-defn-colombia-national-id)
- [Colombia tax identification number](sit-defn-colombia-tax-identification-number)
- [Croatia driver's license number](sit-defn-croatia-drivers-license-number)
- [Croatia identity card number](sit-defn-croatia-identity-card-number)
- [Croatia passport number](sit-defn-croatia-passport-number)
- [Croatia personal identification (OIB) number](sit-defn-croatia-personal-identification-number)
- [Croatia physical addresses](sit-defn-croatia-physical-addresses)
- [Cyprus Driver's License Number](sit-defn-cyprus-drivers-license-number)
- [Cyprus identity card](sit-defn-cyprus-identity-card)
- [Cyprus passport number](sit-defn-cyprus-passport-number)
- [Cyprus physical addresses](sit-defn-cyprus-physical-addresses)
- [Cyprus tax identification number](sit-defn-cyprus-tax-identification-number)
- [Czech driver's license number](sit-defn-czech-drivers-license-number)
- [Czech passport number](sit-defn-czech-passport-number)
- [Czech personal identity number](sit-defn-czech-personal-identity-number)
- [Czech Republic physical addresses](sit-defn-czech-republic-physical-addresses)
- [Denmark driver's license number](sit-defn-denmark-drivers-license-number)
- [Denmark passport number](sit-defn-denmark-passport-number)
- [Denmark personal identification number](sit-defn-denmark-personal-identification-number)
- [Denmark physical addresses](sit-defn-denmark-physical-addresses)
- [Diseases](sit-defn-diseases)
- [Drug Enforcement Agency (DEA) number](sit-defn-drug-enforcement-agency-number)
- [Ecuador Unique Identification Number](sit-defn-ecuador-unique-identification-number)
- [Estonia driver's license number](sit-defn-estonia-drivers-license-number)
- [Estonia passport number](sit-defn-estonia-passport-number)
- [Estonia Personal Identification Code](sit-defn-estonia-personal-identification-code)
- [Estonia physical addresses](sit-defn-estonia-physical-addresses)
- [EU debit card number](sit-defn-eu-debit-card-number)
- [EU driver's license number](sit-defn-eu-drivers-license-number)
- [EU national identification number](sit-defn-eu-national-identification-number)
- [EU passport number](sit-defn-eu-passport-number)
- [EU Social Security Number (SSN) or Equivalent ID](sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax Identification Number (TIN)](sit-defn-eu-tax-identification-number)
- [Finland driver's license number](sit-defn-finland-drivers-license-number)
- [Finland European health insurance number](sit-defn-finland-european-health-insurance-number)
- [Finland national ID](sit-defn-finland-national-id)
- [Finland passport number](sit-defn-finland-passport-number)
- [Finland physical addresses](sit-defn-finland-physical-addresses)
- [France driver's license number](sit-defn-france-drivers-license-number)
- [France health insurance number](sit-defn-france-health-insurance-number)
- [France national id card (CNI)](sit-defn-france-national-id-card)
- [France passport number](sit-defn-france-passport-number)
- [France physical addresses](sit-defn-france-physical-addresses)
- [France social security number (INSEE)](sit-defn-france-social-security-number)
- [France Tax Identification Number (numéro SPI.)](sit-defn-france-tax-identification-number)
- [France value added tax number](sit-defn-france-value-added-tax-number)
- [General password](sit-defn-general-password)
- [General Symmetric key](sit-defn-general-symmetric-key)
- [Generic medication names](sit-defn-generic-medication-names)
- [German Driver's License Number](sit-defn-germany-drivers-license-number)
- [Germany identity card number](sit-defn-germany-identity-card-number)
- [German Passport Number](sit-defn-germany-passport-number)
- [Germany physical addresses](sit-defn-germany-physical-addresses)
- [Germany tax identification number](sit-defn-germany-tax-identification-number)
- [Germany value added tax number](sit-defn-germany-value-added-tax-number)
- [GitHub Personal Access Token](sit-defn-github-personal-access-token)
- [Google API key](sit-defn-google-api-key)
- [Greenland physical addresses](sit-defn-greenland-physical-addresses)
- [Greece driver's license number](sit-defn-greece-drivers-license-number)
- [Greece national ID card](sit-defn-greece-national-id-card)
- [Greece passport number](sit-defn-greece-passport-number)
- [Greece physical addresses](sit-defn-greece-physical-addresses)
- [Greece Social Security Number (AMKA)](sit-defn-greece-social-security-number)
- [Greek Tax Identification Number](sit-defn-greece-tax-identification-number)
- [Hong Kong identity card (HKID) number](sit-defn-hong-kong-identity-card-number)
- [Http authorization header](sit-defn-http-authorization-header)
- [Hungary driver's license number](sit-defn-hungary-drivers-license-number)
- [Hungary passport number](sit-defn-hungary-passport-number)
- [Hungary personal identification number](sit-defn-hungary-personal-identification-number)
- [Hungary physical addresses](sit-defn-hungary-physical-addresses)
- [Hungarian Social Security Number (TAJ)](sit-defn-hungary-social-security-number)
- [Hungary tax identification number](sit-defn-hungary-tax-identification-number)
- [Hungarian Value Added Tax Number](sit-defn-hungary-value-added-tax-number)
- [Iceland physical addresses](sit-defn-iceland-physical-addresses)
- [Impairments Listed In The U.S. Disability Evaluation Under Social Security](sit-defn-impairments-us-disability-evaluation-under-social-security)
- [India driver's License Number](sit-defn-india-drivers-license-number)
- [India GST Number](sit-defn-india-gst-number)
- [India permanent account number (PAN)](sit-defn-india-permanent-account-number)
- [India unique identification (Aadhaar) number](sit-defn-india-unique-identification-number)
- [India Voter Id Card](sit-defn-india-voter-id-card)
- [Indonesia Drivers License Number](sit-defn-indonesia-drivers-license-number)
- [Indonesia identity card (KTP) number](sit-defn-indonesia-identity-card-number)
- [Indonesia passport number](sit-defn-indonesia-passport-number)
- [International banking account number (IBAN)](sit-defn-international-banking-account-number)
- [International classification of diseases (ICD-10-CM)](sit-defn-international-classification-of-diseases-icd-10-cm)
- [International classification of diseases (ICD-9-CM)](sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP address](sit-defn-ip-address)
- [IP Address v4](sit-defn-ip-address-v4)
- [IP Address v6](sit-defn-ip-address-v6)
- [Ireland driver's license number](sit-defn-ireland-drivers-license-number)
- [Ireland passport number](sit-defn-ireland-passport-number)
- [Ireland personal public service (PPS) number](sit-defn-ireland-personal-public-service-number)
- [Ireland physical addresses](sit-defn-ireland-physical-addresses)
- [Israel bank account number](sit-defn-israel-bank-account-number)
- [Israel National ID](sit-defn-israel-national-identification-number)
- [Italy driver's license number](sit-defn-italy-drivers-license-number)
- [Italy fiscal code](sit-defn-italy-fiscal-code)
- [Italy passport number](sit-defn-italy-passport-number)
- [Italy physical addresses](sit-defn-italy-physical-addresses)
- [Italy value added tax number](sit-defn-italy-value-added-tax-number)
- [Japan bank account number](sit-defn-japan-bank-account-number)
- [Japan driver's license number](sit-defn-japan-drivers-license-number)
- [Japanese My Number Corporate](sit-defn-japan-my-number-corporate)
- [Japanese My Number Personal](sit-defn-japan-my-number-personal)
- [Japan passport number](sit-defn-japan-passport-number)
- [Japan physical addresses](sit-defn-japan-physical-addresses)
- [Japanese Residence Card Number](sit-defn-japan-residence-card-number)
- [Japan resident registration number](sit-defn-japan-resident-registration-number)
- [Japan social insurance number (SIN)](sit-defn-japan-social-insurance-number)
- [Lab test terms](sit-defn-lab-test-terms)
- [Latvia driver's license number](sit-defn-latvia-drivers-license-number)
- [Latvia passport number](sit-defn-latvia-passport-number)
- [Latvia personal code](sit-defn-latvia-personal-code)
- [Latvia physical addresses](sit-defn-latvia-physical-addresses)
- [Liechtenstein physical addresses](sit-defn-liechtenstein-physical-addresses)
- [Lifestyles that relate to medical conditions](sit-defn-lifestyles-relate-to-medical-conditions)
- [Lithuania driver's license number](sit-defn-lithuania-drivers-license-number)
- [Lithuania passport number](sit-defn-lithuania-passport-number)
- [Lithuania personal code](sit-defn-lithuania-personal-code)
- [Lithuania physical addresses](sit-defn-lithuania-physical-addresses)
- [Luxembourg Driver's License Number](sit-defn-luxemburg-drivers-license-number)
- [Luxembourg National Identification Number (Natural persons)](sit-defn-luxemburg-national-identification-number-natural-persons)
- [Luxembourg National Identification Number (Non-natural persons)](sit-defn-luxemburg-national-identification-number-non-natural-persons)
- [Luxembourg Passport Number](sit-defn-luxemburg-passport-number)
- [Luxembourg Physical Addresses](sit-defn-luxemburg-physical-addresses)
- [Malaysia Identity Card Number](sit-defn-malaysia-identification-card-number)
- [Malaysia passport number](sit-defn-malaysia-passport-number)
- [Malta driver's license number](sit-defn-malta-drivers-license-number)
- [Malta identity card number](sit-defn-malta-identity-card-number)
- [Malta passport number](sit-defn-malta-passport-number)
- [Malta physical addresses](sit-defn-malta-physical-addresses)
- [Malta Tax ID Number](sit-defn-malta-tax-identification-number)
- [Medical Specialities](sit-defn-medical-specialities)
- [Medicare Beneficiary Identifier (MBI) card](sit-defn-medicare-beneficiary-identifier-card)
- [Mexico Unique Population Registry Code (CURP)](sit-defn-mexico-unique-population-registry-code)
- [Microsoft Bing maps key](sit-defn-microsoft-bing-maps-key)
- [Microsoft Entra client access token](sit-defn-azure-ad-client-access-token)
- [Microsoft Entra client secret](sit-defn-azure-ad-client-secret)
- [Microsoft Entra user Credentials](sit-defn-azure-ad-user-credentials)
- [Netherlands citizen's service (BSN) number](sit-defn-netherlands-citizens-service-number)
- [Netherlands driver's license number](sit-defn-netherlands-drivers-license-number)
- [Netherlands passport number](sit-defn-netherlands-passport-number)
- [Netherlands physical addresses](sit-defn-netherlands-physical-addresses)
- [Netherlands tax identification number](sit-defn-netherlands-tax-identification-number)
- [Netherlands value added tax number](sit-defn-netherlands-value-added-tax-number)
- [New Zealand bank account number](sit-defn-new-zealand-bank-account-number)
- [New Zealand Driver License Number](sit-defn-new-zealand-drivers-license-number)
- [New Zealand inland revenue number](sit-defn-new-zealand-inland-revenue-number)
- [New Zealand ministry of health number](sit-defn-new-zealand-ministry-of-health-number)
- [New Zealand physical addresses](sit-defn-new-zealand-physical-addresses)
- [New Zealand social welfare number](sit-defn-new-zealand-social-welfare-number)
- [Norway Identity Number](sit-defn-norway-identification-number)
- [Norway physical addresses](sit-defn-norway-physical-addresses)
- [Philippines National ID](sit-defn-philippines-national-identification-number)
- [Philippines passport number](sit-defn-philippines-passport-number)
- [Philippines Unified Multi-Purpose ID Number](sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland driver's license number](sit-defn-poland-drivers-license-number)
- [Poland identity card](sit-defn-poland-identity-card)
- [Poland national ID (PESEL)](sit-defn-poland-national-id)
- [Poland Passport Number](sit-defn-poland-passport-number)
- [Poland physical addresses](sit-defn-poland-physical-addresses)
- [Poland REGON number](sit-defn-poland-regon-number)
- [Poland tax identification number](sit-defn-poland-tax-identification-number)
- [Portugal citizen card number](sit-defn-portugal-citizen-card-number)
- [Portugal driver's license number](sit-defn-portugal-drivers-license-number)
- [Portugal passport number](sit-defn-portugal-passport-number)
- [Portugal physical addresses](sit-defn-portugal-physical-addresses)
- [Portugal tax identification number](sit-defn-portugal-tax-identification-number)
- [Qatari ID Card Number](sit-defn-qatari-id-card-number)
- [Romania driver's license number](sit-defn-romania-drivers-license-number)
- [Romania passport number](sit-defn-romania-passport-number)
- [Romania personal numeric code (CNP)](sit-defn-romania-personal-numeric-code)
- [Romania physical addresses](sit-defn-romania-physical-addresses)
- [Russian Passport Number (Domestic)](sit-defn-russia-passport-number-domestic)
- [Russian Passport Number (International)](sit-defn-russia-passport-number-international)
- [Russia physical addresses](sit-defn-russia-physical-addresses)
- [Russia taxpayer identification number](sit-defn-russia-taxpayer-identification-number)
- [Saudi Arabia National ID](sit-defn-saudi-arabia-national-id)
- [Singapore driver's license number](sit-defn-singapore-drivers-license-number)
- [Singapore passport number](sit-defn-singapore-passport-number#singapore-passport-number)
- [Singapore national registration identity card (NRIC) number](sit-defn-singapore-national-registration-identity-card-number)
- [Singapore physical addresses](sit-defn-singapore-physical-addresses)
- [Slack access token](sit-defn-slack-access-token)
- [Slovakia driver's license number](sit-defn-slovakia-drivers-license-number)
- [Slovakia passport number](sit-defn-slovakia-passport-number)
- [Slovakia personal number](sit-defn-slovakia-personal-number)
- [Slovakia physical addresses](sit-defn-slovakia-physical-addresses)
- [Slovenia driver's license number](sit-defn-slovenia-drivers-license-number)
- [Slovenia passport number](sit-defn-slovenia-passport-number)
- [Slovenia physical addresses](sit-defn-slovenia-physical-addresses)
- [Slovenia tax identification number](sit-defn-slovenia-tax-identification-number)
- [Slovenia Unique Master Citizen Number](sit-defn-slovenia-unique-master-citizen-number)
- [South Africa identification number](sit-defn-south-africa-identification-number)
- [South Africa physical addresses](sit-defn-south-africa-physical-addresses)
- [South Korea driver's license number](sit-defn-south-korea-drivers-license-number)
- [South Korea passport number](sit-defn-south-korea-passport-number)
- [South Korea resident registration number](sit-defn-south-korea-resident-registration-number)
- [Spain DNI](sit-defn-spain-dni)
- [Spain driver's license number](sit-defn-spain-drivers-license-number)
- [Spain passport number](sit-defn-spain-passport-number)
- [Spain physical addresses](sit-defn-spain-physical-addresses)
- [Spain social security number (SSN)](sit-defn-spain-social-security-number)
- [Spain tax identification number](sit-defn-spain-tax-identification-number)
- [SQL Server connection string](sit-defn-sql-server-connection-string)
- [Surgical procedures](sit-defn-surgical-procedures)
- [Sweden driver's license number](sit-defn-sweden-drivers-license-number)
- [Sweden national ID](sit-defn-sweden-national-id)
- [Sweden passport number](sit-defn-sweden-passport-number)
- [Sweden physical addresses](sit-defn-sweden-physical-addresses)
- [Sweden tax identification number](sit-defn-sweden-tax-identification-number)
- [SWIFT code](sit-defn-swift-code)
- [Switzerland physical addresses](sit-defn-switzerland-physical-addresses)
- [Swiss Social Security Number AHV](sit-defn-switzerland-ssn-ahv-number)
- [Taiwan National ID](sit-defn-taiwan-national-identification-number)
- [Taiwan passport number](sit-defn-taiwan-passport-number)
- [Taiwan Resident Certificate (ARC/TARC)](sit-defn-taiwan-resident-certificate-number)
- [Thai population identification code](sit-defn-thai-population-identification-code)
- [Turkey national identification number](sit-defn-turkey-national-identification-number)
- [Turkey physical addresses](sit-defn-turkey-physical-addresses)
- [Types of medication](sit-defn-types-of-medication)
- [U.A.E. identity card number](sit-defn-uae-identity-card-number)
- [U.A.E. passport number](sit-defn-uae-passport-number)
- [U.K. driver's license number](sit-defn-uk-drivers-license-number)
- [U.K. electoral roll number](sit-defn-uk-electoral-roll-number)
- [U.K. national health service number](sit-defn-uk-national-health-service-number)
- [U.K. national insurance number (NINO)](sit-defn-uk-national-insurance-number)
- [U.K. physical addresses](sit-defn-uk-physical-addresses)
- [U.K. Unique Taxpayer Reference Number](sit-defn-uk-unique-taxpayer-reference-number)
- [U.S. bank account number](sit-defn-us-bank-account-number)
- [U.S. driver's license number](sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](sit-defn-us-individual-taxpayer-identification-number)
- [U.S. physical addresses](sit-defn-us-physical-addresses)
- [U.S. social security number (SSN)](sit-defn-us-social-security-number)
- [U.S./U.K. passport number](sit-defn-us-uk-passport-number)
- [Ukraine Passport Number (Domestic)](sit-defn-ukraine-passport-domestic)
- [Ukraine Passport Number (International)](sit-defn-ukraine-passport-international)
- [Ukraine physical addresses](sit-defn-ukraine-physical-addresses)
- [User login credentials](sit-defn-user-login-credentials)
- [X.509 certificate private key](sit-defn-x-509-certificate-private-key)

## Exact data match sensitive information types support for policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

Yes.

All exact data match sensitive information types are custom created. For more details, see [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits).

## Custom sensitive information types support for policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

Yes.

Custom sensitive information types that use REGEX, functions, keyword lists and keyword dictionaries support policy tips in Outlook on the Web. For more details, see [Create custom sensitive information types](sit-create-a-custom-sensitive-information-type) and [Create a custom sensitive information type using PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell).

## Sensitivity labels support for policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

Yes.

## Retention labels support for policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

No.

## Trainable classifiers support for policy tips in SharePoint in Microsoft 365 and OneDrive for work or school web client

No.