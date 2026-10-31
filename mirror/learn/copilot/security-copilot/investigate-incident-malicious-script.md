---
layout: Conceptual
title: Investigate an incident's malicious script | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/investigate-incident-malicious-script
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use Security Copilot to investigate an incident and observed suspicious entities.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 830bbf34-52ae-7f78-85f4-77aae24c1409
document_version_independent_id: 830bbf34-52ae-7f78-85f4-77aae24c1409
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/investigate-incident-malicious-script.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: investigate-incident-malicious-script
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/investigate-incident-malicious-script.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: af8fe0e3-6a3c-2aca-854d-75e1f0d5e35b
---

# Investigate an incident's malicious script | Microsoft Learn

**Role mentioned**: SOC TI analyst analyzing suspicious scripts

## Incident investigation scenario

During an incident, security analysts are typically tasked with investigating alerts and gathering pertinent information that's associated with the incident. They conduct root cause analyses and correlate information from a range of sources to determine the potential impact to the organization.

Depending on the scenario, analysts may need to analyze logs, examine malware, reverse engineer files or scripts, and investigate URLs that were observed.

An essential component of an investigation involves understanding what remediation steps to take and effectively conveying significant discoveries to keep stakeholders informed about the current state of the incident.

In this example, Security Copilot is used to perform a comprehensive incident investigation by gathering contextual information from alerts, analyzing a suspicious script, and generating an assessment accompanied by a set of remediation steps.

## Steps

1. Start investigating in Microsoft Defender XDR.

    Security Copilot is integrated in Microsoft Defender XDR. From an incident page, select the **Copilot** button to get a summary of an incident and get details such as the time and date of when an attack started, the entity or asset that started the attack, and assets involved in the attack.

    [![Screenshot of incident summary in Microsoft Defender XDR](media/image1.png)](media/image1.png#lightbox)
2. Analyze the suspicious script.

    Microsoft Defender XDR flags when a suspicious script executes. Use Security Copilot to explain what the suspicious script is doing.

    Note

    Script analysis functions are continuously in development. Analysis of scripts in languages other than PowerShell, batch, and bash are being evaluated.

    With a click of a button, a description is displayed along with an overall summary of the script.

    [![Screenshot of script analyzer in Microsoft Defender XDR](media/image2.png)](media/image2.png#lightbox)
3. Extend the investigation in Security Copilot using natural language prompts and more plugins.

    Continue your investigation in the standalone experience of Security Copilot by selecting **Open in Security Copilot**.

    [![Screenshot of how to investigate by selecting the Open in Security Copilot button](media/open-sc.png)](media/open-sc.png#lightbox)

    The standalone experience allows you to extend the investigation by using natural language prompts.

    [![Screenshot of analyzed script shown in Security Copilot](media/script-analyze-sc.png)](media/script-analyze-sc.png#lightbox)
4. To gain a more comprehensive understanding of the incident, use Security Copilot to gather more information about the suspicious activity seen in the command line script.

    Prompt used:

    *What can you tell me about the reputation of the indicators in the script? Are they malicious? If so, why?*

    Response:

    [![Screenshot of a Security Copilot response](media/image3.png)](media/image3.png#lightbox)

    The response indicates that the several indicators in the script are associated with known threat actors. You can pin this response as a critical piece of information that can be used later.
5. Use Security Copilot to provide an assessment of the incident with supporting evidence and a set of recommendations.

    Prompt used:

    *Summarize the findings from the investigation and conclude with a set of recommendations.*

    Response:

    [![Screenshot of  summary of an incident](media/image4.png)](media/image4.png#lightbox)

    Tip

    You can export the response for future reference. You also have the option of sharing the entire session with other analysts. Other team members who are reviewing the incident can leverage the pin board to get a complete summary of the investigation steps, which saves them valuable time.

    [![Screenshot of incident report pin board](media/image5.png)](media/image5.png#lightbox)

## Conclusion

In this use case, Security Copilot helped conduct a thorough investigation of an incident. Using natural language, analysts are able to get an explanation of what the suspicious script is doing and verify the indicators in the script are associated with known threat actors.

In addition, Security Copilot generated an assessment through a summary report and provided a set of recommendations to contain the incident, which can also be used to improve skills.