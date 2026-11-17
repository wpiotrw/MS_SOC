---
layout: Conceptual
title: OAuth 2.0 authorization code grant - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/agent-authorization-code-oauth-flow
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Learn how public and confidential clients use the authorization code grant with Agent ID.
ms.topic: reference
ms.date: 2026-11-05T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: jmprieur
locale: en-us
document_id: a9209d69-98dd-9705-7362-4a1933470dbd
document_version_independent_id: a9209d69-98dd-9705-7362-4a1933470dbd
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/agent-authorization-code-oauth-flow.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/agent-authorization-code-oauth-flow
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/agent-authorization-code-oauth-flow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: e94c5b07-5396-19bd-6de3-56e32508d772
---

# OAuth 2.0 authorization code grant - Microsoft Entra Agent ID | Microsoft Learn

The OAuth 2.0 authorization code grant signs in a user and obtains tokens with delegated permissions. The user signs in through a browser, Microsoft Entra ID returns a short-lived authorization code, and the client redeems the code at the token endpoint.

An Agent ID solution can use the grant in two ways:

| Client type | Typical role | Client credential | PKCE |
| --- | --- | --- | --- |
| Public client | A local agent signs in the user directly. | No | Required |
| Confidential client | A server-side web client signs in the user before calling a hosted agent. | Yes | Recommended |

Use Microsoft Authentication Library (MSAL) or Microsoft.Identity.Web instead of creating these requests directly. The requests in this article show the protocol fields for reference.

Warning

Microsoft recommends using the approved SDKs like Microsoft.Identity.Web and Microsoft Entra ID Auth SDK (sidecar) libraries to implement these protocols. Manual implementation of these protocols is complex and error-prone, and using the SDKs helps ensure security and compliance with best practices.

Important

Public-client Agent ID support is in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Some features might be unsupported or have constrained capabilities. For more information, see [Universal License Terms for Online Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all).

## Authorization request

Both client types send the user to the tenant's authorization endpoint:

```http
GET https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize?
    client_id={client-id}
    &response_type=code
    &redirect_uri={encoded-redirect-uri}
    &response_mode=query
    &scope=openid%20profile%20offline_access%20api://{resource-client-id}/{scope}
    &state={random-state}
    &nonce={random-nonce}
    &code_challenge={pkce-challenge}
    &code_challenge_method=S256
```

- `client_id` identifies the public or confidential client. A CIMD-based public client uses its HTTPS metadata document URL as the client ID.
- `redirect_uri` must exactly match a redirect URI configured for the client.
- `scope` contains the delegated permissions the client requests. Omit the resource scope when the client only needs to sign in the user.
- `state` binds the response to the initiating session and helps prevent cross-site request forgery.
- `nonce` binds an OpenID Connect ID token to the initiating session.
- `code_challenge` is derived from a high-entropy PKCE verifier by using SHA-256.

After sign-in and consent, Microsoft Entra ID redirects the browser to the registered redirect URI:

```http
GET {redirect-uri}?code={authorization-code}&state={state}
```

Before redeeming the code, validate `state` and handle any OAuth error returned to the redirect URI.

## Public client token request

A public client can't protect a client credential. It redeems the code by using the PKCE verifier:

```http
POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client_id={agent-id-client-id-or-cimd-url}
&grant_type=authorization_code
&code={authorization-code}
&redirect_uri={redirect-uri}
&scope=openid profile offline_access api://{resource-client-id}/{scope}
&code_verifier={pkce-verifier}
```

Don't send a client secret, certificate assertion, or federated credential in this request.

A registered public-client Agent ID must use [single-instance mode](agent-blueprint#instance-modes-preview). A client that uses a [Client ID Metadata Document](client-id-metadata-documents) can use the document's HTTPS URL as its client ID. For implementation guidance, see [Sign in users from a local agent](authenticate-local-agent).

## Confidential client token request

A confidential client runs on a server that can protect credentials. The server, not browser code, redeems the authorization code. The request includes a client credential and the PKCE verifier when the authorization request used PKCE:

```http
POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client_id={confidential-client-id}
&grant_type=authorization_code
&code={authorization-code}
&redirect_uri={redirect-uri}
&scope=openid profile offline_access api://{agent-blueprint-client-id}/{scope}
&code_verifier={pkce-verifier}
&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
&client_assertion={signed-client-assertion}
```

The example uses a certificate-based client assertion. A client secret is also supported, but use a certificate or workload identity federation when possible.

In a hosted Agent ID solution, the confidential client is normally the upstream web application, not the child Agent ID. Request an access token whose audience is the hosted agent's blueprint, send that access token to the agent API, and use the [On-Behalf-Of flow](agent-on-behalf-of-oauth-flow) to call downstream APIs.

For a single-instance agent identity (preview), `<agent-blueprint-client-id>` denotes the client ID shared by the blueprint and agent identity. For a fleet, it denotes the blueprint's client ID, not an individual child agent's ID. For single-instance mode, configure the upstream client's grant through [Grant the upstream client access](aspnet-core-authenticate-users#grant-the-upstream-client-access) before sign-in; browser consent doesn't support the agent identity as a resource.

Don't send an authorization code or ID token to the hosted agent API. Child Agent IDs in the confidential-client pattern don't initiate an interactive `/authorize` request.

## Token response

If the request succeeds, Microsoft Entra ID returns tokens such as:

```json
{
  "token_type": "Bearer",
  "scope": "api://<resource-client-id>/<scope>",
  "expires_in": 3599,
  "access_token": "<access-token>",
  "refresh_token": "<refresh-token>",
  "id_token": "<id-token>"
}
```

The exact response depends on the requested scopes:

- Use the access token only with the resource identified by its `aud` claim.
- Use the ID token to establish the user's sign-in session, not to call an API.
- A refresh token is returned when the request and policy allow offline access.

## Security requirements

- Use PKCE with the `S256` challenge method for public clients. Also use PKCE for confidential clients when the library supports it.
- Match the redirect URI exactly in the authorization and token requests.
- Generate a new `state`, `nonce`, and PKCE verifier for each authorization request.
- Redeem an authorization code only once and only from the client that started the request.
- Don't log authorization codes, client credentials, access tokens, refresh tokens, or ID tokens.
- Validate access tokens in the API. Don't treat possession of an authorization code or ID token as API authorization.