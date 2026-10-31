---
layout: Conceptual
title: CheckPhish and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-checkphish
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the CheckPhish plugin with Microsoft Security Copilot.
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
document_id: c7fd9d9e-7e5a-8912-02e9-66dd03e26155
document_version_independent_id: c7fd9d9e-7e5a-8912-02e9-66dd03e26155
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-checkphish.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-checkphish
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-checkphish.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
platformId: e930d0cd-ede4-8824-301b-24d992866049
---

# CheckPhish and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This plugin allows users to utilize the CheckPhish AI to analyze URLs for potential phishing threats, tech support scams, cryptojacking, and other security risks. Utilizing CheckPhish's advanced machine learning models, this plugin provides detailed insights including:

1. The likelihood of a URL being malicious
2. Classification of the threat type
3. Timestamps for when the URL was last scanned
4. Detailed threat analysis
5. Historical data on URLs to track behavior over time

For more information, see [CheckPhish](https://checkphish.bolster.ai/).

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You need to take the following steps before using the plugin.

1. Get your CheckPhish API key. If you don't have one yet, follow these steps:

    1. Registering on the CheckPhish platform.
    2. Find your API key in your user profile.
    3. Copy the API key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **CheckPhish**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample CheckPhish prompts

After the CheckPhish plugin is configured, you can use the following capabilities with Security Copilot. The following table lists example prompts to try.

| Capability | Example prompts |
| --- | --- |
| URL Scan - Analyze a URL for potential threats  Required input: - URL | - `Ask CheckPhish to check [URL]` - `What does CheckPhish say about [URL]?` |

## Troubleshoot the CheckPhish plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [CheckPhish](https://checkphish.bolster.ai/).