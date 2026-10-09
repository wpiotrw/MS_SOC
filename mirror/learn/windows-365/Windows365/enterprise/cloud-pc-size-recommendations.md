---
layout: Conceptual
title: Windows 365 size recommendations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/cloud-pc-size-recommendations
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about the different Cloud PC sizes that are available with different SKUs in Windows 365.
keywords: 
author: heetpalod13
ms.author: hpalod
manager: dougeby
ms.date: 2024-07-25T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: chbrinkh
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: a58bc849-97bf-54a9-f223-147506836252
document_version_independent_id: a58bc849-97bf-54a9-f223-147506836252
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/cloud-pc-size-recommendations.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/cloud-pc-size-recommendations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/cloud-pc-size-recommendations.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e2c9f30c-00ec-44c0-846c-b20dbfb3283f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/702271fe-87d7-4493-828b-2d6fde3de8ab
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 58004a26-ac16-a51c-b4e7-c26a8e9c7a12
---

# Windows 365 size recommendations | Microsoft Learn

Windows 365 offers fixed-price licensing (through Microsoft 365) for different Cloud PC sizes. You should assess your business requirements to determine which sizes make sense for your users.

If extra resources are needed for the Cloud PC, an admin or end user can easily upgrade the size of their Cloud PC. For more information, see [Resize a Cloud PC](resize-cloud-pc).

For information about end-user hardware requirements, see [End-user hardware requirements](../end-user-hardware-requirements).

This table shows examples of the different sizes available for a Cloud PC:

| Cloud PC CPUs, RAM, and storage | Example scenarios | Recommended apps |
| --- | --- | --- |
| 2vCPU/4GB/256GB2vCPU/4GB/128GB2vCPU/4GB/64GB | Firstline workers, call centers, education/training/CRM access, mergers and acquisition, short-term and seasonal, customer services. | Microsoft 365 Apps, Microsoft Teams (Audio only), OneDrive, Adobe Reader, Microsoft Edge, line-of-business apps, Defender support. |
| 2vCPU/8GB/256GB2vCPU/8GB/128GB | Bring-your-own-PC, work from home, market researchers, government, consultants. | Microsoft 365 Apps, Microsoft Teams, Outlook, Excel, Access, PowerPoint, OneDrive, Adobe Reader, Microsoft Edge, line-of-business apps, Defender support. |
| 4vCPU/16GB/512GB4vCPU/16GB/256GB4vCPU/16GB/128GB | Finance, government, consultants, healthcare services, bring-your-own-PC, work from home. | Microsoft 365 Apps, Microsoft Teams, Outlook, Excel, Access, PowerPoint, Power BI, Dynamics 365, OneDrive, Adobe Reader, Microsoft Edge, line-of-business app, Defender support. |
| 8vCPU/32GB/512GB8vCPU/32GB/256GB8vCPU/32GB/128GB | Software developers, engineers, content creators, design and engineering workstations. | Microsoft 365 Apps, Microsoft Teams, Outlook, Access, OneDrive, Adobe Reader, Microsoft Edge, Power BI, Visual Studio Code, virtualization-based workloads: Hyper-V, Windows Subsystem for Linux (WSL), line-of-business apps, and Defender support. |
| GPU Select 6vCPU/26GB/4GBvRAM/256GB GPU Standard 4vCPU/16GB/4GBvRAM/512GBGPU Super 8CPU/56GB/12GBvRAM/1TBGPU Max 16vCPU/110GB/16GBvRAM/1TBFor details, see [GPU Cloud PCs](gpu-cloud-pc). | Graphic design, image and video rendering, 3D modeling, gaming, data processing, and visualization | Microsoft 365 Apps, Microsoft Teams, Outlook, Excel, Access, Adobe, Figma, Autodesk, Revit, Illustrator, Blender, Unity, ArcGIS, Microsoft Edge, Power BI, Visual Studio Code, line-of-business apps, Defender support. |
| 16vCPU/64GB/512GB16vCPU/64GB/1TB | Software development, engineering, data analysis and visualization, financial services and wealth management. | Microsoft 365 Apps, Microsoft Teams, Outlook, Excel, Access, Adobe Reader, Microsoft Edge, Power BI, Tableau, Visual Studio Code, Blackrock Aladdin, Bloomberg, Eclipse, line-of-business apps, Defender support. |
| 32vCPU/128GB/1TB32vCPU/128GB/2TB | Advanced software development and large-scale engineering workloads, AI/ML model development (non-GPU intensive), high-performance data analytics and visualization, power users running multiple heavy applications concurrently. | Microsoft 365 Apps, Microsoft Teams, Outlook, Excel, Access, Adobe Reader, Microsoft Edge, Power BI, Tableau, Visual Studio Code, Python, R, and data science frameworks (e.g. Pandas, Spark clients), Enterprise financial platforms (e.g. BlackRock, Aladdin, Bloomberg), Virtualization tools (Hyper-V, WSL), Eclipse, line-of-business apps, Defender support. |

The recommended gallery image is available in the Provisioning Policy marketplace. For more information, see [Device images overview](device-images).

## Test performance

To ensure experience expectations are met, you should test your deployment with simulation tools. You can track the user experience and resource consumption with services like Endpoint Analytics.