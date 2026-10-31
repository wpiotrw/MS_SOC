---
layout: Conceptual
title: Set up a connector to archive Skype for Business Server data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-17a-4-skype-for-business-server-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to set up and use a 17a-4 Skype for Business Server DataParser connector to import and archive Skype for Business Server data in Microsoft 365.
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
document_id: 7091123e-b922-22e0-d1d7-d4db81c2849f
document_version_independent_id: 7091123e-b922-22e0-d1d7-d4db81c2849f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-17a-4-skype-for-business-server-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-17a-4-skype-for-business-server-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-17a-4-skype-for-business-server-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/74b1e9df-8124-4d0c-b310-50c3bf3ff02b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7c78426a-2d2c-4bce-8e97-c1c9ab1c453e
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: bdfa3cdd-a896-c8f8-c1c7-f6b17b0dffa7
---

# Set up a connector to archive Skype for Business Server data in Microsoft 365 | Microsoft Learn

Use the [Skype Server DataParser](https://www.17a-4.com/skype-server-dataparser/) from 17a-4 LLC to import and archive data from a Skype for Business Server to user mailboxes in your Microsoft 365 organization. The DataParser includes a Skype for Business connector that you configure to capture items from a third-party data source and import those items to Microsoft 365. The Skype for Business Server DataParser connector converts Skype for Business Server data to an email message format and then imports those items to user mailboxes in Microsoft 365.

After storing Skype for Business Server data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, retention policies and retention labels, and Communication Compliance. By using a Skype for Business Server connector to import and archive data in Microsoft 365, your organization can stay compliant with government and regulatory policies.

## Overview of archiving Skype for Business Server data

The following overview explains the process of using a data connector to archive Skype for Business Server data in Microsoft 365.

![Archiving workflow for Skype for Business Server data from 17a-4.](media/skypeserverdataparserconnectorworkflow.png)

1. Your organization works with 17a-4 to set up and configure the Skype for Business Server DataParser.
2. The DataParser regularly collects Skype for Business Server items and converts the content of a message to an email message format.
3. You create the Skype for Business Server DataParser connector in the [Microsoft Purview portal](purview-portal). The connector connects to DataParser and transfers the messages to a secure Azure Storage location in the Microsoft cloud.
4. The connector creates a subfolder in the Inbox folder named **Skype for Business Server DataParser** in the user mailboxes and imports the Skype for Business Server items to that folder. The connector uses the value of the *Email* property to determine which mailbox to import items to. Every Skype for Business Server item contains this property, which is populated with the email address of every participant.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

- Create a DataParser account for Microsoft connectors. To create an account, contact [17a-4 LLC](https://www.17a-4.com/contact/). You need to sign in to this account when you create the connector in the Microsoft Purview portal.
- Assign the Data Connector Admin role to the user who creates and completes the Skype for Business Server DataParser connector setup in the Microsoft Purview portal. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Step 1: Set up a Skype for Business Server DataParser connector

Create a 17a-4 connector for Skype for Business Server data in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Skype for Business Server DataParser**.
5. On the **Terms of service** page, select **Accept**.
6. Enter a unique name that identifies the connector and then select **Next**.
7. Sign in to your 17a-4 account and complete the steps in the Skype for Business Server DataParser connection workflow.

## Step 2: Configure the Skype for Business Server DataParser connector

Work with 17a-4 Support to configure the Skype for Business Server DataParser connector.

## Step 3: Map Skype for Business Server users to Microsoft 365 users

The Skype for Business Server DataParser connector automatically maps users to their Microsoft 365 email addresses before importing data to Microsoft 365.

## Step 4: Monitor the Skype for Business Server DataParser connector

After you create a Skype for Business Server DataParser connector, you can view the connector status in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select the Skype for Business Server DataParser connector that you created to display the connector properties and information.
4. Under **Connector status with source**, select the **Download log** link to open or save the status log for the connector. This log contains information about the data that's imported to the Microsoft cloud. For more information, see [View admin logs for data connectors](data-connector-admin-logs).

## Connector limits for archiving Skype for Business Server data

Importing attachments or items supports files up to 10 MB.