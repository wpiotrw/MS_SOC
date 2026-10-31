---
layout: Conceptual
title: Work with communications in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-managing-custodian-communications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: eDiscovery (Premium) makes it easy to manage the legal hold notification workflow around notifying custodians in legal investigations.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 92365529-8795-dcf6-34b0-c0c0bfcca7dd
document_version_independent_id: 92365529-8795-dcf6-34b0-c0c0bfcca7dd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-managing-custodian-communications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-managing-custodian-communications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-managing-custodian-communications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: ee10ca7d-00f9-d87e-3e79-3efdc43c06f4
---

# Work with communications in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Microsoft Purview eDiscovery (Premium) allows legal departments to simplify their processes around tracking and distributing legal hold notifications. The custodian communications tool enables legal departments to manage and automate the entire legal hold process, from initial notifications, to reminders, and to escalations, all in one location.

## What is a legal hold notification?

A legal hold (also known as a *litigation hold*) notice is a notification sent from an organization’s legal department to employees, contingent staff, or custodians of data that may be relevant to a legal investigation. These notifications instruct custodians to preserve electronically stored information and any content that may be relevant to an active or impending legal matter. Legal teams must know that each custodian has received, read, understood, and has agreed to comply with the given instructions.

## The legal hold notification process

An organization has a duty to preserve relevant information when it learns about an impending litigation or regulatory investigation. To comply with the preservation requirements of an investigation, the organization should immediately inform potential custodians about their duty to preserve relevant information.

With eDiscovery (Premium), legal teams can create and customize their legal hold notification workflow. The custodian communications tool lets legal teams configure the following notices and workflows:

1. **Issuance notice:** A legal hold notice is issued (or initiated) by a notification from the legal department to custodians who may have relevant information about the case matter. This notice instructs the custodians to preserve any information that may be needed for discovery.
2. **Re-Issuance notice:** During a case, custodians may be required to preserve more content (or less content) than was previously requested. For this scenario, you can update the existing hold notice and reissue it to custodians.
3. **Release notice:** Once a matter is resolved and the custodian is no longer subject to a preservation requirement, the custodian can be released from the case. Additionally, you can notify the custodian that they’re no longer required to preserve content, and provide instructions about how to resume their normal work activity and their data.
4. **Reminders and escalations:** In some instances, just issuing a notice isn't enough to satisfy legal discovery requirements. With each notification, legal teams can schedule a set of reminder and escalation workflows to automatically follow up with unresponsive custodians.

    - **Reminders:** After a legal hold notice has been issued or reissued to a set of custodians, an organization can set up reminders to alert unresponsive custodians.
    - **Escalations:** In some cases, if a custodian remains unresponsive even after a set of reminders over a period of time, the legal team can set up an escalation workflow to notify unresponsive custodians and their manager.

For more information about managing the custodian communication process, see the following:

- [Create a legal hold notice](ediscovery-create-hold-notification)
- [Use the communications editor](ediscovery-using-communications-editor)
- [Manage hold notifications](ediscovery-manage-hold-notifications)
- [Acknowledge a hold notification](ediscovery-acknowledge-hold-notification)