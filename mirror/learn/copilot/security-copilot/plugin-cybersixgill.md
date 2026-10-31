---
layout: Conceptual
title: Cybersixgill and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-cybersixgill
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Cybersixgill plugin you can use with Microsoft Security Copilot.
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
document_id: 37a03d2b-aac5-f54f-6c0b-3f61becb5ec2
document_version_independent_id: 37a03d2b-aac5-f54f-6c0b-3f61becb5ec2
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-cybersixgill.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-cybersixgill
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-cybersixgill.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 1ba2804c-67a1-5a33-7a69-adba434054d7
---

# Cybersixgill and Microsoft Security Copilot | Microsoft Learn

Cybersixgill offers real-time threat intelligence solutions to help security teams detect and respond to imminent threats from the clear, deep, and dark web.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Prerequisites

- The plugin requires the use of an API key that can be obtained from Cybersixgill [developer portal](https://developer.cybersixgill.com/).
- Once logged into the developer portal, obtain and safely copy your API client ID and secret.

Note

If you aren't a Cybersixgill customer, send email to cfs@cybersixgill.com to get your three-month free trial.

## Know before you begin

You need to take the following steps to use the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Select **Settings** to configure your **Cybersixgill** plugin.
4. Select **Save** and begin prompting in Security Copilot.

## Sample Cybersixgill prompts

After the Cybersixgill plugin is configured, you can try one or more of the capabilities listed in the following table:

| Capability | Example prompts |
| --- | --- |
| Check if my organizational credentials were compromised in the dark web | - `According to Cybersixgill, tell me if credentials   of my organization were compromised in the dark web in the last month` - `According to Cybersixgill, tell me if the   following xxx@xxx.com   credentials were exposed in the dark web in the last month` |
| Search about recent breach/ransomware events | - `According to Cybersixgill, Tell me about the last   10 breach events from forum_breach related to the UK. Summarize it in a table   and provide victim name with sector``Tell me about ransomware attacks in the last 90   days targeting the healthcare sector using Cybersixgill database` |
| Get details about specific CVE | - `According to Cybersixgill, tell me if for   CVE-2023-34362 there is POC, metasploit and known to be exploited in the wild   with any associated APTs. include references` |
| Get comprehensive profiles of APTs, Actors, and related Malware and IOCs | - `According to Cybersixgill, tell me about related   malware and IOCs for APT39`- `According to Cybersixgill, tell me about associated APTs with Raccoon Stealer?` - `According to Cybersixgill, I'm a CTI analyst at a   european MSSP. A customer of mine is worried about the APT MuddyWater. Tell   me about it` - `According to Cybersixgill, tell me to which apt  cve-2023-36884 is connected to` |
| Lookup on specific IOCs or IPs | - `According to Cybersixgill, tell me about the following IP [IP]` - `According to Cybersixgill, give me IOCs for racoon stealer` |

## Troubleshoot the Cybersixgill plugin

### Errors occur

If you get errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. For example, if you're using multiple sources that provide information like Cybersixgill, there might be conflicts. Try using the product name `Cybersixgill` in your prompts.

## Provide feedback

To provide feedback, contact [Cybersixgill](https://cybersixgill.com/).