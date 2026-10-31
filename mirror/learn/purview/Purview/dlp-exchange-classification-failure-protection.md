---
layout: Conceptual
title: Configure default protection for classification failures in DLP for Exchange | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-exchange-classification-failure-protection
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
ms.date: 2026-07-16T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
recommendations: false
description: Learn how to configure default protection for classification failures in data loss prevention for Exchange Online
ms.custom: sfi-image-nochange
locale: en-us
document_id: 56fde790-fedc-fc95-c5f5-a7ef7116186c
document_version_independent_id: 56fde790-fedc-fc95-c5f5-a7ef7116186c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-exchange-classification-failure-protection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-exchange-classification-failure-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-exchange-classification-failure-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 95341be4-ec4b-160b-2ea5-b14aeaab6119
---

# Configure default protection for classification failures in DLP for Exchange | Microsoft Learn

Microsoft Purview data loss prevention (DLP) policies for Exchange Online can detect and act on classification failures—cases where the classification service can't fully scan a document. This article shows you how to enable classification failure detection and use the improved conditions to apply protection actions for specific failure types, such as timeouts and throttling.

## Enable classification failure detection

To enable classification failure detection, you can update the setting in the Purview portal or use PowerShell. Allow up to one hour for the setting change to synchronize across the service before validating policy behavior.

Important

This setting applies to Exchange Online only. It doesn't affect SharePoint, OneDrive, Teams, or Endpoint DLP policies.

- **Purview Portal**: To access the setting, from the Microsoft Purview portal, go to **Settings** on the left navigation menu &gt; **Data loss prevention** &gt; **Scan failure settings for Exchange**. In **Scan failure settings for Exchange** turn on the toggle.
- **PowerShell**: Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) and run the following commands.

    ```powershell
    Connect-IPPSSession
    $json = '{"Classification":{"State":1}}'  # To disable, set State to 0
    Set-PolicyConfig -DlpErrorHandlingConfig $json
    ```

## Improved conditions for file attachments

By default, these conditions detect only text extraction failures. After you enable classification failure detection, they also detect classification failures such as timeouts, throttling, and other errors.

The following table compares each condition's capabilities before and after you enable classification failure detection.

| Condition | Default capabilities | Capabilities after you enable detection |
| --- | --- | --- |
| Document couldn't be scanned | Text extraction failures (for example, the file couldn't be opened, the format is unsupported, or the file is password protected). | All text extraction failures, plus Classification failures (for example, when the classification service can't complete scanning of a document because of a timeout, throttling, or another error). |
| Document didn't complete scanning | Partial text extraction (for example, content exceeded extraction limits). | Partial text extraction, plus partial classification failures—for example, when at least one classifier (sensitive information type, exact data match, or trainable classifier) succeeded, but one or more of the others failed because of a timeout, throttling, or another error. |

Note

If your tenant already has rules that use these conditions, you might see an increase in DLP rule matches after you enable detection.

To take different actions for specific classification failure types—**Timeout**, **Throttled**, or **Other**—use the **DocumentScanFailures** condition. Combine it with either **Document couldn't be scanned** or **Document didn't complete scanning** using AND; **DocumentScanFailures** can't be used on its own.

For the complete list of attachment conditions, see [Attachments](dlp-exchange-conditions-and-actions#attachments).

## Rule ordering

Scan-failure rules detect failures only from classifiers that DLP has already evaluated. If a content-detection rule is placed after a scan-failure rule and its classifier fails, the failure won't be detected.

To avoid missed detections, order your rules so that content-detection rules (sensitive information types, exact data matches, and trainable classifiers) have higher priority than scan-failure rules (Timeout, Throttled, Other):

- Content rules at priorities 1–3.
- Scan-failure rules at priorities 4–6.

The following table shows an example that follows this pattern.

| Priority | Rule | Condition | Action |
| --- | --- | --- | --- |
| 1 | Detect credit cards | Content contains Credit Card Number | Block |
| 2 | Detect account numbers | Content contains Account Number | Block |
| 3 | Detect EDM match | Content contains EDM SIT | Block |
| 4 | Full scan timeout | DocumentIsUnsupported AND DocumentScanFailures = Timeout | Audit |
| 5 | Partial scan throttling | ProcessingLimitExceeded AND DocumentScanFailures = Throttled | Audit |
| 6 | Other scan errors | DocumentIsUnsupported AND DocumentScanFailures = Other | Audit |