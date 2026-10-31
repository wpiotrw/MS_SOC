---
layout: Conceptual
title: Roll or rotate a Customer Key or an availability key - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/customer-key-availability-key-roll
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.reviewer: chrwarren
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: Learn how to roll root keys that you store in Azure Key Vault and use with the Microsoft Purview Customer Key.
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 4532a051-ffce-da77-4014-0697e02942cd
document_version_independent_id: 4532a051-ffce-da77-4014-0697e02942cd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/customer-key-availability-key-roll.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-key-availability-key-roll
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/customer-key-availability-key-roll.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 58d3d190-5210-4272-7b2f-88869fc00efd
---

# Roll or rotate a Customer Key or an availability key - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Caution

Roll an encryption key used with Customer Key **only** if required by your organization's security or compliance policies.

**Do not delete or disable any keys**, including older versions, that are or were associated with **Exchange**, **Multi-workload**, or **SharePoint** encryption policies.

For example:

- SharePoint retains backup content for restore and recovery, which might also rely on older keys.

## Prerequisites

Before you roll or rotate keys, ensure you have:

- **Permissions**: Global Administrator or appropriate [Exchange permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions)
- **PowerShell modules installed**:
    - [Azure PowerShell](/en-us/powershell/azure/install-azure-powershell) for Azure Key Vault operations
    - [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) to run the given cmdlets
- **Access to Azure Key Vault**: You must have permissions to create new key versions in your key vaults

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Quick reference: Commands by workload

Use the following table to quickly find the command you need based on your workload and scenario.

| Workload | Scenario | Command |
| --- | --- | --- |
| **Multi-workload** | Refresh DEP with new key version | `Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Refresh` |
| **Multi-workload** | Replace keys in DEP | `Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>` |
| **Exchange** | Refresh DEP with new key version | `Set-DataEncryptionPolicy -Identity <Policy> -Refresh` |
| **Exchange** | Replace keys in DEP | `Set-DataEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>` |
| **SharePoint/OneDrive** | Roll/Rotate a key | `Update-SPODataEncryptionPolicy <SPOAdminSiteUrl> -KeyVaultName <Name> -KeyName <Name> -KeyVersion <Version> -KeyType <Primary \| Secondary>` |
| **SharePoint/OneDrive** | Check roll progress | `Get-SPODataEncryptionPolicy <SPOAdminSiteUrl>` |
| **Azure Key Vault** | Create new key version | `Add-AzKeyVaultKey -VaultName <VaultName> -Name <KeyName> -Destination HSM -KeyOps @('wrapKey','unwrapKey')` |

Note

For SharePoint and OneDrive, the same cmdlet, `Update-SPODataEncryptionPolicy`, is used to roll (or rotate) and replace keys.

## Choose your key rolling method

There are two ways to roll customer-managed root keys. Use the following table to determine which method is right for your scenario.

| Method | When to use | What happens |
| --- | --- | --- |
| **Update existing key** (create new version) | Routine key rotation; maintaining the same key name | Creates a new version of the existing key. The DEP references the same key name but uses the new version after refresh. |
| **Replace with new key** | Compromised key; changing key vault; organizational restructuring | Creates an entirely new key with a new name. The DEP is updated to reference the new key URIs. |

## About rolling the availability key

You can't directly roll the availability key. You can only roll keys you manage in Azure Key Vault.

Microsoft 365 rolls availability keys automatically on an internal schedule with no customer-facing SLA. Administrators don't have direct access to the key store. For more information, see [Understand the availability key](customer-key-availability-key-understand).

Important

For Exchange, creating a new DEP effectively rolls the availability key since each new data encryption policy (DEP) generates a unique availability key.

For SharePoint and OneDrive, availability keys are created at the forest level and shared across DEPs. These keys roll only on Microsoft's internal schedule, but SharePoint, OneDrive, and Teams roll the tenant intermediate key (TIK) with each new DEP to mitigate this.

## Roll customer-managed root keys

Use one of the following methods to roll customer-managed root keys stored in Azure Key Vault. Choose the method that matches your scenario based on the guidance in Choose your key rolling method.

### Method 1: Update an existing key (create a new version)

Use this method to create a new version of an existing key. This approach is recommended for routine key rotations.

#### Step 1: Create a new key version in Azure Key Vault

To request a new version of an existing key, use the `Add-AzKeyVaultKey` cmdlet with the same key name you used when creating the original key.

1. Sign in to your Azure subscription with Azure PowerShell. For instructions, see [Sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps).
2. Run the `Add-AzKeyVaultKey` cmdlet:

    ```powershell
    Add-AzKeyVaultKey -VaultName <VaultName> -Name <KeyName> -Destination HSM -KeyOps @('wrapKey','unwrapKey') -NotBefore (Get-Date)
    ```

    **Example:**

    ```powershell
    Add-AzKeyVaultKey -VaultName Contoso-CK-EX-NA-VaultA1 -Name Contoso-CK-EX-NA-VaultA1-Key001 -Destination HSM -KeyOps @('wrapKey','unwrapKey') -NotBefore (Get-Date -Date "12/27/2016 12:01 AM")
    ```

    In this example, a key named Contoso-CK-EX-NA-VaultA1-Key001 already exists in the Contoso-CK-EX-NA-VaultA1 vault. The cmdlet creates a new version of the key. Previous versions are retained in the key's version history.
3. Repeat this step in each Azure Key Vault that contains keys you want to roll.

#### Step 2: Refresh the DEP to use the new key version

After creating a new key version, refresh the DEP to use it. Connect to [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) with appropriate [Exchange cmdlet permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions), then run the appropriate cmdlet:

**For Multi-workload DEPs:**

```powershell
Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Refresh
```

**For Exchange DEPs:**

```powershell
Set-DataEncryptionPolicy -Identity <Policy> -Refresh
```

Note

The `DataEncryptionPolicyID` property remains the same when refreshing with a new version of the same key. Refreshing the DEP with a new version of the same key doesn't rotate the availability key.

**For SharePoint and OneDrive DEPs:**

SharePoint supports rolling only one key at a time. Wait for the first operation to finish before rolling a second key.

```powershell
Update-SPODataEncryptionPolicy <SPOAdminSiteUrl> -KeyVaultName <Name> -KeyName <Name> -KeyVersion <Version> -KeyType <Primary | Secondary>
```

For Managed HSM keys, use `-KeyVaultURL` instead of `-KeyVaultName`.

To check progress: `Get-SPODataEncryptionPolicy <SPOAdminSiteUrl>`

### Method 2: Replace keys with newly generated keys

Use this method to replace existing keys entirely with new keys.

Important

Keep old keys enabled and accessible until the replacement process is fully completed.

Connect to [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) with the appropriate [Exchange cmdlet permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions), then run the appropriate cmdlet:

**For Exchange DEPs:**

```powershell
Set-DataEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>
```

**For Multi-workload DEPs:**

```powershell
Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>
```

Note

The order of key URIs doesn't matter. To replace only one key, you must still provide both URIs. Wait **24 hours** before disabling old keys, and then an **additional 24-48 hours** before purging.

## Verify key roll status

Use the following commands to verify the status of your key roll operations.

| Workload | Verification command |
| --- | --- |
| **SharePoint/OneDrive** | `Get-SPODataEncryptionPolicy <SPOAdminSiteUrl>` |
| **Exchange** | `Get-DataEncryptionPolicy -Identity <Policy>` |
| **Multi-workload** | `Get-M365DataAtRestEncryptionPolicy -Identity <Policy>` |

## Troubleshooting

The following table lists common issues you might encounter when rolling keys and how to resolve them.

| Issue | Possible cause | Resolution |
| --- | --- | --- |
| Key roll fails with permission error | Insufficient Azure Key Vault permissions | Verify your account has `wrapKey` and `unwrapKey` permissions on the key vault |
| DEP refresh fails | New key version not yet propagated | Wait a few minutes and retry the refresh command |
| SharePoint roll shows "In Progress" for extended time | Large tenant with significant data | SharePoint key rolls can take time for large tenants. Continue monitoring with `Get-SPODataEncryptionPolicy` |
| Can't access encrypted content after key roll | Old key was disabled too soon | Re-enable the old key and wait 24-48 hours before disabling again |