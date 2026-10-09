---
layout: Conceptual
title: Set up Microsoft Purview Customer Key for Windows 365 Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/purview-customer-key
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to set up Microsoft Purview Customer Key for Windows 365 Cloud PCs.
keywords: 
author: ErikjeMS
ms.author: ryclar
manager: dougeby
ms.date: 2026-02-19T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: ryclark
ms.suite: ems
search.appverid: 
ms.custom: intune-azure
ms.collection:
- M365-identity-device-management
- tier1
- essentials-security
locale: en-us
document_id: 9ae8138a-6ea2-d09d-a57a-3451a41050bb
document_version_independent_id: 9ae8138a-6ea2-d09d-a57a-3451a41050bb
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/purview-customer-key.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/purview-customer-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/purview-customer-key.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 58d8a962-a2b8-694a-2f2b-70ca5395a72a
---

# Set up Microsoft Purview Customer Key for Windows 365 Cloud PCs | Microsoft Learn

[Microsoft Purview Customer Key](/en-us/purview/customer-key-overview) is a security feature that lets you add an extra layer of compliance to your data within Microsoft 365 services.

When you use Customer Key with Windows 365 Cloud PCs:

- Your Cloud PC disks, snapshots, and images are encrypted at rest with customer-managed keys instead of Microsoft-managed keys.
- These keys are supplied by you and managed using Azure Key Vault.
- Microsoft manages all other keys, supporting a secure and controlled environment.

You can also [set up Customer Key with managed HSM](/en-us/purview/customer-key-managedhsm#set-up-customer-key-with-managed-hsm).

## Set up Customer Keys for your Windows 365 Cloud PCs

1. [Set up Customer Key](/en-us/purview/customer-key-set-up) as explained in the [Microsoft Purview Customer Key documentation](/en-us/purview/customer-key-overview).
2. [Create a data encryption policy for use with multiple workloads for all tenant users](/en-us/purview/customer-key-manage#create-a-dep-for-use-with-multiple-workloads-for-all-tenant-users). This step includes [assigning a multi-workload policy](/en-us/purview/customer-key-manage#assign-multi-workload-policy). After completing this step, it takes 3-4 hours to update your Intune admin center to include the **Configure** button.
3. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) &gt; **Tenant administration** &gt; **Cloud PC encryption type** &gt; **Configure**.

    ![Screenshot of configure button.](media/purview-customer-key/configure.png)
4. Under **Configure encryption type**, select **Microsoft Purview Customer Key** &gt; **Encrypt existing Cloud PCs**.

    ![Screenshot of Encrypt existing Cloud PCs button.](media/purview-customer-key/encrypt.png)
5. In the confirmation window, select **Encrypt**. A notification states that encrypting started.

Important

Switching encryption types is a deliberate re-encryption operation, not a background transition. After the key change is applied, the Windows 365 backend automatically re-encrypts each Cloud PC's storage and then restarts the Cloud PC. Users will be disconnected during this restart.

Encryption is limited to 20,000 Cloud PCs at a time. You can repeat these steps to encrypt more Cloud PCs.

Encryption can take a long time based on the number of Cloud PCs and the size of the disks. The **Cloud PC encryption type** page is updated with a notification when the encryption is complete.

## Switch to Microsoft-managed keys

You can switch your Cloud PCs from customer-managed keys back to Microsoft-managed (platform-managed) keys at any time.

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) &gt; **Tenant administration** &gt; **Cloud PC encryption type** &gt; **Configure**.
2. Under **Configure encryption type**, select **Microsoft-managed keys** &gt; **Encrypt existing Cloud PCs**.
3. In the confirmation window, select **Encrypt**. A notification states that encrypting started.

Important

Switching encryption types is a deliberate re-encryption operation, not a background transition. After the key change is applied, the Windows 365 backend automatically re-encrypts each Cloud PC's storage and then restarts the Cloud PC. Users will be disconnected during this restart.

Re-encryption is limited to 20,000 Cloud PCs at a time. You can repeat these steps to re-encrypt more Cloud PCs.

Re-encryption can take a long time based on the number of Cloud PCs and the size of the disks. The **Cloud PC encryption type** page is updated with a notification when the re-encryption is complete.