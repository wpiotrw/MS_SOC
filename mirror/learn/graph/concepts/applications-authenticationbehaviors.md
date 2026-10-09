---
layout: Conceptual
title: Manage application authenticationBehaviors - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/applications-authenticationbehaviors
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: FaithOmbongi
ms.author: ombongifaith
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: entra-applications
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Manage application authentication behaviors to adopt new breaking changes.
ms.reviewer: medbhargava
ms.localizationpriority: high
ms.custom: scenarios:getting-started
ms.date: 2025-08-29T00:00:00.0000000Z
locale: en-us
document_id: b022f494-e3a7-c99c-0c91-6de64870578d
document_version_independent_id: b022f494-e3a7-c99c-0c91-6de64870578d
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/applications-authenticationbehaviors.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: applications-authenticationbehaviors
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/applications-authenticationbehaviors.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: d9860451-4908-f3ae-ae02-dd0d08516846
---

# Manage application authenticationBehaviors - Microsoft Graph | Microsoft Learn

The [**authenticationBehaviors**](/en-us/graph/api/resources/authenticationbehaviors) property of the [application](/en-us/graph/api/resources/application) object lets you configure breaking change behaviors related to token issuance. Applications can adopt new breaking changes by enabling a behavior or continue using pre-existing behavior by disabling it.

You can configure the following behaviors:

- Control Cross-Origin-Opener-Policy (COOP) enforcement on browser-based authentication responses.
- Allow or prevent the issuance of email claims with unverified domain owners.
- Enable or disable extended Azure AD Graph access until August 31, 2025, when Azure AD Graph is fully retired.
- Require multitenant applications to have a service principal in the resource tenant as part of authorization checks before they're granted access tokens.

Note

The **authenticationBehaviors** property (including **coopEnforcement**) is available in Microsoft Graph v1.0 and beta for the global service. **coopEnforcement** isn't available in national cloud deployments.

## Read the authenticationBehaviors setting for an application

The **authenticationBehaviors** property is returned only on `$select` requests.

To read the property and other specified properties of all apps in the tenant, run the following sample request. The request returns a `200 OK` response code and a JSON representation of the application object that shows only the selected properties.

```msgraph
GET https://graph.microsoft.com/v1.0/applications?$select=id,displayName,appId,authenticationBehaviors
```

To read only the **authenticationBehaviors** property for a single app, run the following sample request.

```msgraph
GET https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
```

You can also use the **appId** property as follows:

```http
GET https://graph.microsoft.com/v1.0/applications(appId='37bf1fd4-78b0-4fea-ac2d-6c82829e9365')/authenticationBehaviors
```

## Control Cross-Origin-Opener-Policy enforcement

The **coopEnforcement** property controls whether Microsoft Entra authentication responses for an application include enforced Cross-Origin-Opener-Policy (COOP) headers. COOP isolates browser windows from cross-origin opener access and helps protect browser-based authentication flows. The service applies this per-app setting when per-app COOP override evaluation is available for the request.

Applications that use popup authentication should first adopt a COOP-compatible authentication flow. If your application uses MSAL.js, migrate to MSAL.js v5 or later and configure its supported redirect bridge. For more information, see [Migrate from MSAL Browser v4 to v5](/en-us/entra/msal/javascript/browser/v4-migration#cross-origin-opener-policy-coop-support) and [Set up the redirect bridge page in MSAL Browser](/en-us/entra/msal/javascript/browser/redirect-bridge). If an SDK or hosting platform owns the popup and callback, update to a compatible platform release or report the issue to that platform's owner.

The property supports the following values:

- `true`: Explicitly enforce COOP for the application.
- `false`: Explicitly suppress COOP enforcement as a temporary compatibility exception.
- `null`: Remove the explicit override and use the service default.

Note

**coopEnforcement** is available only in the global service and isn't available in national cloud deployments.

Important

Before setting **coopEnforcement** to `true`, test the application's complete authentication flow, including popup closure and delivery of the authentication result to the host application. Setting the property to `false` is a temporary compatibility exception while the application or owning platform is remediated; it isn't a security remediation. The exception doesn't expire automatically. Reset the property to `null` or set it to `true` after remediation.

### Explicitly enable COOP enforcement

The following examples explicitly enable COOP enforcement for an application.

#### Option 1

This pattern for specifying the property in the request URL allows you to update *only* the specified property in the request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "coopEnforcement": true
}
```

#### Option 2

This pattern for specifying the property in the request body lets you update other peer properties in the same request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e
Content-Type: application/json

{
    "authenticationBehaviors": {
        "coopEnforcement": true
    }
}
```

If successful, these requests return a `204 No Content` response.

### Temporarily suppress COOP enforcement

The following examples explicitly suppress COOP enforcement while the application owner remediates an incompatible authentication flow.

#### Option 1

This pattern for specifying the property in the request URL allows you to update *only* the specified property in the request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "coopEnforcement": false
}
```

#### Option 2

This pattern for specifying the property in the request body lets you update other peer properties in the same request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e
Content-Type: application/json

{
    "authenticationBehaviors": {
        "coopEnforcement": false
    }
}
```

If successful, these requests return a `204 No Content` response. A COOP Report-Only header might still be present. After the application or owning platform is remediated, set the property to `true` for controlled validation or reset it to `null` to use the service default.

### Restore the service default

The following examples remove the explicit override.

#### Option 1

This pattern for specifying the property in the request URL allows you to update *only* the specified property in the request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "coopEnforcement": null
}
```

#### Option 2

This pattern for specifying the property in the request body lets you update other peer properties in the same request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e
Content-Type: application/json

{
    "authenticationBehaviors": {
        "coopEnforcement": null
    }
}
```

If successful, these requests return a `204 No Content` response. To confirm the reset state, read the application with `$select=id,appId,authenticationBehaviors`. If the application has no other explicit authentication behavior, **authenticationBehaviors** is `null`. If another authentication behavior is configured, the complex object remains present and **coopEnforcement** is omitted.

Note

In the current beta, if **coopEnforcement** is already absent, another reset request might return `400 Request_BadRequest`. Read the application first and treat an omitted property as already reset.

## Prevent the issuance of email claims with unverified domain owners

As described in the Microsoft security advisory [Potential Risk of Privilege Escalation in Microsoft Entra Applications](https://msrc.microsoft.com/blog/2023/06/potential-risk-of-privilege-escalation-in-azure-ad-applications/), **apps should never use the email claim for authorization purposes**. If your application uses the email claim for authorization or primary user identification purposes, it's subject to account and privilege escalation attacks. This risk of unauthorized access is especially identified in the following scenarios:

- When the **mail** attribute of the [user](/en-us/graph/api/resources/user) object contains an email address with an unverified domain owner
- For multitenant apps where a user from one tenant could escalate their privileges to access resources from another tenant through modification of their **mail** attribute

Today, the default behavior is to remove email addresses with unverified domain owners in claims, except for single-tenant apps and for multitenant apps with previous sign-in activity with unverified emails. If your app falls into either of these exceptions and you want to remove unverified email addresses, set the **removeUnverifiedEmailClaim** property of [authenticationBehaviors](/en-us/graph/api/resources/authenticationbehaviors) to `true` as shown in the following examples. The request returns a `204 No Content` response code.

### Remove email addresses with unverified domain owners from claims

#### Option 1

This pattern for specifying the property in the request URL allows you to update *only* the specified property in the request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "removeUnverifiedEmailClaim": true
}
```

#### Option 2

This pattern for specifying the property in the request body lets you update other peer properties in the same request.

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e
Content-Type: application/json

{
    "authenticationBehaviors": {
        "removeUnverifiedEmailClaim": true
    }
}
```

### Accept email addresses with unverified domain owners in claims

#### Option 1

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "removeUnverifiedEmailClaim": false
}
```

#### Option 2

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e
Content-Type: application/json

{
    "authenticationBehaviors": {
        "removeUnverifiedEmailClaim": false
    }
}
```

### Restore the default behavior

#### Option 1

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/authenticationBehaviors
Content-Type: application/json

{
    "removeUnverifiedEmailClaim": null
}
```

#### Option 2

```http
PATCH https://graph.microsoft.com/v1.0/applications/03ef14b0-ca33-4840-8f4f-d6e91916010e/
Content-Type: application/json

{
    "authenticationBehaviors": {
        "removeUnverifiedEmailClaim": null
    }
}
```

## Allow extended Azure AD Graph access until August 31, 2025

By default, applications created after August 31, 2024 receive a `403 Unauthorized` error when making requests to Azure AD Graph APIs, unless you configure them to allow extended Azure AD Graph access. Additionally, you must configure existing apps created before August 31, 2024 and making requests to Azure AD Graph APIs to allow extended Azure AD Graph access by February 1, 2025. This extended access is available only until June 30, 2025, when Azure AD Graph is fully retired. After this date, all apps receive a `403 Unauthorized` error when making requests to Azure AD Graph APIs, regardless of their extended access configuration. For more information, see [June 2024 update on Azure AD Graph API retirement](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/june-2024-update-on-azure-ad-graph-api-retirement/ba-p/4094534).

The following request shows how to update an app to enable extended Azure AD Graph access. The ID used in this example is the object ID of the application, not the application ID. The request returns a `204 No Content` response code.

#### Option 1

```http
PATCH https://graph.microsoft.com/v1.0/applications/5c142e6f-0bd3-4e58-b510-8a106704f44f/authenticationBehaviors
Content-Type: application/json

{
    "blockAzureADGraphAccess": false
}
```

#### Option 2

```http
PATCH https://graph.microsoft.com/v1.0/applications/5c142e6f-0bd3-4e58-b510-8a106704f44f
Content-Type: application/json

{
    "authenticationBehaviors": {
        "blockAzureADGraphAccess": false
    }
}
```