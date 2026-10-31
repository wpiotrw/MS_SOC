---
layout: Conceptual
title: Valence Security and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-valence
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Valence Security plugin with Microsoft Security Copilot.
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
document_id: 86dcc7b6-1667-db80-7575-419b9b435257
document_version_independent_id: 86dcc7b6-1667-db80-7575-419b9b435257
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-valence.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-valence
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-valence.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 461c0ca9-8788-9376-16ea-f4e4478f5bb6
---

# Valence Security and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Valence combines SaaS security posture management (SSPM) and advanced remediation with business user collaboration to find and fix Software as a Service (SaaS) security risks. The Valence SaaS Security Platform provides visibility and remediation capabilities for business-critical SaaS applications. You can use the Valence Security plugin with Microsoft Security Copilot to:

- Investigate user activity across multiple SaaS platforms; and
- Create reports to understand a specific user's SaaS security posture

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires a Valence Security subscription and an API Key. You'll need to take the following steps before using the plugin.

1. Get your API key. If you don't have one, follow these steps:

    1. Go to the [Valence Security web site](https://www.valencesecurity.com) and sign in.
    2. Go to [API Keys Settings](https://app.valencesecurity.com/settings/apikeys) and generate your API key.
    3. Copy your API key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **Valence Security**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample Valence Security prompts

After the Valence Security plugin is configured, you can use it to investigate or report on user activities across SaaS platforms. The following table provides some example prompts you can try in your Security Copilot prompt bar:

| Capability | Example prompts |
| --- | --- |
| Investigate user activities across SaaS platforms | `"Which high privileged actions did <USER> take over the past day?"``"Show me recent alerts for <USER>"` |
| Create a report about user activities in SaaS platforms | `"Summarize <USER> security SaaS posture"` |

## Troubleshoot the Valence Security plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Valence Security](https://www.valencesecurity.com).