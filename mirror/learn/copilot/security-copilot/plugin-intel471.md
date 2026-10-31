---
layout: Conceptual
title: Intel 471 Threat Intelligence and  Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-intel471
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Intel 471 Threat Intelligence plugin with Microsoft Security Copilot.
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
document_id: 1a3aadc0-4bf0-c3e4-3c87-f4ea884429f8
document_version_independent_id: 1a3aadc0-4bf0-c3e4-3c87-f4ea884429f8
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-intel471.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-intel471
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-intel471.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 1424f6b1-68f6-d8bb-bd42-8796a046436d
---

# Intel 471 Threat Intelligence and  Microsoft Security Copilot | Microsoft Learn

Intel 471 delivers relevant and timely insights into the cyber underground.

You can use the Intel 471 Threat Intelligence plugin with Microsoft Security Copilot to provide:

- Rich context about threats through indicators of compromise to facilitate responding to active threats found in the networks and CTI analysis.
- Relevant and timely intelligence information about the activity groups and adversary scenarios.
- Visibility of potential third-party breaches to improve the risk posture and change the odds of a successful attack.
- Vulnerability intelligence, including the precursors to such activity such as an increase in interest levels among activity groups, proof-of-concept (POC) code being developed, traded, or sold, and more.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires Intel 471 API credentials, which are available as part of Intel 471's paid subscriptions. For more information, please contact sales@intel471.com. You'll need to take the following steps before using the plugin.

1. Get your Intel 471 user account and password.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
4. Next to **Intel 471 Threat Intelligence**, select **Set up**.

    ![Screenshot showing the Intel 471 plugin.](media/intel471-1.png)
5. In the Intel 471 Threat Intelligence settings pane, provide your Intel 471 user account and password.
6. Save your changes.

## Sample Intel 471 Threat Intelligence prompts

After the Intel 471 Threat Intelligence plugin is configured, you can use natural language prompts such as the examples provided in the following image. You can also choose them from the prompts menu located in the prompt input.

![Screenshot showing the Intel 471 plugin example uses.](media/intel471-2.png)

The following table provides examples you can try:

| Capability Prompt Suggestion | Example natural language prompt |
| --- | --- |
| Malware Intelligence | - Search for Malware Intelligence Indicator with sha256 hash cdf2489960aa1acefedf4f1ab4165365db481591a17e31e7b5fca03cc0ccff0f  - Search for reports on operaloader malware family |
| Vulnerability Intelligence | - Search for vulnerability report on CVE-2023-6553 |
| Breach Intelligence | - Find a breach alert for victim TTEC - What is the source of the information for breach of TTEC by actor netsher? |
| Adversary Intelligence | - Find information regarding activity group with handle netnsher. Use Intel 471 plugin |

## Provide feedback

To provide feedback, contact [Intel 471 Threat Intelligence](https://intel471.com/).