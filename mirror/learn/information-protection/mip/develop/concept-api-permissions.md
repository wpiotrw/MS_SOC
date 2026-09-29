---
layout: Conceptual
title: Required API permissions - Microsoft Information Protection SDK | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/information-protection/develop/concept-api-permissions
author: msmbaldwin
ms.author: mbaldwin
uhfHeaderId: MSDocsHeader-Purview
breadcrumb_path: /information-protection/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/5ad50ce6-8a83-ec11-8d21-0022482fa693
feedback_help_link_url: https://learn.microsoft.com/en-us/answers/tags/24/azure-information-protection
feedback_help_link_type: get-help-at-qna
description: Technical details about API permissions needed for Microsoft Purview Information Protection Software Development kit operations.
ms.date: 2026-09-18T00:00:00.0000000Z
ms.topic: concept-article
ms.service: azure-information-protection
locale: en-us
document_id: 41f389c7-5196-0992-5fac-45f9313e1977
document_version_independent_id: c8b83562-799c-fdcb-ef9c-0dd371dd8d5e
original_content_git_url: https://github.com/MicrosoftDocs/Azure-RMSDocs-pr/blob/live/mip/develop/concept-api-permissions.md
site_name: Docs
depot_name: MSDN.MIP
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.MIP/{branchName}{pdfName}
asset_id: develop/concept-api-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: mip/develop/concept-api-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 62b1677d-07d7-83e0-bcf0-23a087bb2392
---

# Required API permissions - Microsoft Information Protection SDK | Microsoft Learn

The MIP SDK uses two backend Azure services for labeling and protection. In the Microsoft Entra app permissions blade, these services are:

- Azure Rights Management Service
- Microsoft Purview Information Protection Sync Service

Grant application permissions to one or more APIs when you use the MIP SDK for labeling and protection. Different application authentication scenarios might require different application permissions. For application authentication scenarios, see [Authentication scenarios](/en-us/entra/identity-platform/authentication-flows-app-scenarios).

Grant tenant-wide admin consent for application permissions when those permissions require administrator consent. For more information, see the [Microsoft Entra documentation](/en-us/entra/identity/enterprise-apps/grant-admin-consent#grant-admin-consent-in-app-registrations).

## Application permissions

Application permissions allow an application in Microsoft Entra ID to act as its own entity, rather than on behalf of a specific user.

| Service | Permission name | Description | Admin consent required |
| --- | --- | --- | --- |
| Azure Rights Management Service | Content.SuperUser | Read all protected content for this tenant | Yes |
| Azure Rights Management Service | Content.DelegatedReader | Read protected content on behalf of a user | Yes |
| Azure Rights Management Service | Content.DelegatedWriter | Create protected content on behalf of a user | Yes |
| Azure Rights Management Service | Content.Writer | Create protected content | Yes |
| Azure Rights Management Service | Application.Read.All | Permission not required for MIP SDK use | Not applicable |
| MIP Sync Service | UnifiedPolicy.Tenant.Read | Read all unified policies of the tenant | Yes |

### Content.SuperUser

Use this permission when an application needs to decrypt all content protected for the specific tenant. Examples of services that require `Content.SuperUser` rights are data loss prevention or cloud access security broker services that must view all content in plaintext to make policy decisions about where that data might flow or be stored.

### Content.DelegatedWriter

Use this permission when an application needs to encrypt content protected by a specific user. Examples of services that require `Content.DelegatedWriter` rights are line-of-business applications that need to encrypt content based on a user's label policies, apply labels, or encrypt content natively. This permission allows the application to encrypt content in the context of the user.

### Content.DelegatedReader

Use this permission when an application needs to decrypt all content protected for a specific user. Examples of services that require `Content.DelegatedReader` rights are line-of-business applications that need to decrypt content based on a user's label policies and display the content natively. This permission allows the application to decrypt and read content in the context of the user.

### Content.Writer

Use this permission when an application needs to list templates and encrypt content. A service that attempts to list templates without this permission receives a token rejected message from the service. Examples of services that require `Content.Writer` are line-of-business applications that apply classification labels to files on export. Content.Writer encrypts the content as the service principal identity, so the owner of the protected files is the service principal identity.

### UnifiedPolicy.Tenant.Read

Use this permission when an application needs to download unified labeling policies for the tenant. Examples of services that require `UnifiedPolicy.Tenant.Read` are applications that need to work with labels as a service principal identity.

## Delegated permissions

Delegated permissions allow an application in Microsoft Entra ID to perform actions on behalf of a particular user.

| Service | Permission name | Description | Admin consent required |
| --- | --- | --- | --- |
| Azure Rights Management Service | user\_impersonation | Create and access protected content for the user | No |
| MIP Sync Service | UnifiedPolicy.User.Read | Read all unified policies a user has access to | No |

### user\_impersonation

Use this permission when an application needs to use Azure Rights Management Services on behalf of the user. Examples of services that require `user_impersonation` rights are applications that need to encrypt or access content based on a user's label policies to apply labels or encrypt content natively.

### UnifiedPolicy.User.Read

Use this permission when an application needs to read unified labeling policies related to a user. Examples of services that require `UnifiedPolicy.User.Read` permissions are applications that need to encrypt and decrypt content based on a user's label policies.