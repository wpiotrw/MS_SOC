---
layout: Conceptual
title: Microsoft Identity Manager licensing and downloads | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-identity-manager/microsoft-identity-manager-licensing
breadcrumb_path: /enterprise-mobility/toc.json
feedback_system: Standard
author: henrymbuguakiarie
ms.author: henrymbugua
description: This article outlines the approaches for licensing Microsoft Identity Manager (MIM) 2016, with pointers on where to download the software.
keywords: 
ms.date: 2024-11-10T00:00:00.0000000Z
ms.topic: concept-article
ms.service: microsoft-identity-manager
ms.assetid: 
ms.reviewer: billmath
ms.suite: ems
locale: en-us
document_id: ab7d8f95-fc1f-174f-e7da-d83504d5829c
document_version_independent_id: c30fa3fe-1aa1-5d54-fa88-eae462a38da1
original_content_git_url: https://github.com/MicrosoftDocs/MIMDocs-pr/blob/live/MIMDocs/microsoft-identity-manager-licensing.md
site_name: Docs
depot_name: Azure.MIMDocs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-identity-manager-licensing
moniker_range_name: 
monikers: []
item_type: Content
source_path: MIMDocs/microsoft-identity-manager-licensing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fecfc034-c4c2-43e6-be47-948bd4addcea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/16cf36da-59bd-4744-91e9-295292c63e5e
platformId: bc5fd2fc-c3e1-c33c-d968-6e9775bf44c5
---

# Microsoft Identity Manager licensing and downloads | Microsoft Learn

This article outlines the approaches for licensing Microsoft Identity Manager (MIM) 2016, with pointers on where to download the software.

## Licensing MIM for your organization

Microsoft Identity Manager 2016 is licensed on a per-user basis. The details on licensing are included in the Product Terms and related documents, which can be downloaded from the [licensing terms](https://www.microsoft.com/licensing/docs/view/Product-Terms) page.

### Licensing for Microsoft Entra ID P1 or P2 customers

Microsoft Identity Manager 2016 is included with Microsoft Entra ID P1 or P2 (P1 and P2), which is part of Enterprise Mobility + Security.

Microsoft Entra ID P1 or P2 is available through a [Microsoft Enterprise Agreement](https://www.microsoft.com/licensing/licensing-programs/enterprise.aspx), the [Open Volume License Program](https://www.microsoft.com/licensing/licensing-programs/open-license.aspx), and the Cloud Solution Providers program. Azure and Microsoft 365 subscribers can also buy Microsoft Entra ID P1 and P2 online. Read more at [Microsoft Entra pricing](https://www.microsoft.com/security/business/microsoft-entra-pricing).

### MIM CALs

If you don't have Microsoft Entra ID P1 or P2 subscriptions for your users, and are using more MIM capabilities beyond synchronization, then a [Client Access License (CAL)](https://www.microsoft.com/en-us/licensing/product-licensing/client-access-license.aspx) is required for each user whose identity is managed in MIM. If you want external users—such as business partners, external contractors, or customers—to be able to access MIM, you can acquire CALs for each of your external users, or acquire External Connector (EC) licenses. Microsoft Identity Manager 2016 CALs aren't required for users whose identity is only in the Microsoft Identity Manager synchronization service and isn't managed in any other MIM component.

### Licenses for platform components

A Windows Server license is required to use Microsoft Identity Manager 2016’s server software as a Windows Server add-on. And a MIM deployment also requires a SQL Server installation. Windows Server and SQL Server licenses aren't included with MIM.

## Obtaining MIM software

Before starting a new install of MIM or an upgrade from an earlier version, ensure you have the latest versions.

If you're starting a fresh install, you need to download the installation files for each MIM component that's relevant to your scenario. Then, download any updates for those files, and then download any other components that are separate downloads from the Download Center.

| Scenario | Component | Required for scenario? | DVD ISO folder name | Comments |
| --- | --- | --- | --- | --- |
| Synchronization | Sync Service (including connector to AD) | Yes | `Synchronization Service` |  |
| Synchronization | PCNS | No | `Password Change Notification Service` | To be installed on domain controllers |
| Synchronization | Connectors for LDAP, SQL, Web Services, PowerShell, Lotus Domino, Graph | No | N/A | Distributed via Download Center |
| Privileged Access Management | MIM Service | Yes | `Service and Portal` |  |
| Self-service | MIM Service, MIM Portal | Yes | `Service and Portal` |  |
| Self-service | Add-ins and extensions | No | `Add-ins and extensions` | To be installed on end-user PCs |
| Self-service | SCSM Reporting | No | `Data Warehouse Support Scripts` |  |
| Self-service | Hybrid reporting agent | No | N/A | Distributed via Download Center |
| Self-service | Language packs | No | `LANGUAGE Packs` |  |
| Certificate Management | CM | Yes | `Certificate Management` |  |
| Certificate Management | CM Bulk Client | No | `CM Bulk Client` |  |
| Certificate Management | CM Client | No | `CM Client` |  |
| Certificate Management | CM App for Windows | No | `FIMCMModernApp*` |  |

### Obtaining Windows installer packages

For a new installation, most organizations with Volume License agreements download the MIM installation packages from the [Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home?#/subscriptions/vlnew/downloadsandkeys). The DVD ISO file contains one folder for each MIM component: `Synchronization Service`, `Service and Portal`, etc. If you're going to install the software on a different computer from which you downloaded it, be sure to copy either the entire ISO file or the folder for the component: don't merely copy just an MSI file out of a folder without the rest of the files and sub-folders.

If you don't have Volume Licensing and have a subscription for Microsoft Entra ID P1 or P2, you can download the Microsoft Entra ID P1 or P2 edition of MIM 2016:

- [MIM 2016 SP3](https://aka.ms/MIMforEntra) — includes the `Synchronization Service` and `Service and Portal` components of MIM 2016 SP3. All the changes from published hotfixes as of April 2026 are included in the installers; later hotfixes must be downloaded separately.
- [MIM 2016 SP2](https://aka.ms/MIMforAADP) — includes the `Synchronization Service` and `Service and Portal` components of MIM 2016 SP2. All the changes from published hotfixes as of March 2021 are included in the installers; later hotfixes must be downloaded separately.

To validate your subscription, the MIM Service installer for the Microsoft Entra ID P1 or P2 edition requires internet connectivity. During installation, you're prompted for Microsoft Entra credentials with permission to read subscribed SKUs from your directory.

If you don't have Volume Licensing but have an appropriate developer subscription, you can download MIM 2016 as an ISO file from [Visual Studio My Benefits Downloads](https://my.visualstudio.com/Downloads). Sign in with your Visual Studio account, then search for:

- **MIM 2016 SP3** — Search for `Microsoft Identity Manager 2016 with Service Pack 3`
- **MIM 2016 SP2** — Search for `Microsoft Identity Manager 2016 with Service Pack 2`

### Obtaining updates

After installing MIM from an MSI file, you should next install the necessary hotfixes.

Check the [Identity Manager version release history](reference/version-history) for the most recent update release, which has a link to the download site for the installer patch files.

To determine which update files are necessary, this table lists the components and the name of the corresponding patch (MSP) file in an update.

| Scenario | Component | DVD ISO folder name | Corresponding update patch file name |
| --- | --- | --- | --- |
| Synchronization | Sync Service | `Synchronization Service` | `MIMSyncService_x64*.msp` |
| Self-service | MIM Service, MIM Portal | `Service and Portal` | `MIMService_x64*msp` |
| Self-service | Add-ins and extensions | `Add-ins and extensions` | `MIMAddinsExtensions*msp` |
| Self-service | Language packs | `LANGUAGE Packs` | `LANGUAGE Packs.zip` |
| Access management (BHOLD) | BHOLD | `BHOLD` | `AccessManagementConnector.msi`, `BHOLD*.msi` |
| Certificate Management | CM | `Certificate Management` | `MIMCM*.msp` |
| Certificate Management | CM Bulk Client | `CM Bulk Client` | `MIMCMBulkClient*msp` |
| Certificate Management | CM Client | `CM Client` | `MIMCMClient*msp` |

Be sure to read any release notes associated with the update prior to installing the MSP file.

Updates to [BHOLD](https://www.microsoft.com/download/details.aspx?id=55950) aren't distributed as MSP files, only as MSI installers.

### Other downloads

The following downloads may also be relevant:

- [Generic LDAP Connector, Generic SQL Connector, Graph Connector, Lotus Domino Connector, PowerShell Connector, Web Services Connector](https://go.microsoft.com/fwlink/?LinkId=717495)
- [Connector for SharePoint User Profile Store](https://www.microsoft.com/download/details.aspx?id=41164)