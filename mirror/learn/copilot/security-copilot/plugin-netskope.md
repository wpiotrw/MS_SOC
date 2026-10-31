---
layout: Conceptual
title: Netskope and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-netskope
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Netskope plugin with Microsoft Security Copilot.
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
document_id: 2d8867e7-bb57-198c-99b1-30d8d61ab522
document_version_independent_id: 2d8867e7-bb57-198c-99b1-30d8d61ab522
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-netskope.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-netskope
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-netskope.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 8942d016-5a1e-67aa-55f7-d9664b185b8c
---

# Netskope and Microsoft Security Copilot | Microsoft Learn

Netskope One is a cloud-native platform that offers converged security and networking services to enable your Secure Access Services Edge (SASE) and Zero Trust transformation. In addition to using the built-in Netskope plugin with Microsoft Security Copilot, you can incorporate other Netskope custom plugins. This article describes how to set up and use the built-in plugin for Security Copilot.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires an API token. You'll need to take the following steps before using the plugin.

1. Get your Netskope API token. If you don't have one, follow the steps in [Netskope's REST API v2 Overview](https://docs.netskope.com/en/netskope-help/admin-console/rest-api/rest-api-v2-overview-312207/).
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **Netskope Reporting for Threat and Data Protection**, select **Set up**.
5. In the **Value** field, paste Netskope API token.
6. Select **Save**.

## Sample Netskope Reporting prompts

After the Netskope Reporting plugin is set up, you can use the following six capabilities with Security Copilot:

- `Get_audit_events`
- `Get_data_alert`
- `Get_data_application`
- `Get_data_infrastructure`
- `Get_data_network`
- `Get_data_page`

The following table provides examples of prompts to try:

| Capability | Example prompt |
| --- | --- |
| Retrieve a list of application events for a specific time frame and domain | `show me Netskope DLP Alerts from 1724996122 and 1724997122` |
| Retrieve a list of security assessment alerts for a specific app | `show me Netskope application events from 1724996122 and 1724997122 for user example@hotmail.com` |
| Retrieve a list of page events for a specific user | `show me Netskope page events for the last 15 minutes from user <IP>` |
| Retrieve a list of page events for a specific user, domain, and traffic type | `show me Netskope page events that occurred in the last 15 minutes from user <IP address> to domain <domain> that is user generated with the traffic type being web` |
| Retrieve a list of alerts for the last 90 minutes that aren't yet acknowledged | `show me Netskope alerts for the last 90 minutes and only show alerts that are not hacked` |

## Troubleshoot the Netskope plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred* | Make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

### Timestamp Support

To filter data to a specific time frame, this plugin requires timestamps in Epoch/UNIX format. To retrieve the relevant time frame in the correct format, use a service such as https://epochconverter.com or https://unixtime.org.

## Provide feedback

To provide feedback, contact [Netskope](https://www.netskope.com/).