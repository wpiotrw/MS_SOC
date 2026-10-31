---
layout: Conceptual
title: GreyNoise Enterprise and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-greynoise
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use GreyNoise Enterprise and GreyNoise Community with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: partner-contribution
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 7cedabf8-b431-930e-f41d-33b419e6c9e0
document_version_independent_id: 7cedabf8-b431-930e-f41d-33b419e6c9e0
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-greynoise.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-greynoise
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-greynoise.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 21120095-7796-4b7c-64bc-89b0c937657d
---

# GreyNoise Enterprise and Microsoft Security Copilot | Microsoft Learn

GreyNoise Enterprise is a cybersecurity platform that collects and analyzes Internet-wide scan and attack data to provide valuable insights into potential threats. GreyNoise integration enables you to use the GreyNoise database to enhance your organization's security posture, identify emerging threats, and prioritize response efforts. You can use either the GreyNoise Enterprise or GreyNoise Community plugin with Security Copilot to get information about IP addresses, scanning activity, and attacker behaviors.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with a GreyNoise account and an API key. Depending on the plan you choose, you might have a limit on how many queries you can run using your API Key. You'll need to take the following steps before using the plugin.

1. Get your GreyNoise credentials and API key. If you don't have them yet, follow these steps:

    1. Go to the [GreyNoise website](https://viz.greynoise.io/signup) and create your account.

        You can start with a free account to obtain a community API Key, or purchase a subscription to obtain an enterprise API Key.
    2. In [GreyNoise Visualizer](https://viz.greynoise.io), in the upper right corner, select your name, and then select **My API Key**.
    3. Copy your API Key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Take one of the following steps:

    - If you purchased a GreyNoise enterprise subscription, turn **GreyNoise Enterprise Plugin** on.
    - If you're using a free GreyNoise account, turn **GreyNoise Community Plugin** on.
5. Select the Settings icon, and in the **Value** field, paste your API Key, and then select **Save**.

## Sample GreyNoise prompts

After you set up your GreyNoise plugin, you can use it by typing a capability name in your prompt bar in Security Copilot. For example, you can type `LookupIpAddressNoise`.

The following table summarizes capabilities and what they do.

| Capability | Example prompts | What it does |
| --- | --- | --- |
| `Lookup IP Address Noise`(works with either GreyNoise Enterprise or GreyNoise Community)Required Input: IP Address (v4 or v6) | - `Tell me about Ip address "118.25.6.39" using the GreyNoise database`- `Use the GreyNoise database to provide info on "118.25.6.39"`- `What does the GreyNoise database say about the IP address 180.126.219.127?`- `I'm curious about any GreyNoise records for the IP address 180.126.219.127. Can you look that up for me?`- `Can you provide me with information on any GreyNoise reports for the IP address 180.126.219.127?`- `I'd like to know if there are any GreyNoise entries for the IP address 180.126.219.127. Can you check that for me?`- `Could you give me an overview of the GreyNoise record for the IP address 180.126.219.127?` | Retrieves noise information about the provided IP address. Returns the following kinds of information: - IP address classification, such as malicious - Noise, such as whether the IP address is likely involved in some form of malicious activity - Riot, such as whether the IP is part of a known benign service or infrastructure - Name associated with the IP - Last seen (when the IP was last active) - Link: A link to visualize the IP's activity on GreyNoise - Success or error message depending, on whether the lookup was successful |
| `Lookup IP Context`(requires GreyNoise Enterprise)Required Input: IP Address (v4 or v6) | `Find the GreyNoise IP Context for IP 183.221.243.13` | Provides context about IPs that GreyNoise observed scanning the internet. Returns a comprehensive set of information including classification (malicious, benign, etc.), last seen timestamp, associated actors, tags, and metadata. |
| `Lookup IP Quick`(requires GreyNoise Enterprise)Required Input: IP Address (v4 or v6) | `Use GreyNoise to do a quick check of IP 183.221.243.13` | Provides a quick way to check if an IP is "noise" or not. Returns a boolean indicating whether the IP is present in the dataset or not. |
| `Lookup Multiple IPs`(requires GreyNoise Enterprise)Required Input: IP Address (v4 or v6) | `Lookup Multiple IPs using GreyNoise 183.221.243.13 and 8.8.8.8` | Provides a quick way to check information on multiple IPs. Returns an array of context information for each IP address, similar to the LookupIpContext endpoint. |
| `Lookup IP Riot`(requires GreyNoise Enterprise)Required Input: IP Address (v4 or v6) | `Use GreyNoise to check the Riot information on IP 183.221.243.13` | Provides information about IPs commonly added to allowlists. Returns a boolean indicating whether the IP is part of the RIOT dataset or not, along with some basic context information if it is. |
| `Lookup GNQL`(requires GreyNoise Enterprise)Required Input: GNQL Query | `Use GreyNoise to check the GNQL information on tags:"RDP Scanner"` | Allows you to use the GreyNoise Query Language (GNQL) to make complex queries against the GreyNoise dataset. Returns an array of results that match the GNQL query. |
| `Look up CVE`(requires GreyNoise Enterprise)Required Input: CVE | `Use the GreyNoise Query Language (GNQL) stats to query against the GreyNoise dataset for CVE information` | Allows you to use the GreyNoise Query Language (GNQL) stats to query against the GreyNoise dataset for CVE information Returns an array of results that match the GNQL CVE query. |

## Troubleshoot the GreyNoise plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

## Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. To prioritize and target GreyNoise, try disabling other custom plugins.

## Provide feedback

To provide feedback, contact [GreyNoise](https://viz.greynoise.io/).