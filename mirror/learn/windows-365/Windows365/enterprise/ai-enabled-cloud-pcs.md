---
layout: Conceptual
title: AI-enabled Cloud PC (Frontier Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/ai-enabled-cloud-pcs
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: 'I-enabled Cloud PCs offers improved Windows Search and Click to Do features currently only available on Copilot+ PCs. This article covers setup requirements, user and IT admin experiences, privacy and security details, and troubleshooting guidance for easy deployment and management. '
author: rachellelcheung
ms.author: racheun
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.topic: concept-article
ms.date: 2026-03-11T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 98c5b3fc-5568-63b2-653d-9ea04915f00b
document_version_independent_id: 98c5b3fc-5568-63b2-653d-9ea04915f00b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/ai-enabled-cloud-pcs.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/ai-enabled-cloud-pcs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/ai-enabled-cloud-pcs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1ccd0352-8572-7316-c7fb-e12812bfbfa4
---

# AI-enabled Cloud PC (Frontier Preview) | Microsoft Learn

## Introduction

AI-enabled Cloud PCs offer improved Windows search and Click to Do features currently only available on Copilot+ PCs. This article covers setup requirements, user and IT admin experiences, privacy and security details, and troubleshooting guidance for easy deployment and management. 

Important

Future availability of these features is dependent on the results of this [Frontier](https://adoption.microsoft.com/copilot/frontier-program/) Public Preview and is subject to change. 

## Requirements

To use AI-enabled Cloud PCs during Frontier Preview, you must meet the Cloud PC specifications and assign AI-enablement to Cloud PCs in Microsoft Intune. 

### Cloud PC specifications

To use AI-enabled features, your Cloud PC must meet the following requirements: 

- Have a Windows 365 Enterprise SKU that has at least 8vCPU, 32GB of RAM and 128 GB minimum of total disk storage.
- Be deployed in one of the following supported regions: 

    - West US 2
    - West US 3
    - East US
    - East US 2
    - Central India
    - Central US
    - South East Asia
    - Australia East
    - UK South
    - West Europe
    - North Europe
    - Japan East
    - Germany West Central
    - South Central US
    - Canada Central
- Have a Windows OS build version of **24H2 (&gt;= 26100.7705)** or **25H2 (&gt;= 26200.7705)**.
- Enable the **RemoteSigned** execution policy on the Cloud PC. 

    - Open **PowerShell** on the Cloud PC with admin privileges (Run as Administrator)
    - Run the following command: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Enable the **Enable features introduced via servicing that are off by default** policy 

    - Open the **Local** **Group Policy Editor** app. (It might appear as **Edit group policy** in Task bar search results.)
    - Navigate to **Windows Components/Windows Update/Manage end user experience/Enable features introduced via servicing that are off by default**. (If this path isn’t visible, start by checking under **Computer Configuration/Administrative Templates**.)
    - Right click on the policy, select **Edit** and in the popup select **Enable** and then select **Apply**.
    - Open the **Settings** app, navigate to **Windows Update**, select **Check for updates**, install any pending updates, and then restart your Cloud PC.

### Assign AI-enablement to Cloud PCs in Intune

You can assign AI-enablement to Cloud PCs in Intune to get related features. See [Manage AI-enabled features (Frontier Preview)](manage-ai-enabled-features) for more details. 

## Validate AI-enabled Cloud PC status

After Cloud PCs are given AI-enabled entitlement, it can take up to **48 hours** for related features to become usable since background processes must complete setup before features are available. Once this wait period is over, **check for any additional Windows Updates and** **restart your Cloud PC (and repeat this until there are no pending updates).** You will likely need to repeat the checking for and applying updates process 3-5 times. Afterwards, AI-enabled status can be verified in multiple places: 

- Windows App
- Windows Task bar
- Intune Reporting

### Windows App

AI-enabled Cloud PCs have an “AI-enabled (Frontier)” tag on the device card within the Windows App. This helps users differentiate AI-enabled devices from other available Cloud PCs. 

![An image showing an example of the &quot;AI-enabled (Frontier)&quot; tag on a device card in the Windows App](media/manage-ai-enabled-features/ai-enabled-tag1.png)

### Windows Task bar (from within the Cloud PC)

AI-enabled Cloud PCs have a magnifying glass with sparkles icon within the search box on the Task bar. 

![An image showing the task bar with a magnifying glass and sparkles icon on a Cloud PC](media/manage-ai-enabled-features/magnifying-sparkles.png)

Note

After a Windows Update, the sparkles might disappear from the magnifying glass icon. If clicking within the Windows search box does not recover the magnifying glass with sparkles icon, see [AI-enabled Cloud PC Known Issues - Windows 365](/en-us/troubleshoot/windows-365/windows-365-ai-enabled-cloud-pc-known-issues) to investigate its absence. 

### Intune Reporting

For more information, see [Manage AI-enabled features (Frontier Preview)](manage-ai-enabled-features) for ways IT admins can use Intune to validate Cloud PCs are AI-enabled. 

## Supported Features

AI-enabled Cloud PCs offer the following features available on Copilot+ PCs: 

- Improved Windows search
- Click to Do

### Improved Windows search

Improved Windows search enables users to locate files using descriptive queries, using AI to interpret intent and deliver relevant results within the Windows Search box in the task bar and in File Explorer. For example, if you have a picture of an airplane titled "Picture26.jpg," and you search "Airplane," the correct file should appear.

**Disclaimer**: Works with specific text, image, and document formats only; optimized for select languages (English, Chinese (Simplified), French, German, Japanese, and Spanish).

![An image showing an example of using improved Windows search on a Cloud PC](media/manage-ai-enabled-features/windows-search.png)

Improved Windows search also allows users to search across multiple sources including local files and cloud storage through OneDrive. Users can search based on the content of the files rather than just the metadata like the title. This unified experience works within the Windows search box in the task bar and in File Explorer. 

To learn more about improved Windows search, see [Find Files Fast with Improved Windows Search](https://www.microsoft.com/en-us/windows/learning-center/find-files-fast-with-improved-search?msockid=32f7b5db7059626d3e32a0d371746303) and see [Semantic indexing for Microsoft Copilot](/en-us/microsoftsearch/semantic-index-for-copilot). 

### Click to Do

Click to Do simplifies the actions necessary to perform common actions on highlighted text or images on the screen. To activate this feature, press Windows key + Q or hold down the Windows key while left clicking an element on your screen. 

![An image showing an example of using Click to DO on a Cloud PC](media/manage-ai-enabled-features/click-to-do.png)

Note

You must launch the **Click to Do** app before using the feature for the first time following AI-enablement and after **every** Cloud PC restart. Afterwards, you can use the keyboard shortcuts to activate Click to Do. 

Note

Currently some intelligent text actions are not supported on Cloud PC yet. Text actions with Microsoft apps like Word and Notepad work, but "Ask Microsoft Copilot" does not yet work.

Note

Image actions now available across devices; other actions vary by device, region, language, and character sets. Subscription required for some actions.

To learn more about Click to Do, see [Click to Do: do more with what’s on your screen - Microsoft Support](https://support.microsoft.com/en-us/windows/click-to-do-do-more-with-what-s-on-your-screen-6848b7d5-7fb0-4c43-b08a-443d6d3f5955).

## Privacy and Security information

AI-enabled Cloud PCs adhere to the privacy documentation for Windows 365 here: [Privacy and data in Windows 365](privacy-personal-data): 

1. **Data processing**: AI-enabled features on Windows 365 Cloud PCs process data ephemerally using a secure Windows 365 cloud service. No personal or user data is stored in the cloud service at any time nor used for training of any AI models.
2. **Data storage**: All data and indexes are stored in the Cloud PC. This behavior is unchanged from existing Windows AI features.
3. **Customer controls**: Tenant IT admin can choose to enable related AI features for specific users and Cloud PCs. These features are off by default so the IT admin must enable them first.

Learn more about privacy, customer data, and customer content in Windows 365: [Privacy and data in Windows 365](privacy-personal-data).

## Troubleshooting

To learn about known issues with AI-enabled Cloud PCs, see [AI-enabled Cloud PC Known Issues - Windows 365](/en-us/troubleshoot/windows-365/windows-365-ai-enabled-cloud-pc-known-issues).