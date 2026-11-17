---
layout: Conceptual
title: Configure Windows Hello for Business | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/configure
ms.subservice: itpro-security
ms.service: windows-client
recommendations: true
adobe-target: true
ms.collection: tier1
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
ms.localizationpriority: medium
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
author: officedocspr5
ms.author: odocspr
description: Learn about the configuration options for Windows Hello for Business and how to implement them in your organization.
ms.topic: how-to
ms.date: 2026-03-29T00:00:00.0000000Z
ms.custom: identity_protection, passwordless, hello_for_business
locale: en-us
document_id: fd7e8e18-1ab8-5043-8b50-c4d0e7c4680f
document_version_independent_id: fd7e8e18-1ab8-5043-8b50-c4d0e7c4680f
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/security/identity-protection/hello-for-business/configure.md
site_name: Docs
depot_name: TechNet.windows-security
page_type: conceptual
interactive_type: msgraph
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.windows-security/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity-protection/hello-for-business/configure
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/security/identity-protection/hello-for-business/configure.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/798bd9d1-9cc5-4fc7-b0e5-8699d1f6ce2a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b5dc5f65-34a8-4bfc-9917-97d1e20c88b2
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
platformId: d4cd5fe9-418d-c8b0-efbc-41bb5f3a0bef
---

# Configure Windows Hello for Business | Microsoft Learn

This article describes the options to configure Windows Hello for Business in an organization, and how to implement them.

## Configuration options

You can configure Windows Hello for Business by using the following options:

- Configuration Service Provider (CSP): commonly used for devices managed by a Mobile Device Management (MDM) solution, like Microsoft Intune. CSPs can also be configured with [provisioning packages](/en-us/windows/configuration/provisioning-packages/how-it-pros-can-use-configuration-service-providers#csps-in-windows-configuration-designer), which are usually used at deployment time or for unmanaged devices. To configure Windows Hello for Business, use the [PassportForWork CSP](/en-us/windows/client-management/mdm/passportforwork-csp)
- Group policy (GPO): used for devices that are Active Directory joined or Microsoft Entra hybrid joined, and aren't managed by a device management solution

## Policy precedence

Some of the Windows Hello for Business policies are available for both computer and user configuration. The following list describes the policy precedence for Windows Hello for Business:

- *User policies* take precedence over *computer policies*. If a user policy is set, the corresponded computer policy is ignored. If a user policy isn't set, the computer policy is used
- Windows Hello for Business policy settings are enforced using the following hierarchy:
    - User - GPO
    - Computer - GPO
    - User - PassportForWork CSP
    - Device - PassportForWork CSP
    - Exchange Active Sync - [DeviceLock CSP](/en-us/windows/client-management/mdm/policy-csp-devicelock)

Important

If you configure password length and complexity settings defined by the DeviceLock CSP, and PIN length and complexity settings defined by the PassportForWork CSP, Windows enforces the strictest policy out of the set of governing policies.

The DeviceLock CSP utilizes the Exchange ActiveSync Policy (EAS) engine. For more information, see [Exchange ActiveSync Policy Engine Overview](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn282287%28v=ws.11%29).

Note

If a policy isn't explicitly configured to require letters or special characters, users can optionally set an alphanumeric PIN.

### Retrieve the Microsoft Entra tenant ID

The configuration via CSP or registry of different Windows Hello for Business policy settings require to specify the Microsoft Entra tenant ID where the device is registered.

To look up your Tenant ID, see [How to find your Microsoft Entra tenant ID](/en-us/entra/fundamentals/how-to-find-tenant) or try the following, ensuring to sign in with your organization's account:

```msgraph
GET https://graph.microsoft.com/v1.0/organization?$select=id
```

For example, the [PassportForWork CSP documentation](/en-us/windows/client-management/mdm/passportforwork-csp#devicetenantid) describes how to configure Windows Hello for Business options using the OMA-URI:

```Device
./Device/Vendor/MSFT/PassportForWork/{TenantId}
```

When configuring devices, replace `TenantID` with your Microsoft Entra tenant ID. For example, if your Microsoft Entra tenant ID is `dcd219dd-bc68-4b9b-bf0b-4a33a796be35`, the OMA-URI would be:

```Device
./Device/Vendor/MSFT/PassportForWork/{dcd219dd-bc68-4b9b-bf0b-4a33a796be35}
```

## Configure Windows Hello for Business using Microsoft Intune

For Microsoft Entra joined devices and Microsoft Entra hybrid joined devices enrolled in Intune, you can use Intune policies to manage Windows Hello for Business.

There are different ways to enable and configure Windows Hello for Business in Intune:

- Using a policy applied at the tenant level. The tenant policy:
    - Is only applied at enrollment time, and any changes to its configuration doesn't apply to devices already enrolled in Intune
    - It applies to *all devices* getting enrolled in Intune. For this reason, the policy is usually disabled and Windows Hello for Business is enabled using a policy targeted to a security group
- A device configuration policy that is applied *after*device enrollment. Any changes to the policy are applied to the devices during regular policy refresh intervals. There are different policy types to choose from:
    - [Settings catalog](/en-us/mem/intune/configuration/settings-catalog)
    - [Security baselines](/en-us/mem/intune/protect/security-baselines)
    - [Custom policy](/en-us/mem/intune/configuration/custom-settings-configure), via the [PassportForWork CSP](/en-us/windows/client-management/mdm/passportforwork-csp)
    - [Account protection policy](/en-us/mem/intune/protect/endpoint-security-account-protection-policy)
    - [Identity protection policy template](/en-us/mem/intune/protect/identity-protection-configure)

### Verify the tenant-wide policy

To check the Windows Hello for Business policy settings applied at enrollment time:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431)
2. Select **Devices** &gt; **Windows** &gt; **Windows Enrollment**
3. Select **Windows Hello for Business**
4. Verify the status of **Configure Windows Hello for Business** and any settings that might be configured

    [![Disablement of Windows Hello for Business from Microsoft Intune admin center.](deploy/images/whfb-intune-disable.png)](deploy/images/whfb-intune-disable.png#lightbox)

## Policy conflicts from multiple policy sources

Windows Hello for Business can be configured by GPO or CSP, but not a combination of both. Avoid mixing GPO and CSP policy settings for Windows Hello for Business, as it can lead to unexpected results. If you mix GPO and CSP policy settings, the conflicting CSP settings aren't applied until the group policy settings are cleared.

Important

The [*MDMWinsOverGP*](/en-us/windows/client-management/mdm/policy-csp-controlpolicyconflict#mdmwinsovergp) policy setting doesn't apply to Windows Hello for Business. MDMWinsOverGP only applies to policies in the *Policy CSP*, while the Windows Hello for Business policies are in the *PassportForWork CSP*.

Note

For more information about deploying Windows Hello for Business configuration using Microsoft Intune, see [Windows device settings to enable Windows Hello for Business in Intune](/en-us/mem/intune/configuration/settings-catalog) and [PassportForWork CSP](/en-us/windows/client-management/mdm/passportforwork-csp).

## Disable Windows Hello for Business enrollment

Windows Hello for Business is enabled by default for devices that are Microsoft Entra joined. If you need to disable the automatic enablement, there are different options, including:

- Disable Windows Hello using the tenant-wide policy
- Disable it using one of the policy types available in Intune, while enabling the Enrollment Status Page (ESP). The ESP can be configured to prevent a user from accessing the desktop until the device receives all the required policies. For more information, see [Set up the Enrollment Status Page](/en-us/mem/intune/enrollment/windows-enrollment-status). The policy setting to configure is [Use Windows Hello for Business](policy-settings#use-windows-hello-for-business)
- Provision the devices using a provisioning package that disables Windows Hello for Business. For more information, see [Provisioning packages for Windows](/en-us/windows/configuration/provisioning-packages/provisioning-packages)
- Scripted solutions that can modify the registry settings to disable Windows Hello for Business during OS deployment

| Configuration type | Details |
| --- | --- |
| CSP (user) | **Key path**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Policies\PassportForWork\<Tenant-ID>\UserSid\Policies`**Key name**: `UsePassportForWork`**Type**: `REG_DWORD`**Value**:`1` to enable`0` to disable |
| CSP (device) | **Key path**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Policies\PassportForWork\<Tenant-ID>\Device\Policies`**Key name**: `UsePassportForWork`**Type**: `REG_DWORD`**Value**:`1` to enable`0` to disable |
| GPO (user) | **Key path**: `HKEY_USERS\<UserSID>\SOFTWARE\Policies\Microsoft\PassportForWork`**Key name**: `Enabled`**Type**: `REG_DWORD`**Value**:`1` to enable`0` to disable |
| GPO (device) | **Key path**: `KEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\PassportForWork`**Key name**: `Enabled`**Type**: `REG_DWORD`**Value**:`1` to enable`0` to disable |

Note

If there's a conflicting device policy and user policy, the user policy takes precedence. It's not recommended to create Local GPO or registry settings that could conflict with an MDM policy. This conflict could lead to unexpected results.

## Monitor Windows Hello sign-in activity

Note

Feature available in Windows Insiders Preview.

Deploying passwordless authentication is only the first step. To manage it at scale, you need to know which methods users sign in with, whether they're using the methods you expect, and where sign-ins fail. Windows Hello sign-in events record this information without changing the user experience.

Use these events to:

- **Audit sign-in methods**: confirm which Windows Hello method was used for each sign-in, and find password sign-ins from users who are set up for Windows Hello.
- **Investigate failures**: see which method was attempted when a sign-in or unlock fails.
- **Measure adoption**: see how many users sign in with Windows Hello and find users who might need help.

#### How it works

Windows records sign-in events in two logs:

- **Audit log**: Events 4628 and 4629 appear next to the existing sign-in events. They use the existing **Audit Logon** policy, so you don't need a new policy to collect them. Use them for security monitoring and audits.
- **Windows Hello for Business Operational log**: Events 5010 and 7010 record each Windows Hello sign-in and unlock, along with its result. Use them for troubleshooting.

#### Where to look

Install a supported Windows build and open **Event Viewer**.

To view events 4628 and 4629, go to **Windows Logs** &gt; **Security**.

| Event ID | Description |
| --- | --- |
| 4628 | (Success) Logged for each sign-in. Records the Windows Hello methods the user has enrolled, the method used (PIN, face or fingerprint), and Enhanced Sign-In Security status. If the user didn't sign in with Windows Hello, the event will record "-" |
| 4629 | (Failure) Logged when a Windows Hello sign-in attempt fails and the method attempted. |

To view events 5010 and 7010, go to **Applications and Services Logs** &gt; **Microsoft** &gt; **Windows** &gt; **HelloForBusiness** &gt; **Operational**.

| Event ID | Description |
| --- | --- |
| 5010 | Records a successful Windows Hello sign-in attempt |
| 7010 | Records an unsuccessful Windows Hello sign-in attempt |