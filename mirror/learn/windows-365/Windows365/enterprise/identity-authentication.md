---
layout: Conceptual
title: Windows 365 identity and authentication | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/identity-authentication
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Windows 365 identity and authentication
keywords: 
author: ChristianMontoya
ms.author: chrimo
manager: pratikshah
ms.date: 2026-05-17T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: davidbel, pratikshah
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 7f4ec446-82c3-359b-915e-1cedda70e658
document_version_independent_id: 7f4ec446-82c3-359b-915e-1cedda70e658
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/identity-authentication.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/identity-authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/identity-authentication.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 529a0888-67ed-87df-9259-09f33a0f99d3
---

# Windows 365 identity and authentication | Microsoft Learn

A Cloud PC user's identity defines which access management services manage that user and Cloud PC. This identity defines:

- The types of Cloud PCs the user has access to.
- The types of non-Cloud PC resources the user has access to.

A device can also have an identity determined by its join type to Microsoft Entra ID. For a device, the join type defines:

- If the device requires line of sight to a domain controller.
- How the device is managed.
- How users authenticate to the device.

## Identity types

There are four identity types:

- **[Hybrid identity](/en-us/entra/identity/hybrid/whatis-hybrid-identity)**: Users or devices that are created in on-premises Active Directory Domain Services, then synchronized to Microsoft Entra ID.
- **[Cloud-only identity](/en-us/microsoft-365/enterprise/manage-microsoft-365-accounts#cloud-only)**: Users or devices that are created and only exist in Microsoft Entra ID.
- **[Federated identity](/en-us/entra/identity/devices/device-join-plan#federated-environment)**: Users that are created in a third-party identity provider, other than Microsoft Entra ID or Active Directory Domain Services, then federated with Microsoft Entra ID.
- **[External identity](/en-us/entra/external-id/identity-providers)**: Users who are created and managed outside of your Microsoft Entra tenant but are invited in to your Microsoft Entra tenant to access your organization's resources.

Note

- Windows 365 supports federated identities when single sign-on is enabled.
- Windows 365 supports external identities when single sign-on is enabled. See external identity for all requirements and limitations.

### External identity

External identity support allows you to invite users to your Entra ID tenant and provide them Cloud PCs. There are several requirements and limitations when providing Cloud PCs to external identities:

- Requirements
    - **Cloud PC operating system**: The Cloud PC must be running Windows 11 Enterprise, versions 24H2 or later with the [2025-09 Cumulative Updates for Windows 11 (KB5065789)](https://support.microsoft.com/kb/KB5065789) or later installed.
    - **Cloud PC join type**: The Cloud PC must be Entra joined.
    - **Single sign-on**: Single sign-on must be configured for the Cloud PC.
    - **Windows App client**: External identity support is generally available on the Windows App on macOS, Windows, Android, or a web browser. See the [Identity](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity)section of Windows App documentation for additional details.
        - **Licensing**: Ensure that external identities have the proper entitlements for software and services on the Cloud PC. See [Windows 365 licensing guidance](/en-us/windows-365/overview#licensing-and-how-to-buy) for more details.
- Limitations
    - **Intune device configuration policies**: Device configuration policies assigned to the external identity won't be applied to the user's Cloud PC. Instead, assign device configuration policies to the device.
    - **Windows 365 Government availability**: Windows 365 Government is supported, and users can connect with the Windows App on Windows and the Windows App on Android.
    - **Cross cloud invites**: Cross-cloud users aren't supported. You can only provide Cloud PCs to users you invite from social identity providers, Microsoft Entra users from the same Microsoft Azure cloud as the Windows 365 offering, or other [identity providers registered in your workforce tenant](/en-us/entra/external-id/identity-providers). You can't provision Cloud PCs for users you invite from Microsoft Azure operated by 21Vianet.
    - **Token protection**: Microsoft Entra has certain [limitations for token protection for external identities](/en-us/entra/identity/conditional-access/concept-token-protection#known-limitations). Learn more about [Windows App support for token protection by platform](/en-us/windows-app/compare-platforms-features?pivots=windows-365#security).
    - **Kerberos authentication**: External identities can't authenticate to on-premises resources using Kerberos or NTLM protocols.
    - **Microsoft 365 apps**: You can only login to the Windows desktop version of the Microsoft 365 apps if:

        1. The invited user is an Entra-based account or a Microsoft Account that is licensed for Microsoft 365 Apps.
        2. The invited user is not blocked from accessing the Microsoft 365 apps by a conditional access policy from the home organization.

        Regardless of the invited account, you can access Microsoft 365 files shared with you by using the appropriate Microsoft 365 app in the web browser of the Cloud PC.
    - **Identity providers**: You can sign-in as an external identity with any of the listed [identity providers](/en-us/entra/external-id/identity-providers), except for one-time passcode sign-in. The following Windows App clients have additional limitations:

        - Android: The only supported social identity provider you can sign in with is a Microsoft account that is configured as a **Connected account** in the Microsoft Authenticator app running on the same device as the client. You can't sign in with Facebook or Google.
    - **Domainless federation**: Windows 365 supports external identities through [Domainless SAML IdP Federation](/en-us/entra/external-id/direct-federation#domainless-saml-idp-federation), however these users must redeem their invitation (including the `domain_hint` parameter) before launching the Windows App. If the user connects to the Windows App but hasn't yet redeemed their invite to the Domainless SAML IdP, the user won't be able to authenticate or accept the invite.

See [Microsoft Entra B2B best practices](/en-us/entra/external-id/b2b-fundamentals) for recommendations on configuring your environment for external identities and [Windows 365 licensing guidance](/en-us/windows-365/overview#licensing-and-how-to-buy).

## Device join types

There are two join types that you can select from when [provisioning a Cloud PC](provisioning):

- **[Microsoft Entra Hybrid Join](/en-us/entra/identity/devices/concept-hybrid-join)**: If you choose this join type, Windows 365 joins your Cloud PC to the Windows Server Active Directory domain you provide. Then, if your organization is properly [configured for Microsoft Entra hybrid join](/en-us/entra/identity/devices/how-to-hybrid-join), the device is synchronized to Microsoft Entra ID.
- **[Microsoft Entra Join](/en-us/entra/identity/devices/concept-directory-join)**: If you choose this join type, Windows 365 joins your Cloud PC directly to Microsoft Entra ID.

The following table shows key capabilities or requirements based on the selected join type:

| Capability or requirement | Microsoft Entra hybrid join | Microsoft Entra join |
| --- | --- | --- |
| Azure subscription | Required | Optional |
| Azure virtual network with line of sight to the domain controller | Required | Optional |
| User identity type supported for login | Hybrid users only | Hybrid users, cloud-only users, or external identities |
| Policy management | Group Policy Objects (GPO) or Intune MDM | Intune MDM only |
| Windows Hello for Business sign-in supported | Yes, and the connecting device must have line of sight to the domain controller through the direct network or a VPN | Yes |

## Authentication

When a user accesses a Cloud PC, there are three separate authentication phases:

- **Cloud service authentication**: Authenticating to the Windows 365 service, which includes subscribing to resources and authenticating to the Gateway, is with Microsoft Entra ID. This is where you can enforce Entra ID Conditional Access policies. Also, this is where you can federate from Entra ID to a 3rd-party identity provider.
- **Remote session authentication**: Authenticating to the Cloud PC. There are multiple ways to authenticate to the remote session, including the recommended single sign-on (SSO).
- **In-session authentication**: Authenticating to applications and web sites within the Cloud PC.

Here is a brief comparison of user authentication options at each authentication phase:

| Cloud service authentication | Remote session authentication | In-session authentication |
| --- | --- | --- |
| - Passwordless authentication (including FIDO security keys, Windows Hello for Business with Cloud Kerberos or Key trust, Microsoft Authenticator multi-factor authentication and more)<br>- Federation to third-party Identity provider<br>- Smartcard (including Entra certificate-based authentication and Windows Hello for Business certificate trust)<br>- Password | - Any **Cloud-service authentication method**, when configured with single sign-on<br>- Smartcard (including Windows Hello for Business certificate trust)<br>- Password | - Passwordless authentication, when configured for in-session passwordless<br>- Smartcard (including Windows Hello for Business certificate trust)<br>- Password |

These are a superset of authentication options per authentication phase. For the list of credential available on the different clients for each of the authentication phase, [compare the clients across platforms](/en-us/azure/virtual-desktop/compare-remote-desktop-clients?pivots=windows-365#authentication).

Important

In order for authentication to work properly, the user's local machine must also be able to access the URLs in the [Remote Desktop clients](/en-us/azure/virtual-desktop/safe-url-list#remote-desktop-clients) section of the [Azure Virtual Desktop required URL list](/en-us/azure/virtual-desktop/safe-url-list).

Windows 365 offers single sign-on (defined as a single authentication prompt that can satisfy both the Windows 365 service authentication and Cloud PC authentication) as part of the service. For more information, see single sign-on.

The following sections provide more information on these authentication phases.

### Cloud service authentication

Users must authenticate with the Windows 365 service when:

- They access https://windows.cloud.microsoft.
- They navigate to the URL that maps directly to their Cloud PC.
- They use a [supported client](../end-user-access-cloud-pc) to list their Cloud PCs.

To access the Windows 365 service, users must first authenticate to the service by signing in with a Microsoft Entra ID account.

#### Multifactor authentication

Follow the instructions in [Set Conditional Access policies](set-conditional-access-policies) to learn how to enforce Microsoft Entra multifactor authentication for your Cloud PCs. That article also tells you how to configure how often your users are prompted to enter their credentials.

#### Passwordless authentication

Users can use any authentication type supported by Microsoft Entra ID, such as [Windows Hello for Business](/en-us/windows/security/identity-protection/hello-for-business/hello-overview) and other [passwordless authentication options](/en-us/entra/identity/authentication/concept-authentication-passwordless) (for example, FIDO keys), to authenticate to the service.

#### Smart card authentication

To use a smart card to authenticate to Microsoft Entra ID, you must first [configure Microsoft Entra certificate-based authentication](/en-us/entra/identity/authentication/concept-certificate-based-authentication) or [configure AD FS for user certificate authentication](/en-us/windows-server/identity/ad-fs/operations/configure-user-certificate-authentication).

#### Third-party identity providers

You can use third-party identity providers as long as they [federate with Microsoft Entra ID](/en-us/entra/identity/devices/device-join-plan#federated-environment).

### Remote session authentication

If you haven't already enabled single sign-on and users haven't saved their credentials locally, they also need to authenticate to the Cloud PC when launching a connection.

#### Single sign-on (SSO)

Single sign-on (SSO) allows the connection to skip the Cloud PC credential prompt and automatically sign the user in to Windows through Microsoft Entra authentication. Microsoft Entra authentication provides other benefits including passwordless authentication and support for third-party identity providers. To get started, review the steps to [configure single sign-on](configure-single-sign-on).

Important

SSO must be configured for external identities to login to the Cloud PC. If SSO isn't configured, the user will be stuck at the remote session authentication prompt.

Without SSO, the client prompts users for their Cloud PC credentials for every connection. The only way to avoid being prompted is to save the credentials in the client. We recommend you only save credentials on secure devices to prevent other users from accessing your resources.

### In-session authentication

After you connect to your Cloud PC, you may be prompted for authentication inside the session. This section explains how to use credentials other than username and password in this scenario.

#### In-session passwordless authentication

Windows 365 supports in-session passwordless authentication using [Windows Hello for Business](/en-us/windows/security/identity-protection/hello-for-business/hello-overview) or security devices like FIDO keys when using the [Windows App](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirection). Passwordless authentication is enabled automatically when the session host and local PC are using the following operating systems:

- Windows 11 Enterprise with the [2022-10 Cumulative Updates for Windows 11 (KB5018418)](https://support.microsoft.com/kb/KB5018418) or later installed.
- Windows 10 Enterprise, versions 20H2 or later with the [2022-10 Cumulative Updates for Windows 10 (KB5018410)](https://support.microsoft.com/kb/KB5018410) or later installed.

For in-session passwordless authentication behavior and app requirements when connecting from other Windows App clients, see the [WebAuthn redirection behavior in Windows App documentation](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirection)

When enabled, all WebAuthn requests in the session are redirected to the local PC. You can use Windows Hello for Business or locally attached security devices to complete the authentication process.

To access Microsoft Entra resources with Windows Hello for Business or security devices, you must enable the FIDO2 Security Key as an authentication method for your users. To enable this method, follow the steps in [Enable FIDO2 security key method](/en-us/azure/active-directory/authentication/howto-authentication-passwordless-security-key#enable-fido2-security-key-method).

Tip

On Windows 11 version 24H2 and later, privacy controls let users decide whether passkeys can be used by an app or website. If a user declines the privacy consent prompt, passkey registration and authentication might not work in Cloud PC sessions. To resolve this issue, direct the user to re-enable passkey access in **Settings** &gt; **Privacy & security** &gt; **Passkey access**. For more information, see [Troubleshoot Windows 11 passkey privacy consent](/en-us/entra/identity/authentication/how-to-plan-rdp-phishing-resistant-passwordless-authentication#troubleshoot-windows-11-passkey-privacy-consent).

#### In-session smart card authentication

To use a smart card in your session, make sure you install the smart card drivers on the Cloud PC and allow smart card redirection as part of [managing RDP device redirections for Cloud PCs](manage-rdp-device-redirections). Review the [client comparison chart](/en-us/azure/virtual-desktop/compare-remote-desktop-clients?pivots=windows-365#in-session-authentication) to make sure your client supports smart card redirection.