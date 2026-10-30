---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Turn pronouns on or off for your organization in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/turn-pronouns-on-or-off?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords: CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
ms.collection:
- Tier2
- M365-subscription-management
- scotvorg
- Adm_O365
- Adm_TOC
- GAUpdates
- operations-pod
ms.custom:
- okr_smb
- AdminTemplateSet
search.appverid: MET150
description: Learn how to turn the pronouns feature on or off in the Microsoft 365 admin center.
ms.date: 2026-04-21T00:00:00.0000000Z
locale: en-us
document_id: 9673b777-a479-8c08-88cf-50c1dfea76cd
document_version_independent_id: 9673b777-a479-8c08-88cf-50c1dfea76cd
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/turn-pronouns-on-or-off.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/turn-pronouns-on-or-off
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/turn-pronouns-on-or-off.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 8380bbe9-a77f-74ed-de37-737652548147
---

# Turn pronouns on or off for your organization in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

As a Microsoft 365 administrator, you can turn on a feature that lets all users in your organization add their pronouns on their profile cards in Microsoft 365. The pronouns feature is off by default and requires configuration to turn on.

Before you decide to turn the feature on or off, see the following resources:

- [Pronouns on your profile in Microsoft 365](https://support.microsoft.com/topic/232c3bfb-a947-4310-86db-b22d63663d85)
- [Frequently asked questions about pronouns in Microsoft 365](https://support.microsoft.com/topic/48135f04-e822-49b5-ba6b-e9bae2ce503a)
- [Pronouns best practices](https://support.microsoft.com/topic/ef1701ad-711d-4c6e-b664-64c3ee188d68)

Pronouns are stored together with a user's other profile data in Microsoft 365 and can be temporarily cached in other Exchange mailboxes (within the same tenant) for faster access by Copilot experiences. The cached data is updated when profile data is updated, and can't be accessed or edited by the user who owns the mailbox where the data is cached.

Pronouns are stored with other data in the user's Exchange mailbox. For more information, see [Data Residency for Exchange Online](../../enterprise/m365-dr-service-exo#how-can-i-determine-customer-data-location).

For example, if a user changes their pronouns in the profile card, the cached data in another user's mailbox is updated with the new pronouns. Users can't edit someone else's pronouns; they can only see pronouns through experiences that show pronouns. Microsoft Copilot is an example of an experience that has access to pronouns.

Important

- Knowing someone's pronouns doesn't always equate to knowing their gender identity. We encourage you to understand any applicable local laws, regulations, and cultural norms that might pose extra risk to employees should their pronouns be publicly displayed, and take this information into consideration when you decide whether to turn on this feature.
- If you decide to use the pronouns feature, we recommend that you engage with internal and/or external subject matter experts in transgender inclusion to consider how pronoun display can complement, not substitute, more comprehensive efforts to support transgender communities in your organization.

## Before you begin

You must be a Global Administrator to do the task in this article. For more information, see [About admin roles](about-admin-roles).

Caution

Global Administrators have almost unlimited access to your organization's settings and most of its data. To help keep your organization secure, we recommend that you limit the number of Global Administrators as much as possible.

Before you decide to turn the pronouns feature on or off, consider the following:

- When you turn the pronouns feature on or off, it can take up to seven hours for users to see changes. For example, if you turn on the pronouns feature, users can't see the option to add pronouns on their profile for up to seven hours. If you turn off the pronouns feature, any previously set pronouns might stay visible in Microsoft 365 (for example, on profiles) for up to seven hours.
- When you turn the pronouns feature off, all the pronouns data created by users is deleted. The data deletion process could take up to 30 days to complete. If you turn the pronouns feature back on within that period, any hidden pronouns that haven't yet been deleted from Microsoft servers become visible in Microsoft 365 experiences, such as profiles.
- After a user adds pronouns to their profile, the pronouns are visible to everyone in your organization. Users can't control who can see their pronouns in Microsoft 365 in your organization. However, pronouns aren't visible to people outside the organization.
- Copilot has access to pronouns from a user's profile and uses what's available at the time of writing when generating text about the user. If the user changes or deletes the pronouns from their profile, pronouns in previously generated text aren't updated retroactively. For example, if Copilot is used to produce a meeting summary, the summary uses the pronouns available at the time and they won't be changed if the user referred to changes to their pronouns after the summary is produced.

## Turn the pronouns feature on or off

1. In the Microsoft 365 admin center, go to the **Settings** &gt; **Org settings** page, and select the [Security & privacy](https://go.microsoft.com/fwlink/p/?linkid=2072756) tab.
2. Select **Pronouns**.
3. To turn on the pronouns feature, in the **Pronouns** pane, select the **Turn on and allow pronouns** checkbox. To turn off the pronouns feature, clear the checkbox.
4. Select **Save**.

To turn the pronouns feature on or off for your organization using Microsoft Graph, see [Manage pronouns settings for an organization using the Microsoft Graph API](/en-us/graph/pronouns-configure-pronouns-availability).