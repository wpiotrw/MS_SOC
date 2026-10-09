---
layout: Conceptual
title: Store FSLogix profile containers on Azure Files using Microsoft Entra ID - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/how-to-configure-profile-container-entra-id-hybrid
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Set up an FSLogix profile container on an Azure file share with your Microsoft Entra domain.
author: sipastak
zone_pivot_groups: fslogix-identity-types
ms.topic: how-to
ms.date: 2026-03-09T00:00:00.0000000Z
ms.author: sipastak
locale: en-us
document_id: 85dfa3b6-b7f5-c747-a79f-1a85d3c64ff6
document_version_independent_id: 85dfa3b6-b7f5-c747-a79f-1a85d3c64ff6
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/how-to-configure-profile-container-entra-id-hybrid.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: how-to-configure-profile-container-entra-id-hybrid
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/how-to-configure-profile-container-entra-id-hybrid.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 776adfe3-ae6b-cb20-3a62-8824bb23c88f
---

# Store FSLogix profile containers on Azure Files using Microsoft Entra ID - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

In this article, you'll learn how to create and configure an Azure Files share for Microsoft Entra Kerberos authentication. This configuration allows you to store FSLogix profiles to be accessed by different users, based on configuration:

- By hybrid user identities from Microsoft Entra joined or Microsoft Entra hybrid joined session hosts without requiring network line-of-sight to domain controllers. This feature is supported in the Azure cloud, Azure for US Government, and Azure operated by 21Vianet.
- By cloud-only identities or external identities. This feature is only supported in the Azure cloud.

Microsoft Entra Kerberos enables Microsoft Entra ID to issue the necessary Kerberos tickets to access the file share with the industry-standard SMB protocol.

## Prerequisites

::: zone pivot="hybrid-identities"

Before deploying this solution, verify that your environment [meets the requirements](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable?tabs=azure-portal#prerequisites) to configure Azure Files with Microsoft Entra Kerberos authentication.

When used for FSLogix profiles in Azure Virtual Desktop, the session hosts don't need to have network line-of-sight to the domain controller (DC). However, a system with network line-of-sight to the DC is required to configure the permissions on the Azure Files share.

::: zone-end

::: zone pivot="cloud-only-or-external-identities"

Before deploying this solution, verify that your environment [meets the requirements](https://go.microsoft.com/fwlink/?linkid=2338978) to configure Azure Files with Microsoft Entra Kerberos authentication for cloud-only or external identities.

::: zone-end

## Configure your Azure storage account and file share

::: zone pivot="hybrid-identities"

To store your FSLogix profiles on an Azure file share:

1. [Create an Azure Storage account](/en-us/azure/storage/files/storage-how-to-create-file-share#create-a-storage-account) if you don't already have one.

    Note

    Your Azure Storage account can't authenticate with both Microsoft Entra ID and a second method like Active Directory Domain Services (AD DS) or Microsoft Entra Domain Services. You can only use one authentication method.
2. [Create an Azure Files share](/en-us/azure/storage/files/storage-how-to-create-file-share#create-a-file-share) under your storage account to store your FSLogix profiles if you haven't already.
3. [Enable Microsoft Entra Kerberos authentication on Azure Files](/en-us/azure/storage/files/storage-files-identity-auth-azure-active-directory-enable) to enable access from Microsoft Entra joined VMs. This includes the following steps:

    1. [Enable Microsoft Entra Kerberos authentication for the storage account](/en-us/azure/storage/files/storage-files-identity-auth-azure-active-directory-enable#enable-microsoft-entra-kerberos-authentication). This will create the Entra ID app registration for the storage account and allow you to provide directory and file-level permissions to groups managed through Entra ID.
    2. [Assign share-level permissions](/en-us/azure/storage/files/storage-files-identity-assign-share-level-permissions). You can assign share-level permissions to your users either by configuring **default share-level permissions** in the identity source page, or by creating **Azure Role-based access control (RBAC) roles**.
    3. [Configure the storage permissions for profile containers](/en-us/fslogix/fslogix-storage-config-ht). Review the recommended list of permissions for FSLogix profiles for allowing users to create and use their own profile, while also allowing admins to manage the share.
4. Configure the Entra ID app registration for the storage account to ensure that users can properly acquire tickets for their assigned Entra ID groups.

    1. [Grant admin consent to the new service principal](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#grant-admin-consent-to-the-new-service-principal). This grants the permissions for users to request Entra ID tokens for the storage account.
    2. [Disable multifactor authentication on the storage account](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#disable-multifactor-authentication-on-the-storage-account). This ensures the user can get the Entra ID token and Kerberos tickets while it happens silently during user logon, since there is no UX to perform step-up authentication.

::: zone-end

::: zone pivot="cloud-only-or-external-identities"

To store your FSLogix profiles on an Azure file share:

1. [Create an Azure Storage account](/en-us/azure/storage/files/storage-how-to-create-file-share#create-a-storage-account) if you don't already have one.

    Note

    Your Azure Storage account can't authenticate with both Microsoft Entra ID and a second method like Active Directory Domain Services (AD DS) or Microsoft Entra Domain Services. You can only use one authentication method.
2. [Create an Azure Files share](https://go.microsoft.com/fwlink/?linkid=2338978) under your storage account to store your FSLogix profiles if you haven't already, where you'll be able to manage permissions through a **Manage access** control.
3. [Enable Microsoft Entra Kerberos authentication on Azure Files](/en-us/azure/storage/files/storage-files-identity-auth-azure-active-directory-enable) to enable access from Microsoft Entra joined VMs. This includes the following steps:

    1. [Enable Microsoft Entra Kerberos authentication for the storage account](/en-us/azure/storage/files/storage-files-identity-auth-azure-active-directory-enable#enable-microsoft-entra-kerberos-authentication). This will create the Entra ID app registration for the storage account and allow you to provide directory and file-level permissions to groups managed through Entra ID.
    2. [Assign share-level permissions](/en-us/azure/storage/files/storage-files-identity-assign-share-level-permissions). You can assign share-level permissions to your users either by configuring **default share-level permissions** in the identity source page, or by creating **Azure Role-based access control (RBAC) roles**.
    3. [Configure the storage permissions for profile containers](/en-us/fslogix/fslogix-storage-config-ht). Review the recommended list of permissions for FSLogix profiles for allowing users to create and use their own profile, while also allowing admins to manage the share. When Entra Kerberos is configured, you'll see a **Manage access** tab to assign permissions, which is the recommended configuration option for cloud-only and external identity users. ![Screenshot that shows an Azure file share with the manage access action option available to select.](media/file-share-manage-access-action.png)![Screenshot that shows the Manage access page, allowing you to add permissions for Entra users or groups, or Security IDs.](media/file-share-manage-access-page.png)
4. Configure the Entra ID app registration for the storage account to ensure that users can properly acquire tickets for their assigned Entra ID groups.

    1. [Grant admin consent to the new service principal](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#grant-admin-consent-to-the-new-service-principal). This grants the permissions for users to request Entra ID tokens for the storage account.
    2. [Disable multifactor authentication on the storage account](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#disable-multifactor-authentication-on-the-storage-account). This ensures the user can get the Entra ID token and Kerberos tickets while it happens silently during user logon, since there is no UX to perform step-up authentication.
    3. [Add an app manifest tag to enable cloud-only groups support](/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#enable-cloud-only-groups-support-mandatory-for-cloud-only-identities). This ensures that Entra will include cloud-only Entra ID groups in the Kerberos ticket, instead of only on-premises groups. When complete, your app manifest should look like this with the `kdc_enable_cloud_group_sids` added in the **tags** portion of the app manifest: ![Screenshots that shows a manifest of an app registration, with the kdc_enable_cloud_group_sids tag added to the tags array.](media/app-manifest-enable-cloud-groups-tag.png)

::: zone-end

## Configure your local Windows device

To access Azure file shares from a Microsoft Entra joined VM for FSLogix profiles, you must configure the local Windows device your FSLogix profiles are being loaded onto. To configure your device:

1. Enable the Microsoft Entra Kerberos functionality using one of the following methods.

    - Configure this Intune [Policy CSP](/en-us/windows/client-management/mdm/policy-configuration-service-provider) with [settings catalog](/en-us/mem/intune/configuration/settings-catalog) and apply it to the session host: [Kerberos/CloudKerberosTicketRetrievalEnabled](/en-us/windows/client-management/mdm/policy-csp-kerberos#kerberos-cloudkerberosticketretrievalenabled).

    Note

    Windows multi-session client operating systems now support this setting provided it is configured with Settings Catalog, where the setting is now available. Learn more at [Using Azure Virtual Desktop multi-session with Intune](/en-us/mem/intune/fundamentals/azure-virtual-desktop-multi-session).

    - Enable this Group policy on your device. The path will be one of the following, depending on the version of Windows you use:
    - `Administrative Templates\System\Kerberos\Allow retrieving the cloud kerberos ticket during the logon`
    - `Administrative Templates\System\Kerberos\Allow retrieving the Azure AD Kerberos Ticket Granting Ticket during logon`
    - Create the following registry value on your device: `reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters /v CloudKerberosTicketRetrievalEnabled /t REG_DWORD /d 1`

::: zone pivot="hybrid-identities"

1. When you use Microsoft Entra ID with a roaming profile solution like FSLogix, the credential keys in Credential Manager must belong to the profile that's currently loading. This lets you load your profile on many different VMs instead of being limited to just one. To enable this setting, create a new registry value by running the following command:

    ```
    reg add HKLM\Software\Policies\Microsoft\AzureADAccount /v LoadCredKeyFromProfile /t REG_DWORD /d 1
    ```

    Note

    The session hosts don't need network line-of-sight to the domain controller.

::: zone-end

::: zone pivot="cloud-only-or-external-identities"

1. When you use Microsoft Entra ID with a roaming profile solution like FSLogix, the credential keys in Credential Manager must belong to the profile that's currently loading. This lets you load your profile on many different VMs instead of being limited to just one. To enable this setting, create a new registry value by running the following command:

    ```
    reg add HKLM\Software\Policies\Microsoft\AzureADAccount /v LoadCredKeyFromProfile /t REG_DWORD /d 1
    ```

::: zone-end

### Configure FSLogix on your local Windows device

This section shows you how to configure your local Windows device with FSLogix. You'll need to follow these instructions every time you configure a device. There are several options available that ensure the registry keys are set on all session hosts. You can set these options in an image or configure a group policy.

To configure FSLogix:

1. [Update or install FSLogix](/en-us/fslogix/install-ht) on your device, if needed.

    Note

    If you're configuring a session host created using the Azure Virtual Desktop service, FSLogix should already be pre-installed.
2. Follow the instructions in [Configure profile container registry settings](/en-us/fslogix/configure-profile-container-tutorial#configure-profile-container-registry-settings) to create the **Enabled** and **VHDLocations** registry values. Set the value of **VHDLocations** to `\\<Storage-account-name>.file.core.windows.net\<file-share-name>`.

## Test your deployment

Once you've installed and configured FSLogix, you can test your deployment by signing in with a user account that's been assigned to an application group on the host pool. The user account you sign in with must have permission to use the file share.

If the user has signed in before, they'll have an existing local profile that the service will use during this session. To avoid creating a local profile, either create a new user account to use for tests or use the configuration methods described in [Tutorial: Configure profile container to redirect user profiles](/en-us/fslogix/configure-profile-container-tutorial/) to enable the *DeleteLocalProfileWhenVHDShouldApply* setting.

Finally, verify the profile created in Azure Files after the user has successfully signed in:

1. Open the Azure portal and sign in with an administrative account.
2. From the sidebar, select **Storage accounts**.
3. Select the storage account you configured for your session host pool.
4. From the sidebar, select **File shares**.
5. Select the file share you configured to store the profiles.
6. If everything's set up correctly, you should see a directory with a name that's formatted like this: `<user SID>_<username>`.