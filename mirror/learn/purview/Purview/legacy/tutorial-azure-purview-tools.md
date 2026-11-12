---
layout: Conceptual
title: Learn about open-source tools and utilities for Microsoft Purview governance services | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/tutorial-azure-purview-tools
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This tutorial lists various tools and utilities available for Microsoft Purview governance services and discusses their usage.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: arindamba
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: tutorial
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 603534af-8376-112f-843b-1095c75652a4
document_version_independent_id: 603534af-8376-112f-843b-1095c75652a4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/tutorial-azure-purview-tools.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/tutorial-azure-purview-tools
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/tutorial-azure-purview-tools.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 19c80dd7-43bd-37b0-9182-2609f4b4df6e
---

# Learn about open-source tools and utilities for Microsoft Purview governance services | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article lists several open-source tools and utilities (command-line, python, and PowerShell interfaces) that help you get started quickly with Microsoft Purview governance services, like Microsoft Purview Data Map, Data Catalog, and Data Estate Insights in a matter of minutes! These tools have been authored & developed by collective effort of the Microsoft Purview Product Group and the open-source community. The objective of such tools is to make learning, starting up, regular usage, and long-term adoption of Microsoft Purview fast and easy.

## Intended audience

- Microsoft Purview community including customers, developers, ISVs, partners, evangelists, and enthusiasts.
- The Microsoft Purview Data Catalog is based on [Apache Atlas](https://atlas.apache.org/) and extends full support for Apache Atlas APIs. We welcome Apache Atlas community, enthusiasts, and developers to wholeheartedly build on and evangelize Microsoft Purview.

## Microsoft Purview customer journey stages

- *Microsoft Purview Learners*: Learners who are starting fresh with Microsoft Purview governance services and are keen to understand and explore how a multicloud unified data governance solution works. A section of learners includes users who want to compare and contrast Microsoft Purview with other competing solutions in the data governance market and try it before adopting for long-term usage.
- *Microsoft Purview Innovators*: Innovators who are keen to understand existing and latest features, ideate, and conceptualize features upcoming on Microsoft Purview. They're adept at building and developing solutions for customers, and have futuristic forward-looking ideas for the next-gen cutting-edge data governance product.
- *Microsoft Purview Enthusiasts/Evangelists*: Enthusiasts who are a combination of Learners and Innovators. They have developed solid understanding and knowledge of Microsoft Purview, hence, are upbeat about adoption of Microsoft Purview. They can help evangelize Microsoft Purview as a service and educate several other Microsoft Purview users and probable customers across the globe.
- *Microsoft Purview Adopters*: Adopters who have migrated from starting up and exploring the Microsoft Purview governance portal and are smoothly using Microsoft Purview for more than a few months.
- *Microsoft Purview Long-Term Regular Users*: Long-term users who have been using the Microsoft Purview governance portal for more than one year and are now confident and comfortable using most advanced use cases on the Azure portal and Microsoft Purview governance portal; furthermore they have near perfect knowledge and awareness of the Microsoft Purview REST APIs and the other use cases supported via Microsoft Purview APIs.

## Microsoft Purview open-source tools and utilities list

1. [Purview-API-via-PowerShell](https://github.com/Azure/Azure-Purview-API-PowerShell/blob/main/README.md)

    - **Recommended customer journey stages**: *Learners, Innovators, Enthusiasts, Adopters, Long-Term Regular Users*
    - **Description**: This utility is based on and covers the entire set functionality described in the [Microsoft Purview REST API reference](/en-us/rest/api/purview/). [Download & Install from PowerShell Gallery](https://aka.ms/purview-api-ps). It helps you execute all the documented Microsoft Purview REST APIs through a breezy fast and easy to use PowerShell interface. Use and automate Microsoft Purview APIs for regular and long-term usage via command-line and scripted methods. This is an alternative for customers looking to do bulk tasks in automated manner, batch-mode, or scheduled cron jobs; as against the GUI method of using the Azure portal and Microsoft Purview governance portal. Detailed documentation, sample usage guide, self-help, and examples are available on [GitHub:Azure-Purview-API-PowerShell](https://github.com/Azure/Azure-Purview-API-PowerShell).
2. [Microsoft Purview Lab](https://aka.ms/purviewlab)

    - **Recommended customer journey stages**: *Learners, Innovators, Enthusiasts*
    - **Description**: A hands-on-lab introducing the myriad features of Microsoft Purview and helping you learn the concepts in a practical and hands-on approach where you execute each step on your own by hand to develop the best possible understanding of Microsoft Purview.
3. [Microsoft Purview CLI](https://aka.ms/purviewcli)

    - **Recommended customer journey stages**: *Innovators, Enthusiasts, Adopters, Long-Term Regular Users*
    - **Description**: Python-based tool to execute the Microsoft Purview APIs similar to [Purview-API-via-PowerShell](https://aka.ms/purview-api-ps) but has limited/lesser functionality than the PowerShell-based framework.
4. [Microsoft Purview Demo](https://aka.ms/pvdemo)

    - **Recommended customer journey stages**: *Learners, Innovators, Enthusiasts*
    - **Description**: An Azure Resource Manager (ARM) template-based tool to automatically set up and deploy fresh new Microsoft Purview account quickly and securely at the issue of just one command. It's similar to [Purview-Starter-Kit](https://github.com/Azure/Azure-Purview-Starter-Kit), the extra feature being it deploys a few more pre-configured data sources - Azure SQL Database, Azure Data Lake Storage Gen2 Account, Azure Data Factory, Azure Synapse Analytics Workspace
5. [PyApacheAtlas: Interface between Microsoft Purview and Apache Atlas](https://github.com/wjohnson/pyapacheatlas) using Atlas APIs

    - **Recommended customer journey stages**: *Innovators, Enthusiasts, Adopters, Long-Term Regular Users*
    - **Description**: A Python package to work with Microsoft Purview and Apache Atlas API. Supports bulk loading, custom lineage, and more from a Pythonic set of classes and Excel templates. The package supports programmatic interaction and an Excel template for low-code uploads.
6. [Microsoft Purview Event Hubs Notifications Reader](https://github.com/Azure/Azure-Purview-API-PowerShell/blob/main/purview_atlas_eventhub_sample.py)

    - **Recommended customer journey stages**: *Innovators, Enthusiasts, Adopters, Long-Term Regular Users*
    - **Description**: This tool demonstrates how to read Microsoft Purview's Event Hubs and catch real-time Kafka notifications from the Event Hubs in Atlas Notifications (https://atlas.apache.org/2.0.0/Notifications.html) format. Further, it generates an excel sheet CSV of the entities and assets on the fly that are discovered live during a scan, and any other notifications of interest that Microsoft Purview generates.

## Feedback and disclaimer

None of the tools come with an express warranty from Microsoft verifying their efficacy or guarantees of functionality. They're certified to be free of any malicious activity or viruses, and guaranteed to not collect any private or sensitive data.

For feedback or questions about efficacy and functionality during usage, contact the respective tool owners and authors on the contact details mentioned in the respective GitHub repo.