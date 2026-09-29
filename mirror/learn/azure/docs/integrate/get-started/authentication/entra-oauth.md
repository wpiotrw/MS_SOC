---
layout: Conceptual
monikers:
- azure-devops
defaultMoniker: azure-devops
versioningType: Ranged
title: Build Azure DevOps integrations with Microsoft Entra OAuth apps - Azure DevOps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/entra-oauth?view=azure-devops
config_moniker_range: azure-devops || >= azure-devops-2022 <= azure-devops-server
feedback_system: Standard
feedback_product_url: https://developercommunity.visualstudio.com/AzureDevOps
breadcrumb_path: /azure/devops/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-AzureDevOps
archive_url: https://docs.microsoft.com/en-us/previous-versions/azure/devops/all/
ms.topic: overview
ms.manager: wiwagn
author: chcomley
ms.author: chcomley
ms.date: 2026-04-02T00:00:00.0000000Z
ms.service: azure-devops
ms.version: ALM
MSHAttr.msprod: ms.prod:ALM
ms.prodfamily: ALM
description: 'Microsoft Entra OAuth apps: Discover how to build secure Azure DevOps integrations using delegated authentication and enhance your development process.'
ms.subservice: azure-devops-security
ms.custom: pat-reduction, UpdateFrequency3
ms.reviewer: chcomley
locale: en-us
document_id: df147a01-bb29-8573-7c94-66adc55f1bba
document_version_independent_id: df147a01-bb29-8573-7c94-66adc55f1bba
original_content_git_url: https://github.com/MicrosoftDocs/azure-devops-docs-pr/blob/live/docs/integrate/get-started/authentication/entra-oauth.md
default_moniker: azure-devops
site_name: Docs
depot_name: MSDN.azure-devops-docs
page_type: conceptual
toc_rel: ../../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.azure-devops-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: integrate/get-started/authentication/entra-oauth
moniker_range_name: 348281b5e6207d94331bdbf3987314df
monikers:
- azure-devops
item_type: Content
source_path: docs/integrate/get-started/authentication/entra-oauth.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5bd2b3fa-c186-4b92-a3c8-09f22a249d37
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7eba7926-b7b2-4a7a-bf89-e6ac53b3e7f6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 8a880040-d633-1c99-689c-72292e5583e6
---

# Build Azure DevOps integrations with Microsoft Entra OAuth apps - Azure DevOps | Microsoft Learn

**Azure DevOps Services**

The Microsoft identity platform offers many ways to authenticate users through [the OAuth 2.0 protocol](/en-us/entra/identity-platform/v2-protocols). In this article, *OAuth tokens* refers to [on-behalf-of user flows](/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow), also known as [delegated flows](/en-us/entra/identity-platform/delegated-access-primer), where apps request tokens to perform actions for their users.

This approach differs from apps that perform actions on-behalf-of themselves. For that approach, use [service principals and managed identities](service-principal-managed-identity).

## Resources for developers

- [Register an application with the Microsoft identity platform](/en-us/entra/identity-platform/quickstart-register-app)
- [Add permissions for access to Microsoft Graph](/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-microsoft-graph): Learn how to add delegated permissions from an Azure resource. Instead of Microsoft Graph, select `Azure DevOps` from the list of resources.
- [Read about scopes and permissions in the Microsoft identity platform](/en-us/entra/identity-platform/scopes-oidc): Understand the `.default` scope. See the scopes available for Azure DevOps in [our list of scopes](oauth#available-scopes).
- [Request permissions through consent](/en-us/entra/identity-platform/consent-types-developer)
- [Use authentication libraries](/en-us/entra/identity-platform/reference-v2-libraries) and [code samples](/en-us/entra/identity-platform/sample-v2-code?tabs=apptype)
- [Explore support and help options for developers](/en-us/entra/identity-platform/developer-support-help-options)

## Resources for admins

- [Understand application management in Microsoft Entra ID](/en-us/entra/identity/enterprise-apps/what-is-application-management)
- [Add an enterprise application](/en-us/entra/identity/enterprise-apps/add-application-portal)
- [Explore the consent experience for applications in Microsoft Entra ID](/en-us/entra/identity-platform/application-consent-experience)

## Tips for building and migrating

- Microsoft Entra apps don't natively support Microsoft account (MSA) users for the Azure DevOps resource. If you're building an app that must cater to MSA users or support both Microsoft Entra and MSA users, [Azure DevOps OAuth apps](azure-devops-oauth) remain your best option. Microsoft is currently working on native support for MSA users through Microsoft Entra OAuth.
- Azure DevOps' resource identifier: `499b84ac-1321-427f-aa17-267ca6975798`
- Azure DevOps' resource URI: `https://app.vssps.visualstudio.com`
- Use the `.default` scope when requesting a token with all scopes that the app is permissioned for.
- In a previous Azure DevOps OAuth app, you might have used Azure DevOps user identifiers that don't exist in Microsoft Entra. When migrating to Microsoft Entra, use the [ReadIdentities API](/en-us/rest/api/azure/devops/ims/identities/read-identities) to resolve and match the different identities used by each identity provider.