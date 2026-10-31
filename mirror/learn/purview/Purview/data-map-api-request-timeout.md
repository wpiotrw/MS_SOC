---
layout: Conceptual
title: Troubleshoot Microsoft Purview Data Map API request timeout exceptions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-api-request-timeout
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes how to self-service troubleshoot Data Map API request timeout exceptions.
locale: en-us
document_id: 3199d15a-a0f0-c501-353e-d19b72fd509f
document_version_independent_id: 3199d15a-a0f0-c501-353e-d19b72fd509f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-api-request-timeout.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-api-request-timeout
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-api-request-timeout.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 39509ca0-2610-e40a-9d43-f3c5c1b869b9
---

# Troubleshoot Microsoft Purview Data Map API request timeout exceptions | Microsoft Learn

Applies to Microsoft Purview Data Map API returned HTTP 408 request timeout.

## Troubleshooting steps

The following list contains known patterns and solutions for request timeout exceptions.

If it doesn't match your case, or the failure can't be resolved after applied the solution, contact [Microsoft Customer Support](https://support.microsoft.com/en-us/contactus) with all request history.

### Time out to list all glossaries

```http
# https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/get-term
GET {endpoint}/datamap/api/atlas/v2/glossary?ignoreTermsAndCategories={ignoreTermsAndCategories}&limit={limit}&offset={offet}&sort={sort}
```

This API by default returns all glossaries together with all terms/categories under those glossaries. If there are 1000 glossaries, each glossary has 1000 terms and 1000 categories, it returns 1000 glossary with 1000 \* (1000 terms + 1000 categories).

- The size of all related terms/categories could be too large to fetch via single API within a reasonable duration. Use query parameter `ignoreTermsAndCategories=true` to reduce total count to load in server side and shrink response size for network transfer. If terms/categories are still needed, you can combine with the below APIs to fetch them.

    - List terms under specific glossary

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-categories
        GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/terms?limit={limit}&offset={offset}&sort={sort}
        ```
    - List categories under specific glossary

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-terms
        GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/categories?limit={limit}&offset={offset}&sort={sort}
        ```
- The size of the all glossary count could be too large to fetch via a single API within a reasonable duration. Use query parameter `limit` and `offset` with small pagination size to get glossaries page by page.

### Time out to get glossary with detailed info

```http
GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/detailed
```

This API by default returns the glossary together with all terms/categories under the glossary.

- The size of all related terms/categories could be too large to fetch via single API within a reasonable duration. We recommend you use the below APIs to have a better pagination experience.

    - Get specific glossary

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/get
        GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}
        ```
    - List terms under specific glossary

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-terms
        GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/terms?limit={limit}&offset={offset}&sort={sort}
        ```
    - List categories under specific glossary

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-categories
        GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/categories?limit={limit}&offset={offset}&sort={sort}
        ```

### Time out to list all terms under specific glossary

```http
# https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-terms
GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/terms
```

By default, this API returns all terms under the glossary.

- The size of all terms under the glossary could be too large to fetch via single API within a reasonable duration. Use query parameters `limit` and `offset` with small pagination size to list terms page by page.

    ```http
    # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-terms
    GET {endpoint}/datamap/api/atlas/v2/glossary/{glossaryGuid}/terms?limit={limit}&offset={offset}&sort={sort}
    ```

### Time out to get single term

```http
# https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/get-term
GET {endpoint}/datamap/api/atlas/v2/glossary/term/{termGuid}
```

This API by default returns the term together with its all relationships. For example, assignedEntities, parent/child terms.

- The size of assignedEntities on the term could be too large to fetch via single API within a reasonable duration. Use query parameter `excludeRelationshipTypes` to ignore assignedEntities relationship called `AtlasGlossarySemanticAssignment` in response. Then use another dedicated API to get assignedEntities with pagination.

    - Get specific term

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/get-term
        GET {endpoint}/datamap/api/atlas/v2/glossary/term/{termGuid}?excludeRelationshipTypes=AtlasGlossarySemanticAssignment
        ```
    - List assignedEntities under specific term

        ```http
        # https://learn.microsoft.com/en-us/rest/api/purview/datamapdataplane/glossary/list-entities-assigned-with-term
        GET {endpoint}/datamap/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities?limit={limit}&offset={offset}&sort={sort}
        ```