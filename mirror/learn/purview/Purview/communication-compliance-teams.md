---
layout: Conceptual
title: Microsoft Teams and Microsoft Purview Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-teams
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learning about Communication Compliance, part of the insider risk solution set, from the Microsoft Teams perspective (this is part of the Microsoft Purview Communication Compliance functionality).
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
audience: admin
ms.reviewer: anwara
ms.date: 2025-02-18T00:00:00.0000000Z
search.appverid: MET150
ms.collection:
- purview-compliance
- M365-collaboration
locale: en-us
document_id: af217c32-1a2f-7f44-a88d-fc721571bf21
document_version_independent_id: af217c32-1a2f-7f44-a88d-fc721571bf21
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-teams.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-teams
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-teams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 851b3f33-739d-969a-a92c-de425775d322
---

# Microsoft Teams and Microsoft Purview Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

Microsoft Purview Communication Compliance is an insider risk solution in Microsoft 365 that helps you minimize communication risks by helping you detect, capture, and act on inappropriate messages in your organization.

For Microsoft Teams, Communication Compliance helps you identify the following types of inappropriate content in Teams channels, private Teams channels, or in 1:1 and group chats:

- Offensive, profane, and harassing language
- Adult, racy, and gory images
- Sharing of sensitive information

Watch the following video to learn how to detect communication risks in Microsoft Teams with Communication Compliance: 

You can also detect offensive communications included in Microsoft Teams transcripts (preview).

For more information on Communication Compliance and how to configure policies for your organization, see [Learn about Communication Compliance](communication-compliance).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## How to use Communication Compliance in Microsoft Teams

Communication Compliance and Microsoft Teams are tightly integrated and can help you minimize communication risks in your organization. After you configure your first Communication Compliance policies, you can actively manage inappropriate Microsoft Teams messages and content that the solution automatically flags in alerts.

### Getting started

To get started with Communication Compliance in Microsoft Teams, [plan](communication-compliance-plan) and create predefined or custom policies to identify inappropriate user activities in Teams channels or in 1:1 and group chats. Remember that you need to [configure](communication-compliance-configure) some permissions and basic prerequisites as part of the configuration process.

Teams administrators can configure Communication Compliance policies at the following levels:

- **User level**: Apply these policies to an individual Teams user or to all Teams users in your organization. These policies cover messages that users send in 1:1 or group chats. The solution automatically detects chat communications for the users across all Microsoft Teams where the users are a member.
- **Teams level**: Apply these policies to a Microsoft Teams channel, including a Private channel. These policies cover messages sent in the Teams channel only.

### Report a message in Microsoft Teams

Note

After you create your first Communication Compliance policy, the organization implements the *User-reported messages* policy. It can take up to 30 days for this feature to become available after you create your first policy.

By default, Teams messaging policies in the [Teams admin center](/en-us/microsoftteams/manage-teams-in-modern-portal) enable the *Report inappropriate content* option for Teams personal and group chat messages. This option lets users in your organization submit inappropriate internal chat messages for review by Communication Compliance reviewers for the policy. For more information about user-reported messages in Communication Compliance, see [Communication Compliance policies](communication-compliance-policies#user-reported-messages-policy).

To access the feature, a user selects **More options** (...) &gt; **More actions** &gt; **Report this message** from a Teams chat.

![Report this message menu.](media/communication-compliance-report-message.png)

In the next dialog box, the user selects the **Inappropriate - Harassment, violence, nudity, and disturbing content** option from the **Select a problem** list.

![Report a message choices.](media/communication-compliance-report-message-choices.png)

Note

Microsoft Defender for Office 365 manages the other choice in the list (**Security risk- Spam, phishing, malicious content**), if available. Depending on which policy options are turned on in the Microsoft Teams admin center, the user might also be presented with just the **Inappropriate - Harassment, violence, nudity, and disturbing content** option. [Learn more about the Microsoft Defender for Office setting](https://go.microsoft.com/fwlink/?linkid=2226727)

After submitting the message for review, the user receives a confirmation of the submittal in Microsoft Teams. Other participants in the chat don't see this notification.

Users in your organization automatically get the global policy unless you create and assign a custom policy. Edit the settings in the global policy or create and assign one or more custom policies to turn on or turn off this feature. For more information, see [Manage messaging policies in Teams](/en-us/microsoftteams/messaging-policies-in-teams).

### Act on inappropriate messages in Microsoft Teams

After you configure your policies and receive Communication Compliance alerts for Microsoft Teams messages, compliance reviewers in your organization can act on these messages. This process also includes user-reported messages if your organization enables that option. Reviewers help safeguard your organization by reviewing Communication Compliance alerts and removing flagged messages from view in Microsoft Teams.

![Remove a message in Teams.](media/communication-compliance-remove-teams-message.png)

Important

If a user reports a message that was sent before they were added to a chat, Teams message remediation isn't supported; the Teams message can't be removed.

When reviewers remove messages and content, viewers see notifications that explain the message or content was removed and what policy is applicable to the removal. The sender of the removed message or content also receives a removal notification and gets the original message content for context relating to its removal. The sender can view the specific policy condition that applies to the message removal.

Example of policy tip seen by sender:

![Policy tip for sender.](media/communication-compliance-warning-1.png)

Example of policy notification seen by the sender:

![Policy condition info for sender.](media/communication-compliance-warning-2.png)

Example of policy tip seen by recipient:

![Policy tip for recipient.](media/communication-compliance-warning-3.png)