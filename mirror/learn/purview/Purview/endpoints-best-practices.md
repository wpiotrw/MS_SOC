---
layout: Conceptual
title: Best practices for on-demand classification on endpoints and billing - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoints-best-practices
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Plan large-scale on-demand classification scans on Windows endpoints and optimize usage in Microsoft Purview.
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-20T00:00:00.0000000Z
audience: ITPro
ms.topic: best-practice
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- tier1
- M365-security-compliance
search.appverid:
- MET150
locale: en-us
document_id: 365fe754-870e-3e97-0939-01bdc41050d7
document_version_independent_id: 365fe754-870e-3e97-0939-01bdc41050d7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoints-best-practices.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoints-best-practices
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoints-best-practices.md
platformId: 92d723f0-cdba-5b3e-1640-e1354abddc11
---

# Best practices for on-demand classification on endpoints and billing - Microsoft Purview | Microsoft Learn

Understand how to plan large-scale scans and how to optimize usage.

## Billing model

On-demand classification uses a pay-as-you-go billing model. You're billed only for files that are actively classified. Previously classified files, skipped files, and failed files aren't billed. Usage is reported in the **Microsoft Purview Usage Center**, and charges appear on your Azure subscription bill.

For current pricing and licensing, see [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/).

## Previously classified files

When a file has already been classified and neither the file content nor the classifiers have changed, the existing classification result is retained on subsequent scans without rescanning. This applies to files classified by prior on-demand scans, as well as files classified by real-time Endpoint DLP when advanced classification is enabled.

### Conditions for previously classified files

Note

Reuse of previously classified verdicts requires that the earlier scan used advanced classification. For Endpoint DLP, advanced classification must be enabled on the DLP policy for its verdicts to be reusable by later on-demand scans.

A file qualifies as previously classified when all the following are true:

- File content unchanged since last verdict.
- The classifiers in the current scan are the same as, or a subset of, the classifiers used in the original scan, and those classifiers are unchanged.
- Classifier definitions unchanged.
- The device has the latest Windows cumulative updates installed.

Previously classified results apply across: on-demand → on-demand, on-demand → Endpoint DLP, and Endpoint DLP → on-demand.

### Previously classified files are visible in results

Previously classified files appear in scan results and audit logs under classification status. The file was evaluated and the existing verdict was confirmed. It doesn't mean the file was skipped or removed from results; it only wasn't rescanned.

Important

Previously classified file recognition isn't retroactive. It only applies to scans run after the required Windows update version 10.8821 is installed. Scans completed before this update aren't eligible. Your first post-update scan establishes the baseline for all future scans.

## What affects scan volume

| Reduces rescanning | Increases rescanning |
| --- | --- |
| Previously classified files on repeat scans | Changing classifiers between scans |
| Files already classified by Endpoint DLP (cross-path) | Large number of new or modified files |
| Narrowing file scope with date range and file type filters | Broad file scope (more file types, longer date ranges) |

## Estimation accuracy over time

An estimate stays representative for a limited window from the day estimation started. Within this window, the estimated file count closely reflects what classification will process. You can still start classification later, but expect higher variance in file counts as files on devices are added, modified, or deleted over time.

A common scenario: an administrator runs estimation, submits the projected scope for budget approval, and the approval cycle takes weeks. If estimation itself also drags out (for example, waiting for slow-responding devices to reach 100%), the combined delay can push classification past the window where the estimate stays representative.

### How to keep the estimate accurate

- **Start with a pilot.** Run a small pilot scan (10–20 users) first to get per-user data for the approval process.
- **Start classification early.** Don't wait for estimation to reach 100%. Starting at 80–90% progress is recommended. Devices that have completed estimation begin classification immediately.
- **Run estimation and classification back-to-back** if your organization is comfortable with the projected scope.

## Best practices for large-scale scans

### Finalize classifiers first

Finalize your sensitive information types and trainable classifiers before starting a scan. Changing classifiers during or between scans invalidates previously classified files and increases rescanning.

Tip

Establish a change-freeze period for classifiers before large scans. Coordinate with your team to ensure that SIT and trainable classifier changes are paused until the scan completes.

### Start with a phased rollout

| Phase | Scope | Goal |
| --- | --- | --- |
| **Phase 1** | 10–20 users | Validate the scan works and understand per-device timing. Complete the full cycle from start estimation to complete classification. |
| **Phase 2** | 50–100 users | Identify device issues and gather per-user data. Complete the full cycle from start estimation to complete classification. |
| **Phase 3** | Full rollout | Scale to all target users with known expectations. Complete the full cycle from start estimation to complete classification. |

The more devices in your scan, the more files are processed in parallel.

### Batch large tenants

For organizations with thousands of users, consider batching scans into groups of users per scan. This approach keeps each scan within the estimation accuracy window, allows batches to run in parallel, and makes it easier to track progress per batch.

Note

A device can only be part of one active scan at a time. Before adding a device to a new estimation or classification scan, ensure its previous scan has reached Classification Complete, Classification Cancelled, or Estimation Cancelled state.

### Handle offline devices

In any large scan, some devices will be offline. Don't wait for 100% device coverage. Run a follow-up scan later to catch devices that missed the first round. Previously classified files aren't rescanned, so the follow-up scan only processes newly scanned files.

## After the scan

- Download scan reports promptly; they're retained for a limited period of 30 days.
- Plan regular scans (monthly or quarterly) to keep classification current if the classifiers are changed or policy has been modified, since previously classified files aren't rescanned.

## Key considerations

- The estimation phase reads only metadata. You can assess scope before committing to classification.
- Subsequent scans typically process fewer files than the initial scan because previously classified files with unchanged content and classifiers aren't rescanned.
- Classification runs on the device. Only classification results and metadata are sent to the Microsoft Purview service.
- On-demand classification uses the same classifiers and Microsoft Purview portal as your existing compliance solutions.