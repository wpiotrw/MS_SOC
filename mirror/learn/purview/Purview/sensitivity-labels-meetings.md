---
layout: Conceptual
title: Use sensitivity labels to protect calendar items, Teams meetings, and chat | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
audience: Admin
ms.topic: how-to
ms.date: 2026-06-10T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
description: Configure sensitivity labels to protect calendar items, and Teams meetings and chat, by enforcing settings and applying label protection actions.
locale: en-us
document_id: e973b34e-59bf-0e55-9847-63ce64ff8779
document_version_independent_id: e973b34e-59bf-0e55-9847-63ce64ff8779
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-meetings.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-meetings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-meetings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 454cfd43-fdb4-7a70-ac15-b1240b1cd613
---

# Use sensitivity labels to protect calendar items, Teams meetings, and chat | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

You won't be able to configure all the options referenced on this page if a [Teams Premium license](/en-us/MicrosoftTeams/enhanced-teams-experience) isn't found for your tenant. For those settings, you'll see an information bar in the Microsoft Purview portal that your organization doesn't have this license.

In addition to using [sensitivity labels](sensitivity-labels) to protect documents and emails, you can extend sensitivity labels to protect meeting invites and responses that use Outlook and Teams, and to protect Teams meetings and chat:

- Meeting organizers apply a sensitivity label to meeting invites from Outlook or Teams. Recipients in your organization see the sensitivity label and all recipients see any headers or footers as configured content markings. Optionally, the meeting invite can be encrypted so only authorized people can see it and access the meeting link. Usage rights can further restrict access, for example, preventing the invite from being forwarded.

    The encryption works similarly to how you can apply a label with encryption to an email. As with [email encryption](ome), if recipients aren't using an email client that can decrypt this meeting invite, they're directed to Outlook on the web or the encryption portal where they can read the invite and access the meeting link.
- The sensitivity label from the meeting invite is automatically inherited by the meeting and protects it even before the meeting starts. For example, prevent copying from the chat if this has been configured for the label. When the meeting starts, it will enforce any meeting options, such as who can bypass the lobby and present.
- Participants from your organization see the label during the Teams meetings. Any meeting settings applied by the label can't be changed directly in Teams. When a label enforces these settings, users see a lock and message that explains the settings are applied by a sensitivity label.

Meeting settings that you can apply with a sensitivity label:

- Who can bypass the lobby
- Who can present
- Who can record and transcribe
- Encryption for meeting video and audio
- Automatically record
- Video watermark for screen sharing and camera streams
- Prevent copying and forwarding of meeting chat, live caption, and transcripts
- Detect sensitive content during screen sharing

Users can apply sensitivity labels to meeting invites when they use Outlook or Teams:

- For Outlook, applying, changing, and viewing sensitivity labels for meeting invites and appointments are supported with Outlook on the web, and with minimum versions of Windows, macOS, iOS and Android. For other versions, platforms, and email clients, encrypted meeting invites can be opened in the same way as encrypted email.
- For Teams, applying, changing, and viewing sensitivity labels for meeting invites are supported with Teams on the web, and with minimum versions of Windows, macOS, iOS and Android.

For more information about those minimum versions, see the Requirements section.

Example showing a Teams meeting invite that has the label **Highly confidential**, and the label applies encryption settings that prevent the invite from being forwarded:

![Example labeled Teams meeting invite that prevents the invite from being forwarded.](media/example-protected-teams-invite.png)

## Requirements

Review [license requirements for sensitivity labeling](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling) to ensure your organization has the right licensing available.

To apply a sensitivity label to meeting invites and appointments using Outlook, users must use Outlook on the web or use built-in labeling from Microsoft 365 Apps for enterprise. For supported versions across Windows, macOS, iOS, and Android, see the [capabilities table for Outlook](sensitivity-labels-versions#sensitivity-label-capabilities-in-outlook) and the row that specifies labeling for **Calendar items**.

To apply a sensitivity label to meeting invites using Teams, enforce meeting options and chat, and display and change sensitivity labels in Teams non-channel meetings, users must use Teams on the web with Edge or Chrome, or one of the following Teams clients:

- **Teams client for Windows**: 1.5.00.32158+
- **Teams client for macOS**: 1.5.00.32154+
- **Teams mobile app for iOS**: 5.23.0+
- **Teams mobile app for Android**: 1416/1.0.0.2023235001+

Important

If meeting participants or organizers don't use a Teams client that meets these requirements, the configured label meeting options can't be enforced for these users.

Sensitivity labels that apply [S/MIME protection](sensitivity-labels-office-apps#configure-a-label-to-apply-smime-protection-in-outlook) or [Double Key Encryption (DKE)](encryption-sensitivity-labels#double-key-encryption) can't be used to protect calendar items, Teams meetings, and chat.

## Limitations

- Preventing copying chat and meeting-related content has some limitations that are listed in the Prevent copying and forwarding for chats and meeting content section on this page.
- Calendar items don't support label encryption that uses S/MIME or Double Key Encryption. You must use the default encryption that uses the Azure Rights Management service, with either admin-defined permissions (the option **Assign permissions now**) or user-defined permissions (the option **Let users assign permissions**).
- Automatic and recommended labeling isn't supported.
- No support for mailboxes on-premises; user mailboxes must be in Exchange Online.

**Specific to Outlook:**

- No support for group calendar meeting invites; participants must be specific users.
- As with labeled and encrypted email, if somebody forwards a meeting invite from an email client other than Outlook, any applied encryption persists but information about the sensitivity label is removed from the email headers.
- The [Share to Teams](/en-us/microsoftteams/teams-outlook-share-teams) option doesn't support sensitivity labels. If the selected sensitivity label applies encryption, the action is prevented with a message that the content is restricted. If the selected sensitivity label doesn't apply encryption, the action isn't prevented but the sensitivity label isn't displayed in Teams.
- For Outlook for Windows, when a labeled and encrypted meeting invite or response is sent, the following configuration setting must be enabled: **Outlook Options** &gt; **Advanced** &gt; **International options** &gt; **Automatically select encoding for outgoing messages**
- Shared calendars:

    - When a user shares their calendar with others, only the calendar owner can create and change sensitivity labels for meetings in that calendar.
    - A shared mailbox calendar doesn't support applying and changing sensitivity labels for meetings.
- For a meeting series:

    - The organizer can apply a sensitivity label for the meeting series but not to individual occurrences.
    - Exceptions for a meeting series will be labeled (and encrypted if applicable) only if they're created after the label is applied to the meeting series. Existing exceptions, including those in the future, won't be labeled.
    - If the organizer changes the meeting body or attachments for a meeting series after it's encrypted by a sensitivity label, existing exceptions won't be updated with those changes.
    - If the organizer changes any meeting attributes (such as start date, end date, location, the meeting body, or attachments) for a specific occurrence in a series after it's encrypted by a sensitivity label, this action automatically creates an exception for the series with the same label for the meeting series.

**Specific to Teams**:

- While a meeting is in session, a sensitivity label can't prevent participants from inviting people to join by copying the meeting link, or by sharing via default email or the Outlook calendar. These choices are from the Teams meeting **Share invite** option.
- If there's a label change made in Teams while the meeting is progress, any changes to the following meeting options won't take effect for the current meeting unless the organizer ends and restarts the meeting:

    - Who can record and transcribe
    - Encryption for meeting video and audio
    - Automatically record and transcribe
    - Video watermark for screen sharing and camera streams
- The following meeting options won't take effect for a Meet Now meeting:

    - Who can record and transcribe
    - Encryption for meeting video and audio
    - Automatically record and transcribe
    - Video watermark for screen sharing and camera streams
- Sensitivity labels can't be applied to live events.
- Labeling meeting invites with Graph APIs isn't supported.

## How to configure a sensitivity label to protect calendar items, Teams meetings, and chat

1. Follow the general instructions to [create or edit a sensitivity label](create-sensitivity-labels#create-and-configure-sensitivity-labels) and make sure the following [label scopes](sensitivity-labels#label-scopes) are selected:

    - **Files & other data assets**
    - **Emails**
    - **Meetings**

    ![Sensitivity label scope options for Items that include Files, Emails, and Meetings.](media/itemswithmeetings-scope-options-sensitivity-label.png)

    All three options are needed because of their interdependency. A meeting consists of a calendar event, the invitation and responses, related attachments, related emails, and the actual Teams meeting. As a result, all these items need the same sensitivity label applied to protect the meeting.
2. On the **Choose protection settings for labeled items** page:

    - Select **Apply or remove encryption** if you want to encrypt meeting invites and responses, and any Office attachment in that calendar item
    - Select **Apply content marking** if you want to add headers or footers to meeting invites and responses
    - Select **Protect Teams meetings and chat** to display the label in Teams meetings and enforce Teams-specific settings for the Teams meeting itself and chat messages
3. On the subsequent pages, configure settings for the options you've selected.

    For more information about configuring encryption for meeting invites, see [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels).

    For more information about the headers and footers that you can apply to meeting invites, see the **Mark the content** information from [What sensitivity labels can do](sensitivity-labels#what-sensitivity-labels-can-do).

    For more information about the settings that you can configure for Teams meetings and chat:

    - Use the Teams documentation for an explanation of each setting. For information about how the settings interact with other configuration methods for Teams, see [Use Teams meeting templates, sensitivity labels, and admin policies together for sensitive meetings](/en-us/microsoftteams/meeting-templates-sensitivity-labels-policies).
    - Specific to the option to prevent copy in chat, see the next section on this page, Prevent copying chat to the clipboard label setting.
4. Complete the label configuration and then create or configure other sensitivity labels if you need different settings for other labels.

### Prevent copying and forwarding for chats and meeting content

The label setting **Prevent copying and forwarding of meeting chat, live caption, and transcripts** also extends to AI-generated meeting recap content.

The setting is enforced for all channel chats, even outside channel meetings. For non-channel meetings, it's enforced only for meetings.

The methods supported to prevent these actions:

- Select the text and then right-click &gt; **Copy** or Ctrl+C
- Forward messages
- Share to Outlook
- Copy link

This setting can't prevent screen captures and doesn't apply to developer tools or third-party apps.

## Configure a corresponding sensitivity label publishing policy

1. Make sure the [label is published](create-sensitivity-labels#publish-sensitivity-labels-by-creating-a-label-policy) to meeting organizers and participants.

1. Configure label policy settings that are specific just to calendar items, Teams meetings, and chat:

    - **Apply a default label to meetings and calendar events**

        - For Outlook: The default label is applied to new calendar events and to existing unlabeled calendar events when they are updated.
        - For Teams: The default label is applied to new calendar events but won't be automatically applied when an existing unlabeled meeting is updated.

        Note

        These settings are independent from, rather than override, the similar policy settings for emails. For example, if you don't select the setting to apply a default label to meetings and calendar events, but do select the setting to apply a default label for emails, no default label is applied to calendar events.
    - **Require users to apply a label to their meetings and calendar events**
    - **Inherit label from files shared to meetings**

        For Teams meetings, automatically apply or recommend that the meeting is labeled with the highest priority sensitivity label from files shared for the meeting when that label is published to the meeting organizer.

        These files can be shared in the chat or uploaded in the **Shared** tab of the meeting, or presented via Live share. Files shared via [screen share or Window share](https://support.microsoft.com/office/present-content-in-microsoft-teams-meetings-fcc2bf59-aecd-4481-8f99-ce55dd836ce8), or shared any other way won't be inherited to meetings.

        A meeting that already has a sensitivity label with a higher priority label won't be overriden. However, a manually applied sensitivity label with a lower priority can be overriden.

        For Teams desktop and web clients, a notification event is sent to the meeting organizer if label inheritance happens before the meeting starts.
    - **Apply meeting label to artifacts**

        This setting is in preview and for MP4 files, requires you to [enable sensitivity labeling support for MP4](sensitivity-labels-sharepoint-onedrive-files#video-support-mp4-files).

        Important

        If MP4 support isn't enabled, these files aren't labeled when you select this option.

        For Teams meetings, automatically apply the meeting's sensitivity label to recordings and their transcripts (.mp4 files), and to meeting notes (.loop files) at the time the artifact is saved to SharePoint or OneDrive. If the meeting label changes later, the inherited label doesn't automatically change.

        Recordings respect any access permissions and usage rights from label encryption settings and can be played directly in a web browser and supported experiences such as SharePoint, Teams, or Clipchamp. However, if a recording and transcript has a label that applies encryption, you can't download them. You can download them if the label doesn't apply encryption, but a downloaded file in this case doesn't retain the labeling information.

        You can, if required, manually relabel these files in SharePoint or OneDrive, by using the file's **Details** pane. For example, change the label to one that doesn't apply encryption so that you can then download and share with others. As with all sensitivity labels, you must have the appropriate permissions to change a sensitivity label that applies encryption, which is always the case for the meeting owner.

## How to configure and apply a label for channel meetings

To apply your label meeting options to channel meetings, the sensitivity label must be associated with a container label for the channel. Then, all channel meetings and [chats](sensitivity-labels-meetings#prevent-copying-and-forwarding-for-chats-and-meeting-content) inherit the associated label, which can't be changed by users.

This association is a setting that's available only when you edit an existing label for [groups and sites](sensitivity-labels-teams-groups-sites). Then, you can select a sensitivity label that you've configured in the previous procedure:

![Screenshot of the option to configure a default sensitivity label to protect channel meetings and chat.](media/sensitivity-label-default-channel-meeting.png)

Note

The option to select this default sensitivity label to protect channel meetings and chat is available only when both of the following conditions apply:

- You're editing an existing sensitivity label, rather than creating a new label.
- The label's scope includes files, emails, and meetings.

If you select a label that applies encryption, it can be a label with admin-defined permissions (**Assign permissions now**) or user-defined permissions (**Do Not Forward** and **Encrypt-Only**).

## End-user documentation

To help end users understand how to apply and change sensitivity labels in Teams and Outlook, see the following articles:

- [Sensitivity labels for Teams meetings](https://support.microsoft.com/office/sensitivity-labels-for-teams-meetings-2b244d1d-72d0-471e-8e58-c41079e190fb).
- [Apply sensitivity labels to your Outlook meetings](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-outlook-meetings-f3c960aa-e094-4447-9c88-6fd7c4b4d33c).

Remember to provide your own guidance which named label to apply for different types of meetings. Then, users can focus on the label name instead of the individual settings applied by the label.