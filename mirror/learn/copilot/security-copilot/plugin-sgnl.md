---
layout: Conceptual
title: SGNL and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-sgnl
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use SGNL with Microsoft Security Copilot.
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
document_id: 6fb461d6-95df-788e-3463-b32268cfc0e7
document_version_independent_id: 6fb461d6-95df-788e-3463-b32268cfc0e7
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-sgnl.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-sgnl
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-sgnl.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: adbf3297-ca8b-6931-95f4-8335f94ca2dd
---

# SGNL and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

SGNL provides a dynamic access platform that provides a foundation for Zero Standing Privilege (ZSP) initiatives to protect against threats to user sessions and credentials. You can use the SGNL Access Intelligence plugin with Microsoft Security Copilot to understand and identify fine-grained access decisions and trends across your organization.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires your SGNL tenant ID and ID token. Make sure your SGNL account has sufficient permissions to read the SGNL Access Decision Logs. You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Next to **SGNL**, select **Set up**.
4. Paste your SGNL tenant ID in the Username field, and your ID token in the password field. Then select **Save**.

## Sample SGNL prompts

After the SGNL plugin is configured, you can use it to summarize logs and identify who accesses sensitive assets. The following table lists some capabilities and example prompts you can try:

| Capability | Example prompt |
| --- | --- |
| Summarize SGNL logs | `Summarize the logs from SGNL for today` |
| Identify principals who accessed sensitive assets | `Which principals have accessed sensitive assets today` |
| Identify who accessed a specific asset | `Which users have accessed <Asset>` |
| Summarize a user's access for a specific time period | `Tell me about <user> access over the last 7 days` |

## Troubleshoot the SGNL plugin

### Errors occur

If you encounter errors occur, such as: *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [SGNL](https://www.sgnl.ai/).