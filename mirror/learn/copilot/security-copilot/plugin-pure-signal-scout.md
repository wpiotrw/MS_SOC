---
layout: Conceptual
title: Pure Signal Scout and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-pure-signal-scout
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Pure Signal Scout plugin with Microsoft Security Copilot.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
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
document_id: 706312f5-1408-6bc8-b197-bc8b8d88d9d2
document_version_independent_id: 706312f5-1408-6bc8-b197-bc8b8d88d9d2
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-pure-signal-scout.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-pure-signal-scout
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-pure-signal-scout.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 62991abb-8a8c-19f3-ef7b-e6a128da7320
---

# Pure Signal Scout and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

[Pure Signal Scout](https://www.team-cymru.com/threat-intelligence-platform) The Team Cymru's Pure Signal Scout plugin enables Security Copilot customers to gather detailed threat intelligence on IP addresses and domains in real-time. Scout delivers unparalleled speed, accuracy, and visibility, helping security analysts make faster, better-informed decisions. Scout's powerful features ensure that security teams can stay ahead of evolving cyber threats. It provides insights into malicious IP activity, domain information, open ports, communication, and more. With AI-enriched data from sources like Passive DNS and cryptographic certificates, it helps security teams detect and block harmful IPs, streamlining investigations and improving response times.

## Know before you begin

Integration with Security Copilot works with an API key that you must retrieve before using the plugin. You can create a new user account or use your existing account to get the key.

### Set up your Pure Signal Scout account and API key

1. Go to [Scout Insight trial](https://www.team-cymru.com/gate/scout-insight-trial) and fill out the required details.
2. Verify your email and set a password.
3. Sign into the [Pure Signal Scout](https://scout.cymru.com/scout) portal.
4. Go to the [API Keys page](https://scout.cymru.com/api_keys).
5. Select **Create**.
6. (Optional) Add a description for the key.
7. Select **Create Key** to generate the key.
8. If the **Create** button is disabled, your organization has reached the maximum number of keys. In this case, follow these steps:

    1. Next to an old key, select **Revoke**.
    2. Select **Create Key** to start generating a new key.

### Use your existing account and get your API key

1. Sign into the [Pure Signal Scout](https://scout.cymru.com/scout) portal.
2. Go to the API[Keys page](https://scout.cymru.com/api_keys).
3. Select **Create**.
4. (Optional) Add a description for the key.
5. Select **Create Key** to generate the key.
6. If the **Create** button is disabled, your organization has reached the maximum number of keys. In this case, follow these steps:

    1. Next to an old key, select **Revoke**.
    2. Select **Create Key** to start generating a new key.

## Configure the Pure Signal Scout Plugin in Security Copilot

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Next to **Pure Signal Scout Plugin**, select **Set up**.

    ![Image of the Pure Signal Scout plugin.](media/pure-signal-scout-plugin.png)
4. In the **Value** field, paste the Pure Signal Scout API key, and then select **Save**.

    ![Image of the Pure Signal Scout plugin settings.](media/api-key-value.png)

## Sample Pure Signal Scout prompts

| Capability | Description | Input Parameters | Example Prompts |
| --- | --- | --- | --- |
| `ScoutFoundationAPI` | Accepts IP addresses and enables bulk analysis, offering insights into whether the set contains suspicious, malicious, or informational IPs. The Scout Foundation API also provides AS information, country codes, and key tags associated with IP addresses. | Required: ips (max 10 IP Addresses) | - `List down the malicious and suspicious IPs from these 8.8.8.8 175.155.2.48 185.220.101.101 192.42.116.175 188.165.200.97 185.220.101.88 178.20.55.182 104.182.36.17 with help of Pure Signal Scout plugin.`- `Using the Pure Signal Scout plugin, find if the IP Address 185.220.100.240 is malicious ?`- `List down key tag associated with IP Address 12wd85.220.100.240 using Scout plugin.` |
| `ScoutIPDetailsAPI` | The Scout IP Details API provides comprehensive information about a specific IP address, covering details such as identity, network communication history, passive DNS data, open ports, X.509 certificates, TLS/SSL fingerprints, and WHOIS records. This endpoint enables users to retrieve a full report on an IP address's behavior and relationships over time by specifying start and end dates or selecting a range of days. | Required: `IP AddressOptional: start_date` :`start_date` can't be more than 90 days back from current date & 30 days before end date `end_date :` can't be in the future Days: min: 1, max: 30 (Relative offset in days from current time in UTC. It can't exceed the maximum range of 30 days.) `size:` default: 100, min: 1, max: 1000 (The size of the response, in records, to return) `sections: identity` comms pdns open\_ports x509 fingerprints whois summary proto\_by\_ip | - `Using Pure Signal Scout to find what open ports are available on this IP address 47.156.224.38?`- `Are there any unusual communication patterns for this IP address 47.156.224.38? Check with the Pure Signal Scout plugin.`- `What are the most frequent destinations for this IP address 47.156.224.38? Find using Scout plugin.`- `Using Scout plugin find what are the connections between this IP address 47.156.224.38 and specific ASNs?`- `Has this IP address 175.155.2.48 been seen in any honeypot data? Find using Scout.`- `What are the potential threats associated with this IP address 175.155.2.48?`- `What are the country/region origins of IPs communicating with this one IP 47.156.224.38?` |
| `ScoutSearchAPI` | The Scout Search API provides detailed information about domains and supports advanced search queries using the Scout Query Language. It returns results that may include country codes, autonomous system (AS) information, tags, WHOIS data, open ports, passive DNS (PDNS), communication details, service information, X.509 certificates, and fingerprints. This API allows users to build a query using various formats, including IP address, domain names, websites, or advanced queries with specific selectors (for example, pdns.domain). Full details on the available search selectors can be found at Scout documentation. | Required: query Optional: `start_date:` can't be more than 90 days back from current date & 30 days before end date`end_date:` can't be future Days: min: 1, max: 30 (Relative offset in days from current time in UTC. It can't exceed the maximum range of 30 days.) size: default: 100, min: 1, max: 5000 (The size of the response, in records, to return) | - `Using Pure Signal Scout to find what is the WHOIS information for this domain 10crypto.top ?`- `Using the Pure Signal Scout plugin can you show me the historical DNS data for this domain akamai.com?`- `What are the most recent WHOIS updates for this subtitleseeker.com? Use Scout plugin.`- `Using Scout to find what is the reverse WHOIS information for this domain 10crypto.top?`- `Use Scout to run the query pdns.domain="*ngrok.io" and give the certificate details about top 10 associated IPs.`- `What organization is associated with subtitleseeker.com in the WHOIS data? Use Scout.` |

## Troubleshoot the Pure Signal Scout plugin

### Errors occur

If you encounter errors like "Couldn't complete your request," try these steps to troubleshoot:

1. Start a new session to refresh context and attempt the prompt again in a new session.
2. Specify a Detailed Prompt: Refer to the best prompt guidelines for Security Copilot [here](https://github.com/Azure/Copilot-For-Security/tree/main/Customer%20Guides/Prompting%20Tips%20for%20Copilot%20For%20Security) and crafting detailed prompts according to Pure Signal Scout plugin skills and capabilities.
3. Adjust the Size Parameter: If the issue persists, reduce the size parameter in your prompt to control response size, for example, "Use size as 10." This can also be adjusted in the IP Details API or Scout Search API to help minimize response payloads.

If the issue continues, sign out of Security Copilot, then sign back in and try again.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities or if they seem to be activating a different plugin, it may be due to other plugins or custom plugins that provide similar capabilities as Pure Signal Scout. For instance, if you have multiple plugins that offer threat intelligence or domain information, conflicts might arise. To prioritize and specifically Pure Signal Scout, consider disabling other custom plugins. Alternatively, you can either use the product name **Pure Signal Scout** in your prompts or specify a particular skill.

## Provide feedback on the Pure Signal Scout plugin

To provide feedback, contact [Pure Signal Scout](https://www.team-cymru.com/?gad_source=1&amp;gclid=CjwKCAiAjeW6BhBAEiwAdKltMm72qzik3SegFtikdzegOtlrOCB45YVNWp2nqrHQdueTp3SSgDMv0xoCWHEQAvD_BwE).