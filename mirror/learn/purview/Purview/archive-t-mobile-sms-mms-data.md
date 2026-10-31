---
layout: Conceptual
title: Set up a connector to archive T-Mobile SMS/MMS data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-t-mobile-sms-mms-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how administrators can set up and use a data connector to import and archive T-Mobile SMS/MMS data into Microsoft 365.
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
document_id: 7cd01faf-b5ec-41dd-94ba-356c6c1c63c1
document_version_independent_id: 7cd01faf-b5ec-41dd-94ba-356c6c1c63c1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-t-mobile-sms-mms-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-t-mobile-sms-mms-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-t-mobile-sms-mms-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7dc81579-d744-1fef-4521-bb984e501469
---

# Set up a connector to archive T-Mobile SMS/MMS data | Microsoft Learn

Use a TeleMessage connector in the Microsoft Purview portal to import and archive SMS and MMS data from T-Mobile Mobile Network. After you set up and configure a connector, it connects to your organization's T-Mobile Network once every day, and imports SMS and MMS data to mailboxes in Microsoft Purview. Before you begin, you'll need a TeleMessage account, T-Mobile account details, corporate-owned devices on the T-Mobile network, and the appropriate Microsoft Purview permissions. For the full list of prerequisites, see Before you begin.

After storing SMS and MMS messages in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, and Microsoft 365 retention policies to T-Mobile Network data. For example, you can search T-Mobile Network data by using eDiscovery or associate the mailbox that contains the T-Mobile Network connector data with a custodian in an eDiscovery (Premium) case. Using a T-Mobile Network connector to import and archive data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Overview of archiving T-Mobile Network data

The following overview explains the process of using a connector to archive T-Mobile Network data in Microsoft 365.

![Archiving workflow for T-Mobile SMS/MMS data.](media/t-mobile-connector-workflow.png)

1. Your organization works with TeleMessage to set up a T-Mobile Network connector. For information, see [T-Mobile Network Archiver](https://www.telemessage.com).
2. In real time, SMS and MMS messages from your organization's T-Mobile Network are copied to the TeleMessage site.
3. The T-Mobile Network connector that you create in the Microsoft Purview portal connects to the TeleMessage site every day and transfers the SMS and MMS messages from the previous 24 hours to a secure Azure Storage location in the Microsoft cloud. The connector also converts the content of SMS and MMS messages to an email message format.
4. The connector imports the mobile communication items to the mailbox of specific users. A new folder named **T-Mobile SMS/MMS Network Archiver** is created in the user's mailbox and the items are imported to it. The connector does this mapping by using the value of the *User's Email address* property. Every SMS and MMS message contains this property, which is populated with the email address of every participant of the message.

In addition to automatic user mapping by using the value of the *User’s Email address* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file contains the mobile phone number and corresponding Microsoft 365 email address for users in your organization. If you enable both automatic user mapping and custom mapping, for every email item the connector first looks at the custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a mobile phone number, the connector uses the values in the email address property of the item it's trying to import. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or in the email address property of the email item, the item won't be imported.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

Some of the implementation steps required to archive T-Mobile Network data are external to Microsoft 365. You must complete these steps before you can create the connector in the Microsoft Purview portal.

- Order the [mobile archiver service from TeleMessage](https://www.telemessage.com) and get a valid administration account for your organization. You need to sign in to this account when you create the connector in the Microsoft Purview portal.
- Obtain your T-Mobile account and billing contact details so you can fill out the TeleMessage onboarding forms and order the message archiving service from T-Mobile.
- Register all users that require T-Mobile SMS/MMS Network archiving in the TeleMessage account. When registering users, be sure to use the same email address that's used for their Microsoft 365 account.
- Ensure users have corporate-owned and corporate-liable mobile phones on the T-Mobile mobile network. Archiving messages in Microsoft 365 isn't available for user-owned or "Bring Your Own Devices (BYOD)" devices.
- Assign the Data Connector Admin role to the user who creates a T-Mobile Network connector. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Create a T-Mobile Network connector

After you complete the prerequisites described in Before you begin, you can create a T-Mobile Network connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the TeleMessage site and transfer SMS and MMS messages to the corresponding user mailboxes in Microsoft 365.

1. Go to [Microsoft Purview portal](https://purview.microsoft.com/) and then select **Data connectors** &gt; **T-Mobile Network**.
2. On the **T-Mobile Network product** description page, select **Add connector**.
3. On the **Terms of service** page, select **Accept**.
4. On the **Login to TeleMessage** page, under Step 3, enter the required information in the following boxes and then select **Next**.

    - **Username:** Your TeleMessage username.
    - **Password:** Your TeleMessage password.
5. After the connector is created, you can close the pop-up window and go to the next page.
6. On the **User mapping** page, enable automatic user mapping. To enable custom mapping, upload a CSV file that contains the user mapping information, and then select **Next**.
7. Review your settings, and then select **Finish** to create the connector.
8. Go to the **Connectors** tab on the **Data connectors** page in the Microsoft Purview portal to see the progress of the import process for the new connector.

## T-Mobile connector limits

Importing attachments or items supports files up to 10 MB.