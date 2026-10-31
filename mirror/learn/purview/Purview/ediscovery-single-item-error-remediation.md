---
layout: Conceptual
title: Single item error remediation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-single-item-error-remediation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can fix a processing error in a document in a review set in eDiscovery (Premium) without having to follow the bulk error remediation process.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: sfi-image-nochange
locale: en-us
document_id: a87177b9-ac49-a333-6b46-c49737485406
document_version_independent_id: a87177b9-ac49-a333-6b46-c49737485406
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-single-item-error-remediation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-single-item-error-remediation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-single-item-error-remediation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 17d1f719-f07f-b085-1cad-51bcbad98f7c
---

# Single item error remediation | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Error remediation gives Microsoft Purview eDiscovery (Premium) users the ability to rectify data issues that prevent eDiscovery (Premium) from properly processing the content. For example, files that are password protected can't be processed because those files are locked or encrypted. Previously, you could only remediate errors in bulk by using [this workflow](ediscovery-error-remediation-when-processing-data). But sometimes, it doesn't make sense to remediate errors in multiple files when you’re unsure if any of those files are responsive to the case you’re investigating. It also might not make sense to remediate errors before you’ve had a chance to review the file metadata (such as file location or who had access) to help you make up-front decisions about responsiveness. A new feature called *single item error remediation* gives eDiscovery managers the ability to view the metadata of files with a processing error and if necessary remediate the error directly in the review set. The article discusses how to identify, ignore, and remediate files with processing errors in a review set.

## Identify documents with errors

Documents with processing errors in a review set are now identified (with a banner). You can remediate or ignore the error. The following screenshot shows the processing error banner for a Word document in a review set that is password-protected. Also notice that you can view the file metadata of documents with processing errors.

![Banner displayed for document with processing error.](media/sierimage1.png)

You can also search for documents that have processing errors by using the **Processing status** condition when [querying the documents in a review set](ediscovery-review-set-search).

![Use the Processing status condition to search for error documents.](media/sierimage2.png)

### Ignore errors

You can ignore a processing error by selecting **Ignore** in the processing error banner. When you ignore an error, the document is removed from the [bulk error remediation workflow](ediscovery-error-remediation-when-processing-data). After an error is ignored, the document banner changes color and indicates that the processing error was ignored. At any time, you can revert the decision to ignore the error by selecting **Revert**.

![Select Ignore to ignore the processing error.](media/sierimage3.png)

You can also search for all documents that had a processing error that was ignored by using the *Ignored processing errors* condition when querying documents in a review set.

![Use the Ignored processing errors condition to search for ignored error documents.](media/sierimage4.png)

## Remediate a document with errors

Sometimes you may be required to remediate a processing error in documents (by removing a password, decrypting an encrypted file, or recovering a corrupted document) and then add the remediated document to the review set. This allows you to review and export the error document together with the other documents in the review set.

To remediate a single document, follow these steps:

1. Select **Download** &gt; **Download original** to download a copy of the file to a local computer.

    ![Download the document with the processing error.](media/sierimage5.png)
2. Remediate the error in the file offline. For encrypted files, that would require decryption software, to remove password protection, either provide the password and save the file or use a password cracker. After you remediate the file, go to the next step.
3. In the review set, select the file with the processing error that you remediated, and then select **Remediation**.

    ![Select Remediation in the banner of the document with processing error.](media/sierimage6.png)
4. Select **Browse**, go to the location of the remediated file on your local computer, and then select the file.

    ![Select Browse and select the remediated file on your local computer.](media/sierimage7.png)

    After selecting the remediated file, it is automatically uploaded to the review set. You can track the processing status of the file.

    ![The status of the remediation process is displayed.](media/sierimage8.png)

    After processing is completed, you can view the remediated document.

    ![You can view the remediated file in the native format in the review set.](media/sierimage9.png)

For more information about what happens when a document is remediated, see [What happens when files are remediated](ediscovery-error-remediation-when-processing-data#what-happens-when-files-are-remediated).

## Search for remediated documents

You can search for all documents in a review set that were remediated by using the **Keywords** condition and specifying the following property:value pair: **IsFromErrorRemediation:true**. This property is also available in the export load file when you export documents from a review set.