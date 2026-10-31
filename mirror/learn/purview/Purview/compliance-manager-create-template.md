---
layout: Conceptual
title: Creating regulation templates in Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-create-template
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-12-03T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
- tier1
search.appverid:
- MOE150
- MET150
description: Create a regulation template in Microsoft Purview Compliance Manager.
locale: en-us
document_id: 1b0dd573-a51b-02fc-2cb0-d9d9414e7eee
document_version_independent_id: 1b0dd573-a51b-02fc-2cb0-d9d9414e7eee
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-create-template.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-create-template
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-create-template.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: 4d6620cb-1424-b72e-1197-5d2f0cd94ada
---

# Creating regulation templates in Compliance Manager | Microsoft Learn

Compliance Manager helps organizations manage regulatory requirements by providing ready-to-use templates. For organizations with unique compliance needs, you can create custom regulation templates using one of two methods:

- Upload a regulation in PDF format
- Start from a blank template

These options allow flexibility for organizations that need to comply with official standards or define custom internal regulations.

To learn more about regulations, see [Learn about regulations in Compliance Manager](compliance-manager-regulations). To see a list of available regulations, see [Compliance Manager regulations list](compliance-manager-regulations-list).

## How It Works

The process starts when the admin uploads a regulatory PDF file. The system analyzes the document for malware, extracts controls and maps controls to existing improvement actions. Any detected errors are displayed for correction. The admin can then update existing controls, add new ones, and manually map actions to controls. Once all adjustments are complete, the draft template is published for use in Compliance Manager.

## Requirements

- A user must hold a role of Compliance Manager Administration or Compliance Manager Assessor. Learn more about [roles and permissions](compliance-manager-setup).
- For PDF upload:
    - A regulation document published by an official regulator or standards body.
    - PDF format only.

## Create a new template based on regulation document (PDF)

1. From your **Regulations** page, select **Create new template**.
2. Select **Upload PDF document**.
3. Modify template name as needed.
4. Optionally, enter overarching regulation name if you want to group multiple templates.
5. Select applicable services.
6. Select **Scan and extract**.

    The system scans, extracts, and maps controls. This process may take several minutes to complete. When the process is complete, you see the results of the scan including malware found, controls extracted, and controls mapped.
7. When the scan is complete, select **Review draft template**.
8. Review the draft template. Add, remove, or edit the controls as needed. When you're satisfied, select **Publish template**.
9. Confirm template details and optionally provide notes, and then select **Publish template**.

The template is published and you can now create an assessment based on your new template.

## Create a blank template

1. From your **Regulations** page, select **Create new template**.
2. Select **Create blank template**.
3. Enter a template name.
4. Enter overarching regulation name.
5. Select applicable services.
6. Select **Create draft template**.
7. Manually add controls to your template. Select **Create control**.
8. In the **Create control** dialog, complete each field and then select **Create**.
9. Manually assign improvement actions to your control. Select one of the following:
    - **Import actions** - select from a list of available actions.
    - **Create action** - define your action.
10. Add as many controls and actions as needed. When you're finish, select **Publish template**.
11. Confirm template details and optionally provide notes, and then select **Publish template**.

The template is published and you can now create an assessment based on your new template.