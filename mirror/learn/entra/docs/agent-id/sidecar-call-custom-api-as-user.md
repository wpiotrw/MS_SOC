---
layout: Conceptual
title: Call a custom API as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-custom-api-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the Auth SDK sidecar and On-Behalf-Of flow to call a custom API for the signed-in user.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: b95110b7-abe8-a415-5261-923c77be73fe
document_version_independent_id: b95110b7-abe8-a415-5261-923c77be73fe
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-custom-api-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-custom-api-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-custom-api-as-user.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 84468223-af60-f04d-fac4-ea9286821bbe
---

# Call a custom API as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use the OAuth On-Behalf-Of (OBO) flow when an upstream client calls an agent for a signed-in user and the agent calls a custom API for that user.

The agent first validates the inbound access token, then forwards the same authorization header to the sidecar. The sidecar uses its configured credential to get a downstream authorization header for that user.

## Prerequisites

- Completion of [Authenticate users with the Auth SDK sidecar](sidecar-authenticate-users), including consent for the upstream client to call the agent.
- A delegated scope exposed by the downstream API.
- Consent for the agent to call that API for the user.

## Configure access

1. Expose a delegated scope on the custom API.
2. Declare the scope in the blueprint's `requiredResourceAccess`.
3. [Obtain user or administrator consent](grant-agent-access-microsoft-365) for the agent identity to use that scope.
4. Configure the API and scope in the sidecar.

## Configure the sidecar

Add a delegated profile for the custom API:

```json
{
  "DownstreamApis": {
    "custom-api": {
      "BaseUrl": "https://api.contoso.com/",
      "Scopes": [
        "api://<custom-api-client-id>/<delegated-scope>"
      ]
    }
  }
}
```

Use the shared client ID and keep identity overrides disabled as described in [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Get a downstream token

Forward the token issued for the agent API:

```http
GET /AuthorizationHeader/custom-api
Authorization: ******
```

Send the returned `authorizationHeader` to the custom API. The custom API must validate the token and enforce the required scope and user authorization.

Don't send the inbound token directly to the custom API. It is intended for the agent, not the downstream resource. Don't return or log either authorization header.

## Call the sidecar and custom API

The following example forwards the inbound user authorization header to the sidecar, reads the downstream authorization header, and calls the custom API:

# [Python](#tab/python)
```python
import requests

SIDECAR_URL = "http://localhost:5000"

inbound_auth_header = "<authorization-header-from-agent-request>"

sidecar_response = requests.get(
    f"{SIDECAR_URL}/AuthorizationHeader/custom-api",
    headers={"Authorization": inbound_auth_header},
    timeout=5,
)

if sidecar_response.status_code in (401, 403):
    raise PermissionError("The sidecar rejected the user token or OBO request.")

sidecar_response.raise_for_status()
authorization_header = sidecar_response.json()["authorizationHeader"]

api_response = requests.get(
    "https://api.contoso.com/user-data",
    headers={"Authorization": authorization_header},
    timeout=10,
)
api_response.raise_for_status()
response_body = api_response.json()
```

# [JavaScript](#tab/javascript)
```javascript
const SIDECAR_URL = "http://localhost:5000";

const inboundAuthHeader = "<authorization-header-from-agent-request>";

const sidecarResponse = await fetch(
    `${SIDECAR_URL}/AuthorizationHeader/custom-api`,
    { headers: { Authorization: inboundAuthHeader } }
);

if (sidecarResponse.status === 401 || sidecarResponse.status === 403) {
    throw new Error("The sidecar rejected the user token or OBO request.");
}

if (!sidecarResponse.ok) {
    throw new Error(`Sidecar request failed with status ${sidecarResponse.status}.`);
}

const { authorizationHeader } = await sidecarResponse.json();

const apiResponse = await fetch("https://api.contoso.com/user-data", {
    headers: { Authorization: authorizationHeader },
});

if (!apiResponse.ok) {
    throw new Error(`API request failed with status ${apiResponse.status}.`);
}

const responseBody = await apiResponse.json();
```

---

Keep `SIDECAR_URL` on loopback in the shared network namespace. Replace the authorization-header placeholder with the complete `Authorization` header received by the agent. Process `responseBody` according to the custom API's response contract.

Treat the sidecar response as a credential. Don't log or return `authorizationHeader`.

Verify that the API enforces the delegated scope and the user's access. If OBO reports missing consent, check upstream access to the agent separately from downstream consent; the OBO exchange can't display a consent prompt.