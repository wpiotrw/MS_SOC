---
layout: Conceptual
title: Learn about the default Office 365 DLP policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-o365-default-policy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-03-10T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Learn about the default data loss prevention Office 365 policy
locale: en-us
document_id: fdf1fd44-cc2d-3020-7136-a898ca4bb603
document_version_independent_id: fdf1fd44-cc2d-3020-7136-a898ca4bb603
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-o365-default-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-o365-default-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-o365-default-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 3fca79da-55d0-5996-d5b3-822ac521c68b
---

# Learn about the default Office 365 DLP policy | Microsoft Learn

To help you protect sensitive data in Microsoft Office 365 apps, Microsoft created a default Microsoft Purview data loss prevention (DLP) policy called **Default Office 365 DLP policy**.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the default policy do?

This default policy looks for items with the sensitive information type [Credit card number](sit-defn-credit-card-number) It's configured like this.

- Admin units: **Full directory**
- Choose where to apply the policy:
    - **Exchange email** &gt; **All groups**
    - **SharePoint sites** &gt; **All sites**
    - **OneDrive accounts** &gt; **All users and groups**
- Conditions:
    - **Content is shared from Microsoft 365** &gt; **with people outside my organization** AND
    - **Content contains** &gt; **Credit card number**
- User Notifications:
    - **On**
    - **Notify these people** &gt; **The person who sent, shared, or modified the content** and **Owner of the SharePoint site or OneDrive account** and **Owner of the SharePoint or OneDrive content**.
    - **Attach matching email message to the notification (applies only to Exchange)**
    - With customized policy tip text.
- Policy mode: **Turn the policy on immediately**

Administrator can view the activities and edit the policies details by logging into the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Navigate to **Data Loss prevention** &gt; **Policies**.

## Edit or delete the default policy

To [edit the default policy for better performance or to delete it](dlp-create-deploy-policy), just use an account with **DLP Compliance Management** permissions. For more information, see, [Permissions](dlp-create-deploy-policy#permissions).