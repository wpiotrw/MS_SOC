---
layout: Conceptual
title: Manage issuing officers in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-issuing-officers
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can add organization-wide issuing officers in eDiscovery (Premium) so they can be added to any custodial communication in any case in your organization.
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
document_id: 39744a14-63a7-81a2-0eb6-c433916c70b3
document_version_independent_id: 39744a14-63a7-81a2-0eb6-c433916c70b3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-issuing-officers.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-issuing-officers
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-issuing-officers.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d681860e-0051-04e1-237b-0403d6da1a56
---

# Manage issuing officers in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When you or others create a hold notification or other type of communication that is sent to a user who is a custodian in case, you have to specify an issuing officer. The notification is sent to the custodian on behalf of the specified issuing officer. For example, a paralegal in your organization might be responsible for creating and sending hold notifications to custodians in a case. In this scenario, the paralegal can specify an attorney in the organization as the issuing officer. Who can be specified as an issuing officer? There are two types of users who can be selected as an issuing officer for a custodian communication:

- Any member of the specific case the communication is being sent in behalf of.
- Any user who is added to a list of organization-wide issuing officers. Users from this list can be added an issuing officer to any case in your organization.

This article explains how to add and remove users to the list of organization-wide issuing officers.

## Before you add an issuing officer

- You must be an eDiscovery Administrator in your organization to add or remove issuing officers. For more information, see [Assign eDiscovery permissions in the Microsoft Purview portal](ediscovery-assign-permissions)
- The user who is added as an issuing officer must have an active mailbox in your Microsoft 365 organization.
- Your organization can have a maximum of 15 issuing officers. Members of a case who can be specified as an issuing officer aren't counted toward this limit. This limit only applies to the number of users that can be added to the **Issuing officers** page in eDiscovery (Premium).

## Add an issuing officer

1. In the Microsoft Purview portal, go to [eDiscovery (Premium)](https://go.microsoft.com/fwlink/p/?linkid=2173764), and then select **eDiscovery (Premium) settings**.

    ![Select eDiscovery (Premium) settings](media/historicalversions1.png)
2. On the **Settings** page, select the **Issuing officers** tab to display the **Manage issuing officers** page.

    ![Issuing officers settings page.](media/aedissuingofficers1.png)
3. Select **Add** and then search for and add one or more users to the list of issuing officers.

After you add users as issuing officers, you or other users will be able to specify these users as an issuing officer for custodian communications for any case in your organization. For more information about creating custodian communications, see [Create a legal hold notice](ediscovery-create-hold-notification).

## Remove an issuing officer

1. In the Microsoft Purview portal, go to [eDiscovery (Premium)](https://go.microsoft.com/fwlink/p/?linkid=2173764), and then select **eDiscovery (Premium) settings**.
2. On the **Settings** page, select the **Issuing officers** tab.
3. Select one or more users in the issuing officers list, and then select **Delete**.

After you delete users from the list of issuing officers, those users can no longer be specified as an issuing officer in new custodian communications, unless the user is a member of the specific case the communication is being issued from. Also, removing an issuing officer won't affect any communications that were sent before the user was removed as an issuing officer.