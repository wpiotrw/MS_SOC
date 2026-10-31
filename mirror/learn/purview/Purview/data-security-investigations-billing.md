---
layout: Conceptual
title: Billing in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-billing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover the pay-as-you-go billing model for Data Security Investigations. Manage storage and AI capacity costs effectively with detailed guidance.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 248102b9-5085-419f-cd91-b1be2533771a
document_version_independent_id: 248102b9-5085-419f-cd91-b1be2533771a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-billing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-billing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-billing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 386cf3d2-681c-7b78-8657-5e75870fed4b
---

# Billing in Data Security Investigations | Microsoft Learn

Billing in Data Security Investigations is based solely on the combination of the amount of stored data and the associated computing capacity needed for AI analysis. It isn't based on a dedicated enterprise [plan or license](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

This billing combination is based on the **storage meter** and **AI capacity** models. The Data Security Investigations non-AI processing and storage meter lets you store data related to an investigation. Data Security Investigations Compute Units (compute unit) measure the computational capacity needed to run the AI analysis within Data Security Investigations.

## Storage meter

The storage meter for Data Security Investigations uses the [pay-as-you-go billing](purview-billing-models) model. You pay for storage on a gigabyte (GB) per month basis for stored data associated with all investigations in your organization.

For example, you have three investigations in your organization that have the following data associated with the items included in the investigation scopes for the current month:

| Investigation | Items | Total data |
| --- | --- | --- |
| Data breach 02/12/2025 | 3,766 | 200 GB |
| Potential data theft 03/03/2025 | 1,982 | 10 GB |
| Risky user activity 04/06/2025 | 287 | 5 GB |

For the current month, your total storage meter is 215 GB and you pay for that amount at the current per gigabyte rate. When you delete an investigation, you stop paying for the associated data storage amount. The charges are prorated to the number of days the data was stored in the billing cycle.

Some other important considerations for managing storage charges:

- If you create an investigation, use data storage, and then delete the investigation in a single 24-hour period, you pay for the storage amount.
- When you delete an investigation anytime after 00:00 UTC, you pay for storage for the full day (24 hours).
- Investigations auto-created by [proactive AI insights from DSPM](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm) consume storage continuously while the toggle is enabled. Because the investigation refreshes every 24 hours, storage charges are ongoing.

For more data storage rates and pricing, see Data Security Investigations [storage meter pricing](https://azure.microsoft.com/pricing/details/purview/).

## AI capacity

Important

To configure the AI capacity for Data Security Investigations, you must be a member of the *Data Security Investigations Admins* role group.

Data Security Investigations uses the [pay-as-you-go billing](purview-billing-models) model for AI capacity. You need compute units for deep analysis and AI-related processing in your investigations. You pay only for the compute units you use.

Proactive AI insights from DSPM also consume compute units. Each 24-hour refresh cycle uses compute units to generate AI insights across five fixed risk categories. For more information, see [Enable proactive AI insights from DSPM](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm).

For guidance on calculating the compute unit needs for your organization, see the Estimate and manage usage of Data Security Investigations Compute Units section in this article.

### Locations for compute units and AI processing

Compute unit processing uses GPU resources in Azure datacenters protected by Azure security and privacy controls. You can choose where to use compute units from any of the following locations:

- Australia/New Zealand (ANZ)
- Europe (EU)
- United Kingdom (UK)
- United States (US)

You can opt in to having compute units provisioned and AI analysis processing done anywhere in the world to mitigate potential disruptions in case your primary location experiences high activity.

Microsoft recommends having compute units and AI processing done anywhere with available GPU capacity. This recommendation enables Data Security Investigations and Azure to determine the optimal location based on load, latency, and responsiveness.

## Best practices for managing investigation costs

Planning and managing costs is an essential part of running effective Data Security Investigations. By estimating costs up front, applying safeguards during configuration, and continuously monitoring usage, you can control spending without limiting your ability to respond to security incidents.

The following best practices help ensure investigations remain cost-efficient while still providing the flexibility required for thorough and timely analysis.

1. **Use the in-product cost estimator before starting investigations**: Before launching an investigation, use the in-product cost estimator to anticipate costs based on investigation size and the analyses you plan to conduct. This process helps data security teams plan budgets with precision and prevent unforeseen expenses.
2. **Use built-in spending controls in Azure**: Use the powerful built-in spend controls included with your Azure subscription, including:

    - Create budgets for the Data Security Investigations resource group and meter level.
    - Configure alerts when spending approaches defined thresholds (for example, 50%, 75%, or 90%).
    - Use Azure Cost Analysis for drill-downs and anomaly detection.
3. **Scope investigations tightly**: Focus on the investigation scope to lower storage and compute costs. Start with targeted searches and expand only as needed based on initial findings.
4. **Delete completed investigations promptly**: When you delete an investigation, you no longer incur costs for using data storage. Charges are prorated to the number of days the data was stored in the billing cycle. Regularly review and remove investigations that you no longer need to minimize ongoing storage costs.
5. **Monitor usage with the usage dashboard**: Use the usage dashboard to track storage and compute unit spending within Data Security Investigations in real time. This granular visibility helps identify cost-saving opportunities and optimize resource allocation across investigations.
6. **Right-size your AI analysis**: Not every investigation requires the full suite of AI capabilities. Consider which analyses (categorization, vector search, examination) are truly necessary for each investigation to optimize compute unit consumption.
7. **Add categories incrementally**: When using [categorization](data-security-investigations-ai-analysis#use-categorization), start with a focused set of categories and add more as your investigation progresses. When you [add new categories](data-security-investigations-ai-analysis#add-or-update-categories) to an existing categorization, you're only charged for the compute units needed to process the net new categories. This approach helps you manage costs effectively while expanding your analysis over time.
8. **Budget for proactive AI costs from DSPM**: If you enable [proactive AI insights from DSPM](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm), the auto-created investigation refreshes every 24 hours, incurring ongoing storage and AI compute charges. Monitor usage regularly and factor these recurring costs into your monthly budget.

## Estimate your investigation data storage and AI costs

Before configuring billing, use the estimate costs tool to calculate an estimate of potential monthly data storage and AI costs for investigations in Data Security Investigations. Use the estimator tool to plan your costs before setting up data storage and compute units for AI features.

Use the tool to estimate individual investigation costs to create an average investigation cost or use the tool to estimate the costs of all anticipated investigations. This estimate is based on current storage and AI usage billing meters for a 30-day period.

Use the guidelines in the Investigation size and complexity section in this article to help complete the fields in the estimator tool.

To estimate investigations costs, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. On the **Estimate storage and AI usage costs** card, select **Estimate costs**.
3. Complete the required and optional fields for a single investigation to calculate an estimated average cost or for the total number of investigations in your organization.
4. Select **Calculate**.
5. Review the estimated costs and recalculate as needed.

## Configure billing

Before you can use Data Security Investigations in your organization, you must configure both billing models. Storage meter billing requires a link to an Azure subscription for pay-as-you-go billing. Capacity billing requires dedicated compute unit configuration.

### Prerequisites

To configure the storage meter and capacity for Data Security Investigations, you must have:

- An Azure subscription in the same tenant as Microsoft Purview.
- An Azure resource group in that subscription.
- The *Global Administrator* role.
- The resource group *Owner* or *Contributor* role.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

### Configure storage meter

The Azure subscription you configure for Data Security Investigations manages all pay-as-you-go capabilities across Microsoft Purview solutions. If you previously configured an Azure subscription for other Microsoft Purview solutions, you don't need to configure an additional subscription.

To configure the storage meter for Data Security Investigations, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Setup pay-as-you-go-billing for data storage** in the **Setup tasks** section.
3. On the **Setup pay-as-you-go-billing for data storage**flyout pane, complete the following fields for the Azure subscription:
    1. **Azure subscription**: The Azure subscription you want to assign to the storage meter.
    2. **Resource group**: The resource group in your Azure subscription you want to assign to the storage meter.
4. Select **Enable**.

### Configure AI capacity

When you configure compute units, you enable the AI capacity for investigations in your organization. To configure AI capacity for Data Security Investigations, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Set up AI capacity** in the **Setup tasks** section.
3. On the **Set up AI capacity**pane, complete the following fields:
    1. **AI analysis data processing location**: The primary country/region. Select from the available locations.
4. Select the check box to confirm that you read, understood, and agreed to the terms and conditions.
5. Select **Confirm**.

## Estimate and manage usage of compute units

To manage the usage of compute units in Data Security Investigations, estimate your likely compute unit usage and the general size of the investigation. While it's challenging to estimate the exact amount of these variables, having a general sense of the investigation processing, size, and complexity helps you make informed decisions about provisioning and scaling compute unit usage.

### Investigation processing

Data Security Investigations supports various processing tools to help you identify and take action on data security incidents. Each processing tool has different variables that you should consider when estimating support for each processing type:

| Process type example | Scale units or variables |
| --- | --- |
| Add to scope (including data preparation for AI analysis) | Size of data and extracted text |
| Vector searches | Size of data searched |
| Categorization | Number of new categories selected. Adding categories to an existing categorization only processes net new categories. |
| Examination | Number of files analyzed |

These variables primarily influence the cost for compute unit billing. They work together to determine the exact amount of compute unit usage per investigation. Each investigation might have a different combination of these cost influencers, so determining the exact compute unit billing estimation is challenging.

![Data Security Investigations compute unit cost influences.](media/dsi-scu-cost-influencers.png)

### Investigation size and complexity

Each investigation uses different amounts of storage and processing power. To estimate the compute unit usage for an investigation, consider the overall size of the investigation. In general, investigations fall into one of the following sizes:

- **Small investigation**: A small investigation to test usage as a proof of concept in your organization.
- **Medium investigation**: A medium investigation, such as a data audit or responding to a minor data security incident.
- **Large investigation**: A large investigation for a significant data breach or leak incident.
- **Extra large investigation**: An extra large investigation for a major data security breach, leak, or incident.

To estimate the total compute units your organization needs for specific types of investigations, use the investigation processing, size, and complexity guidelines in this section. See the following sections during your planning and configuration:

- [Add to scope](data-security-investigations-scope#automatic-vectorization)
- [Vector search and compute units](data-security-investigations-ai-analysis#vector-search-and-compute-units)
- [Categorization and compute units](data-security-investigations-ai-analysis#categorization-and-compute-units)
- [Examination and compute units](data-security-investigations-ai-analysis#examination-and-compute-units)

Important

You aren't billed for failed compute unit operations but are billed for partial completions. For example, you pay when you successfully vectorize partial data in an investigation scope. If you cancel an in-progress job (such as **Add to scope**, Categorization, or Examination), you still pay for any compute units consumed before the cancellation.

## Pay-as-you-go usage dashboard

Use the **Pay-as-you-go usage dashboard** to quickly view and track data storage and compute unit usage for each investigation in your organization. The current data storage and compute unit totals for each investigation help you manage usage and cost per investigation. This information is helpful during reactive investigation surges associated with severe data breaches and ongoing data storage trends.

Note

It might take up to 48 hours for the latest billing data to show up on the **Pay-as-you-go usage dashboard** for your organization. Only users assigned the *Data Security Investigations Admin* role can access the **Pay-as-you-go usage dashboard**.

To view the **Pay-as-you-go usage dashboard**, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned to the [Data Security Investigations Administrator](data-security-investigations-permissions) role group.
2. Select **Usage dashboard** in the left-navigation.

From the **Pay-as-you-go usage dashboard**, you can review:

- The data storage usage for each investigation and the total for each process.
- The total amount of compute units used by Data Security Investigations processes.
- The compute units per day, for the last 7, 14, or 30 day timescale.
- The compute unit usage for each investigation and the total for each process.

Each investigation has the total data storage for each of the following processes:

- **Add to scope**: Storage and compute supporting processes when adding items to the [investigation scope](data-security-investigations-scope), including automatic [vectorization](data-security-investigations-ai#vector-search).
- **Categorization**: Storage and compute supporting [categorization](data-security-investigations-ai#categorization) processes for an investigation.
- **Examination**: Storage and compute supporting [examination](data-security-investigations-ai#examination) processes for an investigation.
- **Interactive AI**: Storage and compute supporting semantic search and AI suggested categories.

To export the data storage and compute information for all investigations, select **Export**. The export file lists the following information:

- **ID**: The ID of the investigation.
- **Date**: The date the report was created for each investigation.
- **Storage**: The total data storage for each process in the investigation.
- **InvestigationName**: The friendly name of the investigation.
- **JobType**: The type of process associated with the data storage or compute usage.
- **JobID**: The ID for the process.
- **ConsumedUnits**: The amount of compute units used for the process.

## Stop billing

To stop billing for Data Security Investigations, disable both storage meter and AI capacity support. This action deletes all investigations in Data Security Investigations and deletes compute units for your resource group.

Caution

Deleting investigations and your compute unit resource group is irreversible. Make sure you export or preserve any investigation results or reports before stopping billing.

### Stop storage meter billing

Data storage charges start when you add items to the scope of an investigation. To stop storage metering, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned to the [Data Security Investigations Administrators](data-security-investigations-permissions) role group.
2. [Delete all existing investigations](data-security-investigations-settings-investigation#delete-an-investigation) in your organization.
3. Verify that no active or pending investigations remain in your organization.

When you delete all investigations, you remove the associated data and stop storage billing for Data Security Investigations.

### Stop AI capacity billing

AI analysis is billed through compute units in Microsoft Azure. To stop compute unit billing, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with a user account that has either the **Owner** or **Contributor** role for the Azure subscription associated with the Data Security Investigations compute unit resource.
2. Go to the **Subscription** where you deployed your Data Security Investigations resource.
3. Select the associated **Resource group** for Data Security Investigations.
4. Select and delete the **DSI compute unit capacity resource** (for example, `DataSecurityInvestigation-GUID`).

When you delete the compute unit resource, all AI capacity and compute billing stops for Data Security Investigations.