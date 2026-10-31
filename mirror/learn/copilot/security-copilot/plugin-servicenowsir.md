---
layout: Conceptual
title: ServiceNow SIR and  Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-servicenowsir
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the ServiceNow SIR plugin with Microsoft Security Copilot.
ms.date: 2026-02-19T00:00:00.0000000Z
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
document_id: 2837990f-e273-f768-b780-e996c5f9e8a5
document_version_independent_id: 2837990f-e273-f768-b780-e996c5f9e8a5
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-servicenowsir.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-servicenowsir
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-servicenowsir.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 5c8cd232-3889-f563-c59d-a7d942198df8
---

# ServiceNow SIR and  Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

In today’s rapidly evolving threat landscape, organizations need cutting-edge security solutions that combine AI-driven intelligence with automated response capabilities. The integration between ServiceNow Security Incident Response (SIR) and Microsoft Security Copilot redefines security operations, enabling dynamic decision-making, real-time insights, and autonomous response capabilities. By implementing this game changer of a solution, organizations can strengthen their security posture, reduce cyber risks, and optimize security operations for the future.

ServiceNow Security Incident Response and Microsoft Security Copilot in action!

To seamlessly integrate ServiceNow Security Incident Response with Microsoft Security Copilot, enabling AI-driven, autonomous security operations that enhance threat detection, accelerate incident response, and improve overall cybersecurity resilience through intelligent AI to AI communication.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

**Scope**

1. Enrich incidents in SIR with threat intelligence and user/device information to get the contextual awareness for incident remediation
2. Share the summary of the security incident from SIR along with corelated insights on user and device information from CMDB to Microsoft

**Value Proposition**

1. Accelerated Investigation and Response: Analyze threats with AI-assisted insights and swiftly transition to remediation using contextual intelligence
2. Improved Operational Efficiency: Reduce the Mean Time to Resolve (MTTR) with natural language enable AI assistance
3. Stronger Security Posture: Use AI-enhanced threat intelligence to proactively identify and mitigate risks before they escalate.

**Integration Approach**

1. AI to Ai communication between SIR and Microsoft Security Copilot.
2. Customers would be able to ask quick queries on ServiceNow Now Assist Panel on the threat intel, user and device information from Microsoft.
3. Similarly, customers would be able to ask for summary of security incidents along with corelated insights of users and device from CMDB on Microsoft security copilot

## Know before you begin

Register the application in ServiceNow

1. Navigate to **System oAuth &gt; Application Registry &gt; New &gt; Create an OAuth API endpoint for external clients**.
2. Set the Name: Microsoft Security Copilot ServiceNowSIR.
3. Set Redirect URL: https://securitycopilot.microsoft.com/auth/v1/callback.
4. **Submit**.

![Screenshot OAuth app registry.](media/oauth_app_registry.png)

Set up the ServiceNowSIR plugin in Microsoft Security Copilot

1. Set the ServiceNow Instance URL.
2. Set the **ClientId** and **ClientSecret** generated in the previous section.
3. Set the **AuthorizationEndpoint** and the **TokenEndpoint**.

![Screenshot ServiceNowSir setup.](media/setup-servicenowsir.png)

## Sample ServiceNowSIR prompts

After the ServiceNowSIR is configured, you can use it by taking one of the following steps:

| Skill | Inputs | Example Prompts |
| --- | --- | --- |
| Get security incident details | - security incident number (required) | - Load ServiceNow security incident SIR0001624<br>- Get ServiceNow the description and short description of security incident SIR0001624 |
| Get security incident summarization | - security incident number (required) | - Get ServiceNow security incident SIR0001624 summary |
| Get correlation insights for a security incident | - security incident number (required)<br>- variable (required)<br>- name (required)<br>- lookback\_period (optional) | - Get ServiceNow security incident SIR0010081 correlation insights with variable cmdb\_ci, name DatabaseServer2 and lookback\_period=365<br>- Get ServiceNow security incident SIR0010081 correlation insights with variable affected\_user, name Alice Brown and lookback\_period=365<br>- Get ServiceNow security incident SIR0010081 correlation insights with variable threat\_intelligence and name `https://keyloggerapp.xxx.com` and lookback\_period=365 |
| Get user by name | - name (required) | - Get ServiceNow user Alice Brown<br>- Get the department and location of ServiceNow user Alice Brown |
| Get CMDB CI by name | - name (required) | - Get ServiceNow configuration item DatabaseServer2<br>- Get ServiceNow the business unit of configuration item DatabaseServer2<br>- Get ServiceNow the location and Manufacturer of configuration item DatabaseServer2 |

## Troubleshoot the ServiceNowSIR plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. You can either use the product name ServiceNowSIR in your prompts, or type the name of a specific capability, like &lt;&gt; instead.

## Provide feedback

To provide feedback, contact ServiceNowSIR product management.