---
layout: Conceptual
title: Use data loss prevention with on-premises repositories | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-use
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MET150
description: Learn how to use data loss prevention with on premises location repositories to scan data at rest and implement protective actions for on premises file shares and on-premises SharePoint folders and document libraries.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 801958e5-a4db-728b-e1bb-17bfd1b492e5
document_version_independent_id: 801958e5-a4db-728b-e1bb-17bfd1b492e5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-on-premises-scanner-use.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-on-premises-scanner-use
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-on-premises-scanner-use.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/062d60c9-ee0f-402e-a046-b4e67c3572d6
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/17d3b3f6-a66e-4c69-9774-14a73c38e669
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 95a5b657-8c55-cfe5-8d2f-84a8a1a53e95
---

# Use data loss prevention with on-premises repositories | Microsoft Learn

To help familiarize you with Microsoft Purview Data Loss Prevention on-premises features and how they surface in DLP policies, we've put together a couple of scenarios for you to follow. These scenarios show you how to discover files that match DLP rules across Activity Explorer, the audit log, and the information protection scanner, and how to enforce protective actions on on-premises file shares and SharePoint document libraries. Specifically, the first scenario covers where DLP rule-match data appears when scanning on-premises repositories, and the second scenario walks through enabling policy enforcement so that protective actions are applied to scanned files.

Important

These DLP on-premises scenarios are not the official procedures for creating and tuning DLP policies. Refer to the following topics when you need to work with DLP policies in general situations:

- [Learn about data loss prevention](dlp-learn-about-dlp)
- [Create and Deploy data loss prevention policies](dlp-create-deploy-policy)

## Scenario: Discover files matching DLP rules

Data from DLP surfaces in several areas:

### View on-premises repository events in Activity Explorer

DLP reports rule matches are available in [Activity Explorer](https://compliance.microsoft.com/dataclassification?viewid=activitiesexplorer).

### View on-premises repository events in the Microsoft 365 audit log

The DLP rule matches are also available in the Audit log UI (see [Search the audit log](audit-search)) and are accessible via PowerShell through the[Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog).

### Use the information protection scanner to inspect matching files

Discovery data is available in a local report in .csv format and is stored under:

**%localappdata%\Microsoft\MSIP\Scanner\Reports\DetailedReport\_%timestamp%.csv report**.

Look for the following columns:

- DLP Mode
- DLP Status
- DLP Comment
- DLP Rule Name
- DLP Actions
- Owner
- Current NTFS Permissions (SDDL)
- Applied NTFS Permissions (SDDL)
- NTFS permissions type

## Scenario: Enforce DLP rule

If you want to enforce DLP rules on scanned files, enforcement must be enabled both on the content scan job and at the policy level in DLP.

### Configure DLP to enforce policy actions

To turn on enforcement for your DLP policy targeting on-premises repositories, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com)
2. Navigate to **Data loss prevention** &gt; **Policies**.
3. Select the DLP policy that is targeted to the on-premises location repositories you have configured for the scanner.
4. Edit the policy.
5. On the **Policy Mode** page, select **Turn the policy on immediately**.
6. Choose **Next** and then choose **Submit**.
7. Choose **Done**.