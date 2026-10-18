---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: onPremisesPublishing resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/onpremisespublishing?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: dhruvinrshah
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-applications
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an Application Proxy onPremisesPublishing object.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-12-19T00:00:00.0000000Z
locale: en-us
document_id: d764f180-bb30-40c3-dc92-b8420b48f208
document_version_independent_id: 2927773f-c1aa-2127-869b-b5fae2f86345
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/onpremisespublishing.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/onpremisespublishing
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/onpremisespublishing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/a21829dd-8109-415c-84d3-07c42e4d33fd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/70f417fa-3512-48b5-a80a-bb8985120ba9
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: a31f20c5-e2b6-8771-684d-52c7bcf50ee9
---

# onPremisesPublishing resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

An on-premises application published via [Microsoft Entra application proxy](/en-us/entra/identity/app-proxy/overview-what-is-app-proxy) is represented by an [application](application) object and its associated **onPremisesPublishing** property. Application Proxy provides secure remote access to on-premises applications.

An **onPremisesPublishing** object represents the set of properties for configuring Application Proxy for an on-premises [application](application).

After [instantiating a custom application](../applicationtemplate-instantiate) or [creating an application](../application-post-applications), the Application Proxy settings for the application can be configured by [updating the application's](../application-update) onPremisesPublishing properties.

For a tutorial about configuring Application Proxy, see [Automate the configuration of Application Proxy using the Microsoft Graph API](/en-us/graph/application-proxy-configure-api).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| alternateUrl | String | If you're configuring a traffic manager in front of multiple app proxy applications, this user-friendly URL points to the traffic manager. |
| applicationServerTimeout | String | The duration the connector waits for a response from the backend application before closing the connection. Possible values are `default`, `long`. When set to default, the backend application timeout has a length of 85 seconds. When set to long, the backend timeout is increased to 180 seconds. Use `long` if your server takes more than 85 seconds to respond to requests or if you are unable to access the application and the error status is "Backend Timeout". Default value is `default`. |
| applicationType | String | System-defined value that indicates whether this application is an application proxy configured application. The possible values are `quickaccessapp` and `nonwebapp`. Read-only. |
| externalAuthenticationType | externalAuthenticationType | Details the pre-authentication setting for the application. Pre-authentication enforces that users must authenticate before accessing the app. Pass through doesn't require authentication. The possible values are: `passthru`, `aadPreAuthentication`. |
| externalUrl | String | The published external URL for the application. For example, `https://intranet-contoso.msappproxy.net/`. |
| internalUrl | String | The internal url of the application. For example, `https://intranet/`. |
| isAccessibleViaZTNAClient | Boolean | Indicates whether the application is accessible via a [Global Secure Access client](/en-us/entra/global-secure-access/concept-clients) on a managed device. |
| isBackendCertificateValidationEnabled | Boolean | Indicates whether backend SSL certificate validation is enabled for the application. For all new Application Proxy apps, the property is set to `true` by default. For all existing apps, the property is set to `false`. |
| isContinuousAccessEvaluationEnabled | Boolean | Indicates whether [continuous access evaluation](/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) is enabled for Application Proxy application. For all Application Proxy apps, the property is set to `true` by default. |
| isDeviceAccessEnabled | Boolean | Indicates whether the Microsoft Entra Private Access application is accessible or available in device access mode. `false` by default. |
| isDnsResolutionEnabled | Boolean | Indicates Microsoft Entra Private Access should handle DNS resolution. `false` by default. |
| isHttpOnlyCookieEnabled | Boolean | Indicates if the HTTPOnly cookie flag should be set in the HTTP response headers. Set this value to `true` to have Application Proxy cookies include the HTTPOnly flag in the HTTP response headers. If using Remote Desktop Services, set this value to False. Default value is `false`. |
| isOnPremPublishingEnabled | Boolean | Indicates if the application is currently being published via Application Proxy or not. This is preset by the system. Read-only. |
| isPersistentCookieEnabled | Boolean | Indicates if the Persistent cookie flag should be set in the HTTP response headers. Keep this value set to `false`. Only use this setting for applications that can't share cookies between processes. For more information about cookie settings, see [Cookie settings for accessing on-premises applications in Microsoft Entra ID](/en-us/azure/active-directory/manage-apps/application-proxy-configure-cookie-settings). Default value is `false`. |
| isSecureCookieEnabled | Boolean | Indicates if the Secure cookie flag should be set in the HTTP response headers. Set this value to `true` to transmit cookies over a secure channel such as an encrypted HTTPS request. Default value is `true`. |
| isStateSessionEnabled | Boolean | Indicates whether validation of the state parameter when the client uses the OAuth 2.0 authorization code grant flow is enabled. This setting allows admins to specify whether they want to enable CSRF protection for their apps. |
| isTranslateHostHeaderEnabled | Boolean | Indicates if the application should translate urls in the response headers. Keep this value as `true` unless your application required the original host header in the authentication request. Default value is `true`. |
| isTranslateLinksInBodyEnabled | Boolean | Indicates if the application should translate urls in the application body. Keep this value as `false` unless you have hardcoded HTML links to other on-premises applications and don't use custom domains. For more information, see [Link translation with Application Proxy](/en-us/azure/active-directory/manage-apps/application-proxy-configure-hard-coded-link-translation). Default value is `false`. |
| onPremisesApplicationSegments (deprecated) | [onPremisesApplicationSegment](onpremisesapplicationsegment) collection | Represents the application segment collection for an on-premises wildcard application. This property is deprecated and will stop returning data on June 1, 2023. Use **segmentsConfiguration** instead. |
| segmentsConfiguration | [segmentConfiguration](segmentconfiguration) | Represents the collection of application segments for an on-premises wildcard application that's published through Microsoft Entra application proxy. |
| singleSignOnSettings | [onPremisesPublishingSingleSignOn](onpremisespublishingsinglesignon) | Represents the single sign-on configuration for the on-premises application. |
| trafficRoutingMethod | trafficRoutingMethod | Indicates how traffic is distributed across multiple connectors in a connector group. The possible values are: `none`, `random`, `sessionPersistence`, `performance` (Not implemented), `unknownFutureValue`. |
| useAlternateUrlForTranslationAndRedirect | Boolean | Indicates whether the application should use **alternateUrl** instead of **externalUrl**. |
| verifiedCustomDomainCertificatesMetadata | [verifiedCustomDomainCertificatesMetadata](verifiedcustomdomaincertificatesmetadata) | Details of the certificate associated with the application when a custom domain is in use. `null` when using the default domain. Read-only. |
| verifiedCustomDomainKeyCredential | [keyCredential](keycredential) | The associated key credential for the custom domain used. |
| verifiedCustomDomainPasswordCredential | [passwordCredential](passwordcredential) | The associated password credential for the custom domain used. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "alternateUrl": "String",
  "applicationServerTimeout": "String",
  "applicationType": "String",
  "externalAuthenticationType": "String",
  "externalUrl": "String",
  "internalUrl": "String",
  "isAccessibleViaZTNAClient": "Boolean",
  "isBackendCertificateValidationEnabled": true,
  "isContinuousAccessEvaluationEnabled": "Boolean",
  "isDeviceAccessEnabled": "Boolean",
  "isDnsResolutionEnabled": "Boolean",
  "isHttpOnlyCookieEnabled": true,
  "isOnPremPublishingEnabled": true,
  "isPersistentCookieEnabled": true,
  "isSecureCookieEnabled": true,
  "isStateSessionEnabled": true,
  "isTranslateHostHeaderEnabled": true,
  "isTranslateLinksInBodyEnabled": true,
  "onPremisesApplicationSegments":[{"@odata.type":"microsoft.graph.onPremisesApplicationSegment"}],
  "segmentsConfiguration":{"@odata.type":"microsoft.graph.segmentConfiguration"},
  "singleSignOnSettings": {"@odata.type": "microsoft.graph.onPremisesPublishingSingleSignOn"},
  "trafficRoutingMethod": "String",
  "useAlternateUrlForTranslationAndRedirect": "Boolean",
  "verifiedCustomDomainCertificatesMetadata": {"@odata.type": "microsoft.graph.verifiedCustomDomainCertificatesMetadata"},
  "verifiedCustomDomainKeyCredential": {"@odata.type": "microsoft.graph.keyCredential"},
  "verifiedCustomDomainPasswordCredential": {"@odata.type": "microsoft.graph.passwordCredential"}
}

```