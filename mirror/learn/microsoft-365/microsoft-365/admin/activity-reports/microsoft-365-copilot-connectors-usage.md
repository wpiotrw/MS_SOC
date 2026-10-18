---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Copilot Connectors Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-connectors-usage?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: kols
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Copilot Connectors usage report gives admins visibility into connector activity across Chat, Agents, and Search. Discover insights to boost Copilot adoption now.
ms.date: 2026-06-25T00:00:00.0000000Z
locale: en-us
document_id: da5bfa80-e11b-da97-f0c4-e8078bae0a2a
document_version_independent_id: da5bfa80-e11b-da97-f0c4-e8078bae0a2a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-365-copilot-connectors-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-365-copilot-connectors-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-365-copilot-connectors-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 27ef4550-fc43-e547-acaa-58c437349a42
---

# Microsoft 365 Copilot Connectors Usage Report - Microsoft 365 admin | Microsoft Learn

Note

The Copilot Connectors usage report is currently in public preview. Deployment processes and functionality might change before the product becomes generally available. During the public preview phase, you might encounter occasional errors or unexpected behavior. These issues are a normal part of the preview experience and help Microsoft improve the product before general availability.

The Microsoft 365 Copilot Connectors usage report helps you understand how Copilot connectors are used across your organization. Use this report to track adoption and engagement trends across Copilot Chat, Agents, and Copilot Search, and to make data-driven decisions that maximize the value of your connector investments.

The report provides insights at the organization, connector, and user level, including:

- Trend views for active usage and connector activity
- Per-user and per-connector breakdowns for any selected time frame
- Data that refreshes within one hour of user activity

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft 365 Copilot Connectors usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Copilot**, and then select **Connectors**.

## Interpret the Microsoft 365 Copilot Connectors usage report

Use the Microsoft 365 Copilot Connectors usage report to see the usage of Microsoft 365 Copilot Connectors in your organization.

At the top, you can filter by different timeframes. You can view the Microsoft 365 Copilot Connectors report over the last 7 or 30 days.

You can view several metrics for Copilot Connectors usage:

[![Screenshot of the Copilot Connectors report page in the Microsoft 365 admin center.](../../media/copilot-connectors/connectors-hero-metrics.png)](../../media/copilot-connectors/connectors-hero-metrics.png#lightbox)

The following table lists the features included for active users of Copilot Connectors:

Note

Connector usage within Cowork is not yet supported.

| Copilot app | Features | What counts as active usage | Learn more about the feature |
| --- | --- | --- | --- |
| Microsoft Copilot app | Copilot Chat, Agents, Search | A licensed Microsoft Copilot user completes the following action:<br>- Types a natural language query in the Copilot Chat, Agents, or Search and presses **Enter**.<br><br>The user receives a Copilot response that includes grounding (citations) from one or more connectors configured for the organization. | [Microsoft 365 Copilot connectors overview](/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector). |

- **Connections used by Copilot** shows the total number of active Copilot Connector connections that were used when Copilot Chat or Copilot Search generated a response to a user's query that was grounded on content from a Copilot connector.
- **Connections used by Agents** shows the total number of active Copilot Connector connections that were used when a declarative agent or custom engine agent generated a response to a user's query that was grounded on content from a Copilot Connector.
- **Active Connector users** shows the total number of users with a Microsoft Copilot license in your organization who received a Copilot-generated response that was grounded on content from Copilot Connectors.
- **Connector responses** shows the total number of responses generated by Copilot Chat, Copilot Search, or in agents that were grounded on content from Copilot Connectors.

In the **Connector adoption** chart, you see the following **Summary** and **Trend** views.

The **Summary view** shows the total number of active users who used features that received Copilot‑generated responses grounded on Copilot Connector content during the selected time frame.

[![Screenshot of the Copilot Connector adoption user count by feature summary report.](../../media/copilot-connectors/user-count-byfeature-summary-view.png)](../../media/copilot-connectors/user-count-byfeature-summary-view.png#lightbox)

The **Trend view** shows the daily trend view of the usage of the features of the selected time frame.

[![Screenshot of the Copilot Connector adoption user count by feature trend report.](../../media/copilot-connectors/user-count-byfeature-trend-view.png)](../../media/copilot-connectors/user-count-byfeature-trend-view.png#lightbox)

The **Responses provided by connectors** chart shows the daily trend of total number of responses delivered to the users that were grounded on Copilot connector content during the selected time frame. When you hover over a specific day on this chart, you see the total number of Connector responses delivered for that day. This interactive feature helps you quickly understand daily engagement patterns with Copilot Connectors across your organization.

[![Screenshot of responses provided by connectors in the Copilot Connectors usage report. ](../../media/copilot-connectors/response-provided-byconnectors-trend-view.png)](../../media/copilot-connectors/response-provided-byconnectors-trend-view.png#lightbox)

### User activity table

| Metric | Definition |
| --- | --- |
| User ID | The user's principal ID |
| Display name | The user's full name |
| Connections used | Total number of distinct connector connections that were used to generate responses grounded on connector content and delivered to users |
| Responses Received | The total number of responses delivered to users in Copilot Chat, Copilot Search, or agents that were grounded on content from one or more Copilot connectors. |
| Last activity date (UTC) | Last date on which the user received a Copilot‑generated response that was grounded on content from a Copilot connector. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

### Connector activity table

| Metric | Definition |
| --- | --- |
| Connection ID | The connector's unique ID |
| Active users | Total number of active users in your organization who received a Copilot-generated response grounded on content from a specific Copilot connector. |
| Responses Provided | Total number of Copilot-generated responses delivered to users across Copilot Chat, Copilot Search, or agents that were grounded on content from a specific Copilot connector. |
| Last activity date (UTC) | Last date on which the Copilot connector was used to generate a Copilot‑generated response delivered to users. |

## FAQ

### What user actions count as active usage of Copilot connectors?

A user is active for Copilot connectors when they have a Microsoft Copilot license and submit an intentional prompt in Copilot Chat, perform a search using Copilot Search, or interact with an agent, and receive a Copilot‑generated response that is grounded on content (citations) from one or more Copilot connectors configured in the organization.

Simply opening Copilot Chat, Copilot Search, or an agent without submitting a prompt or receiving a connector‑grounded response doesn't count as active usage.

### What platforms does Copilot connectors active usage include?

Copilot connectors active usage includes intentional user interactions in Copilot Chat, Copilot Search, or agents across desktop, web, and mobile platforms that result in Copilot‑generated responses grounded on content from one or more Copilot connectors during the selected time frame.

### What is the scope of the user-level table?

The user-level table in the report shows all users licensed for Microsoft Copilot at any point over the past 180 days, even if the user later removed the license or never had any Copilot active usage.