---
layout: Conceptual
title: Get started with data loss prevention protections for Recall | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-recall-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: This article describes the prerequisites and policy configuration to help protect against sensitive information being included in a Recall snapshot.
ai-usage: ai-assisted
locale: en-us
document_id: ff3bf513-d73c-10fd-a2a6-45855473c464
document_version_independent_id: ff3bf513-d73c-10fd-a2a6-45855473c464
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-recall-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-recall-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-recall-get-started.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 7282f98e-ec1b-0916-2318-1e404fc417de
---

# Get started with data loss prevention protections for Recall | Microsoft Learn

[Recall](/en-us/windows/client-management/manage-recall) is a [Copilot+ PC](https://www.microsoft.com/en-us/windows/learning-center/getting-started-copilot-plus-pc) feature that allows users to search locally saved and locally analyzed snapshots of their screen using natural language. To help protect against the inclusion of sensitive content in these snapshots, you can use DLP policies. The following sections walk you through the prerequisites and configuration steps you perform to start using DLP protections for Recall.

DLP protections for Recall are supported for sensitive information types and sensitivity labeled items in:

- Sensitivity labeled Teams channels
- Sensitivity labeled Teams meeting chats
- SIT or sensitivity labeled files that are opened with Microsoft 365 Copilot App (Word, Excel PowerPoint web apps) using Microsoft Edge for Business
- Labeled emails Outlook
- Locally stored files with sensitivity labels or SITs
- Files stored in the cloud that with sensitivity labels or SITS that get opened in Office apps (Word, Excel, PowerPoint) on the device

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you begin

IT admins can set policies that give Copilot+ PC users the option to enable saving snapshots. The user must then opt in to taking snapshots. For more information, see [Manage Recall](/en-us/windows/client-management/manage-recall).

### Prerequisites

Before you configure DLP protections for Recall, ensure the following prerequisites are met:

- meet all device prerequisites for Recall as described in [Manage Recall](/en-us/windows/client-management/manage-recall).
- Microsoft Purview endpoint DLP is enabled for the tenant the Copilot+ PC is onboarded [to endpoint data loss prevention](endpoint-dlp-getting-started).
- Microsoft Intune is running on the tenant to create Windows tenant policies.
- Copilot+ PC must be running
    - Windows build greater than 262100.67225
    - Anti-malware Client version greater than 4.18.2508.5 or higher
    - Teams version 25290.205.4069.4 or higher
    - Office desktop apps (Word, Excel, PowerPoint) version 19127 or higher
    - Microsoft Edge for Business. For more information, see [Automatic activation of your Microsoft Purview DLP policy in Microsoft Edge](/en-us/deployedge/microsoft-edge-dlp-purview-configuration#step-3-turn-on-microsoft-edge-settings)

Set the following Group Policy settings on the Copilot+ PC to enable DLP protections for Recall using either Microsoft Intune or Local Group Policy Editor.

| Local Group Policy | Set to | Required | Notes |
| --- | --- | --- | --- |
| WindowsAI &gt; Turn off saving snapshots for use with Recall | Disable | Yes | This policy makes the Recall feature available to users to opt in. This doesn't automatically start Recall for users. Users must launch recall and opt-in to taking snapshots on their machines. |
| WindowsAI &gt; Set maximum duration for storing snapshots used by Recall | 30-180 | Optional | This is the retention period for snapshots in days |
| WindowsAI/Set maximum storage for snapshots used by Recall | 10-150 | Optional | This is the storage limit. For more information, see, [Manage Recall](/en-us/windows/client-management/manage-recall). |
| WindowsAI &gt; SetDataLossPreventionProvider policy | HKEY\_LOCAL\_MACHINE\software\microsoft\windows defender; value:InstallLocation; binary:endpointdlp.dll; minversion:4.18.25080.5 | Yes | This registry value sets the DLP provider (Microsoft Purview) to be used with Recall. This capability is implemented as a public API. |

For more information, see: [SetDataLossPreventionProvide](/en-us/windows/client-management/mdm/policy-csp-windowsai#setdatalosspreventionprovider)

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

For information on the permissions required to create and manage DLP policies, see [Permissions for creating and deploying DLP policies](dlp-create-deploy-policy#permissions).

## Configuring DLP policy protections for Recall

When you configure a Copilot+ PC so that the user can opt in to Recall, and the user does opt in, you can create new DLP policies or edit existing policies to include protections for Recall.

For general information on creating DLP policies, see [Create and deploy a data loss prevention policy](dlp-create-deploy-policy).

The setting to enable DLP protections for Recall is available when you create or edit a DLP policy in **Enterprise Applications & devices** policies. In the policy editing workflow under **Actions** &gt; **Audit or restrict activities on devices** &gt; **Restrictions in Windows Recall in Copilot+ PCs** &gt; **Restrict content in Windows Recall**. You can select **Audit only** or **Block**.

![screenshot of the Restrict content in Windows Recall selection box.](media/dlp-recall-get-started/dlp-recall.png)

If you select **Audit only**, then the user doesn't see any notification when a snapshot is taken that contains sensitive information. However, the event is logged in the DLP reports.

If you select **Block**, then when a snapshot is taken that contains sensitive information, then the sensitive content isn't included in the snapshot.

View Recall related events in [Microsoft Purview Activity Explorer](data-classification-activity-explorer).