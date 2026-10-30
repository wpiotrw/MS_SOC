---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Adoption Score - Teamwork - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/teamwork?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
search.appverid:
- MET150
- MOE150
description: Details of Teamwork in the Adoption Score report.
locale: en-us
document_id: 1f4ee8cf-fe75-3bdb-0a62-197c3bb81911
document_version_independent_id: 1f4ee8cf-fe75-3bdb-0a62-197c3bb81911
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/teamwork.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/teamwork
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/teamwork.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 346b8630-8fbf-0f90-8994-43267298dc2f
---

# Microsoft Adoption Score - Teamwork - Microsoft 365 admin | Microsoft Learn

Adoption Score provides insights into your organization's digital transformation journey through its use of Microsoft 365 and the technology experiences that support it. Your organization's score reflects technology experience measurements and can be compared to benchmarks from organizations similar to yours. To learn more, check out the [Adoption Score overview](adoption-score) and read [Microsoft's Privacy Statement](https://privacy.microsoft.com/privacystatement).

## Prerequisites

To get started with teamwork insights, users in your organization need to be licensed for:

- Microsoft Teams.
- SharePoint.
- Exchange Online.

For more information, see [assign licenses to users](../manage/assign-licenses-to-users).

When users are active in these products at least once in the last 28 days, you start to see the insights.

## Why your org's teamwork score matters

A fundamental pillar for organizational productivity is when a group of users with a common goal work with each other and with common resources for collective success. Research indicates that when users share information and collaborate in shared workspaces, they save up to 4 hours a week. They can find related documents, find context for previous discussions, and deliver towards shared goals. See the [evidence](https://www.microsoft.com/microsoft-365/blog/wp-content/uploads/sites/2/2019/04/Total-Economic-Impact-Microsoft-Teams.pdf)

## How the teamwork score is calculated

Primary insight in the experience that contains the key metrics for this category in your organization is provided. Then a scoring framework is used for these metrics to calculate your organization's score.

### Primary insight

The primary insight looks at:

- All the users who are communicating using email and messages on Microsoft Teams.
- Interacting with content on the cloud in shared workspaces.

Within Microsoft 365, Microsoft 365 Groups are the foundation for users to come together in a shared workspace with the ability to send emails to the group mailbox, share files on the SharePoint team site, and send channel messages through Microsoft Teams.

[![Screenshot of chart showing primary insights into the teamwork score.](../../media/teamwork-score.png)](../../media/teamwork-score.png#lightbox)

1. **Header**: Provides the key metric of users in your org performing any one the following activities:

    - Sending email to a group mailbox through Exchange.
    - Sending channel messages through Teams.
    - Reading and creating content (what we collectively refer to as content interaction) in SharePoint team sites.

    As a percentage of all users in your org who are performing any of the following activities (within or outside of shared workspaces):

    - Sending email through Exchange.
    - Sending messages (chat or channel messages) on Microsoft Teams.
    - Reading and creating content on OneDrive or SharePoint.

    And have access to at least one of the following services:

    - Exchange.
    - Microsoft Teams.
    - SharePoint.
2. **Body**: Provides more information on how communicating and interacting with content, when done within a shared workspace, can have positive outcomes for productivity in your organization.
3. **Visualization (current state)**:

    - Horizontal bar where the blue portion represents the percentage expressed in the header.
    - Highlights the fraction (numerator/denominator) used for computing the percentage shown in the header.

        - **Numerator**: The number of users in your organization who send email to a group mailbox through Exchange, OR who are sending channel messages through Teams, OR reading and creating content in SharePoint team sites.
        - **Denominator**: The number of users in your org who send emails through Exchange, OR send messages (chat or channel messages) on Microsoft Teams, OR read and create content on OneDrive or SharePoint, AND have access to at least one of the following services: Exchange, Microsoft Teams, or SharePoint.
    - The peer benchmark value of the key metric is also shown as a percentage.
4. **View resources about teamwork**: To view help content, select this link.

#### Trend visualization of the primary insight

The following chart provides the trend of the numerator and the denominator of the key metric in the primary insight. It shows the number of users engaged in shared workspaces, and the number of users communicating or interacting with content within the last 180 days. Each data point on the line chart is an aggregate of activity for the last 28 days.

[![Screenshot of chart that shows number of users engaged in shared workspaces.](../../media/trend-people-in-shared-workspaces.png)](../../media/trend-people-in-shared-workspaces.png#lightbox)

### Scoring framework

The teamwork score for your organization measures at an aggregate (organizational) level whether users are consistently communicating or engaging in file activity in shared workspaces within the last 28 days.

Scores aren't provided at the individual user level.

## Explore more about teamwork in your organization

We also provide additional information about how users in your organization work together. These additional metrics don't directly contribute to your Adoption Score, but are relevant in helping you create an action plan as part of your digital transformation.

### Breakdown of how users engage in shared workspaces

[![Screenshot of chart that shows how users in your org are engaged in shared workspaces.](../../media/people-shared-workspace-engagement.png)](../../media/people-shared-workspace-engagement.png#lightbox)

1. **Header**: Shows a detailed breakdown across the different types of teamwork being measured.
2. **Body**: Provides information on the value of working in shared workspaces to help teams be more effective.
3. **Visualization**: The visualization shows the extent to which users who are communicating or interacting with content are doing so in shared workspaces, as follows:

    - **Sending email**: The colored portion and the fraction represent the percentage of users sending email to group mailboxes. The fraction is composed of:

        - **Numerator**: users sending emails to group mailboxes in the last 28 days.
        - **Denominator**: users sending emails in the last 28 days. These users are the same group of users who are marked as sending email in the primary insight of communication Adoption Score.
    - **Sending messages**: The colored portion and the fraction represent the percentage of users sending messages in channels in Microsoft Teams. The fraction is composed of:

        - **Numerator**: users sending channel messages within the last 28 days.
        - **Denominator**: users sending chat or channel messages in the last 28 days. These users are the same group of users who are marked as sending messages in Microsoft Teams in the primary insight of the communication category in Adoption Score.
    - **Creating content**: The colored portion and the fraction represent the percentage of users reading or creating content on Microsoft 365 SharePoint team sites.

        - **Numerator**: Number of users reading or creating content on Microsoft 365 group connected team sites.
        - **Denominator**: Number of users with access to SharePoint, who read or created content of any kind in OneDrive or SharePoint sites in the last 28 days.
4. **View related content**: To view help content, select this link.

### Breakdown of workspace engagement by size and age

[![Screenshot of chart that shows engagement in workspace as categorized by size and age.](../../media/workspace-engagement-by-size-age.png)](../../media/workspace-engagement-by-size-age.png#lightbox)

1. **Header**: Categorizes engagement by workspace size, based on member count, and workspace age in months.
2. **Body**: Provides information about the value of encouraging users in your organization to keep only the workspaces that are needed to promote more effective teamwork.
3. **Visualization**: The engagement breakdown is shown in the form of a heat-map across two dimensions.

    - **Size of workspace**: Workspaces are broken down into three categories based on the number of members: 2-10 users, 11-100 users, and over 100 users. The **All** category includes all size categories.
    - **Age of workspace**: Categorizes workspaces by the number of months since they were first created. The **All** category includes all age categories.

        Each cell in the chart has a number and color based on the percentage of engaged workspaces that belong in that category. The workspace categories are based on the age and size shown in the intersection of that cell. For example, if the cell at the intersection of 11-100 users and 4-12 months has a value of 52%, it means that 52% of the workspaces with 11-100 members that are between 4-12 months old, have some form of engagement. The percentage is calculated as:

        - **Numerator**: Workspaces that have engagement in the form of communication (email and channel messages) or content interaction in the last 28 days.
        - **Denominator**: All workspaces that are available in your org for the last 28 days.
4. **View related content**: To view help content, select this link.

### Breakdown of workspaces by level of engagement

[![Screenshot of chart that shows the breakdown of workspaces by engagement by groups.](../../media/workspace-by-engagement.png)](../../media/workspace-by-engagement.png#lightbox)

1. **Header**: Provides a breakdown of workspaces broken out by level of engagement, using group email, channel messages, and content interaction.
2. **Body**: Provides information on the value of consistent engagement in the shared workspaces to help make them more effective at teamwork.
3. **Visualization**: Provides a view of the workspaces in your organization based on the intensity of engagement per week. The view includes distributions for different activity types measured within teamwork, in addition to any engagement, which covers the following categories:

    - **Group email**: Percent of workspaces that have no days/1 day/2-3 days/4+ days of group email activity per week over the last 28 days.
    - **Channel messages**: Percent of workspaces that have no days/1 day/2-3 days/4+ days of channel messages per week over the last 28 days.
    - **Content reading or creation**: Percent of workspaces that have no days/1 day/2-3 days/4+ days of reading or creating content per week over the last 28 days.
4. **View related content**: To view help content, select this link.

### Use of teams within Microsoft Teams

[![Screenshot of chart that shows how many share workspaces are used by Microsoft Teams.](../../media/use-of-teams-within-teams.png)](../../media/use-of-teams-within-teams.png#lightbox)

1. **Header**: Shows the number of shared workspaces that have a Microsoft Teams team associated with them.
2. **Body**: Provides information about the value of having a Microsoft Teams team attached to the shared workspaces, to help make users associate with them more effective at teamwork.
3. **Visualization**: The colored part of the donut chart reflects the percentage of workspaces that have a Microsoft Teams team attached to them. The percentage is calculated as follows:

    - **Numerator**: The number of shared workspaces in your organization that had a Microsoft Teams team associated with them in the last 28 days.
    - **Denominator**: The number of shared workspaces in your org in the last 28 days.

        The number in the center of the donut chart represents the total number of shared workspaces that have a Microsoft Teams team associated with them.
4. **View related content**: To view help content, select this link.

## View teamwork trends over time

For each of the insights in this article, you can see how the metrics trend over time by selecting an option from the **Data View** dropdown menu.

[![Screenshot of trends over time chart.](../../media/trends-over-time.png)](../../media/trends-over-time.png#lightbox)

After you select an option, the charts in the report will update to show a trend over time rather than a snapshot of the past month.