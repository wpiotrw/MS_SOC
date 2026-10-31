---
layout: Conceptual
title: Deploy data lifecycle & records management solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-solution
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-26T00:00:00.0000000Z
audience: Admin
ms.topic: solution-overview
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- m365solution-overview
- m365solution-mig
- m365initiative-compliance
- highpri
search.appverid:
- MOE150
- MET150
description: Prescriptive guidance to deploy Microsoft Purview data lifecycle & records management solutions for compliance and regulatory requirements.
locale: en-us
document_id: 3bf25981-1bc1-3ba9-68e2-c1742b8e26a3
document_version_independent_id: 3bf25981-1bc1-3ba9-68e2-c1742b8e26a3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-solution.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-solution
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-solution.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 01e1860a-2ab8-2891-1c6f-354e25916bbf
---

# Deploy data lifecycle & records management solutions | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use **Microsoft Purview Data Lifecycle Management** and **Microsoft Purview Records Management** to manage compliance or regulatory requirements throughout the lifecycle of your Microsoft 365 data & records.

![Overview of steps to deploy a data governance solution with Microsoft Purview](media/data-governance-solution-overview.png)

For data governance that maps and manages data across your data estate, including multi-cloud, and software-as-a-service (SaaS), use [Microsoft Purview Data Map and Microsoft Purview Unified Catalog](data-governance-get-started).

For a data protection solution, see [Deploy an information protection solution with Microsoft Purview](information-protection-solution).

## Licensing

To understand your licensing requirements and options, see the information from the Microsoft Purview Service Description, [Microsoft Purview Data Lifecycle Management & Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-data-lifecycle--records-management) section for feature-level licensing requirements.

## Keep what you need and delete what you don't

![Steps for data lifecycle management solution](media/data-lifecycle-management-solution.png)

Use **Microsoft Purview Data Lifecycle Management** to keep what you need and delete what you don't.

| Step | Description | More information |
| --- | --- | --- |
| 1 | Understand how retention and deletion works for Microsoft 365 services.  After you understand how you can use retention policies and retention labels, identify your workloads that need a retention policy and whether you need to create retention labels for exceptions. | [Learn about retention policies and retention labels](retention) |
| 2 | Create retention policies and if needed, retention labels for exceptions.  The most commonly used retention policies are for Exchange, SharePoint, Teams, Microsoft 365 Groups, and Viva Engage. You can configure exceptions for documents and emails, and dynamically apply retention labels for risky users.  For exceptional circumstances, you might need to expedite the permanent deletion of sensitive information. | [Create retention policies](create-retention-policies)<br>[Create and apply retention labels for your exceptions](create-retention-labels-data-lifecycle-management)<br><br>[Dynamically mitigate the risk of accidental or malicious deletes](retention#dynamically-mitigate-the-risk-of-accidental-or-malicious-deletes)<br><br>[Expedite the permanent deletion of sensitive information from mailboxes](priority-cleanup) |
| 3 | Manage mailboxes.  Enable mailboxes for archiving and auto-expanding archiving, consider whether you need to customize when emails are moved to the archive mailbox, and make mailboxes inactive when users leave the organization. | [Enable archive mailboxes](enable-archive-mailboxes)<br>[Enable auto-expanding archiving](enable-autoexpanding-archiving)<br><br>[Create and manage inactive mailboxes](create-and-manage-inactive-mailboxes) |
| 4 | Import PST files to online mailboxes.  If you have PST files that contain data you want to oversee, you can import them by using network upload or drive shipping. | [Use network upload to import your organization's PST files](pst-import-network-upload)<br>[Use drive shipping to import your organization's PST files](pst-import-drive-shipping) |

To learn more about the capabilities from this solution, see [Learn about data lifecycle management](data-lifecycle-management).

## Manage high-value items

![Steps for records management solution](media/records-management-solution.png)

Use **Microsoft Purview Records Management** to manage your organization's high-value items for business, legal, or regulatory record-keeping requirements.

| Step | Description | More information |
| --- | --- | --- |
| 1 | Understand the records management solution.  Use retention labels with more flexible configuration options and when required, declare items as records. | [Learn about records management](records-management) |
| 2 | Use file plan to manage your retention schedules.  File plan lets you create retention labels interactively or import in bulk, and export for analysis. Labels that you create with file plan support additional administrative information to help you identify and track business or regulatory requirements. | [Use file plan to create and manage retention labels](file-plan-manager) |
| 3 | Apply your retention labels.  Your retention labels can be published and applied manually or automatically in apps, or automatically applied based on sensitive information, keywords or searchable properties, trainable classifiers, or cloud attachments. | [Publish retention labels and apply them in apps](create-apply-retention-labels)<br>[Apply a retention label to content automatically](apply-retention-labels-automatically) |
| 4 | Manage the permanent deletion of data.  Known as the disposition of data, you can require a manual review of content before it's permanently deleted, and provide proof of disposition for records. | [Manage content disposition](disposition) |

Tip

Check the list of [common scenarios](get-started-with-records-management#common-scenarios) for additional configurations supported by records management.

To learn more about the capabilities from this solution, see [Learn about records management](records-management).

## Training resources

Interactive guides: [Microsoft Purview Purview Data Lifecycle Management and Records Management](https://mslearn.cloudguides.com/guides/Microsoft%20Purview%20Records%20Management)

Learning modules for consultants and admins:

- [Introduction to information protection and data lifecycle management in Microsoft Purview](/en-us/training/modules/m365-compliance-information-governance)
- [Manage the data lifecycle in Microsoft Purview](/en-us/training/modules/m365-compliance-information-govern-information/)
- [Manage records in Microsoft Purview](/en-us/training/modules/m365-compliance-information-manage-records/)

For documentation to support users when these solutions are deployed, see the end user documentation sections for [data lifecycle management](get-started-with-data-lifecycle-management#end-user-documentation) and [records management](get-started-with-records-management#end-user-documentation).