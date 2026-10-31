---
layout: Conceptual
title: Configure context-based redirections (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/context-based-redirections
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to configure context-based redirections for Azure Virtual Desktop and Windows 365 by using Microsoft Entra authentication context.
author: suderek-msft
ms.author: suderek
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-10-21T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: 4ae19de6-a084-1677-e3fc-b1d4ee834afb
---

# Configure context-based redirections (Preview) | Microsoft Learn

Context-based redirection enables you to control redirection behavior based on user and session conditions. By using authentication context, you can define when specific client capabilities are allowed or restricted based on factors such as user role, device compliance, or network location. This control helps ensure that sensitive data is only accessible when the session meets the required level of trust.

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
3. Create a Windows 365 [Remote Connection Experience](/en-us/windows-365/enterprise/remote-connection-experience) policy in Microsoft Intune that maps the authentication context to the redirections you want to control. Assign the policy to a device group that contains the target Cloud PCs.

After you configure context-based redirection, connect to a targeted Cloud PC and verify that the redirections behave as expected.

Context-based redirections support full desktop sessions in Windows App on Windows, web browsers, Android, iOS/iPadOS, and macOS. Windows 365 support is limited to Windows 365 Enterprise and Windows 365 Flex dedicated mode.

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
To configure context-based redirection for Azure Virtual Desktop:

1. Create a Conditional Access authentication context.
2. Create a Conditional Access policy that targets the authentication context and specifies the required sign-in conditions. Assign the policy to a user group.
3. Configure the Azure Virtual Desktop host pool's RDP properties to map the authentication context to the redirections you want to control. These settings apply to all session hosts in the host pool.

After you configure context-based redirection, connect to a desktop or launch a RemoteApp from the targeted Azure Virtual Desktop host pool and verify that the redirections behave as expected.

Context-based redirections support full desktop sessions in Windows App on Windows, web browsers, Android, iOS/iPadOS, and macOS. RemoteApp sessions are also supported in Azure Virtual Desktop.

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
7. Set **Enable policy** to **On**.
8. Select **Create**.

The following example policy requires the targeted users to connect from a compliant device:

| Setting | Value |
| --- | --- |
| Users or workload identities | Targeted users or groups |
| Target resources | Authentication contexts |
| Authentication context | Selected authentication context |
| Grant access | Enabled |
| Require device to be marked as compliant | Selected |
| Require all selected controls | Selected |
| Enable policy | On |

[![Screenshot that shows Microsoft Entra Conditional Access policy page for Assigned All - Managed, Compliant Devices. The policy includes all users and one authentication context. In the Grant pane, Grant access, Require device to be marked as compliant, and Require all the selected controls are selected. Enable policy is set to On.](media/context-based-redirections/conditional-access-grant-require-compliant.png)](media/context-based-redirections/conditional-access-grant-require-compliant.png#lightbox)

Users connecting from compliant devices now satisfy the authentication context requirement. Next, associate the authentication context with the redirections you want to control.

## Configure redirections for your product

# [Windows 365](#tab/windows-365)
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
1. Connect to the targeted Cloud PC from a managed, compliant device that satisfies the Conditional Access policy.
2. Verify that the configured redirections are available in the remote session.
3. Connect to the same Cloud PC from a bring-your-own-device (BYOD) or noncompliant device that doesn't satisfy the policy.
4. Verify that the configured redirections are restricted or unavailable.

If the expected behavior doesn't occur, review:

- The Conditional Access policy assignment and authentication context.
- The device compliance status in Microsoft Entra ID and Intune.
- The Windows 365 Remote Connection Experience policy assignment.
- Existing redirection policies that might override the configuration.

# [Azure Virtual Desktop](#tab/azure-virtual-desktop)
1. From a managed, compliant device that satisfies the Conditional Access policy, connect to a desktop or launch a RemoteApp from the targeted Azure Virtual Desktop host pool.
2. Verify that the configured redirections are available in the desktop or RemoteApp session.
3. From a bring-your-own-device (BYOD) or noncompliant device that doesn't satisfy the policy, connect to the same desktop or launch the same RemoteApp.
4. Verify that the configured redirections are restricted or unavailable.
5. If you publish both desktops and RemoteApp applications, repeat these checks for both session types.

If the expected behavior doesn't occur, review:

- The Conditional Access policy assignment and authentication context.
- The device compliance status in Microsoft Entra ID and Intune.
- The Azure Virtual Desktop host pool RDP properties.
- Existing redirection policies that might override the configuration.

---

You can validate individual redirections by using the guidance in the following articles:

- **Clipboard:** Verify whether copy and paste work between the local device and remote session.
- **Drive and storage:**[Configure drive redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-drives-storage).
- **Printer:**[Configure printer redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-printers).
- **USB:**[Configure USB redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-usb).