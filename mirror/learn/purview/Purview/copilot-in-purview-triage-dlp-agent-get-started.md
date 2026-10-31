---
layout: Conceptual
title: Get started with the Microsoft Purview Triage Agent in Data Loss Prevention | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: tracyp
author: MSFTTracyP
manager: laurawi
ms.date: 2026-06-25T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Prepare for and deploy the Microsoft Purview triage agent in Microsoft Purview Data Loss Prevention.
locale: en-us
document_id: 6838720c-2ccd-ea0a-2c34-bd93547374f0
document_version_independent_id: 6838720c-2ccd-ea0a-2c34-bd93547374f0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-triage-dlp-agent-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-triage-dlp-agent-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-triage-dlp-agent-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 01fdf031-9d02-e2fd-e166-a9669af3f6bf
---

# Get started with the Microsoft Purview Triage Agent in Data Loss Prevention | Microsoft Learn

Use these steps to deploy the Microsoft Purview triage agent in Data Loss Prevention (DLP) in both the Microsoft Purview and Microsoft Defender XDR portals.

The Microsoft Purview Triage Agent in DLP triages alerts from policies that are scoped to Exchange, Teams, OneDrive, SharePoint, and devices (Endpoint) locations, *only*. If you want to triage alerts from devices, [Evidence collection for file activities on devices](dlp-copy-matched-items-learn) must be enabled.

## Before you begin

If you're new to Microsoft Security Copilot Agent in Microsoft, read this article.

- [Security Copilot agents in Microsoft Purview overview](copilot-in-purview-agents-overview)

### Subscriptions and licensing

This agent requires [both the standard per seat licensing model and the pay-as-you-go billing model](purview-billing-models). Your organization must be licensed for:

- Microsoft Data Loss Prevention (DLP) to use the DLP triage agent.

The agent consumes security compute units (SCUs) as it performs its tasks. You must have SCUs provisioned for the triage agent to work. The number of SCUs consumed depends on the number and type of alerts that are processed. For more information about SCUs, see [Security compute units (SCUs)](/en-us/copilot/security/get-started-security-copilot#security-compute-units). You can track your SCU consumption in the [usage monitoring tool](/en-us/copilot/security/manage-usage). For more information about onboarding into Microsoft Security Copilot, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).

For information on Security Copilot licensing in E5 see, [Learn about Security Copilot in Microsoft 365 E5](/en-us/copilot/security/security-copilot-inclusion).

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions and Roles

There are different permissions and roles needed to perform different functions with the agent. For more information, Permissions and roles needed are specific to the agent's various functions. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions), and [Roles and role groups in the Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/permissions-in-the-security-and-compliance-center).

Important

An agent now has its own agent identity (read more: [https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id-platform](/en-us/entra/agent-id/identity-platform/what-is-agent-id-platform)) or can be set up by assigning the user's identity who is setting the agent. These settings can be changed anytime by visiting the deployment configurations tab for the agent in Explore agents page. Regarding an agent that that was set up using a user's identity, migration to the agent identity in agent settings is recommended.

#### Permissions for enabling and configuring the Triage Agent in DLP from Microsoft Purview and Defender XDR portals

Assign these roles for setting up the agent using an recommended agent identity, actions like configuring or customizing, or deactivating and removing agents:

For admins (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Role Management | Microsoft Purview Administrators  Organization Management |
| DLP Compliance Management | Compliance Administrator  Compliance Data Administrator  Organization Management  Security Administrator |
| Information Protection Admin | Compliance Administrator  Compliance Data Administrator  Information Protection  Information Protection Admins |
| Data security AI admin | Data Security AI admins |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples are  Organization Management  Compliance administrator  Security Administrator  Compliance Data Administrator  Information Protection  Information Protection Admins  Information Protection Analysts  Information Protection Investigators |

For analysts (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Information Protection Analyst | Compliance Administrator  Compliance Data Administrator  Information Protection  Information Protection Analysts  Information Protection Investigators |
| Information Protection Investigator | Information Protection  Information Protection Investigators |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Purview Agent Deployment | Included in multiple role groups. Some examples include  Compliance Administrator  Data Security Management  Information Protection |
| Information Protection Analysts | Information Protection Investigators  Purview Agent Management |

**Group C**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples include:  Organization Management  Compliance administrator  Security Administrator  Compliance Data Administrator  Information Protection  Information Protection Admins  Information Protection Analysts  Information Protection Investigators |

See [Microsoft Entra Agent ID documentation | Microsoft Learn](/en-us/entra/agent-id/) for more on agent identity.

Wait for 30-min post setting the agent with agent identity for the roles based access to get reflected before initiating any manual run on an alert.

Important

After setup is complete, the agent starts running within 30–60 minutes and begins triaging DLP alerts. By default, the agent processes alerts from all DLP policies generated within the past 30 days. You can modify this behavior at any time by updating the agent’s settings.

#### Roles assigned to the agent

These roles are assigned to the Triage agent in DLP when agent identity is used:

- Information Protection Analyst
- Purview content Analyst
- Data classification content viewer (needed to get the contextual summary)
- Data classification content downloader (needed for endpoint scenario)
- Purview Copilot Workspace Contributor
- Security Copilot Contributor

Important

The agent starts running within 30–60 minutes after setup is complete, and begins triaging DLP alerts. By default, the agent processes alerts from all DLP policies generated in the past 30 days. You can modify this behavior at any time by updating the agent’s settings.

#### Permissions for viewing alert results in Purview and Defender XDR and managing Microsoft Purview Triage Agent for DLP

The account you use to view results along with update triggers, give feedback, or custom instruction for the Triage Agent in DLP must be assigned the roles (any one from each group):

**Group A**

| Role | Role Groups containing the role |
| --- | --- |
| Information Protection Analyst | Compliance Administrator  Compliance Data Administrator  Information Protection  Information Protection Analysts  Information Protection Investigators |
| Information Protection Investigator | Information Protection  Information Protection Investigators |
| Manage Alerts | Compliance Administrator  Compliance Data Administrator  Organization Management  Security Administrator  Security Operator |
| View-Only Manage alerts | Compliance Administrator  Compliance Data Administrator Global Reader  Organization Management  Security Administrator  Security Operator  Security Reader |

**Group B**

| Role | Role Groups containing the role |
| --- | --- |
| Purview Agent Analysis | Included in multiple role groups. Some examples  Compliance administrator  Data Security Management  Information Protection  Information Protection Analysts  Information Protection Investigators |

**Group C**

| Role | Role Groups containing the role |
| --- | --- |
| Security Copilot Contributor | (Managed in Security Copilot) |
| Purview Copilot Workspace Contributor | Included in multiple role groups. Some examples  Organization Management  Compliance administrator  Security Administrator  Compliance Data Administrator  Information Protection  Information Protection Admins  Information Protection Analysts  Information Protection Investigators |

## Deployment and configuration roadmap

Implementing Microsoft Purview agents involves several phases:

1. Infrastructure prerequisites for agents
2. Enable agents
3. Edit agents
4. Deactivate agents
5. Remove agents

### Infrastructure prerequisites

Microsoft Purview triage agent in DLP runs on Microsoft Security Copilot.

- Your tenant must be onboarded to Microsoft Security Copilot. For more information on how to onboard, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).
- You must enable Microsoft 365 data sharing in Security Copilot. For more information, see [Accessing data from Microsoft 365 services](/en-us/copilot/security/privacy-data-security#accessing-data-from-microsoft-365-services).
- You must enable the Microsoft Purview plug-in in Microsoft Security Copilot. For more information, see [Enable the Microsoft Purview source in Microsoft Security Copilot](/en-us/purview/copilot-in-purview-overview#enable-the-microsoft-purview-source-in-microsoft-security-copilot).
- To use the Remediation Capability of the Triage Agent in Data Loss Prevention, you must configure the Microsoft Teams Admin Center to allow the Data Security Triage Agent app to send messages to users. For detailed configuration steps, see [Configure Microsoft Teams for the Data Security Triage Agent remediation messages](copilot-in-purview-triage-dlp-agent-teams-config).

### Enable the agent

This procedure is for organizations that didn't enable any of the Microsoft Purview agents or removed agents and want to enable them again. Once you enable the Microsoft Purview Triage Agent in Data Loss Prevention, they're available for use in Microsoft Purview and Microsoft Defender XDR.

Note

There can be only one instance of each agent in a tenant, regardless of the portal in which it was deployed.

This process works for the Triage Agent in Microsoft Purview.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. On the card for the Triage agent in Data Loss Prevention, select **View Details** to open a page that shows the details about the agent.
5. Select **Setup** to open the **Deploy agent** global configuration page. You can:

    1. Choose to **Run automatically based on a set schedule**. If you don't choose this option, you must run the agent manually one at a time. Microsoft sets the schedule and it isn't configurable by organizations. You can change this setting later when you edit the agent.
    2. Select the **alert timeframe**, which is how far back the agent looks for alerts to triage. Analysts can shorten the timeframe when they edit the agent but not lengthen it. For more information, see [Select Alert timeframe](copilot-in-purview-agents-overview#select-alert-timeframe).
    3. Enable **Remediation reminders in Microsoft Teams**. For Sharepoint/OneDrive alerts triaged as Needs Attention, the agent sends a Microsoft Teams chat to the last modified user of the file, and ask them to remove the sensitive information found in the file related to the alert. (Preview)
    4. Select **Reminder duration**, which is the number of days the agent sends the reminders on Microsoft Teams for a particular file requiring action from last modified user. (Preview)
6. The agent is assigned **Agent Identity**, which allows it to access data and take actions
7. Select **Start**. You see the *Triage Agent in &lt;solution&gt; is active* message when the agent is successfully deployed.

This process works for the Triage Agent in Defender XDR.

Important

The Triage Agent can be deployed from both Microsoft Purview and Defender XDR portals, but can only be managed, edited, and disabled from the Microsoft Purview portal. After deployment from either portal, Agent summaries and outputs can be viewed in both the Microsoft Purview and Defender XDR portals.

1. Sign in to the Microsoft Defender XDR portal with an account that has the required permissions.
2. In the left hand navigation pane, select "Investigation & response" then select "Incidents & alerts" and then select "Alerts".
3. Click into any DLP alert the alert queue.
4. If you don't have the Triage Agent deployed, you will find a banner inside a DLP alert suggesting you deploy it.

    1. Click on "Get started" to start the agent with default settings.
    2. Click on "Learn more" to understand more about the configuration options available to you.
    3. Finish deploying the Agent

#### Deploy from the Defender XDR Security Store

You can also deploy the Data Security Triage Agent from the Security Copilot Security Store in the Defender XDR portal.

Important

The Triage Agent can be deployed from both Microsoft Purview and Defender XDR portals, but can only be managed, edited, and disabled from the Microsoft Purview portal. After deployment from either portal, agent summaries and outputs can be viewed in both portals.

1. Sign in to the [Microsoft Defender XDR portal](https://security.microsoft.com) with an account that has the required permissions.
2. Select **Security Copilot** &gt; **Security Store**.
3. Search for or browse to the **Triage Agent in Data Loss Prevention** card.
4. Select the agent card, then select **Get agent** to begin deployment.
5. After purchase, select **Security Copilot** &gt; **Agents**, find the agent in the **Ready for setup** section, and select **Set up**.
6. Choose whether to run automatically or manually, set the alert timeframe, and optionally enable remediation reminders in Microsoft Teams. For more information on these settings, see Triggers and settings.
7. Select **Start**. The agent begins triaging DLP alerts within 30–60 minutes.

### 'One-Click' deployment and enabling the agent

A quick setup flow with default triggers was introduced. Any admin or analyst for a tenant (with no agent deployed) sees a banner or card on alerts page for Triage agent setup. Select **Start agent** to deploy and enable the agent. The roles needed for this setup align with the roles mentioned previously for normal setup flow.

The default settings for 'One-Click' setup are:

- Identity: Create and use agent identity
- Trigger: Run automatically based on a set schedule
- Alert timeframe: Triage alerts from the last 30 days
- Remediation reminder: Turned OFF (Preview)
- Policy scope: All policies in scope for triage.

These settings can be customized during 'One-Click' setup by selecting the Customize option.

### Edit agent

Once an agent is enabled, it's ready to triage alerts. Edit and set specific triggers for the agent to act upon. These triggers are used to determine which alerts the agent will triage.

Select which triggers are used on either the **Agents** page or, for first run experience, on the **Alerts** page for the solution. Select the **Agent details** button on the top right on alerts page or:

1. In the Microsoft Purview navigation pane (left hand side of the screen), select **Agents**.
2. Select **Explore agents**.
3. Select **Go to agent** for agent you want to edit.
4. Select **Edit agent**.
5. Select **Agent configuration** for editing and configuring settings like Trigger, alert timeframe, remediation reminders, reminder duration, and policy scope.
6. Go to **Agent Custom Instruction** for editing and configuring the customized instruction on how the agent should work in your tenant.
7. Select **Save**

Important

The most recent agent configuration is always used. Agent settings can only be edited from the Microsoft Purview portal even if it was deployed from the Defender XDR portal.

Allow up to 2 hours for the agent to complete triaging in-scope alerts and enabled manual runs after this initial setup.

### Deactivate agents

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **Go to agent** for the agent you want to deactivate.
5. On the far right upper right hand corner of the agent overview page, select the ellipses (three dots) that are located *next to* the **Edit agent** button.
6. Select **Deactivate agent**. Deactivating the agent stops the agent from triaging alerts. It doesn't remove the agent and it doesn't reset the **Select alert timeframe** reference point in time.

Important

Agent can only be deactivated from the Microsoft Purview portal even if it was deployed from the Defender XDR portal.

### Remove agents

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **Go to agent** for the agent you want to remove.
5. On the far right upper right hand corner of the agent overview page, select the ellipses (three dots) that are located *next to* the **Edit agent** button.
6. Select **Remove agent**. Removing the agent deletes it from Microsoft Purview. If you want to use it again you must go through the Enable the Agents, and Edit agents procedures again.

Important

Agent can only be removed from the Microsoft Purview portal even if it was deployed from the Defender XDR portal.

## Triggers and settings

Triggers are groupings of parameters whose values must be met in order for the agent to triage any given alert. Triggers include:

### Run automatically or manually

Once an agent is deployed, and triggers are edited, select whether the agent runs **automatically based on a set schedule** or the **Agent runs manually on one alert at a time** . If you select **Run automatically based on a set schedule**, the agent triages the alerts that are included in the **Select Alert timeframe** setting.

### Select alert timeframe

Choose an alert timeframe. The options are:

- Only triage new alerts
- Last 24 hours
- Last 48 hours
- Last 72 hours
- Last 7 days
- Last 14 days
- Last 21 days
- Last 30 days

If **Only triage new alerts** is selected, the agent only triages alerts that are generated after the agent is deployed. The agent won't triage any alerts that were generated before the agent was deployed, which means that all the *Last # hours or days* options are ignored.

If any of the *Last # hours or days* options are selected, the agent triages alerts that were generated in the selected timeframe. This selection triages all alerts generated before the agent was deployed. All newly generated alerts are also triaged.

### Remediation reminder (Preview)

The Remediation Capability extends the effectiveness of the Alert Triage Agent in Data Loss Prevention by reaching out to the user who violated DLP Policies--by including sensitive data in SharePoint and OneDrive files, for example--via Microsoft Teams. This is applicable only for the alerts categorized as "Needs Attention".

Enabling this setting also enables the bot in Microsoft Teams for the tenant. Reminders are sent once daily to the user who is last modifier of the file in context (combining up to 10 files if multiple files require remediation).

The remediation message includes the file name and a description of what sensitive information requires attention. Once the last person who modified, remediates the file, the file is removed from the remediation reminder for the next day. If no files are found, no reminder is sent.

Important

If your organization's settings for Microsoft Teams do not allow the deployment of new Microsoft Teams apps, the Remediation reminders will not be sent to users in your organization. For configuration steps, see [Configure Microsoft Teams for the Data Security Triage Agent remediation messages](copilot-in-purview-triage-dlp-agent-teams-config).

### Reminder duration (Preview)

The reminder duration reports the number of days the Agent should follow up with the user on files that aren't remediated.

### Policy Scope

A DLP policy must meet certain criteria for it to appear in the **Specify Policy Scope** list and be eligible to be included triage.

Specify the policy scope of the triage agent to control which DLP policy alerts and which policies are eligible for remediation reminders. Remediation reminders must be enabled, and eligible policies must be a subset of the policies defined for agent triage.

##### Full eligibility

A policy is fully *eligible* for inclusion if the DLP Alert Triage Agent supports all the conditions in the policy. All alerts from a fully eligible policy are triaged.

##### Limited eligibility

If a policy has some unsupported conditions--a state called *limited eligibility*--the Microsoft Purview DLP triage agent might not be able to triage all the alerts from that policy. Based on the criteria listed some alerts from the policy won't be triaged in limited eligibility. The reason for policy showing as *limited* can be seen by selecting **Limited** state in the **Specify Policy Scope** picker.

Here are some reasons why a policy can be in a limited eligibility state:

- [Get started with collecting files that match data loss prevention policies from devices](dlp-copy-matched-items-get-started) isn't enabled or the storage associated with it isn't Microsoft storage. Also the File collection setting in policy rule is turned OFF for policies targeting endpoint or devices workload.
- The policy doesn't include one of these workloads: SharePoint, OneDrive, Exchange, Teams, and devices (Endpoint).

The same eligibility status is shown on the DLP policy list page. The eligibility column appears when the DLP Triage Agent is enabled and set up. Once the policies are included in agent scope, only future alerts are checked for scoped policies. Existing triaged alerts, or alerts that have already been generated, aren't impacted.

### Custom instructions (Preview)

During the agent config process, you can give the agent *custom instructions*. Custom instructions only apply to the Triage agent in DLP. Microsoft Purview agents use these natural language instructions to enhance alert triage by:

- Translating your input into structured classification logic.
- Running this logic against the alert content associated with each alert.
- Raising or lowering the alert’s priority if the content matches your custom instruction.

For custom instructions, the agent now supports both content, and metadata-based instruction, such as:

- Focus on alerts related to tax, financial, or legal information from last seven days
- Don't focus on alerts containing credit card numbers, social security numbers, and names of users like Mary@contoso.com
- Deprioritize alerts where the related assets have .pdf or .jpg files

Users can also use provided templates when unsure how to provide instruction. These templates are:

- *Generic instruction*: Helps define the clear classifiers targeted, or prioritized conditions versus those classifiers that aren’t prioritized. Separate complex conditions to avoid agent generating complex inferences.
- *Focus on*: Helps define clear conditions to prioritize. Other conditions are marked as Less Urgent.
- *Reduce overload*: Helps define conditions to deprioritize.
- *Definitions*: Defines definitions for classifiers for the agent's understanding.

#### Edit custom instructions

- The user can add multiple templates to the instruction as required. In other words, they can select a generic instruction and add all needed details or remove whatever isn't required. However, they can also add these templates on demand and enter definitions, then add a couple of *Reduce overload conditions*.
- The user can add more than one condition by clicking on multiple templates, or add separate lines after single template select.
- They can also add conditions in any order and repeat conditions if necessary. For example, the user can add template for definition, then add a *Focus on*, a *Reduce overload*, a *Focus on*, and any needed *Definitions*. Compounding these conditions is like adding things to a cart by selecting and removing the items as required and in any sequence.
- The existing text in the input box isn't removed or replaced when a template is selected. The template-based text is always appended to existing text.
- Users can always edit the input box even with the template as required. They can remove the complete template-provided input or make changes.

On review, the agent combines all instances and presents agentic understanding for confirmation. The output is shown in three segments:

- *Classifiers identified from instructions*: Shows list of classifiers the agent identifies from the instruction.
- *Agent-inferred instructions*: Agent interpretation converts user-provided natural language instruction. Users can deselect any instruction they don't want.
- *Unsupported instructions*: Highlights the instruction if any part of the instruction isn't supported. Users can edit the custom instruction at any time and review it again to remove any unsupported conditions.

Once the instruction is saved, the agent uses it to triage all future alerts. If an alert matches the instruction, a separate summary is generated. The agent also highlights the custom-instruction–matched classifiers for each related document associated with the alert.

### Monitor SCU usage

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for agent you want to edit.
5. Select **Edit agent**.
6. Select **Usage monitoring**.
7. You can track your SCU consumption in the [usage monitoring tool](/en-us/copilot/security/manage-usage).

### Microsoft Purview Alerts page overview

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. Open the solution you want to view the triaged alerts for.
3. Open the **Alerts** page for the solution.
4. In the top right hand area of the page, there's a new toggle that lets you choose between the **Standard** view of the alerts page and a **Triage Agent** view of the alerts page. Set the toggle to the **Triage Agent** view. This view shows agent triaged alerts. The agent groups alerts into four categories:

- **All**
- **Needs attention**
- **Less urgent**
- **Not categorized**

### Defender XDR Alert queue

1. Sign in to the Microsoft Defender XDR portal with an account that has the required permissions.
2. In the left hand navigation pane, select "Investigation & response" then select "Incidents & alerts" and then select "Alerts".
3. Agent-provided summaries and risk factors will be available on DLP alerts triaged by the Agent as they are in Microsoft Purview.

### Triaged alerts

The agent triages alerts generated in the timeframe and using policies you selected. Not all alerts are triaged. Triaged alerts are available to review in both the Microsoft Purview and Defender XDR portals.

Triaged alerts in Microsoft Purview are grouped into four categories:

1. **All**: This category includes all the alerts that the agent triaged. The count indicated in the category might not accurately reflect the true number of alerts until you go into that view and scroll down to load all the alerts. If the conditions that caused the alert to be raised in the first place changed, or if the alert isn't triaged yet, you can select the alert and then select **Run agent** to manually run the agent on the alert.
2. **Needs attention**: This category contains alerts that the agent evaluated and determined pose the greatest risk to your organization. When you select one of these alerts, the details flyout opens to show a summary of the alert and other details.
3. **Less Urgent**: These less urgent results are the alerts the agent evaluated and determined to pose a lower risk to your organization. When you select one of these alerts, the details flyout opens to show a summary of the alert and other details.
4. **Not categorized**: Uncategorized results are the alerts that the agent wasn't able to successfully triage, which can happen for many reasons, including:

- Server error
- In process of reviewing
- other error
- Unsupported error for alerts that contain activities that the agent doesn't support.

Agents triage files up to 2 MB in size.

### How agents prioritize

The Triage Agent in DLP prioritizes alerts based these risk factors:

- *Content Risk*: This category is the primary risk factor used during agent triage, it covers sensitive content based on Microsoft provided sensitive information types (SIT), trainable classifiers, and default sensitivity labels. For more information, see [default sensitivity labels](default-sensitivity-labels-policies).
- *Exfiltration Risk*: Exfiltration of sensitive data shared externally.
- *Policy Risk*: Policy mode and rules with actions affect the prioritization of alerts.
- *Content Risk*: Label removed or downgraded.

Additionally, any custom instruction or feedback is applied for the final verdict categorization.

### Alert Triage details

Important

The Triage agent in DLP only supports alerts from policies that are in active mode. It doesn't triage alerts from DLP policies that are running in simulation mode.

Agents can review alerts that were generated up to 30 days before enablement if the tenant has sufficient SCUs. Alerts that were generated more than 30 days before agent enablement are out of scope.

The Triage agent in DLP triages alerts from Exchange, Devices, SharePoint, OneDrive, Teams. To triage alerts from Devices, you must enable [evidence collection for file activities on devices](dlp-copy-matched-items-learn).

Do manual analysis on alerts not evaluated by an agent.

### Content Analysis

There are some situations where content analysis can be limited.

The content risk prioritization of an alert is based on Sensitive Information Types (SITs), trainable classifiers, and sensitivity labels in content. When an agent evaluates content risk, it only looks for SITs, and trainable classifiers that are defined in the policy.

When a DLP alert is associated with fewer than 10 files, the agent scans all the files and uses them to generate the content summary. When an alert includes 10 or more files, the agent uses the potentially top 10 files to generate the file risk summary. In DLP, the triage agent selects the top 10 risky files based on the number of policy classifier hits, the file size, and the most recent file access time. Once this selection is done, the triage agent adds a note stating that the content summary doesn't include all the files in the alert.

### Remediation capability within alert view (Preview)

There are two ways to view the agent's remediation progress.

You can view remediation status at the alert level on the Triage Agent alert queue in the DLP solution. This view lets a user see fully remediated alerts, meaning users remediated all files implicated in the alert. *In progress* means that the Agent reached out to the user, but the user didn't remediate all the files yet. *Error* indicates that the Teams message couldn't be sent.

Use the second view to see files in a DLP alert that are remediated. You can see the status inside each DLP alert in the *Related assets* section that lists all the files implicated in the alert and the respective remediation status. *Remediated* indicates that the user remediated all detected SITs in the file. If the user remediated some or none of the SITs, the status indicates *In progress*.

Note

The Remediation Capability doesn't cost anything extra. The only costs associated with using this capability are the SCUs needed to triage the DLP alert first.

### Feedback for alerts triaged

Important

You can only provide feedback on alerts in that are in the **Needs attention** or **Less urgent** categories. If you disagree with the agent's initial categorization of an alert, you can use the feedback mechanism to revise the categorization. If the initial value is **Needs attention**, you can change it to **Less urgent**. If the initial categorization is **Less urgent**, you can reprioritize it as **Needs attention**.

You can also add properties, such as a **Sensitive info type** or a **File path** that the agent should use in future evaluations to improve performance. These properties are supported in preview.

- **User email address**: the user who performed the activity that triggered the alert
- **External recipient email address**: to track alerts triggered by Exchange email or Teams interactions with external recipients
- **Sensitive information type**: shows all the SITs within the subscription, the SITs involved in the policy rule triggering the alert are preselected
- **Trainable classifier**: shows all trainable classifiers, the trainable classifiers that are involved in the policy rule triggering the alert are preselected
- **Sensitivity label**: The labels present in the subscription
- **File path**: in case the alert is related to a file and the file path is available. The file path isn't enabled for Endpoint DLP (device) alerts but Full file evidence wasn't enabled at the time of alert triaging
- **Target domain**: for endpoint devices DLP alerts where target domain is present

1. Select any **Needs attention**, or **Less urgent** alert. The selection opens a flyout with the agent provided summary and other settings.
2. Select **Agent feedback**.
3. The **Revise to** field shows the value of the recategorization.
4. Select **+ Add property** and add one or more properties. The added properties are used to improve triaging performance.
5. If you want to **Apply the feedback to all policies**, select that option. Otherwise, the feedback is applied only to the policy that triggered the alert.
6. Select **Review** to see a summary of the changes.
7. Select **Submit** to save the feedback.
8. The current alert doesn't change immediately. Admin has to manually run a triage pass on the alert to change the categorization based on the feedback provided.

#### Managing feedback

You can view and manage all the feedback given for a triaged alert, including exporting, editing, and deleting feedback.

1. In the solution for the alert, open the **Alerts** page.
2. Select the **Needs attention** or **Less urgent** category.
3. Select the alert that you want to manage the feedback for.
4. Select **Agent feedback**.
5. Select **View all feedback**.
6. Select the alert and feedback entry that you want to manage.
7. **Edit**, **Delete**, or **Export** the feedback as needed.

#### Feedback conflict resolution

Feedback conflict can occur when multiple admins provide conflicting feedback for the same user and policy combination on different alerts. Feedback conflict generates an error.

For example:

- Admin 1 provides feedback to change *all* alert's categorization to **Less urgent** if the alert is for User A and Policy P.
- Admin 2 provides feedback to change *an* alert's categorization to **Needs attention** if the alert is for User A and Policy P.

## Other considerations

- For the alert count, only the alerts where single instance of match is enabled are counted. In case an alert is generated for a threshold scenario--for example, generate alert if there are 10 matches in last 24 hours--those alerts aren't counted.