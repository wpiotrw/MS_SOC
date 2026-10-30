---
layout: Conceptual
title: Overview of managed disk encryption options - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: msmbaldwin
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: mbaldwin
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Compare Azure managed disk encryption options, including server-side encryption, encryption at host, Azure Disk Encryption, and confidential disk encryption.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
ms.subservice: security
ms.custom: references_regions
ai-usage: ai-assisted
locale: en-us
document_id: b964cc95-9074-55f1-c150-f74933aa9222
document_version_independent_id: 90d48cea-1b05-d320-f939-179cd5e6b195
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disk-encryption-overview.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/disk-encryption-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disk-encryption-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/837687b0-8846-4eb2-adb6-2b853e8c70c4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8c797fa2-4419-46e7-a4e3-4c97d0a1f2a0
platformId: 2b56ffa3-95b9-5415-85fb-dfd956635f03
---

# Overview of managed disk encryption options - Azure Virtual Machines | Microsoft Learn

Several encryption types are available for your managed disks, including Azure Disk Encryption (ADE), server-side encryption (SSE), and encryption at host.

- **Azure Disk Storage server-side encryption** (also referred to as encryption at rest or Azure Storage encryption) is always enabled. It automatically encrypts data stored on Azure managed disks (OS and data disks) when it persists data on the storage clusters. When you configure it with a disk encryption set (DES), it also supports customer-managed keys. It doesn't encrypt temp disks or disk caches. For full details, see [Server-side encryption of Azure Disk Storage](disk-encryption).
- **Encryption at host** is a virtual machine option that enhances Azure Disk Storage server-side encryption. This option ensures that all temp disks and disk caches are encrypted at rest and flow encrypted to the storage clusters. For full details, see [Encryption at host - End-to-end encryption for your VM data](disk-encryption#encryption-at-host---end-to-end-encryption-for-your-vm-data).
- **Confidential disk encryption** binds disk encryption keys to the virtual machine's TPM and makes the protected disk content accessible only to the VM. The TPM and VM guest state are always encrypted in attested code by using keys released by a secure protocol that bypasses the hypervisor and host operating system. Confidential OS disk encryption protects the OS disk. You can also enable [confidential temp disk encryption](/en-us/azure/confidential-computing/confidential-vm-overview#confidential-temp-disk-encryption) through an opt-in process. You can use encryption at host for other disks on a confidential VM in addition to [confidential disk encryption](/en-us/azure/confidential-computing/confidential-vm-overview#confidential-os-disk-encryption).
- **Azure Disk Encryption** helps protect and safeguard your data to meet your organizational security and compliance commitments. ADE encrypts the OS and data disks of Azure virtual machines (VMs) inside your VMs by using the [DM-Crypt](https://wikipedia.org/wiki/Dm-crypt) feature of Linux or the [BitLocker](https://wikipedia.org/wiki/BitLocker) feature of Windows. ADE is integrated with Azure Key Vault to help you control and manage the disk encryption keys and secrets, with the option to encrypt by using a key encryption key (KEK). For full details, see [Azure Disk Encryption for Linux VMs](linux/disk-encryption-overview) or [Azure Disk Encryption for Windows VMs](windows/disk-encryption-overview).

    Important

    Azure Disk Encryption is scheduled for retirement on **September 15, 2028**. Until that date, you can continue to use Azure Disk Encryption without disruption. On September 15, 2028, ADE-enabled workloads will continue to run, but encrypted disks will fail to unlock after VM reboots, resulting in service disruption.

    Use [encryption at host](/en-us/azure/virtual-machines/disk-encryption) for new VMs, or consider [Confidential VM sizes with OS disk encryption](/en-us/azure/confidential-computing/confidential-vm-overview#confidential-os-disk-encryption) for confidential computing workloads. All ADE-enabled VMs (including backups) must migrate to encryption at host before the retirement date to avoid service disruption. See [Migrate from Azure Disk Encryption to encryption at host](/en-us/azure/virtual-machines/disk-encryption-migrate) for details.

Encryption is part of a layered approach to security. Use it with other recommendations to secure virtual machines and their disks. For full details, see [Compute security recommendations](/en-us/azure/defender-for-cloud/recommendations-reference-compute) and [Restrict import/export access to managed disks](/en-us/azure/virtual-machines/disks-enable-private-links-for-import-export-portal).

## Comparison

The following table compares Disk Storage SSE, ADE, encryption at host, and confidential disk encryption.

Azure Disk Encryption is scheduled for retirement on **September 15, 2028**. Use [encryption at host](disk-encryption#encryption-at-host---end-to-end-encryption-for-your-vm-data) for new VMs, or consider [Confidential VM sizes with OS disk encryption](/en-us/azure/confidential-computing/confidential-vm-overview#confidential-os-disk-encryption) for confidential computing workloads.

| - | **Azure Disk Storage server-side encryption** | **Encryption at host** | **Azure Disk Encryption** | **Confidential disk encryption (for the OS disk only)** |
| --- | --- | --- | --- | --- |
| Encryption at rest (OS and data disks) | Yes | Yes | Yes | Yes |
| Temp disk encryption | No | Yes, supported only with platform-managed keys | Yes | Yes, [opt-in](/en-us/azure/confidential-computing/confidential-vm-overview#confidential-temp-disk-encryption) |
| Encryption of caches | No | Yes | Yes | Yes |
| Data flows encrypted between compute and storage | No | Yes | Yes | Yes |
| Customer control of keys | Yes, when configured with DES | Yes, when configured with DES | Yes, when configured with KEK | Yes, when configured with DES |
| Hardware security module (HSM) support | Azure Key Vault Premium and Managed HSM | Azure Key Vault Premium and Managed HSM | Azure Key Vault Premium | Azure Key Vault Premium and Managed HSM |
| Does not use your VM's CPU | Yes | Yes | No | No |
| Works for custom images | Yes | Yes | No, doesn't work for custom Linux images | Yes |
| Enhanced key protection | No | No | No | Yes |
| Microsoft Defender for Cloud disk encryption status\* | Unhealthy | Healthy | Healthy | Not applicable |

Important

For confidential disk encryption, Microsoft Defender for Cloud doesn't currently have an applicable recommendation.

\* Microsoft Defender for Cloud has the following disk encryption recommendations:

- [Virtual machines and virtual machine scale sets should have encryption at host enabled](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Ffc4d8e41-e223-45ea-9bf5-eada37891d87) (detects only encryption at host).
- [Virtual machines should encrypt temp disks, caches, and data flows between Compute and Storage resources](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F0961003e-5a0a-4549-abde-af6a37f2724d) (detects only Azure Disk Encryption).
- [Windows virtual machines should enable Azure Disk Encryption or EncryptionAtHost](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2fproviders%2fMicrosoft.Authorization%2fpolicyDefinitions%2f3dc5edcd-002d-444c-b216-e123bbfa37c0) (detects both Azure Disk Encryption and EncryptionAtHost).
- [Linux virtual machines should enable Azure Disk Encryption or EncryptionAtHost](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2fproviders%2fMicrosoft.Authorization%2fpolicyDefinitions%2fca88aadc-6e2b-416c-9de2-5a0f01d1693f) (detects both Azure Disk Encryption and EncryptionAtHost).