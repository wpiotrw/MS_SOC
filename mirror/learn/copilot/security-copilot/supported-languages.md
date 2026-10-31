---
layout: Conceptual
title: Supported languages in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/supported-languages
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the supported languages in Microsoft Security Copilot
ms.date: 2026-01-12T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.reviewer: 
locale: en-us
document_id: 35fb5908-50f4-3371-c231-c2d86f9eec9b
document_version_independent_id: 35fb5908-50f4-3371-c231-c2d86f9eec9b
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/supported-languages.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: supported-languages
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/supported-languages.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: e7d4e2f3-cbb5-1281-9ac9-85d34f32b620
---

# Supported languages in Microsoft Security Copilot | Microsoft Learn

Security Copilot supports prompts and providing responses in various languages. This topic provides guidance on the supported languages and how to configure a preferred language.

## Supported languages

The following languages are supported in Security Copilot:

| Languages | Availability |
| --- | --- |
| English (US, GB, AU, CA, IN) | Prompting and product interface |
| Spanish (Spain, Mexico) | Prompting and product interface |
| Japanese | Prompting and product interface |
| French (France, Canada) | Prompting and product interface |
| German | Prompting and product interface |
| Portuguese (Brazil) | Prompting and product interface |
| Italian | Prompting and product interface |
| Chinese Simplified | Prompting and product interface |
| Korean | Prompting and product interface |
| Dutch | Product interface |
| Swedish | Product interface |
| Polish | Product interface |
| Portuguese (Portugal) | Product interface |
| Norwegian | Product interface |
| Turkish | Product interface |
| Danish | Product interface |
| Finnish | Product interface |
| Chinese Traditional | Product interface |
| Arabic | Product interface |
| Thai | Product interface |
| Hebrew | Product interface |
| Czech | Product interface |
| Hungarian | Product interface |
| Ukrainian | Product interface |
| Russian | Product interface |

## Configure language preference

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. In the left navigation pane, navigate to your tenant settings.

    ![Screenshot of tenant settings selection.](media/tenant-settings.png)
3. Select **Settings &gt; Preferences**, select your preferred language.

    ![Screenshot of language selection.](media/languages-selection.png)

## Create prompts using supported languages

**Scenario 1: Prompt using a supported language**

If you set a language in the preferences setting and create a prompt using the selected language, the resulting response aligns with your chosen language setting.

**Scenario 2: Prompt in a different language other than the one set in the preferences settings**

If you create a prompt using a supported language other than the one set in the preferences setting, the resulting response aligns with the language you used when you created the prompt - even if a different language was configured in the preferences settings.

For example, if Spanish was set in the preferences settings, but you created a prompt in English, the resulting response will be in English.

**Scenario 3: Prompt in a different language other than the one set in the preferences settings and request for a response in another supported language**

If you create a prompt that explicitly requests a response in a different supported language, the resulting response will adhere to the language you specified in the prompt. This holds true even if you set a different language in the preferences settings or used a different language to create a prompt. The system prioritizes the language explicitly requested within the prompt.

For example, if Spanish was set in the preferences settings, but you created a prompt in English requesting the response be made in Dutch, the resulting response will be in Dutch.

**Scenario 4: Prompt in a non-supported language**

If you create a prompt using a language that isn't supported, an error will be displayed.