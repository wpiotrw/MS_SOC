---
layout: Conceptual
title: Multicloud support in Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Learn how Microsoft Purview Compliance Manager provides multicloud support so you can track and manage compliance for your organization's cloud services.
locale: en-us
document_id: e7c95686-1d12-a75a-92bc-a969c06d6e73
document_version_independent_id: e7c95686-1d12-a75a-92bc-a969c06d6e73
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-multicloud.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-multicloud
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-multicloud.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: 66324c91-1468-40e4-5800-fa9e28935ece
---

# Multicloud support in Microsoft Purview Compliance Manager | Microsoft Learn

**In this article:** Learn how Compliance Manager helps you automatically assess and manage compliance across your multicloud environment.

## Overview

Compliance Manager now integrates with [Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/defender-for-cloud-introduction), which allows you to assess your compliance posture across Microsoft 365, Microsoft Azure, Google Cloud Platform (GCP), and Amazon Web Services (AWS) with resource-level testing and cloud-specific guidance. This new integration provides customers with a single interface in Compliance Manager to help make it easier to manage compliance across the organization’s digital estate.

This integration allows Compliance Manger to track configurations in your organization’s Microsoft Azure environment and detect signals from other services like GCP and AWS, so that you can assess your progress in meeting controls for the regulations you need to comply with. Compliance Manager provides guidance for implementing improvement actions in non-Microsoft services for meeting controls.

The integration with Defender for Cloud surfaces in two contexts within Compliance Manager:

1. [Assessments](compliance-manager-assessments): When you create an assessment in Compliance Manager, you’ll select a supported regulation and then choose one or more services to assess. Compliance Manger then provides automatic monitoring of configurations in your selected services to determine whether controls are passing or failing.
2. [Improvement actions](compliance-manager-improvement-actions): Using signals from Defender for Cloud, Compliance Manager automatically detects the test status and test result of improvement actions that pertain to Azure and to your non-Microsoft services. With these signals, Compliance Manager automatically tracks the status of actions and resource-level testing details from cloud services like AWS and GCP.

## Supported services

The services listed below can be assessed by Compliance Manager:

- Microsoft 365
- Microsoft Azure cloud services
- Google Cloud Platform
- Amazon Web Services

### Add a new service

If you want to assess a non-Microsoft service that isn't listed above, you can add it as a new service when you're creating a new assessment. When you add a new service, the [universal version of the underlying regulation](compliance-manager-regulations#regulations-overview) is used, and you perform manual implementation and testing work. For instructions on adding a new service, see step 5 of the [assessment creation process](compliance-manager-assessments#create-an-assessment-using-a-guided-process).

Tip

Compliance Manager has a dedicated selection of connectors to support other non-Microsoft services such as Salesforce and Zoom. Visit [Working with connectors in Compliance Manager](compliance-manager-connectors).

## Service subscriptions

When creating assessments, you can select a subscription if the service you choose for the assessment is monitored by Defender for Cloud. Your choice of subscription will affect the evaluation of improvement actions for that service. Learn more about [monitoring assessment progress by service](compliance-manager-assessments#assessment-progress-by-service).

If you choose subscriptions that are in scope within Defender for Cloud for a matching regulation, automated test results are pulled from Defender for Cloud and shown in the assessment.

## Supported regulations

View the [list of regulations supported by both Compliance Manager and Defender for Cloud](compliance-manager-cloud-settings#standards-supported-by-compliance-manager-and-defender-for-cloud).

## Get started

There are setup steps required before you can start building assessments for your cloud services. Visit [Configure cloud settings](compliance-manager-cloud-settings) to get started.

## Resources

- [Quickstart: Set up Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/get-started)