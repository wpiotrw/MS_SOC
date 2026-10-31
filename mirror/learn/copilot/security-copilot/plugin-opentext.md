---
layout: Conceptual
title: OpenText Core Threat Detection and Response and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-opentext
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the OpenText(TM) Core Threat Detection and Response plugin with Microsoft Security Copilot.
ms.date: 2026-02-23T00:00:00.0000000Z
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
document_id: 51579ffb-d883-87f1-2933-6eb25464841f
document_version_independent_id: 51579ffb-d883-87f1-2933-6eb25464841f
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-opentext.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-opentext
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-opentext.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 34935f93-5ed4-ce76-4820-2355d37b9c7e
---

# OpenText Core Threat Detection and Response and Microsoft Security Copilot | Microsoft Learn

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

Your OpenText Core Threat Detection and Response subscription enables you to use this plugin to interact with Security Copilot, gain data insights produced by the product, and take appropriate actions on the risky entities and alerts occurring in your organization.

- Summarize risky activity across the organization.
- Retrieve top risky users, devices, and rare processes.
- Examine specific risky entity and rare process activities.

## Prerequisites

1. Sign in to your OpenText Core Threat Detection and Response account.
2. Make a note of the &lt;Product\_URL&gt; used to sign into your account. Save this URL for plugin configuration.
3. Generate an API token from your account settings. Save the token securely for plugin configuration.

## Know before you begin

1. Open your API token file and locate the **access token** field. Keep the file open. You need to copy and paste the access token value later in this procedure.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Select the **Sources** button.
4. From the **Manage sources** dialog box, scroll down to the **Non-Microsoft** source section.
5. Navigate to the **OpenText Core Threat Detection and Response** plugin and select **Set up**.
6. In the **OpenText Core Threat Detection and Response settings** dialog box do the following:

    1. In the **Instance URL** box, enter the &lt;Product\_URL&gt; for your tenant instance. The URL must be of the format `https://<domain name>/`.
    2. In the **Value** box, enter the access token value of the API token you downloaded. **Note:** Don't include the quotation marks when you copy the value of the API access token.
    3. Select **Save**. The Non-Microsoft plugins area displays the OpenText Core Threat Detection and Response plugin.
7. Configuration is complete. You can begin to submit prompts.

## Sample OpenText Core Threat Detection and Response prompts

The skills listed describe the full interaction of this version of Security Copilot plugin with OpenText Core Threat Detection and Response.

Use natural language prompts. Examples are provided below.

### Skills & Prompts

- **Top Risky Users**

    *Prompt:* What are the top five riskiest users on &lt;date&gt;?
- **Top Risky Devices**

    *Prompt:* What are the top five riskiest devices on &lt;date&gt;?
- **Top Rare Processes**

    *Prompt:* What are the top five riskiest rare processes executed on &lt;date&gt;? Include alert IDs.
- **Summarize Risky Activity**

    *Prompt:* Summarize the risky activity across the organization on &lt;date&gt;.
- **Entity Investigation**

    *Prompt:* Summarize the risky behaviors of &lt;username|hostname&gt; on &lt;date&gt;.
- **Alert Details**

    *Prompt:* What are the details of the alert with ID &lt;alert\_id&gt;?
- **Insider Threat Summary**

    *Prompt:* Can you summarize the insider threats to the above investigation and provide a conclusion and recommendation?

## Troubleshoot the OpenText Core Threat Detection and Response plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Prompts are failing

If the prompts fail to invoke, ensure that you are using a supported prompt. You can refer to the promptbook shared with you to understand the valid prompts. If you're using the correct prompts and yet the prompts fail to invoke, then the plugin service might not be running. Wait for some time for the service to restart, and then try again. If you still face issues, contact [OpenText Support](https://support.cyberreshelp.com/).

## Provide feedback

To provide feedback, contact https://www.opentext.com/products/core-threat-detection-and-response.