---
layout: Conceptual
title: Embedded native authentication CORS concepts - Microsoft identity platform | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/identity-platform/concept-native-authentication-cors
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: /entra/identity-platform/developer-support-help-options
author: cilwerner
ms.author: cwerner
ms.service: identity-platform
description: Understand CORS and proxy requirements for SPAs with Embedded native authentication and BYO UX websites, and why native Android and iOS calls don't need CORS.
ms.topic: concept-article
ms.custom: msecd-doc-authoring-1030
ms.date: 2026-11-17T00:00:00.0000000Z
ai-usage: ai-generated
locale: en-us
document_id: f9db028a-dbef-8762-dc99-9f0add4f316b
document_version_independent_id: f9db028a-dbef-8762-dc99-9f0add4f316b
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/identity-platform/concept-native-authentication-cors.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity-platform/concept-native-authentication-cors
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/identity-platform/concept-native-authentication-cors.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 6f5ad961-ea8d-80ce-af48-473e2afba9db
---

# Embedded native authentication CORS concepts - Microsoft identity platform | Microsoft Learn

Cross-Origin Resource Sharing (CORS) controls whether browser code can read a response from another origin. Single-page applications (SPAs) with Embedded native authentication and Bring Your Own UX (BYO UX) websites need a proxy or edge CORS policy for cross-origin calls to the Native Authentication API.

Android and iOS apps that call the API through native HTTP transports don't need CORS or a CORS proxy. They call the configured service authority directly. The requirements in this article apply to browser requests, not those native API calls.

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](../external-id/media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

**Authentication approach:** Embedded native authentication.

Important

The Native Authentication API V2 is in preview. The [Native Authentication API V1](reference-native-authentication-api-v1) remains generally available. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to preview features.

## Why browser CORS applies

A browser app and its tenant authentication endpoint typically have different origins. For cross-origin requests, the browser checks the server's CORS response headers before exposing the response to application code.

An origin includes the scheme, host, and port. Sharing a parent domain doesn't make two origins the same.

The API's JSON `POST` requests and password-update `PUT` requests require a preflight check. The browser sends `OPTIONS` with the requested method and headers before sending the authentication request. A header such as `client-request-id` also triggers preflight. Form-encoded OAuth requests are part of the same integration; their method and headers determine whether preflight is required.

Browser code remains subject to CORS even when it runs in an embedded webview. CORS governs browser response access; caller authentication and abuse prevention require separate controls.

## Why a proxy is required

The native authentication service handles `OPTIONS` before parsing the API request or invoking its credential action. It returns an empty HTTP `200`. When the request includes `Origin`, the service advertises the action's accepted methods and echoes requested headers in `Access-Control-Allow-Headers`. No additional preflight feature flag is needed.

The service doesn't supply `Access-Control-Allow-Origin` or `Access-Control-Allow-Credentials`. Your proxy or edge supplies the explicit allowed-origin policy. It can forward the service's preflight response or answer a validated preflight locally. An HTML error page with an outer HTTP `200` isn't a successful preflight response.

The proxy preserves the API operations, bodies, and transaction state. Forwarding or omitting the upstream `Origin` header is an implementation choice, not a universal requirement to remove it. Apply your choice consistently and check authorization, native operations, and token exchange together.

## Service authority and proxy transport

For the browser integrations covered in this article, Embedded native authentication and BYO UX service API URLs use a tenant-verified custom authentication domain and the tenant GUID:

```text
https://<tenant-verified-custom-domain>/<tenant-GUID>
```

For example, the service authority might be `https://login.contoso.com/aaaabbbb-0000-cccc-1111-dddd2222eeee`. A local transport prefix might instead be `http://localhost:3001/api`. These values serve different purposes:

| Value | Purpose |
| --- | --- |
| **Service authority** | Identifies the tenant's authentication service. Configure this custom domain and tenant GUID as the upstream authority and validate service-returned links against it. |
| **Transport prefix** | Identifies the browser-facing proxy. It can replace the authority portion of a validated API request for transport, but doesn't change the service authority or transaction. |

With that local prefix, a service path of `/<tenant-GUID>/api/v2.0/signin/start` maps to `/api/api/v2.0/signin/start`. The first `/api` is the proxy prefix; the second belongs to the service path. OAuth requests similarly map to `/api/oauth2/v2.0/authorize-challenge` or `/api/oauth2/v2.0/token`.

For these browser integrations, don't configure a `ciamlogin.com` address as the application's service API authority. Platform-managed origin routing behind a verified custom domain doesn't replace this requirement. Non-browser clients using native HTTP transports don't require a custom domain. See [Configure the API authority](how-to-native-authentication-configure-app#configure-the-api-authority).

## Proxy contract

Configure these settings in your reverse proxy. Forward API bodies and service status codes directly.

| Setting | Configuration |
| --- | --- |
| **Upstream authority** | Set `https://<tenant-verified-custom-domain>/<tenant-GUID>` as the fixed destination. For a custom-domain edge, use the platform's documented service-origin configuration. |
| **Routes** | Allow `/api/v2.0/*`, `/oauth2/v2.0/authorize-challenge`, and `/oauth2/v2.0/token` under the tenant-GUID prefix. |
| **Methods and preflight** | Enable `POST`, password-update `PUT`, and `OPTIONS`. Handle preflight locally or forward it to the service. Approve only configured methods and headers; return `Access-Control-Allow-Methods: POST, PUT`. |
| **Browser origin** | Set `Access-Control-Allow-Origin` to your app's exact origin, such as `https://app.contoso.com`. Return it only for matching `Origin` requests, including on error responses. |
| **Allowed request headers** | Set `Access-Control-Allow-Headers` to `Content-Type, Accept, client-request-id`. For Microsoft Authentication Library (MSAL) clients, also allow `x-client-sku`, `x-client-ver`, `x-client-os`, `x-client-cpu`, `x-client-current-telemetry`, and `x-client-last-telemetry`. |
| **Exposed response headers** | Set `Access-Control-Expose-Headers` to `Retry-After, client-request-id, x-ms-request-id, x-ms-clitelem`. |
| **Caching** | Disable proxy and CDN caching. Add `Cache-Control: no-store` to every response. |
| **Redirects and failures** | Disable automatic upstream redirects and remove response `Location` headers. Return explicit proxy errors for connection failures and timeouts. |

The [API reference](reference-native-authentication) defines the operation-specific methods, headers, request bodies, and responses.

## Proxy implementations

Choose an implementation that fits your hosting environment and meets the same contract:

- [Local proxy](how-to-native-authentication-cors-local) for JavaScript sample development.
- [Azure Functions proxy](how-to-native-authentication-cors-azure-functions) with an adapted HTTP-trigger handler.
- [Azure Front Door proxy](how-to-native-authentication-cors-front-door) on the tenant's custom authentication domain.

The JavaScript SDK's `customAuth.authApiProxyUrl` doesn't remap absolute HAL links. Use CORS policy at the custom-domain edge for those SDK requests. The local and Functions recipes instead show a custom-client transport that validates and maps service links.

The local proxy binds to a loopback interface and isn't a shared hosting recipe. For a deployed proxy, also review capacity, cost, access controls, diagnostics retention, and recovery procedures for your environment.