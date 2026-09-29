---
layout: Conceptual
monikers:
- azure-devops
defaultMoniker: azure-devops
versioningType: Ranged
title: Issue Entra tokens with Azure CLI - Azure DevOps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/devops/cli/entra-tokens?view=azure-devops
config_moniker_range: azure-devops || >= azure-devops-2022 <= azure-devops-server
feedback_system: Standard
feedback_product_url: https://developercommunity.visualstudio.com/AzureDevOps
breadcrumb_path: /azure/devops/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-AzureDevOps
archive_url: https://docs.microsoft.com/en-us/previous-versions/azure/devops/all/
ms.topic: how-to
ms.manager: wiwagn
author: chcomley
ms.author: chcomley
ms.date: 2025-09-16T00:00:00.0000000Z
ms.service: azure-devops
ms.version: ALM
MSHAttr.msprod: ms.prod:ALM
ms.prodfamily: ALM
description: Use Microsoft Entra authentication on top of Azure CLI
ms.subservice: azure-devops-security
ms.custom: pat-reduction
locale: en-us
document_id: f540356a-8414-ebe4-2f8a-3c52a3e4cea2
document_version_independent_id: f540356a-8414-ebe4-2f8a-3c52a3e4cea2
original_content_git_url: https://github.com/MicrosoftDocs/azure-devops-docs-pr/blob/live/docs/cli/entra-tokens.md
default_moniker: azure-devops
site_name: Docs
depot_name: MSDN.azure-devops-docs
page_type: conceptual
interactive_type: azurepowershell
toc_rel: ../dev-resources/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.azure-devops-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: cli/entra-tokens
moniker_range_name: 348281b5e6207d94331bdbf3987314df
monikers:
- azure-devops
item_type: Content
source_path: docs/cli/entra-tokens.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
- https://authoring-docs-microsoft.poolparty.biz/devrel/5bd2b3fa-c186-4b92-a3c8-09f22a249d37
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
- https://authoring-docs-microsoft.poolparty.biz/devrel/7eba7926-b7b2-4a7a-bf89-e6ac53b3e7f6
platformId: 4f309b26-c0a2-d0ec-83fd-c5df8e97b418
---

# Issue Entra tokens with Azure CLI - Azure DevOps | Microsoft Learn

Use the [**Azure CLI**](/en-us/cli/azure/install-azure-cli) to issue a [Microsoft Entra token](../integrate/get-started/authentication/entra) and call [Azure DevOps REST APIs](/en-us/rest/api/azure/devops/). Since Entra access tokens only last for one hour, they're ideal for quick one-off operations. You can use Azure CLI to acquire a user token for yourself or on behalf of a [service principal](../integrate/get-started/authentication/service-principal-managed-identity).

## Prerequisites

| Category | Requirements |
| --- | --- |
| Entra tenant and subscription | Ensure the subscription is associated with the tenant connected to the Azure DevOps organization you're trying to access. If you don't know your tenant or subscription ID, you can find it in the [Azure portal](/en-us/azure/azure-portal/get-subscription-tenant-id). |
| Azure CLI | Download and install the [Azure CLI](/en-us/cli/azure/install-azure-cli). |
| Entra app | (If authenticating for a service principal) Create the Entra application and have the app client ID and client secret ready. |

## Get an Entra token for yourself

# [Azure CLI](#tab/azure-cli)
1. Sign in to the Azure CLI using the `az login` command and follow the on-screen instructions.
2. Set the correct subscription for the signed-in user with these bash commands. Ensure the Azure subscription ID is associated with the tenant connected to the Azure DevOps organization you're trying to access. If you don't know your subscription ID, you can find it in the [Azure portal](/en-us/azure/azure-portal/get-subscription-tenant-id).

    ```bash
    az account set -s <subscription-id>
    ```
3. Generate a Microsoft Entra ID access token with the `az account get-access-token` command using the Azure DevOps resource ID: `499b84ac-1321-427f-aa17-267ca6975798`.

    ```bash
    az account get-access-token \
    --resource 499b84ac-1321-427f-aa17-267ca6975798 \
    --query "accessToken" \
    -o tsv
    ```

# [Azure PowerShell](#tab/azure-powershell)
## Get a token for a user

1. Sign in to Azure PowerShell using the `Connect-AzAccount` command and follow the on-screen instructions.
2. Set the correct subscription for the signed-in user with these PowerShell commands. Ensure the Azure subscription ID is associated with the tenant connected to the Azure DevOps organization you're trying to access. If you don't know your subscription ID, you can find it in the [Azure portal](/en-us/azure/azure-portal/get-subscription-tenant-id).

    ```azurepowershell
    Set-AzContext -Subscription <subscriptionID>
    ```
3. Generate a Microsoft Entra ID access token with the `Get-AzAccessToken` command using the Azure DevOps resource ID: `499b84ac-1321-427f-aa17-267ca6975798`.

    ```azurepowershell
    Get-AzAccessToken -ResourceUrl '499b84ac-1321-427f-aa17-267ca6975798'
    ```

Note

[Get-AzAccessToken](/en-us/powershell/module/az.accounts/get-azaccesstoken) returns the token as a [SecureString](/en-us/dotnet/api/system.security.securestring). If you're unsure of how to use SecureString, refer to the documentation. To convert a SecureString to plain text to use in an Auth Header, leverage the .NET [\[System.Runtime.InteropServices.Marshal\]](/en-us/dotnet/api/system.runtime.interopservices.marshal) class to [convert](/en-us/dotnet/api/system.runtime.interopservices.marshal.securestringtobstr) the SecureString to a BSTR (binary string) pointer, then [read](/en-us/dotnet/api/system.runtime.interopservices.marshal.ptrtostringbstr) the pointer as a plain text string to a variable.

## Get a token for a service principal

1. Sign in to the Azure CLI as the service principal using the `az devops login` command.
2. Follow the on-screen instructions and finish signing in.

```powershell
# To authenticate a service principal with a password or cert:
az login --service-principal -u <app-id> -p <password-or-cert> --tenant <tenant>

# To authenticate a managed identity:
az login --identity
```

1. Set the right correct subscription for the signed-in service principal by entering the command:

```powershell
az account set -s <subscription-id>
```

1. Generate a Microsoft Entra ID access token with the `az account get-access-token` the Azure DevOps resource ID: `499b84ac-1321-427f-aa17-267ca6975798`.

```powershell
$accessToken = az account get-access-token --resource 499b84ac-1321-427f-aa17-267ca6975798 --query "accessToken" --output tsv
```

Note

Use the Azure DevOps application ID, not our resource URI, for generating tokens.

1. Now, you can use `az cli` commands per usual. Let's try to call an Azure DevOps API by passing it in the headers as a `Bearer` token:

```powershell
$apiVersion = "7.1-preview.1"
$uri = "https://dev.azure.com/${yourOrgname}/_apis/projects?api-version=${apiVersion}"
$headers = @{
    Accept = "application/json"
    Authorization = "Bearer $accessToken"
}
Invoke-RestMethod -Uri $uri -Headers $headers -Method Get | Select-Object -ExpandProperty value ` | Select-Object id, name
```

---