---
layout: Conceptual
title: Get started with eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-premium-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to get started eDiscovery (Premium) so you can start creating and managing cases. It also describes the required Microsoft subscriptions and licensing. After you complete a few quick steps, the eDiscovery (Premium) tool is ready to use.
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
- highpri
- purview-compliance
- m365solution-aed
- m365solution-scenario
- highpri
- ediscovery
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: ca3916fa-21df-831d-302d-5de5220956b1
document_version_independent_id: ca3916fa-21df-831d-302d-5de5220956b1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-premium-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-premium-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-premium-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: ee3b8bcc-c714-c62a-942a-2356805888d1
---

# Get started with eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Microsoft Purview eDiscovery (Premium) provides an end-to-end workflow to preserve, collect, review, analyze, and export data that's responsive to your organization's internal and external investigations. Nothing is needed to deploy eDiscovery (Premium), but there are some prerequisite tasks that an IT admin and eDiscovery manager have to complete before your organization can start to create and use eDiscovery (Premium) cases to manage your investigations.

This article discusses the following steps necessary to set up eDiscovery (Premium).

![Steps to set up eDiscovery (Premium).](media/set-up-advanced-ediscovery.png)

This includes ensuring the proper licensing required to access eDiscovery (Premium) and add custodians to cases, and assigning permissions to your legal and investigation team so they can access and manage cases.

## Step 1: Verify and assign appropriate licenses

Microsoft Purview eDiscovery capabilities are included with Microsoft Purview. The licensing requirements may vary even within capabilities, depending on configuration options. For licensing requirements, guidance, and options, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for eDiscovery (Premium).

## Step 2: Assign eDiscovery permissions

To access eDiscovery (Premium) or added as a member of an eDiscovery (Premium) case, a user must be assigned the appropriate permissions. Specifically, a user must be added as a member of the eDiscovery Manager role group in the Microsoft Purview portal. Members of this role group can create and manage eDiscovery (Premium) cases. They can add and remove members, place custodians and content locations on hold, manage legal hold notifications, create and edit searches associated in a case, add search results to a review set, analyze data in a review set, and export and download from an eDiscovery (Premium) case.

For step-by-step guidance to configure permissions for eDiscovery, see [Assign eDiscovery permissions](ediscovery-assign-permissions).

## Step 3: Configure global settings for eDiscovery (Premium)

The last step to complete before people in your organization start to create and use cases is to configure global settings that apply to all cases in your organization. At this time, the only global setting is *attorney-client privilege detection* (more global settings will be available in the future). This setting enables the attorney-client privilege model to run when you analyze data in a review set. The model uses machine learning to determine the likelihood that a document contains content that is legal in nature. It also compares the participants of documents with an attorney list (that you submit when setting up the model) to determine if a document has at least one participant who is an attorney.

For more information about setting up and using the attorney-client privilege detection model, see [Set up attorney-client privilege detection in eDiscovery (Premium)](ediscovery-attorney-privilege-detection).

Note

This is an optional step that you can perform anytime. Not implementing the attorney-client privilege detection model doesn't prevent you from creating and using eDiscovery (Premium) cases.

## Step 4: Verify that required eDiscovery apps are enabled

eDiscovery (Premium) requires the following Enterprise apps to be enabled in your Microsoft 365 or Office 365 organization. If these apps aren't enabled, you won't be able to access all eDiscovery (Premium) view, filter, and search features.

| App | App ID |
| --- | --- |
| Built-in security add-on for on-premises mailboxes (formerly Exchange Online Protection) | 00000007-0000-0ff1-ce00-000000000000 |
| ComplianceWorkbenchApp | 92876b03-76a3-4da8-ad6a-0511ffdf8647 |
| MicrosoftPurviewEDiscovery | b26e684c-5068-4120-a679-64a5d2c909d9 |
| Office365Zoom | 0d38933a-0bbd-41ca-9ebd-28c4b5ba7cb7 |

Note

The *MicrosoftPurviewEDiscovery* app provides support for exporting data via scripts in eDiscovery (Premium). For more information about exporting data via scripts, see [Get caseOperation](/en-us/graph/api/security-caseoperation-get?view=graph-rest-1.0).

For more information about how to view and enable apps, see:

- [Quickstart: View enterprise applications](/en-us/azure/active-directory/manage-apps/view-applications-portal)
- [Quickstart: Add an enterprise application](/en-us/azure/active-directory/manage-apps/add-application-portal)