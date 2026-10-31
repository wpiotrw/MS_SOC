---
layout: Conceptual
title: Metadata Quality in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-metadata-quality
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-04-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand and manage metadata quality in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 21dd3010-ce7d-b797-bea0-1ccab150b60c
document_version_independent_id: 21dd3010-ce7d-b797-bea0-1ccab150b60c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-metadata-quality.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-metadata-quality
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-metadata-quality.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1473a061-9079-a9dd-b287-b1c40f15056e
---

# Metadata Quality in Unified Catalog | Microsoft Learn

Metadata quality is a low-code or no-code experience for data stewards and members of the Chief Data Officer’s office, to write any logic to test the metadata health and quality. Data stewards can write complex logic without worrying about coding, and immediately see results in Microsoft Purview Unified Catalog. Metadata quality comes with a set of predefined logic for each control, that you can read about in [the health controls article](unified-catalog-controls). As a data steward, you can add more rules to the existing logic, and at the next refresh of the health controls, the new metadata quality logic applies to the metadata based on the scope, such as data product, governance domain, or other entity.

## Prerequisites

Users need the [data health owner role](data-governance-roles-permissions#unified-catalog-permissions) to update and manage metadata quality.

## Access metadata quality

1. In **Unified Catalog**, select **Health management**, then select **Controls**.
2. On the **Controls** page, expand **Metadata Quality Management**.

## Add a metadata quality control rule

1. On the metadata quality page, select any control to see its list of controls.

    [![Screenshot of the metadata quality page, with a control selected and it's rule highlighted.](media/metadata-quality/see-control-rules-inline.png)](media/metadata-quality/see-control-rules.png#lightbox)
2. Add a new rule by selecting **Add rule**. The **Add rule** flyout pane opens with a list of all available rules for your current scope. (Example scope: Data product)

    [![Screenshot of the metadata quality new rule menu.](media/metadata-quality/add-new-rule-inline.png)](media/metadata-quality/add-new-rule.png#lightbox)
3. Select a rule, and select **OK**.

    [![Screenshot of the metadata quality new rule menu with a rule selected.](media/metadata-quality/select-ok-inline.png)](media/metadata-quality/select-ok.png#lightbox)
4. Select any more parameters required to complete the logic (For example, select the number of data assets with a classification count)

    [![Screenshot of a new metadata quality rule, adding the final logic steps to resolve the rule.](media/metadata-quality/complete-logic-inline.png)](media/metadata-quality/complete-logic.png#lightbox)
5. Select the checkmark button.
6. Select **Save changes** to save your updates.

    [![Screenshot of the metadata quality rules page with the save changes button highlighted.](media/metadata-quality/select-save-changes-inline.png)](media/metadata-quality/select-save-changes.png#lightbox)

Note

As the metadata quality rules run, all pass checks contribute to [health control scores](unified-catalog-controls), and all failed checks contribute to [health control actions](unified-catalog-data-quality-actions).

## Edit a metadata quality control rule

1. On the metadata quality page, select any control to see its list of controls.

    [![Screenshot of the metadata quality page, with a control selected and its rules highlighted.](media/metadata-quality/see-control-rules-inline.png)](media/metadata-quality/see-control-rules.png#lightbox)
2. Hover over any existing rule and select the pencil icon to edit, or the trash can icon to delete.
3. If you edit, update any rule logic and select the check mark button.
4. Select **Save changes** to save your changes.

### Combine rules

1. Select the checkbox next to more than one rule, then select the **Combine rules** button.
2. Select whether you want to combine the rules with the OR or AND operator.
3. Select **Save changes** to save your updates.

### Reset all rules

At any time, you can reset all rules back to their default using the **Reset** button. If you do, you lose any customizations you made.

## Set severity

Set the severity of your controls to change how they appear in the [health actions](unified-catalog-data-health-management-actions-page) when rule failures occur.

1. In **Unified Catalog**, select **Health management**.
2. Select **Metadata quality**.
3. Select **Configure severity**.

    [![Screenshot of the metadata quality page, with the configure severity button highlighted.](media/metadata-quality/configure-severity-inline.png)](media/metadata-quality/configure-severity.png#lightbox)
4. Select a control category, then select your control.
5. For each control, set the severity to one of these options: Low, Medium, High.
6. Select **Save** to save your changes.
7. When metadata quality rules run, your health actions update according to your new settings.

    [![Screenshot of the health actions page, showing the severity of all the listed health actions.](media/metadata-quality/health-actions.png)](media/metadata-quality/health-actions.png#lightbox)

## Default actions

Here's a list of the default actions that are available out of the box:

| Finding type | Finding subtype | Finding Name | Severity |
| --- | --- | --- | --- |
| Access and use | Compliant data use | Missing terms of use on data products | Medium |
|  | Self-serve access enablement | Missing access policy on data products | Medium |
| Discoverability | Data cataloging | Data product not linked to data assets | High |
|  |  | Missing description on data products | High |
|  |  | Missing published glossary terms on data products | High |
|  |  | Missing use case on data products | High |
|  | Data products connection | Data product not linked to data assets | Medium |
| Estate curation | Classification and labeling | Missing classification on data assets | Medium |
| Health observability | Health management monitoring, alerting, and insights |  |  |
| Metadata quality management | Data product usability | Governance domain description length is fewer than 100 characters | Medium |
|  |  | Data product description length is fewer than 100 characters | Medium |
|  |  | Published glossary term's description length is fewer than 25 characters | Medium |
|  | Linked assets | Data product description length is fewer than 100 characters | Medium |
|  |  | Missing published glossary terms on data product | High |
| Trusted data | Data product certification | Data product isn't endorsed | Low |
|  | Data product ownership | Missing owners on data assets | High |
|  |  | Missing owners on data products | High |
|  | Data quality enablement | Missing data quality scores on data assets | Medium |
| Value creation | Business OKRs alignment | Missing OKRs on data products | Medium |

## Limitations

Currently, you can edit and manage existing health control metadata quality, but you can't create new controls.