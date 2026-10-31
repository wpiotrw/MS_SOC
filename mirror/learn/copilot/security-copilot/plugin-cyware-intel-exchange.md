---
layout: Conceptual
title: Cyware Intel Exchange and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-cyware-intel-exchange
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Cyware Intel Exchange plugin with Microsoft Security Copilot.
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
document_id: 0d1c565b-5908-9843-c145-3f83abc5200b
document_version_independent_id: 0d1c565b-5908-9843-c145-3f83abc5200b
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-cyware-intel-exchange.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-cyware-intel-exchange
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-cyware-intel-exchange.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 48892a6e-518b-5e25-bdff-5ea224169524
---

# Cyware Intel Exchange and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Cyware Intel is an automated Threat Intelligence Platform (TIP) for ingestion, enrichment, analysis, prioritization, actioning, and bidirectional sharing of threat data.

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
4. Next to **Cyware Intel Exchange**, select **Set up**.
5. Provide your Cyware Respond Instance URL and API Token.
6. Select **Save and Test**. Then select **Save**.

## Sample Cyware Respond prompts

After the Cyware Intel Exchange plugin is configured, you can use the following capabilities with Security Copilot. The following table lists example prompts to try.

| Capability | Example prompts |
| --- | --- |
| Querying Threat Intelligence | - `Search Cyware Intel Exchange for the malware Ryuk.` - `Can you search for the above indicator on Cyware Intel Exchange`. |
| Convert Natural Language query to Cyware query language query | - `Can you give me a CQL query to find all malwares associated with the threat actor APT2?` - `Generate CQL query for searching an indicator on Cyware Intel ExchangeGenerate CQL query for searching an indicator on Cyware Intel Exchange.` |

## Troubleshoot the Cyware Intel Exchange plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Cyware](https://cyware.com).