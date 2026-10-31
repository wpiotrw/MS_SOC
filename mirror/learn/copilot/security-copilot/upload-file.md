---
layout: Conceptual
title: Upload a file | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/upload-file
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to upload files to Microsoft Security Copilot so that it can reference your organization's knowledge base content in prompt responses.
ms.date: 2025-10-24T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 4f431b2c-7243-f9c9-62ea-9d7323653dc2
document_version_independent_id: 4f431b2c-7243-f9c9-62ea-9d7323653dc2
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/upload-file.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: upload-file
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/upload-file.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 33aeace0-69ea-dccb-6aff-153f8ac514ec
---

# Upload a file | Microsoft Learn

Important

Some information in this article relates to a prereleased product which might be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

You can upload a file in Microsoft Security Copilot to allow Copilot to refer to the contents of the file for responses when you prompt Copilot and mention your "uploaded files."

Examples of files you can upload are your organization’s policy and compliance documents, investigation and response procedures, and templates. Integrating this wealth of knowledge into Copilot allows Copilot to reason over the knowledge base or documents and generate responses that are more relevant, specific, and customized to your operational needs.

Note

The file upload feature in Copilot doesn't support use cases such as evaluation or detonation of malicious files today.

## Upload a file to Security Copilot

1. Check that the file you're about to upload is a common text file type like DOCX, MD, PDF, and TXT formats, and that each file doesn't exceed 3 MB. You can upload files up to 20 MB in total.
2. In the Copilot home page, select the sources icon ![Screenshot of sources icon.](media/sources-icon.png) in the prompt bar to open the **Manage sources** page.
3. Select **Files** to open the file upload section.

    [![Screenshot of the file upload dialog box.](media/copilot-security-upload-files.png)](media/copilot-security-upload-files.png#lightbox)
4. Select **Upload file** to look for your file.
5. Wait for the file to appear in **Uploads**. If an error message appears, correct the problem and try again.
6. To include the file as a source in your current session, toggle the button beside the file until the toggle is on the right (lit up). If you aren't going to use the file yet, or exclude the file as a source in your current session, keep the toggle button untoggled. (Toggle is on the left, in grey.)
7. To prompt using the uploaded file, read [Prompting for an uploaded file](connect-org-kb#prompting-for-an-uploaded-file).

## Storage and availability

Uploaded files are always stored in the home Geo of the tenant. Uploaded files are stored in the Security Copilot service, not inside your Microsoft tenant boundary.

Uploaded files are only available to the user account that uploaded them, and not available to other users within or outside the tenant.

To learn more about how Security Copilot handles Customer Data, read [Privacy and data security in Security Copilot](privacy-data-security#customer-data-storage-location).

## Delete an uploaded file

To delete the file, select the trash icon next to the file name in **Manage sources &gt; Files &gt; Uploads**.

## Restrict file upload (for owners)

Owners can choose who are allowed to upload files in owner settings. The options are:

- No one can upload files
- Contributors and Owners can upload files

By default, file upload is available for all users (Contributors and Owners).

[![Screenshot of files upload dialog box.](media/copilot-security-upload-file-owner.png)](media/copilot-security-upload-file-owner.png#lightbox)