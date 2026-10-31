---
layout: Conceptual
title: Microsoft Purview Data Map history (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-history
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn what's available in the Microsoft Purview Data Map history (preview).
ms.custom: sfi-image-nochange
locale: en-us
document_id: 07a76b72-6d24-3cf2-ebaf-39a1bb75ea03
document_version_independent_id: 07a76b72-6d24-3cf2-ebaf-39a1bb75ea03
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-history.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-history
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-history.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 586b77ff-1a1a-38f7-83ec-3047a1aad9ea
---

# Microsoft Purview Data Map history (preview) | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

When a user updates an asset in Microsoft Purview, Data Map history logs that change and makes the information available in the Microsoft Purview portal. Information about who added or edited an asset, what edits were made, and when the edit happened, is stored for reference later. This information helps data auditors and business owners to maintain compliance and security in their Microsoft Purview accounts. It also allows data stewards and admins to debug issues and curation in their data assets.

Data Map history is available to users in both the [free](data-governance-free-version) and [enterprise](data-governance-free-version-upgrade-to-enterprise) versions of Microsoft Purview.

Currently, you can view your assets' history either:

- In the Audit solution in the Microsoft Purview portal
- Within individual solutions
- Using the REST API

## Prerequisites

Before you can use Data Map history, [make sure that the audit log is turned on in your organization](audit-log-enable-disable#verify-the-auditing-status-for-your-organization). If it's not, you need to turn it on to access your Data Map history.

## Which assets have history

Currently, these kinds of assets have Data Map history available:

- Classifications\*
- Data assets\*
- Glossary terms\*
- Business assets\*
- Domains
- Collections
- Role assignments
- Data sources
- Scan
- Scan rule set
- Credential
- Policy

\* In-solution experience is currently only available for classifications, data assets, business assets, and glossary terms.

## How to use Data Map history

Data Map history allows you to see the operational history of changes to your Data Map assets in Microsoft Purview.

You're able to see the history for select operations that include:

- Creation
- Updates
- Assignment

For a full list of available operations in Data Map History, see [the audit log activities documentation.](audit-log-activities#microsoft-purview-governance-activities)

Important

Data Map history entries are kept in Audit for 180 days, and are available for 30 days in the in-solution experience. To view audit history for longer, you can use [Microsoft Purview Audit (Premium)](audit-premium).

### Audit solution experience

To view the activities within the Audit solution, follow these instructions:

1. Navigate to the Audit solution within Microsoft Purview

    ![Screenshot of the Audit solution card in the Microsoft Purview portal.](media/data-map-history/audit-card.png)
2. Select **Search** to search for audit records
3. Select time range for activity.
4. Narrow the scope of your search using **Activities - friendly names**, **Activities - operation names**, or **Record types**.

    Tip

    For the list of available activities, see the [audit log activities page](audit-log-activities#microsoft-purview-governance-activities)

    [![Screenshot of the Audit solution search in the Microsoft Purview portal.](media/data-map-history/audit-search.png)](media/data-map-history/audit-search.png#lightbox)
5. Select **Search** and wait for job state to change to **Complete**.

    [![Screenshot of the Audit solution search showing a completed status.](media/data-map-history/search-complete.png)](media/data-map-history/search-complete.png#lightbox)
6. Select your search from the list, and scroll through or filter the history table to find the operations you're looking for.

    [![Screenshot of the audit search results detail page, showing the audit history table with the returned search results.](media/data-map-history/audit-detail-browse.png)](media/data-map-history/audit-detail-browse.png#lightbox)

### In-solution history experience

Note

In-solution experience is currently only available for classifications, data assets, business assets, and glossary terms.

To view the activities, follow these instructions:

1. [Search](unified-catalog-data-assets-search) for a data asset, glossary term, or classification in Microsoft Purview Unified Catalog.
2. Select the **History** tab.
3. Scroll through or filter the history table to find the operations you're looking for.

    [![Screenshot of the in-solution history experience, with the history tab highlighted.](media/data-map-history/in-solution-history.png)](media/data-map-history/in-solution-history.png#lightbox)

## Query Audit log using the REST API

You also can use the Microsoft Purview [REST API](/en-us/rest/api/purview/datamapdataplane/audit/query) to access your Data Map history.

1. To authenticate with the REST API, follow the instructions on the [Authenticate for APIs page](data-gov-api-rest-data-plane).
2. Use the authentication token to POST to this request URL: `https://api.purview-service.microsoft.com/datamap/api/audit/query?api-version=2023-10-01-preview`

Here are a few example API calls you can use to get started:

- Retrieve an asset's history in a time range
- Retrieve the history of a specific operation
- Filter by user who edited an asset
- Filter by keywords
- Example with pagination

### Retrieve an asset's history in a time range

Get all audit history of an asset within a specific time range.

```json
{
  "category": "Asset",
  "guid": "f432d351-5442-4724-945b-516d5d501fc9",
  "startTime": "2024-01-01T00:00:00.000Z",
  "endTime": "2024-01-06T00:00:00.000Z",
  "sortBy": "CreationTime",
  "sortOrder": "Descending"
}
```

### Retrieve the history of a specific operation

Get the history of specific operation type. For example, when classifications are applied to the asset.

Tip

For the list of available operations, see the [audit log activities page](audit-log-activities#microsoft-purview-governance-activities).

```json
{
  "category": "Asset",
  "guid": "f432d351-5442-4724-945b-516d5d501fc9",
  "operationType": "ClassificationAdded",
  "sortBy": "CreationTime",
  "sortOrder": "Descending"
}
```

### Filter by user who edited an asset

```json
{
  "category": "Asset",
  "guid": "f432d351-5442-4724-945b-516d5d501fc9",
  "userId": "contoso@microsoft.com",
  "sortBy": "CreationTime",
  "sortOrder": "Descending"
}
```

### Filter by keywords

Filter by keywords such as a changed attribute name, attribute value, etc.

```json
{
  "category": "Asset",
  "guid": "f432d351-5442-4724-945b-516d5d501fc9",
  "keywords": "userDescription",
  "sortBy": "CreationTime",
  "sortOrder": "Descending"
}
```

### Example with pagination

After the first query, if the "lastPage" property in the response body is false, the use can use the "continuationToken" in the response body to fetch the next page.

```json
{
  "continuationToken": "TY7BbsIwEAV%2fKDZr4oQ0KAcEVKo4klNvK…",
  "category": "Asset",
  "guid": "f432d351-5442-4724-945b-516d5d501fc9",
  "sortBy": "CreationTime",
  "sortOrder": "Descending",
  "pageSize": 10
}

```

## Limitations

1. Currently, it takes a couple minutes for an operational item to appear in an assets **History** tab.
2. Currently, to see a new item in the **History** tab, you need to manually refresh the tab.