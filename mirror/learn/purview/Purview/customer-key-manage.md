---
layout: Conceptual
title: Manage Customer Key encryption policies - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/customer-key-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
ms.reviewer: chrwarren
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: After you set up Customer Key, learn how to manage it by restoring Azure Key Vault keys, managing permissions, and creating and assigning data encryption policies.
ms.custom: msecd-doc-authoring-1014, sfi-ga-nochange, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 1ed160f0-703f-e23e-3db4-e883a04a926f
document_version_independent_id: 1ed160f0-703f-e23e-3db4-e883a04a926f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/customer-key-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-key-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/customer-key-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6cf30564-b6ed-27cf-9911-8edf4a11a504
---

# Manage Customer Key encryption policies - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

After setting up Customer Key, create and assign one or more **data encryption policies (DEPs)** to control how Microsoft 365 encrypts your organization's data at rest. After you assign them, you can manage your encryption keys and policies. For example, you can verify encryption status, view DEP details, disable a DEP, restore keys, or roll back to Microsoft-managed keys.

Microsoft Purview Customer Key also supports **Windows 365 Cloud PCs**. For more information, see [Microsoft Purview Customer Key for Windows 365 Cloud PCs](/en-us/windows-365/enterprise/purview-customer-key).

## Prerequisites

Before managing Customer Key, make sure you have:

- **Completed setup**: Finish all steps in [Set up Customer Key](customer-key-set-up)
- **Key Vault URIs**: Get the URIs for your Azure Key Vault keys. See [Obtain the URI for each Azure Key Vault key](customer-key-set-up#obtain-the-uri-for-each-azure-key-vault-key)
- **Permissions**: Exchange admin permissions (all DEP operations run through Exchange Online PowerShell)
- **PowerShell modules**:
    - [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) for DEP operations
    - [Azure PowerShell](/en-us/powershell/azure/install-azure-powershell) for Key Vault operations

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Quick reference: Commands by task

Use the following tables to quickly find the command you need.

### Create and assign DEPs

| Task | Workload | Command |
| --- | --- | --- |
| Create a DEP | Multi-workload | `New-M365DataAtRestEncryptionPolicy -Name <Name> -AzureKeyIDs <KeyURI1>,<KeyURI2>` |
| Create a DEP | Exchange | `New-DataEncryptionPolicy -Name <Name> -AzureKeyIDs <KeyURI1>,<KeyURI2>` |
| Create a DEP | SharePoint/OneDrive | `Register-SPODataEncryptionPolicy -PrimaryKeyVaultName <Name> -PrimaryKeyName <Name> -PrimaryKeyVersion <Version> -SecondaryKeyVaultName <Name> -SecondaryKeyName <Name> -SecondaryKeyVersion <Version>` |
| Assign a DEP | Multi-workload | `Set-M365DataAtRestEncryptionPolicyAssignment -DataEncryptionPolicy <PolicyName>` |
| Assign a DEP | Exchange mailbox | `Set-Mailbox -Identity <Mailbox> -DataEncryptionPolicy <PolicyName>` |
| Assign a DEP | Hybrid mailbox | `Set-MailUser -Identity <MailUser> -DataEncryptionPolicy <PolicyName>` |

### View and verify DEPs

| Task | Workload | Command |
| --- | --- | --- |
| List all DEPs | Multi-workload | `Get-M365DataAtRestEncryptionPolicy` |
| List all DEPs | Exchange | `Get-DataEncryptionPolicy` |
| View DEP assignment | Multi-workload | `Get-M365DataAtRestEncryptionPolicyAssignment` |
| View mailbox DEP | Exchange | `Get-MailboxStatistics -Identity <Mailbox> | fl DataEncryptionPolicyID` |
| View encryption status | SharePoint/OneDrive | `Get-SPODataEncryptionPolicy` |
| Check mailbox encryption | Exchange | `Get-MailboxStatistics -Identity <Mailbox> | fl IsEncrypted` |

### Manage and disable DEPs

| Task | Workload | Command |
| --- | --- | --- |
| Disable a DEP | Multi-workload | `Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Enabled $false` |
| Unassign a DEP | Exchange | `Set-Mailbox -Identity <Mailbox> -DataEncryptionPolicy $null` |

### Key Vault operations

| Task | Command |
| --- | --- |
| View Key Vault permissions | `Get-AzKeyVault -VaultName <VaultName>` |
| Remove user access | `Remove-AzKeyVaultAccessPolicy -VaultName <VaultName> -UserPrincipalName <UPN>` |
| Restore a key | `Restore-AzKeyVaultKey -VaultName <VaultName> -InputFile <BackupFile>` |

## Create a multi-workload DEP

To create a multi-workload DEP, follow these steps:

1. On your local computer, sign in using a **work or school account** with **Compliance Administrator** permissions, and [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the following cmdlet to create a multi-workload data encryption policy:

    ```powershell
    New-M365DataAtRestEncryptionPolicy -Name <PolicyName> -AzureKeyIDs <KeyVaultURI1, KeyVaultURI2> [-Description <String>]
    ```

    **Parameter definitions:**

    - `-Name`: The name you want to use for the policy. No spaces allowed.
    - `-AzureKeyIDs`: URIs of the two Azure Key Vault keys used in the policy, separated by commas.

        **Example**: `"https://contosoCentralUSvault1.vault.azure.net/keys/Key_02"``"https://contosoWestUSvault1.vault.azure.net/keys/Key_01"`
    - `Description`*(optional)*: A human-readable description of the policy.

        **Example**: `"Policy for multiple workloads for all users in the tenant."`

    ```powershell
    New-M365DataAtRestEncryptionPolicy -Name "Contoso_Global" -AzureKeyIDs "https://contosoWestUSvault1.vault.azure.net/keys/Key_01","https://contosoCentralUSvault1.vault.azure.net/keys/Key_02" -Description "Policy for multiple workloads for all users in the tenant."
    ```

### Assign multi-workload policy

After creating a multi-workload data encryption policy (DEP), assign it using the `Set-M365DataAtRestEncryptionPolicyAssignment` cmdlet. After assignment, Microsoft 365 encrypts your organization's data using the keys specified in the DEP.

```powershell
Set-M365DataAtRestEncryptionPolicyAssignment -DataEncryptionPolicy <PolicyName or ID>
```

Replace `<PolicyName or ID>` with the name or GUID of the policy.

Example:

```powershell
Set-M365DataAtRestEncryptionPolicyAssignment -DataEncryptionPolicy "Contoso_Global"
```

**Windows 365 Cloud PCs**:

After assigning the policy, allow 3–4 hours for the Intune admin center to reflect the update. After the update, follow the steps in the admin center to encrypt existing Cloud PCs.

For more information, see [Set up Customer Keys for your Windows 365 Cloud PCs](/en-us/windows-365/enterprise/purview-customer-key#set-up-customer-keys-for-your-windows-365-cloud-pcs).

## Create a DEP for Exchange mailboxes

Before you begin, complete the required setup steps. For details, see [Set up Customer Key](customer-key-set-up). To create the DEP, you’ll need the Azure Key Vault URIs obtained during setup. For more information, see [Obtain the URI for each Azure Key Vault key](customer-key-set-up#obtain-the-uri-for-each-azure-key-vault-key).

To create a DEP for Exchange mailboxes, follow these steps:

1. On your local computer, using a work or school account that has Exchange admin permissions, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Create a DEP using the `New-DataEncryptionPolicy` cmdlet:

    ```powershell
    New-DataEncryptionPolicy -Name <PolicyName> -Description "Policy Description" -AzureKeyIDs <KeyVaultURI1>, <KeyVaultURI2>
    ```

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `-Name` | Enter a name for the policy. Names can't contain spaces. | `USA_mailboxes` |
    | `-AzureKeyIDs` | Enter the URIs for two keys in separate Azure Key Vaults. Separate them with a comma and a space. | `https://contosoEastUSvault01.vault.azure.net/keys/USA_key_01`, `https://contosoEastUS2vault01.vault.azure.net/keys/USA_key_02` |
    | `-Description` | A user-friendly description that helps identify the policy’s purpose. | `"Root key for mailboxes in USA and its territories"` |

    **Example**:

    ```powershell
    New-DataEncryptionPolicy -Name USA_mailboxes -Description "Root key for mailboxes in USA and its territories" -AzureKeyIDs https://contoso_EastUSvault02.vault.azure.net/keys/USA_key_01, https://contoso_CentralUSvault02.vault.azure.net/keys/USA_Key_02
    ```

    For syntax and parameter information, see [New-DataEncryptionPolicy](/en-us/powershell/module/exchange/new-dataencryptionpolicy).

### Assign a DEP to a mailbox

Assign the DEP with the `Set-Mailbox` cmdlet. Once assigned, Microsoft 365 encrypts the mailbox with the keys in the DEP.

```powershell
Set-Mailbox -Identity <MailboxIdParameter> -DataEncryptionPolicy <PolicyName>
```

For more information, see [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox).

#### Assign a DEP to hybrid mailboxes

In hybrid environments, assign a DEP to synchronized on-premises mailbox data using `Set-MailUser`:

```powershell
Set-MailUser -Identity <MailUserIdParameter> -DataEncryptionPolicy <PolicyName>
```

For more information, see [Set-MailUser](/en-us/powershell/module/exchange/set-mailuser) and [on-premises mailboxes using Outlook for iOS and Android with hybrid Modern Authentication](/en-us/exchange/clients/outlook-for-ios-and-android/use-hybrid-modern-auth).

### Assign a DEP before you migrate a mailbox to the cloud

Assigning a DEP before migration encrypts your mailbox contents during the move, which is more efficient than assigning a DEP after migration.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) using a work or school account with [Exchange Online cmdlet permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions).
2. Run the following command:

    ```powershell
    Set-MailUser -Identity <GeneralMailboxOrMailUserIdParameter> -DataEncryptionPolicy <DataEncryptionPolicyIdParameter>
    ```

### View the DEPs you created for Exchange mailboxes

To list all DEPs in your organization, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) and run:

```powershell
Get-DataEncryptionPolicy
```

For detailed cmdlet information, see [Get-DataEncryptionPolicy](/en-us/powershell/module/exchange/get-dataencryptionpolicy).

### Determine the DEP assigned to a mailbox

To find the DEP assigned to a mailbox, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) and run:

```powershell
Get-Mailbox -Identity <MailboxIdParameter> | fl DataEncryptionPolicy
```

To get the friendly name from the returned GUID:

```powershell
Get-DataEncryptionPolicy <GUID>
```

For more information, see [Get-MailboxStatistics](/en-us/powershell/module/exchange/get-mailboxstatistics).

## Create a DEP for use with SharePoint and OneDrive

Before you begin, make sure you complete the required setup steps. For more information, see [Set up Customer Key](customer-key-set-up).

To configure Customer Key for SharePoint and OneDrive, use SharePoint PowerShell.

A DEP uses two keys from separate Azure Key Vaults in different regions. Single-geo tenants need one DEP; multi-geo tenants need one DEP per geo with different keys. You need the Key Vault URIs for both keys (see [Obtain the URI for each Azure Key Vault key](customer-key-set-up#obtain-the-uri-for-each-azure-key-vault-key)).

1. On your local computer, using a work or school account that has [Exchange Online cmdlet permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions) in your organization, [connect to SharePoint PowerShell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?preserve-view=true&amp;view=sharepoint-ps).
2. Use the `Register-SPODataEncryptionPolicy` cmdlet to register the DEP.

    ```powershell
    Register-SPODataEncryptionPolicy -PrimaryKeyVaultName <PrimaryKeyVaultName> -PrimaryKeyName <PrimaryKeyName> -PrimaryKeyVersion <PrimaryKeyVersion> -SecondaryKeyVaultName <SecondaryKeyVaultName> -SecondaryKeyName <SecondaryKeyName> -SecondaryKeyVersion <SecondaryKeyVersion>
    ```

    Example:

    ```powershell
    Register-SPODataEncryptionPolicy -PrimaryKeyVaultName 'stageRG3vault' -PrimaryKeyName 'SPKey3' -PrimaryKeyVersion 'f635a23bd4a44b9996ff6aadd88d42ba' -SecondaryKeyVaultName 'stageRG5vault' -SecondaryKeyName 'SPKey5' -SecondaryKeyVersion '2b3e8f1d754f438dacdec1f0945f251a'
    ```

    **If using Managed HSM**: Use the full URL of the key **including version** for each vault.

    ```powershell
    Register-SPODataEncryptionPolicy -PrimaryKeyVaultUri <PrimaryKeyVaultURL> -SecondaryKeyVaultUri <SecondaryKeyVaultURL>
    ```

    Example:

    ```powershell
    Register-SPODataEncryptionPolicy -PrimaryKeyVaultURL https://M365-Test.managedhsm.azure.net/keys/Sharepoint-01/aaaa5513974f4780ea67b2f5d8c3dd -SecondaryKeyVaultURL https://M365-Test-02.managedhsm.azure.net/keys/Sharepoint-02/7d8f30343bed4e44a57225bae2012388
    ```

    Note

    After the DEP is registered, encryption of the geo's data begins. This process might take some time.

For full cmdlet reference, see [Register-SPODataEncryptionPolicy](/en-us/powershell/module/sharepoint-online/register-spodataencryptionpolicy?preserve-view=true&amp;view=sharepoint-ps).

## Verify Customer Key encryption status

After rolling a Customer Key, assigning a new data encryption policy (DEP), or migrating a mailbox, follow the steps in this section to confirm that encryption is complete.

### Verify encryption completes for Exchange mailboxes

Encrypting a mailbox with Customer Key can take time. To verify that encryption is complete, determine the DEP assigned to the mailbox and confirm that the returned data encryption policy ID matches the policy you assigned.

### Verify encryption completes for SharePoint and OneDrive

Check on the status of encryption by running the Get-SPODataEncryptionPolicy cmdlet as follows:

```PowerShell
   Get-SPODataEncryptionPolicy
```

The output includes primary/secondary key URIs, encryption status, and percentage of sites onboarded. Status values:

| Status | Description |
| --- | --- |
| **Unregistered** | Customer Key encryption not applied |
| **Registering** | Encryption in progress (shows percentage complete) |
| **Registered** | Encryption complete |
| **Rolling** | Key roll in progress (shows percentage complete) |

## Get details about DEPs you use with multiple workloads

To view multi-workload DEPs, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) with Compliance Administrator permissions and run:

```powershell
Get-M365DataAtRestEncryptionPolicy
```

For details about a specific DEP:

```powershell
Get-M365DataAtRestEncryptionPolicy -Identity "Contoso_Global"
```

## Get multi-workload DEP assignment information

To identify which DEP is assigned to your tenant, [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) and run:

```powershell
Get-M365DataAtRestEncryptionPolicyAssignment
```

## Disable a multi-workload DEP

Before disabling, unassign the DEP from workloads in your tenant. Then [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) and run:

```powershell
Set-M365DataAtRestEncryptionPolicy -Identity "PolicyName" -Enabled $false
```

## Restore Azure Key Vault keys

Before restoring, try using soft delete to recover keys (available for up to 90 days). Full restoration is only needed if a key or vault is permanently lost.

To restore a key using Azure PowerShell, run the following command:

```powershell
Restore-AzKeyVaultKey -VaultName <vault name> -InputFile <filename>
```

**Example**:

```powershell
Restore-AzKeyVaultKey -VaultName Contoso-O365EX-NA-VaultA1 -InputFile Contoso-O365EX-NA-VaultA1-Key001-Backup-20170802.backup
```

Important

If the key vault already contains a key with the same name, the restore operation fails. The `Restore-AzKeyVaultKey` cmdlet restores all versions of the key, including its metadata and name.

## Manage key vault permissions

Use Azure PowerShell to view or remove key vault permissions (for example, when a user leaves the team).

To view permissions:

```powershell
Get-AzKeyVault -VaultName <vault name>
```

**Example**:

```powershell
Get-AzKeyVault -VaultName Contoso-O365EX-NA-VaultA1
```

To remove a user's access:

```powershell
Remove-AzKeyVaultAccessPolicy -VaultName <vault name> -UserPrincipalName <UPN of user>
```

## Roll back from Customer Key to Microsoft-managed keys

You can revert to Microsoft-managed keys, which re-encrypts your data using the default encryption method for each workload.

Important

Rolling back reverts encryption but doesn't delete data. A **data purge** permanently crypto-deletes data and can't be performed on multi-workload policies.

### Roll back from Customer Key for multiple workloads

Important

Rolling back from Customer Key for multiple workloads is **not** supported in Gallatin.

If you no longer want to use Customer Key with multi-workload data encryption policies (DEPs), submit a support request through [Microsoft Support](https://support.microsoft.com/en-us/microsoft-365). Include the following information in your request:

- Tenant fully qualified domain name (FQDN)
- Tenant contact for the rollback request
- Reason for discontinuing Customer Key
- Incident number

Important

You must retain your Azure Key Vaults (AKVs) and encryption keys with the appropriate permissions. This action is required so that data can be rewrapped using Microsoft-managed keys.

### Roll back from Customer Key for Exchange

Important

Rolling back from Customer Key for Exchange is **not** supported in Gallatin.

If you no longer want to encrypt individual mailboxes using mailbox-level data encryption policies (DEPs), you can unassign those DEPs from all mailboxes.

To unassign a mailbox-level DEP, follow these steps:

1. Use a work or school account that has the necessary [Exchange Online PowerShell permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions), and [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the following cmdlet.

    ```powershell
    Set-Mailbox -Identity <mailbox> -DataEncryptionPolicy $null
    ```

This command unassigns the current DEP and re-encrypts the mailbox using the default Microsoft-managed keys.

Note

You can't unassign the DEP associated with Microsoft-managed keys. If you don't want to use Microsoft-managed keys, assign a different DEP to the mailbox instead.

### Roll back from Customer Key for SharePoint and OneDrive

Note

Roll back for Customer Key for SharePoint and OneDrive is currently in preview and is not available to tenants in GCC High, DoD, or M365 operated by 21Vianet.

If you no longer want to use Customer Key for SharePoint and OneDrive, submit a support request through [Microsoft Support](https://support.microsoft.com/en-us/microsoft-365). Include the following information in your request:

- Tenant fully qualified domain name (FQDN)
- Tenant contact for the rollback request
- Reason for discontinuing Customer Key
- Incident number

Important

You must retain your Azure Key Vaults (AKVs) and encryption keys with the appropriate permissions. This action is required so that data can be rewrapped using Microsoft-managed keys.

## Revoke your keys and start the data purge path

You control revocation of all root keys, including the availability key. When you revoke keys to purge data and exit the service, the availability key is deleted after the purge completes. This functionality is only supported for DEPs assigned to individual mailboxes.

Microsoft 365 audits and validates the data purge process. For more information, see the [SSAE 18 SOC 2 Report](https://servicetrust.microsoft.com/), [Risk Assessment and Compliance Guide for Financial Institutions](https://servicetrust.microsoft.com/ViewPage/TrustDocuments?command=Download&amp;downloadType=Document&amp;downloadId=edee9b14-3661-4a16-ba83-c35caf672bd7&amp;docTab=6d000410-c9e9-11e7-9a91-892aae8839ad_FAQ_and_White_Papers), and [Microsoft 365 Exit Planning Considerations](https://servicetrust.microsoft.com/ViewPage/TrustDocuments?command=Download&amp;downloadType=Document&amp;downloadId=77ea7ebf-ce1b-4a5f-9972-d2d81a951d99&amp;docTab=6d000410-c9e9-11e7-9a91-892aae8839ad_FAQ_and_White_Papers).

Important

Purging a multi-workload DEP isn't supported. These policies encrypt data across multiple workloads and users within your tenant. Purging such a DEP would make data across all workloads inaccessible.

If you're exiting Microsoft 365 services entirely, see [how to delete a tenant in Microsoft Entra ID](/en-us/azure/active-directory/enterprise-users/directory-delete-howto).

### Revoke your Customer Keys and the availability key for Exchange

When you initiate the data purge path for Exchange, you place a permanent data purge request on a data encryption policy (DEP). This action permanently deletes encrypted data in all mailboxes assigned to that DEP.

Because the PowerShell cmdlet works on only one DEP at a time, consider reassigning a single DEP to all mailboxes before starting the data purge process.

Warning

Don't use the data purge path to delete a subset of mailboxes. This process is intended only for organizations that are fully exiting the service.

Important

Rolling back from Customer Key for Exchange, is **not** supported in Gallatin.

To initiate the data purge path, follow these steps:

1. Remove wrap and unwrap permissions for **O365 Exchange Online** from your Azure Key Vaults.
2. Use a work or school account with the appropriate [Exchange Online PowerShell permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions), and [connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
3. For each DEP that includes mailboxes you want to purge, run the [`Set-DataEncryptionPolicy`](/en-us/powershell/module/exchange/set-dataencryptionpolicy) cmdlet:

    ```powershell
    Set-DataEncryptionPolicy <Policy ID> -PermanentDataPurgeRequested -PermanentDataPurgeReason <Reason> -PermanentDataPurgeContact <ContactName>
    ```

    If the command fails, confirm that Exchange Online permissions were removed from both keys in the Azure Key Vault, as described in step 1. After you run the `Set-DataEncryptionPolicy` cmdlet with the `-PermanentDataPurgeRequested` switch, the DEP can't be assigned to mailboxes anymore.
4. Contact Microsoft Support and request the Data Purge eDocument.

    Microsoft sends a legal document to confirm and authorize the data purge. The person who signs this is usually an executive or other legally authorized representative.
5. After your representative signs the document, return it to Microsoft (usually via electronic signature).

    After Microsoft receives the signed eDocument, it verifies the authenticity of the signature and signee. After verification, they run the necessary cmdlets to complete the data purge. This process deletes the DEP, marks affected mailboxes for permanent deletion, and removes the availability key. After the process finishes, the data is purged, inaccessible to Exchange, and can't be recovered.

### Revoke your Customer Keys and the availability key for SharePoint and OneDrive

Purging DEPs for SharePoint and OneDrive isn't supported in Customer Key. If you're exiting Microsoft 365 services entirely, you can follow the documented process to delete your tenant.

For details, see [how to delete a tenant in Microsoft Entra ID](/en-us/azure/active-directory/enterprise-users/directory-delete-howto).

### Migrate your Key Vaults from the legacy access policy model to RBAC

If you onboarded to Customer Key using the legacy access policy model, follow these steps to migrate all Azure Key Vaults to use role-based access control (RBAC). To compare the two models and understand why Microsoft recommends RBAC, see [Azure role-based access control (Azure RBAC) vs. access policies (legacy)](/en-us/azure/key-vault/general/rbac-access-policy).

#### Remove legacy access policies

To remove the existing access policies from your Key Vaults, use the `Remove-AzKeyVaultAccessPolicy` cmdlet.

1. Sign in to your Azure subscription with Azure PowerShell. For guidance, see [Sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps).
2. Run the following command to remove access for the **Microsoft 365 Service** principal:

    ```powershell
    Remove-AzKeyVaultAccessPolicy -VaultName <VaultName> -ServicePrincipalName c066d759-24ae-40e7-a56f-027002b5d3e4
    ```
3. Run the following command to remove access for the **Exchange Online** principal:

    ```powershell
    Remove-AzKeyVaultAccessPolicy -VaultName <VaultName> -ServicePrincipalName 00000002-0000-0ff1-ce00-000000000000
    ```
4. Run the following command to remove access for the **SharePoint and OneDrive for work or school service principal**:

    ```powershell
    Remove-AzKeyVaultAccessPolicy -VaultName <VaultName> -ServicePrincipalName 00000003-0000-0ff1-ce00-000000000000
    ```

#### Change the access configuration permission model

After removing the access policies, update the permission model for each Key Vault in the Azure portal:

1. In the Azure portal, navigate to your Key Vault.
2. In the left-hand menu, under **Settings**, select **Access configuration**.
3. Under **Permission model**, choose **Azure role-based access control**.
4. Select **Apply** at the bottom of the screen.

    ![Screenshot of the Azure Key Vault Access configuration page in the Azure portal.](media/ckkeyvaulthome.png)

    ![Screenshot of the Azure role-based access control permission model selected in Key Vault Access configuration.](media/ckkeyvaultconfirm.png)

#### Assign RBAC permissions

After you switch the permission model, follow the steps in [Assign permissions](customer-key-set-up#assign-permissions-to-each-azure-key-vault) to each Key Vault to grant the necessary roles.

## Troubleshooting

The following table lists common Customer Key issues, possible causes, and recommended resolutions.

| Issue | Possible cause | Resolution |
| --- | --- | --- |
| DEP creation fails | Invalid Key Vault URI | Verify the URI format and that the key exists in the vault |
| DEP assignment fails | Insufficient permissions | Ensure you have Exchange admin permissions |
| Mailbox not encrypted after one week | Database move not complete | Contact Microsoft Support |
| `Get-MailboxStatistics` returns no `DataEncryptionPolicyID` | DEP not assigned | Assign a DEP using `Set-Mailbox` |
| SharePoint encryption stuck at "Registering" | Large tenant or key access issue | Verify key permissions; for large tenants, encryption can take time |
| Key restore fails | Key with same name exists | Use a different vault or remove the existing key first |
| Can't connect to Exchange Online PowerShell | Module not installed or outdated | Install or update the [Exchange Online PowerShell module](/en-us/powershell/exchange/exchange-online-powershell-v2) |