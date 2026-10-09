---
layout: Conceptual
title: App Attach in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/app-attach-overview
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: mmoyaaceves
manager: eliotgra
ms.author: mmoyaaceves
ms.service: azure-virtual-desktop
description: Learn how you can dynamically attach applications from an application package to a user session using App Attach in Azure Virtual Desktop.
ms.topic: concept-article
ms.date: 2026-04-22T00:00:00.0000000Z
locale: en-us
document_id: 9660d14a-0aa2-a577-4b3d-1a1f89b6b57b
document_version_independent_id: 9660d14a-0aa2-a577-4b3d-1a1f89b6b57b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/app-attach-overview.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: app-attach-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/app-attach-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/01a89bec-e73f-4ce0-a00a-ae34ad62e5fe
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/50038ab9-5431-4515-9dfc-c24291ef4fce
platformId: 839dcdf7-2908-57a3-b069-f179a96f40e0
---

# App Attach in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn

App Attach enables you to dynamically attach applications from an application package to a user session in Azure Virtual Desktop. Applications aren't installed locally on session hosts or images, making it easier to create custom images for your session hosts, and reducing operational overhead and costs for your organization. Applications run within containers, which separate user data, the operating system, and other applications, increasing security and making them easier to troubleshoot.

Here are some of the key benefits of App Attach:

- Applications are delivered using RemoteApp or as part of a desktop session. Permissions are applied per application per user, giving you greater control over which applications your users can access in a remote session. Desktop users only see the App Attach applications assigned to them.
- The same application package can be used across multiple host pools.
- Applications can run on any session host running a Windows client or supported Windows server operating system in the same Azure region as the application package.
- Applications can be upgraded to a new application version with a new disk image without the need for a maintenance window.
- Users can run multiple versions of the same application concurrently on the same session host.
- Telemetry for usage and health is available through Azure Log Analytics.

You can use the following application package types and file formats:

| Package type | File formats |
| --- | --- |
| MSIX and MSIX bundle | `.msix``.msixbundle` |
| Appx and Appx bundle | `.appx``.appxbundle` |
| App-V | `.appv` |

MSIX and Appx are Windows application package formats that provide a modern packaging experience to Windows applications. Applications run within containers, which separate user data, the operating system, and other applications, increasing security and making them easier to troubleshoot. MSIX and Appx are similar, where the main difference is that MSIX is a superset of Appx. MSIX supports all the features of Appx, plus other features that make it more suitable for enterprise use.

[Microsoft Application Virtualization](/en-us/windows/application-management/app-v/appv-getting-started) (App-V) for Windows delivers Win32 applications to users as virtual applications. Virtual applications are installed on centrally managed servers and delivered to users as a service in real time and on an as-needed basis. Users launch virtual applications from familiar access points and interact with them as if they were installed locally.

You can get MSIX packages from software vendors or you can [create an MSIX package from an existing installer](/en-us/windows/msix/packaging-tool/create-an-msix-overview). To learn more about MSIX, see [What is MSIX?](/en-us/windows/msix/overview).

## How a user gets an application

You can assign different applications to different users in the same host pool or on the same session host. During sign-in, all three of the following requirements must be met for the user to get the right application at the right time:

- The application must be assigned to the host pool. Assigning the application to the host pool enables you to be selective about which host pools the application is available on to ensure that the right hardware resources are available for use by the application. For example, if an application is graphics-intensive, you can ensure it only runs on a host pool with GPU-optimized session hosts.
- The user must be able to sign-in to session hosts in the host pool, so they must be in a Desktop or RemoteApp application group. For a RemoteApp application group, the App Attach application must be added to the application group, but you don't need to add the application to a desktop application group.
- The application must be assigned to the user. You can use a group or a user account.

If all of these requirements are met, the user gets the application. This process provides control over who gets an application on which host pool and also how it's possible for users within a single host pool or even signed in to the same multi-session session host to get different application combinations. Users who don’t meet the requirements don't get the application.

## Application images

Before you can use MSIX application packages with Azure Virtual Desktop, you need to [Create an MSIX image](app-attach-create-msix-image) from your existing application packages. Alternatively, you can use an [App-V package instead](/en-us/windows/application-management/app-v/appv-creating-and-managing-virtualized-applications). You then need to store each MSIX image or App-V package on a file share that's accessible by your session hosts. For more information on the requirements for a file share, see File share.

### Disk image types

For MSIX and Appx disk images, you can use *Composite Image File System (CimFS)*, *VHDX*, or *VHD*, but we don't recommend using VHD. Mounting and unmounting CimFS images is faster than VHD and VHDX images and also consumes less CPU and memory. We only recommend using CimFS for your application images if your session hosts are running Windows 11.

A CimFS image is a combination of several files: one file has the `.cim` file extension and contains metadata, together with at least two other files, one starting with `objectid_` and the other starting with `region_` that contain the actual application data. The files accompanying the `.cim` file don't have a file extension. The following table is a list of example files you'd find for a CimFS image:

| File name | Size |
| --- | --- |
| `MyApp.cim` | 1 KB |
| `objectid_b5742e0b-1b98-40b3-94a6-9cb96f497e56_0` | 27 KB |
| `objectid_b5742e0b-1b98-40b3-94a6-9cb96f497e56_1` | 20 KB |
| `objectid_b5742e0b-1b98-40b3-94a6-9cb96f497e56_2` | 42 KB |
| `region_b5742e0b-1b98-40b3-94a6-9cb96f497e56_0` | 428 KB |
| `region_b5742e0b-1b98-40b3-94a6-9cb96f497e56_1` | 217 KB |
| `region_b5742e0b-1b98-40b3-94a6-9cb96f497e56_2` | 264,132 KB |

The following table is a performance comparison between VHDX and CimFS. These numbers were the result of a test run with 500 files of 300 MB each per format and the tests were performed on a [DSv4 Azure virtual machine](/en-us/azure/virtual-machines/dv4-dsv4-series).

| Metric | VHD | CimFS |
| --- | --- | --- |
| Average mount time | 356 ms | 255 ms |
| Average unmount time | 1615 ms | 36 ms |
| Memory consumption | 6% (of 8 GB) | 2% (of 8 GB) |
| CPU (count spike) | Maxed out multiple times | No effect |

## Application registration

App Attach mounts disk images or App-V packages containing your applications from a file share to a user's session during sign-in, then a registration process makes the applications available to the user. There are two types of registration:

- **On-demand**: applications are only partially registered at sign-in and the full registration of an application is postponed until the user starts the application. On-demand is the registration type we recommend you use as it doesn't affect the time it takes to sign-in to Azure Virtual Desktop. On-demand is the default registration method.
- **Log on blocking**: each application you assign to a user is fully registered. Registration happens while the user is signing in to their session, which might affect the sign-in time to Azure Virtual Desktop.

Important

All MSIX and Appx application packages include a certificate. You're responsible for making sure the certificates are trusted in your environment. Self-signed certificates are supported with the appropriate chain of trust.

App Attach doesn't limit the number of applications users can use. You should consider your available network throughput and the number of open handles per file (each image) your file share supports, as it might limit the number of users or applications you can support. For more information, see File share.

## Application state

Application packages are set as **active** or **inactive**. Packages set to active makes the application available to users. Azure Virtual Desktop ignores packages set to **inactive** and aren't added when a user signs in.

## New versions of applications

You can add a new version of an application by supplying a new image containing the updated application. You can use this new image in two ways:

- **Side by side**: create a new application using the new disk image and assign it to the same host pools and users as the existing application.
- **In-place**: create a new image where the version number of the application changes, then update the existing application to use the new image. The version number can be higher or lower, but you can't update an application with the same version number. Don't delete the existing image until all users are finished using it.

Once updated, users get the updated application version the next time they sign-in. Users don't need to stop using the previous version to add a new version.

## Identity providers

Here are the identity providers you can use with App Attach:

| Identity provider | Status |
| --- | --- |
| Microsoft Entra ID | Supported |
| Active Directory Domain Services (AD DS) | Supported |
| Microsoft Entra Domain Services | Not supported |

## File share

App Attach requires that your application images are stored on an SMB file share, which is then mounted on each session host during sign-in. App Attach doesn't have dependencies on the type of storage fabric the file share uses. We recommend using [Azure Files](/en-us/azure/storage/files/storage-files-introduction) as it's compatible with Microsoft Entra ID or Active Directory Domain Services, and offers great value between cost and management overhead.

You can also use [Azure NetApp Files](/en-us/azure/azure-netapp-files/azure-netapp-files-introduction), but that requires your session hosts to be joined to Active Directory Domain Services.

The following sections provide some guidance on the permissions, performance, and availability required for the file share.

### Permissions

Each session host mounts application images from the file share. You need to configure NTFS and share permissions to allow each session host computer object read access to the files and file share. How you configure the correct permission depends on which storage provider and identity provider you're using for your file share and session hosts.

- To use Azure Files when your session hosts joined to Microsoft Entra ID, you need to assign the [Reader and Data Access](/en-us/azure/role-based-access-control/built-in-roles#reader-and-data-access) Azure role-based access control (RBAC) role to both the **Azure Virtual Desktop** and **Azure Virtual Desktop ARM Provider** service principals. This RBAC role assignment allows your session hosts to access the storage account using access keys or Microsoft Entra.
- To learn how to assign an Azure RBAC role to the Azure Virtual Desktop service principals, see [Assign RBAC roles to the Azure Virtual Desktop service principals](service-principal-assign-roles). In a future update, you won't need to assign the **Azure Virtual Desktop ARM Provider** service principal.

    For more information about using Azure Files with session hosts that are joined to Microsoft Entra ID, Active Directory Domain Services, or Microsoft Entra Domain Services, see [Overview of Azure Files identity-based authentication options for SMB access](/en-us/azure/storage/files/storage-files-active-directory-overview).

    Warning

    Assigning the **Azure Virtual Desktop ARM Provider** service principal to the storage account grants the Azure Virtual Desktop service to all data inside the storage account. We recommended you only store apps to use with App Attach in this storage account and rotate the access keys regularly.
- For Azure Files with Active Directory Domain Services, you need to assign the [Storage File Data SMB Share Reader](/en-us/azure/role-based-access-control/built-in-roles#storage-file-data-smb-share-reader) Azure role-based access control (RBAC) role as the [default share-level permission](/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions#share-level-permissions-for-all-authenticated-identities), and [configure NTFS permissions](/en-us/azure/storage/files/storage-files-identity-ad-ds-configure-permissions) to give read access to each session host's computer object.

    For more information about using Azure Files with session hosts that are joined to Microsoft Entra ID, Active Directory Domain Services, or Microsoft Entra Domain Services, see [Overview of Azure Files identity-based authentication options for SMB access](/en-us/azure/storage/files/storage-files-active-directory-overview).
- For Azure NetApp Files, you can [create an SMB volume](/en-us/azure/azure-netapp-files/azure-netapp-files-create-volumes-smb) and configure NTFS permissions to give read access to each session host's computer object. Your session hosts need to be joined to Active Directory Domain Services or Microsoft Entra Domain Services.

You can verify the permissions are correct by using [PsExec](/en-us/sysinternals/downloads/psexec). For more information, see [Check file share access](/en-us/troubleshoot/azure/virtual-desktop/troubleshoot-app-attach#check-file-share-access).

### User and Deployment Configuration Files

For **App-V packages delivered through App Attach**, you can use [App-V Dynamic Configuration](/en-us/microsoft-desktop-optimization-pack/app-v/appv-dynamic-configuration) files to customize application behavior. App Attach automatically detects standard configuration files that follow the expected naming convention. If they are in the same folder as the App Attach package and the xml is prefixed with the name of the App-V file, these files are automatically associated with the application package during processing. If the file path is \share\folder\filename.appv the examples below will be automatically detected and used with the package.

- \share\folder\filename\_UserConfig.xml
- \share\folder\filename\_DeploymentConfig.xml

```
$a = Get-AzWvdAppAttachPackage -SubscriptionId blahblah -ResourceGroupName blahblahrg -Name contosoPackage

$dependencyType = $a.GetType().Assembly.GetTypes() |
    Where-Object {
        $_.Name -eq 'MsixPackageDependencies' -and
        $_.Namespace -like '*DesktopVirtualization*'
    } |
    Select-Object -First 1

$newDependency = [System.Activator]::CreateInstance($dependencyType)
$newDependency.DependencyName = "FilePathToUserConfig"
$newDependency.Publisher = "Group Object Id"
$newDependency.MinVersion = 1
$dependencyList = $a.ImagePackageDependency
$dependencyList += $newDependency
Update-AzWvdAppAttachPackage -ImagePackageDependency $dependencyList -SubscriptionId blahblah -ResourceGroupName blahblahrg -Name contosoPackage

# Remove logic
$a = Get-AzWvdAppAttachPackage -SubscriptionId blahblah -ResourceGroupName blahblahrg -Name contosoPackage
$dependencyList = $a.ImagePackageDependency
$dependencyList  = $dependencyList | where-Object {$_.DependencyName -ne "FilePathToUserConfig"}
Update-AzWvdAppAttachPackage -ImagePackageDependency $dependencyList -SubscriptionId blahblah -ResourceGroupName blahblahrg -Name contosoPackage
 
```

User configuration files are evaluated at the user level, allowing different users to receive different application settings. Deployment configuration files, by contrast, are applied at the machine level and are shared by all users on the session host. At this time, user configuration is only supported on desktop connections, not remote app connections.

Advanced scenarios may require multiple user configuration files for the same application. In these cases, the additional user configuration files must be explicitly associated with the application package using PowerShell.

App attach checks the dependency object

- Has a file path specified in the **DependencyName** field that ends with UserConfig.xml
- Contains a **Publisher** field that identifies the Microsoft Entra security group that should receive that configuration. The value of the app package's Publisher field must be set to the **Object ID** of the target security group.

During login, App Attach evaluates the user's group memberships and applies the appropriate user configuration based on the associated group.

Administrators should use multiple user configuration files only when different user populations require distinct application settings; standard deployments can continue to rely on the automatically detected single user configuration file.

### Performance

Requirements can vary greatly depending how many packaged applications are stored in an image and you need to test your applications to understand your requirements. For larger images, you need to allocate more bandwidth. The following table gives an example of the requirements a single 1 GB image or App-V package containing one application requires per session host:

| Resource | Requirements |
| --- | --- |
| Steady state IOPs | One IOP |
| Machine boot sign-in | 10 IOPs |
| Latency | 400 ms |

To optimize the performance of your applications, we recommend:

- Your file share should be in the same Azure region as your session hosts. If you're using Azure Files, your storage account needs to be in the same Azure region as your session hosts.
- Exclude the disk images containing your applications from antivirus scans as they're read-only.
- Ensure your storage and network fabric can provide adequate performance. You should avoid using the same file share with [FSLogix profile containers](/en-us/fslogix/concepts-container-types#profile-container).

### Availability

Any disaster recovery plans for Azure Virtual Desktop must include replicating the file share to your secondary failover location. You also need to ensure your file share path is accessible in the secondary location. For example, you can use [Distributed File System (DFS) Namespaces with Azure Files](/en-us/azure/storage/files/files-manage-namespaces) to provide a single share name across different file shares. To learn more about disaster recovery for Azure Virtual Desktop, see [Set up a business continuity and disaster recovery plan](disaster-recovery).

### Azure Files

Azure Files has limits on the number of open handles per root directory, directory, and file. VHDX or CimFS disk images are mounted using the computer account of the session host, meaning one handle is opened per session host per disk image, rather than per user. For more information on the limits and sizing guidance, see [Azure Files scalability and performance targets](/en-us/azure/storage/files/storage-files-scale-targets#file-scale-targets) and [Azure Files sizing guidance for Azure Virtual Desktop](/en-us/azure/storage/files/storage-files-scale-targets#azure-files-sizing-guidance-for-azure-virtual-desktop).

## MSIX and Appx package certificates

All MSIX and Appx packages require a valid code signing certificate. To use these packages with App Attach, you need to ensure the whole certificate chain is trusted on your session hosts. A code signing certificate has the object identifier `1.3.6.1.5.5.7.3.3`. You can get a code signing certificate for your packages from:

- A public certificate authority (CA).
- An internal enterprise or standalone certificate authority, such as [Active Directory Certificate Services](/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview). You need to export the code signing certificate, including its private key.
- A tool such as the PowerShell cmdlet [New-SelfSignedCertificate](/en-us/powershell/module/pki/new-selfsignedcertificate) that generates a self-signed certificate. You should only use self-signed certificates in a test environment. For more information on creating a self-signed certificate for MSIX and Appx packages, see [Create a certificate for package signing](/en-us/windows/msix/package/create-certificate-package-signing).

Once you obtain a certificate, you need to digitally sign your MSIX or Appx packages with the certificate. You can use the [MSIX Packaging Tool](/en-us/windows/msix/packaging-tool/tool-overview) to sign your packages when you create an MSIX package. For more information, see [Create an MSIX package from any desktop installer](/en-us/windows/msix/packaging-tool/create-app-package).

To ensure the certificate is trusted on your session hosts, you need your session hosts to trust the whole certificate chain. How your session hosts trust the certificate chain depends on where you got the certificate from and how you manage your session hosts and the identity provider you use. The following table provides some guidance on how to ensure the certificate is trusted on your session hosts:

- **Public CA**: certificates from a public CA are trusted by default in Windows and Windows Server.
- **Internal Enterprise CA**:

    - For session hosts joined to Active Directory, with AD CS configured as the internal enterprise CA, are trusted by default and stored in the configuration naming context of Active Directory Domain Services. When AD CS is a configured as a standalone CA, you need to configure Group Policy to distribute the root and intermediate certificates to session hosts. For more information, see [Distribute certificates to Windows devices by using Group Policy](/en-us/windows-server/identity/ad-cs/distribute-certificates-group-policy/).
    - For session hosts joined to Microsoft Entra ID, you can use Microsoft Intune to distribute the root and intermediate certificates to session hosts. For more information, see [Trusted root certificate profiles for Microsoft Intune](/en-us/mem/intune/protect/certificates-trusted-root).
    - For session hosts using Microsoft Entra hybrid join, you can use either of the previous methods, depending on your requirements.
- **Self-signed**: install the trusted root to the **Trusted Root Certification Authorities** store on each session host. We don't recommend distributing this certificate using Group Policy or Intune as it should only be used for testing.

Important

You should timestamp your package so that its validity can outlast your certificate's expiration date. Otherwise, once the certificate expires, you need to update the package with a new valid certificate and once again ensure session hosts trust the certificate chain.