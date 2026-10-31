---
layout: Conceptual
title: Create retention labels for exceptions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/create-retention-labels-data-lifecycle-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-12-03T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Instructions to create retention labels for exceptions to retention policies for data lifecycle management so you can retain what you need and delete what you don't.
locale: en-us
document_id: d987ce79-c10e-5c69-f06f-6652dc3bb01d
document_version_independent_id: d987ce79-c10e-5c69-f06f-6652dc3bb01d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/create-retention-labels-data-lifecycle-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: create-retention-labels-data-lifecycle-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/create-retention-labels-data-lifecycle-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b2e8a11b-47c5-549f-7b3d-5b7a23cada06
---

# Create retention labels for exceptions | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

As part of your data governance strategy to retain what you need and delete what you don't, you might need to create a few retention labels for items that need exceptions to your retention policies.

Whereas retention policies automatically apply to all items at the container level (such as SharePoint sites, user mailboxes, and so on), retention labels apply to individual items, such as a SharePoint document or an email message.

Make sure you understand the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) before you use retention labels to supplement a retention policy for specific SharePoint, OneDrive, or Exchange items. Typically, you'll use retention labels to retain specific items longer than an applied retention policy, but they can also be used to override automatic deletion at the end of the retention period, or apply a different deletion period.

As a typical example: The majority of content on your SharePoint sites need to be retained for three years, which is covered with a retention policy. But you have some contract documents that must be retained for seven years. These exceptions can be addressed with retention labels. After assigning the retention policy to all SharePoint sites, you apply the retention labels to the contract documents. All SharePoint items will be retained for three years, and just the contract documents will be retained for seven years.

For more examples of how retention labels can be used as exceptions to retention policies, see [Combining retention policies and retention labels](retention#combining-retention-policies-and-retention-labels).

Retention labels also support more capabilities than retention policies. For more information, see [Compare capabilities for retention policies and retention labels](retention#compare-capabilities-for-retention-policies-and-retention-labels).

Use the following information to help you create retention labels to supplement retention policies as part of your data lifecycle management strategy.

Note

Create retention labels from the **Records management** solution rather than **Data lifecycle management** if you need to use retention labels to manage high-value items for business, legal, or regulatory record-keeping requirements. For example, you want to use event-based retention or disposition review. For instructions, see [Use file plan to create and manage retention labels](file-plan-manager).

## Before you begin

To make sure you have permissions to create and edit retention labels and their policies, see [Permissions for retention policies and retention labels](get-started-with-data-lifecycle-management#permissions-for-retention-policies-and-retention-labels).

## How to create retention labels for data lifecycle management

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Retention labels**.
2. Select **Create a label** and follow the prompts to create the retention label. Be careful what name you choose, because this can't be changed after the label is saved.

    Note

    Retention label names can't contain characters that match this regular expression:

    ```text
    [""#\$%\*\\\&\?\,\;\:\<\>\|\!\'\(\)\[\]\{\}\^`~]+
    ```

    For more information about the retention settings, see [Settings for retaining and deleting content](retention-settings#settings-for-retaining-and-deleting-content).
3. After you have created the label and you see the options to publish the label, auto-apply the label, or just save the label: Select **Just save the label for now**, and then select **Done**.
4. Repeat these steps to create any more retention labels that you need for different retention settings.

To edit an existing label, select it, and then select the **Edit label** option to start the Edit retention label configuration that lets you change the label descriptions and any eligible settings.

Most settings can't be changed after the label is created and saved, which include the label name, and the retention settings except the retention period.