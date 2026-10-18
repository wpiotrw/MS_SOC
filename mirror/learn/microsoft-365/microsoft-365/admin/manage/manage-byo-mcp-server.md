---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Bring your own (BYO) MCP server in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-byo-mcp-server?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to register, review, use, monitor, and manage your own remote MCP servers with Microsoft Agent 365 for centralized governance and observability.
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
document_id: 920e37b4-c350-b2a8-ef05-4f1c8f907f13
document_version_independent_id: 920e37b4-c350-b2a8-ef05-4f1c8f907f13
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-byo-mcp-server.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-byo-mcp-server
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-byo-mcp-server.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: b0b104b3-2e9e-b30e-9209-8c71f58e7464
---

# Bring your own (BYO) MCP server in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

The Bring Your Own (BYO) MCP server feature enables organizations to register their own remote Model Context Protocol (MCP) servers with Microsoft Agent 365 for centralized governance and observability.

Important

- This feature is in preview.
- Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](/en-us/legal/microsoft-365/supplemental-terms), and are available before an official release so that customers can get early access and provide feedback.

Large enterprises often build and operate internal MCP servers to power their agents across various business workflows. These servers typically run outside any organizational governance boundary, with no admin visibility into what tools are exposed, no policy enforcement over how they're invoked, and no usage telemetry for security and compliance teams. BYO MCP server addresses this problem by routing registered servers through the Agent 365 Tooling Gateway, giving IT admins control via the Microsoft 365 admin center and security teams the observability data they need.

Note

Supported client surfaces during preview are Copilot Studio, Visual Studio Code, Claude Code, and GitHub Copilot CLI. Azure AI Foundry and Microsoft 365 Declarative Agents aren't supported.

## How a BYO MCP server works

A BYO MCP server follows this developer-to-admin flow so that remote MCP servers are reviewed and governed before agents can access them:

1. **A developer registers the server** through the Agent 365 CLI and provides the server URL, authentication type, and tools to expose. For more information, see Register a remote MCP server.
2. **An IT admin reviews the request** in the Microsoft 365 admin center and approves or rejects it. After approval, the admin grants the required Microsoft Entra permissions for the server. For more information, see [Review and approve MCP requests](manage-plugins-skills-mcp-servers#review-and-approve-mcp-requests).
3. **Supported clients use the approved server**, such as Copilot Studio and Visual Studio Code, to build and test agents with real tool invocations. For more information, see Use an approved MCP server.
4. **The security team monitors activity** and tool invocations through Microsoft Defender advanced hunting for compliance and anomaly detection. For more information, see Monitor and observe MCP server activity.

Important

This process requires governance and compliance reviews before external MCP integrations become available to end users.

Note

You can't republish new versions of your remote MCP server during preview.

## Register a remote MCP server

Tip

Administrators can use these steps to understand the registration process or provide them to a developer.

You or a developer can register a remote MCP server with Agent 365 by using the CLI. After registration, an IT admin can review and approve the server for use in agent-building surfaces.

Complete the following tasks:

- Understand developer prerequisites.
- Install the Agent 365 CLI.
- Register your MCP server.

### Developer prerequisites

Before registering a remote MCP server, make sure:

- You have installed the Agent 365 CLI version 1.1.165-preview or later.
- The Agent 365 service principal is provisioned in your tenant. If you can't find the service principal associated with app ID `ea9ffc3e-8a23-4a7d-836d-234d7c7565c1`, provision it by using the following resources:

    - [Set up the service principal](/en-us/microsoft-agent-365/developer/tooling#set-up-service-principal).
    - [Learn who can provision a service principal](/en-us/cli/azure/azure-cli-sp-tutorial-1).
- Your MCP server has a publicly accessible endpoint.
- Your server uses one of the following supported authentication types:

    - `NoAuth`.
    - `APIKey` with a header or query parameter.
    - `ExternalOAuth`.
    - `EntraOAuth`.

### Install the Agent 365 CLI

To install the Agent 365 CLI, follow the instructions in [Install the Agent 365 CLI](/en-us/microsoft-agent-365/developer/agent-365-cli#install-the-agent-365-cli).

### Register your MCP server

Choose one of the following methods to register your MCP server with Agent 365:

- **Manual registration via CLI**: Run the `a365 develop-mcp register-external-mcp-server` command from the CLI and manually provide the server details, authentication type, and the tools that your MCP server exposes.
- **Registration via JSON file**: Use `a365 develop-mcp register-external-mcp-server -f <path-to-file.json>` to register your MCP server by providing a JSON file that contains all of the server details, authentication type, and tool definitions in a single file, rather than specifying them individually on the command line.

Important

The examples in this section use *zava.com* as a fictional domain and generic server and tool names for illustration. Replace these values with your actual server URL, name, and tool identifiers.

The following examples show how to register an MCP server by using the Agent 365 CLI with different authentication types.

#### NoAuth

For MCP servers that require no authentication:

```bash
a365 develop-mcp register-external-mcp-server \
--server-name "ZavaServer" \
--server-url "https://mcp.zava.com/mcp" \
--publisher "Contoso" \
--description "My external MCP server for document search" \
--auth-type "NoAuth" \
--tools "tool1,tool2"
```

```json
{
  "serverName": "ext_DocsSearch",
  "serverUrl": "https://docs.contoso.com/api/mcp",
  "authType": "NoAuth",
  "description": "Documentation search MCP Server for Contoso developer docs.",
  "publisherName": "Contoso",
  "tools": [
    {
      "name": "search_docs",
      "description": "Search Contoso developer documentation and code samples."
    }
  ],
  "remoteScopes": null,
  "externalOAuth": null,
  "apiKey": null
}
```

#### APIKey (query parameter)

For servers that pass the API key as a query parameter:

```bash
a365 develop-mcp register-external-mcp-server \
--server-name "ZavaServer" \
--server-url "https://mcp.zava.com/mcp" \
--publisher "Contoso" \
--description "My external MCP server for document search" \
--auth-type APIKey \
--api-key-location Query \
--api-key-name apiKey \
--tools "tool1,tool2"
```

```json
{
  "serverName": "ext_MarketData",
  "serverUrl": "https://api.contoso.com/market/mcp",
  "authType": "APIKey",
  "description": "Real-time stock market data and search from Contoso Market Services.",
  "publisherName": "Contoso",
  "tools": [
    {
      "name": "stock-market-data",
      "description": "Get real-time stock market data and financial information."
    },
    {
      "name": "real-time-search",
      "description": "Search the web for real-time information and news."
    }
  ],
  "remoteScopes": null,
  "externalOAuth": null,
  "apiKey": {
    "location": "Query",
    "name": "apiKey"
  }
}
```

#### APIKey (header)

For servers that pass the API key in a request header:

```bash
a365 develop-mcp register-external-mcp-server \
--server-name "ZavaServer" \
--server-url "https://mcp.zava.com/mcp" \
--publisher "Contoso" \
--description "My external MCP server for document search" \
--auth-type APIKey \
--api-key-location Header \
--api-key-name token \
--tools "tool1,tool2"
```

```json
{
  "serverName": "ext_InternalTools",
  "serverUrl": "https://tools.contoso.com/mcp",
  "authType": "APIKey",
  "description": "Contoso internal tools MCP Server with API key authentication.",
  "publisherName": "Contoso",
  "tools": [
    {
      "name": "tool1",
      "description": "First tool exposed by the server."
    },
    {
      "name": "tool2",
      "description": "Second tool exposed by the server."
    }
  ],
  "remoteScopes": null,
  "externalOAuth": null,
  "apiKey": {
    "location": "Header",
    "name": "X-API-Key"
  }
}
```

#### ExternalOAuth

For servers that authenticate via an external OAuth provider:

```bash
a365 develop-mcp register-external-mcp-server \
--server-name "ZavaServer" \
--server-url "https://zava.com/mcp" \
--publisher "Contoso" \
--description "My external MCP server for document search" \
--auth-type ExternalOAuth \
--idp-authorization-url "https://idp.zava.com/o/oauth2/v2/auth" \
--idp-token-url "https://idp.zava.com/oauth2/token" \
--idp-scopes "https://api.zava.com/read" \
--idp-client-id "<your-client-id>" \
--idp-client-secret "<your-client-secret>" \
--remote-scopes "https://api.zava.com/read" \
--tools "tool1,tool2"
```

```json

{
  "serverName": "ext_Analytics",
  "serverUrl": "https://analytics.contoso.com/mcp",
  "authType": "ExternalOAuth",
  "description": "Contoso Analytics MCP Server for dataset and query operations.",
  "publisherName": "Contoso",
  "tools": [
    {
      "name": "list_datasets",
      "description": "List all available analytics datasets."
    }
  ],
  "remoteScopes": "https://analytics.contoso.com/.default",
  "externalOAuth": {
    "authorizationUrl": "https://auth.contoso.com/oauth2/authorize",
    "tokenUrl": "https://auth.contoso.com/oauth2/token",
    "scopes": "https://analytics.contoso.com/.default",
    "clientId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "clientSecret": "<your-client-secret>"
  },
  "apiKey": null
}
```

#### EntraOAuth

For servers that authenticate via Microsoft Entra ID:

```bash
a365 develop-mcp register-external-mcp-server \
--server-name "ZavaServer" \
--server-url "https://mcp.zava.com/mcp" \
--publisher "Contoso" \
--description "My external MCP server for document search" \
--auth-type EntraOAuth \
--remote-scopes "https://api.zava.com/.default" \
--tools "tool1,tool2"
```

```json
{
  "serverName": "ext_OrgDirectory",
  "serverUrl": "https://directory.contoso.com/mcp",
  "authType": "EntraOAuth",
  "description": "Contoso organization directory MCP Server secured with Entra OAuth.",
  "publisherName": "Contoso",
  "tools": [
    {
      "name": "list_users",
      "description": "List users in the organization directory."
    },
    {
      "name": "get_user_profile",
      "description": "Get the profile of a specific user by ID or UPN."
    }
  ],
  "remoteScopes": "api://contoso-directory/.default",
  "externalOAuth": null,
  "apiKey": null
}
```

After successful registration, submit the MCP server for admin review in the Microsoft 365 admin center.

## Evaluate MCP servers

You can evaluate the quality of your MCP tool definitions with the [`a365 develop-mcp evaluate`](/en-us/microsoft-agent-365/developer/reference/cli/develop-mcp#develop-mcp-evaluate) command. This command inspects your server's tool schemas and generates a report with actionable guidance for improving tool names, descriptions, and parameter schemas.

The semantic checks are scored by a coding agent CLI (GitHub Copilot CLI or Claude Code) that runs *locally on your machine*, under your own account and AI subscription. This command doesn't send tool-schema data to Microsoft.

Important

Only run `evaluate` against MCP servers you trust. The server's tool names, descriptions, and parameter schemas are read through a standard MCP `tools/list` call and handed to a coding agent running on your machine for scoring. This trust notice is printed once at the start of every run that uses an agent. It doesn't apply to `--eval-engine none`, which keeps everything local.

You don't need an admin role to run the evaluation. It runs locally against the MCP server URL you provide and doesn't call Azure or Microsoft Graph.

### Prerequisites

- Install the [Agent 365 CLI](/en-us/microsoft-agent-365/developer/agent-365-cli#install-the-agent-365-cli).
- For semantic (AI) scoring, one locally installed coding agent CLI:
    - **GitHub Copilot CLI**: Install with `npm install -g @github/copilot` (Node.js 18 or later). This is the standalone `copilot` binary, not the `gh copilot` GitHub CLI extension.
    - **Claude Code**: Install with `npm install -g @anthropic-ai/claude-code`, or follow [Claude Code install](https://docs.claude.com/claude-code).
- If neither agent is installed, the command still runs the deterministic checks and writes the checklist, then stops so you can score the semantic checks with your own LLM (bring-your-own-LLM). Pass `--eval-engine none` to skip agent probing entirely.

### How the evaluation works

The command runs a five-step pipeline and logs progress as shown in the following table:

| Step | What it does |
| --- | --- |
| 1. Discover tools | Connects to the MCP server, calls `tools/list`, and captures each tool's schema. |
| 2. Generate checklist | Writes `<server-name>_checklist.json` to the output directory. |
| 3. Run semantic evaluation | Hands the checklist to the selected coding agent for scoring. Skipped when `--eval-engine none` or no agent is available. |
| 4. Analyze | Aggregates per-tool and overall scores and determines the maturity level. |
| 5. Write reports | Produces `<server-name>_eval_report.html` and `<server-name>_eval_report.json`. |

Each check is one of two types:

- **Deterministic**: Rule-based logic in the CLI; pass or fail is exact and needs no AI (for example, "tool name isn't empty").
- **Semantic**: Scored by the coding agent, with a `reason` string explaining the judgment.

The run is idempotent. Re-running the same command reuses an existing `<server-name>_checklist.json` and skips server discovery, which is how the bring-your-own-LLM round trip works: score the checklist yourself, then rerun to resume. Delete the checklist file to force a fresh discovery after you change your tool schemas.

### Examples

Evaluate a local server with automatic engine selection:

```powershell
a365 develop-mcp evaluate --server-url "http://localhost:5000/mcp"
```

Evaluate an authenticated server, with the token supplied through an environment variable and artifacts written to a subfolder:

```powershell
$env:A365_MCP_AUTH_TOKEN = "<bearer-token>"
a365 develop-mcp evaluate --server-url "https://my-mcp-server.contoso.com/mcp" --output-dir "./eval"
```

Generate the checklist only, then score it with your own LLM:

```powershell
a365 develop-mcp evaluate --server-url "https://my-mcp-server.contoso.com/mcp" --eval-engine none
```

Force a specific scoring engine:

```powershell
a365 develop-mcp evaluate --server-url "http://localhost:5000/mcp" --eval-engine claude-code
```

### Read the report

Open `<server-name>_eval_report.html` from the output directory in a browser. The report shows:

- The **overall score** (0-100; higher is better).
- The **per-tool scores** with category breakdowns: tool name, tool description, parameter name, parameter description, and schema structure.
- A **prioritized action-item list**, ordered by impact, including the concrete requirements to reach the next maturity level.

[![Screenshot of the develop-mcp evaluate HTML report showing overall quality score, maturity level, key counts, and per-dimension category scores.](../../media/develop-mcp-evaluate-report.png)](../../media/develop-mcp-evaluate-report.png#lightbox)

### Data handling and AI transparency

- The command processes only your MCP server's **static tool schemas** (names, descriptions, and parameter schemas) from `tools/list`. It doesn't process runtime payloads, end-user data, or personal data.
- The coding agent CLI runs on your machine under your own AI subscription. The model API call is made directly by that CLI to the AI provider under your terms of service and billing. The `a365` CLI specifies the model but doesn't mediate the call.
- The `--auth-token` value is held in memory, sent only as the HTTP `Authorization` header to your server, and never written to disk or passed to the coding agent.
- Output files (`_checklist.json`, `_eval_report.html`, `_eval_report.json`) are written only to your `--output-dir` and stay on your machine.

### Troubleshooting

Use the following troubleshooting guide to diagnose common errors and apply the recommended fix.

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `Unauthorized` from `tools/list` | Wrong or expired bearer token | Reacquire the token and pass it through `A365_MCP_AUTH_TOKEN`. |
| `Unknown eval engine` | Invalid `--eval-engine` value | Use one of `auto`, `github-copilot`, `claude-code`, or `none`. |
| Pipeline stops after `[2/5]` | No coding agent on `PATH` | Install GitHub Copilot CLI or Claude Code, or score the checklist yourself and rerun. |
| `--output-dir cannot be empty or whitespace` | An empty value was passed to `--output-dir` | Pass a valid directory path, or omit the option to use the current directory. |
| `Failed to read existing checklist` | The checklist file is locked or malformed | Delete the checklist file to force a fresh discovery on the next run. |

## Review and approve BYO MCP server requests

After a developer registers a BYO MCP server, an admin reviews and approves it the same way as any other tool request. For the full review and approval steps, see [Review and approve MCP requests](manage-plugins-skills-mcp-servers#review-and-approve-mcp-requests).

### Key governance controls

The following table summarizes the key governance controls:

| Control | Description |
| --- | --- |
| Approval or rejection | An admin approves or rejects each BYO MCP server before it can be used. |
| Server-level block | An admin can block approved servers at any time. Runtime enforcement prevents agents from invoking blocked servers. |
| Tool-level block | An admin can allow or block individual tools within a BYO server instead of the whole server. This capability is rolling out for supported MCP servers registered on Agent 365. Support for BYO MCP servers is planned for a future release. For more information, see [Manage individual tools within an MCP server](manage-plugins-skills-mcp-servers#manage-individual-tools-within-an-mcp-server). |
| Tools snapshot | An admin can view the tools declared by each MCP server. |
| Runtime enforcement | Blocked MCP servers can't be invoked at runtime across any client surface. |
| Delete | An admin can delete a registered BYO MCP server that's no longer needed. For more information, see Delete a BYO MCP server. |

## Use an approved MCP server

After an MCP server is approved and Microsoft Entra grants consent, you can use it across supported agent-building surfaces. The following client surfaces support approved BYO MCP servers during preview:

| Client | Status |
| --- | --- |
| Copilot Studio | Supported |
| Visual Studio Code | Supported |
| Claude Code | Supported |
| GitHub Copilot CLI | Supported |

In Copilot Studio, follow these steps to invoke the approved BYO MCP server:

1. Go to [Copilot Studio](https://copilotstudio.microsoft.com/environments/%7Epersonal/home) in your environment.
2. Create a new custom agent (or open an existing one).
3. Go to the **Tools** section and select **MCP Server**.
4. Select the MCP server from the registry.
5. Test the agent by entering a prompt that invokes the MCP server.

Note

The first time you invoke the server, you might be prompted to complete a one-time connection setup. Follow the provided URL to create the required connection, such as entering your API key for an `APIKey`-based server. When you finish, return to your agent and retry the prompt. After a successful invocation, the MCP server returns the tool output.

Learn how to invoke approved BYO MCP servers from Claude Code, VS Code, and GitHub Copilot CLI in the [Set up Work IQ MCP Servers for coding agents](/en-us/microsoft-agent-365/tooling-servers-overview#extend-your-agents-with-available-or-custom-mcp-servers) section of the Work IQ MCP overview.

## Monitor and observe MCP server activity

Use [Microsoft Defender advanced hunting](/en-us/defender-xdr/advanced-hunting-overview) to track and analyze MCP server invocations. This process shows which agents invoke which MCP servers, when the invocations occur, and other metadata that can help you detect unusual or unauthorized usage.

The following KQL query provides a sample for Defender advanced hunting:

```kusto
CloudAppEvents
| where ActionType in ( "ExecuteToolByGateway")
| where RawEventData contains "tool name"
```

This query returns details including agent name, MCP server name, and invocation metadata.

## Delete a BYO MCP server

You can delete a registered BYO MCP server from the Microsoft 365 admin center when it's no longer needed. Deleting a server removes it from the registry, and agents can no longer invoke it.

To delete a BYO MCP server, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. Select **Agents** &gt; **Tools**, and then select the **Registry** tab.
3. Select the BYO MCP server that you want to delete to open its overview pane.
4. Select **Delete**.
5. Confirm the deletion by selecting **Delete**.