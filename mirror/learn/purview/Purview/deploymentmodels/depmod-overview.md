---
layout: Conceptual
title: Microsoft Purview deployment models | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Microsoft Purview deployment models are scenario-based guides created by the engineering team from proven customer deployments.
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.reviewer: maximeb
ms.date: 2026-03-31T00:00:00.0000000Z
audience: ITPro
ms.topic: best-practice
ms.service: purview
ms.collection:
- purview-deployment-models
ai-usage: ai-assisted
locale: en-us
document_id: a16856e9-6e9d-1bf9-754a-c976717579f6
document_version_independent_id: a16856e9-6e9d-1bf9-754a-c976717579f6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploymentmodels/depmod-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploymentmodels/depmod-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploymentmodels/depmod-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 15613f6e-fd7b-547e-3f36-895d55d34e18
---

# Microsoft Purview deployment models | Microsoft Learn

Microsoft Purview provides integrated solutions and features that complement each other. For new Microsoft Purview administrators, it can be overwhelming to know where to start. But even existing administrators might be unfamiliar with how some Microsoft Purview features can enhance their data security.

To address the need for shorter, actionable, and prescriptive guidance, the Product Engineering team is releasing a new series: Microsoft Purview Deployment Models. Deployment models are scenario-based and include a comprehensive step-by-step guide to jumpstart your deployment.

## Audience

IT professionals, security professionals, and compliance officers who are responsible for deploying and managing Microsoft Purview in their organization. They don't provide detailed technical guidance but rather a high-level overview of the deployment process for a configuration that meets a specific business need. If you're new to Microsoft Purview technologies, concepts, and planning, deployment, and administration, see [Learn about Microsoft Purview](../purview#learn-about-microsoft-purview).

Deployment models come from our engineering teams. They're based on proven deployments with organizations. The objective of deployment models is to enable organizations to accelerate securing content and deploy faster.

## Secure by default with Microsoft Purview

![Secure by default with Microsoft Purview](../media/depmod-overview-thumb-securebydefault1.png)

Use this deployment model to help rapidly implement a secure by default configuration with Microsoft Purview Information Protection, Data Loss Prevention, and Insider Risk Management.

- [Introduction](depmod-secure-by-default-intro)
- [Step 1: Start with default labeling](depmod-secure-by-default-step1)
- [Step 2: Address files with the highest sensitivity](depmod-secure-by-default-step2)
- [Step 3: Expand protection to your entire Microsoft 365 data estate](depmod-secure-by-default-step3)
- [Step 4: Operate, expand, and retroactive actions](depmod-secure-by-default-step4)

## Prevent data leak to shadow AI

![Prevent data leak to shadow AI with Microsoft.](media/depmod-data-leak-shadow-ai-intro/prevent-shadow-ai-thumb.png)

Use this deployment model to help your organization identify and prevent data leaks to shadow AI by using Microsoft Purview, Microsoft Defender for Cloud Apps, Microsoft Entra, and Microsoft Intune.

- [Introduction](depmod-data-leak-shadow-ai-intro)
- [Step 1: Discover AI apps](depmod-data-leak-shadow-ai-step1)
- [Step 2: Block access to unsanctioned AI apps](depmod-data-leak-shadow-ai-step2)
- [Step 3: Block sensitive data going to sanctioned AI apps](depmod-data-leak-shadow-ai-step3)
- [Step 4: Govern data sent to AI apps](depmod-data-leak-shadow-ai-step4)

## Secure and govern Microsoft 365 Copilot agents

![Secure and govern Microsoft 365 Copilot agents with Microsoft Purview.](media/depmod-sc-agents-deployment/screenshot-2025-08-26-130022.png)

Use this deployment model for Microsoft 365 Copilot agents by securing both the grounding data and interactions with Microsoft Purview.

- [Introduction](depmod-sc-agents-deployment)
- [Step 1: Discover risks and identify gaps](depmod-sc-agents-step1)
- [Step 2: Protect sensitive info in grounding data](depmod-sc-agents-step2)
- [Step 3: Protect interactions](depmod-sc-agents-step3)
- [Step 4: Govern interactions](depmod-sc-agents-step4)

## Deploy and use Data Security Posture Management

![Deploy and use Microsoft Purview Data Security Posture Management (DSPM).](media/dspmdiagram.png)

Use this deployment model to prepare for a Data Security Posture Management (DSPM) deployment with step-by-step guidance.

- [Introduction](depmod-dspm-intro)
- [Step 1: Establish foundational elements](depmod-dspm-step1)
- [Step 2: Configure access and analytics](depmod-dspm-step2)
- [Step 3: Understand data landscape and risks](depmod-dspm-step3)
- [Step 4: Take action and investigate with Security Copilot](depmod-dspm-step4)

## Lightweight guide to mitigate data leakage

![Lightweight guide to mitigate data leakage](media/depmod-overview/lightweight-guide-to-mitigate-data-leakage.jpg)

Use this deployment model to enable core data security capabilities with minimal configuration, focusing on essential steps to get started quickly.

- [Introduction](depmod-lightweight-dlp-intro)
- [Step 1: Establish foundational data security](depmod-lightweight-dlp-step1)
- [Step 2: Expand protection to endpoints](depmod-lightweight-dlp-step2)
- [Step 3: Continuous improvement](depmod-lightweight-dlp-step3)

## Reduce false positives by using SITs and advanced classifiers

![Reduce false positives by using SITs and advanced classifiers](../media/blueprint-false-positives.png)

Use this deployment model to minimize false positives by effectively leveraging the classification capabilities of Microsoft Purview.

- [Introduction](depmod-reduce-false-positives)
- [Step 1: Configure pattern-based sensitive data detection](depmod-reduce-false-positives-step1)
- [Step 2: Implement Exact Data Match for precise matching](depmod-reduce-false-positives-step2)
- [Step 3: Use trainable classifiers for complex content](depmod-reduce-false-positives-step3)
- [Step 4: Apply document fingerprinting for templates](depmod-reduce-false-positives-step4)