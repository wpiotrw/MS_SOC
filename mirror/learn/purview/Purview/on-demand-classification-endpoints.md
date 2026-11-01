---
layout: Conceptual
title: Get started with on-demand classification for endpoints - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/on-demand-classification-endpoints
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Identify and classify sensitive content in files at rest on Windows endpoints using Microsoft Purview on-demand classification.
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-20T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- tier1
- M365-security-compliance
search.appverid:
- MET150
locale: en-us
document_id: 037bd350-0d1e-1a16-9d6b-272a521c31f8
document_version_independent_id: 037bd350-0d1e-1a16-9d6b-272a521c31f8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/on-demand-classification-endpoints.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: on-demand-classification-endpoints
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/on-demand-classification-endpoints.md
platformId: e156d2a8-b0e8-1c1f-34af-5cdfd6bee4a0
---

# Get started with on-demand classification for endpoints - Microsoft Purview | Microsoft Learn

On-demand classification identifies and classifies sensitive content in files at rest on Windows endpoints. It's the endpoint workload of [on-demand classification](on-demand-classification), which also covers SharePoint and OneDrive.

Note

This article covers on-demand classification for endpoints. For real-time endpoint protection, see [Learn about Endpoint data loss prevention](endpoint-dlp-learn-about).

## What on-demand classification covers on endpoints

Endpoint DLP classifies files in real time when they're accessed, modified, or shared. On-demand classification extends that coverage to inactive and historical files at rest that Endpoint DLP hasn't processed.

| Capability | Scope | Trigger |
| --- | --- | --- |
| Endpoint DLP (real-time) | Active files (modified, accessed, shared) | Real-time, automatic |
| On-demand classification | Inactive/historical files at rest | Admin-initiated scan |

Together, these capabilities help ensure that both active and inactive files on endpoints are classified according to your organization's current policies.

## What on-demand classification doesn't do

| On-demand classification... | Details |
| --- | --- |
| Doesn't apply sensitivity labels | It classifies files but doesn't label them. Combine with auto-labeling policies to apply labels based on classification results. |
| Doesn't enforce DLP policies directly | Classification results feed into policies, but enforcement happens through Endpoint DLP when files are accessed or shared. |
| Doesn't replace Endpoint DLP | Endpoint DLP handles real-time protection. On-demand classification covers historical files that Endpoint DLP hasn't processed. |

## How on-demand classification works

On-demand classification uses a two-phase approach: estimation followed by classification.

### Phase 1: Estimation

After you create a scan, the estimation process begins on scoped devices. The endpoint agent performs a metadata-only pass without reading file contents or running classifiers:

- Enumerates files that match your scope criteria (selected users, file types, last modified date range).
- Evaluates file eligibility gates, including file size limits, supported file types, and time window filters.
- Checks eligibility for previously classified files by comparing classifier history and file modification state against previous scan results.
- Reports aggregated metadata to the Microsoft Purview service, including eligible file counts and estimated reusable files.

No file contents are read and no classifiers are executed during estimation.

Note

Estimation numbers may differ from the final classification results. Estimation reflects a point-in-time metadata snapshot. Files may change, devices may go offline, or previously classified file eligibility may shift between estimation and classification. This is expected behavior.

### Phase 2: Classification

After reviewing the estimation:

- Select **Start classification** to begin classification.
- Each file is evaluated against your sensitive information types (SITs) and trainable classifiers.
- Files are evaluated against DLP, Microsoft Information Protection (MIP), data lifecycle management (DLM), and insider risk management (IRM) policies simultaneously.
- Previously classified files with unchanged content and classifiers are retained without rescanning.

### Phase 3: Review results

After classification completes:

- View results on the **Items for review** tab.
- Filter and export classified items.
- Monitor device status and scan progress.

## Prerequisites

Devices must be onboarded to Microsoft Purview endpoint data loss prevention. For onboarding and device requirements, see [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started).

| Action | Required role |
| --- | --- |
| Create and run a scan | Compliance Administrator |
| View classification results | Content Explorer Content Viewer or Content Explorer List Viewer |

For licensing requirements, see [Microsoft 365 guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

## Create your first endpoint scan

### Step 1: Navigate to on-demand classification

1. Go to the Microsoft Purview portal.
2. In the left navigation, select **Data Loss Prevention** &gt; **Classifiers**.
3. Select the **On-demand classification** tab.
4. Select **New scan**.

### Step 2: Configure your scan

| Setting | Description | Guidance |
| --- | --- | --- |
| Name & description | A name to identify this scan | Use a descriptive name, such as "Finance team endpoint scan, quarterly" |
| Scope & location | Select **Endpoints** and choose which users' devices to scan | Start with a small user group for your first scan |
| Classifiers | Select which SITs and trainable classifiers to scan for (up to 50) | Include only the classifiers you need. More classifiers means longer scan time. |
| File last modified range | Filter files by when they were last modified | Use this to focus on files from a specific time period |
| File extensions | Which file types to include | Leave as default (all supported types) unless you need to narrow scope |

Endpoint scans are scoped by user. All onboarded devices for selected users are included. System folders (Windows, Program Files) are automatically excluded.

### Step 3: Start estimation

1. Review your scan configuration.
2. Select **Create scan**.
3. The estimation phase begins automatically.

### Step 4: Review estimation and start classification

Once estimation completes, review the estimated file count and projected scope. Select **Start classification** to begin.

You can start classification before estimation reaches 100%. Starting at 80–90% progress is recommended: the final 10–20% typically reflects slow-responding devices, and devices that have completed estimation begin classification immediately while remaining devices join as they finish.

### Step 5: Review results

After classification completes:

1. Open your scan and select the **Items for review** tab.
2. Filter results by classifier, file type, or sensitivity.

## Bandwidth throttling

Each device has a data discovery bandwidth limit per rolling 24-hour period. This limit is independent of other DLP bandwidth and prevents the scan from affecting device performance. When a device reaches the limit, scanning pauses automatically and resumes after the period resets.