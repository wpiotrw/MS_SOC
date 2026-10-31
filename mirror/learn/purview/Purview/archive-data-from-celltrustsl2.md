---
layout: Conceptual
title: Archive data from the CellTrust SL2 platform to Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-data-from-celltrustsl2
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to set up and use a CellTrust SL2 data connector to import and archive mobile communications data.
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
document_id: f7a5b494-589c-17f0-dd61-029409a8a1b8
document_version_independent_id: f7a5b494-589c-17f0-dd61-029409a8a1b8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-data-from-celltrustsl2.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-data-from-celltrustsl2
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-data-from-celltrustsl2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b53f221e-5412-a88c-36c3-043f71057f5e
---

# Archive data from the CellTrust SL2 platform to Microsoft 365 | Microsoft Learn

CellTrust SL2 captures mobile communications data and integrates with the leading archiving technologies to meet the electronic discovery requirements for regulations such as FINRA, HIPAA, FOIA, and TCPA. The SL2 Data Connector imports mobile communication items to Microsoft 365. This article describes the process for integrating SL2 with Microsoft 365 by using the CellTrust SL2 Data Connector for archiving. To complete this process, you need a subscription to the CellTrust SL2 service and familiarity with the SL2 architecture. For information about CellTrust SL2, see https://www.celltrust.com.

After you import data to user mailboxes in Microsoft 365, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, Microsoft 365 retention policies, and Communication Compliance. By using the CellTrust SL2 Data Connector to import and archive data in Microsoft 365, your organization can stay compliant with government and regulatory policies.

## Overview of archiving with the CellTrust SL2 Data Connector

CellTrust's SL2 platform captures communication data from multiple sources. SL2 data sources are either Person-to-Person (P2P) or Application-to-Person (A2P). The process described in this article pertains only to P2P data sources. For all P2P data sources, at least one party in the collaboration is an SL2 user who subscribes to the SL2 service. The following overview explains the process of using the CellTrust SL2 Data Connector in Microsoft 365.

![Diagram of the CellTrust SL2 archiving workflow showing how mobile communications data flows from SL2 services through Azure to Microsoft 365.](media/celltrustsl2connectorworkflow.png)

1. SL2 users send and receive data to and from SL2 services in Microsoft Azure.
2. Your organization has an SL2 domain in CellTrust's SL2 Cloud Service environment. Your domain can have one or more organizational units (OUs). The SL2 Cloud Service transfers your data to a highly secure area in the Microsoft Azure platform, so that your data never leaves the Microsoft Azure environment. Depending on your SL2 plan (Enterprise, SMB, or Government), Microsoft Azure Global or Microsoft Azure Government hosts your domain.
3. After you create the CellTrust SL2 Data Connector in the [Microsoft Purview portal](purview-portal), your domain and OUs (regardless of your SL2 plan) begin sending data to Microsoft 365. The data feed is structured to support reporting based on data sources, OUs, or the domain by itself. As a result, your organization needs only one connector to feed all your data sources to Microsoft 365.
4. The connector creates a folder under each mapped user with an appropriate Microsoft 365 license titled **CellTrust SL2**. This mapping connects a CellTrust SL2 user to an Microsoft 365 mailbox by using an email address. If a user ID in CellTrust SL2 has no match in Microsoft 365, the user's data isn't archived.

## Before you begin

Important

All partner third-party data connector configurations require a provisioned [service principal](/en-us/entra/architecture/service-accounts-principal) for the partner application. This requirement isn't applicable for native Microsoft third-party data connector configurations.

To provision a service principal using PowerShell, see [Provision a service principal for partner third-party data connectors](archive-third-party-data#provision-a-service-principal-for-third-party-data-connectors).

- Verify that you have a domain in the CellTrust SL2 cloud service environment. For more information about obtaining a production or trial SL2 domain, [Contact CellTrust](https://www.celltrust.com/contact-us/#form).
- Get the credentials to access the administrator account for your SL2 domain.
- Assign the Data Connector Admin role to the user who creates the CellTrust SL2 data connector in the Microsoft Purview portal and completes the connector setup, including user mapping. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).
- This data connector is available in GCC environments in the Microsoft 365 US Government cloud. Third-party applications and services might involve storing, transmitting, and processing your organization's customer data on third-party systems that are outside of the Microsoft 365 infrastructure and therefore aren't covered by the Microsoft Purview and data protection commitments. Microsoft makes no representation that use of this product to connect to third-party applications implies that those third-party applications are FedRAMP compliant.
- A domain administrator can set up a connector for the domain or any OUs in that domain. If you use the OU Administrator account, you can only set up a connector for that specific OU.
- To successfully complete the setup steps, you must be assigned a Microsoft 365 E5 license and have the proper Microsoft Office admin rights.

## Step 1: Create a CellTrust SL2 connector

Create a data connector for CellTrust SL2 data in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **CellTrust SL2 (preview)** from the list.
5. Select **Accept** on the **Terms of service** page.
6. Enter a unique name that identifies the connector and select **Next**. The name you enter identifies the connector on the **Data connectors** page after you create it.
7. Select **Sign into CellTrust** on the **Sign in to your CellTrust account** page. You're redirected to the **CellTrust Portal for Microsoft 365** in a new browser window.

## Step 2: Select the domains or OUs to archive

To select domains and OUs for archiving, sign in to an administrator account for your CellTrust SL2 domain and choose which domains and OUs to archive in Microsoft 365.

1. On the CellTrust **Microsoft 365 Connector** page, select your environment in the SL2 cloud service to display a sign-in page.

    Typically, you see one option representing your environment. However, if you have domains in more than one environment, you see options for each environment. After you make a selection, you're redirected to the SL2 authentication page.
2. Sign in with your Domain or OU Administrator account credentials.

    If you sign in as an SL2 domain administrator, you see the name of your domain and the OUs in that domain. If you don't have OUs, you only see the name of your domain. If you sign in as OU Administrator, you only see the name of your OU.
3. Enable the business units you want to archive. Selecting the domain doesn't automatically select the OUs. You must enable each OU separately to archive it.

    ![Screenshot of the CellTrust SL2 connector configuration page showing organizational units (OUs) enabled for archiving in Microsoft 365.](media/enablecelltrustous.png)
4. When you finish your selections, close the browser window and return to the workflow page in Microsoft Purview portal. After a few seconds, the workflow automatically advances to the **User mapping** page.

## Step 3: Map users and complete the connector setup

To complete the connector setup, map users and finalize the configuration in the Microsoft Purview portal.

1. On the **User mapping** page, select **Enable automatic user mapping** if the email address for users is the same in both SL2 and Microsoft 365. Otherwise, manually provide user email addresses by uploading a CSV file that maps users' SL2 address to their Microsoft 365 address.
2. Select **Next**, review your settings, and then select **Finish** to create the connector.

    The new connector is added to the list on the **Data connectors** page.

Tip

To test the new connector, send a text message using your SL2 mobile app or from your SL2 portal. Go to your Microsoft 365 mailbox and open the **CellTrust SL2** folder in your Inbox. It might take a few minutes for the text messages to show up in your mailbox.

## Get help from CellTrust

For details about contacting CellTrust for help with setting up a CellTrust SL2 data connector, see the [CellTrust Customer Support page](https://www.celltrust.com/contact-us/#support).