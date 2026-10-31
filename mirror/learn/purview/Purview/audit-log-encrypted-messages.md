---
layout: Conceptual
title: Encrypted message portal activity log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-encrypted-messages
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to track encrypted message activity with Microsoft Purview. Enable audit logs to monitor external user sign-ins, message reads, and forwards.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-audit
ms.date: 2026-03-23T00:00:00.0000000Z
ms.collection:
- purview-compliance
- audit
search.appverid:
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: b3459505-8a88-6672-9b0e-0cb24b2e383f
document_version_independent_id: b3459505-8a88-6672-9b0e-0cb24b2e383f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-encrypted-messages.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-encrypted-messages
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-encrypted-messages.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 52231aa7-0d67-624f-d40b-d0d03e480bc9
---

# Encrypted message portal activity log | Microsoft Learn

You can access logs for encrypted messages through the encrypted message portal. With these logs, your organization can determine when external recipients read and forward messages. To ensure availability of logs for external recipients, apply a custom branding template to protected emails that your organization sends to external recipients. This template enforces a portal experience. For more information, see [Add your organization's brand to your encrypted messages](add-your-organization-brand-to-encrypted-messages).

## Enable message access audit logs in PowerShell

You can enable the access log by using [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell). The *EnablePortalTrackingLogs* parameter of the **[Set-IrmConfiguration](/en-us/powershell/module/exchange/set-irmconfiguration)** cmdlet specifies whether to enable audit logs for accessing the encrypted message portal. Valid values are:

- $true: Turns on the audit feature.
- $false: Turns off the audit feature.

Example:

```powershell
Set-IrmConfiguration -EnablePortalTrackingLogs $true
```

For more information, see [Set-IRMConfiguration (ExchangePowerShell)](/en-us/powershell/module/exchange/set-irmconfiguration).

## Message access audit information

The access log contains entries for messages sent through the encrypted message portal for the following types of activity:

- External user sign-in timestamp and authentication method
- External user reading messages or attachments
- Attachment download
- Mail replies and forwards

For more information about the message access log schema, see [Audit log activities](audit-log-activities#encrypted-message-portal-activities).

## Search for events in the message access logs

Complete the following steps to get started with search:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select the **Audit** solution card. If the **Audit** solution card isn't displayed, select **View all solutions** and then select **Audit** from the **Core** section.
3. Under **Search**, select the drop-down for **Activities** and type encrypted message portal activities.
4. Under encrypted message portal activities, select the event types to use in the search. Set the date range for the search (default is the previous week), you can also optionally add a particular user in your organization for the search. When ready, select **Search**.
5. Select an event from the list to view the audit properties.