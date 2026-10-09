---
layout: Conceptual
title: Azure Virtual Desktop identities and authentication - Azure - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/authentication
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: ChristianMontoya
manager: eliotgra
ms.author: chrimo
ms.service: azure-virtual-desktop
description: Identities and authentication methods for Azure Virtual Desktop.
ms.topic: article
ms.date: 2024-07-16T00:00:00.0000000Z
ms.custom: docs_inherited
locale: en-us
document_id: aaea7a38-df9d-4a98-07b1-7b051af60bd0
document_version_independent_id: aaea7a38-df9d-4a98-07b1-7b051af60bd0
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/authentication.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 00845655-c969-4210-24a7-a696bc505bb7
---

# Azure Virtual Desktop identities and authentication - Azure - Azure Virtual Desktop | Microsoft Learn

In this article, we'll give you a brief overview of what kinds of identities and authentication methods you can use in Azure Virtual Desktop.

## Identities

Azure Virtual Desktop supports different types of identities depending on which configuration you choose. This section explains which identities you can use for each configuration.

Important

Azure Virtual Desktop doesn’t support signing in to Microsoft Entra ID with one user account, then signing in to Windows with a separate user account. This includes using local Windows accounts or other identities that aren’t represented in Microsoft Entra ID to sign in to session hosts. Signing in with different identities at the same time can lead to users reconnecting to the wrong session host, incorrect or missing information in the Azure portal, error messages when using App Attach, and bypassed Microsoft Entra ID authentication and Conditional Access enforcement. Azure Virtual Desktop supports scenarios where the same Microsoft Entra ID identity is used to authenticate to the service and to sign in to the session host. Microsoft recommends using single sign-on (SSO) with Microsoft Entra authentication.

### On-premises identity

Since users must be discoverable through Microsoft Entra ID to access the Azure Virtual Desktop, user identities that exist only in Active Directory Domain Services (AD DS) aren't supported. This includes standalone Active Directory deployments with Active Directory Federation Services (AD FS).

### Hybrid identity

Azure Virtual Desktop supports [hybrid identities](/en-us/entra/identity/hybrid/whatis-hybrid-identity) through Microsoft Entra ID, including those federated using AD FS. You can manage these user identities in AD DS and sync them to Microsoft Entra ID using [Microsoft Entra Connect](/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect). You can also use Microsoft Entra ID to manage these identities and sync them to [Microsoft Entra Domain Services](/en-us/entra/identity/domain-services/overview).

When accessing Azure Virtual Desktop using hybrid identities, sometimes the User Principal Name (UPN) or Security Identifier (SID) for the user in Active Directory (AD) and Microsoft Entra ID don't match. For example, the AD account user@contoso.local may correspond to user@contoso.com in Microsoft Entra ID. Azure Virtual Desktop only supports this type of configuration if either the UPN or SID for both your AD and Microsoft Entra ID accounts match. SID refers to the user object property "ObjectSID" in AD and "OnPremisesSecurityIdentifier" in Microsoft Entra ID.

### Cloud-only identity

Azure Virtual Desktop supports [cloud-only identities](/en-us/microsoft-365/enterprise/manage-microsoft-365-accounts#cloud-only) when using [Microsoft Entra joined VMs](deploy-azure-ad-joined-vm). These users are created and managed directly in Microsoft Entra ID.

Note

You can also assign hybrid identities to Azure Virtual Desktop Application groups that host Session hosts of join type Microsoft Entra joined.

### Federated identity

If you're using a third-party Identity Provider (IdP), other than Microsoft Entra ID or Active Directory Domain Services, to manage your user accounts, you must ensure that:

- Your IdP is [federated with Microsoft Entra ID](/en-us/entra/identity/devices/device-join-plan#federated-environment).
- Your session hosts are Microsoft Entra joined or [Microsoft Entra hybrid joined](/en-us/entra/identity/devices/hybrid-join-plan).
- You enable [Microsoft Entra authentication](configure-single-sign-on) to the session host.

### External identity

External identity support allows you to invite users to your Entra ID tenant and provide them Azure Virtual Desktop resources. There are several requirements and limitations when providing resources to [external identities](/en-us/entra/external-id/identity-providers):

- Requirements
    - **Session host operating system**: The session host must be running one of the following operating systems:
        - Windows 11 Enterprise single or multi-session, versions 24H2 or later with the [2025-09 Cumulative Updates for Windows 11 (KB5065789)](https://support.microsoft.com/kb/KB5065789) or later installed.
        - Windows Server 2025 with the [2026-01 Cumulative Updates for Windows Server 2025 (KB5073379)](https://support.microsoft.com/kb/KB5073379) or later installed.
    - **Session host join type**: The session host must be Entra joined.
    - **Single sign-on**: Single sign-on must be configured for the host pool.
    - **Windows App client**: External identity support is generally available on the Windows App on Windows, Android, or a web browser. External identity support is in preview on the Windows App on macOS. See the [Identity](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#identity) section of Windows App documentation for additional details.
- Limitations
    - **Intune device configuration policies**: Device configuration policies assigned to the external identity won't be applied to the user on the session host. Instead, assign device configuration policies to the device.
    - **Cloud availability**: This feature is available in the Azure public cloud and Azure for US Government, but not in Azure operated by 21Vianet. Connecting as an external identity to a tenant in Azure for US Government is supported in the [Remote Desktop client](/en-us/azure/virtual-desktop/remote-desktop-client/connect-windows-cloud-services?tabs=windows-msrdc-msi#subscribe-to-a-workspace-with-an-external-identity), the Windows App on Windows, and the Windows App on Android.
    - **Cross cloud invites**: Cross-cloud users aren't supported. You can only provide Azure Virtual Desktop resource access to users you invite from social identity providers, Microsoft Entra users from the same Microsoft Azure cloud as the Azure Virtual Desktop environment, or other [identity providers registered in your workforce tenant](/en-us/entra/external-id/identity-providers). You can't assign Azure Virtual Desktop resources for users you invite from Microsoft Azure operated by 21Vianet.
    - **Token protection**: Microsoft Entra has certain [limitations for token protection for external identities](/en-us/entra/identity/conditional-access/concept-token-protection#known-limitations). Learn more about [Windows App support for token protection by platform](/en-us/windows-app/compare-platforms-features#?pivots=azure-virtual-desktop#security).
    - **Kerberos authentication**: External identities can't authenticate to on-premises resources using Kerberos or NTLM protocols.
    - **Microsoft 365 apps**: You can only login to the Windows desktop version of the Microsoft 365 apps if:

        1. The invited user is an Entra-based account or a Microsoft Account that is licensed for Microsoft 365 Apps.
        2. The invited user is not blocked from accessing the Microsoft 365 apps by a conditional access policy from the home organization.

        Regardless of the invited account, you can access Microsoft 365 files shared with you by using the appropriate Microsoft 365 app in the web browser of the session host.
    - **Identity providers**: You can sign-in as an external identity with any of the listed [identity providers](/en-us/entra/external-id/identity-providers), except for one-time passcode sign-in. The following Windows App clients have additional limitations:

        - Android: The only supported social identity provider you can sign in with is a Microsoft account that is configured as a **Connected account** in the Microsoft Authenticator app running on the same device as the client. You can't sign in with Facebook or Google.
    - **Domainless federation**: Azure Virtual Desktop supports external identities through [Domainless SAML IdP Federation](/en-us/entra/external-id/direct-federation#domainless-saml-idp-federation), however these users must redeem their invitation (including the `domain_hint` parameter) before launching the Windows App. If the user connects to the Windows App but hasn't yet redeemed their invite to the Domainless SAML IdP, the user won't be able to authenticate or accept the invite.

See [Microsoft Entra B2B best practices](/en-us/entra/external-id/b2b-fundamentals) for recommendations on configuring your environment for external identities and [Licensing](licensing#) for licensing guidance.

## Authentication methods

When accessing Azure Virtual Desktop resources, there are three separate authentication phases:

- **Cloud service authentication**: Authenticating to the Azure Virtual Desktop service, which includes subscribing to resources and authenticating to the Gateway, is with Microsoft Entra ID. This is where you can enforce Entra ID Conditional Access policies. Also, this is where you can federate from Entra ID to a 3rd-party identity provider.
- **Remote session authentication**: Authenticating to the remote VM. There are multiple ways to authenticate to the remote session, including the recommended single sign-on (SSO).
- **In-session authentication**: Authenticating to applications and web sites within the remote session.

Here is a brief comparison of user authentication options at each authentication phase:

| Cloud service authentication | Remote session authentication | In-session authentication |
| --- | --- | --- |
| - Passwordless authentication (including FIDO security keys, Windows Hello for Business with Cloud Kerberos or Key trust, Microsoft Authenticator multi-factor authentication and more)<br>- Federation to third-party Identity provider<br>- Smartcard (including Entra certificate-based authentication and Windows Hello for Business certificate trust)<br>- Password | - Any **Cloud-service authentication method**, when configured with single sign-on<br>- Smartcard (including Windows Hello for Business certificate trust)<br>- Password | - Passwordless authentication, when configured for in-session passwordless<br>- Smartcard (including Windows Hello for Business certificate trust)<br>- Password |

These are a superset of authentication options per authentication phase. For the list of credential available on the different clients for each of the authentication phase, [compare the clients across platforms](/en-us/previous-versions/remote-desktop-client/compare-remote-desktop-clients?pivots=azure-virtual-desktop#authentication).

Important

In order for authentication to work properly, your local machine must also be able to access the [required URLs for Remote Desktop clients](safe-url-list#remote-desktop-clients).

The following sections provide more information on these authentication phases.

### Cloud service authentication

To access Azure Virtual Desktop resources, you must first authenticate to the service by signing in with a Microsoft Entra ID account. Authentication happens whenever you subscribe to retrieve your resources, connect to the gateway when launching a connection or when sending diagnostic information to the service. The Microsoft Entra ID resource used for this authentication is Azure Virtual Desktop (app ID 9cdead84-a844-4324-93f2-b2e6bb768d07).

#### Multifactor authentication

Follow the instructions in [Enforce Microsoft Entra multifactor authentication for Azure Virtual Desktop using Conditional Access](set-up-mfa) to learn how to enforce Microsoft Entra multifactor authentication for your deployment. That article will also tell you how to configure how often your users are prompted to enter their credentials. When deploying Microsoft Entra joined VMs, note the extra steps for [Microsoft Entra joined session host VMs](set-up-mfa#azure-ad-joined-session-host-vms).

#### Passwordless authentication

You can use any authentication type supported by Microsoft Entra ID, such as [Windows Hello for Business](/en-us/windows/security/identity-protection/hello-for-business/hello-overview) and other [passwordless authentication options](/en-us/entra/identity/authentication/concept-authentication-passwordless) (for example, FIDO keys), to authenticate to the service.

#### Smart card authentication

To use a smart card to authenticate to Microsoft Entra ID, you must first [configure Microsoft Entra certificate-based authentication](/en-us/entra/identity/authentication/concept-certificate-based-authentication) or [configure AD FS for user certificate authentication](/en-us/windows-server/identity/ad-fs/operations/configure-user-certificate-authentication).

#### Third-party identity providers

You can use third-party identity providers as long as they [federate with Microsoft Entra ID](/en-us/entra/identity/devices/device-join-plan#federated-environment).

### Remote session authentication

If you haven't already enabled single sign-on or saved your credentials locally, you'll also need to authenticate to the session host when launching a connection.

#### Single sign-on (SSO)

SSO allows the connection to skip the session host credential prompt and automatically sign the user in to Windows through Microsoft Entra authentication. For session hosts that are Microsoft Entra joined or Microsoft Entra hybrid joined, it's recommended to enable [SSO using Microsoft Entra authentication](configure-single-sign-on). Microsoft Entra authentication provides other benefits including passwordless authentication and support for third-party identity providers.

Azure Virtual Desktop also supports [SSO using Active Directory Federation Services (AD FS)](configure-adfs-sso) for the Windows Desktop and web clients.

Without SSO, the client prompts users for their session host credentials for every connection. The only way to avoid being prompted is to save the credentials in the client. We recommend you only save credentials on secure devices to prevent other users from accessing your resources.

#### Smart card and Windows Hello for Business

Azure Virtual Desktop supports both NT LAN Manager (NTLM) and Kerberos for session host authentication, however Smart card and Windows Hello for Business can only use Kerberos to sign in. To use Kerberos, the client needs to get Kerberos security tickets from a Key Distribution Center (KDC) service running on a domain controller. To get tickets, the client needs a direct networking line-of-sight to the domain controller. You can get a line-of-sight by connecting directly within your corporate network, using a VPN connection or setting up a [KDC Proxy server](key-distribution-center-proxy).

### In-session authentication

Once you're connected to your RemoteApp or desktop, you may be prompted for authentication inside the session. This section explains how to use credentials other than username and password in this scenario.

#### In-session passwordless authentication

Azure Virtual Desktop supports in-session passwordless authentication using [Windows Hello for Business](/en-us/windows/security/identity-protection/hello-for-business/hello-overview) or security devices like FIDO keys when using the [Windows App](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirection). Passwordless authentication is enabled automatically when the session host and local PC are using the following operating systems:

- Windows 11 Enterprise single or multi-session with the [2022-10 Cumulative Updates for Windows 11 (KB5018418)](https://support.microsoft.com/kb/KB5018418) or later installed.
- Windows 10 single or multi-session, versions 20H2 or later with the [2022-10 Cumulative Updates for Windows 10 (KB5018410)](https://support.microsoft.com/kb/KB5018410) or later installed. 
    Note

    Only supported of Windows 10 versions should be used in production deployments that are covered by Extended Security Updates (ESU).
- Windows Server 2022 with the [2022-10 Cumulative Update for Microsoft server operating system (KB5018421)](https://support.microsoft.com/kb/KB5018421) or later installed.

For in-session passwordless authentication behavior and app requirements when connecting from other Windows App clients, see the [WebAuthn redirection behavior in Windows App documentation](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#other-redirection).

To disable passwordless authentication on your host pool, you must [customize an RDP property](customize-rdp-properties). You can find the **WebAuthn redirection** property under the **Device redirection** tab in the Azure portal or set the **redirectwebauthn** property to **0** using PowerShell.

When enabled, all WebAuthn requests in the session are redirected to the local PC. You can use Windows Hello for Business or locally attached security devices to complete the authentication process.

To access Microsoft Entra resources with Windows Hello for Business or security devices, you must enable the FIDO2 Security Key as an authentication method for your users. To enable this method, follow the steps in [Enable FIDO2 security key method](/en-us/entra/identity/authentication/how-to-enable-passkey-fido2#enable-fido2-security-key-method).

#### In-session smart card authentication

To use a smart card in your session, make sure you've installed the smart card drivers on the session host and enabled [smart card redirection](redirection-configure-smart-cards). Review the comparison charts for [Windows App](/en-us/windows-app/compare-platforms-features?pivots=azure-virtual-desktop#device-redirection) and the [Remote Desktop app](/en-us/previous-versions/remote-desktop-client/compare-remote-desktop-clients?pivots=azure-virtual-desktop#device-redirection) to make you can use smart card redirection.