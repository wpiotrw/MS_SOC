---
layout: Conceptual
title: Microsoft Purview Information Protection scanner Custom Reporting (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploy-scanner-custom-reporting
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-04-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- purview-information-protection
search.appverid:
- MOE150
- MET150
ROBOTS: NOINDEX, NOFOLLOW
description: Learn how Custom Reporting for the Microsoft Purview Information Protection scanner populates database tables so you can build reports on scan results.
ms.custom: msecd-doc-authoring-1012
ai-usage: ai-assisted
locale: en-us
document_id: 6bc92447-97c1-eee9-1026-2adc9e2d02a3
document_version_independent_id: 6bc92447-97c1-eee9-1026-2adc9e2d02a3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploy-scanner-custom-reporting.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy-scanner-custom-reporting
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploy-scanner-custom-reporting.md
platformId: 1b858c2c-4a1c-2d7e-2bd3-322c3b7e74db
---

# Microsoft Purview Information Protection scanner Custom Reporting (preview) | Microsoft Learn

This article describes the Microsoft Purview Information Protection scanner **Custom Reporting** feature (preview). Custom Reporting gives scanner administrators the data they need in the scanner cluster database to build their own reports against scan results—including labeling, protection state, and matched sensitive information types (SITs).

Custom Reporting is available with Microsoft Purview Information Protection client and scanner [version 3.2.89.0](information-protection-client-relnotes#version-32890-preview) or later. Custom Reporting is enabled by an administrator through [Scanner feature control](deploy-scanner-feature-control).

## What Custom Reporting enables

Without Custom Reporting, the scanner produces per-scan CSV and TXT reports and stores a limited set of operational data in the cluster database. To build a complete picture of file state—what changed, what's labeled, what's protected, and what kinds of sensitive data exist where—administrators have to combine multiple CSV exports across scan cycles and load them into a separate reporting tool.

Custom Reporting moves file-state and SIT-match data into the scanner cluster database so that administrators can:

- Query the present and previous label, protection state, and SIT counts for every scanned file in a repository.
- Compute deltas between scans (for example, the change in number of matched SITs per file).
- See which sensitive information types were matched on which files, and how many matches per type.
- Connect the scanner cluster database to a reporting tool of their choice (for example, Power BI, an enterprise reporting warehouse, or a SQL-based dashboarding tool) without first having to stitch CSV exports together.

The scanner remains the source of truth. Custom Reporting writes the additional reporting data to the scanner cluster database on the next scan cycle after the feature is enabled.

## Database schema

The reporting tables and columns required by Custom Reporting were first added to the scanner cluster database schema in client version [3.2.57.0](information-protection-client-relnotes#version-32570). Until Custom Reporting is enabled, the new columns and tables exist but aren't populated. Existing scanner functionality is unchanged.

Note

You don't need to install client version 3.2.57.0 first. Whether you're installing the scanner fresh or upgrading from any earlier version, the scanner deploys the full database schema (including the Custom Reporting tables and columns) on install or upgrade.

When Custom Reporting is enabled by using [Scanner feature control](deploy-scanner-feature-control), the scanner starts populating the following data on the next scan cycle.

### Additions to `dbo.ScannerFiles`

`dbo.ScannerFiles` continues to hold one row per scanned file. Custom Reporting populates the following additional columns to capture file state and the delta between the current and previous scan:

| Column | Type | Description |
| --- | --- | --- |
| `LabelName` | `NVARCHAR(MAX)`, nullable | Current label name applied to the file. `NULL` if unlabeled. |
| `PrevLabelId` | `NVARCHAR(MAX)`, nullable | Label ID applied at the previous scan, stored as a string. `NULL` if previously unlabeled. |
| `PrevLabelName` | `NVARCHAR(MAX)`, nullable | Label name applied at the previous scan. `NULL` if previously unlabeled. |
| `ProtectionState` | `NVARCHAR(MAX)`, nullable | Current protection state for the file at the end of the scan. |
| `PrevProtectionState` | `NVARCHAR(MAX)`, nullable | Protection state recorded at the previous scan. |
| `ClassificationCount` | `INT`, default `0` | Count of sensitive information type matches on the file at the current scan. |
| `LatestScanSessionId` | `UNIQUEIDENTIFIER`, nullable | Identifies the most recent scan session that touched the file. Used to compute deltas across scan cycles. |
| `FileStatus` | `NVARCHAR(MAX)`, nullable | Final disposition of the file in the scan cycle (for example, the requires-justification status set by `ProcessJob`, or `Failed` for files that couldn't be processed). |

### New table: `dbo.MatchedClassificationAction`

`dbo.MatchedClassificationAction` is a new table that stores the matched sensitive information types per file per scan. Each row represents one matched SIT for a single file in a single scan session.

| Column | Type | Description |
| --- | --- | --- |
| `Id` | `BIGINT IDENTITY` (primary key) | Surrogate key for the row. |
| `FilePath` | `NVARCHAR(MAX)`, nullable | Full path of the file that the SIT was matched on. |
| `FileHashPath` | `BINARY(64)`, nullable | Hash of the file path. Joins to `dbo.ScannerFiles.HashPath` and is indexed for join performance. |
| `ScanSessionId` | `UNIQUEIDENTIFIER`, nullable | Identifies the scan session in which the SIT was matched. Joins to `dbo.ScannerFiles.ScanSessionId` and is indexed. |
| `MatchedInformationTypeName` | `NVARCHAR(MAX)`, nullable | Display name of the matched sensitive information type (for example, `U.S. social security number (SSN)`). |
| `MatchedInformationTypeId` | `UNIQUEIDENTIFIER`, nullable | GUID of the matched SIT. The same GUID is used in the local Microsoft Purview Information Protection logs for `Workload=OnPremisesFileShareScanner`. |
| `MatchedInformationTypeCount` | `INT`, default `0` | Number of matches for this SIT in the file. |
| `ConfidenceScore` | `INT`, default `0` | Confidence score of the match. |

### New table: `dbo.ScannedFilesArchive`

`dbo.ScannedFilesArchive` is a new table that stores a historical archive of files the scanner processed, with rows tied to the scan session that created them. Unlike the live `dbo.ScannerFiles` table, which only keeps the latest state of each file, this table preserves prior archived states for change tracking, reporting, and auditing.

Files that the scanner skips because nothing has changed since the previous scan session aren't re-inserted, so later scan sessions don't contain a complete snapshot of all files. Instead, only the existing archive entry from the session that last processed the file remains, which keeps the archive lean while preserving a history of meaningful changes.

| Column | Type | Description |
| --- | --- | --- |
| `Id` | `BIGINT IDENTITY` (primary key) | Surrogate key for the row. |
| `HashPath` | `BINARY(64)` | Hash of the file path. Joins to `dbo.ScannerFiles.HashPath`. |
| `FullPath` | `NVARCHAR(MAX)` | Full path of the file at the time of the scan session. |
| `ScanSessionId` | `UNIQUEIDENTIFIER` | The scan session that produced this archive row. |
| `LastModifiedTime` | `DATETIME2`, nullable | Last-modified timestamp of the file as observed during the scan session. |
| `LabelId` | `UNIQUEIDENTIFIER`, nullable | Label ID applied to the file at the time of the scan session. |
| `IssueCount` | `INT`, default `0` | Number of issues recorded against the file in this scan session. |
| `EndScan` | `DATETIME2`, nullable | Time the file completed processing in this scan session. |
| `JobStartTime` | `DATETIME2`, nullable | Time the processing job for this file started. |
| `LabelName` | `NVARCHAR(MAX)`, nullable | Label name applied at the time of this scan session. |
| `PrevLabelId` | `NVARCHAR(MAX)`, nullable | Label ID at the previous scan session, stored as a string. |
| `PrevLabelName` | `NVARCHAR(MAX)`, nullable | Label name at the previous scan session. |
| `ProtectionState` | `NVARCHAR(MAX)`, nullable | Protection state at the time of this scan session. |
| `PrevProtectionState` | `NVARCHAR(MAX)`, nullable | Protection state at the previous scan session. |
| `ClassificationCount` | `INT`, default `0`, nullable | Count of sensitive information type matches in this scan session. |
| `LatestScanSessionId` | `UNIQUEIDENTIFIER`, nullable | The latest scan session known to have touched the file at the time this archive row was recorded. |
| `FileStatus` | `NVARCHAR(MAX)`, nullable | Disposition of the file in the scan session (for example, `Modified` or `Deleted`). |

`dbo.ScanSummary` (per-scan totals) is unchanged.

## Example questions Custom Reporting can answer

Once Custom Reporting is populating the database, administrators can run queries such as:

- Which repositories have the highest concentration of matched SITs, and how has that concentration changed since the last scan?
- Which files were labeled or relabeled during the most recent scan cycle, and what was the previous label?
- Which files are still unlabeled but contain matches for one or more sensitive information types?
- Which sensitive information types are most prevalent in a given repository, and at what confidence?
- Which files transitioned from unprotected to protected (or the reverse) since the last scan?

## Enable Custom Reporting

Custom Reporting is turned on through [admin-controlled feature configuration](deploy-scanner-feature-control). From any node in the scanner cluster, run:

```powershell
Set-ScannerConfiguration -FeatureSettings @{CustomReporting=$true}
```

To enable Custom Reporting at install time on a new scanner node, use the `-FeatureSettings` parameter with [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner):

```powershell
Install-Scanner -SqlServerInstance SQLSERVER1 -Cluster Europe -FeatureSettings @{CustomReporting=$true}
```

To confirm the current state, run:

```powershell
Get-ScannerConfiguration
```

The change takes effect on every node in the cluster on the next scan cycle. No service restart is required.

To stop populating the Custom Reporting columns and table, run:

```powershell
Set-ScannerConfiguration -FeatureSettings @{CustomReporting=$false}
```

Disabling Custom Reporting stops new writes. Data already written to the reporting columns and tables isn't deleted, so the feature can be re-enabled later without data loss.

## Plan your scanner cluster database for reporting

When you turn on Custom Reporting, the scanner cluster database stores significantly more data:

- Additional columns per file in `dbo.ScannerFiles`
- One row per matched SIT per file per scan in `dbo.MatchedClassificationAction`
- Archive rows in `dbo.ScannedFilesArchive` for files the scanner processes and archives during a scan session (not for every unchanged file in every cycle)

Building reports against the scanner cluster database also adds a read workload that runs alongside the scanner's operational reads and writes.

Before you enable Custom Reporting in production, consider:

- **Cluster size and scan volume.** Estimate the number of files scanned per cycle, the typical number of SIT matches per file, and how often you scan. Use those numbers to size the database.
- **Operational impact.** Reporting queries against the same database that the scanner is writing to can compete with the scanner for resources during a scan cycle.
- **The reporting workload you actually want.** Interactive dashboards, scheduled extracts, and ad-hoc queries each have very different impacts.

For most production deployments, we recommend hosting the scanner cluster database on SQL Server Enterprise so that you can dedicate a read-only replica to reporting. With a SQL Server [Always On availability group](/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server), you can route reporting traffic to a [readable secondary replica](/en-us/sql/database-engine/availability-groups/windows/active-secondaries-readable-secondary-replicas-always-on-availability-groups). Reporting queries then run on the secondary replica instead of competing with the scanner's operational workload on the primary.

This separation lets reporting tools (for example, Power BI) connect to the read-only replica and refresh on their own cadence without affecting scan throughput on the primary.

Note

The scanner itself always reads from and writes to the primary database. Only your custom reporting workload should be pointed at a read-only replica.

## Limitations during preview

- Custom Reporting doesn't include a built-in dashboard in this preview. Customers build their own reports against the scanner cluster database.
- Settings configured by [admin-controlled feature configuration](deploy-scanner-feature-control) aren't synchronized with the Microsoft Purview portal. Not every scanner feature will end up being configurable from the portal. For features that are also configurable from the Microsoft Purview portal, a setting configured in the portal takes precedence and prevents updates from PowerShell.