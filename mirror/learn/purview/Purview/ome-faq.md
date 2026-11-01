---
layout: FAQ
title: Message Encryption FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome-faq
summary: >
  <p>Have a question about how the new message protection capabilities work? Check for an answer here. Also, look at [Frequently asked questions]](azure-rights-management-learn-about.md#frequently-asked-questions) for answers to questions about the Azure Rights Management encryption service from Microsoft Purview Information Protection.</p>
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-14T00:00:00.0000000Z
audience: Admin
ms.topic: faq
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
description: Have a question about how Microsoft Purview Message Encryption works? Check for an answer here.
ms.custom: seo-marvel-apr2020
ms.collection:
- purview-compliance
locale: en-us
document_id: 6886088f-d9b1-d542-78cf-eaf8644d77b1
document_version_independent_id: 6886088f-d9b1-d542-78cf-eaf8644d77b1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
platformId: c76b2776-bc8a-fabb-d18d-f5dd2cae8491
---

# Message Encryption FAQ | Microsoft Learn

Have a question about how the new message protection capabilities work? Check for an answer here. Also, look at [Frequently asked questions]](azure-rights-management-learn-about.md#frequently-asked-questions) for answers to questions about the Azure Rights Management encryption service from Microsoft Purview Information Protection.

## What is Microsoft Purview Message Encryption?

Microsoft Purview Message Encryption combines email encryption and rights management capabilities. Rights management capabilities are powered by Microsoft Purview Information Protection.

## Who can use Microsoft Purview Message Encryption?

You can use Microsoft Purview Message Encryption under the following conditions:

- If you haven't set up Office 365 Message Encryption (OME) or Information Rights Management (IRM) for Exchange.
- If you set up OME and IRM, you can use these steps if you're also using the Azure Rights Management service from Microsoft Purview Information Protection.
- If you're using Exchange with Active Directory Rights Management service (AD RMS), you can't enable these new capabilities right away. Instead, you need to [migrate AD RMS to Azure Information Protection](/en-us/information-protection/plan-design/migrate-from-ad-rms-to-azure-rms) first. When you finish the migration, you can successfully set up Microsoft Purview Message Encryption.

    If you choose to continue to use on-premises AD RMS with Exchange instead of migrating to the Azure Rights Management service, you can't use Microsoft Purview Message Encryption.

## What subscriptions do I need to use Microsoft Purview Message Encryption?

To use Microsoft Purview Message Encryption, you need one of the following plans:

- Microsoft Purview Message Encryption is offered as part of Office 365 Enterprise E3 and E5, Microsoft 365 Enterprise E3 and E5, Microsoft 365 Business Premium, Office 365 A1, A3, and A5, and Office 365 Government G3 and G5. You don't need extra licenses to receive the new protection capabilities powered by Microsoft Purview Information Protection.
- You can also add Azure Information Protection Plan 1 to the following plans to receive Microsoft Purview Message Encryption: Exchange Plan 1, Exchange Plan 2, Office 365 F3, Microsoft 365 Business Basic, Microsoft 365 Business Standard, or Office 365 Enterprise E1.
- Each user benefiting from Microsoft Purview Message Encryption needs a license to use message encryption.
- For the full list, see the [Exchange service descriptions](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-service-description) for Microsoft Purview Message Encryption.

## Can I use Exchange with bring your own key (BYOK) for the Azure Rights Management service?

Yes! Microsoft recommends that you complete the steps to set up BYOK before you set up Microsoft Purview Message Encryption.

For more information about BYOK, see [Planning and implementing your Azure Information Protection tenant key](/en-us/information-protection/plan-design/plan-implement-tenant-key).

## Do Microsoft Purview Message Encryption and BYOK with the Azure Rights Management service change Microsoft's approach to non-Microsoft data requests such as subpoenas?

No. Microsoft Purview Message Encryption and the option to provide and control your own encryption keys, called BYOK for the Azure Rights Management service, weren't designed to respond to law enforcement subpoenas. OME, with BYOK for the Azure Rights Managment service, was designed for compliance-focused organizations. Microsoft takes requests for customer data seriously. As a cloud service provider, we always advocate for the privacy of your data. In the event we get a subpoena, we always attempt to redirect the request directly to you to obtain the information. (Read Brad Smith's blog: [Protecting customer data from government snooping](https://blogs.microsoft.com/blog/2013/12/04/protecting-customer-data-from-government-snooping/)). We periodically publish detailed information of the request we receive. For more information regarding non-Microsoft data requests, see [Responding to government and law enforcement requests to access customer data](https://www.microsoft.com/trustcenter/privacy/govt-requests-for-data) on the Microsoft Trust Center. Also, see "Disclosure of Customer Data" in the [Online Services Terms (OST)](https://www.microsoft.com/licensing/docs/view/licensing-use-rights).

## How is this feature related to legacy Office 365 Message Encryption (OME) and Information Rights Management (IRM) features?

Microsoft Purview Message Encryption is an evolution of the existing IRM and legacy OME solutions. The following table provides more details.

**Comparison of legacy OME, IRM, and Microsoft Purview Message Encryption**

| Capability | Previous versions of OME | IRM | Microsoft Purview Message Encryption |
| --- | --- | --- | --- |
| **Sending an encrypted email** | Only through Exchange mail flow rules | End-user initiated from Outlook for Windows, Outlook for Mac, or Outlook on the web; or through Exchange mail flow rules | End-user initiated from Outlook for Windows, Outlook for Mac, or Outlook on the web; or through mail flow rules |
| **Rights management** | - | Do Not Forward option and custom templates | Do Not Forward option, encrypt-only option, default and custom templates |
| **Supported recipient type** | External recipients only | Internal recipients only | Internal and external recipients |
| **Experience for recipient** | External recipients received an HTML message that they downloaded and opened in a browser or downloaded mobile app. | Internal recipients only received encrypted email in Outlook for Windows, Outlook for Mac, and Outlook on the web. | Internal and external recipients receive email in Outlook for Windows, Outlook for Mac, Outlook on the web, Outlook for Android, and Outlook for iOS, or through a web portal, regardless of whether they are in the same organization or in any organization. The encrypted message portal requires no separate download. |
| **Bring Your Own Key support** | Not available | Not available | BYOK supported |

## How do I enable Microsoft Purview Message Encryption for my organization?

See [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities).

## Is Office 365 Message Encryption deprecated?

Office 365 Message Encryption (OME) was deprecated on July 1, 2023. It's being automatically replaced with Microsoft Purview Message Encryption. If you have an active sender mailbox, you can still view mail from OME.

## My organization uses Active Directory Rights Management, can I use this functionality?

No. If you're using Exchange Online with Active Directory Rights Management service (AD RMS), you can't enable these new capabilities right away. Instead, you need to [migrate AD RMS to Azure Information Protection](/en-us/information-protection/plan-design/migrate-from-ad-rms-to-azure-rms) first.

## My organization has an Exchange Hybrid deployment. Can I use this feature?

On-premises users can send encrypted mail using Exchange Online mail flow rules. You need to route email through Exchange. For more information, see [Part 2: Configure mail to flow from your email server to Microsoft 365](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail#part-2-configure-mail-to-flow-from-your-email-server-to-office-365).

## What email client do I need to use to create an encrypted message? What applications are supported for sending protected messages?

You can create protected messages from Outlook 2016, Outlook 2013 for Windows and Mac, and from Outlook on the web. For more information on sending encrypted messages, see [Send, view, and reply to encrypted messages in Outlook for PC](https://support.microsoft.com/office/send-view-and-reply-to-encrypted-messages-in-outlook-for-pc-eaa43495-9bbb-4fca-922a-df90dee51980?ui=en-us&amp;rs=en-us&amp;ad=us).

## What email clients are supported to read and reply to protected emails?

Microsoft 365 users can read and respond from Outlook for Windows and Mac (2013 and 2016), Outlook on the web, and Outlook mobile (Android and iOS). You can also use the iOS native mail client if your organization allows it. If you aren't a Microsoft 365 user, you can read and reply to encrypted messages on the web through your web browser.

## What email clients support the encrypt-only protected emails?

Microsoft 365 users can use Outlook for PC versions 2019 and Microsoft 365 to create mail protected with the encrypt-only policy. Messages that have the encrypt-only policy applied can be read directly in Outlook on the web, in Outlook for iOS and Android, and Outlook for PC versions 2019 and Microsoft 365.

## Is there a size limit for messages you can send with OME?

Yes. The maximum message size you can send with Microsoft Purview Message Encryption, including attachments, is 25 MB. For more information, see [Message limits](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#message-limits-1).

## Is there a limit to the number of recipients you can send OME-encrypted messages to?

Yes. In some cases that have [connectors](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow) configured such as an Exchange Hybrid deployment, when you include recipients on the **BCC** line, the BCC recipients are removed before mail gets encrypted. Best practice is to move to an Exchange Online, or put all recipients in the **To:** or **CC** fields.

## What type of messages does the encrypted message portal support?

The encrypted message portal only supports mail. The portal doesn't support other message types such as calendar or voice mail.

## What file types are supported as attachments in protected emails? Do attachments inherit the protection policies and permissions associated with protected emails? What about PDF?

You can attach any file type to a protected mail. Protection policies are applied only to a subset of the file formats mentioned in [Supported file types](information-protection-client#supported-file-types). By default, Microsoft Purview Message Encryption encrypts the following Office files extensions:

- docx
- docm
- dotx
- dotm
- pptx
- pptm
- potx
- potm
- ppsx
- ppsm
- thmx
- xlsx
- xlsm
- xlsb
- xltx
- xltm
- xlam
- xps

Microsoft Purview Message Encryption doesn't support the 97-2003 versions of the following Office programs: Word (.doc), Excel (.xls), and PowerPoint (.ppt).

If enabled in Exchange Online, PDF encryption allows you to protect sensitive PDF documents attached to emails. When you send an email, the Office 365 service encrypts PDF file attachments for the newest versions of Outlook, including:

- Outlook (new) Desktop
- Outlook on the web
- Outlook for Mac
- Outlook for iOS
- Outlook for Android

To enable encryption for PDF attachments, using a work or school account that has the Information Rights Management role at a minimum in your tenant, run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```PowerShell
   Set-IRMConfiguration -EnablePdfEncryption $true
```

Protection is inherited from mail to unencrypted attachments only. If a file format is supported, such as a Word, Excel, or PowerPoint file, the file is always protected, even after the recipient downloads the attachment.

For example, say an attachment is protected by Do Not Forward. The original recipient downloads the file, creates a message to a new recipient, and attaches the file. When the new recipient receives the file, they can't open it.

## Can I use mail flow rules to encrypt or decrypt meeting invites and their responses?

No, you must use sensitivity labels to apply or remove encryption for meeting invites and their responses. For more information, see [Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings).

## Are SharePoint or OneDrive attachments supported?

Not yet. SharePoint or OneDrive attachments aren't supported. You can encrypt a mail message, but not the cloud attachments.

## What email clients support preview of encrypted attachments in protected emails?

When attachments are protected with a protected mail, you can preview documents directly using Outlook clients. Outlook supports preview of Office documents (docx, xlsx, pptx, doc, xls, ppt). Outlook on the web supports preview of Office documents (docx, xlsx, pptx) and PDF.

## What email clients support revocation of protected emails?

Outlook on the web supports revocation of protected mail. See [How to revoke an encrypted message that you sent](revoke-ome-encrypted-mail#how-to-revoke-an-encrypted-message-that-you-sent) for details.

## Does the encrypted message portal support preview of encrypted attachments in protected emails?

The encrypted message portal supports preview of any encrypted attachment copies added to the encrypted mail. The support file types include Word, Excel, PowerPoint, and PDF files.

## Can I automatically encrypt messages by setting up policies?

Yes. Use mail flow rules in Exchange Online to automatically encrypt a message based on certain conditions. For example, you can create policies that are based on recipient ID, recipient domain, or on the content in the body or subject of the message. See [Define mail flow rules to encrypt email messages in Office 365](define-mail-flow-rules-to-encrypt-email).

## Can I automatically remove encryption on incoming and outgoing mail?

Admins can set up a mail flow rule to remove encryption for outgoing mail. You can only set up a rule to remove encryption for incoming mail that originates from your Exchange Online organization.

## Can I automatically remove encryption on journal mail?

For an Exchange Online mailbox, admins must enable journal decryption and set up an Exchange Online journaling rule to generate a decrypted copy of the mail into the journaling mailbox. The journaling rule takes any mail or attachment that has encryption and send the original plus a decrypted copy into the journaling mailbox. You can only set up a journaling rule that can decrypt mail or attachments when the encrypted item originates from your organization. To enable Exchange Online journaling:

```PowerShell
Set-IRMConfiguration -JournalReportDecryptionEnabled $true
```

## Can I automatically encrypt messages by setting up policies in Data Loss Prevention (DLP) through the Microsoft Purview portal?

Yes! You can set up mail flow rules in Exchange Online or by using DLP in the Microsoft Purview portal.

## Can I customize encrypted messages with my company branding?

Yes, for mail sent from an Exchange Online mailbox in your organization! For information on customizing email messages and the encrypted message portal, see [Add your organization's brand to your encrypted messages](add-your-organization-brand-to-encrypted-messages).

## On what types of recipients do the encrypted message portal activity logs work?

The encrypted message portal activity logs only capture events for external recipients by accessing the encrypted message portals. Any activities in email clients triggered by external recipients aren't recorded. For internal recipients, see the *MailItemsAccessed* mailbox-auditing action in [Purview Audit (Premium) - Mail items accessed logs](audit-log-investigate-accounts).

## Are there any reporting capabilities or insights for encrypted emails?

There's an Encryption report in the Microsoft Purview portal. See [Microsoft Purview Reports overview](/en-us/purview/purview-reports).

## Can I use message encryption with compliance features such as eDiscovery?

Yes, most messages protected by Microsoft Purview Message Encryption are discoverable. Microsoft Purview Message Encryption protected mail that you receive from another Microsoft 365 organization that has custom branding applied through a mail flow rule is undiscoverable by your eDiscovery service. In other words, if the mail isn't accessible through the user's mailbox, but rather, surfaced only through a link to the encrypted message portal, the mail isn't searchable. See [eDiscovery activities that support encrypted items](ediscovery-decryption#ediscovery-activities-that-support-encrypted-items) for details.

## Can I send as a shared mailbox and encrypt emails?

When an email message matches an encryption mail flow rule, Exchange encrypts the message sending it.

## Can I open encrypted messages sent to a shared mailbox?

Yes! You can open encrypted messages for a shared mailbox. When the mail is sent from the same organization, you can open the mail when you're signed in to a supported Outlook client. If the mail is sent from an external organization, you need to use Outlook on the web.

- Users can open protected mails in a shared mailbox where the shared mailbox received a protected mail as part of a distribution group.
- Users can view attachments that inherit protection from email when they use Outlook for Windows, Outlook for Mac, Outlook for Android, Outlook for iOS, and Outlook on the web.

The following table lists the supported clients for shared mailboxes.

| Platform | Read mail | View email attachments |
| --- | --- | --- |
| Outlook on the web | Yes | Yes |
| Outlook for Windows | Yes | Yes\* |
| Outlook for Mac | Yes | Yes |
| Outlook for Android | Yes | Yes\* |
| Outlook for iOS | Yes | Yes\* |

Note

Android and iOS use the Office mobile app to display encrypted attachments, and don't display attachments directly in Outlook mobile. Outlook for Windows can display encrypted attachments when user is directly assigned to a shared mailbox. (See below on user assignment.)

There are currently two known limitations:

- You can't open attachments to emails that you receive on mobile devices by using Outlook mobile.
- There are two ways to allow a user to view the encrypted mail directly in Outlook for Windows:

    1. Directly assign a user to the shared mailbox, with full access permissions and automapping enabled. For Outlook 64-bit, users don't need to be directly assigned to the mailbox. Automapping is enabled by default for Exchange.
    2. Assign a mail-enabled security group to a shared mailbox. This method requires Outlook version 2402 and only supports mail generated after June 2024.

**To assign a user to a shared mailbox**

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell?v=exchg.150).
2. Run the `Add-MailboxPermission` cmdlet with the `Automapping` parameter. This example gives Ayla full access permission to a support mailbox.

    ```PowerShell
    Add-MailboxPermission -Identity support@contoso.onmicrosoft.com -User ayla@contoso.com -AccessRights FullAccess -AutoMapping $true
    ```

**To assign a mail enabled security group to the shared mailbox**

To use this method, you must encrypt mail with the **Do Not Forward** or **Encrypt-only** protection options. Only mail initiated by the shared mailbox or mail sent within an organization can be opened.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell?v=exchg.150).
2. Run the `Add-MailboxPermission` cmdlet to assign the security group. The following example gives the Contoso front desk security group full access permission to a support mailbox.

    ```PowerShell
    Add-MailboxPermission -Identity support@contoso.onmicrosoft.com -User frontdesk@contoso.com -AccessRights FullAccess
    ```

## Is delegated access supported with opening encrypted messages? Even if a delegate has full access to another user's mailbox?

When delegates are given full access permission to a user's mailbox, delegated access of encrypted mail is supported in Outlook on the web, Outlook for Mac, Outlook for iOS, and Outlook for Android. Outlook for Windows doesn't support delegated access.

## How long do I have access to the mail in the encrypted message portal?

You can sign in to the encrypted message portal to retrieve mail as long as the sender's organization is active and the mail isn't configured to expire.

## What do I do if I don't receive the one-time pass code after I requested it?

First, check the junk or spam folder in your email client. DKIM and DMARC settings for your organization might cause these emails to end up filtered as spam.

Next, check quarantine in the Microsoft Purview portal. Often, messages containing a one-time pass code, especially the first ones your organization receives, end up in quarantine.