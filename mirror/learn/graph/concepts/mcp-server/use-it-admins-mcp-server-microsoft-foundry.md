---
layout: Conceptual
title: Use Microsoft MCP Server for IT Admins from Microsoft Foundry - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/mcp-server/use-it-admins-mcp-server-microsoft-foundry
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Licantrop0
ms.author: lucaspol
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: ent-mcp-server
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Learn how to connect Microsoft MCP Server for IT Admins as a tool in your Microsoft Foundry project to query Microsoft Entra data with natural language.
ms.date: 2026-11-17T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-106
locale: en-us
document_id: 851b4850-4bb4-641e-83a3-7a41d4f5d584
document_version_independent_id: 851b4850-4bb4-641e-83a3-7a41d4f5d584
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/mcp-server/use-it-admins-mcp-server-microsoft-foundry.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mcp-server/use-it-admins-mcp-server-microsoft-foundry
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/mcp-server/use-it-admins-mcp-server-microsoft-foundry.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: a3469f00-f5ef-30b0-350b-13b4849c1c8c
---

# Use Microsoft MCP Server for IT Admins from Microsoft Foundry - Microsoft Graph | Microsoft Learn

[Microsoft MCP Server for IT Admins](overview) lets AI agents query data in your Microsoft Entra tenant by using natural language. This article shows how to connect the MCP server as a tool in your Microsoft Foundry project and start querying your organization's data.

## Prerequisites

- A Microsoft Entra tenant.
- An admin user account in the tenant with the following roles assigned in the [Microsoft Entra admin center](https://entra.microsoft.com):
    - [**Cloud Application Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator), to create the app registration and grant admin consent.
    - The directory roles for the Graph operations your agent performs, so the MCP server can call Graph APIs on behalf of the signed-in user.
    - At least [**Azure AI Developer**](/en-us/azure/role-based-access-control/built-in-roles/ai-machine-learning#azure-ai-developer) role scoped to the Microsoft Foundry project resource to connect tools and use agents.
- A [client app registration](/en-us/entra/identity-platform/quickstart-register-app)in Microsoft Entra with the following configuration:
    - **Application (client) ID**. Note this value for use during setup.
    - A **Web** redirect URI (confidential client), which you add in a later step.
    - **Client secret**. Go to **Certificates & secrets** &gt; **Client secrets** and create a new secret. Copy the secret **value** for use during setup.
    - The three [required Microsoft Graph delegated permissions](get-started#required-permissions) and the Graph permissions for your scenarios, with admin consent.
- A Microsoft Foundry project with at least one agent configured.

## Connect the MCP server as a tool in Microsoft Foundry

Use the custom OAuth provider option to connect your app registration to the Microsoft MCP Server for IT Admins endpoint (`https://mcp.svc.cloud.microsoft/admin`).

1. In the [Microsoft Foundry portal](https://ai.azure.com/), make sure you're using the **New Foundry** UI and navigate to your project.
2. In the sidebar menu, select **Tools**. On the **Tools** tab, select **Connect a tool**.
3. Under **Catalog**, search for **Microsoft MCP Server for IT Admins**, and then select **Create**.

    ![Screenshot of the Foundry Tool Catalog with a search for IT Admins that returns Microsoft MCP Server for IT Admins.](../images/mcp-server/foundry-tool-catalog-it-admins.png)
4. For **OAuth Provider**, select **Custom** to use your own OAuth app registration for token exchange.
5. Provide the following configuration:

    | Field | Value |
    | --- | --- |
    | **Name** | Enter a unique identifier for the tool connection. |
    | **Remote MCP Server endpoint** | Prepopulated with `https://mcp.svc.cloud.microsoft/admin`. Leave it unchanged. |
    | **Authentication** | Prepopulated with **OAuth Identity Passthrough**. Leave it unchanged. |
    | **Client ID** | The application (client) ID from your app registration. |
    | **Client Secret** | The client secret value from your app registration. |
    | **Token URL**, **Auth URL**, and **Refresh URL** | These fields are prepopulated. Replace `organizations` with your tenant ID if your Microsoft Foundry project and app registration are in different tenants. Otherwise, leave `organizations` as the default value. |
    | **Scopes** | Prepopulated with `offline_access` and the three [required permissions](get-started#required-permissions) as `https://mcp.svc.cloud.microsoft/admin/` scopes. Leave it unchanged. |

    ![Screenshot of the Connect the Microsoft MCP Server for IT Admins tool dialog with the Custom OAuth provider selected and the endpoint, URLs, and scopes prepopulated.](../images/mcp-server/foundry-connect-it-admins-tool.png)
6. Select **Connect**, and then copy the **Redirect URL** provided.
7. Return to your Microsoft Entra app registration, go to **Authentication**, add the redirect URL as a redirect URI under **Web**, and save your changes. Foundry exchanges the token on the server with your client secret, so this app registration is a confidential client.

## Query Microsoft Entra data

After you connect the Microsoft MCP Server for IT Admins tool, add it to an agent and start querying your organization's data using natural language.

1. In the Microsoft Foundry sidebar, go to **Agents** and select an existing agent or create a new one.
2. In the agent configuration, add the Microsoft MCP Server for IT Admins tool you connected in the previous section.

### Sign in and authorize access

When you first use the tool, the agent prompts you to sign in and authorize access.

1. Select **Open consent** when prompted to sign in.
2. Follow the authentication prompts to grant access. You typically don't need to sign in again until the connection expires or is disconnected.
3. Approve each MCP tool call as prompted during query execution.

### Example queries

After you sign in, you can ask questions such as:

- "How many users are in my tenant?"
- "Which users haven't signed in for the last 30 days?"
- "Show me all guest users with admin roles."

Note

Microsoft Foundry isn't listed as a client that supports write actions, so use this tool for read queries. Write actions require an MCP client that supports elicitation on MCP protocol version 2026-07-28. For those clients, see [Supported clients](get-started#supported-clients).