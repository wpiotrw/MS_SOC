---
layout: Conceptual
title: Considerations for Microsoft Purview to manage Microsoft 365 Copilot and Channel Agent in Teams for security and compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-m365-copilot-considerations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: yibingchen
ms.service: purview
ms.date: 2026-06-30T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: reference
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Learn about deployment details to manage Microsoft 365 Copilot and Channel Agent in Teams for security and compliance.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 21233e2c-9667-5d72-ec4e-1a261e1a454a
document_version_independent_id: 21233e2c-9667-5d72-ec4e-1a261e1a454a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-m365-copilot-considerations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-m365-copilot-considerations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-m365-copilot-considerations.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: 59dcf1d2-be30-9425-71ee-92772674533d
---

# Considerations for Microsoft Purview to manage Microsoft 365 Copilot and Channel Agent in Teams for security and compliance | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When you understand how you can use Microsoft Purview to [manage data security and compliance protections for Microsoft 365 Copilot](ai-m365-copilot) and [Channel Agent in Teams](ai-teams-channel-agent), use the following detailed information for any prerequisites, considerations, and exemptions that might apply to your organization. Be sure to read these in conjunction with [Microsoft 365 Copilot requirements](/en-us/microsoft-365-copilot/microsoft-365-copilot-requirements) and [Enterprise data protection in Microsoft 365 Copilot and Microsoft Copilot 365 Chat](/en-us/copilot/microsoft-365/enterprise-data-protection#what-is-enterprise-data-protection-in-copilot-for-microsoft-365-and-microsoft-copilot).

For licensing information to use these capabilities for Copilot, see the licensing and service description links at the top of the page. For licensing information for Copilot, see the [service description for Microsoft 365 Copilot](/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot).

## Information protection considerations for Microsoft 365 Copilot

Microsoft 365 Copilot, Microsoft 365 Copilot Chat, and agents have the capability to access data stored within your Microsoft 365 tenant, including mailboxes in Exchange Online and documents in SharePoint or OneDrive.

In addition to accessing Microsoft 365 content, Copilot and agents can also use content from the specific file you're working on in the context of an Office app session, regardless of where that file is stored. For example, local storage, network shares, cloud storage, or a USB stick. When files are open by a user within an app, access is often referred to as *data in use*.

Before you deploy licenses for Copilot, make sure you're familiar with the following details that help you strengthen your data protection solutions:

- If content grants a user VIEW usage rights but not EXTRACT:

    - When a user has this content open in an app, they won't be able to use Copilot.
    - Copilot won't summarize this content but can reference it with a link so the user can then open and view the content outside Copilot.
- You can further prevent Copilot and agents from summarizing labeled files and emails (whether encrypted or not) that are identified by a [Microsoft Purview Data Loss Protection policy](dlp-microsoft365-copilot-location-learn-about). Copilot and agents won't summarize this content but can reference it with a link so the user can then open and view the content outside Copilot.
- Just like your Office apps, Copilot and agents can access sensitivity labels from your organization, but not other organizations. For more information about labeling support across organizations, see [Support for external users and labeled content](sensitivity-labels-office-apps#support-for-external-users-and-labeled-content).
- An advanced PowerShell setting for sensitivity labels can [prevent Office apps from sending content to connected experiences](sensitivity-labels-office-apps#prevent-connected-experiences-that-analyze-content), which includes Microsoft 365 Copilot and agents.
- Copilot and agents can't access unopened documents in SharePoint and OneDrive when they're [labeled and encrypted with user-defined permissions](sensitivity-labels-sharepoint-onedrive-files#support-for-labels-configured-for-user-defined-permissions), unless the label is used as a [default sensitivity label that extends SharePoint permissions to downloaded documents](sensitivity-labels-sharepoint-extend-permissions) or they're directly referenced by typing "**/**" (and in both cases, the user has EXTRACT permissions). Copilot and agents can always access these documents for a user when they're open in the app (data in use).
- [Sensitivity labels that are applied to containers (groups and sites)](sensitivity-labels-teams-groups-sites#support-for-sensitivity-labels) aren't inherited by items in those containers. As a result, the items won't display their container label in Copilot and can't support sensitivity label inheritance. For example, Teams channel chat messages that are summarized from a team that's labeled as Confidential won't display that label for sensitivity context in Microsoft 365 Copilot Chat. Similarly, content from SharePoint site pages and lists won't display the sensitivity label of their container label. Containers that support sensitivity labels include Teams, SharePoint sites, Micrsosoft 365 Groups, Loop workspaces, and Viva Engage.
- If you're using SharePoint information rights management (IRM) library settings that restrict users from copying text, be aware that usage rights are applied when files are downloaded, and not when they're created or uploaded to SharePoint. If you don't want Copilot and agents to summarize these files when they're at rest, use sensitivity labels that apply encryption without the EXTRACT usage right.
- Unlike other automatic labeling scenarios, an inherited label when you create new content will replace a lower priority label that was manually applied.
- When an inherited sensitivity label can't be applied, the text won't be added to the destination item. For example:

    - The destination item is read-only
    - The destination item is already encrypted and the user doesn't have permissions to change the label (requires EXPORT or FULL CONTROL usage rights)
    - The inherited sensitivity label isn't published to the user
- If a user asks Copilot or agents to create new content from labeled and encrypted items, label inheritance isn't supported when the encryption is configured for [user-defined permissions](encryption-sensitivity-labels#let-users-assign-permissions) or if the encryption was applied independently from the label. The user won't be able to send this data to the destination item.
- Because [Double Key Encryption (DKE)](double-key-encryption) is intended for your most sensitive data that's subject to the strictest protection requirements, Copilot and agents can't access this data. As a result, items protected by DKE won't be returned by Copilot, and if a DKE item is open (data in use), you won't be able to use Copilot in the app.
- Sensitivity labels that [protect Teams meetings and chat](sensitivity-labels-meetings) aren't currently recognized by Copilot and agents. For example, data returned from a meeting chat or channel chat won't display an associated sensitivity label, copying chat data can't be prevented for a destination item, and the sensitivity label can't be inherited. This limitation doesn't apply to meeting invites, responses, and calendar events that are protected by sensitivity labels.
- For Microsoft 365 Copilot Chat (formerly known as Business Chat, Graph-grounded chat, and Microsoft 365 Chat):

    - When meeting invites have a sensitivity label applied, the label is applied to the body of the meeting invite but not to the metadata, such as date and time, or recipients. As a result, questions based just on the metadata return data without the label. For example, "What meetings do I have on Monday?" Questions that include the meeting body, such as the agenda, return the data as labeled.
    - If content is encrypted independently from its applied sensitivity label, and that encryption doesn't grant the user EXTRACT usage rights (but includes the VIEW usage right), the content can be returned by Copilot and therefore sent to a source item. An example of when this configuration can occur if a user has applied Office restrictions from Information Rights Management when a document is labeled "General" and that label doesn't apply encryption.
    - If you're using the [extension capabilities that include plugins and the Microsoft Graph Connector](/en-us/microsoftteams/platform/copilot/how-to-extend-copilot), sensitivity labels and encryption that are applied to this data from external sources aren't recognized by Microsoft 365 Copilot Chat. Most of the time this limitation won't apply because the data is unlikely to support sensitivity labels and encryption, although one exception is Power BI data. You can always disconnect the external data sources by using the [Microsoft 365 admin center to turn off those plugins for users](/en-us/microsoft-365/admin/manage/manage-plugins-for-copilot-in-integrated-apps), and [disconnect connections that use a Graph API connector](/en-us/graph/connecting-external-content-manage-connections).

App-specific exceptions:

- **Microsoft 365 Copilot in Outlook**: You must have a minimum version of Outlook to use Microsoft 365 Copilot for encrypted items in Outlook:

    - **Outlook (Classic) for Windows**: Starting with version 2408 in Current Channel and Monthly Enterprise Channel
    - **Outlook for Mac**: Version 16.86.609+
    - **Outlook for iOS**: Version 4.2420.0+
    - **Outlook for Android**: Version 4.2420.0+
    - **Outlook on the web**: Yes
    - [**New Outlook for Windows**](https://support.microsoft.com/office/getting-started-with-the-new-outlook-for-windows-656bb8d9-5a60-49b2-a98b-ba7822bc7627): Yes
- **Microsoft 365 Copilot in Edge**, **Microsoft 365 Copilot in Windows**: Unless [data loss prevention (DLP) is used in Edge](/en-us/deployedge/microsoft-edge-security-dlp), Copilot can reference encrypted content from the active browser tab in Edge when that content doesn't grant the user EXTRACT usage rights. For example, the encrypted content is from Office for the web or Outlook for the web.

### Will an existing label be overridden for sensitivity label inheritance?

Summary of outcomes when Microsoft 365 Copilot automatically applies protection with sensitivity label inheritance:

| Existing label | Override with sensitivity label inheritance |
| --- | --- |
| Manually applied, lower priority | Yes |
| Manually applied, higher priority | No |
| Automatically applied, lower priority | Yes |
| Automatically applied, higher priority | No |
| Default label from policy, lower priority | Yes |
| Default label from policy, higher priority | No |
| Default sensitivity label for a document library, lower priority | Yes |
| Default sensitivity label for a document library, higher priority | No |

### Copilot honors existing protection with the EXTRACT usage right

Although you might not be very familiar with the individual usage rights for encrypted content, they've been around a long time. From Windows Server Rights Management, to Active Directory Rights Management, to the cloud version that became Azure Information Protection with the Azure Rights Management service.

If you've ever received a "Do Not Forward" email, it's using usage rights to prevent you from forwarding the email after you've been authenticated. As with other bundled usage rights that map to common business scenarios, a Do Not Forward email grants the recipient usage rights that control what they can do with the content, and it doesn't include the FORWARD usage right. In addition to not forwarding, you can't print this Do Not Forward email, or copy text from it.

The usage right that grants permission to copy text is **EXTRACT**, with the more user-friendly, common name of **Copy**. It's this usage right that determines whether Copilot or agents can display text to the user from encrypted content.

Note

Because the Full control (OWNER) usage right includes all the usage rights, EXTRACT is automatically included with Full control.

When you use the Microsoft Purview portal to configure a sensitivity label to apply encryption, the first choice is whether to assign the permissions now, or let users assign the permissions. If you assign now, you configure the permissions by either selecting a predefined permission level with a preset group of usage rights, such as Co-Author or Reviewer. Or, you can select custom permissions where you can individually select available usage rights.

In the Microsoft Purview portal, the EXTRACT usage right is displayed as **Copy and extract content(EXTRACT)**. For example, the default permission level selected is **Editor**, where you see **Copy and extract content(EXTRACT)** is included. As a result, content protected with this encryption configuration can be returned by Copilot and agents

![Configuration of usage rights for a sensitivity label where the permissions include EXTRACT.](media/sensitivity-choose-permissions-extract.png)

If you select **Custom** from the dropdown box, and then **Full control(OWNER)** from the list, this configuration will also grant the EXTRACT usage right.

Note

The person applying the encryption always has the EXTRACT usage right, because they are the Rights Management owner. This special role automatically includes all usage rights and some other actions, which means that content a user has encrypted themselves is always eligible to be returned to them by Microsoft 365 Copilot, Microsoft 365 Copilot Chat, and agents. The configured usage restrictions apply to other people who are authorized to access the content.

Alternatively, if you select the encryption configuration to let users assign permissions, for Outlook, this configuration includes predefined permissions for Do Not Forward and Encrypt-Only. The Encrypt-Only option, unlike Do Not Forward, does include the EXTRACT usage right.

When you select custom permissions for Word, Excel, and PowerPoint, users select their own permissions in the Office app when they apply the sensitivity label. There are currently two versions of the dialog box. In the older version, they're informed that from the two selections, **Read** doesn't include the permission to copy content, but **Change** does. These references to copy refer to the EXTRACT usage right. If the user selects **More Options**, they can add the EXTRACT usage right to Read by selecting **Allow users with read access to copy content**.

![Older user dialog box to select permissions that include EXTRACT usage right.](media/restricted-access-dialogbox.png)

In the latest version of the dialog box, **Read** and **Change** is replaced with permission levels where the descriptions that state copy isn't allowed won't include the EXTRACT usage right. The permission levels that do include EXTRACT are **Editor** and **Owner**. For example:

![Newer user dialog box to select permission levels that include EXTRACT usage right.](media/new-permissions-dialogbox.png)

Tip

If you need to check whether a document you're authorized to view includes the EXTRACT usage right, open it in the Windows Office app and customize the status bar to show **Permissions**. Select the icon next to the sensitivity label name to display **My Permission**. View the value for **Copy**, which maps to the EXTRACT usage right, and confirm whether it displays **Yes** or **No**.

For emails, if the permissions aren't displayed at the top of the message in Outlook for Windows, select the information banner with the label name, and then select **View Permission**.

Copilot and agents honor the EXTRACT usage right for a user, however it was applied to the content. Most times, when the content is labeled, the usage rights granted to the user match those from the sensitivity label configuration. However, there are some situations that can result in the content's usage rights being different from the applied label configuration:

- [The sensitivity label is applied after usage rights are already applied](encryption-sensitivity-labels#what-happens-to-existing-encryption-when-a-labels-applied)
- [Usage rights are applied after a sensitivity label has been applied](sensitivity-labels-office-apps#information-rights-management-irm-options-and-sensitivity-labels)

For more information about configuring a sensitivity label for encryption, see [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels).

For technical details about the usage rights, see [Configure usage rights for the Azure Rights Management service](rights-management-usage-rights).

## Information protection considerations for Channel Agent in Teams

Channel Agent in Teams uses sensitivity labeled information to answer user questions that might be derived from its channel files in SharePoint, channel messages and meetings, and standard meetings. For these sensitivity labels, they have many of the same information protection considerations as those listed in the previous section for Microsoft 365 Copilot. For example:

- The highest priority label is displayed in the chat and is used for label inheritance when new AI-generated content is created.
- The content from items encrypted with user-defined permissions and Double Key Encryption isn't accessible.
- Sensitivity labels applied to the channel from the labels' [groups and sites](sensitivity-labels-teams-groups-sites#support-for-sensitivity-labels) configuration aren't used by Channel Agent in Teams.

However, unlike sensitivity labels in Microsoft 365 Copilot:

- Although Channel Agent in Teams honors the EXTRACT permission like Copilot does for the requesting user, the permissions aren't checked for all users in the channel. As a result, Channel Agent could summarize the content of items that one or more users in the channel don't have permissions to open. The requesting user is warned of this risk and administrators have the ability to [turn off Channel Agent in Teams](/en-us/microsoftteams/manage-apps).
- You can't prevent Channel Agent from summarizing labeled files that are identified by a [Microsoft Purview Data Loss Protection policy](dlp-microsoft365-copilot-location-learn-about).
- You can't prevent users from copying chat responses from Channel Agent or prevent these responses from being used by another channel agent in Teams channels.
- [Information barriers](information-barriers) aren't supported for Channel Agent and as a result, these it might return information that crosses barriers.
- Channel Agent in Teams isn't supported with [Microsoft Purview Customer Key](customer-key-overview).

## Compliance management considerations for Microsoft 365 Copilot

Compliance management for interactions with Microsoft 365 Copilot and agents extend across the following apps: Word, Excel, PowerPoint, Outlook, Teams, Loop and Copilot Pages, Whiteboard, OneNote, and Microsoft 365 Copilot Chat (formerly Business Chat, Graph-grounded chat, and Microsoft 365 Chat).

Note

Compliance management for Microsoft 365 Copilot Chat includes prompts and responses to and from the public web when users are signed in and select the **Work** option rather than **Web**.

Compliance tools identify the source Microsoft 365 Copilot interactions by the name of the app. For example, **Copilot in Word**, **Copilot in Teams**, and **Microsoft 365 Chat** (for Microsoft 365 Copilot Chat).

Before your organization uses Microsoft 365 Copilot, make sure you're familiar with the following details to support your compliance management solutions:

- The audit data is designed for data security and compliance purposes, and provides comprehensive visibility into Microsoft 365 Copilot interactions for these use cases. For example, to discover data oversharing risks or to collect interactions for regulatory compliance or legal purposes. It's not intended to be used as the basis for Copilot usage reporting.

    Note

    Any aggregated metrics that you build on top of this audit data such as "prompt count" or "active user count" might not be consistent with the corresponding data points in the official Copilot usage reports provided by Microsoft. Microsoft can't provide guidance on how to use audit log data as the basis for usage reporting, nor can Microsoft guarantee that aggregated usage metrics built on top of audit log data will match similar usage metrics reported in other tools.

    To access accurate information about Copilot usage, use one of the following reports: the [Microsoft 365 Copilot usage report](/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage) in the Microsoft 365 Admin Center or the [Copilot Dashboard](/en-us/viva/insights/org-team-insights/copilot-dashboard) in Viva Insights.
- Auditing captures the Microsoft 365 Copilot activity of search, but not the actual user prompt or response. For this information, use eDiscovery. Or from Microsoft Purview Data Security Posture Management for AI, use [**AI interaction**](dspm-for-ai-considerations#activity-explorer-events) from the **Activity explorer** page.
- Admin-related changes for auditing Copilot aren't yet supported.
- Device identify information isn't currently included in the audit details.
- Retention policies for Copilot interactions don't inform users when messages are deleted as a result of a retention policy.

App-specific exceptions:

- **Microsoft 365 Copilot in Teams**:
    - If transcripts are turned off, the capabilities for auditing, eDiscovery, and retention aren't supported
    - If transcripts are referenced, this action isn't captured for auditing
    - For Microsoft 365 Copilot Chat, Copilot currently can't retain as cloud attachments, referenced files that it returns to users. Files referenced by users are supported to be retained as cloud attachments.