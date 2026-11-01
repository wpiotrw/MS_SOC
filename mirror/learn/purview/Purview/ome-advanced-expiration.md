---
layout: Conceptual
title: Set an expiration date for email encrypted by Microsoft Purview Advanced Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome-advanced-expiration
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: Use Microsoft Purview Advanced Message Encryption to extend your email security by setting an expiration date on emails through a custom branded template.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: a49ddf85-9cdc-8d7c-25da-12f71dee136e
document_version_independent_id: a49ddf85-9cdc-8d7c-25da-12f71dee136e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome-advanced-expiration.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome-advanced-expiration
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome-advanced-expiration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 747bfd8b-affa-1a60-640b-5bf965c92ec9
---

# Set an expiration date for email encrypted by Microsoft Purview Advanced Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

You can use message expiration on emails that your users send to external recipients who use the OME Portal to access encrypted emails. You force recipients to use the OME portal to view and reply to encrypted emails sent by your organization by using a custom branded template that specifies an expiration date in PowerShell.

When you apply your company brand to customize the look of your organization's email messages, you can also specify an expiration for these email messages. With Microsoft Purview Advanced Message Encryption, you can create multiple templates for encrypted emails that originate from your organization. Using a template, you can control how long recipients have access to mail sent by your users.

When an end user receives mail that has an expiration date set, the user sees the expiration date in the wrapper email. If a user tries to open an expired mail, an error appears in the OME portal.

You can only set expiration dates for emails to external recipients.

With Microsoft Purview Advanced Message Encryption, anytime you apply custom branding, Microsoft 365 applies the wrapper to email that fits the mail flow rule to which you apply the template. You can only use expiration if you use custom branding.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Create a custom branding template to force mail expiration by using PowerShell

To create a custom branding template that forces mail expiration, complete the following steps.

1. Using a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, start a Windows PowerShell session and connect to Exchange Online. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the New-OMEConfiguration cmdlet.

    ```powershell
    New-OMEConfiguration -Identity "Expire in 7 days" -ExternalMailExpiryInDays 7
    ```

Where:

- `Identity` is the name of the custom template.
- `ExternalMailExpiryInDays` identifies the number of days that recipients can keep mail before it expires. You can use any value between 1–730 days.