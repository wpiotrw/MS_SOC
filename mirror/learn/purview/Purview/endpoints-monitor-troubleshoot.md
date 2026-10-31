---
layout: Conceptual
title: Monitor and troubleshoot endpoint scans - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoints-monitor-troubleshoot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Track scan progress, understand device and scan statuses, and resolve common issues with on-demand classification for Windows endpoints in Microsoft Purview.
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
document_id: fa210091-e3d3-f24f-926c-c7019b23aeb4
document_version_independent_id: fa210091-e3d3-f24f-926c-c7019b23aeb4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoints-monitor-troubleshoot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoints-monitor-troubleshoot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoints-monitor-troubleshoot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: a2dc9bd3-264e-5628-6578-de3eea5c5de1
---

# Monitor and troubleshoot endpoint scans - Microsoft Purview | Microsoft Learn

Track scan progress, understand device and scan statuses, and resolve common issues with on-demand classification for Windows endpoints.

## Viewing scan progress

1. Go to the Microsoft Purview portal.
2. Navigate to **Data Loss Prevention** &gt; **Classifiers** &gt; **On-demand classification**.
3. Select your scan to view detailed progress.

The scan details page shows:

| Metric | Description |
| --- | --- |
| Scan status | Overall scan phase (estimation or classification) and progress |
| Files scanned | Number of files processed so far |
| Files in scope | Total estimated files from the estimation phase |
| Devices active | Devices currently scanning |
| Devices not responding | Devices that haven't reported recently |
| Devices where scan validity expired | Devices that exceeded the signal validity threshold and were removed from scan scope |

Note

Scan progress in the portal isn't real-time. Updates arrive periodically as devices report their status.

## Understanding scan statuses

### Estimation phase

| Status | Meaning | Action |
| --- | --- | --- |
| Estimation in progress | Devices are counting files and reporting scope | Wait for periodic progress updates |
| Estimation complete | Ready to start classification | Review results and start classification |
| Estimation cancelled | Admin cancelled the estimation | Create a new scan if needed |
| Estimation failed | An error occurred | Check device health and requirements |

### Classification phase

| Status | Meaning | Action |
| --- | --- | --- |
| Classification in progress | Files are being scanned and classified | Monitor progress |
| Classification complete | All devices finished | Review results in the **Items for review** tab |
| Classification cancelled | Admin cancelled classification | Already-classified files are preserved |
| Classification failed | An error occurred | See troubleshooting sections below |

## Understanding device statuses

| Status | Meaning | Action needed |
| --- | --- | --- |
| Active | Device responded recently, scanning normally | No |
| Not responding | No recent signals. The device is likely offline or powered down. A device that's once marked not responding won't participate any further in the scan. | No |
| Completed | Device finished its portion of the scan | No |
| Paused | Device reached the data discovery bandwidth limit | Resumes automatically after the period resets |

Each device has a signal validity threshold. If a device doesn't send any event within this window, it's marked as "Not responding" and is out of scope for the scan.

Note

"Not responding" doesn't indicate a device failure. It typically means the device is offline. Common reasons: device powered off, user on leave, device on a different network.

## Interpreting results

After classification completes:

| Metric | What it means |
| --- | --- |
| Files classified | Files actively scanned and classified (billable) |
| Previously classified files | Files with existing verdicts retained without rescanning, or already covered by another active scan |
| Files failed | Files that couldn't be classified (encrypted, locked). Not billed. |
| Files skipped | Files not found on the system (deleted before the scan moved to the classification phase), empty extracted text in small files, label- or password-protected files, and text extraction or format detection errors |

### Understanding result number differences

| Metric | What it counts | When it updates |
| --- | --- | --- |
| Items found (estimation) | Total files matching your scope and filters | During estimation |
| New matches (classification) | Files actively scanned, a subset of items found | During classification |
| Items for review (portal tab) | Classified items that matched at least one classifier | During and after classification |
| Audit log entries | Events logged per classification action | After classification, with possible delay |

Note

Items found ≠ items classified. Items found is the estimation-phase count (all files in scope). Items classified is the classification-phase count (files actually scanned, minus previously classified and failed files). The difference is primarily due to previously classified files.

Note

Items for review ≠ audit log count. These use different data sources and may show slightly different numbers. A small discrepancy is normal.

Skipped file counts are only finalized during the classification phase, not during estimation.

Note

Endpoint on-demand classification scan results don't flow into Content Explorer. Review results from the **Items for review** tab on the scan.

## Troubleshooting

### Quick reference

| Symptom | Likely cause | Solution |
| --- | --- | --- |
| Item count appears to drop or reset mid-scan | Previously classified files are deducted from the live classified count | Expected behavior. The final count reflects net new classifications, not a scan restart. |
| Device shows "Not responding" | No recent signals | Device is offline. This device won't be part of the current scan. |
| Estimation stuck at x% | Outdated Sense/Defender client on devices | Upgrade to the latest Sense/Defender client through Windows Update |
| Very low file count | Bandwidth limit reached | Expected. Wait for the bandwidth period to reset. |
| High failure count | File access errors | See error categories below |
| Unexpected rescanning | Classifiers changed | Finalize classifiers before starting scans |

### Classification errors

Failed files aren't billed. Common error categories:

| Category | Examples | Solution |
| --- | --- | --- |
| Access errors | Access denied, cloud file placeholder not available locally | Check file permissions; sync cloud files locally |
| Encryption errors | File encrypted, password-protected, BitLocker locked volume | Expected. Encrypted files can't be classified. |
| Format errors | File type not supported, corrupt file | Check file extension filters; no action needed for corrupt files |
| Lock errors | File locked by another application | Transient. File is retried on the next scan. |
| I/O errors | File or path not found (deleted or moved during scan) | No action needed |
| System errors | Local scan database full, unexpected error | Check disk space; restart device and retry |

Note

A small percentage of file failures is normal. Investigate only if failure counts indicate a systemic issue such as permissions problems across many files.

### Estimation shows different numbers than classification

This is expected. Estimation counts all files in scope. Classification skips previously classified files that already have valid verdicts, and some devices may be offline during classification. Estimation provides an upper bound; the actual classification volume is typically lower.

### Agent downgrades

If the endpoint agent (Defender/Sense client) is downgraded or rolled back while a scan is active, scan progress may be affected. Coordinate agent updates with your scan schedule.

### Scan not appearing in the portal

In some environments, backend provisioning may be required before the feature appears. Verify your tenant's licensing and that endpoint DLP is enabled with devices onboarded. If all prerequisites are met, contact Microsoft Support for backend enablement.

## Where to find diagnostic information

| Information | Location |
| --- | --- |
| Scan progress and status | Purview portal → On-demand classification → your scan |
| Classified items with matches | Items for review tab |
| Audit trail of scan events | Unified audit log |
| Failed file count | Scan summary |

## When to contact support

Contact Microsoft Support if:

- Scans fail repeatedly with system errors across multiple devices.
- Estimation doesn't progress despite devices being online and meeting requirements.
- Billing charges don't match expected classification volume.