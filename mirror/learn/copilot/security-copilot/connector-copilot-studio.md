---
layout: Conceptual
title: Copilot Studio connector in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/connector-copilot-studio
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Copilot Studio connector Microsoft Security Copilot
ms.date: 2026-01-15T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
locale: en-us
document_id: 971dd139-a365-79c3-f745-8bf8d9c737e6
document_version_independent_id: 971dd139-a365-79c3-f745-8bf8d9c737e6
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/connector-copilot-studio.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: connector-copilot-studio
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/connector-copilot-studio.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 867fecbf-0065-7611-3152-d95155265e8a
---

# Copilot Studio connector in Microsoft Security Copilot | Microsoft Learn

The Copilot Studio connector enables you to access Security Copilot. This topic provides an introduction to the connector action and its properties to get started integrating Security Copilot in your automation workflows.

The connector exposes the following connector actions:

- Submit a Security Copilot prompt - Submit a natural language prompt to create a new Security Copilot investigation. After completion, the evaluation result will then be returned to your workflow.
- Fetch a Security Copilot prompt status - Submit a natural language prompt to pull the status of a Security Copilot evaluation. After completion, the evaluation result will then be returned to your workflow.

Tip

This connector is also available in all the Microsoft Power Platform experiences such as Microsoft Power Automate and Power Apps.

For more information, see [Power Platform Connector Page](/en-us/connectors/securitycopilot/).

## Prerequisites

- Tenant - Ensure that your tenant administrator sets up access to Microsoft Security Copilot before using the connector.
- Ensure the following authentication type is met:

    - **User Authentication** - This connector only supports delegated permissions via OAuth Authorization Code flow. The user that establishes connection to the connector when designing the Copilot Studio workflow must have access to Microsoft Security Copilot. Learn more about [Microsoft Security Copilot Authentication](/en-us/security-copilot/authentication#access-security-copilot-portal).
- Data access for enhanced interaction - It's important that the authenticated user can access data from various remote security products, including tasks like reading Defender incident reports and gathering multifactor authentication (MFA) details, among others.
- Create a connection in Power Apps - You'll need to create a connection in Power Apps for the Copilot Studio action to connect to Security Copilot. Ensure that you create the connection under same Power Apps environment as Copilot Studio on which you are creating the agent. For more information, see [Manage connections](/en-us/power-apps/maker/canvas-apps/add-manage-connections).

## Submit a Security Copilot prompt

- Create and set up a new agent in Copilot Studio.
- Select **Add action** to configure the initial trigger steps.

    ![Add actions into the Copilot Studio agent in the trigger steps](media/copilot-studio-add-actions.png)
- Search for Microsoft Security Copilot to see the related actions you can use.
- Select **Submit a Security Copilot prompt**.

    [![Selecting Submit a Security Copilot prompt action button](media/copilot-studio-submit-prompt.png)](media/copilot-studio-submit-prompt.png#lightbox)
- Configure the action's connections, then select **Next**.
- Configure your action's options, inputs, and outputs, then select **Add action**.

    ![Configure the options, inputs, and outputs of the action](media/copilot-studio-actions.png)

Proceed with adding the **Fetch prompt status** action to the agent.

## Fetch a Security Copilot prompt status

- Using the same agent, select **Add action** to configure the initial trigger steps.
- Search for Microsoft Security Copilot to see the related actions you can use.
- Select **Fetch prompt status**.

    [![Selecting Submit a Security Copilot prompt action](media/copilot-studio-action-fetch-prompt-status.png)](media/copilot-studio-action-fetch-prompt-status.png#lightbox)
- Configure your action's options, inputs, and outputs, then select **Add action**.

    ![Add actions into the Copilot Studio agent](media/copilot-studio-action-fetch-prompt-status-options.png)

The two actions are now added to the agent.

![Shows the two actions fetch prompt status and submit a prompt in the Security Copilot agent](media/copilot-studio-fetch-submit.png)

## Test the agent

To test the agent, you'll need to turn on the Generative option in the settings page. For more information, see [Turn on generative orchestration for an agent](/en-us/microsoft-copilot-studio/advanced-generative-actions#turn-on-generative-orchestration-for-an-agent).

- Navigate to **Settings &gt; Generative AI &gt; Generative**.

![Shows the Generative AI options.](media/copilot-studio-generative.png)

You'll need to configure this setting otherwise you won't be able to test out the action from the natural language chat experience.

You can test your agent in Copilot Studio by entering the prompt \**Submit a Security Copilot, include the Session Id, Evaluation Id, and Prompt Id in the response*.

Important

Make sure to include Session Id, Evaluation Id, and Prompt Id in the prompt.

You can also test **Fetch the status of the prompt** and you should receive the responses with the details.

![Shows the two actions fetch prompt status and submit a prompt being tested and the output.](media/copilot-studio-test-prompt.png)