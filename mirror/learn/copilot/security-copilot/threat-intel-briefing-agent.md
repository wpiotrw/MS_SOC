---
layout: Conceptual
title: Microsoft Security Copilot Threat Intelligence Briefing Agent | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/threat-intel-briefing-agent
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Security Copilot Threat Intelligence Briefing agent
ms.date: 2026-05-11T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
ms.custom: sfi-image-nochange
locale: en-us
document_id: 2bb18b92-968b-a107-bc3c-f3ba0b48061d
document_version_independent_id: 2bb18b92-968b-a107-bc3c-f3ba0b48061d
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/threat-intel-briefing-agent.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: threat-intel-briefing-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/threat-intel-briefing-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c671beaa-a830-4c9f-aceb-97379ee031ca
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8921374c-4dbe-4ed0-b011-a39e18bfbd98
platformId: 63fbc46f-cab9-1c98-6ed3-20b6c580d6a1
---

# Microsoft Security Copilot Threat Intelligence Briefing Agent | Microsoft Learn

Note

This article discusses the Threat Intelligence Briefing Agent standalone experience in Security Copilot. To learn more about the embedded experience in the Microsoft Defender portal, read [Microsoft Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender](/en-us/defender-xdr/threat-intel-briefing-agent-defender).

Threat intelligence analysts face several challenges in delivering insightful, actionable, contextualized intelligence. The task of developing threat intelligence briefings involves collecting information from various threat feeds, tools, and portals; filtering and correlating this information; and analyzing and mapping organizational risks. These activities happen before analysts can even start developing the report itself and generating insights for when they deliver the briefing. By then, as these processes can take anywhere from hours to days, the threats facing the organization have already evolved, which can render the briefing obsolete.

The Threat Intelligence Briefing Agent was developed in response to these pain points. The Threat Intelligence Briefing Agent in the Microsoft Security Copilot standalone portal generates threat intelligence briefings based on the latest threat actor activity and both internal and external vulnerability information—in a matter of minutes. The agent can help security teams save time by creating a customized, relevant report that provides CISOs, security managers, and analysts with key situational awareness and a solid foundation for defense work.

The agent leverages dynamic automation and deep generative AI along with its wealth of threat intelligence knowledge and signals. When building the briefing, the agent dynamically chooses the next step based on the outcome of the previous step, allowing it to decide in real-time what threat intelligence to include and prioritize. The agent then translates this technical information into a digestible report that can be consumed by various audiences.

The Threat Intelligence Briefing Agent is best suited for customers who have turned on Microsoft Defender External Attack Surface and Microsoft Defender for Endpoint, as the agent relies on signals and insights from these first-party integrations to deliver accurate and context-rich reports.

## Prerequisites

### Products

Microsoft Security Copilot is needed to run this agent.

### Plugins

The following plugin is required to run this agent:

- Microsoft Threat Intelligence

The following plugin is optional but can add more context to the output:

- Microsoft Defender External Attack Surface Management

### User account permissions configuration

Important

**Identity and permissions requirement**: This agent requires connection to an existing user account or creation of a new [agent identity](https://aka.ms/WhatAreAgentIdentities)(recommended). The agent can read data from Defender External Attack Surface Management and Defender Vulnerability Management. You must configure the user account with the appropriate permissions outlined in the following section before setting up the agent.

#### Permission overview

The user account connected to the agent must have these permissions:

**Required permissions:**

- **Microsoft Defender for Endpoint**: Access to Defender Vulnerability Management data
- **Security Copilot Contributor**: Access to Security Copilot platform and agent management

**Optional permissions:**

- **Exposure Management (read)**: Access to Microsoft Security Exposure Management insights, including External Attack Surface Management data

**Role-based access:**

- Owners and contributors can see the report generated by the Threat Intelligence Briefing Agent within the Microsoft Security Copilot agent library page

#### Configure permissions

##### Step 1: Create custom role in Microsoft Defender XDR

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization.

1. Sign in to the [Microsoft Defender portal](https://security.microsoft.com/) as Security Administrator or higher.
2. Navigate to **Permissions** &gt; **Microsoft Defender XDR** &gt; **Roles**.
3. Select **Create custom role**.
4. On the **Basics** tab:

    - **Role name**: `Threat Intel Agent - Read Only`
    - **Description**: `Read-only access for Threat Intelligence Briefing Agent`
    - Select **Next**
5. On the **Choose permissions** page:

    - Select **Security posture**
    - Select **custom permissions**
    - Under **Posture management**, select **Vulnerability management** - **Read**
    - Select **Apply** &gt; **Next**
6. On the **Assign users and data sources** page:

    - Select **Add assignment**
    - **Assignment name**: `Threat Intel Agent Assignment`
    - **Employees**: Select the user account for the agent
    - **Data sources**: Select **Microsoft Defender for Endpoint**
    - Select **Next** &gt; **Submit**

##### Step 2: Assign Security Copilot Contributor role

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Select the home menu &gt; **Role assignment** &gt; **Add members**.
3. Search for and select the user account, then assign **Security Copilot Contributor** role.
4. Select **Add**.

##### Step 3 (Optional): Add External Attack Surface Management permissions

If your organization uses Microsoft Defender External Attack Surface Management:

1. In the Microsoft Defender portal, go to **Permissions** &gt; **Microsoft Defender XDR** &gt; **Roles**.
2. Find the `Threat Intel Agent - Read Only` role and select **Edit**.
3. Navigate to **Choose permissions** &gt; **Security posture** &gt; **Select custom permissions**.
4. Under **Posture management**, add **Exposure Management** - **Read**.
5. In **Data sources**, add **Microsoft Security Exposure Management**.
6. Save the changes.

Important

After setting up permissions, activate the [Microsoft Defender XDR Unified role-based access control (RBAC) model](/en-us/defender-xdr/manage-rbac) for the role to take effect.

Tip

Consider using a dedicated service account for running agents to maintain separation of duties and enhance security monitoring.

### Trigger

This agent runs at the set time interval when turned on, or manually when you want to run it.

## Set up the agent

1. To run the Threat Intelligence Briefing Agent, go to the **Agents** page in the Microsoft Security Copilot standalone portal.

    [![Screenshot of Microsoft Security Copilot agent library page.](media/agents-library-ti.png)](media/agents-library-ti.png#lightbox)
2. Choose the **Threat Intelligence Briefing Agent** and select **Set up**.

    [![Screenshot of Threat Intelligence Briefing Agent details page.](media/2-ti-brief-agent-view-details.png)](media/2-ti-brief-agent-view-details.png#lightbox)
3. Select an identity for the agent. You have the option of choosing to create an agent identity or assign an existing user account. After this, wait for the agent to finish setting up.

    [![Screenshot of Threat Intelligence Briefing Agent set up page.](media/3-ti-brief-agent-setup.png)](media/3-ti-brief-agent-setup.png#lightbox)
4. Specify the input parameters to customize the output, then select **Next**. You can edit these parameters later by selecting the three dots in the upper right section of the agent overview page.

    [![Screenshot of Threat Intelligence Briefing Agent set up parameters page.](media/4-ti-brief-agent-setup.png)](media/4-ti-brief-agent-setup.png#lightbox)

    - Insights to research – the number of vulnerabilities the agent researches for active threats
    - Look back days – how far back the agent researches threats against your vulnerabilities
    - Email – email address of user or distribution group that the briefing is sent to
    - Region – scope of geographical area the agent checks for threats
    - Industry – sector or industry that the agent checks for threats
5. After the agent is created, select **Return to agents** to go back to the **Agents** page, or select **Go to agent** to go to the Threat Intelligence Briefing Agent overview page.

    [![Screenshot of Threat Intelligence Briefing Agent set up page after the agent is created successfully.](media/5-ti-agent-finish.png)](media/5-ti-agent-finish.png#lightbox)
6. To run the agent, go to the upper right of the agent overview page and select **Run**. Select **On the trigger** to schedule the agent to run at the set time or select **One time** to run the report on demand.

## Assess and provide feedback on the agent’s output

The generated reports appear in the Threat Intelligence Briefing Agent page under **Activity**. The page displays the name of the report, the start time, method of generation, and current status.

[![Screenshot of Threat Intelligence Briefing Agent overview page with results.](media/7-ti-brief-agent-page.png)](media/7-ti-brief-agent-page.png#lightbox)

Select one of the reports to assess the agent's output.

[![Screenshot of Threat Intelligence Briefing Agent sample report.](media/8-ti-brief-agent-page.png)](media/8-ti-brief-agent-page.png#lightbox)

The threat intelligence briefing contains a relevant summary of threat information and detailed technical analysis, including any actively exploited vulnerability and its possible organizational impact.

The Threat Intelligence Briefing Agent dynamically chooses the next step based on the outcome of the previous step as it builds the briefing. You can view the agent’s progress toward producing the threat briefing by selecting **View activity**.

[![Screenshot of View activity button.](media/9-ti-briefing-view-activity.png)](media/9-ti-briefing-view-activity.png#lightbox)

You'll see details of the activity, providing you with transparency on the steps the agent takes to produce the output.

[![Screenshot of the activity map.](media/agent-activity-map.png)](media/agent-activity-map.png#lightbox)

You can provide feedback about the briefing by selecting the thumbs up or thumbs down button. You can elaborate in the text box that appears after. Select **Submit** to give your feedback.