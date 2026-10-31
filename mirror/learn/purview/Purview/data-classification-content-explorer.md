---
layout: Conceptual
title: Get started with content explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-content-explorer
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-10-14T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1030
ai-usage: ai-assisted
search.appverid:
- MOE150
- MET150
description: Content explorer allows you to natively view labeled items.
locale: en-us
document_id: dd941198-e28c-3eee-959d-0c1b37fbde7b
document_version_independent_id: dd941198-e28c-3eee-959d-0c1b37fbde7b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-content-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-content-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-content-explorer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- Azure
- M365
- Power
__autotagging_hash:
- C18106F9C12879AA2F9A5B76FFD7759334FF2739858B06A91D9DE368804409F6
platformId: 25dffdd5-e4d1-e75d-1307-f9f7c8289c38
---

# Get started with content explorer | Microsoft Learn

Content Explorer (classic) lets you natively view the items summarized on the overview page. When a document is encrypted, you can't access the document preview, and download is disabled to mitigate any security risks.

## Prerequisites

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

One set of permissions grants access to the content explorer tab, and a more restrictive set grants access to the items in content explorer.

#### Permissions to access the content explorer tab

To access the content explorer tab, assign an account membership in any one of these Entra ID roles or Purview roles. Membership in these roles doesn't grant permission to view the list of items in content explorer or to view the contents of the items in content explorer.

**Entra ID roles**

- Compliance administrator
- Security administrator
- Compliance data administrator

**Microsoft Purview Roles and Role Groups**

You can use roles and role groups to fine tune your access controls beyond the above guidance. Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](purview-permissions).

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

#### Required permissions to access items in content explorer

Access to content explorer is highly restricted because it lets you read the contents of scanned files. Therefore, you need additional permissions to access content explorer data.

These permissions supersede permissions that are locally assigned to the items, which allow viewing of the content. The roles that grant access to content explorer are:

- **Content Explorer List viewer**: Membership in this role group allows you to see each item and its location in list view. The `data classification list viewer` role is preassigned to this role group.
- **Content Explorer Content viewer**: Membership in this role group allows you to view the contents of each item in the list. The `data classification content viewer` role is preassigned to this role group. Additionally, this role is also required to view name of items in list view, which might contain sensitive data.

The account you use to access content explorer **must be in one or both of the role groups**. These are independent role groups and aren't cumulative. For example, if you want to grant an account the ability to view the items and their locations only, grant Content Explorer List viewer rights. If you want that same account to also be able to view the contents of the items in the list, grant Content Explorer Content viewer rights as well.

You can also assign either or both of the roles to a custom role group to tailor access to content explorer.

*Role management* role holders in Microsoft Purview can assign the necessary Content Explorer List Viewer, and Content Explorer Content Viewer role group membership.

Note

Content Explorer support administrative units. Members of role groups that have the *data classification list viewer* or *data classification content viewer* role receive these respective role permissions can be restricted by administrative unit assignments within content explorer. For more on administrative unit support in Purview, see [Administrative units support in Microsoft Purview](/en-us/purview/purview-admin-units).

## Content explorer

Content explorer shows a current snapshot of the items that have a sensitivity label, a retention label, or are classified as a sensitive information type in your organization.

### Sensitive information types

A [DLP policy](dlp-learn-about-dlp) helps protect sensitive information, which is defined as a **sensitive information type**. Microsoft 365 includes [definitions for many common sensitive information types](sit-sensitive-information-type-entity-definitions) from across many different regions that are ready for you to use. For example, credit card numbers, bank account numbers, and national ID numbers.

### Sensitivity labels

A [sensitivity label](sensitivity-labels) is a tag that indicates the value of the item to your organization. You can apply it manually or automatically. Once applied, the label gets embedded in the document and follows the document everywhere it goes. A sensitivity label enables various protective behaviors, such as mandatory watermarking or encryption.

You must enable sensitivity labels for files in SharePoint and OneDrive for the corresponding data to surface in the data classification page. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

### Retention labels

A [retention label](retention) lets you define how long to keep a labeled item and the steps to take before deleting it. You can apply them manually or automatically through policies. They help your organization stay in compliance with legal and regulatory requirements.

### How to use content explorer

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Explorers** &gt; **Content explorer**.
2. If you know the name of the label or the sensitive information type, type it into the filter box.
3. Alternately, you can browse for the item by expanding the label type and selecting the label from the list.
4. Select a location under **All locations** and drill down the folder structure to the item.
5. Double-click to open the item natively in content explorer.

### Export

The **export** control creates a .csv file that contains a listing of whatever the focus of the pane is.

Note

It can take up to *seven days* for counts to update in content explorer and *14 days* for files that are in SharePoint.

### Filter

When you drill down into a location, such as an Exchange or Teams folder, or a SharePoint or OneDrive site, the **Filter** tool appears.

The scope of the search tool is what displays in the **All locations** pane. What you can search on varies depending on the selected location.

When you select **Exchange** or **Teams**, you can search on the full email address of the mailbox, for example `user@domainname.com`.

When you select **SharePoint** or **OneDrive**, you can search on site names, folders, and files.

You can search on:

| Value | Example |
| --- | --- |
| Full site name | `https://contoso.onmicrosoft.com/sites/sitename` |
| File name | `RES_Resume_1234.txt` |
| Text at the beginning of file name | `RES` |
| Text after an underscore character ( \_ ) in file name | `Resume` or `1234` |
| File extension | `txt` |

### Save views in Content Explorer

You can create customized views in content explorer, by configuring what SITs, Sensitivity Labels, Trainable Classifiers, and Retention Labels which are important for you. A view can be made default, to quickly load the view next time content explorer is opened.

## Provide match or not a match accuracy feedback in content explorer

In **Content explorer**, you can see how many matches a sensitive information type (SIT) or trainable classifier has. You can also give feedback on whether an item is actually a match by using the **Match** and **Not a Match** feedback options. Use this feedback to improve your classifiers. For more information, see [Increase classifier accuracy](data-classification-increase-accuracy).

Note

Updating a custom sensitive information type (SIT) definition doesn't by itself reclassify unchanged historical files. For SharePoint and OneDrive files that need updated classification, use [on-demand classification](on-demand-classification), and review its scope, costs, and active-policy effects first. A file's last-modified date alone doesn't establish when it was classified. For the distinction between classification results and auto-labeling policy matches, see [Auto-labeling classification and simulation concepts](auto-label-classification-simulation).

## Email attachment preview

For Exchange items, content explorer supports the preview of email attachments without the need to download the email. The following email attachment file types are supported: `.doc, .docx, .xlsx, .xls, .xlsm, .xlsb, .pptx, .pdf, .txt, .csv, .html, .xml, .json, .rtf, .cpp, .cs, .py, .jpg, .png, .jpeg, and .eml`

Content explorer document preview supports Excel files up to 25 MB.