---
layout: Conceptual
title: UrlScan and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-urlscan
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use UrlScan with Microsoft Security Copilot.
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
document_id: 67ea271d-429c-1865-0639-e39f40fd1083
document_version_independent_id: 67ea271d-429c-1865-0639-e39f40fd1083
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-urlscan.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-urlscan
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-urlscan.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 7d4790d8-051b-b8ec-73f4-f214173919f6
---

# UrlScan and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

UrlScan.io is a free online service and tool that allows users to scan and analyze URLs (Uniform Resource Locators) or website links to determine potential security threats and risks associated with those URLs. It helps users assess the safety and trustworthiness of a website or a specific web page.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You'll need to take the following steps before using the plugin.

1. Get your URL Scan API key. If you don't have one yet, follow these steps:

    1. Go to the [urlscan.io website](https://urlscan.io/) and create your account. Then sign in.
    2. Go to your profile page, and then select **+ Create API key**.
    3. Return to your profile page, and copy your API Key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **UrlScan**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample UrlScan prompts

After the UrlScan plugin is configured, you can use it by taking one of the following steps:

- Access the capability directly by typing `UrlScan` in the prompt bar; or
- Prompt Security Copilot to use the UrlScan API on a website

The following table summarizes how this capability works.

| Capability | Example prompts | What it does |
| --- | --- | --- |
| `UrlScan`Required Input: URL | - `Can you scan https://www.microsoft.com/en-us/ for threats.`- `Use Url scan to check if https://www.microsoft.com/en-us/ is malicious` | Scans a URL for potential security threats and risks. |

## Troubleshoot the UrlScan plugin

### Errors occur

If you counter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [UrlScan](https://urlscan.io/).