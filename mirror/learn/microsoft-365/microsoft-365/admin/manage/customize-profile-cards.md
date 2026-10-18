---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: customize-profile-cards - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/customize-profile-cards?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Informative article on how admins can enable additional properties in profile cards and impact of this
author: SuryaLashmiS
ms.author: srinivasansu
ms.service: microsoft-365-admin
ms.topic: article
ms.date: 2026-08-07T00:00:00.0000000Z
manager: scotv
ms.custom: user-accounts
locale: en-us
document_id: aa68b19d-5caf-b718-1464-6b66b87b1583
document_version_independent_id: aa68b19d-5caf-b718-1464-6b66b87b1583
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/customize-profile-cards.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/customize-profile-cards
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/customize-profile-cards.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 3e5bbdcb-1f54-2590-2c5e-4fd64b51b126
---

# customize-profile-cards - Microsoft 365 admin | Microsoft Learn

[Profile cards](https://support.microsoft.com/en-us/office/profile-cards-in-microsoft-365-e80f931f-5fc4-4a59-ba6e-c1e35a85b501) in Microsoft 365 show key information about an organization's employees. As an admin, you can use the Microsoft 365 admin center to add certain properties to your organization's profile cards. These settings are configured under [People settings](/en-us/microsoft-365/admin/manage/people-settings-in-microsoft-365-admin-center) section in your admin dashboard.

## Before you begin

You must be a Global Administrator or a People Administrator to do the tasks in this article. For more information, see [About admin roles](../add-users/about-admin-roles).

## Properties in profile cards

Properties in profile cards map to attributes in the [Microsoft 365 profile resource](/en-us/graph/api/resources/profile?view=graph-rest-beta&amp;preserve-view=true) and can be populated from various sources, including:

- [Microsoft Entra ID](/en-us/entra/fundamentals/how-to-manage-user-profile-info)
- [Organizational data in Microsoft 365](/en-us/entra/fundamentals/how-to-manage-user-profile-info)
- [Microsoft 365 Copilot connectors for people data](/en-us/graph/peopleconnectors)
- [User-provided details](https://support.microsoft.com/en-gb/office/edit-your-profile-in-microsoft-365-e7056090-56d4-4b81-bb3f-b6af31089ebe)

Read [Build Microsoft 365 Copilot connectors for people data](/en-us/microsoft-365-copilot/extensibility/build-connectors-with-people-data) to learn how to ingest people data from external source systems into Microsoft Graph.

### Default properties

Some properties are shown by default on profile cards when data is available. Admins can't hide these properties:

- Name
- Email
- Chat
- Work phone
- Mobile
- Work location
- Company
- Job title
- Department
- Business address

### Optional properties

Admins can choose to show or hide certain properties on the profile cards. They're hidden by default, but admins can configure their visibility by navigating to **Settings &gt; Org settings &gt; People settings &gt; Profile card &gt; Contact info** in the Microsoft 365 admin center.

When enabled, these properties appear in the **Profile** tab of the profile cards in Outlook Web, Outlook for Windows, Teams, Microsoft Copilot app and People Companion app. They're visible to users viewing their own profile and when viewing the profiles of others.

- Division
- Role
- Employee number
- Employee type
- Cost center
- User principal name
- Alias
- Fax
- Street address
- State
- Postal code

After an admin changes the visibility of these properties, it can take up to 24 hours for changes to be reflected on profile cards.

Note

If enabled, street address, state, and postal code are shown under the Business address attribute on the cards.

Note

Hiding a property removes it from profile cards but doesn't delete the underlying data from Microsoft 365 profiles or stop the property from appearing in other Microsoft 365 experiences. To permanently delete the data, admins need to remove it from the source system.

## How to find the source of a property?

Users can learn the source of each property on their profile cards by [exporting their profile card data](https://support.microsoft.com/en-us/office/export-data-from-your-profile-card-d809f83f-c077-4a95-9b6c-4f093305163d#:%7E:text=Hover%20over%20your%20name%20or%20profile%20photo%20to,as%20a%20JSON%20file%20in%20your%20Downloads%20folder.). The export shows source IDs for each property, indicating the system the data comes from. [Learn what each source ID represents](/en-us/graph/api/resources/profilesourceannotation?view=graph-rest-beta&amp;preserve-view=true)

If a source ID doesn't have a known mapping, the data comes from a third-party source. In this case, users should contact their tenant admin to identify the system. Admins can then match the source ID with a connector ID in Microsoft 365 admin center to find the data source.

## How can users edit their profile info?

Users may want to edit certain organization-managed information shown on their profile card-for example if the property is incorrect or out of date. As above, users should find the source ID of the property and share it with their admin. Admins can then update the info in the source system.