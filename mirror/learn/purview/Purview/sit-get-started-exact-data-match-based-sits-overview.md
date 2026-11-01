---
layout: Conceptual
title: Get Started with EDM SITs in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview
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
- highpri
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Understand exact data match classifiers and compare the new and classic creation experiences in Microsoft Purview. See permissions, licensing, and supported regions.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 4f4ba8c3-a9f7-ff60-ef87-44be6112e833
document_version_independent_id: 4f4ba8c3-a9f7-ff60-ef87-44be6112e833
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-based-sits-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-based-sits-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-based-sits-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9e015556-1fb6-9c1c-2995-b92f370cae2b
---

# Get Started with EDM SITs in Microsoft Purview | Microsoft Learn

Creating an exact data match (EDM) sensitive information type (SIT) and making it available is a multiphase process. You can use the *new experience*, *classic experience*, or PowerShell. This article helps Microsoft Purview administrators compare the new and classic experiences and choose the right one for their needs. Before you begin, review the supported regions and required licenses and permissions.

## Applies to:

- [Create EDM SIT using the new experience](sit-create-edm-sit-unified-ux-workflow)
- [Create EDM SIT using the classic experience](sit-create-edm-sit-classic-ux-workflow)

EDM SITs can be used in:

- Microsoft Purview Data Loss Prevention
- Auto-labeling (service and client side)
- Microsoft Purview Insider Risk Management
- Microsoft Purview eDiscovery
- Microsoft Defender for Cloud Apps

## Before you begin

Familiarize yourself with the concepts and terminology in these articles:

- [Learn about sensitive information types](sit-sensitive-information-type-learn-about)
- [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits)

## Supported regions

The exact data match feature is available in these regions:

- Asia Pacific
- Australia
- Brazil
- Canada
- Europe
- France
- Germany
- India
- Japan
- Korea
- Norway
- Qatar
- South Africa
- Switzerland
- United Arab Emirates
- United Kingdom
- United States
- US Department of Defense (DoD)
- US Government Community Cloud (GCC)
- US Government Community Cloud High (GCC High)

To find out where your tenant is hosting data at rest, see [Where your Microsoft 365 customer data is stored](/en-us/microsoft-365/enterprise/o365-data-locations) and refer to the data center city locations listed there.

## Required licenses and permissions

You must be a Global Admin, Compliance Admin, or Exchange Admin to perform the tasks described in this article. To learn more about Purview permissions, see [Permissions in the Microsoft Purview portal](purview-permissions).

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

See the [Microsoft 365 security and compliance licensing guidance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#data-loss-prevention-for-exchange-online-sharepoint-online-and-onedrive-for-business) for complete licensing information.

## Portal links for your subscription

The following table lists the correct portal URLs for each subscription environment.

| Portal | Worldwide / GCC | GCC High | DoD |
| --- | --- | --- | --- |
| Office SCC | purview.microsoft.com | scc.office365.us | scc.protection.apps.mil |
| Microsoft Defender portal | security.microsoft.com | security.microsoft.us | security.apps.mil |
| Microsoft Purview portal | purview.microsoft.com | purview.microsoft.us | purview.apps.mil |

## New EDM experience

The new EDM experience combines the functionality of the EDM schema and EDM sensitive information type tools into a single user experience. The new experience offers the following benefits:

- A simplified workflow
- Automated schema and SIT creation
- Additional guardrails to ensure better performance

### Simplified workflow

With the new experience, the schema and SIT are created in a single workflow. Creating the schema and SIT together means there are fewer steps, better guidance on mapping primary elements to default SITs, and clearer descriptions of default confidence levels for the rules.

When you need to see the status of an EDM SIT in the creation process, the new experience reports the current creation status in the UI.

- *Data not yet uploaded*
- *Data upload percent*
- *Data upload complete*
- *Indexing complete*
- *Data upload failed*
- *Data indexing failed*

### Automated schema and SIT creation

In the new experience you can provide a sample data file that has the same header values and enough rows (10-20) of representative data to the system. The system validates the format and creates the schema based on the headers. You then identify the primary fields in the schema and the system recommends the SITs that best match the primary fields to associate them with. If you don't want to upload the file, you can enter the same values manually in the UI.

Important

Be sure to use sample data values that aren't sensitive; however, also make sure that the sample values are in the same format as your actual sensitive data. Using nonsensitive data is essential because the sample data file doesn't get encrypted and hashed when you upload it in the same way that your actual sensitive information table does. The data from the sample data file isn't retained nor accessible once the EDM SIT is created.

The system generates the EDM SIT detection rules, one for each primary field. Based on detection of the primary fields, the system creates high and medium confidence rules using all the other fields as corroborative evidence. You can manually add low confidence rules if needed.

### Additional guardrails to ensure better performance

The system warns you if it finds a primary field mapped to a SIT that detects a broad range of values, called a *loosely defined SIT*. Mapping a primary field to a loosely defined SIT can cause the system to perform lookups on large numbers of strings that aren't related to the kind of content that you're looking for. Mapping between these types of SITs and primary fields can result in false negatives and decrease performance.

Note

A *loosely defined SIT*, such as a custom SIT that looks for all personal identification numbers, has detection rules that allow for greater variability in the items detected. A *strongly defined SIT*, such as a U.S. Social Security Number, has detection rules that only allow a narrow, well-defined set of items to be detected.

The system will also warn you if the values in the primary field you select occur multiple times in a large number of rows. Repeated primary-field values across many rows can cause large numbers of result sets to be returned and processed, which could cause a time-out. Timeouts can result in missed detections and poor performance.

## Choosing the right EDM SIT creation experience for you

You can toggle back and forth between the new and classic experiences, but we recommend using the new experience unless your needs fall into one or more of these four use cases, as described below.

### Mapping multiple EDM SITs to the same schema

In EDM, you can create a maximum of 10 schemas. Each time you create an EDM SIT using the new experience, a new schema is created. This results in a 1:1 mapping between EDM schema and EDM SIT. The new experience doesn't support mapping multiple SITs to the same schema.

### Creating or managing more than 10 EDM SITs

Because the new experience doesn't support mapping multiple SITs to the same schema, you're limited to creating and managing 10 EDM SITs. In the classic experience, you can map multiple EDM SITs to the same schema and so have more than 10 EDM SITs. Using the new flow, you receive an error if you try to create an eleventh EDM schema and you won't be able to view more than 10 EDM SITs.

### Specifying the name of your EDM schema

If you need to specify a name for your EDM SIT schemas, you have to use the classic experience to create and manage them. Because the new experience automatically creates the schema, you don't get the opportunity to give your schema a custom name. The autogenerated name is a concatenation of the EDM SIT name and the word *schema*. For example, if the EDM SIT name is *PatientNumber*, the schema name would be *PatientNumberschema*.

### Editing EDM schemas created in the classic experience

All schemas that are created using the classic experience or uploaded as an XML file using PowerShell aren't viewable or manageable in the new experience.

Once you choose your method of creating EDM SITs, select the link for your chosen experience in the Next steps section: [new experience](sit-create-edm-sit-unified-ux-workflow) or [classic experience](sit-create-edm-sit-classic-ux-workflow).