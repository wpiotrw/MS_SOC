---
layout: Conceptual
title: Configure context-based redirection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/context-based-redirections
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to configure context-based redirection for Azure Virtual Desktop and Windows 365 by using Microsoft Entra authentication context.
author: suderek-msft
ms.author: suderek
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-11-16T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
ai-usage: ai-assisted
locale: en-us
document_id: 950b442e-c503-e961-2aa7-2e17a21efafa
document_version_independent_id: 950b442e-c503-e961-2aa7-2e17a21efafa
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/context-based-redirections.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/context-based-redirections
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/context-based-redirections.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: 4ae19de6-a084-1677-e3fc-b1d4ee834afb
---

# Configure context-based redirection | Microsoft Learn

Important

The streaming stack powering Windows 365 and Azure Virtual Desktop is now branded as Direct Stream. This article retains RDP terminology where it still appears in the Microsoft Intune admin center and Azure portal during the transition. For more information, see [Windows 365 at Ignite 2026: Introducing new Cloud PC capabilities for people, agents and IT](https://aka.ms/W365Ignite26Blog).

Context-based redirection enables you to control redirection behavior based on user and session conditions. By using authentication context, you can define when specific client capabilities are allowed or restricted based on factors such as user role, device compliance, or network location. This control helps ensure that sensitive data is only accessible when the session meets the required level of trust.

Context-based redirection is supported for Windows 365 Enterprise, Windows 365 Flex (dedicated mode), Windows 365 Reserve, and Azure Virtual Desktop. Azure Virtual Desktop support includes RemoteApp sessions.

You can apply authentication context to control the following redirections:

- Control clipboard redirection.
- Control drive and storage redirection.
- Control printer redirection.
- Control USB redirection.

Select a tab for your product. Your selection is used for all product-specific steps in this article.

# [Windows 365](#tab/windows-365)
To configure context-based redirection for Windows 365:

1. Create a Conditional Access authentication context.
2. Create a Conditional Access policy that targets the authentication context and specifies the required sign-in conditions. Assign the policy to a user group.
3. Create a device configuration policy in Microsoft Intune that allows the redirections you want to control at the Cloud PC level. Assign the policy to a device group that contains the target Cloud PCs.
4. Create a Windows 365 [Remote Connection Experience](/en-us/windows-365/enterprise/remote-connection-experience) policy in Microsoft Intune that maps the authentication context to the redirections you want to control. Assign the policy to a device group that contains the target Cloud PCs.

After you configure context-based redirection, connect to a targeted Cloud PC and verify that the redirections behave as expected.

Context-based redirection supports full desktop sessions in Windows App on Windows, web browsers, Android, iOS/iPadOS, and macOS.

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
To configure context-based redirection for Azure Virtual Desktop:

1. Create a Conditional Access authentication context.
2. Create a Conditional Access policy that targets the authentication context and specifies the required sign-in conditions. Assign the policy to a user group.
3. Configure the Azure Virtual Desktop host pool's DS properties to map the authentication context to the redirections you want to control. These settings apply to all session hosts in the host pool.

After you configure context-based redirection, connect to a desktop or launch a RemoteApp from the targeted Azure Virtual Desktop host pool and verify that the redirections behave as expected.

Context-based redirection supports full desktop and RemoteApp sessions in Windows App on Windows, web browsers, Android, iOS/iPadOS, and macOS.

---

## Create the Conditional Access authentication context

Authentication contexts are shared identifiers between Microsoft Entra Conditional Access and context-based redirection policies. An authentication context doesn't grant or block redirections. It enables Azure Virtual Desktop or Windows 365 to evaluate whether the Conditional Access requirements associated with that authentication context are satisfied before enabling the configured redirections.

For more information, see [Conditional Access authentication context](/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Select **Entra ID** &gt; **Conditional Access** &gt; **Authentication contexts**.
3. Select **New authentication context**.
4. Enter a name and description for the authentication context.
5. Select **Publish to apps**, and then select an available value from the **ID** list.
6. Select **Save**.

[![Screenshot that shows Microsoft Entra admin center Authentication contexts page. The New authentication context pane shows All Managed, Compliant Devices as the name, a description for trusted sessions from managed and compliant devices, Publish to apps selected, and c8 as the ID.](media/context-based-redirections/auth-context-for-all-managed-compliant-devices.png)](media/context-based-redirections/auth-context-for-all-managed-compliant-devices.png#lightbox)

In this example, an authentication context named **All Managed, Compliant Devices** is published for use in Conditional Access policies. The authentication context acts as a label that connects the Conditional Access requirements to context-based redirection settings. Make a note of its name and ID. You use the same authentication context when you create the Conditional Access policy and configure the product-specific redirection settings.

## Create the Microsoft Entra Conditional Access policy

1. In **Conditional Access**, select **Policies**.
2. Select **New policy**.
3. Enter a name for the policy.
4. Under **Users or workload identities**, include the users or groups to which the policy applies.
5. Under **Target resources**, select **Authentication context**, and then select the authentication context you created.
6. Under **Grant**, select **Grant access** &gt; **Require device to be marked as compliant** &gt; **Select**.
7. (Optional) Under **Conditions** &gt; **Network**, configure the network locations where the policy applies. You can use Microsoft Entra named locations to apply Conditional Access requirements based on the user's network location.

    For more information, see [Conditional Access policy: Use network signals](/en-us/entra/identity/conditional-access/concept-assignment-network).
8. Set **Enable policy** to **On**.
9. Select **Create**.

The following example policy requires the targeted users to connect from a compliant device. Network conditions are optional and aren't configured in this example.

| Setting | Value |
| --- | --- |
| Users or workload identities | Targeted users or groups |
| Target resources | Authentication contexts |
| Authentication context | Selected authentication context |
| Conditions &gt; Network | Not configured (optional) |
| Grant access | Enabled |
| Require device to be marked as compliant | Selected |
| Require all selected controls | Selected |
| Enable policy | On |

[![Screenshot that shows Microsoft Entra Conditional Access policy page for Assigned All - Managed, Compliant Devices. The policy includes all users and one authentication context. In the Grant pane, Grant access, Require device to be marked as compliant, and Require all the selected controls are selected. Enable policy is set to On.](media/context-based-redirections/conditional-access-grant-require-compliant.png)](media/context-based-redirections/conditional-access-grant-require-compliant.png#lightbox)

Users connecting from compliant devices now satisfy the authentication context requirement. Next, associate the authentication context with the redirections you want to control.

## Configure redirections for your product

# [Windows 365](#tab/windows-365)
### Configure redirection settings for Windows 365 Cloud PCs

Before configuring context-based redirection for Windows 365, you must ensure that the redirections you want to control are allowed on your Cloud PCs.

By default, clipboard, drive, printer, and opaque low-level USB redirections are disabled for Windows 365 Cloud PCs. To opt out of these defaults for the redirections you want to manage, create a device configuration policy in Microsoft Intune by using the Settings catalog.

The following components have separate roles:

- **Settings catalog:** Allows the selected redirections at the Cloud PC level.
- **Context-based redirection:** Determines whether each redirection is available for a particular connection.
- **Conditional Access:** Evaluates whether the connection satisfies the required authentication context.

The Settings catalog policy doesn't dynamically enable redirections for individual connections. It allows them at the Cloud PC level, subject to other applicable restrictions. Context-based redirection uses the Conditional Access evaluation to determine their availability for each connection.

Important

Context-based redirection follows the most restrictive applicable policy. If a redirection is disabled by another policy, such as an existing Microsoft Intune configuration policy or Group Policy, context-based redirection can't enable it, even when the authentication context requirements are satisfied.

Make sure the redirections you intend to control are allowed on the Cloud PC before configuring context-based redirection policies.

#### Create a device configuration policy in Microsoft Intune

To configure the redirections you want to use with context-based redirection:

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).
2. Select **Devices** &gt; **Configuration** &gt; **Policies**.
3. Select **Create** &gt; **New policy**.
4. Under **Create a profile**, configure the following settings:

    - **Platform:** Select **Windows 10 and later**.
    - **Profile type:** Select **Settings catalog**.
5. Select **Create**.
6. On the **Basics** page, enter the following information:

    - **Name:** Enter a descriptive name for the policy, such as `Windows 365 - Allow Context-Based Redirection`.
    - **Description:** Optionally, enter a description explaining which redirections the policy allows.
7. Select **Next**.
8. On the **Configuration settings** page, select **+ Add settings** to open the **Settings picker**.
9. In the **Settings picker**, select **Administrative Templates** &gt; **Windows Components** &gt; **Remote Desktop Services** &gt; **Remote Desktop Session Host**.
10. Select the appropriate category and add the settings for the redirections you want to allow at the Cloud PC level.

    The following table lists the four supported redirections and their corresponding Settings catalog locations.

    | Redirection | Settings catalog category | Setting |
    | --- | --- | --- |
    | Clipboard | **Device and Resource Redirection** | **Do not allow Clipboard redirection** |
    | Drive | **Device and Resource Redirection** | **Do not allow drive redirection** |
    | Printer | **Printer Redirection** | **Do not allow client printer redirection** |
    | USB | **Device and Resource Redirection** | **Do not allow supported Plug and Play device redirection** |
11. After selecting the settings you want to configure, close the **Settings picker**.
12. Under **Configuration settings**, set each selected setting to **Disabled**.

    Note

    These settings use the wording "Do not allow." Setting them to **Disabled** allows the corresponding redirection on the Cloud PC.

    - **Disabled:** Allows the redirection at the Cloud PC level.
    - **Enabled:** Blocks the redirection at the Cloud PC level.

    You only need to configure the redirections you intend to use with context-based redirection policies.
13. Select **Next**.
14. On the **Scope tags** page, configure any applicable scope tags, and then select **Next**.
15. On the **Assignments** page:

    1. Select **Add groups**.
    2. Select the Microsoft Entra device group containing the Cloud PCs you want to configure.
    3. Select **Next**.
16. On the **Review + create** page, review your configuration and select **Create**.

[![Screenshot of a Microsoft Intune Settings catalog policy with the Do not allow settings for supported Plug and Play device, drive, clipboard, and client printer redirection set to Disabled.](media/context-based-redirections/intune-opt-out-default-disable-redirection-policy.png)](media/context-based-redirections/intune-opt-out-default-disable-redirection-policy.png#lightbox)

The device configuration policy is created and assigned to the selected Cloud PCs.

After the policy is applied, the selected redirections are allowed at the Cloud PC level, subject to other applicable restrictions. Next, configure a Windows 365 Remote Connection Experience policy to associate each redirection with an authentication context. Context-based redirection then determines whether each redirection is available for a particular connection, based on whether Conditional Access evaluates that connection as satisfying the required authentication context.

For more information, see [Manage RDP device redirections for Cloud PCs](manage-rdp-device-redirections).

#### Create and assign the Windows 365 Remote Connection Experience policy

For Windows 365, create a Remote Connection Experience policy in Intune to associate the authentication context with specific redirections.

Important

Assign the Remote Connection Experience policy to device groups that contain Cloud PCs, not user groups. Context-based redirection is enforced at the device level.

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).
2. Select **Devices** &gt; **Manage Windows 365 Cloud PCs** &gt; **Cloud PC Settings**.
3. Select **Create** &gt; **Remote Connection Experience**.

    [![Screenshot that shows Microsoft Intune admin center on the Windows 365 Settings page. The expanded Create menu lists Cloud PC configuration, Windows app customization, User settings legacy, and Remote connection experience.](media/context-based-redirections/windows-365-settings-create-policy-dropdown.png)](media/context-based-redirections/windows-365-settings-create-policy-dropdown.png#lightbox)
4. On the **Basics** page, enter a name and description, and then select **Next**.
5. On the **Configuration settings** page, expand **Device redirections**. For a targeted redirection, select **Authentication context: Context-based redirection**.

    [![Screenshot that shows Microsoft Intune admin center Create setting page for a Remote Connection Experience policy. Under Device redirections, the Drive and Storage redirection menu includes Authentication context Context-based redirection for all drives.](media/context-based-redirections/remote-connection-experience-authentication-context-dropdown.png)](media/context-based-redirections/remote-connection-experience-authentication-context-dropdown.png#lightbox)
6. In the **Entra Authentication context** list that appears, select the authentication context you created. Repeat this step for each redirection you want to control.

    [![Screenshot that shows Microsoft Intune admin center Create setting page. Drive and Storage, Clipboard, Printer, and USB redirection are each set to Authentication context Context-based redirection, and each Entra Authentication context field is set to c8 All Managed, Compliant Devices.](media/context-based-redirections/set-remote-connection-experience-authentication-context-option.png)](media/context-based-redirections/set-remote-connection-experience-authentication-context-option.png#lightbox)
7. On the **Scope tags** page, select any scope tags to apply, and then select **Next**.
8. On the **Assignments** page, select **Add groups**, select the device groups that contain the Cloud PCs, and then select **Next**.
9. On the **Review + create** page, select **Create**.

#### Verify your redirection configuration

After creating the device configuration policy and the Remote Connection Experience policy:

1. In the Microsoft Intune admin center, select **Devices** &gt; **Configuration**.
2. Select the device configuration policy you created.
3. Review the device assignment and configuration status to confirm that the policy has been applied successfully.
4. Verify that no other configuration policies or Group Policies are blocking the redirections you want to control.
5. Connect to a targeted Cloud PC and verify that the redirections behave as expected based on your configured authentication context and Conditional Access policies.

Important

Allowing redirections through the Settings catalog doesn't override restrictions enforced by other applicable policies.

For example, if clipboard redirection is allowed through the Settings catalog but restricted by a context-based redirection policy, clipboard redirection remains unavailable when the connection doesn't satisfy the required authentication context.

If you make changes to your redirection policies, disconnect and reconnect to your Cloud PC to verify the updated behavior.

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
For Azure Virtual Desktop, configure context-based redirection on the host pool. The settings apply to all session hosts in that host pool for both full desktop sessions and RemoteApp sessions.

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Search for and select **Azure Virtual Desktop**.
3. Select **Host pools**, and then select the host pool you want to configure.
4. Select **RDP Properties** &gt; **Device redirection**.
5. For a redirection you want to control, select **Dynamically configure using authentication context**.
6. In the **Authentication context** list that appears, select the authentication context you created.
7. Repeat the previous two steps for each additional redirection you want to control.
8. Select **Save**.

[![Screenshot that shows Azure portal showing a host pool RDP Properties page with the Device redirection tab selected. Drive and storage redirection and Clipboard redirection are set to Dynamically configure using authentication context, and C8 All Managed, Compliant Devices is selected as the authentication context.](media/context-based-redirections/azure-virtual-desktop-rdp-properties-select-authentication-context-option.png)](media/context-based-redirections/azure-virtual-desktop-rdp-properties-select-authentication-context-option.png#lightbox)

---

## Validate context-based redirection

# [Windows 365](#tab/windows-365)
1. From a managed, compliant device that satisfies the Conditional Access policy, connect to the targeted Cloud PC.
2. Verify that the configured redirections are available in the remote session.
3. From a bring-your-own-device (BYOD) or noncompliant device that doesn't satisfy the policy, connect to the same Cloud PC.
4. Verify that the configured redirections are restricted or unavailable.

If the expected behavior doesn't occur, review:

- The Conditional Access policy assignment and authentication context.
- The device compliance status in Microsoft Entra ID and Intune.
- The Windows 365 Remote Connection Experience policy assignment.
- Existing redirection policies that might override the configuration.

To investigate the effective redirection settings and contributing policy sources, see View effective redirection settings with Resultant Set of Policies (Preview).

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
1. From a managed, compliant device that satisfies the Conditional Access policy, connect to a desktop or launch a RemoteApp from the targeted Azure Virtual Desktop host pool.
2. Verify that the configured redirections are available in the remote session.
3. From a bring-your-own-device (BYOD) or noncompliant device that doesn't satisfy the policy, connect to the same desktop or launch the same RemoteApp.
4. Verify that the configured redirections are restricted or unavailable.
5. If you publish both desktops and RemoteApp applications, repeat these checks for both session types.

If the expected behavior doesn't occur, review:

- The Conditional Access policy assignment and authentication context.
- The device compliance status in Microsoft Entra ID and Intune.
- The Azure Virtual Desktop host pool DS properties.
- Existing redirection policies that might override the configuration.

---

You can validate individual redirections by using the guidance in the following articles:

- **Clipboard:** Verify whether copy and paste work between the local device and remote session.
- **Drive and storage:**[Configure drive redirection over Direct Stream](/en-us/azure/virtual-desktop/redirection-configure-drives-storage).
- **Printer:**[Configure printer redirection over Direct Stream](/en-us/azure/virtual-desktop/redirection-configure-printers).
- **USB:**[Configure USB redirection over Direct Stream](/en-us/azure/virtual-desktop/redirection-configure-usb).

# [Windows 365](#tab/windows-365)
## View effective redirection settings with Resultant Set of Policies (Preview)

Use Resultant Set of Policies (RSOP) to review the effective redirection settings applied to Windows 365 Cloud PC connections. RSOP shows whether a redirection is enabled or disabled for a connection and reports contributing configuration sources to help you troubleshoot unexpected redirection behavior.

RSOP is available for the following redirection capabilities:

- Clipboard redirection
- Printer redirection
- USB redirection
- Drive redirection

### View Resultant Set of Policies

For Windows 365, RSOP information is available through the connection reporting experience in Microsoft Intune.

To review effective redirection settings:

1. Sign in to the Microsoft Intune admin center.
2. Navigate to Devices &gt; Monitor Cloud PCs (under Manage Windows 365 devices)
3. Open the View data table
4. Select the Connection configuration tab
5. Locate the connection you want to investigate.
6. Review the effective redirection settings for the connection.
7. Review the reported policy sources.

[![Screenshot of the Connection configuration tab in Microsoft Intune showing effective drive and storage, printer, USB, and clipboard redirection settings and their policy sources.](media/context-based-redirections/rsop-screenshot.png)](media/context-based-redirections/rsop-screenshot.png#lightbox)

For each supported redirection, administrators can review the following information:

- **Effective value:** Whether the redirection is enabled or disabled for the connection.
- **Policy source:** The available configuration sources contributing to the effective result.

For descriptions of the reported sources, see Understand policy source information.

Policy-source information can help identify where to investigate a restriction, but it doesn't necessarily identify the specific Intune, Group Policy, or registry configuration responsible for the setting.

Note

RSOP reports the effective redirection settings for a connection. The information represents the settings evaluated for that connection and might differ from the current policy configuration if settings have changed since the connection was established.

### Understand redirection precedence

The effective redirection result for a connection depends on settings from three sources:

- **Client-side settings:** Redirection settings configured on the local device or in the client used to establish the connection.
- **VM-side settings:** Redirection settings applied to the Cloud PC or session host.
- **Service-side settings:** Redirection settings managed through the service.

Redirection settings are evaluated at two levels:

1. **Precedence within each source.** Each source determines its effective redirection setting according to its own policy evaluation rules. The effective setting reflects the outcome of those rules, so a disabled configuration doesn't necessarily take precedence over every other configuration within the same source.
2. **Result across sources.** The most restrictive effective setting across the client-side, VM-side, and service-side sources determines whether a redirection is allowed for the connection. If any of these effective settings disables a redirection, the resultant value is **Disabled**, even when the other sources allow it.

An override within one source doesn't override a restriction in another source.

#### Example: Conflicting redirection settings

Consider a connection with the following effective settings for drive redirection:

| Source | Effective setting |
| --- | --- |
| Client-side | Enabled |
| VM-side | Disabled |
| Service-side | Enabled |
| **Resultant value** | **Disabled** |

In this example, drive redirection is disabled because the effective VM-side setting restricts it, even though the client-side and service-side settings allow it.

### Understand policy source information

The following table describes the policy sources reported by RSOP and their root categories.

| Policy source | Root category | Definition |
| --- | --- | --- |
| **Machine Group Policy** (`MachineGP`) | VM-side | Machine-level redirection policy applied to the Cloud PC. |
| **User Group Policy** (`UserGP`) | VM-side | User-level redirection policy applied within the Cloud PC. |
| **Machine Clipboard Policy** (`MachineCSClipLevelGP`, `MachineSCClipLevelGP`) | VM-side | Machine-level restrictions controlling clipboard redirection between the Cloud PC and local device. |
| **User Clipboard Policy** (`UserCSClipLevelGP`, `UserSCClipLevelGP`) | VM-side | User-level restrictions controlling clipboard redirection between the Cloud PC and local device. |
| **Client Machine Group Policy** (`ClientMachineGP`) | Client-side | Machine-level redirection policy applied to the local device used to connect. |
| **Client User Group Policy** (`ClientUserGP`) | Client-side | User-level redirection policy applied to the local device. |
| **Windows App UI** (`ClientUI`) | Client-side | Redirection settings configured in Windows App. |
| **Client OS Registry** (`ClientRegistry`) | Client-side | Redirection settings obtained from the local device's registry. |
| **Windows App RDP File** (`ClientReceivedRdpFile`) | Client-side | Redirection settings supplied through the connection configuration. |
| **Conditional Access** (`ConditionalAccess`) | Service-side | Redirection restrictions based on the authentication context and its Conditional Access requirements. |
| **Cloud PC Settings** (`SessionHostRDPSettings`) | Service-side | Redirection settings configured for the Cloud PC through Windows 365. |
| **Windows 365 System Default** (`SessionHostPoolRDPSettings`) | Service-side | Default redirection settings provided through Windows 365. |

RSOP reports the effective machine policy value observed on the Cloud PC or session host. However, it doesn't identify which underlying management mechanism produced that value.

The machine policy value can originate from configurations managed through:

- Microsoft Intune.
- Active Directory Group Policy.
- Local Group Policy.
- Registry settings.

#### Example: Interpret a disabled machine policy

Suppose RSOP reports a disabled machine-level redirection setting and identifies **Machine Group Policy** (`MachineGP`) as a contributing source. This indicates a machine-level restriction on the Cloud PC. Despite its name, this source label doesn't identify whether the setting originated from Microsoft Intune, Active Directory Group Policy, local Group Policy, or registry configuration.

If an administrator configures conflicting redirection settings through Intune and Group Policy, RSOP reports the effective machine policy value after the applicable policy processing has occurred. It doesn't independently evaluate the **MDMWinsOverGP** configuration or identify which management mechanism took precedence.

To identify the originating configuration, review the applicable Intune policies, Active Directory and local Group Policies, and registry settings on the Cloud PC or session host.

Important

RSOP is a reporting capability, not a policy evaluation or enforcement engine. It displays the effective redirection result and available policy-source information but doesn't determine the precedence of underlying management configurations.

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
The RSOP reporting experience in Microsoft Intune is available only for Windows 365. For Azure Virtual Desktop, use the validation steps to verify redirection behavior.

---