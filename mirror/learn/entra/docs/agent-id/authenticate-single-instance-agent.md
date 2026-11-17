---
layout: Conceptual
title: Single-instance OAuth (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/authenticate-single-instance-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Understand direct authentication with a single-instance Agent ID and find the local, ASP.NET Core, and sidecar walkthroughs.
ms.topic: concept-article
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 2e5981c8-aec2-5af9-419f-9d2aa29cead0
document_version_independent_id: 2e5981c8-aec2-5af9-419f-9d2aa29cead0
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/authenticate-single-instance-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/authenticate-single-instance-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/authenticate-single-instance-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 31df8532-5c0f-aecd-1897-745844275024
---

# Single-instance OAuth (preview) | Microsoft Learn

A single-instance Agent ID (preview) authenticates directly with the client ID it shares with its blueprint. It uses the same authentication-library APIs as a regular application. It doesn't acquire an intermediate blueprint impersonation token or send `fmi_path`.

The blueprint and Agent ID have different directory object IDs. Configure credentials on the blueprint, grant permissions to the Agent ID, and use their shared OAuth client ID for token requests. A single-instance blueprint has no blueprint principal.

## Choose an integration path

Important

Single-instance agent identities are in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Some features might be unsupported or have constrained capabilities. For more information, see [Universal License Terms for Online Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all).

Choose a walkthrough based on where your agent runs. If you're building a platform that hosts separate agents for teams or customers, follow the fleet guidance.

| Environment | Walkthrough |
| --- | --- |
| Local public client | [Sign in users from a local agent](authenticate-local-agent). |
| Cloud agent with ASP.NET Core | [Call a custom API as an agent](call-api-custom). |
| Cloud agent with the Auth SDK sidecar | [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities). |
| Shared runtime with many identities | [Plan an agent fleet](plan-agent-fleet). |

Authentication requires a provisioned single-instance Agent ID and a tenant enabled for authentication. Successful Microsoft Graph provisioning alone doesn't establish authentication enablement. For setup, see [Create a single-instance agent identity](create-single-instance-agent).

## Sign in a user

Local public clients use authorization code flow with PKCE and no client credential. Confidential clients use a credential on the blueprint. An authentication library handles state, PKCE, token caching, and refresh rather than requiring hand-built protocol requests.

For local sign-in and refresh behavior, follow [Sign in users from a local agent](authenticate-local-agent). For a front end that calls a hosted agent API, follow [Authenticate users to an ASP.NET Core agent API](aspnet-core-authenticate-users) or [Authenticate users with the sidecar](sidecar-authenticate-users).

## Grant application permissions

Declaring permissions on the blueprint doesn't grant them. An administrator grants application permissions to the agent identity. Browser-based admin consent requires a registered `web` redirect URI, even for an unattended agent.

For the consent request and assignment verification, see [Grant application permissions in the cloud-agent walkthrough](call-api-custom#grant-application-permissions). For Microsoft Graph, see [Grant application permissions to an agent identity](grant-application-permissions-agent-identity).

## Request an app-only token

The standard client credentials flow uses the shared client ID, the blueprint credential, and the resource's `/.default` scope. It doesn't use an Agent ID override.

Follow [Call a custom API with ASP.NET Core](call-api-custom#call-the-api) for `CreateAuthorizationHeaderForAppAsync`, or [Call a custom API with the sidecar](sidecar-call-custom-api-as-agent) for the corresponding HTTP endpoint. For protocol parameters, see [OAuth 2.0 client credentials flow](../identity-platform/v2-oauth2-client-creds-grant-flow).

## Call a downstream API on behalf of a user

OBO exchanges an incoming user access token for a downstream token. The incoming token must target the agent's shared client ID, not Microsoft Graph or another resource. The agent authenticates with its blueprint credential. The downstream API evaluates the user's delegated access.

Two separate grants are required: front-end access to the agent's exposed scope and the agent's delegated access to the downstream API. During preview, grant front-end access through Microsoft Graph as described in [Grant the upstream client access](aspnet-core-authenticate-users#grant-the-upstream-client-access).

Follow [Call a custom API as a user with ASP.NET Core](aspnet-core-call-custom-api-as-user) or [Call a custom API as a user with the sidecar](sidecar-call-custom-api-as-user). These walkthroughs use standard OBO, without an intermediate blueprint exchange. For protocol parameters, see [OAuth 2.0 On-Behalf-Of flow](../identity-platform/v2-oauth2-on-behalf-of-flow).

## Verify access

A successful token response establishes token issuance, not authorization at the API. API authorization depends on a valid signature, issuer, audience, and lifetime, plus the required scope or role. Requests with insufficient permissions are rejected. Tokens, certificate assertions, and private keys aren't safe diagnostic output.

For API-side validation, see [Secure a web API with Microsoft Entra ID](how-to-validate-agent-tokens-downstream-api).