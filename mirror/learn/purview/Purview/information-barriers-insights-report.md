---
layout: Conceptual
title: SharePoint and OneDrive insights report (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-insights-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the insights report to get information about Information Barriers usage in your organization.
keywords: Microsoft 365, Microsoft Purview, compliance, Information Barriers
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-information-barriers
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
f1.keywords:
- NOCSH
ms.custom:
- seo-marvel-apr2020
- sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: d927d078-2e7b-287b-d583-7ef18b92f21e
document_version_independent_id: d927d078-2e7b-287b-d583-7ef18b92f21e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-insights-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-insights-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-insights-report.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 3051d910-471c-ba49-d06b-d241d089a1ba
---

# SharePoint and OneDrive insights report (preview) | Microsoft Learn

The insights report in [Information Barriers (IB)](information-barriers) helps you identify and discover usage patterns across SharePoint sites and OneDrive accounts in your organization. As an administrator, you can use PowerShell to create and view reports that identify top sites and their modes, so you can apply suitable controls for the sites.

The insights report provides the following information for the top 100 most actively used SharePoint sites and OneDrive accounts in your organization:

| Report section | Description | Applies to |
| --- | --- | --- |
| Explicit mode section | Top restrictive sites with highest collaboration between IB users | SharePoint sites and OneDrive accounts |
| Implicit mode section | Top sites with highest collaboration between compatible users | SharePoint sites only |
| Mixed mode section | Top accounts with collaboration between segmented and unsegmented users | OneDrive accounts only |
| Mode Distribution section | The number and percentage of modes across all sites and accounts | SharePoint sites and OneDrive accounts |
| Open mode section | Top least restrictive sites | SharePoint sites and OneDrive accounts |
| Owner Moderated mode section | Top sites with highest collaboration between IB users and non-IB users | SharePoint sites and OneDrive accounts |

## Prerequisites

- Your organization must have Information Barriers enabled for SharePoint and OneDrive to create the insights report. To enable IB in SharePoint and OneDrive for your organization, see [Use Information Barriers with SharePoint](information-barriers-sharepoint#enable-sharepoint-and-onedrive-information-barriers-in-your-organization).
- You must use the latest version of the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you installed a previous version of the SharePoint Online Management Shell, go to **Add or remove programs** and uninstall *SharePoint Online Management Shell*. Then, install the latest version. To learn more, see [Get started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

## Create the insights report

Before you can run specific queries for Information Barriers details, you must first create a report. After the report finishes successfully, you can run specific detail reports.

The system supports one insights report for every 24-hour period. When you create the next report, it overwrites the previous report. For example, if you create an insights report on April 25, 2023, at 4:10 PM, you can't create another insights report until after 4:10 PM on April 26, 2023.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

To create the insights report, complete the following steps:

1. [Connect to SharePoint Online](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps&amp;toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) as a global administrator or SharePoint administrator in Microsoft 365.
2. Run the following PowerShell cmdlet and accept the confirmation prompt to create the insights report:

    ```powershell
    Start-SPOInformationBarriersInsightsReport
    ```

    Note

    Depending on the number of SharePoint sites and OneDrive accounts in your organization, it might take up to one hour to create this report.

    You can automate acceptance of the confirmation prompt when creating the insights report by appending the *-Yes* parameter to the cmdlet. For example, `Start-SPOInformationBarriersInsightsReport -Yes`.
3. Run the following PowerShell cmdlet to view the status of the insights report:

    ```powershell
    Get-SPOInformationBarriersInsightsReport
    ```

    The following example shows the information returned for the insights report:

    ```text
    State: Completed
    Id: ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776
    StartTimeInUtc: 4/25/2023 4:10:16 PM
    CompleteTimeInUtc: 4/25/2023 4:10:25 PM
    QueuedTimeInUtc: 4/25/2023 4:06:47 PM
    ```

    The report is ready to view or download when the *State* value is *Completed*. Other *State* values include:

    - *Not Started*: State when the insights report hasn't started.
    - *In Progress*: State when the insights report is in progress.
    - *Error*: State when the insights report failed.

## Insights reports for SharePoint sites

### View a summary of modes with results for SharePoint sites

To view a summary of the modes with results for SharePoint sites, use the following cmdlet syntax to view insights from the report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776
```

**Example results**:

```text
Content: Explicit, Implicit, Open, OwnerModerated, ModeDistribution
State: Completed
Id: ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776
StartTimeInUtc: 4/25/2023 4:10:16 PM
CompleteTimeInUtc: 4/25/2023 4:10:25 PM
QueuedTimeInUtc: 4/25/2023 4:06:47 PM
```

In this example, the insights report results are displayed for SharePoint sites included in the organization with an ID of *ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776*. The values in the *Content* line represent the modes that have results in the report. If a mode (applicable to SharePoint) isn't listed, there aren't any SharePoint sites in the organization with that mode.

### View the details for a specific mode for SharePoint sites

To view details about a specific mode with results for SharePoint sites, use the following cmdlet syntax to view insights from the insights report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -section <Mode>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776 -section Explicit
```

**Example results**:

```text
SiteName: Contoso Budget Planning
SiteURL: https://contoso.sharepoint.com/sites/ContosoBudgetPlanning
Site Owner: User1
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Explicit

SiteName: Contoso Training Budgets
SiteURL: https://contoso.sharepoint.com/sites/ContosoTrainingBudgets
Site Owner: User2
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Explicit

SiteName: Contoso Viewpoint Project
SiteURL: https://contoso.sharepoint.com/sites/ContosoViewpointProject
Site Owner: User3
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Explicit
```

### View the details for the mode distribution for SharePoint sites

To view details about the mode distribution with results for SharePoint sites, use the following cmdlet syntax to view insights from the insights report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -section <ModeDistribution>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776 -section ModeDistribution
```

**Example results**:

```text
Total site count: 10000
Owner Moderated SiteCount: 500 SitePercentage: 5
Open SiteCount: 1682 SitePercentage: 16.82
Explicit SiteCount: 3628 SitePercentage: 36.82
Implicit SiteCount: 4190 SitePercentage: 41.9
```

## Insights reports for OneDrive accounts

### View a summary of modes with results for OneDrive accounts

To view a summary of the modes with results for OneDrive accounts, use the following cmdlet syntax to view insights from the insights report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -service <OneDrive>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776 -service OneDrive
```

**Example results**:

```text
Content: Explicit, Mixed, Open, OwnerModerated, ModeDistribution
State: Completed
Id: ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776
StartTimeInUtc: 4/25/2023 4:10:16 PM
CompleteTimeInUtc: 4/25/2023 4:10:25 PM
QueuedTimeInUtc: 4/25/2023 4:06:47 PM
```

In this example, you see the insights report results for OneDrive accounts included in the organization with an ID of *ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776*. The values in the *Content* line represent the modes that have results in the report. If a mode (applicable to OneDrive) isn't listed, there aren't any OneDrive accounts in the organization with that mode.

### View the details for a specific mode for OneDrive accounts

To view details about a specific mode with results for OneDrive accounts, use the following cmdlet syntax to view insights from the insights report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -service OneDrive -section <Mode>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776 -service OneDrive -section Open
```

**Example results**:

```text
SiteName: User1
SiteURL: https://spdfcontoso-my.sharepoint.com/personal/user1_spdfcontoso_onmicrosoft_com
Site Owner: user1@spdfcontoso.onmicrosoft.com
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Open

SiteName: User2
SiteURL: https://spdfcontoso-my.sharepoint.com/personal/user2_spdfcontoso_onmicrosoft_com
Site Owner: user2@spdfcontoso.onmicrosoft.com
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Open

SiteName: User3
SiteURL: https://spdfcontoso-my.sharepoint.com/personal/user3_spdfcontoso_onmicrosoft_com
Site Owner: user3@spdfcontoso.onmicrosoft.com
LastActivity: 4/25/2023 4:10:16 PM
IBMode: Open
```

### View the details for the mode distribution for OneDrive accounts

To view details about the mode distribution with results for OneDrive accounts, use the following cmdlet syntax to view insights from the insights report:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -service OneDrive -section <ModeDistribution>
```

**Example**:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId ec65a1cf-9b1a-48c2-a1b4-f923ac4c0776 -service OneDrive -section ModeDistribution
```

**Example results**:

```text
Total site count: 19305
Owner Moderated SiteCount: 167 SitePercentage: 0.87
Mixed SiteCount: 4881 SitePercentage: 25.28
Explicit SiteCount: 4910 SitePercentage: 25.43
Open SiteCount: 9347 SitePercentage: 48.42
```

## Download the results of the insights report

To download the full results of a specific insights report for SharePoint sites, use the following cmdlet syntax:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -section <report you want to download> -action Download -FullDetails
```

The report automatically exports as a .csv file with a file name of *SharePoint\_the name of the report type*. For example, if you download the *Explicit* report, the file name is *SharePoint\_Explicit.csv*. The *-FullDetails* property supports downloading up to 1 million records for SharePoint sites.

To download the results of a specific insights report for OneDrive accounts, use the following cmdlet syntax:

```powershell
Get-SPOInformationBarriersInsightsReport -reportId <ID> -service OneDrive -section <report you want to download> -action Download
```

The report automatically exports as a .csv file with a file name of *OneDrive\_the name of the report type*. For example, if you download the *Explicit* report, the file name is *OneDrive\_Explicit.csv*.

To rename the report or export to custom locations, use standard PowerShell parameters. For more information, see the [PowerShell documentation](/en-us/powershell/?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Audit activities for the insights report

You can view audit events for the insights report in the [Microsoft Purview portal](purview-portal). For more information about the activities logged, see [Information Barriers activities](audit-log-activities#information-barriers-activities).