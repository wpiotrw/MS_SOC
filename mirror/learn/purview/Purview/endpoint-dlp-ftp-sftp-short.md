---
layout: Conceptual
title: Protect FTP/SFTP Transfers in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-ftp-sftp-short
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Endpoint data loss prevention (DLP) in Microsoft Purview can monitor and protect sensitive data that users transfer over FTP and SFTP from managed Windows devices.
author: pan11gadi
ms.author: pangadi
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.topic: how-to
ms.collection:
- purview-compliance
ms.date: 2026-10-16T00:00:00.0000000Z
ai-usage: ai-generated
ms.custom: msecd-doc-authoring-1023
locale: en-us
document_id: 6987b5fc-1fb5-aaf0-9639-6c3be8e93100
document_version_independent_id: 6987b5fc-1fb5-aaf0-9639-6c3be8e93100
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-ftp-sftp-short.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-ftp-sftp-short
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-ftp-sftp-short.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: c30d2315-3e8b-c5c0-061e-2ed1c045435e
---

# Protect FTP/SFTP Transfers in Microsoft Purview | Microsoft Learn

Endpoint data loss prevention (DLP) in Microsoft Purview can monitor and protect sensitive data transferred over FTP and SFTP from managed Windows devices. Endpoint DLP evaluates these transfers against your policy rules, just as it does other device activities such as copying to USB devices or network shares. You can review the resulting events in Activity explorer.

This article explains how to add FTP and SFTP transfers to an Endpoint DLP policy rule and review the resulting events.

Before you begin, review the device onboarding and permissions requirements in Prerequisites.

## Prerequisites

- Devices onboarded to Microsoft Purview.
- Permissions to [create and deploy DLP policies](dlp-create-deploy-policy#permissions) and [view Activity explorer](data-classification-activity-explorer#permissions). Use the least-privileged roles needed for these tasks.

## Create the policy

We recommend starting with a small pilot group and setting the action to Audit only. Review Activity explorer to understand how users transfer files over FTP/SFTP before you deploy the policy broadly.

To create the policy:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to Data loss prevention &gt; Policies &gt; Create policy.
2. On the Locations page, select Devices, and then scope the policy to the users or device groups you want.
3. Create a rule, and add the conditions you want to detect, such as sensitive information types or sensitivity labels.
4. Under Actions, select Audit or restrict activities on devices.
5. In File activities for all apps, select Apply restrictions to specific activity.
6. Select the FTP and SFTP transfers checkbox, and then choose an action. Supported actions are Audit only, Block, Block with override, and Allow.
7. (Optional) Turn on policy tips under User notifications.
8. Review and publish the policy.

The Create rule page shows FTP and SFTP transfers selected with its action set to Block.

[![Screenshot of a device DLP rule highlighting FTP and SFTP transfers selected with the Block action.](media/endpoint-dlp-ftp-sftp/ftp-sftp-rule-block.png)](media/endpoint-dlp-ftp-sftp/ftp-sftp-rule-block.png#lightbox)

## End-user notification

Example of an end-user notification for a blocked FTP transfer:

[![Screenshot of a data loss prevention notification informing a user that an FTP file transfer is not allowed.](media/endpoint-dlp-ftp-sftp/ftp-sftp-end-user-notification-inline.png)](media/endpoint-dlp-ftp-sftp/ftp-sftp-end-user-notification.png#lightbox)

## Review activity

Use Activity explorer to review the details of each transfer.

1. Open Activity explorer.
2. Filter Activity to File transfer by FTP/SFTP. Review the user, device, file, matched policy, and action for each transfer.

## Collect full file evidence

FTP and SFTP transfers support full file evidence (FFE) collection. Enable evidence collection in Endpoint DLP settings and configure it in your DLP policy. When a user attempts to transfer a matched file, a complete copy can be saved.

For requirements and setup, see [Get started with evidence collection for file activities on devices](dlp-copy-matched-items-get-started).