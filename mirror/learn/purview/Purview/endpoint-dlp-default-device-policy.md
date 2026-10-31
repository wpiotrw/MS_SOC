---
layout: Conceptual
title: Learn about the default DLP policy for devices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-default-device-policy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-03-11T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Learn about the default DLP policy for devices
locale: en-us
document_id: 2b65704f-4cea-871d-cefb-08235da4b266
document_version_independent_id: 2b65704f-4cea-871d-cefb-08235da4b266
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-default-device-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-default-device-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-default-device-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 62fe722e-c7ae-5746-fc66-5fb62bf8bf31
---

# Learn about the default DLP policy for devices | Microsoft Learn

To help you protect sensitive data on endpoint devices, Microsoft provides a default Microsoft Purview data loss prevention (DLP) policy called **Default policy for devices**.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the default policy do?

This default policy looks for items with the sensitive information type [Credit card number](sit-defn-credit-card-number) It's configured like this.

- Admin units: **Full directory**
- Choose where to apply the policy: **Devices** &gt; **All users, groups, devices, device groups**
    - **SharePoint sites** &gt; **All sites**
    - **OneDrive accounts** &gt; **All users and groups**
- Conditions:
    - **Content contains** &gt; **Credit card number**
- Action:
    - **Audit or restrict activities on devices**
        - **Upload to a restricted cloud service domain or access from an unallowed browser** &gt; **Audit only**
        - **Copy to clipboard** &gt; **Audit only**
        - **Copy to a removable USB device** &gt; **Audit only**
        - **Copy to a network share** &gt; **Audit only**
        - **Print** &gt; **Audit only**
        - **Copy or move using unallowed Bluetooth app** &gt; **Audit only**
        - **Copy or move using RDP** &gt; **Audit only**
    - **App access restrictions** &gt; **Access by restricted apps** &gt; **Audit only**
- Policy mode: **Turn the policy on immediately**

Administrator can view the activities and edit the policies details by logging into the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Navigate to **Data Loss prevention** &gt; **Policies**.

## Edit or delete the default policy

To [edit the default policy for better performance or to delete it](dlp-create-deploy-policy), just use an account with **DLP Compliance Management** permissions. For more information, see, [Permissions](dlp-create-deploy-policy#permissions).