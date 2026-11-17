---
layout: Conceptual
title: Windows Hello for Business overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/
ms.subservice: itpro-security
ms.service: windows-client
recommendations: true
adobe-target: true
ms.collection: tier1
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
ms.localizationpriority: medium
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
author: officedocspr5
ms.author: odocspr
description: Learn how Windows Hello for Business replaces passwords with strong two-factor authentication on Windows devices.
ms.topic: overview
ms.date: 2026-03-29T00:00:00.0000000Z
ms.custom: identity_protection, passwordless, hello_for_business
locale: en-us
document_id: 424b6dd0-819f-95a0-7676-a235e1d4867e
document_version_independent_id: 14e88cb8-0063-cc8d-8b39-4e18d448b0b9
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/security/identity-protection/hello-for-business/index.md
site_name: Docs
depot_name: TechNet.windows-security
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.windows-security/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity-protection/hello-for-business/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/security/identity-protection/hello-for-business/index.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/798bd9d1-9cc5-4fc7-b0e5-8699d1f6ce2a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5717abce-88c6-42bd-821b-0d6370225d52
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b5dc5f65-34a8-4bfc-9917-97d1e20c88b2
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b472b5d5-52dd-4477-99f9-23fa324788f7
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
platformId: 8b750341-1bc5-b194-965a-bf0d612d7a4b
---

# Windows Hello for Business overview | Microsoft Learn

## Windows Hello for Business at a glance

Windows Hello for Business extends Windows Hello to work with an organization's Active Directory and Microsoft Entra ID accounts. It provides single sign-on access to work or school resources such as OneDrive, work email, and other business apps. Windows Hello for Business also gives IT admins the ability to manage PIN and other sign-in requirements for devices connecting to work or school resources.

After Windows Hello for Business is provisioned, users can use a PIN, face, or fingerprint to unlock credentials and sign in to their Windows device.

Provisioning methods include:

Passkeys (preview), which provide a seamless way for users to authenticate to Microsoft Entra ID without entering a username or password Temporary Access Pass (TAP), a time-limited passcode with strong authentication requirements issued through Microsoft Entra ID Existing multifactor authentication with Microsoft Entra ID, including the Microsoft Authenticator app Windows Hello for Business enhances security by replacing traditional usernames and passwords with a combination of a security key or certificate and a PIN or biometric data. This setup securely maps the credentials to a user account.

There are various deployment models available for Windows Hello for Business, providing flexibility to meet the diverse needs of different organizations. Among these models, the Hybrid cloud Kerberos trust model is recommended and considered the simplest for organizations operating in hybrid environments.

### Learn More

- [Windows Hello for Business overview](/en-us/windows/security/identity-protection/hello-for-business)
- [Enable passkeys (FIDO2) for your organization](/en-us/entra/identity/authentication/how-to-enable-passkey-fido2)

## Windows Hello for Business in depth

*Windows Hello* is an authentication technology that allows users to sign in to their Windows devices using biometric data, or a PIN, instead of a traditional password. It provides enhanced security through phish-resistant two-factor authentication, and built-in brute force protection. With FIDO/WebAuthn, Windows Hello can also be used to sign in to supported websites, reducing the need to remember multiple complex passwords.

*Windows Hello for Business* is an **extension** of Windows Hello that provides enterprise-grade security and management capabilities, including device attestation, certificate-based authentication, and conditional access policies. Policy settings can be deployed to devices to ensure they're secure and compliant with organizational requirements.

The following table lists the main authentication and security differences between Windows Hello and Windows Hello for business:

| - | Windows Hello | Windows Hello for Business |
| --- | --- | --- |
| **Authentication** | Users can authenticate to:- A Microsoft account (MSA)- Identity providers (IdPs) that support [Fast ID Online (FIDO) v2.0](https://fidoalliance.org/) authentication | Users can authenticate to:- A Microsoft Entra ID account- An Active Directory account- Identity provider (IdP) or relying party (RP) services that support [Fast ID Online (FIDO) v2.0](https://fidoalliance.org/) authentication |
| **Security** | It uses **key-based** authentication.There's no symmetric secret (password) which can be stolen from a server or phished from a user and used remotely. | It uses **key-based** or **certificate-based** authentication.There's no symmetric secret (password) which can be stolen from a server or phished from a user and used remotely. |

Windows Hello can also be used with local accounts for convenient sign-ins, instead of entering a password. This configuration isn't backed by asymmetric (public/private) key, so it doesn't offer the same level of security as key-based or certificate-based authentication that is available with MSA or Microsoft Entra accounts. In all other aspects, using Windows Hello with a local account is like using it with MSA or Entra ID. For enhanced security, it's recommended to use Windows Hello with a Microsoft account (MSA) or identity providers (IdPs) that support FIDO2 authentication.

Note

FIDO2 (Fast Identity Online) authentication is an open standard for passwordless authentication. It allows users to sign in to their devices and apps using biometric authentication or a physical security key, without the need for a traditional password. FIDO2 support in Windows Hello and Windows Hello for Business provides an additional layer of security and convenience for users, while also reducing the risk of password-related attacks.

## Benefits

Windows Hello for Business provides many benefits, including:

- It helps to strengthen protections against credential theft. An attacker must have both the device and the biometric or PIN, making it much more difficult to gain access without the user's knowledge
- Since no passwords are used, it circumvents phishing and brute force attacks. Most importantly, it prevents server breaches and replay attacks because the credentials are asymmetric and generated within isolated environments of TPMs
- Users get a simple and convenient authentication method (backed up with a PIN) that's always with them, so there's nothing to lose. The use of a PIN doesn't compromise security, since Windows Hello has built-in brute force protection, and the PIN never leaves the device
- You can add biometric devices as part of a coordinated rollout or to specific users, as needed

The following video shows a demonstration of Windows Hello for Business in action, where a user signs in with a fingerprint:

## Windows Hello and two factor authentication

Windows Hello for Business uses a two-factor authentication method that combines a device-specific credential with a biometric or PIN gesture. This credential is tied to your identity provider, such as Microsoft Entra ID or Active Directory, and can be used to access organization apps, websites, and services.

After an initial two-step verification of the user during provisioning, Windows Hello is set up on the user's device and Windows asks the user to set a gesture, which can be a biometric, and a PIN. The user provides the gesture to verify their identity. Windows then uses Windows Hello to authenticate users.

Windows Hello for Business is considered two-factor authentication based on the observed authentication factors of: *something you have*, *something you know*, and *something that's part of you*. Windows Hello for Business incorporates two of these factors: something you have (the user's private key protected by the device's security module) and something you know (your PIN). With the proper hardware, you can enhance the user experience by introducing biometrics. By using biometrics, you can replace the *something you know* authentication factor with the *something that is part of you* factor, with the assurances that users can fall back to the *something you know factor*. Windows Hello for Business also qualifies as a standalone multifactor authentication method in Microsoft Entra ID. It satisfies step-up prompts, authentication strengths, and sign-in frequency checks without requiring an additional credential.

## Biometric sign-in

Windows Hello provides reliable, fully integrated biometric authentication based on facial recognition or fingerprint matching. Windows Hello uses a combination of special infrared (IR) cameras and software to increase accuracy and guard against spoofing. Major hardware vendors are shipping devices that have integrated Windows Hello-compatible cameras and fingerprint readers.

On devices that support Windows Hello, an easy biometric gesture unlocks users' credentials:

- **Facial recognition**: this type of biometric recognition uses special cameras that see in IR light, which allows them to reliably tell the difference between a photograph or scan and a living person. Several vendors offer external cameras that incorporate this technology, and many laptop manufacturers incorporate it into their devices
- **Fingerprint recognition**: this type of biometric recognition uses a capacitive fingerprint sensor to scan your fingerprint. Most existing fingerprint readers work with Windows, whether they're external or integrated into laptops or USB keyboards
- **Iris Recognition**: this type of biometric recognition uses cameras to perform scan of your iris

Windows stores biometric data that is used to implement Windows Hello securely on the local device only. The biometric data doesn't roam and is never sent to external devices or servers. Because Windows Hello only stores biometric identification data on the device, there's no single collection point an attacker can compromise to steal biometric data.

## Windows edition and licensing requirements

The following table lists the Windows editions that support Windows Hello for Business:

| Windows Pro | Windows Enterprise | Windows Pro Education/SE | Windows Education |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

Windows Hello for Business license entitlements are granted by the following licenses:

| Windows Pro/Pro Education/SE | Windows Enterprise E3 | Windows Enterprise E5 | Windows Education A3 | Windows Education A5 |
| --- | --- | --- | --- | --- |
| Yes | Yes | Yes | Yes | Yes |

For more information about Windows licensing, see [Windows licensing overview](/en-us/windows/whats-new/windows-licensing).

Note

Windows Hello for Business doesn't work with [Microsoft Entra Domain Services](/en-us/entra/identity/domain-services/overview).

## Hardware requirements

Microsoft collaborates with manufacturers to help ensuring a high-level of performance and protection is met by each sensor and device, based on the following requirements:

- **False Accept Rate (FAR):** represents the instance a biometric identification solution verifies an unauthorized person. This is normally represented as a ratio of number of instances in a given population size, for example 1 in 100,000. This can also be represented as a percentage of occurrence, for example, 0.001%. This measurement is heavily considered the most important regarding the security of the biometric algorithm
- **False Reject Rate (FRR):** represents the instances a biometric identification solution fails to verify an authorized person correctly. Represented as a percentage, the sum of the True Accept Rate and False Reject Rate is 1. Can be with or without anti-spoofing or liveness detection

### Fingerprint sensor requirements

To allow fingerprint matching, devices must have fingerprint sensors and software. Fingerprint sensors can be touch sensors (large area or small area) or swipe sensors. Each type of sensor has its own set of detailed requirements that must be implemented by the manufacturer, but all of the sensors must include anti-spoofing measures.

Acceptable performance range for small to large size touch sensors:

- False Accept Rate (FAR): &lt;0.001 - 0.002%
- Effective, real world FRR with Anti-spoofing or liveness detection: &lt;10%

Acceptable performance range for swipe sensors:

- False Accept Rate (FAR): &lt;0.002%
- Effective, real world FRR with Anti-spoofing or liveness detection: &lt;10%

### Facial recognition sensors

To allow facial recognition, you must have devices with integrated special infrared (IR) sensors and software. Facial recognition sensors use special cameras that see in IR light, letting them tell the difference between a photo and a living person while scanning an employee's facial features. These sensors, like the fingerprint sensors, must also include anti-spoofing measures (required) and a way to configure them (optional).

- False Accept Rate (FAR): &lt;0.001%
- False Reject Rate (FRR) without Anti-spoofing or liveness detection: &lt;5%
- Effective, real world FRR with Anti-spoofing or liveness detection: &lt;10%

Note

Windows Hello face authentication doesn't support wearing a mask during enrollment or authentication. If your working environment doesn't allow you to remove a mask temporarily, consider using PIN or fingerprint.

### Iris recognition sensor requirements

To use Iris authentication, you need a [HoloLens 2 device](/en-us/hololens/). All HoloLens 2 editions are equipped with the same sensors. Iris is implemented the same way as other Windows Hello technologies and achieves biometrics security FAR of 1/100K.

For more information about the hardware requirements for Windows Hello, see [Windows Hello biometric requirements](/en-us/windows-hardware/design/device-experiences/windows-hello-biometric-requirements).