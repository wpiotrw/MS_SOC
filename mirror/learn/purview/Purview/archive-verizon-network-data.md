---
layout: Conceptual
title: Set up a connector to archive Verizon Network data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-verizon-network-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admins can set up a TeleMessage connector to import and archive SMS and MMS data from the Verizon Network in Microsoft 365. This lets you archive data from third-party data sources in Microsoft 365 so you can use compliance features such as legal hold, eDiscovery, and retention policies to manage your organization's third-party data.
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
document_id: 75c225aa-e81a-9d70-aa4f-5fa5670692fc
document_version_independent_id: 75c225aa-e81a-9d70-aa4f-5fa5670692fc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-verizon-network-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-verizon-network-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-verizon-network-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b56e65e1-c85e-b961-a93b-caf40debae1c
---

# Set up a connector to archive Verizon Network data in Microsoft 365 | Microsoft Learn

Use the TeleMessage connector to import and archive Short Messaging Service (SMS) and Multimedia Messaging Service (MMS) data from Verizon Network. Before you begin, review the prerequisites for setting up the Verizon Network connector. After you set up and configure a connector, it connects to your organization's Verizon Network once every day and imports SMS and MMS data to mailboxes in Microsoft 365.

After storing Verizon Network connector data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, and Microsoft 365 retention policies to Verizon data. For example, you can search Verizon SMS and MMS messages by using eDiscovery or associate the mailbox that contains Verizon Network data with a custodian in a Microsoft Purview eDiscovery (Premium) case. Using a Verizon Network connector to import and archive data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Overview of archiving Verizon Network data

The following overview explains the process of using a connector to archive Verizon Network data in Microsoft 365.

![Diagram of the Verizon Network archiving workflow showing SMS and MMS messages transferred from TeleMessage through the Verizon Network connector to Microsoft 365 user mailboxes.](media/verizonnetworkconnectorworkflow.png)

1. Your organization works with TeleMessage and Verizon to set up a Verizon Network connector. For more information, see [Verizon Network Archiver](https://www.telemessage.com).
2. Once every 24 hours, your organization's Verizon Network copies SMS and MMS messages to the TeleMessage site.
3. The Verizon Network connector that you create in the [Microsoft Purview portal](purview-portal) connects to the TeleMessage site every day and transfers the SMS and MMS messages from the previous 24 hours to a secure Azure Storage location in the Microsoft cloud. The connector also converts the content of SMS and MMS messages to an email message format.
4. The connector imports the mobile communication items to the mailbox of a specific user. A new folder named **Verizon SMS/MMS Network Archiver** is created in the specific user's mailbox and the items are imported to it. The connector does this mapping by using the value of the *User’s Email address* property. Every SMS and MMS message contains this property, which is populated with the email address of every participant of the message.

    In addition to automatic user mapping by using the value of the *User’s Email address* property, you can also implement custom mapping by uploading a CSV mapping file. This mapping file contains the mobile phone number and corresponding Microsoft 365 email address for users in your organization. If you enable both automatic user mapping and custom mapping, for every Verizon item the connector first looks at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's mobile phone number, the connector uses the values in the email address property of the item it's trying to import. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or in the email address property of the Verizon item, the item won't be imported.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

Some of the implementation steps required to archive Verizon Network data are external to Microsoft 365. You must complete these steps before you can create a connector in the Microsoft Purview portal.

- Order the [Verizon Network Archiver service from TeleMessage](https://www.telemessage.com) and get a valid administration account for your organization. You need to sign in to this account when you create the connector in the Microsoft Purview portal.
- Obtain your Verizon Network account and billing contact details so you can fill out the TeleMessage onboarding forms and order the message archiving service from Verizon.
- Register all users that require Verizon SMS and MMS archiving in the TeleMessage account. When registering users, use the same email address that's used for their Microsoft 365 account.
- Ensure your employees have corporate-owned and corporate-liable mobile phones on the Verizon mobile network. Archiving messages in Microsoft 365 isn't available for employee-owned or Bring Your Own Devices (BYOD) devices.
- Assign the Data Connector Admin role to the user who creates a Verizon Network connector. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Create a Verizon Network connector

After you complete the prerequisites described in Before you begin, you can create a Verizon Network connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the TeleMessage site and transfer SMS and MMS messages to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Verizon Network**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Login to TeleMessage** page, under Step 3, enter the required information in the following boxes and then select **Next**.

    - **Username:** Your TeleMessage username.
    - **Password:** Your TeleMessage password.
7. After the connector is created, you can close the pop-up window and go to the next page.
8. On the **User mapping** page, enable automatic user mapping and select **Next**. If you need custom mapping, upload a CSV file, and select **Next**.
9. Review your settings, and then select **Finish** to create the connector.

## Limits for archiving Verizon Network data

Importing attachments or items supports files up to 10 MB.