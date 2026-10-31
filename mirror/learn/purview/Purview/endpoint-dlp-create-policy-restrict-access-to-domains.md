---
layout: Conceptual
title: Help prevent risky user activity by monitoring or restricting access to sensitive service domains | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: DLP policy creation scenario to prevent risky user activity by monitoring or restricting access to sensitive service domains.
ai-usage: ai-assisted
locale: en-us
document_id: 6ee6f0f4-ad2c-6bf8-5df2-8e2a237f1769
document_version_independent_id: 6ee6f0f4-ad2c-6bf8-5df2-8e2a237f1769
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-create-policy-restrict-access-to-domains.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-create-policy-restrict-access-to-domains
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-create-policy-restrict-access-to-domains.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 43da2ff2-5ffc-3445-f221-50f6058ba66f
---

# Help prevent risky user activity by monitoring or restricting access to sensitive service domains | Microsoft Learn

## Overview

This scenario demonstrates how to monitor and control user interactions with sensitive websites using Microsoft Purview DLP. By defining **sensitive service domains**, organizations can audit or restrict actions such as copying, printing, or saving web content when users access these sites.

Policy enforcement occurs in a supported, DLP-aware browser environment, ensuring consistent control and user guidance. This enables organizations to protect sensitive data accessed through web applications while maintaining flexibility to tailor controls based on business needs.

Note

The following web browsers are supported:

- Microsoft Edge (Win/macOS)
- Chrome (Win/macOS)- Microsoft Purview extension for Chrome Windows only
- Firefox (Win/macOS)- Microsoft Purview extension for Firefox Windows only
- Safari (macOS only)

## Prerequisites and assumptions

This article uses the process you learned in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](sensitivity-labels)
- [Get started with sensitivity labels](get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

The policy configuration in this article uses alerts. To learn more, see [Get started with the data loss prevention alerts](dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to monitor and control how users interact with sensitive websites to reduce the risk of data exposure through browser-based activities. Specifically, we want to audit or restrict actions such as copying data, printing content, or saving web pages locally when users access designated sensitive service domains.*

*To achieve this, we will define a set of **sensitive service domains** and configure a policy that detects when users access these sites through supported browsers. When a match occurs, we will apply activity-specific controls—such as auditing or blocking printing, copying, or file-saving actions—while ensuring users are redirected to supported browsers (such as Microsoft Edge) where these controls can be enforced consistently.*

This approach enables granular control of in-browser data handling for sensitive sites, helping protect organizational data while maintaining flexibility in how policies are applied and tuned over time.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to monitor and control user interactions with designated sensitive websites…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices (or scoped test users) |
| “We want to define which websites are considered sensitive for monitoring or restriction…” | - Endpoint settings: Configure **Service domains** and **Sensitive service domain groups**- Domains defined using URL/IP/IP range with wildcard support |
| “We want to detect when users access these sensitive sites in supported browsers…” | - Condition: **User accessed a sensitive site from Edge**- Browser coverage: Supported browsers with Microsoft Purview extensions where applicable |
| “We want to ensure policy enforcement occurs in a DLP-aware browser…” | - Browser handling: Redirect unsupported browsers (e.g., Chrome/Firefox) to **Microsoft Edge** when accessing sensitive domains |
| “We want to audit or restrict specific user activities performed on sensitive websites…” | - Actions: **Audit or restrict activities when users access sensitive sites**- Activity controls include: copy, print, save as local files |
| “We want fine-grained control over which activities are monitored or blocked…” | - Action configuration: Select individual user activities (copy, print, save)- Choose audit, block, or block with override depending on requirement |
| “We want to flexibly apply controls across different sets of sensitive domains…” | - Rule configuration: Assign one or more **Sensitive service domain groups**- Reusable group design for scalability |
| “We want to finalize and deploy the policy for immediate use…” | - Policy mode: Submit and enable policy- Deployment: Active policy with configured monitoring/restriction behavior |

## Steps to create the sensitive service domains policy

Perform the following steps to configure sensitive service domains and create the DLP policy.

### Configure Sensitive service domains

Use the following steps to define sensitive service domains and create a DLP policy that monitors or restricts user activity on those domains.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear icon in the upper left hand corner) &gt; **Data Loss Prevention** &gt; **Endpoint settings** &gt; **Browser and domain restrictions to sensitive data** &gt; **Service domains**.
2. Set **Service domains** to **Block**.
3. To control whether sensitive files can be uploaded to specific domains, select **Add cloud service domain**.
4. Enter the domain that you want to audit or block and choose the **+** button. Repeat for any additional domains. Choose **Save**.
5. Under **Sensitive service domain groups**, choose **Create sensitive service domain group**.
6. Give the group a name, select the **Match type** you want (you can select from **URL**, **IP address**, **IP address range**), and enter the URL, IP address, or IP address range to be audited or blocked. When matching a URL, you can add multiple websites to a group and use wildcards to cover subdomains. For example, `www.contoso.com` for just the top level website or \*.contoso.com for corp.contoso.com, hr.contoso.com, fin.contoso.com.
7. Select **Save**.
8. In the left navigation pane, select **Data loss prevention** &gt; **Policies**.
9. On the policy template page, select **Data stored in connected sources**.
10. Create and scope a policy that is applied only to the **Devices** location. For detailed steps on scoping a policy to the Devices location, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy#define-policy-scope). Be sure to scope the **Admin units** to **Full directory**.
11. Create a rule that uses the condition **the user accessed a sensitive site from Edge**, and the action **Audit or restrict activities when users access sensitive sites in Microsoft Edge browser on Windows devices**.
12. In the action, under **Sensitive Site Restrictions**, select **Add or remove Sensitive site groups**.
13. Create and/or select the **Sensitive site groups** you want. Any website under the group(s) you select here will be redirected to Microsoft Edge when opened in Chrome or Firefox (so long as the Microsoft Purview extension is installed).
14. Select **Add**.
15. Select the user activities you want to monitor or restrict and the actions you want Microsoft Purview to take in response to those activities.
16. Finish configuring the rule and policy and choose **Submit** and then **Done**.