---
layout: Conceptual
title: Set up a connector to archive WeChat data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-wechat-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Set up and use a connector in the Microsoft Purview portal to import and archive WeChat data in Microsoft 365.
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
ms.collection:
- purview-compliance
- data-connectors
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 3d880915-1ab6-b41c-fa5d-96991bbce15f
document_version_independent_id: 3d880915-1ab6-b41c-fa5d-96991bbce15f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-wechat-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-wechat-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-wechat-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6270a5fc-bd08-fe2f-0f46-3da5ff2fc8b1
---

# Set up a connector to archive WeChat data in Microsoft 365 | Microsoft Learn

Use the TeleMessage connector to import and archive WeChat and WeCom calls, chats, attachments, files, and recalled messages. When you set up and configure a connector, it connects to your organization's TeleMessage account and imports the mobile communication of employees who use the TeleMessage WeChat Archiver to mailboxes in Microsoft 365.

After storing WeChat Archiver connector data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to WeChat communication data. For example, you can search WeChat communication by using eDiscovery or associate the mailbox that contains the WeChat Archiver connector data with a custodian in an eDiscovery (Premium) case. Using a WeChat Archiver connector to import and archive data in Microsoft 365 can help your organization stay compliant with corporate governance regulations and regulatory policies.

## Overview of archiving WeChat communication data

The following overview explains the process of using a connector to archive WeChat communications data in Microsoft 365.

![Diagram of the WeChat Archiver data workflow showing data transferred from TeleMessage to Microsoft 365 user mailboxes through the Microsoft Purview connector.](media/wechatconnectorworkflow.png)

1. Your organization works with TeleMessage to set up a WeChat Archiver connector.
2. In real time, your organization's WeChat data is copied to the TeleMessage site.
3. The WeChat Archiver connector that you create in the [Microsoft Purview portal](purview-portal) connects to the TeleMessage site every day and transfers the email messages from the previous 24 hours to a secure Azure Storage area in the Microsoft Cloud.
4. The connector imports the mobile communication items to the mailbox of a specific user. A new folder named WeChat Archiver is created in the specific user's mailbox and the items are imported to it. The connector does mapping by using the value of the *User's Email address* property. Every email message contains this property, which is populated with the email address of every participant of the email message. In addition to automatic user mapping using the value of the *User's Email address* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file should contain User's mobile Number and the corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every email item the connector will first look at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's mobile number, the connector will use the User ‘s email address property of the email item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *user's email address* property of the email item, the item won't be imported.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

- Work with TeleMessage to set up a WeChat archive connector. For activation steps, see [Activating the TeleMessage WeChat Archiver for Microsoft 365](https://www.telemessage.com).
- Set up a TeleMessage connector for Microsoft 365 and get a valid company administration account. To purchase the service, see [Order Microsoft 365 Mobile Archiving](https://www.telemessage.com).
- Register all users that require WeChat archiving in the TeleMessage account with the same email address that is used for the user's Microsoft 365 account.
- Install the Tencent WeCom app on the mobile phones of users in your organization and activate it. The WeCom app lets users communicate and chat with other WeChat and WeCom users.
- Assign the Data Connector Admin role to the user who creates a WeChat Archiver connector in the Microsoft Purview portal. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Create a WeChat Archiver connector

Complete the following steps to create a WeChat Archiver connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the TeleMessage site and transfer WeChat communications data to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **WeChat Archiver**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Login to TeleMessage** page, under Step 3, enter the required information in the following boxes and then select **Next**.

    - **Username**: Your TeleMessage user name.
    - **Password**: Your TeleMessage password.
7. After you create the connector, you can close the TeleMessage sign-in pop-up window.
8. On the **User mapping** page, enable automatic user mapping. You can also upload a custom user mapping CSV file.
9. Select **Next**, review your settings, and then select **Finish** to create the connector.

## WeChat connector limits

Importing attachments or items supports files up to 10 MB.