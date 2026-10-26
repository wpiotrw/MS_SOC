---
layout: Conceptual
title: Manage plugins, skills, and MCP servers in Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers
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
description: Learn how to manage plugin and skill availability, review requests, and govern MCP servers and their tools in the Microsoft 365 admin center.
ai-usage: ai-assisted
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-10-14T00:00:00.0000000Z
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
document_id: a173292f-fd6e-5470-c667-f47bfb847e67
document_version_independent_id: a173292f-fd6e-5470-c667-f47bfb847e67
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/manage-plugins-skills-mcp-servers.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage-plugins-skills-mcp-servers
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/manage-plugins-skills-mcp-servers.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d56bfe0c-ecd5-4d90-854f-35482bbb1314
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/02e99b71-5808-477b-9387-4c6efa24e46b
platformId: 3ace7e56-441d-f3f6-6cf1-e3df613dd436
---

# Manage plugins, skills, and MCP servers in Microsoft 365 admin center | Microsoft Learn

Plugins are packaged integrations that extend agents with reusable capabilities, including skills, Model Context Protocol (MCP) servers, and connectors. Skills provide reusable instructions or workflows that help agents perform tasks consistently. For definitions of these and other tool types, see [Key concepts](agent-tools-overview#key-concepts) in the Agent Tools overview.

This article explains how to upload, install, uninstall, and delete plugins and skills; manage plugin availability; review access requests; and govern MCP servers in the [Microsoft 365 admin center](https://admin.microsoft.com/).

Plugins are primarily available to end users in the Copilot channel, where they extend the experience with specialized capabilities, data, and actions. Organizations can make plugins available to users based on their business needs and governance requirements. The plugin catalog can include third-party plugins published by independent providers and plugins published by Microsoft, giving organizations access to a broad range of ready-to-use capabilities while allowing administrators to determine which plugins are appropriate for their users.

Administrators can view the complete list of plugins available to their organization in the Microsoft 365 admin center. They can review publisher information and manage plugin availability based on the publisher, helping ensure that only approved Microsoft or third-party plugins are available to users.

## Manage plugin availability at the organization level

Use the Microsoft 365 admin center to control which categories of plugins users can discover and install on the Copilot channel. These settings apply across your organization and can be configured by publisher type.

To manage plugin availability at the organization level, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Settings** &gt; **Agent and plugin access**.
3. Under the installation settings, choose which publisher categories users can access: **Microsoft**, **your organization**, or **certified external publishers**.
4. Select a category to allow users to discover and install plugins from that publisher type.

If a category isn't selected, affected plugins remain discoverable but display the message: "This plugin is blocked by your organization's policy."

## Manage plugin availability for users

Administrators can control who can use an individual plugin in the Microsoft 365 admin center.

To manage plugin availability for users, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools** &gt; **Plugins**.
3. Select the plugin that you want to manage.
4. Open **Users**, and then choose one of the following availability options:
    - **All users**: Make the plugin available to everyone in the organization.
    - **No users**: Make the plugin unavailable to all users.
    - **Specific users and groups**: Make the plugin available only to selected users or groups.
5. Review your selection, and then save the changes.

## Review plugin access requests

If a plugin is restricted by organization-level availability settings or by its user availability configuration, users can still discover the plugin in the Copilot channel. The plugin appears as blocked by organizational policy, and eligible users can select **Request access**.

The request is sent to the Microsoft 365 admin center, where an administrator can review the request and either approve or reject it.

To review a plugin access request, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools** &gt; **Requests**.
3. Select the plugin access request that you want to review.
4. Review the request details, including the user and the requested plugin.
5. Select **Approve** to grant access, or select **Reject** to deny the request.

## Upload plugins or skills

You can upload your own plugins or skills to make them available for agents in your organization through the Microsoft 365 admin center.

Before you can upload a plugin or a skill, a developer needs to package it into a manifest file. For more information about creating a manifest file, see [Cowork plugin development](/en-us/microsoft-365/copilot/cowork/cowork-plugin-development).

To upload a plugin or skill, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools** &gt; **Registry**.

    [![Screenshot showing the Tools registry in the Microsoft 365 admin center with tool categories, filters, and the Upload button.](media/tools-registry-list.png)](media/tools-registry-list.png#lightbox)
3. Select **Upload**.
4. Upload the manifest file for the plugin or skill.

    [![Screenshot showing the Upload manifest file step of the tool upload wizard with the Choose file button highlighted.](media/tools-upload-manifest.png)](media/tools-upload-manifest.png#lightbox)
5. After the manifest uploads, review the components included in the package, such as MCP servers and skills, and then select **Next**.
6. In the **Scope users** pane, choose who can use the plugin or skill by selecting either **All users** or **Specific users or groups**.

    [![Screenshot showing the Select users step of the plugin install wizard with the All users option and Next button highlighted.](media/plugin-install-select-users.png)](media/plugin-install-select-users.png#lightbox)
7. Review the configuration, and then select **Install**.

    [![Screenshot showing the Review &amp;amp; install pane of the plugin install wizard with the Install button highlighted.](media/plugin-install-review.png)](media/plugin-install-review.png#lightbox)

## Manage plugins and skills

Managing a skill uses the same actions and steps as managing a plugin, so this section applies to both plugins and skills.

### Tool actions

| Tool actions | Description |
| --- | --- |
| **Install and uninstall** | Install a plugin or skill for users so that it's ready to use without manual installation by end users. You can uninstall a previously installed plugin or skill. |
| **Manage user availability** | Make a plugin or skill available to all users, no users, or specific users and groups. |
| **Delete** | Delete a plugin or skill package that was uploaded to your tenant. Deleting isn't available for plugins or skills that come from the Microsoft 365 Store. |
| **Block** | Block a plugin or skill across your organization to prevent users and agents from accessing it. |

Note

Delete applies only to plugins and skills that were uploaded to your tenant. User availability settings apply to any plugin or skill, whether it was uploaded or made available from the Microsoft 365 Store. To restrict access by user or publisher category, see Manage plugin availability for users or Manage plugin availability at the organization level.

### Install a plugin or skill

You can install a plugin or skill for your entire organization or for specific users or groups by using the same process as for other apps in the Microsoft 365 admin center.

To install a plugin or skill so that it's available, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools**.
3. From the list, select the plugin or skill that you want to install, and then select **Install**.

    [![Screenshot showing a plugin's Overview pane in the Microsoft 365 admin center with the Install button highlighted.](media/plugin-overview-pane.png)](media/plugin-overview-pane.png#lightbox)
4. In the installation pane, review the details for the plugin or skill.
5. Choose who can use the plugin or skill by selecting **All users** or **Specific users or groups**.
6. Select **Next**, review the installation details, and then select **Install**.

### Uninstall a plugin or skill

Uninstall a plugin or skill to remove it from the environment. It isn't available to agents unless you install it again.

To uninstall a plugin or skill so that it's unavailable, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools**.
3. From the list, select the plugin or skill that you want to uninstall, and then select **Uninstall**.

    [![Screenshot showing an installed plugin's Overview pane in the Microsoft 365 admin center with the Uninstall button highlighted.](media/plugin-overview-installed.png)](media/plugin-overview-installed.png#lightbox)
4. Select **Uninstall** to confirm.

    [![Screenshot showing the confirmation dialog for uninstalling a plugin with the Uninstall button highlighted.](media/plugin-uninstall-confirm.png)](media/plugin-uninstall-confirm.png#lightbox)

### Delete a plugin or skill

You can delete a previously uploaded plugin or skill package across your entire organization by using the Microsoft 365 admin center. When you delete it, agents can no longer use it and it's removed from the registry.

To delete a plugin or skill, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools**.
3. From the list, select the plugin or skill that you want to delete.
4. Select **Delete**, and then select **Delete** again to confirm.

### Block a plugin or skill

You can block a plugin or skill package across your entire organization by using the Microsoft 365 admin center. When you block it, agents can no longer use it.

To block a plugin or skill, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Tools** &gt; **Plugins**.
3. From the list, select the plugin or skill that you want to block.
4. Select **Block**, and then select **Block** again to confirm.

Note

Blocking a plugin prevents users from accessing the plugin and any agents that depend on it. Associated MCP servers and connectors remain available to other plugins. Blocking an MCP server also blocks dependent plugins and linked connectors. Blocking a plugin package blocks its included agents because they share the same governance controls. Unblocking the plugin package restores access to the associated agents.

## Review and approve MCP requests

After a developer registers a tool, such as a remote MCP server, the tool appears in the Microsoft 365 admin center for review and approval.

[![Screenshot showing the Requests (preview) tab listing pending tool requests in the Microsoft 365 admin center.](media/tools-requests-tab.png)](media/tools-requests-tab.png#lightbox)

With the required permissions, you can review, approve, or reject requests to control which tools are available in your organization.

Important

To complete the review and approval process, you must meet two requirements:

- You must have access to the **Tools** page in the Microsoft 365 admin center to manage agent tools and review MCP server registration requests.
- You must be able to grant tenant-wide consent.

Two roles meet both requirements:

- [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator).
- [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator).

Use roles with the fewest permissions, and limit the number of users who have admin permissions. See [Least privileged roles by task in Microsoft Entra ID](/en-us/entra/identity/role-based-access-control/delegate-by-task).

To learn more about admin roles and permissions in the Microsoft 365 admin center, see:

- [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).
- [Grant tenant-wide admin consent to an application](/en-us/entra/identity/enterprise-apps/grant-admin-consent).

To review and approve MCP server registration requests, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. Select **Agents** &gt; **Tools**, and then select the **Requests (preview)** tab.
3. Review the server name, publisher, requester, and request date.
4. Review the server information and declared tools for accuracy and compliance.
5. Select **Approve** to make the server available in the organizational registry, or **Reject** to deny the request.
6. After approval, consent to the Microsoft Entra permissions required by the MCP server. The server becomes available to agent-building surfaces only after consent is granted.

Note

After approval and consent, the MCP server can take up to 30 minutes to appear in all Microsoft Copilot Studio environments in the tenant.

The registry displays the following status indicators for MCP servers:

- **Available**: The tool is active and ready for use.
- **Blocked**: The tool is disabled, and agents can't access it.

### Block or allow an MCP server

To block or allow an entire MCP server, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. Select **Agents** &gt; **Tools**, and then select the **Registry** tab.
3. Select an MCP server from the list to open its overview pane.

    [![Screenshot showing an MCP server's Overview pane in the Microsoft 365 admin center with the Block button highlighted.](media/mcp-server-overview.png)](media/mcp-server-overview.png#lightbox)
4. Select **Block** to restrict the server across your organization, or **Unblock** to restore access to a previously blocked server.

Blocking an MCP server disables all the tools it exposes. If one or more plugins use the MCP server, you can also block those plugins. To control individual tools instead of the entire server, use tool-level granular control.

## Manage individual tools within an MCP server

Note

Tool-level granular control is rolling out to tenants and supports only specific types of MCP servers registered on Agent 365.

By default, blocking an MCP server disables all the tools it exposes. Tool-level granular control lets you allow or block individual tools within a supported MCP server registered on Agent 365 instead of blocking the entire server. Use this capability to keep high-risk tools, such as tools that write, delete, or process payments, turned off by default while allowing lower-risk tools on the same server.

If an MCP server doesn't support tool discovery, the **Tools** tab shows a message that the server doesn't support tool discovery, and individual tools aren't available to manage. In this case, use Block or allow an MCP server to control the entire server instead.

To manage individual tools within an MCP server, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. Select **Agents** &gt; **Tools**, and then select the **Registry** tab.
3. Select an MCP server from the list to open its overview pane.
4. Select the **Tools** tab. The list shows every tool the server exposes, along with its description and an **Enabled** or **Disabled** toggle.

    [![Screenshot showing the Tools tab of an MCP server with a list of tools and their Enabled/Disabled toggles.](media/mcp-tools-tab.png)](media/mcp-tools-tab.png#lightbox)
5. Turn individual tools on or off as needed.
6. Select **Save** to apply your changes, or **Discard changes** to cancel.

    [![Screenshot showing the Tools tab with Save and Discard changes buttons highlighted after toggling a tool.](media/mcp-tools-save.png)](media/mcp-tools-save.png#lightbox)

The policy you set for each tool applies wherever the tool is used and is enforced at runtime by the Agent 365 Tooling Gateway.

For information about registering, evaluating, and monitoring your own remote MCP servers, see [Bring your own (BYO) MCP server](manage-byo-mcp-server). For information about connecting an Azure AI Gateway or Azure API Management instance so its registered MCP servers are automatically discovered, see [Manage Tools Gateway](manage-tools-gateway).

## Frequently asked questions

**How can I block all third-party plugins?**

Use organization-level availability settings to control this. Go to **Agents** &gt; **Settings** &gt; **Agent and plugin access**, and clear the publisher category for **certified external publishers**. This prevents users from discovering or installing plugins published by third parties, while plugins from Microsoft or your organization can still be governed separately. For more information, see Manage plugin availability at the organization level.

**Can I block an individual MCP server that's included in a plugin?**

Yes. Select the MCP server to view the plugins that use it. When you block the server, you can also block all linked plugins.