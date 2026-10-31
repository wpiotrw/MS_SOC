---
layout: Conceptual
title: Darktrace and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-darktrace
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Darktrace plugin with Microsoft Security Copilot.
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
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 7c11f2b2-3bd1-2e7f-e433-ad21bea1967c
document_version_independent_id: 7c11f2b2-3bd1-2e7f-e433-ad21bea1967c
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-darktrace.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-darktrace
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-darktrace.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: fc42a9c7-25ce-a3b9-464b-071806139c02
---

# Darktrace and Microsoft Security Copilot | Microsoft Learn

Darktrace offers cybersecurity AI services to provide preemptive visibility into security posture, real-time detection, and autonomous response to known and unknown threats. You can use the Darktrace plugin with Microsoft Security Copilot to proactively detect and investigate threats across your digital ecosystem.

- Query Darktrace's rich and high fidelity security data using natural language, streamlining the investigation process and enabling faster threat response.
- Leverage Copilot's generative AI capabilities to interact with Darktrace's security alerts, device information, and email security insights, enhancing the overall understanding of your security landscape.
- Gain comprehensive visibility into your organization's security posture, including device connections, external endpoints, Cyber AI Analyst incidents, and email-related threats.

By integrating Darktrace's unparalleled AI-driven threat detection and mitigation with Microsoft Security Copilot, this plugin improves the capabilities of security teams across the board. Obtain real-time insights into possible security incidents, privileged accounts, and unusual user activities through an easy-to-use, natural language interface.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

The Darktrace integration with Security Copilot uses OAuth Client Credentials flow to authenticate and requires a Client Application to be configured in the Darktrace Active AI Security Portal. Please note that Security Copilot integration is currently only available to Early Adopters of the ActiveAI Security Portal. If you would like to trial Security Copilot, please contact your Darktrace account team. You'll need to take the following steps before using the plugin.

1. Sign into your Darktrace ActiveAI Security Portal, go to the Client Applications page, and create your CCA.

    - Your Darktrace API URL
    - Client ID
    - Client Secret
    - Your Scopes
    - Token Endpoint
2. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
3. Access **Manage plugins** by selecting the **Sources** button from the prompt bar.
4. Next to **Darktrace**, select the toggle to enable it.
5. In the settings pane for the plugin, provide the information you saved from step 1. Leave AuthorizationContentType field as default, and in the TokenEndpoint field enter `https://auth.login.darktrace.com/oauth/token`.
6. Save your changes.

## Sample Darktrace prompts

After the Darktrace plugin is configured, you can use it by including `Darktrace` in your Security Copilot prompt along with an action. The following table lists example prompts to try.

| Capability | Example prompts |
| --- | --- |
| Get Model Breaches | `What were the top 5 high-scoring Darktrace alerts in the last week?``Show me all the model breaches involving device ID 500 in the past month from Darktrace.``Retrieve the model breach information for pbid 1234 and explain what occurred.``Display Darktrace model breaches for subnet ID 250 with a minimum score of 0.7 in the last 72 hours.` |
| Get Model Breach Comments | `What are the latest comments on the Darktrace model breach with pbid 4567?``Has anyone added any valuable information to the model breach with pbid 1234 in Darktrace?` |
| Get AI Analyst Incident Groups | `Show me the Darktrace AI Analyst incidents with a score higher than 90 from the past week.``List all critical incidents involving device ID 1500 in the last month from Darktrace.``Retrieve incidents associated with subnet ID 300 in the past 7 days from Darktrace and display them in the German language.``Are there any Darktrace AI Analyst incidents with the unique identifier "abcd-1234-efgh-5678" in the system?` |
| Get AI Analyst Incident Events | `Give me a detailed breakdown of the Darktrace incident with groupid "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633".``Show me more information about this Darktrace incident in Spanish.``What are the Darktrace AI Analyst events for device ID 1000 that are part of critical incidents?` |
| Get AI Analyst Incident Comments | `What are the recent comments on the Darktrace AI Analyst event with incident_id "04a3f36e-4u8w-v9dh-x6lb-894778cf9633"?``Has anyone from the security team added any context to this Darktrace incident?` |
| Get Device Information | `Can you provide detailed information about device ID 1234 from Darktrace, including any tags associated with it?``What is the current IP address of device ID 9 in the Darktrace system?``Retrieve the device information for the entity with MAC address "AA:BB:CC:DD:EE:FF" from Darktrace.` |
| Search Devices | `Find all devices in subnet 10.0.1.0/24 with a "Respond" tag and sort them by last seen using Darktrace.``Has Darktrace seen a laptop with the IP address 8.8.8.8?``Show me a list of devices that could be owned by "sarah" in Darktrace, sorted by last seen activity.` |
| Format Model Breaches as Table | `Get me high scoring model alerts from Darktrace in the past week, format the results as a table, and give me definitions of any complex terminology.``Display all Darktrace model breaches involving device ID 250 in the past month in a table format, and include a column with descriptions of the breach categories.``Present Darktrace model breaches for subnet ID 100 with a minimum score of 0.8 in the last 72 hours as a table, and include a column with the involved devices' hostnames.` |
| Analyze AI Analyst Incident Trends | `What are the common themes among the Darktrace AI Analyst incidents with a score higher than 90 from the past month?``Analyze the Darktrace AI Analyst incidents involving device ID 1500 in the last month and identify any patterns or trends in the security events.``Are there any recurring issues or attack vectors in the Darktrace AI Analyst incidents associated with subnet ID 200 in the past 7 days?` |
| Investigate AI Analyst Incident Event | `Can you provide a detailed analysis of the Darktrace AI Analyst event with incident_id "04a3f36e-4u8w-v9dh-x6lb-894778cf9633" and suggest possible mitigations?``Investigate the Darktrace AI Analyst event with incident_id "04a3f36e-4u8w-v9dh-x6lb-894778cf9633" in depth and provide a report on its potential impact on our network.` |
| Device Owner Identification | `Can you identify the owner of the device with IP address 8.8.8.8 in Darktrace based on its activity patterns and associated user accounts?``Determine the likely owner of the device with MAC address "AA:BB:CC:DD:EE:FF" in Darktrace by analyzing its usage patterns and associated services.` |

## Troubleshooting the Darktrace plugin

### Timestamp Support

To filter data to a specific time frame, this plugin may require timestamps in Epoch/UNIX format. To retrieve the relevant time frame in the correct format, use a service such as https://epochconverter.com or https://unixtime.org.

## Provide feedback

To provide feedback, contact [Darktrace](https://darktrace.com/).