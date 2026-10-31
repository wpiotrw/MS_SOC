---
layout: Conceptual
title: Double Key Encryption (DKE) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/double-key-encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Double Key Encryption helps you to protect highly sensitive data while maintaining control of your key.
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-10-27T00:00:00.0000000Z
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
audience: Admin
ms.reviewer: esaggese
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: 45266846-5305-7de3-1f25-d84ef8b626db
document_version_independent_id: 45266846-5305-7de3-1f25-d84ef8b626db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/double-key-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: double-key-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/double-key-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/e93f3d5f-c77d-4365-a7fb-c9f2234416c7
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/62e8d07a-cc62-4934-b30b-e168a571e51d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 266feb33-cc16-f072-8357-b4bb7d8026bd
---

# Double Key Encryption (DKE) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

> 
> *Applies to: Microsoft Purview Double Key Encryption, [Microsoft Purview](https://www.microsoft.com/microsoft-365/business/compliance-management), [Microsoft Purview Information Protection](https://www.microsoft.com/microsoft-365/business/compliance-management)*
> 
> *Service description for: [Microsoft Purview](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)*

Double Key Encryption (DKE) enables you to protect your highly sensitive data to meet specialized requirements. DKE lets you maintain control of your encryption keys. It uses two keys to protect data; one key in your control and a second key you store securely in Microsoft Azure. You maintain control of one of your keys using the Double Key Encryption service. Viewing data protected with Double Key Encryption requires access to both keys.

DKE helps you meet regulatory requirements across several regulations and standards such as the General Data Protection Regulation (GDPR), the Health Insurance Portability and Accountability Act (HIPAA), the Gramm-Leach-Bliley Act (GLBA), Russia’s data localization law – Federal Law No. 242-FZ, Australia’s Federal Privacy Act 1988, and New Zealand’s Privacy Act 1993.

After you set up the DKE service and your keys, you apply protection to your highly sensitive content by using [sensitivity labels](sensitivity-labels).

## Supported deployment scenarios

DKE supports several different configurations including both cloud and on-premises deployments. These deployments help to ensure that encrypted data remains opaque wherever you store it.

You can host the Double Key Encryption service used to request your key in a location of your choice (on-premises key management server or in the cloud). You maintain the service as you would any other application. Double Key Encryption lets you control access to the Double Key Encryption service. You can store your highly sensitive data on-premises or move it to the cloud. Double Key Encryption gives you the control to store your data and key in the same geographical location.

For more information about the default, cloud-based tenant root keys, see [Managing the root key for your Azure Rights Management service](rights-management-tenant-key).

## When your organization should adopt DKE

DKE isn't for every organization, nor for all of your data. Let's say a typical organizational data landscape has the following structure:

- Nonsensitive data (about 80% of data): Most of an organization’s data falls into this category. There are no issues or concerns with moving this data to the cloud today. Moving such data to the cloud can be beneficial and the organization can use the security built into the cloud.
- Sensitive (about 15% of data): Sensitive data needs to be protected. The organization expects the cloud service provider to provide security while enhancing productivity for this category of data so that they can meet compliance regulations. You want to ensure this data is labeled correctly using Microsoft Purview Information Protection and is protected with access control and retention and audit policies.
- Highly sensitive (about 5% of data): This set is the organization’s crown jewels and needs to be heavily guarded. The organization doesn't want anyone to have access to such data. This category of data can also have regulatory requirements to have the keys in the same geographical region as the data. The keys might also need to be under the organization’s strict custody. This content has the highest classification in your organization ("Top Secret") and access is restricted to just a few people. Highly sensitive data is what malicious users are after. Loss of this data can damage the organization's reputation and break trust with their customers.

As mentioned, Double Key Encryption is intended for your most sensitive data that is subject to the strictest protection requirements. You should do due diligence in identifying the right data to cover with this solution before you deploy. In some cases, you might need to narrow your scope and use other solutions. For example, for most of your data, consider Microsoft Purview Information Protection with Microsoft-managed keys or bring your own key (BYOK). These solutions are sufficient for documents that aren't subject to enhanced protections and regulatory requirements. Also, these solutions enable you to use the most powerful Microsoft 365 services; services that you can't use with DKE encrypted content. For example:

- Mail flow rules including anti-malware and spam that require visibility into the attachment
- Microsoft Delve
- eDiscovery
- Content search and indexing
- Office Web Apps including coauthoring functionality
- Copilot

DKE encrypted data isn't accessible at rest to Microsoft 365 services including Copilot. While you're using your DKE encrypted data in Office, the data still isn't accessible to Copilot, and you can't use Copilot in apps while you're using DKE encrypted data.

External applications or services that aren't integrated with DKE through the Microsoft Information Protection SDK are unable to perform actions on the encrypted data. The Microsoft Information Protection SDK 1.7+ supports Double Key Encryption. Applications that integrate with our SDK can reason over this data with sufficient permissions and integrations in place.

When your DKE encrypted data is in use in an Office app, it might be accessible to other Microsoft 365 services, depending on your Office version:

- In the latest versions of Office, DKE encrypted data in use is also not accessible to Microsoft 365 services. Because this change rolled out at the same time as the separate privacy control for sensitivity labels that prevents sending labeled content to connected experiences for analysis, you can identify the minimum Office versions by using the [capabilities table](sensitivity-labels-versions) and the row **Prevent connected experiences that analyze content**.
- In previous versions of Office, DKE encrypted data in use is accessible to Microsoft 365 services unless you use a policy setting to turn off connected experiences that analyze content. For more information, see [Use policy settings to manage privacy controls for Microsoft 365 Apps for enterprise](/en-us/deployoffice/privacy/manage-privacy-controls#policy-setting-for-connected-experiences-that-analyze-your-content).

Use Microsoft Purview Information Protection capabilities (classification and labeling) to protect most of your sensitive data and only use DKE for your mission-critical data. Double Key Encryption is relevant for sensitive data in highly regulated industries such as financial services and healthcare.

### Sensitivity label features that don't support DKE

Because DKE doesn't use a cloud-based key managed by the Azure Rights Management service, several sensitivity label features can't work with DKE-encrypted content:

- **Co-authoring and AutoSave**

    - Coauthoring and AutoSave aren't supported for Office documents encrypted with DKE. Labels with DKE still display in Office apps, but coauthoring and AutoSave are disabled when the label is applied. For more information, see [Coauthoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring).
- **Files in SharePoint and OneDrive**

    - SharePoint and OneDrive can't process DKE-encrypted files. These files can't be opened in Office for the web, and collaborative features such as coauthoring, eDiscovery, data loss prevention, and search don't work for DKE-encrypted files in these locations. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).
- **Default label for a SharePoint document library**

    - A sensitivity label that uses DKE can't be set as the default sensitivity label for a SharePoint document library. For more information, see [Configure a default sensitivity label for a SharePoint document library](sensitivity-labels-sharepoint-default-label).
- **Loop components and pages**

    - Sensitivity labels configured with DKE aren't supported for Loop components and pages. For more information, see [Sensitivity labels for Loop components and pages](sensitivity-labels-loop).
- **Teams meetings and chat**

    - DKE labels can't be used to protect calendar items, Teams meetings, and chat. Meetings and chat require encryption that uses the Azure Rights Management service. For more information, see [Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings).

If your organizations have any of the following requirements, you can use DKE to help secure your content:

- You have regulatory requirements to hold keys within a geographical boundary.
- All of the keys that you hold for data encryption and decryption are maintained in your data center.

## DKE encryption workflow

This section breaks apart the workflow into separate steps to illustrate how two keys are used to protect an Office document.

### Step 1: Bootstrapping

![A diagram shows step 1 of the encryption workflow for DKE, bootstrapping.](media/dke-encryption-workflow-bootstrap-1.png)

The Microsoft Office client performs startup configuration tasks and sends requests and information to the Azure Rights Management encryption service. This process is also called *bootstrapping*. Tasks include authorizing the user using Microsoft Entra ID, downloading certificates and templates, and so on. Bootstrapping tasks are first-time connection and startup tasks that give the user access to the Azure Rights Management encryption policies.

### Step 2: Collect and cache the public key for the Azure Rights Management service

![A diagram shows step 2 of the encryption workflow for DKE, collect and cache the Azure public key.](media/dke-encryption-workflow-retrieve-azure-key-2.png)

The Office app retrieves the public key from the Azure Key Vault in the encryption service based on the authorized user using Microsoft Entra ID. Once collected, the client caches the key for 30 days by default. Once cached, the client doesn't have to bootstrap to the Azure Rights Management service again until the key expires. As an administrator, you can configure a different caching period for the Azure Rights Management service. You need to set a cache period for this key or accept the 30 day default. Without a cache period, offline publishing doesn't work.

### Step 3: Request the DKE public key

![A diagram shows step 3 of the encryption workflow for DKE, request the DKE public key.](media/dke-encryption-workflow-request-dke-key-3.png)

The Office client requests your other public key from the Double Key Encryption service based on the authorized user using Microsoft Entra ID.

### Step 4: Collect and cache the DKE key

![A diagram shows step 4 of the encryption workflow for DKE, collect and cache the DKE public key.](media/dke-encryption-workflow-retrieve-dke-key-4.png)

The Double Key Encryption service sends this public key to the Office client. The client caches the key in the device for as long you configured it to. Unlike the key from Azure,

- You don't have to set up a cache period for the key hosted by the Double Key Encryption service.
- If you do want to set up a cache period, you can set it up when you deploy the Double Key Encryption service, or after you deploy.

### Step 5: Protect the document with the DKE key

![A diagram shows step 5 of the encryption workflow for DKE, protect the document with the DKE key.](media/dke-encryption-workflow-protect-dke-5.png)

The Microsoft Office client encrypts the part of the metadata **that controls access to the content** using your public key that was retrieved from the Double Key Encryption service.

### Step 6: Protect the document with the Azure key

![A diagram shows step 6 of the encryption workflow for DKE, protect the document with the Azure key.](media/dke-encryption-workflow-protect-azure-6.png)

The Microsoft Office client encrypts **the already encrypted part of the document metadata** with your public key from Azure.

The data is now protected with both keys.

## System and licensing requirements for DKE

This section details server and client system and configuration requirements that must be met before you can successfully deploy DKE in your environment.

### licensing requirements for DKE

For licensing options for Double Key Encryption, see [Microsoft Purview Information Protection Double Key Encryption](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-double-key-encryption) in the Microsoft Purview service description.

### The Azure Rights Management service is required for DKE

DKE works with sensitivity labels and requires encryption with rights management from Microsoft Purview Information Protection.

### DKE labeling requirements for Office apps

Use sensitivity labels built in to Office apps to support DKE in Word, Excel, PowerPoint, and Outlook. For supported versions, see the [capabilities tables](sensitivity-labels-versions) and the row **Double Key Encryption (DKE)**.

### DKE on client computers

Users apply DKE sensitivity labels through these interfaces.

- Sensitivity labeling in Windows Office apps
- Microsoft Purview Information Protection file labeler in Windows File Explorer
- Microsoft Purview Information Protection PowerShell
- Microsoft Purview Information Protection scanner

Install prerequisites on each client computer where you want to protect and consume protected documents.

### Supported environments for storing and viewing DKE-protected content

**Supported applications**. [Microsoft 365 Apps for enterprise](https://www.microsoft.com/microsoft-365/business/microsoft-365-apps-for-enterprise-product) clients on Windows, including Word, Excel, PowerPoint, and Outlook.

**Online content support**. You can store documents and files that are protected with Double Key Encryption online in both SharePoint and OneDrive. You must label and protect documents and files with DKE by supported applications before you upload to these locations. You can share encrypted content by email, but you can't view encrypted documents and files online. Instead, you must view protected content using the supported desktop applications and clients on your local computer.

**Labeling scenarios outside of Office apps**. Apply DKE labels outside of Office apps using the Microsoft Purview Information Protection file labeler in File Explorer right-click options, Microsoft Purview Information Protection PowerShell labeling cmdlets, or the Microsoft Purview Information Protection scanner.

**Viewing DKE-protected content outside of Office apps**. You can use the Microsoft Purview Information Protection Viewer to consume DKE-protected emails and documents such as PDF.

**Encrypt Only and Do Not Forward scenarios**. Encrypt Only and Do Not Forward aren't supported with DKE in Outlook. All other Office applications support user-defined permission labels with DKE.