---
layout: FAQ
title: Sensitivity labels in Microsoft Purview Data Map FAQ (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq
summary: >
  <p>This article lists frequently asked questions about sensitivity labeling in the Microsoft Purview Data Map, with their answers and links to more information.</br></br></p>

  <blockquote>

  </blockquote>

  <div class="IMPORTANT">

  <p>Important</p>

  <p>Labeling in the Microsoft Purview Data Map is currently in preview. The <a href="https://azure.microsoft.com/support/legal/preview-supplemental-terms/">Supplemental Terms of Use for Microsoft Azure Previews</a> include other legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.</p>

  </div>
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about frequently asked questions for Microsoft Purview Data Map sensitivity labels.
services: purview
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.service: purview
ms.subservice: purview-data-governance
ms.topic: faq
ms.date: 2025-07-09T00:00:00.0000000Z
ms.custom: sfi-ga-flagged
locale: en-us
document_id: 221ad067-d2b1-e5bd-faf4-ef300c5ed371
document_version_independent_id: 221ad067-d2b1-e5bd-faf4-ef300c5ed371
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-sensitivity-labels-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-sensitivity-labels-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-sensitivity-labels-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 103cf34a-b33b-6742-0d46-affa1bb1d2de
---

# Sensitivity labels in Microsoft Purview Data Map FAQ (preview) | Microsoft Learn

This article lists frequently asked questions about sensitivity labeling in the Microsoft Purview Data Map, with their answers and links to more information.

Important

Labeling in the Microsoft Purview Data Map is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include other legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

## Licensing and setup

### What are the licensing requirements to apply sensitivity labels in Microsoft Purview Data Map?

To use sensitivity labels in the Microsoft Purview Data Map, you'll need at least one Microsoft 365 license/account within the same Microsoft Entra tenant as your Microsoft Purview account.

The following Microsoft 365 licenses are required to automatically apply sensitivity labels to your assets in [Microsoft 365](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#which-licenses-provide-the-rights-for-a-user-to-benefit-from-the-service) and [the Microsoft Purview Data Map](data-map-sensitivity-labels-apply):

- Microsoft 365 E5/A5/G5
- Microsoft 365 E5/A5/G5 Compliance
- Microsoft 365 E5/A5/G5 Information Protection, and Governance
- Office 365 E5, Enterprise Mobility + Security E5/A5/G5, and AIP Plan 2

For more information, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection).

To use auto-labeling and protection policies for non-Microsoft 365 data sources, 1 Microsoft 365 E5 licenses and set up of pay as you go billing model will be required. To understand pay as you go billing by assets protected, see the [pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model). For information about the specific licenses required, see this [information on sensitivity labels](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling). Microsoft 365 E5 trial licenses can be attained for your tenant by navigating [here](https://signup.microsoft.com/signup?ShowInternalOffers=true&amp;OfferId=f6f20264-e785-4749-bd8e-884bab076de4) from your environment.

### How are sensitivity labels applied to non-Microsoft 365 locations?

You can [create and apply autolabeling policies](data-map-sensitivity-labels-apply) to detect Microsoft out-of-the-box classifiers to specific or all data assets that are registered in Data Map for supported locations.

- Sensitivity labels are applied only to the asset metadata in Data Map and aren't applied to the actual files and database columns. These sensitivity labels don't modify your files and databases in any way.

## Classifications vs sensitivity labels

### What is the difference between classifications and sensitivity labels?

The following table lists the differences between classifications and sensitivity labels:

| Comparison | Classifications | Sensitivity labels |
| --- | --- | --- |
| **Definition** | Classifications are regular expressions or patterns that can help identify data types that exist inside an asset. | Sensitivity labels are tags that allow organizations to categorize data based on business impact, while abstracting the type of data from the user. |
| **Examples** | Social Security Number, Drive license number, Bank account number, etc. | Highly confidential, Confidential, General, Public, etc. |
| **Scope** | The scope of classifications applied to an asset is limited to the Microsoft Purview Data Map where the classifications were applied. If the data moves to an asset managed by another Microsoft Purview Data Map, classifications applied in the original location aren't visible in the new location. | Sensitivity labels applied on an asset travel with the data no matter where the data goes. For example, this means that sensitivity labels applied to a file in Microsoft Purview Information Protection are automatically visible and remain applied to the file, even if it moves to Azure, SharePoint, or Teams. |
| **Scan Process** | Scanning an asset in the Microsoft Purview Data Map looks for both system-defined and user-defined (custom) classifications in your data. If found, classifications are added in the Microsoft Purview map for the scanned asset. | If you have an auto-labeling policy for Azure Storage or Azure SQL, scanning an asset in the Microsoft Purview Data Map applies the labels to assets in the catalog based on the out-of-the-box classifications found in the scan and defined in the auto-labeling policy. |
| **Authoring environment** | Custom classifications and classification rules can be created in the Microsoft Purview Data Map. You can also create custom classifications in Microsoft Purview Information Protection. However, we don't yet support importing them to the Microsoft Purview Data Map. | Manage auto-labeling of sensitivity labels in Microsoft Purview using the [Microsoft Purview Information Protection](create-sensitivity-labels). |
| **Assignment Limits** | Assets can have no classifications, or one or more classifications assigned. | Each asset/ database column can have only one sensitivity label. |
| **Asset application workflow** | You can use Microsoft Purview Unified Catalog to manually add or modify classifications that are assigned to an asset. | In the Microsoft Purview Data Map, sensitivity labels are automatically assigned to assets based on classifications found. Applying labels manually in the Microsoft Purview Data Map isn't currently supported. |
| **More Information** | [Learn more about classifications](data-map-classification-custom). | [Learn more about sensitivity labels](create-sensitivity-labels). |
|  |  |  |

### Are classifications and Sensitive Information Types (SITs) the same thing?

While classifications and SITs are fundamentally the same things, classifications are a Microsoft Purview Data Map concept and SITs are a Microsoft Purview Information Protection concept. Both classifications and SITs are used by their respective services to identify the type of data found in an asset.

## Labeling capabilities in the Microsoft Purview Data Map

### Which data sources can I apply sensitivity labels to in the Microsoft Purview Data Map?

You can apply sensitivity labels to all the data sources listed under [Supported data sources for sensitivity labels in the Microsoft Purview Data Map](data-map-sensitivity-labels#supported-data-sources).

### Which file types can I apply sensitivity labels to in the Microsoft Purview Data Map?

You can apply sensitivity labels to all [Microsoft Purview Data Map supported file types](data-map-data-sources).

### Can I use my custom Sensitive Information Type (SIT) in Microsoft Purview Information Protection for schematized data assets?

No, [custom sensitive information types](sensitive-information-type-learn-about#creating-custom-sensitive-information-types) aren't supported in the Microsoft Purview Data Map at this time. The Microsoft Purview Data Map currently only supports Microsoft Purview Information Protection [built-in sensitive information types](sensitive-information-type-learn-about).

### Can I use the advanced classifiers from Microsoft Purview Information Protection in the Microsoft Purview Data Map?

No, advanced classifiers aren't currently supported in the Microsoft Purview Data Map and won't appear.

### Can autolabeling for Purview Data Map apply to assets that might include credential content?

Data Map currently doesn't support scanning for credentials. When Data Map supports scanning for credentials, you should be able to apply labels based on credentials found.

### Can I manually label an asset, or manually modify or remove a label in the Microsoft Purview Data Map?

The Microsoft Purview Data Map supports auto-labeling only. Labels are automatically applied to assets in the data map based on autolabeling policy configuration.

The Data Map doesn't currently support manually applying a label, modifying, or removing a label from an asset. However, when you apply a label on an office document and then scan it into Data Map, the label will be applied to the data asset. While the label is applied to the actual file in Microsoft Purview Information Protection, it's only added as metadata in Data Map. While there are differences in how a label is applied to an asset across various services/applications, labels travel with the data and are recognized by all the services you extend it to.

### Can I apply encryption and/or content marking to files in the Microsoft Purview Data Map, as I can for Office documents and emails?

No, although the sensitivity label might be configured for these protection actions, we don't currently support encryption and content marking for files in the Microsoft Purview Data Map. We only support protection actions that are configured in protection policies.

### Does the Microsoft Purview Data Map support data loss prevention?

No, Data Map doesn't currently provide data loss prevention (DLP) capabilities. [Data Loss Prevention](information-protection#prevent-data-loss) is currently supported only for Microsoft 365 apps and services, including Fabric.

## Access and roles

### Where can I manage my autolabeling policies for labeling beyond Microsoft 365?

Sensitivity labels and autolabeling policies are managed in Microsoft Purview Information Protection. For more information, see [How to create sensitivity labels in Microsoft Purview Information Protection](data-map-sensitivity-labels-apply).

### Who can manage sensitivity labels?

The following built-in admin roles include permissions to manage sensitivity labels (most to least permissive):

- Global Administrator
- Compliance Administrator
- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

For more information, see [Permissions required to create and manage sensitivity labels](get-started-with-sensitivity-labels#permissions-required-to-create-and-manage-sensitivity-labels). After you have compliance and global administrators configured, those administrators can [give access to individual users](/en-us/microsoft-365/security/office-365-security/grant-access-to-the-security-and-compliance-center).

Note

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

### Who can search and browse assets with sensitivity labels in Microsoft Purview Unified Catalog?

All users with at least data reader access to the Microsoft Purview Data Map have permissions to search and browse assets with sensitivity labels in Unified Catalog.

### Who can view the sensitivity label insights report in Microsoft Purview Data Estate Insights?

All users with the [insights reader role](data-gov-classic-permissions#roles) and at least [data reader](data-gov-classic-permissions#roles) permissions on applicable collections will have permissions to view sensitivity label insights reports in Microsoft Purview Data Estate Insights.

## Technical details

### Does the Microsoft Purview Data Map scan an entire asset when applying autolabeling policies to the database columns?

The Microsoft Purview scanner samples the data. For more information, see [sampling data for classification and autolabeling](data-map-data-sources#sampling-data-for-classification).

### If there are multiple sensitivity labels that meet the classification criteria, which label is applied?

Sensitivity labels have a priority 'order' and the Microsoft Purview Data Map uses this order to assign labels. If there are multiple labels meeting the classification criteria, the Microsoft Purview Data Map selects the label with the highest order.

For more information, see [Label priority order matters](sensitivity-labels#label-priority-order-matters).

## SQL data discovery and classification

### Why does Microsoft support two classification experiences for SQL databases, Microsoft Purview and SQL data discovery and classification?

Microsoft Purview provides a classification and labeling experience for all your Azure assets including SQL databases. Microsoft Purview is intended for organizations that want to manage their entire data estate in a single place with the power of classification, labeling, alerting, and more. Microsoft Purview uses sensitivity labels, which have a global scope and travel with your data no matter where it moves to or what it transforms into.

In contrast, [SQL data discovery and classification](/en-us/azure/azure-sql/database/data-discovery-and-classification-overview) is built into SQL. SQL data discovery and classification existed before Microsoft Purview as a way to provide basic capabilities for discovering, classifying, labeling, and reporting the sensitive data in your SQL databases. SQL data discovery and classification use local labels that don't have a global scope and don't support sensitivity labels.

### I applied labels in SQL data discovery and classification. Why are these labels not showing up on my asset in Microsoft Purview?

SQL classification uses local labels, while Microsoft Purview uses sensitivity labels. Labels applied in the SQL classification experience won't show up in Microsoft Purview. For more information, see [Labeling for SQL databases](data-map-sensitivity-labels#labeling-for-sql-databases).

For more information, see: