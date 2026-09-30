---
layout: Conceptual
title: Manage and maintain Azure Connected Machine agent proxy settings - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/manage-agent-proxy-settings
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: This article describes proxy setting management tasks for the Azure Connected Machine agent.
ms.date: 2026-09-23T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: d649bbdd-6956-34d6-1cfb-08f7ba8d039d
document_version_independent_id: 1b9622fd-a96d-692e-6a49-25eb3673caf7
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/manage-agent-proxy-settings.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/manage-agent-proxy-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/manage-agent-proxy-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 64ea1802-4b7d-ddaf-09e6-e48f56b5fd7c
---

# Manage and maintain Azure Connected Machine agent proxy settings - Azure Arc | Microsoft Learn

Use the methods described in this article to configure the agent to communicate with the service through a proxy server or to remove this configuration after deployment. The agent communicates outbound by using the HTTP protocol under this scenario.

You can configure proxy settings by using the `azcmagent config` command or system environment variables. If you specify a proxy server in both the agent configuration and system environment variables, the agent configuration takes precedence and becomes the effective setting. Use `azcmagent show` to view the effective proxy configuration for the agent.

Note

Azure Arc-enabled servers don't support using [Log Analytics gateway](/en-us/azure/azure-monitor/agents/gateway) as a proxy for the Connected Machine agent.

### Agent-specific proxy configuration

Agent-specific proxy configuration is the preferred way to configure proxy server settings. This method is available starting with version 1.13 of the Azure Connected Machine agent. By using agent-specific proxy configuration, you can prevent the proxy settings for the Azure Connected Machine agent from interfering with other applications on your system.

Note

Some extensions deployed to Azure Arc-enabled servers don't inherit the agent-specific proxy configuration. For guidance on configuring proxy settings for extensions, see the documentation for each extension you deploy.

To configure the agent to communicate through a proxy server, run the following command:

```bash
azcmagent config set proxy.url "http://ProxyServerFQDN:port"
```

You can use an IP address or simple hostname in place of the FQDN if your network requires it. If your proxy server runs on port 80, you can omit ":80" at the end.

To check if a proxy server URL is configured in the agent settings, run the following command:

```bash
azcmagent config get proxy.url
```

To stop the agent from communicating through a proxy server, run the following command:

```bash
azcmagent config clear proxy.url
```

You don't need to restart any services when reconfiguring the proxy settings by using the `azcmagent config` command.

### Proxy bypass for private endpoints

Starting with agent version 1.15, you can specify services that shouldn't use the specified proxy server. This configuration helps with split-network designs and private endpoint scenarios where you want Microsoft Entra ID and Azure Resource Manager traffic to go through your proxy server to public endpoints, but you want Azure Arc traffic to skip the proxy and communicate with a private IP address on your network.

The proxy bypass feature doesn't require you to enter specific URLs to bypass. Instead, provide the name of any services that shouldn't use the proxy server. The location parameter refers to the Azure region of the Arc-enabled server.

Setting the proxy bypass value to `ArcData` only bypasses the traffic of the Azure extension for SQL Server and not the Arc agent.

| Proxy bypass value | Affected endpoints |
| --- | --- |
| `AAD` | `login.windows.net``login.microsoftonline.com``pas.windows.net` |
| `ARM` | `management.azure.com` |
| `AMA` | `global.handler.control.monitor.azure.com``<virtual-machine-region-name>.handler.control.monitor.azure.com``<log-analytics-workspace-id>.ods.opinsights.azure.com``management.azure.com``<virtual-machine-region-name>.monitoring.azure.com``<data-collection-endpoint>.<virtual-machine-region-name>.ingest.monitor.azure.com` |
| `Arc` | `his.arc.azure.com``guestconfiguration.azure.com` |
| `ArcData`^1^ | `*.<region>.arcdataservices.com` |

Note

The `AAD` bypass value applies only to the endpoints listed in the preceding table. It doesn't bypass regional Microsoft Entra endpoints such as `<region>.login.microsoft.com`. When you configure a proxy server, ensure the proxy allows `*.login.microsoft.com` or each regional endpoint required by your Arc-enabled servers. For more information, see [Connected Machine agent network requirements](network-requirements).

^1^ The proxy bypass value `ArcData` is available starting with Azure Connected Machine agent version 1.36 and Azure Extension for SQL Server version 1.1.2504.99. Earlier versions include the SQL Server enabled by Azure Arc endpoints in the "Arc" proxy bypass value.

To send Microsoft Entra ID and Azure Resource Manager traffic through a proxy server, but skip the proxy for Azure Arc traffic, run the following command:

```bash
azcmagent config set proxy.url "http://ProxyServerFQDN:port"
azcmagent config set proxy.bypass "Arc"
```

To provide a list of services, separate the service names by commas:

```bash
azcmagent config set proxy.bypass "ARM,Arc"
```

To clear the proxy bypass, run the following command:

```bash
azcmagent config clear proxy.bypass
```

You can view the effective proxy server and proxy bypass configuration by running `azcmagent show`.

### Windows environment variables

On Windows, the Azure Connected Machine agent first checks the `proxy.url` agent configuration property (starting with agent version 1.13), and then the system-wide `HTTPS_PROXY` environment variable, to determine which proxy server to use. If both are empty, the agent doesn't use a proxy server, even if the default Windows system-wide proxy setting is configured.

Use the agent-specific proxy configuration instead of the system environment variable.

To set the proxy server environment variable, run the following commands:

```powershell
# If a proxy server is needed, execute these commands with the proxy URL and port.
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://ProxyServerFQDN:port", "Machine")
$env:HTTPS_PROXY = [System.Environment]::GetEnvironmentVariable("HTTPS_PROXY", "Machine")
# For the changes to take effect, the agent services need to be restarted after the proxy environment variable is set.
Restart-Service -Name himds, ExtensionService, GCArcService
```

To configure the agent to stop communicating through a proxy server, run the following commands:

```powershell
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $null, "Machine")
$env:HTTPS_PROXY = [System.Environment]::GetEnvironmentVariable("HTTPS_PROXY", "Machine")
# For the changes to take effect, the agent services need to be restarted after the proxy environment variable removed.
Restart-Service -Name himds, ExtensionService, GCArcService
```

### Linux environment variables

On Linux, the Azure Connected Machine agent first checks the `proxy.url` agent configuration property (starting with agent version 1.13), and then the `HTTPS_PROXY` environment variable set for the himds, GC\_Ext, and GCArcService daemons. An included script configures systemd's default proxy settings so that the Azure Connected Machine agent and all other services on the machine use a specified proxy server.

To configure the agent to communicate through a proxy server, run the following command:

```bash
sudo /opt/azcmagent/bin/azcmagent_proxy add "http://ProxyServerFQDN:port"
```

To remove the environment variable, run the following command:

```bash
sudo /opt/azcmagent/bin/azcmagent_proxy remove
```

### Migrate from environment variables to agent-specific proxy configuration

If you're already using environment variables to configure the proxy server for the Azure Connected Machine agent, and you want to migrate to the agent-specific proxy configuration based on local agent settings, follow these steps:

1. [Upgrade the Azure Connected Machine agent](manage-agent) to the latest version.
2. Configure the agent with your proxy server information by running `azcmagent config set proxy.url "http://ProxyServerFQDN:port"`.
3. Remove the unused environment variables by following the steps for Windows or Linux.