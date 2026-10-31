---
layout: Conceptual
title: Learn about Microsoft Purview Data Lifecycle Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-lifecycle-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-05-06T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- highpri
- SPO_Content
description: Learn how Microsoft Purview Data Lifecycle Management helps you keep what you need and delete what you don't.
locale: en-us
document_id: 06574876-3297-0f0b-ecdd-c4e455019b70
document_version_independent_id: 06574876-3297-0f0b-ecdd-c4e455019b70
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-lifecycle-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-lifecycle-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-lifecycle-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 59c55d3b-ddd6-a4f6-3a61-b65661f87d58
---

# Learn about Microsoft Purview Data Lifecycle Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Microsoft Purview Data Lifecycle Management (formerly Microsoft Information Governance) provides you with tools and capabilities to retain the content that you need to keep, and delete the content that you don't.

Retaining and deleting content is often needed for compliance and regulatory requirement, but deleting content that no longer has business value also helps you manage risk and liability. For example, it reduces your attack surface.

## Microsoft 365 features

**Retention policies** are the cornerstone for data lifecycle management. Use these policies for Microsoft 365 workloads that include Exchange, SharePoint, OneDrive, Teams, and Viva Engage. Configure whether content for these services needs to be retained indefinitely, or for a specific period if users edit or delete it. Or you can configure the policy to automatically permanently delete the content after a specified period if it's not already deleted. You can also combine these two actions for retain and then delete, which is a very typical configuration. For example, retain email for three years and then delete it.

When you configure a retention policy, you can target all instances in your organization (such as all mailboxes and all SharePoint sites), or individual instances (such as only the mailboxes for specific departments or regions, or just selected SharePoint sites).

If you need exceptions for individual emails or documents, such as a longer retention period for legal documents, you do this with **retention labels** that you publish to apps so that users can apply them, or automatically apply them by inspecting the content.

Retention labels are also used with **Adaptive Protection**, if you're using [this solution with insider risk management](insider-risk-management-adaptive-protection). In this case, the retention label and auto-apply policy is automatically created for you. For details, see [Dynamically mitigate the risk of accidental or malicious deletes](retention#dynamically-mitigate-the-risk-of-accidental-or-malicious-deletes).

Under the covers, retention labels are also used with [priority cleanup](priority-cleanup) for scenarios where you need to expedite the permanent deletion of sensitive information from mailboxes, even if they have existing holds for retention or eDiscovery.

For more information about retention policies and retention labels, and how retention works in Microsoft 365, see [Learn about retention policies and retention labels](retention).

Note

If you need to manage high-value items for business, legal, or regulatory record-keeping requirements, use retention labels with [records management](records-management) rather than retention labels with data lifecycle management.

Other data lifecycle management capabilities to help you keep what you need and delete what you don't:

- **Mailbox archiving** to provide users with additional mailbox storage space, and auto-expanding archiving for mailboxes that need more than 100 GB storage. A default archiving policy automatically moves email to the archive mailbox, and if required, you can customize this policy. For more information about mailbox archiving, see [Learn about archive mailboxes](archive-mailboxes).
- **Inactive mailboxes** that retain mailbox content after employees leave the organization. For more information about inactive mailboxes, see [Learn about inactive mailboxes](inactive-mailboxes-in-office-365).
- **Import service for PST files** by using network upload or drive shipping. For more information, see [Learn about importing your organization's PST files](pst-import-overview).

## Exchange (legacy) features

**Retention policies and retention tags** from messaging records management (MRM), and **journaling rules** are older compliance features from Exchange that were originally configurable from the Classic Exchange admin center. They haven't been brought forward to the [new Exchange admin center](/en-us/exchange/features-in-new-eac).

If you're not already using these features, or have a specific business requirement to use them instead of the Microsoft 365 features for data lifecycle management, we don't recommend you use these older compliance features. Instead, use the newer Microsoft 365 features that retain data in place and support policies across other Microsoft 365 services.

For more information, see [Use retention policies and retention labels instead of older features](retention#use-retention-policies-and-retention-labels-instead-of-older-features).

## Deployment guidance

For deployment guidance for data lifecycle management that includes a recommended deployment roadmap, licensing information, permissions, a list of supported scenarios, and end-user documentation, see [Get started with data lifecycle management](get-started-with-data-lifecycle-management).

Looking for deployment guidance to protect your data? See [Deploy an information protection solution with Microsoft Purview](information-protection-solution).