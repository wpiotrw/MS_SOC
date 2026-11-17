---
layout: Conceptual
title: Administrator protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/
ms.subservice: itpro-security
ms.service: windows-client
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
ms.localizationpriority: medium
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
author: officedocspr5
ms.author: odocspr
description: Learn how Administrator protection protects users with just-in-time administrator privileges and helps prevent unauthorized system changes.
ms.topic: overview
ms.date: 2026-10-13T00:00:00.0000000Z
ms.custom: app_security, app_driver_control
locale: en-us
document_id: c82e95b5-28a0-6277-228c-34e0c9e32d08
document_version_independent_id: c82e95b5-28a0-6277-228c-34e0c9e32d08
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/security/application-security/application-control/administrator-protection/index.md
site_name: Docs
depot_name: TechNet.windows-security
page_type: conceptual
toc_rel: ../../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.windows-security/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: application-security/application-control/administrator-protection/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/security/application-security/application-control/administrator-protection/index.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/691e3042-55ad-4ce1-b5e9-649b1cc47b5c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b7d11190-096c-4ddb-87db-63764f603aac
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: c5eb4340-b139-36a2-0fa4-f73c654255d9
---

# Administrator protection | Microsoft Learn

Administrator protection is a platform security feature in Windows 11 designed to ensure users run with the least privilege needed, elevating to admin rights only when necessary and only with the user's explicit approval. This feature operates on the principle of least privilege, keeping users in a deprivileged state and granting just-in-time elevation rights only when needed.

In today's digital landscape, users with Administrator rights on Windows have powerful capabilities to modify configurations and make system-wide changes that might affect the overall security posture of a Windows 11 device. Administrative privileges create a significant attack vector. Malicious actors often exploit these privileges to gain unauthorized access to user data, compromise privacy, and disable OS security features without the user’s knowledge.

Administrator protection addresses this challenge by requiring users to verify their identity with Windows Hello integrated authentication. It enforces this verification before allowing actions that need administrator privileges, such as installing software, changing system settings like the time or registry, and accessing sensitive data.

## Benefits

Administrator protection provides several key benefits:

- **Enhanced security**: By requiring explicit authorization from the user for every administrative task, Administrator protection protects Windows from accidental changes by users and changes by malware. It helps ensure that users are aware of potentially harmful actions before they occur, providing an extra layer of defense against threats.
- **User control**: Administrator protection requires users to decide explicitly whether they want a particular application to run as elevated. This helps ensure that only authorized apps can make system changes, reducing the risk of accidental or malicious modifications.
- **Malware reduction**: Malicious software often relies on admin privileges to change device settings and execute harmful actions. Administrator protection breaks the attack kill chain since malware can no longer silently acquire admin privileges.

## System requirements

Administrator protection is now available with [KB5120998](https://support.microsoft.com/servicing/os/windows-11/2026/08/kb5120998-windows-11-24h2-25h2-update). The feature is off by default. Enterprise customers can enable the feature using custom OMA-URI.

Supported editions: Windows 11 Home, Pro, Enterprise, Education.

Administrator protection currently applies to supported Windows 11 devices outside Windows 365 Cloud PCs and Azure Virtual Desktop session hosts. Support for these environments, as well as Windows Server editions, is planned for a future release.

For Windows 365 and Azure Virtual Desktop session hosts, configure users as standard users to follow least-privilege best practices.

Note

If your organization uses [Windows security baselines](https://techcommunity.microsoft.com/blog/microsoft-security-baselines/windows-11-version-26h2-security-baseline/4560382), Administrator protection becomes enabled by default with the October 2026 Windows security update. The security baselines for Windows 11, versions 26H2, 25H2, and 24H2 include the new default settings, manageable by policy. Review, test your existing configuration, and adjust it as appropriate for your environment. [Details of policies](?tabs=gpo#configuration)

## How Administrator protection works

At its core, Administrator protection operates on the principle of least privilege. When a user signs in to Windows, they receive a deprivileged user token. However, when admin privileges are needed, Windows requests that the user authorize the operation. Once authorized, Windows uses a hidden, system-generated, profile-separated user account to create an isolated admin token. This token is issued to the requesting process and is destroyed once the process ends, ensuring that admin privileges don't persist. The architectural changes ensure that no one can access or tamper with the code or data of elevated sessions without proper authorization.

Some applications might rely on admin rights always being present, and the elevated profile being accessible when running unelevated. With this new approach, some scenarios in those apps might need updates to work smoothly with the enhanced security model. Microsoft is actively collaborating with app developers to help them adapt, ensuring your favorite experiences remain seamless while keeping your system protected. For guidance on developing your applications, see [Enhance your application security with administrator protection](https://blogs.windows.com/windowsdeveloper/2025/05/19/enhance-your-application-security-with-administrator-protection/).

Ultimately, these changes are all about making Windows more secure for you, so you can enjoy powerful features with greater peace of mind.

### Key architectural highlights

![Diagram of the administrator protection architecture.](images/architecture.png)

- **Just-in-time elevation**: Users stay deprivileged and are granted just-in-time elevation rights only during an admin operation. The admin token is discarded after use and recreated when another task requiring admin privileges is performed.
- **Profile separation**: Administrator protection uses hidden, system-generated, profile-separated user accounts to create isolated admin tokens. This helps ensure that user-level malware can't compromise the elevated session.
- **No auto-elevations**: Users need to interactively authorize every admin operation. This ensures that the administrator user stays in full control and that admin privileges aren't abused.
- **Windows Hello integration**: Administrator protection is integrated with Windows Hello for simple and secure authorization.

## Configuration

You can enable administrator protection through several methods:

- [Microsoft Intune Settings Catalog](?tabs=intune#configuration)
- [CSP](?tabs=csp#configuration)
- [Group policy](?tabs=gpo#configuration)
- [Windows Security Settings (Preview)](?tabs=security#configuration)

# [Intune](#tab/intune)
To configure devices by using Microsoft Intune, [create a **Settings catalog** policy](/en-us/intune/intune-service/configuration/settings-catalog), and use the settings listed under the category **`Local Policies Security Options`**:

- User Account Control Type Of Admin Approval Mode (enables the feature)
- User Account Control Behavior Of the Elevation Prompt for Administrator Protection (Choose type of elevation prompt)

Assign the policy to a security group that contains as members the devices or users that you want to configure.

# [CSP](#tab/csp)
Administrator protection is also configurable in the [LocalPoliciesSecurityOptions](/en-us/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions) CSP:

- To enable Administrator protection, configure `UserAccountControl_TypeOfAdminApprovalMode`.
- To choose between consent and credential prompts, use `UserAccountControl_BehaviorOfTheElevationPromptForAdministratorProtection`.

In Microsoft Intune, you can use a [custom policy](/en-us/intune/intune-service/configuration/custom-settings-windows-10) to deploy the [LocalPoliciesSecurityOptions](/en-us/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions) CSP.

# [GPO](#tab/gpo)
You can use security policies to configure how Administrator protection works in your organization. The policies can be configured locally by using the Local Security Policy snap-in (`secpol.msc`) or configured for the domain, OU, or specific groups by group policy.

To configure Administrator protection using group policy:

1. Navigate to **Computer Configuration** &gt; **Windows Settings** &gt; **Security Settings** &gt; **Local Policies** &gt; **Security Options**.
2. Locate the policy for "User Account Control: Configure type of Admin Approval Mode" and change the setting to "Admin Approval Mode with Administrator protection".
3. Configure prompt behavior by selecting the desired behavior in the "User Account Control: Behavior of the elevation prompt for administrators running with Administrator protection" policy.
4. To apply the changes, **restart** the device.

To disable the feature change the setting of "User Account Control: Configure type of Admin Approval Mode" to "Legacy Admin Approval Mode (Default)". Restart will be required.

**If you have the policy set in your security baseline, adjust the baseline with the policy update as needed.**

# [Windows Security](#tab/security)
Note

This option is currently available in Windows Insider Program as a preview. It will be rolled out to everyone gradually.

![Screenshot of the Windows Security app showing how to enable administrator protection.](images/security-app-admin-protection.png)

You can enable Administrator protection on your device by going to the Account protection section in the Windows Security app and turning on the toggle.

1. Select the Start button, search for Windows Security, and launch the **Windows Security** app.
2. Select Account Protection, then locate the Administrator protection settings.
3. Select the toggle to turn on Administrator protection.
4. When prompted, restart your device to apply the changes.

---

Important

A reboot is required for Administrator Protection to take effect.

### Monitoring and Reporting Events

To track elevations, administrator protection has two new Event Tracing for Windows (ETW) events under the existing **Microsoft-Windows-LUA** provider with GUID `{93c05d69-51a3-485e-877f-1806a8731346}`:

| Event ID | Event Name | Description |
| --- | --- | --- |
| 15031 | Elevation Approved | Logged when a user successfully authenticates and elevation is granted |
| 15032 | Elevation Denied/Fail | Logged when elevation is denied, fails, or times out |

#### What gets logged

- The Security Identifier (SID) of the user who triggered the elevation
- The application name and path
- The elevation outcome (approved, denied, timeout)
- The system managed admin account used to perform the task
- The authentication method (e.g., password, PIN, Windows Hello)

#### How to capture these events

- Enable the **Microsoft-Windows-LUA** provider (GUID: `{93c05d69-51a3-485e-877f-1806a8731346}`)
- Use **Logman** or **WPR** (Windows Performance Recorder) to start a trace session
- Filter for Event IDs `15031` and `15032`
- Analyze the resulting .etl file using Windows Performance Analyzer or your preferred tool

Here’s a sample command:

```cmd
logman start AdminProtectionTrace -p {93c05d69-51a3-485e-877f-1806a8731346} -ets
```

### Troubleshooting

Note

**When not to enable this feature:**

- Windows 365 Cloud PCs. [Enterprise and Flex](/en-us/troubleshoot/windows-365/known-issues-enterprise#administrator-protection-isnt-supported-on-cloud-pcs), [Business](/en-us/troubleshoot/windows-365/known-issues#administrator-protection-isnt-supported-on-cloud-pcs).
- [Azure Virtual Desktop session hosts](/en-us/azure/virtual-desktop/security-recommendations#administrator-protection-isnt-supported)
- For devices that require Hyper-V.
- If you're using apps that access shared files across profiles.
- For device which are managed with [Local Administrator Password Solution (LAPS)](/en-us/windows-server/identity/laps/laps-overview)

- Settings data for applications don't carry over across the regular(unelevated) and the elevated profiles. Only elevate apps you truly need to.
- If you are using development tools or environments like Windows Subsystem for Linux (WSL) or Visual Studio that you also need to run elevated for specific tasks like performance testing, you will need to reinstall and configure the distro in the elevated profile separately.
- Remote logon on Windows 365 Cloud PC and Azure Virtual Desktop session hosts, roaming profiles, and backup admins aren't supported.
- For cross-machine remote administration scenarios, remote elevation behavior can be controlled by the [User Account Control: Allow remote logon with elevated privileges for domain users in the local Administrators group when Administrator protection is enabled](/en-us/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions#useraccountcontrol_allowremotelogonwithelevatedprivilegesfordomainusersinthelocaladministratorsgroupwhenadministratorprotectionisenabled) policy.

    Behavior:

    - Disabled (Default): Domain users in the local Administrators group perform remote logons without elevated privileges.
    - Enabled: Domain users in the local Administrators group perform remote logons with elevated privileges, matching traditional UAC behavior.

    For more granular control, use the [User Account Control: Allow remote logon with elevated privileges for specified domain users and groups when Administrator protection is enabled](/en-us/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions#useraccountcontrol_allowremotelogonwithelevatedprivilegesforspecifieddomainusersandgroupswhenadministratorprotectionisenabled) policy to grant elevated remote logons only to designated domain users or groups while keeping others non-elevated.
- [Non-admin RDP logons fail with error 0xC000000D on devices with Administrator protection enabled after installing KB5124010](/en-us/windows/release-health/status-windows-11-26h2#5031msgdesc). Workaround: Turn off Administrator protection on impacted devices by resetting the User Account Control Type of Admin Approval Mode policy via Intune or Group Policy.
- Administrator protection
- A few applications don't show the launch icon in the start menu after installation. This issue is fixed with [KB5124010](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124010-windows-11-24h2-25h2-update). If the issue persists, you will need to navigate manually to installation location: `AppData\Roaming\Microsoft\Windows\Start Menu\Programs\<App name>`
- When apps run elevated with administrator protection, Single Sign-On (SSO) credentials from the standard session aren't available to the elevated session. Any domain or cloud authentication must be re-established within that elevated session.
- Network Drives/Resources Inaccessible from elevated apps. Install it in user context to enable network credential prompts. If it's essential to install an application as elevated, copy installation files to a local drive before elevating.
- Some apps using Edge extensions may request elevated permissions even when launched normally. This is fixed with [KB5124010](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124010-windows-11-24h2-25h2-update). If the issue persists, you will need to disable Administrator protection.
- If updating any of your applications is blocked, try downloading the update as elevated and then install it. If this fails, temporarily disable Administrator protection.