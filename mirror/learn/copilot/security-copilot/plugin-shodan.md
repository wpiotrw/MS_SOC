---
layout: Conceptual
title: Shodan and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-shodan
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Shodan plugin with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: cfd693f6-4f0a-57e4-cf2a-239093954bd0
document_version_independent_id: cfd693f6-4f0a-57e4-cf2a-239093954bd0
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-shodan.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-shodan
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-shodan.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: d21dcacc-a8db-be73-8f60-e591aa31f200
---

# Shodan and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Shodan is a search engine that allows users to find specific types of devices connected to the internet using various filters. It provides a global view of how certain devices are connected and can be used to discover which devices are connected to the internet, where they're located, and who is using them. You can use the Shodan plugins with Microsoft Security Copilot to get enhanced visibility of their internet-facing assets and better detect threats and vulnerabilities.

If you do not have a Shodan membership and/or account, you can use the "Shodan InternetDB" plugin to retrieve IP information of open ports, hostnames, open ports, vulnerabilities. If you have a Shodan membership, you can use the "Shodan" plugin with your API key to get access to advanced capabilities that you're subscribed to.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires a [Shodan membership](https://account.shodan.io/billing/member) and an API Key. You'll need to take the following steps before using the plugin.

1. Get your Shodan API key. If you don't have one yet, follow these steps:

    1. Go to your Shodan portal and sign in.
    2. Select **Account**, and on the **Account Overview** tab, next to **API Key**, select **Show**.
    3. Copy your API key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **Shodan**, select the toggle to enable it.
5. In the Shodan Plugin settings pane, in the **Value** field, paste your API key.
6. Save your changes.

## Sample Shodan prompts

After the Shodan plugin is configured, you can use it by typing `Shodan` in your Security Copilot prompt bar.

The following table lists capabilities and example prompts to try:

| Capability | Example prompts |
| --- | --- |
| `Check Shodan InternetDB IP address`(uses Shodan Internet DB Plugin)Ask Shodan InternetDB about an IP addressRequired:- `ip` | `Use the Shodan InternetDB database to provide info on "118.25.6.39"``Check IP address "118.25.6.39" using Shodan InternetDB database` |
| `CheckShodanHostIP`(requires a [Shodan membership](https://account.shodan.io/billing/member))Accepts an IP address (v4 or v6) and provides information about the queried IP, including related country/region, last updated dates, hostnames, and ISP.Required:- `ip`Optional:- `history`- `minify` | `Check IP Address 8.8.8.8 using Shodan``Use Shodan to check IP address  8.8.8.8``What does Shodan say about IP address 8.8.8.8?` |
| `GetShodanHostCount`Behaves like `GetShodanHostSearch`, except that it doesn't return any host results; instead, it returns the total number of results that matched the query and any facet information that was requested. This method doesn't consume query credits.Required:- `query`Optional- `facets` | `What does Shodan know about the host count for port:22?``Use Shodan to look up the host count for port:22` |
| `GetShodanHostSearch`(requires a [Shodan membership](https://account.shodan.io/billing/member))Searches Shodan using the same query syntax as the website and uses facets to get summary information for different properties. This method might use API query credits depending on usage. If any of the following criteria are met, your account is deducted one query credit: - The search query contains a filter.- Accessing results past the first page using the *page*. For every 100 results past the first page, one query credit is deducted.Required:- `query`Optional:- `facets` | `Search for hosts running port:22 using Shodan.``Use Shodan to look up the hosts running port:22.` |
| `GetShodanHostSearchFacets`Returns a list of facets that can be used to get a breakdown of the top values for a property. | `List all search facets from Shodan records.`` What are all the Shodan search facets?` |
| `GetShodanHostSearchFilters`Returns a list of search filters that can be used in the search query. | `List all filters that can be used when searching Shodan records.``What are the Shodan search filters?` |
| `GetShodanHostSearchTokens`Enables you to determine which filters are being used by the query string and what parameters were provided to the filters.Required:- `query` | `Use Shodan to break down Raspbian port:22 into tokens.``Get the Shodan host search tokens for Raspbian port:22.` |
| `GetShodanPorts`Returns a list of port numbers that the crawlers are looking for. | `List all ports that Shodan is crawling on the Internet.``Get all Shodan ports.` |
| `GetShodanProtocols` Returns an object containing all the protocols that can be used when launching an Internet scan. | `List all protocols that can be used when performing on-demand Internet scans via Shodan.``What protocols can be used with Shodan?` |
| `GetShodanScans`(requires a [Shodan membership](https://account.shodan.io/billing/member))Returns a list of all the on-demand scans that are currently active on the account. | `Get list of all the created scans via Shodan.``What are all the scans created by Shodan?` |
| `GetShodanScansID`(requires a [Shodan membership](https://account.shodan.io/billing/member))Checks the progress of a previously submitted scan request. Possible values for the status are:- `SUBMITTING`- `QUEUE`- `PROCESSING`- `DONE`Required:- `id` | `Get the status of the scan request DQdcm6QYgENbGj0R using Shodan.``What does Shodan say about the scan request DQdcm6QYgENbGj0R?` |
| `GetShodanAlertIDInfo`(requires a [Shodan membership](https://account.shodan.io/billing/member))Returns information about a specific network alert.Required:- `id` | `Get the details for the network alert 0DC55K0N2HHZS3D1 using Shodan.``What does Shodan say about the network alert 0DC55K0N2HHZS3D1?` |
| `GetShodanAlertsInfo`(requires a [Shodan membership](https://account.shodan.io/billing/member))Returns a list of all the network alerts that are currently active on the account. | `Get a list created alerts using Shodan.``What are all the created alerts in Shodan?` |
| `GetShodanAlertTriggers`Returns a list of all the triggers that can be enabled on network alerts. | `Get a list of available triggers using Shodan.``What are all the available triggers in Shodan?` |
| `GetShodanNotifiers`Returns a list of all the notifiers that the user has created. | `Get a list of my notifiers using Shodan.``What are all the notifiers in Shodan?` |
| `GetShodanNotifierProvider` Returns a list of all the notification providers that are available and the parameters to submit when creating them. | `Get a list of notifier providers on Shodan.``What are all the notifier providers in Shodan?` |
| `GetShodanBulkData` Returns a list of datasets that can be downloaded in Shodan. | `Get a list of datasets that can be downloaded in Shodan.``What are all the datasets that can be downloaded in Shodan?` |
| `GetShodanBulkDataDataset`Required: - `dataset` Returns a list of files that users can download from the dataset. | `Get a list of files that can be downloaded in Shodan raw-daily dataset.``What are all the files that can be downloaded from Shodan raw-daily dataset?` |
| `GetShodanDomain`Required:  - `domain` Optional: - `history`- `type`Get all the subdomains and other DNS entries for the given domain. | `Check domain google.com using Shodan.``Use Shodan to check domain google.com` |
| `GetShodanDomainResolve`Optional: - `hostnames` Look up the IP address for the provided list of hostnames. | `Check the IP of google.com, facebook.com using Shodan.``Use Shodan to check IP of google.com, facebook.com` |
| `GetShodanDomainReverse`Optional:  - `ips` Look up the hostnames that have been defined for the given list of IP addresses. | `Check the hostnames of 74.125.227.230,204.79.197.200 using Shodan.``Use Shodan to check the domains of 74.125.227.230,204.79.197.200` |
| `GetShodanHTTPHeaders` Shows the HTTP headers that your client sends when connecting to a webserver. | `Check the HTTP headers using Shodan.``Use Shodan to check the HTTP headers.` |
| `GetShodanMyIP` Get your current IP address as seen from the Internet. | `Get my current IP address using Shodan.``Use Shodan to get my current IP address.` |

## Troubleshoot the Shodan plugin

### Errors occur

If you encounter errors occur, such as: *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Shodan](https://www.shodan.io/).