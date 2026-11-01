---
layout: Conceptual
title: Manage Purview Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/manage-office-365-message-encryption
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
ms.date: 2026-06-22T00:00:00.0000000Z
search.appverid:
- MET150
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
description: Once you've finished setting up message encryption, learn how to customize your deployment in several ways.
ai-usage: ai-assisted
locale: en-us
document_id: 91349aa3-02bb-34e2-caff-2e9604174a4c
document_version_independent_id: 91349aa3-02bb-34e2-caff-2e9604174a4c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/manage-office-365-message-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manage-office-365-message-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/manage-office-365-message-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 09846932-60fd-03be-e761-2ed6bf873d5d
---

# Manage Purview Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Once you've finished setting up Purview Message Encryption, you can customize the configuration of your deployment in several ways. For example, you can configure whether to enable one-time pass codes, display the **Encrypt** button in Outlook on the web, and more. The tasks in this article describe how.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Manage whether Google, Yahoo, and Microsoft Account recipients can use these accounts to sign in to the encrypted message portal

When you set up the message encryption, users in your organization can send messages to recipients that are outside of your organization. If the recipient uses a *social ID* such as a Google account, Yahoo account, or Microsoft account, the recipient can sign in to the encrypted message portal with a social ID. If you want, you can choose not to allow recipients to use social IDs to sign in to the encrypted message portal.

### To manage whether recipients can use social IDs to sign in to the encrypted message portal

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-OMEConfiguration cmdlet with the SocialIdSignIn parameter as follows:

    ```powershell
    Set-OMEConfiguration -Identity <"OMEConfigurationIdParameter"> -SocialIdSignIn <$true|$false>
    ```

    For example, to disable social IDs:

    ```powershell
    Set-OMEConfiguration -Identity "OME Configuration" -SocialIdSignIn $false
    ```

    To enable social IDs:

    ```powershell
    Set-OMEConfiguration -Identity "OME Configuration" -SocialIdSignIn $true
    ```

## Manage the use of one-time pass codes for the encrypted message portal

If the recipient of a message encrypted by message encryption doesn't use Outlook, regardless of the account used by the recipient, the recipient receives a limited-time web-view link that lets them read the message. This link includes a one-time pass code. As an administrator, you can decide if recipients can use one-time pass codes to sign in to the encrypted message portal.

### To manage whether OME generates one-time pass codes

Perform the following steps to manage whether OME generates one-time pass codes.

1. Use a work or school account that has sufficient administrator permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-OMEConfiguration cmdlet with the OTPEnabled parameter:

    ```powershell
    Set-OMEConfiguration -Identity <"OMEConfigurationIdParameter"> -OTPEnabled <$true|$false>
    ```

    For example, to disable one-time pass codes:

    ```powershell
    Set-OMEConfiguration -Identity "OME Configuration" -OTPEnabled $false
    ```

    To enable one-time pass codes:

    ```powershell
    Set-OMEConfiguration -Identity "OME Configuration" -OTPEnabled $true
    ```

## Manage the display of the Encrypt button in Outlook on the web

As an administrator, you can manage whether to display the **Encrypt** button in Outlook on the web to end users.

### To manage whether the Encrypt button appears in Outlook on the web

Perform the following steps to manage whether the **Encrypt** button appears in Outlook on the web.

1. Use a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-IRMConfiguration cmdlet with the -SimplifiedClientAccessEnabled parameter:

    ```powershell
    Set-IRMConfiguration -SimplifiedClientAccessEnabled <$true|$false>
    ```

    For example, to disable the **Encrypt** button:

    ```powershell
    Set-IRMConfiguration -SimplifiedClientAccessEnabled $false
    ```

    To enable the **Encrypt** button:

    ```powershell
    Set-IRMConfiguration -SimplifiedClientAccessEnabled $true
    ```

## Enable service-side decryption of email messages for iOS mail app users

The iOS mail app can't decrypt messages protected with message encryption. As a Microsoft 365 administrator, you can apply service-side decryption for messages delivered to the iOS mail app. When you choose to do use service-side decryption, the service sends a decrypted copy of the message to the iOS device. The client device stores a decrypted copy of the message. The message also retains information about usage rights even though the iOS mail app doesn't apply client-side usage rights to the user. The user can copy or print the message even if they didn't originally have the rights to do so. However, if the user attempts to complete an action that requires the Microsoft 365 mail server, such as forwarding the message, the server won't permit the action if the user didn't originally have the usage right to do so. However, end users can work around "Do Not Forward" usage restriction by forwarding the message from a different account within the iOS mail app. Regardless of whether you set up service-side decryption of mail, attachments to encrypted and rights protected mail can't be viewed in the iOS mail app.

If you choose not to allow decrypted messages to be sent to iOS mail app users, users receive a message that states that they don't have the rights to view the message. By default, service-side decryption of email messages isn't enabled.

For more information, and for a view of the client experience, see [View encrypted messages on your iPhone or iPad](https://support.microsoft.com/en-us/office/view-protected-messages-on-your-iphone-or-ipad-4d631321-0d26-4bcc-a483-d294dd0b1caf).

### To manage whether iOS mail app users can view messages protected by message encryption

Perform the following steps to manage whether iOS mail app users can view messages protected by message encryption.

1. Use a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-ActiveSyncOrganizations cmdlet with the AllowRMSSupportForUnenlightenedApps parameter:

    ```powershell
    Set-ActiveSyncOrganizationSettings -AllowRMSSupportForUnenlightenedApps <$true|$false>
    ```

    For example, to configure the service to decrypt messages before they're sent to unenlightened apps like the iOS mail app:

    ```powershell
    Set-ActiveSyncOrganizationSettings -AllowRMSSupportForUnenlightenedApps $true
    ```

    Or, to configure the service not to send decrypted messages to unenlightened apps:

    ```powershell
    Set-ActiveSyncOrganizationSettings -AllowRMSSupportForUnenlightenedApps $false
    ```

Note

Individual mailbox policies (OWA/ActiveSync) override the AllowRMSSupportForUnenlightenedApps setting (i.e. if -IRMEnabled is set to False within the respective OWA Mailbox policy or ActiveSync Mailbox policy, then the AllowRMSSupportForUnenlightenedApps setting doesn't apply).

## Enable service-side decryption of email attachments for web browser mail clients

Normally, when you use message encryption, attachments are automatically encrypted. As an administrator, you can apply service-side decryption for email attachments that users download from a web browser.

When you use service-side decryption, the service sends a decrypted copy of the file to the device. The message is still encrypted. The email attachment also keeps information about usage rights even though the browser doesn't apply client-side usage rights to the user. The user can copy or print the email attachment even if they didn't originally have the rights to do so. However, if the user tries to complete an action that requires the Microsoft 365 mail server, such as forwarding the attachment, the server won't permit the action if the user didn't originally have the usage right to do so.

Regardless of whether you set up service-side decryption of attachments, users can't view any attachments to encrypted and rights protected mail in the iOS mail app.

If you choose not to allow decrypted email attachments, which is the default, users receive a message that states that they don't have the rights to view the attachment.

For more information about how Microsoft 365 implements encryption for emails and email attachments with the Encrypt-Only option, see [Encrypt-Only option for emails.](rights-management-usage-rights#encrypt-only-option-for-emails)

### To manage whether email attachments are decrypted on download from a web browser

Perform the following steps to manage whether email attachments are decrypted when downloaded from a web browser.

1. Use a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the Set-IRMConfiguration cmdlet with the DecryptAttachmentForEncryptOnly parameter:

    ```powershell
    Set-IRMConfiguration -DecryptAttachmentForEncryptOnly <$true|$false>
    ```

    For example, to configure the service to decrypt email attachments when a user downloads them from a web browser:

    ```powershell
    Set-IRMConfiguration -DecryptAttachmentForEncryptOnly $true
    ```

    To configure the service to leave encrypted email attachments as they are upon download:

    ```powershell
    Set-IRMConfiguration -DecryptAttachmentForEncryptOnly $false
    ```

## Ensure all external recipients use the encrypted message portal to read encrypted mail

You can use custom branding templates to force recipients to receive a wrapper mail that directs them to read encrypted email in the encrypted message portal instead of using Outlook or Outlook on the web. You might want to do force this experience if you use want greater control over how recipients use the mail they receive. For example, if external recipients view email in the web portal, you can set an expiration date for the email, and you can revoke the email. These features are only supported through the encrypted message portal. You can use the Encrypt option and the Do Not Forward option when creating the mail flow rules.

### Use a custom template to force all external recipients to use the encrypted message portal and for encrypted email

Perform the following steps to create a custom template that forces all external recipients to use the encrypted message portal for encrypted email.

1. Use a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, and connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the New-TransportRule cmdlet:

    ```powershell
    New-TransportRule -name "<mail flow rule name>" -FromScope "InOrganization" -ApplyRightsProtectionTemplate "<option name>" -ApplyRightsProtectionCustomizationTemplate "<template name>"
    ```

    where:

    - `mail flow rule name` is the name you want to use for the new mail flow rule.
    - `option name` is either `Encrypt` or `Do Not Forward`.
    - `template name` is the name you gave the custom branding template, for example `OME Configuration`.

    To encrypt all external email with the "OME Configuration" template and apply the Encrypt-Only option:

    ```powershell
    New-TransportRule -name "<All outgoing mail>" -FromScope "InOrganization" -ApplyRightsProtectionTemplate "Encrypt" -ApplyRightsProtectionCustomizationTemplate "OME Configuration"
    ```

    To encrypt all external email with the "OME Configuration" template and apply the Do Not Forward option:

    ```powershell
    New-TransportRule -name "<All outgoing mail>" -FromScope "InOrganization" -ApplyRightsProtectionTemplate "Do Not Forward" -ApplyRightsProtectionCustomizationTemplate "OME Configuration"
    ```

## Customize the appearance of email messages and the encrypted message portal

For detailed information about how you can customize Microsoft Purview Message Encryption for your organization, see [Add your organization's brand to your encrypted messages](add-your-organization-brand-to-encrypted-messages). To track and revoke encrypted messages, you must add your custom branding to the encrypted message portal.

## Disable Microsoft Purview Message Encryption

We hope it doesn't come to it, but if you need to, disabling Microsoft Purview Message Encryption is straightforward. First, remove any mail flow rules you've created that use Microsoft Purview Message Encryption. For information about removing mail flow rules, see [Manage mail flow rules](/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules). Then, complete these steps in Exchange Online PowerShell.

### To disable Microsoft Purview Message Encryption

Perform the following steps to disable Microsoft Purview Message Encryption.

1. Using a work or school account that has sufficient permissions in your organization, such as Compliance Administrator, connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. If you enabled the **Encrypt** button in Outlook on the web, disable it by running the Set-IRMConfiguration cmdlet with the SimplifiedClientAccessEnabled parameter. Otherwise, skip this step.

    ```powershell
    Set-IRMConfiguration -SimplifiedClientAccessEnabled $false
    ```
3. Disable the Microsoft Purview Message Encryption by running the Set-IRMConfiguration cmdlet with the AzureRMSLicensingEnabled parameter set to false:

    ```powershell
    Set-IRMConfiguration -AzureRMSLicensingEnabled $false
    ```