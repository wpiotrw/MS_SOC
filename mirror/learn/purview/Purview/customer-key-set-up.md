---
layout: Conceptual
title: Set up Customer Key - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/customer-key-set-up
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: kreagle
ms.date: 2025-09-08T00:00:00.0000000Z
author: k-reagle
manager: laurawi
ms.reviewer: chrwarren
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: This article describes the steps to create and configure the required Azure resources and then provides the steps to set up Customer Key.
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 4e9c6974-b9b2-e8c5-218c-7bfa070748a7
document_version_independent_id: 4e9c6974-b9b2-e8c5-218c-7bfa070748a7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/customer-key-set-up.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-key-set-up
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/customer-key-set-up.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 2e6c71cd-c413-f6fd-de69-4311fa52c47e
---

# Set up Customer Key - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Customer Key lets you control your organization's encryption keys and configure Microsoft 365 to use those keys to encrypt your data at rest in Microsoft's datacenters.

This article walks you through creating and configuring the required Azure resources, then enabling Customer Key. After setup, you assign policies that determine which keys encrypt data across Microsoft 365 workloads.

For a general overview and more information, see [Overview of Customer Key](customer-key-overview).

Important

Customer Key gives you control over root encryption keys that can affect your entire organization. Mistakes with these keys can lead to service interruptions or permanent data loss.

## Prerequisites

Before setting up Customer Key, ensure you have:

- **Licensing**: For licensing requirements, see [Microsoft Purview Customer Key Licensing](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-customer-key)
- **Azure subscriptions**: Two paid Azure subscriptions (Free, Trial, Sponsorship, MSDN, or Legacy Support aren't eligible)
- **Permissions**: Exchange admin permissions (all Customer Key operations run through Exchange Online PowerShell)
- **PowerShell modules**:
    - [Azure PowerShell](/en-us/powershell/azure/install-azure-powershell) (v4.4.0 or higher recommended) for Key Vault/HSM operations
    - [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) for DEP operations
- **Azure knowledge**: Familiarity with [Azure Key Vault](/en-us/azure/key-vault/) and [Microsoft Entra tenant](/en-us/previous-versions/azure/azure-services/jj573650%28v=azure.100%29#what-is-an-azure-ad-tenant) concepts

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

If you need help beyond the documentation, contact [Microsoft Support](https://support.microsoft.com/microsoft-365). To share feedback or suggestions about Customer Key or this documentation, visit the [Microsoft 365 Community](https://techcommunity.microsoft.com/t5/microsoft-365/bd-p/microsoft-365).

## Overview of steps to set up Customer Key

To set up Customer Key, complete the following tasks in order. The rest of this article provides detailed instructions for each task, or links out to more information for each step in the process.

Important

The setup process differs depending on whether you're using **Azure Key Vault** or **Managed HSM**. The shared prerequisites appear first, followed by configuration-specific instructions.

### Prerequisites for all configurations

- Create two new Azure subscriptions
- Register the required Service Principals

### Configuration-specific setup

- Set up using Azure Key Vault
- Set up using Managed HSM

### Onboarding options

Choose the onboarding method that applies to your scenario:

- Onboard using the Customer Key Onboarding Service (recommended for most tenants)
- Onboard to Customer Key for SharePoint and OneDrive
- Onboard to Customer Key for special cloud environments

## Quick reference: Key setup commands

Use the following tables to quickly find the commands you need during setup.

### Service principal registration

| Task | Command |
| --- | --- |
| Check if Customer Key Onboarding app is registered | `Get-AzADServicePrincipal -ServicePrincipalName 19f7f505-34aa-44a4-9dcc-6a768854d2ea` |
| Register Customer Key Onboarding app | `New-AzADServicePrincipal -ApplicationId 19f7f505-34aa-44a4-9dcc-6a768854d2ea` |
| Check if M365DataAtRestEncryption app is registered | `Get-AzADServicePrincipal -ServicePrincipalName c066d759-24ae-40e7-a56f-027002b5d3e4` |
| Register M365DataAtRestEncryption app | `New-AzADServicePrincipal -ApplicationId c066d759-24ae-40e7-a56f-027002b5d3e4` |
| Check if Exchange Online app is registered | `Get-AzADServicePrincipal -ServicePrincipalName 00000002-0000-0ff1-ce00-000000000000` |
| Register Exchange Online app | `New-AzADServicePrincipal -ApplicationId 00000002-0000-0ff1-ce00-000000000000` |

### Azure Key Vault operations

| Task | Command |
| --- | --- |
| Create a key | `Add-AzKeyVaultKey -VaultName <VaultName> -Name <KeyName> -Destination HSM` |
| Get key URI | `(Get-AzKeyVaultKey -VaultName <VaultName>).Id` |
| Check key expiration | `Get-AzKeyVaultKey -VaultName <VaultName>` |
| Update key expiration | `Update-AzKeyVaultKey -VaultName <VaultName> -Name <KeyName> -Expires (Get-Date -Date "12/31/9999")` |
| Back up a key | `Backup-AzKeyVaultKey -VaultName <VaultName> -Name <KeyName> -OutputFile <BackupFile>` |

### Managed HSM operations

| Task | Command |
| --- | --- |
| Create a key | `Add-AzKeyVaultKey -HsmName <HSMName> -Name <KeyName> -Destination HSM` |
| Get key URI | `(Get-AzKeyVaultKey -HsmName <HSMName>).Id` |
| Check key expiration | `Get-AzKeyVaultKey -HsmName <HSMName>` |
| Update key expiration | `Update-AzKeyVaultKey -HsmName <HSMName> -Name <KeyName> -Expires (Get-Date -Date "12/31/9999")` |
| Back up a key | `Backup-AzKeyVaultKey -HsmName <HSMName> -Name <KeyName> -OutputFile <BackupFile>` |

### Customer Key onboarding

| Task | Command |
| --- | --- |
| Install onboarding module | `Install-Module -Name M365CustomerKeyOnboarding` |
| Create onboarding request | `New-CustomerKeyOnboardingRequest -Organization <TenantID> -Scenario <MDEP\|EXO> -Subscription1 <SubID1> -KeyIdentifier1 <KeyURI1> -Subscription2 <SubID2> -KeyIdentifier2 <KeyURI2> -OnboardingMode <Validate\|Enable>` |
| View onboarding requests | `Get-CustomerKeyOnboardingRequest -OrganizationID <TenantID>` |
| View failed validations | `$request.FailedValidations` |
| View passed validations | `$request.PassedValidations` |

## Create two new Azure subscriptions

Customer Key requires two Azure subscriptions. As a best practice, Microsoft recommends creating new Azure subscriptions specifically for use with Customer Key.

Azure Key Vault keys can only be authorized for applications in the same Microsoft Entra tenant. To assign data encryption policies (DEPs), make sure to create both subscriptions under the same Microsoft Entra tenant used by your organization. For example, use your work or school account that has proper administrator privileges in your organization. For step-by-step guidance, see [Sign up for Azure as an organization](/en-us/azure/active-directory/fundamentals/sign-up-organization).

Important

Customer Key requires two keys for each DEP. To support this requirement, you must create two separate Azure subscriptions. As a best practice, have different members of your organization manage one key in each subscription. These subscriptions should be used only to administer encryption keys for Microsoft 365. This configuration helps protect your organization in case someone accidentally, intentionally, or maliciously deletes or mismanages a key they control.

Following these best practices reduces the risk of human error and simplifies Customer Key management.

## Register the required Service Principals

To use the Customer Key, your tenant must have the required service principals registered. The following sections show you how to check whether the service principals are already registered in your tenant. If they aren't, run the `New-AzADServicePrincipal` cmdlet.

### Register the Service Principal for the Customer Key Onboarding Application

To check if the Customer Key Onboarding application is already registered with the correct permissions, run the following command:

```powershell
Get-AzADServicePrincipal -ServicePrincipalName 19f7f505-34aa-44a4-9dcc-6a768854d2ea
```

If it isn't registered, run:

```powershell
New-AzADServicePrincipal -ApplicationId 19f7f505-34aa-44a4-9dcc-6a768854d2ea
```

### Register the Service Principal for the M365DataAtRestEncryption Application

To check if the M365DataAtRestEncryption application is already registered with the correct permissions, run the following command:

```powershell
Get-AzADServicePrincipal -ServicePrincipalName c066d759-24ae-40e7-a56f-027002b5d3e4
```

If it isn't registered, run:

```powershell
New-AzADServicePrincipal -ApplicationId c066d759-24ae-40e7-a56f-027002b5d3e4
```

### Register the Service Principal for the Office 365 Exchange Online Application

To check if the Office 365 Exchange Online application is already registered with the correct permissions, run the following command:

```powershell
Get-AzADServicePrincipal -ServicePrincipalName 00000002-0000-0ff1-ce00-000000000000
```

If it isn't registered, run:

```powershell
New-AzADServicePrincipal -ApplicationId 00000002-0000-0ff1-ce00-000000000000
```

## Configuration-specific setup steps

Important

The following steps differ depending on whether you're using **Azure Key Vault** or **Managed HSM**. Use the tabs below to select your configuration.

# [Azure Key Vault](#tab/akv)
### Create a premium Azure Key Vault in each subscription

Prior to creating a key vault, perform the steps in [Getting Started with Azure Key Vault](/en-us/azure/key-vault/general/overview). These steps guide you through installing and launching Azure PowerShell, and connecting to your subscription. Next, create a resource group and a key vault.

Important

When creating your key vaults, you **must** enable both **soft delete** and **purge protection** during the initial vault creation process. Customer Key requires all vaults to have both features enabled with a retention period of **90** days. These settings can't be disabled once enabled, so it's critical to configure them correctly from the start. If you plan to enable firewall on your key vaults, ensure you select the option for [Allow Trusted Microsoft Services](/en-us/azure/key-vault/general/network-security#key-vault-firewall-enabled-trusted-services-only).

When you create a key vault, you must choose an SKU: either Standard or Premium. The Standard SKU uses software-protected keys without a Hardware Security Module (HSM), while the premium SKU allows the use of HSMs to protect keys. Customer Key supports key vaults with either of the two SKUs, but Microsoft strongly recommends using the Premium SKU. The cost of operations is the same for both; so, the only price difference comes from the monthly cost of each HSM-protected key. For pricing details, see [Key Vault pricing](https://azure.microsoft.com/pricing/details/key-vault/).

Important

Use the Premium SKU key vaults and HSM-protected keys for production data. Use Standard SKU key vaults and keys only for testing and validation.

#### Enabling soft delete and purge protection

Soft delete allows you to recover deleted keys or vaults within 90 days. Purge protection prevents permanent deletion until the retention period passes. Customer Key requires both features with a **90-day** retention period. Soft delete is enabled by default for new vaults; enable it manually for existing vaults.

To enable these features, see [Azure Key Vault recovery management with soft delete and purge protection](/en-us/azure/key-vault/general/key-vault-recovery?tabs=azure-portal).

**For each Microsoft 365 workload for which you use Customer Key, create a key vault in each of the two Azure subscriptions you set up earlier.**

#### Key Vault configuration

Note

If you're using Customer Key for Multiple Workloads, Exchange, and SharePoint scenarios, you need **three pairs** of key vaults, for a total of **six**.

Use a clear naming convention that reflects the intended use of the DEP with which you associate the vaults. The following table shows how to map each Azure Key Vault to each workload.

| Key Vault Name | Permissions for Multiple Microsoft 365 Workloads (M365DataAtRestEncryption) | Permissions for Exchange | Permissions for SharePoint and OneDrive |
| --- | --- | --- | --- |
| ContosoM365AKV01 | **Yes** | No | No |
| ContosoM365AKV02 | **Yes** | No | No |
| ContosoEXOAKV01 | No | **Yes** | No |
| ContosoEXOAKV02 | No | **Yes** | No |
| ContosoSPOAKV01 | No | No | **Yes** |
| ContosoSPOAKV02 | No | No | **Yes** |

![Vault Configuration](media/customerkeyvaultconfiguration.png)

Creating key vaults also requires setting up Azure resource groups. Key vaults require a small amount of storage, and logging (if enabled) also stores data. As a best practice, Microsoft recommends assigning different administrators to manage each resource group. These roles should align with the admins responsible for managing the associated Customer Key resources.

For Exchange, a DEP is scoped at the mailbox level. Each mailbox can have only one policy assigned, and you can create up to 50 policies. A SharePoint policy covers all data in an organization's geographic location (or geo), while a multi-workload policy covers supported workloads across all users in the organization.

Important

If you're using Customer Key for Multiple Workloads, Exchange, and SharePoint and OneDrive, make sure to create two Azure Key Vaults for each workload. This means you need a total of six key vaults.

### Assign permissions to each Azure Key Vault

Assign the required permissions to each key vault using [Azure role-based access control (Azure RBAC)](/en-us/azure/role-based-access-control/overview) in the Azure portal. This section explains how to apply the correct permissions using RBAC.

#### Assigning permissions using RBAC method

To assign (`wrapKey`, `unwrapKey`, and `get`) on your **Azure Key Vault**, assign the **Key Vault Crypto Service Encryption User** role to the appropriate Microsoft 365 app. See [Grant permission to applications to access an Azure Key Vault using Azure RBAC](/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli).

When assigning the role, search for the following app names in your tenant:

- **Multiple Workloads**: `M365DataAtRestEncryption`
- **Exchange**: `Office 365 Exchange Online`
- **SharePoint and OneDrive**: `Office 365 SharePoint Online`

If you don't see the app you're looking for, make sure you register the app in the tenant.

For more information about assigning roles and permissions, see [Use role-based access control to manage access to your Azure subscription resources](/en-us/azure/active-directory/role-based-access-control-configure).

#### Assigning user roles

Customer Key requires both **Key Vault Administrators** (for daily key management tasks) and **Key Vault Contributors** (for permission and role assignment). By design, Administrators can't delete keys to prevent data loss.

For detailed steps, see [Azure built-in roles for Key Vault data plane operations](/en-us/azure/key-vault/general/rbac-guide?tabs=azurepowershell#azure-built-in-roles-for-key-vault-data-plane-operations).

### Add a key to each Key Vault either by creating or importing a key

There are two ways to add keys to an Azure Key Vault: you can create a key directly in the vault or import an existing key. Creating a key in Azure is simpler, but importing a key gives you full control over how the key is generated. Use RSA keys. Customer Key supports RSA key lengths up to 4,096 bits. Azure Key Vault doesn't support wrapping and unwrapping with elliptical curve (EC) keys.

To add a key to each vault, see [Add-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/add-azkeyvaultkey).

If you prefer to generate a key on-premises and then import it into Azure, perform the steps in [How to generate and transfer HSM-protected keys for Azure Key Vault](/en-us/azure/key-vault/keys/hsm-protected-keys). Use the Azure instructions to add a key to each Key Vault.

### Verify expiration date of your keys

To check that your keys don't have an expiration date, run the [Get-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/get-azkeyvault) cmdlet.

For Azure Key Vault:

```powershell
Get-AzKeyVaultKey -VaultName <vault name>
```

Customer Key can't use expired keys. Any operation using an expired key fails and can cause service outages.

Once set, an expiration date can't be removed, but you can change it. If you must use a key with an expiration date, update it to `12/31/9999` and use the legacy onboarding method.

Caution

Don't set expiration dates on encryption keys used with Customer Key. The Customer Key Onboarding Service only accepts keys without an expiration date.

To change the expiration date, use the [Update-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/update-azkeyvaultkey) cmdlet:

```powershell
Update-AzKeyVaultKey -VaultName <vault name> -Name <key name> -Expires (Get-Date -Date "12/31/9999")
```

### Back up Azure Key Vault Key

After you create or modify a key, make sure to immediately back it up. Store backup copies in both online and offline locations to help prevent data loss.

To back up a key in Azure Key Vault, use the [Backup-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/backup-azkeyvaultkey) cmdlet.

Important

If a key is deleted without a backup, it can't be recovered. Always create a backup after any key change or creation.

### Obtain the URI for each Azure Key Vault key

After you set up your Key Vaults and add your keys, run the following command to get the URI for each key. You need these URIs when creating and assigning DEPs; so, be sure to save them somewhere secure.

Run the following command in Azure PowerShell—once for each Key Vault:

```powershell
(Get-AzKeyVaultKey -VaultName <vault name>).Id
```

# [Managed HSM](#tab/mhsm)
### Set up Customer Key with Managed HSM

Microsoft 365 Customer Key supports RSA keys stored in Azure Key Vault Managed HSM, a FIPS 140-2 Level 3 compliant solution.

Managed HSM is a fully managed, highly available, single-tenant service that helps safeguard cryptographic keys using FIPS 140-2 Level 3–validated hardware security modules (HSMs). It supports cloud applications that require high-assurance key protection.

For more information about the service, see the [Azure Key Vault Managed HSM overview](/en-us/azure/key-vault/managed-hsm/overview).

To set up Customer Key using Managed HSM, follow the steps in the order listed. This article includes detailed guidance for HSM-specific tasks and links to shared setup steps from the standard Customer Key process.

Important

Managed HSM uses a different set of PowerShell cmdlets than classic Azure Key Vault. Make sure to use the correct tooling in each step.

### Create a resource group, provision, and activate a Managed HSM

Unlike standard Azure Key Vault, which typically requires three pairs of key vaults (six total) to support all workloads, Managed HSM only requires **two instances**, one per Azure subscription, regardless of how many Customer Key workloads you plan to use.

Important

Managed HSM has soft delete automatically enabled and can't be disabled. However, you **must** enable **purge protection** during the initial HSM creation process. Customer Key requires purge protection to be enabled to ensure keys can't be permanently deleted during the retention period. For guidance on enabling purge protection, see [Managed HSM recovery management](/en-us/azure/key-vault/managed-hsm/recovery?tabs=azure-cli). If you plan to enable firewall on your Managed HSMs, ensure you select the option for [Allow Trusted Microsoft Services](/en-us/azure/key-vault/managed-hsm/configure-network-security?tabs=azure-portal)

To provision and activate your Managed HSM instances, follow the steps in the [Managed HSM Quickstart using PowerShell](/en-us/azure/key-vault/managed-hsm/quick-create-powershell).

![Diagram of simplified HSM setup with two Managed HSM instances](media/customerkeymanagedhsm.png)

### Assign permissions to each Managed HSM

Managed HSM uses local role-based access control (RBAC) to manage permissions. To assign the required access for Customer Key, you must grant the **Managed HSM Crypto Service Encryption User** role to the appropriate Microsoft 365 application.

This role grants the following permissions on the key: `wrapKey`, `unwrapKey`, and `get`.

For more information, see [Managed HSM role management](/en-us/azure/key-vault/managed-hsm/role-management).

When assigning the role, search for the following Microsoft 365 app names:

- **Multiple workloads**: `M365DataAtRestEncryption`
- **Exchange**: `Office 365 Exchange Online`
- **SharePoint and OneDrive**: `Office 365 SharePoint Online`

If you don’t see the expected app in your tenant, verify that you [registered the required service principals](customer-key-set-up#register-the-required-service-principals).

To learn more about assigning roles, see [Use role-based access control to manage access to your Azure subscription resources](/en-us/azure/active-directory/role-based-access-control-configure).

### Assign user roles to your Managed HSM

**Managed HSM Administrators** are responsible for day-to-day management tasks such as `backup`, `create`, `get`, `import`, `list`, and `restore`.

For role definitions and guidance on assigning user roles, see [Assigning user roles](customer-key-set-up#assigning-user-roles).

### Add a key to each Managed HSM

Managed HSM supports only HSM-protected keys. When creating keys for use with Customer Key, you must use the **RSA-HSM** key type.

To create a key directly in Managed HSM, follow the steps in [Add-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/add-azkeyvaultkey).

If you prefer to generate a key on-premises and then import it into your Managed HSM, see [How to generate and transfer HSM-protected keys for Azure Key Vault](/en-us/azure/key-vault/keys/hsm-protected-keys).

Use these instructions to create one key in each Managed HSM instance.

### Verify the expiration date of your Managed HSM keys

To check that your keys don't have an expiration date, run the [Get-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/get-azkeyvault) cmdlet.

For Managed HSM:

```powershell
Get-AzKeyVaultKey -HsmName <HSM name>
```

Customer Key can't use expired keys. Any operation using an expired key fails and can cause service outages.

Once set, an expiration date can't be removed, but you can change it. If you must use a key with an expiration date, update it to `12/31/9999` and use the legacy onboarding method.

To change the expiration date, use the [Update-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/update-azkeyvaultkey) cmdlet:

```powershell
Update-AzKeyVaultKey -HsmName <HSM name> -Name <key name> -Expires (Get-Date -Date "12/31/9999")
```

### Back up your Managed HSM Key

To back up your Managed HSM Key, see [Backup-AzKeyVaultKey](/en-us/powershell/module/az.keyvault/backup-azkeyvaultkey).

### Obtain the URI for each Managed HSM key

After you set up your Managed HSMs and add your keys, run the following command to get the URI for each key. You need these URIs when creating and assigning data encryption policies (DEPs), so be sure to save them somewhere secure.

Run the following command in Azure PowerShell—once for each Managed HSM:

```powershell
(Get-AzKeyVaultKey -HsmName <HSM name>).Id
```

---

Tip

Moving a key vault across resource groups within the same subscription is supported for Customer Key tenants and doesn’t cause downtime.

## Onboard using the Customer Key Onboarding Service

The Microsoft 365 Customer Key Onboarding Service allows you to enable Customer Key in your tenant. This service automatically validates the required Customer Key resources. If you'd prefer, you can validate your resources separately before proceeding with enablement.

Important

This service isn't currently available for the following scenarios:

- **Special clouds tenant**: See Onboard to Customer Key for special cloud environments.
- **SharePoint and OneDrive**: See Onboard to Customer Key for SharePoint and OneDrive.

The account used for onboarding **must** have the following permissions:

1. [Service principal registration permissions](/en-us/powershell/azure/create-azure-service-principal-azureps): To register the required service principals.
2. [Reader role](/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli#key-vault-scope-role-assignment): On each Azure Key Vault used in the onboarding cmdlet.

### Install the `M365CustomerKeyOnboarding` PowerShell module

1. Sign in to your Azure subscription with Azure PowerShell. For guidance, see [Sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps).
2. Install the **latest version** of the `M365CustomerKeyOnboarding` module from the [PowerShell Gallery](https://www.powershellgallery.com/packages/M365CustomerKeyOnboarding).

- To confirm you're using the latest version, check the **Version History** tab at the bottom of the module page.
- Copy and paste the install command into your session and run it.
- If you're prompted, select **Yes to All** to continue.

### Using the two different onboarding modes

There are two different onboarding modes available when using the Customer Key Onboarding Service: **Validate**, and **Enable**. Each mode serves a different purpose in the onboarding process.

When running the cmdlet (as guided in Create an Onboarding request), specify the mode using the `-OnboardingMode` parameter.

#### Validate

Use the `Validate` mode to confirm that your Customer Key resource configuration is correct. This mode doesn’t make any changes to your environment.

Important

You can run this mode as many times as needed, especially after making changes to your configuration.

#### Enable

Use the `Enable` mode when you're ready to onboard your tenant to Customer Key. This mode enables Customer Key for the workload you specify using the `-Scenario` parameter.

If you want to enable Customer Key for both **Multiple Workloads** and **Exchange**, run the cmdlet twice, once for each workload.

Before running in Enable mode, make sure your validation results show **Passed** under `ValidationResult`.

Important

Your resources must pass all checks in `Validate` mode for the onboarding process to succeed in Enable mode.

### Creating an onboarding request

The first step in the onboarding process is to create a new request. In PowerShell, you can store the results of a cmdlet in a variable using the `$` symbol followed by the variable name.

In this example, the onboarding request is stored in a variable named `$request`:

```powershell
$request = New-CustomerKeyOnboardingRequest -Organization <tenantID> -Scenario <Scenario> -Subscription1 <subscriptionID1> -KeyIdentifier1 <KeyURI1> -Subscription2 <subscriptionID2> -KeyIdentifier2 <KeyURI2> -OnboardingMode <OnboardingMode>
```

| Parameter | Description | Example |
| --- | --- | --- |
| `-Organization` | Your tenant ID (GUID format) | `aaaabbbb-0000-cccc-1111-dddd2222eeee` |
| `-Scenario` | Workload: `MDEP` (Multiple Workloads) or `EXO` (Exchange) | `MDEP` or `EXO` |
| `-Subscription1` | First Azure subscription ID | `aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e` |
| `-KeyIdentifier1` | Key URI for first AKV/HSM key | `https://exampleVault1.vault.azure.net/keys/customerKey1` |
| `-Subscription2` | Second Azure subscription ID | `bbbb1b1b-cc2c-dd3d-ee4e-ffffff5f5f5f` |
| `-KeyIdentifier2` | Key URI for second AKV/HSM key | `https://exampleVault2.vault.azure.net/keys/customerKey2` |
| `-OnboardingMode` | `Validate` (test only) or `Enable` (test and enable) | `Validate` or `Enable` |

### Sign in with your tenant admin credentials

When prompted, a browser window opens. Sign in using your tenant admin account with the necessary privileges to complete onboarding.

![Prompt to sign in with a privileged account](media/ckologin.png)

#### View validation and enablement details

After successfully signing in, return to your PowerShell window. Run the variable you used when creating the onboarding request to view its output:

```powershell
$request
```

![CKO Request Output](media/ckorequestoutput.png)

You receive an output that includes `ID`, `CreatedDate`, `ValidationResult`, and `EnablementResult`.

| Output | Description |
| --- | --- |
| `ID` | ID associated with the created onboarding request. |
| `CreatedDate` | Date on which the request was created. |
| `ValidationResult` | Indicator of successful/unsuccessful validation. |
| `EnablementResult` | Indicator of successful/unsuccessful enablement. |

A tenant that's ready to use Customer Key shows **Success** for both `ValidationResult` and `EnablementResult`.

If both values show **Success**, proceed to Next Steps.

### Troubleshooting failed validations details

If validation fails during onboarding, perform the following steps to investigate the cause. This process helps identify which Customer Key resources are misconfigured.

1. List all onboarding requests for your tenant to find the `RequestID` of the one you want to investigate:

```powershell
Get-CustomerKeyOnboardingRequest -OrganizationID <OrganizationID>
```

1. Store the specific onboarding request into a variable:

```powershell
$request = Get-CustomerKeyOnboardingRequest -OrganizationID <OrganizationID> -RequestID <RequestID>
```

1. View the failed validation details:

```powershell
$request.FailedValidations
```

![Example of failed validation output in PowerShell](media/ckofailedvalidation.png)

Each validation rule includes the following fields:

- **ExpectedValue**: What the resource configuration should be.
- **ActualValue**: What was detected in your environment.
- **Scope**: The first five characters of the subscription ID that helps you identify which subscription (and its associated Key Vault) has the issue.
- **Details**: Describes the root cause and offers guidance to resolve the problem.

The following table summarizes common validation rules and how to resolve failures:

| RuleName | Description | Solution |
| --- | --- | --- |
| `OrganizationHasRequiredServicePlan` | Verifies whether your organization has the required licenses for *Exchange*. | See Prerequisites. |
| `EligibleLicenseCount` | Verifies whether your organization has the required licenses for *Multiple Workloads*. | See [Microsoft Purview Customer Key Licensing](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-customer-key). |
| `KeyNeverExpires` | Ensures that the key has no expiration date. | See the key expiration verification steps in Configuration-specific setup |
| `KeyOperationsSupported` | Verifies whether the key supports required operations for the workload. | See the permissions assignment steps in Configuration-specific setup |
| `RecoveryLevel` | Checks if the key recovery level is `Recoverable`. | Ensure both soft delete and purge protection are enabled. See Enabling Soft Delete and Purge Protection for Azure Key Vault or Create a resource group provision, and activate a Managed HSM for Managed HSM. |
| `SubscriptionInRequestOrganization` | Confirms that your Azure subscription belongs to your organization. | Make sure the subscription was created within the specified tenant. |
| `SubscriptionsCountPerScenario` | Confirms that two subscriptions were provided. | Make sure your onboarding request includes **two** subscriptions. |
| `SubscriptionUniquePerScenario` | Ensures you're using two unique subscriptions per scenario. | Double-check that both subscription IDs are different. |
| `VaultExistsinSubscription` | Confirms that the AKV/Managed HSM is part of the given subscription. | Verify whether the Key Vault/HSM was created in the correct subscription. |

### Checking passed validations

To view which validations were successful during the onboarding process, perform the following steps:

1. Store the specific onboarding request into the variable '$request'

```powershell
$request = Get-CustomerKeyOnboardingRequest -OrganizationID <OrganizationID> -RequestID <RequestID>
```

1. Run the following command to display all passed validations:

```powershell
$request.PassedValidations
```

This command returns a list of all the validations that passed successfully for the selected onboarding request.

![CKO PassedValidation](media/ckopassedvalidation.png)

## Onboard to Customer Key for special cloud environments

If your tenant is located in **GCC-H**, **DoD**, or **M365 operated by 21Vianet**, complete all required Customer Key setup steps first.

- For **GCC-H** and **DoD** tenants, contact [Microsoft Support](https://support.microsoft.com/microsoft-365) and request onboarding for U.S. government tenants.
- For customers in Microsoft 365 operated by 21Vianet (China), configure your Customer Key resources using [Azure operated by 21Vianet portal](https://portal.azure.cn). Then, contact [Microsoft Support](https://support.microsoft.com/microsoft-365) and request onboarding for your tenant.

Note

For SharePoint and OneDrive, customers in Microsoft 365 operated by 21Vianet can onboard directly (no support request required) after completing the key vault creation process by following the steps in [Create a premium Azure Key Vault in each subscription](customer-key-set-up#create-a-premium-azure-key-vault-in-each-subscription) and then [Create a DEP for use with SharePoint and OneDrive](customer-key-manage#create-a-dep-for-use-with-sharepoint-and-onedrive).

## Onboard to Customer Key for SharePoint and OneDrive

To onboard to Customer Key for SharePoint and OneDrive, your Azure Key Vaults must meet the following prerequisites:

1. Enable both soft delete and purge protection during the initial vault creation process. See [Enabling Soft Delete and Purge Protection](/en-us/purview/customer-key-set-up?tabs=akv) for Azure Key Vault.

If this prerequisite is satisfied, perform the steps in [Create a DEP for use with SharePoint and OneDrive](customer-key-manage#create-a-dep-for-use-with-sharepoint-and-onedrive).