---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: onlineMeetingbase resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/onlinemeetingbase?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: awang119
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: cloud-communications
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Contains basic information about a meeting.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-08-08T00:00:00.0000000Z
locale: en-us
document_id: 356807b6-8aee-d9d0-138c-3c041fb4ce1e
document_version_independent_id: 63c604eb-b267-7d40-fccb-2adcb07c2582
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/onlinemeetingbase.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/onlinemeetingbase
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/onlinemeetingbase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
platformId: 43396e2e-e1f4-337d-489c-dfa20b3d10b6
---

# onlineMeetingbase resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a base online meeting. The base type of [onlineMeeting](onlinemeeting) and [virtualEventSession](virtualeventsession).

Inherits from [entity](entity).

Tip

This is an abstract type and can't be used directly. Use the derived types [onlineMeeting](onlinemeeting) and [virtualEventSession](virtualeventsession) instead.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| allowAttendeeToEnableCamera | Boolean | Indicates whether attendees can turn on their camera. |
| allowAttendeeToEnableMic | Boolean | Indicates whether attendees can turn on their microphone. |
| allowBreakoutRooms | Boolean | Indicates whether breakout rooms are enabled for the meeting. |
| allowCopyingAndSharingMeetingContent | Boolean | Indicates whether the ability to copy and share meeting content is enabled for the meeting. |
| allowedLobbyAdmitters | allowedLobbyAdmitterRoles | Specifies the users who can admit from the lobby. The possible values are: `organizerAndCoOrganizersAndPresenters`, `organizerAndCoOrganizers`, `unknownFutureValue`. |
| allowedPresenters | onlineMeetingPresenters | Specifies who can be a presenter in a meeting. The possible values are: `everyone`, `organization`, `roleIsPresenter`, `organizer`, `unknownFutureValue`. Inherited from [onlineMeetingBase](onlinemeetingbase). |
| allowMeetingChat | meetingChatMode | Specifies the mode of the meeting chat. |
| allowLiveShare | meetingLiveShareOptions | Indicates whether live share is enabled for the meeting. The possible values are: `enabled`, `disabled`, `unknownFutureValue`. |
| allowParticipantsToChangeName | Boolean | Specifies if participants are allowed to rename themselves in an instance of the meeting. |
| allowTeamworkReactions | Boolean | Indicates if Teams reactions are enabled for the meeting. |
| allowTranscription | Boolean | Indicates whether transcription is enabled for the meeting. |
| allowPowerPointSharing | Boolean | Indicates whether PowerPoint live is enabled for the meeting. |
| allowRecording | Boolean | Indicates whether recording is enabled for the meeting. |
| allowWhiteboard | Boolean | Indicates whether whiteboard is enabled for the meeting. |
| anonymizeIdentityForRoles | onlineMeetingRole collection | Specifies whose identity is anonymized in the meeting. The possible values are: `attendee`. The `attendee` value can't be removed through a PATCH operation once added. |
| audioConferencing | [audioConferencing](audioconferencing) | The phone access (dial-in) information for an online meeting. Read-only. |
| chatInfo | [chatInfo](chatinfo) | The chat information associated with this online meeting. |
| chatRestrictions | [chatRestrictions](chatrestrictions) | Specifies the configuration settings for meeting chat restrictions. |
| cloudVideoInteropInfo | [cloudVideoInteropInfo](cloudvideointeropinfo) | Conferencing device integration settings for [Cloud Video Interop (CVI)](/en-us/microsoftteams/cloud-video-interop). Read-only. |
| expiryDateTime | DateTimeOffset | Indicates the date and time when the meeting resource expires. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. |
| id | String | The default ID associated with the online meeting. Read-only. |
| isEndToEndEncryptionEnabled | Boolean | Indicates whether end-to-end encryption (E2EE) is enabled for the online meeting. |
| isEntryExitAnnounced | Boolean | Indicates whether to announce when callers join or leave. |
| joinInformation | [itemBody](itembody) | The join information in the language and locale variant specified in 'Accept-Language' request HTTP header. Read-only. |
| joinMeetingIdSettings | [joinMeetingIdSettings](joinmeetingidsettings) | Specifies the **joinMeetingId**, the meeting passcode, and the requirement for the passcode. Once an **onlineMeeting** is created, the **joinMeetingIdSettings** can't be modified. To make any changes to this property, you must cancel this meeting and create a new one. |
| joinWebUrl | String | The join URL of the online meeting. Read-only. |
| lobbyBypassSettings | [lobbyBypassSettings](lobbybypasssettings) | Specifies which participants can bypass the meeting lobby. |
| meetingOptionsWebUrl | String | Provides the URL to the Teams meeting options page for the specified meeting. This link allows *only the organizer* to configure meeting settings. |
| meetingSpokenLanguageTag | String | Specifies the spoken language used during the meeting for recording and transcription purposes. |
| meetingType | onlineMeetingType | The type of the online meeting. The possible values are: `adhoc`, `scheduled`, `recurring`, `broadcast`, `meetnow`, `unknownFutureValue`. Read-only. |
| recordAutomatically | Boolean | Indicates whether to record the meeting automatically. |
| sensitivityLabelAssignment | [onlineMeetingSensitivityLabelAssignment](onlinemeetingsensitivitylabelassignment) | Specifies the sensitivity label applied to the Teams meeting. |
| shareMeetingChatHistoryDefault | meetingChatHistoryDefaultMode | Specifies whether meeting chat history is shared with participants. The possible values are: `all`, `none`, `unknownFutureValue`. |
| subject | String | The subject of the online meeting. |
| videoTeleconferenceId | String | The video teleconferencing ID. Read-only. |
| watermarkProtection | [watermarkProtectionValues](watermarkprotectionvalues) | Specifies whether the client application should apply a watermark to a content type. |

### allowedLobbyAdmitterRoles values

| Value | Description |
| --- | --- |
| organizerAndCoOrganizersAndPresenters | Meeting organizer, co-organizers, and presenters. |
| organizerAndCoOrganizers | Meeting organizer and co-organizers. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

### meetingChatMode values

| Value | Description |
| --- | --- |
| enabled | Meeting chat is enabled. |
| disabled | Meeting chat is disabled. |
| limited | Meeting chat is enabled but only during the meeting call. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

### meetingChatHistoryDefaultMode values

| Value | Description |
| --- | --- |
| all | All meeting chat history is shared. |
| none | No meeting chat history is shared. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

### meetingLiveShareOptions values

| Value | Description |
| --- | --- |
| enabled | Meeting live share is enabled. |
| disabled | Meeting live share is disabled. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

### onlineMeetingPresenters values

| Value | Description |
| --- | --- |
| everyone | Everyone is a presenter. Default. |
| organization | Everyone in organizer’s organization is a presenter. |
| roleIsPresenter | Only the participants whose role is presenter are presenters. |
| organizer | Only the organizer is a presenter. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

### onlineMeetingType values

| Value | Description |
| --- | --- |
| adhoc | The meeting is an ad hoc meeting. |
| scheduled | The meeting is a scheduled meeting. |
| recurring | The meeting is a recurring meeting. |
| broadcast | The meeting is a broadcast meeting. |
| meetnow | The meeting is a *Meet now* session. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| attendanceReports | [meetingAttendanceReport](meetingattendancereport) collection | The attendance reports of an online meeting. Read-only. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "allowAttendeeToEnableCamera": "Boolean",
  "allowAttendeeToEnableMic": "Boolean",
  "allowBreakoutRooms": "Boolean",
  "allowCopyingAndSharingMeetingContent": "Boolean",
  "allowedLobbyAdmitters": "String",
  "allowedPresenters": "String",
  "allowLiveShare": "String",
  "allowMeetingChat": "String",
  "allowPowerPointSharing": "Boolean",
  "allowRecording": "Boolean",
  "allowTeamworkReactions": "Boolean",
  "allowTranscription": "Boolean",
  "allowWhiteboard": "Boolean",
  "anonymizeIdentityForRoles": ["String"],
  "audioConferencing": {"@odata.type": "microsoft.graph.audioConferencing"},
  "chatInfo": {"@odata.type": "microsoft.graph.chatInfo"},
  "chatRestrictions":{"@odata.type": "microsoft.graph.chatRestrictions"},
  "cloudVideoInteropInfo": {"@odata.type": "microsoft.graph.cloudVideoInteropInfo"},
  "expiryDateTime": "String (timestamp)",
  "id": "String (identifier)",  
  "isEndToEndEncryptionEnabled": "Boolean",
  "isEntryExitAnnounced": "Boolean",
  "joinInformation": {"@odata.type": "microsoft.graph.itemBody"},
  "joinMeetingIdSettings": {"@odata.type": "microsoft.graph.joinMeetingIdSettings"},
  "joinWebUrl": "String",
  "lobbyBypassSettings": {"@odata.type": "microsoft.graph.lobbyBypassSettings"},
  "meetingOptionsWebUrl": "String",
  "meetingSpokenLanguageTag": "String",
  "meetingType": "String",
  "recordAutomatically": "Boolean",
  "sensitivityLabelAssignment": {"@odata.type": "microsoft.graph.onlineMeetingSensitivityLabelAssignment"},
  "shareMeetingChatHistoryDefault": "microsoft.graph.meetingChatHistoryDefaultMode",
  "subject": "String",
  "videoTeleconferenceId": "String",
  "watermarkProtection": {"@odata.type": "microsoft.graph.watermarkProtectionValues"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/onlinemeetingbase?view=graph-rest-beta&accept=text/markdown)
