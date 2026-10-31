---
layout: Conceptual
title: What is Microsoft Security Copilot? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Microsoft Security Copilot is an AI-powered, natural language, security analysis solution designed to help security professionals defend against sophisticated attacks at machine speed and scale.
ms.update-cycle: 180-days
ms.date: 2026-04-20T00:00:00.0000000Z
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-overview
ms.custom: copilot-learning-hub
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 4c36ec69-d555-734d-6bb6-c97fa95cbca2
document_version_independent_id: 4c36ec69-d555-734d-6bb6-c97fa95cbca2
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/microsoft-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/microsoft-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 4c555be5-d761-aed8-bc0d-974d5fc88820
---

# What is Microsoft Security Copilot? | Microsoft Learn

Microsoft Security Copilot (Security Copilot) is a generative AI-powered security solution that helps increase the efficiency and capabilities of defenders to improve security outcomes at machine speed and scale.

Security Copilot provides a natural language, assistive copilot experience. Security Copilot helps support security professionals in various end-to-end scenarios such as incident response, threat hunting, intelligence gathering, posture management, and more. For more information, see [Security Copilot primary use cases](microsoft-security-copilot#security-copilot-primary-use-cases).

Designed with integration in mind, Security Copilot offers a standalone experience and also seamlessly integrates with products in the Microsoft Security portfolio. Security Copilot integrates with products such as [Microsoft Defender XDR](/en-us/defender-xdr/microsoft-365-defender), [Microsoft Sentinel](/en-us/azure/sentinel/overview), [Microsoft Intune](/en-us/intune/intune-service/fundamentals/what-is-intune), [Microsoft Entra](/en-us/entra/security-copilot/security-copilot-in-entra), and other third-party services such as ServiceNow and Jamf. For more information, see [Security Copilot experiences](experiences-security-copilot).

Tip

Visit the [Microsoft Security Copilot Adoption hub](https://aka.ms/SecurityCopilot/Adoption) to access useful links to training, videos, GitHub repository for sample plugins, and other technical readiness information.

The solution leverages the full power of OpenAI architecture to generate a response to a user prompt by using security-specific plugins, including organization-specific information, authoritative sources, and global threat intelligence. By using plugins as data point sources, security professionals have wider visibility into threats and gain more context. Incident responders also have the opportunity to extend the solution's functionalities. For more information about plugins, read [Manage plugins](manage-plugins).

Note

**Disclaimer:** This documentation is only intended for customers using commercial clouds. Currently, Security Copilot is not designed for use by customers using US government clouds, including but not limited to GCC, GCC High, DoD, and Microsoft Azure Government. For more information, consult with your Microsoft representative.

## Security Copilot primary use cases

Security Copilot focuses on making the following use cases easy to accomplish.

- **Investigate and remediate security threats**: Gain context for incidents to quickly triage complex security alerts into actionable summaries and remediate quicker with step-by-step response guidance.
- **Build KQL queries or analyze suspicious scripts**: Eliminate the need to manually write query-language scripts or reverse engineer malware scripts with natural language translation to enable every team member to execute technical tasks.
- **Understand risks and manage security posture of the organization**: Get a broad picture of your environment with prioritized risks to uncover opportunities to improve posture more easily.
- **Troubleshoot IT issues faster**: Synthesize relevant information rapidly and receive actionable insights to identify and resolve IT issues quickly.
- **Define and manage security policies**: Define a new policy, cross-reference it with others for conflicts, and summarize existing policies to manage complex organizational context quickly and easily.
- **Configure secure lifecycle workflows**: Build groups and set access parameters with step-by-step guidance to ensure a seamless configuration to prevent security vulnerabilities.
- **Develop reports for stakeholders**: Get a clear and concise report that summarizes the context and environment, open issues, and protective measures prepared for the tone and language of the report’s audience.
- **Build and add agents**: Developers can build and add agents to Security Copilot ecosystem.

Read [Use cases for Security Copilot](use-case-role-overview) to delve deeper into the different security team roles like CISOs, threat intelligence analysts, IT admins, and the like, who can benefit from each highlighted use case.

## How does Security Copilot work?

Security Copilot capabilities can be accessed through an immersive standalone experience and through intuitive embedded experiences available in other Microsoft security products. The foundation language model and proprietary Microsoft technologies work together in an underlying system that helps increase the efficiency and capabilities of defenders.

- **Microsoft security solutions** such as Microsoft Defender XDR, Microsoft Sentinel, and Microsoft Intune integrate seamlessly with Security Copilot. There are some embedded experiences available in Microsoft security solutions that give access to Security Copilot and prompt capabilities in the context of their work within those solutions.
- **Plugins from Microsoft and third-party security products** are a means to extend and integrate services with Security Copilot. Plugins bring more context from event logs, alerts, incidents, and policies from both Microsoft security products and supported third-party solutions such as ServiceNow.
- **Security Copilot also has access to threat intelligence and authoritative content** through plugins. These plugins can search across Microsoft Defender Threat Intelligence articles and intel profiles, Microsoft Defender XDR threat analytics reports, and vulnerability disclosure publications, among others.

[![Image of how Security Copilot works.](media/security-copilot-diagram.png)](media/security-copilot-diagram.png#lightbox)

Here's an explanation of how Security Copilot works:

- User prompts from security products are sent to Security Copilot.
- Security Copilot then preprocesses the input prompt through an approach called grounding, which improves the specificity of the prompt to help you get answers that are relevant and actionable to your prompt. Security Copilot accesses plugins for preprocessing, then sends the modified prompt to the language model.
- Security Copilot takes the response from the language model and post-processes it. This post-processing includes accessing plugins to gain contextualized information.
- Security Copilot returns the response, where the user can review and assess the response.

Security Copilot iteratively processes and orchestrates these sophisticated services to help produce results that are relevant to your organization because they're contextually based on your organizational data.