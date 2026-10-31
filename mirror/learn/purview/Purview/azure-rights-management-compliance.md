---
layout: Conceptual
title: Compliance & information for the Azure Rights Management service | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/azure-rights-management-compliance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Supporting information that includes legal, compliance, and SLAs for the Azure Rights Management encryption  service from Microsoft Purview Information Protection.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: c5e24708-301a-cd9b-635c-5f188e15414c
document_version_independent_id: c5e24708-301a-cd9b-635c-5f188e15414c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/azure-rights-management-compliance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: azure-rights-management-compliance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/azure-rights-management-compliance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 283db508-8a25-069e-64ad-4c276f566bcd
---

# Compliance & information for the Azure Rights Management service | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The Azure Rights Management service supports other services and also relies on other services. If you’re looking for information that is related to this encryption service but not about how to use the service, check the following resources:

## Suitability for different countries/regions

Given the variability between laws and regulations in different countries/regions, different use cases and scenarios, and the varying requirements between different business sectors, consult your legal adviser to help you answer whether the Azure Rights Management service is suitable for your country/region.

However, some relevant information that can help your legal adviser make a determination:

- The Azure Rights Management service uses AES 256 and AES 128 to encrypt documents. For more information, see [Cryptographic controls, algorithms, and key lengths](rights-management-how-does-it-work#cryptographic-controls-algorithms-and-key-lengths).
- All encryption keys used by the Azure Rights Management service are protected with a customer-specific root key that uses RSA 2048 bits. RSA 1024 bits is also supported for backwards compatibility. For more information, see [Cryptographic controls, algorithms, and key lengths](rights-management-how-does-it-work#cryptographic-controls-algorithms-and-key-lengths).
- Customer-specific root keys are either managed by Microsoft or provisioned by the customer in a nCipher HSM by using "bring your own key" (BYOK). The Azure Rights Management service also supports features for on-premises encryption, for content that cannot be encrypted with a cloud-based key. For more information, see [Managing the root key for your Azure Rights Management service](rights-management-tenant-key).
- The Azure Rights Management service is hosted in regional data centers across the globe. The Azure Rights Management service keys always remain within the region in which the service was originally deployed.
- The Azure Rights Management service doesn't transmit document contents from clients to the Azure Rights Management service. Content encryption and decryption operations are performed in-place in the client device. Or, for service-based rendering, these operations are performed within the service that’s rendering the content. For more information, see [How the Azure Rights Management service works](rights-management-how-does-it-work).

## Legal and privacy

- For Microsoft Azure agreement information: [Microsoft Azure Agreement](https://azure.microsoft.com/support/legal/subscription-agreement/)
- For Microsoft Azure privacy information: [Microsoft Azure Privacy Statement](https://azure.microsoft.com/support/legal/privacy-statement/)

## Security, compliance, and auditing

See the [Security, compliance, and regulatory requirements](/en-us/purview/azure-rights-management-learn-about#security-compliance-and-regulatory-requirements) section in the [Learn about the Azure Rights Management service](azure-rights-management-learn-about) article, for information about specific certifications for the Azure Rights Management service. In addition:

- For external certifications for the Azure Rights Management service: [Microsoft Azure Trust Center](https://azure.microsoft.com/support/trust-center/)
- For FIPS 140 information: [FIPS 140 Validation](/en-us/windows/security/threat-protection/fips-140-validation)

For in-depth technical information about how the encryption technology works, see [How the Azure Rights Management service works: Technical details](rights-management-how-does-it-work).

## Service level agreements (SLAs)

The following service level agreement resources apply to the Azure Rights Management service and its dependencies:

- [SLA for the Azure Rights Management service](https://azure.microsoft.com/support/legal/sla/information-protection/v1_0/)
- [SLA for Microsoft Entra ID](https://azure.microsoft.com/support/legal/sla/active-directory/v1_0/)
- [SLA for Azure Key Vault](https://azure.microsoft.com/support/legal/sla/key-vault/v1_0/)

## Documentation

For related product documentation, see the following resources:

- Microsoft Entra documentation: [Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-whatis)
- Microsoft 365 documentation: [Microsoft 365 for enterprise documentation and resources](/en-us/Office365/Enterprise/)