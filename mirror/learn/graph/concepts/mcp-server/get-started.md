---
layout: Conceptual
title: Get started with Microsoft MCP Server for IT Admins - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/mcp-server/get-started
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
ms.topic: get-started
description: Register an MCP client app, grant Microsoft Graph permissions, and connect VS Code, GitHub Copilot, Claude, ChatGPT, or another MCP client to Microsoft MCP Server for IT Admins.
ms.date: 2026-11-17T00:00:00.0000000Z
locale: en-us
document_id: 6ffea37a-1b32-8941-2553-53b29fef2edc
document_version_independent_id: 6ffea37a-1b32-8941-2553-53b29fef2edc
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/mcp-server/get-started.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mcp-server/get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/mcp-server/get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/341fdab2-4964-4759-8241-f5820b012a47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cc1f92bb-c0d6-4d40-99ce-dabea3161a84
platformId: 8dcb4721-e1a9-e147-c2eb-4d21b1b9c632
---

# Get started with Microsoft MCP Server for IT Admins - Microsoft Graph | Microsoft Learn

To use Microsoft MCP Server for IT Admins, register an app for your MCP client in your Microsoft Entra tenant, grant it Microsoft Graph delegated permissions, and configure the client with the server URL and the app's client ID.

This article describes how to register and configure an MCP client, connect the supported clients, and migrate from Microsoft MCP Server for Enterprise.

## Prerequisites

- A Microsoft Entra tenant.
- To register the app and grant admin consent, an account with the *Cloud Application Administrator* or *Application Administrator* role.
- For each user of the MCP client, the Microsoft Entra roles needed for the Graph operations they run. The MCP server runs every request with the signed-in user's permissions.

## Register and configure an MCP client

Each MCP client needs an app registration in your tenant. Dynamic Client Registration (DCR) isn't supported. Support for Client ID Metadata Documents (CIMD) is coming for third-party clients such as ChatGPT and Claude, and will make the app registration optional for them. Visual Studio Code, the GitHub Copilot app, and GitHub Copilot CLI will still require an app registration.

An administrator completes these steps once per tenant for each client app:

1. In the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType%7E/null/isMSAApp%7E/false), register an app for the MCP client. Under **Supported account types**, select **Accounts in this organizational directory only**.
2. Add the redirect URI for your client from the Supported clients table under **Mobile and desktop applications**. Microsoft Entra then treats the app as a public client, so the app doesn't need a client secret. All the clients in the table, including ChatGPT and Claude, connect as public clients.

    Don't add the redirect URI under **Web**. Microsoft Entra treats Web apps as confidential clients and requires a client secret at sign-in. The admin center's **Redirect URIs** box doesn't accept `http://127.0.0.1`. To add it, open the app's **Manifest** and add `http://127.0.0.1` to `publicClient.redirectUris`, keeping any existing entries. For more information, see [Prefer 127.0.0.1 over localhost](/en-us/entra/identity-platform/reply-url#prefer-127001-over-localhost).
3. Go to **API permissions** &gt; **Add a permission** &gt; **Microsoft Graph** &gt; **Delegated permissions**, and add:

    - The three required permissions.
    - The Graph permissions your scenarios need, such as `User.Read.All`, `Group.ReadWrite.All`, `Policy.Read.All`, or `DeviceManagementManagedDevices.Read.All`. For the full list, see the [Microsoft Graph permissions reference](../permissions-reference).
4. [Grant admin consent](/en-us/entra/identity/enterprise-apps/grant-admin-consent) for `MCP.Server.Access` and every other permission on the app that requires admin consent. On the **API permissions** page, select **Grant admin consent for &lt;tenant&gt;**. Use this page rather than **Consent on behalf of your organization** at client sign-in: the client requests only the three required permissions, so sign-in consent doesn't cover your scenario permissions.
5. (Optional) To allow only selected users, open the app in **Enterprise applications**, set **Assignment required?** to **Yes**, and [assign users or groups](/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal).
6. Configure your client with the server URL and the app's **Application (client) ID**, as described in Supported clients.

Users then sign in with their work account when their client prompts them.

### Required permissions

| Microsoft Graph delegated permission | Purpose |
| --- | --- |
| [MCP.Server.Access](../permissions-reference#mcpserveraccess) | Lets the client call Microsoft MCP Server for IT Admins. Requires admin consent. |
| [User.Read](../permissions-reference#userread) | Signs in the user and reads their profile. |
| [EntitlementMgmt-SubjectAccess.ReadWrite](../permissions-reference#entitlementmgmt-subjectaccessreadwrite) | Lets the `request_access` tool request access packages for the signed-in user. |

Your MCP client requests only these three permissions when the user signs in. It writes them as OAuth scopes that start with the MCP server's URL. Clients that use OAuth discovery request them automatically. If your client asks you to enter scopes, use this value:

```text
https://mcp.svc.cloud.microsoft/admin/MCP.Server.Access https://mcp.svc.cloud.microsoft/admin/User.Read https://mcp.svc.cloud.microsoft/admin/EntitlementMgmt-SubjectAccess.ReadWrite
```

Don't add your scenario permissions, such as `User.Read.All`, to this value. The MCP server calls Microsoft Graph with the permissions that you consented to on the app registration, so the client doesn't request them separately.

### Configuration values

| Property | Value | Notes |
| --- | --- | --- |
| MCP endpoint | `https://mcp.svc.cloud.microsoft/admin` | Configure in your client. |
| MCP client app ID | The **Application (client) ID** of your app registration | Required in every client. |
| Redirect URI (reply URL) | See Supported clients | Required on your app registration. |
| Scopes | See Required permissions | Most clients discover them automatically. |
| Token endpoint auth method | `client_secret_post` | Required in some clients, such as ChatGPT, even though the app is a public client. Leave the client secret empty. |
| MCP server app ID | `e8c77dc2-69b3-43f4-bc51-3213c9d915b4` | Appears in [Microsoft Graph activity logs](overview#logs). You don't provision it in your tenant. |

## Supported clients

Microsoft MCP Server for IT Admins works with any MCP client that supports OAuth with a preregistered client ID.

Write actions also require a client that supports elicitation on the latest MCP protocol version, [2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), which is stateless. In clients without that support, read tools work but the server denies write actions. When a client adopts the latest MCP version, write actions start working without any change on your side. A client that supports write actions can still fall back to an earlier protocol version when it connects, and the server then denies write actions for that connection. For more information, see Troubleshooting.

Add each redirect URI under **Mobile and desktop applications** in your app registration.

| Client | Redirect URI | Write actions |
| --- | --- | --- |
| Visual Studio Code | `http://localhost` | Supported |
| [GitHub Copilot app](https://github.com/github/app) | `http://127.0.0.1` (add it through the manifest) | Supported |
| GitHub Copilot CLI | `http://127.0.0.1` (add it through the manifest) | Supported |
| Claude Code | `http://localhost/callback` | Supported |
| ChatGPT | `https://chatgpt.com/connector/oauth/<random_chars>` | Supported |
| Claude (claude.ai, desktop, and mobile app) | `https://claude.ai/api/mcp/auth_callback` | Denied: elicitation isn't supported yet |

Microsoft Entra ignores the port when it matches `localhost` and `127.0.0.1` redirect URIs, so clients can use dynamic ports.

Copilot Studio and Microsoft Foundry connect from a server-hosted connector and use a **Web** (confidential client) app registration. Use them for read queries; they aren't listed as supporting write actions. For their setup, see [Use Microsoft MCP Server for IT Admins from Copilot Studio](use-it-admins-mcp-server-copilot-studio) and [Use Microsoft MCP Server for IT Admins from Microsoft Foundry](use-it-admins-mcp-server-microsoft-foundry).

# [Visual Studio Code](#tab/vscode)
1. Register an app with `http://localhost` as the redirect URI under **Mobile and desktop applications**.
2. In Visual Studio Code, run **MCP: Open User Configuration** from the Command Palette. Add the server to `mcp.json`, and replace the client ID:

    ```json
    {
      "servers": {
        "mcp-admin": {
          "type": "http",
          "url": "https://mcp.svc.cloud.microsoft/admin",
          "oauth": {
            "clientId": "<REGISTERED_APP_CLIENT_ID>"
          }
        }
      }
    }
    ```
3. Start the server from `mcp.json` and sign in with an account from your tenant.

# [GitHub Copilot app](#tab/github-copilot-app)
1. Register an app with `http://127.0.0.1` as the redirect URI. Add it to `publicClient.redirectUris` in the app's manifest, as described in step 2 of Register and configure an MCP client.
2. Go to **Customize** &gt; **MCP** &gt; **Add server**, select **HTTP**, and enter:
    - **Name**: `mcp-admin`
    - **URL**: `https://mcp.svc.cloud.microsoft/admin`
    - **OAuth Client ID**: the client ID of your registered app
3. Select **Sign in** and sign in with an account from your tenant.

# [GitHub Copilot CLI](#tab/github-copilot-cli)
1. Register an app with `http://127.0.0.1` as the redirect URI. Add it to `publicClient.redirectUris` in the app's manifest, as described in step 2 of Register and configure an MCP client.
2. Add the server to `~/.copilot/mcp-config.json`. Put your app's client ID in `oauthClientId`, and set `oauthPublicClient` to `true`:

    ```json
    {
      "mcpServers": {
        "mcp-admin": {
          "type": "http",
          "url": "https://mcp.svc.cloud.microsoft/admin",
          "headers": {},
          "tools": ["*"],
          "oauthClientId": "<REGISTERED_APP_CLIENT_ID>",
          "oauthPublicClient": true
        }
      }
    }
    ```

    You can also run `/mcp add` to enter the connection details interactively, and then add `oauthClientId` and `oauthPublicClient` to the new entry.
3. Sign in with an account from your tenant when prompted.

For more information, see the [GitHub Copilot CLI documentation](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli).

# [Claude Code](#tab/claude-code)
1. Register an app with `http://localhost/callback` as the redirect URI under **Mobile and desktop applications**.
2. Add the server, and replace the client ID:

    ```bash
    claude mcp add --transport http --client-id <REGISTERED_APP_CLIENT_ID> mcp-admin https://mcp.svc.cloud.microsoft/admin
    ```
3. In Claude Code, run `/mcp`, select `mcp-admin`, and sign in with an account from your tenant.

# [ChatGPT](#tab/chatgpt)
1. In ChatGPT, go to **Settings** &gt; **Apps** &gt; **Create App**. Enter the **Name** and **MCP Server URL** (`https://mcp.svc.cloud.microsoft/admin`), select **OAuth** authentication, and open **Advanced settings**.
2. Under **Registration method**, select **User-Defined OAuth Client** and copy the **Callback URL**.
3. Register an app with the callback URL as the redirect URI under **Mobile and desktop applications**.
4. Back in ChatGPT, enter your app's client ID and leave **OAuth Client Secret** empty. Keep `client_secret_post` as the **Token endpoint auth method**.
5. Confirm the risk notice that ChatGPT shows, select **Create**, and sign in with an account from your tenant.

# [Claude](#tab/claude)
Note

Claude.ai, Claude Desktop, and the Claude mobile app don't support MCP elicitation yet, so the server denies write actions and only read tools work. For write actions, use Claude Code.

1. Register an app with `https://claude.ai/api/mcp/auth_callback` as the redirect URI under **Mobile and desktop applications**.
2. In Claude, go to **Customize** &gt; **Connectors**, select **+** &gt; **Add custom connector**, and enter the **Name** and **URL** (`https://mcp.svc.cloud.microsoft/admin`).
3. Open **Advanced settings**, enter your app's client ID, and leave the client secret empty.
4. Save the connector, select **Connect**, and sign in with an account from your tenant.

---

## Migrate from Microsoft MCP Server for Enterprise

Microsoft MCP Server for Enterprise (`https://mcp.svc.cloud.microsoft/enterprise`) is deprecated. The `/enterprise` endpoint keeps working for a few months, so you can migrate one client at a time:

1. **Prepare an app registration.** Follow Register and configure an MCP client. You can reuse an existing custom app if its redirect URI matches the Supported clients table. The Visual Studio Code default app isn't supported, so every client needs its own app registration.
2. **Map your permissions.** For each `MCP.<permission>` scope your client had, add the matching Microsoft Graph delegated permission `<permission>`. For example, `MCP.User.Read.All` becomes `User.Read.All`. Also add the three required permissions.
3. **Grant admin consent** for the new permissions.
4. **Update the client configuration.** Change the URL to `https://mcp.svc.cloud.microsoft/admin` and set your app's client ID.
5. **Sign in again**, so the client gets a token with the new permissions.
6. **Verify** with a read question that the app has permission for, such as "*How many users are in my tenant?*".
7. **Remove the `/enterprise` server entry** from the client. After you migrate all your clients, you can revoke your apps' grants to the **Microsoft MCP Server for Enterprise** resource (`MCP.User.Read.All` and the other `MCP.*` scopes it exposes), because the new endpoint doesn't use them. Keep the Microsoft Graph `MCP.Server.Access` permission. The new endpoint also doesn't need the MCP server provisioned in your tenant or the Microsoft Entra PowerShell module.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `AADSTS50011`: redirect URI mismatch | Add your client's redirect URI from the Supported clients table under **Mobile and desktop applications**. Add `http://127.0.0.1` through the manifest. For Copilot Studio and Microsoft Foundry, add the redirect URL that the connector shows under **Web**. |
| `AADSTS7000218`: the request body must contain `client_assertion` or `client_secret` | The redirect URI is under **Web**, so Microsoft Entra expects a secret. For the clients in the Supported clients table, move it to **Mobile and desktop applications**. For Copilot Studio and Microsoft Foundry, keep it under **Web** and check the connector's client secret or federated credential. |
| `AADSTS65001`: consent required | Grant admin consent for `MCP.Server.Access` and the other permissions that require it. |
| `AADSTS50105`: user not assigned | **Assignment required?** is set to **Yes** and the user isn't assigned. Assign the user, or one of their groups, to the app. |
| Invalid scope error | The client still uses the Microsoft MCP Server for Enterprise configuration (the `api://e8c77dc2-69b3-43f4-bc51-3213c9d915b4/.default` scope or `MCP.*` scopes such as `MCP.User.Read.All`). Remove the server, add it again with the `/admin` URL, and sign in again. |
| Microsoft Graph returns `403 Forbidden` | The app lacks the Graph permission, or the user lacks the role. Add the permission and grant consent, activate the role in PIM, or let the agent call `request_access`. |
| Write action denied, or no confirmation prompt | The client doesn't support elicitation on MCP protocol version 2026-07-28. Use a client that supports write actions from the Supported clients table. |
| Write action denied in a client that supports write actions | The client fell back to an earlier MCP protocol version when it connected, so elicitation isn't available. Check the client's MCP logs for the negotiated protocol version, update the client to its latest version, and restart the server connection. |