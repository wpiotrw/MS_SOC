---
layout: Conceptual
title: Overview of the eDiscovery (Premium) solution in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the eDiscovery (Premium) solution in Microsoft Purview. This article provides an overview of eDiscovery (Premium) in Microsoft Purview, a tool to help you manage internal and external investigations. It also frames the business reasons for using eDiscovery (Premium) to manage your legal investigations.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- m365solution-aed
- m365solution-overview
- highpri
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: f88a3e38-19be-ccf7-de91-4a63ac597dea
document_version_independent_id: f88a3e38-19be-ccf7-de91-4a63ac597dea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 5c181c32-3684-a5dd-0fd2-d8827b2abb5e
---

# Overview of the eDiscovery (Premium) solution in Microsoft Purview | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The Microsoft Purview eDiscovery (Premium) solution builds on the existing [Microsoft eDiscovery (Standard)](ediscovery-standard-get-started) and analytics capabilities. eDiscovery (Premium) provides an end-to-end workflow to preserve, collect, analyze, review, and export content that's responsive to your organization's internal and external investigations across Microsoft 365 and Office 365.

You can also use eDiscovery (Premium) to place an eDiscovery hold on content locations, such as Exchange mailboxes, SharePoint sites, OneDrive accounts, and Microsoft Teams. It also lets legal teams manage the entire legal hold notification workflow to communicate with custodians involved in a case.

## eDiscovery (Premium) capabilities

eDiscovery (Premium) can help your organization respond to legal matters or internal investigations by discovering data where it lives. You can seamlessly manage eDiscovery workflows by identifying persons of interest and their data sources, seamlessly apply holds to preserve data, and then manage the legal hold communication process. By collecting data from the source, you can search the live Microsoft 365 platform to quickly find what you need. Intelligent, machine learning capabilities such as deep indexing, email threading, and near duplicate detection also help you reduce large volumes of data to a relevant data set.

The following sections describe how these eDiscovery (Premium) capabilities can help your organization.

![eDiscovery (Premium) capabilities.](media/advanced-ediscovery-capabilities.png)

### Discover and collect data in-place

Traditionally, organizations that rely on multiple third-party eDiscovery solutions require copying large volumes of data out of Microsoft 365 to process and having to host duplicate data. This necessity increases the time to find relevant data and the risk, cost, and complexity of managing multiple solutions.

eDiscovery (Premium) in Microsoft 365 lets you discover data at the source and staying within your Microsoft 365 security and compliance boundary. By collecting data in-place from the live system, eDiscovery (Premium) reduces the friction of going back to the source and reduces unnecessary work of having to find missing content, which often happens when journaling lags in traditional eDiscovery solutions.

Native search and collection capabilities for data in Teams, Viva Engage, SharePoint Online, OneDrive for Business, and Exchange Online further enhances data discovery. For example, eDiscovery (Premium):

- Reconstructs Teams conversations (instead of returning individual messages from conversations).
- Collects cloud-based content shared with users by use of links or modern attachments in email message and Teams chats.
- Has built-in support for hundreds of non-Microsoft 365 file types.
- Collects data from third-party sources (such as Bloomberg, Facebook, Slack, and Zoom Meetings) that's imported and archived in Microsoft 365 by [data connectors](archive-third-party-data).

### Manage eDiscovery workflow in one platform

eDiscovery (Premium) can help you reduce the number of eDiscovery solutions you need to rely on. It provides a streamlined, end-to-end workflow, all which occurs within Microsoft 365. eDiscovery (Premium) helps reduce the friction of identifying and collecting potential sources of relevant information by automatically mapping unique and shared data sources to the person of interest (known as a *custodian*), and by providing reporting and analytics on potentially relevant data prior to collecting it for analysis and review.

Additionally, Microsoft Graph APIs can help you automate the eDiscovery workflow and extend eDiscovery (Premium) for custom solutions.

### Cull data intelligently

Intelligent, machine learning capabilities in eDiscovery (Premium) help you reduce the amount of data to review. These intelligent capabilities help you reduce and cull large volumes of data to a relevant set. For example, a built-in review set query helps filter only for unique content by identifying near duplicates. This capability can substantially reduce the amount of data to review.

Additional machine learning capabilities can further refine and identify relevant data using smart tags and technology assisted review tools like the Relevance modules.

## eDiscovery (Premium) alignment with the Electronic Discovery Reference Model

The built-in workflow of eDiscovery (Premium) in Microsoft 365 aligns with the eDiscovery process outlined by the Electronic Discovery Reference Model (EDRM).

![The Electronic Discovery Reference Model (EDRM).](media/edrmv2.png)

(Image based on the EDRM model on edrm.net)

At a high level, here's how eDiscovery (Premium) supports the EDRM workflow:

- **Identification.** After you identify potential persons of interest in an investigation, you can add them as custodians (also called *data custodians*, because they may possess information that's relevant to the investigation) to an eDiscovery (Premium) case. After users are added as custodians, it's easy to preserve, collect, and review custodian documents.
- **Preservation.** To preserve and protect data that's relevant to an investigation, eDiscovery (Premium) lets you place a legal hold on the data sources associated with the custodians in a case. You can also place non-custodial data on hold. eDiscovery (Premium) also has a built-in communications workflow so you can send legal hold notifications to custodians and track their acknowledgments.
- **Collection.** After you identified (and preserved) the data sources relevant to the investigation, you can use the built-in search tool in eDiscovery (Premium) search for and collect live data from the custodial data sources (and non-custodial data sources, if applicable) that may be relevant to the case.
- **Processing.** After you've collected all data relevant to the case, the next step is process it for further review and analysis. In eDiscovery (Premium), the in-place data that you identified in the collection phase is copied to an Azure Storage location (called a *review set*), which provides you with a static view of the case data.
- **Review.** After data has been added to a review set, you can view specific documents and run additional queries to reduce the data to what is most relevant to the case. Also, can annotate and tag specific documents.
- **Analysis.** eDiscovery (Premium) provides integrated analytics tool that helps you further cull data from the review set that you determine isn't relevant to the investigation. In addition to reducing the volume of relevant data, Advance eDiscovery also helps you save legal review costs by letting you organize content to make the review process easier and more efficient.
- **Production** and **Presentation.** When you're ready, you can export documents from a review set for legal review. You can export documents in their native format or in an EDRM-specified format so they can be imported into third-party review applications.

## Subscriptions and licensing

Microsoft Purview eDiscovery capabilities are included with Microsoft Purview. The licensing requirements may vary even within capabilities, depending on configuration options. For licensing requirements, guidance, and options, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for eDiscovery (Standard) and eDiscovery (Premium).

For information about how to assign licenses, see [Assign licenses to users](/en-us/microsoft-365/admin/manage/assign-licenses-to-users).

## Get started with eDiscovery (Premium)

There are two quick and easy steps to get started with eDiscovery (Premium).

![Workflow getting started with eDiscovery (Premium).](media/get-started-aed.png)

| Steps | Description |
| --- | --- |
| [Set up eDiscovery (Premium)](ediscovery-premium-get-started) | After verifying the subscription and licensing requirements, you can assign permissions and configure organization-wide settings to get started using eDiscovery (Premium). |
| [Create and manage cases](ediscovery-create-and-manage-cases) | Create cases to manage the eDiscovery (Premium) workflow for all legal and other types of investigations in your organization. |
|  |  |

## Integration with Insider Risk Management

Cases in [Microsoft Purview Insider Risk Management](https://compliance.microsoft.com/insiderriskmgmt) can be quickly escalated to new cases in Microsoft Purview eDiscovery (Premium) when additional legal review is needed for potentially risky user activity. The tight integration between these solutions can help your risk and legal teams work more efficiently and can help provide a complete end-to-end view of user activities under review. Check out how to [get started with Insider Risk Management](insider-risk-management-configure) and how to easily [escalate an Insider Risk Management case](insider-risk-management-cases#escalate-for-investigation) to an eDiscovery (Premium) case.

## Training

Training your IT administrators, eDiscovery managers, and compliance investigation teams in the basics for eDiscovery (Premium) can help your organization get started more quickly using Microsoft 365 eDiscovery tools. Microsoft 365 provides the following resource to help these users in your organization getting started with eDiscovery: [Describe the eDiscovery and audit capabilities of Microsoft 365](/en-us/training/modules/describe-ediscovery-capabilities-of-microsoft-365).