---
layout: Conceptual
title: How data flows in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-data-flows
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use this article to learn more about how data flows between Data Map, Defender for Cloud Apps, and Microsoft Purview solutions.
keywords: Microsoft 365, Microsoft Purview, compliance, solutions
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
search.appverid:
- MET150
ms.collection:
- purview-compliance
- essentials-compliance
ai-usage: ai-assisted
locale: en-us
document_id: 18b3c362-3959-9464-6e71-fa1417e55323
document_version_independent_id: 18b3c362-3959-9464-6e71-fa1417e55323
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-data-flows.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-data-flows
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-data-flows.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e69816a-aaaa-474e-a36f-3ec7790fadc3
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/ae012320-d2b3-47d8-abdc-898a64d069a9
platformId: 2c7b6634-d670-45ad-340e-89dbd9a377c8
---

# How data flows in Microsoft Purview | Microsoft Learn

This article describes how [Microsoft Purview](purview) shares data between Purview solutions. This information supplements the commitments made to you in the relevant sections of the [Microsoft Product Terms](https://www.microsoft.com/licensing/docs/view/Product-Terms) and the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA).

The Data Map provides a unified map of your data assets and can identify the assets’ relationships for effective governance. Microsoft Defender for Cloud Apps gives you full visibility of your SaaS app landscape to help protect your apps.

When you create an enterprise account, either by [upgrading a free tier account](data-governance-free-version-upgrade-to-enterprise) or by creating a new enterprise account, you can register data sources within your data estate. By registering data sources, users in the enterprise account can [scan](data-map-scan-ingestion) the registered data sources. After you complete registration and scan activities for a data source, data flows between [Data Map](data-map) and some Microsoft Purview solutions.

Important

If you don't want to authorize data flows throughout Microsoft Purview, don't register or scan any of the data sources in your data estate into Data Map.

The following table describes how Microsoft Purview solutions share data with Data Map and receive data from Data Map and [Microsoft Defender for Cloud Apps](/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

| Microsoft Purview Solution | What gets shared to Data Map | What is received from Data Map | What is received from Microsoft Defender for Cloud Apps |
| --- | --- | --- | --- |
| Microsoft Purview Audit | N/A | - Service configuration data  - Audited activities data (including audit records and log query permissions)  - Admin operations data | N/A |
| Microsoft Purview Unified Catalog | N/A | - Asset details, including asset metadata, classification data, and label data | N/A |
| Microsoft Purview Data Loss Prevention (DLP) | - DLP policies and configuration | - Classification data  - Policy hit audit events and policy distribution acknowledgment status | N/A |
| Microsoft Purview Information Protection | - Label definitions, policies, and configurations  -Label insights and aggregations for Microsoft 365  - Microsoft Information Protection policies and configurations  - Classification data for Microsoft 365  - Asset metadata for Microsoft 365  - Telemetry data for protection policies and labels | - Label insights and aggregations  - Classification data  - Tenant roles, role groups, and license information  - Scan setup and execution details  - Asset metadata (owner and additional information including name, path, consent status)  - Policy hit audit events and policy distribution acknowledgment status | N/A |
| Microsoft Purview Insider Risk Management | N/A | N/A | - Cloud app events (activity log) and connection status |
| Microsoft Purview Policy | N/A | - Label names, policies and Ids  - Policy definition | N/A |