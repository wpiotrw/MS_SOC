---
layout: Conceptual
title: Publish applications with RemoteApp in Azure Virtual Desktop - Azure - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/publish-applications-stream-remoteapp
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: rick-man
manager: eliotgra
ms.author: rickman
ms.service: azure-virtual-desktop
description: How to publish applications with RemoteApp in Azure Virtual Desktop using the Azure portal and Azure PowerShell.
ms.topic: how-to
ms.custom: devx-track-azurepowershell
ms.date: 2025-06-04T00:00:00.0000000Z
locale: en-us
document_id: 0831cfbf-741b-8e22-ecdb-b9521c5e4ee7
document_version_independent_id: 0831cfbf-741b-8e22-ecdb-b9521c5e4ee7
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/publish-applications-stream-remoteapp.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: publish-applications-stream-remoteapp
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/publish-applications-stream-remoteapp.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: ad90a86a-222b-04ec-f79c-de4b6b82e15b
---

# Publish applications with RemoteApp in Azure Virtual Desktop - Azure - Azure Virtual Desktop | Microsoft Learn

There are two ways to make applications available to users in Azure Virtual Desktop: as part of a full desktop or as individual applications with *RemoteApp*. You publish applications by adding them to an application group, which is associated with a host pool and workspace, and assigned to users. For more information about application groups, see [Terminology](terminology#application-groups).

With RemoteApp application groups, you publish applications to stream remotely that are installed locally on session hosts or delivered dynamically using *App Attach*. These applications are presented to users as individual applications in [Windows App](/en-us/windows-app/overview).

This article shows you how to publish applications that are installed locally with RemoteApp using the Azure portal and Azure PowerShell. You can't publish applications using Azure CLI.

Important

Users who have access to both a desktop application group and RemoteApp application group assigned to the same host pool only have access to the type of applications from the application group determined by the preferred application group type for the host pool. For more information, see [Preferred application group type behavior for pooled host pools](preferred-application-group-type).

## Prerequisites

# [Azure portal](#tab/portal)
In order to publish an application to a RemoteApp application group, you need the following things:

- An Azure account with an active subscription.
- An existing [host pool](create-host-pool) with [session hosts](add-session-hosts-host-pool), a [RemoteApp application group, and a workspace](create-application-group-workspace).
- At least one session host is powered on in the host pool the application group is assigned to.
- The applications you want to publish are installed on the session hosts in the host pool the application group is assigned to. If you're using App Attach, you must add and assign an MSIX, Appx, or App-V package to your host pool before you start. For more information, see [Add and manage App Attach applications](app-attach-setup).
- As a minimum, the Azure account you use must have the [Desktop Virtualization Application Group Contributor](rbac#desktop-virtualization-application-group-contributor) built-in role-based access control (RBAC) roles on the resource group, or on the subscription to create the resources.

# [Azure PowerShell](#tab/powershell)
In order to publish an application to a RemoteApp application group, you need the following things:

- An Azure account with an active subscription.
- An existing [host pool](create-host-pool) with [session hosts](add-session-hosts-host-pool), a [RemoteApp application group, and a workspace](create-application-group-workspace).
- At least one session host is powered on in the host pool the application group is assigned to.
- The applications you want to publish are installed on the session hosts in the host pool the application group is assigned to. If you're using App Attach, you must add and assign an MSIX package to your host pool. For more information, see [Add and manage App Attach applications](app-attach-setup).
- As a minimum, the Azure account you use must have the [Desktop Virtualization Application Group Contributor](rbac#desktop-virtualization-application-group-contributor) built-in role-based access control (RBAC) roles on the resource group, or on the subscription to create the resources.
- If you want to publish an App Attach application, you need to use version 4.2.0 or later of the *Az.DesktopVirtualization* PowerShell module, which contains the cmdlets that support App Attach. You can download and install the Az.DesktopVirtualization PowerShell module from the [PowerShell Gallery](https://www.powershellgallery.com/packages/Az.DesktopVirtualization/).
- If you want to publish an application from the Microsoft Store, you also need the [Appx](/en-us/powershell/module/appx) module, which is part of Windows.

---

## Add applications to a RemoteApp application group

To add applications to a RemoteApp application group, select the relevant tab for your scenario and follow the steps.

# [Azure portal](#tab/portal)
Here's how to add applications to a RemoteApp application group using the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the search bar, type *Azure Virtual Desktop* and select the matching service entry.
3. Select **Application groups**, then select the RemoteApp application group you want to add an application to.
4. Select **Applications**, select **+ Add**. Make sure you have at least one session host powered on in the host pool the application group is assigned to.
5. On the **Basics** tab, from **application source** drop-down list, select **App Attach**, **Start menu**, or **File path**. The remaining fields change depending on the application source you select.

    - For **App Attach**, complete the following information. Your MSIX package must already be [added and assigned to your host pool](app-attach-setup).

        | Parameter | Value/Description |
        | --- | --- |
        | Package | Select a package available for the host pool from the drop-down list. |
        | Application | Select an application from the drop-down list. |
        | Application identifier | Enter a unique identifier for the application. |
        | Display name | Enter a friendly name for the application that is to users. |
        | Description | Enter a description for the application. |
    - For **Start menu**, complete the following information:

        | Parameter | Value/Description |
        | --- | --- |
        | Application | Select an application from the drop-down list. |
        | Display name | Enter a friendly name for the application that is to users. |
        | Description | Enter a description for the application. |
        | Application path | Review the file path to the `.exe` file for the application and change it if necessary. |
        | Require command line | Select if you need to add a specific command to run when the application launches. If you select **Yes**, enter the command in the **Command line** field. |
    - For **File path**, complete the following information:

        | Parameter | Value/Description |
        | --- | --- |
        | Application path | Enter the file path to the `.exe` file for the application. |
        | Application identifier | Enter a unique identifier for the application. |
        | Display name | Enter a friendly name for the application that is displayed to users. |
        | Description | Enter a description for the application. |
        | Require command line | Select if you need to add a specific command to run when the application launches. If you select **Yes**, enter the command in the **Command line** field. |

        If you would like to pin the RemoteApp, you can use the toggle **Create desktop shortcut (Preview)**. After this, additional Intune setup is needed to enable this policy, otherwise the configuration will not take effect. [Learn more here](/en-us/windows-app/device-actions?tabs=windows)

    Once you've completed this tab, select **Next**.
6. On the **Icon** tab, the options you see depend on the application source you selected on the **Basics** tab. With **App Attach** you can use a UNC path, but for **Start Menu** and **File path** you can only use a local path.

    - If you selected **App Attach**, select **Default** to use the default icon for the application, or select **File path** to use a custom icon.

        For **File path**, select one of the following options:

        - **Browse Azure Files** to use an icon from an Azure file share. Select **Select a storage account** and select the storage account containing your icon file, then select **Select icon file**. Browse to the file share and directory your icon is in, check the box next to the icon you want to add, for example `MyApp.ico`, then select **Select**. You can also use a `.png` file. For **Icon index**, specify the index number for the icon you want to use. This is usually **0**.
        - **UNC file path** to use an icon from a file share. For **Icon path**, enter the UNC path to your icon file, for example `\\MyFileShare\MyApp.ico`. You can also use a `.png` file. For **Icon index**, specify the index number for the icon you want to use. This is usually **0**.
    - If you selected **Start menu** or **File path**, for **Icon path**, enter a local path to the `.exe` file or your icon file, for example `C:\Program Files\MyApp\MyApp.exe`. For **Icon index**, specify the index number for the icon you want to use. This is usually **0**.

    Once you've completed this tab, select **Review + add**.
7. On the **Review + add** tab, ensure validation passes and review the information that is used to add the application, then select **Add** to add the application to the RemoteApp application group.

# [Azure PowerShell](#tab/powershell)
Here's how to add applications to a RemoteApp application group using the [Az.DesktopVirtualization](/en-us/powershell/module/az.desktopvirtualization) PowerShell module. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. Add an application to a RemoteApp application group by running the commands in one of the following examples.
2. To add an application from the **Windows Start menu** of your session hosts, run the following commands. This example publishes WordPad with its default icon and has no command line parameters.

    ```azurepowershell
    # List the available applications in the start menu
    $parameters = @{
    ApplicationGroupName = '<ApplicationGroupName>'
    ResourceGroupName = '<ResourceGroupName>'
    }
    
    Get-AzWvdStartMenuItem @parameters | Select-Object Name, AppAlias
    ```

    Use the `AppAlias` value from the previous command for the application you want to publish:

    ```azurepowershell
    # Use the value from AppAlias in the previous command
    $parameters = @{
    Name = 'WordPad'
    AppAlias = 'wordpad'
    GroupName = '<ApplicationGroupName>'
    ResourceGroupName = '<ResourceGroupName>'
    CommandLineSetting = 'DoNotAllow'
    }
    
    New-AzWvdApplication @parameters
    ```

    - To add an application by specifying a **file path** on your session hosts, run the following commands. This example specifies Microsoft Excel with a different icon index, and adds a command line parameter.

        ```azurepowershell
        $parameters = @{
        Name = 'Microsoft Excel'
        FilePath = 'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        GroupName = '<ApplicationGroupName>'
        ResourceGroupName = '<ResourceGroupName>'
        IconPath = 'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        IconIndex = '1'
        CommandLineSetting = 'Require'
        CommandLineArgument = '/t http://MySite/finance-template.xltx'
        ShowInPortal = $true
        }
        
        New-AzWvdApplication @parameters
        ```
    - To add an MSIX or Appx application from App Attach, your MSIX package must already be [added and assigned to your host pool](app-attach-setup). Run the commands from one of the following examples:
    - Get the package and application details and store them in a variable by running the following commands:

        ```azurepowershell
        $parameters = @{
        Name = '<Name>'
        ResourceGroupName = '<ResourceGroupName>'
        }
        
        $package = Get-AzWvdAppAttachPackage @parameters
        
        Write-Host "These are the application IDs available in the package. Many packages only contain one application." -ForegroundColor Yellow
        $package.ImagePackageApplication.AppId
        ```

        Make a note of the application ID you want to publish (for example `App`), then run the following commands to add the application to the RemoteApp application group:

        ```azurepowershell
        $parameters = @{
        Name = '<ApplicationName>'
        ApplicationType = 'MsixApplication'
        MsixPackageFamilyName = $package.ImagePackageFamilyName
        MsixPackageApplicationId = '<ApplicationID>'
        GroupName = '<ApplicationGroupName>'
        ResourceGroupName = '<ResourceGroupName>'
        CommandLineSetting = 'DoNotAllow'
        }
        
        New-AzWvdApplication @parameters
        
        ```
    - If you would like to create a RemoteApps shortcut on desktop, you can use this [PowerShell script in preview](https://www.powershellgallery.com/packages/Az.DesktopVirtualization/6.0.1-preview). After this, additional Intune setup is needed to enable this policy, otherwise the configuration will not take effect. [Learn more here](/en-us/windows-app/device-actions?tabs=windows)
3. Verify the list of applications in the application group by running the following command:

    ```azurepowershell
    $parameters = @{
        GroupName = '<ApplicationGroupName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    Get-AzWvdApplication @parameters
    ```

---

## Assign applications to users

Applications aren't assigned individually to users unless you're using App Attach. Instead, users are assigned to application groups. When a user is assigned to an application group, they can access all the applications in that group. To learn how to assign users to application groups, see [Assign users to an application group](create-application-group-workspace#assign-users-to-an-application-group) or [Add and manage App Attach applications](app-attach-setup?pivots=app-attach).

## Publish Microsoft Store applications

Applications in the Microsoft Store are updated frequently and often install automatically. The directory path for an application installed from the Microsoft Store includes the version number, which changes each time an application is updated. If an update happens automatically, the path changes and the application is no longer available to users. You can publish applications using the Windows `shell:appsFolder` location as the path in the format `shell:AppsFolder\<PackageFamilyName>!<AppId>`, which doesn't use the `.exe` file or the directory path with the version number. This method ensures that the application location is always correct.

Using `shell:appsFolder` means the application icon isn't picked up automatically from the application. You should provide an icon file on a local drive on each session host in a path that doesn't change, unlike the application installation directory.

Select the relevant tab for your scenario and follow the steps.

# [Azure portal](#tab/portal)
Here's how to publish a Microsoft Store application using the Windows user interface and the Azure portal:

1. On your session host, open **File Explorer** and go to the path `shell:appsFolder`.
2. Find the application in the list, right-click it, then select **Create a shortcut**.
3. For the shortcut prompt that appears, select **Yes** to place the shortcut on the desktop.
4. View the properties of the shortcut and make a note of the **Target** value. This value is the package family name and application ID you need to publish the application.
5. Follow the steps in the section Add applications to a RemoteApp application group for publishing an application based on **File path**. For the parameter **Application path**, use the value from the **Target** field of the shortcut you created, then specify the icon path as your local icon file.

# [Azure PowerShell](#tab/powershell)
Here's how to publish a Microsoft Store application using PowerShell and Azure PowerShell. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. You also need to connect to a session host to run PowerShell commands as an administrator. On a session host, get a list of installed applications from the Microsoft Store by running the following commands:

    ```powershell
    Get-AppxPackage -AllUsers | Sort-Object Name | Select-Object Name, PackageFamilyName
    ```
2. Make a note of the value for `PackageFamilyName`, then run the following command to get the `AppId` value:

    ```powershell
    $packageFamilyName = '<PackageFamilyName>'
    
    (Get-AppxPackage -AllUsers | ? PackageFamilyName -eq $packageFamilyName | Get-AppxPackageManifest).Package.Applications.Application.Id
    ```
3. Use Azure PowerShell with the values for `PackageFamilyName` and `AppId` combined with an exclamation mark (`!`) in between, together with the `FilePath` parameter to add an application to a RemoteApp application group by running the following commands. In this example, *Microsoft Paint* from the Microsoft Store is added:

    ```azurepowershell
    $parameters = @{
        Name = 'Microsoft Paint'
        ResourceGroupName = '<ResourceGroupName>'
        ApplicationGroupName = '<ApplicationGroupName>'
        FilePath = 'shell:appsFolder\Microsoft.Paint_8wekyb3d8bbwe!App'
        CommandLineSetting = 'DoNotAllow'
        IconPath = 'C:\Icons\Microsoft Paint.png'
        IconIndex = '0'
        ShowInPortal = $true
    }
    
    New-AzWvdApplication @parameters
    ```

    The output should be similar to the following example:

    ```output
    Name
    ----
    myappgroup/Microsoft Paint
    ```

---

## Publish Windows Sandbox

[Windows Sandbox](/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) provides a lightweight desktop environment to safely run applications in isolation. You can use Windows Sandbox with Azure Virtual Desktop in a desktop or RemoteApp session.

Your session hosts need to use a virtual machine (VM) size that supports [nested virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization). To check if a VM series supports nested virtualization, see [Sizes for virtual machines in Azure](/en-us/azure/virtual-machines/sizes), go to the relevant article for the series of the VM, and check the list of supported features.

1. To install Windows Sandbox on your session hosts, follow the steps in [Windows Sandbox overview](/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview). We recommend you install Windows Sandbox in a custom image you can use when creating your session hosts.
2. Once you installed Windows Sandbox on your session hosts, it's available in a desktop session. If you also want to publish it as a RemoteApp, follow the steps to Add applications to a RemoteApp application group and use the file path `C:\Windows\System32\WindowsSandbox.exe`.