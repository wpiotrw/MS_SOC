---
layout: Conceptual
title: IPGeolocation and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-ipgeolocation
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the IPGeolocation plugin with Microsoft Security Copilot.
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
document_id: da5c4d90-bbe1-bbbc-6718-c2a0d0b6c559
document_version_independent_id: da5c4d90-bbe1-bbbc-6718-c2a0d0b6c559
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-ipgeolocation.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-ipgeolocation
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-ipgeolocation.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
platformId: 88ba1272-88dc-99b1-7f19-30c1da3e7fed
---

# IPGeolocation and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

IPGeolocation is a powerful API service providing comprehensive geolocation data, time zone information, currency details, security insights (such as VPN, proxy, and bot detection), and hostname resolution based on IP addresses. Designed for developers, security analysts, and digital service providers, our platform helps enhance security, optimize user experiences, and improve decision-making processes with real-time geolocation intelligence. IPGeolocation seamlessly integrates with your existing systems to improve workflow efficiency.

By integrating the IPGeolocation API into Security Copilot, users can enhance their system's ability to detect threats, tailor content delivery, and make informed decisions with accurate location and security data based on an IP address.

Note

This article contains information about non-Microsoft plugins. This article is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for non-Microsoft plugins. Contact the vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You need to take the following steps before using the plugin.

1. Get your IPGeolocation API key. If you don't have one yet, follow these steps:

    1. First, [Sign Up](https://app.ipgeolocation.io/signup) on IPGeolocation using any preferred method (GitHub, Google, or Email). If you signed up with email, follow the instructions to verify your account and sign in.
    2. From your [dashboard](https://app.ipgeolocation.io/dashboard), copy your API key.

    ![Image of IPGeolocation dashboard](media/ipgeolocation-dashboard-api-key.png)
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **IPGeolocation**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample IPGeolocation prompts

Note

Security, domain lookup (in place of IP Address), and hostname lookup features are available only with paid subscriptions. All other information can be accessed with a free or developer plan, which allows up to 1,000 API requests per day. Paid plans don't have any request limits. For more details, visit [IPGeolocation Pricing](https://ipgeolocation.io/pricing.html).

After the IPGeolocation plugin is configured, you can use the following capabilities with Security Copilot. The following table lists example prompts to try.

| Capability | Example prompts |
| --- | --- |
| IP Address Details (Geolocation, Security, Time Zone, and Hostname Info) | `Give me complete details including threat score and security data, geolocation, time zone info, and hostname for IP address 49.12.212.42.` |
| Time Zone and Currency Information | `Provide the time zone and currency associated with the IP address 49.12.212.42.` |
| ASN Lookup Information | `What ASN is associated with the IP address 49.12.212.42?` |
| Location Insights for a Specific IP Address | `Give me all available location insights for the IP address '8.8.8.8' utilizing IPGeolocation.` |
| Security Insights for an IP Address | `Is the IP address 146.70.250.27 a VPN or an attacker IP address according to IPGeolocation?` |
| Lookup Domain | `Provide all available insights, including location, security, time zone, and other relevant data, for the domain example.com using ipgeolocation.` |

## Troubleshoot the IPGeolocation plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred* | Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [IPGeolocation](https://ipgeolocation.io/).