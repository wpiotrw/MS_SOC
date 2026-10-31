---
layout: Conceptual
title: Get started with the Microsoft Purview Posture Agent | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: tracyp
author: MSFTTracyP
manager: laurawi
ms.date: 2026-06-23T00:00:00.0000000Z
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
description: Learn how to enable, configure, and monitor Microsoft Purview Posture Agent in Microsoft Purview solutions for enhanced compliance and protection.
locale: en-us
document_id: fad87f86-5f05-7a95-dd4e-3db92df370c9
document_version_independent_id: fad87f86-5f05-7a95-dd4e-3db92df370c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/copilot-in-purview-posture-agent-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-in-purview-posture-agent-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/copilot-in-purview-posture-agent-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 51d08a71-a569-560a-f61e-6e623fd724aa
---

# Get started with the Microsoft Purview Posture Agent | Microsoft Learn

This feature is in preview.

The Microsoft Purview Posture Agent in [Data Security Posture Management](data-security-posture-management-learn-about) uses natural language prompts to help you find sensitive information across your organization. Follow these steps to deploy the Microsoft Purview Posture Agent in the following Microsoft Purview solutions:

- [Data Security Investigations](data-security-investigations)
- [Data Security Posture Management](data-security-posture-management-learn-about)

## Before you begin

If you're new to Microsoft Security Copilot Agent in Microsoft Purview, read this article.

- [Security Copilot Agents in Microsoft Purview Overview](copilot-in-purview-agents-overview)

### SKU/subscriptions and licensing

This agent requires [both the standard per seat licensing model and the pay-as-you-go billing model](purview-billing-models). Your organization must be licensed for:

- Microsoft 365 E5, with security compute units (SCUs) provisioned to use the Microsoft Purview posture agent in Data Security Posture Management.

The agent consumes security compute units (SCUs) as it performs its tasks. You must have SCUs provisioned for the agent to work. The agent consumes SCUs every time it runs based on the complexity of analysis it performs. For more information about SCUs, see [Security compute units (SCUs)](/en-us/copilot/security/get-started-security-copilot#security-compute-units). You can track your SCU consumption in the [usage monitoring tool](/en-us/copilot/security/manage-usage). For more information about onboarding into Microsoft Security Copilot, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).

For information on Security Copilot licensing in E5 see, [Learn about Security Copilot in Microsoft 365 E5](/en-us/copilot/security/security-copilot-inclusion).

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions and Roles

You can enable and deploy the Microsoft Purview Posture Agent in Data Security Posture Management or Data Security Investigations with either an organizational user account or an *agent identity*.

We recommend that you deploy the agent using an *agent identity*. The account used to deploy the agent with an agent identity must have the *Role Management* role. To get started with agent identities, see [Governing Agent Identities (preview)](/en-us/entra/id-governance/agent-id-governance-overview).

If you enable and deploy the agent with your organizational user account, see Permissions for deploying the Posture Agent.

There are different permissions and roles needed to perform different functions with the agent. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions), and [Roles and role groups in the Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/permissions-in-the-security-and-compliance-center).

#### Permissions for deploying the Posture Agent

Use an account that has **the following roles as described** in the table.

| One from Group A | OR Both from Group B | AND One from Group C | - |
| --- | --- | --- | --- |
| - Compliance Admin OR- Security Reader OR Data Security Viewer OR- Data Security AI Viewer OR- Data Security AI Admin | - Purview Content Analyst- Purview Agent Deployment | - Purview Copilot Workspace Contributor |  |

#### Permissions for running and viewing results from the Posture Agent

Use an account that has **the following roles as described** in the table.

| Role Name | Can run Posture Agent and view summary | Can view content snippet that matched intent | Can view file matched intent | Can label file |
| --- | --- | --- | --- | --- |
| Compliance Admin | Yes | No | No | No |
| Security Reader | Yes | No | No | No |
| Data Security Viewer | Yes | No | No | No |
| Data Security AI Viewer | Yes | No | No | No |
| Data Security AI Admin | Yes | No | No | No |
| Data Classification Content Viewer | Yes | Yes | Yes | Yes |
| Data Classification List Viewer | Yes | Yes | No | No |
| Data Security Investigation Reviewer | Yes | Yes | No | No |
| Data Security Investigation Investigator | Yes | Yes | Yes | Yes |
| Data Security Investigation Admin | Yes | Yes | Yes | Yes |
| Purview Content Analyst | Yes | Yes | Yes | Yes |

## Deployment and configuration roadmap

Implementing the Microsoft Purview agents involves several phases:

1. Infrastructure prerequisites
2. Enable the agent
3. Manage the agent configuration
4. Monitor SCU usage

### Infrastructure prerequisites

- Your tenant must be onboarded to Microsoft Security Copilot. For more information on how to onboard, see [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot).
- You must enable Microsoft 365 data sharing in Security Copilot. For more information, see [Accessing data from Microsoft 365 services](/en-us/copilot/security/privacy-data-security#accessing-data-from-microsoft-365-services).
- You must enable the Microsoft Purview plug-in in Microsoft Security Copilot. For more information, see [Enable the Microsoft Purview source in Microsoft Security Copilot](/en-us/purview/copilot-in-purview-overview#enable-the-microsoft-purview-source-in-microsoft-security-copilot).

Important

You can only run two prompts concurrently.

### Enabling the agent

This procedure is for organizations that without the Microsoft Purview Posture Agent for Data Security Posture Management enabled or organizations who removed it and want to enable it again. After you enable the agent, it's available in Microsoft Purview. There can be only one instance of each agent in a tenant.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select the agent to enable, and then select **Add**. A page opens that shows the requirements to enable the agent.
5. Select **Setup**, this action opens the **Deploy agent**global configuration page. You can:
    1. Choose **Create and use agent identity (recommended)** or **Assign and use my identity**.
6. Select **Start**. You see the **Agent is now active** message when the agent is successfully deployed.

### Managing the agent configuration

After the agent is deployed, make minor changes to the agent configuration as needed.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **Go to agent** for the agent you want to manage. This action opens the agent overview page.
5. Select the ellipses (three dots) on the upper right hand corner of the agent overview page, next to the **Edit agent** button. From here you can **Deactivate agent** which makes it inactive, but doesn't uninstall it. If you want to uninstall it, select **Remove agent**.
6. Select **Edit agent** to update **Agent identity** under **Deployment configuration**.

### Deactivate agent

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for the agent you want to pause. This action opens the agent overview page.
5. In the upper-right corner of the agent overview page, select the ellipsis (three dots) next to the **Edit agent** button.
6. Select **Deactivate agent**. Deactivating the agent stops it from functioning. It doesn't remove the agent.

### Remove agent

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for the agent you want to remove. This action opens the agent overview page.
5. On the far right upper right hand corner of the agent overview page, select the ellipses (three dots) that are located *next to* the **Edit agent** button.
6. Select **Remove agent**. Removing the agent deletes it from Microsoft Purview. To use it again, follow Enabling the agent.

### Monitoring SCU usage

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an account that has the required permissions.
2. In the left hand navigation pane, select **Agents**.
3. Select **Explore agents**.
4. Select **View agent** for the agent you want to edit. This action opens the agent overview page.
5. Select the **Performance** tab.
6. Track your SCU consumption in the [usage monitoring tool](/en-us/copilot/security/manage-usage).

In some cases, the Agent downloads and scans max 5 GB or 10K items from the selected data sources. The Agent only returns the top 1,000 matched items.

### Labeling files discovered by the Agent

You can apply sensitivity labels directly to discovered files. This application means the Data Security Posture Agent not only helps you identify sensitive content, but also helps you start protecting it faster without switching to a separate workflow. 

The sensitivity labels available in this feature are the same labels that you define in the Information Protection solution. You can select up to 10 files at a time and apply the same label to all selected files. For supported file types, see [File types supported - Microsoft Information Protection (MIP) SDK | Microsoft Learn](/en-us/information-protection/develop/concept-supported-filetypes). 

**Prerequisites**: 

1. To view the latest status for labels applied to files, make sure auditing is turned on: [https://learn.microsoft.com/en-us/purview/audit-log-enable-disable](/en-us/purview/audit-log-enable-disable)
2. Users with the Data Classification Content Viewer or the Purview Content Analyst role can apply sensitivity labels.

**Steps to apply the label**

1. Select a discovery that includes items on the **Files** tab.
2. Review the items in the list, then select up to 10 files by using the checkboxes.
3. After you select the files, select **Label** to open the list of sensitivity labels available in your organization. you can apply sensitivity labels directly to discovered files.
4. Choose a label.
5. Refresh the page after 30 to 60 minutes to check the labeling status.

### Run Agent on a schedule

Schedule prompts to run automatically on a recurring basis—daily, weekly, or monthly—so you can continuously monitor data risks without manual effort. Instead of rerunning the same investigations, the agent re-executes the prompt on the same prompt and data sources and surfaces updated results based on changes in your data estate. This scheduling helps you stay on top of new or evolving sensitive data over time while building a consistent monitoring workflow.

You can set a schedule for a prompt at the time of or after running a prompt, if the prompt is eligible to be scheduled.

## Run prompts the Agent intelligently suggests

The Agent generates rich insights based on what the Agent observed in your environment. These insights may help you ask the right questions to the Agent and run more targeted prompts. Instead of starting from scratch, you can build on what the agent already found, making investigations feel more relevant.

Each recommendation includes a **suggested prompt** and **pre-selected data source**, so you can launch a discovery directly from the card with a single click. The intent and sources are prefilled, but you can also edit them further.

## Tips and Tricks to write better prompts and get sharper results

Help the Agent understand your intent better. The Agent particularly understands these five search parameters well:

| **Search parameter** | **How it helps** |
| --- | --- |
| Identifiers | Basic filters such as people, titles, file names, file characteristics, time ranges, and sharing status. Example: Emails from john@contoso.com; files modified last seven days; documents with attachments; externally shared items. |
| Sensitive information types (SITs) | Filters for regulated or business-sensitive content using named sensitive information types or their identifiers. Example: Documents containing credit card numbers; emails with passport numbers; files with at least five SSNs and confidence above 85%. |
| Sensitivity labels | Filters based on the sensitivity labels already applied to content. Example: Documents labeled Confidential; items with the Public label. |
| Keywords | Searches for specific words or phrases that appear in the body text of an item. Example: Emails containing the words "merger" and "acquisition". |
| Intent of the file/data asset | Meaning-based search for broader themes or concepts rather than exact keywords. Example: Documents discussing strategies for improving employee retention; communications about frustration with project delays. |

**Example of a prompt that may deliver sharp results**

A single request can combine multiple filter types in one query for sharper results.

**Example:** "PDF documents larger than 1 MB, labeled Confidential, that explain data privacy policies, from the last 90 days."

This prompt contains search parameters Identifiers, Sensitivity labels, Keywords, and Intent of the file/data asset.

**Examples of prompts that may not deliver sharp results**

Sometimes a request is too vague, contradictory, or asks for something the search service doesn't support. In those cases, you see an invalid result with a reason explaining why the request couldn't be interpreted.

| **Prompt** | **Why it may not deliver sharp results** |
| --- | --- |
| "Find stuff", "Sensitive data", "Emails" | Too vague |
| "What’s the weather today?" | Unrelated to search |
| "Files created in 2025 and modified in the last week" | Conflicting time ranges |
| "Emails from the legal team", "messages from the finance team" | Abstract groups instead of concrete people |
| A request that doesn’t yield any keywords, conditions, or topic to search on | Asks for something with no actionable detail at all |