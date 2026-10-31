---
layout: Conceptual
title: Learn about the Microsoft Purview extension for Chrome | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-18T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MET150
description: The Microsoft Purview Extension extends monitoring and control of file activities and protective actions to the Google Chrome browser
locale: en-us
document_id: b3619998-c37c-66e2-ebe6-d028ff969519
document_version_independent_id: b3619998-c37c-66e2-ebe6-d028ff969519
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-chrome-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-chrome-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-chrome-learn-about.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
platformId: 871c2808-e13b-3661-4f48-1bf3fd15f18f
---

# Learn about the Microsoft Purview extension for Chrome | Microsoft Learn

[Endpoint data loss prevention (endpoint DLP)](endpoint-dlp-learn-about) extends the activity monitoring and protection capabilities of [Microsoft Purview Data Loss Prevention (DLP)](dlp-learn-about-dlp) to sensitive items on Windows 10/11 devices. Once you onboard devices into the Microsoft Purview solutions, information about what users are doing with sensitive items is made visible in [activity explorer](data-classification-activity-explorer). Then you can enforce protective actions on those items using [data loss prevention policies](dlp-learn-about-dlp).

After you install the Microsoft Purview extension for Chrome on a Windows 10/11 device, your organization can monitor attempts to access or upload a sensitive item to a cloud service in Google Chrome, and enforce protective actions via DLP.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Activities you can monitor and take action on

The extension enables you to audit and manage the following types of activities users take on sensitive items on devices running Windows 10/11.

| activity | description | supported policy actions |
| --- | --- | --- |
| file copied to cloud | Detects when a user attempts to upload a sensitive item to a restricted service domain through the Chrome browser | audit, block with override, block |
| file printed | Detects when a user attempts to print a sensitive item from the Chrome browser to a local or network printer | audit, block with override, block |
| file copied to clipboard | Detects when a user attempts to copy & paste information from a sensitive item in the Chrome browser into another app, process, or item. | audit, block with override, block |
| file copied to removable storage | Detects when a user attempts to copy a sensitive item or information from the Chrome browser to removable media or USB device | audit, block with override, block |
| file copied to network share | Detects when a user attempts to copy a sensitive item or information from the Chrome browser to a network share or mapped network drive. | audit, block with override, block |

Note

Microsoft Purview Insider Risk Management requires that this extension be installed to monitor and take action on activities in the Chrome browser. For more information, see [Learn about and configure Insider Risk Management browser signal detection](insider-risk-management-browser-support).

### Purview Chrome extension behavior

The DLPEngine caches all files for about 15 minutes by default to prevent repeated upload attempts. During the cache period, the file is blocked from being uploaded to any domain, so if you upload to an unallowed domain and then immediately to an allowed domain, the cached response may block the upload.

Tip

Microsoft recommends that you use Microsoft Edge if you need to upload files in quick succession.

## Deployment process

1. [Get started with endpoint data loss prevention](endpoint-dlp-getting-started)
2. [Onboarding tools and methods for Windows 10/11 devices](device-onboarding-overview)
3. [Install the extension for Chrome on your Windows 10/11 devices](dlp-chrome-get-started)
    Note

    Command access for the user is a prerequisite for the Microsoft Purview Extension extension for Chrome to work.
4. [Create and Deploy data loss prevention policies](dlp-create-deploy-policy) that restrict upload to cloud service, or access by unallowed browsers actions and apply them to your Windows 10/11 devices