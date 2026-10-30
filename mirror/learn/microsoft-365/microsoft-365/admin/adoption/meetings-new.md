---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Adoption Score - Meetings - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/meetings-new?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords: NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.reviewer: 
ms.date: 2026-01-23T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- scotvorg
- highpri
- operations-pod
ms.custom: 
search.appverid: MET150
description: Learn more about Meetings insights score in the Adoption Score report.
locale: en-us
document_id: 33212da9-1ade-32bd-8e3e-7f33fa221c01
document_version_independent_id: 33212da9-1ade-32bd-8e3e-7f33fa221c01
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/meetings-new.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/meetings-new
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/meetings-new.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 5dac72ae-194c-0b15-36dd-2267d4e7e6ea
---

# Microsoft Adoption Score - Meetings - Microsoft 365 admin | Microsoft Learn

Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

Adoption Score provides insights into your organization's digital transformation journey through its use of Microsoft 365 and the technology experiences that support it. Your organization's score reflects technology experience measurements and can be compared to benchmarks from organizations similar to yours. To learn more, check out the [Adoption Score overview](adoption-score) and read [Microsoft's Privacy Statement](https://privacy.microsoft.com/privacystatement).

Note

This documentation is for the newest version of Meetings insights. If you're still using the previous version of Meetings insights, see the article for [Meetings insights (Previous Version)](meetings).

## Prerequisites

To get started with Meetings insights, people in your organization need to be licensed for:

- Microsoft Teams

For more information, see [assign licenses to users](../manage/assign-licenses-to-users).

After people have been active in Teams at least once in the last 28 days, you'll start to see the insights.

## Why your organization's meetings score matters

Meetings, where people explore ideas, plan, solve problems, and make decisions, are a fundamental pillar for organizational productivity. Research indicates that when people use online meeting tools effectively, they tend to save up to 104 minutes per week.

## How we calculate the meetings score

Microsoft Teams integrates with Outlook calendar and provides a host of capabilities to make your meetings more engaging and effective. We provide an overall score for Meetings and then sub scores for each of the best practices in the Set up, Meet up and Follow up sections.

## Overall score

The overall meeting score is calculated by averaging out the scores across the three phases: Set up, Meet up, and Follow up. We take into account the number of attendees and the duration of the meeting when tallying the final averaged scores.

For each meeting:

1. We compute the three sub-scores (Pre, During, Post), by averaging the features, for each meeting. For example, Set Up: 30, Meet up: 40, Follow up: 20
2. We then compute the average of the three sub-scores for the meeting. From the above example, 30+40+20/3 = 30
3. We compute the weight of each meeting based on the meeting duration and meeting size. The longer or bigger a meeting, the more impact it has in the final score.
4. We then perform a weighted sum average on scores from all meetings of the tenant based on meeting weights to compute the final meeting score for the tenant.

![Screenshot: Meeting score for Microsoft Teams meetings.](../../media/adoption-score-meetings.jpg)

1. **Header**: Shows the score, out of 100, based on the average of Set Up, Meet Up and Follow Up phases for online meetings on Microsoft Teams held in the past 28 days.
2. **Body**: Provides more information on how using online meeting tools effectively can make meetings more effective.
3. **Visualization (current state)**: In this horizontal bar chart, the blue (colored) portion represents the score (out of 100) shown in the header.

## Trend visualization of the score

The following chart shows the trend-line of score over the selected period. Each data point on the line chart is an aggregate of activity for the last 28 days.

![Screenshot: Time trend chart for meeting score.](../../media/meetings-time-trend.jpg)

## What makes up my score?

We provide you with supporting data on each of the Set Up, Meet up and Follow Up phases. The score for each insight is calculated out of 100.

## Set up

This represents the phase that involves scheduling and sharing the details of the meeting and participants joining the meeting.

![Screenshot: Set up phase section for meeting score.](../../media/adoption-score-set-up.jpg)

- **Communication shared ahead of time**: This represents the score for Microsoft Teams meetings that had a Teams conversation meeting chat started before conducting the meeting. For this to be tracked, a user must go to the meeting chat with the participants and send a message to the participants, before the scheduled meeting time.
- **Invitation accepted at a high rate (&gt;50%)**: This represents the score for Microsoft Teams meetings that had more than 50% of invited participants accept the meeting invite.

## Meet up

This represents the phase of when attendees are in the meeting.

![Screenshot: Meet up phase section for meeting score.](../../media/meetings-meet-up.jpg)

- **Used at least one interactive feature**: This represents the score for Microsoft Teams meetings that had attendees use at least one interactive feature. These interactive features include raising hand, sending a meeting chat message, or sending a reaction in the meeting. The score is calculated out of 100.
- **Participated with audio or chat at a high rate (&gt;33%)**: This represents the score for Microsoft Teams meetings that had more than 33% of the participants either speak in a meeting, send a meeting chat, or both. The score is calculated out of 100.
- **Shared visual content**: This represents the score for Microsoft Teams meetings that had attendees share any visual content in the meeting by either turning on their video, sharing screen, or both. The score is calculated out of 100.

## Follow up

![Screenshot: Follow up phase section for meeting score.](../../media/meetings-follow-up.jpg)

- **Created recording**: This represents the score for Microsoft Teams meetings that had the meeting recorded. The score is calculated out of 100.
- **Sent out post-meeting communication**: This represents the score for Microsoft Teams meetings that had attendee(s) share any chat messages on the meeting chat thread after the conclusion of that meeting. The score is calculated out of 100.

## How can I impact my score?

This section helps understand two insights for the organization:

1. **Most significant growth**: This section depicts the part of the score that had the highest growth in the past 28 days.
2. **Biggest area for improvement**: This section depicts the part of the score that has the biggest room to improve and impact the org's Adoption Score in the future.

## Dig deeper into meetings

This section consists of three sub-sections:

1. **Additional insights**: Here we provide more insights that help organizations identify trends and user behaviors across meetings.
2. **Interesting findings**: Here we provide some interesting facts about meetings being conducted in the organization.
3. **Microsoft Research**: Here we reference Microsoft blogs and public research that provide recommended practices and their impacts to have effective meetings.

Note

The 'Dig deeper into meetings' section does not contribute to the overall score of the Meetings Page in Adoption Score People Experiences, however some insights in this section may expand on a primary insight used to calculate a score.