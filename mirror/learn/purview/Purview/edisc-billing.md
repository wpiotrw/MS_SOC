---
layout: Conceptual
title: Billing in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-billing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about billing in Microsoft Purview eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-12-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 78d46e28-9c82-0162-aaca-95d35d17ef5e
document_version_independent_id: 78d46e28-9c82-0162-aaca-95d35d17ef5e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-billing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-billing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-billing.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ce39dbaa-5b7f-dc39-9d57-b3fbb1558564
---

# Billing in eDiscovery | Microsoft Learn

eDiscovery uses a billing model based on the combination of your enterprise subscription and pay-as-you-go billing for certain features. This new billing combination includes:

- Your [Microsoft 365 subscription](https://www.microsoft.com/microsoft-365/compare-all-microsoft-365-plans) and any add-ons. Depending on the licensing and subscriptions for your organization, you have access to specific premium eDiscovery features in the Microsoft Purview portal. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for eDiscovery.
- [Pay-as-you-go billing](purview-billing-models#pay-as-you-go-billing-model) for data storage for non-Microsoft 365 enterprise and cloud AI application data in eDiscovery cases.
- Pay-as-you-go billing for using Microsoft Graph APIs for tenants with E3 eDiscovery licenses.

## Configure pay-as-you-go billing

Before you can use features associated with non-Microsoft 365 AI data in eDiscovery in your organization, or use Microsoft Graph APIs with an E3 eDiscovery license, you must configure an Azure subscription for pay-as-you-go billing. For step-by-step guidance, see Enable [Microsoft Purview pay-as-you-go features](purview-payg-subscription-based-enablement).

## Billing details for Microsoft Graph API usage for E3 eDiscovery licensed organizations

Microsoft Graph APIs support tenants with E3 eDiscovery licenses, enabling automation and integration of eDiscovery workflows. These APIs support case management, search, hold, and export operations, offering a secure and consistent experience aligned with the Microsoft Purview portal.

These APIs replicate the portal experience and include:

- **Case management:** Create, Get, List, Update, Close, Reopen, Delete
- **Search management:** Create, List, Get, Update, Delete, Estimate Statistics
- **Hold management:** List, Create, Get, Update, Delete
- **Data source management:** Add, List
- **Export:** Export results, Export report only

    For more details on how to use the APIs, see [Use the Microsoft Purview eDiscovery API v1.0](/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)

### Billing calculation for API usage

To use any of the APIs, you need to activate the pay-as-you-go subscription.

Currently, usage of all APIs except Export APIs doesn't contribute towards billing. Usage of Export API is billed based on the volume of data exported. Each organization receives an included amount of free storage per month, with additional usage billed at a set price per GB. The monthly billing details are available in the billing section on the [Azure portal](https://portal.azure.com).

For more information about API storage and pricing, see [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/).

For example, the following table outlines the Graph API billing for a sample month of eDiscovery activity and uses a hypothetical billing rate of $10 USD per GB:

| Day | Case | API used | Volume | Monthly cumulative volume | Charges | Cumulative charges |
| --- | --- | --- | --- | --- | --- | --- |
| Day 1 | Case 1 | Create case, Create Search 1 | N/A | 0 | 0 | 0 |
| Day 2 | Case 1 | Create Search 2, Create Hold, Add data sources | N/A | 0 | 0 | 0 |
| Day 3 | Case 1 | Export report | 1 GB | 1 GB | 0 | 0 |
| Day 6 | Case 1 | Export results | 24 GB | 25 GB | 0 | 0 |
| Day 10 | Case 2 | Create case, Create Search | 0 | 25 GB | 0 | 0 |
| Day 11 | Case 2 | Export results and reports | 20 GB | 45 GB | 0 | 0 |
| Day 14 | Case 1 | Create Search 3 | 0 | 45 GB | 0 | 0 |
| Day 17 | Case 1 | Export results from Search 3 | 15 GB | 60 GB | $100 | $100 |
| Day 21 | Case 2 | Create search and export results | 12 GB | 72 GB | $120 | $220 |

## Billing details for non-Microsoft 365 enterprise and cloud AI application data

### Data types

Depending on the type of data included in eDiscovery cases in your organization, subscription or pay-as-you-go billing applies:

- **Microsoft 365 data**: Non-AI data from Microsoft 365 services and applications. This data type includes data from Microsoft services like Exchange, SharePoint, OneDrive, and others.

    This data storage is included in your enterprise subscription and isn't subject to pay-as-you-go billing.
- **Microsoft 365 AI data**: AI data from Microsoft 365 services and applications. This data type includes AI data from Microsoft services like Microsoft 365 Copilot and AI data from Microsoft Office applications like Microsoft Word, Microsoft Excel, Microsoft PowerPoint, and others.

    This data storage is included in your enterprise subscription and isn't subject to pay-as-you-go billing.
- **Non-Microsoft 365 AI data**: Data from other generative AI applications from Microsoft and other connected external AI applications. This data type includes [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), and any connected or cloud AI application.

    This data storage isn't included in your enterprise subscription and is subject to pay-as-you-go billing. Data for non-Microsoft 365 services and applications is identified by *ItemClass*.

    The following ItemClasses are applicable to pay-as-you-go billing:

    - IPM.SkypeTeams.Message.Copilot.Fabric.\*
    - IPM.SkypeTeams.Message.Copilot.Security.SecurityCopilot
    - IPM.SkypeTeams.Message.Copilot.BAP\*
    - IPM.SkypeTeams.Message.Copilot.Sql.\*
    - IPM.SkypeTeams.Message.ConnectedAIApp.\*
    - IPM.SkypeTeams.Message.CloudAIApp.SaaS.\*

### Non-Microsoft 365 AI data scope

You can add and export non-Microsoft 365 AI data to an eDiscovery case in several ways. Your organization retains this data as long as a case is active or closed. Depending on the data type and the type of process taken in eDiscovery, the application of data storage costs varies.

The following eDiscovery processes use pay-as-you-go billing for non-Microsoft 365 AI data:

- Direct export of this data from cases by using the Microsoft Purview portal
- Adding this data to a review set
- Exporting this data by using Microsoft Graph API

Important

If you use the legacy eDiscovery experience in the Microsoft Purview portal, importing non-Microsoft 365 or non-Office 365 data to a review set is excluded from pay-as-you-go billing and isn't charged.

The following eDiscovery processes don't use pay-as-you-go billing for non-Microsoft 365 AI data and are included in your enterprise subscription:

- All search processes
- All hold processes
- All case management processes

Tip

A breakdown of the total size of Microsoft 365 data and non-Microsoft 365 AI data is included in the [*summary.csv report*](edisc-process-report-use#consumption-summary) for [exports from search](edisc-search-export) and [exports from review sets](edisc-review-set-export). This report includes details for metadata when exporting from a review set and can help you estimate data storage charges.

### Billing calculation for non-Microsoft 365 AI data

Every 24 hours, the system calculates the total amount of data storage for non-Microsoft 365 AI data for all active and closed eDiscovery cases. Deleted cases don't incur data storage charges after they're deleted. The system multiplies the total amount of data by the daily storage rate to determine the total data storage cost for the day.

At the end of each month, the system adds together the daily charges for the total eDiscovery data storage costs. These costs are part of the all-up data meter storage costs in your Azure account. The system itemizes details for each eDiscovery process and the costs. Use the [Summary.csv report](edisc-process-report-use#summary-csv-report) to review a [breakdown of the volume](edisc-process-report-use#consumption-summary) of Microsoft 365 and non-Microsoft 365 AI data for processes in scope for pay-as-you-go billing.

For example, the following table outlines the non-Microsoft 365 AI data storage amounts for a sample month of eDiscovery activity:

| Day | Case | Action | Daily data volume | Running daily total |
| --- | --- | --- | --- | --- |
| Day 1 | Case 1 | Direct export in active case | 1 GB | 1 GB |
| Day 2 | All cases | No actions | 0 GB | 1 GB |
| Day 3 | Case 2 | Add to review set in active case | 5 GB | 6 GB |
| Day 4 | All cases | No actions | 0 GB | 6 GB |
| Day 5 | Case 3 | Direct API export in active case | 2 GB | 8 GB |
| Day 6 | All cases | No actions | 0 GB | 8 GB |
| Day 7 | All cases | No actions | 0 GB | 8 GB |
| Day 8 | All cases | No actions | 0 GB | 8 GB |
| Day 9 | Case 1 | Apply holds in active case (not billable) | 2 GB | 8 GB |
| Day 10 | All cases | No actions | 0 GB | 8 GB |
| Day 11 | Case 1 | Closed case | 0 GB | 8 GB |
| Day 12 | All cases | No actions | 0 GB | 8 GB |
| Day 13 | Case 2 | Add to review set in active case | 2 GB | 10 GB |
| Day 14 | All cases | No actions | 0 GB | 10 GB |
| Day 15 | All cases | No actions | 0 GB | 10 GB |
| Day 16 | All cases | No actions | 0 GB | 10 GB |
| Day 17 | Case 1 | Reopened as active case and export | 1 GB | 11 GB |
| Day 18 | All cases | No actions | 0 GB | 11 GB |
| Day 19 | All cases | No actions | 0 GB | 11 GB |
| Day 20 | All cases | No actions | 0 GB | 11 GB |
| Day 21 | Case 1 | Direct export in active case | 1 GB | 12 GB |
| Day 22 | All cases | No actions | 0 GB | 12 GB |
| Day 23 | All cases | No actions | 0 GB | 12 GB |
| Day 24 | All cases | No actions | 0 GB | 12 GB |
| Day 25 | Case 1 | Deleted case (removes data storage) | 3 GB | 9 GB |
| Day 26 | All cases | No actions | 0 GB | 9 GB |
| Day 27 | Case 2 | Export from review set in active case (not billable) | 2 GB | 9 GB |
| Day 28 | All cases | No actions | 0 GB | 9 GB |

In this example, the total amount of non-Microsoft 365 AI data storage that is subject to pay-as-you-go-billing rates for the month is 246 GB. Data associated with processes that aren't applicable to data storage billing and data that you remove from your organization don't appear on your monthly bill. You can view billing details in the [Azure portal](https://portal.azure.com).

#### Excluding non-Microsoft 365 AI data

To exclude non-Microsoft 365 AI data from processes subject to pay-as-you-go billing, use search conditions and filters to exclude this data type.

#### KeyQL condition

Use the following KeyQL statement with the *Equals* operator to exclude non-Microsoft 365 AI data from a search query:

```
(NOT((ItemClass:IPM.SkypeTeams.Message.Copilot.Fabric.*) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.Security.SecurityCopilot) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.BAP*) OR (ItemClass:IPM.SkypeTeams.Message.ConnectedAIApp.*) OR (ItemClass:IPM.SkypeTeams.Message.CloudAIApp.SaaS.*) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.sql.*)))
```

#### Filter

Use the *Contains none of* operator for the **Non M365 AI activity** type filter to exclude non-Microsoft 365 AI data.