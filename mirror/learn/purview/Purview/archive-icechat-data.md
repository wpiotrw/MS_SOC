---
layout: Conceptual
title: Set up a connector to archive ICE Chat data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-icechat-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admins can set up a connector to import and archive data from the ICE Chat tool into Microsoft 365. This lets you archive data from third-party data sources in Microsoft 365 so you can use compliance features such as legal hold, eDiscovery, and retention policies to manage your organization's third-party data.
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
document_id: 20a97718-d07c-c396-5ade-a7c799171ee6
document_version_independent_id: 20a97718-d07c-c396-5ade-a7c799171ee6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-icechat-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-icechat-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-icechat-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1c2f5322-1cc7-0389-1881-7c6a5c234c41
---

# Set up a connector to archive ICE Chat data | Microsoft Learn

Use a native connector to import and archive financial services chat data from the ICE Chat collaboration tool. After you set up and configure a connector, it connects to your organization's ICE Chat secure FTP (SFTP) site once every day, converts the content of chat messages to an email message format, and then imports those items to mailboxes in Microsoft 365.

After storing ICE Chat data in user mailboxes, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to ICE Chat data. For example, you can search ICE Chat messages by using eDiscovery or associate the mailbox that contains the ICE Chat data in an eDiscovery case. Using an ICE Chat connector to import and archive data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Overview of archiving ICE Chat data

The following overview explains the process of using a connector to archive ICE chat data in Microsoft 365.

![Diagram of the ICE Chat archiving workflow showing how chat messages flow from the ICE Chat SFTP site through the connector to Microsoft 365 mailboxes.](media/icechatconnectorworkflow.png)

1. Your organization works with ICE Chat to set up an ICE Chat SFTP site. You also work with ICE Chat to configure ICE Chat to copy chat messages to your ICE Chat SFTP site.
2. Once every 24 hours, ICE Chat copies chat messages to your ICE Chat SFTP site.
3. The ICE Chat connector that you create in the [Microsoft Purview portal](purview-portal) connects to the ICE Chat SFTP site every day and transfers the chat messages from the previous 24 hours to a secure Azure Storage location in the Microsoft cloud. The connector also converts the content of a chat massage to an email message format.
4. The connector imports chat message items to the mailboxes of specific users. A new folder named **ICE Chat** is created in the user mailboxes and the chat message items are imported to that folder. The connector uses the value of the *SenderEmail* and *RecipientEmail* properties. Every chat message contains these properties, which are populated with email address of the sender and every recipient/participant of the chat message.

    In addition to automatic user mapping that uses the values of the *SenderEmail* and *RecipientEmail* property (which means that the connector imports a chat message to the sender's mailbox and the mailboxes of every recipient), you can also define custom user mapping by uploading a CSV mapping file. This mapping file contains the ICE Chat *ImId* and the corresponding Microsoft 365 mailbox address for every user in your organization. If you enable automatic user mapping and provide a custom-mapping file, for every chat item the connector first looks at the custom-mapping file. If it doesn't find a valid Microsoft 365 user account that corresponds to a user's ICE Chat ImId, the connector uses the *SenderEmail* and *RecipientEmail* properties of the chat item to import the item to the mailboxes of the chat participants. If the connector doesn't find a valid Microsoft 365 user in either the custom-mapping file or the *SenderEmail* and *RecipientEmail* properties, the item won't be imported.

## Before you begin

Some implementation steps for archiving ICE Chat data are external to Microsoft 365. You must complete these steps before you create the connector in the Microsoft Purview portal.

- ICE Chat charges customers a fee for external compliance. Your organization should contact the ICE Chat sales group to discuss and sign the ICE Chat data services agreement, which you can get at [ICE Data Services Agreement (PDF)](https://www.theice.com/publicdocs/agreements/ICE_Data_Services_Agreement.pdf). This agreement is between ICE Chat and your organization and doesn't involve Microsoft. After you set up an ICE Chat SFTP site (see Configure the ICE Chat SFTP site), ICE Chat provides the FTP credentials directly to your organization. Then you provide those credentials to Microsoft when you create the connector (see Create an ICE Chat connector).
- You must set up an ICE Chat SFTP site before creating the connector (see Create an ICE Chat connector). After working with ICE Chat to set up the SFTP site, data from ICE Chat is uploaded to the SFTP site every day. The connector you create in the Create an ICE Chat connector step connects to this SFTP site and transfers the chat data to Microsoft 365 mailboxes. SFTP also encrypts the ICE Chat data that's sent to mailboxes during the transfer process.
- To set up an ICE Chat connector, you need keys and key passphrases for Pretty Good Privacy (PGP) and Secure Shell (SSH). These keys configure the ICE Chat SFTP site and help the connector connect to the ICE Chat SFTP site to import data to Microsoft 365. The PGP key configures the encryption of data that's transferred from the ICE Chat SFTP site to Microsoft 365. The SSH key configures secure shell to enable a secure remote authentication when the connector connects to the ICE Chat SFTP site.

    When setting up a connector, you can use public keys and key passphrases provided by Microsoft or your own private keys and passphrases. Use the public keys provided by Microsoft. However, if your organization already configured an ICE Chat SFTP site by using private keys, you can create a connector by using these same private keys.
- The ICE Chat connector can import up to 200,000 items in a single day. If there are more than 200,000 items on the SFTP site, none of those items are imported to Microsoft 365.
- The admin who creates the ICE Chat connector in Step 3 (and who downloads the public keys and IP address in Step 1) must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Set up a connector by using public keys

The steps in this section show you how to set up an ICE Chat connector by using the public keys for Pretty Good Privacy (PGP) and Secure Shell (SSH).

### Step 1: Obtain PGP and SSH public keys

First, get a copy of the public keys for Pretty Good Privacy (PGP) and Secure Shell (SSH). You use these keys in Step 2 to configure the ICE Chat SFTP site to allow the connector (that you create in Step 3) to connect to the SFTP site and transfer the ICE Chat data to Microsoft 365 mailboxes. You also get an IP address during the public-key download process, which you use when configuring the ICE Chat SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **ICE Chat** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH public keys provided by Microsoft**.
7. Under step 1, select the **Download SSH key**, **Download PGP key**, and **Download IP address** links to save a copy of each file to your local computer.

    These files contain the following items that you use to configure the ICE Chat SFTP site in Step 2:

    - PGP public key: Use this key to configure the encryption of data that's transferred from the ICE Chat SFTP site to Microsoft 365.
    - SSH public key: Use this key to configure Secure SSH to enable a secure remote authentication when the connector connects to the ICE Chat SFTP site.
    - IP address: Configure the ICE Chat SFTP site to accept a connection request only from this IP address, which is used by the ICE Chat connector that you create in Step 3.
8. Select **Cancel** to close the workflow. You return to this workflow in the Create an ICE Chat connector section to create the connector.

### Step 2: Configure the ICE Chat SFTP site

Next, use the PGP and SSH public keys and the IP address that you obtained in the Obtain PGP and SSH public keys step to configure PGP encryption and SSH authentication for the ICE Chat SFTP site. This configuration lets the ICE Chat connector that you create in the Create an ICE Chat connector section connect to the ICE Chat SFTP site and transfer ICE Chat data to Microsoft 365. You need to work with ICE Chat customer support to set up your ICE Chat SFTP site.

### Step 3: Create an ICE Chat connector

In the last step, you create an ICE Chat connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the ICE Chat SFTP site and transfer chat messages to the corresponding user mailboxes in Microsoft 365.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **ICE Chat** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH public keys**.
7. Under Step 3, enter the required information in the following boxes and then select **Validate connection**.

    - **Firm code:** The ID for your organization, which you use as the username for the ICE Chat SFTP site.
    - **Password:** The password for your ICE Chat SFTP site.
    - **SFTP URL:** The URL for the ICE Chat SFTP site (for example, `sftp.theice.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for the ICE Chat SFTP site. The connector uses this port to connect to the SFTP site.
8. After the connection is successfully validated, select **Next**.
9. On the **Define user** page, specify the users to import data for.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
10. On the **Map external users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required. You can download a copy of the user-mapping CSV file on this page. You can add the user mappings to the file and then upload it.

    Note

    The custom mapping file contains the ICE Chat imid and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every chat item, the connector first looks at the custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's ICE Chat imid, the connector imports the item to the mailboxes for the users specified in the *SenderEmail* and *RecipientEmail* properties of the chat item. If the connector doesn't find a valid Microsoft 365 user by either automatic or custom user mapping, the item isn't imported.
11. Select **Next**, review your settings, and then select **Finish** to create the connector.

## Set up a connector by using private keys

The steps in this section show you how to set up an ICE Chat connector by using PGP and SSH private keys. Use this connector setup option if your organization already configured an ICE Chat SFTP site by using private keys.

### Step 1: Get an IP address to configure the ICE Chat SFTP site

If your organization uses PGP and SSH private keys to set up an ICE Chat SFTP site, get an IP address and give it to ICE Chat customer support. The ICE Chat SFTP site must accept connection requests from this IP address. The IP address you download in this step is also used by the ICE Chat connector to connect to the SFTP site and transfer ICE Chat data to Microsoft 365.

To get the IP address:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **ICE Chat** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.
7. Under step 1, select **Download IP address** to save a copy of the IP address file to your local computer.
8. Select **Cancel** to close the workflow. You return to this workflow in the Create an ICE Chat connector section to create the connector.

Work with ICE Chat customer support to configure your ICE Chat SFTP site to accept connection requests from this IP address.

### Step 2: Create an ICE Chat connector

After you configure your ICE Chat SFTP site, create an ICE Chat connector in the Microsoft Purview portal. The connector uses the information you provide to connect to the ICE Chat SFTP site and transfer email messages to the corresponding user mailboxes in Microsoft 365. To complete this step, make sure you have copies of the same private keys and key passphrases that you used to set up your ICE Chat SFTP site.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. Select **ICE Chat** from the list.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for content source** page, select **I want to use PGP and SSH private keys**.
7. Under Step 3, enter the required information in the following boxes and then select **Validate connection**.

    - **Name:** The name for the connector. It must be unique in your organization.
    - **Firm code:** The ID for your organization that is used as the username for the ICE Chat SFTP site.
    - **Password:** The password for your organization's ICE Chat SFTP site.
    - **SFTP URL:** The URL for the ICE Chat SFTP site (for example, `sftp.theice.com`). You can also use an IP address for this value.
    - **SFTP port:** The port number for the ICE Chat SFTP site. The connector uses this port to connect to the SFTP site.
    - **PGP private key:** The PGP private key for the ICE Chat SFTP site. Include the entire private key value, including the beginning and ending lines of the key block.
    - **PGP key passphrase:** The passphrase for the PGP private key.
    - **SSH private key:** The SSH private key for the ICE Chat SFTP site. Include the entire private key value, including the beginning and ending lines of the key block.
    - **SSH key passphrase:** The passphrase for the SSH private key.
8. After the connection is successfully validated, select **Next**.
9. On the **Define user** page, specify the users to import data for.

    - **All users in your organization**. Select this option to import data for all users.
    - **Only users on Litigation hold**. Select this option to import data only for users whose mailboxes are placed on Litigation hold. This option imports data to user mailboxes that have the LitigationHoldEnabled property set to True. For more information, see [Create a Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
10. On the **Map ICE Chat users to Microsoft 365 users** page, enable automatic user mapping and provide custom user mapping as required.

    Note

    The custom mapping file contains the ICE Chat imid and corresponding Microsoft 365 mailbox address for each user. If you enable automatic user mapping and provide a custom mapping, for every chat item, the connector first looks at the custom mapping file. If it doesn't find a valid Microsoft 365 user that corresponds to a user's ICE Chat imid, the connector imports the item to the mailboxes for the users specified in the *SenderEmail* and *RecipientEmail* properties of the chat item. If the connector doesn't find a valid Microsoft 365 user by either automatic or custom user mapping, the item isn't imported.
11. Select **Next**, review your settings, and then select **Finish** to create the connector.