---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: AI Adoption Category in Adoption Score - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/ai-adoption-score?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-05-20T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
ms.custom:
- sfi-ga-nochange
- GAUpdates
search.appverid:
- MET150
- MOE150
description: Learn how the AI adoption category in Adoption Score works, compare your benchmark, and take action to improve Copilot adoption in your organization.
locale: en-us
document_id: 668b6f43-0bfd-0d6b-beb3-1452aaeabbf5
document_version_independent_id: 668b6f43-0bfd-0d6b-beb3-1452aaeabbf5
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/ai-adoption-score.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/ai-adoption-score
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/ai-adoption-score.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: ec91f481-9842-fb18-e99a-cfc209860274
---

# AI Adoption Category in Adoption Score - Microsoft 365 admin | Microsoft Learn

As AI rapidly enters the day-to-day experience of people in your organization, Microsoft introduced a new People Experiences category called AI adoption.

The AI adoption score represents the extent to which users in your organization use Microsoft Copilot as a daily habit. A score of 100 means that all licensed Microsoft Copilot users in your organization use Copilot features for an average of at least three days per week (or 12 out of the past 28 days). Users that reach this three-day threshold in a given month are highly likely to become long-term engaged users of Microsoft Copilot. If users fall short of that three-day threshold, the score still gives credit for making progress to it. Use the other insights on the page to understand what behaviors and features contribute to your score, and to identify actions to take to boost your score.

[![Screenshot of the Adoption Score dashboard with the AI adoption category.](../../media/ai-assistance.png)](../../media/ai-assistance.png#lightbox)

## AI adoption score calculation methodology

The AI adoption score is calculated based on a target of getting each licensed user to use Microsoft Copilot for an average of three days per week. The three-day threshold is used because individuals that achieve it have a high likelihood of becoming a consistent long-term user of Microsoft Copilot. The score is computed in a way that your organization still gets credit if users fall short of the three-day threshold. For example, a score of 66 out of 100 indicates that, on average, licensed users are active in Copilot for two days per week (two-thirds of the way towards the three-day target).

Note

For organizations that enable at least one user for Microsoft Copilot, the AI adoption score is now added to your total Adoption Score, causing the denominator for the overall score to increase by 100. If your organization doesn't have any Microsoft Copilot licenses, then the maximum total score is unchanged (700 or 800) and the peer benchmark is unchanged (sum of all categories reports except AI adoption score).

How the score is calculated:

- For each user licensed for Microsoft Copilot, Microsoft calculates the number of days out of the prior 28 days on which the user actively used Microsoft Copilot.
    - The score accounts for Copilot usage in the following Microsoft 365 applications: Outlook, Teams, Copilot Chat, Word, PowerPoint, Excel, OneNote, and Loop. Only intentional user actions in these apps are considered. The set of actions is consistent with those used for the [Microsoft Copilot usage report](/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage).
    - The use of agents in any of the applications listed previously is included in addition to non agentic features, like summarizing a Word document or drafting an email in Outlook.
- An individual-level score is produced for each user by dividing the count of active days by 12. For example, eight days of usage results in (8/12) × 100 = 66.67. 12 days over a 28 day period is equivalent to an average of three days per week.
- The tenant-level score is produced by taking the average score across all licensed users in the organization. A score of 50 out of 100, indicates that, on average, licensed users in your organization use Microsoft Copilot for six days out of the past 28 days (which means an average of 1.5 days per week).

## Peer benchmark for AI adoption score

The AI adoption score peer benchmark helps you compare your organization's score with organizations like yours. The benchmark is an average of the AI adoption scores of organizations similar to yours, based on region, industry, and number of licensed users. For more information, see [Understand your organization's Adoption Score](adoption-score#understand-your-organizations-adoption-score).

[![Screenshot of the chart for the AI adoption score.](../../media/ai-current-chart.png)](../../media/ai-current-chart.png#lightbox)

## Time trends

Time trend data is provided for each category score to track progress. This data provides visibility of Copilot usage across various Microsoft 365 applications over different time ranges, similar to other categories. Alongside the current 28-day rolling period (RL28), insights are available for:

- 30 days (RL30)
- 90 days (RL90)
- 180 days (RL180)

![Screenshot of the time trend options dropdown.](../../media/ai-time-trend.png)

## View AI adoption resources

Resources are available for administrators to facilitate adoption, including:

- Copilot Prompt Gallery
- Success Kit (v2.0)
- User Enablement
- Copilot Dashboard in Viva Insights
- Microsoft Copilot Scenario

![Screenshot of the resources list for Copilot adoption.](../../media/ai-as-resources.png)

## Organizational messages in AI adoption score

Organizational messages in AI adoption score help you promote Microsoft Copilot features to licensed users who haven't tried key capabilities yet. Use organizational messages to quickly deliver actionable notifications directly in Microsoft products (including Teams and Windows), targeted to users based on their Microsoft Copilot activity, all while maintaining user-level privacy.

[![Screenshot of the recommendation cards for Copilot organizational messages.](../../media/ai-as-org-message.png)](../../media/ai-as-org-message.png#lightbox)

To use organizational messages in AI adoption score, you must be assigned one of the following admin roles:

- Organizational message writer

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

After selecting **Take action**, the following message configuration panel appears:

[![Screenshot of the pane from where to create an organizational message for Copilot.](../../media/ai-as-org-message-create.png)](../../media/ai-as-org-message-create.png#lightbox)

Administrators can select one of three message options. The system sends messages to users who have a Copilot license assigned to them but didn't actively use relevant Copilot features over the prior 28 days. Admins can further filter down this list by excluding certain groups. Admins can also configure the start date and end date for the message.

To edit a message after it's already scheduled, admins must cancel and reschedule the message.

Currently, organizational messages show up on either new Teams or Windows 11 notification center. The system adjusts the languages of the messages based on end-users' preferred languages.

## How are people using Microsoft Copilot?

Microsoft Copilot usage insights are organized into six key areas:

- Microsoft Copilot usage frequency
- Teams meetings and chats
- Documents (Word, Excel, PowerPoint, OneNote)
- Emails
- Microsoft Copilot Chat
- Agents for Copilot

These insights show how many users engage with various Copilot features compared to the total number of users enabled over a 28-day period.

Use these insights to:

- Identify which Copilot features are most popular among your users.
- Spot underutilized features that might benefit from more user training.
- Track adoption trends across different Microsoft 365 applications over 7, 30, 90, and 180 days' time ranges.

[![Screenshot of charts showing how people use Copilot.](../../media/ai-using-copilot.png)](../../media/ai-using-copilot.png#lightbox)

Note

When you select the settings to opt out specific user groups from calculating People experience insights in Adoption Score, the AI adoption category doesn't respect that opt out for the current release.

## Sentiment survey upload experience

In this section, you can upload Copilot survey results to display them in the Microsoft Copilot Dashboard.

Note

You can't view the results on this page; they're only available in the Microsoft Copilot Dashboard.

Use this feature to provide your organizational leaders with a centralized location for insights on how users feel about the AI adoption they receive from Copilot.

This feature is only available for Global administrators. Users without this role can't see it in the Microsoft 365 admin center.

### Upload survey data

To access the Sentiment survey upload feature in the Microsoft 365 admin center, follow these steps:

1. In the Microsoft 365 admin center, go to **Reports** &gt; **Adoption Score**.
2. Navigate to **AI adoption score** and select **View details**.
3. On the AI adoption score page, navigate to **Assess Copilot sentiment for your org** and select **Record survey results**.

[![Screenshot showing the dashboard to upload survey data for Copilot sentiment.](../../media/as-upload-survey.png)](../../media/as-upload-survey.png#lightbox)

### Update results over time

[![Screenshot showing the screen for updating survey results for Copilot sentiment.](../../media/as-update-results.png)](../../media/as-update-results.png#lightbox)

To keep the Copilot Dashboard updated with the latest feedback from your users, upload new survey data as often as you want.

![Screenshot showing the screen for deleting survey results for Copilot sentiment.](../../media/as-delete-survey.png)

To delete or overwrite the existing survey data, select the **Delete** or **Overwrite** buttons at the bottom of the page. These actions can't be undone.

### Suggested Copilot survey questions

To measure Copilot user sentiment in your organization, deliver a survey to users that asks them to indicate their level of agreement with the following four statements:

- *Using Copilot helps improve the quality of my work or output.*
- *Using Copilot helps me spend less mental effort on mundane or repetitive tasks.*
- *Using Copilot allows me to complete tasks faster.*
- *When I use Copilot, I'm more productive.*

For each of these questions, allow users to indicate whether they strongly disagree, disagree, neither agree nor disagree, agree, or strongly agree with the statement. You can then combine the agree and strongly agree responses to compute the percentage of users who agreed with each statement and compare results with the Microsoft benchmarks shown in this tab.

Your user survey doesn't need to be limited to these four statements, but include them at a minimum for easy comparison with Microsoft's benchmark results.