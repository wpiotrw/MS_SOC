---
layout: Conceptual
title: Microsoft Purview Information Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-protection
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-26T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-information-protection
search.appverid:
- MOE150
- MET150
ms.collection:
- m365solution-mip
- m365initiative-compliance
- highpri
recommendations: false
description: Implement Microsoft Purview Information Protection capabilities to help you protect sensitive information wherever it lives or travels.
locale: en-us
document_id: 8b3be5f5-ddd6-1441-6e5b-cb673521192f
document_version_independent_id: 8b3be5f5-ddd6-1441-6e5b-cb673521192f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-protection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f4c82bee-e8ff-749e-8cc8-ae4113d6e0c1
---

# Microsoft Purview Information Protection | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Implement capabilities from **Microsoft Purview Information Protection** (formerly Microsoft Information Protection) to help you discover, classify, and protect sensitive information wherever it lives or travels.

These information protection capabilities give you the tools to know your data, protect your data, and prevent data loss.

![Image of how Microsoft Purview Information Protection helps you discover, classify, and protect sensitive data.](media/powered-by-intelligent-platform.png)

Use the following sections to learn more about the available capabilities and how to get started with each one. However, if you're looking for a guided deployment, see [Deploy an information protection solution with Microsoft Purview](information-protection-solution).

For information about governing your data for compliance or regulatory requirements, see [Govern your data with Microsoft Purview](manage-data-governance).

## Know your data

To understand your data landscape and identify sensitive data across your hybrid environment, use the following capabilities:

| Capability | What problems does it solve? | Get started |
| --- | --- | --- |
| [Sensitive information types](sit-sensitive-information-type-learn-about) | Identifies sensitive data by using built-in or custom regular expressions or a function. Corroborative evidence includes keywords, confidence levels, and proximity. | [Customize a built-in sensitive information type](sit-customize-a-built-in-sensitive-information-type) |
| [Trainable classifiers](trainable-classifiers-learn-about) | Identifies sensitive data by using examples of the data you're interested in rather than identifying elements in the item (pattern matching). You can use built-in classifiers or train a classifier with your own content. | [Get started with trainable classifiers](trainable-classifiers-get-started-with) |
| [Data classification](data-classification-overview) | A graphical identification of items in your organization that have a sensitivity label, a retention label, or have been classified. You can also use this information to gain insights into the actions that your users are taking on these items. | [Get started with content explorer](data-classification-content-explorer)<br>[Get started with activity explorer](data-classification-activity-explorer) |

## Protect your data

To apply flexible protection actions that include encryption, access restrictions, and visual markings, use the following capabilities:

| Capability | What problems does it solve? | Get started |
| --- | --- | --- |
| [Sensitivity labels](sensitivity-labels) | A single labeling solution across apps, services, and devices to protect your data as it travels inside and outside your organization.  Example scenarios: - [Manage sensitivity labels for Office apps](sensitivity-labels-office-apps)- [Encrypt documents and emails](encryption-sensitivity-labels)- [Protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings) For a comprehensive list of supported scenarios for sensitivity labels, see the Get started documentation. | [Get started with sensitivity labels](get-started-with-sensitivity-labels) |
| [Microsoft Purview Information Protection client](https://www.microsoft.com/download/details.aspx?id=53018) | For Windows computers, extends labeling to File Explorer and PowerShell | [Extend sensitivity labeling on Windows](information-protection-client) |
| [Double Key Encryption](double-key-encryption) | Under all circumstances, only your organization can ever decrypt protected content or for regulatory requirements, you must hold encryption keys within a geographical boundary. | [Deploy Double Key Encryption](double-key-encryption-setup) |
| [Message Encryption](ome) | Encrypts email messages and attached documents that are sent to any user on any device, so only authorized recipients can read emailed information.  Example scenario: [Revoke email encrypted by Advanced Message Encryption](revoke-ome-encrypted-mail) | [Set up Message Encryption](set-up-new-message-encryption-capabilities) |
| [Service encryption with Customer Key](customer-key-overview) | Protects against viewing of data by unauthorized systems or personnel, and complements BitLocker disk encryption in Microsoft datacenters. | [Set up Customer Key](customer-key-set-up) |
| [SharePoint Information Rights Management (IRM)](set-up-irm-in-sp-admin-center#irm-enable-sharepoint-document-libraries-and-lists) | Protects SharePoint lists and libraries so that when a user checks out a document, the downloaded file is protected so that only authorized people can view and use the file according to policies that you specify. | [Set up Information Rights Management (IRM) in SharePoint admin center](set-up-irm-in-sp-admin-center) |
| [Rights Management connector](/en-us/azure/information-protection/deploy-rms-connector) | Protection-only for existing on-premises deployments that use Exchange or SharePoint Server, or file servers that run Windows Server and File Classification Infrastructure (FCI). | [Steps to deploy the RMS connector](/en-us/azure/information-protection/deploy-rms-connector#steps-to-deploy-the-rms-connector) |
| [Information protection scanner](deploy-scanner) | Discovers, labels, and protects sensitive information that resides in data stores that are on premises. | [Configuring and installing the information protection scanner](deploy-scanner-configure-install) |
| [Microsoft Defender for Cloud Apps](/en-us/cloud-app-security/what-is-cloud-app-security) | Discovers, labels, and protects sensitive information that resides in data stores that are in the cloud. | [Discover, classify, label, and protect regulated and sensitive data stored in the cloud](/en-us/cloud-app-security/best-practices#discover-classify-label-and-protect-regulated-and-sensitive-data-stored-in-the-cloud) |
| [Microsoft Purview Data Map](data-map) | Identifies sensitive data and applies automatic labeling to content in Microsoft Purview Data Map assets. These include files in storage such as Azure Data Lake and Azure Files, and schematized data such as columns in Azure SQL DB and Azure Cosmos DB. | [Labeling in Microsoft Purview Data Map](data-map-sensitivity-labels) |
| [Microsoft Information Protection SDK](/en-us/information-protection/develop/overview#microsoft-information-protection-sdk) | Extends sensitivity labels to third-party apps and services.  Example scenario: [Set and get a sensitivity label (C++)](/en-us/information-protection/develop/quick-file-set-get-label-cpp) | [Microsoft Information Protection (MIP) SDK setup and configuration](/en-us/information-protection/develop/setup-configure-mip) |

## Prevent data loss

To help prevent accidental oversharing of sensitive information, use the following capabilities:

| Capability | What problems does it solve? | Get started |
| --- | --- | --- |
| [Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) | Helps prevent unintentional sharing of sensitive items. | [Learn about data loss prevention](dlp-learn-about-dlp) |
| [Endpoint data loss prevention](endpoint-dlp-learn-about) | Extends DLP capabilities to items that are used and shared on Windows 10 computers. | [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started) |
| [Microsoft Purview extension for Chrome](dlp-chrome-learn-about) | Extends DLP capabilities to the Chrome browser | [Get started with the Microsoft Purview extension for Chrome](dlp-chrome-get-started) |
| [Microsoft Purview data loss prevention on-premises repositories](dlp-on-premises-scanner-learn) | Extends DLP monitoring of file activities and protective actions for those files to on-premises file shares and SharePoint folders and document libraries. | [Get started with Microsoft Purview data loss prevention on-premises repositories](dlp-on-premises-scanner-get-started) |
| [Protect sensitive information in Microsoft Teams chat and channel messages](dlp-microsoft-teams) | Extends some DLP functionality to Teams chat and channel messages | [Learn about the default data loss prevention policy in Microsoft Teams](dlp-teams-default-policy) |

## Licensing requirements

License requirements to protect your sensitive data depend on the scenarios and features you use. Rather than set licensing requirements for each capability listed on this page, for more information, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) and the related [PDF download](https://go.microsoft.com/fwlink/?linkid=2139145) for feature-level licensing requirements.