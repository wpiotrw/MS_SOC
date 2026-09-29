---
layout: Conceptual
title: What's new in Windows 365 Enterprise | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/whats-new
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Find out what's new in Windows 365 Enterprise
keywords: 
author: hinallur
ms.author: hinallur
manager: bobroudebush
ms.date: 2026-09-24T00:00:00.0000000Z
ms.topic: whats-new
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: traceyadams
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 0cdc4d57-0856-07b5-1a8b-dc34bad8553a
document_version_independent_id: 0cdc4d57-0856-07b5-1a8b-dc34bad8553a
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/whats-new.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/whats-new
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/whats-new.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 848ba603-86e5-cb96-b12c-6327db16447e
---

# What's new in Windows 365 Enterprise | Microsoft Learn

Learn what new features are available in Windows 365 Enterprise and Windows 365 Flex.

Note

Each monthly update may roll out over several weeks and might not be immediately available to all customers.

For information about Windows App and its features, see [What's new in Windows App](/en-us/windows-app/whats-new?tabs=windows).

For more information about public preview items, see [Public preview in Windows 365](../public-preview).

## Week of September 28, 2026

### Bulk deprovision Cloud PCs in grace period is generally available

Bulk deprovisioning for Windows 365 Enterprise and Windows 365 Flex dedicated Cloud PCs in grace period is now generally available. Administrators can deprovision multiple eligible Cloud PCs at once rather than waiting for the seven-day grace period to expire, simplifying management when multiple Cloud PCs need to be removed. The current documentation describes bulk deprovisioning through the provisioning policy view and the Intune Bulk Action Wizard. For more information, see [End grace period for Cloud PCs in Windows 365](/en-us/windows-365/enterprise/end-grace-period).

## Week of September 21, 2026

### Developer Configuration with pre-installed Microsoft 365 Apps is generally available

This image provides a consistent, ready-to-use developer environment by preinstalling essential development tools and applying the required configurations across Windows 365 CPC. This image is available for Windows 365 Enterprise and Windows 365 Flex Dedicated mode. See more: [Device images in Windows 365](/en-us/windows-365/enterprise/device-images).

### Alternate regions for Business Continuity and Disaster Recovery are now generally available

Alternate regions are generally available for Business Continuity and Disaster Recovery (BCDR) scenarios. These regions help organizations meet unique disaster recovery and data sovereignty requirements. Administrators can select alternate regions for Cross-region Disaster Recovery (CRDR) and Disaster Recovery Plus (DR+) configurations, including Australia Southeast, South India, Canada East, and West US. Alternate regions are available for disaster recovery scenarios only and aren't supported for Cloud PC provisioning.

For more information about alternate regions, see [Requirements for Windows 365](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2Cent)

### Business Continuity and Disaster Recovery in Cloud PC Settings is now generally available

The setup process for Point-in-Time Restore, Cross-region Disaster Recovery, and Disaster Recovery Plus is now generally available within Cloud PC Settings. This aligns with the centralized approach that Cloud PC Settings offers. These features can now be enabled together within a singular Cloud PC Configuration.

For more information, see [Enable Business Continuity and Disaster Recovery](/en-us/windows-365/enterprise/business-continuity-disaster-recovery-setup)

### Session State Retention for Windows 365 Flex dedicated Cloud PCs (Public Preview)

Session State Retention is now available in public preview for eligible Windows 365 Flex dedicated Cloud PCs. Session State Retention complements Intelligent pre-start to improve the reconnect experience for Windows 365 Flex dedicated users. Intelligent pre-start helps ensure the Cloud PC is powered on and ready when the user needs it, while Session State Retention preserves the user’s active session while the Cloud PC is idle. After a user has been disconnected for a set idle period (default: 2 hours), an eligible Cloud PC preserves the session state instead of powering off. On the next connection, users return to their open apps and work exactly where they left off.

Both capabilities are quality-of-life improvements delivered as part of the Windows 365 service. Together, they enhance the end-user experience by moving reconnect toward a model in which device readiness and session continuity are invisible to users and happen behind the scenes, without requiring users to change how they work or manage either capability.

For more information, see [State retention for Windows 365 Flex dedicated Cloud PCs](introduction-windows-365-flex#session-state-retention-for-windows-365-flex-dedicated-cloud-pcs-preview).

## Week of September 14, 2026

### Use TWAIN scanners in remote sessions (Public Preview)

TWAIN scanner redirection is now available in public preview for Windows 365. It enables supported scanners connected to a local Windows device to be redirected to a Cloud PC using high-level redirection, providing an optimized scanning experience compared to USB redirection. For more information, see [Configure scanner redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-scanners?pivots=windows-365).

### iOS preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on iOS. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the iOS device or that are connected to the iOS device (such as a physical security key or through QR code).

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

### iOS preview support for external identities

External identity support is in preview for the Windows App on iOS. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](identity-authentication#external-identity).

### macOS support for external identities is now generally available

External identity support is now generally available for the Windows App on macOS. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](identity-authentication#external-identity).

### User provisioning for Windows 365 Reserve (Generally Available)

User provisioning for Windows 365 Reserve is now generally available. When enabled by IT, eligible users can initiate Cloud PC provisioning directly from Windows App, helping them quickly access a Reserve Cloud PC without waiting for an administrator to provision it. Administrators control availability through Windows App settings for Windows 365 in Microsoft Intune and can scope the capability to specific Microsoft Entra ID user groups. For more information, see [Managing Windows 365 Reserve](windows-365-reserve-manage).

### RDP Shortpath for public networks and RDP Multipath with UDP support in Windows App for macOS Beta

RDP Shortpath for public networks and RDP Multipath with UDP are now available in Windows App for macOS Beta, [version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test), for Azure Virtual Desktop and Windows 365. This update enables UDP-based connectivity over RDP Shortpath and extends RDP Multipath resiliency to macOS, helping provide a more reliable and consistent connection experience across changing network conditions.

### RDP Multipath availability in Azure Government

RDP Multipath with redundant UDP transport paths is generally available for Windows 365 in Azure Government. The phased GA rollout of redundant TCP transport paths has also started, further improving connection resiliency by providing additional transport paths when network conditions change.

For more information, see [RDP Multipath](rdp-multipath).

### RDP Shortpath with TURN availability in Azure Government

The phased GA rollout of RDP Shortpath via TURN has started for Windows 365 in Azure Government. TURN provides relayed UDP connectivity when a direct connection can't be established. Azure Government uses the new dedicated 20.140.236.0/22 IP range for STUN and TURN connectivity.

## Week of September 7, 2026

### Admin Insights for Windows 365 is generally available

Admin Insights for Windows 365 is now generally available. The experience gives IT administrators a prioritized view of important signals across their Cloud PC environment, helping them quickly identify where attention may be needed. Administrators can review relevant insights directly within the Windows 365 experience and open associated reports or devices views for more information.

For more information, see [Admin Insights for Windows 365](/en-us/windows-365/enterprise/admin-insights).

### Enable local admin setting in Cloud PC configurations now in Public Preview

The existing **Enable local admin** setting can now be configured through **Devices &gt; Cloud PC Settings &gt; Create &gt; Cloud PC configurations** in Intune. This setting allows IT admins to grant users local administrator permissions on their Cloud PCs.

To learn more, see [Cloud PC configurations](/en-us/windows-365/enterprise/cloud-pc-configurations).

### Display Protection for Windows 365 (Public Preview)

Display Protection for Windows 365 is now available in public preview. Display Protection helps protect sensitive content displayed during Cloud PC sessions by securing the display path between the Cloud PC and supported endpoint devices. Administrators can configure the level of display protection in Microsoft Intune. For more information, see [Display Protection for Windows 365 and Azure Virtual Desktop](/en-us/windows-365/enterprise/windows-cloud-display-protection).

### Cloud PC recovery is now available for Windows 365 Government

Cloud PC recovery is now generally available for Windows 365 Enterprise in GCC and GCCH. Administrators can recover eligible Cloud PCs that were deprovisioned after a license expired by reprovisioning the Cloud PC and using the restore action, extending the recovery capability previously released for commercial environments. For more information, see [Overview of restoring a Cloud PC to a previous state with Windows 365 Enterprise](/en-us/windows-365/enterprise/restore-overview#recovering-cloud-pcs-deprovisioned-due-to-license-expiration).

## Week of August 31, 2026

### Add Cloud Apps from file path is now generally available.

Windows 365 administrators can add Cloud Apps by specifying a file path, expanding the applications available on Windows 365 Flex shared Cloud PCs. Administrators can define custom app properties and configure command-line parameters for applications that require manual configuration. For more information, see [Windows 365 Cloud Apps](/en-us/windows-365/enterprise/cloud-apps).

### Autopilot Device Preparation support for Citrix Cloud PCs

Autopilot Device Preparation (DPP) support for Citrix Cloud PCs is now generally available for Windows 365 Government. Administrators can use device preparation policies with Citrix Cloud PCs to help ensure required apps and scripts are installed during provisioning before the Cloud PC is ready for use.

## Week of August 24, 2026

### Bulk provisioning and deprovisioning for Windows 365 Reserve supports up to 1,000 devices (Public Preview)

Windows 365 Reserve now supports bulk provisioning and deprovisioning of up to 1,000 Cloud PCs in a single request. Admins can provision and deprovision larger groups of Reserve Cloud PCs at once, reducing the need to split large-scale provisioning operations into smaller batches.

For more information, see [Managing Windows 365 Reserve](/en-us/windows-365/enterprise/windows-365-reserve-manage).

### Autopilot Device Preparation for Windows 365 Reserve is now generally available.

Administrators can assign Device Preparation policies to Windows 365 Reserve provisioning policies in Microsoft Intune so required applications and configurations are applied during provisioning before users connect to their Cloud PCs. Cloud PCs show a Preparing status while setup is in progress. For more information, see [Managing Windows 365 Reserve](/en-us/windows-365/enterprise/windows-365-reserve-manage).

### Developer Configuration image adds M365 Apps (Public Preview)

The Windows 11 Enterprise Developer Configuration image now also includes M365 Apps. For more information, see [Device images in Windows 365](device-images).

## Week of August 10, 2026

### Autopilot Device Preparation support for Windows 365 Government

Autopilot Device Preparation is now generally available for Windows 365 Enterprise and Windows 365 Flex in dedicated mode in Government environments. IT administrators can use device preparation policies to help ensure required Intune apps and scripts are applied to Cloud PCs during provisioning before they're made available to users. For more information, see [Use Autopilot device preparation with Cloud PCs](/en-us/windows-365/enterprise/autopilot-device-preparation).

### Developer Configuration image adds Intelligent Terminal and Coreutils (Public Preview)

The Windows 11 Enterprise Developer Configuration gallery image now includes Intelligent Terminal and Coreutils, providing developers with additional built-in tools as part of the preconfigured development environment available in Windows 365. For more information, see [Device images in Windows 365](device-images).

### macOS preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on macOS. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the macOS device or that are connected to the macOS device (such as a physical security key or through QR code).

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

### Modern Auto-Reconnect begins rollout

Windows 365 has started the rollout of Modern Auto-Reconnect, a new connection recovery experience designed to improve resiliency during temporary network interruptions.

Modern Auto-Reconnect helps users stay productive by preserving their Cloud PC connection experience and restoring connectivity more quickly when network connectivity returns. Instead of relying on repeated reconnect attempts, the feature leverages RDP Multipath to maintain connection continuity and reduce disruptions caused by brief network outages, changes in network conditions, or transitions between networks.

Users can benefit from:

- Faster recovery after temporary network interruptions
- Reduced user-visible disruptions during connectivity changes
- Preservation of open applications and in-progress work
- A more seamless experience when switching between networks or recovering from brief connectivity drops

This feature is being introduced through a quality-driven, phased rollout, helping ensure a smooth and reliable experience as availability expands across Windows 365. Until rollout is complete, the feature might not be available on all eligible Cloud PCs.

For more information, see [here](fast-reconnect).

## Week of Aug 3, 2026

### Customer-managed encryption for Windows 365 Reserve (GA)

Microsoft Purview Customer Key (CMK) support for Windows 365 Reserve is now generally available. Administrators can encrypt Reserve Cloud PC disks with customer-managed keys stored in Azure Key Vault, providing greater control over encryption key management, including key rotation and revocation. This capability extends the existing Customer Key experience for Windows 365 Cloud PCs to Windows 365 Reserve. For more information, see [Microsoft Purview Customer Key setup and support for W365](/en-us/windows-365/enterprise/purview-customer-key).

### Screen Capture Protection for web connections is now available

Screen Capture Protection is now available when accessing Windows 365 Cloud PCs from supported web browsers. This capability helps protect sensitive information by preventing screen content from being captured during remote sessions, enhancing security across more connection experiences. For more information, see [Enable screen capture protection in Windows 365](/en-us/azure/virtual-desktop/screen-capture-protection?context=%2fwindows-365%2fcontext%2fpr-context&amp;tabs=intune).

## Week of July 27, 2026

### Default display settings for Cloud PCs (Public Preview)

IT administrators can now configure the default display setting for Windows 365 Cloud PCs as either a single display or all displays. Users can override the default with their own display preferences in Windows App. For more information, see [Remote connection experience](/en-us/windows-365/enterprise/remote-connection-experience).

### Autopilot Device Preparation for Citrix Cloud PCs is now available

Windows Autopilot Device Preparation (DPP) is now supported for Cloud PCs with Citrix integration. This brings the Citrix Cloud PC provisioning experience in line with other supported Windows 365 deployment scenarios and helps make sure the required applications and scripts are installed before users access their Cloud PCs. Administrators can now include device preparation policies for Citrix Cloud PCs in their provisioning workflow.

### Bulk deprovision for Cloud PCs in grace period (Public Preview)

Bulk deprovision for Cloud PCs in grace period is now available in Public Preview for Windows 365 Enterprise and Windows 365 Frontline Dedicated. Administrators can deprovision multiple Cloud PCs at once from the Windows 365 admin experience instead of waiting for the seven-day grace period to expire or ending the grace period one Cloud PC at a time. This update streamlines Cloud PC lifecycle management and helps administrators quickly remove Cloud PCs that are no longer needed. For more information, see [Deprovision or end grace period for Cloud PCs](/en-us/windows-365/enterprise/end-grace-period).

### PowerShell execution policy hardening for Cloud PC provisioning

Windows 365 now sets the PowerShell execution policy to `RemoteSigned` at the `LocalMachine` scope during Cloud PC provisioning. This change improves security by requiring downloaded scripts to be digitally signed, while allowing locally created scripts and Custom Script Extension (CSE) scripts to run without signatures. This setting applies to all Cloud PC products.

If your organization sets the PowerShell execution policy to `AllSigned` through Intune or Group Policy, provisioning and other CSE-based operations can fail. For more information, see [Automated provisioning steps](automated-provisioning-steps) and [Known issues](known-issues-enterprise#windows-365-provisioning-fails).

### Android support for external identities is now generally available

External identity support is now generally available for the Windows App on Android. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](identity-authentication#external-identity).

### Android preview support for in-session passwordless authentication

In-session passwordless authentication is in preview for the Windows App on Android. This allows users to complete in-session WebAuthn challenges using passkeys that are stored on the Android device through a (software-based) passkey provider like Microsoft Authenticator. Using passkeys from other devices (such as a physical security key or through QR code) is not supported.

For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirections).

## Week of July 20, 2026

### Alternate regions for Business Continuity and Disaster Recovery in Public Preview

Windows 365 now supports alternate Azure regions for Business Continuity and Disaster Recovery (BCDR) scenarios, helping organizations meet disaster recovery and data sovereignty requirements in geographies where only one Windows 365-supported region is available. Administrators can select alternate regions for **Cross-region Disaster Recovery (CRDR)** and **Disaster Recovery Plus (DR+)** configurations, including **Australia Southeast**, and **South India**. Alternate regions are available for disaster recovery scenarios only and aren't supported for Cloud PC provisioning.

For more information about alternate regions, see [Requirements for Windows 365](/en-us/windows-365/enterprise/requirements).

### Admin Insights for Windows 365 expands to the Monitor Cloud PCs page (Public Preview)

Admin Insights for Windows 365 is now available on the Monitor Cloud PCs page &gt; Connection health tab. The experience now surfaces outlier cards that help administrators quickly identify Cloud PCs with elevated latency or connection failure rates, helping administrators quickly investigate and address potential issues. For more information, see [Admin Insights for Windows 365](/en-us/windows-365/enterprise/admin-insights).

## Week of July 13, 2026

### Cloud PC Settings is now generally available

Cloud PC settings are now generally available in Microsoft Intune. Administrators can configure four different object types: Cloud PC configurations, Windows App settings, Remote connection experience and User settings. This will provide a centralized approach to managing Cloud PC settings and policies. For more information, see [Settings overview](/en-us/windows-365/enterprise/settings-overview).

### Add Cloud Apps from a file path in Public Preview

Windows 365 admins can now manually add Cloud Apps by specifying a file path. This capability expands the set of applications you can deliver through Windows 365 Cloud Apps on Windows 365 Flex shared Cloud PCs, including apps that aren't surfaced through Start Menu discovery. This feature allows admins to duplicate applications, define custom app properties and set command-line parameters. For more information, see [Windows 365 Cloud Apps](/en-us/windows-365/enterprise/cloud-apps).

### Updated provisioning policy page in Microsoft Intune

In the Microsoft Intune admin center, when you go to Provision Cloud PCs &gt; Provisioning policies and select a policy, you'll notice a new multi‑tab page layout with Overview, Properties, Devices, and Action Status tabs. Admins can now view Cloud PCs from the policy, initiate bulk device actions, and view action status. Additionally, Windows 365 Flex shared provisioning policies with experience type Cloud App have a new Cloud Apps tab. For more information, see [View provisioning policies](/en-us/windows-365/enterprise/view-provisioning-policy).

## Week of July 6, 2026

### Rerank settings policies (Public Preview)

Windows 365 now supports reranking settings policies. Administrators can prioritize settings policies to determine which policy takes precedence when conflicting settings are configured. Policies can be reordered by changing their rank, using drag-and-drop controls, or moving policies up and down the list. Learn more in [Settings overview](/en-us/windows-365/enterprise/settings-overview).

### RDP Multipath with redundant TCP transport paths is now generally available

RDP Multipath with redundant TCP transport paths is now generally available for Windows 365 Cloud PC. This enhancement extends the resiliency benefits of RDP Multipath to TCP-based connections, enabling Windows 365 Cloud PC to maintain multiple standby TCP transport paths and automatically switch between them when network degradation is detected.

Key benefits include:

- Improved session resiliency across restrictive network environments
- Automatic failover between available transport paths
- Reduced session interruptions and disconnects
- No additional configuration required when prerequisites are met

For more information, see [RDP Multipath](rdp-multipath).

### More flexible device naming templates for Windows 365 Flex shared mode

Admins can now create more flexible device naming templates for Windows 365 Flex Cloud PCs in shared mode. Device names can be between 5 and 15 characters and include a prefix of up to 10 characters, with support for hyphens and a required random alphanumeric suffix of at least 5 characters. This update aligns naming capabilities across Windows 365 Enterprise and Windows 365 Flex, helping organizations apply naming conventions that match their business and operational requirements.

### Customer-managed encryption for Windows 365 Reserve (Public Preview)

Windows 365 Reserve now supports Microsoft Purview Customer Key (CMK), enabling administrators to encrypt Reserve Cloud PC disks with customer-managed keys stored in Azure Key Vault. This capability helps organizations meet security and compliance requirements by providing greater control over encryption key management, including key rotation, revocation, and auditing. Support for Customer Key in Reserve extends the existing CMK experience available for Windows 365 Cloud PCs. For more information, see [Microsoft Purview Customer Key setup and support for W365](/en-us/windows-365/enterprise/purview-customer-key).

## Week of June 15, 2026

### Added external identity support for Domainless federation

With the general availability of Domainless SAML IdP federation in Entra ID, you can provision a Cloud PC for an external identity whose email domain differs from the domain configured on the SAML IdP. These users must redeem their invitation to the organization prior to signing into the Windows App.

For more information, see [External identity](identity-authentication#external-identity) and [Domainless SAML IdP federation](/en-us/entra/external-id/direct-federation#domainless-saml-idp-federation).

## Week of June 8, 2026

### Built-in administrator account disabled during Cloud PC provisioning

During Cloud PC provisioning, the built-in administrator account is now disabled by default, helping improve security and reduce confusion without affecting admin or end-user workflows.

## Week of June 1, 2026

### Enhanced Windows 365 Flex Shared Cloud PC naming template (Public Preview)

Admins can now configure more flexible naming templates for Windows 365 Flex (shared mode) Cloud PCs. This update aligns Windows 365 Flex Shared with Enterprise and Windows 365 Flex Dedicated experiences, allowing device names between 5 and 15 characters, with a prefix of up to 10 characters and a random alphanumeric string of at least 5 characters. Hyphen placement is now fully flexible within the prefix, providing greater control over naming conventions. These enhancements help organizations apply business unit–based naming standards and maintain compatibility with downstream systems and tooling, simplifying transitions from physical PCs to Cloud PCs.

### Context-based redirections (Public Preview)

Context-based redirections are now available in public preview for Windows 365. This server-side capability enables admins to dynamically control clipboard, printer, drives, and low-level USB redirection behavior based on user identity, device compliance, and network conditions. By enforcing policies dynamically for bring-your-own-device (BYOD) scenarios, organizations can better protect sensitive data without relying on client-side controls. For more information, see [Context-based redirections in Windows 365](/en-us/windows-365/enterprise/context-based-redirections).

### GPU support for Windows 365 Flex shared Cloud PCs

Windows 365 Flex now supports GPU-enabled Cloud PCs in shared mode. This allows admins to assign GPU SKUs to shared Cloud PCs, enabling users to run graphics-intensive or performance-heavy workloads. With support extended beyond dedicated configurations, organizations gain more flexibility in how they deploy GPU-powered environments. For more information, see [GPU Cloud PCs in Windows 365](/en-us/windows-365/enterprise/gpu-cloud-pc).

### GPU Select SKU for Cloud PCs

Windows 365 introduces the GPU Select SKU, delivering higher-performance graphics capabilities at a lower cost for UI, multimedia, and productivity scenarios. Organizations can now choose from a broader set of GPU configurations to meet diverse performance needs. For more information, see [GPU Cloud PCs in Windows 365](/en-us/windows-365/enterprise/gpu-cloud-pc).

### 32 vCPU Cloud PC size now available

Windows 365 introduces a new 32 vCPU Cloud PC size, enabling greater compute power for complex and resource-intensive workloads. Ideal for development, simulations, and data-heavy scenarios, it helps improve performance and execution speed while reducing dependence on local hardware. Organizations can now support advanced workloads with a broader set of Cloud PC configurations. For more information, see [Windows 365 size recommendations](/en-us/windows-365/enterprise/cloud-pc-size-recommendations).

### New Windows 11 dev-ready image for Cloud PCs

Windows 365 introduces a new Windows 11 developer optimized image (preview) that includes preinstalled tools and configurations for development scenarios. This helps reduce onboarding time and simplifies environment setup for developers while maintaining a consistent experience across Cloud PCs. Organizations can now provision development-ready environments with minimal configuration. For more information, see [Device images in Windows 365](/en-us/windows-365/enterprise/device-images).

## Week of May 25, 2026

### Importing custom images from an Azure Compute Gallery now generally available

The ability for admins to import custom images from an Azure Compute Gallery is now generally available. Learn more [here](/en-us/windows-365/enterprise/add-device-images).

### Teams RemoteApp and CloudApp support for Windows App is now generally available

Slimcore-based Teams optimization is now supported for RemoteApps and CloudApps in the Windows App. This update enables Teams features beyond desktop sessions, with SlimCore-based optimization for improved performance. Support is limited to Windows App; non-Windows clients are not included. For more information, see [Microsoft Teams on a Cloud PC](/en-us/windows-365/enterprise/teams-on-cloud-pc).

## Week of May 11, 2026

### Improved licensing assignment logic for Cloud PC resize operations is now available

Windows 365 now features enhanced licensing assignment logic for group-based license (GBL) resize operations. The system validates both source license removal and target license assignment—regardless of order—before triggering a resize. This update prevents accidental Cloud PC provisioning, reduces policy-related reprovisioning errors, and ensures resizes occur predictably without creating duplicate Cloud PCs. If a user’s policy changes during a license transition, the resize fails gracefully with a clear error, allowing admins to correct the configuration before retrying. No new admin actions are required; existing workflows remain unchanged. Learn more about [resizing Cloud PCs](/en-us/windows-365/enterprise/resize-cloud-pc-bulk).

### Autopilot device preparation for Cloud PC provisioning is now available

Windows 365 now supports Autopilot device preparation with Cloud PC provisioning, enabling admins to define readiness criteria and ensure apps and scripts are installed before a Cloud PC is marked as provisioned. For more information, see [Use Autopilot device preparation with Cloud PCs](autopilot-device-preparation).

### Windows Autopilot support for Windows 365 Reserve (Public Preview)

Autopilot Device Preparation is now available in Public Preview for Windows 365 Reserve. With DPP enabled, provisioning completes only after required applications and configurations are installed and validated - improving reliability and security while reducing the need for custom images. 

Admins can optionally link [Autopilot Device Preparation](/en-us/autopilot/device-preparation/overview) with Reserve provisioning policies in Microsoft Intune. Cloud PCs provisioned with DPP show a Preparing status while device setup is in progress. There are no changes to Reserve licensing, usage limits, or the end-user experience.

### RDP Multipath with redundant TCP transport paths begins GA rollout

Windows 365 has started the general availability (GA) rollout of **RDP Multipath with redundant TCP transport paths**. This enhancement improves connection resiliency to **Windows 365 Cloud PCs** by enabling multiple TCP transport paths and automatically switching between them when network degradation is detected.

Redundant TCP transport paths complement existing UDP‑based RDP Multipath and help maintain reliable connectivity in environments where UDP connectivity is unreliable or unavailable. The feature is being enabled through a **phased, quality‑driven rollout**. Until rollout is complete, redundant TCP may not be consistently enabled across all Cloud PCs.

For more information, see [RDP Multipath](rdp-multipath).

## Week of May 4, 2026

### Windows 365 Frontline is now Windows 365 Flex

Windows 365 Frontline is renamed to **Windows 365 Flex**. The product, licensing, and capabilities are unchanged—only the name is different. For more information about the rebrand, see [Expanding access to Windows 365](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-365-and-azure-virtual-desktop-expanding-access/4515931) on the Windows IT Pro Blog.

### Admin Insights for Windows 365

Admin Insights for Windows 365 is now in public preview, designed to help IT administrators quickly understand what’s happening in their environment and where to focus. IT administrators managing Windows 365 Cloud PCs rely on a range of signals across the Microsoft Intune admin center—including reports, alerts, and device views—to understand the health of their environment. These tools provide valuable visibility, but as environments scale, quickly surfacing what needs attention becomes more important. Admin Insights builds on existing reporting, monitoring, and alerting by bringing important signals together directly into the Windows 365 experience.

For more information, see [Admin Insights for Windows 365](/en-us/windows-365/enterprise/admin-insights).

## Week of April 27, 2026

### Snapshot-based reset for Windows 365 Flex shared Cloud PCs (Public Preview)

Snapshot-based reset is in public preview for Windows 365 Flex shared Cloud PCs. When a user signs out, the Cloud PC reverts to a known-good snapshot before the next user signs in. No files, settings, or app changes from the previous session carry over.

Use snapshot-based reset to:

- Give each user a clean Cloud PC at sign-in.
- Keep user data isolated between sessions on a shared Cloud PC.
- Avoid configuration drift on shared Cloud PCs over time.

For more information, see [Snapshot-based reset for Windows 365 Flex shared Cloud PCs](/en-us/windows-365/enterprise/windows-365-flex-snapshot-based-reset).

## Week of April 13, 2026

### User‑initiated provisioning for Windows 365 Reserve (public preview)

Windows 365 Reserve now supports user‑initiated provisioning in public preview, giving eligible users the ability to set up their Reserve Cloud PC directly from the Windows App when they need secure access quickly—such as during device failures or while traveling.

This capability is off by default and fully governed by IT. Admins can enable user provisioning through Windows App settings for Windows 365 in Microsoft Intune and scope it to specific Microsoft Entra ID user groups. When enabled, users can start provisioning on demand while IT continues to manage policies, licensing, and overall governance, helping reduce downtime without changing existing administrative controls.

For more information, see [Managing Windows 365 Reserve](windows-365-reserve-manage).

## Week of April 6, 2026

### Updates to Windows 365 navigation in the Microsoft Intune admin center now generally available

The Windows 365 experience in the Microsoft Intune admin center has been updated with a new, dedicated navigation area under **Devices** called **Manage Windows 365 Cloud PCs**. The Windows 365 entry point has moved from the **Devices &gt; Device onboarding** section to this new location, where existing management options—such as Overview, All Cloud PCs, All Cloud Apps, and Settings—are now organized in a vertical navigation menu. **Provision Cloud PCs** contains Provisioning policies, Custom images, and Azure Network Connections.

In addition, a new Windows 365 administration section is available under **Tenant administration**, grouping related pages such as Cloud PC encryption type, Cloud PC alerts, Cloud PC maintenance windows, and Partner connectors. This update doesn’t affect any existing features, workflows, assignments, or Cloud PC behaviors.

### Cloud PC Monitoring (Public Preview)

Cloud PC Monitoring is now available in public preview for Windows 365. This feature provides IT admins with enhanced visibility into Cloud PC health, performance, and configuration through integrated dashboards in the Microsoft Intune admin center. Admins can view connection health trends, Cloud PC reliability data, and user‑ and device‑level insights to support troubleshooting and help‑desk scenarios across their Cloud PC environment. Cloud PC Monitoring helps organizations monitor end‑to‑end configuration and more quickly identify and investigate performance and connection issues.

For more information, see [Cloud PC monitoring overview](/en-us/windows-365/enterprise/cloud-pc-monitoring-overview).

### Azure Network Connection health checks now enforce required Windows 365 endpoints

Beginning in April 2026, Azure Network Connection (ANC) health checks will return an Error instead of a Warning if the following required endpoints aren't reachable, blocking new Cloud PC provisioning until resolved:

- \*.service.windows.cloud.microsoft
- \*.windows.cloud.microsoft
- \*.windows.static.microsoft

No new endpoints are being added. Existing Cloud PCs and Microsoft-hosted network deployments aren't affected.

For more information, see [Azure Network Connection health checks](/en-us/troubleshoot/windows-365/health-checks) and [Azure Network Connection connectivity requirements.](/en-us/windows-365/enterprise/understanding-network-connectivity-flows-cloud-side)

### Windows 365 Power Platform connector (Public Preview)

We are excited to announce the Public Preview of the Windows 365 connector for Power Platform and Azure Logic Apps!

With prebuilt actions and triggers for Windows 365 built on top of Graph, IT and operations teams can use Power Automate and Azure Logic Apps to build Cloud PC workflows, such as sending emails to users when Cloud PCs are provisioned.

For more information on the triggers and actions, see [Windows 365 - Connectors](/en-us/connectors/windows365/) and [Windows 365 Power Platform connector](/en-us/windows-365/enterprise/windows365-power-platform-connector).

### Windows 365 Government support for external identities

You can now provision a Cloud PC for an external identity in Windows 365 Government. External identity users can connect to the service using the latest **Windows App on Windows**.

For more information, see [External identity](identity-authentication#external-identity), along with appropriate [Windows 365 licensing guidance](/en-us/windows-365/overview#licensing-for-external-identities).

## Week of March 30, 2026

### Additional client support for external identities

External identity support is now in preview for the Windows App on macOS and Android. For more information on client versions and capabilities, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity).

For latest information on external identity support, see [External identity](identity-authentication#external-identity).

### Intelligent pre‑start for Windows 365 Flex (Dedicated mode) is now generally available

This capability uses predictive insights to determine when a user is likely to connect and proactively starts their Cloud PC in advance, so it’s ready when they sign in. By reducing the time required for the Cloud PC to boot, Intelligent pre‑start helps minimize connection delays and improves the overall login experience for Windows 365 Flex users.

This enhancement is designed to support task‑based and time‑bound work patterns, enabling faster access to Cloud PCs without requiring any changes to user or admin workflows.

For more information, see [Intelligent pre‑start for Windows 365 Flex in Dedicated mode](/en-us/windows-365/enterprise/introduction-windows-365-flex#intelligent-prestart-for-windows-365-flex-in-dedicated-mode).

### Additional regions for Windows 365 Flex (shared)

Windows 365 Flex in Shared mode is now available in the following regions:

- Brazil – Brazil South
- Italy (EU) – Italy North
- Netherlands (EU) – West Europe

These regions are now selectable in Windows 365 Flex (shared) provisioning policies in Microsoft Intune.

### Azure Network Connections now show available IP capacity

Administrators can now view available IP capacity for each Azure network connection (ANC) directly in the Azure network connections experience in the Microsoft Intune admin center. This visibility helps you plan subnet capacity before provisioning and scaling Cloud PCs, and it can help identify capacity constraints that may affect provisioning success. The value surfaces as an IP availability count and is intended for troubleshooting and planning without exposing individual IP addresses.

## Week of March 23, 2026

### Additional regions for Windows 365 Flex (shared)

Windows 365 Flex in Shared mode is now available in additional regions:

- Poland (EU) – Central
- Sweden (EU) – Central
- Mexico – Central
- New Zealand – North

These regions are now selectable in Windows 365 Flex (shared) provisioning policies in Microsoft Intune. For more information, see [Supported regions for Cloud PC provisioning](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2Cshared#supported-azure-regions-for-cloud-pc-provisioning).

### Remote connection experience for Windows 365 (Public Preview)

Windows 365 introduces the Remote connection experience in preview, enabling IT administrators to configure connection‑level settings that apply just‑in‑time when users connect to targeted Cloud PCs. These settings can be assigned to specific device groups through Microsoft Intune to help tailor and manage how users interact with their Cloud PC during remote sessions. For more information, see [Remote connection experience](/en-us/windows-365/enterprise/remote-connection-experience).

### New Azure region support for Windows 365 Government

Windows 365 Government now supports Cloud PC provisioning in the US Government – Texas region.

### Cloud Apps support for APPX and MSIX applications

Cloud Apps now support APPX and MSIX applications in addition to traditional Win32 apps. Admins can discover and publish a broader set of applications including Microsoft Teams and new Outlook when configuring Cloud Apps for Windows 365. Cloud Apps support for APPX and MSIX applications in existing Cloud Apps provisioning policies requires reprovisioning. This will enable the discovery of APPX and MSIX applications. The management experience and publishing workflow remain the same, while expanding the types of applications that can be made available to users.

### Enhanced resiliency and expanded regional availability for Windows 365 Government

Windows 365 Government now supports Microsoft Hosted Network (MHN) with Multi‑Region Selection for Government Community Cloud (GCC and GCC High). This enhanced deployment experience distributes Cloud PCs across multiple regions using a three‑tier region selection model, helping improve resiliency while giving admins greater flexibility and control over where Cloud PCs are provisioned.

In addition, the US Gov Texas region is now available for Windows 365 Government customers in GCC and GCC High, enabling Cloud PCs to be provisioned in an additional U.S. government region. For more information, see [Microsoft Hosted Network with Multi-Region Selection](/en-us/windows-365/enterprise/enhanced-resiliency-mhn) and [Supported U.S. Government regions for Windows 365](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2Cgov#supported-azure-regions-for-cloud-pc-provisioning).

## Week of March 16, 2026

### Expanded regional availability for Windows 365 Flex (shared)

Windows 365 Flex (Shared mode) is now available in the following additional regions:

- France (EU) – France Central
- Norway – Norway East
- Spain (EU) – Spain Central

Windows 365 Flex in Shared mode is now available in these regions, enabling organizations to provision Cloud PCs closer to users. This expansion supports lower latency and local data residency requirements for shift‑based and shared access scenarios. For more information, see [Supported regions for Cloud PC provisioning](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2Cshared#supported-azure-regions-for-cloud-pc-provisioning).

### Recovery for Windows 365 Enterprise Cloud PCs that were Deprovisioned due to License Expiration is now available

This feature has now moved out of preview and is now generally available. The grace period alert has now expanded so that admins can configure an alert for Cloud PC deprovisioning. For more information, see [Point-in-time restore for Windows 365 Enterprise](/en-us/windows-365/enterprise/restore-overview) and [Alerts in Windows 365](/en-us/windows-365/enterprise/alerts).

### Faster Cloud PC Compliance Evaluation During Provisioning

Cloud PCs now evaluate Intune compliance policies during provisioning without requiring user sign‑in, enabling devices to become compliant on first boot. This improvement delivers faster and more reliable compliance reporting, helping administrators ensure Conditional Access and compliance policies take effect immediately.

This enhancement is included in the latest Windows update (KB5070311) for Windows 11 25H2 and 24H2 and is already available in updated gallery images. No administrative action is required—new Cloud PCs created from gallery images will automatically benefit from the improved compliance evaluation flow.

## Week of March 9, 2026

### Expanded Microsoft Teams media optimizations now available

Microsoft Teams optimizations in Windows 365 are available when accessing Cloud PCs from Windows App on iOS and Android (GA for WebRTC) and macOS (preview for Slimcore) platforms. Teams provides optimized calling and meeting experiences on Cloud PCs, with ongoing improvements delivered through the Windows App and the new Teams architecture. For more information, see [Microsoft Teams on a Cloud PC](/en-us/windows-365/enterprise/teams-on-cloud-pc).

### Windows 365 support for Germany West Central and Switzerland North

Windows 365 Flex in Shared mode is now available in Germany West Central and Switzerland North. This regional expansion helps organizations provision Cloud PCs closer to users, supporting lower latency and local data residency requirements for shift‑based and shared access scenarios. For more information, see [Supported regions for Cloud PC provisioning](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2cent).

### Windows 365 Flex shared provisioning policies update

Windows 365 Flex (Shared mode) provisioning policies now support up to 5,000 Cloud PCs per policy. This update allows organizations to scale Windows 365 Flex deployments more efficiently and reduces the need to manage multiple provisioning policies as Windows 365 Flex workforces grow.

### Captive portal support for Windows 365 Boot

Windows 365 Boot now supports captive portals, allowing users to connect to Wi‑Fi networks that require web‑based sign‑in, such as accepting terms or completing one‑time password authentication. Network registration opens in the default browser, with clearer connectivity status shown in Quick Settings and Action Center. This update applies to Windows 365 Boot devices only.

## Week of March 2, 2026

### Resize support for Windows 365 Flex dedicated Cloud PCs

Resize support for Windows 365 Flex dedicated Cloud PCs is now generally available. Admins can resize Windows 365 Flex dedicated Cloud PCs after provisioning to adjust compute and storage configurations without reprovisioning. This capability provides greater operational flexibility when user requirements change and helps reduce the overhead of managing capacity. Admins can respond more easily to evolving performance needs while keeping existing Cloud PCs intact. For more information, see [Resize Windows 365 Flex Cloud PCs in Dedicated mode](resize-windows-365-flex-cloud-pc).

## Week of February 23, 2026

### Windows first sign-in restore experience now available

Windows Backup for Organizations on Cloud PCs brings restore parity between physical Windows devices and Windows 365. When users sign in to a Cloud PC for the first time, they can restore their Windows personalization settings and Microsoft Store app list from an existing organizational backup—getting back to a familiar, productive environment in minutes. A key scenario is Windows 365 Reserve, where users temporarily transition from a physical device to a Cloud PC. With backup restore at first sign-in, Reserve users retain their personalized experience during the transition and seamlessly return to work without IT intervention, reducing disruption and support overhead. Learn more about supported versions of Windows and how to enable the feature [here](/en-us/windows/configuration/windows-backup/?tabs=intune).

## Week of February 9, 2026

### Custom images from an Azure Compute Gallery (Public Preview)

Admins can now import custom images from an Azure Compute Gallery. Learn more [here](/en-us/windows-365/enterprise/add-device-images).

### Windows 365 support for New Zealand North

Windows 365 Enterprise and Windows 365 Frontline (Dedicated mode) are now available in the New Zealand North region. This expansion allows organizations in New Zealand and nearby areas to provision Cloud PCs closer to their users, helping improve performance.

For more information, see [Supported regions for Cloud PC provisioning](/en-us/windows-365/enterprise/requirements?tabs=enterprise%2cent).

## Week of February 2, 2026

### Region flexibility for Cloud PC provisioning

When you select Microsoft Hosted Network with automatic region selection in your provisioning policy, Windows 365 now distributes Cloud PCs across multiple Azure regions within your selected geography. The service evaluates region health at provisioning time and excludes unhealthy regions to improve deployment success and resiliency. This feature helps minimize the impact of regional outages by spreading Cloud PCs across healthy regions.

For more information, see [Create provisioning policies](/en-us/windows-365/enterprise/create-provisioning-policy).

### Centralized RDP Shortpath configuration for Cloud PCs is now generally available

Admins can now manage RDP Shortpath modes—Managed, Public/STUN, and Public/TURN—using Microsoft Intune or Group Policy, enabling predictable and policy-driven behavior across Cloud PCs. Registry based policies remove the need for manual host configuration and ensure consistent Shortpath setup.

### Migration API now generally available

The Windows 365 migration API has moved out of preview and into general availability. This enables partners and customers to develop tailored solutions that streamline the transition to Windows 365. By leveraging automation with the Microsoft Graph API and integrating with Microsoft Intune, it allows users to move to Windows 365 more efficiently. This Migration API marks a major step forward in simplifying the migration of persistent VMs from Azure to Windows 365, minimizing both complexity and downtime.

### iOS and iPadOS now support screen capture protection via Microsoft Intune Mobile Application Management (MAM)

Screen capture protection helps prevent sensitive information from being captured on client devices. When you enable screen capture protection, remote content is automatically blocked in screenshots and screen sharing. You can now use Intune MAM policies to configure screen capture protection on iOS and iPadOS. For more information, see [Screen capture protection](/en-us/azure/virtual-desktop/screen-capture-protection).

## Week of January 26, 2026

### Microsoft Purview Customer Key support for Windows 365 Flex (Shared mode)

Windows 365 Flex in Shared mode now supports Microsoft Purview Customer Key for service encryption. With this enhancement, newly provisioned Cloud PCs will automatically be protected using Customer Key for organizations that have onboarded the capability in Microsoft Purview. This update applies to customers using Windows 365 Flex licenses who have configured Customer Key for added control over service side encryption.

## Week of January 19, 2026

### Expanded UDP Connectivity Validation with the TURN Health Check

The existing UDP connectivity check in Azure Network Connection (ANC) validates STUN (Session Traversal Utilities for NAT) reachability. We’re enhancing this check to also validate TURN (Traversal Using Relays around NAT) connectivity, giving administrators a more complete view of relay-path readiness. With TURN health surfaced alongside STUN on the ANC page, administrators can more quickly spot and remediate relay-path issues before they impact users.

Learn more about [Azure network connection health checks.](/en-us/troubleshoot/windows-365/health-checks)

Learn more about [Network Connectivity Flows.](understanding-remote-desktop-protocol-traffic)

## Week of January 12, 2026

### Improved Cloud PC Visibility with a New Column on the Azure Network Connection Page

We have introduced a new column in the Azure Network Connection (ANC) page to give administrators better visibility into their Cloud PC environment. This column displays the number of devices provisioned per ANC, helping you quickly assess distribution and capacity. It’s also interactive—selecting the value takes you directly to the All Cloud PCs view, where you can see detailed information about the Cloud PCs associated with that specific ANC. This enhancement streamlines navigation and improves management efficiency for large-scale deployments.

## Week of December 15, 2025

### Enhanced Microsoft Hosted Network Cloud PC Resiliency with Multi-Region Selection

We're introducing a three-tier region selection experience and an enhanced deployment service that distributes your Cloud PCs across the maximum number of regions to improve resiliency while giving admins greater flexibility and control.

For more information, see [Microsoft Hosted Network with Multi-Region Selection](enhanced-resiliency-mhn).

## Week of November 17, 2025

### Windows 365 support for external identities is now generally available

You can now provision a Cloud PC for an external identity. There's no change to the administrative flow to provision this Cloud PC, as it follows the same provisioning flows for both Windows 365 Enterprise and Windows 365 Flex Cloud PCs.

For more information, see [External identity](identity-authentication#external-identity), how to [Provide Cloud PCs to external identities](provide-cloud-pc-external-identities), and appropriate [Windows 365 licensing guidance](/en-us/windows-365/overview#licensing-for-external-identities).

### Windows 365 Reserve now generally available

Windows 365 Reserve has moved out of preview and into general availability. Windows 365 Reserve is a version of Windows 365 designed for users who primarily work on physical PCs. It provides organizations with flexible, short-term Cloud PC access to keep employees productive during unexpected disruptions. This offering supports business continuity by enabling quick, secure access to Cloud PCs when physical devices are unavailable. For more information, see [Windows 365 Reserve](introduction-windows-365-reserve)

### Windows 365 Cloud Apps now generally available

Windows 365 Cloud Apps has moved out of preview and into general availability and now supports publishing Intune apps as Cloud Apps via Autopilot Device Preparation (preview). For more information, see [Windows 365 Cloud Apps](cloud-apps).

### User Experience Sync (UES) now generally available

[User Experience Sync](windows-365-flex-user-experience-sync) is now generally available for Windows 365. UES delivers a consistent experience by saving user settings and app data across sessions, so users can be productive as soon as they sign in. It’s designed for Windows 365 Flex Shared mode and [Cloud Apps](cloud-apps) scenarios, making it ideal for occasional use workers who share devices or need personalized settings across multiple sessions. IT admins benefit from simplified end user experience management and built-in tools to monitor storage and resolve issues quickly.

### Windows Cloud Keyboard Input Protection now in preview

Windows Cloud Keyboard Input Protection is now in preview - purpose-built to address endpoint security concerns for Windows 365 and Azure Virtual Desktop. This feature encrypts keystrokes at the kernel level, protecting against keylogger malware and other endpoint threats. It marks a major step forward in helping customers secure sensitive input data and strengthen endpoint security in cloud-based workspaces, see [Windows Cloud Input Protection](windows-cloud-input-protection).

### AI-enabled Cloud PCs now in Frontier Public Preview

AI-enabled Cloud PCs are now available in Frontier Public Preview for customers wanting to try the latest Windows AI capabilities with Windows 365. IT admins can enable this ability for specific users so that they can use improved Windows search and Click to Do to enhance their productivity. For more information including minimum Windows 365 SKU requirements, minimum Windows OS requirements, and supported regions, see [AI-enabled Cloud PCs](ai-enabled-cloud-pcs).

### Link Autopilot device preparation with Windows 365 Enterprise Cloud PCs and Frontline Cloud PCs in dedicated mode (Public Preview)

You can now link Autopilot device preparation with Windows 365 Enterprise Cloud PCs and Windows 365 Flex Cloud PCs Dedicated mode. For more information, see [Use Autopilot device preparation with Cloud PCs](autopilot-device-preparation).

### Windows 365 Switch Supports Home Edition

Windows 365 Switch now supports Windows 11 Home edition, making it an excellent choice for Bring Your Own Device (BYOD) scenarios.

## Week of November 3, 2025

### RDP Multipath is now fully rolled out!

We’ve completed the phased deployment of RDP Multipath across all eligible connections. This feature enhances reliability and performance by leveraging multiple network paths for your remote sessions, ensuring a more resilient and seamless experience.

## Week of October 13, 2025

### Migration API (public preview)

The Windows 365 migration API enables partners and customers to develop tailored solutions that streamline the transition to Windows 365. By leveraging automation with the Microsoft Graph API and integrating with Microsoft Intune, it allows users to move to Windows 365 more efficiently. This Migration API marks a major step forward in simplifying the migration of persistent VMs from Azure to Windows 365, minimizing both complexity and downtime.

## Week of September 22, 2025

### Device provisioning

#### Windows 365 support for external identities (preview)

You can now provision a Cloud PC for an external identity. There is no change to the administrative flow to provision this Cloud PC, as it follows the same provisioning flows for both Windows 365 Enterprise and Windows 365 Flex Cloud PCs.

For more information, see [External identity (preview)](identity-authentication#external-identity), along with appropriate [Windows 365 licensing guidance](/en-us/windows-365/overview#licensing-for-external-identities).

### Global expansion of TURN Relay

Microsoft has expanded the TURN relay infrastructure globally, deploying it across 39 Azure regions with a dedicated IP range of 51.5.0.0/16 for Azure Virtual Desktop and Windows 365. This transition from the previously shared 20.202.0.0/16 subnet enhances RDP Shortpath for Public Networks, offering improved performance, reliability, and user experience.

## Week of September 15, 2025

### Windows 365 Boot Updates

The latest Windows 365 Boot updates are now rolling out to GA with a modern, streamlined connection experience that reduces startup times. Users with multiple Cloud PCs who haven’t set a default can now access the Connection Center during logon to choose which Cloud PC to start. We’ve also added error handling improvements—if you hit an error, selecting Cancel takes you to the Connection Center, where you can restart or troubleshoot your Cloud PC directly from the ellipses (…) menu. Finally, Windows 365 Boot now supports cross-region disaster recovery, helping ensure resilience and business continuity.

### Copilot in Intune for Windows 365

#### Copilot in Intune support for Windows 365 is now generally available

IT admins can now prompt Copilot in Intune chat to ask questions about their Windows 365 Cloud PCs. Example prompts:

- "Show me my Enterprise Cloud PC licenses"
- "Analyze trends in bandwidth performance"
- "Summarize Cloud PCs that have never been used"

Copilot in Intune support enables admins to more rapidly access insights on their Cloud PCs, accelerating decision-making and improving outcomes. For more information, see [Copilot in Intune for Windows 365](/en-us/windows-365/enterprise/copilot-in-intune-for-windows365).

### Windows 365 Flex

#### Windows 365 Cloud Apps (preview)

The Windows 365 Cloud Apps feature allows administrators to give users secure access to individual apps hosted on a Cloud PC, without requiring a dedicated Cloud PC for every user. [Windows 365 Flex licenses](windows-365-flex-license) entitle organizations to stream Windows 365 Cloud Apps when operating Cloud PCs in Shared mode. For more information, see [Windows 365 Cloud Apps](cloud-apps).

#### Windows 365 Flex Cloud PCs in Dedicated mode generally available on US government cloud

You can now provision Windows 365 Flex Cloud PCs in Dedicated mode in US Government Community Cloud (GCC). For more information, see [Windows 365 Government](/en-us/windows-365/enterprise/introduction-windows-365-government).

## Week of September 8, 2025

### Business Continuity and Disaster Recovery

#### Cross-region Disaster Recovery for Windows 365 Flex (Dedicated mode)

Already available for W365 Enterprise, Cross-region DR now extends to Windows 365 Flex (Dedicated mode), supporting shift-based roles in critical industries where downtime is not an option and disaster recovery is essential. This add-on feature creates "snapshots" of Cloud PCs in customer-defined, geographically distant locations. In the event of a regional outage, these snapshots can be recovered as Cloud PCs running in the selected backup location, helping keep your users productive even if their primary region goes down.

### Windows 365 Partner Integrations

#### HP Anyware for Windows 365 Enterprise

HP Anyware for Windows 365 Enterprise has been expanded to include support for Windows 365 GPU-enabled Enterprise Cloud PCs. This integration brings the power of PC-over-IP (PCoIP) — a protocol known for delivering high-definition, low-latency performance—to Windows 365, making it ideal for graphics-intensive workloads such as 3D modeling, video editing, and data visualization.

## Week of August 25, 2025

### Windows App

#### Token protection generally available in Windows App on Windows devices

You can now use a Conditional Access policy to require token protection for sign-in tokens (refresh tokens) on Windows devices. Such policies can reduce attacks using token theft by ensuring a token is usable only from the intended device. For more information, see [Microsoft Entra Conditional Access token protection explained](/en-us/entra/identity/conditional-access/concept-token-protection).

## Week of August 4, 2025

### Device Management

#### Recover Windows 365 Enterprise Cloud PCs that were Deprovisioned due to License Expiration (preview)

You can now recover Windows 365 Enterprise Cloud PCs that were deprovisioned due to license expiration. Once you repurchase the expired licenses and ensure you have followed the prerequisites, you can use the retention snapshot to restore the Cloud PC for your end user. For more information, see [Point-in-time restore for Windows 365 Enterprise](/en-us/windows-365/enterprise/restore-overview).

#### RDP Multipath is now generally available

Remote Desktop Protocol (RDP) Multipath is now generally available for Azure Virtual Desktop and Windows 365. This feature improves connection reliability and performance by intelligently managing multiple network paths between the client and the session host or Cloud PC. Multipath dynamically selects the best available path and provides seamless failover, delivering a smooth user experience even in environments with variable network conditions. We’re rolling out this feature in phases, so an increasing percentage of connections will benefit from RDP Multipath as deployment continues. For more information, see [RDP Multipath](rdp-multipath).

### Device Security

#### Select redirections disabled for newly provisioned and reprovisioned Cloud PCs

Windows 365 is enhancing Cloud PC security by having clipboard, drive, opaque low-level USB, and printer redirections disabled by default for all newly provisioned and reprovisioned Cloud PCs. This change minimizes the risk of data exfiltration and malware injections, which provides a more secure experience and aligns with the Microsoft Secure Future Initiative (SFI) principle to have security protections enabled and enforced by default.

For more information, see [Manage RDP device redirections for Cloud PCs](manage-rdp-device-redirections).

## Week of June 30, 2025 (Service release 2506)

### Device management

#### Two new display language packs for Cloud PCs

English (Ireland) and English (Australia) are now available as language packs that you can use in provisioning policies to set up a default display language for Cloud PCs. For more information, see [Use a provisioning policy to set up a default display language on Cloud PCs](use-provisioning-policy-default-display-language).

### Windows 365 Flex

#### Intelligent pre-start for Windows 365 Flex in Dedicated mode (preview)

Windows 365 Flex Cloud PCs have the ability to predict when a user connects and pre-start their Cloud PC before they connect. This prediction improves connect times for such users' Cloud PCs. For more information, see [Intelligent pre-start for Windows 365 Flex in Dedicated mode](introduction-windows-365-flex).

#### Configure non-UTC time zones for bulk reprovisioning for Windows 365 Flex Cloud PCs in Shared mode

You can now configure non-UTC time zones when scheduling bulk reprovisioning for Windows 365 Flex Cloud PCs in Shared mode. For more information, see [Schedule bulk reprovision Windows 365 Flex Cloud PCs in Shared mode](windows-365-flex-shared-bulk-reprovision#schedule-bulk-reprovision-windows-365-flex-cloud-pcs-in-shared-mode).

## Week of June 23, 2025

### Device management

#### Cross region disaster recovery for Windows 365 Flex in Dedicated mode (preview)

Windows 365 Flex in Dedicated mode now supports cross region disaster recovery. For more information, see [Cross region disaster recovery in Windows 365](cross-region-disaster-recovery).

## Week of June 2, 2025

### Device management

#### High Efficiency Video Coding (H.265) hardware acceleration support

Windows 365 GPU-enabled Super and Max SKUs now support graphics processing unit (GPU) acceleration for frame encoding using HEVC/H.265. GPU acceleration improves graphical experiences when using the Remote Desktop Protocol (RDP) with a compatible GPU-enabled Cloud PCs.

For more information, see [GPU Cloud PCs in Windows 365](gpu-cloud-pc) and [Enable GPU acceleration for Azure Virtual Desktop](/en-us/azure/virtual-desktop/graphics-enable-gpu-acceleration?tabs=intune).

#### Windows 365 Flex Dedicated mode concurrency management now generally available

Windows 365 Frontline Dedicated mode concurrency management has moved out of preview and into general availability. For more information, see [Concurrency management](create-provisioning-policy).

#### Teams VDI 1.0 support on iOS(preview)

Windows 365 now supports Teams VDI 1.0 on iOS. For more information, see [Microsoft Teams on a Cloud PC](teams-on-cloud-pc).

## Week of May 28, 2025 (Service release 2505)

### Monitor and troubleshoot

#### Cloud PC utilization report: new options for aggregated time connected

You can now:

- Pick time spans of 28, 60, and 90 days for the aggregated time connected data.
- See Cloud PCs that no one has connected to yet.

For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### Cloud PC action status report batch progress now generally available

The following feature has moved out of preview and into general availability:

The Cloud PC action status report shows batches of devices on which actions were triggered. You can see the batch current progress. For more information, see [Cloud PC actions report](report-cloud-pc-actions).

### End user experience

#### windows365.microsoft.com being replaced by Windows App

The windows365.microsoft.com end user portal is currently being deprecated. Navigation to windows365.microsoft.com is automatically redirected to Windows App on the web. This deprecation will be complete on June 1, 2025. (Windows 365 Government users can still access the end user portal.)

## Week of April 28, 2025 (Service release 2504)

### Device management

#### Guidance when placing a Cloud PC under review

Adhere to SEC Rule 17a-4 by configuring Azure Blob storage for immutability. For more information, see [Place a Cloud PC under review](place-cloud-pc-under-review) and [Azure - Cohasset Assessment - WORM Storage (2024) Report](https://servicetrust.microsoft.com/DocumentPage/19b08fd4-d276-43e8-9461-715981d0ea20).

#### Resize Windows 365 Flex Cloud PCs in Dedicated mode (preview)

Admins can now resize Windows 365 Flex Cloud PCs in Dedicated mode. For more information, see [Resize Windows 365 Flex Cloud PCs in Dedicated mode](resize-windows-365-flex-cloud-pc).

### Device security

#### Credential Guard and HVCI enabled by default

Newly provisioned and reprovisioned Cloud PCs running a Windows 11 gallery image now have VBS, HVCI, and Credential Guard enabled by default. For more information, see [Windows 365 security](security).

### Monitor and troubleshoot

#### Connected Windows 365 Flex Cloud PCs report is generally available

The Connected Windows 365 Flex Cloud PCs report has moved out of preview and into general availability. For more information, see [Connected Windows 365 Flex Cloud PCs report](report-connected-windows-365-flex-cloud-pcs).

### Windows App

#### Token protection (Preview) in Windows App on Windows devices

You can now use a Conditional Access policy to require token protection for sign-in tokens (refresh tokens) on Windows devices. Such policies can reduce attacks using token theft by ensuring a token is usable only from the intended device. For more information, see [Microsoft Entra Conditional Access token protection explained](/en-us/entra/identity/conditional-access/concept-token-protection).

## Week of April 21, 2025

### Device management

#### Move selected Cloud PCs from one region or Azure network connection to another

You can now move selected Cloud PCs from one region or Azure network connection (ANC) to another. For more information, see [Move Cloud PC](move-cloud-pc).

### Device provisioning

#### Create provisioning policy process warning for lack of Windows 365 Flex licenses

When creating a provisioning policy for Windows 365 Flex Cloud PCs, the process now provides a warning if the tenant has no Windows 365 Flex licenses.

### Documentation

#### New documentation article: Microsoft and customer roles and responsibilities for Windows 365

We’ve created a new article. For more information, see [Microsoft and customer roles and responsibilities for Windows 365](/en-us/windows-365/customer-microsoft-responsibilities).

## Week of April 14, 2025

### Device management

#### Health status for Cloud PC restore point

You can now see the health status of Cloud PC restore points before deciding to start a restore. For more information, see [Restore a single Cloud PC to a previous state](restore-single-cloud-pc) and [Restore multiple Cloud PCs in bulk](restore-bulk).

### Monitor and troubleshoot

#### Concurrency buffer usage alert

You can set up a new alert to monitor concurrency buffer usage for Windows 365 Flex in Dedicated mode.

#### Cloud PC concurrency report update

The Connected Windows 365 Flex Cloud PCs report now shows a user's session length. You can also restart Windows 365 Flex Cloud PCs from the report if you've reached max concurrency on any individual assignments. For more information, see [Connected Windows 365 Flex Cloud PCs report](report-connected-windows-365-flex-cloud-pcs).

## Week of April 7, 2025

### Windows 365 Government

#### Windows 365 Government scope tag support

Windows 365 Government now supports scope tags.

## Week of March 31, 2025 (Service release 2503)

### Device management

### Every time sign-in frequency option now is generally available

The Every time sign-in frequency option has moved out of preview and into general availability. For more information, see [Set conditional access policies](set-conditional-access-policies).

#### Default Visual Effects performance option change

The Visual Effects performance option now defaults to **Let Windows choose what’s best for my computer**.

#### Windows 365 disaster recovery options

Admins now have two options for disaster recovery: the existing cross region disaster recovery and the new disaster recovery plus. The latter allocates a second Cloud PC at the time of configuration which improves RTO. As the recovery Cloud PC already exists, there isn't a capacity risk at the time of failure. For more information, see [Windows 365 disaster recovery plus](disaster-recovery-plus).

### Provisioning

#### Data disk not allowed for custom images

Uploading a custom image with attached managed data disks are no longer allowed for Windows 365 custom images.

### Windows 365 Frontline

#### Windows 365 Frontline Cloud PCs in Shared mode now generally available

Windows 365 Frontline Cloud PCs in Shared mode has moved out of preview and into general availability. For more information, see [Windows 365 Frontline in Shared mode](introduction-windows-365-flex#windows-365-flex-in-shared-mode).

#### Link Autopilot device preparation with Windows 365 Frontline Cloud PCs in Shared mode

You can now link Autopilot device preparation with Windows 365 Frontline Cloud PCs in Shared mode. For more information, see [Use policy-driven Autopilot device preparation with Windows 365 Frontline Cloud PCs in Shared mode](autopilot-device-preparation).

### End user experience

#### Return to local desktop

When in Windows 365 Boot mode (Windows 11 only), users can now switch back to their physical device desktop from either:

- CTRL-ALT-DEL screen
- Cloud PC error screens

Administrators can configure and customize this feature within the Guided Scenario for Boot.

### Windows App

#### Access Windows App using Edge on personal Windows devices with MAM

You can now enable protected Mobile Application Management (MAM) access to Windows App using Microsoft Edge on personal Windows devices. For more information, see [Require local client device security compliance with Microsoft Intune and Microsoft Entra Conditional Access](/en-us/windows-app/require-device-security-compliance-intune).

## Week of March 17, 2025

### Device management

#### Redirection performance improvement

Admins now have the option to configure performance improvements for Windows App on Windows operating systems drive redirection. For more information, see [Configure fixed, removable, and network drive redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-configure-drives-storage?tabs=intune&amp;pivots=windows-365).

## Week of March 10, 2025

### Provisioning

#### Windows 365 support for Mexico Central

Windows 365 Enterprise now supports the Mexico Central region in the Central America geography. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

#### Windows 365 support for Spain Central

Windows 365 Enterprise now supports the Spain Central region in the European Union geography. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

## Week of February 26, 2025 (Service release 2502)

### Windows App

#### Support for FIDO devices and passkeys on Android (preview)

Windows App and the Remote Desktop app for Android now support FIDO devices and passkeys for Microsoft Entra ID sign in on brokered and unbrokered devices. For more information, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#cloud-service-authentication).

#### Intune Mobile Application Management (MAM) support on Windows App on Android (preview) for devices running Android 15

Intune MAM policies can now be applied to Windows App on Android (preview) when the device is running on Android 15. Previously, Windows App could run on Android 15, but MAM policies wouldn’t take effect.

## Week of February 3, 2025 (Service release 2501)

### Device management

#### Storage access tier selection when placing Cloud PC under review

To help lower your storage costs, hot, cool, cold and archive tiers can now be selected when placing a Cloud PC under review. To help with compliance it is now also possible to place a Cloud PC under review onto hot, cool and cold access tiers configured with immutability support.

#### New Device Type filter on All Cloud PCs page

The new Device Type filter on the All Cloud PCs page lets you filter the results by the type of Cloud PC (Enterprise, Frontline, Dev Box, Power Automate).

### Provisioning

#### Windows 365 support for Japan West

Windows 365 Enterprise will support the Japan West region in the Japan geography. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

#### Schedule bulk reprovisioning for Windows 365 Frontline Cloud PCs in Shared mode

You can now schedule bulk reprovisioning for Windows 365 Frontline Cloud PCs in Shared mode. For more information, see [Bulk reprovision Windows 365 Frontline Cloud PCs in Shared mode](windows-365-flex-shared-bulk-reprovision#schedule-bulk-reprovision-windows-365-flex-cloud-pcs-in-shared-mode).

### Windows 365 Frontline

#### More precise Windows 365 Frontline concurrency control

You can now allocate concurrent sessions for Windows 365 Frontline Cloud PCs in Dedicated mode for each Microsoft Entra group assigned in the provisioning policy. This lets you reserve sessions to specific groups so sessions won't be consumed by other groups, and help you control your maximum concurrency limits.

## Week of December 17, 2024

### Device management

#### Restore, restart, and troubleshoot actions in the Cloud PCs that aren't available report

You can now use the **Bulk device actions** command on the **Cloud PCs that aren't available** report to restore, restart, and troubleshoot actions directly from the report. For more information, see [Cloud PCs that aren't available report](report-cloud-pcs-not-available).

## Week of December 9, 2024

### Device management

#### Move selected Cloud PCs to a new region

You can now move selected Cloud PCs to a new region. This is instead of moving all Cloud PCs in a provisioning policy.

## Week of December 2, 2024 (Service release 2411)

### Device management

#### Intune scope tags are now generally available

Windows 365 support for [Intune scope tags](/en-us/mem/intune/fundamentals/scope-tags) has moved out of preview and into general availability. For more information, see [Scope tags](role-based-access#scope-tags).

#### Create and share restore points for up to 5,000 Cloud PCs

You can now bulk create restore points for up to 5,000 Cloud PCs. You can then share the restore points to a specified Azure storage account. For more information, see [Create multiple manual restore points in bulk](create-manual-restore-point#create-multiple-manual-restore-points-in-bulk).

### Monitor and troubleshoot

#### Dedicated and shared data on Connected Frontline Cloud PCs report

The Connected Frontline Cloud PCs report now shows:

- Separate data for dedicated versus shared Frontline Cloud PCs.
- The user that is currently connected and their session length
- Ability to restart Frontline Cloud PCs to disconnect user from their session and bring concurrency below threshold limits.

For more information, see [Connected Frontline Cloud PCs](report-connected-windows-365-flex-cloud-pcs).

#### Cloud PC actions report support for moving Cloud PCs

You can use the Cloud PC actions report to see the status of moving Cloud PCs to new regions.

#### Windows 365 Government supports bulk Troubleshoot action

The Troubleshoot remote action can now be used in bulk with Windows 365 Government. For more information, see [Remotely manage Windows 365 devices](remotely-manage-cloud-pc).

### Provisioning

#### Azure network connection limit increased

The Azure network connection limit for each tenant has been increased. For more information, see [Maximum azure network connections](azure-network-connections#maximum-azure-network-connections).

### Provisioning

#### Windows 365 now supports Israel Central

Windows 365 Enterprise now supports the Israel Central region in the Middle East geography. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

## Week of November 19, 2024

### Windows 365 Frontline

#### Windows 365 Frontline in Shared mode (preview)

Windows 365 Frontline in Shared mode gives you the ability to provision a collection of Cloud PCs that can be used across multiple users mapped to a Microsoft Entra ID group. One active Cloud PC is permitted per license. For more information, see [Windows 365 Frontline in Shared mode](introduction-windows-365-flex#windows-365-flex-in-shared-mode).

### Device management

#### Configure client device redirection settings for Windows App on iOS/iPadOS/Android using Microsoft Intune

You can now use Microsoft Intune Mobile Application Management to check for device posture and manage redirections for Windows App on iOS, iPadOS, and Android (preview). You can use Microsoft Intune on both corporate managed and personal devices.

### Device security

#### Support for FIDO devices and passkeys on macOS and iOS

Windows App and the Remote Desktop app for macOS and iOS now support FIDO devices and passkeys for Microsoft Entra ID sign in on brokered and unbrokered devices. For more information, see [Support for FIDO2 authentication with Microsoft Entra ID](/en-us/entra/identity/authentication/concept-fido2-compatibility#native-application-support).

### Partners

#### Use Citrix HDX Plus with Windows 365 Frontline

You can now use Citrix HDX Plus with Windows 365 Frontline Cloud PCs.

## Week of October 28, 2024 (Service release 2410)

### Device management

#### Bulk Troubleshoot action now generally available

The Troubleshoot action in bulk has moved out of preview and into general availability.

For more information, see [Remotely manage Windows 365 devices](remotely-manage-cloud-pc).

#### Microsoft Remote Desktop iOS client now supports Yubikey smart card redirection

The Microsoft Remote Desktop iOS client now supports smart card redirection for YubiKeys using USB-C or Lightning connector. This enables in-session smart card usage.

### Monitor and troubleshoot

### Update to Cloud PC action status report

The Cloud PC action status report now shows batches of devices on which actions were triggered. You can see the batch current progress. For more information, see [Cloud PC actions report](report-cloud-pc-actions).

### Azure network connections inactive state

Azure network connections that meet either of the following conditions for more than four weeks are now marked as inactive:

- ANCs that aren't associated with provisioning policies.
- ANCs with provisioning policies that have no Cloud PCs associate with them.

#### Cloud PC connection quality report now available for Windows 365 Government

The Cloud PC connection quality report is now available for Windows 365 Government, both Government Community Cloud (GCC) and GCC-High. For more information, see [Cloud PC connection quality report](report-cloud-pc-connection-quality).

## Week of October 21, 2024

#### Windows 365 support for AVC mixed mode when MMR isn't enabled (preview)

AVC Mixed Mode is now available in the default graphics profile. When MMR isn't enabled, AVC/h.264 is used to encode detected image content instead of the RemoteFX image encoder. This improves performance when encoding images relative to bitrate and framerate in network-constrained scenarios.

## Week of October 14, 2024

### Device security

#### New Windows 365 IP subnet for RDP connectivity

Core TCP-based RDP traffic for Cloud PC connections uses the \*.wvd.microsoft.com wildcard fully qualified domain name (FQDN). The FQDN remains unchanged, but the underlying IP addresses associated with it will shortly be changed to a single subnet. This will simplify optimization of this traffic and reduce the need for future change management.

### Device management

#### Call redirection

Windows 365 now supports multimedia redirection call redirection. For more information, see [Use multimedia redirection](/en-us/azure/virtual-desktop/multimedia-redirection).

### Partners

#### HP Anyware for Windows 365 is now generally available

HP Anyware for Windows 365 has moved out of preview and into general availability.

For more information, see [Set up HP Anyware for Windows 365 Enterprise](hp-anyware-set-up)

## Week of September 30, 2024 (Service release 2409)

### Monitor and troubleshoot

#### Unavailable Cloud PCs report added to Reporting overview page

The **Cloud PCs that aren't available** report has been added to the **Reports** &gt; **Cloud PC overview** page.

### Device provisioning

#### Windows 11 24H2 cloud PCs gallery images

The latest Windows Enterprise 24H2 images are available for provisioning new devices. You can update your provisioning policies to use either of the following images:

- Windows 11 Enterprise 24H2
- Windows 11 Enterprise + Microsoft 365 Apps 24H2

## Week of September 23, 2024

### Device management

#### Windows 11 Cloud PCs now support EN-NZ

Windows 365 Cloud PCs now support EN-NZ for Windows 11.

## Week of September 16, 2024

### Device management

#### Support for symmetric NAT with RDP Shortpath

RDP Shortpath in Windows 365 now supports establishing an indirect UDP connection using Traversal Using Relays around NAT (TURN) for symmetric NAT. TURN is a popular standard for device-to-device networking for low latency, high-throughput data transmission with Azure Communication Services. For more information about TURN and Azure Communication Services, see [Network Traversal Concepts](/en-us/azure/communication-services/concepts/network-traversal). For more information about RDP Shortpath, see [Use RDP Shortpath for public networks with Windows 365](rdp-shortpath-public-networks).

### Windows 365 support for HEVC video coding

Windows 365 will support Hardware High Efficiency Video Coding (HEVC) h.265 4:2:0 on Compatible GPU-enabled Cloud PCs. For more information, see [Enable GPU acceleration for Azure Virtual Desktop](/en-us/azure/virtual-desktop/enable-gpu-acceleration?tabs=intune).

### Windows App

#### Windows App is now generally available

Windows App has moved out of preview and into general availability.

For more information, see [What is Windows App?](/en-us/windows-app/overview)

## Week of August 26, 2024 (Service release 2408)

### Apps

#### Azure Monitor support on Windows 365 Cloud PCs

Azure Monitor Agent can now be installed on Windows 365 Enterprise and Windows 365 Government Cloud PCs. For more information, see [Azure Monitor overview](/en-us/azure/azure-monitor/overview).

### Device security

#### Session lock experience configuration for single sign-on

You can now configure the remote session lock experience when single sign-on is enabled between the default disconnect behavior and showing the remote lock screen. For more information, see [Configure single sign-on for Windows 365 using Microsoft Entra authentication](configure-single-sign-on).

#### Windows 365 support for Microsoft Purview Customer Key is now generally available

Windows 365 support for encrypting Cloud PCs by setting up Microsoft Purview Customer Key has moved out of preview and into general availability. For more information, see [Service encryption with Microsoft Purview Customer Key](/en-us/purview/customer-key-overview).

## Week of August 5, 2024

### Documentation

#### Updated documentation article: Windows 365 service resilience

We’ve created a new article explaining Windows 365 service resilience. For more information, see [Windows 365 service resilience](resilience).

## Week of July 29, 2024 (Service release 2407)

### Device management

#### Uni-directional clipboard support is now generally available

Uni-directional clipboard support for Cloud PCs has moved out of preview and is now generally available. For more information, see [Configure the clipboard transfer direction and types of data that can be copied in Azure Virtual Desktop](/en-us/azure/virtual-desktop/clipboard-transfer-direction-data-types).

#### Closing port 3389 by default for newly provisioned and reprovisioned Cloud PCs

To help secure your Windows 365 environment, the inbound port 3389 is now closed by default.

#### Windows 365 support for AVC mixed mode when MMR isn't enabled (preview)

Windows 365 now supports AVC mixed mode when MMR is not enabled.

### Device security

#### Windows 365 Government now supports Customer Lockbox

Windows 365 Government now supports Microsoft Purview Customer Lockbox.

For more information, see [Microsoft Purview Customer Lockbox](/en-us/purview/customer-lockbox-requests).

### Monitor and troubleshoot

#### New Intune report and device action for Windows enrollment attestation (public preview)

Use the new device attestation status report in Microsoft Intune to find out if a device has attested and enrolled securely while being hardware-backed. For more information, see [Device attestation status report](/en-us/mem/intune/fundamentals/reports#device-attestation-status-report).

### Partners

#### Support for Omnissa Horizon clients and the Blast protocol with Windows 365 Enterprise is now generally available

Support for Omnissa (previously VMware) Horizon clients and the Blast protocol with Windows 365 Enterprise Cloud PCs has moved out of preview and into general availability. For more information, see [Set up Omnissa Horizon for Windows 365 Enterprise](set-up-omnissa-horizon).

### Provisioning

#### New GPU offerings for Cloud PCs are now generally available

New GPU offerings for Window 365 Enterprise Cloud PCs have moved out of preview and into general availability. For more information, see [GPU Cloud PCs](gpu-cloud-pc).

### Windows 365 Frontline

#### The Windows 365 Frontline concurrency buffer is now generally available

The Windows 365 concurrency buffer has moved out of preview and into general availability.

## Week of July 23, 2024

### Updated default settings for Windows 365 security baselines

Several Windows 365 Security baseline default values have changed. For a full list of all the updated settings, see [List of the settings in the Windows 365 Cloud PC security baseline in Intune](/en-us/mem/intune/protect/security-baseline-settings-windows-365).

## Week of July 15, 2024

### Cloud PC support for FIDO devices and passkeys on macOS and iOS (preview)

Windows 365 Cloud PCs now support FIDO devices and passkeys for Microsoft Entra ID sign in on macOS and iOS.

## Week of July 8, 2024

### Device management

### Chroma subsampling default change to 4:2:0

To reduce monitor support issues, the Windows 365 service now defaults the chroma subsampling at 4:2:0. (instead of the previous 4:4:4). For more information, see [Change the default chroma value for Windows 365 Cloud PCs](chroma-value-change-default).

## Week of July 1, 2024

### Apps

#### Windows 365 Cloud PC gallery images use new Teams VDI

Windows 365 Cloud PC gallery images now use the new Teams Virtualized Desktop Infrastructure (VDI). For more information, see [Microsoft Teams on a Cloud PC](teams-on-cloud-pc) and [New VDI solution for Teams](/en-us/MicrosoftTeams/vdi-2).

### Device management

#### Cross region disaster recovery

Windows 365 now supports cross region disaster recovery. For more information, see [Cross region disaster recovery in Windows 365](cross-region-disaster-recovery).

## Week of June 24, 2024 (Service release 2406)

### Device management

#### Windows 365 Boot and Windows 365 Switch now support battery status redirection

Windows 365 Boot and Windows 365 Switch now support battery status redirection. Cloud PCs now show the local PC's battery status.

#### Upgrade Windows 365 licenses in Microsoft admin center

Customers that have Modern Microsoft Cloud Agreements can upgrade their existing Windows 365 licenses in the Microsoft Admin Center.

### Device security

#### Single sign-on Windows 365 clients authentication change

Single sign-on for Windows 365 is transitioning to use the Windows Cloud Login Entra ID cloud app for Windows authentication starting with the Windows and Web clients. For more information, see [Set Conditional Access policies](set-conditional-access-policies).

### Monitor and troubleshoot

#### Windows 365 Government now supports Cloud PC utilization report

Windows 365 Government now supports the Cloud PC utilization report. For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### Cloud PC size recommendation report is now generally available

The Cloud PC size recommendation report has moved out of preview and is now generally available. For more information, see [Cloud PC recommendations report](report-cloud-pc-recommendations).

## Week of June 3, 2024 (Service release 2405)

### Device security

#### Windows 365 support for Microsoft Purview forensic evidence

Windows 365 now supports [Microsoft Purview forensic evidence](/en-us/purview/insider-risk-management-forensic-evidence). For more information, see [Set up forensic evidence](forensic-evidence-set-up).

### Device management

#### Troubleshoot action now supports bulk

The Troubleshoot remote action can now be used in bulk. For more information, see [Remotely manage Windows 365 devices](remotely-manage-cloud-pc).

### Government Community Cloud

#### New Windows 365 Frontline offers for GCC

New Windows 365 Frontline offers are now available for Government Community Cloud (GCC) customers using the Azure Commercial cloud.

## Week of May 27, 2024

### Device management

#### New Windows 365 Cloud PC images available in the gallery

New Cloud PC gallery images for Windows 10 and Windows 11 are now available. These improved images have harmonized optimizations with Windows 365 apps images for better policy management:

- Win 10 Enterprise Cloud PC: 21H2, 22H2,
- Win 11 Enterprise Cloud PC: 21H2, 22H2, 23H2

#### Manage redirections for Cloud PCs on Android devices

You can now use the Intune admin center to manage redirections for Android users who access their Cloud PCs using Microsoft Remote Desktop.

#### Manage redirections for Cloud PCs on iOS/iPadOS devices

You can now use the Intune admin center to manage redirections for iOS/iPadOS users who access their Cloud PCs using Microsoft Remote Desktop and Windows App.

## Week of May 20, 2024

### Device management

#### Windows 365 Cloud PC gallery images now pre-install new Microsoft Teams

Gallery images for Windows 365 Cloud PCs now come with the new Microsoft Teams pre-installed (not Teams (Classic)). This applies to Windows Enterprise 11 23H2 and 22H2. For more information, see [Gallery images](device-images#gallery-images).

## Week of May 6, 2024 (Service release 2404)

### Device security

#### FQDNs removed from requirement list

Many required FQDNs were previously moved to the \*.infra.windows365.microsoft.com wildcard FQDN. The old FQDNs are now being removed. For an updated list of FQDNs, see [Network requirements](requirements-network).

### Monitor and troubleshoot

#### Cloud PCs that aren't available report is now generally available

The **Cloud PCs that aren't available report** has moved out of preview and into general availability. For more information, see [Cloud PCs that aren't available report](report-cloud-pcs-not-available).

### Role-based access control

#### Intune scope tags (preview)

Windows 365 now supports [Intune scope tags](/en-us/mem/intune/fundamentals/scope-tags). For more information, see [Scope tags](role-based-access#scope-tags).

## Week of April 10, 2024

### Partners

#### Use HP Anyware for Windows 365 Enterprise (preview)

You can now use HP Anyware for Windows 365 Enterprise Cloud PCs. For more information, see [Set up HP Anyware for Windows 365 Enterprise](hp-anyware-set-up).

## Week of April 1, 2024

### Device management

#### Step-up licenses now support storage

For Windows 365, step-up licenses now support storage. For more information, see [Resize with Step-up Licenses](resize-cloud-pc#resize-with-step-up-licenses).

## Week of March 26, 2024 (Service release 2403)

### Device management

#### Concurrency buffer for Windows 365 Frontline Cloud PCs

A new concurrency buffer lets you exceed the max concurrency count for a limited time under certain circumstances, like during shift changes. For more information, see [Concurrency buffer](concurrency-buffer).

#### Maintenance windows (public preview)

You can now set maintenance windows for running remote actions on Cloud PCs. This will notify users in-session about the impending remote action period. For more information, see [Cloud PC maintenance windows](cloud-pc-maintenance-windows).

#### Bulk remote action support

You can now use bulk actions with the following remote actions: Restore, Restart, Resize, and Reprovision. For more information, see [Remotely manage Windows 365 devices](remotely-manage-cloud-pc).

### Device security

#### Microsoft Purview Data Loss Prevention support for Windows 365 Enterprise

Microsoft Purview Data Loss Prevention (DLP) now supports Windows 365 Enterprise. For more information, see [Endpoint DLP support for virtualized environments](/en-us/purview/endpoint-dlp-getting-started#endpoint-dlp-support-for-virtualized-environments).

#### Windows 365 Boot Shared mode supports FIDO

Windows 365 Boot Shared mode now supports FIDO. For more information, see [How-to: Password-less FIDO2 Security Key Sign-in to Windows 10 HAADJ Devices](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/how-to-password-less-fido2-security-key-sign-in-to-windows-10/ba-p/1434583).

### Documentation

#### Updated documentation article: Known issues

We’ve updated the article [Known issues: Windows 365 Enterprise and Frontline](known-issues-enterprise#teams-isnt-enforcing-screen-capture-protection), add a known issue for Teams isn't enforcing screen capture.

### Miscellaneous

#### Microsoft Graph APIs support for Windows 365 v1.0 workloads

In addition to Beta workloads, the Microsoft Graph APIs now support Windows 365 as v1.0 workloads. For more information, see [Use Microsoft Entra ID to access the Windows 365 APIs in Microsoft Graph](permission-scopes).

### Monitor and troubleshoot

#### Cloud PC utilization report creation date

The Cloud PC utilization report now shows the Cloud PC creation date. For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### Cloud PC size recommendation report (public preview)

A new Intune admin center report recommends appropriate sizes for Cloud PCs to better fit your organization's needs. For more information, see [Cloud PC recommendations report](report-cloud-pc-recommendations).

#### Improvements to Cloud PC connection quality report are now generally available

Improvements to the Cloud PC connection quality report have moved out of preview and into general availability. These improvements include:

- a more comprehensive view of the overall performance of their Cloud PCs.
- a more detailed view of devices when they are in a state of poor performance due to high round trip times.
- Tenant level visibility to most recent/current for:
    - Round Trip Time.
    - Bandwidth.
    - Connection Time.
    - UDP Utilization.
- Connection specific detail on client IP and associated CPC Gateway.
- Filters for all columns.

For more information, see [Cloud PC connection quality report](report-cloud-pc-connection-quality).

### Windows 365 Frontline

#### Windows 365 Frontline support for power on/off in bulk

You can now use bulk actions to turn on/off Windows 365 Frontline Cloud PCs.

## Week of March 11, 2024

### Documentation

#### Updated documentation article: Forced browser sign-in setting for Cloud PC gallery images

We’ve updated the article [Device images overview](device-images#gallery-images), noting that gallery images have [forced browser sign-in](/en-us/deployedge/microsoft-edge-policies#browsersignin) pre-applied.

## Week of March 4, 2024 (Service release 2402)

### Monitor and troubleshoot

#### Alerts for Windows 365 Frontline maximum concurrent Cloud PCs

A new alert notifies admins when the maximum concurrent Cloud PCs are active for Windows 365 Frontline subscriptions.

#### Cloud PC utilization report now generally available

The **Cloud PC utilization** report has moved out of preview and into general availability. For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### Device action data kept for 90 days

On the **Overview** page for individual Cloud PCs, the **Actions** will show actions performed within the last 90 days.

### Windows 365 Switch

#### Windows 365 Switch support for Windows 365 Frontline

Windows 365 Switch now supports Windows 365 Frontline Cloud PCs. For more information, see [Windows 365 Switch](windows-365-switch-overview).

### Device management

#### Offline Windows 365 Frontline Cloud PCs update sync

Windows 365 Frontline Cloud PCs that haven’t been used for seven days are now automatically turned on and synced with Windows Update client policies.

#### Admins can remotely power on and off Windows 365 Frontline Cloud PCs

Admins can now power on and off Windows 365 Frontline Cloud PCs using remote actions. For more information, see [Remotely manage Windows 365 devices](remotely-manage-cloud-pc).

#### Uni-directional clipboard support (preview)

You can now configure uni-directional clipboard for Cloud PCs that have Windows Insider Build 25898 or later. For more information, see [Configure the clipboard transfer direction and types of data that can be copied in Azure Virtual Desktop](/en-us/azure/virtual-desktop/clipboard-transfer-direction-data-types).

### Device security

#### Customer Lockbox support is now generally available

Windows 365 Enterprise and Frontline support for Microsoft Purview Customer Lockbox has moved out of preview and is now generally available.

For more information, see [Microsoft Purview Customer Lockbox](/en-us/purview/customer-lockbox-requests).

## Week of February 26, 2024

### Device security

#### New faster sign-in frequency option (preview)

When single sign-on is enabled, selecting the **Conditional Access** &gt; **Session** &gt; **Sign-in frequency** &gt; **Every time** option provides a faster reauthentication period of 5-10 minutes depending on the client used. For more information, see [Set Conditional Access policies](set-conditional-access-policies).

### Windows 365 Boot

#### Shared and dedicated Windows 365 Boot device modes are now generally available

Windows 365 Boot shared and dedicated device modes have moved out of preview and into general availability.

For more information, see [What is Windows 365 Boot?](windows-365-boot-overview) and [Guided scenario - deploy Windows 365 Boot to shared physical devices](windows-365-boot-guide).

#### Windows 365 Boot sign-in page customization is now generally available

Windows 365 Boot support for sign-in page customization has moved out of preview and into general availability. For more information, see [Guided scenario - deploy Windows 365 Boot to shared physical devices](windows-365-boot-guide).

#### Windows 365 Boot fail fast notifications are now generally available

Windows 365 Boot detection and notification of network or application setup issues has moved out of preview and into general availability.

#### Manage local PC settings through Windows 365 Boot is now generally available

User management of local PC settings through their Windows 365 Boot Cloud PC has moved out of preview and into general availability.

### Windows 365 Switch

#### Windows 365 Switch desktop identifiers are now generally available

Windows Task view identifiers for Cloud PC or local PC have moved out of preview and into general availability.

#### Windows 365 Switch improved disconnecting is now generally available

The ability for users to seamlessly disconnect from their Cloud PC without leaving their local desktop has moved out of preview and into general availability. For more information, see [Windows 365 Switch](https://support.microsoft.com/en-us/windows/windows-365-switch-4ea65cc3-05ff-4166-ac8b-389af27108f8).

#### Windows 365 Switch connection status now generally available

Connection status and timeout information on the connection screen for Windows 365 Switch with Windows 365 Frontline Cloud PCs has moved out of preview and into general availability.

## Week of January 29, 2024 (Service release 2401)

### Device security

#### FQDN requirement changes

Many required FQDNs have been moved to the \*.infra.windows365.microsoft.com wildcard FQDN. This move reduces the initial configuration requirements and the change rate of connectivity requirements. For Windows 365 Government, the FQDNs were moved to \*.infra.windows365.microsoft.us. To avoid any issues when provisioning new Cloud PCs, you must make sure that *.infra.windows365.microsoft.com (*.infra.windows365.microsoft.us for Windows 365 Government) is an accessible endpoint in your network allow list.

### End user experience

#### End users can restart their Windows Cloud PC using the keyboard

For newly created Cloud PCs, end users can now restart or shut down their Cloud PC by using the keyboard combination CTL+ALT+DEL. This doesn't apply to Cloud PCs created before 1/31/2024.

## Week of January 15, 2024

### Documentation

#### Updated documentation article: Relative performance for different Cloud PC sizes

We’ve updated the article and added performance information for additional Cloud PC sizes. For more information, see [Relative performance for different Cloud PC sizes](../relative-cloud-pc-performance).

## Week of January 8, 2024 (Service release 2312)

### Monitor and troubleshoot

#### New alert rule: Cloud PCs that aren't available (preview)

A new alert rule is now available to notify you when Cloud PCs aren't available. For more information about alerts in general, see [Alerts in Windows 365](alerts). For more information about the report, see [Cloud PCs that aren't available report](report-cloud-pcs-not-available). This feature is not yet available for Windows 365 Frontline.

### Provisioning

#### Windows 365 now supports Italy North and Poland Central

Windows 365 Enterprise and Windows 365 Frontline Cloud PC now support the Italy North and Poland Central regions. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

### Windows 365 Boot

#### Manage local PC settings through Windows 365 Boot (preview)

Users can now access and manage local PC settings more easily from their Windows 365 Boot Cloud PC. These include sound, display, and other device specific settings of their local PC. Settings can be found by going to Start &gt; **Settings** in the Cloud PC.

#### Windows 365 Boot sign-in page customization (preview)

Windows 365 Boot now supports customizing the Cloud PC sign-in page with company logo branding for Cloud PCs in shared PC mode. For more information, see [Guided scenario - deploy Windows 365 Boot to shared physical devices](windows-365-boot-guide).

#### Windows 365 Boot device modes - shared and dedicated (preview)

Windows 365 Boot now supports two modes of signing in to a Cloud PC from a physical device:

- Shared PC mode: Multiple users can use the same physical device to sign in to their own Cloud PCs through the Windows 11 sign-in screen.
- (New) Dedicated PC mode: The physical device is assigned to a specific user to sign in to their Cloud PC through the Windows 11 sign-in screen.

For more information, see [What is Windows 365 Boot?](windows-365-boot-overview) and [Guided scenario - deploy Windows 365 Boot to shared physical devices](windows-365-boot-guide).

#### Windows 365 Boot fail fast notifications (preview)

To speed up the sign-in process, Windows 365 Boot now detects network or application setup issues and notifies the users about them immediately during the sign-in process.

### Windows 365 Switch

#### Windows 365 Switch improved disconnecting (preview)

Users can now seamlessly disconnect from their Cloud PC without leaving their local desktop. For more information, see [Windows 365 Switch](https://support.microsoft.com/en-us/windows/windows-365-switch-4ea65cc3-05ff-4166-ac8b-389af27108f8).

#### Windows 365 Switch desktop identifiers (preview)

When switching between desktops using Task view, each desktop is identified as a Cloud PC or Local PC.

#### Windows 365 Switch connection status (preview)

When using Windows 365 Switch with Windows 365 Frontline Cloud PCs, users now see connection status and timeout information on the connection screen. In case of an error, users can copy the correlation ID to help with resolving the issue.

## Week of December 10, 2023

### Device security

#### Windows 365 support for Microsoft Purview Customer Key (preview)

Windows 365 now supports encrypting Cloud PCs by setting up Microsoft Purview Customer Key. For more information, see [Service encryption with Microsoft Purview Customer Key](/en-us/purview/customer-key-overview).

## Week of December 04, 2023 (Service release 2311)

### Device management

#### Windows 365 Boot is now available for Windows 365 Government

Windows 365 Boot is now available for US Government Community Cloud (GCC) customers using Windows 365 Government. For more information, see [What is Windows 365 Boot?](windows-365-boot-overview).

### End user experience

#### UI change in web client

The gear icon menu has been updated.

#### New Microsoft Teams app is now generally available for Windows 365

The new Microsoft Teams app has moved out of preview and into general availability. It's been optimized for faster performance and more efficient resource use on Cloud PCs. For more information, see [Upgrade to new Teams for Virtualized Desktop Infrastructure](/en-us/microsoftteams/new-teams-vdi-requirements-deploy).

The new Microsoft Teams app is not yet available in the Windows 365 gallery images.

### Monitor and troubleshoot

#### New report: Action status (preview)

A new report is now available that lets you know which actions have been performed successfully on Cloud PCs. For failed actions, possible reasons will also be provided. For more information, see [Cloud PC actions report](report-cloud-pc-actions).

#### New filter option for the Connected Frontline Cloud PCs report

A new filter is available in the Connected Frontline Cloud PCs report. This new filter shows hourly data for various data periods. For more information, see [Connected Frontline Cloud PCs report (preview)](report-connected-windows-365-flex-cloud-pcs).

## Week of November 13, 2023

### Device security

#### Screen capture protection in Windows 365 settings catalog

You can now implement screen capture protection for your Cloud PCs by using the settings catalog. Alongside watermarking, screen capture is a deterrent to data leaks and data loss. For more information, see [Enable screen capture protection in Azure Virtual Desktop](/en-us/azure/virtual-desktop/screen-capture-protection) and [Configure the administrative template](/en-us/azure/virtual-desktop/administrative-template?tabs=intune#configure-the-administrative-template).

This feature isn’t supported on Android, iOS, or web clients. Enabling this feature blocks users from accessing their Cloud PCs when using these clients.

#### Watermarking support in Windows 365 settings catalog

You can now implement watermarking for your Cloud PCs by using the settings catalog. Alongside screen capture, watermarking is a deterrent to data leaks and data loss. For more information, see [Watermarking in Azure Virtual Desktop](/en-us/azure/virtual-desktop/watermarking) and [Configure the administrative template](/en-us/azure/virtual-desktop/administrative-template?tabs=intune#configure-the-administrative-template).

#### Customer Lockbox support (preview)

Windows 365 Enterprise and Frontline now support Microsoft Purview Customer Lockbox.

For more information, see [Microsoft Purview Customer Lockbox](/en-us/purview/customer-lockbox-requests).

### Provisioning

#### Single sign-on is now generally available

The following single sign-on updates have moved out of preview and are now generally available:

- Single sign-on for Microsoft Entra joined and Microsoft Entra hybrid joined Cloud PCs.
- You can turn on single sign-on separately for each provisioning policy to apply it to new Cloud PCs.
- You can apply single sign-on to existing Cloud PCs.
- A new Azure Network Connection check for Microsoft Entra hybrid joined provisioning policies to make sure that the domain is properly configured for single sign-on.

These updates are also available for Windows 365 Frontline.

#### New GPU offerings for Cloud PCs (preview)

Three new GPU offerings are now available for Window 365 Enterprise Cloud PCs. For more information, see [GPU Cloud PCs.](gpu-cloud-pc)

### End user experience

#### Windows App now available in public preview

Windows App lets users securely connect to Windows devices and apps. Supported remote devices include:

- Azure Virtual Desktop
- Windows 365 Cloud PC
- Microsoft Dev Box
- Remote Desktop Services
- Remote PC

Windows App is available for Windows, macOS, iOS and iPadOS, and web browsers.

For more information, see [What is Windows App?](/en-us/windows-app/overview)

## Week of October 30, 2023 (Service release 2310)

### Device management

#### Permissions update for placing a Cloud PC under review

You now need an additional role, Storage Blob Data Contributor, to place a Cloud PC under review. For more information, see [Place a Windows 365 Enterprise Cloud PC under review](place-cloud-pc-under-review).

### Device provisioning

#### Two new sizes for Cloud PCs

Two new sizes are now available for Windows 365 Cloud PCs:

- 16vCPU/64GB RAM/512GB storage​
- 16vCPU/64GB RAM/1TB storage

These 16 vCPU licenses can be purchased and assigned in the same way that you purchase and assign other Windows 365 licenses.

#### New gallery images

Two new gallery images are now available for Windows 365 Cloud PCs:

- Windows 11 Preview + Microsoft 365 Apps 23H2
- Windows 11 Preview + OS Optimizations 23H2

You can choose the new gallery images when [creating a provisioning policy](create-provisioning-policy).

### Miscellaneous

#### New Graph API for Windows 365 Frontline

A new graph API is now available for Windows 365 Frontline.

### Monitor and troubleshoot

#### Audit logs supported in Azure Log Analytics

You can now send Windows 365 audit log data directly to Azure Log Analytics, Event Hub, or certain third-party solutions. For more information, see [Send Windows 365 audit logs to diagnostic settings in Azure Monitor](get-cloud-pc-audit-logs-using-powershell#send-windows-365-audit-logs-to-diagnostic-settings-in-azure-monitor).

## Week of September 25, 2023 (Service release 2309)

### Device management

#### The resize action is now generally available

The resize action has moved out of preview and into general availability. This feature is also available for both Windows 365 Government and Windows 365 Government customers using Windows 365 Enterprise. The resize action isn't currently available for Windows 365 Frontline. For more information, see [Resize a Cloud PC](resize-cloud-pc).

#### Windows 365 Boot is now generally available

Windows 365 Boot has moved out of preview and into general availability. For more information, see [What is Windows 365 Boot?](windows-365-boot-overview) This feature isn't currently available for Windows 365 Government.

### Monitor and troubleshoot

#### New filter options in the Cloud PC utilization report

Two new filter options are now available for the **Cloud PC utilization** report:

- **Date last connected** filter option: **No connection within the last 60 days**
- **Time connected** filter option: **None (0 hours)**

For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### New report: Cloud PCs that can't connect

A new report is now available that provides metrics that help admins evaluate tenant level device connection status and reliability. For example, you can observe:

- devices that have unhealthy hosts.
- users' connections that consistently or frequently fail.
- systemic issues, like an Azure infrastructure issue, that is impacting the ability of a user to connect.

For more information, see [Cloud PCs that aren't available report](report-cloud-pcs-not-available).

#### Improvements to Cloud PC connection quality report

Improvements to the Cloud PC connection quality report include:

- A more comprehensive view of the overall performance of their Cloud PCs.
- A more detailed view of devices when they are in a state of poor performance due to high round trip times.
- Tenant level visibility to most recent/current for:
    - Round Trip Time.
    - Bandwidth.
    - Connection Time.
    - UDP Utilization.
- Connection specific detail on client IP and associated CPC Gateway.
- Filters for all columns.

### Provisioning

#### Single sign-on updates

The following updates related to single sign-on are now available:

- [Public preview features](../public-preview).
    - Single sign-on for Microsoft Entra hybrid join Cloud PCs.
    - You can turn on single sign-on separately for each provisioning policy.
    - A new Azure Network Connection check to make sure that the network is properly configured for single sign-on.
    - Apply single sign-on to existing Microsoft Entra joined and Microsoft Entra hybrid joined Cloud PCs.

For more information, see [Create provisioning policy](create-provisioning-policy) and [Edit provisioning policy](edit-provisioning-policy).

### End user experience

#### Windows 365 Switch is now generally available

Windows 365 Switch has moved out of preview and into general availability. For more information, see [Windows 365 Switch](windows-365-switch-overview). This feature isn't currently available for Windows 365 Government.

## Week of September 18, 2023

### Documentation

#### Windows 365 help documentation updated for Microsoft Entra ID

Windows 365 help documentation has been updated for the rebranding of Azure Active Directory to Microsoft Entra ID. For more information, see [New name for Azure Active Directory](/en-us/azure/active-directory/fundamentals/new-name). Some areas of the Microsoft Intune user interface haven't yet been updated to Microsoft Entra ID, so you might see differences until those updates are made.

## Week of August 28, 2023 (Service release 2308)

### Monitor and troubleshoot

#### System alerts and email notifications are now generally available

System alerts and email notifications have moved out of preview and into general availability. For more information, see [Alerts](alerts).

#### New report: Connected Frontline Cloud PCs

The Connected Frontline Cloud PCs report is now available. For more information, see [Connected Frontline Cloud PCs report](report-connected-windows-365-flex-cloud-pcs).

#### Endpoint Analytics resource performance report now available to GCCH customers

The Endpoint Analytics resource performance report is now available to Government Community Cloud High (GCCH) customers. For more information, see [Resource performance report](report-resource-performance).

#### New Cloud PC overview report page

All Cloud PC reports can now be accessed from the **Cloud PC overview** section under **Device management**.

## Week of August 21, 2023

### Partners

#### Use VMWare Horizon clients and the Blast protocol with Windows 365 Enterprise (public preview)

VMWare Horizon clients and the Blast protocol can be used with Windows 365 Enterprise Cloud PCs. This is a [public preview](../public-preview). For more information, see [Set up VMware Horizon for Windows 365 Enterprise](set-up-omnissa-horizon).

## Week of August 7, 2023

### End user experience

#### Windows 11 Task view support for Cloud PCs (preview)

Windows 365 Switch lets users connect to their Cloud PC by using the Windows 11 Task view. They can also use Task view to switch between their Cloud PC and their local device. For more information, see [Windows 365 Switch](windows-365-switch-overview) and the [Windows 365 Switch end user help article](https://support.microsoft.com/windows/windows-365-switch-4ea65cc3-05ff-4166-ac8b-389af27108f8).

#### LG webOS 23 support on windows365.microsoft.com

The Windows 365 web site, windows365.microsoft.com, now supports LG webOS 23.

### Security

#### Tamper protection support for Windows 365

Windows 365 now supports use of endpoint security Antivirus policy to manage Tamper protection for Windows 365 Cloud PCs. Support for Tamper protection requires devices to onboard to Microsoft Defender for Endpoint before the policy that enables Tamper protection is applied.

## Week of July 31, 2023 (Service release 2307)

### Device management

#### Move Cloud PC is now generally available

Move Cloud PC has moved out of preview and into general availability. For more information, see [Move Cloud PC](move-cloud-pc).

#### New setting to allow users to reprovision their own Cloud PC

You can now grant users permission to reset (reprovision) their own Cloud PC. For more information, see [Make a user a local admin](assign-users-as-local-admin).

### Device security

#### Azure network connection (ANC) least privilege update

A new, more secure least privilege is now available. You must manually remove the old network contributor role from the resources where the ANC was created. For more information, see [Role-based access control](role-based-access).

### Miscellaneous

#### Provide feedback button for admins is now generally available

The **Provide feedback** button has moved out of preview and into general availability.

## Week of July 17, 2023

### End user experience

#### Windows 365 web client camera support (preview)

Users can now give their Cloud PC access to their local device's camera.

## Week of July 3, 2023 (Service release 2306)

### Device management

#### Windows 365 Frontline is now generally available

Windows 365 Frontline has moved out of preview and into general availability. For more information, see [What is Windows 365 Frontline?](introduction-windows-365-flex)

#### Group-based license support for Cloud PC resizing

Both single and bulk resizing now support Cloud PCs that were provisioned with group-based licenses.

### End user experience

#### Windows365.microsoft.com Open in browser button includes Windows 365 app and Open in Remote Desktop app

Users now have two options when they select the **Open in browser** drop-down button to open a Cloud PC user session from the windows365.microsoft.com page:

- **Open in Windows 365 app**
- **Open in Remote Desktop app**

#### Windows 365 app update notifications for users

Windows 365 app users will get a notification when an update is available. If users choose to update, the app closes and they'll get a Windows notification when the update is complete.

### Monitor and troubleshoot

#### Resource performance report in Endpoint Analytics now available for Windows 365 Government

The resource performance report in Endpoint Analytics is now available for Windows 365 Government. For more information, see [Resource performance report](report-resource-performance).

#### Correlation IDs for Azure network connection notifications

The Azure network connection health check status in Microsoft Intune now includes a correlation ID. This ID helps the support team troubleshoot customer issues. Make sure to provide the ID number when you contact Microsoft support.

### Windows 365 Government

#### Windows 365 app support for Windows 365 Government environments

The Windows 365 app now supports Windows 365 Government environments.

#### Windows 365 app pin Cloud PC to task bar now supports Windows 365 Government

Windows 365 Government users can now pin their Cloud PC to the task bar in the Windows 365 app for Windows 11 platforms.

## Week of June 12, 2023

### Apps

#### Windows 365 Government support for virtualization-based workloads

Virtualization-based workloads are now supported in Windows 365 Government environments. For more information, see [Set up virtualization-based workloads on your Cloud PC](nested-virtualization).

### Documentation

#### New documentation article: High-level architecture diagram

We’ve published a new help documentation article. For more information, see [High-level architecture diagram](high-level-architecture).

## Week of June 5, 2023

### Miscellaneous

#### Microsoft 365 admin center: Windows 365 cloud PC advanced deployment guide

The Advanced deployment guides page in the Microsoft 365 admin center has a new guide to help admins plan for, deploy, and scale Windows 365 Enterprise in their organization. This guide has a checklist of Cloud PC configuration tasks and includes best practices, tools, and recommendations based on the tenant's configuration.

#### Windows 365 Enterprise can now be purchased by government customers

Windows 365 Enterprise can now be purchased by customers with an existing Government Community Cloud (GCC) tenant. Such customers can use their Azure Commercial subscription if they want to use custom images and Azure network connections. (Previously, customers with a GCC tenant could only buy Windows 365 Government. An Azure Government subscription was required for custom images and Azure network connections.) Windows 365 Enterprise is a commercial product with commercial licensing terms and conditions.

Windows 365 Enterprise is FedRAMP compliant. Except for FedRAMP, Windows 365 Enterprise doesn't offer the same compliance as Windows 365 Government. CJIS and IRS 1075 aren't supported in Windows 365 Enterprise.

### Windows 365 Government

#### Windows 365 Government setup tool

A new Windows 365 Government setup tool is now available. It replaces the PowerShell scripts that were used to set up tenant mapping and permissions. For more information, see [Set up tenants for Windows 365 Government](set-up-tenants-windows-365-gcc).

## Week of May 29, 2023 (Service release 2305)

### Device management

#### Cloud PC on-demand restore points and copy to Azure Storage account are now generally available

Cloud PC on-demand restore points and copy to an Azure Storage account have moved out of preview and into general availability. For more information, see [Create on-demand manual restore points for Cloud PCs](create-manual-restore-point) and [Share Cloud PC restore points to an Azure Storage Account](share-restore-points-storage).

#### Shortpath for managed/private networks

Managed network RDP Shortpath is available for Windows 365. For more information about RDP Shortpath in Windows 365, see [Use RDP Shortpath for private networks with Windows 365](rdp-shortpath-private-networks).

#### Move Cloud PC

A new provisioning policy option lets you define a new region or ANC for the provisioning policy. When you initiate the move:

1. All Cloud PCs in the provisioning policy that no longer match the updated region or ANC will be shut down.
2. All such Cloud PCs will be moved to the new region or ANC.

It may take several hours for the moves to complete.

New Cloud PCs created by the provisioning policy will be created in the new region or ANC.

For more information, see [Move Cloud PC](move-cloud-pc).

### Miscellaneous

#### Provide feedback button for admins (preview)

A **Provide feedback** button is now available in several Windows 365 admin pages in the Intune admin center.

### Monitor and troubleshoot

#### Admin alert when a Cloud PC enters the grace period

Admins are now alerted when a Cloud PC enters the grace period. For more information about grace periods, see [Device management overview for Cloud PCs](device-management-overview). For information about how to view and customize alerts, see [Alerts in Windows 365](alerts).

### Windows 365 app

#### Windows 365 app supports dark mode

The Windows 365 app now supports dark mode. End users have the option to set the Windows 365 app to light or dark mode, or to match system settings.

#### Windows 365 app settings support for multiple monitors

Users can now change multiple monitor setting in the Windows 365 app.

### Windows 365 Government

#### Windows 365 Government Azure Network Connection set up improvement

During Azure network connection (ANC) creation or editing, instead of copying and pasting details (like Subscription ID, and VNET name) for the ANC, you can now select options from a drop-down menu. For more information, see [Set up tenants for Windows 365 Government](set-up-tenants-windows-365-gcc).

## Week of May 22, 2023

### Device management

#### Windows 365 Boot: users can sign in directly to their Cloud PC from their physical device (preview)

Windows 365 Boot lets admins configure Windows 11 physical devices so that users can:

- Avoid signing in to their physical device.
- Sign in directly to their Windows 365 Cloud PC on their physical device.

For more information, see [What is Windows 365 Boot?](windows-365-boot-overview)

### Documentation

#### New documentation article: Using Intune, install the Windows 365 app on physical devices

We’ve published a new help documentation article. For more information, see [Using Intune, install the Windows 365 app on physical devices](install-windows-365-app-intune).

## Week of April 24, 2023 (Service release 2304)

### End user experience

#### Windows 365 web client keyboard shortcut redirection

Windows 365 web client users can now use keyboard shortcuts (like Alt + Tab) on their Cloud PC. These shortcuts would normally be intercepted by the host operating system and not sent to the Cloud PC. For more information about these keyboard shortcuts, see [Access a Cloud PC](../end-user-access-cloud-pc).

#### Windows 365 app: pin Cloud PC to task bar

End users can now pin their Cloud PC to the task bar in the Windows 365 app. This lets them launch the Cloud PC from the task bar icon without going into the connection center.

#### Windows365.microsoft.com dark mode

You now have the option to use dark mode on windows365.microsoft.com. For more information, see [Access a Cloud PC](../end-user-access-cloud-pc).

### Provisioning

#### Windows 365 now supports South Africa North and Sweden Central

Windows 365 Cloud PC now supports the South Africa North and Sweden Central regions. For more information, see [Supported Azure regions for Cloud PC provisioning](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning).

### Windows 365 Government

#### Windows 365 Government with custom images or Azure network connections

For Windows 365 Government customers, the **Custom images** and **Azure network connection** pages have been updated to make it clear that:

- Before using custom images with Windows 365 Government, you must link your Azure Commercial tenant with your Azure Government tenant.
- Before using Azure network connections with Windows 365 Government, you must link your Azure Commercial tenant with your Azure Government tenant.

## Week of April 10, 2023

### End user experience

#### Location redirection

Users can now turn on Location redirection so that their Cloud PCs use their correct geographic location. For more information, see [Location redirection](../end-user-access-cloud-pc#location-preview).

## Week of April 3, 2023

### Device management

#### Windows 365 Frontline

Windows 365 Frontline is a new version of Windows 365 that helps organizations save costs by providing a single license to provision three Cloud PC virtual machines. For each Windows 365 Frontline license that you buy, you can provision three different Cloud PCs that can’t be used concurrently. Instead, each user receives a unique Cloud PC that they can use when the other two users on the same license aren’t signed into their Cloud PCs. For more information, see [What is Windows 365 Frontline?](introduction-windows-365-flex)

#### Convert Windows 365 licenses to higher level licenses

Customers with an active direct enterprise agreement can now convert lower-level Windows 365 licenses to higher-level licenses. Reach out to your field specialist to learn more.

### Documentation

#### New documentation article: Relative performance for different Cloud PC sizes

We’ve published a new help documentation article. For more information, see [Relative performance for different Cloud PC sizes](../relative-cloud-pc-performance).

## Week of March 28, 2023 (Service release 2303)

### Device provisioning

#### Cloud PC custom name template

You can now create a template to automatically create unique names for new Cloud PCs. For more information, see [Create provisioning policies](create-provisioning-policy).

### Device security

#### FQDN tags

FQDN tags help customers simplify the creation and maintenance of the necessary rules for outbound network traffic through Azure firewalls. For more information, see [Use Azure Firewall to manage and secure Windows 365 environments](azure-firewall-windows-365).

### Miscellaneous

#### Windows 365 and FedRAMP

Windows 365 Enterprise has been assessed by a FedRAMP authorized auditor to meet FedRAMP requirements at data centers within the Continental US.

### Windows 365 Government

#### Windows 365 Gov support for transferring files from your Cloud PC by using windows365.microsoft.com web client

You can use the windows365.microsoft.com web client to transfer files to and from your Windows 365 Gov Cloud PC. For more information, see [Transfer files to and from a Cloud PC](../end-user-access-cloud-pc#transfer-files-to-and-from-a-cloud-pc).

#### Higher Cloud PC screen resolution option for Windows 365 Gov

Windows 365 Gov Cloud PC users can now choose a higher screen resolution when they connect to their Cloud PC from https://windows365.microsoft.com.

## Week of March 6, 2023

### Device management

#### Create on-demand Cloud PC restore points and copy them to an Azure Storage account

You can now create on-demand Cloud PC restore points and copy them to an Azure Storage account. For more information, see [Create on-demand manual restore points for Cloud PCs](create-manual-restore-point) and [Share Cloud PC restore points to an Azure Storage Account](share-restore-points-storage).

### Role-based access control

#### Permission changes for Azure network connection operations

The permissions required for the editing, creating, and deleting Azure network connection (ANC) and health check retry operations have changed: You must now have [Intune Administrator](/en-us/azure/active-directory/roles/permissions-reference#intune-administrator) or [Windows 365 Administrator](/en-us/azure/active-directory/roles/permissions-reference) permissions. For more information, see [Azure network connections](azure-network-connections).

## Week of February 27, 2023 (Service release 2302)

### Apps

#### Windows 365 app is now generally available

The Windows 365 app has moved out of preview and into general availability.

#### Improved video playback by using multimedia redirection is now generally available

Improved video playback performance on your Cloud PCs by using multimedia redirection (MMR) has moved out of preview and into general availability. For more information, see [Video playback improvement](troubleshooting#video-playback-improvements).

#### Cloud PC web client: improved feedback interface for end users

The Cloud PC web client (accessible from windows365.microsoft.com) has an improved feedback interface for end users to provide feedback.

### Device management

#### Hardware acceleration for the windows365.microsoft.com web client

On the windows365.microsoft.com web client, you can now benefit from hardware acceleration. This option is turned on by default and improves motion performance for activities like scrolling, moving windows, or playback of video.

#### Configure installed language and region for provisioning Cloud PCs in GCC/H environments

When creating a provisioning policy, admins can now configure the installed language and region for new Cloud PCs in US Government Community Cloud (GCC) and GCC High environments. For more information, see [Provide users a localized Windows experience](provide-localized-windows-experience)

### Device provisioning

#### Add more Azure Network Connections to a provisioning policy

A new Azure Network Connection (ANC) option lets you add more ANCs to a provisioning policy and define a priority order for their use. By preparing multiple ANCs in different Azure regions, admins can make provisioning more reliable in the rare case capacity constraints in a region.

#### GCC/H support for geography option in Windows 365 provisioning policy

The **Geography** setting in provisioning policies is now supported for US Government Community Cloud (GCC) and GCC High environments. For more information, see [Create provisioning policies](create-provisioning-policy).

### Documentation

#### New documentation article: Azure network connection domain credential life cycle

We’ve published a new help documentation article. For more information, see [Azure network connection domain credential life cycle](azure-network-connection-domain-credential).

## Week of February 20, 2023

### Partners

#### Citrix HDX Plus support is now generally available

Windows 365 support for Citrix HDX Plus has moved out of preview and into general availability. For more information, see [Set up Citrix HDX Plus for Windows 365 Enterprise](set-up-citrix).

## Week of February 6, 2023

### Apps

#### Nested virtualization now supports 4vCPU Cloud PCs

Windows 365 nested virtualization now supports 4vCPU Cloud PCs. For more information, see [Set up virtualization-based workloads support](nested-virtualization).

## Week of January 30, 2023 (Service release 2301)

### Apps

#### Windows 365 app now supports Windows 10

The Windows 365 app now supports Windows 10.

#### Microsoft Teams: Share application windows from Windows 365 Cloud PC

In Microsoft Teams, you can now share specific windows from your Cloud PC desktop. Previously, you could only share the full Cloud PC desktop.

### End user experience

#### Open Cloud PCs in a Remote Desktop app from windows365.microsoft.com

From windows365.microsoft.com, you can now open a Cloud PC in a Remote Desktop app. For more information, see [Access a Cloud PC](../end-user-access-cloud-pc#home-page).

#### Improved feedback interface for end users

windows365.microsoft.com has improved the interface for end users to provide feedback.

#### Get Cloud PC connection details from windows365.microsoft.com

On windows365.microsoft.com, you can now get Cloud PC connection details like transport protocol, round-trip time, frame rate, and more.

## Week of January 16, 2023

### Monitor and troubleshoot

#### Windows 365 Government support for forensic auditing of Cloud PCs

Forensic auditing is now available for Windows 365 Government. For more information, see [Digital forensics and Windows 365 Enterprise Cloud PCs](digital-forensics) and [Place a Cloud PC under review](place-cloud-pc-under-review).

## Week of January 2, 2023

### Role-based access control

#### Support for custom Windows 365 RBAC roles now generally available

Support for custom Windows 365 role-based access control (RBAC) roles has moved out of preview and into general availability. These custom roles are also now supported for Windows 365 Government (Government Community Cloud and Government Community Cloud High). For more information, see [Custom roles](role-based-access#custom-roles).

## Week of December 12, 2022

### Provisioning

#### Provision Azure Active Directory Join Cloud PCs with single sign-on (public preview)

Windows 365 now supports creating Azure Active Directory Join Cloud PCs that use single sign-on for Cloud PC login. Existing Cloud PCs won’t have single sign-on configured. For more information, see [Create provisioning policy](create-provisioning-policy) and [Edit provisioning policy](edit-provisioning-policy).

### Provisioning

#### Configure installed language and region for provisioning Cloud PCs generally available

Language pre-configuration for Cloud PCs has moved out of preview and into general availability. Admins can select the **Language & Region pack** under **Configuration** in their provisioning policy to pre-configure the language for the endpoint devices. For more information, see [Use a provisioning policy to set up a default display language on Cloud PCs](use-provisioning-policy-default-display-language).

### Device management

#### New Third-party connector column on All devices page

There's a new column on the **All devices page**: **Third-party connector**. For more information, see [Device management overview for Cloud PCs](device-management-overview).

#### Retry Citrix agent installation

You can now use the **Retry Citrix agent installation** option instead of doing a full provisioning retry. For more information, see [Retry Citrix agent installation](retry-citrix-agent-installation).

### Documentation

#### New documentation article: Windows 365 deployment options

We’ve published a new help documentation article. For more information, see [Windows 365 deployment options](deployment-options).

## Week of December 5, 2022

### Device management

#### Support for RDP Shortpath for public networks now generally available

Support for RDP Shortpath for public networks has moved out of preview and into general availability. For more information about RDP Shortpath, see [Use RDP Shortpath for public networks with Windows 365](rdp-shortpath-public-networks).

## Week of November 28, 2022

### Provisioning

#### New Geography option in Windows 365 provisioning policy

The new **Geography** setting gives admins two ways to choose Azure regions during provisioning.

- You can select a specific region to make sure that your Cloud PCs are only provisioned in that region.
- You can select **Automatic** to let the Windows 365 service automatically select a region (within the Geography) at the time of provisioning.

Existing provisioning policies will automatically populate the **Geography** and **Region** settings based on existing settings. No admin action is required.

For more information, see [Create provisioning policies](create-provisioning-policy).

### Windows 365 app

#### Updated Windows 365 app installation to install dependent applications

The Windows 365 app installation process has been updated to automatically install dependent applications.

#### Azure Active Directory policy updated for Windows 365 app

The Azure Active Directory (Azure AD) policy has been updated so that no extra Conditional Access policy change is required to use the Windows 365 app.

## Week of November 14, 2022

### Documentation

#### New documentation article: Use the Enrollment Status Page with Cloud PCs

We’ve published a new help documentation article. For more information, see [Use the Enrollment Status Page with Cloud PCs](enrollment-status-page).

## Week of November 7, 2022

### Windows 365 Government

#### Windows 365 Government now supports Windows 11 and Secure boot

Windows 365 Government now supports the following features:

- Creating Cloud PCs that use [Secure boot](/en-us/windows-hardware/design/device-experiences/oem-secure-boot).
- Windows 11 options in the gallery images list.
- Creating custom images running Windows 11 (must be Generation 2 virtual machines).

## Week of October 24, 2022

### Device management

#### Point-in-time restore now generally available

Point-in-time restore has moved out of preview and into general availability. For more information, see [Point-in-time restore for Windows 365 Enterprise](restore-overview).

### Provisioning

#### New supported Azure region: UAE North

A new Azure region is now supported for Windows 365 Cloud PC provisioning: UAE North.

For more information about supported Azure regions, see [Supported Azure regions for Cloud PC provisioning](requirements#supported-azure-regions-for-cloud-pc-provisioning).

## Week of October 17, 2022

### Monitor and troubleshoot

#### New Azure Network Connection health check

A new check has been added the Azure Network Connection health checks: **UDP connection server reachable**. For more information, see [Azure network connections health checks](health-checks).

#### Forensic auditing of Cloud PCs now generally available

Forensic auditing has moved out of preview and into general availability. For more information, see [Digital forensics and Windows 365 Enterprise Cloud PCs](digital-forensics) and [Place a Cloud PC under review](place-cloud-pc-under-review).

## Week of October 10, 2022

### Apps

#### Windows 365 app in public preview

A new app to sign in to and manage your Windows 365 Cloud PCs is now in public preview. The app provides functionality similar to the windows365.microsoft.com web site for accessing and managing your Cloud PCs.

### Device provisioning

#### Support for US Government environments

Government organizations can now use Windows 365 services first in US Government Community Cloud (GCC) High environments and later in GCC environments. All Windows 365 dependency services must also be used by the organization within the associated Government environment. For more information, see [What is Windows 365 Government?](introduction-windows-365-government)

### Partners

#### Use Citrix HDX Plus with Windows 365 Enterprise

You can now use Citrix HDX Plus with Windows 365 Enterprise Cloud PCs. For more information, see [Set up Citrix HDX Plus for Windows 365 Enterprise](set-up-citrix).

### Monitor and troubleshoot

#### Cloud PC utilization report

A new report is now available for Cloud PCs. The **Cloud PC utilization** report shows how many hours users have been connected to their Cloud PCs. Information for individual Cloud PCs and aggregated data is also shown. For more information, see [Cloud PC utilization report](report-cloud-pc-utilization).

#### Cloud PC with connection quality issues report

A new report is now available for Cloud PCs. The **Cloud PCs with connection quality issues** report shows information for round-trip time, available bandwidth, and remoting sign-in time. Information for individual Cloud PCs and aggregated data is also shown. For more information, see [Cloud PC connection quality report](report-cloud-pc-connection-quality).

## Week of September 26, 2022 (Service release 2209)

### Monitor and troubleshoot

#### System alerts and email notifications (preview)

You can now set up system alerts and automated emails to be notified when certain events, warnings, or errors occur in the Windows 365 service. A subset of critical Cloud PC issues will be sent automatically to admins. In addition, you can define alert rules, such as target audience (devices, user groups, tenants), thresholds, frequency, and notification channels. For more information, see [Alerts](alerts).

### Miscellaneous

#### Allow list URL change for Windows 365

We've added a new endpoint which the Windows 365 service requires to be accessible: \*.infra.windows365.microsoft.com". This is part of ongoing endpoint consolidation work to reduce the number of FQDNs required to be accessible for the service.

## Week of September 19, 2022

### Device management

#### Downsize Cloud PCs (Preview)

You can now downsize a Cloud PC's RAM and specifications (except disk size). For more information, see [Resize a Cloud PC](resize-cloud-pc).

### Device provisioning

#### Windows 365 Cloud PC support for Windows 11 Enterprise version 22H2

New gallery images are now available that include support for Windows 11 version 22H2. The following gallery images can be used for newly provisioned Cloud PCs:

- Win11 22H2 + M365 Apps
- Win11 22H2 + Optimizations

## Week of August 29, 2022 (Service release 2208)

### Monitor and troubleshoot

#### New health check: Localization language package readiness

The **Azure network connection** tab has a new health check: **Localization language package readiness**. This health check verifies that the operating system and Microsoft 365 language packages can install. It also makes sure that the localization package download link is reachable. For more information, see [Azure network connection health checks](health-checks).

#### Review Cloud PC connectivity health checks and errors in Microsoft Intune admin center

You can now review connectivity health checks and errors in the Microsoft Intune admin center to help you understand if your users are experiencing connectivity issues. You’ll also get a troubleshooting tool to help resolve connectivity issues. To see the checks, select **Devices** &gt; **Windows 365** &gt; **Azure network connections** &gt; select a connection in the list &gt; **Overview**. This feature is rolling out to all customers over the next few weeks.

### Provisioning

#### New supported Azure regions: East Asia, Korea Central, Norway East, Switzerland North

New Azure regions are now supported for Windows 365 Cloud PC provisioning: East Asia, Korea Central, Norway East, and Switzerland North.

For more information about supported Azure regions, see [Supported Azure regions for Cloud PC provisioning](requirements#supported-azure-regions-for-cloud-pc-provisioning).

## Week of August 22, 2022

### Documentation

#### New documentation article: Restrict Office 365 services to Cloud PCs

We’ve published a new help documentation article. For more information, see [Restrict Office 365 services to Cloud PCs](restrict-office-365-cloud-pcs).

## Week of August 15, 2022

### App management

#### Language and region configuration now also applies to Microsoft 365 Apps

Provisioning policies configured for language now also apply to Microsoft 365 Apps. When a user first signs in, their Microsoft 365 Apps will use the configured language. For more information, see [Provide a localized Windows experience](provide-localized-windows-experience).

### Monitor and troubleshoot

#### Remoting connection report in Endpoint Analytics now generally available

The remoting connection report in Endpoint Analytics has moved out of preview and into general availability. For more information, see [Remoting connection report](report-remoting-connection).

#### Resource performance report in Endpoint Analytics now generally available

The resource performance report in Endpoint Analytics has moved out of preview and into general availability. For more information, see [Resource performance report](report-resource-performance).

## Week of August 8, 2022

### Documentation

#### New documentation article: Windows 365 security

We’ve published a new help documentation article. For more information, see [Windows 365 security](security).

## Week of July 25, 2022

### Resize action support for more Cloud PCs

The resize action now supports Cloud PCs that are Azure Active Directory joined.

## Week of July 18, 2022

### Apps

#### Cloud PC Outlook mail sync setting

For newly provisioned and reprovisioned Cloud PCs, you can now set the Outlook mail sync setting to 6 or 12 months.

### Device provisioning

#### Provision Cloud PCs with Secure Boot

Support for creating Cloud PCs that use [Secure boot](/en-us/windows-hardware/design/device-experiences/oem-secure-boot) functionality is now available in Europe, APAC, and North American regions. Existing Cloud PCs won't have secure boot automatically enabled.

## Week of July 4, 2022 (Service release 2206)

### Apps

#### Support for virtualization-based workloads now generally available

Support for virtualization-based workloads has moved out of preview and into general availability. For more information, see [Set up virtualization-based workloads on your Cloud PC](nested-virtualization).

### End user experience

#### Transfer files from your Cloud PC by using windows365.microsoft.com web client

You can use the windows365.microsoft.com web client to transfer files to and from your Cloud PC. For more information, see [Transfer files to and from a Cloud PC](../end-user-access-cloud-pc#transfer-files-to-and-from-a-cloud-pc).

### Monitor and troubleshoot

#### New health check: verify that Intune enrollment restrictions allow Windows enrollment

The **Azure network connection** tab has a new health check: **Intune enrollment restrictions allow Windows enrollment**. This health check verifies that Intune enrollment restrictions are configured to allow Windows enrollment. Windows 365 Enterprise requires Intune enrollment during provisioning.

## Week of June 6, 2022 (Service release 2205)

### Monitor and troubleshoot

#### Forensic auditing of Cloud PCs

You can now place a Cloud PC under review. This action starts a process to create a secure snapshot of a Cloud PC. You can then analyze the snapshot using electronic discovery solutions. For more information, see [Digital forensics and Windows 365 Enterprise Cloud PCs](digital-forensics) and [Place a Cloud PC under review](place-cloud-pc-under-review).

## Week of May 16, 2022

### Device management

#### Support for RDP Shortpath for public networks

Windows 365 Enterprise Cloud PCs now support RDP Shortpath for public networks. For more information about RDP Shortpath, see [Use RDP Shortpath for public networks (preview) with Windows 365](rdp-shortpath-public-networks).

#### Windows 365 ending support for Windows 10 version 1909 (19H2)

Windows 365 no longer supports Windows 10 version 1909 (19H2).

### User experience

#### Windows 365 Cloud PC support for Teams background effects

Windows 365 Cloud PCs now support background effects in Teams. For more information, see the blog [Microsoft Teams background effects generally available on Windows 365](https://techcommunity.microsoft.com/t5/windows-365/microsoft-teams-background-effects-generally-available-on/m-p/3403274).

#### Windows 365 Cloud PC support for Teams multi-window and Call me

Windows 365 Cloud PCs now support multi-window and Call Me in Teams. For more information, see the blog [Teams Multi-window support and Call Me generally available on Windows 365](https://techcommunity.microsoft.com/t5/windows-365/teams-multi-window-support-and-call-me-generally-available-on/m-p/3403252).

## Week of May 9, 2022 (Service release 2204)

### Device management

#### Support for Azure AD joined Cloud PCs now general available

Support for Azure AD joined Cloud PCs has moved out of preview and into general availability.

### Provisioning

#### Provision Cloud PCs with Secure Boot

Cloud PC support for [Secure boot](/en-us/windows-hardware/design/device-experiences/oem-secure-boot) functionality is now rolling out in Asia Pacific (APAC) regions and Europe. This feature will roll out to all customers over the next few months.

## Week of May 2, 2022

### Documentation

#### New documentation article: Manage Windows 365 Cloud PCs with Configuration Manager

We’ve published a new help documentation article. For more information, see [Manage Windows 365 Cloud PCs with Configuration Manager](manage-cloud-pcs-using-configuration-manager).

## Week of April 18, 2022

### On-premises network connection has been renamed to Azure network connection

The term **on-premises network connection** has been renamed to **Azure network connection** in all user interfaces, documentation, and communications.

### Change Cloud PC time zone

Non-admin users can now change their Cloud PC’s time zone.

## Week of April 11, 2022

### Scripts

#### Windows365-PSScripts GitHub repository is now open for contributions

The Windows365-PSSCripts GitHub repository is now open. It contains Windows 365-related scripts to help admins manage Cloud PCs. You can also contribute your own scripts to help others use Windows 365.

For more information, see the [Windows365-PSScripts GitHub repository readme](https://github.com/microsoft/Windows365-PSScripts).

## Week of April 4, 2022 (Service release 2203)

### Apps

#### Live captions for Microsoft Teams on Windows 365 Cloud PCs

For Windows 365 Enterprise and Business Cloud PCs, Microsoft Teams can now detect what is said in a meeting and display real-time captions. The captions can be toggled on and off.

To use live captions in a meeting, go to your meeting controls and select **More options** and Turn on live captions.

For more information, see [Microsoft Teams Live Captions generally available on Windows 365](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/microsoft-teams-live-captions-generally-available-on-windows-365/ba-p/3265208) and [Use live captions in a Teams meeting](https://support.microsoft.com/office/use-live-captions-in-a-teams-meeting-4be2d304-f675-4b57-8347-cbd000a21260).

#### Nested virtualization (preview)

For most currently supported regions, Windows 365 8vCPU/32GB licenses now support nested virtualizations for different developer scenarios to use systems like WSL/Hyper-V. Southeast Asia and West US 2 aren't currently supported for this feature. For more information, see [Set up nested virtualization on your Cloud PC](nested-virtualization).

#### Improve video playback by using multimedia redirection

You can improve video playback performance on your Cloud PCs by using multimedia redirection (MMR). For more information, see [Video playback improvement](troubleshooting#video-playback-improvements).

### Device management

#### windows365.microsoft.com now generally available

The [windows365.microsoft.com](https://windows365.microsoft.com/) web client has moved out of preview and into general availability.

### Device provisioning

#### Upload a custom image without an Azure network connection

Customers using Azure Active Directory (Azure AD) Join without bringing an Azure virtual network can now upload custom images directly on the image tab in Microsoft Intune. Previously, to upload an image, customers needed to create an ANC for the destination Azure subscription that provides the image.

#### Cloud PC name appended to the network interface name

A Cloud PC’s name is now appended to the network interface name within the Azure portal. This naming makes it easier to find the IP address for the Cloud PC when an Azure network connection is selected.

### End-user experience

#### End user feedback

End users can now provide feedback to Microsoft from within the Windows 365 web client and directly on windows365.microsoft.com.

#### End user error log collection

End users can now collect error logs.

## Week of March 24, 2022

### Device management

#### New remote action: Remote Help

The [Remote Help remote action](/en-us/mem/intune/remote-actions/remote-help) (in the Microsoft Intune admin center) lets admins start a remote session into an end user’s Cloud PC.

## Week of February 28, 2022 (Service release 2202)

### Device management

#### Point-in-time restore (preview)

Administrators and users can now restore a Cloud PC to a state from a previous point in time. Multiple near-term and long-term restore points are available. For more information, see [Point-in-time restore for Windows 365 Enterprise](restore-overview).

#### Higher Cloud PC screen resolution option (preview)

Cloud PC users can now choose a higher screen resolution when they connect to their Cloud PC from https://windows365.microsoft.com.

### Documentation

#### New documentation article: Windows 365 approved partners

We’ve published a new help documentation article. For more information, see [Windows 365 approved partners](../partners).

## Week of February 14, 2022

### Documentation

#### New documentation article: Windows 365 identity and authentication

We’ve published a new help documentation article. For more information, see [Windows 365 identity and authentication](identity-authentication).

### Device management

#### Support for Azure AD joined Cloud PCs

Windows 365 Enterprise now supports Cloud PCs that are Azure AD joined. These devices can run in either:

- A Microsoft-hosted network:
    - You don’t need to bring any Azure infrastructure
    - You don't need to create an Azure network connection
- Your own network (using an Azure network connection)

#### Configure installed language and region for provisioning Cloud PCs

When creating a provisioning policy, admins can now configure the installed language and region for new Cloud PCs. Previously, Cloud PCs were only created with English (United States). For more information, see [Provide users a localized Windows experience](provide-localized-windows-experience)

### Monitor and troubleshoot

#### Use Collect diagnostics to collect more details from Windows 365 devices through Intune remote actions

Intune’s remote action to Collect diagnostics now collects more details from Windows 365 Cloud PCs.

The new details for Windows 365 Cloud PCs include the following registry data:

- HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\AddIns\WebRTC Redirector
- HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Teams\

To learn more about the **Collect diagnostics** remote action, see [Collect diagnostics from a Windows device](/en-us/mem/intune/remote-actions/collect-diagnostics).

### Provisioning

#### New supported Azure regions: US Central and German West Central

Two new Azure regions are now for Windows 365 Cloud PC provisioning: US Central and German West Central.

For more information about supported Azure regions, see [Supported Azure regions for Cloud PC provisioning](requirements#supported-azure-regions-for-cloud-pc-provisioning).

## Week of January 17, 2022

#### New documentation article: Optimize Cisco Webex on a Windows 365 Cloud PC

We’ve published a new help documentation article. For more information, see [Optimize Cisco Webex on a Windows 365 Cloud PC](cisco-webex-support).

## Week of January 10, 2022

#### New documentation: Data encryption in Windows 365

We've added information to the help documentation about encryption for Windows 365 Cloud PCs. For more information, see [Data encryption in Windows 365](encryption).

## Week of January 3, 2022

#### New documentation: Gallery image update cycle

We've added information to the help documentation about the update cycle for Windows 365 Cloud PC gallery images. For more information, see [Gallery image update cycle](device-images#gallery-image-update-cycle).

## Week of December 13, 2021

### Device management

#### Cloud PCs in grace period count towards active Cloud PC license usage

Cloud PCs that are in grace period now count towards your active Cloud PC license usage. This policy makes sure that your organization’s active Cloud PC allocation matches the total available licenses in your tenant.

For more information about grace period, see [Device management overview](device-management-overview) and [End grace period](end-grace-period).

## Week of November 29, 2021 (Service release 2111)

### Device management

#### Operating system end of support status for Cloud PCs

The **Provisioning policies** page has a new column: **Image status**. It tells you if the device image for each provisioning policy uses an operating system (OS) that is supported by Microsoft Windows security and other updates. For more information, see [Lifecycle policies and end of support for Cloud PC OS](end-of-support).

#### New documentation article: Optimize Zoom on a Windows 365 Cloud PC

We’ve published a new help documentation article. For more information, see [Optimize Zoom on a Windows 365 Cloud PC](zoom-support).

### Device security

#### Two new security baseline settings for Windows 11 Cloud PCs

Windows 365 Enterprise now supports the following Windows 11 security baseline settings:

- **Tamper Protection**: Helps protect Cloud PCs from bad actors bypassing security features like anti-virus protection.
- **Script Scanning**: Helps identify possible threats by intercepting scripts and scanning them before they’re run.

For more information about the security baseline updates for Windows 11, see [Windows 11 Security baseline](https://techcommunity.microsoft.com/t5/microsoft-security-baselines/windows-11-security-baseline/ba-p/2810772). For more information about setting security baselines for Cloud PCs, see [Deploy security baselines](deploy-security-baselines).

## Week of November 1, 2021 (Service release 2110)

### Device management

#### Improved user interface for online access to Cloud PCs

The user interface on https://windows365.microsoft.com has been improved with:

- Faster load times.
- Higher performance reliability.
- Local resource settings (printer, microphone, clipboard).
- Alternative keyboard settings.
- Edit settings in-session.
- Accessibility support.

### Provisioning

#### Provisioning maximum timeout changed to five hours

To improve reliability, the maximum provisioning timeout has been changed to five hours.

### Role-based access control

#### Custom Windows 365 RBAC roles in public preview

Custom Windows 365 role-based access control (RBAC) roles are now available in the Microsoft Intune admin center. You can mix-and-match Windows 365 permissions to create custom roles for your organization's needs. You can also create both Windows 365 and Intune custom roles and give granular admin permissions to admins for both services. For more information, see [Custom roles](role-based-access#custom-roles).

## Week of October 11, 2021 (Service release 2109)

### Device management

#### Resize support for preview and trial licenses

If you have a combination of paid and free trial licenses, the Resize remote action will use your paid licenses first. When those licenses run out, it will use your trial licenses. For more information, see [Resize a Cloud PC](resize-cloud-pc).

### Device provisioning

#### Health check improvement

The **DNS can resolve Active Directory domain** health check has been improved. A new step has been added to look for the following Azure Active Directory DNS record. If it can’t be found, the check fails.

`_ldap._tcp.example.com -type SRV`

### Role-based access control

#### Windows 365 Administrator role

The Windows 365 Administrator role is now available for admins by using role assignment in the Microsoft Intune admin center and Azure Active Directory (Azure AD) for Windows. With this role, admins can broadly manage Windows 365 Enterprise Cloud PCs, users, devices, and groups. This new role is in addition to the other existing roles that Windows 365 currently supports: Azure AD Global Admin, Intune Admin, and Cloud PC granular roles in Microsoft Intune. For more information, see [Role-based access control](role-based-access).

## Week of October 4, 2021

### Device management

#### Support for Windows 11

Windows 365 Enterprise now supports Windows 11 as a Cloud PC operating system.

Windows 11 Cloud PCs require Generation 2 (Gen2) virtual machines. For information about converting existing Generation 1 custom device images to Gen2, see [Convert an existing custom device image to a generation 2 virtual machine](device-images-convert-generation-2).

## Week of September 13, 2021

### Device management

#### New PowerShell script for installing languages on custom device images

The [Windows365LanguagesInstaller PowerShell script](https://www.powershellgallery.com/packages/Windows365LanguagesInstaller) can install 38 additional languages on your custom device images. For more information, see [Provide a localized Windows experience](create-custom-image-languages#add-languages-to-windows-using-a-script-and-capture-the-image).

## Week of September 6, 2021 (Service release 2108)

### Device management

#### End grace period option

Certain conditions put a Cloud PC into a seven-day grace period. At the end of this time, the Cloud PC will be deprovisioned and user will lose access.

You can now immediately end the grace period for individual Cloud PCs. By ending the grace period manually, you won’t have to wait the full seven days to remove user access from the Cloud PC.

For more information on grace periods, see [End grace period](end-grace-period).

## Week of August 30, 2021

### Monitor and troubleshoot

#### Resource performance report in Endpoint Analytics

Endpoint analytics has a new report named **Resource performance**. The **Resource performance report** includes metrics for CPU and RAM performance on Cloud PCs. For more information, see [Resource performance report](report-resource-performance).

#### Remoting connection report in Endpoint Analytics

Endpoint analytics has a new report named **Remoting connection report**. This report includes the following metrics:

- **Cloud PC Sign in time (sec)** provides the total time users take to connect to the cloud PC.
- **Round Trip Time (ms)** provides insights on the speed and reliability of network connections from the user location.

For more information, see [Remoting connection report](report-remoting-connection).

## Week of August 2, 2021

### Windows 365 now generally available

Windows 365 is a new service from Microsoft that automatically creates Cloud PCs for your end users. Cloud PCs are a new hybrid personal computing category that uses both the power of the cloud and the accessing device to provide a full and personalized Windows virtual machine. Admins can use Microsoft Intune to define the configurations and applications that are provisioned for each user’s Cloud PC. End users can access their Cloud PC from any device and any location. Windows 365 stores the end user’s Cloud PC and data in the cloud, not on the device, providing a secure experience.

For more information about Windows 365, see [Windows 365](https://www.microsoft.com/windows-365?rtc=1).