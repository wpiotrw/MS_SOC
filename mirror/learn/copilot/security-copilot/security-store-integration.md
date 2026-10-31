---
layout: Conceptual
title: Microsoft Security Store in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/security-store-integration
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Security Store in Microsoft Security Copilot.
ms.date: 2025-09-30T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
locale: en-us
document_id: 78394d66-fdb1-5e0a-35f2-16e01393a2c4
document_version_independent_id: 78394d66-fdb1-5e0a-35f2-16e01393a2c4
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/security-store-integration.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: security-store-integration
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/security-store-integration.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 992caa99-3cc8-f31b-130f-44185d63f61a
---

# Microsoft Security Store in Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

[Security Store](/en-us/security/store/what-is-security-store) is Microsoft Security’s new security-optimized storefront that enables organizations to find, try, buy, and deploy Microsoft and partner-built security solutions and agents. These solutions and agent integrate directly with Microsoft Security products such as Microsoft Defender, Microsoft Sentinel, Microsoft Entra, Purview, Intune and Security Copilot, offering a unified experience that simplifies procurement and accelerates time to value.

For more information, see [Security Store documentation](/en-us/security/store/what-is-security-store).

Security Store is integrated into the standalone experience of Microsoft Security Copilot, offering users a streamlined way to discover and acquire security agents directly within the portal.

Analysts and other security stakeholders can explore available agents both Microsoft and non-Microsoft, without leaving the Security Copilot portal. After you find an agent you'd like to use, you can proceed to the Security Store to purchase or subscribe to the agent or solution that you want to deploy. Security Store is where you manage billing as well.

After getting the agent or solution, you can then configure and operate the agents within Microsoft Security Copilot, maintaining a clear separation between purchasing and operational management.

## Discover and get agents

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com) and go to the **Home menu** &gt; **Security Store**.

    ![Image of Security Store in the menu](media/menu-security-store.png)
2. Search for an agent and refine your results by using filters such as publisher, product, or pricing. Agents can also be viewed in a list format.

    ![Image of Security Store](media/view-security-store.png)
3. Select the agent you'd like to use and then select **Get agent**.

    For Microsoft agents, you'll be routed to the **Active agents** page.

    For Non-Microsoft agents, you'll be routed to Security Store where you can purchase or subscribe to agents. For more information, see Get Agents in Security Store.

    Important

    Purchases and subscriptions done in Security Store are handled separately from the Security Copilot platform. Removing an agent from Security Copilot doesn't end a subscription, you'll need to manage the billing in Security Store.  Using agents within Security Copilot incurs Security Compute Units (SCUs), which are billed independently from any subscription fees.

After getting an agent and setting it up, you'll see the agent in the **Active agents** section.

If the agent has a dependent plugin, the plugin is enable for the agent to use (but not configured). To configure the plugin, go to **Manage sources** &gt; find the plugin &gt; configure the plugin. After completing the configuration steps, you can then use the agent successfully.

If the agent doesn't rely on a dependent plugin, you can configure it using the standard setup process.

Tip

If you're a developer and want to create agents and publish to Security Store, see [Custom agent overview](/en-us/copilot/security/developer/custom-agent-overview).