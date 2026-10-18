---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage Tools Gateway in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-gateway?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
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
ms.service: microsoft-365-copilot
ms.subservice: agent-management
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
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 72596944-469c-1236-8889-cb62a83f3644
document_version_independent_id: 72596944-469c-1236-8889-cb62a83f3644
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-tools-gateway.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-tools-gateway
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-tools-gateway.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bf4dbf7f-261c-4ae9-9fee-5989668a780a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1c4b5d48-3f26-4bd8-9592-816d9c1a3420
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 9dbed676-4a2c-32ce-8fda-1298e07b9182
---

# Manage Tools Gateway in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

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