---
layout: Conceptual
title: FAQ and reference for endpoint scans - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoints-faq-reference
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Answers to common questions and key terms for on-demand classification for Windows endpoints in Microsoft Purview.
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-20T00:00:00.0000000Z
audience: ITPro
ms.topic: faq
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- tier1
- M365-security-compliance
search.appverid:
- MET150
locale: en-us
document_id: ef5653f0-8466-13db-4717-1be6230910b5
document_version_independent_id: ef5653f0-8466-13db-4717-1be6230910b5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoints-faq-reference.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoints-faq-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoints-faq-reference.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 03926d7c-a79e-71d9-e172-1dbfaae9cd50
---

# FAQ and reference for endpoint scans - Microsoft Purview | Microsoft Learn

Answers to common questions and key terms for on-demand classification for Windows endpoints in Microsoft Purview.

## General

### Does on-demand classification apply sensitivity labels to files?

No. On-demand classification identifies and classifies sensitive content but doesn't apply sensitivity labels. To apply labels based on classification results, configure auto-labeling policies.

### Is on-demand classification required for Endpoint DLP to work?

No. Endpoint DLP works independently and classifies files in real time when they're created, modified, or used. On-demand classification is a separate, complementary capability that covers historical files at rest.

### Does on-demand classification affect the user experience on endpoints?

On-demand classification runs in the background with minimal resource usage. A per-device bandwidth limit ensures scanning doesn't degrade device performance.

### Does turning on a DLP policy automatically classify historical data?

No. DLP policies classify files when they're accessed, modified, or shared (real-time classification). Historical files that remain untouched aren't retroactively classified by DLP, however you can utilize JIT feature to prevent data loss. On-demand classification is required to cover those files.

## Classification and labeling

### Why was my file classified but not labeled?

Classification and labeling are separate steps. Classification identifies whether a file contains sensitive content. Labeling applies a sensitivity label based on classification results. For labels to be applied, configure auto-labeling policies.

### Does opening or editing a file trigger reclassification?

Yes, but through Endpoint DLP (real-time classification), not on-demand classification. When a file is modified, the Endpoint DLP engine reclassifies it automatically. On-demand classification runs only when an admin starts a scan.

### Do I need to rerun on-demand classification when I create a new SIT?

Yes, if you want historical files evaluated against the new SIT. Existing verdicts were created using the classifiers available at scan time. A new SIT isn't automatically applied to previously classified files. A new scan that includes the new SIT classifies the files against it.

## Cost and billing

### Is estimation billed?

No. Estimation is a metadata-only pass. The endpoint agent enumerates files and evaluates eligibility gates (file size, type, time window) and previously classified file potential, but doesn't read file contents or run classifiers. No charges are incurred during estimation.

### What is the billing model?

On-demand classification uses a pay-as-you-go billing model. You're billed only for files that are actively classified. Previously classified files and failed files aren't billed. For current pricing and licensing, see [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/).

### Will I be charged twice if I scan the same files again?

No. Files that haven't changed and use the same classifiers are recognized as previously classified files and aren't rescanned or billed.

### Why do I have to pay if DLP has already scanned the file?

If the file qualifies as previously classified, you don't. Files classified by real-time Endpoint DLP are recognized as previously classified during on-demand scans at no charge, if the file content and classifiers haven't changed. This is cross-path recognition.

### Why is my actual scan volume lower than the estimate?

The estimate shows an upper bound and assumes all files will be classified. Actual volume is lower because previously classified files aren't rescanned, some devices may be offline, and some files might be deleted before classification.

### How do I see my usage and charges?

Usage is reported in the Microsoft Purview Usage Center. Charges appear on your Azure subscription bill.

## Scans

### Can I cancel a running scan?

Yes. Already-classified files remain classified. Canceling doesn't undo completed work.

### Can I run multiple scans at the same time?

Yes. If a device is scoped by multiple active scans, the first scan is processed while the other scans are queued.

### Can I start classification before estimation reaches 100%?

Yes. Starting at 80–90% progress is recommended. The final 10–20% typically reflects slow-responding devices, and waiting for them can push the overall estimation phase past the window where the estimate stays representative. Devices that have completed estimation begin classification immediately, and remaining devices join as they finish.

### What happens if I change classifiers during a scan?

Changing sensitive information types or trainable classifiers during a scan invalidates the estimation. You should re-estimate before continuing to classification if you want the estimated and classified numbers to match.

### What files are excluded from scanning?

System folders are automatically excluded: the Windows directory, Program Files, legacy application data folders, and Windows Error Reporting data. On-demand classification scans user data directories such as Documents, Desktop, and Downloads.

## Devices

### Why does my device show "Not responding"?

The device hasn't sent signals for an extended period, currently cutoff limit is 48 hours. This typically means the device is powered off, hibernating, or not connected to the network.

### What are the device requirements?

Devices must be onboarded to Microsoft Purview endpoint DLP and have the latest Windows cumulative updates installed. For full device requirements, see [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started).

### Does on-demand classification work on macOS?

Not currently. macOS support is planned but no release date is available.

## Results

### Where can I see which files failed?

Individual failed files aren't listed in the portal or audit logs. The portal shows the total count of failed files. Review the error categories in [Monitor and troubleshoot endpoint scans](endpoints-monitor-troubleshoot) for common causes.

### Why don't audit log counts match Items for review counts?

Audit logs and the Items for review tab use different data sources and counting logic. Timing differences, deduplication, and filter differences can cause minor discrepancies. A small gap is normal.

### What is the difference between "skipped" and "failed" files?

| Status | Meaning | Billed |
| --- | --- | --- |
| Classified | File was scanned and classified | Yes |
| Previously classified | File was scanned previously and had a valid prior verdict | No |
| Skipped | Excluded by filters | No |
| Failed | Could not be scanned (encrypted, locked, access denied) | No |

## Previously classified files

### When are files not recognized as previously classified?

Files aren't recognized as previously classified when the file was earlier not classified using advanced classification, has been modified, classifier definitions have changed, or new classifiers were added that weren't in the original classification.

### Does this work between on-demand and Endpoint DLP?

Yes. Previously classified file recognition works across on-demand → on-demand, on-demand → Endpoint DLP, and Endpoint DLP → on-demand.

### Is previously classified file recognition retroactive?

No. Previously classified file recognition only applies to scans run after the required Windows update is installed. Your first post-update scan establishes the baseline for all future scans.

## Feature gaps

### Can I mark false positives in the scan results?

There's no built-in workflow to mark items as false positives directly within on-demand classification results. Export results and manage them externally, or report false positive SIT matches through your normal classifier tuning process.

### Does the portal show an estimated time remaining for scans?

No. The portal shows scan progress but doesn't provide an estimated time of completion.

### The on-demand classification option isn't visible in my portal. What should I do?

In some environments, backend provisioning may be required. Verify licensing and endpoint DLP onboarding. If all prerequisites are met, contact Microsoft Support for backend enablement.

## Key terms

| Term | Definition |
| --- | --- |
| On-demand classification | Admin-initiated scan that classifies sensitive content in files at rest on endpoints. |
| Estimation | First phase that enumerates files, evaluates eligibility gates, and checks previously classified file potential using metadata only. No file content is read. The estimate stays representative for a limited window from the day estimation started. |
| Classification | Second phase that scans files against classifiers and is billed under the pay-as-you-go model. |
| Verdict | Classification result stored on a file, recording which classifiers matched. |
| Previously classified files | Files with existing classification results from prior scans or classified by Endpoint DLP in real time. These files aren't rescanned or billed when content and classifiers are unchanged. Requires latest Windows updates. |
| Active data | Files frequently modified, accessed, or shared. Classified by Endpoint DLP in real time. |
| Inactive/historical data | Files at rest that haven't been recently modified. The target of on-demand classification. |