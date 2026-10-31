---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set up Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-set-up?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: m365-core
ms.subservice: security
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- AdminTemplateSet
- basic-mobility-security
description: Admins can learn how to set up Basic Mobility and Security in Microsoft 365 Basic or Microsoft 365 Standard organizations to secure and manage mobile devices that access company data.
locale: en-us
document_id: a98c9535-5625-398f-6712-9cb6abc749da
document_version_independent_id: a98c9535-5625-398f-6712-9cb6abc749da
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-set-up.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-set-up
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-set-up.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: eaa8726e-5d78-b369-4ace-bdc6075dd4a6
---

# Set up Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn

Before you can use Basic Mobility and Security to manage devices and protect access to company, you need to follow the procedures in this article to turn on and configure Basic Mobility and Security in the organization.

For more information about Basic Mobility and Security, see [Overview of Basic Mobility and Security in Microsoft 365 for business](m365b-devices-basic-mobility-security-overview).

## What do you need to know before you begin?

- You open the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity.
- To connect to Security & Compliance PowerShell, see [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
- You need to be assigned permissions before you can do the procedures in this article. You have the following options:

    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**^\*^ or **Directory Writers** roles gives users the required permissions *and* permissions for other features in Microsoft 365.

        Important

        ^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).
- Questions? See the [Basic Mobility and Security FAQ](m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Step 1: Enable Basic Mobility and Security in the organization

Tip

If Basic Mobility and Security is already enabled in your organization, **Enable feature** isn't available on the **Overview** tab of the **Basic Mobility and Security** page, so you can skip this step.

Use the following steps to enable Basic Mobility and Security in your organization:

1. On the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity, verify the **Overview** tab is selected.
2. On the **Overview** tab, select **Enable feature**.

    [![Screenshot showing the Basic Mobility and Security page with the Enable feature link available.](../../media/basic-mobility-security-enable-feature.png)](../../media/basic-mobility-security-enable-feature.png#lightbox)
3. In the confirmation dialog that opens, select **OK**. The following message is shown in the dialog:

> 
> Activation request submitted for processing. Please reload the page in a few minutes.
4. After a few minutes, refresh the page in your browser.

After Basic Mobility and Security is enabled, the following changes happen on the **Overview** tab of the **Basic Mobility and Security** page:

- **Enable feature** on the **Overview** tab is replaced by **Managed devices** and **Manage Apple MDM Push Certificate**.
- The **Policies** and **Organization Setting** tabs are available.

[![Screenshot showing the Basic Mobility and Security page after the feature is enabled.](../../media/basic-mobility-security-feature-enabled.png)](../../media/basic-mobility-security-feature-enabled.png#lightbox)

### Use PowerShell to enable Basic Mobility and Security in the organization

If you'd rather use [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to enable Basic Mobility and security in your organization, do the following steps:

1. Run the following one line commands to see if Basic Mobility and Security is already enabled in the organization:

    ```powershell
    Write-Output -InputObject `r`n,"Device tenant policy",("-"*25); Get-DeviceTenantPolicy | Format-Table Name; Write-Output -InputObject "Device tenant rule",("-"*25); Get-DeviceTenantRule | Format-List Name,ExclusionList,BlockUnsupportedDevices
    ```
2. If the previous command returns no results, run the following commands to enable Basic Mobility and Security using the same values as if you enabled it on the **Overview** tab of the **Basic Mobility and Security** page:

    ```powershell
    New-DeviceTenantPolicy
    
    New-DeviceTenantRule -ExclusionList 00000000-0000-0000-0000-000000000000
    ```

    Tip

    The value `00000000-0000-0000-0000-000000000000` means all users are included in Basic Mobility and Security (no security groups specify exceptions from Basic Mobility and Security). Or you can specify the GUID values of one or more security groups separated by commas to exclude from Basic Mobility and Security/ For instructions, see the Use PowerShell to configure organization settings in Basic Mobility and Security section later in this article.

    Likewise, you can set the *BlockUnsupportedDevices* parameter to the value `$true` when you create the device tenant rule instead of setting it later.

For detailed syntax and parameter information, see [New-DeviceTenantPolicy](/en-us/powershell/module/exchangepowershell/new-devicetenantpolicy) and [New-DeviceTenantRule](/en-us/powershell/module/exchangepowershell/new-devicetenantrule).

## Step 2: Configure CNAME records for custom Microsoft 365 domains in Basic Mobility and Security

Tip

This step is required if users sign in using accounts in a custom Microsoft 365 domain (for example, `michelle@contoso.com`). If users sign in using accounts in the Microsoft Online Email Routing Address (MOERA) domain only (for example, `michelle@contoso.onmicrosoft.com`), you can skip this step.

You need to add two CNAME records for Basic Mobility and Security at the DNS registrar for your custom Microsoft 365 email domain. The basic syntax of the CNAME records is:

```text
Hostname: EnterpriseEnrollment.company_domain.com
Points to address or value: EnterpriseEnrollment-s.manage.microsoft.us

Hostname: EnterpriseRegistration.company_domain.com
Points to address or value: EnterpriseRegistration.windows.net
```

For example:

```text
Hostname: EnterpriseEnrollment.contoso.com
Points to address or value: EnterpriseEnrollment-s.manage.microsoft.us

Hostname: EnterpriseRegistration.contoso.com
Points to address or value: EnterpriseRegistration.windows.net
```

Tip

Need help with setting up the CNAME records? We provide instructions to create CNAME records for different Microsoft 365 services at many domain registrars. You can use these instructions as a starting point to create the CNAME records for Basic Mobility and Security. For more information, see [Add DNS records to connect your domain](../get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).

If you're unfamiliar with DNS configuration, contact your domain registrar and ask for help.

After you add the CNAME records, users who sign in on Windows devices using email addresses in the custom Microsoft 365 domain are redirected to enroll in Basic Mobility and Security.

## Step 3: Create an Apple Push Notification service certificate for Apple devices

Tip

If you don't plan on using Basic Mobility and Security to manage iOS/iPadOS devices, you can skip this step.

Basic Mobility and Security requires an Apple Push Notification service (APNs) certificate to manage iOS/iPadOS devices. Use the following steps to create an APNs certificate:

1. Do either of the following steps:

    - On the **Overview** tab of the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity, select **Manage Apple MDM Push Certificate** to open the **Configure MDM Push Certificate** page. Or, use the direct link https://portal.azure.com/#view/Microsoft_Intune_Enrollment/APNSCertificateUploadBlade.
    - Go to the **iOS/iPadOS | Enrollment** page of the Intune admin center at [https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesIosMenu/~/iosEnrollment](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesIosMenu/%7E/iosEnrollment). In the **Prerequisites** section, select **Apple MDM Push Certificate** to open the **Configure MDM Push Certificate** flyout.
2. On the **Configure MDM Push Certificate** page or flyout, do the displayed steps to configure the APNs certificate. For detailed instructions, start at [Step 1: Grant Microsoft permission to send user and device information to Apple](/en-us/intune/intune-service/enrollment/apple-mdm-push-certificate-get#step-1-grant-microsoft-permission-to-send-user-and-device-information-to-apple).

The Apple MDM Push certificate is valid for 365 days (with a 30-day grace period to renew after it expires). You need to renew the certificate every year to maintain Apple device management. For instructions, see [Renew Apple MDM push certificate](/en-us/intune/intune-service/enrollment/apple-mdm-push-certificate-get#renew-apple-mdm-push-certificate).

### Step 4: Configure organization settings in Basic Mobility and Security

The **Organization Setting** tab on the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity contains the following settings that you need to consider:

- **Access restriction for unsupported MDM device**: Prevents users from accessing Microsoft 365 email on devices that Basic Mobility and Security doesn't support. For more information about supported devices, see [Supported device platforms in Basic Mobility and Security](m365b-devices-basic-mobility-security-overview#supported-device-platforms-in-basic-mobility-and-security).

    After you expand this section, the following values are available:

    - **Allow access (device enrollment is required)**. This value is the default.
    - **Block access**: We recommend this value to help secure your organization. Unsupported devices aren't allowed to access Microsoft 365 email on the device. After you select this value, the tab automatically refreshes and both sections on the page are collapsed. Expand this section to see the value you selected.

    [![Screenshot of the Organization setting tab on the Basic Mobility and Security page showing the two sections expanded and Block access selected.](../../media/basic-mobility-security-organization-setting-tab.png)](../../media/basic-mobility-security-organization-setting-tab.png#lightbox)
- **Security groups excluded from access control**: Use this setting to exclude members of the specified security groups from Basic Mobility and Security. For example:

    - Specific, temporary exceptions for known, noncompliant devices.
    - You no longer want to use Basic Mobility and Security in your organization (specify one or more groups that contain all users in your organization).

    The following security group types are supported:

    - **User groups**: To create user security groups in the Microsoft 365 admin center, see [Create, edit, or delete a security group](../email/create-edit-or-delete-a-security-group)

        Business Basic and Business Standard include Microsoft Entra Free, which supports creating **assigned user groups** (not dynamic user groups), although the built-in **All Users** dynamic user group is available. To create assigned user groups in the Microsoft Entra admin center, see [Create a basic group and add members](/en-us/entra/fundamentals/how-to-manage-groups#create-a-basic-group-and-add-members). Use the following settings:

        - **Group type**: **Security** (default).
        - **Microsoft Entra roles can be assigned to the group**: **No** (default).
        - **Members**: (Step 10): Select **No members selected**. On the **Add members** page that opens, select the **Users** tab to select the users to add to the group.
    - **Assigned device groups**: Similarly, Microsoft Entra Free supports creating assigned device groups (not dynamic device groups). To create assigned device groups in the Microsoft Entra admin center, see [Create a basic group and add members](/en-us/entra/fundamentals/how-to-manage-groups#create-a-basic-group-and-add-members). Use the following settings:

        - **Group type**: **Security** (default).
        - **Microsoft Entra roles can be assigned to the group**: **No** (default).
        - **Members**: (Step 10): Select **No members selected**. On the **Add members** page that opens, select the **Devices** tab to select the devices to add to the group.

        After you expand this section, start typing the name of the group in the box, and then select the group when it appears. The tab automatically refreshes and the section collapses. Expand the section to see the group you selected below the box.

        To remove a selected group, select ![](../../media/m365-cc-sc-remove-selection-icon.png) on the entry. The tab automatically refreshes and the section collapses. Expand the section to see the group you removed is no longer below the box.

        Repeat these steps as many times as necessary.

### Use PowerShell to configure organization settings in Basic Mobility and Security

If you'd rather use [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to configure organization setting in Basic Mobility and Security in your organization, do the following steps:

1. Run the following command to see the current status of the settings:

    ```powershell
    Get-DeviceTenantRule | Format-List BlockUnsupportedDevices,ExclusionList
    ```

    If the current values of *ExclusionList* are truncated, run the following command to see them all:

    ```powershell
    Get-DeviceTenantRule | Select-Object -ExpandProperty ExclusionList
    ```
2. To configure the organization settings, use the following syntax:

    ```powershell
    Set-DeviceTenantPolicy [-BlockUnsupportedDevices <$true | $false>] [-ExclusionList "SecurityGroupGUID1","SecurityGroupGUID2",..."SecurityGroupGUIDN"]
    ```

    - *BlockUnsupportedDevices*: Corresponds to the **Access restriction for unsupported MDM device** setting.

        - `$true` = **Block Access**
        - `$false` = **Allow access (device enrollment is required)** (default)
    - *ExclusionList*: Corresponds to the **Security groups excluded from access control** setting. Specify one or more security groups separated with commas. You identify groups by GUID value:

        - The value `00000000-0000-0000-0000-000000000000` means no security groups are excluded (default).
        - To find the GUID values of available security groups, use the following procedures:
            1. If necessary, install the Microsoft Graph PowerShell module in PowerShell by running the following command:

                ```powershell
                Install-Module -Name Microsoft.Graph -Scope CurrentUser
                ```

                Answer yes to any directives about installing the NuGet provider or installing from the PSGallery.
            2. Connect to Microsoft.Graph.Groups PowerShell by running the following command:

                ```powershell
                Connect-MgGraph -Scopes "Group.ReadWrite.All"
                ```

                For detailed syntax and parameter information, see [Connect-MgGraph](/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph).
            3. Run the following command:

                ```powershell
                Get-MgGroup
                ```

                Use the DisplayName value to find and copy the Id value to use.

                Tip

                You might need to decrease the font size in the PowerShell window and run the command again to clearly see all of the values. For example, click in the window and use the scroll wheel on your mouse to scroll down, and then run the command again.

                You can't use [Microsoft 365 Groups](../create-groups/office-365-groups) (the *GroupTypes* property value is `Unified`).

                Values that you specify for the *ExclusionList* parameter overwrite existing values. Refer back to Step 1 to see how to view the complete list of security groups.

                For detailed syntax and parameter information, see [Get-MgGroup](/en-us/powershell/module/microsoft.graph.groups/get-mggroup).

    This example configures the following organization settings:

    - Block access for unsupported devices.
    - Exclude the specified security groups from Basic Mobility and Security.

    ```powershell
    Set-DeviceTenantPolicy -BlockUnsupportedDevices $true -ExclusionList "6010e907-3193-4a6f-b94c-a4c24b1398cc","0be37e4a-8f43-4b9f-ab7f-74659816067a"
    ```

    For detailed syntax and parameter information, see [Set-DeviceTenantPolicy](/en-us/powershell/module/exchangepowershell/set-devicetenantpolicy).

### Step 5: Create device security policies

For instructions, see [Configure policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure).