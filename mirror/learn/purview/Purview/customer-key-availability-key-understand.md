---
layout: Conceptual
title: Learn about the availability key for Customer Key - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/customer-key-availability-key-understand
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.reviewer: chrwarren
ms.date: 2025-10-09T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Learn about the availability key used to recover lost customer keys.
locale: en-us
document_id: b0e733fc-fe67-436a-c465-d1f8a5e58a1a
document_version_independent_id: b0e733fc-fe67-436a-c465-d1f8a5e58a1a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/customer-key-availability-key-understand.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-key-availability-key-understand
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/customer-key-availability-key-understand.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 6996df8f-387f-845a-9eef-5dcef1104058
---

# Learn about the availability key for Customer Key - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The availability key is a root key automatically generated when you create a data encryption policy (DEP). Microsoft 365 stores and protects this key. Unlike the keys you manage in Azure Key Vault, you can't directly access it. Only Microsoft 365 service code can use it programmatically.

Its primary purpose is recovery from unexpected loss of your root keys. If you lose control of your keys, contact Microsoft Support to recover data using the availability key and migrate to a new DEP.

The availability key differs from Azure Key Vault keys in three ways:

- **Recovery**: Provides a break-glass option if both Azure Key Vault keys are lost
- **Defense in depth**: Logical separation of control and storage prevents total loss from a single failure
- **High availability**: Supports temporary Azure Key Vault outages for Exchange/Multi-Workload (SharePoint/OneDrive only uses it during explicit recovery requests)

You have sole authority to disable or destroy the availability key when leaving the service. For more information, see the [Microsoft Trust Center](https://www.microsoft.com/trustcenter/Privacy/govt-requests-for-data).

## Availability key uses

The availability key supports recovery if an attacker gains control of your key vault or mismanagement causes key loss. All services share these behaviors:

- **Recovery**: Decrypts data so you can re-encrypt with a new DEP
- **Programmatic only**: No direct admin access; only service code can use it
- **Not a substitute**: Your two Customer Keys remain the primary encryption roots

**Service-specific behavior:**

# [Exchange and Multi-workload](#tab/exchange-uses)
In addition to supporting recovery, the availability key ensures continued access during short Azure Key Vault outages for background operations such as anti-malware scans, eDiscovery, DLP, mailbox migrations, and indexing.

**Fallback logic**: If unwrap fails with one Customer Key, the service tries the second. If both fail with system errors, it falls back to the availability key. Access denied errors don't trigger fallback for user actions.

# [SharePoint and OneDrive](#tab/spo-uses)
Not used for transient availability. Only used when you explicitly request recovery through Microsoft Support.

---

## Availability key security

Microsoft protects availability keys in access-controlled internal secret stores. Customers can't directly access the availability key. You can only roll keys you manage in Azure Key Vault. All operations occur through automated service code. For more information, see [Roll or rotate a Customer Key or an availability key](customer-key-availability-key-roll).

### Availability key secret stores

Management operations require privilege escalation through Lockbox with justification, manager approval, and automatic time-bound revocation.

| Workload | Storage location |
| --- | --- |
| **Exchange and Multi-workload** | Exchange Active Directory secret store in tenant-specific containers |
| **SharePoint and OneDrive** | Internal secret store with SQL Database back end; keys wrapped with AES-256/HMAC and RSA-2048 certificates |

### Defense-in-depth

Microsoft uses defense-in-depth to protect availability keys:

- **Application isolation**: Only Microsoft 365 service code can use keys for encryption/decryption
- **Logical separation**: Customer Keys, availability keys, and customer data are stored in isolated locations
- **Access controls**: Engineers have no direct access to secret stores (see [Administrative Access Controls](/en-us/compliance/assurance/assurance-administrative-access-controls-overview))
- **Technical controls**: Block interactive sign-in to privileged service accounts
- **Monitoring**: Continuous intrusion detection, centralized logging, and alerts for unauthorized access attempts or baseline deviations

## Use the availability key to recover from key loss

If you lose control of your Customer Keys, the availability key lets you decrypt affected data and re-encrypt it under a new DEP with new Customer Keys.

# [Exchange and Multi-workload](#tab/exchange-recovery)
1. Create two new Customer Keys in separate Azure subscriptions.
2. Create a new DEP (Exchange or Multi-workload).
3. Assign the DEP to impacted mailboxes or tenant.
4. Allow background re-encryption (up to 72 hours). The availability key protects data during transition.

# [SharePoint and OneDrive](#tab/spo-recovery)
1. Open a Support request to activate the availability key.
2. Create two new Customer Keys and a new SharePoint/OneDrive DEP.
3. Re-onboard with the new DEP (typical recovery: ~4 hours after activation, varies by site count).

---

## How the availability key is used

# [Exchange and Multi-workload](#tab/exchange-how)
When you create a DEP, Microsoft 365 generates a DEP Key encrypted three times: once with each Customer Key and once with the availability key. Only encrypted versions are stored.

**Decryption flow:**

1. Decrypt the DEP Key using a Customer Key.
2. Use the DEP Key to decrypt the Mailbox/Workload Key.
3. Use that key to decrypt and access the data.

# [SharePoint and OneDrive](#tab/spo-how)
SharePoint/OneDrive uses a different architecture. When enabled, Microsoft 365 creates a tenant intermediate key (TIK) encrypted twice with your Customer Keys (plus a copy with the availability key for recovery).

**Key hierarchy:** TIK → Site keys → Blob keys → File chunks (stored in Azure Blob Storage)

**Decryption flow:**

1. Decrypt the TIK with a Customer Key.
2. Use the TIK to decrypt a site key.
3. Use the site key to decrypt a blob key.
4. Use the blob key to decrypt the file chunk.

For performance, the service issues two parallel decryption requests; the first success is used. Decrypted TIKs are cached and refreshed before expiration. The availability key can only decrypt the TIK after you explicitly request recovery through Support.

Note

Customer Key covers SharePoint file data in Azure Blob Storage, not list items or metadata in SQL. Customer Lockbox governs human access.

---

## Availability key triggers

# [Exchange and Multi-workload](#tab/exchange-triggers)
When Microsoft 365 needs a DEP Key:

1. Reads the DEP to identify both Customer Keys.
2. Randomly selects one key and requests Azure Key Vault to unwrap the DEP Key.
3. If that fails, tries the alternate key.
4. If both fail, evaluates failure type:
    - **System errors** (Key Vault unavailable, timeouts, network faults): Falls back to availability key.
    - **Access denied** (key deleted, permissions removed): User request fails with error (no fallback).

Important

Internal operations (mailbox moves, indexing, anti-virus, eDiscovery, DLP) can still fall back to the availability key when both Customer Keys are unreachable, regardless of error type, until you delete the availability key.

# [SharePoint and OneDrive](#tab/spo-triggers)
You must contact Microsoft Support to explicitly request an availability key to use for recovery.

---

### Audit logs and the availability key

Automated background processing doesn't generate customer-visible logs. When the availability key is used, fallback events create [Unified Audit Log](audit-search) entries in the Microsoft Purview portal:

- **Record type**: CustomerKeyServiceEncryption
- **Activity**: Fallback to availability key
- **Workload field**: `Exchange` or `M365DataAtRestEncryption`

Fields include date, time, organization ID, DEP ID, Policy ID, and Request ID ([schema details](/en-us/office/office-365-management-api/office-365-management-activity-api-schema)).

![Audit log search for availability key events](media/customerkeyauditlogsearchavailabilitykeyloggingimage.png)

![Availability key custom parameters](media/customerkeyauditlogsearchavailabilitykeyloggingcustomparam.png)

Note

SharePoint availability key usage isn't logged until the customer provides Lockbox approval.

## Availability key in the Customer Key hierarchy

The availability key wraps the tier of keys below it in the encryption hierarchy. Algorithms by service:

| Service | Algorithm |
| --- | --- |
| Exchange and Multi-workload | AES-256 |
| SharePoint and OneDrive | RSA-2048 |

### Encryption ciphers for Exchange

![Encryption ciphers for Exchange in Customer Key](media/customerkeyencryptionhierarchiesexchangeskype.png)

### Encryption ciphers for SharePoint

![Encryption ciphers for SharePoint in Customer Key](media/customerkeyencryptionhierarchiessharepointonedriveteamsfiles.png)