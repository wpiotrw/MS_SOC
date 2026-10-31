---
layout: Conceptual
title: Use promptbooks in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/using-promptbooks
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Get familiar with using prebuilt promptbooks in Microsoft Security Copilot to investigate incidents in Microsoft Sentinel and Microsoft Defender XDR or get suspicious script analysis, threat actor, and vulnerability assessment reports.
ms.date: 2026-06-01T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 8c4fddfc-0815-94be-4f47-d5bf1f478fcb
document_version_independent_id: 8c4fddfc-0815-94be-4f47-d5bf1f478fcb
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/using-promptbooks.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: using-promptbooks
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/using-promptbooks.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: a97ab293-ae60-8047-a856-7d624c2b22e7
---

# Use promptbooks in Microsoft Security Copilot | Microsoft Learn

Security Copilot comes with prebuilt promptbooks, a series of prompts that have been put together to accomplish specific security-related tasks. They can function in a similar way as security playbooks—ready-to-use workflows that can serve as templates to automate repetitive steps—for instance, regarding incident response or investigations. Each prebuilt promptbook requires a specific input (for example, a code snippet or a threat actor name).

## View the promptbook library

You can find the different promptbooks by going to the [promptbook library](prompting-security-copilot#using-the-promptbooks-library) or by selecting the Prompts icon ![Screenshot of sparkle icon.](media/sparkle-button.png) at the prompt bar. You can then search for a promptbook or select **See all promptbooks** to view all.

## Use different promptbooks

Available promptbooks include:

- Check impact of an external threat article
- Incident investigation
- Microsoft User analysis
- Suspicious script analysis
- Threat actor profile
- Threat Intelligence 360 report based on MDTI article
- Vulnerability impact assessment

Watch the following video to learn more about promptbooks:

### Check impact of an external threat article

Using this promptbook, you can analyze any external threat intelligence articles to extract indicators from it and gather any relevant Microsoft Defender Threat Intelligence article.

To run the **Check impact of an external threat article** promptbook:

1. Make sure that you have turned on the **Microsoft Threat Intelligence** plugin by following the steps in [Enable the Security Copilot integration in Defender TI](/en-us/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence#turn-on-the-security-copilot-integration-in-defender-ti).
2. In Security Copilot, select the Prompts button in the prompt bar and start to type a few letters of the promptbook named **Check impact of an external threat article** until the promptbook appears in the list.

    [![Screenshot of check impact of an external threat article promptbook.](media/promptbook-threat-article-tb.png)](media/promptbook-threat-article.png#lightbox)
3. Provide the URL of the external threat intelligence article you want to analyze and extract indicators from.
4. Next, select **Submit**.
5. Wait for Security Copilot to run the URL through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts, building on each response until it gets to the last prompt.
6. Read the responses by Security Copilot. You can use the generated KQL queries to aid in investigation.

### Incident investigation

You can run the incident investigation promptbook after supplying an incident number to either the Microsoft Sentinel or Microsoft Defender XDR plugin. Use the appropriate promptbook for the plugin you want to use. The incident investigation promptbooks contain several prompts to generate an executive report for a nontechnical audience that summarizes the investigation. Each prompt builds on the previous prompt.

To run the Microsoft Sentinel **Incident investigation** promptbook:

1. Select the Prompts button in the prompt bar and start to type "incident investigation" until the promptbooks appear in the list.
2. Select **Microsoft Sentinel incident investigation**. (To use the Microsoft Defender XDR plugin instead, select **Microsoft Defender XDR incident investigation**.)

    [![Screenshot of incident investigation promptbook.](media/promptbook-incident-tb.png)](media/promptbook-incident.png#lightbox)
3. Supply the incident number that you want to investigate in the input box that says *SENTINEL\_INCIDENT\_ID*.
4. Next, select **Submit**.
5. Wait for Security Copilot to run the incident number through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts, building on each response until it gets to the last prompt.
6. Read the responses by Security Copilot. The last prompt by Security Copilot generates an executive report summarizing the investigation based on the responses. Review and verify whether the responses are accurate and meet your needs.

### Microsoft User analysis

The Microsoft User analysis promptbook can be used by an IT Admin to analyze and get detailed insights about a user and associated devices across multiple Microsoft 365 products. This includes sign-in and authentication data from Microsoft Entra ID, device information from Intune, unusual activity details from Microsoft Purview, and a Microsoft Defender summary highlighting important detections.

To get a comprehensive response from this promptbook, you first need to activate or make sure that you have the following roles:

- Security Reader role for Microsoft Entra ID, Intune, and Defender at a minimum
- Insider Risk Management Investigator or Analyst role for Microsoft Purview

To run the **Microsoft User analysis** promptbook:

1. Go to the Promptbook library and look for the **Microsoft User Analysis** promptbook.
2. Select **Start new session**.

    [![Screenshot of Microsoft user analysis promptbook.](media/promptbook-user-tb.png)](media/promptbook-user.png#lightbox)
3. You need the following inputs:

    - the user principal name or UPN of the user
    - the time range you want Security Copilot to look up the information.
4. Next, select the **Submit** button in the upper right corner of the dialog box.
5. Wait for Security Copilot to run your inputs through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts and builds on each until it gets to the last prompt.
6. Read the response from Security Copilot. Using the response from the prompts, you can deduce faster whether the user being investigated has been performing suspicious activities so you can focus on your next steps in securing your system.

### Suspicious script analysis

The suspicious script analysis promptbook is useful when you're investigating a PowerShell or Windows command-line script. For example, if a PowerShell script was involved in a critical incident in your network, you can copy the body of the script and run the promptbook to find out more about it.

To run the **Suspicious script analysis** promptbook:

1.Select the Prompts button in the prompt bar and start to type "suspicious script analysis" until the promptbooks appear in the list.

1. Select **Suspicious script analysis**.
2. Paste the script string that you want analyzed in the input box saying *SNIPPET*.

    [![Screenshot shows suspicious script analysis in a promptbook.](media/promptbook-script-tb.png)](media/promptbook-script.png#lightbox)
3. Next, select **Submit**.
4. Wait for Security Copilot to run the script content through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts, building on each response until it gets to the last prompt.
5. Read the responses by Security Copilot. The last prompt by Security Copilot generates a full report of what the script does, any related threat activities, and recommended next steps based on the assessment about file intent. Review and verify whether the responses are accurate and meet your needs.

### Threat actor profile

The threat actor profile promptbook is a quick way to get an executive summary about a specific threat actor. The promptbook looks for any existing threat intelligence articles about the actor, including known tools, tactics, and procedures (TTPs) and indicators, including remediation suggestions. It then summarizes the findings into a report for less technical readers.

To run the **Threat actor profile** promptbook:

1. Select the Prompts button in the prompt bar and start to type "threat actor profile" until the promptbooks appear in the list.
2. Select **Threat actor profile**.
3. Type the name of the threat actor in the input box that says *Threat actor name*.

    [![Screenshot of threat actor promptbook.](media/promptbook-actor-tb.png)](media/promptbook-actor.png#lightbox)
4. Next, select **Submit**.
5. Wait forSecurity Copilot to run the threat actor name through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts and builds on each until it gets to the last prompt.
6. Read the response by Security Copilot. The last prompt by Security Copilot generates an easily readable report that includes pertinent information about the identified threat actor. Review and verify whether the responses are accurate and meet your needs.

### Threat Intelligence 360 report based on MDTI article

By using this promptbook, you can get a detailed report about whether the threats discussed in a given Microsoft Defender Threat Intelligence article are affecting the organization, including relevant indicators and hunting queries.

To run the **Microsoft Threat Intelligence** promptbook:

1. Make sure that you have turned on the **Microsoft Threat Intelligence** plugin by following the steps in [Enable the Security Copilot integration in Defender TI](/en-us/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence#turn-on-the-security-copilot-integration-in-defender-ti).
2. In Security Copilot, select the Prompts button in the prompt bar and start to type the promptbook name until the promptbook appears in the list.
3. Select the promptbook named **Threat Intelligence 360 report based on MDTI article**.
4. Type the name of the Defender Threat Intelligence article in the input box that says *MDTI Article Name*.

    [![Screenshot of TI report promptbook.](media/promptbook-ti-report-tb.png)](media/promptbook-ti-report.png#lightbox)
5. Next, select **Submit**.
6. Wait for Security Copilot to run the article through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts and builds on each until it gets to the last prompt.
7. Read the response by Security Copilot.

### Vulnerability impact assessment

The vulnerability impact assessment promptbook accepts a CVE number or known vulnerability name to find out if the vulnerability has been publicly disclosed or exploited and whether it has been used by threat actors in their campaigns. It can then provide recommendations to address or mitigate the threat and summarize these findings in an executive summary.

To run the **Vulnerability impact assessment** promptbook:

1. Select the Prompts button in the prompt bar and start to type "vulnerability impact assessment" until the promptbooks appear in the list.
2. Select **Vulnerability impact assessment**.
3. Type the CVE number or common vulnerability name that you want to learn about in the input box saying *CVEID*.

    [![Screenshot of vulnerability impact assessment promptbook.](media/promptbook-vuln-tb.png)](media/promptbook-vuln.png#lightbox)
4. Next, select **Submit**.
5. Wait for Security Copilot to run the vulnerability name or CVE through the different prompts. If you see a round progress indicator in place of the response, then the promptbook is still running. Security Copilot generates responses for each of the prompts and builds on each until it gets to the last prompt.
6. Read the response from Security Copilot. The last prompt generates an easily readable report about the vulnerability. The report includes details about known exploitation activities, including mitigation suggestions. Review and verify whether the responses are accurate and meet your needs.