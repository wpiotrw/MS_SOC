---
layout: Conceptual
title: Set up a connector to archive Bloomberg Message data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-bloomberg-message-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators can set up a data connector to import and archive data from the Bloomberg Message email tool in Microsoft 365. This lets you archive data from third-party data sources in Microsoft 365 so you can use compliance features such as legal hold, eDiscovery, and retention policies to manage your organization's third-party data.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
ms.collection:
- purview-compliance
- data-connectors
ai-usage: ai-assisted
locale: en-us
document_id: e65a6ee3-1c6c-47ba-afd1-ec022cc4c76c
document_version_independent_id: e65a6ee3-1c6c-47ba-afd1-ec022cc4c76c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-bloomberg-message-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-bloomberg-message-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-bloomberg-message-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 884c69e4-7b38-dd7f-44c6-7f431844f22b
---

# Set up a connector to archive Bloomberg Message data | Microsoft Learn

Use a data connector to import and archive financial services email data from the [Bloomberg Message](https://www.bloomberg.com/professional/products/bloomberg-terminal/collaboration-tools/) collaboration tool. After you set up and configure a connector, it connects to your organization's Bloomberg secure FTP (SFTP) site once every day, and imports email items to mailboxes in Microsoft 365.

After storing Bloomberg Message data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to Bloomberg Message data. For example, you can search Bloomberg Message emails by using eDiscovery or associate the mailbox that contains the Bloomberg Message data with a custodian in an eDiscovery (Premium) case. Using a Bloomberg Message connector to import and archive data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Overview of archiving Bloomberg Message data

The following overview explains the process of using a connector to archive Bloomberg Message data in Microsoft 365.

![Bloomberg Message import and archive process.](media/bloombergmessagearchiving.png)

1. Your organization works with Bloomberg to set up a Bloomberg SFTP site. You also work with Bloomberg to configure Bloomberg Message to copy email messages to the Bloomberg SFTP site.
2. Every 24 hours, Bloomberg Message copies email messages to the Bloomberg SFTP site.
3. The Bloomberg Message connector that you create in the [Microsoft Purview portal](purview-portal) connects to the Bloomberg SFTP site every day and transfers the email messages from the previous 24 hours to a secure Azure Storage area in the Microsoft Cloud.
4. The connector imports the email message items to the mailbox of a specific user. A new folder named BloombergMessage is created in the specific user's mailbox and the items are imported to it.

    The connector uses the value of the CorporateEmailAddress property. Every email message contains this property, which is populated with the email address of every participant of the email message. In addition to automatic user mapping by using the value of the *CorporateEmailAddress* property, you can also define a custom mapping by uploading a CSV mapping file. This mapping file contains a Bloomberg UUID and the corresponding Microsoft 365 mailbox address for each user in your organization. If you enable automatic user mapping and provide a custom mapping, for every email item the connector first looks at the custom-mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector uses the *CorporateEmailAddress* property of the email item. If the connector doesn't find a valid Microsoft 365 user in either the custom-mapping file or the *CorporateEmailAddress* property of the email item, the item won't be imported.

## Before you begin

Some of the implementation steps for archiving Bloomberg Message data are external to Microsoft 365. You must complete these steps before you create the connector in the Microsoft Purview portal.

- To set up a Bloomberg Message connector, you need keys and key passphrases for Pretty Good Privacy (PGP) and Secure Shell (SSH). Use these keys to configure the Bloomberg SFTP site. The connector uses these keys to connect to the Bloomberg SFTP site and import data to Microsoft 365. Use the PGP key to configure the encryption of data that's transferred from the Bloomberg SFTP site to Microsoft 365. Use the SSH key to configure secure shell to enable a secure remote authentication when the connector connects to the Bloomberg SFTP site.

    When setting up a connector, you can use public keys and key passphrases provided by Microsoft or use your own private keys and passphrases. Use the public keys provided by Microsoft. However, if your organization already configured a Bloomberg SFTP site by using private keys, you can create a connector by using these same private keys.
- Subscribe to [Bloomberg Anywhere](https://www.bloomberg.com/professional/product/remote-access/?bbgsum-page=DG-WS-PROF-PROD-BBA). This subscription is required so that you can sign in to Bloomberg Anywhere to access the Bloomberg SFTP site that you set up and configure.
- Set up a Bloomberg SFTP (Secure file transfer protocol) site. After working with Bloomberg to set up the SFTP site, data from Bloomberg Message is uploaded to the SFTP site every day. The connector you create in Step 2 connects to this SFTP site and transfers the email data to Microsoft 365 mailboxes. SFTP also encrypts the Bloomberg Message data that is sent to mailboxes during the transfer process.

    For information about Bloomberg SFTP (also called *BB-SFTP*):

    - See the "SFTP Connectivity Standards" document at [Bloomberg Support](https://www.bloomberg.com/professional/support/documentation/).
    - Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc).
- After you work with Bloomberg to set up an SFTP site, Bloomberg provides some information to you after you respond to the Bloomberg implementation email message. Save a copy of the following information. You use it to set up a connector in Step 3.

    - Firm code, which is an ID for your organization and is used to sign in to the Bloomberg SFTP site.
    - Password for your Bloomberg SFTP site
    - URL for Bloomberg SFTP site (for example, sftp.bloomberg.com). In addition, Bloomberg might also provide a corresponding IP address for the Bloomberg SFTP site, which you can also use to set up the connector.
    - Port number for Bloomberg SFTP site
- The Bloomberg Message connector can import a total of 200,000 items in a single day. If there are more than 200,000 items on the SFTP site, none of those items are imported to Microsoft 365.
- The user who creates a Bloomberg Message connector in Step 3 (and who downloads the public keys and IP address in Step 1) must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Set up a connector by using public keys

The following steps show you how to set up a Bloomberg Message connector by using the public keys for Pretty Good Privacy (PGP) and Secure Shell (SSH).

### Step 1: Obtain PGP and SSH public keys

First, get a copy of the PGP and SSH public keys. You use these keys in Step 2 to set up the Bloomberg SFTP site so it allows the connector (that you create in Step 3) to connect to the SFTP site and transfer the Bloomberg Message email data to Microsoft 365 mailboxes. You also get an IP address in this step, which you use when configuring the Bloomberg SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Bloomberg Message**, select **View**.
5. On the **Bloomberg Message** product description page, select **Add connector**.
6. On the **Terms of service** page, select **Accept**.
7. On the **Add credentials for content source** page, select **I want to use PGP and SSH public keys provided by Microsoft**.

    ![Select the option to use public keys.](media/bloombergmessagepublickeysoption.png)
8. Under step 1, select the **Download SSH key**, **Download PGP key**, and **Download IP address** links to save a copy of each file to your local computer.

    ![Links to download public keys and IP address.](media/bloombergmessagepublickeydownloadlinks.png)

    These files contain the following items that you use to configure the Bloomberg SFTP site in Step 2:

    - PGP public key: Use this key to configure the encryption of data that's transferred from the Bloomberg SFTP site to Microsoft 365.
    - SSH public key: Use this key to configure secure shell to enable a secure remote authentication when the connector connects to the Bloomberg SFTP site.
    - IP address: Configure the Bloomberg SFTP site to accept connection requests from this IP address. The same IP address is used by the Bloomberg Message connector to connect to the SFTP site and transfer Bloomberg Message data to Microsoft 365.
9. Select **Cancel** to close the workflow. You come back to this workflow in Step 3 to create the connector.

### Step 2: Configure the Bloomberg SFTP site

Note

If your organization previously set up a Bloomberg SFTP site to archive Instant Bloomberg data by using public PGP and SSH keys, you don't need to set up another one. You can specify the same SFTP site when you create the connector in Step 3.

Use the PGP and SSH public keys and the IP address that you got in Step 1 to configure PGP encryption and SSH authentication for the Bloomberg SFTP site. This configuration lets the Bloomberg Message connector that you create in Step 3 connect to the Bloomberg SFTP site and transfer Bloomberg Message data to Microsoft 365. You need to work with Bloomberg customer support to set up your Bloomberg SFTP site. Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc) for assistance.

Important

Bloomberg recommends that you attach the three files that you download in Step 1 to an email message and send it to their customer support team when working with them to set up your Bloomberg SFTP site.

### Step 3: Create a Bloomberg Message connector

In this step, you create a Bloomberg Message connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the Bloomberg SFTP site and transfer email messages to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **Bloomberg Message** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH public keys provided by Microsoft**.
7. Under Step 3, enter the required information in the following boxes and then select **Validate connection**.

    - **Name:** The name for the connector. It must be unique in your organization.
    - **Firm code:** The ID for your organization that is used as the username for the Bloomberg SFTP site.
    - **Password:** The password for your organization's Bloomberg SFTP site.
    - **SFTP URL:** The URL for the Bloomberg SFTP site (for example, `sftp.bloomberg.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for the Bloomberg SFTP site. The connector uses this port to connect to the SFTP site.
8. After the connection is successfully validated, select **Next**.
9. On the **Define user** page, specify the users to import data for.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
10. On the **Map Bloomberg Message users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required.

    Note

    The connector imports message items to the mailbox of a specific user. A new folder named **BloombergMessage** is created in the specific user's mailbox and the items are imported to it. The connector uses the value of the *CorporateEmailAddress* property. Every chat message contains this property, and the property is populated with the email address of every participant of the chat message. In addition to automatic user mapping using the value of the *CorporateEmailAddress* property, you can also define custom mapping by uploading a CSV mapping file. The mapping file should contain the Bloomberg UUID and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every message item the connector will first look at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector will use the *CorporateEmailAddress* property of the chat item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *CorporateEmailAddress* property of the message item, the item won't be imported.
11. Select **Next**, review your settings, and then select **Finish** to create the connector.

## Set up a connector by using private keys

The steps in this section show you how to set up a Bloomberg Message connector by using PGP and SSH private keys. Use this connector setup option if your organization already configured a Bloomberg SFTP site by using private keys.

### Step 1: Obtain an IP address to configure the Bloomberg SFTP site

Note

If your organization previously configured a Bloomberg SFTP site to archive Instant Bloomberg data by using PGP and SSH private keys, you don't need to configure another one. You can specify the same SFTP site when you create the connector in Step 2.

If your organization used PGP and SSH private keys to set up a Bloomberg SFTP site, you need to obtain an IP address and provide it to Bloomberg customer support. The Bloomberg SFTP site must be configured to accept connection requests from this IP address. The same IP address is used by the Bloomberg Message connector to connect to the SFTP site and transfer Bloomberg Message data to Microsoft 365.

To obtain the IP address:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **Bloomberg Message** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.
7. Under step 1, select **Download IP address** to save a copy of the IP address file to your local computer.

    ![Download the IP address.](media/bloombergmessageconnectoripaddress.png)
8. Select **Cancel** to close the workflow. You come back to this workflow in Step 4 to create the connector.

You need to work with Bloomberg customer support to configure your Bloomberg SFTP site to accept connection requests from this IP address. Contact [Bloomberg customer support](https://service.bloomberg.com/portal/sessions/new?utm_source=bloomberg-menu&amp;utm_medium=csc) for assistance.

### Step 2: Create a Bloomberg Message connector

After configuring your Bloomberg SFTP site, create a Bloomberg Message connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the Bloomberg SFTP site and transfer email messages to the corresponding user mailboxes in Microsoft 365. To complete this step, have copies of the same private keys and key passphrases that you used to set up your Bloomberg SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **Bloomberg Message** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.

    ![Select the option to use private keys.](media/bloombergmessageprivatekeysoption.png)
7. Under Step 3, enter the required information in the following boxes and then select **Validate connection**.

    - **Name:** The name for the connector. It must be unique in your organization.
    - **Firm code:** The ID for your organization that is used as the username for the Bloomberg SFTP site.
    - **Password:** The password for your organization's Bloomberg SFTP site.
    - **SFTP URL:** The URL for the Bloomberg SFTP site (for example, `sftp.bloomberg.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for the Bloomberg SFTP site. The connector uses this port to connect to the SFTP site.
    - **PGP private key:** The PGP private key for the Bloomberg SFTP site. Include the entire private key value, including the beginning and ending lines of the key block.
    - **PGP key passphrase:** The passphrase for the PGP private key.
    - **SSH private key:** The SSH private key for the Bloomberg SFTP site. Include the entire private key value, including the beginning and ending lines of the key block.
    - **SSH key passphrase:** The passphrase for the SSH private key.
8. After the connection is successfully validated, select **Next**.
9. On the **Define user** page, specify the users to import data for.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
10. On the **Map Bloomberg Message users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required.

    Note

    The connector imports message items to the mailbox of a specific user. A new folder named **BloombergMessage** is created in the specific user's mailbox and the items are imported to it. The connector uses the value of the *CorporateEmailAddress* property. Every chat message contains this property, and the property is populated with the email address of every participant of the chat message. In addition to automatic user mapping using the value of the *CorporateEmailAddress* property, you can also define custom mapping by uploading a CSV mapping file. The mapping file should contain the Bloomberg UUID and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every message item the connector will first look at custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's Bloomberg UUID, the connector will use the *CorporateEmailAddress* property of the chat item. If the connector doesn't find a valid Microsoft 365 user in either the custom mapping file or the *CorporateEmailAddress* property of the message item, the item won't be imported.
11. Select **Next**, review your settings, and then select **Finish** to create the connector.

## Limits

- Microsoft 365 doesn't support threading for Bloomberg Message email. The system imports individual messages sent to a person, but it doesn't show them in a threaded conversation.