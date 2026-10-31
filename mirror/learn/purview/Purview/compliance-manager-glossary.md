---
layout: Conceptual
title: Glossary of terms for Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-glossary
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-02-04T00:00:00.0000000Z
audience: Admin
ms.topic: glossary
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Get definitions of key terms used in Microsoft Purview Compliance Manager.
locale: en-us
document_id: 383ef286-7e21-f960-0873-3174c28ce5cd
document_version_independent_id: 383ef286-7e21-f960-0873-3174c28ce5cd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-glossary.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: 67f868be-aa7e-4263-834b-e8375de00bf6
---

# Glossary of terms for Microsoft Purview Compliance Manager | Microsoft Learn

This glossary provides a brief description of important terms and concepts in the context of Microsoft Purview Compliance Manager. This glossary can help you learn and use the solution tools and features quickly and effectively.

| Term | Description |
| --- | --- |
| **Assessment** | A grouping of controls from a specific regulation, standard, or policy. Completing the actions within an assessment helps you meet the requirements of a standard, regulation, or law. |
| **Control** | Generally, a specific measure or action that an organization implements to mitigate or manage risks associated with a particular requirement or objective of a regulation, standard, or policy. As used in Compliance Manager: A control is a requirement of a regulation that defines how you assess and manage system configuration, organizational process, and people responsible for meeting a specific requirement of a regulation, standard, or policy. |
| **Improvement action** | A compliance activity with recommended implementation instructions, intended to help towards completion of a control. |
| **License** | In the context of Compliance Manager regulations: A single Compliance Manager license allows you to create an unlimited number of assessments for multiple versions of a regulation. |
| **Regulation** | A rule or requirement imposed by a governing authority, such as a government agency, to achieve a specific purpose. Also commonly understood as a standard or framework. Compliance Manager supports several industry regulations, providing over 360 regulatory templates for building assessments. |
| **Service** | A data source, such as Microsoft Azure or Amazon Web Services (AWS), or more broadly, the digital entity that’s being assessed and that benefits from the actions taken. For an assessment, you designate the service that it should evaluate. Completing an improvement action in the assessment benefits the service. |
| **Service instance** | For Compliance Manager connectors, each service instance represents an account with a non-Microsoft service provider. For example, an organization may have multiple accounts in Salesforce, such as one for development and testing, one for production, etc. Connectors are set up for each service instance using one email address and password. So an organization may have several connectors for one service, which enables the organization to monitor assessment progress across all instances of a service. |
| **Solution** | A feature or capability used to complete an improvement action. For example, a Microsoft product, such as Microsoft Data Loss Prevention, or a setting in a service like Azure or AWS. |
| **Subscription** | A type of account to create, assess, and manage a service covered by Microsoft Defender for Cloud, such as Azure, Google Cloud Platform, or Amazon Web Services. Examples: an Azure account for development and testing purposes, an Azure account for production, etc. |
| **Virtual resources** | A cloud computing-based resource that is managed virtually, such as VMs and virtual storage disks. |