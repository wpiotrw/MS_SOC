---
layout: Conceptual
title: Compliance in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/compliance-overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
author: ErikjeMS
ms.author: tnevins1
manager: dougeby
audience: ITPro
ms.topic: concept-article
ms.service: windows-365
ms.collection:
- tier1
- essentials-compliance
ms.localizationpriority: medium
description: Learn about compliance certifications, dependencies, and features in Windows 365 supporting data protection and regulatory requirements.
ms.date: 2024-12-09T00:00:00.0000000Z
locale: en-us
document_id: c80cbbab-6726-ef7f-ca9a-bbd8e85a317b
document_version_independent_id: c80cbbab-6726-ef7f-ca9a-bbd8e85a317b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/compliance-overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/compliance-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 2bb8c771-8745-f08f-955a-ea26e28aadee
---

# Compliance in Windows 365 | Microsoft Learn

Windows 365 supports compliance features to help organizations meet national, regional, and industry-specific regulations. Windows 365 align with Microsoft's commitment to data protection, privacy, and compliance, offering tools to help secure and manage data effectively.

## Shared responsibility model

Microsoft ensures that Windows 365 complies with various industry standards and regulatory frameworks. However, customers are responsible for implementing their data protection and compliance strategies to align with their specific organizational requirements.

## Compliance certifications

Windows 365 are covered under several compliance certifications and regulatory standards. The following table provides a sample of the key certifications that are covered:

| Certification or Standard | Description | Applicability |
| --- | --- | --- |
| [GDPR](/en-us/compliance/regulatory/gdpr) | EU General Data Protection Regulation for data privacy | European Union |
| [ISO 27001](/en-us/compliance/regulatory/offering-iso-27001) | International standard for information security management | Global |
| [HIPAA](/en-us/compliance/regulatory/offering-hipaa-hitech) | U.S. Health Insurance Portability and Accountability Act | United States |

Note

Windows 365 helps your organization meet regulatory compliance standards. Windows 365 supports additional certifications, including ISO/IEC 27001, [ISO 22301](/en-us/compliance/regulatory/offering-iso-22301), [ISO/IEC 27017](/en-us/compliance/regulatory/offering-iso-27017), [ISO/IEC 27018](/en-us/compliance/regulatory/offering-iso-27018), [ISO/IEC 27701](/en-us/compliance/regulatory/offering-iso-27701), SOC 2 Type 2, FedRAMP, HIPAA, and HITRUST.

For additional certifications, visit [Microsoft Compliance Offerings](/en-us/compliance/regulatory/offering-home).

## Compliance dependencies

Windows 365 leverages other Microsoft services for compliance, including:

- [Microsoft Purview](/en-us/purview/purview): A suite of data governance and compliance tools.
- [Microsoft Entra ID](/en-us/entra/fundamentals/whatis): Identity and access management, formerly known as Azure Active Directory (Azure AD).
- [Microsoft Purview Compliance Manager](/en-us/purview/compliance-manager): Tools for managing compliance across your organization.
- [Microsoft Intune](/en-us/mem): Enforces device compliance and Conditional Access policies to protect access to Windows 365 Cloud PCs.

## Microsoft Intune capabilities for compliance

Microsoft Intune helps enforce compliance policies and protect organizational data specifically for Windows 365:

- **Conditional Access**: Ensures only compliant devices running Windows 365 can access sensitive data. See [Conditional Access](/en-us/mem/intune/protect/conditional-access).
- **Device Compliance Enforcement**: Enforces device compliance policies to meet organizational security requirements. See [Device Compliance Policies](/en-us/mem/intune/protect/device-compliance-get-started).

For more information about Intune compliance capabilities, visit the [Microsoft Intune documentation](/en-us/mem).

## Data location and encryption

Windows 365 supports compliance with data residency requirements by supporting Microsoft Cloud's regional and global data storage policies. These policies include:

- Data location: Data is stored in Microsoft-managed data centers. For more information, see [Windows 365 data storage](enterprise/privacy-personal-data#windows-365-data-storage).
- Encryption: Data is encrypted at rest and in transit. For more information, see [Data encryption in Windows 365](enterprise/encryption).

## Compliance features

Windows 365 includes several compliance features that help organizations meet regulatory requirements, manage data lifecycles, and protect sensitive information. These features are designed to ensure your organization can effectively monitor, classify, and safeguard its data while maintaining compliance with industry standards.

### Data lifecycle management

Windows 365 supports data lifecycle management through retention policies and labels. These features help organizations retain or delete data based on compliance requirements. For setup instructions, see [How long is customer data and customer content stored?](enterprise/privacy-personal-data#how-long-is-customer-data-and-customer-content-stored)

### Auditing and reporting

Microsoft Purview supports auditing and reporting for Windows 365. IT administrators can monitor data usage and ensure adherence to organizational compliance policies. For more information, visit the [Microsoft Purview Customer Key for Windows 365 Cloud PCs](enterprise/purview-customer-key).

### Privacy controls

Windows 365 includes privacy controls to manage data collection, storage, and sharing:

For details about privacy, see [Privacy, customer data, and customer content in Windows 365](enterprise/privacy-personal-data).