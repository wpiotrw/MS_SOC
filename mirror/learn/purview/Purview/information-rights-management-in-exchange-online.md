---
layout: Conceptual
title: Exchange Online mail encryption with AD RMS | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-rights-management-in-exchange-online
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-08T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.assetid: 2c956776-0016-4be6-b4cd-133a237f4a9e
ms.collection: 
ms.custom:
- seo-marvel-apr2020
description: Learn how to configure Exchange Online IRM to use on-premises Active Directory Rights Management Service (AD RMS) to satisfy your organization requirements.
locale: en-us
document_id: e33eff78-80c8-d1db-d15c-cc7e207a9957
document_version_independent_id: e33eff78-80c8-d1db-d15c-cc7e207a9957
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-rights-management-in-exchange-online.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-rights-management-in-exchange-online
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-rights-management-in-exchange-online.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f5263c5d-4e0a-f74a-ee4f-e0484c941113
---

# Exchange Online mail encryption with AD RMS | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

To help prevent information leakage, Exchange Online includes Information Rights Management (IRM) functionality that provides online and offline protection of email messages and attachments. You can configure Exchange Online IRM to use on-premises Active Directory Rights Management Service (AD RMS), if needed, to satisfy your organization requirements. This is not common. If you do not have a requirement to use AD RMS, use [Microsoft Purview Message Encryption](ome) instead.

IRM protection can be applied by users in Microsoft Outlook or Outlook on the web, and it can be applied by administrators using transport protection rules or Outlook protection rules. IRM helps you and your users control who can access, forward, print, or copy sensitive data within an email.

## Changes to how IRM works with message encryption and Microsoft Entra ID

As of September 2017, when you set up Microsoft Purview Message Encryption for your organization, you also set up IRM for use with the Azure Rights Management service. You no longer set up IRM with Rights Management service separately. Instead, message encryption and rights management work seamlessly together. For more details about Microsoft Purview Message Encryption, see [Message Encryption FAQ](ome-faq). If you're ready to get started using Microsoft Purview Message Encryption within your organization, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities).

## How IRM works with Exchange Online and Active Directory Rights Management Services

Exchange Online IRM uses on-premises Active Directory Rights Management Services (AD RMS), an information protection technology in Windows Server 2008 and later. IRM protection is applied to email by applying an AD RMS rights policy template to an email message. Rights are attached to the message itself so that protection occurs online and offline and inside and outside of your organization's firewall.

Users can apply a template to an email message to control the permissions that recipients have on a message. Actions, such as forwarding, extracting information from a message, saving a message or printing a message can be controlled by applying an AD RMS rights policy to the message.

You can configure IRM to use an AD RMS server running Windows Server 2008 or later. You can use this AD RMS server to manage the AD RMS rights policy templates for your cloud-based organization. Outlook also relies on the AD RMS server to enable users to apply IRM protection to messages they send. For details, see [Configure IRM to use an on-premises AD RMS server](configure-irm-to-use-an-on-premises-ad-rms-server).

After it's enabled, IRM protection can be applied to messages as follows:

- **Users can manually apply a template using Outlook and Outlook on the web.** Users can apply an AD RMS rights policy template to an email message by selecting the template from the **Set permissions** list. When users send an IRM-protected message, any attached files that use a supported format also receive the same IRM protection as the message. IRM protection is applied to files associated with Word, Excel, and PowerPoint, as well as .xps files and attached email messages.
- **Administrators can use transport protection rules to apply IRM protection automatically to both Outlook and Outlook on the web.** You can create transport protection rules to IRM-protect messages. Configure the transport protection rule action to apply an AD RMS rights policy template to messages that meet the rule condition. After you enable IRM, your organization's AD RMS rights policy templates are available to use with the transport protection rule action called **Apply rights protection to the message with**.
- **Administrators can create Outlook protection rules.** Outlook protection rules automatically apply IRM-protection to messages in Outlook 2010 (not Outlook on the web) based on message conditions that include the sender's department, who the message is sent to, and whether recipients are inside or outside your organization. For details, see [Create an Outlook Protection Rule](/en-us/exchange/create-an-outlook-protection-rule-exchange-2013-help).