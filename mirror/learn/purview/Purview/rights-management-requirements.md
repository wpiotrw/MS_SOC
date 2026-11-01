---
layout: Conceptual
title: Requirements for the Azure Rights Management service | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/rights-management-requirements
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2025-08-31T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Identify the prerequisites required to use the Azure Rights Management encryption service from Microsoft Purview Information Protection.
locale: en-us
document_id: c9cfad74-9133-640b-8ea8-258a79d21184
document_version_independent_id: c9cfad74-9133-640b-8ea8-258a79d21184
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/rights-management-requirements.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: rights-management-requirements
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/rights-management-requirements.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b03f8462-86b4-1820-b214-ec65269a0228
---

# Requirements for the Azure Rights Management service | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Before you start to encrypt items by using [the Azure Rights Management service](azure-rights-management-learn-about) from Microsoft Purview Information Protection, make sure you meet all the requirements.

## Firewalls and network infrastructure

If you have firewalls or similar intervening network devices that are configured to allow specific connections, the network connectivity requirements are listed in the following Microsoft 365 article: [Microsoft 365 Common and Office Online](/en-us/office365/enterprise/urls-and-ip-address-ranges#microsoft-365-common-and-office-online).

The Azure Rights Management service has the following additional requirements:

- **If you use the [Microsoft Purview Information Protection client](information-protection-client)**: To download sensitivity labels and label policies, allow the following URL over HTTPS: \***.protection.outlook.com**
- **If you use web proxies**: If your web proxy requires authentication, you must configure the proxy to use integrated Windows authentication with the user's Active Directory sign in credentials.

    To support **Proxy.pac** files when using a proxy to acquire a token, add the following new registry key:

    - **Path**: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIP\`
    - **Key**: `UseDefaultCredentialsInProxy`
    - **Type**: `DWORD`
    - **Value**: `1`
- **TLS client-to-service connections**. Don't terminate any TLS client-to-service connections, for example to perform packet-level inspection, to the **aadrm.com** URL. Doing so breaks the certificate pinning that clients for the Azure Rights Management service use with Microsoft-managed Certificate Authorities (CAs) to help secure their communication with the Azure Rights Management service.

    To determine whether your client connection is terminated before it reaches the Azure Rights Management service, use the following PowerShell commands:

    ```PowerShell
    $request = [System.Net.HttpWebRequest]::Create("https://admin.na.aadrm.com/admin/admin.svc")
    $request.GetResponse()
    $request.ServicePoint.Certificate.Issuer
    ```

    The result should show that the issuing CA is from a Microsoft CA, for example: `CN=Microsoft Secure Server CA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US`.

    If you see an issuing CA name that isn't from Microsoft, it's likely that your secure client-to-service connection is being terminated and needs reconfiguration on your firewall.
- **Microsoft 365 Enhanced Configuration Service (ECS)**. The Azure Rights Management service must have access to the **config.edge.skype.com** URL, which is a Microsoft 365 Enhanced Configuration Service (ECS).

    ECS provides Microsoft the ability to reconfigure the Azure Rights Management service when it's necessary. For example, ECS is used to control the gradual rollout of features or updates, while the impact of the rollout is monitored from diagnostic data being collected.

    ECS is also used to mitigate security or performance issues with a feature or update. ECS also supports configuration changes related to diagnostic data, to help ensure that the appropriate events are being collected.

    Limiting the **config.edge.skype.com** URL may affect Microsoft’s ability to mitigate errors and may affect your ability to test preview features.

    For more information, see [Essential services for Office](/en-us/microsoft-365-apps/privacy/essential-services).
- **Audit logging URL network connectivity**. The Azure Rights Management service must be able to access the following URLs to support audit logs:

    - `https://*.events.data.microsoft.com`
    - `https://*.aria.microsoft.com` (Android device data only)

### Coexistence with Active Directory Rights Management Services (AD RMS)

Using the on-premises version of Active Directory Rights Management Services (AD RMS) and the Azure Rights Management service side by side, in the same organization, to encrypt content by the same user in the same organization, isn't supported in AD RMS unless you're using the HYOK (hold your own key) configuration for the AD RMS root encryption key.

This scenario isn't supported for a migration to the Azure Rights Management Service. The supported migration paths are:

- [From AD RMS to the Azure Rights Management service](/en-us/azure/information-protection/migrate-from-ad-rms-to-azure-rms)
- [From the Azure Rights Management service to AD RMS](/en-us/powershell/module/aipservice/Set-AipServiceMigrationUrl)

For other, non-migration scenarios, where both services are active in the same organization, both services must be configured so that only one of them allows any given user to encrypt content. Configure such scenarios as follows:

- Use redirections for an [AD RMS to Azure Rights Management migration](/en-us/azure/information-protection/migrate-from-ad-rms-to-azure-rms).
- If both services must be active for different users at the same time, use service-side configurations to enforce exclusivity. Use [onboarding controls](activate-rights-management-service#configuring-onboarding-controls-for-a-phased-deployment) from the Azure Rights Management service, and an ACL on the Publish URL to set **Read-Only** mode for AD RMS.

### Azure Network Security Groups and Service Tags

If you're using an Azure endpoint and an Azure Network Security Group (NSG), make sure to allow access to all ports for the following Service Tags:

- **AzureInformationProtection**
- **AzureActiveDirectory**
- **AzureFrontDoor.Frontend**

Additionally, in this case, the Azure Rights Management service also depends on the following IP addresses and ports:

- **13.107.9.198**
- **13.107.6.198**
- **2620:1ec:4::198**
- **2620:1ec:a92::198**
- **13.107.6.181**
- **13.107.9.181**
- **Port 443**, for HTTPS traffic

Make sure to create rules that allow outbound access to these specific IP addresses, and via this port.

## Supported on-premises servers for the Azure Rights Management service

The following on-premises servers are supported with the Azure Rights Management service when you use the Microsoft Rights Management connector:

- Exchange Server
- SharePoint Server
- File servers that run Windows Server and use File Classification Infrastructure (FCI)

For supported versions, other requirements, and configuration steps for the connector, see [Deploying the Microsoft Rights Management connector](/en-us/information-protection/deploy-rms-connector).

## Supported operating systems

The following operating systems natively support the Azure Rights Management service. However, if you install an app that uses the Azure Rights Management service, such as Microsoft 365 Enterprise apps or the Microsoft Purview Information Protection client, check that app's requirements for supported operating systems.

| OS | Supported versions |
| --- | --- |
| **Windows computers** | - Windows 10 (x86, x64) - Windows 11 (x86, x64) |
| **macOS** | Minimum version of macOS 10.8 (Mountain Lion) |
| **Android phones and tablets** | Minimum version of Android 6.0 |
| **iPhone and iPad** | Minimum version of iOS 11.0 |
| **Windows phones and tablets** | Windows 10 Mobile |

## Microsoft Entra requirements

A Microsoft Entra directory is a requirement for using the Azure Rights Management service. Use an account from a Microsoft Entra directory to sign in to the Microsoft Purview portal.

If you have a subscription that includes Microsoft Purview Information Protection, your Microsoft Entra directory is automatically created for you if needed.

The following sections list additional Microsoft Entra requirements for specific scenarios.

### Support for certificate-based authentication (CBA)

When iOS and Android apps support the Azure Rights Management service, they support certificate-based authentication.

For more information, see [Get started with certificate-based authentication in Microsoft Entra ID with federation](/en-us/entra/identity/authentication/certificate-based-authentication-federation-get-started).

### Multifactor authentication (MFA)

To use multifactor authentication (MFA) with the Azure Rights Management service, you must have at least one of the following installed:

- **Microsoft-managed tenants, with Microsoft Entra ID or Microsoft 365**. Configure Azure MFA to enforce MFA for users.

    For more information, see:

    - [Plan a Microsoft Entra multifactor authentication deployment](/en-us/entra/identity/authentication/howto-mfa-getstarted)
    - [How it works: Microsoft Entra multifactor authentication](/en-us/entra/identity/authentication/concept-mfa-howitworks)
- **Federated tenants, where federation servers operate on-premises**. Configure your federation servers for Microsoft Entra ID or Microsoft 365. For example, if you're using Active Directory Federation Services (AD FS), see [Configure Additional Authentication Methods for AD FS](/en-us/windows-server/identity/ad-fs/operations/configure-additional-authentication-methods-for-ad-fs).

#### Rights Management connector and MFA

The Rights Management connector and the Microsoft Purview Information Protection scanner don't support MFA.

If you deploy the connector or scanner, the following accounts mustn't require MFA:

- The account that installs and configures the connector.
- The service principal account in Microsoft Entra ID, **Aadrm\_S-1-7-0**, that the connector creates.
- The service account that runs the scanner.

### User UPN values don't match their email addresses

Configurations where users' UPN values don't match their email addresses isn't a recommended configuration, and doesn't support single-sign on for the Azure Rights Management service.

If you can't change the UPN value, configure alternate IDs for the relevant users, and instruct them how to sign in to their Office apps by using this alternate ID.

For more information, see [Configuring Alternate Login ID](/en-us/windows-server/identity/ad-fs/operations/configuring-alternate-login-id).

Tip

If the domain name in the UPN value is a domain that is verified for your tenant, add the user's UPN value as another email address to the Microsoft Entra ID **proxyAddresses** attribute. This allows the user to be authorized for the Azure Rights Management service if their UPN value is specified at the time the usage rights are granted.

For more information, see [Learn how user accounts and groups use the Azure Rights Management service](rights-management-users-groups).

### Authenticating on-premises using another authentication provider

If you're using a mobile device or Mac computer that authenticates on-premises using a non-Microsoft authentication provider, it must support the OAuth 2.0 protocol.

### Advanced configurations for Entra ID

For dependent configurations in Entra that can prevent or allow access to the Azure Rights Management service, see [Microsoft Entra configuration for encrypted content](encryption-azure-ad-configuration).