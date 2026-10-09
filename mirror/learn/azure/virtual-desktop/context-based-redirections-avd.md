---
layout: Conceptual
title: Context-based Redirections (Preview) - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/context-based-redirections-avd
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: suderek-msft
manager: eliotgra
ms.author: suderek
ms.service: azure-virtual-desktop
description: Context-based redirection is a capability that implements granular access policies for clipboard, drive, printer, and USB redirections based on authentication context.
ms.topic: feature-guide
ms.date: 2026-05-21T00:00:00.0000000Z
locale: en-us
document_id: 802570e4-1e45-f9c8-2226-189cc390f236
document_version_independent_id: 802570e4-1e45-f9c8-2226-189cc390f236
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/context-based-redirections-avd.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: context-based-redirections-avd
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/context-based-redirections-avd.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: f556e123-4e81-89d3-ed55-ed0f92f08625
---

# Context-based Redirections (Preview) - Azure Virtual Desktop | Microsoft Learn

Context-based redirection enables organizations to control redirection behavior based on user and session conditions. By using authentication context, admins can define when specific client capabilities should be allowed or restricted based on factors such as user role, device compliance, or network location. This helps ensure that sensitive data is only accessible when the session meets the required level of trust.

Setting up context-based redirection for Azure Virtual Desktop involves the following high-level steps:

Create a **Conditional Access (CA) policy** with an authentication context and assign it to a **user group**.

1. Configure any required **device compliance or configuration policies**, typically assigned to a **device group**.

Configure **Azure Virtual Desktop host pool RDP properties** to map the authentication context to specific redirections. These settings are applied at the **host pool level** and affect all session hosts within that pool.

Validate the behavior from the end-user perspective by connecting to a targeted Azure Virtual Desktop session and verifying the expected redirection behavior.

You can apply authentication context to control the following redirections:

- Clipboard
- Drive
- Printer
- USB

Note

Context-based redirections (Preview) will be supported in the Windows App on Windows, web browsers, Android, iOS/iPadOS, and macOS for full desktop sessions on Azure Virtual Desktop.

## Admin workflow to author Conditional Access policies

1. Sign in to the [Azure Portal](https://portal.azure.com/).
2. In the search bar, enter *Microsoft Entra Conditional Access.*
3. Navigate to **Manage** &gt; **Authentication contexts**.
4. Press **New authentication context**.
5. Enter the name, description of the new authentication context
6. Select the **Publish to apps** checkmark and then select a variable from the **ID** dropdown.
7. Press **Save**.
8. While in **Entra** **Conditional Access**, navigate to **Policies** on the sidebar.
9. Press **New Policy** and select the following configurations to create a new Conditional Access policy for managed, compliant devices:

    1. Input the name of this new Conditional Access policy.
    2. In **User or agents**, select **All users** under **Include**.
    3. In **Target resources**, click on the dropdown under **Select what this policy applies to** and select **Authentication context**.
    4. Under **Select the authentication contexts this policy** **will apply to**, click on the authentication context you want to use.
    5. In **Grant**, select **Grant access** and then check the **Require device to be marked as compliant** and press **Select**.
    6. Toggle the **Enable policy** to **On**.
    7. Press **Create**.

## Admin workflow to set auth context for Azure Virtual Desktop host pool RDP properties

For Azure Virtual Desktop, the context-based redirection settings can be set at the host pool level.

Here’s how to configure authentication context on an Azure Virtual Desktop host pool to dynamically control redirections based on user and session conditions:

1. Sign in to the [Azure Portal](https://portal.azure.com/).
2. In the search bar, enter *Azure Virtual Desktop* and select the matching service entry.
3. Select **Host pools**, then select the name of the host pool you want to configure.
4. Select **RDP Properties**, then select the **Device redirection** tab.
5. Head over to the targeted redirections, select in the dropdown options **Dynamically configure using authentication context**.
6. **Authentication context** selection will appear, click on the dropdown and select the authentication context you want to use.
7. Press **Save**.

## Validate context-based redirection behavior

To validate that context-based redirection is working as expected, test connections from devices with different trust levels and confirm the correct redirection behavior is applied.

1. Connect to the Azure Virtual Desktop host pool from a **managed, compliant device** that satisfies the Conditional Access policy requirements.

    - Verify that the configured redirections are available within the remote session.
2. Connect to the same Azure Virtual Desktop host pool from a bring-your-own-device (**BYOD**) **or noncompliant device** that doesn’t satisfy the Conditional Access policy requirements.

    - Verify that the configured redirections are restricted or unavailable within the remote session.
3. If the expected behavior doesn’t occur, review:

    - The Conditional Access policy assignment and authentication context configuration.
    - Device compliance status in Microsoft Entra ID/Intune.
    - The Azure Virtual Desktop host pool RDP property configuration.
    - Any existing redirection policies that may override the configured behavior.

You can validate individual redirections by following the testing guidance in each redirection’s respective Microsoft Learn documentation:

1. **Clipboard redirection:** Verify whether copy and paste work between the local device and remote session.
2. **Drive redirection:** Review [Configure fixed, removable, and network drive redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-drives-storage).
3. **Printer redirection:** Review [Configure printer redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-printers).
4. **USB redirection:** Review [Configure USB redirection on Windows over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-usb).