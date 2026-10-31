---
layout: Conceptual
title: Preserve Bcc and expanded distribution group recipients for eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-preserve-recipients
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to preserve mailbox Bcc and distribution group content to meet regulatory compliance and eDiscovery requirements.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: cb1918d7-2568-9300-c927-8960f03ec85e
document_version_independent_id: cb1918d7-2568-9300-c927-8960f03ec85e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-preserve-recipients.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-preserve-recipients
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-preserve-recipients.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 20fd6d4f-3ecb-aeed-3b27-6afbb9444ccd
---

# Preserve Bcc and expanded distribution group recipients for eDiscovery | Microsoft Learn

By creating [litigation holds](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), [eDiscovery holds](edisc-hold-manage), and [retention policies](retention) in Microsoft Purview, you can preserve mailbox content to meet regulatory compliance and eDiscovery requirements. All messages include information about recipients directly addressed in the To and Cc fields by default. But your organization might require the ability to search for and reproduce details about all recipients of a message. This requirement includes:

- **Recipients addressed using the Bcc field of a message:** Bcc recipients are stored in the message in the sender's mailbox, but not included in headers of the message delivered to recipients.
- **Expanded distribution group recipients:** Recipients who receive the message because they're members of a distribution group to which the message was addressed, either in the To, Cc, or Bcc fields.

Exchange Online and Exchange Server 2013 (Cumulative Update 7 and later versions) retain information about Bcc and expanded distribution group recipients. You can search for this information by using an eDiscovery tool in the Microsoft Purview portal.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## How Bcc recipients and expanded distribution group recipients are preserved

Important

Only the sender's mailbox's Sent Items contains distribution group expansion.

Information about Bcc recipients is stored with the message in the sender's mailbox. This information is indexed and available to eDiscovery searches and holds.

Information about expanded distribution group recipients is stored with the message after you place a mailbox on Litigation Hold. In Microsoft 365, this information is also stored when a Microsoft Purview retention policy is applied to a mailbox. Distribution group membership is determined at the time the message is sent. The expanded recipients list stored with the message isn't impacted by changes to membership of the group after the message is sent.

| Information about... | Is stored in... | Is stored by default? | Is accessible to... |
| --- | --- | --- | --- |
| To: and Cc: recipients | Message properties in the sender and recipients' mailboxes. | Yes | Sender, recipients, and compliance officers |
| Bcc: recipients | Message property in the sender's mailbox. | Yes | Sender and compliance officers |
| Expanded distribution group recipients | Message properties in the sender's mailbox. | No. Expanded distribution group recipient information is stored after a mailbox is placed on Litigation Hold or assigned to a Microsoft Purview retention policy. | Sender and Compliance officers |

## Search for messages with expanded distribution group recipients

When you search for messages sent to a recipient, eDiscovery search results now include messages sent to a distribution group that the recipient is a member of, but only in the sender mailbox and if the sender is on hold.

Important

Distribution group expansion details are only available in the sender’s mailbox under Sent Items. If you search the recipient’s mailbox, messages sent to distribution groups don't show the expanded list of group members.

**Scenario**: John is a member of the US-Sales distribution group. This table shows eDiscovery search results when Bob sends a message to John directly or indirectly via a distribution group.

| When you search Bob's mailbox for messages sent... | And the message is sent with... | Results include message? |
| --- | --- | --- |
| To: John | John on To: | Yes |
| To: John | US-Sales on To: | Yes |
| To: US-Sales | US-Sales on To: | Yes |
| Cc: John | John on Cc: | Yes |
| Cc: John | US-Sales on Cc: | Yes |
| Cc: US-Sales | US-Sales on Cc: | Yes |

| When you search John's mailbox for message... | And the message is sent with... | Results include message? |
| --- | --- | --- |
| To/Cc | US-Sales on To/Cc: | No. Only sender mailbox can be searched. |

## Search for messages with Bcc

**Scenario**: Bob sends an email to John (To/Cc) and Jack (Bcc directly, or indirectly via a distribution group). The following tables show the eDiscovery search results.

Important

Distribution group expansion detail is only available if the sender is on hold.

| When you search Bob's mailbox... | For messages sent... | Results include message? | Notes |
| --- | --- | --- | --- |
| Bob's mailbox | To:/Cc: John | Yes | Shows an indication that Jack was Bcc'ed. |
| Bob's mailbox | Bcc: Jack | Yes | Shows an indication that Jack was Bcc'ed. |
| Bob's mailbox | Bcc: Jack (via distribution group) | Yes | List of members of the Bcc'ed distribution group, expanded when the message was sent, is visible in eDiscovery search preview, export, and logs. |

| When you search John's mailbox... | For messages sent... | Results include message? | Notes |
| --- | --- | --- | --- |
| John's mailbox | To:/Cc: John | Yes | No indication of Bcc recipients. |
| John's mailbox | Bcc: Jack (directly or via distribution group) | No | Bcc: information isn't stored in the message delivered to recipients. You must search the **sender's mailbox**. |

| When you search Jack's mailbox... | For messages sent... | Results include message? | Notes |
| --- | --- | --- | --- |
| Jack's mailbox | To:/Cc: John (directly or via distribution group) | Yes | To:/Cc: information is included in message delivered to all recipients. |
| Jack's mailbox | Bcc: Jack (directly or via distribution group) | No | Bcc: information isn't stored in the message delivered to recipients. You must search the **sender's mailbox.** |

## Frequently asked questions

**When and where is Bcc recipient information stored?**

By default, the original message in the sender's mailbox stores Bcc recipient information. If the Bcc recipient is a distribution group, the system expands distribution group membership only if the sender's mailbox is on hold or assigned to a Microsoft 365 retention policy.

**When and where is the list of expanded distribution group recipients stored?**

The system expands group membership when the sender sends the message. The original message in the sender's mailbox stores the list of expanded distribution group members. The sender's mailbox must be on Litigation Hold or assigned to a Microsoft 365 retention policy.

**Can the To/Cc recipients see which recipients were Bcc'ed?**

No. This information isn't included in message headers, and isn't visible to To/Cc recipients. The sender can see the Bcc field stored in the original message stored in their mailbox. Compliance officers can see this information when searching the sender's mailbox.

**How can I ensure that expanded distribution group recipients are always preserved?**

To ensure that expanded distribution group members are always preserved with a message, [Place all mailboxes on hold](/en-us/Exchange/policy-and-compliance/holds/place-all-mailboxes-on-hold?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) or create an organization-wide Microsoft 365 retention policy.

**Which types of groups are supported?**

Distribution groups, mail-enabled security groups, and dynamic distribution groups are supported.

**Is there a limit on the number of distribution group recipients that are expanded and stored in the message?**

The system preserves up to 10,000 members of a distribution group.

**Are nested distribution groups supported?**

Yes, the system expands 25 levels of nested distribution groups.

**Where is the Bcc and expanded distribution group recipient information visible?**

Compliance officers can see Bcc and expanded distribution group recipient information when performing an eDiscovery search. Bcc and expanded distribution group recipients are included in search results copied to a Discovery mailbox or exported to a PST file and in the eDiscovery log included in search results. Bcc recipient information is also available in search preview.

**What happens if a member of a distribution group is hidden from the organization's global address list (GAL)?**

There's no impact. If recipients are hidden from the GAL, they're still included in the list of recipients for the expanded distribution group.