---
layout: Conceptual
title: Investigate and remediate Communication Compliance alerts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Investigate and remediate Communication Compliance alerts in Microsoft Purview.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
- microsoft-365-copilot
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-image-nochange
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
locale: en-us
document_id: f5943932-8723-73be-b15b-8fc3f5e6cb5a
document_version_independent_id: f5943932-8723-73be-b15b-8fc3f5e6cb5a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-investigate-remediate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-investigate-remediate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-investigate-remediate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 6744d735-76a7-7bdb-525a-aa1cd9ae580a
---

# Investigate and remediate Communication Compliance alerts | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

After you configure [Communication Compliance policies](communication-compliance-policies), you receive alerts for message issues that match your policy conditions. To view and act on alerts, assign users the following permissions:

- The *Communication Compliance Analysts* or the *Communication Compliance Investigators* role group
- Reviewer in the policy that is associated with the alert

After you establish required permissions, use the following working instructions to investigate and remediate issues.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Investigate policy matches and alerts

Important

On June 1, 2025, the new **Policy Match Preservation** setting goes into effect. On that date, existing policy matches might be permanently deleted based on the time period you select in the **Policy Match Preservation** setting. New policy matches are preserved for that time period. You have until **May 19** to change the time period if you don't want to use the default setting of **1 year**. For details, see Policy Match Preservation setting.

To investigate issues detected by your policies, review policy matches and alerts. The Communication Compliance area provides several features to help you quickly investigate policy matches and alerts:

### Policies page

When you sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization, select the **Communication Compliance** solution, then select the **Policies** page. This page shows Communication Compliance policies configured for your Microsoft 365 organization and links to recommended policy templates.

Note

If your role group is [scoped by one or more admin units](purview-admin-units), you see a message at the top of the page that you can only view and manage the policies that you're scoped for. To learn more about what you can access, select **View role groups** in the banner.

Each policy listed includes the following columns:

- **Messages scanned today**: The total number of messages that the policy scanned on the current day for users and locations that are in scope of the policy. If there's a policy match, the item is added to the **New pending today** column. The number refreshes automatically once per hour, it doesn't update if you refresh the page. At the end of the UTC day, the count resets to zero.

    Tip

    If the value in the column is 0 or a low number, it might be because the policy is too strict. For example, the policy might be focused on just one user or on just one location that the in-scope user doesn't use. You might see a wide variety of aggregate numbers in this column if your policies have different focuses. For example, one policy might be focused on an entire department of users sending messages from multiple locations while another policy might be focused on just one user or just one location.

    - **New pending today**: Shows the number of policy matches for the current day. This value updates whenever you open the page. You can also select the **Refresh** button to get the latest count. At the end of the UTC day, the count resets to zero.
    - **Total pending**: The count of policy matches that need review. This value updates whenever you open the page. You can select the **Refresh** button to get the latest count. After refreshing, this number matches the number on the **Pending** tab.
    - **Total resolved**: The total number of resolved policy matches. This value updates whenever you open the page. You can select the **Refresh** button to get the latest count. After refreshing, this number matches the number on the **Resolved** tab.
    - **Status**: The status of the policy (Active or Deactivated).
    - **Last modified**: The date and Coordinated Universal Time (UTC) of the last policy modification.
    - **Last policy scan**: The UTC date for the last policy scan.

    To start remediation actions, select the policy associated with the alert to launch the **Policy details** page. From the **Policy details** page, you can review a summary of the activities, review, and act on policy matches on the **Pending** tab, summarize a lengthy message by using Microsoft Copilot in Microsoft Purview, or review the history of closed policy matches on the **Resolved** tab. For details, see Review and remediate policy matches and alerts.

### Alerts page

Go to **Communication Compliance** &gt; **Alerts** to display the last 30 days of alerts grouped by policy matches. This view lets you quickly see which Communication Compliance policies generate the most alerts, ordered by severity. An alert isn't the same thing as a policy match. An alert generally consists of multiple policy matches, not just one policy match. After the required number of policy matches is met for a particular alert, the alert is created and email is sent to the alert recipient.

- **Reports page**: Go to **Communication Compliance** &gt; **Reports** to display Communication Compliance report widgets. Each widget provides an overview of Communication Compliance activities and statuses, including access to deeper insights about policy matches and remediation actions.

Tip

[Analyze interactions entered into generative AI applications](communication-compliance-channels#generative-ai).

## Tips for quickly reviewing policy matches on the Pending or Resolved tab

- When you select a message to review on the **Pending** tab or the **Resolved** tab, the condition that caused the policy match appears in an alert message bar (yellow banner) at the top of the **Source** tab. This alert message bar is a quick way to determine the condition or conditions that caused the policy match. If there are multiple conditions, select **View all** in the banner to see all the conditions that caused the policy match. At this time, only Microsoft provided trainable classifiers and sensitive information types are highlighted as conditions in the yellow banner.
- Sometimes it's useful to quickly review policy settings without opening a policy. For example, if you're testing multiple policies with different conditions, you might want to save time by reviewing conditions for each policy to determine risk before opening the policy. You can do this by selecting **Policy settings**, which opens a panel where you can view the policy settings. If you're a member of the Communication Compliance or Communication Compliance Admins role group, you can view and change settings from the panel. If you're a member of the Communication Compliance Investigators or Communication Compliance Analysts role group, you can view settings but you can't change them.

### Policy Match Preservation setting

When a Communication Compliance policy finds a message that matches the policy, the solution stores a *copy* of the message (not the original message). Starting June 1, 2025, you can use the **Policy Match Preservation** setting to specify how long to save policy matches in Communication Compliance. You can choose **1 month**, **6 months**, **1 year**, or **7 years**. The default value is **1 year**.

Note

You can also specify a preservation period when you create or edit a policy. The preservation period you select within a policy takes precedence over the global **Policy Match Preservation** setting.

When the global **Policy Match Preservation** setting goes into effect on April 1, 2025:

- The value in the **Policy Match Preservation** setting applies to all existing policy matches. The system automatically deletes policy matches that are older than the selected time period. For example, if the **Policy Match Preservation** setting is **1 year** (the default), the system permanently deletes any policy matches older than 1 year as of September 1. Only the policy matches in Communication Compliance are deleted because they're copies of the original messages. This process doesn't delete original copies from user shards. You can use [Microsoft Purview Data Lifecycle Management](retention) to set up a retention policy for original messages.
- New policy matches as of September 1 receive a timestamp with the preservation period specified in the setting.
- If you change the time period in the setting after September 1, the preservation period applies going forward. For example, if you select **1 year** as the time period on September 1, then change the setting to **7 years** on September 3, policy matches from September 1 and September 2 are preserved for 1 year, and policy matches starting on September 3 are preserved for 7 years.

#### What you need to do

The **Policy Match Preservation** setting becomes available for your organization on April 1, 2025. Between April 1 and May 30, select the time period for preserving policy matches for your organization. The selection isn't applied until June 1, 2025.

##### Change the time period for the global **Policy Match Preservation** setting

To change the global policy match preservation period, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select the **Settings** button in the upper-right corner of the page, then select **Communication Compliance** to go to the Communication Compliance global settings.
3. Select the **Policy Match Preservation** setting, then select a new time period.
4. Select **Confirm** in the confirmation dialog box.

##### Change the policy match preservation time period for a custom policy

You can also select a time period for preserving policy matches in the policy workflow for a custom policy. When you set a time period in a custom policy, it takes precedence over the selection in the global **Policy Match Preservation** setting. This option is useful for policies that are the exception to the norm.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution, then select **Policies** in the left navigation.
3. Select the **More actions** (ellipsis) button in the row for the policy you want to change, then select **Edit**.
4. On the **Name and describe your policy** page in the policy workflow, under **Preserve policy matches**, make a selection. If you leave the **Global Setting** selection, the policy uses the time period selected in the global **Policy Match Preservation** setting. If you choose any other time period, it takes precedence over the selection in the global setting.

### Using filters

Sort the messages so it's easier for you to investigate. From the **Policy details** page, Communication Compliance supports multilevel filtering for several message fields to help you quickly investigate and review messages with policy matches. You can filter pending and resolved items for each configured policy. You can configure filter queries for a policy or configure and save custom and default filter queries for use in each specific policy. After configuring fields for a filter, you see the filter fields displayed on the top of the message queue that you can configure for specific filter values.

Key filters (the **Body/Subject**, **Date**, **Sender**, and **Tags** filters) always display on the **Pending** and **Resolved** tabs to make it easy to access those filters.

For the **Date** filter, the date and time for events are listed in Coordinated Universal Time (UTC). When filtering messages for views, the requesting user's local date/time determines the results based on the conversion of the user's local date/time to UTC. For example, if a user in U.S. Pacific Daylight Time (PDT) filters a report from 8/30/2021 to 8/31/2021 at 00:00, the report includes messages from 8/30/2021 07:00 UTC to 8/31/2021 07:00 UTC. If the same user was in U.S. Eastern Daylight Time (EDT) when filtering at 00:00, the report includes messages from 8/30/2021 04:00 UTC to 8/31/2021 04:00 UTC.

#### Filter details

Communication Compliance filters help you filter and sort messages for quicker investigation and remediation actions. You can filter on the **Pending** and **Resolved** tabs for each policy. To save a filter or filter set as a saved filter query, you must configure one or more values as filter selections.

The following table outlines filter details:

| Filter | Details |
| --- | --- |
| **Body/Subject** | The message body or subject. Use this filter to search for keywords or a keyword phrase in the body or subject of the message. The subject appears in the **Subject** column for email messages. For Teams messages, nothing appears in the **Subject** column. |
| **Classifiers** | The name of built-in and custom classifiers that apply to the message. Some examples include *Targeted Harassment*, *Profanity*, *Threat*, and more. |
| **Date** | The date the message was sent or received by a user in your organization. To filter for a single day, select a date range that starts with the day you want results for and end with the following day. For example, to filter results for 9/20/2020, choose a filter date range of 9/20/2020-9/21/2020. |
| **Escalated To** | The user name of the person included as part of a message escalation action. |
| **File class** | The class of the message based on the message type, either *message* or *attachment*. |
| **Has attachment** | The attachment presence in the message. |
| **Item class** | The source of the message based on the message type, email, Microsoft Teams chat, Bloomberg, and more. For more information, see [Item Types and Message Classes](/en-us/office/vba/outlook/concepts/forms/item-types-and-message-classes). |
| **Language** | The detected language of text in the message. The message is classified according to the language of most the message text. For example, for a message containing both German and Italian text, but most text is German, the message is classified as German (DE). For a list of supported languages, see [Trainable classifiers](trainable-classifiers-learn-about).  You can also filter by more than one language. For example, to filter messages classified as German and Italian, enter 'DE,IT' (the two-digit language codes) in the Language filter search box. To view the detected language classification for a message, select a message, select View message details, and scroll to the *EmailDetectedLanguage* field. |
| **Recipient domains** | The domain to which the message was sent; this domain is typically your Microsoft 365 subscription domain by default. |
| **Recipient** | The user to which the message was sent. **Note**: The **Recipient** field includes recipients in the **To** and **CC** fields. **BCC** fields aren't supported. |
| **Sender domain** | The domain that sent the message. |
| **Sender** | The person who sent the message. |
| **Size** | The size of the message in KB. |
| **Tags** | The tags assigned to a message, either *Questionable*, *Compliant*, or *Noncompliant*. |

#### Configure a filter

To configure a filter for policy matches, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select a policy to see policy matches (if any) for that policy.
4. On the **Policy** page, select either the **Pending** or **Resolved** tab to display the items for filtering.
5. Select **Filters**.
6. Select one or more filter checkboxes, then select **Apply**.
7. To save the selected filters as a filter query, select **Save the query** after you configure at least one filter value. Enter a name for the filter query, then select **Save**. This filter is available to use for only this policy and is listed in the **Saved filter queries** section of the **Filters** page.

## Review and remediate policy matches and alerts

After you review policy matches or alerts and configure filtering, take remediation action. Start your remediation process with the following workflow on the **Policy** or **Alerts** pages.

Note

If you see a policy prefaced with "DSPM for AI" (or "AI hub" from the preview name), the policy was created in Data Security Posture Management for AI, not in Communication Compliance. For more information about this solution, see [Data Security Posture Management (DSPM) for AI](dspm-for-ai).

### Examine the message basics

Sometimes it's obvious from the source or subject that you can immediately remediate a message. The message might be spurious or incorrectly matched to a policy and you should resolve it as misclassified. To mark a message as misclassified, select **Resolve** and **Item was misclassified** to leave a note in the item's history that it's misclassified and remove it from the **Pending** queue. To share misclassified content with Microsoft, select **Send message content, attachments, and subject** to remove it from the **Pending** queue and report the items to Microsoft.

Note

Misclassified options in the **Resolve** pane don't appear if the condition that caused the policy match isn't based on a trainable classifier. Reporting misclassified items to Microsoft isn't supported for Content Safety classifiers yet.

From the source or sender information, you might already know how the message should be routed or handled in these circumstances. Consider using **Tag as** or **Escalate** to assign a tag to applicable messages or to send messages to a designated reviewer.

### Examine the message details

After reviewing the message basics, open the message to examine the details and determine further remediation actions.

Tip

For lengthy messages, you can save time by summarizing the message (including attachments, transcripts, and recordings) with Copilot in Microsoft Purview.

Select a message to view the complete message header and body information. Several different options and views are available to help you decide the proper course of action:

- **Sentiment**: Messages include a sentiment evaluation (powered by [Azure Cognitive Service for Language](/en-us/azure/cognitive-services/language-service/overview)) to help investigators quickly prioritize potentially riskier messages to address first. The **Sentiment** column displays the message sentiment and is enabled in the default view. Messages are flagged with one of the following values:

    | Value | Description |
    | --- | --- |
    | Positive | Messages with *Positive* sentiment indicate a lower priority for triaging. |
    | Negative | Messages with *Negative* sentiment indicate messages to prioritize. |
    | Neutral | Messages with *Neutral* sentiment are determined to be neither positive nor negative. |
    | Not available | *Not available* appears in the column for file formats that aren't supported. For example, sentiment analysis isn't available for any image that's attached to a Teams or email message, text extracted from an OCR image, or text or recordings from a Teams transcript. *Not available* also appears if the message includes more than 5,120 words. |
    | Scanning | *Scanning* appears in the the column when Communication Compliance is trying to determine the appropriate sentiment value for the message. |
- **Attachments**: This option allows you to examine Modern attachments that match policy conditions. Modern attachments content is extracted as text and is viewable on the **Pending** tab. For more information, see the [Communication Compliance feature reference](communication-compliance-channels).
- **Source**: This view is the standard message view commonly seen in most web-based messaging platforms. The header information is formatted in the normal style and the message body supports embedded graphic files and word-wrapped text. If [optical character recognition (OCR)](communication-compliance-policies#optical-character-recognition-ocr) is enabled for the policy, images containing printed or handwritten text that match policy conditional are viewed as a child item for the associated message in this view.
- **Plain text**: Text view that displays a line-numbered text-only view of the message and includes keyword highlighting in messages and attachments for sensitive info type terms, terms identified by built-in classifiers assigned to a policy, or for terms included in a dedicated keyword dictionary assigned to a policy. Keyword highlighting, which is currently available for English language only, can help direct you to the area of interest in long messages and attachments. In some cases, highlighted text might be only in attachments for messages matching policy conditions. Embedded files aren't displayed and the line numbering in this view is helpful for referencing pertinent details among multiple reviewers.
- **Conversation**: This view, which is available for Teams chat messages, displays up to five messages before and after a message to help reviewers view the activity in the conversational context. Select **Load more** to load up to 20 messages before and after a message. To download messages, select **Download conversation**. This action downloads an image file of everything you see in the user interface and also a .csv file of all the message metadata (UserId, UserName, and so on).

    The Conversation view context helps reviewers quickly evaluate messages and make more informed message resolution decisions. Real-time message additions to conversations are displayed, including all inline images, emojis, and stickers available in Teams. Image or text file attachments to messages aren't displayed. Notifications are automatically displayed for messages that have been edited or for messages deleted from the Conversation window. When a message is resolved, the associated conversational messages aren't retained with the resolved message.
- **Pattern detected** notification: Many harassing and bullying actions over time involve recurring instances of the same behavior by a user. The *Pattern detected* notification is displayed in the message details and raises attention to the message. Detection of patterns is on a per-policy basis and evaluates behavior over the last 30 days when at least two messages are sent to the same recipient by a sender. Investigators and reviewers can use this notification to identify repeated behavior to evaluate the message as appropriate.
- **Translation**: This view automatically converts message text to the language configured in the *Displayed language* setting in the Microsoft 365 subscription for each reviewer. This conversion includes the text for the policy match and everything included in the conversation view (up to five messages before and five messages after the policy match). The *Translation* view helps broaden investigative support for organizations with multilingual users and eliminates the need for additional translation services outside of the Communication Compliance review process. Using Microsoft translation services, Communication Compliance automatically detects if the text is in a different language than the user's current system setting and displays alert message text accordingly. For a complete list of supported languages, see [Microsoft Translator Languages](https://www.microsoft.com/translator/business/languages/). Languages listed in the *Translator Language List* are supported in the *Translation* view.
- **User activity**: This view provides risk profile, policy matches, and user activities captured by [Insider Risk Management](insider-risk-management) and Communication Compliance. This integration helps Communication Compliance investigators quickly see risk severity and the associated activities for the user while investigating and triaging pending policy matches.

    The **User activity** view displays the *Insider risk severity* level for the user and has two sections, one for Communication Compliance policy matches and activities and one for Insider Risk Management risk activities. View the risk severity of the user from Insider Risk Management in the *Source* tab if data sharing is enabled. For more information, see [Share Insider Risk Management data with other solutions](insider-risk-management-settings-share-data#share-alert-severity-levels-with-other-microsoft-security-solutions).

    **Communication Compliance policy matches**: This section displays the total number of communication *Policy matches* and the total number of *Remediation actions* for the user included in this policy match.

    Select **View details** in this section to display a timeline of Communication Compliance activities for the user. This timeline includes:

    - Totals for *Policy matches* and *Remediation actions* for the user
    - Details for each activity associated with the user for the past 30 days.

    **Insider risk activity**: This section displays the total number of *Risk activities* and the total number of *Unusual activities* for activities associated with this user for Insider Risk Management policies. *Unusual activities* are activities for the user that are considered potentially risky, as they're unusual and a departure from their typical activities.

    Select **View details** in this section to display a timeline of insider risk activity for the user. This timeline includes:

    - The insider risk [severity level](insider-risk-management-activities#alert-status-and-severity).
    - Totals for *All activities* and *Unusual activities*.
    - Details for each activity associated with the user from the [Activity explorer](insider-risk-management-activities#activity-explorer-tab) in Insider Risk Management.

    To view the insider risk activities in insider risk management, select **Open in insider risk management**.

    **Timeline**: This section displays a history of all communications for user activities. This timeline allows investigators to review all communications for a user, helping to identify any inappropriate handling of confidential information. Only previous policy matches for the user associated with the alert are displayed.

    For each Copilot interaction, the details for the user prompt and the Copilot response are available for review. The date and time for each interaction are provided in UTC.

### Summarize a message by using Copilot in Microsoft Purview

You can use Copilot in Microsoft Purview to get a contextual summary of a Teams, email, or Viva Engage message included in a policy match. The summary is in the context of one or more [Microsoft provided trainable classifiers](classifier-tc-definitions) that flag the message (for example, stock manipulation). This feature saves time for investigators if the message content is lengthy.

Copilot in Microsoft Purview summarizes the entire message, including any video recordings, meetings transcripts, or attachments (docx, pdf, or txt files).

#### Limitations

Be aware of the following limitations when using Copilot in Microsoft Purview to summarize messages:

- The message content must be at least 100 words and less than 15,000 words. If the message content is fewer than 100 words or more than 15,000 words, Copilot in Microsoft Purview doesn't summarize it.
- Summarize items in various languages supported by Security Copilot. For more information, see [Supported languages in Microsoft Security Copilot](/en-us/copilot/security/supported-languages).
- At this time, only individual Teams messages can be summarized. If you summarize an individual Teams message, Copilot doesn't pull in the surrounding conversation.

#### Prerequisites for using Copilot in Microsoft Purview

To summarize a message in Communication Compliance by using Copilot in Microsoft Purview, you must have specific licenses and onboard your organization to Copilot in Microsoft Purview. For details, see [Copilot in Microsoft Purview licensing requirements and onboarding](/en-us/copilot/security/get-started-security-copilot). You must also be a member of the *Communication Compliance*, *Communication Compliance Analysts*, or *Communication Compliance Investigators* role.

#### Summarize a message

1. In Communication Compliance, go to the **Policies** page, and then open any policy to view policy matches for that policy.
2. Select a message in the list. You can select a parent item or a child item (but it's easier to select the parent item).
3. Select **Summarize**. This option appears below the message details. It opens the **Copilot** panel on the right side of the screen and displays a summary of the message.

    Important

    You might see a generic error message that says "An error occurred" after selecting **Summarize**. This error message can appear for any of the following reasons:

    - You don't have the [required license](/en-us/copilot/security/get-started-security-copilot) for Copilot in Microsoft Purview.
    - You don't have the required Communication Compliance role and/or the Security Copilot contributor role. To use Copilot in Microsoft Purview, you must have one of the following Communication Compliance roles: *Communication Compliance*, *Communication Compliance Analysts*, *Communication Compliance Investigators*. You must also have the [Security Copilot contributor role](/en-us/copilot/security/authentication), which should be turned on by default for all users in a Microsoft Entra organization.
    - There's an internal error. Microsoft provides more information for these errors.
4. Select one of the suggested prompts at the bottom of the panel to use Copilot to create the summary. For example, if the classifier that flagged a message is Stock manipulation, select *Summarize this message and supported attachments in the context of Stock manipulation category detected*. You can also enter an open-ended question in the "Ask a question" box.

    ![Screenshot of the Copilot in Microsoft Purview panel showing a message summary, suggested prompts, and the Ask a question box for Communication Compliance investigators.](media/communication-compliance-security-copilot1.png)

    a. **Summarize**. b. Summary generated by **Summarize**. c. Suggested Copilot prompts. d. "Ask a question" box for open-ended Copilot questions.

    Note

    Only message content is summarized. If you ask a question relevant to the message content, Copilot provides a result. If the question isn't relevant to message content, Copilot instructs you to ask a different question.
5. If you want to provide feedback on the summarized content, select the drop-down arrow in the lower-right corner below the summary, and then enter your feedback.
6. After reviewing the summary, you can remediate the policy match like any other policy match. For remediation options, see Decide on a remediation action.

Note

Copilot in Microsoft Purview responses are also recorded in [Microsoft Security Copilot](/en-us/security-copilot/experiences-security-copilot).

### Understanding hidden matches

When a Communication Compliance policy triggers, it highlights the exact matches in the **Plain text** tab. However, policies can also flag messages where the keywords are hidden and embedded in nonvisible metadata, such as HTML tags or encoded strings. By default, the plain text view doesn't show this content.

The following scenarios show where hidden content matches might occur:

- **HTML tags**: Hyperlinks embedded in HTML tags, for example:

    ```html
    <a href="https://example.com">Click here</a>.
    ```
- **Alternative text for images**: Descriptive text for images, for example:

    ```html
    <img src="sunset.png" alt="Sunset over the lake">
    ```
- **Encoded strings**: Encoded strings that represent different content when decoded, for example:

    `Base64: U3Vuc2V0IG92ZXIgdGhlIGxha2U=` decodes to *Sunset over the lake*
- **Filename of attachment**: The file name of the attachment might lead to a policy match but isn't clearly highlighted in the text view.
- **OCR:** Text extracted from images using Optical Character Recognition (OCR).

If a message doesn't appear to match the conditions you set for the policy, complete the following steps:

1. Select and download the message with the policy match.
2. Extract the contents of the zipped folder.
3. Locate the .eml file.
4. Open the .eml file with any text editor.
5. Use the *Find* function to search for the individual keywords in the policy conditions to identify where the match occurs.

### Review Microsoft Teams meetings transcripts

If you deploy Microsoft Teams in your organization, you can review Teams meetings transcripts for actionable alerts. Teams transcripts are automatically included if you choose Teams as a Microsoft 365 location when you create a custom policy or when you create a policy based on a template.

- **Scheduled meetings**: Communication Compliance ignores communication direction for Teams transcripts. If an individual is an invitee or is present in a scheduled (nonrecurring) meeting, the policy includes all of the meeting content, regardless of who says what in the meeting. This approach also helps in situations where a user is attending the meeting through a hub device in a conference room, since it's not always possible to tell whether an offending communication comes from an in-scope user. Since all meeting content is included, an investigator can review the recording of the meeting to determine if the offending communication is by an in-scope user.
- **Recurring meetings**: For recurring meetings, the policy evaluates only the following users:

    - Users who were invited to the meeting
    - Users identified by the transcript as having spoken during the meeting
- **Unscheduled meetings**: For unscheduled meetings (Meet now meetings), the policy evaluates only users who are identified by the transcript as having spoken during the meeting.

#### Requirements

To review Teams meeting transcripts, you must turn on meeting transcripts for your organization, since meeting transcripts aren't turned on by default. [Learn more about turning on meeting transcripts for your organization](/en-us/microsoftteams/meeting-transcription-captions#use-the-teams-admin-center-to-turn-on-or-turn-off-transcription).

#### Limitations

The following limitations apply when reviewing Microsoft Teams meeting transcripts in Communication Compliance:

- You can set one or more of the following policy conditions:

    - Content matches any of these classifiers.
    - Content contains any of these sensitive info types.
    - Message contains any of these words.
    - Message contains none of these words.

    **Any other policy conditions are ignored.**[Choose conditions for your policies](communication-compliance-policies#choose-conditions-for-your-policies).

    Note

    If you don't set any conditions, the policy captures transcripts for all meetings.
- Only sensitive info types, keyword lists, and regulatory Microsoft provided trainable classifiers are detected. Regulatory trainable classifiers include:

    - [Corporate sabotage](trainable-classifiers-definitions#corporate-sabotage)
    - [Gifts and entertainment](trainable-classifiers-definitions#gifts--entertainment)
    - [Money laundering](trainable-classifiers-definitions#money-laundering)
    - [Regulatory collusion](trainable-classifiers-definitions#regulatory-collusion)
    - [Stock manipulation](trainable-classifiers-definitions#stock-manipulation)
    - [Unauthorized disclosure](trainable-classifiers-definitions#unauthorized-disclosure)

    Note

    All other classifiers, including business conduct classifiers, aren't detected.
- Ad-hoc (unscheduled) meetings aren't captured.
- External meetings aren't captured if the meeting organizer is outside your organization.
- Meeting recordings started by an uninvited user aren't captured.

#### Resolve an alert for a communication in a meeting transcript

After you create a policy, an alert triggers when the policy detects a transcript that contains offending content. The alert brings the offending content and background context to the attention of an investigator.

To resolve an alert related to a meeting transcript:

1. Select the **Source** tab and then review the transcript for the offending content. The **Source** tab shows the entire transcript. When you select the **Source** tab, the transcript automatically scrolls to the line that contains the policy match. The offensive keyword or phrase is highlighted.
2. Use the **Plain text** tab to do a line-by-line review of the text, including start and stop times in relation to the overall meeting time. Text is captured 30 seconds before and after the offending communication.
3. Select the **Translation** tab to review translations in up to eight languages for the **Plain text** tab. Messages in other languages are automatically converted to the display language of the reviewer.
4. Select the **User history** tab to see a historical view of all user message remediation activities, such as past notifications and escalations for policy matches.
5. Use **Resolve**, **Notify**, **Tag as**, **Escalate**, and **Escalate for investigation** options to resolve the alert. To learn more about these options, see Decide on a remediation action.

### Decide on a remediation action

After reviewing message details, choose from several remediation actions:

- **Resolve**: Selecting **Resolve** immediately removes the message from the **Pending** queue and prevents any further action on the message. When you select **Resolve**, you close the message without further classification. You can also mark the message as misclassified if the alerting process or any Microsoft provided trainable classifiers incorrectly generated it. The **Resolved** tab displays all resolved messages.

    To save investigators time when duplicate policy matches appear across multiple policies, the solution turns on the **Cross-policy resolution** setting (preview) by default. When you resolve a policy match, Communication Compliance automatically resolves all instances of the same policy match in any policy where it's detected, regardless of the reviewer's scope. The item history for each policy notes cross-policy resolution actions, and the number of **Resolved** items increments in the *Items and actions per policy* and *Items and actions per location* reports for all related policies.

    When the **Cross-policy resolution** setting is turned on, this message appears in the **Resolve** pane.

    ![Screenshot of the Resolve pane in Communication Compliance showing a notification that resolving this policy match also resolves matching instances in other policies.](media/communication-compliance-cross-policy-resolution-message.png)

    If you don't want to automatically resolve all instances of the same policy match when an investigator resolves a policy match, turn off the **Cross-policy resolution** setting. Anyone who can resolve messages (anyone with the *Communication Compliance*, *Communication Compliance Investigators*, or *Communication Compliance Analyst* role) knows if the setting is turned off because the message in the **Resolve** pane disappears. To turn off the setting, in the [Microsoft Purview portal](purview-portal), select **Settings** in the upper-right corner of the page, select **Communication Compliance**, then select the **Cross-policy resolution** setting.
- **Power Automate**: Use a Power Automate flow to automate process tasks for a message. By default, Communication Compliance includes the *Notify manager when a user has a Communication Compliance alert* flow template that reviewers can use to automate the notification process for users with message alerts. For more information about creating and managing Power Automate flows in Communication Compliance, see the [Consider Power Automate flows](communication-compliance-power-automate).
- **Tag as**: Tag the message as *Compliant*, *Noncompliant*, or *Questionable* as it relates to the policies and standards for your organization. You can also create a custom tag. Adding tags and tagging comments helps you micro-filter messages for escalations or as part of other internal review processes. After tagging is complete, you can also choose to resolve the message to move it out of the pending queue. You can filter on any tag value.
- **Notify**: Use **Notify** to assign a custom notice template to the message and send a warning notice to the user. Choose the appropriate notice template configured in the **Communication Compliance settings** area and select **Send** to email a reminder to the user that sent the message and to resolve the issue.
- **Escalate**: Use **Escalate** to choose other people in your organization who should review the message. Choose from a list of reviewers configured in the Communication Compliance policy to send an email notification requesting additional review of the message. The selected reviewer can use a link in the email notification to go directly to items escalated to them for review.
- **Escalate for investigation**: Use **Escalate for investigation** to create a new [eDiscovery (Premium) case](ediscovery-overview) for single or multiple messages. Provide a name and notes for the new case. The custodian is automatically filled in for you. You don't need any additional permissions to manage the case. Creating a case doesn't resolve or create a new tag for the message. You can select a total of 100 messages when creating an eDiscovery (Premium) case during the remediation process. Messages in all communication channels included in Communication Compliance are supported. For example, you could select 50 Microsoft Teams chats, 25 Exchange Online email messages, and 25 Viva Engage messages when you open a new eDiscovery (Premium) case for a user.
- **Remove message in Teams**: Use **Remove message in Teams** to block potentially inappropriate messages and content identified in messages from Microsoft Teams channels and 1:1 and group chats. This action includes Teams chat messages reported by users and chat messages detected using machine-learning and classifier-based Communication Compliance policies. Removed messages and content are replaced with a policy tip that explains that it's blocked and the policy that applies to its removal from view. Recipients are provided a link in the policy tip to learn more about the applicable policy and the review process. The sender receives a policy tip for the blocked message and content but can review the details of the blocked message and content for context regarding the removal.

### Create a custom tag

You can tag a policy match as *Compliant*, *Non-compliant*, or *Questionable* as it relates to the policies and standards for your organization. If you need more flexibility than the standard tags provide, create a custom tag. For example, you might want to create an *Escalated* tag so investigators can let other team members know that a policy match is already escalated. Since you can apply multiple tags to any policy match, using the same example, investigators could apply that tag and also apply the *Non-compliant* tag for a policy match.

Keep the following points in mind for custom tags:

- You can apply tags to policy matches that appear on the **Pending** tab.
- You can apply multiple tags to a policy match.
- You can create up to 10 custom tags per policy.
- You create custom tags at the policy level so if you want to use the same custom tag for multiple policies, you must recreate the tag for each policy.
- When you apply a custom tag to a policy match:
    - The tag appears in the **Tags** column in the list of policy matches. If you apply more than one tag, each tag appears in the **Tags** column.
    - The tag appears in the **Tags** filter. You can then select the checkbox for that tag to filter all policy matches by that tag.
    - A **Custom tag** column appears in the following reports: *Items and actions per policy*, *Items and actions per location*, and *Activity by user*.
- If you delete a custom tag for a policy:
    - It's removed from any previous items that you tagged with that custom tag.
    - You can no longer filter by that tag.

Tip

Any action you take with custom tags is tracked in the **History of remediation actions** pane. Select **View item history** to display this pane.

#### Create and apply a custom tag for a policy match

1. On **Policies**, select a policy to view the policy matches for that policy.
2. Select the checkbox for the policy match that you want to create a custom tag for. Select the checkboxes for multiple policy matches if you want to apply a custom tag in bulk.
3. Select **Tag as** on the command bar.
4. In the **Tag item** pane, select **Add a new tag**.
5. Enter the name of the new tag, then press Enter to add the new tag. 
    Note

    A custom tag must be between 3 and 64 characters and can't include special characters. Spaces and hyphens are allowed.
6. Select the checkbox for the new tag to apply it to the policy match.
7. In the **Comment** box, add a comment to describe the purpose of the tag (optional).
8. Select **Save**.

#### Edit or delete a custom tag

1. On **Policies**, select a policy to view the policy matches for that policy.
2. Select the checkbox for the policy match that has the custom tag you want to edit.
3. Select **Tag as** on the command bar.
4. In the **Tag item** pane, select the ellipsis next to the custom tag.
5. Select **Edit**, make your changes, or select **Delete** to delete the tag. 
    Important

    If you delete a custom tag, it's removed from any previous items that you tagged with that custom tag. You can no longer filter by that tag.
6. Select **Save**.

## Unresolve messages

When you resolve messages, the messages are removed from the **Pending** tab and displayed in the **Resolved** tab. Investigation and remediation actions aren't available for messages in the *Resolved* tab. However, you might need to take extra action on a message that you mistakenly resolved or that needs further investigation after initial resolution. Use the **Unresolve** command to move one or more messages from the **Resolved** tab back to the **Pending** tab.

### Unresolve a message

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation, then select a policy that contains the resolved message to view the policy matches.
4. Select the **Resolved** tab.
5. On the **Resolved** tab, select one or more messages.
6. On the command bar, select **Unresolve**.
7. On the **Unresolve item** pane, add any comments, then select **Save**.
8. Select the **Pending** tab to verify that the selected items are displayed.

### Archive message details outside of Communication Compliance (optional)

Export or download message details if you need to archive the messages in a separate storage solution. If you select one or more policy matches and then select **Download** in the bar over the list, you automatically add the selected messages to a .zip file that you can save in storage outside of Microsoft 365. The size limit for files downloaded by using **Download** is 3 MB.

#### Export a collection of message details that exceeds 3 MB in size

To download messages that cumulatively exceed 3 MB in size, use **Export files** (displayed in the upper-right corner of the **Policies** page). For example, you might want to download policy matches each week for archiving purposes. The download size limit for the **Export files** command is 3 GB. The maximum number of items depends on whether you select documents (limit of 1,000 items) or users (limit of 50,000). Files are exported to a .zip file that you can then download. The .zip file contains all the message files as well as a summary .TXT file that includes data for the following fields: Document, Doc ID, Custodian, Subject/title, File name, File type, Error, and Message.

On the **Exports** tab, the export has a status of *In progress* or *Ready to download*. To download a file that has a *Ready to download* status, select the files batch in the **Name** list, then select **Download export(s)** over the list.

You can either select the policy matches that you want to export, select **Export files**, and then select the list of documents or users you want to export, or you can select **Export files** and then select the documents, users, and date ranges that you want to export. After you select **Export**, it takes a few minutes for the job to complete. You receive an email notification with a link to the **Exports** tab when the export is ready to download. To download a file that has a *Ready to download* status, select the files batch in the **Name** list, then select **Download export(s)** over the list.

Note

To include attachments in exported files, you must select them manually in the list of policy matches. They're not automatically included with their parent message file.

Tip

You can also [create and download a Message details report](communication-compliance-reports-audits#export-a-message-details-report).