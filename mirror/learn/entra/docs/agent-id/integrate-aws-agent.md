---
layout: Conceptual
title: Use an AWS workload identity with Microsoft Entra Agent ID - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/integrate-aws-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use an AWS token to get an Agent ID token and call a protected API.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 35d16ffb-6b42-53b6-6af5-caf87d807956
document_version_independent_id: 35d16ffb-6b42-53b6-6af5-caf87d807956
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/integrate-aws-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/integrate-aws-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/integrate-aws-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 4c49af80-8ab9-28f8-6615-41840cf9c387
---

# Use an AWS workload identity with Microsoft Entra Agent ID - Microsoft Entra Agent ID | Microsoft Learn

Use workload identity federation when an agent hosted on Amazon Web Services (AWS) calls a Microsoft Entra-protected resource as itself. AWS Security Token Service (STS) issues a short-lived JSON Web Token (JWT). Microsoft Entra ID trusts that token as a federated credential for the agent identity blueprint.

This path supports app-only access. It doesn't authenticate users or perform an On-Behalf-Of flow.

## Prerequisites

- An [agent identity blueprint](create-blueprint) and [Agent ID](create-delete-agent-identities).
- An AWS IAM role for the hosted workload.
- Permission to enable AWS IAM Outbound Identity Federation and update the IAM role.
- An application permission, app role, or resource role assigned to the Agent ID.
- Python 3 with current `boto3` and `requests` packages for the example.
- An execution environment authenticated as the AWS workload role. Run the example there so `boto3` uses that role, not an unrelated developer identity.

## Enable AWS outbound identity federation

Enable the feature for the AWS account:

```azurecli
aws iam enable-outbound-web-identity-federation
```

Record the account-specific issuer URL returned by AWS. The `GetWebIdentityToken` API requires a regional STS endpoint and isn't available through the global endpoint.

Grant the workload role permission to request only tokens intended for Microsoft Entra ID:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:GetWebIdentityToken",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "sts:IdentityTokenAudience": "api://AzureADTokenExchange"
        },
        "NumericLessThanEquals": {
          "sts:DurationSeconds": 300
        }
      }
    }
  ]
}
```

For the complete AWS procedure, see [Getting started with outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html).

## Add the AWS identity to the blueprint

Add a federated credential to the agent identity blueprint:

1. Open the blueprint in the Microsoft Entra admin center.
2. Select **Credentials** &gt; **Federated credentials** &gt; **Add credential**.
3. Select **Other issuer**.
4. Enter the AWS account-specific issuer URL.
5. Enter the IAM role ARN as the subject, such as `arn:aws:iam::<account-id>:role/<role-name>`.
6. Enter `api://AzureADTokenExchange` as the audience.
7. Add the credential.

The issuer, subject, and audience must exactly match the `iss`, `sub`, and `aud` claims in the AWS token. Wildcards aren't supported. For more information, see [Add a federated credential to an agent identity blueprint](manage-agent-blueprint#add-a-federated-credential) and [AWS outbound token claims](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_token_claims.html).

## Grant access to the Agent ID

Grant the Agent ID the application permission or resource role required by the target API. The federated credential only authenticates the blueprint; it doesn't authorize access to a downstream resource.

For a custom API, expose and assign an application role. For an Azure resource, assign the Agent ID the required Azure role.

## Exchange the AWS token

Install the example dependencies:

```bash
pip install --upgrade boto3 requests
```

The following example gets an AWS token, exchanges it for an Agent ID resource token, and calls the protected API:

```python
import boto3
import requests

TENANT_ID = "<tenant-id>"
BLUEPRINT_CLIENT_ID = "<agent-identity-blueprint-client-id>"
AGENT_ID_CLIENT_ID = "<agent-identity-client-id>"
RESOURCE_SCOPE = "api://<resource-client-id>/.default"
RESOURCE_URL = "https://api.contoso.com/data"

token_endpoint = (
    f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
)

def exchange_token(client_id, scope, assertion, fmi_path=None):
    data = {
        "client_id": client_id,
        "scope": scope,
        "grant_type": "client_credentials",
        "client_assertion_type":
            "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": assertion,
    }
    if fmi_path:
        data["fmi_path"] = fmi_path

    response = requests.post(token_endpoint, data=data, timeout=30)
    response.raise_for_status()
    return response.json()["access_token"]

sts = boto3.client("sts", region_name="<aws-region>")
aws_token = sts.get_web_identity_token(
    Audience=["api://AzureADTokenExchange"],
    SigningAlgorithm="RS256",
    DurationSeconds=300,
)["WebIdentityToken"]

blueprint_token = exchange_token(
    BLUEPRINT_CLIENT_ID,
    "api://AzureADTokenExchange/.default",
    aws_token,
    AGENT_ID_CLIENT_ID,
)

resource_token = exchange_token(
    AGENT_ID_CLIENT_ID,
    RESOURCE_SCOPE,
    blueprint_token,
)

resource_response = requests.get(
    RESOURCE_URL,
    headers={"Authorization": f"Bearer {resource_token}"},
    timeout=30,
)
resource_response.raise_for_status()
```

Don't log the AWS assertion, blueprint token, or resource token. Request a new AWS token for each exchange rather than storing it.

Verify that the resource call returns the API's expected successful response. If the AWS token request fails, check the workload role, regional STS endpoint, and outbound federation permission. If the Microsoft Entra exchange fails, check the blueprint's federated credential and the selected agent ID. If only the resource call fails, check the resource scope and the permissions assigned to the Agent ID; successful federation doesn't grant API access.

For the Agent ID exchanges, see [Agent autonomous app OAuth flow](agent-autonomous-app-oauth-flow). For the AWS token API, see [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html).

## Clean up test access

Remove test-only resource permissions and the federated credential when you no longer need this integration. Coordinate with the AWS account owner before removing role permissions or disabling account-wide outbound federation; other workloads might depend on them. Delete the Agent ID or blueprint only if no remaining agent uses those resources.