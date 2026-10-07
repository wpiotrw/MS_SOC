---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: x509CertificateAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/x509certificateauthenticationmethodconfiguration?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vimrang
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the details of the Microsoft Entra native Certificate-Based Authentication (CBA) in the tenant, including whether the authentication method is enabled or disabled and the users and groups who can register and use it.
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: X509 certificate
toc.keywords:
- certificate-based authentication
- CBA
ms.date: 2025-03-10T00:00:00.0000000Z
locale: en-us
document_id: 7850c55f-c20e-1956-2267-5bf715edf86d
document_version_independent_id: f3c2a8ce-6f25-f313-66a1-321db1cffe6d
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/x509certificateauthenticationmethodconfiguration.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/x509certificateauthenticationmethodconfiguration
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/x509certificateauthenticationmethodconfiguration.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 156b1c83-0986-e32f-9f25-ae3ad880db5f
---

# x509CertificateAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents the details of the Microsoft Entra native Certificate-Based Authentication (CBA) in the tenant, including whether the authentication method is enabled or disabled and the users and groups who can register and use it.

Inherits from [authenticationMethodConfiguration](authenticationmethodconfiguration).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../x509certificateauthenticationmethodconfiguration-get) | [x509CertificateAuthenticationMethodConfiguration](x509certificateauthenticationmethodconfiguration) | Read the properties and relationships of a x509CertificateAuthenticationMethodConfiguration object. |
| [Update](../x509certificateauthenticationmethodconfiguration-update) | [x509CertificateAuthenticationMethodConfiguration](x509certificateauthenticationmethodconfiguration) | Update the properties of a x509CertificateAuthenticationMethodConfiguration object. |
| [Delete](../x509certificateauthenticationmethodconfiguration-delete) | None | Delete the tenant-customized x509CertificateAuthenticationMethodConfiguration object and restore the default configuration. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| authenticationModeConfiguration | [x509CertificateAuthenticationModeConfiguration](x509certificateauthenticationmodeconfiguration) | Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings. |
| certificateAuthorityScopes | [x509CertificateAuthorityScope](x509certificateauthorityscope) collection | Defines configuration to allow a group of users to use certificates from specific issuing certificate authorities to successfully authenticate. |
| certificateUserBindings | [x509CertificateUserBinding](x509certificateuserbinding) collection | Defines fields in the X.509 certificate that map to attributes of the Microsoft Entra user object in order to bind the certificate to the user. The **priority** of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored. |
| crlValidationConfiguration | [x509CertificateCRLValidationConfiguration](x509certificatecrlvalidationconfiguration) | Determines whether certificate based authentication should fail if the issuing CA doesn't have a valid certificate revocation list configured. |
| excludeTargets | [excludeTarget](excludetarget) collection | Groups of users that are excluded from the policy. |
| id | String | The identifier for the authentication method policy. The value is always `X509Certificate`. Inherited from [authenticationMethodConfiguration](authenticationmethodconfiguration). |
| issuerHintsConfiguration | [x509CertificateIssuerHintsConfiguration](x509certificateissuerhintsconfiguration) | Determines whether issuer(CA) hints are sent back to the client side to filter the certificates shown in certificate picker. |
| state | authenticationMethodState | The possible values are: `enabled`, `disabled`. Inherited from [authenticationMethodConfiguration](authenticationmethodconfiguration). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| includeTargets | [authenticationMethodTarget](authenticationmethodtarget) collection | A collection of groups that are enabled to use the authentication method. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration",
  "id": "String (identifier)",
  "state": "String",
  "excludeTargets": [
    {
      "@odata.type": "microsoft.graph.excludeTarget"
    }
  ],
  "certificateUserBindings": [
    {
      "@odata.type": "microsoft.graph.x509CertificateUserBinding"
    }
  ],
  "authenticationModeConfiguration": {
    "@odata.type": "microsoft.graph.x509CertificateAuthenticationModeConfiguration"
  },
  "issuerHintsConfiguration": {
    "@odata.type": "microsoft.graph.x509CertificateIssuerHintsConfiguration"
  },
  "certificateAuthorityScopes": [
    {
      "@odata.type": "microsoft.graph.x509CertificateAuthorityScope"
    }
  ],
  "crlValidationConfiguration": {
    "@odata.type": "microsoft.graph.x509CertificateCRLValidationConfiguration"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/x509certificateauthenticationmethodconfiguration?view=graph-rest-beta&accept=text/markdown)
