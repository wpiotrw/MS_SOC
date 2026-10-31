---
layout: Conceptual
title: Email threading in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-email-threading
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: When conducting an eDiscovery (Premium) analysis, email threading parses an email conversation and separates each message into different categories.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 655f6558-e312-bfc7-acf7-dc2b26dc4050
document_version_independent_id: 655f6558-e312-bfc7-acf7-dc2b26dc4050
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-email-threading.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-email-threading
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-email-threading.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: ba95df16-632f-9ce2-300f-1c1e89d4130a
---

# Email threading in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Consider an email conversation that has been going on for a while. In most cases, the last message in the email thread includes the contents of all the preceding messages. Therefore, reviewing the last message gives a complete context of the conversation that happened in the thread. Email threading identifies such messages so that reviewers can review a fraction of collected documents without losing any context.

## What does email threading do?

Email threading in eDiscovery refers to the process of organizing a sequence of related emails that are part of the same conversation. This includes the initial email and all subsequent replies and forwards linked to that original email. By grouping these emails into threads, reviewers can see the entire context of a conversation, making it easier to understand the flow of communication. This approach helps identify relevant information more efficiently, as it eliminates the need to review each email individually. Email messages post analytics process can have the following metadata populated:

- **Is Inclusive**: This field identifies whether an email contains all the unique content from a thread, including all previous replies. It ensures that only the most comprehensive email in a thread is reviewed, which is essential for understanding the full context of the conversation without having to review each individual reply.
- **Has Unique Attachments**: This field marks emails that contain attachments not found in other emails within the same thread. Even if the email content is duplicated, unique attachments are flagged to ensure that all relevant documents are reviewed. This is important in the legal review process to ensure that no unique evidence is overlooked, even if the email body itself is not unique.

## How is it different from conversations in Outlook?

At a glance, this sounds similar to conversation groupings in Outlook. However, there are some important distinctions. Consider an email conversation that got forked into two conversations; for instance, someone responded to an email that isn't the latest in the conversation so the last two emails in the conversation both have unique content.

Outlook would still group the emails into a single conversation; reading only the last email would mean missing the context of the second-to-last email, which also contains unique content. Because email threading parses out each email into individual components and compares them, email threading would mark both of the last two emails as inclusive, ensuring that you won't miss any context as long as you read all emails marked as inclusive.

Let's also consider an email thread with multiple replies, where some replies include inline responses that modify the quoted content. If an inline reply alters part of the previous email, the latest reply doesn't fully encompass the content of the earlier email. Both the latest reply and the earlier email with unique content are marked as inclusive. This approach ensures that any unique information from the inline reply is preserved and not overlooked.