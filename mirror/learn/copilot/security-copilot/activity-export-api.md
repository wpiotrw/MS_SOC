---
layout: Conceptual
title: Export Activity in Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/activity-export-api
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how Security Copilot Admin Export APIs let workspace administrators export prompts and prompt responses in a paginated format, including API contract and schema details.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
search.audiencetype: Admin
search.appverid: MET150
f1.keywords: NOCSH
audience: ITPro
locale: en-us
document_id: 029b9ccb-2221-e4ec-9ebc-e034106b12e8
document_version_independent_id: 029b9ccb-2221-e4ec-9ebc-e034106b12e8
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/activity-export-api.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: activity-export-api
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/activity-export-api.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 8016bc0a-9d19-297d-6f9a-8090a5160231
---

# Export Activity in Security Copilot | Microsoft Learn

This document describes the API contracts and expected output data schemas for the Security Copilot Admin Export APIs.

Export APIs provide workspace administrators with the ability to export prompts and prompt responses in a paginated format.

## Authenticate and authorize Export Activity API requests

- Authorization: Bearer token authentication
- Required Permissions: Workspace Owner / Administrator

### Authenticate with a Service Principal

1. **Create an app registration** (for example, use a name like `mysecuritycopilotexportapp`).

    - Use the Microsoft Entra ID quickstart: [Register an app (portal)](/en-us/entra/identity-platform/quickstart-register-app).
    - If you prefer CLI, create the identity via the tutorial: [Create a service principal (Azure CLI)](/en-us/cli/azure/azure-cli-sp-tutorial-1).
    - Add credentials to the app registration as needed: [Add credentials (client secret/cert)](/en-us/entra/identity-platform/how-to-add-credentials). For a step‑by‑step client‑secret creation, see [Create client secret (explicit steps)](/en-us/graph/auth-register-app-v2#option-2-add-a-client-secret) or the portal guide, [Register an app and create a Service Principal (portal)](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret).

    Note

    Only existing Owners can do the specific action.
2. **Add the new Service Principal as an Owner in Security Copilot role assignments**

    See, [Security Copilot roles and assignments](/en-us/copilot/security/authentication). Security Copilot **supports assigning permissions to role‑assignable groups (RAGs)**, so create a RAG and then add your Service Principal (SP) to it as follows:

    - [Create a role‑assignable group](/en-us/entra/identity/role-based-access-control/groups-create-eligible)
    - Add the SP to the group (pick either): [Portal—Manage groups (add members)](/en-us/entra/fundamentals/how-to-manage-groups#add-members-or-owners-of-a-group) or [API—Microsoft Graph: Add group member](/en-us/graph/api/group-post-members)
3. **Retrieve a bearer token for your service principal.**

    Example using Azure CLI and a client secret:

    ```
    # Login as service principal (supports no-subscription tenants)
    az login --service-principal -u 94e67e0c-7c41-4f5b-b5ae-f5b5918e2382 -p <client-secret> --tenant 536279f6-15cc-45f2-be2d-61e352b51eef --allow-no-subscriptions
    
    # Retrieve access token for Security Copilot (v1 resource pattern)
    az account get-access-token --resource https://api.securitycopilot.microsoft.com
    ```

### Authenticate as a User

Ensure your user account has the Security Copilot Owner role before retrieving a bearer token.

- Example using Azure CLI (v2 pattern with `/.default`):

```azurecli
az account get-access-token --scope https://api.securitycopilot.microsoft.com/.default
```

### Related content

- [Sign in as SP (CLI)](/en-us/cli/azure/authenticate-azure-cli-service-principal)
- [Get access token (CLI)](/en-us/cli/azure/account)
- [`.default` scope explained](/en-us/entra/identity-platform/scopes-oidc)
- [Get access token (CLI)](/en-us/cli/azure/account) and [`.default` scope](/en-us/entra/identity-platform/scopes-oidc).

### Response behavior for non-Owners

For non-owners, the following response is returned for API calls:

```json
{
  "message": "Your role doesn\u0027t have access to the info requested. Contact a Security Administrator to change your role or try again with a different account. Learn more about copilot",
  "code": "403",
  "traceId": "0HNF1M54NKVJ3:00000041",
  "error": {
    "message": "Your role doesn\u0027t have access to the info requested. Contact a Security Administrator to change your role or try again with a different account. Learn more about copilot",
    "copilotErrorId": "doesNotHaveAccessToSecurityCopilot",
    "code": "403",
    "innerError": {
      "message": null,
      "date": "2025-08-22T19:32:04.4726177Z",
      "correlationId": "aaaa0000-bb11-2222-33cc-444444dddddd"
    },
    "traceId": "0HNF1M54NKVJ3:00000041"
  }
}
```

## API endpoints

### Prompts Export API

```http
https://api.securitycopilot.microsoft.com/exports/prompts

```

`GET /exports/prompts`

#### Query parameters

*N/A*

#### Request example

```http
GET /exports/prompts?sessionCount=500&startDate=2024-01-01T00:00:00Z&endDate=2024-12-31T23:59:59Z
Authorization: Bearer <token>
```

#### Response schema

**Success response** - `(200 OK)`

```json
{
  "workspaceId": "string",
  "workspaceName": "string",
  "tenantId": "string",
  "prompts": [
    {
      // Prompt object schema (see Framework.Models.Prompt)
    }
  ],
  "sessionsContinuationToken": "string?",
  "totalCount": "integer?",
  "sessionCount": "integer"
}
```

**Error codes and messages**

| Status Code | Error Code | Error Message |
| --- | --- | --- |
| 400 | Bad Request | Invalid parameters or missing workspace/tenant information |
| 404 | Not Found | Admin export APIs not enabled |
| 500 | Internal Server Error | Server error during export |

### Evaluations Export API

```http
https://api.securitycopilot.microsoft.com/exports/evaluations
```

`GET /exports/evaluations`

#### Query parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sessionCount` | `integer` | No | `100` | Number of sessions to fetch (range: 1–1000). |
| `continuationToken` | `string` | No | `null` | Token for pagination. |
| `startDate` | `DateTimeOffset` | No | `null` | Start date filter (inclusive, ISO format). |
| `endDate` | `DateTimeOffset` | No | `null` | End date filter (inclusive, ISO format). |
| `orderByDescending` | `boolean` | No | `false` | Order results by descending. |

#### Request example

```http
GET /exports/evaluations?sessionCount=200&continuationToken=abc123
Authorization: Bearer <token>
```

#### Response schema

**Success response** - `(200 OK)`

```json
{
  "workspaceId": "string",
  "workspaceName": "string",
  "tenantId": "string",
  "evaluations": [
    {
      // Evaluation object schema
    }
  ],
  "sessionsContinuationToken": "string?",
  "totalCount": "integer?",
  "sessionCount": "integer"
}
```

**Error codes and messages**

| Status Code | Error Code | Error Message |
| --- | --- | --- |
| 400 | Bad Request | Invalid parameters or missing workspace/tenant information |
| 404 | Not Found | Admin export APIs not enabled |
| 500 | Internal Server Error | Server error during export |

## Data models

### Base response properties

Both export APIs return responses with these common properties:

| Property | Type | Description |
| --- | --- | --- |
| `workspaceId` | `string` | The workspace ID that is exported |
| `workspaceName` | `string` | The workspace name that is exported |
| `tenantId` | `string` | The tenant ID that is exported |
| `sessionsContinuationToken` | `string?` | Token for next page (null if no more data) |
| `totalCount` | `integer?` | Total count of items in current page |
| `sessionCount` | `integer` | Session count used for this request |

## Pagination

Both APIs support cursor-based pagination:

1. **Initial Request:** Make request without `continuationToken`.
2. **Subsequent Requests:** Use `sessionsContinuationToken` from the previous response.
3. **End of Data:** When `sessionsContinuationToken` is null, no more data is available.

### Pagination example

**First request**

```http
GET /exports/prompts?sessionCount=100
```

**Response includes continuationToken**

```json
{
  "sessionsContinuationToken": "[{\"compositeToken\":{\"token\":null,\"range\":{\"min\":\"05C1D1D5378D58\",\"max\":\"05C1D3CFCBB964\"}},\"resumeValues\":[\"2025-08-01T23:49:27.8981554+00:00\"],\"rid\":\"xQAMAIZUJBs7BEAAAADABQ==\",\"skipCount\":1}]",
  "prompts": [...],
  // ... other properties
}
```

**Next request using token (URL encoded)**

```http
GET /exports/prompts?sessionCount=100&continuationToken=%5B%7B%22compositeToken%22%3A%7B%22token%22%3Anull%2C%22range%22%3A%7B%22min%22%3A%2205C1D1D5378D58%22%2C%22max%22%3A%2205C1D3CFCBB964%22%7D%7D%2C%22resumeValues%22%3A%5B%222025-08-01T23%3A49%3A27.8981554%2B00%3A00%22%5D%2C%22rid%22%3A%22xQAMAIZUJBs7BEAAAADABQ%3D%3D%22%2C%22skipCount%22%3A1%7D%5D
```

Note

- If your service principal has no subscriptions, `az login` might report that none were found; in this case, include `--allow-no-subscriptions`.
- For tokens, you can use either `--resource https://api.securitycopilot.microsoft.com` (v1) or `--scope https://api.securitycopilot.microsoft.com/.default` (v2), depending on your auth flow. See, [Get access token (CLI)](/en-us/cli/azure/account) and [`.default` scope](/en-us/entra/identity-platform/scopes-oidc).

## Related content

Use the following articles for guidance:

- [**Register an app (portal)**](/en-us/entra/identity-platform/quickstart-register-app)
- [**Create SP (CLI tutorial)**](/en-us/cli/azure/azure-cli-sp-tutorial-1)
- [**Add credentials (client secret/cert)**](/en-us/entra/identity-platform/how-to-add-credentials)
- [**Create client secret (explicit steps)**](/en-us/graph/auth-register-app-v2#option-2-add-a-client-secret)
- [**(Alt) Create client secret in portal**](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret)
- [**Security Copilot roles & assignments)**](/en-us/copilot/security/authentication)
- [**Add Service Principal to a group (portal)**](/en-us/entra/fundamentals/how-to-manage-groups#add-members-or-owners-of-a-group)
- [**Add Service Principal to a group (API)**](/en-us/graph/api/group-post-members)
- [**Sign in as SP (CLI)**](/en-us/cli/azure/authenticate-azure-cli-service-principal)
- [**Get access token (CLI)**](/en-us/cli/azure/account)