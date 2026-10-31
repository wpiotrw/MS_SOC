---
layout: Conceptual
title: Aviatrix and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-aviatrix
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Aviatrix plugin with Microsoft Security Copilot.
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
document_id: 57ce9b3f-8dd4-ce3d-fdb4-c0ffc83c3969
document_version_independent_id: 57ce9b3f-8dd4-ce3d-fdb4-c0ffc83c3969
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-aviatrix.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-aviatrix
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-aviatrix.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c671beaa-a830-4c9f-aceb-97379ee031ca
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8921374c-4dbe-4ed0-b011-a39e18bfbd98
platformId: f9913aaa-86ad-02b5-0b12-4169dfe5c1d5
---

# Aviatrix and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Aviatrix and Microsoft Security Copilot have partnered to bring together an AI enabled plugin to allow customers to leverage Microsoft Defender Threat Intelligence with Aviatrix to gain insight into new threats and mitigate them through firewall policy enforcement. Integration with Aviatrix across Microsoft Security Copilot, Microsoft Defender Threat Intelligence, and Microsoft Sentinel are outlined and enabled through Microsoft LogicApps in this document.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Next to **Aviatrix**, select **Set up**.
4. Enter your Aviatrix controller username and password.
5. Save your changes.

## Sample Aviatrix prompts

After the Aviatrix plugin is configured, you can type "Aviatrix" in your Security Copilot prompt bar, followed by an action. The following list provides example prompts to try:

- `Aviatrix show me my firewall policies.`
- `Aviatrix show me log data for x.x.x.x.`
- `Aviatrix show me all blocked ports.`
- `Aviatrix show me all allowed rules.`

Aviatrix allows you to gain insight by allowing users to easily query our detailed resource, firewall, and log data. Be creative with your prompts using natural language.

## Troubleshoot the Aviatrix plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Aviatrix](https://aviatrix.com/).