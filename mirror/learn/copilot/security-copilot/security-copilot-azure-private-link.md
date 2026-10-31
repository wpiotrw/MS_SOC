---
layout: Conceptual
title: Understand why Azure Private Link isn't needed for Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/security-copilot-azure-private-link
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Understand why Azure Private Link isn't needed for Security Copilot
ms.update-cycle: 180-days
ms.date: 2026-01-12T00:00:00.0000000Z
ms.topic: reference
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-overview
ms.custom: copilot-learning-hub
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 6e8a9a4f-b169-7efd-6615-f78c72dc2515
document_version_independent_id: 6e8a9a4f-b169-7efd-6615-f78c72dc2515
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/security-copilot-azure-private-link.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: security-copilot-azure-private-link
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/security-copilot-azure-private-link.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/16cd61cd-9ecf-429b-b494-91576c41f8e4
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/c4bdb33a-5524-4b66-b162-03f5621d7902
platformId: 2ff1d612-993f-8eb2-4a98-489a67b0abc0
---

# Understand why Azure Private Link isn't needed for Security Copilot | Microsoft Learn

Security Copilot is a multitenant, cloud-native SaaS solution. Unlike single-tenant services that benefit from Azure Private Link’s network isolation, Copilot is designed to operate securely over public endpoints. It can't be deployed into a customer’s private network or virtual network, and Private Link isn't supported or required.

## Secure by design architecture

- Security Copilot achieves the goals of Private Link secure, isolated data flows through its architecture:
- **Encrypted Communications**: All traffic is secured with TLS 1.2+ encryption, ensuring confidentiality and integrity across public endpoints.
- **Identity-Based Access Control**: Microsoft Entra authentication and role-based permissions enforce strict tenant-level isolation. Every request is authenticated and authorized.
- **Microsoft Backbone Routing**: Service-to-service communication (for example, with Microsoft Sentinel or Defender) occurs over Microsoft’s internal cloud network, not the public internet. This ensures data stays within Microsoft’s trusted infrastructure.
- **No Inbound Exposure**: Customers don't need to expose internal systems. For plugin integrations, outbound calls from Copilot can be restricted to known IP ranges, maintaining Zero Trust principles.

## Compliance and data protection

Security Copilot complies with Microsoft’s enterprise-grade security and privacy standards:

- **Encryption at Rest and in Transit**: All customer data is protected using AES-256 encryption at rest and TLS 1.2+ in transit, ensuring confidentiality and integrity throughout the data lifecycle.
- **Tenant and Region Isolation**: Data is stored within the customer’s home region and logically isolated by tenant. This guarantees that no data is commingled across organizations, supporting regulatory and operational boundaries.
- **No Data Shared with OpenAI**: Although Security Copilot leverages AI models, customer data isn't sent to OpenAI or external providers. All model processing occurs entirely within Microsoft’s compliance boundary, using infrastructure managed and secured by Microsoft.
- **Compliance Frameworks**: Security Copilot aligns with Microsoft’s broader compliance commitments, including SOC 2, ISO 27001, and GDPR. Customers can apply their own governance policies-such as retention, eDiscovery, and access controls through integrations with Microsoft Purview.

This architecture ensures that even without Azure Private Link, Security Copilot meets the security and compliance expectations of regulated and security-conscious organizations.

## Understand why Private Link isn’t needed

Implementing Private Link in a multitenant SaaS would require managing thousands of private endpoints-an operationally unscalable model. Moreover, most users access Copilot from varied locations, making network-level isolation less relevant than application-layer security. Copilot’s design already meets the intent of Private Link through secure defaults and cloud-native protections.

## Summary

Security Copilot achieves the goals of Private Link secure, isolated data flows through its architecture. For technical customers, this means strong security without the need for network tunneling or endpoint management.