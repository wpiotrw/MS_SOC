---
layout: Conceptual
title: Set up Information Rights Management (IRM) in SharePoint admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/set-up-irm-in-sp-admin-center
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-04-22T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- SPO160
- MET150
description: Learn how to use SharePoint IRM through Azure Rights Management Services (RMS) to protect SharePoint lists and document libraries.
ms.collection:
- purview-compliance
- SPO_Content
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
locale: en-us
document_id: 6f520b89-4cfc-bded-9929-4a68b77a0e3a
document_version_independent_id: 6f520b89-4cfc-bded-9929-4a68b77a0e3a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/set-up-irm-in-sp-admin-center.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: set-up-irm-in-sp-admin-center
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/set-up-irm-in-sp-admin-center.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: afa053d7-f03e-c6ec-c1a9-b3ec3fe5c7c5
---

# Set up Information Rights Management (IRM) in SharePoint admin center | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Within SharePoint in Microsoft 365, IRM protection is applied to files at the list and library level. Before your organization can use IRM protection, you must first set up Rights Management. IRM relies on the Azure Rights Management service from Azure Information Protection to encrypt and assign usage restrictions. Some Microsoft 365 plans include Azure Rights Management, but not all.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Turn on IRM service using SharePoint admin center

Before your organization can IRM-protect SharePoint lists and libraries, you must first activate the Rights Management service for your organization. To learn how, see [Activating Azure Rights Management](/en-us/information-protection/deploy-use/activate-service).

After you activate the Rights Management service, sign in to the SharePoint admin center to turn on IRM.

1. Sign in to SharePoint using a work or school account that has site owner or SharePoint administrator permissions.
2. Select the app launcher icon ![The app launcher icon in Office 365.](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, your work or school account doesn't have administrator permissions in your organization.)
3. In the left pane, choose **Admin centers** &gt; [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219).
4. In the left pane, choose **settings**, and then choose **classic settings page**.
5. In the **Information Rights Management (IRM)** section, choose **Use the IRM service specified in your configuration**, and then choose **Refresh IRM Settings**. After you refresh IRM settings, people in your organization can begin using IRM in their SharePoint lists and document libraries. However, the options to do so might take up to an hour to appear in Library Settings and List Settings.

## IRM-enable SharePoint document libraries and lists

After IRM settings refresh, site owners can IRM-protect their SharePoint lists and document libraries. For more information, see [Apply Information Rights Management to a list or library](apply-irm-to-a-list-or-library).

When site owners enable IRM for a list or library, they can protect any supported file types in that list or library. When IRM is enabled for a library, rights management applies to all of the files in that library. When you enable IRM for a list, rights management applies only to files that are attached to list items, not the actual list items.

When people download files in an IRM-enabled list or library, the files are encrypted so that only authorized people can view them. Each rights-managed file also contains an issuance license that imposes restrictions on the people who view the file. Typical restrictions include:

- Making a file read-only
- Disabling the copying of text
- Preventing people from saving a local copy
- Preventing people from printing the file

Client programs that can read IRM-supported file types use the issuance license within the rights-managed file to enforce these restrictions. So, a rights-managed file retains its protection even after download. To enable IRM on a list or library, see [Apply Information Rights Management to a list or library](apply-irm-to-a-list-or-library).

You can't create or edit documents in an IRM-enabled library using Office in a browser. Instead, one person at a time can download and edit IRM-encrypted files. Use check-in and check-out to manage *coauthor*, or authoring across multiple users.

When you download a PDF file from an IRM-protected library, Microsoft 365 creates a protected PDF file. The file's extension doesn't change, but the file is protected. To view this file, you need the information protection viewer, the full information protection client, or another application that supports viewing protected PDF files.

SharePoint supports encryption of the following file types:

- PDF
- The 97-2003 file formats for the following Microsoft Office programs: Word, Excel, and PowerPoint
- The Office Open XML formats for the following Microsoft Office programs: Word, Excel, and PowerPoint
- The XML Paper Specification (XPS) format

Note

IRM protection can't be applied to protected documents (like digitally signed PDF files) as SharePoint needs to open the document on upload.