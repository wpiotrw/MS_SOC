---
layout: Conceptual
title: Learn about the default DLP policy in Microsoft Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-teams-default-policy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-06-24T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
description: Learn about the default data loss prevention policy in Microsoft Teams
locale: en-us
document_id: 5ba27a61-fe32-37ab-2649-605dc03ceb23
document_version_independent_id: 5ba27a61-fe32-37ab-2649-605dc03ceb23
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-teams-default-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-teams-default-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-teams-default-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c5abca30-95b3-a553-36b2-081426c86e70
---

# Learn about the default DLP policy in Microsoft Teams | Microsoft Learn

[Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) capabilities have been extended to include Microsoft Teams chat and channel messages, including private channel messages. As a part of this release, we created a default DLP policy for Microsoft Teams for first-time customers to the [Microsoft Purview portal](https://purview.microsoft.com).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the default policy do?

The default DLP policy for Teams tracks all the credit card numbers shared internally and externally to the organization. This policy is on by default for all users of the tenant. It does not generate any policy tips for end users but does generate an Alert event and also triggers a low severity email to the admin (added in the policy). Administrator can view the activities and edit the policies details by logging into the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Navigate to **Data Loss prevention** &gt; **Policies**.

![default Teams DLP policy.](media/default-teams-dlp-policy.png)

## Edit or delete the default policy

To [edit the default policy for better performance or to delete it](dlp-create-deploy-policy), just use an account with **DLP Compliance Management** permissions. For more information, see, [Permissions](dlp-create-deploy-policy#permissions).