---
layout: Conceptual
title: Learn about the Microsoft Purview extension for Firefox | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-firefox-extension-learn
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-08-21T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
search.appverid:
- MET150
description: The Microsoft Purview extension for Firefox extends monitoring and control of file activities and protective actions to the Firefox browser
locale: en-us
document_id: 229697e8-90e4-8e1d-2b0e-2c5f05225812
document_version_independent_id: 229697e8-90e4-8e1d-2b0e-2c5f05225812
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-firefox-extension-learn.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-firefox-extension-learn
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-firefox-extension-learn.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
platformId: b6aa637d-c53b-5c5c-41eb-eb2c5677cbf7
---

# Learn about the Microsoft Purview extension for Firefox | Microsoft Learn

[Endpoint data loss prevention (endpoint DLP)](endpoint-dlp-learn-about) extends the activity monitoring and protection capabilities of [Microsoft Purview data loss prevention (DLP)](dlp-learn-about-dlp) to sensitive items that are on Windows 10/11 devices. Once you onboard devices to the Microsoft Purview solutions, the information about what users are doing with sensitive items is made visible in [activity explorer](data-classification-activity-explorer). Then you can enforce protective actions on those items via [DLP policies](dlp-learn-about-dlp).

After you install the Firefox extension on a Windows 10/11 device, your organization can monitor when a user attempts to access or upload a sensitive item to a cloud service using Mozilla Firefox, and enforce protective actions via DLP.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Activities you can monitor and take action on

The extension enables you to audit and manage the following types of activities users take on sensitive items on devices running Mozilla Firefox in Windows 10.

| activity | description | supported policy actions |
| --- | --- | --- |
| file copied to cloud | Detects when a user attempts to upload a sensitive item to a restricted service domain through the Firefox browser | audit, block with override, block |
| file printed | Detects when a user attempts to print a sensitive item that is open in the Firefox browser to a local or network printer | audit, block with override, block |
| file copied to clipboard | Detects when a user attempts to copy information from a sensitive item in the Firefox browser into another app, process, or item. | audit, block with override, block |
| file copied to removable storage | Detects when a user attempts to copy a sensitive item or information from a sensitive item in the Firefox browser to removable media or USB device | audit, block with override, block |
| file copied to network share | Detects when a user attempts to copy a sensitive item or information from the Firefox browser to a network share or mapped network drive. | audit, block with override, block |

## Deployment process

1. [Get started with endpoint data loss prevention](endpoint-dlp-getting-started)
2. [Onboarding tools and methods for Windows 10 devices](device-onboarding-overview)
3. [Install the extension for Firefox extension on your Windows 10 devices](dlp-firefox-extension-get-started)
4. [Create and Deploy data loss prevention policies](dlp-create-deploy-policy) that restrict upload to cloud service, or access by unallowed browsers actions and apply them to your Windows 10 devices