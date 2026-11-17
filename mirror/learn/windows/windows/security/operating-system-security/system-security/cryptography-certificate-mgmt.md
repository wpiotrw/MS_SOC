---
layout: Conceptual
title: Cryptography and certificate management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/cryptography-certificate-mgmt
ms.subservice: itpro-security
ms.service: windows-client
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
ms.localizationpriority: medium
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
author: officedocspr5
ms.author: odocspr
description: Get an overview of cryptography and certificate management in Windows
ms.topic: overview
ms.date: 2026-11-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: skhadeer, aathipsa
ms.custom: os_security, system_security
locale: en-us
document_id: 4275aca7-4d83-7f98-4765-74a0fae6b0d9
document_version_independent_id: 4275aca7-4d83-7f98-4765-74a0fae6b0d9
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/security/operating-system-security/system-security/cryptography-certificate-mgmt.md
site_name: Docs
depot_name: TechNet.windows-security
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.windows-security/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: operating-system-security/system-security/cryptography-certificate-mgmt
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/security/operating-system-security/system-security/cryptography-certificate-mgmt.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 74c168ea-de63-b317-6b2a-272ee4e63b86
---

# Cryptography and certificate management | Microsoft Learn

## Cryptography at a glance

Cryptography uses code to convert data so that only a specific recipient can read it by using a key. Cryptography enforces privacy to prevent anyone except the intended recipient from reading data, integrity to ensure data is free of tampering, and authentication that verifies identity to ensure that communication is secure. The cryptography stack in Windows extends from the chip to the cloud enabling Windows, applications, and services to protect system and user secrets.

Cryptography in Windows is *Federal Information Processing Standards (FIPS) 140* certified. FIPS 140 certification ensures that only US government-approved algorithms are used (RSA for signing, ECDH with NIST curves for key agreement, AES for symmetric encryption, and SHA2 for hashing), tests module integrity to prove that no tampering occurred, and proves the randomness for entropy sources.

Windows cryptographic modules provide low-level primitives such as:

- Random number generators (RNG)
- Symmetric and asymmetric encryption (support for AES 128/256 and RSA 512 to 16,384, in 64-bit increments and ECDSA over NIST-standard prime curves P-256, P-384, P-521)
- Post quantum algorithms (ML-KEM, ML-DSA) and IETF composite ML-DSA/ECDSA
- Hashing (support for SHA-256, SHA-384, SHA-512, and SHA-3\*)
- Signing and verification (padding support for OAEP, PSS, PKCS1)
- Key agreement and key derivation (support for ECDH over NIST-standard prime curves P-256, P-384, P-521, and HKDF)

Windows natively exposes the cryptographic modules through the Crypto API (CAPI) and the [Cryptography Next Generation API (CNG)](/en-us/windows/win32/seccng/cng-portal), which is powered by Microsoft's open-source cryptographic library *SymCrypt*. SymCrypt is part of Microsoft's commitment to transparency, which includes the global [Microsoft Government Security Program](/en-us/security/engineering/ProgramOverview) that aims to provide the confidential security information and resources people need to trust Microsoft's products and services. The program offers controlled access to source code, threat and vulnerability information exchange, opportunities to engage with technical content about Microsoft's products and services, and access to five globally distributed Transparency Centers. Application developers can use the APIs to perform low-level cryptographic operations (BCrypt), key storage operations (NCrypt), protect static data (DPAPI), and securely share secrets (DPAPI-NG).

Windows includes support for the SHA-3 family of hash functions and SHA-3 derived functions (SHAKE, cSHAKE, and KMAC). These are the latest standardized hash functions by the National Institute of Standards and Technology (NIST) and you can use them through the Windows CNG library:

- **Supported SHA-3 hash functions:** SHA3-256, SHA3-384, SHA3-512 (SHA3-224 isn't supported)
- **Supported SHA-3 HMAC algorithms:** HMAC-SHA3-256, HMAC-SHA3-384, HMAC-SHA3-512
- **Supported SHA-3 derived algorithms:** extendable-output functions (XOF) (SHAKE128, SHAKE256), customizable XOFs (cSHAKE128, cSHAKE256), and KMAC (KMAC128, KMAC256, KMACXOF128, KMACXOF256).

## Cryptography in depth

Cryptography uses code to convert data so that only a specific recipient can read it by using a key. Cryptography enforces privacy to prevent anyone except the intended recipient from reading data, integrity to ensure data is free of tampering, and authentication that verifies identity to ensure that communication is secure. The cryptography stack in Windows extends from the chip to the cloud enabling Windows, applications, and services protect system and user secrets.

Cryptography in Windows is Federal Information Processing Standards (FIPS) 140 certified. FIPS 140 certification ensures that US government approved algorithms are being used (RSA for signing, ECDH with NIST curves for key agreement, AES for symmetric encryption, and SHA2 for hashing), tests module integrity to prove that no tampering occurred and proves the randomness for entropy sources.

Windows cryptographic modules provide low-level primitives such as:

- Random number generators (RNG)
- Symmetric and asymmetric encryption (support for AES 128/256 and RSA 512 to 16384, in 64-bit increments and ECDSA over NIST-standard prime curves P-256, P-384, P-521)
- Hashing (support for SHA-256, SHA-384, SHA-512, and SHA-3\*)
- Signing and verification (padding support for OAEP, PSS, PKCS1)
- Key agreement and key derivation (support for ECDH over NIST-standard prime curves P-256, P-384, P-521, and HKDF)

These modules are natively exposed on Windows through the Crypto API (CAPI) and the Cryptography Next Generation API (CNG) which is powered by Microsoft's open-source cryptographic library SymCrypt. Application developers can use these APIs to perform low-level cryptographic operations (BCrypt), key storage operations (NCrypt), protect static data (DPAPI), and securely share secrets (DPAPI-NG).

\*With this release we added support for the SHA-3 family of hash functions and SHA-3 derived functions (SHAKE, cSHAKE, and KMAC). These are the latest standardized hash functions by the National Institute of Standards and Technology (NIST) and can be leveraged through the Windows CNG library. Below is a list of the supported SHA-3 functions:

Supported SHA-3 hash functions: SHA3-256, SHA3-384, SHA3-512 (SHA3-224 is not supported) Supported SHA-3 HMAC algorithms: HMAC-SHA3-256, HMAC-SHA3-384, HMAC-SHA3-512 Supported SHA-3 derived algorithms: extendable-output functions (XOF) (SHAKE128, SHAKE256), customizable XOFs (cSHAKE128, cSHAKE256), and KMAC (KMAC128, KMAC256, KMACXOF128, KMACXOF256).

## Post-quantum cryptography at a glance

Windows supports post-quantum cryptographic algorithms through [Cryptography API: Next Generation (CNG)](/en-us/windows/win32/seccng/cng-portal) and the Certificate and Cryptographic Messaging functions in our core cryptographic library, SymCrypt. Supported algorithms include [ML-KEM](https://csrc.nist.gov/pubs/fips/203/final) for key encapsulation and [ML-DSA](https://csrc.nist.gov/pubs/fips/204/final) for digital signatures.

Visit our [crypto developer's page](/en-us/windows/win32/seccng/typical-cng-programming) to learn more on how you can get started!

Using ML-KEM in scenarios where public key encapsulation or key exchange is desired, can help prepare for *harvest now, decrypt later* threat.

Here are the supported parameter sets:

| **Algorithm** | **Public key size** | **Ciphertext size** | **Shared secret size** | **NIST security level** |
| --- | --- | --- | --- | --- |
| ML-KEM 512 | 800 bytes | 768 bytes | 32 bytes | Level 1 |
| ML-KEM 768 | 1,184 bytes | 1,088 bytes | 32 bytes | Level 3 |
| ML-KEM 1024 | 1,568 bytes | 1,568 bytes | 32 bytes | Level 5 |

Windows supports ML-DSA through CNG for generating and verifying post-quantum digital signatures. Applications can use ML-DSA in scenarios that require verification of identity, data integrity, or authenticity.

Here are the supported parameter sets:

| **Algorithm** | **Public key size** | **Private key size** | **Signature size** | **NIST security level** |
| --- | --- | --- | --- | --- |
| ML-DSA-44 | 1,312 bytes | 2,560 bytes | 2,420 bytes | Level 2 |
| ML-DSA-65 | 1,952 bytes | 4,032 bytes | 3,309 bytes | Level 3 |
| ML-DSA-87 | 2,592 bytes | 4,896 bytes | 4,627 bytes | Level 5 |

### Composite ML-DSA/ECDSA

Windows supports IETF Composite ML-DSA/ECDSA digital signatures, which combine post-quantum ML-DSA with classical ECDSA. Both signature components must be successfully verified for a composite signature to be valid.

The following composite parameter sets are supported:

| **Parameter set** | **Algorithms** |
| --- | --- |
| `44-ECDSA-P256-SHA256` | ML-DSA-44 and ECDSA P-256 |
| `65-ECDSA-P256-SHA512` | ML-DSA-65 and ECDSA P-256 |
| `65-ECDSA-P384-SHA512` | ML-DSA-65 and ECDSA P-384 |
| `87-ECDSA-P384-SHA512` | ML-DSA-87 and ECDSA P-384 |

Algorithm availability depends on the Windows version and cryptographic provider. For more information, see [Composite ML-DSA on Windows](/en-us/dotnet/core/compatibility/cryptography/11/compositemldsa-windows-native).

### Composite signatures in Cryptographic Message Syntax (CMS)

Windows Certificate and Cryptographic Messaging APIs have been extended to support post-quantum and composite digital signatures in Cryptographic Message Syntax (CMS/PKCS#7). These capabilities enable applications to work with composite ML-DSA/ECDSA signatures in cryptographic messages.

### Hybrid Public Key Encryption (HPKE)

Windows cryptographic APIs are being extended to support [Hybrid Public Key Encryption (HPKE)](https://www.rfc-editor.org/rfc/rfc9180), which combines key encapsulation, key derivation, and authenticated encryption to protect data.

HPKE support is under development for Cryptography API: Next Generation (CNG), including BCrypt and NCrypt interfaces. This work will enable applications to use HPKE for cryptographic operations, including scenarios involving post-quantum and hybrid key encapsulation mechanisms.

## Certificates at a glance

To help safeguard and authenticate information, Windows provides comprehensive support for certificates and certificate management. Use the built-in certificate management command-line utility (`certmgr.exe`) or Microsoft Management Console (MMC) snap-in (`certmgr.msc`) to view and manage certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs). Whenever you use a certificate in Windows, the system validates that the leaf certificate and all the certificates in its chain of trust aren't revoked or compromised. The trusted root and intermediate certificates and publicly revoked certificates on the machine serve as a reference for Public Key Infrastructure (PKI) trust and are updated monthly by the Microsoft Trusted Root program. If a trusted certificate or root is revoked, all global devices are updated, so users can trust that Windows automatically protects against vulnerabilities in public key infrastructure. For cloud and enterprise deployments, Windows also offers users the ability to autoenroll and renew certificates in Active Directory with group policy to reduce the risk of potential outages due to certificate expiration or misconfiguration.

## Certificates in depth

Windows offers several APIs to operate and manage certificates. Certificates are crucial to public key infrastructure (PKI) as they provide the means for safeguarding and authenticating information. Certificates are electronic documents used to claim ownership of a public key. Public keys are used to prove server and client identity, validate code integrity, and used in secure emails. Windows offers users the ability to autoenroll and renew certificates in Active Directory with Group Policy to reduce the risk of potential outages due to certificate expiration or misconfiguration. Windows validates certificates through an automatic update mechanism that downloads certificate trust lists (CTL) daily. Trusted root certificates are used by applications as a reference for trustworthy PKI hierarchies and digital certificates. The list of trusted and untrusted certificates are stored in the CTL and can be updated by administrators. In the case of certificate revocation, a certificate is added as an untrusted certificate in the CTL causing it to be revoked globally across user devices immediately.

Windows also offers enterprise certificate pinning to help reduce man-in-the-middle attacks by enabling users to protect their internal domain names from chaining to unwanted certificates. A web application's server authentication certificate chain is checked to ensure it matches a restricted set of certificates. Any web application triggering a name mismatch starts event logging and prevents user access from Microsoft Edge.