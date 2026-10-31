---
layout: Conceptual
title: Setup and manage Security Copilot agents | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/agents-manage
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to setup and manage Security Copilot agents.
ms.date: 2026-03-23T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
ms.custom:
- sfi-ga-nochange
- sfi-image-nochange
locale: en-us
document_id: 8d6a06c9-feb1-6767-f8c3-30b3837a2bd7
document_version_independent_id: 8d6a06c9-feb1-6767-f8c3-30b3837a2bd7
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/agents-manage.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agents-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/agents-manage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: aae08d39-eafa-e711-f999-dec493e8a75e
---

# Setup and manage Security Copilot agents | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This article provides guidance on how Owners and Contributors can effectively set up and manage agents.

This topic helps you learn about:

- Setting up an agent
- Providing feedback directly to an agent to improve its performance
- Controlling an agent's activity by running or pausing it
- Editing its settings
- Managing its memory to ensure it produces results that are relevant and accurate
- Browsing for agents in Security Store

These management controls give you the flexibility to customize agents to fit your workflows while ensuring you maintain full control over their capabilities and behavior.

Note

Depending on how your administrator configured access determines if that agent is available in your workspace.

## Set up Microsoft-built agents

You must set up an agent in order to use it. Follow these setup steps for agents built by Microsoft.

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com).
2. In the left navigation pane, select **Agents**. The agents library is displayed.
3. Choose an agent that you want to use and select **Set up** to proceed to the agent details page.
4. Select an identity for the agent. You have the option of choosing to create an agent identity or assign an existing user account.

    Tip

    It's recommended that you create an agent identity. For more information, see [What are agent identities?](https://aka.ms/WhatAreAgentIdentities).

    [![Image of the agent setup - select an identity](media/select-an-identity.png)](media/select-an-identity.png#lightbox)
5. Follow the setup instructions and add input parameters, if necessary. Parameters vary by agent. For more information, see [Agent terminology](agents-overview#agent-terminology).

    | Parameter | Description |
    | --- | --- |
    | Trigger | An event or condition that tells an agentic system to initiate an action or series of actions. |
    | Permissions | The level of authorization an AI agent is granted that enables it to access specific information or carry out tasks. |
    | Identity | The credentials that the agent uses when it runs. For some agents, you have the option of creating an agent ID or connect using an existing user account. |
    | Plugins | A component that extends what an agent can do by providing access to capabilities in Microsoft and non-Microsoft services and public websites through APIs. |
    | Products | The Microsoft products that are required for the agent to run. |
    | Role-based access | The required roles or permissions required to turn on and/or run the agent. |
6. After completing the setup, you'll be taken to the agent page.
7. Select **Run** to view the agent output or manage the agent.

## Set up partner-built agents

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

When setting up a partner-built agent that accesses a Microsoft tool (skill) and accesses data from a Microsoft product such as Microsoft Intune, Microsoft Entra, Microsoft Sentinel, Defender, or Defender Threat Intelligence, a Global Administrator within the tenant must approve to allow access of required permissions for the agent.

Once the approval is granted, Security Copilot owners and contributors can finish the agent setup including setting up the identity, trigger, and other values.

For agents that don't need Microsoft product permissions, approval isn't required.

### For Security Copilot Owner and Contributors

1. During the agent setup process, a banner is shown stating that agent requires consent from the Global Administrator and the Set up button disabled.

    [![Image of the agent setup disabled for partner agents in Security Copilot](media/setup-disabled.png)](media/setup-disabled.png#lightbox)
2. Select **Copy Link** to share it with the Global Administrator. After the Global Administrator completes the approval steps, you can proceed with the agent setup steps.
3. Select **Set up** to proceed to the agent details page.
4. Assign an existing user account and sign in, then select **Next**.

    [![Image of assigning an existing account for the agent](media/assign-existing-account.png)](media/assign-existing-account.png#lightbox)
5. Follow the setup instructions and add input parameters, if necessary. Parameters vary by agent. For more information, see [Agent terminology](agents-overview#agent-terminology).
6. After completing the setup, you'll be taken to the agent page.
7. Select **Run** to view the agent output or manage the agent.

### For Global Administrators

1. Open the link provided by the Security Copilot Owner/Contributor to approve the agent setup. You can also navigate to **Active agents** &gt; select **Set up** on the agent.
2. The agent modal displays the agent details and the message to approve. Review the required permissions and other details about the agent such as description, trigger, and others.
3. Start the approval process by selecting **Start approval**. Follow the prompts to grant the necessary permissions.

    [![Image of the agent setup approval required for Global Administrator in Security Copilot](media/start-approval.png)](media/start-approval.png#lightbox)

    You need to approve the use of the agent for use in your org. Depending on the agent, you might also need to approve agents that use Microsoft-built skills or plugins to access data and perform actions.

    [![Image of the agent approve by Global Administrator in Security Copilot](media/global-admin-approve.png)](media/global-admin-approve.png#lightbox)
4. Once the approval is complete, the Security Copilot owner or contributor can finish the setup of the agent. You also have the option of setting up the agent for users in your org.

## Provide feedback

Owners and Contributors can provide feedback to the agent to help it improve. When you provide feedback related to the agent, the agent takes your input into consideration during its operations. This feedback is stored in the agent's memory, allowing it to tailor its responses and actions based on your insights. You can also manage the agent's memory to further refine the considerations it takes when forming outputs. For more information, see Managing the agent's memory.

If your feedback is to Microsoft, your inputs may be considered in future plans. This feedback helps improve the overall product by informing the development team about user experiences and suggestions for enhancements.

1. In the agent results pane, select the feedback button.

    ![Available feedback](media/agent-result-feedback-buttons.png)
2. Select whether your feedback is for the agent or to Microsoft from the drop-down menu.

    ![Agent feedback option](media/agent-feedback.png)

    ![Product feedback option](media/agent-feedback-microsoft.png)
3. Provide details related to your feedback and select **Submit**.

## Manage the agent's memory

After providing feedback to the agent, you have the option of tweaking its memory. Managing the agent's memory is crucial for tailoring its performance. You can control what information the agent retains and uses, ensuring that it considers relevant data when forming outputs. This management helps in refining the agent's responses and improving its overall effectiveness.

1. From the agent page, select the overflow menu (...) then **Manage memory**. Your previously entered feedback to the agent is listed.

    ![Manage agent memory](media/manage-memory-button.png)
2. Select the feedback you want to review.
3. You can choose to remove the feedback from memory by selecting **Reject feedback**.

## Run or pause an agent

You have the flexibility to configure the agent to run automatically or manually. If you prefer the agent to operate in the background, you can set it to run automatically. Alternatively, you can choose to run it manually when needed. If the agent isn't required to be active, you can pause it to stop its operations temporarily.

1. Go to the agent you want to configure.
2. Select whether to pause or run the agent.

    ![Pause or run the agent](media/pause-run-agent.png)

    If the agent trigger is already turned on, it automatically runs as scheduled and the **On the trigger** button is greyed out. You can also choose to manually run the agent by selecting **One time**.

## Edit an agent

Owners and Contributors can edit an agent to modify its configuration settings. This includes adjusting its identity or other available parameters to better suit your needs. Editing allows you to customize the agent's behavior and ensure it aligns with your specific requirements.

1. Go to the agent you want to edit.
2. Select **Edit**.

    ![Edit agent option](media/edit-agent-button.png)
3. Update the agent details and select **Finish**.

## Browse more agents in Security Store

In the Agents page, you can easily access agents in Security Store. For more information, see [Security Store documentation](/en-us/security/store/).

Select **Browse more agents** or select **Security Store** from the menu. For more information, see [Microsoft Security Store in Microsoft Security Copilot](security-store-integration).