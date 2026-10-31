---
layout: Conceptual
title: Manage security compute unit usage in Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/manage-usage
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to monitor and manage the use of security compute units in Security Copilot.
ms.date: 2026-05-28T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- sfi-image-nochange
ms.reviewer: 
locale: en-us
document_id: f830030d-c97b-c2ed-bd72-3c69a7f6fc17
document_version_independent_id: f830030d-c97b-c2ed-bd72-3c69a7f6fc17
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/manage-usage.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manage-usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/manage-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: dec6ce4f-9e8d-de06-66af-9b7252ad0de4
---

# Manage security compute unit usage in Security Copilot | Microsoft Learn

The usage monitoring dashboard provides a comprehensive view into various data dimensions to help you keep track of Security Compute Units (SCUs) usage in Security Copilot. You have visibility into the number of provisioned and overage units used, the specific plugins employed during sessions, and the initiators of those sessions. The dashboard also allows you to apply filters and export usage data seamlessly. The dashboard includes up to 90 days of data, offering a robust window into recent activity.

Tip

To understand what Security Compute Units are and the available capacity models, see [Understand Security Compute Units and capacity](security-compute-units-capacity).

## Monitor security compute units usage

Copilot owners can view the usage over time within the Microsoft Security Copilot usage monitoring dashboard.

To view the usage dashboard:

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com) and go to the **Home menu** &gt; **Owner settings**.
2. Select **Usage monitoring**.

The usage dashboard shows how many SCUs are consumed over a period of time by your Microsoft Security Copilot workloads.

## Understand the data dimensions

Use the data dimensions to get a granular view of how SCUs are being used.

Capacities are captured on the tabs at the top of the dashboard. Select a capacity to view the usage information related to that specific capacity.

You can toggle between the various capacity resources that you own. You see information such as provisioned units used, overage units used, and the workspace that's using the capacity.

The following table provides information on what each column represents and helps you interpret data accurately:

| Column | Description | Examples/Types |
| --- | --- | --- |
| Session ID | A unique identifier for each Copilot session. | a123b456-789-1011-1c2-d12345678e99 |
| Date | Date when the user initiated the session, displayed in local time zone. | Sept 10, 08:30 AM |
| Units used | Number of SCUs used in the session. | 0.6 |
| Initiated by | The user that initiated the session. | Ben Heppard |
| Category | The format in which session was made.  There are three category types: - Prompt- Promptbook- Agent- Primitive | **Prompt**: A single prompt. **Promptbook**: A session related to a promptbook. For example, a user initiates "Script Analysis" promptbooks in which five prompts are called. Each prompt from promptbook call has a category as "promptbook". **Agent**: An interactive or a fully autonomous computational entity that works to achieve a specific goal. It's defined by its ability to perceive and react to its environment, make decisions, and produce outcomes to meet its objective. **Primitive**: An AI inference call performed by a service, application, or workflow, typically without direct user interaction. |
| Type | The method used for the session. There are two invocation types:- Manual Action  - Automated Action. | **Manual Action**: User triggered calls. A user must manually initiate. For example, a user types and submits prompt in prompt bar. **Automated Action**: Calls that are automatically initiated/scheduled. For example, incident summary or scheduled logic app. |
| Copilot experience | The user interface where the session was initiated from. Users can use the standalone interface, an embedded interface, or through LogicApps. | - Security Copilot portal [(Standalone experience)](/en-us/copilot/security/experiences-security-copilot#standalone-and-embedded-experiences) - Copilot in Microsoft products [(Embedded experience)](/en-us/copilot/security/experiences-security-copilot#standalone-and-embedded-experiences); for example, inside Microsoft Defender XDR.  - Azure Logic Apps - Users can initiate Security Copilot workflows using Azure Logic Apps. |
| Plugin used | The plugin used in the session. | Microsoft Entra, Microsoft Defender XDR. |
| Status | Indicates if SCUs are used. | All available units used. |

## Apply filters

Use filters to narrow down the displayed information in the dashboard. Applying filters can help you analyze relevant data without reviewing the entire data set.

Note

Currently, filters are only applied to the table and not the bar chart.

![Screenshot showing the usage monitoring dashboard filter button.](media/usage-monitor-filter.png)

The following filters are available:

- Copilot experience
- Users
- Plugins used
- Type
- Category

Important

Selecting a date range impacts the data shown in the table. For instance, choosing **Last 24 hours** and then selecting a filter, such as a specific user, will display information related to that user from only the past 24 hours.

Selecting a bar in the chart filters the table to show information for that specific day.

## Export usage dashboard data

Export usage dashboard data into Excel files for easier analysis, sharing, or offline access. Select the **Export** button on the corner of the dashboard.

![Screenshot showing the usage monitoring dashboard export button.](media/usage-monitor-export.png)

## Nearing and crossing security compute unit limit

When the usage in your organization is nearing the limit, you're notified of it when submitting the prompts. To avoid disruption, you can contact the Azure capacity owner or contributor to increase the security compute units or limit the number of prompts.

### Experience when nearing security compute unit limit

When you're in the middle of an investigation and the usage is nearing the provisioned capacity limit, a notification is displayed in response to a prompt.

The capacity limit notifications are also shown in Security Copilot embedded experiences and it informs the analyst to contact the Azure capacity owner or contributor to increase the capacity or limit the number of prompts to avoid disruptions.

The notification allows the analyst to react before they run out of capacity.

### Experience when security compute unit limit is exceeded

When the provisioned and overage SCUs is crossed, the analyst will see an error message stating that due to high usage in the organization Copilot can't respond to requests. Analysts can't submit more prompts at this time. More capacity would become available in the next hour.

The analyst is asked to contact the Azure capacity owner or contributor to increase the provisioned SCUs.

The error message view only appears when your organization reaches 100% of capacity.

## Update the provisioned and overage security compute units (SCUs)

You can update provisioned security compute units and overage units in the Azure portal and the Security Copilot portal. You also have the option to view billing in Azure while updating SCUs.

**Azure portal required role:** Azure capacity owner or contributor.

**Security Copilot portal required role:** Azure capacity owner or contributor who are also Security Copilot owners.

Note

Users can expect capacity adjustments to take effect within 30 minutes.

### Process to update provisioned and overage security compute units (SCUs)

You can update the provisioned and overage SCUs as follows:

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com) and go to **Settings**.
2. There are two ways you can update the provisioned and overage SCUs:

    - Through the owner settings page: Under **Security compute units** or **Number of overage units**, select **Change**.
    - Through the usage dashboard: Select **Change units** in the main dashboard.

    In either option, update the number of security compute units (SCUs) for the provisioned and overage units. You also have the option to view billing in Azure by selecting **View billing in Azure**.

    As the number of SCUs are increased or decreased, the estimated monthly cost changes accordingly, assuming the provisioned capacity remains the same 24 hours a day for the whole month.

    - Through the owner settings page: Under **Security compute units** or **Number of overage units**, select **Change**.
    - Through the usage dashboard: Select **Change units** in the main dashboard.

    In either option, update the number of security compute units (SCUs) for the provisioned and overage units. You also have the option to view billing in Azure by selecting **View billing in Azure**.

    As the number of SCUs is increased or decreased, the estimated monthly cost changes accordingly, assuming the provisioned capacity remains the same 24 hours a day for the whole month.

## Offboard and delete capacity

To offboard from Security Copilot, you'll need to delete the provisioned capacity. You need to be at least a Security Administrator role to accomplish this task.

Note

To export Security Copilot data, you will need to contact Security Copilot support. For more information, see [Contact Security Copilot support](support).

### Delete capacity from the Owner settings

Warning

Deleting capacity and their internal data is a permanent action and cannot be undone.

You can delete capacity from the Owner settings page or the usage monitoring page.

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com).
2. Select the **Home menu** icon.
3. Navigate to the **Owner settings** or **Usage monitoring** section.
4. In the units section, select **Change**.
5. Select the overflow menu (**...**).
6. Select **Delete the capacity**.
7. Confirm that you want to delete capacity. This action deletes the active capacity for the tenant.

## Understand SCU charges by capability

SCUs are charged based on the capability release stage:

| Capability stage | Charged? |
| --- | --- |
| Generally available (GA) | Yes |
| Public preview | Yes |
| Private preview | No |