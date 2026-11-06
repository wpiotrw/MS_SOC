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
description: Learn how to connect Azure AI Gateway or a LiteLLM gateway to the Microsoft 365 admin center to discover and govern registered MCP servers.
ai-usage: ai-assisted
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-11-05T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/302444b9-4a43-4841-8014-3d9e4251ff15
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bebd8809-dac1-4c22-83e2-66d98af8a94d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 82e398ed-872d-3124-af2b-cb9518ab0ea3
---

# Manage Tools Gateway in Microsoft 365 admin center | Microsoft Learn

Connect Azure AI Gateway or a LiteLLM gateway to Microsoft Agent 365 to discover and govern the Model Context Protocol (MCP) servers registered with the gateway. Agent 365 brings the registered MCP servers into the Tools experience, where administrators can review and govern them, monitor MCP server activity, and configure supported security protections for MCP tool calls.

Agent 365 currently supports Azure AI Gateway and LiteLLM. Each gateway requires its own connection and configuration process.

Use the section for your gateway to complete the connection and protection configuration. Then use the shared discovery and governance steps:

- Connect Azure AI Gateway.
- Connect LiteLLM.
- Discover and govern MCP servers.

Important

- This feature is in preview.
- Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](/en-us/legal/microsoft-365/supplemental-terms), and are available before an official release so that customers can get early access and provide feedback.

## Connect Azure AI Gateway

Use this section to connect Azure AI Gateway and, if needed, configure tool-call protection.

### Azure AI Gateway prerequisites

Before you connect Azure AI Gateway, make sure that the gateway is configured, you have the Global Administrator role in Microsoft 365, and its MCP servers are registered. For detailed prerequisites, configuration, and governance guidance, see [Govern tools with Microsoft Agent 365 and Azure API Management (preview)](/en-us/azure/api-management/agent-365).

### Connect the Azure gateway to Microsoft 365

Note

You must have the Global Administrator role to connect Azure AI Gateway. The AI Administrator role doesn't support this operation.

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/) as a Global Administrator.
2. Go to **Agents** &gt; **Settings**.
3. Select **Gateways**.
4. Next to **Microsoft Azure**, turn on the toggle to connect an Azure API Management service or Azure AI Gateway.
5. Review and accept the requested permissions.

You need to provide consent once per tenant, and it applies to all MCP servers in the connected gateway. Individual servers don't require separate consent.

Note

After you connect the gateway, Agent 365 discovers the MCP servers registered with it and makes them available on the Tools page. Discovery might take a few minutes. Go to **Agents** &gt; **Tools** and refresh the page to view the discovered MCP servers. To manage the discovered MCP servers, see Discover and govern MCP servers.

### Protect Azure AI Gateway tool calls with Microsoft Defender

To protect tool calls through Azure AI Gateway, configure the **Agent 365 tool threat protection** policy in the AI Gateway portal. The policy uses Microsoft Defender and Microsoft Purview to evaluate tool requests and results.

For prerequisites and gateway-specific configuration steps, see [Protect tool calls with Defender and Purview in AI Gateway tier (preview)](/en-us/azure/api-management/ai-gateway-policy-tool-threat). This protection requires the AI Gateway tier in Azure API Management and a delegated Microsoft Entra ID user token. App-only service-to-service calls aren't supported.

To monitor MCP server activity, see [Monitor and observe MCP server activity](manage-byo-mcp-server#monitor-and-observe-mcp-server-activity).

## Connect LiteLLM

Microsoft Agent 365 lets you connect to a LiteLLM gateway to discover and govern its registered MCP servers and protect MCP tool calls. LiteLLM is a third-party AI gateway and isn't built or supported by Microsoft. For information about LiteLLM and registering MCP servers with its gateway, see [LiteLLM gateway](https://docs.litellm.ai/docs/mcp) in the LiteLLM documentation.

### LiteLLM prerequisites

Before you begin, ensure that:

- You have access to a LiteLLM gateway with registered MCP servers.
- You have a gateway name, gateway URL, and API key for the LiteLLM proxy.
- You have the Global Administrator role in Microsoft 365 to access the Microsoft 365 admin center. This requirement applies to Microsoft 365, not to roles in LiteLLM.

The following sections explain how to connect the LiteLLM gateway and configure protection for MCP tool calls. After setup, use the shared steps to discover and govern MCP servers.

### Connect the LiteLLM gateway to Microsoft 365

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/) with the Microsoft 365 administrator role listed in the prerequisites.
2. Go to **Agents** &gt; **Settings** &gt; **Gateways**.
3. Under **LiteLLM Gateway**, select **Connect gateway**.
4. Enter the following information:
    - **Gateway name**: A friendly name to identify this gateway in the Microsoft 365 admin center.
    - **Gateway URL**: The URL of your LiteLLM proxy.
    - **API key**: An API key for the LiteLLM proxy.

You need to provide consent once per tenant, and it applies to all MCP servers in the connected gateway. Individual servers don't require separate consent.

Note

After you connect the LiteLLM gateway, Agent 365 discovers the MCP servers registered with it and makes them available on the **Tools** page. Discovery might take a few minutes. Go to **Agents** &gt; **Tools** and refresh the page to view the discovered MCP servers. To manage the discovered MCP servers, see Discover and govern MCP servers

### Protect LiteLLM MCP tool calls

Microsoft Agent 365 Guardrails uses Microsoft Defender to evaluate MCP tool calls that LiteLLM makes and provide runtime threat protection.

Configure protection in this order:

1. Create or identify the Microsoft Entra application that LiteLLM uses for the gateway.
2. Complete the required Microsoft Entra configuration.
3. Complete the corresponding configuration in LiteLLM.

#### Create the app registration

1. In the [Microsoft Entra admin center](https://entra.microsoft.com/), switch to the target tenant.
2. Go to **App registrations**, and then select **New registration**.
3. For the application name, enter `litellm-enterprise-api`.
4. For **Supported account types**, select **Accounts in this organizational directory only**.
5. Select **Register**.
6. Copy the **Application (client) ID**, and keep it as `GATEWAY_API_APP_ID` for the LiteLLM configuration.

Note

If the gateway already has an appropriate API application, reuse the existing application instead of creating another one. Preserve its existing roles, assignments, credentials, and unrelated permissions.

#### Configure LiteLLM

After you complete the Microsoft Entra configuration, use `GATEWAY_API_APP_ID` to complete the corresponding gateway configuration. For LiteLLM configuration guidance, see [LiteLLM gateway](https://docs.litellm.ai/docs/mcp) in the LiteLLM documentation.

## Discover and govern MCP servers

After you connect Azure AI Gateway or LiteLLM, you can access MCP servers that register with the connected gateway through the **Tools** experience in the Microsoft 365 admin center. These discovery and governance steps are common to both gateways.

1. In the Microsoft 365 admin center, go to **Agents** &gt; **Tools**.
2. Filter the list by source, and then select the gateway whose MCP servers you want to view.
3. Select an MCP server to review its details and the tools it exposes.

You can block or allow an MCP server to manage its availability. For the common governance procedure, see [Block or allow an MCP server](manage-plugins-skills-mcp-servers#block-or-allow-an-mcp-server).

For supported MCP servers, you can also manage the availability of individual tools. For more information, see [Manage individual tools within an MCP server](manage-plugins-skills-mcp-servers#manage-individual-tools-within-an-mcp-server).