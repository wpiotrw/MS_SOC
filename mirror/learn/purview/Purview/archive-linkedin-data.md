---
layout: Conceptual
title: Set up a connector to archive LinkedIn data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-linkedin-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how administrators can setup & use a native connector to import data from a LinkedIn Company Page to Microsoft 365.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
search.appverid:
- MET150
ms.collection:
- purview-compliance
- data-connectors
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: c09c33bf-ebbd-dfc1-95fb-7fafb443ef28
document_version_independent_id: c09c33bf-ebbd-dfc1-95fb-7fafb443ef28
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-linkedin-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-linkedin-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-linkedin-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/aec7dc3e-0dad-4b82-accf-63218d8767d5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f260444a-7ec6-4768-8e41-ad2438092724
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 06e0bb5a-68a0-1df9-871d-524b84e135a4
---

# Set up a connector to archive LinkedIn data | Microsoft Learn

Use a connector to import and archive data from LinkedIn Company pages. After you set up and configure a connector, it connects to the account for the specific LinkedIn Company page once every 24 hours. The connector converts the messages posted to the Company page to an email message, then imports those items to a mailbox in Microsoft 365.

After storing the LinkedIn Company page data in a mailbox, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, and Microsoft 365 retention policies to LinkedIn data. For example, you can search for these items by using eDiscovery or associate the storage mailbox with a custodian in a Microsoft Purview eDiscovery (Premium) case. Creating a connector to import and archive LinkedIn data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Before you begin

Before you create the connector, make sure you meet the following requirements:

- Assign the Data Connector Admin role to the user who creates a LinkedIn Company Page connector. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- Have the sign-in credentials (email address or phone number and password) of a LinkedIn user account that is an admin for the LinkedIn Company Page that you want to archive. You use these credentials to sign into LinkedIn when setting up the connector.
- Understand that the LinkedIn connector can import a total of 200,000 items in a single day. If there are more than 200,000 LinkedIn items in a day, none of those items are imported to Microsoft 365.

## Create a LinkedIn connector

Perform the following steps to create a LinkedIn connector in Microsoft Purview.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **LinkedIn company pages** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Sign in with LinkedIn** page, select **Sign in with LinkedIn**.
7. On the LinkedIn sign in page, enter the email address (or phone number) and password for the LinkedIn account associated with the company page that you want to archive, then select **Sign in**. A workflow page displays with a list of all LinkedIn Company Pages associated with the account that you signed in to. You can only configure a connector for one company page. If your organization has multiple LinkedIn Company Pages, you need to create a connector for each one.
8. Select the company page that you want to archive items from, then select **Next**.
9. On the **Choose storage location** page, select the email address of a Microsoft 365 mailbox that the LinkedIn items will be imported to, then select **Next**. Items are imported to the inbox folder in this mailbox. The mailbox used must have an Exchange Online Plan 1 or Plan 2 license.
10. Select **Next** to review the connector settings and then select **Finish** to complete the connector setup.

Note

LinkedIn items are imported to the LinkedIn subfolder in the inbox of the storage mailbox in Microsoft 365. They appear as email messages.