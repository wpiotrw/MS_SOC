---
layout: Conceptual
title: Configure Global Secure Access Browser Settings (Preview) - Global Secure Access | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-global-secure-access-browser-settings
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: HULKsmashGithub
ms.author: alexpav
ms.service: global-secure-access
manager: dougeby
description: Configure Global Secure Access secure enterprise browser settings and traffic forwarding for native Microsoft Edge integration on Windows and macOS.
ms.topic: how-to
ms.date: 2026-11-13T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: 03cac259-3378-a881-f2b0-83b23c285169
document_version_independent_id: 03cac259-3378-a881-f2b0-83b23c285169
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/global-secure-access/how-to-configure-global-secure-access-browser-settings.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: global-secure-access/how-to-configure-global-secure-access-browser-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/global-secure-access/how-to-configure-global-secure-access-browser-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 5020c6b1-42e4-1962-67e9-8d9251c7d057
---

# Configure Global Secure Access Browser Settings (Preview) - Global Secure Access | Microsoft Learn

Configure secure enterprise browser with Microsoft Edge and Global Secure Access to give employees browser-only access to private web applications and protect browsing activity of users signed in to Microsoft Edge for Business using your organization's work account.

Enable the traffic types for secure enterprise browser using the Entra admin center, and then use the Microsoft 365 Admin center to configure an Edge Management Service (EMS) policy. This preview supports Windows and macOS.

## Prerequisites

- A tenant onboarded to Global Secure Access. See [Access Global Secure Access in the admin center](quickstart-access-admin-center).
- The **Global Secure Access Administrator** role to configure Global Secure Access.
- The **Application Administrator** role to assign users to traffic forwarding profiles and to configure Private Access enterprise applications and connector groups.
- Licenses for the Global Secure Access capabilities you plan to use. See [Global Secure Access licensing](overview-what-is-global-secure-access#licensing-overview).
- The [Edge Administrator](../identity/role-based-access-control/permissions-reference#edge-administrator) role, the least-privileged role to configure and assign the Edge policy in the M365 admin center.
- Configuration allowing for [M365 targeted releases](/en-us/microsoft-365/admin/manage/release-options-in-office-365) in your tenant. Alternatively, you can access the M365 admin center using the secure enterprise browser settings preview URL https://admin.cloud.microsoft/?flagOverrides=EnableEdgeGSA:true#/Edge/PolicyConfiguration/id/SecurityProtections .
- Microsoft Edge for Windows or macOS, version **157.0.4341.46** or newer.
- Work accounts in your tenant for the employees who use the feature. Business-to-business (B2B) guest accounts aren't supported because users can't sign in to Edge with those accounts.
- For Private Access, private web applications configured by fully qualified domain name (FQDN) and the associated private network connectors. See [Configure per-app access](how-to-configure-per-app-access).

Important

EMS is the only supported method to enable this integration in Edge for the preview. Intune app policies aren't supported for this configuration.

On Windows, the Global Secure Access client can run while Microsoft Edge is configured for Global Secure Access.

Important

On macOS, running the Global Secure Access client while Edge is configured for Global Secure Access isn't supported and results in certificate prompts. Keep the client disabled while using the Edge integration on macOS.

## Configure traffic forwarding in Global Secure Access

Global Secure Access calculates the user's traffic forwarding policy from traffic forwarding profiles, just as it does for the Global Secure Access client. Configure these profiles for your intended users before testing Edge.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a **Global Secure Access Administrator**.
2. Go to **Global Secure Access** &gt; **Connect** &gt; **Traffic forwarding**.
3. Configure the profiles for the traffic types you want to forward:

    - For internet and Microsoft 365 browsing, configure the [Internet traffic profile](how-to-manage-internet-access-profile) and the [Microsoft traffic profile](how-to-manage-microsoft-profile).
    - For private web applications, configure a [Private Access traffic forwarding profile](how-to-manage-private-access-profile) and the applications employees need.
4. [Assign the profiles to the intended users](how-to-manage-users-groups-assignment). Confirm that the users who receive the Edge policy are included in the applicable Global Secure Access profile assignments.

The Edge policy enables the browser integration. It doesn't define a separate set of traffic forwarding rules.

## Enable browser access in the Global Secure Access portal

Choose which traffic types Edge can forward to Global Secure Access. Internet Access and Microsoft 365 share a browser enablement control; Private Access is enabled separately.

1. In the Microsoft Entra admin center, go to **Global Secure Access** &gt; **Connect** &gt; **Explicit forward proxy**.
2. Turn on **Global Secure Access with Microsoft Edge**.
3. Under **Settings**, select the traffic types required for your deployment:

    - **Internet Access with Microsoft Edge**. Select this option for both internet and Microsoft 365 traffic. There isn't a separate Microsoft 365 browser enablement option.
    - **Private Access with Microsoft Edge**. Select this option for private web applications.

    [![Screenshot of Global Secure Access with Microsoft Edge enabled, with Internet Access and Private Access selected.](media/howto-secure-enterprise-browser/enable-browser-access.png)](media/howto-secure-enterprise-browser/enable-browser-access.png#lightbox)
4. Configure the Edge policy in the M365 admin center.

Enabling Internet Access for Edge also enables Microsoft 365 support in the browser configuration. Continue to manage the forwarding rules and user assignments for each traffic profile in Global Secure Access.

## Configure the Edge policy

Use the M365 admin center to enable the Edge integration for the users who need browser-based access. Global Secure Access portal enablement and the EMS policy are both required.

Follow [Configure Global Secure Access policy in Microsoft Edge secure enterprise browser settings](how-to-configure-global-secure-access-edge-policy) to create and assign the cloud policy, set **Enable secure network access (preview)** to **Enabled**, and save your changes.

Global Secure Access delivers Transport Layer Security (TLS) inspection certificate trust automatically to Edge. No separate manual certificate deployment to Edge is required for this integration. For Internet Access, configure the certificate and [TLS inspection policies](how-to-transport-layer-security) in Global Secure Access. Automatic trust delivery to Edge doesn't replace that service configuration or establish device-wide certificate trust.

## Validate browser access

Test from an employee account included in both the Edge policy assignment and the applicable Global Secure Access traffic forwarding profiles.

1. On a Windows or macOS device, open the supported version of Edge and sign in to a work profile with the employee's account.
2. Open `edge://policy` and confirm that the policy configured in EMS appears with the intended value.
3. Browse to destinations covered by your enabled profiles:

    - An internet destination covered by your Internet Access policy.
    - A Microsoft 365 destination covered by your Microsoft traffic profile, if enabled.
    - A private web application using its FQDN, if Private Access is enabled.
4. In the Microsoft Entra admin center, go to **Global Secure Access** &gt; **Monitor** &gt; **Traffic logs**.
5. Select **Transactions** and filter **Device Category** to **Secure enterprise browser**.
6. Review the corresponding transactions. Compare the traffic type, destination, and access decision with your configured policies.

The Microsoft Entra traffic profile isn't supported in this preview. Don't use compliant network checks or tenant restrictions v2 policies for Microsoft Entra ID to validate this integration. Private DNS is also unsupported.

If access fails or traffic doesn't match your policy, use [Troubleshoot secure enterprise browser](troubleshoot-secure-enterprise-browser) to check assignments, effective Edge policies, and traffic logs.