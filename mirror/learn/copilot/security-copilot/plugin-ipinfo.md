---
layout: Conceptual
title: IPinfo and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-ipinfo
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the IPinfo plugin with Microsoft Security Copilot.
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
- sfi-image-nochange
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 20734c88-3e71-621c-5819-ba91bb6a308d
document_version_independent_id: 20734c88-3e71-621c-5819-ba91bb6a308d
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-ipinfo.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-ipinfo
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-ipinfo.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 2834c4a7-0504-1fba-69cf-ee401ca34054
---

# IPinfo and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

[IPinfo](https://ipinfo.io/) is an internet data company specializing in [IP geolocation](https://ipinfo.io/products/ip-geolocation-api), [IP to Privacy Detection (VPN, Tor, Proxy, etc.)](https://ipinfo.io/products/proxy-vpn-detection-api), [ASN data](https://ipinfo.io/products/asn-api), [company data](https://ipinfo.io/products/ip-company-api), [carrier metadatadata](https://ipinfo.io/products/ip-carrier-api), [WHOIS data](https://ipinfo.io/products/whois-api), and other internet data services. IPinfo’s internet data can help organizations conduct [cybersecurity research](https://ipinfo.io/use-cases/cybersecurity), [threat intelligence and network administration](https://ipinfo.io/use-cases/ip-data-for-fraud-prevention), among many other things.

With IPinfo’s broad internet data resources, the IPinfo plugin for Microsoft Security Copilot allows users to get diverse metadata information on internet-connected devices, create robust threat intel models, and run effective security control measurements.

IPinfo offers access to various internet data based on different service tiers. The IPinfo plugin will provide internet metadata based on the service tier of your IPinfo access token. However, our free IP geolocation data is accessible to users through a free account that you can start today. The free tier lets users have 50,000 IP to Geolocation/ASN lookups monthly. Through Copilot, you can use the “IPinfo” plugin to get more advanced data services.

Explore the plugin features from this video, [Microsoft Security Copilot Demo](https://www.youtube.com/watch?v=zVU0LxYgluk).

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot works with an API key. You need to take the following steps before using the plugin.

1. Sign up for IPinfo and get your access token. If you do not have an IPinfo account yet, follow these steps:

    1. Go to the [IPinfo website](https://ipinfo.io/signup) and create your free account. To access IPinfo's premium data, see the API offerings on the [pricing page](https://ipinfo.io/pricing).
    2. After signing up, go to the account dashboard and scroll down to the token section.
    3. From there, copy your IPinfo access token.

    ![Image of IPinfo dashboard](media/ipinfo-plugin-access-token.png)
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
4. Next to **IPinfo**, select **Set up**.
5. In the **Value** field, paste your API Key, and then select **Save**.

## Sample IPinfo prompts

After the IPinfo plugin is configured, you can type "IPinfo" in your Security Copilot prompt bar, followed by an action. The following table lists example prompts to try.

| Capability | Description | Example prompts |
| --- | --- | --- |
| getInformationByIp | Returns information about the provided IP. Supports both IPv4 and IPv6 addresses. Returns all the IP metadata available on the IP address from IPinfo. The free tier provides IP location information. For ASN, company, privacy detection, and other IP metadata, you have to subscribe to a paid tier. | `Look up the IP address `8.8.8.8`using IPinfo.  Give me the IP insights on the IP address`8.8.8.8`using IPinfo.  Give me information on the IP`8.8.8.8`using IPinfo.` |
| getLocationByIp | Returns a location for the selected IP. | `Give me all available location insights for the IP address '8.8.8.8' utilizing IPinfo.` |
| getPrivacyInformationByIp | Returns privacy information about the selected IP, such as VPN, proxy, Tor, relay and hosting service/data center/bot. | `Is the IP address `171.239.211.111` a VPN or an anonymous IP address according to IPinfo?` |
| getCompany | Returns information of the organization that is operating an IP address such as name, organization type and their official domain. | `Using IPinfo, tell me about the company that operates the IP address 60.29.162.215.` |
| getAsn | Returns information about an ASN, such as the assigned prefixes, related domain, and more. | `Using IPinfo, provide me with insights into ASN 52210. List out the ranges they operate.` |
| getRanges | Our IP address ranges API returns a list of all of the IP addresses ranges assigned to or operated by a company, identified by the provided domain name. | `What are the IP ranges operated by vercel.com according to IPinfo?` |
| getDomains | Our Hosted Domains, or Reverse IP API returns a list of all of the domains hosted on the provided IP address. | `What domains are hosted on the IP address `208.80.154.224` according to IPinfo?` |
| getAbuse | IP to abuse contact information such as email address, postal/ZIP code, city, state, country/region, name, network, and phone number. | `Please provide me with the abuse contact for the IP address `2a15:1e89:8000::` using IPinfo.` |

## Troubleshoot the IPinfo plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact [IPinfo](https://community.ipinfo.io/).