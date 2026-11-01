---
layout: Conceptual
title: Learn about optical character recognition in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ocr-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.date: 2026-04-30T00:00:00.0000000Z
ms.custom:
- msecd-doc-authoring-1012
- sfi-ga-nochange
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how optical character recognition (OCR) in Microsoft Purview scans images for sensitive information across Exchange, SharePoint, OneDrive, Teams, and devices.
locale: en-us
document_id: 50a1d913-5e05-7949-75c2-c3b8a41aba27
document_version_independent_id: 50a1d913-5e05-7949-75c2-c3b8a41aba27
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ocr-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ocr-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ocr-learn-about.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 32484686-dfc1-d33f-69e3-918d2f51ba4e
---

# Learn about optical character recognition in Microsoft Purview | Microsoft Learn

By using optical character recognition (OCR) scanning, Microsoft Purview can scan images for sensitive information. OCR scanning is an optional feature that you must enable at the tenant level. After you enable it, select the locations where you want to scan images. You can scan images in Exchange, SharePoint, OneDrive, Teams, Windows, and macOS devices. When you configure the OCR settings, Microsoft Purview applies your existing policies for data loss prevention (DLP), records management, and insider risk management (IRM) to images and text-based content. For example, if you configure the DLP condition *content contains sensitive information* and include a data classifier such as the **Credit Card** sensitive information type (SIT), Microsoft Purview scans for credit card numbers in both text and images at all of the chosen locations.

## Workflow at a glance

| Phase | What's needed |
| --- | --- |
| **Create Azure subscription if needed** | If your organization doesn't already have an Azure pay-as-you-go subscription for your tenant, your Global admin needs to start by creating an [Azure account](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions). |
| **Estimate your OCR scanning charges** | [Use the OCR cost estimator](ocr-cost-estimator) to estimate the expected charges for your specific use cases. |
| **Set up pay-as-you-go billing to enable OCR.** | Your Global or SharePoint admin must follow the instructions in [Set up Microsoft Syntex billing in Azure](/en-us/microsoft-365/syntex/syntex-azure-billing#set-up-microsoft-syntex-billing-in-azure) to add a subscription for OCR. |
| **Configure OCR scanning settings** | The Compliance admin for your organization configures the OCR settings for your tenant. |

## Prerequisites

To use OCR scanning, your organization's Global admin needs to verify that an Azure pay-as-you-go subscription is in place. If not, they need to set up the subscription by following the instructions in [Create your initial Azure subscriptions](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions).

## Configure billing

When you enable OCR, all sensitive information types and trainable classifiers can detect characters that are in images.

Because it's an optional feature, your Global admin must set up pay-as-you-go billing to enable OCR. Refer to the instructions in [Set up Microsoft Syntex billing in Azure](/en-us/microsoft-365/syntex/syntex-azure-billing#set-up-microsoft-syntex-billing-in-azure) to add a subscription for OCR.

Note

After you enter billing information in Microsoft Syntex, your Compliance admin can configure OCR in Microsoft Purview without any extra setup or licensing requirements.

You can find OCR pay-as-you-go pricing information on the [Set up Microsoft Syntex billing in Azure](/en-us/microsoft-365/syntex/syntex-azure-billing#set-up-microsoft-syntex-billing-in-azure) page.

## Estimate your OCR scanning charges

Each image scanned counts as one transaction. This pricing means that stand-alone images (JPEG, JPG, PNG, BMP, or TIFF) each count as a single transaction. It also means that *each page* in a PDF file is charged separately. For example, if there are 10 pages in a PDF file, an OCR scan of the PDF file counts as 10 separate scans. For information on using the OCR cost estimator, see [Estimate your OCR costs](ocr-cost-estimator#estimate-your-ocr-costs).

Note

To reduce your OCR costs, the service uses the following caching mechanisms: Small images, such as logos and signatures that are sent in email via Microsoft Exchange, are scanned and billed only once per unique image across all users of the tenant for a moving window of five days. For Endpoint, the cache is maintained for 30 days. Caching is local to each endpoint device and only classifiers identified on the image and image hash are stored. Customer data isn't stored. There's no caching mechanism for standalone images in SharePoint and OneDrive. However, in embedded file types, if only text is updated, images aren't scanned again.

The service checks multiple parameters, including image stream hash and image size, to see if it can use the cache. If any parameter doesn't match, the service OCRs the image again.

Additionally, you can use each scanned image in any number of policies across data loss prevention, insider risk management, auto-labeling, and records management at no extra charge.

Important

For information about the Adobe requirements for using Microsoft Purview Data Loss Prevention (DLP) features with PDF files, see this article from Adobe: [Microsoft Purview Information Protection Support in Acrobat](https://helpx.adobe.com/enterprise/kb/mpip-support-acrobat.html).

## Configure your OCR settings

To configure OCR scanning for your tenant, follow these steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings**.
3. Select **Optical character recognition (OCR)** to enter your OCR configuration settings.
4. Select the locations where you want to scan images.
5. Select the groups that you want included or excluded from OCR scans.
6. Select **Done**.

For the full list of locations where OCR scans images and the solutions that act on the results, see Supported locations and solutions.

## Permissions

To create and deploy policies, your account must be a member of one of these role groups:

- Compliance administrator
- Compliance data administrator
- Global administrator
- Information Protection
- Information Protection Admin

Note

In general, OCR settings take effect about an hour after you turn them on.

Note

For information on OCR functionality in Microsoft Purview Communication Compliance, see [Create and manage communication compliance policies](communication-compliance-policies#optical-character-recognition-ocr).

## Supported locations and solutions

| Location | Supported Solutions |
| --- | --- |
| Exchange | Data loss prevention  Information protection: [Auto-labeling policies](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange) Records management: [Autoapply retention label policies](apply-retention-labels-automatically#automatically-apply-a-retention-label-to-retain-or-delete-content)^1^ |
| SharePoint sites | Data loss prevention  Insider risk management^2^ Records management: [Autoapply retention label policies](apply-retention-labels-automatically#automatically-apply-a-retention-label-to-retain-or-delete-content)^1^ |
| OneDrive accounts | Data loss prevention  Records management: [Autoapply retention label policies](apply-retention-labels-automatically#automatically-apply-a-retention-label-to-retain-or-delete-content)^1^ |
| Teams chat and channel messages | Data loss prevention  Insider risk management^2^ |
| Devices | Data loss prevention  Insider risk management^2^ |

^1^ Supports keywords and sensitive information types.^2^ Considers sensitive information types and trainable classifiers present in images for risk scoring.

## Supported file types

This functionality supports scanning images in the following file types, with the noted requirements:

| Locations | Supported file types |
| --- | --- |
| Exchange | JPEG, JPG, PNG, BMP, TIFF, and PDFs (scanned). Embedded images in DOCX, PPTX, XLSX, RAR, TAR, ZIP, 7z, and hybrid PDFs (containing searchable text and images) with a limit of 20 embedded images scanned per file. |
| SharePoint and OneDrive | BMP, PNG, JPEG, JPG, JFIF, ARW, CR2, CRW, ERF, GIF, MEF, MRW, NEF, NRW, ORF, PEF, RAW, RW2, RW1, SR2, TIF, TIFF, HEIC, HEIF, ARI, BAY, CAP, CR3, DCS, DCR, DRF, EIP, FFF, IIQ, K25, KDC, MOS, PTX, PXN, RAF, RWL, SRF, SRW, X3F, DNG, PDFs (scanned and hybrid containing searchable text and images) Embedded images in DOCX, PPTX, XLSX |
| Teams, Windows, and macOS endpoint | JPEG, JPG, PNG, BMP, TIFF, and PDF (image only) |

## Image requirements

| Requirement | Limit |
| --- | --- |
| File size (Exchange, Teams) | 20 MB max |
| File size (SharePoint, OneDrive, Windows, and macOS endpoints) | 50 MB max |
| Image resolution | 50 × 50 px minimum, 16,000 × 16,000 px maximum |

Important

- Only images uploaded after OCR is enabled are scanned.
- OCR extracts only the first 2 million characters of text.
- By default, incoming email (email from users outside the organization), internal mails (email shared within the users of the organization), and outgoing email (email sent to users outside the organization) are subject to OCR scanning. To exclude incoming mails from OCR scan, change the OCR settings from the default scope of **All sender groups** to the **Specific sender groups** and specify the internal groups that you want OCR to scan. To restrict OCR scans to mails sent outside the organization only, select the option under **Advanced Setting (Only Exchange)**. After selecting this checkbox, neither incoming mails nor any internal communications are OCRed. For information on changing the configurations, see Configure your OCR settings.
- Data loss prevention policy tips aren't supported for images in Exchange.
- If you [exclude a path](dlp-configure-endpoint-settings#file-path-exclusions) in the endpoint data loss prevention settings, OCR doesn't scan images in those folders.
- When OCR is turned on for Windows and macOS devices, the devices start sending messages to the cloud for scanning. The default bandwidth limit is [1,024 MB of data per device per day](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection). OCR stops scanning images once this daily limit is reached. If you want to continue scanning images, you can increase the bandwidth limit.
- For Endpoint Device, ensure that any network settings aren't obstructing the OCR, and a wildcard should be present allowing blob.core.windows.net endpoints.
- For Exchange, the feature supports embedded images in DOCX, PPTX, XLSX, RAR, TAR, ZIP, 7z, and hybrid PDFs (containing searchable text and images) with a limit of 20 embedded images scanned per file.

## Supported languages

OCR scanning supports more than [150 languages](/en-us/azure/ai-services/computer-vision/language-support).

## Summary

- To use OCR, set up Microsoft Syntex pay-as-you-go billing. (You don't need to set up Microsoft Syntex itself.)
- Configure OCR at the tenant level, so once OCR is configured, it's available to the entire Microsoft Purview stack.
- You don't need to create separate data classifiers for OCR. Once OCR is configured, existing [sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types), [exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types), [trainable classifiers](trainable-classifiers-learn-about#learn-about-trainable-classifiers), and [fingerprint SITs](sit-document-fingerprinting#document-fingerprinting) scan images as well as documents and emails.
- Microsoft Purview eDiscovery supports OCR at the case level. For more information, see [Search and analytics settings in eDiscovery](edisc-settings-search-analytics).