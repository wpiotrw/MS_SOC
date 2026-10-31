---
layout: Conceptual
title: CrowdSec Cyber Threat Intelligence and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-crowdsec
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the CrowdSec Threat Intelligence plugin with Microsoft Security Copilot.
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
document_id: 474cecb2-cd5e-0aca-6dfe-a3a1054b48ca
document_version_independent_id: 474cecb2-cd5e-0aca-6dfe-a3a1054b48ca
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-crowdsec.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-crowdsec
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-crowdsec.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 52dea951-0e00-6b03-a654-991a68526f23
---

# CrowdSec Cyber Threat Intelligence and Microsoft Security Copilot | Microsoft Learn

[CrowdSec Threat Intelligence](https://www.crowdsec.net/cyber-threat-intelligence) is an open-source, collaborative security stack that enables you to analyze behaviors, respond to attacks, and share signals across the community. CrowdSec Threat Intelligence provides information about IP addresses and verification or identification of potentially aggressive IP addresses. You can use the CrowdSec Cyber Threat Intelligence (CrowdSec CTI) plugin with Microsoft Security Copilot.

This plugin allows users to enhance their IP investigations with threat intelligence sourced from CrowdSec and get insights such as:

- Curated IP and IP range reputations
- Background noise level assessment
- Detailed records of malicious behaviors
- MITRE techniques associated with the IP
- Countries/Regions targeted by the attacker
- Classification of the attacker
- Historical activity and aggressiveness metrics (covering the past 24h, 7 days, 30 days, and overall)

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You'll need to take the following steps before using the plugin.

Note

Depending on which account you have, you might have a limit of up to 50 queries per day. It depends on your licensing for CrowdSec.

1. Get your CrowdSec API key. If you don't have one yet, follow these steps:

    1. Go to the [CrowdSec website](https://app.crowdsec.net) and create your free account.
    2. In your personal account settings, go to **API Keys** and select **+ New key**. You can follow the [steps here] (https://doc.crowdsec.net/u/cti_api/integration_securitycopilot/)
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **CrowdSec Threat Intelligence**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample CrowdSec CTI prompts

After the CrowdSec CTI plugin is configured, you can use it by taking one of the following steps:

- Access the capability directly by typing `LookupIpAddressSmokeDataset` in the prompt bar; or
- Prompt Security Copilot to use the CrowdSec Threat Intelligence API on an IP address

The following table summarizes how this capability works.

| Capability | What it does |
| --- | --- |
| `LookupIpAddressSmokeDataset`Example Prompt(s):  - What can CrowdSec tell me about this IP: [IP]  - According to CrowdSec what are the top targeted countries/regions by this IP: [IP] - Inputs: [IP] Required Input: IP Address | Searches CrowdSec's dataset for an IP address to know more about: - What it does in terms of observed behaviors, targeted protocols, and exploited vulnerabilities. - In what categories it belongs, such as proxy/VPN, CDN exit node, and Legit security scanner. - What it targets, in terms of countries/regions or services.- Existing cross-references, such as lists - How virulent it is. - For how long it's been reported by users. - The confidence level of the information. |

## Troubleshoot the CTI plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. You can either use the product name `CrowdSec` in your prompts, or type the name of a specific capability, like `LookupIpAddressSmokeDataset` instead.

## Provide feedback

To provide feedback, contact CrowdSec through [Discourse](https://discourse.crowdsec.net/) or using the support or feedback action directly in your [CrowdSec Console](https://app.crowdsec.net/).