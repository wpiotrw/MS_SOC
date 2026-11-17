---
layout: Conceptual
title: Client ID Metadata Documents in Microsoft Entra ID - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/client-id-metadata-documents
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Learn how Client ID Metadata Documents let OAuth clients identify themselves to Microsoft Entra ID without prior client registration.
ms.topic: concept-article
ms.date: 2026-09-21T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 1c01ace9-d183-cbfd-fc66-10afe9b2ff28
document_version_independent_id: 1c01ace9-d183-cbfd-fc66-10afe9b2ff28
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/client-id-metadata-documents.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/client-id-metadata-documents
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/client-id-metadata-documents.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 11b6c4e1-0a0d-b824-b442-fe31134dc117
---

# Client ID Metadata Documents in Microsoft Entra ID - Microsoft Entra Agent ID | Microsoft Learn

Client ID Metadata Documents (CIMD) let an OAuth client identify itself by using an HTTPS URL instead of a preassigned client ID. The document at that URL contains the client's OAuth metadata. Microsoft Entra ID retrieves and validates the document, represents the client as an agent identity in the tenant, and issues tokens under the tenant's existing consent and security policies.

Important

Client ID Metadata Document support in Microsoft Entra ID is in public preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Some features might be unsupported or have constrained capabilities. For more information, see [Universal License Terms for Online Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all).

CIMD is useful when a client must connect to many authorization servers with which it has no prior relationship. For example, an MCP client can discover remote Model Context Protocol (MCP) servers at runtime, and each server might use a different authorization server. Requiring every client to be registered with every authorization server doesn't scale.

CIMD is defined by the [OAuth Client ID Metadata Document specification](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/). The MCP authorization specification recommends CIMD for clients that don't have another supported registration mechanism.

## How CIMD works with Microsoft Entra ID

A typical CIMD authorization flow has the following steps:

[![Swimlane diagram showing a user connecting an MCP client to an MCP server. The client discovers Microsoft Entra ID, sends an authorization request with a CIMD URL as its client ID, and Entra retrieves and validates the metadata document. Entra obtains consent if required, creates an agent identity if needed, and issues an access token that the client uses to call the MCP server.](media/client-id-metadata-documents/client-id-metadata-document-authorization-flow.svg)](media/client-id-metadata-documents/client-id-metadata-document-authorization-flow.svg#lightbox)

1. An MCP client discovers that an MCP server uses Microsoft Entra ID as its authorization server.
2. The client reads the authorization server metadata and determines that CIMD is supported.
3. The client sends an authorization request. Its `client_id` is the HTTPS URL of its metadata document.
4. Microsoft Entra ID retrieves the document and validates its contents, including an exact match between the requested `client_id` and the document's `client_id`.
5. Microsoft Entra ID derives a stable app ID from the canonical document URL and looks for a matching agent identity in the tenant.
6. If the identity doesn't exist, tenant policy determines whether it can be created through consent. An administrator can instead add the CIMD client in advance.
7. Microsoft Entra ID validates the requested redirect URI and permissions, obtains any required consent, and issues an audience-restricted access token.
8. The client presents the token to the MCP server.

The CIMD URL is the durable identity of the client. Moving the document to another URL creates a different identity and doesn't preserve permissions granted to the old identity.

## How Microsoft Entra represents a CIMD client

Microsoft Entra ID represents a CIMD client as an [agent identity](what-are-agent-identities) in each tenant where the client is approved.

A CIMD-backed agent identity:

- Has an app ID derived from the canonical CIMD URL.
- Stores the CIMD URL as an immutable identifier.
- Has a read-only agent identity blueprint in each tenant, and no blueprint service principal.
- Uses the external metadata document as the source of truth for its OAuth configuration.
- Appears in agent identity inventory, audit logs, and sign-in logs.

Because the metadata remains in the external document, features that inspect OAuth configuration stored on an Entra application object might not evaluate a CIMD client. Review the governance considerations before adopting CIMD.

## When to use CIMD

Implementers should always prefer pre-registration of a client with Entra when possible. For high-volume or strategic integrations, a conventional registered client ID provides the most stable identity and the broadest Entra capabilities. CIMD should only be used when all of the following conditions apply:

- The client must connect to many independently operated authorization servers.
- The authorization servers can't reasonably preregister the client.
- The client uses a user-present, delegated OAuth flow.
- The client can publish stable metadata on a public HTTPS URL.
- The client accepts the limitations described in this article.

An MCP client that discovers many remote servers at runtime is the primary scenario.

## Supported capabilities and limitations

The following table summarizes the capabilities and limitations of CIMD-backed agent identities.

| Capability | CIMD support |
| --- | --- |
| OAuth authorization code flow with a signed-in user | Supported |
| Refresh tokens | Supported |
| Proof Key for Code Exchange (PKCE) | Supported |
| Client credentials flow | Not supported |
| Device code flow | Supported |
| Acting as an OAuth resource or token audience | Not supported |
| ID tokens or SAML tokens for user sign-in | Not supported |
| Shared client secrets | Not supported |
| Publisher verification or Microsoft 365 certification | Not supported |
| Multiple agent identities sharing one blueprint | Not supported |
| Agent user accounts | Not supported |
| Windows Web Account Manager (WAM) | Not supported |
| In-place conversion to or from a conventional client ID | Not supported |

## Security model

CIMD proves that a client controls a URL. It doesn't prove that the client is trustworthy or should receive access to organizational data.

Microsoft Entra ID applies the following protections:

- **HTTPS-only identifiers:** A CIMD client ID must be an HTTPS URL with a path. User information and fragments aren't allowed in the URL.
- **Exact identity match:** The `client_id` in the document must exactly match the URL used as the client ID.
- **Exact redirect matching:** The redirect URI in an authorization request must exactly match a URI in the document.
- **Consent policy enforcement:** Existing tenant consent policy determines whether users can add the client and which delegated permissions they can grant.
- **No app-only tokens:** CIMD clients can't use the client credentials grant.
- **Audience restriction:** Microsoft Entra ID doesn't issue tokens whose audience is the CIMD client.

Under the default recommended consent policy, users can consent only to low-risk OAuth permissions for CIMD clients. Sensitive permissions require administrator consent. For administrator guidance, see [Manage CIMD clients in Microsoft Entra ID](manage-client-id-metadata-document-clients).

## Governance considerations

Before using CIMD, account for the following considerations:

- The client owner controls the metadata document and can change its contents.
- The document URL is immutable in Microsoft Entra ID. A URL change requires a new identity and new consent grants.
- App management policy and other controls that inspect configuration stored on an application object don't cover metadata that remains only in the CIMD document.
- CIMD clients don't support publisher verification or Microsoft 365 certification.
- Entra doesn't provide a tenant-managed domain allowlist or blocklist for CIMD URLs.
- Losing control of the document URL or its domain can affect every tenant that trusts that client identity.

Use least-privilege delegated permissions, preapprove clients that need sensitive access, monitor their sign-ins, and remove identities that are no longer required.