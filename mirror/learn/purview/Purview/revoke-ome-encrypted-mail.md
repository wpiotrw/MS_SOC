---
layout: Conceptual
title: Revoke email encrypted by Advanced Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/revoke-ome-encrypted-mail
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.date: 2026-06-26T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: As an administrator and as a message sender, you can revoke certain emails that were encrypted with Microsoft Purview Advanced Message Encryption.
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 9a1ee0c9-ed28-cb9d-3b74-583ca0dee4a9
document_version_independent_id: 9a1ee0c9-ed28-cb9d-3b74-583ca0dee4a9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/revoke-ome-encrypted-mail.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: revoke-ome-encrypted-mail
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/revoke-ome-encrypted-mail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 40f6d439-293b-c5b5-8e5c-9ce48883a140
---

# Revoke email encrypted by Advanced Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

This article is part of a larger series of articles about [Microsoft Purview Message Encryption](ome).

If a message was encrypted using Microsoft Purview Advanced Message Encryption, and you are a Microsoft 365 admin or you are the sender of the message, you can revoke the message under certain conditions. Admins revoke messages using PowerShell. As a sender, you revoke a message that you sent directly from Outlook on the web. This article describes the circumstances under which revocation is possible and how to do it.

Note

To guarantee that the ability to track and revoke encrypted messages is available, you must add a custom branding template. See [Add your organization's brand to your encrypted messages](add-your-organization-brand-to-encrypted-messages)

## Encrypted emails that you can revoke

Admins and message senders can revoke encrypted emails if the recipient received a link-based, branded encrypted email. If the recipient received a native inline experience in a supported Outlook client, then you can't revoke the message.

Whether a recipient receives a link-based experience or an inline experience depends on the recipient identity type: Microsoft 365 and Microsoft account recipients (for example, outlook.com users) get an inline experience in supported Outlook clients. All other recipient types, such as Gmail and Yahoo recipients, get a link-based experience.

Admins and message senders can revoke messages that are encrypted using encryption applied directly from Outlook on the web. For example, messages encrypted with the Encrypt Only option.

![Screenshot showing Encrypt Only option in Outlook on the web.](media/adhocencryptionrevoke.png)

## Recipient experience for revoked encrypted emails

Once an email has been revoked, the recipient receives an error when they access the encrypted email through the encryption portal: "The message has been revoked by the sender".

![Screenshot of the encryption portal showing the error message that the sender has revoked the encrypted email.](media/revoked-encrypted-email.png)

## How to revoke an encrypted message that you sent

You can revoke a mail that you sent to a single recipient that uses a social account such as gmail.com or yahoo.com. In other words, you can revoke an email sent to a single recipient that received the link-based experience.

You cannot revoke a mail that you sent to a recipient that uses a work or school account from Microsoft 365 or a user that uses a Microsoft account, for example, an outlook.com account.

To revoke an encrypted message that you sent, complete these steps

1. In Outlook on the web, in your **Sent** folder, browse to the message you want to revoke.

    If the mail is revocable, you'll see the "Remove external access" link at the top of the message.

    ![Screenshot showing encrypted mail that you want to revoke in Outlook on the web.](media/infoprotect-email-encryption/adhocencryptionrevokesentmsg.png)
2. Click **Remove external access** to revoke the message.

    The message shows that its status is revoked.

    ![Screenshot showing revoked encrypted message in Outlook on the web.](media/adhocencryptionrevokedmsg.png)

## How to revoke an encrypted message as an administrator

Microsoft 365 administrators follow these general steps to revoke an eligible encrypted email:

- Get the Message ID of the email.
- Verify that you can revoke the message.
- Revoke the mail.

### Step 1: Obtain the Message ID of the email

Before you can revoke an encrypted mail, gather the Message ID of the mail. The MessageId is usually of the format:

`<xxxxxxxxxxxxxxxxxxxxxxx@xxxxxx.xxxx.prod.outlook.com>`

There are multiple ways to find the Message ID of the email that you want to revoke. The following procedures describe two options, but you can use any method that provides the ID.

#### To identify the Message ID of the email you want to revoke by using Message Trace in the Microsoft Purview portal

Use Message Trace in the Microsoft Purview portal to find the Message ID for the encrypted email.

1. Search for the email by sender or recipient using [New Message Trace in Microsoft Purview portal](https://blogs.technet.microsoft.com/exchange/2018/05/02/new-message-trace-in-office-365-security-compliance-center/).
2. Once you've located the email, select it to bring up the **Message trace details** pane. Expand **More Information** to locate the Message ID.

#### To identify the Message ID of the email you want to revoke by using Message Encryption reports in the Microsoft Purview portal

You can also use Message Encryption reports in the Microsoft Purview portal to locate the Message ID.

1. In the Microsoft Purview portal, navigate to the **Message encryption report**. For information on this report, see [View email security reports in the Security & Compliance Center](/en-us/microsoft-365/security/office-365-security/reports-email-security).
2. Choose the **View details** table and identify the message that you want to revoke.
3. Double-click the message to view details that include the Message ID.

### Step 2: Verify that the mail is revocable

To verify whether you can revoke a message, check whether the Revocation Status field is visible in the Encryption report, in the **Details** table in the Microsoft Purview portal.

To verify whether you can revoke a particular email message by using Windows PowerShell, complete these steps.

1. Using a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, start a Windows PowerShell session and connect to Exchange Online. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Get-OMEMessageStatus cmdlet as follows:

    ```powershell
    Get-OMEMessageStatus -MessageId "<message id>" | ft -a  Subject, IsRevocable
    ```

    This command returns the subject of the message and whether the message is revocable. For example,

    ```console
    Subject        IsRevocable
    -------        -----------
    "Test message" True
    ```

### Step 3: Revoke the mail

Once you know the Message ID of the email you want to revoke, and you have verified that the message is revocable, you can revoke the email using the Microsoft Purview portal or Windows PowerShell.

To revoke the message using the Microsoft Purview portal

1. Using a work or school account that has compliance administrator permissions in your organization, connect to the Microsoft Purview portal.
2. In the **Encryption report**, in the **Details** table for the message, choose **Revoke message**.

To revoke an email by using Windows PowerShell, use the Set-OMEMessageRevocation cmdlet.

1. Using a work or school account that has compliance administrator, or Exchange administrator permissions in your organization, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-OMEMessageRevocation cmdlet as follows:

    ```powershell
    Set-OMEMessageRevocation -Revoke $true -MessageId "<messageId>"
    ```
3. To check whether the email was revoked, run the Get-OMEMessageStatus cmdlet as follows:

    ```powershell
    Get-OMEMessageStatus -MessageId "<messageId>" | ft -a  Subject, Revoked
    ```

    If revocation was successful, the cmdlet returns the following result:

    ```console
    Revoked: True
    ```

## Advanced Message Encryption references and related guidance

- [Microsoft Purview Advanced Message Encryption](ome-advanced-message-encryption)
- [Microsoft Purview Advanced Message Encryption - email expiration](ome-advanced-expiration)
- [Message policy and compliance service description](/en-us/office365/servicedescriptions/exchange-online-service-description/message-policy-and-compliance)