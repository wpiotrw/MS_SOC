---
layout: Conceptual
title: Troubleshoot AzCopy in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-troubleshooting-azcopy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Troubleshoot errors for Azure AzCopy when loading non-Office 365 data for error remediation in eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: troubleshooting
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-mar2020
- seo-marvel-apr2020
locale: en-us
document_id: 7f2124b1-7542-9ed7-74a3-f3b63d8fe1f5
document_version_independent_id: 7f2124b1-7542-9ed7-74a3-f3b63d8fe1f5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-troubleshooting-azcopy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-troubleshooting-azcopy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-troubleshooting-azcopy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: ca943ddb-7675-4178-8986-37b237d90083
---

# Troubleshoot AzCopy in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When loading non-Microsoft 365 data or documents for error remediation in Microsoft Purview eDiscovery (Premium), the user interface supplies an Azure AzCopy command that contains parameters with the location of where the files that you want to upload are stored and the Azure storage location that the files will be uploaded to. To upload your documents, you copy this command and then run it in a Command Prompt on your local computer.

Usually the command that's provided works when you run it. However, there may be cases when the command that's displayed won't run successfully. Here's a few possible reasons.

## The supported version of AzCopy isn't installed on the local computer

You should use the latest version of AzCopy to load non-Microsoft 365 data in eDiscovery (Premium). To install the latest version, see [Get started with AzCopy](/en-us/azure/storage/common/storage-use-azcopy-v10).

## AzCopy isn't installed on the local computer or it's not installed in the default location

If AzCopy isn't installed or it's installed in a location other than the default install location (which is `%ProgramFiles(x86)%`), you may receive the following error when you run the AzCopy command:

> 
> The system cannot find the path specified.

If AzCopy isn't installed on the local computer, see [Get started with AzCopy](/en-us/azure/storage/common/storage-use-azcopy-v10). Be sure to install it in the default location.

If AzCopy is installed, but it's installed in a location different than the default location, you can copy the command, paste it to a text file, and then change the path to the location where AzCopy is installed. For example, if Azcopy is located in `%ProgramFiles%`, then you can change the first part of the command from `%ProgramFiles(x86)%\Microsoft SDKs\Azure\AzCopy.exe` to `%ProgramFiles%\Microsoft SDKs\Azure\AzCopy`. After you make this change, copy it from the text file, and then run it a Command Prompt.

Tip

If AzCopy is installed in a location other then the default install location, consider uninstalling it and then re-installing it in the default location. This will help prevent this issue in the future.