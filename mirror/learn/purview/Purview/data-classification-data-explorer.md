---
layout: Conceptual
title: Get started with data explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-data-explorer
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-01-23T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-ga-nochange
search.appverid:
- MOE150
- MET150
description: Data explorer allows you to natively view labeled items.
locale: en-us
document_id: 5fd46e5b-dc9d-9771-2e6e-559ffccdbb8a
document_version_independent_id: 5fd46e5b-dc9d-9771-2e6e-559ffccdbb8a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-data-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-data-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-data-explorer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: d1fc60f5-c0ba-4427-b6c5-f3223d110b3b
---

# Get started with data explorer | Microsoft Learn

Data explorer allows you to natively view the items that were summarized on the overview page.

Document preview and download is disabled if the document is encrypted to mitigate security risks.

## Prerequisites

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

Important

Access to data explorer is highly restricted because it lets you read the contents of scanned files. These permissions supersede permissions that are locally assigned to the items, which allow viewing of the content.

#### Microsoft Entra ID roles to access the data explorer tab

In order to get access to the data explorer tab, an account must be assigned membership in any one of these roles or role groups. Membership in these roles doesn't allow you to view the list of items in content explorer or to view the contents of the items in data explorer.

- Compliance administrator
- Security administrator
- Compliance data administrator
- Global administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

#### Required Microsoft Purview permissions to access items in data explorer

Access to data explorer is configured in the [Microsoft Purview portal](https://purview.microsoft.com/). There are two roles that grant access to data explorer. **Data Explorer List viewer** and **Data Explorer Content viewer**.

These are independent role groups and the permissions they grant aren't cumulative. For example, if you want to grant an account the ability to view the items and their locations only, grant Data Explorer List viewer rights. If you want that same account to also be able to view the contents of the items in the list, grant Data Explorer Content viewer rights as well.

You can also assign either or both of the roles to a custom role group to tailor access to content explorer.

- **Data Explorer List viewer**: Membership in this role group allows you to see each item and its location in list view. The `data classification list viewer` role has been pre-assigned to this role group.
- **Data Explorer Content viewer**: Membership in this role group allows you to view the contents of each item in the list. The `data classification content viewer` role has been pre-assigned to this role group. Additionally, this role is also required to view name of items in list view, which may contain sensitive data.

Note

Data explorer supports administrative units. Members of role groups that have the *data classification list viewer* or *data classification content viewer* role will receive these respective role permissions can be restricted by administrative unit assignments within data explorer. For more on administrative unit support in Purview, see [Administrative units support in Microsoft Purview](/en-us/purview/purview-admin-units).

*Role management* role holders in Microsoft Purview can assign the necessary data explorer list viewer, and data explorer content viewer role group membership.

#### Fine tune Microsoft Purview Roles and Role Groups

There are roles and role groups that you use to fine tune your access controls.

Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

## Data explorer

Data explorer shows a current snapshot of the items that have a sensitivity label, a retention label or have been classified as a sensitive information type in your organization.

### Sensitive information types

A [DLP policy](dlp-learn-about-dlp) can help protect sensitive information, which is defined as a **sensitive information type**. Microsoft 365 includes [definitions for many common sensitive information types](sit-sensitive-information-type-entity-definitions) from across many different regions that are ready for you to use. For example, a credit card number, bank account numbers, and national ID numbers.

### Sensitivity labels

A [sensitivity label](sensitivity-labels) is simply a tag that indicates the value of the item to your organization. It can be applied manually, or automatically. Once applied, the label gets embedded in the document and will follow the document everywhere it goes. A sensitivity label enables various protective behaviors, such as mandatory watermarking or encryption.

Sensitivity labels must be enabled for files that are in SharePoint and OneDrive in order for the corresponding data to surface in the data classification page. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

Encrypted sensitivity labels are not surfaced on content explorer for SharePoint and OneDrive.

### Retention labels

A [retention label](retention) allows you to define how long a labeled item is kept and the steps to be taken prior to deleting it. They're applied manually or automatically via policies. They can play a role in helping your organization stay in compliance with legal and regulatory requirements.

### Trainable Classifiers

A [trainable classifiers](trainable-classifiers-learn-about) allows you to identify sensitive data by using examples of the data you're interested in rather than identifying elements in the item (pattern matching). You can use built-in classifiers or train a classifier with your own content.

### How to use data content explorer

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protectionn** &gt; **Explorers** &gt; **Data explorer**.
2. If you know the name of the label, classifiers or the sensitive information type, you can type that into the filter box.
3. Alternately, you can browse for the item by expanding the type and selecting the type from the list.
4. Select a data source under **Data source** and drill down the folder structure to the item.
5. Double-click to open the item natively in data explorer.

### Export

The **Export** control will create a .csv file that contains a listing of whatever the focus of the pane is.

Note

It can take up to *seven days* for counts to be updated in data content explorer, *fourteen days* for files that are in SharePoint.

### Filter

When you drill down into a location, such as an Exchange or Teams folder, or a SharePoint or OneDrive site, the **Filter** tool appears.

The scope of the search tool is what is displaying in the **All locations** pane and what you can search on varies depending on the selected location.

When **Exchange** or **Teams** is the selected location, you can search on the full email address of the mailbox, for example `user@domainname.com`.

When either **SharePoint** or **OneDrive** are selected location, the search tool will appear when you drill down to site names, folders and files.

You can search on:

| value | example |
| --- | --- |
| full site name | `https://contoso.onmicrosoft.com/sites/sitename` |
| file name | `RES_Resume_1234.txt` |
| text at the beginning of file name | `RES` |
| text after an underscore character ( \_ ) in file name | `Resume` or `1234` |
| file extension | `txt` |