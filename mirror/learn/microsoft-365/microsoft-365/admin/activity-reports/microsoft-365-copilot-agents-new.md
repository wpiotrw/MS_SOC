---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Copilot Agents Usage Report (Preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-agents-new?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: nesanghi
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
- magic-ai-copilot
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Copilot Agents usage report provides detailed analytics on agent usage, user engagement, and performance. Discover how to optimize your organization.
ms.date: 2026-07-28T00:00:00.0000000Z
locale: en-us
document_id: 21b993b4-df64-c684-63d5-559126c102f1
document_version_independent_id: 21b993b4-df64-c684-63d5-559126c102f1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-365-copilot-agents-new.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-365-copilot-agents-new
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-365-copilot-agents-new.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: eb14263a-02b8-dd54-f5e1-a59b6ec36a0e
---

# Microsoft Copilot Agents Usage Report (Preview) - Microsoft 365 admin | Microsoft Learn

The Microsoft Copilot Agent usage report helps you track how agents are used in Microsoft Copilot Chat and Microsoft 365 apps - Word, Excel, and PowerPoint. You can see which agents both licensed and unlicensed Microsoft Copilot users use across Declarative, SharePoint, and Custom engine agents. These agents include agents built by your organization, Microsoft, and Third-party.

You can view usage within an hour from when users interact with agents. The report includes key metrics such as:

- Total active users and agents
- Summary and daily time series
- Active usage per user, per agent, and per agent-user pair

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Copilot Agents usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Copilot**, and then select **Agents**.

## Interpret the Microsoft Copilot Agents usage report

Use the Agents usage report to see the usage of agents in your organization that your organization, Microsoft, or Third-party built. These agents include agents that an admin approves, and agents that users create through agent builder and share with users in your organization. Admins can manage agents in the same way as they manage any other app by using Copilot controls in the Microsoft 365 admin center. For more information, see [Manage agents for Microsoft Copilot in the Microsoft 365 admin center](/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps).

At the top of the report, you can filter by different periods. You can view the agent report over the last 7 or 30 days.

[![Screenshot of Microsoft Copilot agent usage metrics dashboard showing filtering options and summary statistics.](../../media/agent-filters-and-metrics.png)](../../media/agent-filters-and-metrics.png#lightbox)

- **Total active users** shows how many unique users in your organization - whether they have a Microsoft Copilot license or not - used agents in Microsoft Copilot Chat during the selected time period. This count includes agents created by your organization, Microsoft, or Third-party.
- **Active users (licensed)** shows how many unique users in your organization who had a Microsoft Copilot license used agents in Microsoft Copilot Chat during the selected time period.
- **Active users (unlicensed)** shows how many unique users in your organization, who didn't have a Microsoft Copilot license and used agents in Microsoft Copilot Chat during the selected time period.
- **Total active agents** shows how many unique apps with an agent element in that app with at least one active user over the selected time period. This count includes agents created by your organization, including agents both admin approved and shared by users in your organization, Microsoft built agents, and agents built by Third-party.

An active user of an agent is a user who asks an agent a question and receives a response. Users interact with agents in the following ways:

- By selecting the agent from the side panel in Microsoft Copilot Chat and at-mentioning the agent in the chat experience.
- By selecting the **Open navigation panel** button in the top corner of Microsoft Copilot in Word, Excel, or PowerPoint.

To learn more about managing and enabling agents in your organization, see [Manage agents for Microsoft Copilot in the Microsoft 365 admin center](/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps).

### Users by license type

[![Screenshot of summary chart displaying agent usage comparison between licensed and unlicensed Microsoft Copilot users.](../../media/license-type-summary-chart.png)](../../media/license-type-summary-chart.png#lightbox)

The definition of active users (licensed and unlicensed) is the same as provided earlier.

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many users with a Microsoft Copilot license used agents compared with users who don't have a Microsoft Copilot license, over the selected time frame.
- **Trend view** shows daily agent usage over the selected time frame, comparing how many users with a Microsoft Copilot license used agents compared with users who don't have a Microsoft Copilot license.

[![Screenshot of the trend chart for agent usage by license type in Microsoft Copilot.](../../media/license-type-line-chart.png)](../../media/license-type-line-chart.png#lightbox)

### Users by creator type

Shows how many users actively used an agent, grouped by who created the agent.

[![Screenshot of the summary of active users of agents for a select time period.](../../media/users-by-creator-type-summary.png)](../../media/users-by-creator-type-summary.png#lightbox)

The definition of active users is the same as provided earlier. The **Creator type** tells you who built the agent. The following table describes the different types:

| Creator type value | Description |
| --- | --- |
| Your Users | Agents created by individuals in your organization using tools like [agent builder](/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog but users can use them for themselves, or share them via a link with others in the same organization. |
| Your org | Agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](/en-us/microsoft-365/developer/overview-m365-agents-toolkit) or [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your organization. |
| Microsoft | Agents built by Microsoft |
| Third-party | Agents built by trusted non-Microsoft developers and published for broader or public availability and admin-approved for use in your organization. |
| Any | The agent is any of the listed creator types, such as Your Users, Your org, Microsoft, or Third-party. |

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many users used an agent where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft Copilot license, over the selected time frame.
- **Trend view** shows daily usage of agents - how many users used an agent each day where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft Copilot license, over the selected time frame.

[![Screenshot of the trend chart for number of active users by creator type for a selected time period.](../../media/users-by-creator-type-line-chart.png)](../../media/users-by-creator-type-line-chart.png#lightbox)

### Agents by creator type

Shows how many agents users in your organization used, grouped by who created the agent.

[![Screenshot of the summary chart for the number of active agents by creator type for a select period.](../../media/agents-by-creator-type-summary.png)](../../media/agents-by-creator-type-summary.png#lightbox)

The definition of **active agents** and **Creator type** is the same as provided earlier.

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many agents users in your organization used where the agent was one of the Creator types described earlier, regardless of whether the users had a Microsoft Copilot license, over the selected time frame.
- **Trend view** shows daily usage of agents - how many agents users in your organization used each day where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft Copilot license, over the selected time frame.

[![Screenshot of the trend chart for number of active agents by creator type for a selected time period.](../../media/agents-by-creator-type-line-chart.png)](../../media/agents-by-creator-type-line-chart.png#lightbox)

### User details table

[![Screenshot of the details table for agent users in Microsoft Copilot.](../../media/user-details-table.png)](../../media/user-details-table.png#lightbox)

| Metric | Definition |
| --- | --- |
| Username | The user's principal name. |
| Display name | The full name of the user. |
| Number of agents used | The number of distinct agents the user used for the selected time period. |
| Agent responses received | Total responses from all agents used during the selected time period. |
| Last activity date (UTC) | The most recent date the user used an agent, regardless of the selected time period of past 7 or 30 days. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

### Agent details table

[![Screenshot of the details table for agent usage in Microsoft Copilot.](../../media/agent-details-table.png)](../../media/agent-details-table.png#lightbox)

| Metric | Definition |
| --- | --- |
| Agent ID | An agent is an element of an app. The ID is the app identifier generated by Microsoft. |
| Agent name | The name of the app as present in the app manifest. |
| Creator type | Indicates who built the agent. The following list defines the values:<br>- **Your Users** are agents created by individuals in your organization using tools like [agent builder](/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog, but users can use the agents for themselves, or share agents via a link with others in the same organization.<br>- **Your org** are agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](/en-us/microsoft-365/developer/overview-m365-agents-toolkit), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your organization.<br>- **Microsoft** are agents built by Microsoft.<br>- **Third-party** are agents built by trusted non-Microsoft developers and published for broader or public availability and admin-approved for use in your organization.<br>- **Any** are agents from any of the listed creator types. |
| Active users (licensed) | The number of unique users in your organization with a Microsoft Copilot license who used the agent for the selected time period. |
| Active users (unlicensed) | The number of unique users in your organization without a Microsoft Copilot license who used the agent for the time period selected. |
| Responses sent to users | The total agent responses sent to all users during the selected period. |
| Last activity date (UTC) | The date when the agent was last used by anyone in your organization. |

### Users and agent details table

[![Screenshot of the details table for agents and users in Microsoft Copilot.](../../media/user-and-agent-details-table.png)](../../media/user-and-agent-details-table.png#lightbox)

| Metric | Definition |
| --- | --- |
| Agent ID | An agent is an element of an app. The ID is the app identifier generated by Microsoft. |
| Agent name | The name of the app as present in the app manifest. |
| Creator type | Indicates who built the agent. The following list defines the values:<br>- **Your Users** are agents created by individuals in your organization using tools like [agent builder](/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog, but users can use the agents for themselves, or share agents via a link with others in the same organization.<br>- **Your org** are agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](/en-us/microsoft-365/developer/overview-m365-agents-toolkit), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your organization.<br>- **Microsoft** are agents built by Microsoft.<br>- **Third-party** are agents built by trusted non-Microsoft developers and published for broader or public availability and admin-approved for use in your organization.<br>- **Any** are agents from any of the listed creator types. |
| Username | The user's principal name. |
| Responses sent to users | Agent responses sent to a user by an agent during the selected period. This is a per-user, per-agent view. |
| Last activity date (UTC) | The date when the agent was last used by anyone in your organization. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

## FAQ

### Why am I not seeing Cowork usage in the Copilot agent usage report?

Cowork usage is not included in the Copilot agent usage report because the report is designed to show usage and adoption of agents in Copilot. You can track adoption of Cowork separately in the [Cowork usage report](/en-us/microsoft-365/admin/activity-reports/cowork-usage-report) in the Microsoft 365 admin center.

### Why does this report only show the past 7 and 30 days, while other usage reports also show the past 90 and 180 days?

The agent report doesn't yet include the past 90 and 180 days but will add this capability in a future update.

### What is "Last activity detected"?

Last activity detected shows the most recent date and timestamp (in UTC) when user activity generated agent usage.

### Are agents created from Microsoft Copilot Studio and Teams Toolkit included?

Yes. The following agents are the agents for which usage is reported:

- Agents created in Microsoft Copilot Studio by users in your organization and approved by an admin.
- Agents created in Teams Toolkit by users in your organization and approved by an admin.
- Agents created by users through [agent builder](/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder) for users that have this feature enabled and shared with other users in your organization.

### Why is the total active user count less than the sum of licensed and unlicensed active users?

The sum of active users without a license and active users with a license might exceed the total active users if you assigned or removed licenses during the selected timeframe.

### How can I view the username or display name if they're hidden?

By default, the usage report anonymizes the username and display name. Global administrators can change settings to reveal or conceal these values.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

To learn how to change the setting to show the username and display name information, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

### Are SharePoint agents used in Teams included in the usage report?

No. SharePoint agents used in Teams aren't currently included in the usage metrics in the report. For more information, see [Share an agent from SharePoint in Teams - Microsoft Support](https://support.microsoft.com/office/share-an-agent-from-sharepoint-in-teams-6dcbf7b5-8c13-44e5-a68a-dbd71fb76ad3).

### Why is the "Total active users" count smaller than the sum of unlicensed and licensed user counts for my organization?

You might see this discrepancy if a user's Microsoft Copilot license changes during the selected time period. For example, the user might be assigned a Copilot license and later remove it within that same period.