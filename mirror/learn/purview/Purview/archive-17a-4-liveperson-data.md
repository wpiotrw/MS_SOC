---
layout: Conceptual
title: Set up a connector to archive LivePerson Conversational Cloud data in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-17a-4-liveperson-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to set up and use a 17a-4 LivePerson Conversational Cloud DataParser connector to import and archive LivePerson Conversational Cloud data in Microsoft 365.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-20T00:00:00.0000000Z
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
document_id: ec69c976-4201-3dfc-5b53-7ff703ba528c
document_version_independent_id: ec69c976-4201-3dfc-5b53-7ff703ba528c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-17a-4-liveperson-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-17a-4-liveperson-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-17a-4-liveperson-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 32e30d0a-472f-73dd-f7c9-835570d847c3
---

# Set up a connector to archive LivePerson Conversational Cloud data in Microsoft 365 | Microsoft Learn

Use the [LivePerson Conversational Cloud DataParser](https://www.17a-4.com/liveperson-dataparser/) from 17a-4 LLC to import and archive data from LivePerson Conversational Cloud to user mailboxes in your Microsoft 365 organization. The DataParser includes a LivePerson Conversational Cloud connector that's configured to capture items from a third-party data source and import those items to Microsoft 365. The LivePerson Conversational Cloud DataParser connector converts data to an email message format and then imports those items to user mailboxes in Microsoft 365.

After you store data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, retention policies and retention labels, and Communication Compliance. By using a LivePerson Conversational Cloud connector to import and archive data in Microsoft 365, you help your organization stay compliant with government and regulatory policies.

## Overview of archiving LivePerson Conversational Cloud data

The following overview explains the process of using a data connector to archive LivePerson Conversational Cloud data in Microsoft 365.

![Archiving workflow for LivePerson Conversational Cloud data from 17a-4.](media/liveengagedataparserconnectorworkflow.png)

1. Your organization works with 17a-4 to set up and configure the LivePerson Conversational Cloud DataParser.
2. The DataParser regularly collects LivePerson Conversational Cloud items and converts the content of a message to an email message format.
3. You create the LivePerson Conversational Cloud DataParser connector in the [Microsoft Purview portal](purview-portal). The connector connects to DataParser and transfers the messages to a secure Azure Storage location in the Microsoft cloud.
4. The connector creates a subfolder in the Inbox folder named **LivePerson Conversational Cloud DataParser** in the user mailboxes and imports the items to that folder. The connector uses the value of the *Email* property to determine which mailbox to import items to. Every item contains this property, which is populated with the email address of every participant.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

- Create a DataParser account for Microsoft connectors. To create an account, contact [17a-4 LLC](https://www.17a-4.com/contact/). You need to sign in to this account when you set up the LivePerson Conversational Cloud DataParser connector in the Microsoft Purview portal.
- Assign the Data Connector Admin role to the user who sets up and completes the LivePerson Conversational Cloud DataParser connector configuration in the Microsoft Purview portal. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.

## Step 1: Set up a LivePerson Conversational Cloud DataParser connector

Create a 17a-4 connector for LivePerson Conversational Cloud data in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **LivePerson Conversational Cloud DataParser**.
5. On the **Terms of service** page, select **Accept**.
6. Enter a unique name that identifies the connector and then select **Next**.
7. Sign in to your 17a-4 account and complete the steps in the LivePerson Conversational Cloud DataParser connection workflow.

## Step 2: Configure the LivePerson Conversational Cloud DataParser connector

Work with 17a-4 Support to configure the LivePerson Conversational Cloud DataParser connector.

## Step 3: Map LivePerson Conversational Cloud users to Microsoft 365 users

The LivePerson Conversational Cloud DataParser connector automatically maps users to their Microsoft 365 email addresses before importing data to Microsoft 365.

## Step 4: Monitor the LivePerson Conversational Cloud DataParser connector

After you create a LivePerson Conversational Cloud DataParser connector, you can view the connector status in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select the LivePerson Conversational Cloud DataParser connector that you created to display the flyout page, which contains the properties and information about the connector.
4. Under **Connector status with source**, select the **Download log** link to open (or save) the status log for the connector. This log contains information about the data that's been imported to the Microsoft cloud. For more information, see [View admin logs for data connectors](data-connector-admin-logs).

## Connector limits for archiving LivePerson Conversational Cloud data

Importing attachments or items supports files up to 10 MB.