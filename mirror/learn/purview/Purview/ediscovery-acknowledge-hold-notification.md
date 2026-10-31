---
layout: Conceptual
title: Acknowledge a hold notification | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-acknowledge-hold-notification
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use eDiscovery (Premium) to send and follow up on legal hold notifications through email and monitor obligation status.
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
ms.assetid: 
ms.custom:
- seo-marvel-apr2020
locale: en-us
document_id: 4dfdd54d-9c91-7209-a797-b596a26b839c
document_version_independent_id: 4dfdd54d-9c91-7209-a797-b596a26b839c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-acknowledge-hold-notification.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-acknowledge-hold-notification
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-acknowledge-hold-notification.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 97a7cbbf-15e3-e031-52e3-19fe2fe77945
---

# Acknowledge a hold notification | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When responding to a regulatory request or investigation, you might need to inform custodians of their obligation to preserve electronically stored information (ESI) and any material that might be relevant to an active or imminent legal matter. After you send the notification, legal teams need to know that each custodian receives, reads, understands, and agrees to follow the given instructions.

To help reduce the time, cost, and effort of following up with your custodians, eDiscovery (Premium) enables you to send and follow up on legal hold notifications through email. In addition to email notices, each custodian can access an individualized Microsoft Purview portal, so custodians stay informed of changes to their obligation status.

## Email notifications

After you issue a Legal Hold Notification, each custodian receives a unique and personalized email containing your defined legal hold notice and added instructions.

Tip

To allow your custodians to acknowledge their notice or access their Microsoft Purview portal directly from their email, see how you can use the built-in [Communication Editor](ediscovery-using-communications-editor).

Based on the configuration of your legal hold notification, your custodians might receive the following notices:

- **Issuance notice:** The first notice you send to your custodian. This notice contains your issuance instructions and the hold notice appended to the end of your message.
- **Reminder notice:** If you enable this notice, your custodians receive a reminder notice based on the specified frequency and interval. The reminders continue to be sent either until the custodian acknowledges their notice or until the number of reminders is exhausted.
- **Escalation notice:** If you enable this notice, your custodian and their manager receive an escalation notice after the reminder notices are exhausted. The system automatically sends escalation notices until the specified number of escalations is completed or until the custodian acknowledges their hold notification.
- **Reissue notice:** During an investigation, if you update the contents of the hold notice, the updated notice is automatically sent to the custodian.
- **Release notice:** When you release a custodian from the case, you send the release notice to the custodian.

## Microsoft Purview portal

In addition to the email notifications, each custodian can access a unique Microsoft Purview portal. Through the Microsoft Purview portal, each custodian can view, access, and acknowledge their active hold notifications.