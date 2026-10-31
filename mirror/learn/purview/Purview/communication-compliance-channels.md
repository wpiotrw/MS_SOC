---
layout: Conceptual
title: Detect channel signals with Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-channels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn more about detecting channel signals with Communication Compliance.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-08-28T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
- microsoft-365-copilot
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: 2a2e470e-c6cb-81cd-42a9-cf4da613eea5
document_version_independent_id: 2a2e470e-c6cb-81cd-42a9-cf4da613eea5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-channels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-channels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-channels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- Azure
- M365
__autotagging_hash:
- 12E31829D0D72BA8DD4905361217955C21A2805D849738D6715B933B1601DE4F
platformId: afee7312-1a46-9f2d-737a-d0d94e568697
---

# Detect channel signals with Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

With Communication Compliance policies, you can choose to analyze messages in one or more of the following communication platforms as a group or as standalone sources. Your organization retains original messages captured across these platforms in the original platform location in accordance with your [retention and hold policies](data-lifecycle-management). Communication Compliance policies retain copies of messages used for analysis and investigation for as long as a policy is in place, even if users leave your organization and their mailboxes are deleted. When you delete a communication policy, you also delete copies of messages associated with the policy.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Generative AI

Important

To detect inappropriate or risky interactions for non-Microsoft 365 AI data, you need to enable [pay-as-you-go billing](/en-us/purview/purview-billing-models) in your organization. Non-Microsoft 365 AI data includes information from other generative AI applications from Microsoft and other connected external AI applications. This data type includes [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and any connected or cloud AI application. There aren't any pay-as-you-go billing requirements or charges for Microsoft 365 detecting inappropriate or risky interaction for Microsoft 365 Copilot data.

Communication Compliance supports numerous generative AI applications. You can use Communication Compliance policies to analyze interactions (prompts and responses) entered into these applications and help detect inappropriate or risky interactions or sharing of confidential information. Communication Compliance supports the following generative AI applications:

- **Microsoft Copilot experiences**: Support for user interactions in [Microsoft 365 Copilot](/en-us/copilot/microsoft-365/) and other Copilots built using [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/).
- **Enterprise AI apps**: Non-Copilot AI apps that you onboard or connect to your organization by using methods like [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) registration and [data connectors](data-map).
- **Other AI apps**: Other AI applications detected through browser activity and categorized as *Generative AI* in the Defender for Cloud Apps catalog.

Use the following links to learn more about creating a Communication Compliance policy that detects Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions and other Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and Microsoft 365 Copilot Chat:

- [Configure a Communication Compliance policy to detect for Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions](communication-compliance-copilot)
- [Microsoft Purview data security and compliance protections for generative AI apps](ai-microsoft-purview)

## Microsoft Teams

You can analyze chats in public and private Microsoft Teams channels and individual communications. When you assign users to a Communication Compliance policy with Microsoft Teams coverage selected, the solution automatically detects chat communications across all Microsoft Teams where users are a member.

To learn how to detect communication risks in Microsoft Teams with Communication Compliance, watch the following video: 

Microsoft Purview Communication Compliance automatically includes Microsoft Teams coverage for predefined policy templates and selects it as the default in the custom policy template. Teams transcripts are also included. Teams chats matching Communication Compliance policy conditions might take up to 48 hours to process.

For Teams private chat and private channels, Communication Compliance policies support modern attachment analysis. Shared Channels support in Teams is handled automatically and doesn't require additional Communication Compliance configuration changes. Communication Compliance policies do not support modern attachments in shared channels. The following table summarizes Communication Compliance behavior when sharing Teams channels with groups and users:

| **Scenario** | **Communication Compliance behavior** |
| --- | --- |
| **Share a channel with an internal team** | Communication Compliance policies apply to included users and all messages in the shared channel |
| **Share a channel with an external team** | Communication Compliance policies apply to internal included users and messages in the shared channel for the internal organization |

Modern attachments are files sourced from [OneDrive](/en-us/onedrive/plan-onedrive-enterprise#modern-attachments) or [SharePoint](/en-us/sharepoint/dev/solution-guidance/modern-experience-customizations) sites that are included in Teams messages. Text is automatically extracted from these attachments for automated processing and potential matches with active Communication Compliance policy conditions and classifiers. There's no extra configuration necessary for modern attachment detection and processing. Text is only extracted for attachments matching policy conditions at the time the message is sent. Text isn't extracted for attachments for messages with policy matches, even if the attachment also has a policy match.

Modern attachment analysis is supported for the following file types:

- Microsoft Word (.docx)
- Microsoft Excel (.xlsx, .xls, .csv)
- Microsoft PowerPoint (.pptx)
- Text (.txt)
- Portable Document Format (.pdf)

Modern attachments like files hosted on OneDrive or SharePoint sites are supported if shared as Teams messages. The extracted text from these attachments is saved as .txt files and included with the Teams message in Communication Compliance. Additionally, the URL to the original file is attached separately for review. Extracted text for modern attachments is included with the associated message on the **Pending** tab of the policy's dashboard. The extracted text for an attachment is named as the attachment file name (and format extension) and the .txt extension. For example, the extracted text for an attachment named *ContosoBusinessPlan.docx* appears as *ContosoBusinessPlan.docx.txt* in the **Pending** tab of the policy's dashboard.

Select the extracted attachment text to view the details in the *Source* and *Plain text* views. After reviewing, you can resolve or take action on the attachment text using the command bar controls. You can also download the attachment for review outside of the Communication Compliance review process.

Use the following group management configurations to bring individual user chats and channel communications in Teams in scope:

- **For Teams chats:** Assign individual users or assign a [distribution group](https://support.office.com/article/Distribution-groups-E8BA58A8-FAB2-4AAF-8AA1-2A304052D2DE) to the Communication Compliance policy. This setting is for one-to-one or one-to-many user/chat relationships.
- **For Teams channel communications:** If any member of the channel is a scoped user within a policy and the **Inbound** direction is configured as the **Communication direction** for the policy, all messages sent within the channel are subject to review by Communication Compliance, even for users in the channel that aren't explicitly scoped.

    For example, consider the following set of circumstances:
- User A is scoped in a Communication Compliance policy.

    - User A is a member of a Teams channel.
    - **Inbound** is selected as the direction for the policy.
    - User B and User C aren't scoped in a Communication Compliance policy.
    - User B and User C are members of the same Teams channel as User A.
    - User B and User C are posting in the channel, but aren't communicating directly with User A.

    In this scenario, a message from User B or User C can be flagged as a policy match even if they don't communicate directly with user A. This result is because User A is technically receiving the message from User B and User C since they're part of the same channel. In this case, if you want to exclude User B and User C from potentially being flagged for policy matches, select a different communication direction in the applicable Communication Compliance policy.

    On the other hand, if User B and User C have a conversation on another channel or in a chat that doesn't include User A, the conversation isn't reviewed by the policy even if the conversation would otherwise provide a policy match since User A, the scoped user, isn't included in the conversation.
- **For Teams chats with hybrid email environments**: Communication Compliance can detect chat messages for organizations with an Exchange on-premises deployment or an external email provider that enabled Microsoft Teams. You must create a distribution group for the users with on-premises or external mailboxes. When creating a Communication Compliance policy, assign this distribution group using **Choose users and groups** in the policy workflow. For more information about the requirements and limitations for enabling cloud-based storage and Teams support for on-premises users, see [Search for and export Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).

Tip

For a more flexible configuration and to reduce administrative overhead, consider using an [adaptive scope](purview-adaptive-scopes) instead of a distribution group.

## Exchange

You can analyze all mailboxes hosted on Microsoft Exchange Online as part of your Microsoft 365 or Office 365 subscription. Exchange email messages and attachments that match Communication Compliance policy conditions might take about 24 hours to process. Supported attachment types for Communication Compliance are the same as the [file types supported for Exchange mail flow rule content inspections](/en-us/exchange/security-and-compliance/mail-flow-rules/inspect-message-attachments#supported-file-types-for-mail-flow-rule-content-inspection).

## Viva Engage

You can also analyze private messages, public conversations, and associated attachments in Microsoft Viva Engage communities. When you add users to a Communication Compliance policy that includes Viva Engage as a defined channel, the analysis includes communications across all Viva Engage communities that a user is a member of. Viva Engage chats without attachments that match Communication Compliance policy conditions can take up to one hour to process. Viva Engage chats with attachments can take up to 24 hours to process.

You must configure Viva Engage in [Native Mode](/en-us/viva/engage/overview-native-mode) for Communication Compliance policies to detect Viva Engage communications and attachments. In Native Mode, all Viva Engage users are in Microsoft Entra ID, all groups are Microsoft 365 Groups, and all files are stored in SharePoint.

## Non-Microsoft sources

You can analyze communications for data imported into all mailboxes in your Microsoft 365 organization from non-Microsoft sources like [Instant Bloomberg](archive-instant-bloomberg-data), [Slack](archive-slack-data), [Zoom](archive-zoommeetings-data), SMS, and many others. For a full list of connectors supported in Communication Compliance, see [Learn about connectors for third-party data](archive-third-party-data).

You must configure a [third-party connector](archive-third-party-data) for your Microsoft 365 organization before you can assign the connector to a Communication Compliance policy. The **Third-Party Sources** section of the Communication Compliance policy workflow only displays currently configured third-party connectors.

Note

Content from all non-Microsoft channels (such as WhatsApp or Instant Bloomberg) takes 24 to 48 hours for detection by Communication Compliance, depending on how frequently the data is imported from those non-Microsoft channels.

## Channel limits

| Channel | Current limit |
| --- | --- |
| All channels | Maximum of 25 attachments per policy match |
| Teams public channels | Maximum of 250 users for public channel messages for static scopes with users |
| Teams public channels | No support or coverage for public channel messages for adaptive scopes with users |