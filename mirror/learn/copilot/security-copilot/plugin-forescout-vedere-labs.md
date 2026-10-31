---
layout: Conceptual
title: Forescout Vedere Labs and  Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-forescout-vedere-labs
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Forescout Vedere Labs plugin with Microsoft Security Copilot.
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
document_id: 15f3e31a-3638-f035-03c5-bd7286274c45
document_version_independent_id: 15f3e31a-3638-f035-03c5-bd7286274c45
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-forescout-vedere-labs.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-forescout-vedere-labs
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-forescout-vedere-labs.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 34750004-83c7-8c26-5828-fa59d67e2095
---

# Forescout Vedere Labs and  Microsoft Security Copilot | Microsoft Learn

Forescout Vedere Labs research team provides a threat intelligence feed containing IP, URL, and File hash indicators for all activity seen and monitored by Forescout, including information on Known Exploited Vulnerabilities and Vedere Labs own reported CVEs. With the extensive research conducted, this provides indicators and CVE details across IT, OT, IoT and IoMT, allowing anyone to benefit from this research. The research helps security teams speed up threat hunting efforts in combination with Microsoft Security Copilot. Additionally, this service also allows for lookups against domain names to check for use of Domain Generation Algorithms (DGA) or data exfiltration techniques.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Prerequisites

Forescout Vedere Labs Threat Feed API Key.

## Know before you begin

Integration with Security Copilot requires an API key for authorization. Navigate to [Forescout Vedere Labs](https://forescout.vederelabs.com/register) and register for a free API Key to start taking advantage of the vulnerabilities and indicators provided by this feed. You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
3. Next to **Forescout Vedere Labs**, select **Set up**.
4. In the Forescout Vedere Labs settings pane, input your API key in the **Value** field, and then select **Save**.

## Sample Forescout Vedere Labs prompts

After the Forescout Vedere Labs plugin is configured, you can use the following capabilities with Security Copilot.

The following table provides examples you can try:

| Capability | Example prompts |
| --- | --- |
| Get Indicators | `Show me vedere labs file indicators for the past 8 hours``Tell me about any indicators for [IP] or [File Hash]` |
| Get Exploited CVEs | `Show me all known exploited vulnerabilities in the last 7 days``give me the latest 5 KEVs according to Vedere Labs from the past 7 days with a confidence score of at least 6` |
| Get Vedere Labs CVEs | `Show me the most recent Vedere Labs CVE` |
| Lookup Domain | `Has "example.com" got any indicators of malicious use``Check if "dga.com" is using any techniques related to malware` |

## Provide feedback

To provide feedback, contact [Forescout Vedere Labs](https://forescout.vederelabs.com/).