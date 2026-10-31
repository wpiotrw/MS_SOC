---
layout: Conceptual
title: Set up a connector to archive Rogers Network data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-rogers-network-archiver-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admins can set up a TeleMessage connector to import and archive Rogers Network data in Microsoft 365. This lets you archive data from third-party data sources in Microsoft 365 so you can use compliance features such as legal hold, eDiscovery, and retention policies to manage your organization's third-party data.
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
document_id: 40d12359-742f-7d8d-6012-46f573d8a853
document_version_independent_id: 40d12359-742f-7d8d-6012-46f573d8a853
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-rogers-network-archiver-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-rogers-network-archiver-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-rogers-network-archiver-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7357edea-fb0f-380b-37a3-b36a952767ef
---

# Set up a connector to archive Rogers Network data in Microsoft 365 | Microsoft Learn

Use the TeleMessage connector to import and archive SMS and MMS data from the Rogers mobile network. When you set up and configure a [Rogers Network Archiver connector](https://www.telemessage.com), it connects to your organization's Rogers mobile network and imports SMS and MMS data to mailboxes in Microsoft 365. Before you set up the connector, you need a TeleMessage account, Rogers account details, and the Data Connector Admin role. For the full list of prerequisites, see Before you begin.

After storing data from the Rogers mobile network in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, and Microsoft 365 retention policies to the data. For example, you can search for SMS and MMS messages from the Rogers mobile network by using eDiscovery or a search associated with a Microsoft Purview eDiscovery case. Using a Rogers Network Archiver connector to import and archive data in Microsoft 365 can help your organization stay compliant with corporate governance regulations and regulatory policies.

## Overview of archiving Rogers mobile network data

The following overview explains the process of using a connector to archive Rogers SMS and MMS data in Microsoft 365.

![Diagram of the Rogers Network Archiver connector workflow showing data flow from the Rogers mobile network through TeleMessage to Microsoft 365 user mailboxes.](media/rogersnetworkconnectorworkflow.png)

1. Your organization works with TeleMessage to set up a Rogers Network Archiver connector. For more information, see [Activating the TeleMessage Rogers Network Archiver for Microsoft 365](https://www.telemessage.com).
2. In real time, your organization's Rogers mobile network copies data to the TeleMessage site.
3. The Rogers Network Archiver connector that you create in the [Microsoft Purview portal](purview-portal) connects to the TeleMessage site every day and transfers the email messages from the previous 24 hours to a secure Azure Storage area in the Microsoft Cloud.
4. The connector imports the mobile communication items to the mailbox of a specific user. A new folder named Rogers SMS/MMS Network Archiver is created in the specific user's mailbox and the items are imported to it. The connector does the mapping by using the value of the *User's Email address* property. Every email message contains this property, which is populated with the email address of every participant of the email message.

    In addition to automatic user mapping by using the value of the *User's Email address* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file should contain User's mobile Number and the corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every email item the connector first looks at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's mobile number, the connector uses the user's email address property of the email item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *user's email address* property of the email item, the item isn't imported.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

- Order the [Rogers Network Archiver service from TeleMessage](https://www.telemessage.com) and get a valid administration account for your organization. You need to sign in to this account when you create the connector in the Microsoft Purview portal.
- Register all users that require Rogers Network archiving in the TeleMessage account. When registering users, use the same email address that's used for their Microsoft 365 account.
- Ensure your employees have corporate-owned and corporate-liable mobile phones on the O2 mobile network. Archiving messages in Microsoft 365 isn't available for employee-owned or "Bring Your Own Devices (BYOD) devices.
- Get the Rogers account and billing contact details for your organization so that you can complete the onboarding forms and order the message archiving service from Rogers.
- Assign the Data Connector Admin role to the user who creates the Rogers Network Archiver connector in Create a Rogers Network Archiver connector. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Create a Rogers Network Archiver connector

After you complete the prerequisites described in Before you begin, you can create the Rogers Network Archiver connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the TeleMessage site and transfer Rogers SMS/MMS data to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Rogers Network Archiver**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Login to TeleMessage** page, in the credentials section of the login form, enter the required information in the following boxes and then select **Next**.

    - **Username:** Your TeleMessage username.
    - **Password:** Your TeleMessage password.
7. After the connector is created, you can close the pop-up window and go to the next page.
8. On the **User mapping** page, enable automatic user mapping. To enable custom mapping, upload a CSV file that contains the user mapping information, and then select **Next**.
9. Review your settings, and then select **Finish** to create the connector.

## Rogers Network Archiver limits

Importing attachments or items supports files up to 10 MB.