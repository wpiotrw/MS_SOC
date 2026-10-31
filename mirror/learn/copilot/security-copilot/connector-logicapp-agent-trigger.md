---
layout: Conceptual
title: Trigger Security Copilot agents from Azure Logic Apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Use Azure Logic Apps to trigger Microsoft Security Copilot agents and automate security workflows. Learn how to configure and verify agent runs.
ms.date: 2026-04-10T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
search.appverid: MET150
f1.keywords: NOCSH
audience: ITPro
locale: en-us
document_id: c5fee032-3c06-4acd-c273-884462c8380c
document_version_independent_id: c5fee032-3c06-4acd-c273-884462c8380c
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/connector-logicapp-agent-trigger.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: connector-logicapp-agent-trigger
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/connector-logicapp-agent-trigger.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e60d1924-c4ad-4104-bd1b-973758bbac7a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/91d5f984-ee3d-43c4-9daf-bb09a6bc4e1a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 0cccc351-1730-719a-c19e-9b0b4d96fc5d
---

# Trigger Security Copilot agents from Azure Logic Apps | Microsoft Learn

Building on how organizations already use Logic Apps to automate security workflows, a new connector action for Security Copilot in Logic Apps flows allows teams to easily invoke agents they create as part of repeatable workflows. This automated workflow brings deeper AI-driven investigation, context, and decision support into tasks such as incident triage, threat intelligence analysis, and policy validation.

This article explains how to trigger Microsoft Security Copilot agents within the automated Azure Logic Apps workflows by configuring prerequisites, adding the agent action in Logic Apps, and verifying the agent run in Security Copilot.

Using the Security Copilot Logic Apps agent connector, you can:

- Trigger previously configured Microsoft Security Copilot agents from Logic App
- Chain agent execution with other Logic Apps actions
- Pass inputs dynamically from earlier workflow steps including advanced parameter support

## Before you begin

Make sure you have the following resources and permissions:

- Access to **Microsoft Security Copilot** with permission to create and run agents.
- An agent that is already created and configured (agent that is set up and ready to run) in Security Copilot.

    Note

    When you create your own agent, you must upload the plugin containing the agent to **Anyone in this Workspace** to be available for triggering from Logic Apps.
- Access to **Azure Logic Apps** (Consumption or Standard).
- Permission to create connections in Azure Logic Apps.

## Step 1: Set up an agent in Security Copilot

Logic Apps can only trigger agents that are fully configured and available in your Security Copilot workspace.

1. Create a new agent or select an existing agent in [Security Copilot](https://securitycopilot.microsoft.com/). The following table provides reference to documentation for creating agents:

| Type | Description |
| --- | --- |
| Plugins | Build and upload a [custom plugin](/en-us/copilot/security/developer/build-agent-manifest) |
| Agents | Build [custom agents](/en-us/copilot/security/developer/agent-standalone-overview) using natural language or the agent builder form |

1. Complete the agent **Set up** process. For more information, see [Setup agents](agents-manage).
2. Configure the **agent run identity** during setup.

    - This identity is used when the agent executes.
    - It is separate from the identity used to sign in to the Logic Apps connector.
3. If you create your own **custom agent**, you must upload as a plugin that contains the agent and set sharing to **Anyone in this workspace**, so that the agent is available to trigger from Azure Logic Apps.

[![Image of the agent setup in Security Copilot](media/logic-apps-agent-set-up.png)](media/logic-apps-agent-set-up.png#lightbox)

The illustration shows the agents that are set up and ready to use in the **Agents in use** section.

Note

Currently, agents must be created and set up in the **default workspace**. Agents created in non-default workspace aren't available to trigger from Logic Apps. So, if an agent isn't shared with the workspace or is missing required setup, it does not appear in Logic Apps.

## Step 2: Add an action in Azure Logic Apps

1. In the [Azure portal](https://ms.portal.azure.com/#home), create a new Logic App or open an existing one.
2. Open the **Logic app designer**.
3. Add a **trigger** as the first step to start any workflow in Azure Logic Apps. For information on adding a trigger, see [Add a trigger](/en-us/azure/logic-apps/add-trigger-action-workflow?tabs=consumption#add-a-trigger-to-start-your-workflow).
4. Select **Add an action** in the Logic app designer.

    [![Image of the add action in Logic apps](media/logic-apps-add-action.png)](media/logic-apps-add-action.png#lightbox)

## Step 3: Add the Security Copilot agent action

1. Search for **Security Copilot** connector. The Security Copilot actions are displayed.
2. Select the action **Execute a Security Copilot Agent**.

    [![Image of the agent action in Logic apps using the Security Copilot connector](media/logic-apps-agent-action.png)](media/logic-apps-agent-action.png#lightbox)

## Step 4: Create the connector connection

Create a connection when you add the agent action for the first time.

1. The **Create connection** window is displayed.
2. Sign in with an identity that has access to Security Copilot to create a new connection.

    [![Image of the create a connection to Security Copilot in Logic apps](media/logic-apps-create-connection.png)](media/logic-apps-create-connection.png#lightbox)

Important

The connection sign-in identity is used only to access Security Copilot. The agent itself runs using the agent run identity configured during agent setup.

## Step 5: Configure the agent parameters

1. In the **Agent Name** field, select the agent you want to run.
2. Select the trigger configuration (the default trigger is typically sufficient).
3. Provide required parameters.

    - Fill in all the required inputs.
    - Find optional inputs under **Advanced parameters**.

    [![Image of the screen to put agent parameters for Security Copilot in Logic apps](media/logic-apps-agent-parameters.png)](media/logic-apps-agent-parameters.png#lightbox)
4. (Optional) You can pass in outputs of previous steps as agent inputs.
5. Select **Save** to save the workflow.
6. **Run** the Logic App manually or wait for the trigger to fire.
7. Select **Show runs** to see the **Runs history**. Confirm that the agent action completed successfully.

    [![Image of the screen to the succeeded agent run history in Logic apps](media/logic-apps-run-history.png)](media/logic-apps-run-history.png#lightbox)
8. You can also see the response in the Status as **Succeeded**.

    [![Image of the succeeded status response in Logic apps](media/logic-apps-run-succeeded.png)](media/logic-apps-run-succeeded.png#lightbox)

## Step 6: Verify the agent run in Security Copilot

1. Navigate to **Security Copilot**.
2. Open the agent you triggered.
3. Confirm that the agent run appears in the agent run history.

    [![Image of the screen to verify agent run in Security Copilot after its triggered from Logic apps](media/logic-apps-copilot-agent-run.png)](media/logic-apps-copilot-agent-run.png#lightbox)

You can also edit the Logic Apps action to select a different agent.

## Troubleshooting

**Agent doesn't appear in Logic Apps**

- Make sure you fully set up the agent in Security Copilot.
- For custom agents, confirm you share the plugin that contains the agent with **Anyone in this workspace** so the agent is available to trigger from Logic Apps.

**Permission or sign-in errors**

- Verify the Logic Apps connection identity has access to Security Copilot.
- Verify the agent run identity has the required permissions.

**Missing required inputs**

- Check that you provide all required agent inputs in the action configuration.