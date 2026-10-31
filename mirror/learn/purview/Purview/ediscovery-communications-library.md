---
layout: Conceptual
title: Manage custodian communications templates in the Communications library in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-communications-library
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can add custodian communications templates (such as a template for hold notification) in eDiscovery (Premium) so they can be used in any case in your organization.
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
document_id: 3d396f58-0ac6-f44a-9b95-667d6b12a3b9
document_version_independent_id: 3d396f58-0ac6-f44a-9b95-667d6b12a3b9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-communications-library.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-communications-library
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-communications-library.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 8ede3a5c-26ed-3028-a5ae-c71bbf45bd34
---

# Manage custodian communications templates in the Communications library in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When you or other users create a hold notification or other types of custodian communications, you had to create the communication document from scratch by using the communications editor on the **Communications** tab in an eDiscovery (Premium) case. Now, we've released a new feature that lets you create communications templates that can be used to create communications in any case in your organization. After communication templates are created, they're available to be used in a case. This means that paralegals or other users who create custodian communications don't have to start from scratch to build a notification. Instead, they can select a template to build the notification that is sent to a custodian.

This article explains how to create organization-wide communications templates and select them when creating a new custodian notification for a specific eDiscovery (Premium) case.

## Before you create templates in the Communications library

- You must be an eDiscovery Administrator in your organization to add or remove templates in the Communications library in eDiscovery (Premium). For more information, see [Assign eDiscovery permissions in the Microsoft Purview portal](ediscovery-assign-permissions)
- Your organization can have a maximum of 50 templates in the Communications library.

## Create a communications template

1. In the Microsoft Purview portal, go to [eDiscovery (Premium)](https://go.microsoft.com/fwlink/p/?linkid=2173764), and then select **eDiscovery (Premium) settings**.

    ![Select eDiscovery (Premium) settings](media/historicalversions1.png)
2. On the **Settings** page, select the **Communications library** tab.
3. On the **Communications library** page, select **Create**.
4. Follow the procedure to create a custodian communication. For step-by-step instructions, see [Create a legal hold notification](ediscovery-create-hold-notification).

    Note

    The steps to create a communications template are the same as the workflow to create a notification within a case. The only difference is that when you create a template, you don't specify an issuing officer and you don't assign custodians. Specifying an issuing officer and assigning custodians is done when you use a communications template to create a custodian notification for a case.
5. After you create a template, it's displayed on the **Communications library** page.

    ![Templates displayed in Communications library](media/aedcommunicationslibrary1.png)

You or other eDiscovery Administrators can edit a communications template. Any changes that you make to a template don't affect or modify any notifications that were previously created using that template. These changes will only apply to new notifications that created using the updated template.

## Use a communications template to create a custodian notification

After one or more communications templates are created in the Communications library, these templates can be selected to create a custodian notification in a case.

To select a template:

1. In the Microsoft Purview portal, go to **eDiscovery &gt; Premium** to display the list of cases in your organization.
2. Select a case, select the **Communications** tab, and then select **New communication**.
3. On the **Name communication** page, use the **Select communication template** drop-down list to select a communications template to use to create the custodian notification.

    The list of templates in your organization's Communication library is displayed in the drop-down list.

    ![Templates from Communications library displayed in the drop-down list.](media/aedcommunicationstemplates1.png)