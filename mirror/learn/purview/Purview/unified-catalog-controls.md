---
layout: Conceptual
title: Data Health Controls in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-controls
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to access and manage health management controls in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 5b4fecde-e09a-1fe3-cfc5-99b2cdae5448
document_version_independent_id: 5b4fecde-e09a-1fe3-cfc5-99b2cdae5448
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-controls.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-controls
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-controls.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: ec3514c8-0f0a-c9ba-dd17-078b4dc166d3
---

# Data Health Controls in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Data health controls help your team analyze and track your health management. Track your journey to complete data governance by monitoring your governance health, and use the provided health controls to track your progress. Data health controls are specific measures, processes, and tools that you implement to monitor, maintain, and improve the quality, security, and overall health of your organization's data. These controls are part of a broader data governance framework and are essential for ensuring that data remains accurate, consistent, and usable across the organization.

Data health controls are essential components of a comprehensive data governance strategy. They help organizations maintain the integrity, security, and usability of their data assets. Some benefits include:

- **Improved data quality:** Ensures that data remains accurate, consistent, and reliable for decision-making.
- **Enhanced security:** Protects sensitive data from breaches, unauthorized access, and corruption.
- **Regulatory compliance:** Helps organizations adhere to legal and industry standards for data management.
- **Operational efficiency:** Reduces the time and resources spent on correcting data issues and ensures that data is readily available and usable.
- **Risk mitigation:** Prevents costly errors and data-related risks that can arise from poor data management.

## Prerequisites

- You need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions to view data estate health information.
- You need [data health owner](data-governance-roles-permissions#unified-catalog-permissions) permissions to update or edit any health controls.

## Limitations

- Currently, you can't create custom controls.

## Access data health controls

To view controls, go to **Unified Catalog** &gt; **Health management** &gt; **Controls**. The **Controls** page shows your governance scores at the domain level, so you can understand your organization's progress at a glance.

Health controls are grouped into several categories that you can open to view their parts. Category scores are an aggregate of the controls underneath them. They show their current score and their target, so you can see areas for growth.

Select any category or individual health control for a detailed view.

## Available health controls

The currently available health controls are:

| Control grouping | Control | Description |
| --- | --- | --- |
| Access and use | Self-serve access enablement | Percentage of data products that have self-serve policies and workflows enabled. |
|  | Compliant data use | Percentage of data subscriptions with a provided data use purpose. |
| Discoverability | Data cataloging | Percentage of data products that a data product owner publishes in the governance domain. |
|  | Data products connection | Percentage of data products that have data assets mapped. |
| Estate Curation | Classification and labeling | Percentage of data products and governance domains that are classified and labeled. |
|  | Critical data identification | Percentage of business domains with at least one critical data element. |
| Value creation | Business OKRs alignment | Percentage of data products aligned with one or more business objectives and key results (OKRs). |
| Trusted data | Data product ownership | Percentage of data products that have owners assigned. |
|  | Data quality enablement | Percentage of data products with a data quality score. |
|  | Data product certification | Percentage of data products certified by an authorized data product owner in the governance domain. |
| Metadata quality management | Data product useability | Percentage of data products that have: a description greater than 100 characters, a parent domain with a description of over 100 characters, and a glossary term with at least a 25 character description. |
|  | Linked assets | Percentage of data products with at least one linked asset and published glossary term. |

## Edit health controls

If you're a [data health owner](data-governance-roles-permissions#unified-catalog-permissions), you can edit your health controls to:

- Edit control details, such as owners, description, and governance domains.
- Activate or deactivate a control to manage scores.
- Configure thresholds to reflect your business goals.

## Edit control details

1. On the **Controls** page, expand a control group name to view individual controls.
2. Hover over the name of the control you want to edit and select the **Edit** pencil button. You arrive at the **Details** tab of the **Edit control** page.
3. At **Owner**, add or remove owner names.
4. At **Description**, edit the control's description.
5. At **Domains**, select all governance domains you want to include in the score, and deselect any domains you don't want to include.
6. Select **Save** at the top right of the page to save your changes.

## Activate or deactivate a control

You can deactivate any control so that new scores no longer roll up to a control group.

1. On the **Controls** page, expand a control group name to view individual controls.
2. Hover over the name of the control you want to edit and select the **Edit** pencil button. You arrive at the **Details** tab of the **Edit control** page.
3. Select the **Active** toggle to switch the control to the active or inactive state.
4. Select **Save** at the top right of the page to save your changes.

## Configure control thresholds

Adjust your health control's target score status, or threshold, to reflect your business goals.

1. On the **Controls** page, expand a control group name to view individual controls.
2. Hover over the name of the control you want to edit and select the **Edit** pencil button.
3. On the **Edit control** page, select **Thresholds**.
4. Make the following adjustments:

    1. Set the overall target score to reflect your goals.
    2. Adjust existing threshold conditions to show any of these statuses:
        - Undefined
        - Healthy
        - Fair
        - Not healthy
        - Critical
    3. Add and remove conditions on existing rules to calculate status based on score.
    4. Add or remove thresholds to calculate your status based on target score.

    Tip

    To return to the saved calculation before your edits, select the **Reset** command at the top right of the page.
5. Select **Save** at the top right of the page to save your changes.

## Configure control rules

Add rules to controls to measure their performance.

1. On the **Controls** page, expand a control group name to view individual controls.
2. Hover over the name of the control you want to edit and select the **Edit** pencil button.
3. On the **Edit control** page, select **Rules**.
4. Select **Add rule**. The **Add rule** flyout pane opens.
5. Search for a rule from the **Data product rules** list and select the rule to add it.
6. Select **OK**.
7. Add the needed parameter and accept it by selecting the check symbol.
8. Select **Save changes**.

## Configure rules severity

1. On the **Controls** page, expand a control group name to view individual controls.
2. Hover over the name of the control you want to edit and select the **Edit** pencil button.
3. On the **Edit control** page, select **Rules**.
4. Select **Configure severity**.
5. Select a control name, and update the severity for the **Finding name**. Finding names are the rule names, and you see these finding names as action name if the defined rule fails for the applied severity.

## Schedule control refresh

The schedule for the control refresh affects your health management actions and reports, as the controls provide the basis for many of these values. Consider how often you want to evaluate your overall data estate health, and schedule the controls refresh accordingly.

1. On the **Controls** page, select **Schedule refresh**.
2. At **Start**, enter a date, time, and time zone.
3. Set the frequency by selecting a number and choosing between **Days**, **Weeks**, or **Months**.
4. At **Until**, set an end date for the schedule, or leave blank if you want it to continue on the schedule indefinitely.
5. Save the configured schedule.

## Data health controls pricing

Data health controls usage is billed based on the Data Governance Processing Unit (DGPU) pay-as-you-go meters. The Basic SKU is used for compute of data health controls. Find details on [how pricing is computed for data health controls](data-governance-billing#data-health-controls-pricing).