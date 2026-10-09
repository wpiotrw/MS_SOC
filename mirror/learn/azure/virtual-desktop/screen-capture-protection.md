---
layout: Conceptual
title: Screen capture protection in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/screen-capture-protection
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: Fragnightmist
manager: eliotgra
ms.author: ryclar
ms.service: azure-virtual-desktop
description: Learn how to enable screen capture protection in Azure Virtual Desktop and Windows 365 to help prevent sensitive information from being captured on client devices.
ms.topic: how-to
ms.date: 2026-09-29T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 9ca8b48c-157d-ac7b-de5b-cc56b6af5457
document_version_independent_id: 9ca8b48c-157d-ac7b-de5b-cc56b6af5457
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/screen-capture-protection.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: screen-capture-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/screen-capture-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: e777d2a3-9627-8b54-be29-a5f524b3096e
---

# Screen capture protection in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn

Screen capture protection, alongside [watermarking](watermarking), helps prevent sensitive data from being captured on client devices using specific operating system (OS) features and APIs. When you enable screen capture protection, remote content is automatically blocked in screenshots and screen sharing. This feature can be applied to Azure Virtual Desktop virtual machines and Windows 365 Cloud PCs.

When screen capture protection (SCP) is enabled to block screen capture on the client, users can continue to share their remote desktop or individual applications using supported collaboration experiences such as Microsoft Teams. Compatibility between SCP and Teams screen sharing depends on the use of supported client configurations. When unsupported configurations are used, protected content might appear as a black screen during sharing. For current compatibility requirements and configuration guidance with Teams, see [Azure Virtual Desktop screen capture protection and Microsoft Teams compatibility](/en-us/microsoftteams/vdi-2#avd-screen-capture-protection-and-microsoft-teams-compatibility).

Important

Screen capture protection doesn't provide Digital Rights Management (DRM)-level protection. It prevents screen capture through standard OS features and APIs and isn't a substitute for DRM solutions. For comprehensive data protection, use screen capture protection as part of a broader defense-in-depth security strategy that includes other controls, such as Conditional Access policies, data loss prevention, and endpoint management.

Tip

- To increase the security of your sensitive information, you should also disable clipboard, drive, and printer redirection. Disabling redirection helps prevent users from copying content from the remote session. To learn about supported redirection values, see [Device redirection](rdp-properties#device-redirection).
- To discourage other methods of screen capture, such as taking a photo of a screen with a physical camera, you can enable [watermarking](watermarking), where admins can use a QR code to trace the session.

## Determine your configuration

The steps to configure screen capture protection depend on where you configure it, which platforms your users are connecting from, and what scenario you want to achieve.

- **Native clients on Windows and macOS**: when users connect with the natively installed Windows App or Remote Desktop client, configure screen capture protection on the virtual machines (Azure Virtual Desktop) or Cloud PCs (Windows 365) using an Intune device configuration policy or Group Policy. The native client enforces these settings without an Intune MAM app protection policy. For browser connections, including Microsoft Edge on Windows, follow Pattern 3: Web endpoints (browser access).

    When you configure screen capture protection on virtual machines or Cloud PCs, there are two further settings you can configure to help meet your requirements:

    - **Block screen capture on client**: prevents screen capture from the local device of applications running in the remote session.
    - **Block screen capture on client and server**: prevents screen capture from the local device of applications running in the remote session, but also prevents tools and services within the virtual machine or Cloud PC capturing the screen.

    In this scenario, here's the outcome when connecting from each platform type:

| Platform | Connection allowed | Screen capture blocked |
| --- | --- | --- |
| **Windows** | ✅ | ✅ |
| **macOS** | ✅ | ✅ |
| **iOS/iPadOS** | ✅^1^ | ✅^1^ |
| **Android** | ✅^1^ | ✅^1^ |
| **Web** | ✅^1^ | ✅^1^ |

^1. **Hybrid enforcement (iOS/iPadOS/Android/Web)**: When screen capture protection is enabled on the virtual machine or Cloud PC, connections from Windows App on iOS/iPadOS and Android are allowed when an Intune MAM app protection policy that blocks screen capture applies to the app. On the web, connections from Microsoft Edge for Business are allowed when the Edge work profile receives an Intune MAM app protection policy that enforces screen capture protection through the Edge data loss prevention (DLP) features. Hybrid enforcement isn't applicable on platforms that don't support Intune MAM.^

Note

Hybrid enforcement requires the following minimum app versions:

- **iOS/iPadOS**: Windows App version 11.2.4
- **Android**: Windows App version 11.0.0.94 (or later supporting hybrid enforcement)
- **Web**: Microsoft Edge for Business on Windows, version 134.0.3124.51 or later (version 147 or later on devices managed by a different organization)

- **Android, iOS/iPadOS, and web connections**: configure an Intune MAM app protection policy for the supported client app and assign it to the users who need protection. For Android and iOS/iPadOS, the policy applies to Windows App. For web connections on Windows, the policy applies to Microsoft Edge for Business through the user's work profile. This client-side protection prevents local screen capture of protected content; it doesn't prevent tools and services within the virtual machine or Cloud PC from capturing the screen. For configuration steps, see Enable screen capture protection with Intune MAM.

    In this scenario, here's the outcome when connecting from each platform type:

| Platform | Connection allowed | Screen capture blocked |
| --- | --- | --- |
| **Windows** | ✅ | ❌ |
| **macOS** | ✅ | ❌ |
| **iOS/iPadOS** | ✅ | ✅ |
| **Android** | ✅ | ✅ |
| **Web** | ✅ | ✅^1^ |

^1. On the web, screen capture protection is enforced by the Edge for Business data loss prevention (DLP) features when users connect with Microsoft Edge for Business and receive an Intune MAM app protection policy. For configuration steps, see Enable screen capture protection with Intune MAM.^

Important

For Android and iOS/iPadOS devices, and for the web client (on Windows), screen capture protection is enforced through Intune mobile application management (MAM). In each case, you configure two things: an Intune MAM app protection policy that applies screen capture protection, and a Conditional Access policy that requires the app protection policy so users can only connect when the policy is applied to the client. The exact app protection policy setting differs by platform — on Android and iOS/iPadOS you block screen capture directly, while on the web you configure Microsoft Edge for Business, where screen capture protection is enforced through the Edge data loss prevention (DLP) features. When screen capture protection is configured on your virtual machines or Cloud PCs, this is the supported model for these platforms. For configuration steps, see Enable screen capture protection with Intune MAM.

## Platform considerations for screen capture protection on macOS

Screen capture protection is fully supported on Windows, but it has known limitations on macOS due to the platform's current security architecture:

- **Microsoft Teams compatibility**: on macOS, enabling screen capture protection might interfere with screen sharing in Microsoft Teams, potentially causing shared windows to appear blank or not display properly. If Teams-based collaboration is required, screen capture protection might need to be temporarily disabled on the device.
- **Platform-level enforcement**: due to macOS restrictions, some native applications might not fully respect screen capture protection enforcement. This is a limitation of the operating system's available APIs, not a defect in screen capture protection itself.

Here are some recommendations for these limitations:

- For collaboration-heavy macOS workflows, consider configuring screen capture protection settings based on business need and risk level.
- For highly sensitive content, Windows endpoints are recommended for full enforcement of screen protection features.
- Watermarking and administrative policies can be used to further discourage misuse on platforms with limited enforcement.

## Admin deployment patterns

The following patterns describe common deployment scenarios for screen capture protection:

### Pattern 1: Native desktop clients (Windows and macOS)

Use this pattern when users connect with the natively installed Windows App or Remote Desktop client on Windows or macOS.

- Configure screen capture protection on the virtual machines (Azure Virtual Desktop) or Cloud PCs (Windows 365) using an Intune device configuration policy or Group Policy.
- Windows App and the Remote Desktop client enforce the configured screen capture protection settings automatically.

An Intune MAM app protection policy isn't required for these native clients. Browser connections use a different configuration, even when the browser runs on a Windows device. For browser connections, follow Pattern 3: Web endpoints (browser access).

### Pattern 2: Mixed endpoints (Windows/macOS and Android/iOS)

If your users connect from both desktop and mobile devices, use hybrid enforcement. Configure screen capture protection on both the virtual machine or Cloud PC and the Intune MAM app protection policy.

- Configure virtual machines (Azure Virtual Desktop) or Cloud PCs (Windows 365) with screen capture protection enabled (Intune or Group Policy).
- Configure an Intune MAM app protection policy to block screen capture on Android and iOS/iPadOS devices.
- On Android and iOS/iPadOS, Windows App supports hybrid enforcement: if both the admin-configured SCP and the MAM policy block screen capture, the connection is allowed and screen capture is blocked. If the MAM policy doesn't block screen capture, the Android and iOS/iPadOS connection is blocked.

### Pattern 3: Web endpoints (browser access)

For Windows App in a web browser, use Microsoft Edge for Business on Windows with an Intune MAM app protection policy that targets Microsoft Edge. Also configure a Conditional Access policy that requires app protection before allowing access to your remote resources.

The user must sign in to an Edge work profile with your organization's work account and use that same account to access Windows App from that profile. Signing in to the Windows App website alone isn't sufficient: the Edge work profile must receive your organization's app protection policy.

Assign the app protection policy to the users who require protection. For example, if a contractor accesses your organization's remote resources using a work account that your organization provides, include that account in the policy assignment. Assigning the policy to a different account doesn't protect the profile used for that connection.

A user might have work accounts from more than one organization, such as a contractor who works for several clients. On a device that none of these organizations manages, the user signs in to a separate Edge work profile for each work account. Each profile receives only its own organization's app protection policy. To connect to your remote resources with screen capture protection, the user must open Windows App from the profile that's signed in with your organization's work account.

Users don't need to enroll their devices in your organization's device management. Web screen capture protection is supported on personal devices and, with Microsoft Edge for Business version 147 or later, on devices managed by a different organization, such as a contractor's employer. The following limitations apply:

- **Devices managed by your organization**: devices managed by the same tenant that applies the app protection policy aren't supported with this configuration. Users on these devices can't access your remote resources from the browser when the Conditional Access policy applies. They can connect with the natively installed Windows App instead, with screen capture protection configured on your virtual machines or Cloud PCs as described in Pattern 1.
- **Endpoint DLP on the device**: if device-level Endpoint DLP is enabled, the app protection policy can't be applied to the Edge work profile unless the organization that manages the device configures the `MAMWithDeviceDLPEnabled` policy for Microsoft Edge. For a device managed by a contractor's employer, the contractor's employer must configure this policy.
- **Microsoft Defender for Cloud Apps DLP policies**: in Microsoft Edge version 149 and later, if a Microsoft Defender for Cloud Apps DLP policy also applies, it's enforced instead of the app protection policy. Both policies belong to your organization, so you can adjust the Defender for Cloud Apps policy to get the behavior you want.

For more information, see [Supported scenarios and known limitations](/en-us/deployedge/microsoft-edge-cross-tenant-support-using-intune-mam#supported-scenarios-and-known-limitations).

To configure this pattern:

- Create a Conditional Access policy that targets your remote resources, applies to the **Windows** device platform and the **Browser** client app, and requires an app protection policy. For the resources to select, see Step 2: Require app protection before allowing access with Conditional Access.
- Create an Intune MAM app protection policy for Windows that targets Microsoft Edge and restricts cut, copy, and paste to organizational sources and destinations, which activates screen capture protection across the Edge work profile.
- For configuration steps, see Enable screen capture protection with Intune MAM.

## Prerequisites

Before you can configure screen capture protection, ensure you meet the following prerequisites:

- For scenarios where you need to configure virtual machines or Cloud PCs, those virtual machines or Cloud PCs must be running Windows 11, version 22H2 or later, or Windows 10, version 22H2 or later.
- Users connecting with a natively installed client must use a supported version of Windows App or the Remote Desktop client. The following tables show supported native-client scenarios:

    - Windows App:

        | Platform | Minimum version | Desktop session | RemoteApp session |
        | --- | --- | --- | --- |
        | Windows App on Windows | Any | Yes | Yes. Local device OS must be Windows 11, version 22H2 or later. |
        | Windows App on macOS | Any | Yes | Yes |
        | Windows App on iOS/iPadOS | 11.2.4 | Yes | Yes |
        | Windows App on Android¹ | 11.0.0.94 | Yes | Yes |

        ^1. Doesn't include support for ChromeOS because Intune MAM isn't supported on ChromeOS.^
    - Remote Desktop client:

        | Platform | Minimum version | Desktop session | RemoteApp session |
        | --- | --- | --- | --- |
        | Windows (desktop client) | 1.2.1672 | Yes | Yes. Local device OS must be Windows 11, version 22H2 or later. |
        | macOS | 10.7.0 | Yes | Yes |
- For Windows App in a web browser, you need:

    - Microsoft Edge for Business on Windows, version **134.0.3124.51** or later. On devices managed by a different organization, version **147** or later is required. We recommend using the latest version of Microsoft Edge.
    - A personal Windows device, or a Windows device managed by a different organization. Devices managed by the same tenant that applies the app protection policy aren't supported. For other device limitations, including Endpoint DLP, see [Supported scenarios and known limitations](/en-us/deployedge/microsoft-edge-cross-tenant-support-using-intune-mam#supported-scenarios-and-known-limitations).
    - An Edge work profile signed in with the organization's work account that the user uses to access Windows App.
    - A Microsoft Entra ID security group containing the users' work accounts. Use this group when assigning the Intune app protection policy and the corresponding Conditional Access policy.

    For additional Intune and Conditional Access prerequisites, see [Require local client device security compliance with Microsoft Intune and Microsoft Entra Conditional Access](/en-us/windows-app/require-device-security-compliance-intune#prerequisites).
- To configure an Intune device configuration policy on virtual machines or Cloud PCs, you need:

    - A Microsoft Entra ID account that's assigned the [Policy and Profile manager](/en-us/intune/fundamentals/role-based-access-control/ref-built-in-roles#policy-and-profile-manager) built-in RBAC role.
    - A group containing the virtual machines or Cloud PCs you want to configure.
- To configure Group Policy, you need:

    - A domain account that is a member of the **Domain Admins** security group.
    - A security group or organizational unit (OU) containing the devices you want to configure.

## Enable screen capture protection on virtual machines and Cloud PCs using an Intune device configuration policy or Group Policy

Select the relevant tab for your scenario.

# [Microsoft Intune](#tab/intune)
To configure screen capture protection on virtual machines (Azure Virtual Desktop) or Cloud PCs (Windows 365) using Microsoft Intune:

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).
2. [Create or edit a configuration profile](/en-us/intune/device-configuration/settings-catalog/configure-admx-templates-windows) for **Windows 10 and later** devices, with the **Settings catalog** profile type.
3. In the settings picker, browse to **Administrative templates** &gt; **Windows Components** &gt; **Remote Desktop Services** &gt; **Remote Desktop Session Host** &gt; **Azure Virtual Desktop**.

    [![A screenshot showing the Azure Virtual Desktop options in the Microsoft Intune portal.](media/administrative-template/azure-virtual-desktop-intune-settings-catalog.png)](media/administrative-template/azure-virtual-desktop-intune-settings-catalog.png#lightbox)
4. Check the box for **Enable screen capture protection**, then close the settings picker.
5. Expand the **Administrative templates** category, then toggle the switch for **Enable screen capture protection** to **Enabled**.

    [![A screenshot showing the screen capture protection settings in Microsoft Intune.](media/screen-capture-protection/screen-capture-protection-intune.png)](media/screen-capture-protection/screen-capture-protection-intune.png#lightbox)
6. Toggle the switch for **Screen Capture Protection Options (Device)** to **off** for **Block screen capture on client**, or **on** for **Block screen capture on client and server** based on your requirements, then select **OK**.
7. Select **Next**.
8. *Optional*: On the **Scope tags** tab, select a scope tag to filter the profile. For more information about scope tags, see [Use role-based access control (RBAC) and scope tags for distributed IT](/en-us/intune/fundamentals/role-based-access-control/scope-tags).
9. On the **Assignments** tab, select the group containing the computers providing a remote session you want to configure, then select **Next**.
10. On the **Review + create** tab, review the settings, then select **Create**.
11. Once the policy applies to the computers providing a remote session, restart them for the settings to take effect.

# [Group Policy](#tab/group-policy)
To configure screen capture protection on virtual machines (Azure Virtual Desktop) or Cloud PCs (Windows 365) using Group Policy in an Active Directory domain:

1. Follow the steps to make the [Administrative template for Azure Virtual Desktop](administrative-template) available in Group Policy.
2. Open the **Group Policy Management** console on a device you use to manage the Active Directory domain.
3. Create or edit a policy that targets the computers providing a remote session you want to configure.
4. Navigate to **Computer Configuration** &gt; **Policies** &gt; **Administrative Templates** &gt; **Windows Components** &gt; **Remote Desktop Services** &gt; **Remote Desktop Session Host** &gt; **Azure Virtual Desktop**.

    [![A screenshot showing the Azure Virtual Desktop options in Group Policy.](media/administrative-template/azure-virtual-desktop-gpo.png)](media/administrative-template/azure-virtual-desktop-gpo.png#lightbox)
5. Double-click the policy setting **Enable screen capture protection** to open it, then select **Enabled**.

    [![A screenshot showing the screen capture protection settings in Group Policy.](media/screen-capture-protection/screen-capture-protection-group-policy.png)](media/screen-capture-protection/screen-capture-protection-group-policy.png#lightbox)
6. From the drop-down menu, select the screen capture protection scenario you want to use from **Block screen capture on client** or **Block screen capture on client and server** based on your requirements, then select **OK**.
7. Ensure the policy is applied to the computers providing a remote session, then restart them for the settings to take effect.

---

## Enable screen capture protection with Intune MAM

For Android, iOS/iPadOS, and the web client (on Windows), you enforce screen capture protection through Intune mobile application management (MAM). For each of these approaches, the configuration has two parts:

1. **Apply screen capture protection**: configure an Intune MAM app protection policy with the required screen capture protection settings. The supported client app enforces those settings.
2. **Require app protection before allowing access**: configure a Conditional Access policy that requires an app protection policy before users can access the targeted remote resources.

### Step 1: Apply screen capture protection with an Intune MAM app protection policy

Configure an Intune MAM app protection policy for the platform your users connect from. Follow the steps in [Create an app protection policy](/en-us/windows-app/require-device-security-compliance-intune#create-an-app-protection-policy), and use the app selection and screen capture protection settings below for your platform:

- **iOS/iPadOS** (Windows App): set **Screen capture** to **Block**.

    [![A screenshot showing the iOS screen capture protection settings in MAM policy.](media/screen-capture-protection/ios-toggle-for-screencaptureprotection-on-mobileapplicationmanagement.jpg)](media/screen-capture-protection/ios-toggle-for-screencaptureprotection-on-mobileapplicationmanagement.jpg#lightbox)
- **Android** (Windows App): set **Screen capture** to **Block**.

    [![A screenshot showing the Android screen capture protection settings in MAM policy.](media/screen-capture-protection/android-toggle-for-screencaptureprotection-on-mobileapplicationmanagement.jpg)](media/screen-capture-protection/android-toggle-for-screencaptureprotection-on-mobileapplicationmanagement.jpg#lightbox)
- **Web (Microsoft Edge for Business on Windows)**: create or edit an Intune app protection policy with the following settings:

    | Setting | Value |
    | --- | --- |
    | **Policy platform** | **Windows** |
    | **Apps** | **Microsoft Edge** |
    | **Data protection** &gt; **Allow cut, copy, and paste for** | **Org data destinations and org data sources** |
    | **Assignments** | Include the security group containing the work accounts that users sign in to their Edge work profiles with. Confirm that these users aren't excluded from the policy. |

    For web connections, Microsoft Edge is the app that receives the app protection policy, not the natively installed Windows App. The user must access Windows App from the Edge work profile that receives this policy.

    The clipboard setting above restricts copy and paste and automatically activates screen capture protection across the entire protected Edge work profile, including all tabs in that profile. Protection isn't limited to the Windows App tab. For more information, see [Data protection features for Microsoft Edge using Intune App Protection (MAM)](/en-us/deployedge/microsoft-edge-enabling-dlp-features#protected-clipboard).

Configure other settings based on your requirements, then assign the app protection policy to your users.

### Step 2: Require app protection before allowing access with Conditional Access

The Intune MAM app protection policy configures screen capture protection, and the supported client app enforces it. For web connections, Microsoft Edge for Business enforces protection in the work profile that receives the policy.

Conditional Access doesn't block screen capture itself. It requires an app protection policy before granting access to the targeted remote resources, preventing access through an unprotected app or browser. For web connections, users might be prompted to sign in to the required Edge work profile and complete MAM registration. Signing in alone isn't sufficient; the app protection policy must be applied.

For web connections, distinguish the policy targets:

- The Intune app protection policy targets **Microsoft Edge**, the client app that enforces protection.
- The Conditional Access policy targets the **remote resources** users access. Select **Browser** under **Conditions &gt; Client apps**, not as a target resource.

In the [Microsoft Entra admin center](https://entra.microsoft.com/), create a policy with the following settings:

| Setting | Value |
| --- | --- |
| **Target resources** &gt; **Resources (formerly cloud apps)** | - **Azure Virtual Desktop**: select **Azure Virtual Desktop** (app ID `9cdead84-a844-4324-93f2-b2e6bb768d07`). It might be listed as **Windows Virtual Desktop**.- **Windows 365**: select **Windows 365** (app ID `0af06dc6-e4b5-4f28-818e-e78e62d137a5`) and **Azure Virtual Desktop**. Windows 365 might be listed as **Cloud PC**.- **Single sign-on**: if single sign-on is enabled, also select **Windows Cloud Login** (app ID `270efc09-cd0d-444b-a71f-39af4910ec45`). |
| **Grant** | **Require app protection policy** |

Under **Conditions**, set the device platform and client app for each platform you want to protect:

| Platform | **Device platforms** | **Client apps** |
| --- | --- | --- |
| **Android** | **Android** | **Mobile apps and desktop clients** |
| **iOS/iPadOS** | **iOS** | **Mobile apps and desktop clients** |
| **Web (Windows)** | **Windows** | **Browser** |

Create the web policy separately from any Android and iOS/iPadOS policy. Native clients on Windows, such as Windows App, don't support app protection policies. A policy that includes both the **Windows** device platform and **Mobile apps and desktop clients** blocks their connections.

For more information about these resources, including how a policy that targets Windows 365 can also affect admin portal sign-ins, see [Set Conditional Access policies for Windows 365](/en-us/windows-365/enterprise/set-conditional-access-policies) and [Enforce Microsoft Entra multifactor authentication for Azure Virtual Desktop using Conditional Access](set-up-mfa).

Assign each policy to the same users as the corresponding app protection policy.

Important

- This Conditional Access configuration isn't supported on Windows devices managed by the same tenant that applies the app protection policy. Users on these devices can't access your remote resources from the browser when this policy applies. For these devices, users can connect with the natively installed Windows App, which enforces the screen capture protection configured on your virtual machines or Cloud PCs.
- Don't add **Require device to be marked as compliant** to this policy. Microsoft Edge doesn't support that grant for this configuration, and it blocks users from MAM enrollment.

## Verify screen capture protection

To verify screen capture protection is working:

1. Connect to a new remote session with a supported client. Don't reconnect to an existing session. You need to sign out of any existing sessions and sign back in for the change to take effect.
2. From a local device, take a screenshot or share your screen in a Teams call or meeting. The content is blocked or hidden.
3. On Windows and macOS devices, if you enabled **Block screen capture on client and server** on your virtual machines or Cloud PCs, try to capture the screen using a tool or service within the virtual machine or Cloud PC. The content is blocked or hidden.

If you enable screen capture protection on virtual machines or Cloud PCs, you must connect from a supported device. If you don't, you see an error message indicating that screen capture protection is enabled. The error message looks similar to these screenshots:

- Web browser:

    ![A screenshot from Windows App in a web browser showing an error message that screen capture is enabled and you need to connect from a supported client.](media/screen-capture-protection/screen-capture-protection-connection-blocked-web.png)
- iOS/iPadOS:

    ![A screenshot from Windows App for iOS/iPadOS showing an error message that screen capture is enabled and you need to connect from a supported client.](media/screen-capture-protection/screen-capture-protection-connection-blocked-ios-ipados.png)

### Verify and troubleshoot web screen capture protection

For Windows App in a web browser, verify both that the Edge work profile receives the required app protection policy and that Conditional Access requires app protection before granting access.

1. **Check the browser and device.** Confirm the following:

    - The user is using Microsoft Edge for Business on Windows, version 134.0.3124.51 or later, or version 147 or later on a device managed by a different organization.
    - The device isn't managed by the same tenant that applies the app protection policy. This configuration doesn't support those devices.
    - Endpoint DLP isn't blocking the app protection policy. In Microsoft Edge, go to `edge://edge-dlp-internals`. On the **Feature Status** page, if Endpoint DLP is listed as the provider with a state of **Available**, device-level Endpoint DLP is enabled. The app protection policy can't be applied until the organization that manages the device configures the `MAMWithDeviceDLPEnabled` policy for Microsoft Edge. That organization can set it in Intune for Edge 148 and later, or with Group Policy or the registry for Edge 147. For more information, see [How to verify whether Endpoint DLP is enabled on a device](/en-us/deployedge/microsoft-edge-cross-tenant-support-using-intune-mam#how-to-verify-whether-endpoint-dlp-is-enabled-on-a-device).
2. **Check the signed-in identity.** Confirm that the user is signed in to the Edge work profile with your organization's work account and accesses Windows App from that profile using the same account. Signing in to the website alone isn't sufficient. Complete any required work-profile sign-in and MAM registration prompts. If the user has work profiles for more than one organization, confirm they're using the one for your organization. Each profile receives only its own organization's app protection policy.
3. **Check app protection policy targeting and settings.** Confirm that the Windows app protection policy targets **Microsoft Edge**, includes the user's work account through its assigned group, and doesn't exclude that user. Under **Data protection**, confirm that **Allow cut, copy, and paste for** is set to **Org data destinations and org data sources**. If your organization also applies a Microsoft Defender for Cloud Apps DLP policy, in Microsoft Edge version 149 and later that policy is enforced instead of the app protection policy.
4. **Check policy delivery.** In the Microsoft Intune admin center, go to **Apps &gt; Monitor &gt; App protection status**. Review the policy name, app version, and last sync for the user's app instance. Check that the expected policy is reported and that the app has checked in since the configuration changed. Assignment alone doesn't confirm that the tested app instance has received the latest configuration. For more information, see [Monitor app protection policies](/en-us/intune/app-management/protection/monitor-policies).
5. **Check Conditional Access.** Confirm that the policy includes the intended user and remote resources, applies to **Windows** and **Browser**, and uses **Require app protection policy**. A policy in **Report-only** mode doesn't enforce this requirement. Review the user's Microsoft Entra sign-in event to identify which policies applied and any failure details. See [Troubleshoot Conditional Access sign-in problems](/en-us/entra/identity/conditional-access/troubleshoot-conditional-access).
6. **Test a new remote session.** After the required policy is applied, save any work and sign out of the existing remote session. Start a new session from the protected Edge work profile and attempt a local screenshot. The protected remote content should be blocked or hidden. Using a test account, also verify that access without the required app protection isn't granted until the access requirements are met.

If the result is unexpected, record the affected work account, Edge version, policy names, reproduction time, and any sign-in error or correlation ID for further troubleshooting. Check policy targeting and delivery before concluding that the browser scenario is unsupported.

### Verify and troubleshoot Android or iOS/iPadOS hybrid enforcement

When admin-configured SCP is enabled, Android or iOS/iPadOS connections are only allowed if the MAM app protection policy also blocks screen capture (hybrid enforcement).

To verify Android or iOS/iPadOS hybrid enforcement is working:

1. Confirm the Intune MAM app protection policy is applied to the user and device. In the Microsoft Intune admin center, check the app protection policy status for the user under **Apps** &gt; **Monitor** &gt; **App protection status**.
2. On the Android or iOS/iPadOS device, sign out of Windows App and sign back in to pick up the latest policy settings.
3. Connect to the remote session. If both the admin-configured SCP and the MAM policy block screen capture, the connection succeeds and screen capture is blocked.

If Android or iOS/iPadOS connections are blocked unexpectedly, check the following:

- Verify the MAM app protection policy is assigned to the user and that **Screen capture** is set to **Block**.
- Restart Windows App on the Android or iOS/iPadOS device or sign out and sign back in.
- Confirm that the installed version of Windows App for Android or iOS/iPadOS supports hybrid enforcement.
- Confirm the Android device isn't running ChromeOS or Meta Quest, which don't support Intune MAM.

Tip

If a user is blocked because the MAM policy isn't applied or doesn't block screen capture, recommend the following message to help them understand the issue:

> 
> "Your organization requires screen capture protection to be enforced on your device to connect to this remote session. Make sure you're using Windows App with an app protection policy that blocks screen capture. Contact your IT admin for assistance."