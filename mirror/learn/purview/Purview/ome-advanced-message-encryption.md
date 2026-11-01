---
layout: Conceptual
title: Advanced Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome-advanced-message-encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-encryption
ms.date: 2023-09-08T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Advanced Message Encryption helps organizations meet their compliance obligations by enabling admins to do even more with protected messages.
locale: en-us
document_id: 6af32817-e1df-736f-86af-71470bddbb18
document_version_independent_id: 6af32817-e1df-736f-86af-71470bddbb18
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome-advanced-message-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome-advanced-message-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome-advanced-message-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
platformId: c86cb119-e052-49fe-a7f2-a00134e5d21d
---

# Advanced Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Advanced Message Encryption helps customers meet compliance obligations that require more flexible controls over external recipients and their access to encrypted emails. With Advanced Message Encryption in Office 365, you can control sensitive emails shared outside the organization with automatic policies and track those activities through the encrypted message portal access logs. You configure these policies to identify sensitive information types such as PII, Financial, or Health IDs, or you can use keywords to enhance protection. Once you've configured the policies, you pair policies with custom branded email templates and then add an expiration date for extra control of emails that fit the policy. Also, admins can further control encrypted emails accessed externally through a secure web portal by revoking access to the mail at any time.

You can only revoke and set an expiration date for emails sent to external recipients.

## Get started with Microsoft Purview Advanced Message Encryption

The following articles describe how you set up and use Advanced Message Encryption.

If you do not have Office 365 Message Encryption set up already, see [Set up new Office 365 Message Encryption capabilities](set-up-new-message-encryption-capabilities).

With Advanced Message Encryption, you're not limited to a single branding template. Instead, you can create and use multiple branding templates. Adding custom branding also lets you enable tracking a revocation of encrypted messages. For information, see [Add your organization's brand to your encrypted messages](add-your-organization-brand-to-encrypted-messages). When you use custom branding, external recipients receive a notification email that contains a link to the OME portal. The mail flow rule determines which branding template the notification email and OME Portal use. This way, your secure content isn't sent outside your organization.

You can only revoke messages and apply expiration dates to messages that users receive through the portal. In other words, email that has a custom branding template applied. For more information and an example, see the guidance in [Ensure all external recipients use the encrypted message portal to read encrypted mail](manage-office-365-message-encryption#ensure-all-external-recipients-use-the-encrypted-message-portal-to-read-encrypted-mail).

[Set an expiration date for email encrypted by Microsoft Purview Advanced Message Encryption](ome-advanced-expiration). Control sensitive emails shared outside the organization with automatic policies that enhance protection by expiring access through a secure web portal to encrypted emails.

[Revoke email encrypted by Microsoft Purview Advanced Message Encryption](revoke-ome-encrypted-mail). Control sensitive emails shared outside the organization and enhance protection by revoking access through a secure web portal to encrypted emails.

[Encrypted message portal activity log by Microsoft Purview Advanced Message Encryption](audit-log-encrypted-messages). Monitor sensitive emails shared outside the organization in the encrypted message portal.