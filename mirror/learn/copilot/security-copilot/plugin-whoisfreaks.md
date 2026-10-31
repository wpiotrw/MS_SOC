---
layout: Conceptual
title: Whoisfreaks and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-whoisfreaks
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Whoisfreaks plugin you can use with Microsoft Security Copilot.
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
document_id: 095b4adb-d3a5-58fa-e0dd-50984d1252da
document_version_independent_id: 095b4adb-d3a5-58fa-e0dd-50984d1252da
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-whoisfreaks.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-whoisfreaks
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-whoisfreaks.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: b66ed85d-4276-8cd2-dfff-0ff21ab1b7fd
---

# Whoisfreaks and Microsoft Security Copilot | Microsoft Learn

Whoisfreaks helps elevate your cyber-security strategy with domain and IP intelligence services. Designed for analysts, researchers, and brand owners. Our platform provides unparalleled insights and monitoring capabilities to protect your digital assets. Stay ahead of threats, ensure brand integrity, and make informed decisions with real-time data you can trust. Our platform seamlessly integrates with existing systems, enhancing workflow efficiency and effectiveness.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Prerequisites

- The plugin requires the use of an API key that can be obtained from the Whoisfreaks [portal](https://whoisfreaks.com/signup.html)
- Once logged into the Whoisfreaks portal, obtain and safely copy your API key.

## Know before you begin

You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Select **Settings** to configure your **Whoisfreaks** plugin.
4. Select **Save** and begin prompting in Security Copilot.

## Sample Whoisfreaks prompts

After the Whoisfreaks plugin is configured, you can try one or more of the capabilities listed in the following table:

| Capability | Example prompts |
| --- | --- |
| Get Whoisfreaks Live, historical, and reverse WHOIS data | `Give me ownership details of ipgeolocation.io using whoisfreaks.``Which domains are acquired by <Name>?` |
| Get Whoisfreaks Live, historical and reverse DNS information | `give me historical DNS data for  <domain name>` |
| Get Whoisfreaks Live SSL Certificates Info for a specific domain | `When does whoisfreaks.com' SSL certificate expire?` |
| Get Whoisfreaks IP WHOIS info | `Give me WHOIS details of 8.8.8.8` |
| Get Whoisfreaks ASN WHOIS info | `'AS13335' AS number belongs to which organization?` |
| Get Whoisfreaks Domain Availability | `Is 'whoisfreaks.pk' a registered domain or not?` |

## Troubleshoot the Whoisfreaks plugin

### Errors occur

If you get errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. For example, if you're using multiple sources that provide information like Whoisfreaks, there might be conflicts.

## Provide feedback

To provide feedback, contact [Whoisfreaks](https://whoisfreaks.com).