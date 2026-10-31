---
layout: Conceptual
title: Set up a connector to archive Instant Bloomberg data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how administrators can set up and use a data connector to import and archive data from the Instant Bloomberg chat tool into Microsoft 365.
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
document_id: 56a35b1c-a3e0-096b-1a41-8b6bb8195764
document_version_independent_id: 56a35b1c-a3e0-096b-1a41-8b6bb8195764
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-instant-bloomberg-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-instant-bloomberg-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-instant-bloomberg-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 842dd45f-a678-d9db-270e-f549f2333588
---

# Set up a connector to archive Instant Bloomberg data | Microsoft Learn

Use a connector to import and archive financial services chat data from the [Instant Bloomberg](https://www.bloomberg.com/professional/products/bloomberg-terminal/collaboration-tools/) collaboration tool. After you set up and configure a connector, it connects to your organization's Bloomberg secure FTP site (SFTP) once every day, converts the content of chat messages to an email message format, and then imports those items to mailboxes in Microsoft 365.

After storing Instant Bloomberg data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to Instant Bloomberg data. For example, you can search Instant Bloomberg chat messages by using eDiscovery or associate the mailbox that contains the Instant Bloomberg data with a custodian in a Microsoft Purview eDiscovery (Premium) case. By using an Instant Bloomberg connector to import and archive data in Microsoft 365, you can help your organization stay compliant with government and regulatory policies.

## Overview of archiving Instant Bloomberg data

The following overview explains the process of using a connector to archive Instant Bloomberg chat data in Microsoft 365.

![Diagram of the Instant Bloomberg import and archive process showing data flowing from Bloomberg SFTP site into Microsoft 365 mailboxes.](media/instantbloombergdataarchiving.png)

1. Your organization works with Bloomberg to set up a Bloomberg SFTP site. You also work with Bloomberg to configure Instant Bloomberg to copy chat messages to your Bloomberg SFTP site.
2. Every 24 hours, Instant Bloomberg copies chat messages to the Bloomberg SFTP site.
3. The Instant Bloomberg connector that you create in the [Microsoft Purview portal](purview-portal) connects to the Bloomberg SFTP site every day and transfers the chat messages from the previous 24 hours to a secure Azure Storage area in the Microsoft Cloud. The connector also converts the content of a chat massage to an email message format.
4. The connector imports the chat message items to the mailbox of a specific user. A new folder named InstantBloomberg is created in the specific user's mailbox and the items are imported to it. The connector uses the value of the *CorporateEmailAddress* property. Every chat message contains this property, which is populated with the email address of every participant of the chat message. In addition to automatic user mapping by using the value of the *CorporateEmailAddress* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file should contain a Bloomberg UUID and the corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every chat item the connector first looks at custom-mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector uses the *CorporateEmailAddress* property of the chat item. If the connector doesn't find a valid Microsoft 365 user in either the custom-mapping file or the *CorporateEmailAddress* property of the chat item, the item isn't imported.

## Before you begin

Some of the implementation steps required to archive Instant Bloomberg data are external to Microsoft 365. You must complete these steps before you can create the connector in the Microsoft Purview portal.

- To set up an Instant Bloomberg connector, you need keys and key passphrases for Pretty Good Privacy (PGP) and Secure Shell (SSH). Use these keys to configure the Bloomberg SFTP site. The connector uses these keys to connect to the Bloomberg SFTP site and import data to Microsoft 365. Use the PGP key to configure the encryption of data that's transferred from the Bloomberg SFTP site to Microsoft 365. Use the SSH key to configure secure shell to enable a secure remote authentication when the connector connects to the Bloomberg SFTP site.

    When setting up a connector, you can use public keys and key passphrases provided by Microsoft or use your own private keys and passphrases. Use the public keys provided by Microsoft. However, if your organization already configured a Bloomberg SFTP site by using private keys, you can create a connector by using these same private keys.
- Subscribe to [Bloomberg Anywhere](https://www.bloomberg.com/professional/product/remote-access/?bbgsum-page=DG-WS-PROF-PROD-BBA). This subscription is required so that you can sign in to Bloomberg Anywhere to access the Bloomberg SFTP site that you set up and configure.
- Set up a Bloomberg SFTP (Secure file transfer protocol) site. After working with Bloomberg to set up the SFTP site, data from Instant Bloomberg is uploaded to the SFTP site every day. The connector you create in Step 2 connects to this SFTP site and transfers the chat data to Microsoft 365 mailboxes. SFTP also encrypts the Instant Bloomberg chat data that you send to mailboxes during the transfer process.

    For external information about Bloomberg SFTP (also called *BB-SFTP*), use the following resources:

    - See the "SFTP Connectivity Standards" document at [Bloomberg Support](https://www.bloomberg.com/professional/support/documentation/).
    - Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc).

    After you work with Bloomberg to set up an SFTP site, Bloomberg provides some information to you after you respond to the Bloomberg implementation email message. Save a copy of the following information. You use it to set up a connector in Step 3.

    - Firm code, which is an ID for your organization and is used to sign in to the Bloomberg SFTP site.
    - Password for your Bloomberg SFTP site
    - URL for Bloomberg SFTP site (for example, sftp.bloomberg.com)
    - Port number for Bloomberg SFTP site
- The Instant Bloomberg connector can import a total of 200,000 items in a single day. If there are more than 200,000 items on the SFTP site, none of those items are imported to Microsoft 365.
- The user who downloads the public keys and IP address in the "Get PGP and SSH and public keys" procedure and creates the connector in the "Create an Instant Bloomberg connector" procedure must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Set up a connector by using public keys

The steps in this section show you how to set up an Instant Bloomberg connector by using the public keys for Pretty Good Privacy (PGP) and Secure Shell (SSH).

### Step 1: Get PGP and SSH and public keys

First, get a copy of the public keys for Pretty Good Privacy (PGP) and Secure Shell (SSH). You use these keys to configure the Bloomberg SFTP site and to allow the Instant Bloomberg connector that you create later to connect to the SFTP site and transfer the Instant Bloomberg chat data to Microsoft 365 mailboxes. You also download an IP address during this key-download procedure, which you use when configuring the Bloomberg SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Instant Bloomberg**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH public keys provided by Microsoft**.
7. Under step 1, select the **Download SSH key**, **Download PGP key**, and **Download IP address** links to save a copy of each file to your local computer.

    These files contain the following items that you use to configure the Bloomberg SFTP site in Step 2:

    - PGP public key: Use this key to configure the encryption of data that's transferred from the Bloomberg SFTP site to Microsoft 365.
    - SSH public key: Use this key to configure secure shell to enable a secure remote authentication when the connector connects to the Bloomberg SFTP site.
    - IP address: Configure the Bloomberg SFTP site to accept connection requests from this IP address. The same IP address is used by the Instant Bloomberg connector to connect to the SFTP site and transfer Instant Bloomberg data to Microsoft 365.
8. Select **Cancel** to close the Add credentials workflow. You return to this connector setup workflow later to create the Instant Bloomberg connector.

### Step 2: Configure the Bloomberg SFTP site

Use the PGP and SSH public keys and the IP address that you downloaded earlier to set up PGP encryption and SSH authentication for the Bloomberg SFTP site. The PGP encryption and SSH authentication configuration lets the Instant Bloomberg connector connect to the Bloomberg SFTP site and transfer Instant Bloomberg data to Microsoft 365 after you create the connector later in this procedure. You need to work with Bloomberg customer support to set up your Bloomberg SFTP site. Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc) for assistance.

Important

Bloomberg recommends that you attach the downloaded SSH key, PGP key, and IP address files to an email message and send them to their customer support team when working with them to set up your Bloomberg SFTP site.

### Step 3: Create an Instant Bloomberg connector

In this step, you create an Instant Bloomberg connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the Bloomberg SFTP site and transfer chat messages to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Instant Bloomberg**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for Bloomberg SFTP site** page, in the SFTP credentials section, enter the required information in the following boxes and then select **Next**.

    - **Firm code:** The ID for your organization that Bloomberg uses as the username for the SFTP site.
    - **Password:** Password for Bloomberg SFTP site.
    - **SFTP URL:** The URL for Bloomberg SFTP site (for example, `sftp.bloomberg.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for Bloomberg SFTP site. The connector uses this port to connect to the SFTP site.
7. On the **Define user** page, select one of the following options to specify the users whose data you want to import.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
8. On the **Select data types to import** page, select the required data types to be imported apart from **Messages**
9. On the **Map Instant Bloomberg users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required

    Note

    The connector imports the chat message items to the mailbox of a specific user. A new folder named **InstantBloomberg** is created in the specific user's mailbox and the items are imported to it. The connector uses the value of the *CorporateEmailAddress* property. Every chat message contains this property, and the property is populated with the email address of every participant of the chat message. In addition to automatic user mapping using the value of the *CorporateEmailAddress* property, you can also define custom mapping by uploading a CSV mapping file. The mapping file should contain the Bloomberg UUID and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every chat item the connector first looks at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector uses the *CorporateEmailAddress* property of the chat item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *CorporateEmailAddress* property of the chat item, the item won't be imported.
10. Select **Next**, review your settings, and then select **Finish** to create the connector.

## Set up a connector by using private keys

The following procedure shows how to set up an Instant Bloomberg connector by using PGP and SSH private keys. Use this connector setup option if your organization already configured a Bloomberg SFTP site by using private keys.

### Step 1: Get an IP address to configure the Bloomberg SFTP site

Note

If your organization previously configured a Bloomberg SFTP site to archive Bloomberg Message data by using PGP and SSH private keys, you don't need to configure another one. You can specify the previously configured Bloomberg SFTP site when you create the Instant Bloomberg connector later in this procedure.

If your organization uses PGP and SSH private keys to set up a Bloomberg SFTP site, you need to get an IP address and give it to Bloomberg customer support. The Bloomberg SFTP site must accept connection requests from this IP address. The same IP address is used by the Instant Bloomberg connector to connect to the SFTP site and transfer Instant Bloomberg data to Microsoft 365.

To get the IP address:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Instant Bloomberg**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.
7. Under step 1, select **Download IP address** to save a copy of the IP address file to your local computer.

    ![Screenshot of the connector setup page showing the Download IP address link for configuring the Bloomberg SFTP site.](media/instantbloombergconnectoripaddress.png)
8. Select **Cancel** to close the workflow. You return to this workflow in Step 2 to create the connector.

Work with Bloomberg customer support to configure your Bloomberg SFTP site to accept connection requests from this IP address. Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc) for assistance.

### Step 2: Create an Instant Bloomberg connector

After you configure your Bloomberg SFTP site, create an Instant Bloomberg connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the Bloomberg SFTP site and transfer email messages to the corresponding user mailboxes in Microsoft 365. Before creating the connector, be sure to have copies of the PGP and SSH private keys and key passphrases that you used to set up your Bloomberg SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Instant Bloomberg**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.

    ![Screenshot of the Add credentials for content source page showing the option to use PGP and SSH private keys selected.](media/instantbloombergprivatekeysoption.png)
7. In the connection details section, enter the required information in the following boxes and then select **Validate connection**.

    - **Name:** The name for the connector. It must be unique in your organization.
    - **Firm code:** The ID for your organization that Bloomberg uses as the username for the SFTP site.
    - **Password:** The password for your organization's Bloomberg SFTP site.
    - **SFTP URL:** The URL for the Bloomberg SFTP site (for example, `sftp.bloomberg.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for the Bloomberg SFTP site. The connector uses this port to connect to the SFTP site.
    - **PGP private key:** The PGP private key for the Bloomberg SFTP site. Be sure to include the entire private key value, including the beginning and ending lines of the key block.
    - **PGP key passphrase:** The passphrase for the PGP private key.
    - **SSH private key:** The SSH private key for the Bloomberg SFTP site. Be sure to include the entire private key value, including the beginning and ending lines of the key block.
    - **SSH key passphrase:** The passphrase for the SSH private key.
8. After the connection is successfully validated, select **Next**.
9. On the **Define user** page, select one of the following options to specify the users whose data you want to import.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
10. On the **Map Instant Bloomberg users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required.

    Note

    The connector imports the chat message items to the mailbox of a specific user. A new folder named **InstantBloomberg** is created in the specific user's mailbox and the items are imported to it. The connector uses the value of the *CorporateEmailAddress* property. Every chat message contains this property, and the property is populated with the email address of every participant of the chat message. In addition to automatic user mapping using the value of the *CorporateEmailAddress* property, you can also define custom mapping by uploading a CSV mapping file. The mapping file should contain the Bloomberg UUID and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every chat item the connector first looks at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector uses the *CorporateEmailAddress* property of the chat item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *CorporateEmailAddress* property of the chat item, the item won't be imported.
11. Select **Next**, review your settings, and then select **Finish** to create the connector.