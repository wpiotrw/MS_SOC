---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Adoption Score Report Overview - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/adoption-score?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.reviewer: 
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-05-20T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: high
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
ms.custom:
- sfi-ga-nochange
- AdminTemplateSet
search.appverid:
- MET150
- MOE150
description: Use the Microsoft Adoption Score report to track productivity, compare with peers, and find recommended actions to improve Microsoft 365 adoption today.
locale: en-us
document_id: 84f39061-b5f8-f229-90da-8bd4b87ac7b0
document_version_independent_id: 84f39061-b5f8-f229-90da-8bd4b87ac7b0
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/adoption-score.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/adoption-score
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/adoption-score.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: fbf2dfb1-0254-c80b-14e6-58a5aab8d80d
---

# Microsoft Adoption Score Report Overview - Microsoft 365 admin | Microsoft Learn

Note

Technology experiences retirement (January 2026) Starting January 22, 2026, the Microsoft 365 admin center retires the **Technology experiences** score and its three categories: **Network connectivity**, **Microsoft 365 Apps health**, and **Endpoint analytics** from the **Adoption Score** report. This change rolls out and completes in February 2026.

After this change, the overall **Adoption Score** equals the People experiences score. The **People experiences** score measures end user progress toward embedding Microsoft 365 and Copilot into day-to-day productivity workflows.

As part of this change, the maximum possible Adoption Score changes from 900 to 600. Admins and report readers who regularly use the **Adoption Score** see a change to the total score value when the update reaches their tenant. This change doesn't impact end users.

The **Adoption Score** supports the journey to digital transformation with insights into how your organization uses Microsoft 365. You can compare your organization's score to baselines from organizations similar in size to yours.

The **Adoption Score** provides:

- **Metrics** to help you see where you are on your digital transformation journey.
- **Insights** about the data to help you identify opportunities to improve productivity and satisfaction in your organization.
- **Recommended actions** you can take to help your organization use Microsoft 365 products efficiently.
- **Categories:** Quantifies how the organization works using Microsoft 365 categories like content collaboration, mobility, communication, meetings, teamwork, and AI adoption.

    For each of the mentioned categories, the score looks at public research to identify some best practices and associated benefits in the form of organizational effectiveness. For example, Forrester research shows that when people collaborate and share content in the cloud (instead of emailing attachments), they can save up to 100 minutes a week. Furthermore, the score quantifies the use of these best practices in your organization to help you see where you are on your digital transformation journey.

    To understand more about options to configure for your organization, see [privacy controls for Adoption Score](privacy).

Note

All insights are calculated using data at the organizational level, not the individual level.

## Adoption Score prerequisites

You must have a Microsoft 365 for business or Office 365 for enterprise subscription.

Note

You don't need a license to Viva Insights to use the Adoption Score features.

The **Adoption Score** report is only available in the Microsoft 365 admin center. You can access the report only if you have one of the following roles:

- Global Administrator
- Exchange Administrator
- SharePoint Administrator
- Skype for Business Administrator
- Teams Service Administrator
- Teams Communications Administrator
- Global Reader
- Reports Reader
- AI Report Reader
- Usage Summary Reports Reader
- User Experience Success Manager
- Organizational Messages Writer Role

Caution

Global Administrators have almost unlimited access to your organization's settings and most of its data. To help keep your organization secure, we recommend that you limit the number of Global Administrators as much as possible.

The role-based access control model for Adoption Score helps organizations further digital transformation efforts with Microsoft 365 by providing the flexibility to assign roles to IT professionals within an organization.

Microsoft is committed to protecting individual privacy. [Privacy controls for Adoption Score](privacy) explains the controls we provide you, as your organization's IT administrator, to ensure that the information is actionable while not compromising the trust you place in Microsoft.

You can access the experience from the Microsoft 365 admin center under **Reports** &gt; **Adoption Score**.

Note

This feature isn't available in GCC High, GCC, and DOD tenants.

## How the score is calculated

Your Adoption Score is based on the combined scores of five categories (six categories if you enabled Copilot licenses). Each category is weighted equally, with a total of 100 points. The highest possible Adoption Score is 600.

### Score categories

- Communication (100 points)
- Meetings (100 points)
- Content collaboration (100 points)
- Teamwork (100 points)
- Mobility (100 points)
- AI Adoption (100 points) if Microsoft Copilot licenses are enabled
- **Total possible = 600 points**

In each score category, the key indicators show how your organization is using Microsoft 365 in its journey towards digital transformation. You can see 28-day and 180-day views of the key activities. The report also includes extra metrics that aren't used in score calculation but help you identify underlying usage statistics and configurations that you can address.

The **Adoption Score** includes data from Exchange, SharePoint, OneDrive, Teams, Word, Excel, PowerPoint, OneNote, Outlook, Viva Engage, and Skype.

Your organization's score is updated daily and reflects user actions completed in the last 28 days (including the current day).

## Understand your organization's Adoption Score

The Adoption Score home page shows your organization's total score and score history. It also shows the primary insight for each category.

[![Screenshot of the Adoption Score page in Microsoft 365 admin center Reports.](../../media/prodscore-landing.png)](../../media/prodscore-landing.png#lightbox)

Note

Adoption Score sub-scores are computed on different schedules. Your score might update over the first few days as all sub-scores become available. This behavior is expected. All sub-scores typically arrive within three days, but occasional delays of four to five days might occur. If a sub-score is delayed beyond seven days, you receive a notification in the **Service Health Dashboard** in the Microsoft 365 admin center.

**Your organization's score** appears as a percentage value and in points. You can see your points in the numerator and the maximum possible points in the denominator.

**Peer benchmarks** show you how your organization's score compares with organizations like yours. The peer benchmark is calculated as the average of measures within a set of similar organizations. The set of organizations is composed of organizations in your region with a similar number of licensed users, types of licenses, industry, and tenure with Microsoft 365.

**Understanding your benchmark position:**

- **At or over the benchmark:** Your organization is performing well relative to peer organizations. Being at the benchmark indicates healthy adoption; exceeding it shows strong digital transformation progress.
- **Under the benchmark:** This status indicates an opportunity to improve adoption. Review recommended actions in each category to understand where your organization might gain productivity improvements.
- **Aiming for 100/100 in each category:** While 100 points in every category represents strong execution, the peer benchmark provides a realistic baseline for similar organizations. Many mature organizations operate effectively at 80–90 points per category. Focus on areas that align with your organization's business goals rather than pursuing maximum scores across all categories equally.
- **Being over the benchmark is beneficial:** There's no threshold where exceeding peer performance is negative. Higher adoption typically correlates with improved productivity and employee satisfaction.

Note

Microsoft uses internal data to determine the industry that an organization maps to. Tenants under a parent organization map to the same industry as the parent organization. Organizations can't view or modify industry mappings.

## Category details pages

Each category details page shows the primary insight and supporting metrics. It also shows related research and actions you can take to drive change in your organization. Research supports the importance and rationale behind the primary insights for each category. For example, Forrester research shows that when people collaborate and share content in the cloud (instead of emailing attachments), they can save time each week.

The details pages are:

- [Content collaboration](content-collaboration)
- [Communication](communication)
- [Meetings](meetings)
- [Mobility](mobility)
- [Teamwork](teamwork)
- [AI adoption](ai-adoption-score)

## Group level aggregates

The group-level filters help admins and adoption strategists understand how different groups, based on data from Microsoft Entra ID, are performing. Use the filters to provide higher granularity of insights and actions.

[Learn more about Group Level Aggregates](group-level-aggregates).

## Adoption Score organizational messages

Organizational Messages is a new feature added to Adoption Score that increases the actionability of admins to reach employees and drive adoption awareness. For example, to improve the content collaboration score, admins can notify users to use cloud attachments in Outlook instead of file attachments. Currently, admins can send messages to drive the adoption scenarios for OneDrive SharePoint, Teams Chat, using @mention in Outlook, and cloud attachments in Outlook.

[Learn more about Adoption Score Organizational Messages](organizational-messages).

## Provide feedback on Adoption Score

Share your thoughts about Adoption Score and your ideas about how to improve it. You can provide feedback in the following ways:

- Use the **Feedback** button within the Adoption Score product pages in the Microsoft 365 admin center.
- Email the Adoption Score team at **adoptscorefeedback@microsoft.com** (note: allow up to 2–3 business days for response).
- If you experience issues contacting the team, verify your email address and spam filters, or use the in-product feedback option as an alternative.