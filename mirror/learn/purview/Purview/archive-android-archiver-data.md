---
layout: Conceptual
title: Set up a connector to archive Android mobile data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-android-archiver-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admins can set up a TeleMessage connector to import and archive SMS, MMS, and voice calls from Android mobile phones. This lets you archive data from third-party data sources in Microsoft 365 so you can use compliance features such as legal hold, eDiscovery, and retention policies to manage your organization's third-party data.
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
document_id: baa5f865-288e-a34b-1f60-bd6d25fcbd83
document_version_independent_id: baa5f865-288e-a34b-1f60-bd6d25fcbd83
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-android-archiver-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-android-archiver-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-android-archiver-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e0713607-225a-86e3-e8ce-ecfccfd865d0
---

# Set up a connector to archive Android mobile data | Microsoft Learn

Use a TeleMessage connector to import and archive SMS, MMS, voice calls, and call logs from Android mobile phones. After you set up and configure a connector, it connects to your organization's TeleMessage account once every day and imports the mobile communication of employees using the TeleMessage Android Archiver to mailboxes in Microsoft 365.

After storing data from Android mobile phones in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, and Microsoft 365 retention policies to Android Archiver data. For example, you can search Android Archiver mobile communication by using eDiscovery or associate the mailbox that contains the Android Archiver connector data with a custodian in an eDiscovery (Premium) case. Using an Android Archiver connector to import and archive data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Overview of archiving Android mobile data

The following overview explains the process of using a connector to archive Android mobile data in Microsoft 365.

![Android Archiver connector workflow diagram showing data flow from mobile phones to Microsoft 365.](media/androidarchiverconnectorworkflow.png)

1. Your organization works with TeleMessage to set up an Android Archiver connector. For more information, see [Android Archiver](https://www.telemessage.com).
2. In real time, SMS, MMS, voice calls, and call logs from your organization's Android mobile phones are copied to the TeleMessage site.
3. The Android Archiver connector that you create in the [Microsoft Purview portal](purview-portal) connects to the TeleMessage site every day and transfers the Android data from the previous 24 hours to a secure Azure Storage location in the Microsoft cloud. The connector also converts the Android data to an email message format.
4. The connector imports the mobile communication items to the mailbox of a specific user. A new folder named Android Archiver is created in the specific user's mailbox, and the items are imported to the folder. The connector does mapping by using the value of the *User's Email address* property. Every email message contains this property, which is populated with the email address of every participant of the email message. In addition to automatic user mapping by using the value of the *User's Email address* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file should contain the mobile number and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every email item the connector first looks at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's mobile number, the connector uses the user's email address property of the email item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *User's email address* property of the email item, the item won't be imported.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

Some of the implementation steps required to archive Android communication data are external to Microsoft 365. You must complete these steps before you can create the connector in the Microsoft Purview portal.

- Order the [Android Archiver service from TeleMessage](https://www.telemessage.com) and get a valid administration account for your organization. You need to sign in to this account when you create the connector.
- Register all users that require the Android Archiver service in the TeleMessage account. When registering users, use the same email address that's used for their Microsoft 365 account.
- Install and activate the TeleMessage Android Archiver app on the mobile phones of your employees.
- Assign the Data Connector Admin role to the user who creates a Android Archiver connector. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Create an Android Archiver connector

After completing the prerequisite tasks, create an Android Archiver connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the TeleMessage site and transfer Android communication to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Android Archiver**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Login to TeleMessage** page, enter the required information in the following boxes and then select **Next**.

    - **Username:** Your TeleMessage username.
    - **Password:** Your TeleMessage password.
7. After you create the connector, close the pop-up window and select **Next**.
8. On the **User mapping** page, enable automatic user mapping and select **Next**. If you need custom mapping, upload a CSV file, and select **Next**.
9. Review your settings, then select **Finish** to create the connector.

## Android Archiver connector limits

The connector supports importing attachments or items up to 10 MB.