---
layout: Conceptual
title: Security Copilot in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: tracyp
author: MSFTTracyP
manager: laurawi
ms.update-cycle: 180-days
ms.date: 2026-02-24T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.collection:
- highpri
- purview-compliance
- msec-ai-copilot
search.appverid:
- MET150
description: Learn how Microsoft Security Copilot is used in Microsoft Purview
locale: en-us
document_id: 7d495682-ee7d-9e0b-2890-2a65d4833230
document_version_independent_id: 7d495682-ee7d-9e0b-2890-2a65d4833230
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 4f581963-bf14-4dd7-5101-15ffa0f0d87c
---

# Security Copilot in Microsoft Purview | Microsoft Learn

Microsoft Security Copilot is a cloud-based AI platform that can assist security and compliance professionals in protecting their organization's data. Security and compliance professionals can use Security Copilot to identify, summarize, triage, and remediate issues within the following Microsoft Purview solutions:

- [Data Security Posture Agent (DSPM)](data-security-posture-management-copilot)
- [Microsoft Purview Data Loss Prevention (DLP)](dlp-alerts-dashboard-get-started)
- [Microsoft Purview Insider Risk Management](insider-risk-management-activities#use-copilot-to-summarize-an-alert)
- [Microsoft Purview Communication Compliance](communication-compliance-copilot)
- [Microsoft Purview eDiscovery](edisc-review-set-view#summarize-an-item-by-using-microsoft-security-copilot)

For more information about what Security Copilot can do and the different scenarios it supports, read [What is Microsoft Security Copilot?](/en-us/security-copilot/microsoft-security-copilot).

## Know before you begin

If you're new to Security Copilot, you should familiarize yourself with it by reading these articles:

- [What is Microsoft Security Copilot?](/en-us/security-copilot/microsoft-security-copilot)
- [Microsoft Security Copilot experiences](/en-us/security-copilot/experiences-security-copilot)
- [Get started with Microsoft Security Copilot](/en-us/security-copilot/get-started-security-copilot)
- [Understand authentication in Microsoft Security Copilot](/en-us/security-copilot/authentication)
- [Prompting in Microsoft Security Copilot](/en-us/security-copilot/prompting-security-copilot)
- [Configure Owner settings](/en-us/copilot/security/owner-settings)
- [Learn about Security Copilot in Microsoft 365 E5](/en-us/copilot/security/security-copilot-inclusion)

## Security Copilot integration in Microsoft Purview

When you sign up for Security Copilot in the same tenant as Microsoft Purview, you can use both the Security Copilot embedded and standalone experiences. Security Copilot capabilities, like summarizing DLP or insider risk management alerts, are embedded into Microsoft Purview features.

**Copilot in Microsoft Purview embedded experiences** is a set of capabilities that are embedded in Microsoft Purview features. For more information, see [standalone and embedded experiences](/en-us/security-copilot/experiences-security-copilot#standalone-and-embedded-experiences).

**Copilot in Microsoft Purview standalone experience** is a chat-like experience that you can use to ask questions and get answers about your data. For more information, see [standalone and embedded experiences](/en-us/security-copilot/experiences-security-copilot#standalone-and-embedded-experiences).

### Key features in the embedded experience

You can open Security Copilot in Microsoft Purview by selecting the **Copilot** icon in the top navigation bar. It's available across all Microsoft Purview solutions.

![Screenshot that shows the Security Copilot launch control in the top navigation bar.](media/copilot-launch-top-navigation.png)

The embedded experience in Purview can help you:

- *Get AI-generated summaries from Microsoft Purview product documentation*.
- *Use suggested or customized prompts in DSPM*. Learn more about the data security posture in your organization. For more information, see [Use Microsoft Security Copilot with Data Security Posture Management](data-security-posture-management-copilot).
- *Summarize alerts in DLP*. For more information on this and how to access Security Copilot in DLP, see [Investigate a DLP alert](dlp-alerts-dashboard-get-started#investigate-a-dlp-alert).
- *Get insights into policies*. Security copilot can help you understand what your policies are doing in your organization, and where they're active. For more information, see [Get Insights with Microsoft Security Copilot](dlp-test-dlp-policies#get-insights-with-microsoft-security-copilot).
- *Summarize alerts in insider risk management*. For more information on this and how to access Security Copilot in Insider Risk Management, see [Investigate insider risk management activities](insider-risk-management-activities#use-copilot-to-summarize-an-alert).
- *Summarize policy matches based on trainable classifiers for communication compliance*. Communication compliance also provides an interactive prompt experience to dig deeper into the summary. For more information on this and the steps to access Copilot in Communication Compliance, see [Investigate and remediate communication compliance alerts](communication-compliance-investigate-remediate#summarize-a-message-by-using-copilot-in-microsoft-purview).
- *Get contextual summary for eDiscovery cases*. For more information, see [Group and view documents in a review set in eDiscovery (Premium)](ediscovery-view-documents-in-review-set#copilot-activity-view).
- *Gain insights in activity explorer data and generate filters from natural language prompts (preview)*. For more information, see [Microsoft Security Copilot in activity explorer (preview)](data-classification-activity-explorer#microsoft-security-copilot-in-activity-explorer-preview).

### Key features in the standalone experience

The Security Copilot in Microsoft Purview standalone experience has many built in capabilities. You can use these capabilities to get insights from your Purview data and make connections between datapoints. This information can help you understand your information security and compliance posture and triage alerts.

- *DLP and Insider Risk Management data and user risk promptbook.* Security Copilot in Microsoft Purview analyzes data from DLP and insider risk management and, by running multiple, sequential prompts [contained in a promptbook](/en-us/security-copilot/using-promptbooks#what-are-promptbooks), presents you with integrated results. For more information, see [Microsoft Copilot in Microsoft Purview prompts and promptbooks](copilot-in-purview-promptbooks).

#### System capabilities of Security Copilot

In the standalone experience, there are built-in capabilities (prompts) that are available once the Microsoft Purview plugin is enabled.

Security Copilot in Microsoft Purview brings three types of capabilities:

- Summarize Microsoft Purview alerts.
- Triage Microsoft Purview alerts.
- Drill down into your Microsoft Purview data.

## Enable the Microsoft Purview source in Microsoft Security Copilot

Important

Security Copilot in Purview must be enabled for both the standalone and embedded experiences to work.

Security Copilot in Purview is enabled by default. To enable or disable the Microsoft Purview source in Microsoft Security Copilot, follow these steps:

1. Ensure that you have [permissions](/en-us/security-copilot/authentication#access-copilot-for-security-platform).
2. Open https://securitycopilot.microsoft.com/.
3. Open **Sources** in the prompt bar.

    ![Screenshot that shows the plugins that are available, enabled, and disabled in Microsoft Security Copilot.](media/copilot-for-security-plugins.png)
4. On the **Manage plugins** page, set the **Purview** toggle to **On** to enable or **Off** to disable.

### Review the Microsoft Purview system capabilities

1. Select the capabilities control in the prompt bar.

    ![Screenshot that shows the system capabilities and promptbooks icon.](media/copilot-security-capabilities-promptbooks.png)
2. Select **See all system capabilities** to see all the system capabilities that are available for Microsoft Purview. Here are a few:

    - Get Data Risk Summary
    - Get User Risk Summary
    - Summarize Purview Alert
    - Triage Purview Alerts
    - Zoom into Purview Data and User Risk

### Sample prompts

For guidance on writing effective prompts, see [Prompting in Microsoft Security Copilot](/en-us/security-copilot/prompting-security-copilot). Here are some examples:

- *Show me the top five DLP alerts from the past 24 hours*.
- *Summarize the DLP alert with ID &lt;12345&gt;*.
- *What's the risk profile of the user that's associated with the DLP alert &lt;12345&gt;*.
- *Show me the Insider Risk Management alerts for &lt;user&gt;* .
- *What items did user &lt;user&gt; exfiltrate in the past 30 days*.

## Provide feedback

Your feedback is vital to guide the current and planned development of the product. The best way to provide this feedback is directly in the product. Select **How’s this response?** at the bottom of each completed prompt and choose any of the following options:

- **Looks right** - Select if the results are accurate, based on your assessment.
- **Needs improvement** - Select if any detail in the results is incorrect or incomplete, based on your assessment.
- **Inappropriate** - Select if the results contain questionable, ambiguous, or potentially harmful information.

For each feedback option, you can provide more information in the next dialog box that appears. Whenever possible, and especially when the result is **Needs improvement**, write a few words explaining what can be done to improve the outcome. If you entered prompts specific to Microsoft Purview and the results aren't related, then include that information.

## Privacy and data security in Microsoft Security Copilot

To understand how Microsoft Security Copilot in Purview handles your prompts and the data that's retrieved from the service (prompt output), see the [Privacy and data security in Microsoft Security Copilot](/en-us/security-copilot/privacy-data-security).