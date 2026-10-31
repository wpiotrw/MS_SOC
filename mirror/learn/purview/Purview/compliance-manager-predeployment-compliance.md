---
layout: Conceptual
title: Predeployment compliance with Microsoft Purview Compliance Manager (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-11-04T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Assess predeployment compliance (preview) with Microsoft services in Microsoft Purview Compliance Manager.
locale: en-us
document_id: 1f81fe82-4470-dcb3-952d-3ea52b5c51fc
document_version_independent_id: 1f81fe82-4470-dcb3-952d-3ea52b5c51fc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-predeployment-compliance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-predeployment-compliance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-predeployment-compliance.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: c44f5bf6-ca00-e7bc-76c0-b653d0ac3490
---

# Predeployment compliance with Microsoft Purview Compliance Manager (preview) | Microsoft Learn

Compliance Manager provides a way for organizations to understand Microsoft's compliance posture with Microsoft services before deployment. By reviewing the data provided in the **Sub-service compliance readiness** group of [regulations](compliance-manager-regulations), you can analyze in detail how using Azure services can contribute to your organization's overall compliance posture in regard to these four regulations:

- ISO/IEC 27001:2013
- NIST 800-53 rev.4
- PCI DSS v4.0
- System and Organization Controls (SOC) 2

## Get started on the Regulations page

In Compliance Manager, go to the **Regulations** page. The first grouping of regulations you see is **Sub-service compliance readiness**. You can filter your view to only these regulations by selecting **Pre-deployment** on the **Availability** filter. A deeper subservice filter is available once you select a regulation to start viewing its actions and controls.

The subservice compliance readiness regulations aren't for creating assessments, and interacting with these regulations doesn't activate them or require a license. When you open them, they display detailed information on the controls and improvement actions managed by you and Microsoft that can contribute to an improved compliance posture using Microsoft services.

To view an individual regulation, select its name from the list to open its details page.

## Explore predeployment regulation details

When you select a regulation from the **Regulations** page, a details page opens. Each details page has expandable sections for **All actions** and **All controls.** When you open the regulation's page, the **All actions** section is automatically expanded. Minimize the **All actions** section to more easily get to the **All controls** section underneath.

### All actions section

The **All actions** section of the regulation details page provides detailed information about the features supported by the service, and the relevant actions to be taken by your organization and actions managed by Microsoft (learn more about the [shared responsibility model](compliance-manager-improvement-actions#overview)).

##### Your actions tab

The **Your actions** tab has a table with the features supported by the service. Select a name from the **Feature | Action** column to display a details panel along the right side, which you can maximize to full screen. The details screen includes a control description, feature description, and the related Cloud Security Benchmark ID. It also provides prescriptive guidance and the automated technical policies, with deep links to reference content, that you can enable for monitoring compliance. The **Related controls** tab displays related controls from various regulations to help you examine all potentially affected controls simultaneously.

An array of filters allows you to customize your view based on service, subservice, control family, and control ID.

Use the **Sub-service** filter to delve deeper into your service review. This detailed view provides specific information tailored to your selected subservice to enable a more customized compliance review process.

##### Microsoft actions tab

The **Microsoft actions** tab displays the actions that Microsoft takes care of as the service provider for meeting regulatory requirements. Select a name from the **Feature | Action** column to display a details panel along the right side. You can maximize the panel to full screen, which displays a control description, the Azure control framework ID, and, on the **Implementation** tab, details on the steps taken by Microsoft to fulfill the action. The **Related controls** tab displays related controls from various regulations to help you examine all potentially affected controls simultaneously.

### All controls section

The **All controls** section displays a table listing all the controls for the regulation. Under the **Control title** column, select a control to display a details panel along the right side. You can maximize the panel to full screen, which displays details of the regulatory requirements, and tabs that list your actions and Microsoft actions.

## Export action and control data

In both the **All actions** and **All controls** sections, there are commands at the top of each table that enable you to export all or selected actions and controls into a CSV or JSON file format.

Select **Export all** to export all items, and select your desired format from the dropdown. To export only selected items, check the box next to the action or control names, then select **Export selected**, then select the desired format.