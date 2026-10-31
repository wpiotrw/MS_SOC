---
layout: Conceptual
title: AbuseIPDB and  Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-abuseipdb
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the AbuseIPDB plugin with Microsoft Security Copilot.
ms.date: 2026-01-15T00:00:00.0000000Z
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
document_id: f5d5d31d-71eb-2f1d-53c4-76dad2f5bda0
document_version_independent_id: f5d5d31d-71eb-2f1d-53c4-76dad2f5bda0
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-abuseipdb.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-abuseipdb
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-abuseipdb.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: af7dfd70-47f0-2366-6750-6138407a18e7
---

# AbuseIPDB and  Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

AbuseIPDB is a project managed by Marathon Studios Inc. Their mission is to help make the Web safer by providing a central repository for Webmasters, System Administrators, and other interested parties to report and identify IP addresses that have been associated with malicious activity online. You can use the AbuseIPDB plugin with Microsoft Security Copilot.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You'll need to take the following steps before using the plugin.

1. Get your AbuseIPDB API key. If you don't have one yet, follow these steps:

    1. Go to the [AbuseIPDB website](https://www.abuseipdb.com/).
    2. Select on the **Sign Up** button, located at the top right corner of the page.
    3. Fill in the required information, such as your email address, username, and password.
    4. Complete any other steps for verification, if necessary.
    5. Once registered, sign-in to your AbuseIPDB account.
2. Access the API key.

    1. After logging in, go to the [AbuseIPDB Homepage](https://www.abuseipdb.com/) page.
    2. Navigate to the API tab and select on **Create key**.
    3. After clicking on Create Key a modal appears. You'll be asked to input a name; you can pick any name for your key. For example, enter "developer\_key" and select the create button.
    4. The newly generated API key should populate on the same API tab. You need this same key-in later steps for the connector.
3. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
4. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
5. Next to **AbuseIPDB**, select **Set up**.
6. In the AbuseIPDB plugin settings pane, in the **Value** field, paste your API Key, and then select **Save**.

## Sample AbuseIPDB prompts

After the AbuseIPDB plugin is configured, you can use the following capabilities with Security Copilot.

The following table provides examples you can try:

| Capability | Input | Example prompts |
| --- | --- | --- |
| `CheckIPAddress` Accepts an IP address (v4 or v6) and provides information about the queried IP, including version, origin country/region, usage type, ISP, and domain. Abusive reports are included. | Required: - `ipAddress` Optional: - `maxAgeInDays` (default 30, min 1, max 365) - `verbose` | - Tell me about IP address 118.25.6.39 using AbuseIPDB database  - What does the abuseipdb database say about the IP address 180.126.219.127? - I'm curious about any abuseipdb records for the IP address 180.126.219.127. Can you look that up for me for the last 10 days? |
| `CheckNetworkBlock` This capability takes a subnet in CIDR notation (v4 or v6) and returns details about the queried network, including its netmask, possible hosts count, and address space description. URL-encode the network due to forward slashes in CIDR notation. | Required: - `network` Optional: - `maxAgeInDays`(default 30, min 1, max 365) | - Check the network block 1.1.1.1/24 for any reported IP addresses within the past 10 days. - I'm trying to find out if there are any reported IP addresses on the network block 1.1.1.1/24 in the past 10 days. Can you assist me with that?- Could you help me check if any IP addresses are reported on the network block 1.1.1.1/24 within the last 10 days? |
| `ListBlockListedIpAddresses` This capability returns a list IP addresses most reported by AbuseIPDB users with or without other filters. Entries include IP, abuse score, and last report timestamp, sorted by score and timestamp. | Optional:- `confidenceMinimum` (default 100, min 25, max 100)- `limit`(default 10,000, min 1, restrictions)- `plaintext`-`onlyCountries`-`exceptCountries`- `ipVersion`(default 4,6 mixed) | - List blocklisted IP addresses from AbuseIPDB - According to AbuseIPDB, are there any blocklisted IP addresses from China? |
| `ReportIPAddress` Reporting IP addresses is the core feature of AbuseIPDB. To report an IP address, use this skill. It will return the updated abuseConfidenceScore for the IP address we specify. | Required: - `ip` - `categories` (restrictions 30, these nos. belong to a mapping)  Optional:  - `comment` - `timestamp` | - Could you report the IP address 180.126.219.126 on AbuseIPDB for category 18 and add a comment "This category is separate from DDoS attacks."? - Submit the IP address 180.126.219.126 to AbuseIPDB, tagging it as category 1,2. - Make an entry for the IP address 180.126.219.126 in AbuseIPDB, designating it as category 18. |

## Provide feedback

To provide feedback, contact [AbuseIPDB](https://www.abuseipdb.com/).