---
layout: Conceptual
title: Windows 365 requirements | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/requirements
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Windows 365 requirements
keywords: 
author: ericorman
ms.author: ericor
manager: tscott
ms.date: 2026-03-06T00:00:00.0000000Z
ms.topic: how-to
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
document_id: be34deb5-431e-8f2d-31e9-3e3636012834
document_version_independent_id: be34deb5-431e-8f2d-31e9-3e3636012834
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/requirements.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/requirements
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/requirements.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c450d479-44e5-4a9c-9b93-e6f9b69dd42d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e273b0-a43e-4cc8-9bf9-67d4d6a1e869
platformId: 7ee10758-1c5e-77dd-7cbd-60fee23751bf
---

# Windows 365 requirements | Microsoft Learn

Important

Windows 365 Frontline is now **Windows 365 Flex**. The product name in the Microsoft Intune admin center is being updated and may still appear as **Frontline** in some places. This article reflects those existing references where updates are still in progress. For more information about the rebrand, see [Expanding access to Windows 365](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-365-and-azure-virtual-desktop-expanding-access/4515931).

To use Cloud PCs, you must meet the following requirements:

## Azure requirements

# [Windows 365 Enterprise and Windows 365 Flex](#tab/enterprise)
None, if you plan on provisioning Microsoft Entra joined Cloud PCs on a Microsoft hosted network.

If you choose to provision Cloud PCs on your own network, an active Azure subscription with the following configurations is required:

- Sufficient permissions to grant Windows 365:
    - A reader role on the Azure subscription.
    - Windows365 network interface contributor role on the specified resource group.
    - Windows365 network user role on the virtual network.

# [Windows 365 Government](#tab/government)
All of the Windows 365 Enterprise requirements apply with the following additions.

A subscription in Azure Government is required for Windows 365 Government customers who would like to use any of the following capabilities:

- Hybrid AADJ
- AADJ and with the customer providing their own network
- Custom Images

---

## Microsoft Entra ID and Intune requirements

- A valid and working Intune and Microsoft Entra tenant.
- Intune default device type enrollment restrictions must be set to Allow Windows (MDM) platform for corporate enrollment. For more information, see [Device Enrollment Restrictions Limitations](/en-us/mem/intune/enrollment/enrollment-restrictions-set#limitations).
- Infrastructure configuration: If you plan on provisioning Microsoft Entra hybrid joined Cloud PCs, you must configure your infrastructure to automatically Microsoft Entra hybrid join any devices that domain join to the on-premises Active Directory. This [configuration lets them be recognized and managed in the cloud](/en-us/azure/active-directory/devices/overview).
- Microsoft Entra Domain Services isn't supported because it doesn't support Microsoft Entra hybrid join.

## Domain requirements

None, if you plan on provisioning Microsoft Entra joined Cloud PCs on a Microsoft hosted network.

If you choose to provision Microsoft Entra hybrid joined Cloud PCs, then the following configurations on your domain are required:

- If an organizational unit is specified, ensure it exists and is valid.
- An Active Directory user account with sufficient permissions to join the computer into the specified organizational unit within the Active Directory domain. If you don't specify an organizational unit, the user account must have sufficient permissions to join the computer to the Active Directory domain.
- User accounts that are assigned Cloud PCs must have a synced identity available in both Active Directory and Microsoft Entra ID.

Note

For the user account used to join the Cloud PCs to the Active Directory Domain Services, make sure to set up appropriate delegation following the instructions in [Increase the computer account limit in the Organizational Unit](/en-us/mem/autopilot/windows-autopilot-hybrid#increase-the-computer-account-limit-in-the-organizational-unit).

## Licensing requirements

- You must have an Intune license to use Intune to manage the devices.
- Windows 365 Enterprise: Users must have licenses for Windows E3, Intune, Microsoft Entra ID P1, and Windows 365 to use their Cloud PC.
- Windows 365 Flex: Users must
    - Have licenses for Windows E3, Intune, Microsoft Entra ID P1.
    - Be added to the Microsoft Entra security group in the provisioning policy to use their Cloud PC.

## Management requirements

- You must use [Microsoft Intune admin center](https://admin.microsoft.com/) to manage your Cloud PCs.
- You must have a Windows 365 Enterprise or Windows 365 Flex license to manage Cloud PC configurations.

## Role and identity requirements

- Admin role: You must be an [Intune Administrator in Microsoft Entra ID](/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles#intune-administrator) or [Windows 365 Administrator](/en-us/azure/active-directory/roles/permissions-reference) to provision Cloud PCs.
- User identity: Cloud PC users must be configured with [hybrid identities](/en-us/azure/active-directory/hybrid/whatis-hybrid-identity) so that they can authenticate with resources both on-premises and in the cloud.

## Supported Azure regions for Cloud PC provisioning

# [Windows 365 Enterprise and Windows 365 Flex](#tab/ent)
[Windows 365 Enterprise](/en-us/windows-365/enterprise/overview) and [Windows 365 Flex in Dedicated mode](/en-us/windows-365/enterprise/introduction-windows-365-flex#windows-365-flex-in-dedicated-mode) support multi-region selection model (Geography → Region Group → Region) to maximize resiliency and minimize provisioning failures.

[Windows 365 Flex in Shared mode](/en-us/windows-365/enterprise/introduction-windows-365-flex#windows-365-flex-in-shared-mode) requires selection of one specific Azure region. Multi-region selection is not available for this SKU.

You can provision Windows 365 Enterprise and Windows 365 Flex Cloud PCs in the following Azure regions (categorized by geography):

### Africa

| Region Group | Region |
| --- | --- |
| South Africa | South Africa North |

### Asia

| Region Group | Region |
| --- | --- |
| Hong Kong SAR | East Asia |
| Japan | Japan East |
| Japan | Japan West |
| South Korea | Korea Central |
| Singapore | Southeast Asia |

### Australia & New Zealand (ANZ)

| Region Group | Region |
| --- | --- |
| Australia | Australia East |
| New Zealand | New Zealand North |

### Canada

| Region Group | Region |
| --- | --- |
| Canada | Canada Central |

### Mexico

| Region Group | Region |
| --- | --- |
| Mexico | Mexico Central |

### Europe

| Region Group | Region |
| --- | --- |
| France (EU) | France Central |
| Germany (EU) | Germany West Central |
| Ireland (EU) | North Europe |
| Italy (EU) | Italy North |
| Netherlands (EU) | West Europe |
| Norway | Norway East |
| Poland (EU) | Poland Central |
| Spain (EU) | Spain Central |
| Sweden (EU) | Sweden Central |
| Switzerland | Switzerland North |
| United Kingdom | UK South |

### India

| Region Group | Region |
| --- | --- |
| India | India Central |

### Middle East

| Region Group | Region |
| --- | --- |
| Qatar | Qatar Central (Restricted) |
| Israel | Israel Central |
| UAE | UAE North |

### South America

| Region Group | Region |
| --- | --- |
| Brazil | Brazil South |

### US Central

| Region Group | Region |
| --- | --- |
| US Central | Central US |
| US Central | South Central US |

### US East

| Region Group | Region |
| --- | --- |
| US East | East US |
| US East | East US 2 |

### US West

| Region Group | Region |
| --- | --- |
| US West | West US 2 (Restricted) |
| US West | West US 3 |

# [Windows 365 Government](#tab/gov)
### Windows 365 for GCC and GCCH

For GCC and GCC High (GCCH) only, you can provision Windows 365 Enterprise and Windows 365 Flex in Dedicated mode Cloud PCs in the following Azure Government regions.

| Region |
| --- |
| Government US Arizona |
| Government US Virginia |
| Government US Texas |

### Windows 365 for FedRAMP

For FedRAMP only, you can provision Windows 365 Enterprise and Windows 365 Flex in Dedicated mode Cloud PCs in the following Azure regions.

| Region Group | Region |
| --- | --- |
| US Central | Central US |
| US Central | South Central US |
| US East | East US |
| US East | East US 2 |
| US West | West US 2 (Restricted) |
| US West | West US 3 |

---

### Alternate regions for Business Continuity and Disaster Recovery

A recommended region is an Azure region that supports availability zones and is the preferred location for Cloud PCs in a given geography. Alternate regions help to optimize latency and provide a second region for disaster recovery needs but don't support multiple availability zones. Alternate regions are only available for Cross-region Disaster Recovery (CRDR) and Disaster Recovery Plus (DR+). Because alternate regions only have one availability zone, there is no zonal resistance.

The following alternate regions are available:

| Geography | Recommended Region | Alternate Region |
| --- | --- | --- |
| Australasia | Australia East | Australia Southeast |
| US West | West US 2, West US 3 | West US |
| Canada | Canada Central | Canada East |
| India | Central India | South India |

##### How to configure alternate regions

Alternate regions can be selected in Cloud PC configurations. When selecting regions for CRDR or DR+, alternate regions appear below recommended regions with an **"Alternate region"** label to distinguish them.

##### Microsoft Hosted Network (MHN)

When using a Microsoft Hosted Network (MHN), navigate to your Cloud PC configuration. After enabling Cross-Region Disaster Recovery or Disaster Recovery Plus, select **Change selection** under Region groups/regions. Alternate regions appear below the recommended region for the selected geography.

##### Azure Network Connection (ANC)

For ANC deployments, virtual networks in alternate regions appear under a separate **Alternate Region** section in the ANC dropdown. Select the appropriate virtual network for your disaster recovery configuration.

Important

Alternate regions are not considered when "**Auto select new region groups**" and "**Auto select new regions**" are selected. They must always be intentionally selected in a Cloud PC Configuration.

##### Considerations

- **No availability zone support**: Alternate regions don't have multiple availability zones, so resources in an alternate region aren't protected from datacenter-level failures within that region. If the underlying datacenter experiences an outage, your backup Cloud PCs in the alternate region could be unavailable until the issue is resolved.
- **Disaster recovery only**: Alternate regions are supported for CRDR and DR+ scenarios only. They are not supported for Cloud PC provisioning.