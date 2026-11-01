---
layout: Conceptual
title: About document fingerprinting | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-31T00:00:00.0000000Z
audience: ITPro
ms.topic: article
search.appverid: MET150
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
description: Document fingerprinting makes it easier for you to protect information by identifying standard forms that are used by your organization. This article describes the concepts behind document fingerprinting and how to create one by using PowerShell.
locale: en-us
document_id: 5fc7a49d-4b0a-52db-99be-cc9c3edc72c9
document_version_independent_id: 5fc7a49d-4b0a-52db-99be-cc9c3edc72c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-document-fingerprinting.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-document-fingerprinting
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-document-fingerprinting.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
platformId: 13713ee8-dbf0-7339-5a87-93e4a99816ca
---

# About document fingerprinting | Microsoft Learn

Document fingerprinting is a Microsoft Purview feature that takes a standard form that you provide and creates a sensitive information type (SIT) based on that form. Document fingerprinting makes it easier for you to protect sensitive information by identifying standard forms that are used throughout your organization. This article describes the concepts behind document fingerprinting and how to create a document fingerprint using the user interface or using PowerShell.

Document fingerprinting includes the following benefits:

- SITs created from document fingerprinting can be used as a detection method in DLP policies scoped to Exchange, SharePoint, OneDrive, Teams, and Devices.
- [MIP auto-labeling](apply-sensitivity-label-automatically) can use document fingerprinting as a detection method in Exchange, SharePoint, and OneDrive.
- Document fingerprint features can be managed through the Microsoft Purview user interface.
- Partial matching is supported.
- Exact matching is supported.
- Improved detection accuracy
- Support for detection in multiple languages, including dual-byte languages such as Chinese, Japanese, and Korean.

Important

If you are an E5 customer, we recommend updating your existing fingerprints to take advantage of the full document fingerprint feature set. If you are an E3 customer, we recommend upgrading to an E5 license. If you choose not to, you won't be able to modify existing fingerprints or create new ones after April, 2023.

## Basic scenario for document fingerprinting

As mentioned, the document fingerprinting feature converts a standard form of information into a sensitive information type (SIT), which you can use in the rules of your DLP policies. For example, you can create a document fingerprint based on a blank patent template and then create a DLP policy that detects and blocks all outgoing patent templates with sensitive content filled in. Optionally, you can set up [policy tips](dlp-use-notifications-and-policy-tips) to notify senders that they might be sending sensitive information, and that the sender should verify that the recipients are qualified to receive the patents. This process works with any text-based forms used in your organization. Other examples of forms that you can upload include:

- Government forms
- Health Insurance Portability and Accountability Act (HIPAA) compliance forms
- Employee information forms for Human Resources departments
- Custom forms created specifically for your organization

Ideally, your organization already has an established business practice of using certain forms to transmit sensitive information. To enable detection, upload an empty form to be converted to a document fingerprint. Next, set up a corresponding policy. Once you complete these steps, DLP detects any documents in outbound mail that match that fingerprint.

For more information on designing a DLP policy, see [Design a data loss prevention policy](dlp-policy-design).

For more informaiton on creating and deploying a DLP policy, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy).

## How document fingerprinting works

You know documents don't have actual fingerprints, but the name helps explain the feature. In the same way a person's fingerprints have unique patterns, frequently used forms (templates) can have patterns of words that are unique to them. You can use the SIT that's based on this pattern to detect files that were created using the same template. This is why uploading a form or template creates the most effective type of document fingerprint. Everyone who fills out a form uses the same original set of words and then adds their own words to the document. Documents to be scanned can't be password protected and must contain all the text from the original form.

![Diagram of document fingerprinting.](media/document-fingerprinting-diagram.png)

The patent template contains the blank fields **Patent title**, **Inventors**, and **Description**, along with descriptions for each of those fields — that's the word pattern. When you upload the original patent template, it's in one of the supported file types and in plain text. MIcrosoft Purview converts this word pattern into a document fingerprint, which is a small Unicode XML file containing a unique hash value that represents the original text. As a security measure, the original document itself isn't stored; only the hash value is stored. The original document can't be reconstructed from the hash value. The patent fingerprint is represented in a SIT that you can use as a condition in a DLP policy.

For example, if you set up a DLP policy that prevents regular employees from sending outgoing messages containing patents, DLP uses the patent fingerprint SIT to detect patents and block those emails. Alternatively, you might want to let your legal department be able to send patents to other organizations because it has a business need for doing so. To allow specific departments to send sensitive information, create exceptions for those departments in your DLP policy. Alternatively, you can allow them to override a policy tip with a business justification.

Important

Text in embedded documents is not considered for fingerprint creation. You need to provide sample template files that don't contain embedded documents.

#### Limitations of document fingerprinting

Document fingerprinting doesn't detect sensitive information in the following cases:

- Password protected files
- Files that contain images only
- Documents that don't contain all the text from the original form used to create the document fingerprint
- Files larger than 4 MB

Note

To use document fingerprinting with devices, [**Advanced classification scanning and protection**](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) must be turned on.

Fingerprints are stored in a separate rule pack. This rule pack has a maximum size limit of 300 KB. Given this limit, you can create approximately 100 fingerprints per tenant.

Note

The template used to create a fingerprint should have at least 256 characters. The supported extracted text length for the fingerprint template must be between 256 and 204,800 characters.

The following examples show what happens if you create a document fingerprint based on a patent template. However, you can use any form as a basis for creating a document fingerprint.

### Example: Create a patent document that matches the document fingerprint of a patent template

1. In the Microsoft Purview portal, navigate to **Data Loss Prevention** or **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types**.
2. On the **Sensitive info types** page, choose **+ Create Fingerprint based SIT**.
3. Enter a name and description for your new SIT.
4. Upload the file you wish to use as the fingerprint template.
5. OPTIONAL: Adjust the requirements for each confidence level. (For more information, see Partial matching and Exact matching.)
6. Choose **Next**.
7. Review your settings and then choose **Create**.
8. When the confirmation page displays, choose **Done**.

### PowerShell example of a patent document matching a document fingerprint of a patent template

```powershell
>> $Patent_Form = ([System.IO.File]::ReadAllBytes('C:\My Documents\patent.docx'))

>> New-DlpSensitiveInformationType -Name "Patent SIT" -FileData $Patent_Form  -ThresholdConfig @{low=40;medium=60;high=80} -IsExact $false -Description "Contoso Patent Template"
```

### Partial matching

To configure partial matching of a document fingerprint, when you are setting the configuration options during template upload, set the confidence level, choose **Low**, **Medium**, or **High**, and designate how much of the text in the file must match the fingerprint in terms of a percentage between 30% - 90%.

A high confidence level returns the fewest false positives but might result in more false negatives. Low or medium confidence levels return more false positives but few to zero false negatives.

- **low confidence**: Matched items contain the fewest false negatives but the most false positives. Low confidence returns all low, medium, and high confidence matches.
- **medium confidence**: Matched items contain an average number of false positives and false negatives. Medium confidence returns all medium, and high confidence matches.
- **high confidence**: Matched items contain the fewest false positives but the most false negatives.

### Exact matching

To configure exact matching of a document fingerprint, select **Exact** as the value for the high confidence level. When you set the high confidence level to **Exact**, only files that have exactly the same text as the fingerprint are detected. If the file has even a small deviation from the fingerprint, it won't be detected.

## Already using fingerprint SITs?

Your existing fingerprints and policies/rules for those fingerprints should continue to work. If you don't want to use the latest fingerprint features, you don't have to do anything.

If you have an E5 license and want to use the latest fingerprint features, you have 2 choices:

- Create a new fingerprint.
- migrate a policy to the newer version.

Note

Creating new fingerprints using the templates on which a fingerprint already exists is not supported.

## Create a custom sensitive information type based on document fingerprinting using PowerShell

Currently, you can create a document fingerprint only in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

To create a custom SIT based on a document fingerprint, use the **New-DlpSensitiveInformationType** cmdlet. The following example creates a new document fingerprint named “Contoso Customer Confidential” based on the file C:\My Documents\Contoso Customer Form.docx.

```powershell
$Employee_Form = ([System.IO.File]::ReadAllBytes('C:\My Documents\Contoso Customer Form.docx'))

New-DlpSensitiveInformationType -Name "Contoso Customer Confidential" -FileData $Employee_Form -ThresholdConfig @{low=40;medium=60;high=80} -IsExact $false -Description "Message contains Contoso customer information."
```

Finally, add the "Contoso Customer Confidential" sensitive information type to a DLP policy in the Microsoft Purview portal. This example adds a rule to an existing DLP policy, named "ConfidentialPolicy".

```powershell
New-DlpComplianceRule -Name "ContosoConfidentialRule" -Policy "ConfidentialPolicy" -ContentContainsSensitiveInformation @{Name="Contoso Customer Confidential"} -BlockAccess $True
```

You can also use the Fingerprint SIT in mail flow rules in Exchange, as shown in the following example. To run this command, you first need to connect to Exchange PowerShell. Also, note that it takes time for the SITs to sync with the Exchange admin center.

```powershell
New-TransportRule -Name "Notify :External Recipient Contoso confidential" -NotifySender NotifyOnly -Mode Enforce -SentToScope NotInOrganization -MessageContainsDataClassification @{Name=" Contoso Customer Confidential"}
```

DLP can now detect documents that match the Contoso Customer Form.docx document fingerprint.

For syntax and parameter information, see:

- [New-DlpFingerprint](/en-us/powershell/module/exchange/New-DlpFingerprint)
- [New-DlpSensitiveInformationType](/en-us/powershell/module/exchange/New-DlpSensitiveInformationType)
- [Remove-DlpSensitiveInformationType](/en-us/powershell/module/exchange/Remove-DlpSensitiveInformationType)
- [Set-DlpSensitiveInformationType](/en-us/powershell/module/exchange/Set-DlpSensitiveInformationType)
- [Get-DlpSensitiveInformationType](/en-us/powershell/module/exchange/Get-DlpSensitiveInformationType)

## Edit, test, or delete a document fingerprint

To do this in the Microsoft Purview portal, open the fingerprint SIT you want to edit, test, or delete and choose the appropriate icon.

To do this via PowerShell, run the following commands:

**Edit a document fingerprint**

```powershell
>> Set-DlpSensitiveInformationType -Name "Fingerprint SIT" -FileData ([System.IO.File]::ReadAllBytes('C:\My Documents\file1.docx')) -ThresholdConfig @{low=30;medium=50;high=80} -IsExact $false-Description "A friendly Description"
```

**Test a document fingerprint**

```powershell
>> $r = Test-DataClassification -TextToClassify "Credit card information Visa: 4485 3647 3952 7352. Patient Identifier or SSN: 452-12-1232"
>> $r.ClassificationResults
```

**Delete a document fingerprint**

```powershell
>> Remove-DlpSensitiveInformationType "Fingerprint SIT"
```

## Migrate an existing fingerprint SIT to a via the Microsoft Purview Portal

1. Open the Microsoft Purview portal &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types**.
2. Open the SIT containing the fingerprint that you want to migrate.
3. Choose **Edit**.
4. Upload the same fingerprint file again.
5. Review the fingerprint settings &gt; **Done**.

## Migrate a fingerprint using PowerShell

Enter the following command:

```powershell
Set-DlpSensitiveInformationType -Name "Old Fingerprint" -FileData ([System.IO.File]::ReadAllBytes('C:\My Documents\file1.docx')) -ThresholdConfig @{low=30;medium=50;high=80} -IsExact $false-Description "A friendly Description"
```