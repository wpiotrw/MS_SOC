---
layout: Conceptual
title: Use Data Security Posture Management analytics trends and reports - (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-reports
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how analytics reports with Data Security Posture Management (classic).
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-12-15T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.collection:
- purview-compliance
- data-security-posture-management
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
locale: en-us
document_id: fdfd28b7-483a-e433-7bc4-8e7882eb1704
document_version_independent_id: fdfd28b7-483a-e433-7bc4-8e7882eb1704
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-reports.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-reports
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: df6a1f3b-ddf6-fefd-794f-632248a88595
---

# Use Data Security Posture Management analytics trends and reports - (classic) | Microsoft Learn

Note

This article is for the **classic** version of Data Security Posture Management, now replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Data security posture management (DSPM) analytics trends and reports help you quickly view the unprotected and protected sensitive assets and potentially risky user activities in your organization.

## Working with reports

For each report, use the following features to help filter, review, evaluate, and export DSPM insights:

- **Charts**: Hover on specific areas of report information for metrics and more details about insights.
- **Customize columns**: Select **Customize columns** to add or remove columns and associated information from a report.
- **Export**: Select **Export** to create a .csv file that contains the values included in a report.

## Analytics reports

- **Unprotected sensitive assets across data sources**: This report displays the location of sensitive assets containing one or more classifiers (sensitive information types, exact data match classifiers, trainable classifiers) and:

    - Aren't protected by a data loss prevention (DLP) policy that restricts exfiltration activities.
    - Don't have a sensitivity label applied that controls access.
- **Users performing top risk-related activities on unprotected sensitive assets**: This report displays the number of users flagged by [Insider Risk Management](insider-risk-management-activities) (departing users, potentially disgruntled users, high risk users, potential high impact users, potentially risky users) who recently performed activities containing sensitive assets that:

    - Contain any type of classifier (sensitive information types, exact data match classifiers, trainable classifiers) that aren't protected by a DLP policy that blocks access or don't have a sensitivity label applied that control access.

## Trends

You can view trends on the **Overview** page. They help you see the recent history of sensitive data assets and user activities in your organization. Trends help you monitor your data security posture over time and track the status of protected assets. When you hover over specific points in the trends, you can view details about that point in time or area.

- **Sensitive assets labeled (automatically + manually)**: Percentage of assets per week that have sensitivity labels applied, either manually by users or automatically by auto-labeling policies.
- **Sensitive assets protected by at least one DLP policy**: Percentage of sensitive assets in your organization that contain any type of classifier (sensitive information types, exact data match classifiers, trainable classifiers) and are protected by at least one DLP policy.
- **Potentially risky users**: Number of users per week who are assigned insider risk severity levels (*Low*, *Medium*, *High*) based on activity detected by Insider Risk Management policies.