---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Change user profile photo - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/change-user-profile-photos?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-12-11T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
ms.custom:
- VSBFY23
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
- has-azure-ad-ps-ref
- user-accounts
search.appverid: 
description: Learn how a Microsoft 365 admin can add, update, and remove the pictures in user account profiles and Microsoft 365 Group profiles.
customer-intent: As an admin, I want to update a user's profile photo in Microsoft 365.
locale: en-us
document_id: 27d32511-e023-d009-1847-f91dc04845e1
document_version_independent_id: 27d32511-e023-d009-1847-f91dc04845e1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/change-user-profile-photos.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/change-user-profile-photos
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/change-user-profile-photos.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: f3a82699-83be-3246-6507-4de9be80d2c2
---

# Change user profile photo - Microsoft 365 admin | Microsoft Learn

Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

This article explains how to manage profile photos and photo update settings on user accounts and [Microsoft 365 Groups](../create-groups/office-365-groups).

## Before you begin

You must be a [Global Administrator](about-admin-roles) to complete these steps.

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

Here are some points to keep in mind:

- You can't remove existing user photos using the Microsoft 365 admin center. You can only use Microsoft Graph PowerShell.
- You can't manage user photos for Microsoft 365 Groups using the Microsoft 365 admin center. You can only use Microsoft Graph PowerShell.
- The maximum supported size of a photo is 4 MB.
- User profile photo updates don't affect other user account properties. Configuration of the environment where new updates can be performed doesn't affect existing user profile photos in the cloud or in on-premises environments.

## Use the Microsoft 365 admin center to change a user's profile photo

1. In the Microsoft 365 admin center, go to **Users** &gt; [Active users](https://go.microsoft.com/fwlink/p/?linkid=834822).
2. On the **Active users** page, select the user by clicking on their display name. In the details flyout that opens, select **Change photo** under their existing photo placeholder or photo at the top of the flyout.

    [![The Change user action in the properties of the user account in the Microsoft 365 admin center.](../../media/user-photo-user-properties.png)](../../media/user-photo-user-properties.png#lightbox)
3. In the **Change photo** flyout that opens, select ![](../../media/m365-cc-sc-import-icon.png)**Choose photo**.
4. In the **File upload** dialog that opens, find and select the photo, and then select **Open**.
5. On the **Change photo** flyout, select **Save changes**, and then select ![](../../media/m365-cc-sc-back-icon.png)**Back** to return to the details flyout, or ![](../../media/m365-cc-sc-remove-selection-icon.png)**Close** to return to the **Active users** page

Tip

In the user details flyout or the **Change photo** flyout, you can download an existing photo by right-clicking on the photo and selecting **Save image as**.

## Manage user photos in Microsoft Graph PowerShell

After you [install the Microsoft Graph PowerShell SDK](/en-us/powershell/microsoftgraph/installation), use the **Connect-MgGraph** cmdlet to sign in with the required scopes. You need to sign in with an admin account to consent to the required scopes.

- **Users only**:

    ```powershell
    Connect-MgGraph -Scopes "User.ReadWrite.All"
    ```
- **Microsoft 365 Groups only**:

    ```powershell
    Connect-MgGraph -Scopes "Group.ReadWrite.All"
    ```
- **Users and Microsoft 365 groups**:

    ```powershell
    Connect-MgGraph -Scopes "User.ReadWrite.All","Group.ReadWrite.All"
    ```

### Add user photos in Microsoft Graph PowerShell

- **Users**:

    ```powershell
    Set-MgUserPhotoContent -UserId <UPN> -InFile "<PhotoPathAndFileName>"
    ```

    For example:

    ```powershell
    Set-MgUserPhotoContent -UserId albertas@contoso.onmicrosoft.com -InFile "C:\Upload\Alberta Sanchez.png"
    ```

    For detailed syntax and parameter information, see [Set-MgUserPhotoContent](/en-us/powershell/module/microsoft.graph.users/set-mguserphotocontent).
- **Microsoft 365 Groups**:

    ```powershell
    Set-MgGroupPhotoContent -GroupId <ID> -InFile "<PhotoPathAndFileName>"
    ```

    You get the ID GUID value of the Microsoft 365 Group from the output of a **Get-MgGroup** command.

    For example:

    ```powershell
    Set-MgGroupPhotoContent -GroupId 173cd812-5563-439c-9da4-bc2715fa2aee -InFile "C:\Upload\Sales Department.png"
    ```

    For detailed syntax and parameter information, see [Set-MgGroupPhotoContent](/en-us/powershell/module/microsoft.graph.groups/set-mggroupphotocontent).

### Get information about user photos in Microsoft Graph PowerShell

The commands return the following information about the existing photo:

- **Id**: The value is Default.
- **Height**: In pixels.
- **Width**: In pixels.

If the user has no photo, the commands return the error: `Exception of type 'Microsoft.Fast.Profile.Core.Exception.ImageNotFoundException' was thrown.`.

- **Users**:

    ```powershell
    Get-MgUserPhoto -UserId <UPN>
    ```

    For example:

    ```powershell
    Get-MgUserPhoto -UserId albertas@contoso.onmicrosoft.com
    ```

    For detailed syntax and parameter information, see [Get-MgUserPhoto](/en-us/powershell/module/microsoft.graph.users/get-mguserphoto).
- **Microsoft 365 Groups**:

    ```powershell
    Get-MgGroupPhoto -GroupId <ID>
    ```

    You get the ID GUID value of the Microsoft 365 Group from the output of a **Get-MgGroup** command.

    For example:

    ```powershell
    Get-MgGroupPhoto -GroupId 173cd812-5563-439c-9da4-bc2715fa2aee
    ```

    For detailed syntax and parameter information, see [Get-MgGroupPhoto](/en-us/powershell/module/microsoft.graph.groups/get-mggroupphoto).

### Download user photos in Microsoft Graph PowerShell

- **Users**:

    ```powershell
    Get-MgUserPhotoContent -UserId <UPN> -OutFile "<PhotoPathAndFileName>
    ```

    For example:

    ```powershell
    Get-MgUserPhotoContent -UserId albertas@contoso.onmicrosoft.com -OutFile "C:\Download\Alberta Sanchez.png"
    ```

    For detailed syntax and parameter information, see [Get-MgUserPhotoContent](/en-us/powershell/module/microsoft.graph.users/get-mguserphotocontent).
- **Microsoft 365 Groups**:

    ```powershell
    Get-MgGroupPhotoContent -GroupId <ID> -OutFile "<PhotoPathAndFileName>
    ```

    You get the ID GUID value of the Microsoft 365 Group from the output of a **Get-MgGroup** command.

    For example:

    ```powershell
    Get-MgGroupPhotoContent -GroupId 173cd812-5563-439c-9da4-bc2715fa2aee -OutFile "C:\Download\Sales Department.png"
    ```

    For detailed syntax and parameter information, see [Get-MgGroupPhotoContent](/en-us/powershell/module/microsoft.graph.groups/get-mggroupphotocontent).

### Remove user photos in Microsoft Graph PowerShell

- **Users**:

    ```powershell
    Remove-MgUserPhoto -UserId <UPN>
    ```

    For example:

    ```powershell
    Remove-MgUserPhoto -UserId albertas@contoso.onmicrosoft.com
    ```

    For detailed syntax and parameter information, see [Remove-MgUserPhoto](/en-us/powershell/module/exchangepowershell/remove-userphoto).
- **Microsoft 365 Groups**:

    ```powershell
    Remove-MgGroupPhoto -GroupId <ID>
    ```

    You get the ID GUID value of the Microsoft 365 Group from the output of a **Get-MgGroup** command.

    For example:

    ```powershell
    Remove-MgGroupPhoto -GroupId 173cd812-5563-439c-9da4-bc2715fa2aee
    ```

    For detailed syntax and parameter information, see [Remove-MgGroupPhoto](/en-us/powershell/module/exchangepowershell/remove-userphoto).

## Configure photo update settings in your Microsoft 365 organization

Photo update settings in your organization include controlling the environment where user profile photos can be updated and which roles are required.

Important

When you change photo update settings, it can take up to 24 hours for the changes to reflect throughout Microsoft 365. For example, if you block cloud user profile photo updates, it can take up to 24 hours before the users are blocked from making updates.

### Select where user profile photos can be edited using Microsoft Graph

Currently, you can configure the photo update settings using Microsoft Graph only. For more information, see [Manage user profile photo settings in Microsoft 365 using Microsoft Graph](/en-us/graph/profilephoto-configure-settings).