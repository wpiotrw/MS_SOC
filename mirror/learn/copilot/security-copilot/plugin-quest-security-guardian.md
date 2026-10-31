---
layout: Conceptual
title: Quest Security Guardian and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-quest-security-guardian
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Quest Security Guardian plugin with Microsoft Security Copilot.
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
document_id: e5c22d70-c326-85b3-49f8-c68209796987
document_version_independent_id: e5c22d70-c326-85b3-49f8-c68209796987
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-quest-security-guardian.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-quest-security-guardian
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-quest-security-guardian.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/37da4cc9-0cfc-42a9-ba5e-805706b01ef8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3661fb96-d414-4a4e-b7ad-9370637790dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
platformId: 245d058c-2adc-d02c-f88c-0174c4e73b4e
---

# Quest Security Guardian and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Quest Security Guardian is an Active Directory security tool designed to reduce your attack surface. From a simplified unified workspace, Security Guardian reduces alert fatigue by prioritizing your most exploitable vulnerabilities and Active Directory configurations that demand attention. The solution spotlights what happened if you’re exposed and how to fix the problem.

The Security Guardian Plugin exposes all of Security Guardian's threat indicators, findings, and alerts to Microsoft Security Copilot. This allows all the data to be combined with other security findings (increasing signal strength) and ultimately acted on by Security Analysts to identify and fix vulnerabilities faster.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Next to **Quest Security Guardian**, select the toggle to enable it.

    Provide the following information:

    - Tenant Id: The ID of the Microsoft Entra ID Organization that the Microsoft Sentinel workspace is in.
    - Subscription Id: The ID of the Azure Subscription that the Microsoft Sentinel workspace is in.
    - Resource Group Name: The name of the Resource Group that the Microsoft Sentinel workspace is in.
    - Workspace Name: The name of the Microsoft Sentinel workspace.
4. Save your changes.

## Sample Quest Security Guardian prompts

After the Quest Security Guardian plugin is configured, you can use it to:

- Access the plugin capabilities by selecting the **Plugin button** from the prompt bar and selecting **Quest Security Guardian**.
- Prompt Security Copilot using any of the following example prompts.

Example prompts:

- `Generate a report using Security Guardian and summarize the top 5 trends the indicators show and then summarize how these impact our company and suggest a couple of ways to resolve or mitigate them.`

## Troubleshoot the Quest Security Guardian plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Quest Security Guardian](https://quest.com).