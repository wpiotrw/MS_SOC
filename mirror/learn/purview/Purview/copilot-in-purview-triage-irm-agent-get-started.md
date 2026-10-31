---
layout: Conceptual
title: Get started with the Microsoft Purview Triage Agent in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: Prepare for and deploy the Microsoft Purview triage agent in Insider Risk Management.
ai-usage: ai-assisted
locale: en-us
document_id: a2cfa7a9-6cee-f570-13c1-81947a040da4
document_version_independent_id: a2cfa7a9-6cee-f570-13c1-81947a040da4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-triage-irm-agent-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-triage-irm-agent-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-triage-irm-agent-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: c54dbc93-5289-7fc1-dcca-3b1b9d0a7521
---

# Get started with the Microsoft Purview Triage Agent in Insider Risk Management | Microsoft Learn

Use these steps to deploy the Microsoft Purview triage agent in Microsoft Purview Insider Risk Management. Before you begin, make sure you meet the licensing, permissions, and infrastructure prerequisites described in this article.

## Before you begin

If you're new to Microsoft Purview triage agent in Insider Risk Management, you should read this article.

- [Security Copilot Agents in Microsoft Purview Overview (preview)](copilot-in-purview-agents-overview)

### SKU/subscriptions licensing

The Triage Agent in Insider Risk Management requires both the standard per-seat licensing model and the pay-as-you-go billing model. For more information, see [Purview billing models](purview-billing-models). Your organization must be licensed for:

- Microsoft Purview Insider Risk Management to use the Insider Risk Management triage agent.

Microsoft Purview triage agents consume security compute units (SCUs) as they perform their tasks. You must have SCUs provisioned for the triage agents to work. The number of SCUs consumed depends on the number and type of alerts that are processed. For more information about SCUs, see [Security compute units (SCUs)](/en-us/copilot/security/get-started-security-copilot#security-compute-units). You can track your SCU consumption in the [Security Copilot usage monitoring tool](/en-us/copilot/security/manage-usage). For more information about onboarding into Microsoft Security Copilot, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).

For information on Security Copilot licensing in E5 see, [Learn about Security Copilot in Microsoft 365 E5](/en-us/copilot/security/security-copilot-inclusion)

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions and roles

There are different permissions and roles needed to perform different functions. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions), and [Roles and role groups in the Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/permissions-in-the-security-and-compliance-center).

Assign these roles for setting up the agent using a recommended agent identity, actions like configuring or customizing, or deactivating and removing agents:

For admins (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Role Management | Purview Administrators  Organization Management |
| Insider Risk Management Admin | Compliance Administrator  Insider Risk Management  Insider Risk Management Admins  Organization Management |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples  Organization Management  Compliance Administrator  Security Administrator  Compliance Data Administrator  Insider Risk Management  Insider Risk Management Admins  Insider Risk Management Analysts  Insider Risk Management Investigators |

For analysts (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Insider Risk Management Analysis | Insider Risk Management  Insider Risk Management Analysts |
| Insider Risk Management Investigation | Insider Risk Management  Insider Risk Management Investigators |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Purview Agent Deployment | Included in multiple role groups. Some examples  Compliance Administrator  Data Security Management  Insider Risk Management  Insider Risk Management Analysts  Insider Risk Management Investigators  Purview Agent Management |

**Group C**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples  Organization Management  Compliance Administrator  Security Administrator  Compliance Data Administrator  Insider Risk Management  Insider Risk Management Admins  Insider Risk Management Analysts  Insider Risk Management Investigators |

Important

Agents run in the security context of the last user that saved the agent configuration. This authentication is good for 90 days. After 90 days, the agent will stop running until the configuration is manually saved again.

#### Permissions for viewing triaged Insider Risk Management alerts

The account that you use to view the Insider Risk Management triage agent alert activity must be assigned the roles (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Insider Risk Management Analysis | Insider Risk Management  Insider Risk Management Analysts |
| Insider Risk Management Investigation | Insider Risk Management  Insider Risk Management Investigators |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Purview Agent Analysis | Included in multiple role groups. Some examples  Compliance Administrator  Data Security Management  Insider Risk Management  Insider Risk Management Analysts  Insider Risk Management Investigators |

**Group C**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples  Organization Management  Compliance Administrator  Security Administrator  Compliance Data Administrator  Insider Risk Management  Insider Risk Management Admins  Insider Risk Management Analysts  Insider Risk Management Investigators |

## Deployment and configuration roadmap

Deploying the Microsoft Purview Insider Risk Management triage agent involves these phases:

1. Infrastructure prerequisites
2. Enabling agents
3. Set up agents
4. Deactivate agents
5. Remove agents

### Infrastructure prerequisites

Microsoft Purview triage agents run on Microsoft Security Copilot.

1. Your tenant must be onboarded to Microsoft Security Copilot. For more information on how to onboard, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).
2. You must enable Microsoft 365 data sharing in Security Copilot. For more information, see [Accessing data from Microsoft 365 services](/en-us/copilot/security/privacy-data-security#accessing-data-from-microsoft-365-services).
3. You must enable the Microsoft Purview plug-in in Microsoft Security Copilot. For more information, see [Enable the Microsoft Purview source in Microsoft Security Copilot](/en-us/purview/copilot-in-purview-overview#enable-the-microsoft-purview-source-in-microsoft-security-copilot).

### Enabling agents

This procedure is for organizations that haven't enabled any of the Microsoft Purview agents or have previously removed the agents and want to enable them again. Once you enable the agents, they're available for use in Microsoft Purview. There can be only one instance of each agent in a tenant. This procedure works for both the Purview DLP triage agent and the Insider Risk Management triage agent.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select the agent that you want to enable and select **Add**. This opens a page that shows the requirements to enable the agent.
5. Select **Setup**, this opens the **Deploy agent**global configuration page. You can:
    1. Choose to **Run automatically based on a set schedule**. If you don't choose this option, you must run the agent manually one at a time. The scheduled is set by Microsoft and isn't configurable by organizations. You can change this setting later when you edit the agent.
    2. **Select the alert timeframe**, which is how far back the agent looks for alerts to triage. Analysts can shorten the timeframe when they edit the agent but not lengthen it. For more information, see [Select Alert timeframe](copilot-in-purview-agents-overview#select-alert-timeframe).
6. Select **Deploy**. You see the *Alert Triage Agent in &lt;solution&gt; is deployed* message when the agent is successfully deployed.

### Set up agents

Once an agent is enabled, you need to set specific triggers for the agent. The triggers are used to determine which alerts the agent triages. You can do this either in the **Agents** page or, for first run experience on the **Alerts** page for the solution. For this procedure, we'll use the first run experience **Alerts** page method. This procedure assumes that you still have the Microsoft Purview portal open to the **Explore agents** page from the Enabling agents procedure.

Important

The most recent agent configuration is always used.

1. Select **Go to &lt;solution&gt;**. This opens the **Alerts** page for the solution.
2. Because you are in the first run experience, you see dialog box that with a **Customize** button which, when selected, opens the **Customize Alert Triage Agent** flyout.
3. Here, choose either to accept the default global setting for **Select alert timeframe** or change it to be shorter than what was configured during agent deployment.
4. Enter [custom instructions](copilot-in-purview-agents-overview#custom-instructions) for the agent. The agent interprets your natural language input and uses it to better identifyw hich types of alerts matter most to you. This helps you identify and respond faster to the most relevant alerts.
5. Choose **Select policies** to select the policies whose alerts will be triaged by the agent. In preview, all policies are selected by default, you can change that here.
6. Select **Review**.
7. Select **Start agent**. Allow up to 2 hours for the agent to complete triaging the in scope alerts and enabled manual runs from this initial setup.

### Deactivate agents

Use the following steps to deactivate an agent without removing it.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for the agent you want to deactivate. This opens the agent overview page.
5. On the far right upper right hand corner of the agent overview page, select the ellipses (three dots) that are located *next to* the **Edit agent** button.
6. Select **Deactivate agent**.

Deactivating the agent stops it from triaging alerts. It doesn't remove the agent and it doesn't reset the **Select alert timeframe** reference point in time.

### Remove agents

Use the following steps to permanently remove an agent from Microsoft Purview.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for the agent you want to pause. This opens the agent overview page.
5. On the far right upper right hand corner of the agent overview page, select the ellipses (three dots) that are located *next to* the **Edit agent** button.
6. Select **Remove agent**.

    Warning

    Removing the agent deletes it from Microsoft Purview and resets the **Select Alert timeframe** reference point in time. If you want to use the agent again, you must re-enable and set it up again.

### Edit agents

Use the following steps to edit an existing agent's configuration and triggers.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for agent you want to edit. This opens the agent overview page.
5. Select **Edit agent**. This opens the **Edit agent** page.
6. Select **Triggers**.
7. Here you can change when the agent runs, either **Agent will run manually on one alert at a time** or **Agent will run automatically based on a set schedule**.
8. Select **Edit** to change the **Select alert timeframe** value and the policies that the agent will triage alerts from.
9. If you select **Agent will run manually on one alert at a time**, you can select a single alert in the **Alerts** page for the solution. Set the toggle to **Alert Triage Agent** and select **Run Agent**.
10. You can also change the **Intent** if you want.

### Monitoring SCU usage

Use the following steps to view security compute unit (SCU) usage for an agent.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for agent you want to edit. This opens the agent overview page.
5. Select **Edit agent**. This opens the **Edit agent** page.
6. Select **Usage monitoring**.
7. You can track your SCU consumption in the [Security Copilot usage monitoring tool](/en-us/copilot/security/manage-usage).

### Alerts page overview

Use the following steps to open the Alerts page and view alerts triaged by the agent.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required Purview agent permissions.
2. Open the solution you want to view the triaged alerts for.
3. Open the **Alerts** page for the solution.
4. In the top right hand area of the page, there's a new toggle that lets you choose between the **Standard** view of the alerts page and a **Triage Agent** view of the alerts page. Set the toggle to the **Triage Agent**view. This view shows the alerts that have been triaged by the agent. The alerts are grouped by the agent into four categories:
    - **All**
    - **Needs attention**
    - **Less Urgent**
    - **Not categorized**