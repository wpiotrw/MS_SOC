---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Adoption Score Organizational Messages - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/organizational-messages?view=o365-worldwide
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
ms.date: 2026-06-05T00:00:00.0000000Z
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
ms.custom:
- AdminTemplateSet
- campaignIDs-batch1
- GAUpdates
search.appverid:
- MET150
- MOE150
description: Learn how to use organizational messages in Adoption Score to target users in Microsoft 365, improve user adoption, and increase engagement with in-product notifications. Start creating messages today.
locale: en-us
document_id: 18299c90-c8a0-9f49-b11b-013f4589e440
document_version_independent_id: 18299c90-c8a0-9f49-b11b-013f4589e440
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/organizational-messages.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/organizational-messages
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/organizational-messages.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 32df71fc-4023-3ca2-ea72-5b49f7202207
---

# Microsoft Adoption Score Organizational Messages - Microsoft 365 admin | Microsoft Learn

IT admins can use organizational messages to deliver clear, actionable messages in-product and in a targeted way, while maintaining user-level privacy. Adoption Score organizational messages use targeted in-product notifications to advise on Microsoft 365 recommended practices based on Adoption Score insights. Send users the following types of messages:

- Reminders to use products that you recently deployed.
- Encouragement to try a product on a different surface.
- Recommendations of new ways of working, such as using **@mentions** to improve response rates in communications.

Templated messages are delivered to users in their flow of work through surfaces including Microsoft Outlook, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, and Microsoft Teams. Authorized professionals can use the organizational messages wizard in Adoption Score to:

- Choose from up to three templated message types.
- Define when and how often a message can be displayed.
- Exclude groups or priority accounts from receiving the message.

Organizational messages for Adoption Score initially roll out to **Communication**, **Content Collaboration**, and **Mobility** with more to follow to support all People Experience categories.

Note

This feature is currently in preview. If you encounter any bugs or have any suggestions, provide feedback in the Microsoft 365 admin center. Microsoft appreciates your feedback and reaches out to you as fast as it can.

This video provides an overview of how to use organizational messages to help increase Microsoft Copilot adoption. It's 2 minutes and 48 seconds long.

## Who can use this feature

To get a successful preview experience, you need the [**Organizational Messages Writer**](/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-messages-writer) role.

The **Organizational Messages Writer** role is the new built-in role that assigned admins use to view and configure messages. The Global administrator can assign the **Organizational Messages Writer** role to admins:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Roles** to expand it.
3. Under **Roles**, select [**Role assignments**](https://admin.cloud.microsoft/?#/rbac/directory).
4. In the **Role assignments** page, scroll to the bottom of the list of roles and select **Show all roles**.
5. Scroll through the alphabetical list of roles and find the **Organizational Messages Writer** role. Once found, select it.

    Tip

    You can also use the **Search this list** search box to find the **Organizational Messages Writer** role.
6. In the **Organizational Messages Writer** pane, select the **Assigned** tab.
7. Select **Add users** or **Add groups**.
8. In the **Add users** or **Add groups** pane, search for the users or groups you want to assign the role to, and then select them.
9. When you select all the users or groups you want to assign the role to, select **Add**.

## Where organizational messages appear

In this preview, Microsoft supports the teaching call-out and business bars in all currently supported versions of Microsoft Office and Microsoft 365 in the following apps:

- Microsoft Word.
- Microsoft Excel.
- Microsoft PowerPoint.
- Microsoft Outlook Desktop Apps.
- Microsoft Teams.

[![Screenshot of in-product notification recommending users use Teams messages more.](../../media/org-message-location-bar-expanded.jpg)](../../media/org-message-location-bar-expanded.jpg#lightbox)

*The user sees an in-product notification recommending they use Teams messages more.*

Microsoft supports the desktop teaching call-out messages in all currently supported versions of Microsoft Office and Microsoft 365.

[![Screenshot of in-product notification recommending users save to OneDrive more.](../../media/org-message-location.png)](../../media/org-message-location.png#lightbox)

*The user sees an in-product notification recommending they save to OneDrive more.*

[![Screenshot of in-product notification pop-up in Teams recommending users use interactive features during Teams meetings.](../../media/teams-from-your-org.png)](../../media/teams-from-your-org.png#lightbox)

*The user sees an in-product notification recommending they use interactive features during Teams meetings.*

## How to enable Adoption Score Organizational Messages

To enable Adoption Score Organizational Messages, the global administrator needs to first enable Adoption Score. To enable Adoption Score, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org settings**](https://admin.cloud.microsoft/?#/Settings/Services).
4. In the **Org Settings** page, select **Adoption Score**.
5. In the **Adoption Score** pane:

    1. Make sure the **Insight calculations and display** tab is selected.
    2. Under **Select users and groups for calculating insights**, select **Include all users (recommended)**. It can take up to 24 hours for insights to become available.
    3. Select the **Organizational Messages** tab and then select **Allow approved admins to send in-product recommendations to specified users**.
    4. Select **Save**.

Note

Only a global administrator can enable Adoption Score. The Organizational Messages Writer role can only opt in for Adoption Score Organizational Messages.

After Adoption Score is enabled, the Organizational Messages Writer can opt in for Adoption Score Organizational Message.

For more information on how to enable Adoption Score, see [Privacy controls for Adoption Score](privacy).

[![Screenshot of how to enable Organizational Messages in Adoption Score.](../../media/org-message-adoption-score.png)](../../media/org-message-adoption-score.png#lightbox)

## Capabilities

As an Organizational Messages Writer, you can complete the following tasks:

- Choose a message from a set of templated content for business bars or teaching call-outs.
- Select the recipients based on user activities, Microsoft Entra user groups, and group level aggregates.
- Schedule a time frame and frequency for delivery of the messages.
- Save drafts anytime during the message creation process.
- Track the status of organizational messages and user engagement.
- Manage scheduled or active organizational messages.

## Increase Adoption Score by creating Organizational Messages

You can create organizational messages in Adoption Score by using either of the following methods:

- Create organizational messages based on recommendations to improve your organization's adoption score.
- Create organizational messages from a list of all available actions.

### Create organizational messages based on recommendations to improve your organization's adoption score

To create organizational messages based on recommendations to improve your organization's adoption score, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Adoption Score**](https://admin.cloud.microsoft/?#/Reports/AdoptionScore).
4. In the **Adoption Score** page, make sure the **Overview** tab is selected.
5. The **Adoption Score** &gt; **Overview** page displays the adoption score for your organization across several different categories including:

    - Communication.
    - Meetings.
    - Content collaboration.
    - Teamwork.
    - Mobility.
    - AI adoption.
6. Select **View details** for any one of the categories to see the details and insights for that category.
7. In the details pane for the category, you see the insights and recommendations for that category, including the current adoption score. Under the **How can I impact my score?** section, you see recommended actions that you can take to improve the adoption score for that category.
8. Select **See what action you can take** to display available recommended actions and organizational messages you can send to users to encourage them to adopt the recommended practices and improve your organization's adoption score.
9. In the pane that opens after selecting **See what action you can take**, make sure the **Recommended Action** tab is selected, and then select **Create message**.

    Note

    If **Manage active message** is displayed instead of **Create message**, there's already an active message for the selected recommended action. Each tenant can only have one active message for each action. You can select **Manage active message** to go to the [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) page to manage the active message. For more information on how to cancel an active message and schedule a new one, see the section Cancel or clone messages in this article.
10. Go to the section Create an organizational message in this article for additional steps on how to create and schedule an organizational message to send to your users.

### Create organizational messages from a list of all available actions

To create organizational messages from a list of all available actions, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Adoption Score**](https://admin.cloud.microsoft/?#/Reports/AdoptionScore).
4. In the **Adoption Score** page, select the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allactions) tab next to the **Overview** tab.
5. Make sure **All available actions** is selected and then choose one of the listed available messages.
6. In the **Recommended actions details** pane, select **Create message** to start creating an organizational message that you can send to your users.

    Note

    If **Manage active message** is displayed instead of **Create message**, there's already an active message for the selected recommended action. Each tenant can only have one active message for each action. You can select **Manage active message** to go to the [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) page to manage the active message. For more information on how to cancel an active message and schedule a new one, see the section Cancel or clone messages in this article.
7. Go to the section Create an organizational message in this article for additional steps on how to create and schedule an organizational message to send to your users.

### Create an organizational message

Before you proceed, make sure you follow the steps in one of the following sections in this article to reach the **Make recommendations to users** page:

- Create organizational messages based on recommendations to improve your organization's adoption score.
- Create organizational messages from a list of all available actions.

Tip

You can select **Save and Close** at any point during the message creation process to save a draft of the message. The draft is stored in [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) under the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) tab of the **Adoption Score** page. To edit or schedule the draft message, see the section Edit or schedule a draft message.

To create an organizational message, follow these steps:

1. In the **Make recommendations to users** page of the **Overview** step, select **Next**.
2. The **Create messages** page of the **Messages** step displays where the organizational message appears. In the **Select a message** dropdown menu, select a message option for the organizational message. If desired, select **Preview this message** to see an example of what recipients see during the date range you choose. When finished, select **Next**.

    Note

    The message shows up in the same language that is set on the user's device. Currently, there are 41 languages supported. See the section Supported localization for messages for a list of supported languages.
3. In the **Select message recipients** page of the **Recipients** step, the system selects recipients by default based on their activities. For example, targeted users aren't actively using OneDrive or SharePoint with the apps enabled for the past 28 days. You can also:

    - Select **Apply filter** &gt; **Choose organizational attribute** to select additional recipients based on the following attributes:

        - **Groups**: Send messages to specific Microsoft Entra user groups.
        - **Companies, Departments, or Locations**: Using group-level aggregates, you can apply attributes filter such as companies, departments, or location to target specific groups of audiences. For more information, see [Group Level Aggregates in Adoption Score](group-level-aggregates).
    - Omit users with priority accounts or in certain Microsoft 365 Groups by selecting the appropriate **Omit** options.

    When finished, select **Next**.

    Note

    The recipient list is refreshed daily. The users who adopted the recommended practices are removed from the recipient lists.

    [![Screenshot of selecting recipients for Organizational Messages in Adoption Score.](../../media/org-message-select-recipients.png)](../../media/org-message-select-recipients.png#lightbox)
4. In the **Schedule your message** page of the **Schedule** step, select a start date and end date for when the message should be delivered to users. You can also select the frequency of how often the message is delivered by using the **Select interval** dropdown menu. When finished, select **Next**.

    Note

    - If you set the frequency of the message to once a week, the message only shows on one of the surfaces per week. After the user selects or dismisses the message, it doesn't show up again.
    - Teaching call-out messages only appear twice in their lifetime even if the user doesn't select it.

    [![Screenshot of scheduling your message for Organizational Messages in Adoption Score.](../../media/org-message-schedule-message.png)](../../media/org-message-schedule-message.png#lightbox)
5. In the **Review details & finish** page of the **Finish** step, review the details of the organizational message.

    - If you're ready to schedule the message, select **Schedule**.
    - If you want to save the message as a draft, select **Save and Close**. The draft is stored in [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) under the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) tab of the **Adoption Score** page. To edit or schedule the draft message, see the section Edit or schedule a draft message.

### Track the status of the messages and user engagement

After you create messages, you can see the reporting in a table in [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) under the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) tab of the **Adoption Score** page. The table provides the following information:

| **Column name** | **Values** | **Notes** |
| --- | --- | --- |
| **Message name** | Name of the message. |  |
| **Status** | - Draft<br>- Scheduled<br>- Active<br>- Canceled<br>- Completed<br>- Error |  |
| **Last edited date** | Date and time of the last edit. |  |
| **Start date** | Date and time when the message is scheduled to start. |  |
| **End date** | Date and time when the message is scheduled to end. |  |
| **Related category** | Category related to the message. |  |
| **Related metric** | Metric related to the message. |  |
| **Creator** | User who created the message. |  |
| **Total messages seen** | Total number of times the message was shown to users. | Available after messages are active. |
| **Total clicks** | Total number of times users selected the message. | Available after messages are active. |

Note

Product admins, users with the [Reports Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) role, and user success specialists with reader permissions can access this capability.

[![Screenshot of tracking the status of your message for Organizational Messages in Adoption Score.](../../media/org-message-track-status.png)](../../media/org-message-track-status.png#lightbox)

### Edit or schedule a draft message

To edit or schedule an organizational draft message, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Adoption Score**](https://admin.cloud.microsoft/?#/Reports/AdoptionScore).
4. In the **Adoption Score** page, select the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) tab next to the **Overview** tab.
5. Select [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages).
6. Under **Draft messages**, find the message you want to edit and then select it.
7. To edit the message, follow the steps in the Create an organizational message section of this article. When you finish, select **Schedule** to schedule the message or **Save and Close** to save the changes to the draft.

### Cancel or clone messages

To cancel an active organization message or clone an existing message, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Adoption Score**](https://admin.cloud.microsoft/?#/Reports/AdoptionScore).
4. In the **Adoption Score** page, select the [**Actions**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages) tab next to the **Overview** tab.
5. Select [**Manage your org's messages**](https://admin.cloud.microsoft/?#/adoptionscore/allmessages).
6. Under **Active messages**, find the message you want to cancel or clone, and then select the vertical ellipsis (**⁝**) next to the message to show the **More actions** dropdown menu.
7. In the **More actions** dropdown menu, select one of the options:

    - **Cancel active message** to cancel the active message
    - **Clone** to create a new message with the same settings as the existing message.

Note

Each tenant can have one active message for each action. If you want to schedule a new message, follow the steps in this section to cancel active ones.

## Organizational Messages in Microsoft Intune

Organizational messages in Microsoft Intune enable organizations to deliver branded personalized messages to their users via native Windows 11 surfaces, such as **Notification Center** and the **Get started** app. These messages help people ramp up in new roles quicker, learn more about their organization, and stay informed of new updates and trainings. For more information, see [Create a policy that allows organizational messages in Microsoft Intune](/en-us/microsoft-365/admin/misc/organizational-messages-microsoft-365#create-a-policy-that-allows-organizational-messages-in-microsoft-intune).

## Frequently asked questions (FAQs)

### Why does the total number of messages seen differ from the expected number?

For any given message, not every user selected as message recipients receives the message. This behavior is expected because the message delivery depends on other factors that affect a message's reach, including:

- **User behavior**: Some delivery channels require the user to go to a specific location or app to have a chance to see the message. For example, a Microsoft 365 app call-out message can only be delivered to a user who opens the Microsoft 365 app.
- **System protections to prevent over-messaging and user dissatisfaction**: Some communication channels have message frequency limits if too many messages are live at a given time. For example, a Teaching call-out doesn't appear more than twice to each user.

### How can I test the messages before sending them to users of my entire company?

Send messages to specific Microsoft Entra groups, such as your IT department. For more information, see the Create an organizational message section in this article.

### What is the recommended time frame window for the messages?

As the frequency of the messages is at most once a week, the recommended minimum duration is one month. The recommended length of the time window is 12 months. The recipient's list is refreshed daily. Your messages are always sent to users who didn't adopt the recommended practices in the last 28 days. Messages aren't repeatedly sent to users who already adopted.

### Can I customize the text in the messages?

Not currently, but additional customization options will be enabled in future releases.

## Supported localization for messages

| Languages | Locale |
| --- | --- |
| Arabic | ar |
| Bulgarian | bg |
| Chinese (Simplified) | zh-cn |
| Chinese (Traditional) | zh-tw |
| Croatian | hr |
| Czech | cs |
| Danish | da |
| Dutch | nl |
| English (United States) | en |
| Estonian | et |
| Finnish | fi |
| French (France) | fr |
| German | de |
| Greek | el |
| Hebrew | he |
| Hungarian | hu |
| Indonesian | id |
| Italian | it |
| Japanese | ja |
| Korean | ko |
| Latvian | lv |
| Lithuanian | lt |
| Norwegian (Bokmål) | no |
| Polish | pl |
| Portuguese (Brazil) | pt-br |
| Portuguese (Portugal) | pt-pt |
| Romanian | ro |
| Russian | ru |
| Serbian (Latin) | sr |
| Slovak | sk |
| Slovenian | sl |
| Spanish (Spain) | es |
| Swedish | sv |
| Thai | th |
| Turkish | tr |
| Ukrainian | uk |
| Vietnamese | vi |
| Catalan | ca |
| Basque | eu |
| Galician | gl |
| Serbian (Cyrillic) RS | sr-Cyrl |