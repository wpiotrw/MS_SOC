---
layout: Conceptual
title: Define mail flow rules to encrypt email messages | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/define-mail-flow-rules-to-encrypt-email
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
- MOE150
ms.assetid: 9b7daf19-d5f2-415b-bc43-a0f5f4a585e8
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1014, admindeeplinkMAC, admindeeplinkEXCHANGE, sfi-ga-nochange
description: Admins can learn to create mail flow rules (transport rules) to encrypt and decrypt messages using Microsoft Purview Message Encryption.
ai-usage: ai-assisted
locale: en-us
document_id: 1f48c14f-5c2c-0be5-b40d-95f0b2281b97
document_version_independent_id: 1f48c14f-5c2c-0be5-b40d-95f0b2281b97
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/define-mail-flow-rules-to-encrypt-email.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: define-mail-flow-rules-to-encrypt-email
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/define-mail-flow-rules-to-encrypt-email.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: f92756fe-5436-dc94-4f0d-0cd95fc210b1
---

# Define mail flow rules to encrypt email messages | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

As an administrator that manages Exchange Online, you can create mail flow rules (also known as transport rules) to help protect email messages you send and receive. You can set up rules to encrypt any outgoing email messages and remove encryption from encrypted messages coming from inside your organization or from replies to encrypted messages sent from your organization. You can use the [Exchange admin center (EAC)](https://go.microsoft.com/fwlink/p/?linkid=2059104) or Exchange Online PowerShell to create these rules. In addition to overall encryption rules, you can also choose to enable or disable individual message encryption options for end users.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

You can't encrypt inbound mail from senders outside of your Exchange Online organization. If a mail flow rule is set up to encrypt mail from outside the organization, the inbound mail will be delivered without encryption.

If you recently migrated from Active Directory RMS to the Azure Rights Management service, you'll need to review your existing mail flow rules to ensure that they continue to work in your new environment. Also, to use Microsoft Purview Message Encryption with the Azure Rights Management service, you need to update your existing mail flow rules. Otherwise, your users will continue to receive encrypted mail that uses the previous HTML attachment format instead of the new, seamless experience. If you haven't set up message encryption yet, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities) for information.

For information about the components that make up mail flow rules and how mail flow rules work, see [Mail flow rules (transport rules) in Exchange Online](/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules).

Important

For hybrid Exchange environments, on-premises users can send and receive encrypted mail using message encryption only if email is routed through Exchange Online. To configure message encryption in a hybrid Exchange environment, you need to first [configure hybrid using the Hybrid Configuration wizard](/en-us/Exchange/exchange-hybrid) and then [configure mail to flow from Office 365 to your email server](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail#part-1-configure-mail-to-flow-from-office-365-to-your-on-premises-email-server) and [configure mail to flow from your email server to Office 365](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail#part-2-configure-mail-to-flow-from-your-email-server-to-office-365). Once you've configured mail to flow through Office 365, then you can configure mail flow rules for message encryption by using the procedures in this article.

## Create mail flow rules to encrypt email messages with Microsoft Purview Message Encryption

You can define mail flow rules for triggering message encryption with by using the EAC.

### Use the EAC to create a rule for encrypting email messages with Microsoft Purview Message Encryption

Perform the following steps to create a mail flow rule that encrypts email messages using Microsoft Purview Message Encryption.

1. In a web browser, using a work or school account that has been granted sufficient permissions, such as Compliance Administrator, [sign in to Microsoft 365](https://support.microsoft.com/article/b9582171-fd1f-4284-9846-bdd72bb28426#ID0EAABAAA=Web_browser).
2. Choose the **Admin** tile.
3. In the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), choose **Admin centers** &gt; **Exchange**.
4. In the EAC, go to **Mail flow** &gt; **Rules** and select **New**![New icon for creating a new mail flow rule in Exchange admin center.](media/457cd93f-22c2-4571-9f83-1b129bcfb58e.gif) &gt; **Create a new rule**. For more information about using the EAC, see [Exchange admin center in Exchange Online](/en-us/exchange/exchange-admin-center).
5. In **Name**, type a name for the rule, such as Encrypt mail for DrToniRamos@hotmail.com.
6. In **Apply this rule if**, select where the mail originates from inside the Exchange Online organization. Add **The sender is located** &gt; **Inside the organization** for sending mail.
7. In **Apply this rule if**, select a condition, and enter a value if necessary. For example, to encrypt messages going to DrToniRamos@hotmail.com:

    1. In **Apply this rule if**, select **the recipient is**.
    2. Select an existing name from the contact list or type a new email address in the **check names** box.

        - To select an existing name, select it from the list and then click **OK**.
        - To enter a new name, type an email address in the **check names** box and then select **check names** &gt; **OK**.
8. To add more conditions, choose **More options** and then choose **add condition** and select from the list.

    For example, to apply the rule only if the recipient is outside your organization, select **add condition** and then select **The recipient is external/internal** &gt; **Outside the organization** &gt; **OK**.
9. To enable message encryption, from **Do the following**, select **Modify the message security** and then choose **Apply Office 365 Message Encryption and rights protection**. Select an RMS template from the list, choose **Save**, and then choose **OK**.

The list of templates includes all default templates and options as well as any custom templates you've created for use by Microsoft 365. If the list is empty, ensure that you have set up Microsoft Purview Message Encryption as described in [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities). For information about the **Do Not Forward** option, see [Do Not Forward option for emails](rights-management-usage-rights#do-not-forward-option-for-emails). For information about the **encrypt-only** option, see [Encrypt-only option for emails](rights-management-usage-rights#encrypt-only-option-for-emails).

You can choose **add action** if you want to specify another action.

### Use the EAC to update an existing mail flow rule to use Microsoft Purview Message Encryption

Perform the following steps to update an existing mail flow rule to use Microsoft Purview Message Encryption.

1. In a web browser, using a work or school account that has been granted sufficient administrator permissions, such as Compliance Administrator, [sign in to Microsoft 365](https://support.microsoft.com/article/b9582171-fd1f-4284-9846-bdd72bb28426#ID0EAABAAA=Web_browser).
2. Choose the **Admin** tile.
3. In the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), choose **Admin centers** &gt; **Exchange**.
4. In the EAC, go to **Mail flow** &gt; **Rules**.
5. In the list of mail flow rules, select the rule you want to modify to use with Microsoft Purview Message Encryption and then choose **Edit**![Edit icon for modifying an existing mail flow rule.](media/ebd260e4-3556-4fb0-b0bb-cc489773042c.gif).
6. To enable encryption using Microsoft Purview Message Encryption, from **Do the following**, choose **Modify the message security** and then choose **Apply Office 365 Message Encryption and rights protection**. Select an RMS template from the list, choose **Save** and then choose **OK**.

    The list of templates includes all default templates and options as well as any custom templates you've created for use by Microsoft 365. If the list is empty, ensure that you have set up Microsoft Purview Message Encryption as described in [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities). For information about the Do Not Forward option, see [Do Not Forward option for emails](rights-management-usage-rights#do-not-forward-option-for-emails). For information about the encrypt-only option, see [Encrypt Only option for emails](rights-management-usage-rights#encrypt-only-option-for-emails).

    You can choose **add action** if you want to specify another action.
7. From the **Do the following** list, remove any actions that are assigned to **Modify the message security** &gt; **Apply the previous version of OME**.
8. Choose **Save**.

## Create mail flow rules to remove encryption for email messages with Microsoft Purview Message Encryption

You can define mail flow rules to remove message encryption with Microsoft Purview Message Encryption by using the EAC.

### Use the EAC to create a rule to remove encryption from email messages with Microsoft Purview Message Encryption

You can remove encryption from messages that was applied by your organization. You can also remove encryption from any encrypted attachments to ensure the whole email message is without any protection.

1. In a web browser, using a work or school account that has been granted sufficient permissions, such as Compliance Administrator, [sign in to Microsoft 365](https://support.microsoft.com/article/b9582171-fd1f-4284-9846-bdd72bb28426#ID0EAABAAA=Web_browser).
2. Choose the **Admin** tile.
3. In the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), choose **Admin centers** &gt; **Exchange**.
4. In the EAC, go to **Mail flow** &gt; **Rules** and select **New**![New icon for creating a new mail flow rule to remove encryption.](media/457cd93f-22c2-4571-9f83-1b129bcfb58e.gif) &gt; **Create a new rule**. For more information about using the EAC, see [Exchange admin center in Exchange Online](/en-us/exchange/exchange-admin-center).
5. In **Name**, type a name for the rule, such as `Remove encryption from outgoing mail`.
6. In **Apply this rule if**, select the conditions where encryption should be removed from messages. Add **The sender is located** &gt; **Inside the organization** for sending mail out to any recipients *or* add **The recipient is located** &gt; **Inside the organization** for receiving mail replies from outside the organization.
7. In **Do the following**, select **Modify the message security** &gt; **Remove Office 365 Message Encryption and rights protection applied by the organization**.
8. (Optional) In **Do the following**, select **Modify the message security** &gt; **Remove attachment rights protection protection applied by the organization**.
9. Save the rule.

## Create mail flow rules for Office 365 Message Encryption without Microsoft Purview Message Encryption

Office 365 Message Encryption is deprecated as of July 1, 2023. If you haven't yet moved your organization to Microsoft Purview Message Encryption, Microsoft recommends that you make a plan to move as soon as it is reasonable for your organization. For instructions, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities).