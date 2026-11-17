---
layout: Conceptual
title: FIDO2 security keys | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/security/identity-protection/fido2-security-keys
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
description: The FIDO Alliance, the Fast Identity Online Alliance, or FIDO, is an industry standards body, established to promote authentication technologies and standards that reduce reliance on passwords.
ms.topic: overview
ms.date: 2026-11-03T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: a0c7e6a6-be34-0089-7788-6c52eedd5c43
document_version_independent_id: a0c7e6a6-be34-0089-7788-6c52eedd5c43
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/security/identity-protection/fido2-security-keys.md
site_name: Docs
depot_name: TechNet.windows-security
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.windows-security/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity-protection/fido2-security-keys
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/security/identity-protection/fido2-security-keys.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/691e3042-55ad-4ce1-b5e9-649b1cc47b5c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b7d11190-096c-4ddb-87db-63764f603aac
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 62262ccc-9cac-73e1-a27e-9d6a8b0c705b
---

# FIDO2 security keys | Microsoft Learn

## FIDO2 at a glance

The FIDO Alliance, the Fast Identity Online Alliance, or FIDO, is an industry standards body, established to promote authentication technologies and standards that reduce reliance on passwords. The FIDO Alliance and World Wide Web Consortium (W3C) worked together to define the Client to Authenticator Protocol (CTAP2) and Web Authentication (WebAuthn) specifications. These specifications are the industry standard for providing strong, phishing-resistant, user-friendly, and privacy-preserving authentication across the web and apps. FIDO standards and certifications are becoming recognized as the leading standard for creating secure authentication solutions across enterprises, governments, and consumer markets. Windows 11 can also use external FIDO2 security keys for authentication alongside or in addition to Windows Hello and Windows Hello for Business, which is also a FIDO2-certified passwordless solution. As a result, Windows 11 can be used as a FIDO authenticator for many popular identity management services.

## Managing your security keys

Windows 11 makes FIDO2 security keys easier to manage and use. With security key management in Settings **(preview)**, users can see the passkeys stored on a security key and remove them one at a time, instead of resetting the entire key to clear a single passkey.

### Learn more

- [Passkeys](passkeys/)
- [Enable passkeys (FIDO2) in Microsoft Entra ID](/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2)
- [Enable security key sign-in to Windows](/en-us/entra/identity/authentication/howto-authentication-passwordless-security-key-windows)
- [Microsoft Authenticator](microsoft-authenticator)