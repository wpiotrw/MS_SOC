---
layout: Conceptual
title: Manage Tools Gateway in Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway
breadcrumb_path: ../breadcrumb/agent365/toc.json
uhfHeaderId: MSDocsHeader-Agent365
feedback_system: Standard
permissioned-type: public
ms.service: agent-365
hideScope: false
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
ms.subservice: admin
description: Learn how to connect an AI Gateway or Azure API Management instance to the Microsoft 365 admin center to discover and govern registered MCP servers.
ai-usage: ai-assisted
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-09-28T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: how-to
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
- operations-pod
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 1a219749-13ee-517b-987b-fce4223aa1b3
document_version_independent_id: 1a219749-13ee-517b-987b-fce4223aa1b3
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/manage-tools-gateway.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage-tools-gateway
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/manage-tools-gateway.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bf4dbf7f-261c-4ae9-9fee-5989668a780a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/302444b9-4a43-4841-8014-3d9e4251ff15
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1c4b5d48-3f26-4bd8-9592-816d9c1a3420
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bebd8809-dac1-4c22-83e2-66d98af8a94d
platformId: 82e398ed-872d-3124-af2b-cb9518ab0ea3
---

# Manage Tools Gateway in Microsoft 365 admin center | Microsoft Learn

Connect your AI Gateway or Azure API Management (APIM) instance to the Microsoft 365 admin center to discover and govern the Model Context Protocol (MCP) servers registered with it. After a Global Administrator grants tenant-wide consent, the MCP servers appear on the **Tools** page, where administrators can manage them alongside other agent tools.

Important

- This feature is in preview.
- Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](/en-us/legal/microsoft-365/supplemental-terms), and are available before an official release so that customers can get early access and provide feedback.

## Capabilities

As an administrator, you can:

- View MCP servers registered in the connected gateway.
- Review MCP servers in the centralized tools inventory.
- Apply governance policies and control availability for agents.
- Automatically discover MCP servers added to the gateway later.

## Prerequisites

Before you begin, make sure that:

- An AI Gateway or APIM instance is configured.
- MCP servers are registered in the gateway.
- A Global Administrator is available to grant consent.
- You have access to the Microsoft 365 admin center.

## Connect your gateway

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/) as a Global Administrator.
2. Go to **Agents** &gt; **Settings**.
3. Select **Gateways**.
4. Under **Gateways**, connect one of the following gateway types:
    - **Microsoft Azure**: Turn on the toggle to connect an Azure API Management service or Azure AI Gateway. Review and accept the requested permissions. For Azure configuration and governance guidance, see [Govern tools with Microsoft Agent 365 and Azure API Management (preview)](https://go.microsoft.com/fwlink/?LinkId=2382608).
    - **LiteLLM gateway**: Select **Connect a gateway**, and then enter the gateway name, gateway URL, and API key.

Consent is required once per tenant and applies to all MCP servers in the connected gateway. Individual servers don't require separate consent.

## Review and govern MCP servers

Discovery starts automatically after consent is granted and typically completes within a few minutes.

1. In the Microsoft 365 admin center, go to **Agents** &gt; **Tools**.
2. Filter the list by source, and then select **AI gateway** to review the discovered MCP servers.
3. Apply governance policies to block or allow each server.

Note

Tool-level granular control is supported for MCP servers registered in an AI Gateway tier in Azure API Management service. You can block or allow individual tools within a server instead of the entire server. For more information, see [Manage individual tools within an MCP server](manage-plugins-skills-mcp-servers#manage-individual-tools-within-an-mcp-server).

New MCP servers registered in the connected gateway are discovered automatically during subsequent refreshes.

## Frequently asked questions

**Is AI Gateway or APIM required?**

Yes. The Microsoft 365 admin center discovers only MCP servers registered in a connected AI Gateway or APIM instance.

**Who can grant consent?**

A user assigned the Global Administrator role must complete the consent process.

**Is consent required for each MCP server?**

No. Consent is granted once per tenant and applies to all MCP servers in the connected gateway.

**How long does discovery take?**

MCP servers typically appear within a few minutes. If they don't appear, refresh the **Tools** page and allow more time.

**Can the Microsoft 365 admin center discover MCP servers outside the connected gateway?**

No. Only MCP servers registered in the connected gateway are discovered.

**Are newly registered MCP servers discovered automatically?**

Yes. New MCP servers surface during the gateway discovery and refresh process.