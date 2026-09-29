---
layout: Conceptual
title: What's new in Azure Virtual Desktop? - Azure - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/whats-new
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: hinallur
manager: eliotgra
ms.author: hinallur
ms.service: azure-virtual-desktop
description: Learn about new features and product updates for Azure Virtual Desktop.
ms.topic: release-notes
ms.custom: references_regions
ms.date: 2026-09-24T00:00:00.0000000Z
locale: en-us
document_id: 179e0581-18c2-c983-1490-bcdcb19c3d66
document_version_independent_id: 179e0581-18c2-c983-1490-bcdcb19c3d66
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/whats-new.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: whats-new
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/whats-new.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: 9093e3e1-d6a4-d879-b9aa-248c8195a044
---

# What's new in Azure Virtual Desktop? - Azure - Azure Virtual Desktop | Microsoft Learn

Important

Azure Virtual Desktop classic retires September 30, 2026. Connections to classic resources will be blocked after retirement.

To prevent disruption, [migrate](automatic-migration) remaining classic resources to Azure Resource Manager-based host pools before September 30, 2026.

Azure Virtual Desktop updates regularly. This article is where you find out about:

- The latest updates
- New features
- Improvements to existing features
- Bug fixes

Make sure to check back here often to keep up with new updates.

Tip

See [What's new in documentation](whats-new-documentation), where we highlight new and updated articles for Azure Virtual Desktop.

## September 2026

Here's what changed in September 2026:

### Managed identity support is now generally available

Managed identity support for Azure Virtual Desktop host pools is now generally available. You can use managed identities for session host configuration, autoscale, Start VM on Connect, and Azure Virtual Desktop for Azure local.

In a future service update, host pools configured with a session host configuration will **require a managed identity** in order to add session hosts to the host pool.

For more information, see [Configure managed identity in Azure Virtual Desktop](configure-managed-identity).

### Use TWAIN scanners in remote sessions (Public Preview)

TWAIN scanner redirection is now available in public preview for Azure Virtual Desktop. It enables supported scanners connected to a local Windows device to be redirected into a remote session using high-level redirection, providing an optimized scanning experience compared to USB redirection. For more information, see [Configure scanner redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-scanners).

### iOS preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on iOS. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the iOS device or that are connected to the iOS device (such as a physical security key or through QR code).

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

### iOS preview support for external identities

External identity support is in preview for the Windows App on iOS. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](authentication#external-identity).

### macOS support for external identities is now generally available

External identity support is now generally available for the Windows App on macOS. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](authentication#external-identity).

### RDP Multipath with UDP support for Windows App on macOS Beta

RDP Multipath with UDP transport paths is now available with **Windows App on macOS Beta, [version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test)** for Azure Virtual Desktop.

This expands the resiliency benefits of RDP Multipath to macOS users by enabling multiple UDP transport paths with RDP Shortpath for public networks. RDP Multipath continuously monitors available paths and can transition traffic to an alternate path when network conditions change, helping reduce session interruptions and improve connection reliability.

To get started, use **Windows App on macOS Beta, [version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test)** or later and ensure your environment meets the RDP Shortpath for public networks requirements.

### RDP Multipath in Azure Government

RDP Multipath with **redundant UDP transport paths is generally available in Azure Government**, helping improve connection resiliency by maintaining multiple network paths and automatically switching to an available path when needed.

The **phased GA rollout of redundant TCP transport paths has started**. Until the rollout is complete, customers can try redundant TCP by using the **validation ring**.

### RDP Shortpath with TURN relay in Azure Government

RDP Shortpath via TURN is now available in public preview in Azure Government, enabling relayed UDP connectivity when a direct connection isn't possible. This release introduces a new dedicated TURN relay IP range for Azure Government: 20.140.236.0/22 over UDP port 3478. Customers can try the capability by using the validation ring.

### Display Protection for Azure Virtual Desktop (Public Preview)

Display Protection for Azure Virtual Desktop is now available in public preview. Display Protection helps protect sensitive content displayed during remote sessions by securing the display path between the session host and supported endpoint devices. Administrators can configure the required level of display protection for their host pools in the Azure portal. For more information, see [Display Protection for Windows 365 and Azure Virtual Desktop](/en-us/windows-365/enterprise/windows-cloud-display-protection).

### New guidance on Windows update management methodologies for session hosts

New documentation is now available to help you choose the right servicing strategy for your Azure Virtual Desktop session hosts. It covers the supported methods for monthly security and quality updates, feature updates, and OS version upgrades across Windows client Enterprise, multi-session, and Windows Server — including which methods are recommended per operating system and how each maps to the patch in-place or image-based servicing model. For more information, see [Windows update management methodologies for session hosts](/en-us/azure/virtual-desktop/windows-update-management-methodologies-session-hosts).

### Azure Virtual Desktop Hybrid (Generally Available)

Azure Virtual Desktop Hybrid is now generally available. It extends Azure Virtual Desktop to existing on-premises infrastructure, enabling organizations to run session hosts on on-premises hypervisors or physical Windows Server devices. Azure Arc connects the session hosts to Azure, and the Azure Virtual Desktop Arc extension installs the required components and registers the device with a host pool. For more information, see [Azure Virtual Desktop Hybrid Overview](/en-us/azure/virtual-desktop/hybrid-overview).

### Pin RemoteApp shortcuts to local desktops (Public Preview)

Pinning RemoteApp shortcuts to local desktops is now available in public preview for Azure Virtual Desktop. Administrators can pin RemoteApp shortcuts to local desktops on behalf of users, and users can also pin RemoteApp shortcuts themselves. This provides faster access to frequently used remote applications directly from the local desktop. For more information, see [Publish applications with RemoteApp in Azure Virtual Desktop](/en-us/azure/virtual-desktop/publish-applications-stream-remoteapp?tabs=portal).

## August 2026

Here's what changed in August 2026:

### App Attach support for multiple user configuration files

Azure Virtual Desktop App Attach now supports App-V packages that use multiple user configuration files. This update helps close a feature gap with App-V Server and supports organizations migrating existing App-V applications to Azure Virtual Desktop with fewer package modifications. App Attach in Azure Virtual Desktop. For more information, see [App Attach in Azure Virtual Desktop](/en-us/azure/virtual-desktop/app-attach-overview).

### macOS preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on macOS. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the macOS device or that are connected to the macOS device (such as a physical security key or through QR code).

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

### Modern Auto-Reconnect begins rollout in Azure Virtual Desktop

Modern Auto-Reconnect enhances connection resiliency during temporary network interruptions by preserving the current connection state and restoring connectivity more quickly when a network path becomes available. Powered by RDP Multipath, the feature reduces user-visible interruptions and improves recovery during network transitions and brief connectivity losses.

Modern Auto-Reconnect is being introduced through a quality-driven, phased rollout, ensuring a smooth and reliable experience as availability expands across Azure Virtual Desktop deployments.

For more information, click [here](/en-us/azure/virtual-desktop/fast-reconnect)

### Screen Capture Protection for web connections is now available

Screen Capture Protection is now available when accessing Azure Virtual Desktop session hosts from supported web browsers. This capability helps protect sensitive information by preventing screen content from being captured during remote sessions, enhancing security across more connection experiences. For more information, see [Enable screen capture protection in Windows 365](/en-us/azure/virtual-desktop/screen-capture-protection?tabs=intune).

### RAW printing support for Azure Virtual Desktop (Public Preview)

RAW printing support is now available in Public Preview for Azure Virtual Desktop. Administrators can configure printer redirection to use RAW print jobs instead of XPS, helping support devices such as label printers that require RAW printing. This capability reduces the need to install printer drivers on session hosts and simplifies management of specialized printing scenarios. For more information, see [Configure printer redirection](/en-us/azure/virtual-desktop/redirection-configure-printers?tabs=intune&amp;pivots=azure-virtual-desktop).

### Modern Auto-Reconnect (Public Preview)

Modern Auto-Reconnect introduces an enhanced session recovery experience for Azure Virtual Desktop that preserves session state during temporary network interruptions and automatically restores connectivity when network conditions improve. Powered by RDP Multipath, it delivers faster recovery, fewer user-visible disruptions, and a more seamless user experience compared to the traditional reconnect model. For more information, click [here](/en-us/azure/virtual-desktop/fast-reconnect).

## July 2026

Here's what changed in July 2026:

### Remote assistance for RemoteApp sessions with Intune Remote Help

Intune Remote Help now supports remote assistance within Azure Virtual Desktop RemoteApp sessions. During a session, a helper can see and control the published apps that the user is running, but not the rest of their desktop. Remote Help is also now included at no additional cost with Microsoft 365 E3 and E5. For more information, see [Provide help in Azure Virtual Desktop desktop and RemoteApp sessions](/en-us/intune/remote-help/start-session?tabs=windows%2Cwindowsnative#provide-help-in-azure-virtual-desktop-desktop-and-remoteapp-sessions).

### Android support for external identities is now generally available

External identity support is now generally available for the Windows App on Android. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](authentication#external-identity).

### Android preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on Android. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the Android device through a (software-based) passkey provider like Microsoft Authenticator. Using passkeys from other devices (such as a physical security key or through QR code) is not supported.

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

### RDP Multipath with redundant TCP transport paths is now generally available

RDP Multipath with redundant TCP transport paths is now generally available for Azure Virtual Desktop. This enhancement extends the resiliency benefits of RDP Multipath to TCP-based connections, enabling Azure Virtual Desktop to maintain multiple standby TCP transport paths and automatically switch between them when network degradation is detected.

Key benefits include:

- Improved session resiliency across restrictive network environments
- Automatic failover between available transport paths
- Reduced session interruptions and disconnects
- No additional configuration required when prerequisites are met

For more information, see *[Use RDP Multipath to improve Azure Virtual Desktop connections](/en-us/azure/virtual-desktop/rdp-multipath)*.

## June 2026

Here's what changed in June 2026:

### Automated Host Pools

Automated host pools are now available, providing a new way to maintain a homogeneous pool of session hosts. By setting a single Session Host Configuration (SHC), administrators can automatically enforce configuration settings across all session hosts in the pool. Updates can be made by modifying the configuration instead of manually updating each session host. To learn more, see [Session Host Configuration](/en-us/azure/virtual-desktop/host-pool-management-approaches) and [Session host update](/en-us/azure/virtual-desktop/session-host-update) for Azure Virtual Desktop.

### Dynamic Autoscaling

Dynamic autoscaling is now available for pooled host pools with session host configuration. Administrators can optimize deployment costs by creating schedules that dynamically create and delete session host virtual machines based on usage patterns. To learn more, see [Create and assign an autoscale scaling plan for Azure Virtual Desktop](/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan?tabs=portal%2Cintune&amp;pivots=dynamic).

### Ephemeral OS Disks

Ephemeral OS disks are now available and optimized for stateless workloads. They enable nonpersistent virtual machines with lower-latency read and write operations, along with fast reset and reimage capabilities that return VMs and scale set instances to their original boot state. To learn more, see [Ephemeral OS disks on Azure Virtual Desktop](/en-us/azure/virtual-desktop/deploy/session-hosts/ephemeral-os-disks?tabs=portal).

### Added external identity support for Domainless federation

With the general availability of Domainless SAML IdP federation in Entra ID, you can provide desktops and RemoteApps to an external identity whose email domain differs from the domain configured on the SAML IdP. These users must redeem their invitation to the organization prior to signing into the Windows App.

For more information, see [External identity](authentication#external-identity) and [Domainless SAML IdP federation](/en-us/entra/external-id/direct-federation#domainless-saml-idp-federation).

### Context-based redirections (Public Preview)

Context-based redirections are now available in public preview for Azure Virtual Desktop. This server-side capability enables admins to dynamically control clipboard, printer, drives, and low-level USB redirection behavior based on user identity, device compliance, and network conditions. By enforcing policies dynamically for bring-your-own-device (BYOD) scenarios, organizations can better protect sensitive data without relying on client-side controls. For more information, see [Context-based redirections in Azure Virtual Desktop](/en-us/azure/virtual-desktop/context-based-redirections-avd).

## May 2026

Here's what changed in May 2026:

### FSLogix support for cloud-only and external identities is now generally available

You can now provide FSLogix profile containers for both cloud-only and external identities. With this functionality, you can provide the same user experience on a pooled host pool that you already can for hybrid users.

This capability is already built-in to existing versions of FSLogix.

For more information, see [Use Azure Files and Microsoft Entra ID for cloud-only and external identities](/en-us/fslogix/how-to-configure-profile-container-azure-ad?context=/azure/virtual-desktop/context/context&amp;pivots=cloud-only-or-external-identities).

### AVD for hybrid environments with Arc-Enabled Servers (Public Preview)

You can now deploy Azure Virtual Desktop session hosts on any hypervisor or bare-metal Windows Server using the Azure Arc extension. This update expands hybrid deployment options, allowing admins to add Arc-Enabled Servers to AVD host pools and manage them alongside Azure-based resources. VM provisioning and power management are not included in this release. For more information, see the [AVD hybrid overview](/en-us/azure/virtual-desktop/hybrid-overview).

### RDP Multipath with redundant TCP transport paths begins GA rollout

Azure Virtual Desktop has started the **general availability (GA) rollout of RDP Multipath with redundant TCP transport paths**. This enhancement improves session resiliency by enabling Azure Virtual Desktop to maintain multiple TCP transport paths and automatically switch between them when network degradation is detected.

The feature is being enabled through a **phased, quality‑driven rollout** to ensure a stable and reliable experience. Until the rollout reaches full availability, redundant TCP may not be consistently enabled across all host pools.

For more information, see *[Use RDP Multipath to improve Azure Virtual Desktop connections](/en-us/azure/virtual-desktop/rdp-multipath)*.

## April 2026

Here's what changed in April 2026:

### App Attach support for Windows Server 2025 and 2022 in Azure Virtual Desktop is now available

Azure Virtual Desktop now officially supports App Attach on Windows Server 2025 and 2022. App Attach enables applications to be packaged and mounted on demand, reducing image bloat and improving manageability for organizations running Windows Server-based session hosts. This update brings greater flexibility and performance benefits, aligns with the end of life for App-V in April, and extends support to a broader range of Azure Virtual Desktop deployment scenarios, including Hybrid environments.

### Enhanced session resilience with RDP Multipath (Public Preview)

Azure Virtual Desktop introduces RDP Multipath in public preview, adding redundant TCP paths to its connection transport. This enhancement improves session resilience by intelligently managing multiple network routes, ensuring users can maintain access even when their primary connection is disrupted. The update aims to reduce session interruptions and improve reliability for Azure Virtual Desktop users. For more information, see [RDP Multipath for Azure Virtual Desktop](/en-us/azure/virtual-desktop/rdp-multipath).

### Additional client support for external identities in Microsoft Azure for US Government

External identity support for Azure Virtual Desktop deployments in Microsoft Azure for US Government is now available on the Windows App for Windows. This requires that the user configure a registry key on the device running the Windows App. For more information on the registry key, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

### Additional client support for external identities

External identity support is now in preview for the Windows App on macOS and Android. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](authentication#external-identity).

## March 2026

Here's what changed in March 2026:

### New Microsoft Teams media optimization architecture expands to additional platforms

New Microsoft Teams media optimization on macOS is now available in Preview for Azure Virtual Desktop. Additionally, WebRTC-based Teams is now Generally Available for Azure Virtual Desktop. Azure Virtual Desktop now supports the new Teams media optimization architecture (SlimCore) on macOS when using New Teams and connecting through the Windows App.

## February 2026

Here's what changed in February 2026:

### RDP Shortpath (UDP) over Private Link is now generally available

Azure Virtual Desktop now supports RDP Shortpath using UDP over Azure Private Link with explicit opt‑in, enabling high‑performance connections on private network paths while non‑opted connections continue using WebSocket (TCP). For more information, see [Azure Private Link with Azure Virtual Desktop](/en-us/azure/virtual-desktop/private-link-overview).

## January 2026

Here's what changed in January 2026:

### Centralized RDP Shortpath management is now generally available

IT admins can now configure all RDP Shortpath transport modes—Managed, Public/STUN, and Public/TURN—directly through Microsoft Intune or Group Policy. These configurations use registry‑backed policies for consistent and scalable management across session hosts.

For Azure Virtual Desktop, these GPO/Intune settings apply in addition to host pool Shortpath settings, providing an extra layer of control at the session‑host level.

## December 2025

There were no changes to Azure Virtual Desktop in December 2025.

## November 2025

Here's what changed in November 2025:

### Azure Virtual Desktop support for external identities is now generally available

You can now provide Azure Virtual Desktop resources for an external identity. There is no change to the administrative flow to assign the resources, as you still assign the user to the app group.

FSLogix profile container user for external identities is in preview.

For more information, see [External identity](authentication#external-identity), how to [Provide access to external identities](provide-access-external-identities), and appropriate [Azure Virtual Desktop licensing guidance](licensing).

### FSLogix support for cloud-only and external identities is now in preview

You can now provide FSLogix profile containers for both cloud-only and external identities, which is in preview. With this functionality, you can provide the same user experience on a pooled host pool that you already can for hybrid users.

This capability is already built-in to existing versions of FSLogix.

For more information, see [Use Azure Files and Microsoft Entra ID for cloud-only and external identities](/en-us/fslogix/how-to-configure-profile-container-azure-ad?context=/azure/virtual-desktop/context/context).

### Enhancements to RemoteApps (preview)

Enhanced user experiences for RemoteApps are rolling out to public preview. Enhancements include improved support for Windows Snap and full-screen mode, better DPI handling, and refined visuals like borders, shadows, and theme integration in Windows OS. To learn how to enable these improvements during preview, see [RemoteApp enhancements (preview)](remoteapp-enhancements).

### Windows Cloud Keyboard Input Protection (preview)

Windows Cloud Keyboard Input Protection is now in preview - purpose-built to address endpoint security concerns for Windows 365 and Azure Virtual Desktop. This feature encrypts keystrokes at the kernel level, protecting against keylogger malware and other endpoint threats. It marks a major step forward in helping customers secure sensitive input data and strengthen endpoint security in cloud-based workspaces, see [Windows Cloud Input Protection](/en-us/windows-365/enterprise/windows-cloud-input-protection).

### RDP Multipath is now fully rolled out!

We’ve completed the phased deployment of RDP Multipath across all eligible connections. This feature enhances reliability and performance by leveraging multiple network paths for your remote sessions, ensuring a more resilient and seamless experience.

## October 2025

Here's what changed in October 2025:

### Ephemeral OS Disk Support Now in Public Preview

Ephemeral OS disk support is now available in public preview for Azure Virtual Desktop. Designed for stateless workloads, ephemeral OS disks store the operating system on the virtual machine’s local storage rather than remote storage. This enables a faster session host creation experience and improved performance, while maintaining a consistent and responsive user experience.

Key benefits:

- **Faster provisioning and reimaging:** Session hosts can be created or reset quickly.
- **Improved performance:** Local read/write operations deliver faster access times and reduced latency.
- **Optimized for stateless workloads:** Ideal for environments that do not need to retain session host state information between uses.

Learn more about configuring [Ephemeral OS disk on Azure Virtual Desktop](/en-us/azure/virtual-desktop/deploy/session-hosts/ephemeral-os-disks?tabs=portal).

## September 2025

Here's what changed in September 2025:

### Azure Virtual Desktop support for external identities, without FSLogix (preview)

You can now provide Azure Virtual Desktop resources for an external identity. There is no change to the administrative flow to assign the resources, as you still assign the user to the app group.

The current preview support of external identities doesn't support the use of FSLogix.

For more information, see [External identity (preview)](authentication#external-identity), along with appropriate [Azure Virtual Desktop licensing guidance](licensing).

### Managed identity support for all host pools using session host configuration and cross-subscription image support

We expanded support for adding a managed identity to all Azure Virtual Desktop host pools and made it accessible from the [Azure production portal](https://portal.azure.com). Creating a new host pool with a session host configuration in Azure portal with require assigning a managed identity. This removes the need to assign permissions to the Azure Virtual Desktop service principal when using a session host configuration with your host pool. In addition, this also provides:

- Granular per-host pool control of permissions required to create and update session hosts
- Permissions auto assigned based on session host configuration parameters
- Support for key vaults with public access disabled that allow access from trusted Microsoft services
- Support for accessing images hosted in another Azure subscription within the same tenant

In upcoming service updates, you will need to use a managed identity to use the session host configuration feature, with an estimated progression of:

- Starting **September 19, 2025**, new host pools that use a session host configuration in Azure portal must be created using a managed identity.
- Starting **October 15, 2025**, existing host pools with a session host configuration will no longer be able to update their session host configuration until a managed identity is added.
- Starting **November 15, 2025**, existing host pools with a session host configuration will no longer be able to create session hosts until a managed identity is added.

Learn more about [using managed identities with Azure Virtual Desktop host pools](configure-managed-identity) and [deploying a host pool using session host configuration](deploy-azure-virtual-desktop?pivots=host-pool-session-host-configuration).

### Global expansion of TURN Relay

Microsoft has expanded the TURN relay infrastructure globally, deploying it across 39 Azure regions with a dedicated IP range of 51.5.0.0/16 for Azure Virtual Desktop and Windows 365. This transition from the previously shared 20.202.0.0/16 subnet enhances RDP Shortpath for Public Networks, offering improved performance, reliability, and user experience.

## August 2025

Here's what changed in August 2025:

### Token protection support in Windows App on Windows devices is now generally available

You can now use a Conditional Access policy to require token protection for sign-in tokens (refresh tokens) on Windows devices. Such policies can reduce attacks using token theft by ensuring a token is usable only from the intended device. For more information, see [Microsoft Entra Conditional Access token protection explained](/en-us/entra/identity/conditional-access/concept-token-protection).

### Managed identity support for validation host pools using session host configuration

We have added support to add a managed identity to Azure Virtual Desktop host pools when using the [Azure preview portal](https://preview.portal.azure.com). At this time only host pools that are [configured as a validation environment](configure-validation-environment) are supported. Assigning a managed identity to an Azure Virtual Desktop host pool removes the need to assign permissions to the Azure Virtual Desktop service principal when using a session host configuration with your host pool. In addition, this also provides:

- Granular per-host pool control of permissions required to create and update session hosts
- Permissions auto assigned based on session host configuration parameters
- Support for key vaults with public access disabled that allow access from trusted Microsoft services

In upcoming service updates, you will need to use a managed identity to use the session host configuration feature, with an estimated progression of:

- Starting **September 18th, 2025** (previously September 1, 2025), new host pools that use a session host configuration in Azure portal must be created using a managed identity.
- Starting **October 15th, 2025** (previously October 1, 2025), existing host pools with a session host configuration will no longer be able to update their session host configuration until a managed identity is added.
- Starting **November 15th, 2025** (previously November 1, 2025), existing host pools with a session host configuration will no longer be able to create session hosts until a managed identity is added.

Learn more about [using managed identities with Azure Virtual Desktop host pools](service-principal-assign-roles), [deploying a host pool using session host configuration](deploy-azure-virtual-desktop?pivots=host-pool-session-host-configuration), and [configuring a managed identity](configure-managed-identity).

## July 2025

Here's what changed in July 2025:

### Select redirections disabled for new host pools

Azure Virtual Desktop is enhancing its default security by disabling clipboard, drive, opaque low-level USB, and printer redirections for all newly created host pools. This change minimizes the risk of data exfiltration and malware injections, making it easier to have a more secure experience by default. IT admins can enable these redirections as needed using the host pool Remote Desktop Protocol (RDP) properties in the Microsoft Azure portal or by using other methods such as Microsoft Intune or Group Policy.

For more information, see [Peripheral and resource direction overview](redirection-remote-desktop-protocol).

### RDP Multipath is now generally available

Remote Desktop Protocol (RDP) Multipath is now generally available for Azure Virtual Desktop and Windows 365. This feature improves connection reliability and performance by intelligently managing multiple network paths between the client and the session host or Cloud PC. Multipath dynamically selects the best available path and provides seamless failover, delivering a smoother user experience even in environments with variable network conditions. We’re rolling out this feature in phases, so an increasing percentage of connections will benefit from RDP Multipath as deployment continues.

For more information, see [RDP Multipath](rdp-multipath).

## June 2025

Here's what changed in June 2025:

### High Efficiency Video Coding (HEVC/H.265) hardware acceleration support is now generally available

Azure Virtual Desktop graphics processing unit (GPU) acceleration support for frame encoding using HEVC/H.265 is now generally available. GPU acceleration improves graphical experiences when using the Remote Desktop Protocol (RDP) with a compatible GPU-enabled Azure Virtual Machine.

For more information, see [Enable GPU acceleration for Azure Virtual Desktop](graphics-enable-gpu-acceleration).

### Session host creation using a session host configuration

We extended the session host creation functionality from session host update and dynamic autoscaling to apply to all session hosts created in a host pool with a session host configuration. We also added support for Microsoft Entra-joined devices. This update brings the following changes:

- You can configure a host pool to use Microsoft Entra-join without needing to assign the **Virtual Machine User** RBAC role to a user.
- Error reporting is consistent across services and auto-retry functionality is added to session host creation to mitigate transient errors.
- Log analytics for a host pool now includes session host creation activity, providing a consolidated view of session host management. Resource group deployments no longer contain per-session host creation details.
- The host pool user interface, including banners, provides session host creation status on the session host menu item, though you should also enable log analytics on a host pool to see a detailed diagnostic history.
- You can now increase the host pool size via API or custom ARM templates, which triggers the Azure Virtual Desktop service to create new session hosts.

For more information, see [Create a host pool with a session host configuration](deploy-azure-virtual-desktop?pivots=host-pool-session-host-configuration) and [Add session hosts to a host pool](add-session-hosts-host-pool?pivots=host-pool-session-host-configuration).

### Microsoft Teams media optimization for iOS/iPadOS is in preview

You can now use Microsoft Teams media optimization when connecting to Azure Virtual Desktop from iOS/iPadOS, which is now available in preview. Teams Media optimization redirects calling and meeting functionality to the local device when using Windows App. For more information, see [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd) and [Supported features for Microsoft Teams on Azure Virtual Desktop](teams-supported-features).

## May 2025

Here's what changed in May 2025:

### Connect directly to Azure Virtual Desktop with a direct launch URL

You can now connect directly to Azure Virtual Desktop using a direct launch URL. The direct launch URL opens Windows App in a web browser and connects directly to a specific resource, such as a desktop or application, without requiring the user to select it from a list. This feature is useful for scenarios where you want to provide a direct link to a specific resource.

For more information, see [Access desktops and apps using direct launch URLs for Windows App in a web browser](/en-us/windows-app/direct-launch-urls?tabs=avd).

### Multiple personal desktops for a single user is now generally available

Multiple personal desktop assignment allows you to assign more than one personal desktop to a single user in a single host pool, and is now generally available. Multiple desktops are useful for users juggling diverse business roles, such as backend and frontend development or transitioning between testing and production environments.

For more information, see [Assign multiple personal desktops to a single user](configure-host-pool-personal-desktop-assignment-type#assign-multiple-personal-desktops-to-a-single-user).

## April 2025

Here's what changed in April 2025:

### Control Windows App in a web browser using Microsoft Edge on personal Windows devices

Use Microsoft Intune mobile application management (MAM) to enable protected access an Azure Virtual Desktop session when using Windows App in a web browser using Microsoft Edge on personal Windows devices. You can check the security posture of a local device before granting access, and secure organization data by disabling drive, clipboard, and printer redirection.

For more information, see [Require local client device security compliance with Microsoft Intune and Microsoft Entra Conditional Access](/en-us/windows-app/require-device-security-compliance-intune?tabs=web).

### Windows App on Android is now generally available

Windows App on Android is now generally available, with an enhanced user experience, increased reliability, and features such as Microsoft Intune mobile application management and Passkey authentication. Windows App replaces the Remote Desktop client on Android. Installations of the Remote Desktop client on Android change to Windows App next time the app is updated.

For more information, see [Windows App](https://aka.ms/WindowsApp).

### Every time sign-in frequency Conditional Access option is now generally available

Using Microsoft Entra sign-in frequency with Azure Virtual Desktop prompts users to reauthenticate when launching a new connection after a period of time, and is now generally available You can now require reauthentication after a shorter period of time.

For more information, see [Configure sign-in frequency](set-up-mfa?tabs=avd#configure-sign-in-frequency).

### Using Microsoft Entra Conditional Access token protection with Windows App on Windows devices to connect to Azure Virtual Desktop is now in preview

You can now use Microsoft Entra Conditional Access token protection with Windows App on Windows devices to connect to Azure Virtual Desktop, which is now in preview. Token protection helps reduce token theft attacks by ensuring a token is usable only from the intended device.

For more information, see [Microsoft Entra Conditional Access: token protection](/en-us/entra/identity/conditional-access/concept-token-protection).

## March 2025

Here's what changed in March 2025:

### Quickstart for Azure Virtual Desktop is now generally available

Quickstart enables you to easily evaluate a Windows 11 Enterprise multi-session remotely and become familiar with the service before deploying it in production.

When you use QuickStart, it deploys a sample Azure Virtual Desktop environment consisting of minimal resources and configuration. A user then signs into Windows App and connects to a full virtual desktop session. Deployment takes approximately 20 minutes to complete.

For more information, see [Quickstart: deploy a sample Azure Virtual Desktop environment](quickstart).

### Improved drive redirection performance

When a user opens or lists the contents of a redirected drive, the remote session enumerates files and folders of the current directory. If you have a large number of files and folders on the redirected drives, the enumeration process can take a long time and impact the performance of the remote session. For session hosts running Windows 11 24H2, we improved the performance of enumerating files and folders on redirected drives is greatly improved. To get the improved performance, you need to configure your session hosts.

For more information, see [Improve performance of enumerating files and folders on redirected drives](redirection-configure-drives-storage?pivots=azure-virtual-desktop).

### Assign multiple personal desktops to a single user (preview)

Multiple personal desktop assignment allows you to assign more than one personal desktop to a single user in a single host pool. Multiple desktops are useful for users juggling diverse business roles, such as backend and frontend development or transitioning between testing and production environments.

For more information, see [Assign multiple personal desktops to a single user](configure-host-pool-personal-desktop-assignment-type#assign-multiple-personal-desktops-to-a-single-user).

### Added Asia-Pacific as a data location

We now support storing customer input data and service-generated data in the Asia-Pacific geography. For more information, see [Data locations for Azure Virtual Desktop](data-locations).

### MSIX App Attach deprecation

MSIX App Attach will be deprecated on June 1, 2025. Make sure to move all apps to App Attach by this date. For more information, see [App Attach and MSIX App Attach in Azure Virtual Desktop](app-attach-overview).

## February 2025

Here's what changed in February 2025:

### Using Azure Private Link with RDP Shortpath for managed networks is now in preview

Private Link provides private connectivity to your remote resources over a private endpoint. You can now use Azure Private Link with RDP Shortpath for managed networks, which is now available in preview. All other RDP Shortpath options using STUN or TURN aren't currently supported with Private Link.

For more information, see [Azure Private Link with Azure Virtual Desktop](private-link-overview).

### Updated browser requirements to connect to Azure Virtual Desktop using Windows App in a web browser or the Remote Desktop web client

Starting June 15, 2025, using Windows App in a web browser or the Remote Desktop web client will have updated browser requirements. Ensure your browser is updated and meets the requirements listed at [Get started with Windows App to connect to devices and apps](/en-us/windows-app/get-started-connect-devices-desktops-apps?pivots=azure-virtual-desktop&amp;tabs=web-avd#prerequisites) or [Get started with the Remote Desktop client](/en-us/previous-versions/remote-desktop-client/connect-windows-cloud-services?tabs=windows-msrdc-msi) by this date.

### Support for FIDO devices and passkeys on connecting to Azure Virtual Desktop from an Android device is now in preview

Windows App and the Remote Desktop app for Android now support FIDO devices and passkeys for Microsoft Entra ID sign-in. For more information, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#cloud-service-authentication).

### Expanded cloud support for Microsoft Intune management of devices connecting to Azure Virtual Desktop

The current capabilities of managing devices connecting to Azure Virtual Desktop using Microsoft Intune have been expanded to include Intune for US Government GCC, [Intune for US Government GCC High and DoD](/en-us/intune/intune/fundamentals/intune-govt-service-description), and [Intune operated by 21Vianet](/en-us/mem/intune/fundamentals/china) (China).

For more information, see [Require local client device security compliance with Microsoft Intune and Microsoft Entra Conditional Access](/en-us/windows-app/require-device-security-compliance-intune?context=/azure/virtual-desktop/context/context).

## January 2025

Here's what changed in January 2025:

### Quickstart for Azure Virtual Desktop is now in preview

Quickstart enables you to easily evaluate a Windows 11 Enterprise multi-session remotely and become familiar with the service before deploying it in production.

When you use QuickStart, it deploys a sample Azure Virtual Desktop environment consisting of minimal resources and configuration. A user then signs into Windows App and connects to a full virtual desktop session. Deployment takes approximately 20 minutes to complete.

For more information, see [Quickstart: deploy a sample Azure Virtual Desktop environment](quickstart).

### iOS and iPadOS now support screen capture protection via Microsoft Intune Mobile Application Management (MAM)

Screen capture protection helps prevent sensitive information from being captured on client devices. When you enable screen capture protection, remote content is automatically blocked in screenshots and screen sharing. You can now use Intune MAM policies to configure screen capture protection on iOS and iPadOS.

For more information, see [Screen capture protection in Azure Virtual Desktop](screen-capture-protection).

### Microsoft Intune Mobile Application Management (MAM) support on Windows App on Android (preview) for devices running Android 15

Intune MAM policies can now be applied to Windows App on Android (preview) when the device is running on Android 15. Previously, Windows App could run on Android 15, but MAM policies wouldn’t take effect. 

For more information, see [Require local client device security compliance with Microsoft Intune and Microsoft Entra Conditional Access](/en-us/windows-app/require-device-security-compliance-intune?context=/azure/virtual-desktop/context/context).

## December 2024

There were no changes to Azure Virtual Desktop in December 2024.

## November 2024

Here's what changed in November 2024:

### Session host configuration and update for Azure Virtual Desktop is now in preview

Session host configuration enables you to define the underlying virtual machine disk type, operating system image, and other properties of all session hosts in a newly created pooled host pool. Session host update allows you to modify your session host configuration and roll out the changes to existing hosts in batches, minimizing downtime. This deletes the existing virtual machines and creates new ones that are added to your host pool with the updated configuration.

For more information, see [Session host update for Azure Virtual Desktop](session-host-update).

### Dynamic autoscaling for Azure Virtual Desktop is now in preview

Dynamic autoscaling is now in preview for Azure Virtual Desktop. This new scaling method can adjust the available capacity in the host pool by creating, deleting, and/or turning on/off session hosts. Dynamic autoscaling can only be used for pooled host pools with session host configuration. For more information about autoscale scaling plans, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios).

For more information, see [Create and assign an autoscale scaling plan for Azure Virtual Desktop](autoscale-create-assign-scaling-plan).

### Deploy App-V apps in Azure Virtual Desktop via integrated experience is now available in preview

Microsoft Application Virtualization (App-V) for Windows delivers Win32 applications to users as virtual applications. Virtual applications are installed on centrally managed servers and delivered to users as a service in real time and on an as-needed basis. Users launch virtual applications from familiar access points and interact with them as if they were installed locally.

For more information, see [App Attach and MSIX App Attach in Azure Virtual Desktop](app-attach-overview).

### Applications can be delivered from partner solutions with App Attach is now available

Several partners provide application delivery solutions to Azure Virtual Desktop via integration with App Attach.

For more information, and a list of supported solutions, see [Deliver applications from partner solutions to Azure Virtual Desktop with App Attach](app-attach-partner-solutions).

### Azure Virtual Desktop on Azure Extended Zones is now available

Azure Extended Zones are small-footprint extensions of Azure placed in metros, industry centers, or a specific jurisdiction to serve low latency and/or data residency workloads. Azure Extended Zones is supported for Azure Virtual Desktop and can run latency-sensitive and throughput-intensive applications close to end users and within approved data residency boundaries.

For more information, see [Azure Virtual Desktop on Azure Extended Zones](azure-extended-zones).

### Azure Virtual Desktop for Azure Stack HCI is now Azure Virtual Desktop for Azure Local

All current features and existing pricing for AVD for Azure Stack HCI are now supported in select versions of AVD for Azure Local.

For more information, see [Azure Virtual Desktop on Azure Local](/en-us/azure/virtual-desktop/azure-local-overview).

### Windows Server 2025 is now supported in Azure Virtual Desktop

Windows Server 2025 is now supported in Azure Virtual Desktop to be deployed as a session hosts to provide desktops and applications.

For more information, see [Prerequisites for Azure Virtual Desktop](prerequisites).

### Support for FIDO devices and passkeys on macOS and iOS is now available

Windows App and the Remote Desktop app now support FIDO devices and passkeys for Microsoft Entra ID sign in on macOS and iOS.

For more information see [Azure Virtual Desktop identities and authentication](authentication).

## October 2024

Here's what changed in October 2024:

### YubiKey smart card redirection on iOS and iPadOS is now in preview

Yubico and Microsoft have partnered to provide smart card redirection for iOS and iPadOS Windows App users, which is available in preview starting in version 11.0.4. The Yubico integration supports the latest [YubiKey 5 portfolio](https://www.yubico.com/products/yubikey-5-overview/).

For YubiKey support, contact [Yubico Support Services](https://www.yubico.com/support/support-services/).

### AVC Mixed mode support for Azure Virtual Desktop and Windows 365 session desktop when multimedia redirection is not enabled

AVC Mixed Mode is now available in the default graphics profile. When multimedia redirection isn't enabled, AVC/h.264 is used to encode detected image content instead of the RemoteFX image encoder. This improves performance when encoding images relative to bitrate and framerate in network-constrained scenarios.

For more information, see [Graphics encoding over the Remote Desktop Protocol](graphics-encoding).

### New Teams SlimCore changes are now available

Microsoft Teams on Azure Virtual Desktop supports chat and collaboration. With media optimizations, it also supports calling and meeting functionality by redirecting it to the local device when using Windows App or the Remote Desktop client on a supported platform.

There are two versions of Teams, classic Teams and [new Teams](/en-us/microsoftteams/new-teams-desktop-admin), and you can use either with Azure Virtual Desktop. New Teams has feature parity with classic Teams, and improves performance, reliability, and security.

New Teams can use either SlimCore or the WebRTC Redirector Service. SlimCore is now available. If you use SlimCore, you should also install the WebRTC Redirector Service. This allows a user to fall back to WebRTC, such as if they roam between different devices that don't support the new optimization architecture. For more information about SlimCore and how to opt into the preview, see [New VDI solution for Teams](/en-us/microsoftteams/vdi-2).

For more information, see [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd).

### Multimedia redirection for video playback and calls in a remote session

Multimedia redirection call redirection is now generally available. Multimedia redirection redirects video playback and calls in a remote session from Azure Virtual Desktop, a Windows 365 Cloud PC, or Microsoft Dev Box to your local device for faster processing and rendering. 

For more information, see [Multimedia redirection for video playback and calls in a remote session](multimedia-redirection-video-playback-calls?tabs=intune&amp;pivots=azure-virtual-desktop).

### Standardized naming of selectable images in Azure Virtual Desktop is now available

Image naming is now consistent when selecting images from the dropdown menu. As all new images published are Gen2, we're dropping this post-fix from the display name in the Azure Virtual Desktop dropdowns and will only add Gen1 when it is required. The change doesn’t impact naming in the Azure Marketplace.

### Windows 11, version 24H2 images are now available in the Azure Marketplace

Windows 11 Enterprise and Windows 11 Enterprise multi-session are now available in the Azure Marketplace. The updated images, Windows 11 + Windows 365 apps and Windows 11, are available.

For additional information to configure languages other than English, see [Install language packs on Windows 11 Enterprise VMs in Azure Virtual Desktop](windows-11-language-packs).

### Configuring client device redirection settings for Windows App on iOS/iPadOS using Microsoft Intune

You can now use Microsoft Intune Mobile Application Management to check for device posture and manage redirections for Windows App on iOS and iPadOS, You can use Microsoft Intune on both corporate managed and personal devices.

For more information, see [Manage local device redirection settings with Microsoft Intune](/en-us/windows-app/manage-device-redirection-intune?context=/azure/virtual-desktop/context/context).

## September 2024

Here's what changed in September 2024:

### Relayed RDP Shortpath (TURN) for public networks is now available

This enhancement allows UDP connections via relays using the Traversal Using Relays around NAT (TURN) protocol, extending the functionality of RDP Shortpath on public networks for everyone.

For detailed configuration guidance, including prerequisites and default configurations, see [Configure RDP Shortpath for Azure Virtual Desktop](configure-rdp-shortpath).

### Windows App is now available

Windows App is now generally available on Windows, macOS, iOS, iPadOS, and web browsers, and in preview on Android. You can use it to connect to Azure Virtual Desktop, Windows 365, Microsoft Dev Box, Remote Desktop Services, and remote PCs, securely connecting you to Windows devices and apps. To learn more about what each platform supports, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?toc=admins%2Ftoc.json&amp;pivots=azure-virtual-desktop). Windows App is now available through the appropriate store for each client platform, ensuring a smooth update process. 

For more information, see [What is Windows App?](/en-us/windows-app/overview) and [Windows App get started](/en-us/windows-app/get-started-connect-devices-desktops-apps?tabs=windows-avd%2Cwindows-w365%2Cwindows-devbox%2Cmacos-rds%2Cmacos-pc&amp;pivots=azure-virtual-desktop).

### Enabling HEVC GPU acceleration for Azure Virtual Desktop is now in preview

High Efficiency Video Coding (H.265) hardware acceleration is currently in preview. Azure Virtual Desktop supports graphics processing unit (GPU) acceleration for frame encoding which will result in improved graphical experience when using the Remote Desktop Protocol (RDP) with a GPU-enabled Virtual Machine. GPU acceleration is crucial for delivering high-fidelity graphical experiences in graphics-intensive applications, such as those used by graphic designers, video editors, and 3D modelers.

For more information, see [Enable GPU acceleration for Azure Virtual Desktop](graphics-enable-gpu-acceleration).

## August 2024

Here's what changed in August 2024:

### Configure the session lock behavior for Azure Virtual Desktop is now available

You can choose whether the session is disconnected or the remote lock screen is shown when a remote session is locked, either by the user or by policy. When the session lock behavior is set to disconnect, a dialog is shown to let users know they were disconnected. Users can choose the **Reconnect** option from the dialog when they're ready to connect again.

For more information, see [Configure the session lock behavior for Azure Virtual Desktop](configure-session-lock-behavior).

### Configuring the clipboard transfer direction in Azure Virtual Desktop is now available

Clipboard redirection in Azure Virtual Desktop allows users to copy and paste content between the user's local device and the remote session in either direction. You might want to limit the direction of the clipboard for users, to help prevent data exfiltration or malicious files being copied to a session host. You can configure whether users can use the clipboard from session host to client, or client to session host, and the types of data that can be copied.

For more information see [Configure the clipboard transfer direction in Azure Virtual Desktop](clipboard-transfer-direction-data-types).

### Microsoft Purview forensic evidence is now compatible with Azure Virtual Desktop

Forensic evidence is an opt-in add-on feature in Insider Risk Management that gives security teams visual insights into potential insider data security incidents, with user privacy built in. Microsoft Purview Insider Risk Management correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage and security violations. Insider risk management enables customers to create policies to manage security and compliance. 

For more information see [Learn about insider risk management forensic evidence](purview-forensic-evidence).

### Support for FIDO devices and passkeys on macOS and iOS is now available

Windows App and the Remote Desktop app now support FIDO devices and passkeys for Microsoft Entra ID sign in on macOS and iOS.

For more information see [Azure Virtual Desktop identities and authentication](authentication).

### New Microsoft Teams can be installed on an image using custom image templates

New Teams has replaced classic Teams when using [custom image templates](custom-image-templates). When updating an existing template, classic Teams is replaced by new Teams. No action is required. When reusing an existing template which references classic Teams, it's updated to new Teams by Microsoft.

For more information see [End of availability for classic Teams client](/en-us/microsoftteams/teams-classic-client-end-of-availability).

## July 2024

Here's what changed in July 2024:

### New Teams available on Windows Enterprise multi-session images with Microsoft 365 apps pre-installed

Our Windows Enterprise multi-session images with Microsoft 365 apps have been updated with the new Teams app pre-installed. Users accessing newly provisioned session hosts with the latest images, updated late July, enjoy the new experience. Learn more about [What's changing in the new Microsoft Teams](/en-us/microsoftteams/new-teams-whats-changing).

Learn more about Windows Enterprise multi-session in our [FAQ](windows-multisession-faq).

## June 2024

Here's what changed in June 2024:

### Configuring the default chroma value for Azure Virtual Desktop is now in preview

The chroma value determines the color space used for encoding. By default, the chroma value is set to 4:2:0, which provides a good balance between image quality and network bandwidth. You can increase the default chroma value to 4:4:4 to improve image quality. You don't need to use GPU acceleration to change the default chroma value.

For more information, see [Configure default chroma value for Azure Virtual Desktop](configure-default-chroma-value).

### New Teams SlimCore changes are now available in preview

Microsoft Teams on Azure Virtual Desktop supports chat and collaboration. With media optimizations, it also supports calling and meeting functionality by redirecting it to the local device when using Windows App or the Remote Desktop client on a supported platform.

There are two versions of Teams, Classic Teams and [New Teams](/en-us/microsoftteams/new-teams-desktop-admin), and you can use either with Azure Virtual Desktop. New Teams has feature parity with Classic Teams, and improves performance, reliability, and security.

New Teams can use either SlimCore or the WebRTC Redirector Service. SlimCore is available in preview and you need to [opt in to the preview](/en-us/microsoftteams/public-preview-doc-updates?tabs=new-teams-client) to use it. If you use SlimCore, you should also install the WebRTC Redirector Service. This allows a user to fall back to WebRTC, such as if they roam between different devices that don't support the new optimization architecture. For more information about SlimCore and how to opt into the preview, see [New VDI solution for Teams](/en-us/microsoftteams/vdi-2).

For more information, see [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd).

### Preferred application group type behavior for pooled host pools in Azure Virtual Desktop has been updated

An application group is a logical grouping of applications that are available on session hosts in a host pool. Application groups control whether a full desktop or which applications from a host pool are available to users to connect to. An application group can only be assigned to a single host pool, but you can assign multiple application groups to the same host pool. Users can be assigned to multiple application groups across multiple host pools, which enable you to vary the applications and desktops that users can access.

For more information, see [Preferred application group type behavior for pooled host pools in Azure Virtual Desktop](preferred-application-group-type).

### Additional data and metrics for Connection Reliability for Azure Virtual Desktop is now available

Using Azure Virtual Desktop Insights can help you understand your deployments of Azure Virtual Desktop. It can help with checks such as which client versions are connecting, opportunities for cost saving, or knowing if you have resource limitations or connectivity issues.

The reliability of a connection can have a significant impact on the end-user experience. Azure Virtual Desktop Insights can help you understand disconnection events and correlations between errors that affect end users.

For more information and instructions, see [Use cases for Azure Virtual Desktop Insights](insights-use-cases).

### RDP Shortpath configuration in host pool settings

You can granularly control how RDP Shortpath is used by configuring the networking settings of a host pool using the Azure portal or Azure PowerShell. Configuring RDP Shortpath on the host pool enables you to optionally set which of the four RDP Shortpath options you want to use and is used alongside the session host configuration.

For more information, see [Configure RDP Shortpath for Azure Virtual Desktop](configure-rdp-shortpath).

### Adding and managing App Attach applications in Azure Virtual Desktop is now available

App Attach enables you to dynamically attach applications from an application package to a user session in Azure Virtual Desktop. Applications aren't installed locally on session hosts or images, making it easier to create custom images for your session hosts, and reducing operational overhead and costs for your organization. Delivering applications with App Attach also gives you greater control over which applications your users can access in a remote session.

For more information and instructions, see [Add and manage App Attach and MSIX App Attach applications](app-attach-setup).

## May 2024

Here's what changed in May 2024:

### New Microsoft Teams now pre-installed in Windows 11 multi-session with Microsoft 365 Apps gallery images

Images for Windows 11 multi-session with Microsoft 365 Apps in the Azure Marketplace now come with the new Microsoft Teams pre-installed (not Teams (Classic)). This applies to Windows 11 Enterprise multi-session 23H2 and 22H2. 

### Configuring client device redirection for Windows App and the Remote Desktop app using Microsoft Intune is now in preview

You can now use Microsoft Intune to configure client device redirection settings for Windows App and the Remote Desktop app in preview. IT admins can configure different redirection scenarios based on group membership and whether the device is managed by Intune or unmanaged. Additional capabilities include the ability to check and restrict access to Azure Virtual Desktop based on criteria such as OS version, allowed app (Windows App or the Remote Desktop app), allowed app version number, whether a threat is detected by Mobile Threat Defense (MTD), the device is jailbroken/rooted, and more.

For more information, see [Manage local device redirection settings with Microsoft Intune](/en-us/windows-app/manage-device-redirection-intune?context=/azure/virtual-desktop/context/context).

### Hibernate support for session hosts in a personal host pool is generally available

Deploying session hosts in a personal host pool with hibernate support is now generally available. With hibernate support, you can pause session hosts you aren't using. For more information, see [Hibernating Windows virtual machines](/en-us/azure/virtual-machines/windows/hibernate-resume-windows).

### Hibernate support for autoscale is generally available

Autoscale support for virtual machines that use hibernate is generally available, enabling session hosts to be scaled automatically while preserving their state. For more information, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios) and [Hibernating virtual machines](/en-us/azure/virtual-machines/hibernate-resume).

### Support for Trusted Launch virtual machines support in Azure Government and Azure operated by 21Vianet

Trusted Launch virtual machines are now available in Azure Government and Azure operated by 21Vianet. Deploying Trusted Launch virtual machines in your Azure Virtual Desktop environment improves the security posture of your session hosts by helping protect against advanced and persistent attack techniques. You can select Trusted Launch when you create a new host pool with machines or add a new virtual machine to an existing host pool.

For more information about the benefits of Trusted Launch, see our [Trusted Launch documentation](/en-us/azure/virtual-machines/trusted-launch).

## April 2024

Here's what changed in April 2024:

### Updated the administrative template for Watermarking in Intune and Group Policy

The [administrative template for Azure Virtual Desktop](administrative-template) now includes updated template settings for watermarking, which are available in Microsoft Intune and Group Policy. For more information, along with instructions, see [Enable watermarking](watermarking#enable-watermarking) and

### Autoscale and Start VM on Connect for Azure Virtual Desktop on Azure Stack HCI is in preview

Autoscale and Start VM on Connect are now available for session hosts running on Azure Stack HCI in preview. Autoscale lets you scale your session host virtual machines in a host pool up or down according to schedule to optimize deployment costs. Start VM On Connect lets you reduce costs by enabling end users to turn on their session host virtual machines only when they need them so you can power them off when they're not needed.

For more information, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios) and [Set up Start VM on Connect](start-virtual-machine-connect).

## March 2024

Here's what changed in March 2024:

### ms-avd Uniform Resource Identifier (URI) scheme for Azure Virtual Desktop with the Remote Desktop client now generally available

The Uniform Resource Identifier (URI) scheme `ms-avd`, which is used to invoke the Remote Desktop client with specific commands, parameters, and values designed for using Azure Virtual Desktop, is now generally available. For example, you can use a URI to subscribe to a workspace or connect to a particular desktop or RemoteApp.

For more information and examples, see [Uniform Resource Identifier schemes with the Remote Desktop client for Azure Virtual Desktop](uri-scheme).

### Every time sign-in frequency Conditional Access option is now in preview

Using Microsoft Entra sign-in frequency with Azure Virtual Desktop prompts users to reauthenticate when launching a new connection after a period of time. You can now require reauthentication after a shorter period of time.

For more information, see [Configure sign-in frequency](set-up-mfa?tabs=avd#configure-sign-in-frequency).

### Configuring the clipboard transfer direction is now in preview

Clipboard redirection in Azure Virtual Desktop allows users to copy and paste content in either direction between the user's local device and the remote session. However, in some scenarios you might want to limit the direction of the clipboard for users to prevent data exfiltration or copying malicious files to a session host. You can configure users to only be able to use the clipboard to copy data from session host to client or client to session host, as well as what kind of data they can copy.

For more information, see [Configure the clipboard transfer direction in Azure Virtual Desktop](clipboard-transfer-direction-data-types?tabs=intune).

### Azure Proactive Resiliency Library (APRL) for Azure Virtual Desktop workload now available

The APRL now has recommendations for Azure Virtual Desktop, which can help you can meet resiliency targets for your applications through a holistic self-serve resilience experience. APRL recommendations cover Azure Virtual Desktop requirements and definitions, letting you run automated configuration checks against workload requirements. APRL also contains supporting Azure Resource Graph queries that you can use to identify resources that aren't fully compliant with APRL guidance and recommendations.

For more information about these recommendations, see the [Azure Proactive Resiliency Library (APRL)](https://azure.github.io/Azure-Proactive-Resiliency-Library/).

## February 2024

Here's what changed in February 2024:

### Azure Virtual Desktop for Azure Stack HCI now generally available

Azure Virtual Desktop for Azure Stack HCI extends the capabilities of the Microsoft Cloud to your datacenters. Bringing the benefits of Azure Virtual Desktop and Azure Stack HCI together, organizations can securely run virtualized desktops and apps on-premises in their datacenter and at the edges of their organization. This versatility is especially useful for organizations with data residency and proximity requirements or latency-sensitive workloads.

For more information, see [Azure Virtual Desktop for Azure Stack HCI now available!](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/azure-virtual-desktop-for-azure-stack-hci-now-available/ba-p/4038030)

### New Azure Virtual Desktop web client is now available

We've updated the Azure Virtual Desktop web client to the new web client. All users automatically migrate to this new version of the web client to access their resources.

For more information about the new features available in the new web client, see [Use features of the Remote Desktop Web client](/en-us/previous-versions/remote-desktop-client/client-features-web-cloud).

## January 2024

There were no major releases or new features in January 2024.

## December 2023

Here's what changed in December 2023:

### New App Attach features for Azure Virtual Desktop in preview

The preview of *App Attach* is now available. App Attach brings many benefits over MSIX App Attach, including assigning applications per user, using the same application package across multiple host pools, upgrading applications, and being able to run two versions of the same application concurrently on the same session host.

For more information, see [New App Attach features for Azure Virtual Desktop in preview](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/new-app-attach-features-for-azure-virtual-desktop-in-public/ba-p/4002826) and [MSIX App Attach and App Attach in Azure Virtual Desktop](app-attach-overview?pivots=app-attach).

### The new Microsoft Teams desktop client is now generally available to use with Azure Virtual Desktop

The [new Microsoft Teams desktop client](/en-us/microsoftteams/new-teams-desktop-admin) is now generally available to use with Azure Virtual Desktop. The new Teams desktop client has feature parity with the classic Teams app and improved performance, reliability, and security.

For more information, see [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd).

## November 2023

Here's what changed in November 2023:

### Administrators can now easily start, stop, and restart session hosts

You can now stop, start and restart session hosts directly in the Azure portal. You can also choose whether to perform the operation on a single session host or on multiple session hosts in your host pool at the same time.

### Use community images and directed shared images when deploying session hosts

You can now select community images and directed shared images to use for your session hosts when you [deploy Azure Virtual Desktop in the Azure portal](deploy-azure-virtual-desktop?tabs=portal), [add session hosts to a host pool](add-session-hosts-host-pool), or [create custom images](custom-image-templates).

Community images and associated publisher information aren't verified or tested by Microsoft, so make sure to verify any custom images you deploy using this method.

For more information on preparing, storing and sharing images to be used to create virtual machines, see [Store and share VM images in a compute gallery](/en-us/azure/virtual-machines/shared-image-galleries).

### Windows 11 version 23H2 and 22H2 images added to the Azure Marketplace

Windows 11 Enterprise multi-session, versions 23H2 and 22H2 with Microsoft 365 apps preinstalled are now available in Azure Marketplace. You can use these images when you [deploy Azure Virtual Desktop in the Azure portal](deploy-azure-virtual-desktop?tabs=portal), [add session hosts to a host pool](add-session-hosts-host-pool), or [create custom images](custom-image-templates).

### Autoscale for personal host pools is generally available

Autoscale lets you scale your session host virtual machines (VMs) in a host pool up or down according to schedule, optimizing deployment costs.

For more information, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios).

### Hibernate support for autoscale is in preview

Autoscale can now use the hibernate feature in preview, which can pause session hosts you aren't using. For more information, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios) and [Hibernating virtual machines](/en-us/azure/virtual-machines/hibernate-resume).

### Updated preview of Azure Virtual Desktop on Azure Stack HCI

We've updated the preview of Azure Virtual Desktop on Azure Stack HCI. You can now deploy Azure Virtual Desktop with your session hosts on Azure Stack HCI as an integrated experience with Azure Virtual Desktop in the Azure portal. For more information, see [Azure Virtual Desktop on Azure Stack HCI](azure-stack-hci-overview) and [Deploy Azure Virtual Desktop](deploy-azure-virtual-desktop).

### Single sign-on using Microsoft Entra authentication is now generally available

Single sign-on using Microsoft Entra authentication is now generally available. Single sign-on enables users to automatically sign the user into Windows, without prompting them for their credentials for every connection.

For more information, see [Configure single sign-on for Azure Virtual Desktop using Microsoft Entra authentication](configure-single-sign-on).

### In-session passwordless authentication is now generally available

In-session passwordless authentication is now generally available. Azure Virtual Desktop supports in-session passwordless authentication using Windows Hello for Business or security devices like FIDO keys.

For more information, see [In-session passwordless authentication](authentication#in-session-authentication).

### Windows App preview

Windows App is available in preview for Windows, macOS, iOS and iPadOS, and in a web browser. You can use it to connect to Azure Virtual Desktop, Windows 365, Microsoft Dev Box, Remote Desktop Services, and remote PCs, securely connecting you to Windows devices and apps. For more information, see [Windows App](/en-us/windows-app/overview).

## October 2023

Here's what changed in October 2023:

### New article about Azure Virtual Desktop service architecture and resilience

We've published a new article about the service architecture for Azure Virtual Desktop and how it provides a resilient, reliable, and secure service for organizations and users. Most components are Microsoft-managed, but some are customer-managed.

You can learn more at [Azure Virtual Desktop service architecture and resilience](service-architecture-resilience).

### OneDrive with RemoteApp in preview

You can now use Microsoft OneDrive alongside a RemoteApp in preview. You can use this feature to access and synchronize your files while using a RemoteApp. When you connect to a RemoteApp, OneDrive can automatically launch as a companion to the RemoteApp.

For more information about prerequisites and configuration, see [Use Microsoft OneDrive with a RemoteApp in Azure Virtual Desktop (preview)](onedrive-remoteapp).

### Administrative template for FSLogix now available in Intune settings catalog

The [administrative template for FSLogix](/en-us/fslogix/how-to-use-group-policy-templates) is now available in the [Intune settings catalog](/en-us/mem/intune/configuration/administrative-templates-windows). This template enables you to configure FSLogix settings centrally for [session hosts that are enrolled in Intune](management#microsoft-intune).

## September 2023

Here's what changed in September 2023:

### Azure Virtual Desktop (classic) deprecation

Azure Virtual Desktop (classic) now blocks users from creating new tenants. Customers should be deploying the current version of Azure Virtual Desktop for any new workloads. However, while Azure Virtual Desktop (classic) blocks new tenants, you can still access all other ongoing operation and management processes. We will no longer support Azure Virtual Desktop (classic) in September 2026, so we highly recommend you migrate from classic to Azure Virtual Desktop before then.

For more information about the Azure Virtual Desktop (classic) retirement, see [Azure Virtual Desktop (classic) retirement](/en-us/previous-versions/azure/virtual-desktop-classic/classic-retirement).

### Updates to Azure Virtual Desktop overview page in the Azure portal

We've updated the overview page in the Azure Virtual Desktop administrator portal to include new visuals and tile links. These updates make it easier to navigate to documentation, find the forums for collaboration and discussion, submit feedback, and locate release notes for Azure Virtual Desktop.

### The latest version of FSLogix is now included in Windows Enterprise multi-session images

We added the latest version of FSLogix to Windows 10 and 11 Enterprise multi-session images in the Azure Marketplace. As of September 12, 2023, all images come preinstalled with the latest version of FSLogix.

For more information about what's new in FSLogix, see the [FSLogix Release Notes](/en-us/fslogix/overview-release-notes?context=%2Fazure%2Fvirtual-desktop%2Fcontext%2Fcontext).

### Azure Virtual Desktop Insights support for the Azure Monitor Agent is now generally available

Azure Virtual Desktop Insights is a dashboard built on Azure Monitor workbooks that helps you understand your Azure Virtual Desktop environments. Azure Virtual Desktop Insights support for the Azure Monitor agent is now generally available. For more information, see [Use Azure Virtual Desktop Insights to monitor your deployment](insights?tabs=monitor).

The Log Analytics agent for Azure Monitor is deprecating on August 31, 2024. We recommend you migrate monitoring your virtual machines (VMs) and servers to Azure Monitor Agent before that date. For more information about how to migrate, see [Migrate to Azure Monitor Agent from Log Analytics agent](/en-us/azure/azure-monitor/agents/azure-monitor-agent-migration).

### Custom Image Template feature is now generally available

Azure Virtual Desktop just made it easier for you to create your golden image with the new Custom Image Template feature. You can use this new management option in the Azure portal to include built-in or custom scripts in your template that you can reuse. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-azure-virtual-desktop-custom/ba-p/3909907).

## August 2023

Here's what changed in August 2023:

### Updated Group Policy templates for FSLogix

The [FSLogix 2210 hotfix 2](/en-us/fslogix/overview-release-notes#fslogix-2210-hotfix-2-29861260056) release includes updates to the Group Policy templates. Before this release, the Group Policy template files had some unique behaviors that made it difficult to find the correct policy name based on the list of configuration settings for Profiles, Office Data File Containers (ODFC), and Cloud Cache.

For more information about FSLogix Group Policy Template Files, see [How to Use FSLogix Group Policy Template Files for FSLogix](/en-us/fslogix/how-to-use-group-policy-templates).

### Improvements in custom image templates

We've updated the text, tooltips, and links for custom image templates in the Azure portal to make them easier to use. You can also now go to the built-in customization settings and remove Clipchamp in the Remove AppX package list.

We built the custom image templates feature using [Azure Image Builder](/en-us/azure/virtual-machines/image-builder-overview) for you to use with Azure Virtual Desktop. For more information, see [Custom image templates](custom-image-templates).

## July 2023

Here's what changed in July 2023:

### Watermarking is now generally available

[Watermarking](watermarking), when used with screen capture protection, helps protect your sensitive information from capture on client endpoints. When you enable watermarking, QR code watermarks appear as part of remote desktops. The QR code contains the connection ID of a remote session that admins can use to trace the session. You can configure watermarking on session hosts and enforce it with the Remote Desktop client.

### Audio call redirection for Azure Virtual Desktop in preview

Call redirection, which optimizes audio calls for WebRTC-based calling apps, is now in preview. Multimedia redirection redirects media content from Azure Virtual Desktop to your local machine for faster processing and rendering. Both Microsoft Edge and Google Chrome support this feature when using the Windows Desktop client.

For more information about which sites are compatible with this feature, see [Call redirection](multimedia-redirection-video-playback-calls#call-redirection).

### Autoscale for personal host pools is currently in preview

Autoscale for personal host pools is now in preview. Autoscale lets you scale your session host virtual machines (VMs) in a host pool up or down according to a schedule to optimize deployment costs.

To learn more about autoscale for personal host pools, see [Autoscale scaling plans and example scenarios in Azure Virtual Desktop](autoscale-scenarios).

### Confidential virtual machines and Trusted Launch virtual machines are now generally available in Azure Virtual Desktop

Confidential virtual machines and Trusted Launch virtual machines for Azure Virtual Desktop are now generally available. You can select these options when you create a new host pool with machines or add a new virtual machine to an existing host pool.

Azure confidential virtual machines (VMs) offer VM memory encryption with integrity protection, which strengthens guest protections to deny the hypervisor and other host management components code access to the VM memory and state. For more information about the security benefits of confidential VMs, see our [confidential computing documentation](/en-us/azure/confidential-computing/confidential-vm-overview).

Trusted Launch protects against advanced and persistent attack techniques. This feature allows you to securely deploy your VMs with verified boot loaders, OS kernels, and drivers. Trusted Launch also protects keys, certificates, and secrets in VMs. For more information about the benefits of Trusted Launch, see our [Trusted Launch documentation](/en-us/azure/virtual-machines/trusted-launch). Trusted Launch is now enabled by default for all Windows images used with Azure Virtual Desktop.

For more information about this announcement, see [Announcing General Availability of confidential VMs in Azure Virtual Desktop](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-confidential-vms-in-azure/ba-p/3857974).

### Private Link with Azure Virtual Desktop is now generally available

Private Link with Azure Virtual Desktop allows users to establish secure connections to remote resources using private endpoints. With Private Link, traffic between your virtual network and the Azure Virtual Desktop service is routed through the Microsoft *backbone* network. This routing eliminates the need to expose your service to the public internet, enhancing the overall security of your infrastructure. By keeping traffic within this protected network, Private Link adds an extra layer of security for your Azure Virtual Desktop environment. For more information about Private Link, see [Azure Private Link with Azure Virtual Desktop](private-link-overview) or read [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-general-availability-of-private-link-for-azure/ba-p/3874429).

### Tamper protection support for Azure Virtual Desktop

Microsoft Intune now supports the use of endpoint security [antivirus policy](/en-us/mem/intune/protect/endpoint-security-antivirus-policy#prerequisites-for-tamper-protection) to manage [tamper protection](/en-us/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection) for Azure Virtual Desktop session hosts running Windows 11 Enterprise or Windows 11 Enterprise multi-session. Support for tamper protection requires you to onboard session hosts to Microsoft Defender for Endpoint before you apply the policy that enables tamper protection.

## June 2023

Here's what changed in June 2023:

### Azure Virtual Desktop Insights support for the Azure Monitor Agent now in preview

Azure Virtual Desktop Insights is a dashboard built on Azure Monitor workbooks that helps IT professionals understand their Azure Virtual Desktop environments. Azure Virtual Desktops Insights support for the Azure Monitor agent is now in preview. For more information, see [Use Azure Virtual Desktop Insights to monitor your deployment](insights?tabs=monitor).

### Administrative template for Azure Virtual Desktop now available in Intune

We've created an administrative template for Azure Virtual Desktop to help you configure certain features in Azure Virtual Desktop. This administrative template is now available in Intune, which enables you to centrally configure session hosts that are enrolled in Intune and Azure Active Directory (Azure AD) joined or hybrid Azure AD joined.

For more information, see [Administrative template for Azure Virtual Desktop](administrative-template?tabs=intune).

## May 2023

Here's what changed in May 2023:

### Custom image templates is now in preview

Custom image templates is now in preview. Custom image templates help you easily create a custom image that you can use when deploying session host VMs. With custom images, you can standardize the configuration of your session host VMs for your organization. Custom image templates is built on [Azure Image Builder](/en-us/azure/virtual-machines/image-builder-overview) and tailored for Azure Virtual Desktop. For more information about the preview, check out [Custom image templates](custom-image-templates) or read [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-public-preview-of-azure-virtual-desktop-custom/ba-p/3784361).

## April 2023

Here's what changed in April 2023:

### Azure Virtual Desktop Store app for Windows in preview

The [Azure Virtual Desktop Store app for Windows](users/connect-windows-azure-virtual-desktop-app?toc=/azure/virtual-desktop/toc.json&amp;bc=/azure/virtual-desktop/breadcrumb/toc.json) is now in preview for Windows 10 and 11. With the Store App, you can now automatically update the client, unlike with the Remote Desktop client. You can also pin a RemoteApp to your Start menu to personalize your desktop and reduce clutter.

For more information about the preview release version, check out [Use features of the Azure Virtual Desktop Store app for Windows when connecting to Azure Virtual Desktop (preview)](/en-us/previous-versions/remote-desktop-client/client-features-windows-msrdc?toc=%2Fazure%2Fvirtual-desktop%2Ftoc.json&amp;bc=%2Fazure%2Fvirtual-desktop%2Fbreadcrumb%2Ftoc.json), [What's new in the Azure Virtual Desktop Store App (preview)](whats-new-client-windows-azure-virtual-desktop-app), or read [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-of-the-new-azure-virtual-desktop-app/ba-p/3785698).

### Intune user-scope configuration for Windows 10 Enterprise multi-session VMs now generally available

Microsoft Intune user-scope configuration for Azure Virtual Desktop multi-session Virtual Machines (VMs) on Windows 10 and 11 is now generally available. With this feature, you're able to:

- Configure user-scope policies using the Settings catalog and assign those policies to groups of users.
- Configure user certificates and assign them to users.
- Configure PowerShell scripts to install in user context and assign the scripts to users.

For more information, see [Azure Virtual Desktop multi-session with Intune](/en-us/mem/intune/fundamentals/azure-virtual-desktop-multi-session) or [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-intune-user-scope-configuration-for-azure-virtual/ba-p/3667410).

## March 2023

Here's what changed in March 2023:

### Redesigned connection bar for the Windows Desktop client

The latest version of the Windows Desktop client includes a redesigned connection bar. For more information, see [Updates for version 1.2.4159](/en-us/previous-versions/remote-desktop-client/whats-new-windows#updates-for-version-124159).

### Shutdown session host status

The Shutdown session host status is now available in the Azure Virtual Desktop portal and the most recent API version. For more information, see [Session host statuses and health checks](troubleshoot-statuses-checks#session-host-statuses).

### Windows 10 and 11 22H2 images now visible in the image drop-down menu

Windows 10 and 11 22H2 Enterprise and Enterprise multi-session images are now visible in the image dropdown when creating a new host pool or adding a VM in a host pool from the Azure Virtual Desktop portal.

### ms-avd Uniform Resource Identifier (URI) scheme in preview

A Uniform Resource Identifier (URI) scheme for Azure Virtual Desktop that you can use with the Remote Desktop client for Azure Virtual Desktop. You can use `ms-avd` to subscribe to a workspace or connect to a particular desktop or RemoteApp. URI schemes provide fast and efficient end-user connection to Azure Virtual Desktop resources. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-public-preview-of-uniform-resource-identifier/ba-p/3763075) and [URI schemes with the Remote Desktop client for Azure Virtual Desktop (preview)](uri-scheme).

### Azure Virtual Desktop Insights at Scale now generally available

Azure Virtual Desktop Insights at Scale is now generally available. This feature gives you the ability to review performance and diagnostic information in multiple host pools at the same time in a single view. If you're an existing Azure Virtual Desktop Insights user, you get this feature without having to do any extra configuration or setup. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-general-availability-of-azure-virtual-desktop/ba-p/3738624) and [Use Azure Virtual Desktop Insights to monitor your deployment](insights).

## February 2023

Here's what changed in February 2023:

### Symmetric NAT support for RDP Shortpath in preview

This feature is an extension of the generally available Remote Desktop Protocol (RDP) Shortpath feature that allows us to establish a User Datagram Protocol (UDP) connection indirectly using a relay with the TURN (Traversal Using Relays around NAT) protocol for symmetric NAT (Network Address Translation). For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-of-symmetric-nat-support-for-rdp/ba-p/3736466) or [RDP Shortpath for Azure Virtual Desktop](rdp-shortpath?tabs=public-networks).

### Multimedia redirection enhancements now generally available

Multimedia redirection is now generally available. Multimedia redirection enables smooth video playback while viewing videos in a browser running on Azure Virtual Desktop. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-multimedia-redirection-mmr-on/ba-p/3736489) or [Multimedia redirection for video playback and calls in a remote session](multimedia-redirection-video-playback-calls).

### New User Interface for Azure Virtual Desktop web client now in preview

The Azure Virtual Desktop web client has a new user interface (UI) that's now in preview. This new UI gives the web client a cleaner, more modern look and feel. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-of-the-new-azure-virtual-desktop-web/ba-p/3731165) or [Use features of the Remote Desktop Web client](/en-us/previous-versions/remote-desktop-client/client-features-web-cloud?toc=%2Fazure%2Fvirtual-desktop%2Ftoc.json#display-preferences).

## January 2023

Here's what changed in January 2023:

### Watermarking for Azure Virtual Desktop now in preview

Watermarking for Azure Virtual Desktop is now in preview for the Windows Desktop client. This feature protects sensitive information from being captured on client endpoints by adding watermarks to remote desktops. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-for-watermarking-on-azure-virtual/ba-p/3730264) or [Watermarking in Azure Virtual Desktop](watermarking).

### Give or Take Control for macOS Teams on Azure Virtual Desktop now generally available

Version 1.31.2211.15001 of the WebRTC Redirector service includes support for Give or Take Control for macOS users. This version includes performance improvements for Give or Take Control on Windows. For more information, see [Updates for version 1.31.2211.15001](whats-new-webrtc#updates-for-version-131221115001).

### Microsoft Teams application window sharing on Azure Virtual Desktop now generally available

Previously, users could only share their full desktop windows or a Microsoft PowerPoint Live presentation during Teams calls. With application window sharing, users can now choose a specific window to share from their desktop screen and help reduce the risk of displaying sensitive content during meetings or calls. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-teams-application-window-sharing-is-now-generally/ba-p/3719595).

### Windows 7 End of Support

Starting January 10, 2023, Azure Virtual Desktop no longer supports Windows 7 as a client or host. We recommend upgrading to a supported Windows release. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/avd-support-for-windows-7-ended-on-january-10th-2023/m-p/3715785).

## December 2022

Here's what changed in December 2022:

### FSLogix 2210 now generally available

FSLogix version 2210 is now generally available. This version introduces new features like VHD Disk Compaction, a new process that improves user experience with AppX applications like built-in Windows apps (inbox apps) and Recycle Bin roaming. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-fslogix-2210/ba-p/3695166) or [What’s new in FSLogix](/en-us/fslogix/whats-new?context=%2Fazure%2Fvirtual-desktop%2Fcontext%2Fcontext#fslogix-2210-29836152326).

### India metadata service now generally available

The Azure Virtual Desktop region in India is now generally available. Customers can now store their Azure Virtual Desktop objects and metadata within a database located in the India geography. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/azure-virtual-desktop-metadata-database-is-now-available-in/ba-p/3670768).

### Confidential Virtual Machine support for Azure Virtual Desktop now in preview

Azure Confidential VM support is now in preview. Azure Confidential VMs increase data privacy and security by protecting data in use. The preview update also adds support for Windows 11 22H2 to Confidential VMs. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/confidential-virtual-machine-support-for-azure-virtual-desktop/ba-p/3686350).

## November 2022

Here's what changed in November 2022:

### RDP Shortpath for public networks now generally available

Remote Desktop Protocol (RDP) Shortpath for public networks is now generally available. RDP Shortpath improves the transport reliability of Azure Virtual Desktop connections by establishing a direct User Datagram Protocol (UDP) data flow between the Remote Desktop client and session hosts. This feature will be enabled by default for all customers. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-rdp-shortpath/ba-p/3691026).

### Azure Virtual Desktop Insights at Scale in preview

The ability to review performance and diagnostic information across multiple host pools in one view with Azure Virtual Desktop Insights at Scale is now in preview. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-public-preview-of-avd-insights-at-scale/ba-p/3685387) or [Use Azure Virtual Desktop Insights to monitor your deployment](insights).

### Intune user configuration for Windows 11 Enterprise multi-session VMs now generally available

Microsoft Intune user scope configuration for Azure Virtual Desktop multi-session VMs on Windows 11 is now generally available. With this feature, you're able to:

- Configure user scope policies using the Settings catalog and assign them to groups of users.
- Configure user certificates and assign them to users.
- Configure PowerShell scripts to install in the user context and assign them to users.

For more information, see [Azure Virtual Desktop multi-session with Intune](/en-us/mem/intune/fundamentals/azure-virtual-desktop-multi-session) or [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-intune-user-scope-configuration-for-azure-virtual/ba-p/3667410).

### Azure Active Directory Join VMs with FSLogix profiles on Azure Files now generally available

FSLogix profiles with Azure Active Directory (AD)-joined Windows 10, 11, and Windows Server 2022 VMs for hybrid users in Azure Virtual Desktop are now generally available. These FSLogix profiles let you seamlessly access file shares from Azure AD-joined VMs and use them to store your FSLogix profile containers. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-fslogix-profiles-for-azure-ad/ba-p/3671310).

### Private Link for Azure Virtual Desktop now in preview

Private endpoints from Azure Private Link for Azure Virtual Desktop are now in preview. Private Link can enable traffic between session hosts, clients, and the Azure Virtual Desktop service to flow through a private endpoint within your virtual network instead of the public internet. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-public-preview-of-private-link-for-azure-virtual/m-p/3671226), read our overview at [Use Azure Private Link with Azure Virtual Desktop (preview)](private-link-overview), or get started at [Set up Private Link for Azure Virtual Desktop (preview)](private-link-setup).

## October 2022

Here's what changed in October 2022:

### Background effects for macOS Teams on Azure Virtual Desktop now generally available

Background effects for Teams on Azure Virtual Desktop is now generally available for the macOS version of Teams on Azure Virtual Desktop. This feature lets meeting participants select an available image in Teams to change their background or choose to blur their background. Background effects are only compatible with version 10.7.10 or later of the Azure Virtual Desktop macOS client. For more information, see [What’s new in the macOS client](/en-us/windows-server/remote/remote-desktop-services/clients/mac-whatsnew?toc=%2Fazure%2Fvirtual-desktop%2Ftoc.json&amp;bc=%2Fazure%2Fvirtual-desktop%2Fbreadcrumb%2Ftoc.json#updates-for-version-10710).

### Host pool deployment support for Azure availability zones now generally available

We've improved the host pool deployment process. You can now deploy host pools into up to three availability zones in supported Azure regions. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-support-for-azure/ba-p/3636262).

### FSLogix version 2210 now in preview

FSLogix version 2210 is now preview. This new version includes new features, bug fixes, and other improvements. One of the new features is Disk Compaction, which lets you remove white space in a disk to shrink the disk size. Disk Compaction saves you significant amounts of storage capacity in the storage spaces where you keep your FSLogix disks. For more information, see [What’s new in FSLogix](/en-us/fslogix/whats-new#fslogix-2210-29830844092---public-preview) or [the FSLogix Disk Compaction blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-fslogix-disk-compaction/ba-p/3644807).

### Universal Print for Azure Virtual Desktop now generally available

The release of Windows 11 22H2 includes an improved printing experience that combines the benefits of Azure Virtual Desktop and Universal Print for Windows 11 multi-session users. Learn more at [Printing on Azure Virtual Desktop using Universal Print](/en-us/universal-print/fundamentals/universal-print-avd).

## September 2022

Here's what changed in September 2022:

### Single sign-on and passwordless authentication now in preview

The ability to enable an Azure Active Directory (AD)-based single sign-on experience and support for passwordless authentication, using Windows Hello and security devices (like FIDO2 keys) is now in preview. This feature is available for Windows 10, Windows, 11 and Windows Server 2022 session hosts with the September Cumulative Update Preview installed. The single sign-on experience is currently compatible with the Windows Desktop and web clients. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-of-sso-and-passwordless-authentication/ba-p/3638244).

### Connection graphics data logs for Azure Virtual Desktop now in preview

The ability to collect graphics data for your Azure Virtual Desktop connections through Azure Log Analytics is now in preview. This data can help administrators understand factors across the server, client, and network that contribute to slow or choppy experiences for a user. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/collect-and-query-graphics-data-for-azure-virtual-desktop/m-p/3638565).

### Multimedia redirection enhancements now in preview

An upgraded version of multimedia redirection for Azure Virtual Desktop is now in preview. We've made various improvements to this version, including more supported websites, RemoteApp browser support, and enhancements to media controls for better clarity and one-click tracing. Learn more at [Multimedia redirection on Azure Virtual Desktop (preview)](multimedia-redirection) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/new-multimedia-redirection-upgrades-on-azure-virtual-desktop-are/m-p/3639520).

### Grouping costs by Azure Virtual Desktop host pool now in preview

Microsoft Cost Management has a new feature in preview that lets you group Azure Virtual Desktop costs with Azure tags by using the cm-resource-parent tag key. Cost grouping makes it easier to understand and manage costs by host pool. Learn more at [Tag Azure Virtual Desktop resources to manage costs](tag-virtual-desktop-resources) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/group-costs-by-host-pool-with-cost-management-now-in-public/ba-p/3638285).

## August 2022

Here's what changed in August 2022:

### Azure portal updates

We've made the following updates to the Azure portal:

- Improved search, filtering, and performance.
- Added Windows Server 2022 images to the image selection list.
- Added "Preferred group type" to the "Basics" tab in the host pool creation process.
- Enabled custom images for Trusted Launch VMs.
- New selectable cards, including the following:
    - Unavailable machines.
    - User session.
- Removed the "Advanced" tab for the process to add a VM to the host pool.
- Removed the storage blob image option from the host pool creation and adding VM processes.
- Bug fixes.
- Made the following improvements to the "getting started" setup process:
    - Unchecked link Azure template.
    - Removed validation on existing domain admins.

### Updates to the preview version of FSLogix profiles for Azure AD-joined VMs

We've updated the preview version of the Azure Files integration with Azure AD Kerberos for hybrid identities so that it's now simpler to deploy and manage. The update should give users using FSLogix user profiles on Azure AD-joined session host an overall better experience. For more information, see [the Azure Files blog post](https://techcommunity.microsoft.com/t5/azure-storage-blog/public-preview-leverage-azure-active-directory-kerberos-with/ba-p/3612111).

### Single sign-on and passwordless authentication now in Windows Insider preview

In the Windows Insider build of Windows 11 22H2, you can now enable a preview version of the Azure AD-based single sign-on experience. This Windows Insider build also supports passwordless authentication with Windows Hello and security devices like FIDO2 keys. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/insider-preview-single-sign-on-and-passwordless-authentication/m-p/3608842).

### Universal Print for Azure Virtual Desktop now in Windows Insider preview

The latest Windows Insider build of Windows 11 22H2 also includes a preview version of the Universal Print for Azure Virtual Desktop feature. This feature provides an improved printing experience that combines the benefits of Azure Virtual Desktop and Universal Print for Windows 11 multi-session users. Learn more at [Printing on Azure Virtual Desktop using Universal Print](/en-us/universal-print/fundamentals/universal-print-avd) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/a-better-printing-experience-for-azure-virtual-desktop-with/m-p/3598592).

### Autoscale for pooled host pools now generally available

Autoscale on Azure Virtual Desktop for pooled host pools is now generally available. This feature is a native automated scaling solution that automatically turns session host virtual machines on and off according to the schedule and capacity thresholds that you define to fit your workload. Learn more at [How autoscale works](autoscale-scenarios) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-autoscale-for-pooled-host/ba-p/3591462).

### Azure Virtual Desktop with Trusted Launch update

Azure Virtual Desktop now supports provisioning Trusted Launch virtual machines with custom images stored in an Azure Compute Gallery. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/avd-now-supports-azure-compute-gallery-custom-images-with/m-p/3593955).

## July 2022

Here's what changed in July 2022:

### Scheduled agent updates now generally available

Scheduled agent updates on Azure Virtual Desktop are now generally available. This feature gives IT admins control over when the Azure Virtual Desktop agent, side-by-side stack, and Geneva Monitoring agent get updated. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-scheduled-agent-updates-on/ba-p/3579236).

### FSLogix 2201 hotfix 2

The FSLogix 2201 hotfix 2 update includes fixes to multi-session VHD mounting, Cloud Cache meta tracking files, and registry cleanup operations. This update doesn't include new features. Learn more at [What’s new in FSLogix](/en-us/fslogix/whats-new?context=%2Fazure%2Fvirtual-desktop%2Fcontext%2Fcontext#fslogix-2201-hotfix-2-29822850276) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-fslogix-2201-hotfix-2-2-9-8228-50276-has-been/m-p/3579409).

### Japan and Australia metadata service now generally available

The Azure Virtual Desktop metadata database located in Japan and Australia is now generally available. This update allows customers to store their Azure Virtual Desktop objects and metadata within a database located within that geography. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-general-availability-of-the-azure-virtual-desktop/ba-p/3570756).

### Azure Virtual Desktop moving away from Storage Blob image type

Storage Blob images are created from unmanaged disks, which means they lack the availability, scalability, and frictionless user experience that managed images and Shared Image Gallery images offer. As a result, Azure Virtual Desktop will be deprecating support for Storage Blobs image types by August 22, 2022. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/azure-virtual-desktop-is-moving-away-from-storage-blob-image/ba-p/3568364).

### Azure Virtual Desktop Custom Configuration changing to PowerShell

Starting July 21, 2022, Azure Virtual Desktop will replace the Custom Configuration Azure Resource Manager template parameters for creating host pools, adding session hosts to host pools, and the Getting Started feature with a PowerShell script URL parameter stored in a publicly accessible location. This replacement includes the parameters' respective Azure Resource Manager templates. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/azure-virtual-desktop-custom-configuration-breaking-change/m-p/3568069).

## June 2022

Here's what changed in June 2022:

### Australia metadata service in preview

The Azure Virtual Desktop metadata database located in Australia is now in preview. This allows customers to store their Azure Virtual Desktop objects and metadata within a database located within our Australia geography, ensuring that the data will only reside within Australia. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-the-public-preview-of-the-azure-virtual-desktop/ba-p/3483090).

### Intune user configuration for Windows 11 Enterprise multi-session VMs in preview

Deploying Intune user configuration policies from the Microsoft Intune admin center to Windows 11 Enterprise multi-session VMs on Azure Virtual Desktop is now in preview. In this preview, you can configure the following features:

- User scope policies using the Settings catalog.
- User certificates via Templates.
- PowerShell scripts to run in the user context.

For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/public-preview-intune-user-configuration-for-windows-11-multi/m-p/3562093).

### Teams media optimizations for macOS now generally available

Teams media optimizations for redirecting audio and video during calls and meetings to a local macOS machine is now generally available. Learn more at [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-teams-media-optimizations-is-now-generally-available/ba-p/3563125).

## May 2022

Here's what changed in May 2022:

### Background effects with Teams on Azure Virtual Desktop now generally available

Users can now make meetings more personalized and avoid unexpected distractions by applying background effects. Meeting participants can select an available image in Teams to change their background or choose to blur their background. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-teams-background-effects-is-now-generally-available-on/ba-p/3401961).

### Multi-window and "Call me with Teams" features now generally available

The multi-window feature gives users the option to pop out chats, meetings, calls, or documents into separate windows to streamline their workflow. The "Call me with Teams" feature lets users transfer a Teams call to their phone. Both features are now generally available in Teams on Azure Virtual Desktop. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-teams-multi-window-support-and-call-me-are-now-in-ga/ba-p/3401830).

### Japan metadata service in preview

The Azure Virtual Desktop metadata database located in Japan is now in preview. This allows customers to store their Azure Virtual Desktop objects and metadata within a database located within our Japan geography, ensuring that the data will only reside within Japan. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-the-public-preview-of-the-azure-virtual-desktop/m-p/3417497).

### FSLogix 2201 hotfix

The latest update for FSLogix 2201 includes fixes to Cloud Cache and container redirection processes. No new features are included with this update. Learn more at [What’s new in FSLogix](/en-us/fslogix/whats-new?context=%2Fazure%2Fvirtual-desktop%2Fcontext%2Fcontext) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-fslogix-2201-hotfix-1-2-9-8171-14983-has-been/m-p/3435445).

## April 2022

Here's what changed in April 2022:

### Intune device configuration for Windows multi-session now generally available

Deploying Intune device configuration policies from the Microsoft Intune admin center to Windows multi-session VMs on Azure Virtual Desktop is now generally available. Learn more at [Using Azure Virtual Desktop multi-session with Intune](/en-us/mem/intune/fundamentals/azure-virtual-desktop-multi-session) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/intune-device-configuration-for-azure-virtual-desktop-multi/ba-p/3294444).

### Scheduled Agent Updates preview

Scheduled Agent Updates is a new feature in preview that lets IT admins specify the time and day the Azure Virtual Desktop agent, side-by-side stack, and Geneva Monitoring agent will update. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/scheduled-agent-updates-is-now-in-public-preview-on-azure/m-p/3285874).

### RDP Shortpath for public networks now in preview

A new feature for RDP Shortpath is now in preview. With this feature, RDP Shortpath can provide a direct UDP-based network transport for user sessions over public networks. Learn more at [Azure Virtual Desktop RDP Shortpath for public networks (preview)](shortpath-public) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-public-preview-of-azure-virtual-desktop-rdp-shortpath/m-p/3284763).

### The Azure Virtual Desktop web client has a new URL

Starting April 18, 2022, the Azure Virtual Desktop and Azure Virtual Desktop (classic) web clients redirect to a new URL. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/reminder-the-avd-web-client-will-be-moving-to-a-new-url/m-p/3278231).

## March 2022

Here's what changed in March 2022:

### Live Captions with Teams on Azure Virtual Desktop now generally available

Accessibility has always been important to us, so we're pleased to announce that Teams for Azure Virtual Desktop now supports real-time captions. Learn how to use live captions at [Use live captions in a Teams meeting](https://support.microsoft.com/office/use-live-captions-in-a-teams-meeting-4be2d304-f675-4b57-8347-cbd000a21260). For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/microsoft-teams-live-captions-is-now-generally-available-on/ba-p/3264148).

### Multimedia redirection enhancements now in preview

An upgraded version of multimedia redirection for Azure Virtual Desktop is now in preview. We've made various improvements to this version, including more supported websites and media controls for our users. Learn more at [Multimedia redirection for Azure Virtual Desktop](multimedia-redirection) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/new-multimedia-redirection-upgrades-on-azure-virtual-desktop-are/ba-p/3264146).

### FSLogix version 2201 is now generally available

FSLogix version 2201 is now generally available. This version includes improved sign-in and sign-out times, cloud cache performance improvements, and accessibility updates. For more information, see [the FSLogix release notes](/en-us/fslogix/whats-new?context=/azure/virtual-desktop/context/context#fslogix-2201-29811153415) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-general-availability-of-fslogix-2201-2-9-8111-53415/m-p/3270742).

## February 2022

Here's what changed in February 2022:

### Network data for Azure Virtual Desktop user connections

You now collect network data (both round trip time and available bandwidth) throughout a user’s connection in Azure Virtual Desktop with Azure Log Analytics. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/collect-and-query-network-data-for-azure-virtual-desktop/m-p/3140397).

### Unassigning and reassigning personal desktops now generally available

The feature that lets you reassign or unassign personal desktops is now generally available. You can unassign or reassign desktops using the Azure portal or REST API. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/azure-virtual-desktop-support-for-personal-desktop-unassignment/m-p/3168914).

### Teams media optimizations for macOS now in preview

Teams media optimizations for redirecting audio and video during calls and meetings to a local macOS machine are now in preview. To use this feature, you'll need to update your Azure Virtual Desktop macOS client to version 10.7.7 or later. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/teams-media-optimizations-now-in-public-preview-on-azure-virtual/ba-p/3165276) or [Use Microsoft Teams on Azure Virtual Desktop](teams-on-avd).

## January 2022

Here's what changed in January 2022:

### FSLogix version 2201 preview

FSLogix version 2201 is now in preview. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/the-fslogix-2201-public-preview-is-now-available/td-p/3070794) or [the FSLogix release notes](/en-us/fslogix/whats-new#fslogix-2201-public-preview-29804843478).

### Migration tool now generally available

The PowerShell commands that migrate metadata from Azure Virtual Desktop (classic) to Azure Virtual Desktop are now generally available. To learn more about migrating your existing deployment, see [Migrate automatically from Azure Virtual Desktop (classic)](automatic-migration) or [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/tool-to-migrate-from-azure-virtual-desktop-classic-to-arm/m-p/3094856#M8527).

### Increased application group limit

We've increased number of Azure Virtual Desktop application groups you can have on each Azure Active Directory tenant from 200 to 500. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/increase-in-avd-application-group-limit-to-500/m-p/3094678).

### Updates to required URLs

We've updated the required URL list for Azure Virtual Desktop to accommodate Azure Virtual Desktop agent traffic. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/important-new-changes-in-required-urls/m-p/3094897#M8529).

## December 2021

Here's what changed in December 2021:

### Azure portal updates

You can now automatically create Trusted Launch virtual machines through the host pool creation process instead of having to manually create and add them to a host pool after deployment. To access this feature, select the **Virtual machines** tab while creating a host pool. Learn more at [Trusted Launch for Azure virtual machines](/en-us/azure/virtual-machines/trusted-launch).

### Azure Active Directory Join VMs with FSLogix profiles on Azure Files

Azure Active Directory-joined session hosts for FSLogix profiles on Azure Files in Windows 10 and 11 multi-session is now in preview. We've updated Azure Files to use a Kerberos protocol for Azure Active Directory that lets you secure folders in the file share to individual users. This new feature also allows FSLogix to function within your deployment without an Active Directory Domain Controller. For more information, check out [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop-blog/announcing-public-preview-of-fslogix-profiles-for-azure-ad/ba-p/3019855).

### Azure Virtual Desktop pricing calculator updates

We've made some significant updates to improve the Azure Virtual Desktop pricing experience on the Azure pricing calculator, including the following:

- You can now calculate costs for any number of users greater than zero.
- The calculator now includes storage and networking or bandwidth costs.
- We've added new info messages for clarity.
- Fixed bugs that affected storage configuration.

For more information, see the [pricing calculator](https://azure.microsoft.com/pricing/calculator/).

## November 2021

Here's what changed in November 2021:

### Azure Virtual Desktop for Azure Stack HCI

Azure Virtual Desktop for Azure Stack HCI is now in preview. This feature is for customers who need desktop virtualization for apps that have to stay on-premises for performance and data security reasons. To learn more, see [our blog post](https://aka.ms/avd-ignite2021-blogpost) and [the Azure Virtual Desktop for Azure Stack HCI documentation](azure-stack-hci-overview).

### Autoscale preview

We're pleased to introduce the new autoscale feature, which lets you stop or start session hosts automatically based on a schedule you set. Autoscale lets you optimize infrastructure costs by configuring your shared or pooled desktops to only charge for the resources you actually use. You can learn more about the autoscale feature by reading [our documentation](autoscale-scaling-plan) and watching [our Azure Academy video](https://www.youtube.com/watch?v=JolOG7abfa4&amp;ab_channel=AzureAcademy).

### Azure Virtual Desktop starter kit for Power Automate

Your organization can now use the Azure Virtual Desktop starter kit to manage its robotic process automation (RPA) workloads. Learn more by reading [our documentation](/en-us/power-automate/desktop-flows/avd-overview).

### Tagging with Azure Virtual Desktop

We recently released new documentation about how to configure tags for Azure Virtual Desktop to track and manage costs. For more information, see [Tag Azure Virtual Desktop resources](tag-virtual-desktop-resources).

## October 2021

Here's what changed in October 2021:

### Azure Virtual Desktop support for Windows 11

Azure Virtual Desktop support for Windows 11 is now generally available for single and multi-session deployments. You can now use Windows 11 images when creating host pools in the Azure portal. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/windows-11-is-now-generally-available-on-azure-virtual-desktop/ba-p/2810545).

### RDP Shortpath now generally available

Remote Desktop Protocol (RDP) Shortpath for managed networks is now generally available. RDP Shortpath establishes a direct connection between the Remote Desktop client and the session host. This direct connection reduces dependency on gateways, improves the connection's reliability, and increases the bandwidth available for each user session. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/rdp-shortpath-for-managed-networks-is-generally-available/m-p/2861468).

### Screen capture protection updates

Screen capture protection is now supported on the macOS client and the Azure Government and Azure operated by 21Vianet clouds. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/screen-capture-protection-for-macos-client-and-support-for/m-p/2840089#M7940).

### Azure Active Directory domain join

Azure Active Directory domain join for Azure Virtual Desktop VMs is now available in the Azure Government and Azure operated by 21Vianet clouds. Microsoft Intune is currently only supported in the Azure Public cloud. Learn more at [Deploy Azure AD-joined virtual machines in Azure Virtual Desktop](deploy-azure-ad-joined-vm).

### Breaking change in Azure Virtual Desktop Azure Resource Manager template

A breaking change has been introduced into the Azure Resource Manager template for Azure Virtual Desktop. If you're using any code that depends on the change, then you need to follow the directions in [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/azure-virtual-desktop-arm-template-change-removal-of-script/m-p/2851538#M7971) to address the issue.

### Autoscale (preview) preview

Autoscale for Azure Virtual Desktop is now in preview. This feature natively turns your VMs in pooled host pools on or off based on availability needs. Scheduling when your VMs turn on and off optimizes deployment costs, and this feature also offers flexible scheduling options based on your needs. Once you've configured the required custom Role-Based Access Control (RBAC) role, you can start configuring your scaling plan. For more information, see [Autoscale (preview) for Azure Virtual Desktop host pools](autoscale-scaling-plan).

## September 2021

Here's what changed in September 2021.

### Azure portal updates

You can now use Azure Resource Manager templates for any update you want to apply to your session hosts after deployment. You can access this feature by selecting the **Virtual machines** tab while creating a host pool.

You can also now set host pool, application group, and workspace diagnostic settings while creating host pools instead of afterwards. Configuring these settings during the host pool creation process also automatically sets up reporting data for Azure Virtual Desktop Insights.

### Azure Active Directory domain join

Azure Active Directory domain join is now generally available. This service lets you join your session hosts to Azure Active Directory (Azure AD). Domain join also lets you autoenroll into Microsoft Intune. You can access this feature in the Azure public cloud, but not the Government cloud or Azure operated by 21Vianet. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-general-availability-of-azure-ad-joined-vms-support/ba-p/2751083).

### Azure operated by 21Vianet

Azure Virtual Desktop is now generally available in the Azure operated by 21Vianet cloud. For more information, see [our blog post](https://azure.microsoft.com/updates/general-availability-azure-virtual-desktop-is-now-available-in-the-azure-china-cloud/).

### Automatic migration module tool

With the automatic migration tool, you can move your organization from Azure Virtual Desktop (classic) to Azure Virtual Desktop with just a few PowerShell commands. This feature is currently in preview, and you can find out more at [Automatic migration](automatic-migration).

## August 2021

Here's what changed in August 2021:

### Windows 11 (Preview) for Azure Virtual Desktop

Windows 11 (Preview) images are now available in the Azure Marketplace for customers to test and validate with Azure Virtual Desktop. For more information, see [our announcement](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/windows-11-preview-is-now-available-on-azure-virtual-desktop/ba-p/2666468).

### Multimedia redirection is now in preview

Multimedia redirection gives you smooth video playback while watching videos in your Azure Virtual Desktop web browser and works with Microsoft Edge and Google Chrome. Learn more at [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/public-preview-announcing-public-preview-of-multimedia/m-p/2663244#M7692).

### Windows Defender Application Control and Azure Disk Encryption support

Azure Virtual Desktop now supports Windows Defender Application Control to control which drivers and applications are allowed to run on Windows VMs, and Azure Disk Encryption, which uses Windows BitLocker to provide volume encryption for the OS and data disks of your VMs. For more information, see [our announcement](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/support-for-windows-defender-application-control-and-azure-disk/m-p/2658633#M7685).

### Signing into Azure Active Directory using smart cards and Active Directory Federation Services is now supported in Azure Virtual Desktop

While this isn't a new feature for Azure Active Directory, Azure Virtual Desktop now supports configuring Active Directory Federation Services to sign in with smart cards. For more information, see [our announcement](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/signing-in-to-azure-ad-using-smart-cards-now-supported-in-azure/m-p/2654209#M7671).

### Screen capture protection is now generally available

Prevent sensitive information from being screen captured by software running on the client endpoints with screen capture protection in Azure Virtual Desktop. Learn more at our [blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-general-availability-of-screen-capture-protection-for/m-p/2699684).

## July 2021

Here's what changed in July 2021:

### Azure Virtual Desktop images now include optimized Teams

All available images in the Azure Virtual Desktop image gallery that include Microsoft 365 Apps for Enterprise now have the media-optimized version of Teams for Azure Virtual Desktop pre-installed. For more information, see [our announcement](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/media-optimization-for-microsoft-teams-now-part-of-win10/m-p/2550054#M7442).

### Azure Active Directory Domain Join for Session hosts is in preview

You can now join your Azure Virtual Desktop VMs directly to Azure Active Directory (Azure AD). This feature lets you connect to your VMs from any device with basic credentials. You can also automatically enroll your VMs with Microsoft Intune. For certain scenarios, this helps eliminate the need for a domain controller, reduce costs, and streamline your deployment. Learn more at [Deploy Azure AD joined virtual machines in Azure Virtual Desktop](deploy-azure-ad-joined-vm).

### FSLogix version 2105 is now available

FSLogix version 2105 is now generally available. This version includes improved sign-in times and bug fixes that weren't available in the preview version (version 2105). For more detailed information, you can see [the FSLogix release notes](/en-us/fslogix/whats-new) and [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-general-availability-of-fslogix-2105-2-9-7838-44263/m-p/2539491#M7412).

### Azure Virtual Desktop in China has entered preview

With Azure Virtual Desktop available in China, we now have more rounded global coverage that helps organizations support customers in this region with improved performance and latency. Learn more at [our announcement page](https://azure.microsoft.com/updates/azure-virtual-desktop-is-now-available-in-the-azure-china-cloud-in-preview/).

### The getting started feature for Azure Virtual Desktop

This feature offers a streamlined onboarding experience in the Azure portal to set up your Azure Virtual Desktop environment. You can use this feature to create deployments that meet system requirements for automated Azure Active Directory Domain Services the simple and easy way. For more information, check out our [blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/getting-started-wizard-in-azure-virtual-desktop/m-p/2451385).

### Start VM on connect is now generally available

The start VM on connect feature is now generally available. This feature helps you optimize costs by letting you turn off deallocated or stopped VMs, letting your deployment be flexible with user demands. For more information, see [Start Virtual Machine on Connect](start-virtual-machine-connect).

### RemoteApp streaming

We recently announced a new pricing option for RemoteApp streaming for using Azure Virtual Desktop to deliver apps as a service to your customers and business partners. For example, software vendors can use RemoteApp streaming to deliver apps as a software as a service (SaaS) solution that's accessible to their customers. To learn more about RemoteApp streaming, check out [our documentation](remote-app-streaming/overview).

### New Azure Virtual Desktop handbooks

We recently released four new handbooks to help you design and deploy Azure Virtual Desktop in different scenarios:

- [Application Management](https://azure.microsoft.com/resources/azure-virtual-desktop-handbook-application-management/) shows you how to modernize application delivery and simplify IT management.
- In [Disaster Recovery](https://azure.microsoft.com/resources/azure-virtual-desktop-handbook-disaster-recovery/), learn how to strengthen business resilience by developing a disaster recovery strategy.
- Get more value from Citrix investments with the [Citrix Cloud with Azure Virtual Desktop](https://azure.microsoft.com/resources/migration-guide-citrix-cloud-with-azure-virtual-desktop/) migration guide.
- Get more value from existing VMware investments with the [VMware Horizon with Azure Virtual Desktop](https://azure.microsoft.com/resources/migration-guide-vmware-horizon-cloud-and-azure-virtual-desktop/) migration guide.

## June 2021

Here's what changed in June 2021:

### Windows Virtual Desktop is now Azure Virtual Desktop

To better align with our vision of a flexible cloud desktop and application platform, we've renamed Windows Virtual Desktop to Azure Virtual Desktop. Learn more at [the announcement post in our blog](https://azure.microsoft.com/blog/azure-virtual-desktop-the-desktop-and-app-virtualization-platform-for-the-hybrid-workplace/).

### EU, UK, and Canada geographies are now generally available

Metadata service for the European Union, UK, and Canada is now in general availability. These new locations are very important to data sovereignty outside the US. For more information, see [our blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/announcing-public-preview-of-azure-virtual-desktop-service/m-p/2478401#M7314).

### The Getting Started tool is now in preview

We created the Azure Virtual Desktop Getting Started tool to make the deployment process easier for first-time users. By simplifying and automating the deployment process, we hope this tool helps make adopting Azure Virtual Desktop faster and more accessible to a wider variety of users. Learn more at our [blog post](https://techcommunity.microsoft.com/t5/azure-virtual-desktop/getting-started-wizard-in-azure-virtual-desktop/m-p/2451385).

### Azure Virtual Desktop pricing calculator updates

We've made some significant updates to improve the Azure Virtual Desktop pricing experience on the Azure pricing calculator, including the following:

- We've updated the service name to Azure Virtual Desktop
- We also updated the layout with the following new items:
    - A Storage section with both managed disk and file storage bandwidth
    - A custom section that shows cost-per-user

You can access the pricing calculator at [this page](https://azure.microsoft.com/pricing/calculator/).

### Single Sign-on (SSO) using Active Directory Federation Services (AD FS)

The AD FS single-sign on feature is now generally available. This feature lets customers use AD FS to give a single sign-on experience for users on the Windows and web clients. For more information, see [Configure AD FS single sign-on for Azure Virtual Desktop](configure-adfs-sso).

## May 2021

Here's what's new for May 2021:

### Smart card authentication

We've now officially released the Key Distribution Center (KDC) Proxy Remote Desktop Protocol (RDP) properties. These properties enable Kerberos authentication for the RDP portion of an Azure Virtual Desktop session, which includes permitting Network Level Authentication without a password. Learn more at our [blog post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/new-feature-smart-card-authentication-for-windows-virtual/m-p/2323226).

### The web client now supports file transfer

Starting with the preview version of the web client, version 1.0.24.7 (preview), users can now transfer files between their remote session and local computer. To upload files to the remote session, select the upload icon in the menu at the top of the web client page. To download files, search for **Remote Desktop Virtual Drive** in the Start menu on your remote session. After you've opened your virtual drive, just drag and drop your files into the Downloads folder and the browser will begin downloading the files to your local computer.

### Start VM on connect support updates

Start VM on connect (preview) now supports pooled host pools and the Azure Government Cloud. To learn more, read our [blog post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/leverage-start-vm-on-connect-for-pooled-host-pools-and-azure-gov/m-p/2349866).

### Latency improvements for the United Arab Emirates region

We've expanded our Azure control plane presence to the United Arab Emirates (UAE), so customers in that region can now experience improved latency. Learn more at our [Azure Virtual Desktop roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=Windows%20Virtual%20Desktop&amp;searchterms=64545).

### Ending Internet Explorer 11 support

On September 30, 2021, the Azure Virtual Desktop web client will no longer support Internet Explorer 11. We recommend you start using the [Microsoft Edge](https://www.microsoft.com/edge?form=MY01R2&amp;OCID=MY01R2&amp;r=1) browser for your web client and remote sessions instead. For more information, see the announcement in [this blog post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/windows-virtual-desktop-web-client-to-end-support-for-internet/m-p/2369007).

### Microsoft Intune preview

We've started the preview for Microsoft Intune support in Windows 10 Enterprise multi-session. Intune support lets you manage your Windows 10 VMs with the same tools as your local devices. Learn more at our [Microsoft Endpoint Manager documentation](/en-us/mem/intune/fundamentals/windows-virtual-desktop-multi-session).

### FSLogix version 2105 preview

We have released a preview of the latest version of the FSLogix agent. Check out our [blog post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/public-preview-fslogix-release-2105-is-now-available-in-public/m-p/2380996/thread-id/7105) for more information and to submit the form you need to access the preview.

### May 2021 updates for Teams for Azure Virtual Desktop

For this update, we resolved an issue that caused the screen to remain black while sharing video. We also fixed a mismatch in video resolutions between the session client and the Teams server. Teams on Azure Virtual Desktop should now change resolution and bit rates based on input from the Teams server.

### Azure portal deployment updates

We've made the following updates to the deployment process in the Azure portal:

- Added new images (including GEN2) to the drop-down list box of "image" when creating a new Azure Virtual Desktop session host VM.
- You can now configure boot diagnostics for virtual machines when creating a host pool.
- Added a tool tip to the RDP proxy in the advanced host pool RDP properties tab.
- Added an information bubble for the icon path when adding an application from an MSIX package.
- You can no longer do managed boot diagnostics with an unmanaged disk.
- Updated the template for creating a host pool in Azure Resource Manager so that the Azure portal can now support creating host pools with third-party marketplace images.

### Single sign-on using Active Directory Federation Services preview

We've started a preview for Active Directory Federation Services (AD FS) support for single sign-on (SSO) per host pool. Learn more at [Configure AD FS single sign-on for Azure Virtual Desktop](configure-adfs-sso).

### Enterprise-scale support

We've released an updated section of the Cloud Adoption framework for Enterprise-scale support for Azure Virtual Desktop. For more information, see [Enterprise-scale support for the Azure Virtual Desktop construction set](/en-us/azure/cloud-adoption-framework/scenarios/wvd/enterprise-scale-landing-zone).

### Customer adoption kit

We've recently released the Azure Virtual Desktop Customer adoption kit to help customers and partners set up Azure Virtual Desktop for their customers. You can download the kit [here](https://www.microsoft.com/azure/partners/resources/customer-adoption-kit-windows-virtual-desktop).

## April 2021

Here's what's new for April:

### Use the Start VM on Connect feature (preview) in the Azure portal

You can now configure Start VM on Connect (preview) in the Azure portal. With this update, users can access their VMs from the Android and macOS clients. To learn more, see [Start VM on Connect](start-virtual-machine-connect).

### Required URL Check tool

The Azure Virtual Desktop agent, version 1.0.2944.400 includes a tool that validates URLs and displays whether the virtual machine can access the URLs it needs to function. If any required URLs are accessible, the tool lists them so you can unblock them, if needed. Learn more at [Required URL Check tool](required-url-check-tool).

### Updates to the Azure portal UI for Azure Virtual Desktop

Here's what changed in the latest update of the Azure portal UI for Azure Virtual Desktop:

- Fixed an issue that caused an error to appear when retrieving the session host while drain mode is enabled.
- Upgraded the Portal SDK to version 7.161.0.
- Fixed an issue that caused the resource ID missing error message to appear in the User Sessions tab.
- The Azure portal now shows detailed sub-status messages for session hosts.

### April 2021 updates for Teams on Azure Virtual Desktop

Here's what's new for Teams on Azure Virtual Desktop:

- Added hardware acceleration for video processing of outgoing video streams for Windows 10-based clients.
- When joining a meeting with both a front facing camera and a rear facing or external camera, the front facing camera is selected by default.
- Resolved an issue that made Teams crash on x86-based machines.
- Resolved an issue that caused striations during screen sharing.
- Resolved an issue that prevented meeting members from seeing incoming video or screen sharing.

### MSIX App Attach is now generally available

MSIX App Attach for Azure Virtual Desktop has now come out of preview and is available to all users. Learn more about MSIX App Attach at [our TechCommunity announcement](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/msix-app-attach-is-now-generally-available/m-p/2270468).

### The macOS client now supports Apple Silicon and Big Sur

The macOS Azure Virtual Desktop client now supports Apple Silicon and Big Sur. The full list of updates is available in [What's new in the macOS client](/en-us/windows-server/remote/remote-desktop-services/clients/mac-whatsnew).

## March 2021

Here's what changed in March 2021.

### Updates to the Azure portal UI for Azure Virtual Desktop

We've made the following updates to Azure Virtual Desktop for the Azure portal:

- We've enabled new availability options (availability set and zones) for the workflows to create host pools and add VMs.
- We've fixed an issue where a host with the "Needs assistance" status appeared as unavailable. Now the host has a warning icon next to it.
- We've enabled sorting for active sessions.
- You can now send messages to or sign out specific users on the host details tab.
- We've changed the maximum session limit field.
- We've added an OU validation path to the workflow to create a host pool.
- You can now use the latest version of the Windows 10 image when you create a personal host pool.

### Generation 2 images and Trusted Launch

The Azure Marketplace now has Generation 2 images for Windows 10 Enterprise and Windows 10 Enterprise multi-session. These images enable you to use Trusted Launch VMs. Learn more about Generation 2 VMs at [Should I create a generation 1 or 2 virtual machine](/en-us/azure/virtual-machines/generation-2). To learn how to provision Azure Virtual Desktop Trusted Launch VMs, see [our TechCommunity post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/windows-virtual-desktop-support-for-trusted-launch/m-p/2206170).

### FSLogix is now preinstalled on Windows 10 Enterprise multi-session images

Based on customer feedback, we've released a new version of the Windows 10 Enterprise multi-session image that has an unconfigured version of FSLogix already installed. We hope this makes your Azure Virtual Desktop deployment easier.

### Azure Virtual Desktop Insights is now in General Availability

Azure Virtual Desktop Insights is now generally available to the public. This feature is an automated service that monitors your deployments and lets you view events, health, and troubleshooting suggestions in a single place. For more information, see [our documentation](insights) or check out [our TechCommunity post](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/azure-monitor-for-windows-virtual-desktop-is-generally-available/m-p/2242861).

### March 2021 updates for Teams on Azure Virtual Desktop

We've made the following updates for Teams on Azure Virtual Desktop:

- We've improved video quality performance on calls and 2x2 mode.
- We've reduced CPU utilization by 5-10% (depending on CPU generation) by using hardware offload of video processing (XVP).
- Older machines can now use XVP and hardware decoding to display more incoming video streams smoothly in 2x2 mode.
- We've updated the WebRTC stack from M74 to M88 for better AV sync performance and fewer transient issues.
- We've replaced our software H264 encoder with OpenH264 (OSS used in Teams on the web), which increased the video quality of the outgoing camera.
- We enabled 2x2 mode for Teams Server for the general public on March 30. 2x2 mode shows up to four incoming video streams at the same time.

### Start VM on Connect preview

The new host pool setting, Start VM on Connect, is now available in preview. This setting lets you turn on your VMs whenever you need them. If you want to save costs, you need to deallocate your VMs by configuring your Azure Compute settings. For more information, check out [our blog post](https://aka.ms/wvdstartvmonconnect) and [our documentation](start-virtual-machine-connect).

### Azure Virtual Desktop Specialty certification

We've released a beta version of the AZ-140 exam that will let you prove your expertise in Azure Virtual Desktop in Azure. To learn more, check out [our TechCommunity post](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/beta-exam-prove-your-expertise-in-windows-virtual-desktop-on/ba-p/2147107).

## February 2021

Here's what changed in February 2021.

### Portal experience

We've improved the Azure portal experience in the following ways:

- Bulk drain mode on hosts in the session host grid tab.
- MSIX App Attach is now available for preview.
- Fixed host pool overview info for dark mode.

### EU metadata storage now in preview

We're now hosting a preview of the Europe (EU) geography as a storage option for service metadata in Azure Virtual Desktop. Customers can choose between West or North Europe when they create their service objects. The service objects and metadata for the host pools will be stored in the Azure geography associated with each region. To learn more, read [our blog post announcing the preview](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/announcing-public-preview-of-windows-virtual-desktop-service/m-p/2143939).

### Teams on Azure Virtual Desktop plugin updates

We've improved video call quality on the Azure Virtual Desktop plugin by addressing the most commonly reported issues, such as when the screen would suddenly go dark or the video and sound desynchronized. These improvements should increase the performance of single-video view with active speaker switching. We also fixed an issue where hardware devices with special characters weren't available in Teams.

## January 2021

Here's what changed in January 2021:

### New Azure Virtual Desktop offer

New customers save 30 percent on Azure Virtual Desktop computing costs for D-series and Bs-series virtual machines for up to 90 days when using the native Microsoft solution. You can redeem this offer in the Azure portal before March 31, 2021. Learn more at our [Azure Virtual Desktop offer page](https://azure.microsoft.com/services/virtual-desktop/offer/).

### networkSecurityGroupRules value change

In the Azure Resource Manager nested template, we changed the default value for `networkSecurityGroupRules` from an object to an array. This prevents errors if you use `managedDisks-customimagevm.json` without specifying a value for `networkSecurityGroupRules`. This wasn't a breaking change and is backward compatible.

### FSLogix hotfix update

We’ve released FSLogix, version 2009 HF\_01 (2.9.7654.46150) to solve issues in the previous release (2.9.7621.30127). We recommend you stop using the previous version and update FSLogix as soon as possible.

For more information, see the release notes in [What's new in FSLogix](/en-us/fslogix/whats-new#fslogix-apps-2009-hf_01-29765446150).

### Azure portal experience improvements

We've made the following improvements to the Azure portal experience:

- You can now add local VM admin credentials directly instead of having to add a local account created with the Active Directory domain join account credentials.
- Users can now list both individual and group assignments in separate tabs for individual users and groups.
- The version number of the Azure Virtual Desktop Agent is now visible in the Virtual Machine overview for host pools.
- Added bulk delete for host pools and application groups.
- You can now enable or disable drain mode for multiple session hosts in a host pool.
- Removed the public IP field from the VM details page.

### Azure Virtual Desktop Agent troubleshooting

We recently set up the [Azure Virtual Desktop Agent troubleshooting guide](/en-us/troubleshoot/azure/virtual-desktop/troubleshoot-agent) to help customers who have encountered common issues.

### Microsoft Defender for Endpoint integration

Microsoft Defender for Endpoint integration is now generally available. This feature gives your Azure Virtual Desktop VMs the same investigation experience as a local Windows 10 machine. If you're using Windows 10 Enterprise multi-session, Microsoft Defender for Endpoint supports up to 50 concurrent user connections, giving you the cost savings of Windows 10 Enterprise multi-session and the confidence of Microsoft Defender for Endpoint. For more information, check out our [blog post](https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/windows-virtual-desktop-support-is-now-generally-available/ba-p/2103712).

### Azure Security baseline for Azure Virtual Desktop

We've recently published [an article about the Azure security baseline](/en-us/security/benchmark/azure/baselines/azure-virtual-desktop-security-baseline) for Azure Virtual Desktop that we'd like to call your attention to. These guidelines include information about how to apply the Microsoft cloud security benchmark to Azure Virtual Desktop. The Microsoft cloud security benchmark describes the settings and practices we recommend you use to secure your cloud solutions on Azure.

## December 2020

Here's what changed in December 2020:

### Azure Virtual Desktop Insights

The preview for Azure Virtual Desktop Insights is now available. This new feature includes a robust dashboard built on top of Azure Monitor Workbooks to help IT professionals understand their Azure Virtual Desktop environments. Check out [the announcement on our blog](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/azure-monitor-for-windows-virtual-desktop-public-preview/m-p/1946587) for more details.

### Azure Resource Manager template change

In the latest update, we've removed all public IP address parameter from the Azure Resource Manager template for creating and provisioning host pools. We highly recommend you avoid using public IPs for Azure Virtual Desktop to keep your deployment secure. If your deployment relied on public IPs, you need to reconfigure it to use private IPs instead, otherwise your deployment won't work properly.

### MSIX App Attach preview

MSIX App Attach is another service that began its preview this month. MSIX App Attach is a service that dynamically presents MSIX applications to your Azure Virtual Desktop Session host VMs. Check out [the announcement on our blog](https://techcommunity.microsoft.com/t5/windows-virtual-desktop/msix-app-attach-azure-portal-integration-public-preview/m-p/1986231) for more details.

### Screen capture protection

This month also marked the beginning of the preview for screen capture protection. You can use this feature to prevent sensitive information from being captured on the client endpoints. Give screen capture protection a try by going to [this page](https://aka.ms/WVDScreenCaptureProtection).

### Built-in roles

We've added new built-in roles for Azure Virtual Desktop for admin permissions. For more information, see [Built-in roles for Azure Virtual Desktop](rbac).

### Application group limit increase

We've increased the default application group limit per Azure Active Directory tenant to 200 groups.

## November 2020

### Azure portal experience

We've fixed two bugs in the Azure portal user experience:

- The Desktop application friendly name is no longer overwritten on the "Add VM" workflow.
- The session host tab will now load if session hosts are part of scale sets.

### FSLogix client, version 2009

We've released a new version of the FSLogix client with many fixes and improvements. Learn more at [our blog post](https://social.msdn.microsoft.com/Forums/defe5828-fba4-4715-a68c-0e4d83eefa6b/release-notes-for-fslogix-apps-release-2009-29762130127?forum=FSLogix).

### RDP Shortpath preview

RDP Shortpath introduces direct connectivity to your Azure Virtual Desktop session host using point-to-site and site-to-site VPNs and ExpressRoute. It also introduces the URCP transport protocol. RDP Shortpath is designed to reduce latency and network hops in order to improve user experience. Learn more at [Azure Virtual Desktop RDP Shortpath](shortpath).

### Az.DesktopVirtualization, version 2.0.1

We've released version 2.0.1 of the Azure Virtual Desktop cmdlets. This update includes cmdlets that let you manage MSIX App Attach. You can download the new version at [the PowerShell gallery](https://www.powershellgallery.com/packages/Az.DesktopVirtualization/2.0.1).

### Azure Advisor updates

Azure Advisor now has a new recommendation for proximity guidance in Azure Virtual Desktop, and a new recommendation for optimizing performance in depth-first load balanced host pools. Learn more at [the Azure website](https://azure.microsoft.com/updates/new-recommendations-from-azure-advisor/).

## October 2020

Here's what changed in October 2020:

### Improved performance

We've optimized performance by reducing connection latency in the following Azure geographies:

- Switzerland
- Canada

### Azure Government Cloud availability

The Azure Government Cloud is now generally available. Learn more at [our blog post](https://azure.microsoft.com/updates/windows-virtual-desktop-is-now-generally-available-in-the-azure-government-cloud/).

### Azure Virtual Desktop Azure portal updates

We've made some updates to the Azure Virtual Desktop Azure portal:

- Fixed a resourceID error that prevented users from opening the "Sessions" tab.
- Streamlined the UI on the "Session hosts" tab.
- Fixed the "Defaults," "Usability," and "Restore defaults" settings under RDP properties.
- Made "Remove" and "Delete" functions consistent across all tabs.
- The portal now validates app names in the "Add an app" workflow.
- Fixed an issue where the session host export data wasn't aligned in the columns.
- Fixed an issue where the portal couldn't retrieve user sessions.
- Fixed an issue in session host retrieval that happened when the virtual machine was created in a different resource group.
- Updated the "Session host" tab to list both active and disconnected sessions.
- The "Applications" tab now has pages.
- Fixed an issue where the "requires command line" text didn't display correctly in the "Application list" tab.
- Fixed an issue when the portal couldn't deploy host pools or virtual machines while using the German-language version of the Shared Image Gallery.

## September 2020

Here's what changed in September 2020:

- We've optimized performance by reducing connection latency in the following Azure geographies:

    - Germany
    - South Africa (for validation environments only)
- We released version 1.2.1364 of the Windows Desktop client for Azure Virtual Desktop. In this update, we made the following changes:

    - Fixed an issue where single sign-on (SSO) didn't work on Windows 7.
    - Fixed an issue that caused the client to disconnect when a user who enabled media optimization for Teams tried to call or join a Teams meeting while another app had an audio stream open in exclusive mode.
    - Fixed an issue where Teams didn't enumerate audio or video devices when media optimization for Teams was enabled.
    - Added a "Need help with settings?" link to the desktop settings page.
    - Fixed an issue with the "Subscribe" button that happened when using high-contrast dark themes.
- Thanks to the tremendous help from our users, we've fixed two critical issues for the Microsoft Store Remote Desktop client. We continue to review feedback and fix issues as we broaden our phased release of the client to more users worldwide.
- We've added a new feature that lets you change VM location, image, resource group, prefix name, network config as part of the workflow for adding a VM to your deployment in the Azure portal.
- IT Pros can now manage hybrid Azure Active Directory-joined Windows 10 Enterprise VMs using Microsoft Intune. To learn more, see [our blog post](https://techcommunity.microsoft.com/t5/microsoft-endpoint-manager-blog/microsoft-endpoint-manager-announces-support-for-windows-virtual/ba-p/1681048).

## August 2020

Here's what changed in August 2020:

- We've improved performance to reduce connection latency in the following Azure regions:

    - United Kingdom
    - France
    - Norway
    - South Korea
- The Microsoft Store Remote Desktop Client is now generally available. This version of the Microsoft Store Remote Desktop Client is compatible with Azure Virtual Desktop. We've also introduced refreshed UI flows for improved user experiences. This update includes fluent design, light and dark modes, and many other exciting changes. We've also rewritten the client to use the same underlying remote desktop protocol (RDP) engine as the iOS, macOS, and Android clients. This lets us deliver new features at a faster rate across all platforms. [Download the client](https://www.microsoft.com/p/microsoft-remote-desktop/9wzdncrfj3ps?rtc=1&amp;activetab=pivot:overviewtab).
- We fixed an issue in the Teams Desktop client (version 1.3.00.21759) where the client only showed the UTC time zone in the chat, channels, and calendar. The updated client now shows the remote session's time zone instead.
- Azure Advisor is now a part of Azure Virtual Desktop. When you access Azure Virtual Desktop through the Azure portal, you can see recommendations for optimizing your Azure Virtual Desktop environment. Learn more at [Introduction to Azure Advisor](/en-us/azure/advisor/advisor-overview).
- Azure CLI now supports Azure Virtual Desktop (`az desktopvirtualization`) to help you automate your Azure Virtual Desktop deployments. Check out [desktopvirtualization](/en-us/cli/azure/desktopvirtualization) for a list of extension commands.
- We've updated our deployment templates to make them fully compatible with the Azure Virtual Desktop Azure Resource Manager interfaces. You can find the templates on [GitHub](https://github.com/Azure/RDS-Templates/tree/master/ARM-wvd-templates).
- The Azure Virtual Desktop US Gov portal is now in preview. To learn more, see [our announcement](https://azure.microsoft.com/updates/windows-virtual-desktop-is-now-available-in-the-azure-government-cloud-in-preview/).

## July 2020

July was when Azure Virtual Desktop with Azure Resource Management integration became generally available.

Here's what changed with this new release:

- The *Fall 2019 release* is now known as *Azure Virtual Desktop (classic)*, while the *Spring 2020 release* is now just *Azure Virtual Desktop*. For more information, check out [this blog post](https://azure.microsoft.com/blog/new-windows-virtual-desktop-capabilities-now-generally-available/).

To learn more about new features, check out [this blog post](https://techcommunity.microsoft.com/t5/itops-talk-blog/windows-virtual-desktop-spring-update-enters-public-preview/ba-p/1340245).

### Autoscaling tool update

The latest version of the autoscaling tool that was in preview is now generally available. This tool uses an Azure Automation account and the Azure Logic App to automatically shut down and restart session host VMs within a host pool, reducing infrastructure costs. Learn more at [Scale session hosts using Azure Automation](set-up-scaling-script).

### Azure portal

You can now do the following things with the Azure portal in Azure Virtual Desktop:

- Directly assign users to personal desktop session hosts
- Change the validation environment setting for host pools

### Diagnostics

We've released some new prebuilt queries for the Log Analytics workspace. To access the queries, go to **Logs** and under **Category**, select **Azure Virtual Desktop**. Learn more at [Use Log Analytics for the diagnostics feature](diagnostics-log-analytics).

### Update for Remote Desktop client for Android

The [Remote Desktop client for Android](https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx) now supports Azure Virtual Desktop connections. Starting with version 10.0.7, the Android client features a new UI for improved user experience. The client also integrates with Microsoft Authenticator on Android devices to enable conditional access when subscribing to Azure Virtual Desktop workspaces.

The previous version of Remote Desktop client is now called “Remote Desktop 8." Any existing connections you have in the earlier version of the client will be transferred seamlessly to the new client. The new client has been rewritten to the same underlying RDP core engine as the iOS and macOS clients, faster release of new features across all platforms.

### Teams update

We've made improvements to Microsoft Teams for Azure Virtual Desktop. Most importantly, Azure Virtual Desktop now supports audio and video optimization for the Windows Desktop client. Redirection improves latency by creating direct paths between users when they use audio or video in calls and meetings. Less distance means fewer hops, which makes calls look and sound smoother. Learn more at [Use Teams on Azure Virtual Desktop](teams-on-avd).

## June 2020

Last month, we introduced Azure Virtual Desktop with Azure Resource Manager integration in preview. This update has lots of exciting new features we'd love to tell you about. Here's what's new for this version of Azure Virtual Desktop.

### Azure Virtual Desktop is now integrated with Azure Resource Manager

Azure Virtual Desktop is now integrated into Azure Resource Manager. In the latest update, all Azure Virtual Desktop objects are now Azure Resource Manager resources. This update is also integrated with Azure role-based access control (Azure RBAC). See [What is Azure Resource Manager?](/en-us/azure/azure-resource-manager/management/overview) to learn more.

Here's what this change does for you:

- Azure Virtual Desktop is now integrated with the Azure portal. This means you can manage everything directly in the portal, no PowerShell, web apps, or third-party tools required. To get started, check out our tutorial at [Create a host pool with the Azure portal](create-host-pools-azure-marketplace).
- Before this update, you could only publish desktops and applications to individual users. With Azure Resource Manager, you can now publish resources to Azure Active Directory groups.
- The earlier version of Azure Virtual Desktop had four built-in admin roles that you could assign to a tenant or host pool. These roles are now in [Azure role-based access control (Azure RBAC)](/en-us/azure/role-based-access-control/overview). You can apply these roles to every Azure Virtual Desktop Azure Resource Manager object, which lets you have a full, rich delegation model.
- In this update, you no longer need to run Azure Marketplace or the GitHub template repeatedly to expand a host pool. All you need to expand a host pool is to go to your host pool in the Azure portal and select **+ Add** to deploy additional session hosts.
- Host pool deployment is now fully integrated with the [Azure Shared Image Gallery](/en-us/azure/virtual-machines/shared-image-galleries). Shared Image Gallery is a separate Azure service that stores VM image definitions, including image versioning. You can also use global replication to copy and send your images to other Azure regions for local deployment.
- Monitoring functions that used to be done through PowerShell or the Diagnostics Service web app have now moved to Log Analytics in the Azure portal. You also now have two options to visualize your reports. You can run Kusto queries and use Workbooks to create visual reports.
- You're no longer required to complete Azure Active Directory consent to use Azure Virtual Desktop. In this update, the Azure Active Directory tenant on your Azure subscription authenticates your users and provides Azure RBAC controls for your admins.

### PowerShell support

We've added new AzWvd cmdlets to the Azure Az PowerShell module with this update. This new module is supported in PowerShell Core, which runs on .NET Core.

To install the module, follow the instructions in [Set up the PowerShell module for Azure Virtual Desktop](powershell-module).

You can also see a list of available commands at the [AzWvd PowerShell reference](/en-us/powershell/module/az.desktopvirtualization/#desktopvirtualization).

For more information about the new features, check out [our blog post](https://techcommunity.microsoft.com/t5/itops-talk-blog/windows-virtual-desktop-spring-update-enters-public-preview/ba-p/1340245).

### Additional gateways

We've added a new gateway cluster in South Africa to reduce connection latency.

### Microsoft Teams on Azure Virtual Desktop (Preview)

We've made some improvements to Microsoft Teams for Azure Virtual Desktop. Most importantly, Azure Virtual Desktop now supports audio and visual redirection for calls. Redirection improves latency by creating direct paths between users when they call using audio or video. Less distance means fewer hops, which makes calls look and sound smoother.

To learn more, see [our blog post](https://azure.microsoft.com/updates/windows-virtual-desktop-media-optimization-for-microsoft-teams-is-now-available-in-public-preview/).