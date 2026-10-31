---
layout: Conceptual
title: Privacy and data in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/privacy-personal-data
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about privacy and data in Windows 365.
keywords: 
author: ErikjeMS
ms.author: shupadhyaya
manager: dougeby
ms.date: 2024-10-02T00:00:00.0000000Z
ms.topic: concept-article
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: tnevins1, pratikshah
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
- essentials-privacy
locale: en-us
document_id: c367344e-34a2-9f45-5ad8-fb9312144138
document_version_independent_id: c367344e-34a2-9f45-5ad8-fb9312144138
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/privacy-personal-data.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/privacy-personal-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/privacy-personal-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: d3bb27e8-025b-e456-3247-30c8ea66bfce
---

# Privacy and data in Windows 365 | Microsoft Learn

Windows 365 is a cloud-based service that lets you provision and manage Cloud PC for your users. You manage the Cloud PCs with the rest of your devices by using Microsoft Intune (Windows 365 Enterprise) or a self-serviced experience (Windows 365 Business). This documentation provides details on data platform and privacy compliance for Windows 365. Unless otherwise specified, the term Windows 365 in this document refers to both Windows 365 Enterprise and the Windows 365 Business. Where the details below differ, each product is called out individually.

## Windows 365 data sources and purpose

Windows 365 provides its service to customers by gathering and using data from the sources listed below. These sources provide a comprehensive view of the devices that Windows 365 manages.

- [Microsoft Windows Enterprise](/en-us/windows/resources/) - for managing the device setup experience, managing connections to other services, and operational support for IT pros.
- [Microsoft Intune product family](/en-us/mem/endpoint-manager-overview) – for device and app management, data security, and device configurations.
- [Endpoint analytics](/en-us/intune/endpoint-analytics) – part of the Microsoft Intune product family, specifically for analytical insights about device and app usage.
- [Microsoft 365 apps for enterprise](https://www.microsoft.com/microsoft-365/enterprise/compare-office-365-plans?rtc=1) – for management of Microsoft 365 Apps.

To protect and maintain enrolled devices, Windows 365 processes and copies data from online services and data pipelines configured by the customer to Windows 365. After data is integrated from these services into Windows 365, the [Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all) and [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement) applicable to Windows 365 also applies to the data. Windows 365 ensures appropriate data confidentiality, security, and resilience. Windows 365 employs extra internal privacy and security measures to ensure proper handling of personal data.

## Windows 365 data storage

Depending on a tenant's region and preference, Windows 365 stores its customer content in Azure regions in North America, Europe, or Asia Pacific. Cloud PC virtual disk, customer content, data and storage associated with the Cloud PC lives in the Azure region that the Cloud PC is [provisioned](provisioning) in. For Windows 365 Enterprise, the region is defined in the Microsoft hosted network or [Azure network connection](azure-network-connections) (ANC) settings within the Cloud PC's associated provisioning policy. Windows 365 Business stores customer data in the Azure region of the Cloud PC itself.

To manage the Cloud PC, certain data relating to the Cloud PC (like the machine’s name, diagnostic data, and service-generated data) is stored in Azure data centers in North America, Europe, or Asia Pacific, as defined by the tenant's location. This storage is mapped based on Microsoft Online tenant's country/region to the nearest Azure region.

Other customer data, diagnostic data, or service-generated data may be collected by [Azure Virtual Desktop](/en-us/azure/virtual-desktop/data-locations) or [Intune](/en-us/mem/intune/protect/privacy-personal-data) because Windows 365 depends on these services.

For more information on where your data is located, see:

- [Microsoft Entra ID - Where is your data located?](https://msit.powerbi.com/view?r=eyJrIjoiODdjOWViZDctMWRhZS00ODUzLWI4MmQtNWM5NjBkZTBkNjFlIiwidCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsImMiOjV9)
- [Data locations for Azure Virtual Desktop](/en-us/azure/virtual-desktop/data-locations)
- [Windows 365 supported regions](planning-guide#objective-geographical-regions)
- [Where your Microsoft 365 customer data is stored](/en-us/microsoft-365/enterprise/o365-data-locations)

### How long is customer data and customer content stored?

Windows 365 treats both the Cloud PC disk and the data on the VM itself as customer content.

When a user is removed from Windows 365, Windows 365 keeps non-alert personal data for a maximum of 90 days. In passive scenarios, data is kept for a minimum of 90 days and a maximum of 180 days. To access customer data saved in a passive scenario, contact support. For security purposes, alert data collected by Microsoft Defender for Endpoint is stored for [180 days if the customer uses Microsoft Defender for Endpoint](/en-us/microsoft-365/security/defender-endpoint/data-storage-privacy#what-data-does-microsoft-defender-atp-collect).

For more information on data retention, see [Data retention, deletion, and destruction in Microsoft 365](/en-us/compliance/assurance/assurance-data-retention-deletion-and-destruction-overview).

Windows 365 defaults to Microsoft Intune’s standard practice to [audit, export, or delete personal data](/en-us/mem/intune/protect/privacy-data-audit-export-delete).

Personal data is processed in the audited compliance boundary of the Intune service under the technical security measures assured through [Microsoft Online Services Terms](https://www.microsoft.com/licensing/docs).

For more information about individual data retention and storage policies of all dependent service, see:

- [Where your Microsoft 365 customer data is stored](/en-us/microsoft-365/enterprise/o365-data-locations)
- [Data collection in Intune](/en-us/mem/intune/protect/privacy-data-collect)
- [Data storage and processing in Intune](/en-us/mem/intune/protect/privacy-data-store-process)

## Isolation and access control

Each internal customer data subscription in Windows 365 Enterprise contains Azure Virtual Desktop (AVD) metadata, Cloud PCs, and Storage from multiple tenants. Each VM is connected to a single virtual network interface card (NIC). During provisioning of the Cloud PC, that NIC is attached to a single virtual network in a customer's Azure subscription. The virtual network is defined by the tenant administrator. Every Cloud PC is assigned to a single user by using the AVD connection brokering layer. The access control list (ACL) for the AVD layer is authenticated by Microsoft Entra ID at the tenant and user level. Network access to and from a Cloud PC in Windows 365 is at the control and discretion of each tenant administrator. So, Cloud PCs in tenant A can't be accessed by users in tenant B, unless the tenant A administrator chooses to provide connectivity outside Windows 365 and AVD at the network layer in their own subscription.

For Windows 365 Business, one or more dedicated virtual networks are created in a tenant. The service automatically creates more networks as needed and doesn't guarantee that all Windows 365 Business Cloud PCs in the same tenant will have network connectivity to each other.

All the isolation described above happens on a per user, per Cloud PC basis, since Windows 365 doesn't support multi-user scenarios.

For a full description of Windows 365 architecture, see [Windows 365 architecture](architecture). For more information on isolation in Microsoft 365, see [Isolation and Access Control in Microsoft 365](/en-us/microsoft-365/enterprise/microsoft-365-isolation-in-microsoft-365). For more on Access Management in Microsoft 365, refer to [Identity and Access Management - Microsoft Service Assurance](/en-us/compliance/assurance/assurance-identity-and-access-management).

## Compliance and legal

Audit reports for Windows 365 will be available for download at the [Microsoft Service Trust Portal](https://aka.ms/stp) when they're completed. The Microsoft Service Trust Portal serves as a central repository for Microsoft Enterprise Online Services.

**Microsoft’s privacy notice to end users of products provided by organizational customers** - The [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement) notifies end users that when they sign in to Microsoft products with a work account, a) their organization can control and administer their account (including controlling privacy-related settings) and access and process their data, and b) Microsoft may collect and process the data to provide the service to the organization and end users.