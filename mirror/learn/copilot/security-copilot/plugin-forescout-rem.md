---
layout: Conceptual
title: Forescout Risk and Exposure Management and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-forescout-rem
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Forescout Risk and Exposure Management plugin with Microsoft Security Copilot.
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
document_id: 9218ad06-4995-525f-b790-b6c5086597a6
document_version_independent_id: 9218ad06-4995-525f-b790-b6c5086597a6
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-forescout-rem.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-forescout-rem
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-forescout-rem.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: e8f1606a-d059-d9bc-a483-ef91948495de
---

# Forescout Risk and Exposure Management and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Forescout Risk and Exposure Management (REM) platform provides data across all devices in a customer environment as discovered by the Forescout platform. REM gives a single view of device risk and vulnerabilities, including a timeline to track events and changes to a device risk value. Combining the contextual data from the Forescout REM platform with Microsoft Security Copilot allows security teams to quickly assess the risk posed across their environments and prioritise work by getting clear information on their exposure to different vulnerabilities or configurations which exist.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You need to take the following steps before using the plugin.

1. Get your Forescout Risk and Exposure Management API key. If you don't have one yet, follow these steps:

    1. Login to Forescout Cloud.
    2. In the Forescout Cloud Console, select **Integrations** under the **Administration** menu.
    3. Click the **Generate API Key** button next to the category of your application - IoT/OT. The Generate API Key configuration screen appears.
    4. Provide a meaningful name for the API key such as **Microsoft Security Copilot**.
    5. Select a time for the API key to expire or select **Never Expires**. If the key is set to expire, select users to receive Email notifications about the API key generation and expiry date.
    6. Click the **Generate** button and copy the API key that appears on screen. This API key is unique and non-retrievable once the window is closed. Save this key in a secure location for use in Microsoft Security Copilot.
    7. Copy the API Endpoint URL that appears below the key.
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
4. Next to **Forescout Risk and Exposure Management**, select **Set up**.
5. In the Forescout Risk and Exposure Management plugin settings pane, under **Forescout Cloud Data Exchange API Endpoint URL** enter the API endpoint URL.
6. In the **Value** field, paste your API Key, and then select **Save**.

## Sample Forescout Risk and Exposure Management prompts

After the Forescout Risk and Exposure Management plugin is configured, you can use the following capabilities with Security Copilot.

The following table lists example prompts to try.

| Capability | Example prompts |
| --- | --- |
| Get REM assets | - `Using Forescout, tell me about my top 5 riskiest devices.` - `Tell me about the risks for X.` - `Show me all devices with CVE-1234-5678.` |

## Troubleshoot the Forescout Risk and Exposure Management plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [Forescout Risk and Exposure Management](https://www.forescout.com/solutions/risk-and-exposure-management/).