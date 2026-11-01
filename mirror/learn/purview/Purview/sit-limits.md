---
layout: Conceptual
title: Sensitive information type limits | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-limits
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2025-03-31T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn about instance count and other sensitive information type limits
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 5155de58-e810-b6c6-1984-13f69a9866c3
document_version_independent_id: 5155de58-e810-b6c6-1984-13f69a9866c3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-limits.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-limits.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 8dc51a8b-81c4-a20a-5afe-8eb9e3f08137
---

# Sensitive information type limits | Microsoft Learn

These limits apply to all Microsoft Purview policies that use SITs.

To ensure high performance and lower latency, there are limitations in custom SIT configurations, as described in the following table.

| Limit | Value |
| --- | --- |
| Maximum number of custom SITs created through the Microsoft Purview portal | 500 |
| Maximum length of regular expression | 1024 characters |
| Maximum length for a given term in a keyword list | 50 characters |
| Maximum number of terms in keyword list | 2048 |
| Maximum number of distinct regexes per SIT | 20 |
| Maximum combined size for all keyword dictionaries (post compression) | 1MB (~1,000,000 characters) |
| Maximum number of rule packages | 10 |
| Maximum number of SITs per rule package | 50 |
| Maximum size of a rule package | 150KB |
| Capturing group in a regular expression | 1 |

Note

The regex pattern must use exactly one primary capturing group. Use noncapturing groups for any prefix/suffix (for example: `(?:prefix)(primary capturing group)(?:suffix)`). Multiple top-level capturing groups separated by `|` outside the primary group aren't supported; put alternation variants inside the single capturing group. For more information, see [Create a custom sensitive information type](sit-create-a-custom-sensitive-information-type).

Note

If you have a business need to create more than 500 custom SITs, please raise a support ticket.

### Instance count supported values for SIT

The SIT instance count limit applies when using SITs in these solutions:

- Microsoft Purview Data Loss Prevention policies
- Microsoft Purview Information Protection policies
- Microsoft Purview Data Lifecycle Management
- Communication Compliance
- Microsoft Purview Records Management
- Microsoft Defender for Cloud Apps
- Microsoft Priva

For a scanned item to satisfy the rule criteria, the number of unique instances of a SIT in any single item must fall between the min and max values. This is called the **Instance count**.

- **Min** field: the lower limit (minimum number) of unique instances of a SIT that must be found in an item to trigger a match. The min field supports values of 1 to 500.
- **Max**field: the upper limit on the number of unique instances of a SIT that can be found in an item and still trigger a match. The max field supports the following values:
    - 1 to 500 - Use a value between `1` and `500` when you want to set a specific upper limit of 500 or less on the number of instances of a SIT in an item.
    - Any - Use `Any` when you want to ensure that the unique instance count criterion is satisfied when an undefined number of unique instances of a SIT are found in a scanned item and that the specified number of unique instances meets or exceeds the minimum number of unique instances value. In other words, the unique instance count criteria are met as long as the min value is met.

For example, if you want the rule to trigger a match when at least 500 unique instances of a SIT are found in a single item, set the **min** value to `500` and the **max** value to `Any`.