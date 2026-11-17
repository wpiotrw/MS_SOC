---
layout: Conceptual
title: Secure Enterprise Browser Overview (Preview) - Global Secure Access | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-enterprise-browser
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: HULKsmashGithub
ms.author: alexpav
ms.service: global-secure-access
manager: dougeby
description: Learn how secure enterprise browser combines Microsoft Edge and Global Secure Access for private web apps and protected internet and Microsoft 365 browsing.
ms.topic: concept-article
ms.date: 2026-11-13T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: a90b7a78-8b60-c8b2-a438-6bae4062e890
document_version_independent_id: a90b7a78-8b60-c8b2-a438-6bae4062e890
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/global-secure-access/concept-secure-enterprise-browser.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: global-secure-access/concept-secure-enterprise-browser
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/global-secure-access/concept-secure-enterprise-browser.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 3999f5d8-8099-212d-9dfa-a356c7b16179
---

# Secure Enterprise Browser Overview (Preview) - Global Secure Access | Microsoft Learn

Secure enterprise browser integrates Microsoft Edge with Global Secure Access (GSA) for browser-based access to private web applications. It also protects internet and Microsoft 365 traffic without installing the Global Secure Access client. Microsoft Entra Conditional Access steers users to sign in to Microsoft Edge using their work account. Edge Management Service (EMS) delivers the GSA policy to Edge. Edge uses the traffic forwarding policy calculated from your Global Secure Access traffic forwarding profiles.

This article explains the supported scenarios, how traffic forwarding works, and the limitations of the preview. The preview supports Microsoft Edge on Windows and macOS.

## Browser-only access scenarios

You can use secure enterprise browser when you want to allow access to private web applications and when you want to protect user's browsing activities using Global Secure Access policies, without deploying the GSA client software or requiring a managed device.

- **Limited browser-only access for your users with Entra ID work accounts.** Give employees access to selected private web applications through Edge, rather than deploying a client for access from other applications. Use Global Secure Access traffic forwarding profiles and application assignments to define the resources available to those users.
- **Company-owned kiosks.** Protect internet access on Windows kiosks where employees use Edge with their work accounts.
- **Virtual desktop infrastructure (VDI).** Provide employees with access to private web applications and protect their internet access in Edge on Windows VDI devices without installing the Global Secure Access client.

Note

These scenarios require users to sign in to Edge with a work account in your tenant. Business-to-business (B2B) guest accounts aren't supported because users can't sign in to Edge with a B2B guest account.

## Traffic forwarding and policy

Global Secure Access calculates the user's traffic forwarding policy from traffic forwarding profiles, just as it does for the Global Secure Access client. Edge retrieves that policy and uses it to forward browser traffic to the service.

There are three configuration elements for secure enterprise browser connectivity:

- **Global Secure Access Microsoft Edge Configuration** determines which traffic types are enabled for Edge and which forwarding profiles and rules apply to the user. Here, you can selectively enable Internet Access (which includes Microsoft 365), Private Access, or both.
- **Global Secure Access Traffic Forwarding Configuration** determines the resulting traffic forwarding policy for the signed-in user.
- **Edge Management Experience (EMX) policy** enables the integration in Edge - it instructs Edge to follow the traffic forwarding policy for the signed-in user.

For background on profile configuration, see [Global Secure Access traffic forwarding profiles](concept-traffic-forwarding).

## Supported traffic profiles

You can enable Internet Access and Private Access for Microsoft Edge independently. Microsoft 365 traffic is enabled together with Internet Access in the browser enablement configuration.

| Traffic profile | Preview support |
| --- | --- |
| **Internet** | Supported. Global Secure Access applies Microsoft Entra Internet Access policies, including Transport Layer Security (TLS) inspection and bypass policies. |
| **Microsoft 365** | Supported. Enabled together with Internet Access for Edge. The Microsoft traffic forwarding profile determines how Microsoft 365 traffic is forwarded. No TLS inspection, no web filtering policies. |
| **Private Access** | Supported for private web applications configured by fully qualified domain name (FQDN). |
| **Microsoft Entra** | Not supported. |

Global Secure Access delivers TLS inspection certificate trust automatically to Edge. You don't need to deploy the TLS inspection certificate to user's devices or to Microsoft Edge profiles. You still configure the certificate and TLS inspection policies in Global Secure Access.

## Preview requirements and limitations

Plan your deployment around these preview boundaries:

- **Platforms:** Microsoft Edge on Windows and macOS.
- **Global Secure Access client coexistence:** On Windows, running the Global Secure Access client while Microsoft Edge is configured for Global Secure Access is supported. On macOS, this coexistence isn't supported. Enabling the client while Edge is configured for Global Secure Access results in unexpected mutual TLS (mTLS) certificate prompts presented to the user.
- **Minimum Edge version:** 157.0.4341.46.
- **Browser configuration:** EMS policy is the only supported configuration method. Intune app policies aren't supported for enabling this integration in the preview.
- **Identity:** Users sign in to Edge with a work account in the tenant configured for Global Secure Access. B2B guest accounts aren't supported.
- **Microsoft Entra ID traffic:** The Microsoft Entra traffic profile isn't supported. Compliant network checks and universal tenant restrictions for Microsoft Entra ID aren't supported by this preview.
- **Private name resolution:** Private DNS isn't supported. Configure private web applications by FQDN rather than relying on IP-only application definitions to provide private name resolution.