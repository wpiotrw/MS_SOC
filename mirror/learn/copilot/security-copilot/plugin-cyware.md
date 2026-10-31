---
layout: Conceptual
title: Cyware Respond and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-cyware
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Cyware plugin with Microsoft Security Copilot.
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
document_id: a72ea284-c88f-708b-678f-fed44aef8db5
document_version_independent_id: a72ea284-c88f-708b-678f-fed44aef8db5
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-cyware.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-cyware
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-cyware.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 3abb5af0-51da-57c7-7cf0-840697a9916f
---

# Cyware Respond and Microsoft Security Copilot | Microsoft Learn

Cyware offers threat intelligence management, security collaboration, and orchestrated response solutions. Cyware Respond is an end-to-end incident management and threat response automation platform. You can use the Cyware Respond plugin with Microsoft Security Copilot to find specific types of incidents, actions, applications, critical software assets, malware, vulnerabilities, and more.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires an API Key. You'll need to take the following steps before using the plugin.

1. Get your Cyware Respond API key. If you don't have one yet, follow these steps:

    1. Go to the [Cyware website](https://cyware.com) and create an account.
    2. Go to the Admin panel, and then go to **Open APIs**.
    3. Create a new OpenAPI credential set.
    4. Copy your OpenAPI token generated.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **Cyware Respond**, select **Set up**.
5. Provide your Cyware Respond Instance URL and API Token.
6. Select **Save and Test**. Then select **Save**.

## Sample Cyware Respond prompts

After the Cyware Respond plugin is configured, you can use it by typing `Cyware Respond` in your Security Copilot prompt bar, followed by an action. The following table provides several examples you can try:

| Capability | Example prompts |
| --- | --- |
| **Incident Management** |  |
| Querying incidents | `"Search for incidents related to 'ransomware' in Cyware Respond."``"Find incidents mentioning 'data breach' in Cyware Respond."` |
| Retrieving incident details | `"Get details for the above incident from Cyware Respond."``"Show more information about the incident in Cyware Respond with UUID <uuid>."` |
| **Action Management** |  |
| Querying actions | `"Look up actions tagged with 'isolate' from this week in Cyware Respond."``"Find all 'network scan' actions performed yesterday in Cyware Respond."` |
| Action details | `"Retrieve details of the last action we discussed from Cyware Respond."``"Can you provide more info on the previously mentioned action in Cyware Respond?"` |
| **Application Management** |  |
| Querying applications | `"Search for applications with 'firewall' in their name in Cyware Respond."``"Find security tools updated recently in Cyware Respond."` |
| Application details | `"Get details for the above application from Cyware Respond."``"Show configuration details for the previously discussed security application in Cyware Respond."` |
| **Software asset management** |  |
| Querying software assets | `"List critical software assets in Cyware Respond."``"Search for software needing updates in Cyware Respond."` |
| Software details | `"Provide details for the last mentioned software asset in Cyware Respond."``"Can you fetch the version info of the software we talked about earlier in Cyware Respond?"` |
| **Campaign management** |  |
| Querying campaigns | `"Find all active campaigns related to 'phishing' in Cyware Respond."``"Search for recent campaigns targeting remote employees in Cyware Respond."` |
| Campaign details | `"Get campaign details for the previously mentioned campaign in Cyware Respond."``"Show more details about that cyber threat campaign from Cyware Respond."` |
| **Threat intelligence management** |  |
| Querying threat intelligence | `"Search for threat intel on 'DDoS attacks' in Cyware Respond."``"Retrieve updates on 'APT groups' from this week in Cyware Respond."` |
| Threat intel details | `"Show details of the last threat intel we discussed in Cyware Respond."``"Can you provide more info on the threat actor mentioned earlier in Cyware Respond?"` |
| **Malware Management** |  |
| Querying malware | `"Find all malware detections from the past week in Cyware Respond."``"Search for 'spyware' detections in the marketing department in Cyware Respond."` |
| Malware details | `"Give me the details of the previously mentioned malware in Cyware Respond."``"I need more information on that 'ransomware' we identified in Cyware Respond."` |
| **Vulnerability management** |  |
| Querying vulnerabilities | `"Search for high-severity vulnerabilities in Cyware Respond."``"List all vulnerabilities discovered in the network infrastructure in Cyware Respond."` |
| Vulnerability details | `"Get details of the vulnerability we discussed last time in Cyware Respond."``"Show mitigation steps for the above-mentioned vulnerability in Cyware Respond.` |

## Troubleshoot the Cyware plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Cyware](https://cyware.com).