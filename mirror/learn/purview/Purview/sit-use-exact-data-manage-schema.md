---
layout: Conceptual
title: Manage your exact data match schema | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-use-exact-data-manage-schema
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-22T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Edit or delete an exact data match schema used by Microsoft Purview to support exact data match classification. Follow the required management steps before updating related data sets or rules.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: a5344a37-3c2b-f87a-3e5b-1538775085ad
document_version_independent_id: a5344a37-3c2b-f87a-3e5b-1538775085ad
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-use-exact-data-manage-schema.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-use-exact-data-manage-schema
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-use-exact-data-manage-schema.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 88e142ee-2e74-6604-e38e-882cc5e15cb1
---

# Manage your exact data match schema | Microsoft Learn

## Editing the schema for EDM-based classification manually

If you want to make changes to your EDM schema, for example the **edm.xml** file, such as changing which fields are used for EDM-based classification, follow these steps:

Tip

You can change your EDM schema and sensitive information table source file to take advantage of **configurable match**. When configured, EDM will ignore case differences and some delimiters when it evaluates an item. This makes defining your xml schema and your sensitive data files easier. To learn more see, [Using the caseInsensitive and ignoredDelimiters fields](sit-get-started-exact-data-match-create-schema#using-the-caseinsensitive-and-ignoreddelimiters-fields).

1. Edit your **edm.xml** file (this file is discussed in the [Create the schema for exact data match based sensitive information types](sit-get-started-exact-data-match-create-schema#create-the-schema-for-exact-data-match-based-sensitive-information-types).
2. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
3. To update your database schema, run the following command:

    ```powershell
    Set-DlpEdmSchema -FileData ([System.IO.File]::ReadAllBytes('.\\edm.xml')) -Confirm:$true
    ```

    You're prompted to confirm as follows:

> 
> Confirm
> 
> Are you sure you want to perform this action?
> 
> EDM Schema for the data store 'patientrecords' will be updated.
> 
> [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):

    Tip

    If you want your changes to occur without confirmation, don't use `-Confirm:$true` in Step 3.

    Note

    It can take between 10-60 minutes to update the EDMSchema with additions. The update must complete before you execute steps that use the additions.

## Removing the schema for EDM-based classification manually

If you want to remove the schema you're using for EDM-based classification, follow these steps:

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run the following command, substituting the data store name of "patient records" with the one you want to remove (using the patientrecords store as an example):

    ```powershell
    Remove-DlpEdmSchema -Identity 'patientrecords'
    ```

    You're prompted to confirm the following message:

> 
> Confirm
> 
> Are you sure you want to perform this action?
> 
> EDM Schema for the data store 'patientrecords' will be removed.
> 
> [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):

    Tip

    If you want the schema removal to occur without confirmation, omit the `-Confirm:$true` parameter from the `Remove-DlpEdmSchema` command.

### Edit or delete the EDM schema with the wizard

To edit or delete an EDM schema by using the wizard, follow these steps:

1. Open **Compliance center** &gt; **Data classification** &gt; **Classifiers**.
2. Choose **EDM classifiers**.
3. Double-click on the EDM SIT you want to edit.
4. Choose **Edit EDM sensitive info type** or **Delete EDM sensitive info type** from the flyout.
5. Follow the steps in the wizard to complete your edits or to delete the classifier.

Important

If you want to remove a schema, and it is already associated with an EDM sensitive info type, you must first delete the EDM sensitive info type, then you can delete the schema.