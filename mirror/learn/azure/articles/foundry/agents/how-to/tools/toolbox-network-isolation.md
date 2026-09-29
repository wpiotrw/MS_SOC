---
layout: Conceptual
title: Network isolation for a toolbox in Microsoft Foundry - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/toolbox-network-isolation
breadcrumb_path: ../../../../breadcrumb/azure-ai/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure-ai-foundry
ms.suite: office
author: mattwojo
learn_banner_products:
- azure
manager: mcleans
ms.author: mattwoj
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Understand how toolbox tool traffic flows when your Microsoft Foundry project uses network isolation, and set up a network-secured toolbox for Basic and Standard agent projects.
reviewer: lindazqli
ms.reviewer: zhuoqunli
ms.date: 2026-08-03T00:00:00.0000000Z
ms.manager: mcleans
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: dev-focus
ai-usage: ai-assisted
locale: en-us
document_id: f3369f51-a398-d6b2-b40d-423eb413926f
document_version_independent_id: 2d1e80f2-2ba6-8679-893e-43b96d14ff17
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/tools/toolbox-network-isolation.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: foundry/agents/how-to/tools/toolbox-network-isolation
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/tools/toolbox-network-isolation.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 41493887-cf12-ce60-027b-48a414e8b0c7
---

# Network isolation for a toolbox in Microsoft Foundry - Microsoft Foundry | Microsoft Learn

A toolbox is a logical container for tools and doesn't deploy its own networking resources. The networking configuration of the Microsoft Foundry project that hosts the toolbox governs all network access.

When your project runs inside a virtual network (VNet) with [network isolation (private link)](../../../how-to/configure-private-link), agents reach the toolbox MCP endpoint through the project's private endpoint. Each downstream tool's traffic flows differently depending on the tool type.

Tool connectivity depends on where the downstream service is hosted. Some tools communicate with Azure resources that support private endpoints, some invoke services that run through the project's delegated subnet, and others depend on Microsoft-managed services that currently require public or backbone connectivity. Review how each tool behaves before you add it to a toolbox in a network-isolated environment.

## Network isolation support for tools in a toolbox

Network-isolated projects work best with tools that support private endpoints or VNet subnet integration. Review the support table before building a toolbox intended for regulated or highly secured environments.

The following table shows how each tool's traffic flows when your project uses network isolation. Some tools route through your VNet subnet or a private endpoint, some use public endpoints or the Microsoft backbone network, and some aren't supported in a network-isolated project.

| Tool | VNet support (traffic flow) |
| --- | --- |
| [Model Context Protocol (MCP)](model-context-protocol) | ✅ Supported (through your VNet subnet). |
| [Azure AI Search](ai-search) | ✅ Supported (through private endpoint). |
| [File search](file-search) | ✅ Supported (through private endpoint). |
| [OpenAPI](openapi) | ✅ Supported (through your VNet subnet). |
| [Agent-to-agent (A2A)](agent-to-agent) | ✅ Supported (through your VNet subnet). |
| [Web search](web-search) | ✅ Supported. Relies on Microsoft-managed public endpoints. |
| [Code interpreter](code-interpreter) | ✅ Supported (Microsoft backbone network). |
| [Skills](skills) | ✅ Supported (network behavior depends on the tools used by the skill). |
| [Fabric IQ](fabric-iq) | ⚠️ Partial. Fabric IQ connectivity is provided through MCP integration. Support depends on the specific Fabric item and networking configuration. See [Restrict network access](fabric-iq#restrict-network-access). |
| [Work IQ](work-iq) | ❌ Not supported in network-isolated projects. |
| [Browser automation](browser-automation) | ❌ Not supported. |
| [Tool search](tool-search) | N/A |

Tools that use your VNet subnet communicate through the delegated subnet associated with the Foundry project. These tools can access resources reachable from that subnet, subject to your network security rules.

For the authoritative, tool-by-tool support matrix, see [Agent tools with network isolation](../../../how-to/configure-private-link#agent-tools-with-network-isolation). For the full list of tools and their SDK and tooling support, see [Feature support](toolbox#feature-support).

## Set up a network-secured project

Set up network isolation at the project level, then create your toolbox in that project. You can find the infrastructure-as-code templates in the [Foundry samples infrastructure setup repository](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep) (Bicep, with a Terraform mirror). The template you choose depends on your [agent project type](../../concepts/networking-options#bring-your-own-virtual-network-requirements).

### Configure a Basic agent project

A Basic agent project uses platform-managed data resources. To place it inside your own virtual network with private endpoints and no public egress, deploy the [`11-private-network-basic-vnet`](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/11-private-network-basic-vnet) template. To restrict who can call the endpoint while keeping public egress, use [`10-private-network-basic`](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/10-private-network-basic).

### Configure a Standard agent project

A Standard agent project brings your own data resources (Azure Cosmos DB, Azure Storage, and Azure AI Search). For full isolation with no public egress and bring-your-own data resources, deploy the [`15-private-network-standard-agent-setup`](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/15-private-network-standard-agent-setup) template.

For the full template catalog and what each one provisions, see the [infrastructure setup README](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep#readme). For a step-by-step walkthrough of customizing the scaffolded infrastructure, see [Set up private networking for Foundry Agent Service](../virtual-networks).