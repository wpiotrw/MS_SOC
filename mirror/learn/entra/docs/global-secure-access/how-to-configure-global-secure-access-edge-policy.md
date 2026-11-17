---
layout: Conceptual
title: Configure Global Secure Access Policy in Microsoft Edge (Preview) - Global Secure Access | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-global-secure-access-edge-policy
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: HULKsmashGithub
ms.author: alexpav
ms.service: global-secure-access
manager: dougeby
description: Configure the Global Secure Access policy in Microsoft Edge secure enterprise browser settings and assign it to employee work profiles on Windows and macOS.
ms.topic: how-to
ms.date: 2026-11-13T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: 465449ec-bbbe-8728-d7cb-ba925c554474
document_version_independent_id: 465449ec-bbbe-8728-d7cb-ba925c554474
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/global-secure-access/how-to-configure-global-secure-access-edge-policy.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: global-secure-access/how-to-configure-global-secure-access-edge-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/global-secure-access/how-to-configure-global-secure-access-edge-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: faded6d1-7d35-aa81-a239-7677390551d1
---

# Configure Global Secure Access Policy in Microsoft Edge (Preview) - Global Secure Access | Microsoft Learn

Configure a Microsoft Edge policy in Edge Management Experience (EMX) to enable secure enterprise browser for your employees. Create and assign a cloud policy to enable secure network access for Edge on Windows and macOS. Before you begin, configure Global Secure Access for browser access and confirm your Edge Administrator role assignment. For the full requirements, see Prerequisites.

The Edge policy enables the browser integration. Global Secure Access traffic forwarding profiles determine the traffic forwarding rules that apply to each user.

## Prerequisites

- Global Secure Access traffic forwarding and browser enablement configured for your deployment. Complete the [Global Secure Access configuration steps](how-to-configure-global-secure-access-browser-settings#configure-traffic-forwarding-in-global-secure-access) before configuring Edge.
- An account with an active [Edge Administrator](../identity/role-based-access-control/permissions-reference#edge-administrator) role, the least-privileged role for this task.
- Microsoft Edge for Windows or macOS, version **157.0.4341.46** or newer.
- Employee work accounts in your Global Secure Access tenant. Business-to-business (B2B) guest accounts aren't supported.

Important

On Windows, the Global Secure Access client can run while Edge is configured for Global Secure Access. On macOS, this coexistence isn't supported and results in certificate prompts. Keep the client disabled while using the Edge integration on macOS.

## Create and assign the Edge policy

Create a cloud policy and choose the employees who receive it. You configure the secure network access setting after creating the policy.

1. In the Microsoft 365 admin center, open the [Microsoft Edge policy creation page](https://admin.cloud.microsoft/#/Edge/PolicyConfiguration/id/CreateConfiguration). Sign in with your Edge Administrator account.
2. On **Basics**, enter a **Name** for the policy, such as *Global Secure Access Settings*, and a **Description**.
3. Under **Platforms**, select **Windows 10+**, **macOS 11+**, or both for your deployment. Set **Policy type** to **Cloud**.

    [![Screenshot of the policy Basics page with a name, description, Windows and macOS platforms, and Cloud policy type.](media/how-to-configure-edge-policy-global-secure-access/create-policy.png)](media/how-to-configure-edge-policy-global-secure-access/create-policy.png#lightbox)
4. Skip to **Assignments**. Select **Add all users** to apply the policy to all users in your tenant. Alternatively, use **Select group** to target a specific security group.

    [![Screenshot of the Assignments page showing the All users assignment and the controls for selecting a group or adding all users.](media/how-to-configure-edge-policy-global-secure-access/assign-policy.png)](media/how-to-configure-edge-policy-global-secure-access/assign-policy.png#lightbox)
5. On **Finish**, review the policy name, platforms, and assignments. Select **Review and create**.

    [![Screenshot of the Finish page showing the cloud policy configuration, user assignment, and Review and create button.](media/how-to-configure-edge-policy-global-secure-access/review-policy.png)](media/how-to-configure-edge-policy-global-secure-access/review-policy.png#lightbox)

## Enable secure network access

Open the policy you created to configure its security settings.

1. On **Configuration policies**, select your new policy.

    [![Screenshot of the Configuration policies list with the newly created Global Secure Access Settings cloud policy.](media/how-to-configure-edge-policy-global-secure-access/select-policy.png)](media/how-to-configure-edge-policy-global-secure-access/select-policy.png#lightbox)
2. Select **Customization Settings** &gt; **Security settings**.
3. Under **Secure Network Access**, set **Enable secure network access (preview)** to **Enabled**.

    [![Screenshot of Security settings with Enable secure network access set to Enabled and Save changes available.](media/how-to-configure-edge-policy-global-secure-access/enable-secure-network-access.png)](media/how-to-configure-edge-policy-global-secure-access/enable-secure-network-access.png#lightbox)
4. If your organization relies on universal tenant restrictions, you can also configure **Enable browser-based tenant restrictions**. Microsoft Entra traffic doesn't pass through the Global Secure Access network channel in Edge. Global Secure Access universal tenant restrictions aren't enforced for that traffic. The browser-based setting is separate from the Global Secure Access integration.
5. Select **Save changes**.

The configuration policy applies when assigned employees sign in to Edge with a work account from your organization.

## Validate the policy

Test with an employee account included in both the Edge policy assignment and the applicable Global Secure Access traffic forwarding profiles.

1. Open Edge on a supported Windows or macOS device and sign in to a work profile with the employee's account.
2. Open `edge://policy` and check the effective policy value and any reported errors.
3. Complete [Validate browser access](how-to-configure-global-secure-access-browser-settings#validate-browser-access) to test destinations and confirm the corresponding Global Secure Access transactions.