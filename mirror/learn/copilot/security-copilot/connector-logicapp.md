---
layout: Conceptual
title: Logic Apps connectors in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/connector-logicapp
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about Logic Apps connectors in Microsoft Security Copilot
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
document_id: 6a349c46-4cc6-bcd8-97db-9f3d88524515
document_version_independent_id: 6a349c46-4cc6-bcd8-97db-9f3d88524515
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/connector-logicapp.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: connector-logicapp
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/connector-logicapp.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/e60d1924-c4ad-4104-bd1b-973758bbac7a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/91d5f984-ee3d-43c4-9daf-bb09a6bc4e1a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 881d65f5-16fa-1062-6582-92d071858771
---

# Logic Apps connectors in Microsoft Security Copilot | Microsoft Learn

The Microsoft Security Copilot Logic Apps connector allows you to call into Copilot from an Azure Logic Apps workflow. This document provides an introduction to the connector action and its properties to get started integrating Security Copilot in your automation workflows.

The connector exposes 2 connector actions:

- Submit a Security Copilot prompt - Submit a natural language prompt to create a new Security Copilot investigation. After completion, the evaluation result will then be returned to your workflow.
- Submit a Security Copilot promptbook - Given a promptbook, invoke a new Security Copilot promptbook evaluation and return the output to your Azure Logic Apps workflow.

Tip

This connector is also available in all the Microsoft Power Platform experiences such as Microsoft Power Automate and Power Apps.

For more information, see [Power Platform Connector Page](/en-us/connectors/securitycopilot/).

## Prerequisites

- Tenant - Ensure that your tenant administrator sets up access to Microsoft Security Copilot before using the connector.
- User Authentication - This connector only supports delegated permissions via OAuth Authorization Code flow. The user that establishes connection to the connector when designing the Azure Logic Apps workflow must have access to Microsoft Security Copilot. Learn more about [Microsoft Security Copilot Authentication](/en-us/security-copilot/authentication#access-security-copilot-portal).
- Data access for enhanced interaction - It's important that the authenticated user can access data from various remote security products, including tasks like reading Defender incident reports and gathering multifactor authentication (MFA) details, among others.

## Submit a Security Copilot prompt

- Create and set up a new Logic Apps workflow in the Azure portal.

    - The connector is available in both "Standard" and "Consumption" plan types.
- Configure the initial trigger step and proceed to search for the Copilot action "Submit a Security Copilot prompt".
- Fill in the parameters on the Copilot action.

    ![Azure Logic Apps Connector Parameters](media/logicapp-connector-1.png)
- Reference the following descriptions for the Copilot Action Parameters

    - Prompt Content (Required): Enter the natural language prompt to be evaluated.
    - Session ID (Optional): Enter an existing Copilot sessionId for maintaining continuity in your tasks, allowing to ask prompts within the same investigation. If omitted, Copilot creates a new investigation.
    - Plugins (Optional): Enter a list of plugin names for your investigation, scoping down the potential plugins that Copilot can pick to execute and answer your natural language prompt. Useful to avoid plugin collisions.
    - Direct Skill Name (Optional): Enter a specific Copilot skill to execute. Convenient way to bypass the standard Copilot planner if you know a specific skill to trigger.
    - Direct Skill Inputs (Optional): Enter a JSON body containing key/value pairs for required skill parameters. Useful when providing a Direct Skill Name to execute.

## Submit a Security Copilot promptbook

- Create a new Azure Logic Apps workflow in the Azure portal.

    - The connector is available in both "Standard" and "Consumption" plan types.
- After setting up the Azure Logic App and configuring the initial trigger step, proceed to search for the Security Copilot action.

    ![Azure Logic Apps Connector - action](media/clientslogicappconnectorrunpromptbook1.png)
- After choosing the new Security Copilot action, proceed to fill in the following information.

    ![Submit a Copilot promptbook](media/clientslogicappconnectorrunpromptbook2.png)
- Promptbook Name (required): Select a promptbook from the dropdown list.
- Promptbook Inputs (required): Inputs are displayed dynamically for promptbooks with input fields. Enter the specific inputs for each input field.

    Note

    You will need to ensure that required fields, such ash `<SENTINEL_INCIDENT_ID>`, `<THREATACTORNAME>`, or `<DEFENDER_INCIDENT_ID>` are filled in the input fields. Otherwise, the Azure Logic App workflow will not run successfully.
- Session ID (optional): Enter an existing Security Copilot sessionId for maintaining continuity in your tasks, allowing to ask prompts within the same session. If omitted, Security Copilot will create a new session.