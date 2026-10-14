---
layout: Conceptual
title: Alerts in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/alerts
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how view, create, and customize alerts in Windows 365.
keywords: 
author: Scottduf
ms.author: scottduf
manager: dougeby
ms.date: 2026-03-24T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: feadebay
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 5e0db96e-8a6b-600d-cda4-d415240d994e
document_version_independent_id: 5e0db96e-8a6b-600d-cda4-d415240d994e
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/alerts.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/alerts
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/alerts.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 055820ea-5783-d23c-1d4e-72684afa8788
---

# Alerts in Windows 365 | Microsoft Learn

The Windows 365 Alerts system notifies you when specific events occur in your Cloud PC environment, like connection, provisioning, or image upload failures. There are also alerts to notify you when you've reached or passed the maximum concurrency threshold for Windows 365 Flex Cloud PCs or when pooled user storage is running low for User Experience Sync. By default, alerts appear in the Microsoft Intune admin center as pop-up notifications (you can also turn on email notifications). You can customize the built-in alert rules:

- Set conditions and thresholds for triggering alerts.
- Define the severity of alerts.
- Turn each alert rule on or off.
- Configure each alert to notify you in the console and/or by email.

If emails are turned on, when an alert rule is triggered, one email is sent to the designated email address. After the alert is resolved, if it's triggered again, another email is sent to the designated address.

## Requirements

To see alerts, your account must meet the following requirements:

- Windows 365 Enterprise
- One of the following roles:
    - Intune Administrator
    - Windows 365 Administrator

## View alerts

To view the list of recent alerts, sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) &gt; **Tenant administration** &gt; **Cloud PC Alerts**.

![Screenshot of view alerts](media/alerts/view-alerts.png)

### Filters

By default, only active alerts are shown. You can use the **Add filter** option to filter by:

- Severity
    - Informational
    - Warning
    - Critical
- State
    - Active
    - Resolved

### Alert summary

You can select an alert from the list to see a summary of that alert.

![Screenshot of view alert.](media/alerts/alert-summary.png)

Select the link next to **Reports** to see more details.

## Customize alert rule

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) &gt; **Tenant administration** &gt; **Cloud PC Alerts** &gt; **Alert rules**.

    ![Screenshot of view alert rules.](media/alerts/view-alert-rules.png)
2. Select a rule from the list.
3. On the **System rule** page, make any changes that you want in the **Conditions**, **Settings**, and **Notifications** sections.

    ![Screenshot of system rule.](media/alerts/system-rule.png)
4. Select **Apply** to save the changes to the rule.