---
layout: Conceptual
title: Triage incidents with enriched threat intelligence | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/triage-alert-with-enriched-threat-intel
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use effective prompts in Microsoft Security Copilot to reduce time to triage incidents based on enrichment from threat intelligence.
ms.date: 2026-05-26T00:00:00.0000000Z
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
search.appverid: MET150
f1.keywords: NOCSH
audience: ITPro
locale: en-us
document_id: 8b4b9443-ac23-2a87-a009-7d03cf78868e
document_version_independent_id: 8b4b9443-ac23-2a87-a009-7d03cf78868e
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/triage-alert-with-enriched-threat-intel.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: triage-alert-with-enriched-threat-intel
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/triage-alert-with-enriched-threat-intel.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 268ac50e-6a24-5e8b-44f7-5e365703971d
---

# Triage incidents with enriched threat intelligence | Microsoft Learn

The article covers how an analyst uses Security Copilot to quickly triage an incident using sample prompts.

**Roles mentioned**: SOC analyst and identity admin for incident triage (main), CISO and other stakeholders for incident report summary (recipient)

## Incident triage scenario

As a security operations center (SOC) analyst, you review alerts and incidents assigned to you. Your duty is to identify if real action needs to be taken. You leverage information within the alerts associated with the incident to guide your process. You often collect contextual information to further understand the next steps you should take. With the enrichment of involved entities and full understanding of the underlying alerts, you determine whether to escalate or remediate the incident.

In this detailed example, an analyst uses Security Copilot to quickly triage an incident. If the incident is a real threat, the goal is to either gather new indicators of compromise or link entities to finished intelligence. In this case, the threat intelligence is summarized by Security Copilot to show the connection to a known threat actor and inform the severity assessment.

## Steps to triage incidents using threat intelligence

1. **Start your day with Security Copilot. Retrieve the latest Microsoft Defender XDR incident that's assigned to you and summarize the alerts associated with it.**

    Prompt used:

    *What is the latest active Defender incident assigned to me, `angus.macgregor@contoso.com`? Summarize it, including the alerts associated with it.*

    Response:

    ![Screenshot of summary of Defender alert.](media/use-case-defender-incident-summary.png)

    Looks like possible credential theft. You follow the recommended actions and begin to scope the incident and validate the alert.
2. **Focus in on specific entities to get more information about them.**

    Prompt used:

    *Elaborate on the details of this Defender incident alert, including the entities involved.*

    Response:

    ![Screenshot of Defender alert enrichment.](media/use-case-defender-alert-details.png)

    Now you have a user account and device to further investigate. In this case, you choose to understand more about the affected user before digging into the details of the attack on the device.
3. **Get more information about this user to guide next steps. What type of actions might be next for someone with her credentials?**

    Prompt used:

    *Tell me more about the user entity.*

    Response:

    ![Screenshot of detailed user information.](media/use-case-user-entity-details.png)

    You find out this user is works in Sales. If her credential was stolen, this could affect sales data. You remember that your Sentinel workspace has an SAP solution to help detect threats there. Is this Defender alert linked to a Microsoft Sentinel incident? Your first priority is to determine if there has been any suspicious activity by this user in SAP.
4. **Use a saved hunting query to correlate entities with Sentinel incidents.**

    You manually activate the suggested prompt for the **Natural language to Sentinel KQL** plugin to run your query.

    ![Screenshot showing suggested prompt for Microsoft Sentinel hunting queries.](media/manually-run-sentinel-hunting-query.png)

    Tip

    If the query needs to be adjusted slightly, edit the prompt and re-run it. For instance, your query projected `IncidentNames`, but those are simply GUIDs. You remember it's the `Title` field you really want. Simply edit the prompt and select the **Re-run prompt** option.

    ![Screenshot showing prompt options for edit, re-run and delete.](media/use-case-edit-prompt.png)

    Adjusted prompt used:

    *Run the following KQL*

    ```
        *SecurityAlert | where Entities has "`adele.vance@contoso.com`" and TimeGenerated >= datetime(10/06/2023) | join kind=inner (SecurityIncident | mv-expand SystemAlertId = AlertIds | extend SystemAlertId = tostring(SystemAlertId)) on SystemAlertId | summarize by IncidentNumber, Title*
    ```

    Response:

    ![Screenshot showing Microsoft Sentinel hunting query results.](media/use-case-run-kql.png)

    The SAP related incident is now your first priority.
5. **Pivot your investigation to the SAP incident associated with the user from the original alert.**

    Prompt used:

    *Elaborate on Sentinel incident 33805 and give me details about the entities.*

    Response:

    ![Screenshot showing Microsoft Sentinel incident summary.](media/use-case-sentinel-incident-details.png)

    A lot of information is returned from this prompt. The malicious IP and possible exfiltration of financial data stand out as important items to investigate further.
6. **Find out more about the IP address entity and examine how it was determined to be malicious.**

    Prompt used:

    *Give me more details about the IP address and why is it malicious?*

    Response:

    ![Screenshot showing details of malicious IP.](media/use-case-mdti-ip-enrichment.png)
7. **Create a summary report**

    Save time in the escalation process with a summary for leadership and incident response teams.

    Prompt used:

    *Write a report based on this investigation. Lead with your assessment of the original Defender incident and whether the threat of credential theft is real. Conclude your assessment on how that threat relates to the Sentinel incident regarding the file downloaded to a malicious IP.*

    Response:

    ![Screenshot showing investigation summary report.](media/use-case-summary.png)
8. **Pin the most useful prompts responses and edit the session name.**

    You've reached your goal and determined the assigned Microsoft Defender XDR incident is a real threat. By linking it to a Microsoft Sentinel incident involving an exfiltrated SAP file, you prepare to collaborate with your escalation team.

    ![Screenshot showing pin board and edited session name.](media/use-case-edit-session-and-share.png)

## Conclusion

In this use case, Security Copilot helped triage an assigned incident quickly. You confirmed the alert required real action by investigating related incidents. The hunt resulted in finding an incident with an IP entity linked to finished intelligence about the threat actor and C2 tool used. With a succinct pin board, you shared the session and a summary report giving the escalation team the information they need to respond effectively.