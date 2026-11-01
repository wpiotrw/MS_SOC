---
layout: Conceptual
title: Use named entities in DLP policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-named-entities-use
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
description: Apply named entities in Microsoft Purview DLP policies to improve detection of sensitive data such as person names and physical addresses. Includes prerequisites, supported locations, and best practices.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: b5fb27a4-8219-8ce6-1a35-210e64fa3a8b
document_version_independent_id: b5fb27a4-8219-8ce6-1a35-210e64fa3a8b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-named-entities-use.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-named-entities-use
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-named-entities-use.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e69816a-aaaa-474e-a36f-3ec7790fadc3
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ae012320-d2b3-47d8-abdc-898a64d069a9
platformId: 8948b9d3-a1ed-c0bd-a693-c0c225a7b8ef
---

# Use named entities in DLP policies | Microsoft Learn

Read through [Named entities in sensitive information types](sit-named-entities-learn) before you start to use named entity SITs.

## Before you begin

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and edit data loss prevention (DLP) policies, must have the **DLP Compliance Management** role permissions. For more information, see [Add users or groups to a Microsoft Purview built-in role group](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group).

## Supported locations

You can use named entity SITs and enhanced policies to detect and protect sensitive items in these locations:

- SharePoint sites
- OneDrive accounts
- Teams chat and channel messages
- Devices (Windows 10/11 endpoint devices)
- Exchange mailboxes
- Microsoft Defender for Cloud Apps

Named entity SITs and enhanced policies aren't supported for:

- On-premises repositories
- Power BI

## Create and edit enhanced policies

To create or edit a DLP policy, use the procedures in [Create and Deploy data loss prevention policies](dlp-create-deploy-policy).

## Workloads and services that support named entities

The following workloads and services support named entities:

- **Microsoft 365 eDiscovery** supports the use of named entities in Substrate services.
- **Microsoft Defender for Cloud Apps** supports the use of named entities in Defender for Cloud Apps policies in the Defender for Cloud Apps portal.
- **Insider Risk Management** supports the use of named entities in Substrate services.
- **Records Management** supports the use of named entities.
- **Exact Data Match Sensitive Information Types** supports the use of named entities.

### Unified DLP support for named entities

The following table shows named entity support in Unified DLP workloads and services.

| Workload/Services | Support for Named Entities |
| --- | --- |
| Office Win32 clients policy tip | Not supported |
| Office WAC clients policy tip | Supported |
| OWA policy tip | Not supported |
| Outlook for Microsoft 365 policy tip | Supported |
| Endpoints (Windows 10, and 11 devices) | Supported |
| Exchange Transport rules | Supported |
| OneDrive for Business data-at-rest | Supported |
| SharePoint Online data-at-rest | Supported |
| Teams data-at-rest | Supported |
| Email messages data-at-rest | Supported for tenants with Privacy Service Plan |
| Microsoft Defender for Cloud Apps | Supported |

### Autolabeling support for named entities

The following table lists named entity support for autolabeling workloads and services.

| Workload/Services | Support for Named Entities |
| --- | --- |
| Office Win32 clients offline | Supported, user must select label and manually apply |
| Online Office Win32 clients online | Supported with old confidence scheme |
| Outlook online | Supported with old confidence scheme |
| Office WAC client | Supported |
| OWA | Supported |
| Exchange transport | Supported |
| OneDrive for Business data-at-rest | Supported |
| SharePoint Online data-at-rest | Supported |
| Microsoft Purview Information Protection scanner | Not supported |

## Known issues

The following table summarizes current known issues when using named entities and their impact.

| Issue | Impact |
| --- | --- |
| DLP Policy tips (OWA, Outlook, Office Win32 clients) | Policy tips with entity condition results in "no match" |
| Asian language support for person name (Chinese, Japanese, Korean) | Named entities supported for Latin-based character set only (that is, kanji isn't supported) for person name |
| On-premises repositories | Not supported as a workload |
| Power BI (preview) | Not supported |

## Best practices for using named entity SITs

Here are some practices you can use when you create or edit a policy that uses a named entity SIT.

- Use low instance counts (three to five) when you're looking for data that's in a spreadsheet and the keyword that's required by the SIT for that data is only in the column header. For example, let's say you're looking for US Social Security numbers, and the keyword `Social Security Number` only occurs in the column header. Since the values (the corroborative evidence) are in the cells below, it's likely that only the first few instances would be in close enough proximity to the keyword to be detected.
- If you're using a named entity SIT, like All Full Names, to help find US Social Security numbers, use larger instance counts such as 10 or 50. Then, when both the person names and the SSNs are detected together, you're more likely to get true positives.
- You can use [Autolabeling simulations](apply-sensitivity-label-automatically#learn-about-simulation-mode) to test the accuracy of named entity SITs. Run a simulation using a named entity SIT to see what items match the policy. With this information, you can fine tune accuracy by adjusting the instance counts and confidence levels in your custom policies or the enhanced template conditions. You can iterate simulations until the accuracy is where you want it before deploying a DLP or autolabeling policy containing named entities in production. Here's an overview of the autolabeling simulation workflow:

1. Identify the SIT or combination of SITs you want to test in simulation mode, either custom or cloned and edited
2. Identify or create a sensitivity label to be applied when the autolabeling policy finds a match in Exchange, SharePoint sites, or OneDrive accounts
3. Create a sensitivity autolabeling policy that uses the SIT from step 1 and with same Conditions and Exceptions that are used in your DLP policy
4. Run the policy simulation
5. View the results
6. Tune the SIT or policy and the instance count and confidence levels to reduce false positives.
7. Repeat until you get the accuracy results you want