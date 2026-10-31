---
layout: Conceptual
title: Compare Windows 365 Business and Enterprise | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/business-enterprise-comparison
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: What are the differences between Windows 365 Business and Enterprise?
keywords: 
author: ErikjeMS
ms.author: bgiammona
manager: dougeby
ms.date: 2025-12-11T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: naramkri
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: b618ec4d-f656-7a58-454b-f8e552ef36e3
document_version_independent_id: b618ec4d-f656-7a58-454b-f8e552ef36e3
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/business-enterprise-comparison.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: business-enterprise-comparison
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/business-enterprise-comparison.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c22d028c-74fc-4a73-888d-224bc5e88509
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c450d479-44e5-4a9c-9b93-e6f9b69dd42d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bde49cda-0860-45af-9aef-2992cbefc8c4
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e273b0-a43e-4cc8-9bf9-67d4d6a1e869
platformId: 816efeda-88ef-4b6a-561e-d416605172fb
---

# Compare Windows 365 Business and Enterprise | Microsoft Learn

This article compares two editions: [Windows 365 Business](business/) and [Windows 365 Enterprise](enterprise/).

## General comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Domain Join | Microsoft Entra join without Azure Virtual Network (VNet) support. | Microsoft Entra join without VNet support.Microsoft Entra join with VNet support.Hybrid Microsoft Entra ID with VNet support.For other domain support, see [In development for Windows 365 Enterprise](enterprise/in-development). |

## Purchasing and licensing comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Purchase channels | Web direct, self-service, Cloud Solution Provider (CSP). | Web direct, Enterprise Agreements (EA), CSP. |
| License assignment | Microsoft 365 Admin Center or the Microsoft Entra admin center. | Microsoft 365 Admin Center or the Microsoft Entra portal. |
| Licensing requirements | No licensing pre-requirements to buy and deploy Windows 365 Business. Other features (like device management) can be used if users are licensed for Microsoft Endpoint Management. | Each user must be licensed for Windows 10 or 11 Enterprise (when available), Microsoft Intune, and Microsoft Entra ID P1. |
| Networking costs | Outbound data/month is based on the RAM of the Cloud PC:- 2-GB RAM = 12-GB outbound data- 4-GB or 8-GB RAM = 20-GB outbound data- 16-GB RAM = 40-GB outbound data- 32-GB RAM = 70-GB outbound dataData bandwidth may be restricted when these levels are exceeded. | When providing a network, Networking goes through the customer's Azure VNet and isn't included in the license. [Azure bandwidth pricing](https://azure.microsoft.com/pricing/details/bandwidth/) applies for these network usage costs. If using a Microsoft-hosted network, the same charges (as described in Windows 365 Business networking charges) apply. |
| User limits | Capped to 300 users per tenant. [Commercial Licensing Terms](https://www.microsoft.com/licensing/terms/productoffering/Windows365/MOSA) | No user per tenant. [Commercial Licensing Terms](https://www.microsoft.com/licensing/terms/productoffering/Windows365/MOSA) |

## Administrative comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Provisioning | Provisioning is simplified and uses default configurations.Cloud PCs are automatically provisioned with a standard image after a Cloud PC license is assigned. | Provisioning is configurable and customizable to the needs of the organization.Admins select the network, configure user permissions (local admin or not), and assign the policy to a Microsoft Entra group.Cloud PCs are then provisioned by using standard gallery images or custom images (admin choice). |
| Policy management | Not Supported. | Group Policy Objects (GPO) and Intune MDM are supported. |
| Application deployment | Supported only if you have Intune license. | Supported. |
| Windows updates | Default Windows Update client policies are configured for users. With an Intune license, these settings can be edited. | Can be managed by using Intune. |
| Device management | Device management is limited to assigning and unassigning of Cloud PC licenses in the Microsoft Admin Center. Some device management is possible in Microsoft Intune if you have an Intune license but Cloud PCs won't be visible in the Windows 365 page. | Microsoft Intune admin center options, including image management, link and access on-premises resources, granular targeting of policies, resizing Cloud PCs, other user experience settings, and all the policy-based management options available to physical devices. |
| Monitoring | Not supported. | Endpoint Analytics reporting and monitoring, service health, and operational health alerts. |
| Troubleshooting | Not supported | Microsoft Intune troubleshooting including the Troubleshooting page, device management actions, and reprovisioning of Cloud PCs to their initial state. |
| Partner/programmatic access | Not supported | Partners can manage Cloud PCs through Microsoft 365 Lighthouse or restful web APIs (Graph) to support Managed Service Provider tooling for up to 300 seats. |
| Universal Print | Not supported. | Supported. |

## End user comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Management | Users can [restart, reset, rename, and troubleshoot](end-user-access-cloud-pc#user-actions) their Cloud PCs on the Windows 365 homepage. | Users can [restart, rename, and troubleshoot](end-user-access-cloud-pc) their Cloud PCs on the Windows 365 homepage. |
| Role | By default, each user is a Standard User on their Cloud PC. To grant Local Administrator permissions to a specific user on a Cloud PC, see [Remote management actions](business/remotely-manage-business-cloud-pcs#remote-management-actions). To grant Local Administrator permissions for Cloud PCs that you create in the future, see [Change organizational default settings](business/change-organization-default-settings). | By default, each user is assigned a standard user role on their Cloud PC. This role can be changed by the admin in the Microsoft Intune admin center. |
| Access | Users can access their Cloud PC at windows365.microsoft.com or by using Microsoft Remote Desktop or the Windows app. | Users can access their Cloud PC at windows.cloud.microsoft or by using Microsoft Remote Desktop or the Windows app. |
| Platform | Any platform that supports [Microsoft Remote Desktop clients](/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) or the Windows app. | Any platform that supports [Microsoft Remote Desktop clients](/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) or the Windows app. |

## Security comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Conditional Access | Conditional Access policies can be deployed only by using Microsoft Entra ID with a Microsoft Entra ID P1 license. | Conditional Access policies can be deployed by using the Microsoft Intune admin center or Microsoft Entra ID. |
| [Per-user multi-factor authentication (MFA)](/en-us/azure/active-directory/authentication/howto-mfa-userstates) | Only MFA using [Microsoft Entra Conditional Access](/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) is supported. Legacy per-user MFA isn't supported. | Legacy per-user MFA is supported for user connections to Microsoft Entra hybrid joined Cloud PCs. It's not supported for user connections to Microsoft Entra joined Cloud PCs. |
| Security baselines | Not supported. | Dedicated Security Baselines can be edited and deployed by using Microsoft Intune. |
| Microsoft Defender for Endpoint | Supported if the customer separately has the requisite E5 license. | Integration with Defender for Endpoint. If the customer has an E5 license, all Cloud PCs will respond to Defender for Endpoint policies and show up in MDE dashboards. |

## Support comparisons

| Capability | Windows 365 Business | Windows 365 Enterprise |
| --- | --- | --- |
| Support channels | Support tickets can be filed through the Microsoft 365 Admin Center. | Support tickets can be filed through Microsoft Intune (recommended) and the Microsoft 365 Admin Center. |