---
layout: Conceptual
title: Access Azure resources with managed identity on Azure Arc-enabled servers - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/managed-identity-authentication
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: schaffererin
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: schaffererin
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: This article describes Azure Instance Metadata Service support for Azure Arc-enabled servers and how you can authenticate against Azure resources by using a managed identity.
ms.topic: concept-article
ms.date: 2026-02-05T00:00:00.0000000Z
locale: en-us
document_id: 8ec54523-244d-f725-325d-43c7a8b2c002
document_version_independent_id: 8aa03d64-59f8-98b2-6981-7613a529d769
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/managed-identity-authentication.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/managed-identity-authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/managed-identity-authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: b7947876-c270-cc27-6cf6-7df1190a46a4
---

# Access Azure resources with managed identity on Azure Arc-enabled servers - Azure Arc | Microsoft Learn

Applications or processes running directly on an Azure Arc-enabled server can use managed identities to access other Azure resources that support Microsoft Entra ID-based authentication. An application can obtain an [access token](/en-us/azure/active-directory/develop/developer-glossary#access-token) representing its managed identity and use it as a bearer token to authenticate itself to another service.

Azure Arc-enabled servers use a system-assigned managed identity by default. To connect a supported server with user-assigned managed identities during the preview, see [Connect an Azure Arc-enabled server with a user-assigned managed identity (preview)](connect-user-assigned-managed-identity-preview).

For a detailed description of managed identities and the distinction between system-assigned and user-assigned identities, see the [managed identity overview](/en-us/azure/active-directory/managed-identities-azure-resources/overview).

In this article, you learn how a server can use a system-assigned managed identity to access [Azure Key Vault](/en-us/azure/key-vault/general/overview). Azure Key Vault allows your client application to use a secret to access resources that aren't secured by Microsoft Entra ID. For example, Azure Key Vault can store TLS/SSL certificates used by your IIS web servers and securely deploy the certificates to Windows or Linux servers outside of Azure.

## Security overview

When you onboard your server to Azure Arc-enabled servers and configure it to use a managed identity, several actions occur (similar to what happens for an Azure VM):

- Azure Resource Manager receives a request to enable the system-assigned managed identity on the Azure Arc-enabled server.
- Azure Resource Manager creates a service principal in Microsoft Entra ID for the identity of the server. The service principal is created in the Microsoft Entra tenant that's trusted by the subscription.
- Azure Resource Manager configures the identity on the server by updating the [Azure Instance Metadata Service (IMDS)](/en-us/azure/virtual-machines/instance-metadata-service) identity endpoint for Windows or Linux with the service principal client ID and certificate. The endpoint is a REST endpoint accessible only from within the server by using a well-known, non-routable IP address. This service provides a subset of metadata information about the Azure Arc-enabled server to help manage and configure it.

The environment of a managed-identity-enabled server is configured with the following variables on an Azure Arc-enabled server:

- **IMDS\_ENDPOINT**: The IMDS endpoint IP address `http://localhost:40342` for Azure Arc-enabled servers.
- **IDENTITY\_ENDPOINT**: The localhost endpoint `http://localhost:40342/metadata/identity/oauth2/token` corresponding to the service's managed identity.

Your code that's running on the server can request a token from the Azure Instance Metadata service endpoint, accessible only from within the server.

Applications can retrieve the system environment variables **IDENTITY\_ENDPOINT** and **IMDS\_ENDPOINT** values and use them to discover these endpoints. Applications with any access level can make requests to the endpoints. Metadata responses are handled as normal and given to any process on the machine. However, when a request is made that would expose a token, the client must provide a secret to attest that they're able to access data that's only available to higher-privileged users.

## Prerequisites

Before you begin, ensure that you have the following prerequisites in place:

- An understanding of [managed identities](/en-us/azure/active-directory/managed-identities-azure-resources/overview).
- A server connected to Azure Arc-enabled servers.
- On Windows, you must be a member of the local `Administrators` group or the `Hybrid Agent Extension Applications` group. On Linux, you must be a member of the `himds` group.
- You must have the [Owner role](/en-us/azure/role-based-access-control/built-in-roles#owner) in the Azure subscription or resource group that contains the Arc-enabled servers in order to perform the required resource creation and role management steps.
- An Azure Key Vault to store and retrieve your credentials, and assign the Azure Arc identity access to the KeyVault.

    - To configure access by the managed identity used by the server, see [Grant access for Linux](/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-nonaad#grant-access) or [Grant access for Windows](/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-windows-vm-access-nonaad#grant-access). When you enter the name of your VM, use the name of the Azure Arc-enabled server.

## Acquire an access token using REST API

The method to obtain and use a system-assigned managed identity to authenticate with Azure resources is similar to the method used with an Azure VM.

For an Azure Arc-enabled Windows server, use PowerShell to invoke the web request that gets the token from the local host on the specific port. Specify the request by using the IP address or the environmental variable **IDENTITY\_ENDPOINT**.

```powershell
$apiVersion = "2020-06-01"
$resource = "https://management.azure.com/"
$endpoint = "{0}?resource={1}&api-version={2}" -f $env:IDENTITY_ENDPOINT,$resource,$apiVersion
$secretFile = ""
try
{
    Invoke-WebRequest -Method GET -Uri $endpoint -Headers @{Metadata='True'} -UseBasicParsing
}
catch
{
    $wwwAuthHeader = $_.Exception.Response.Headers["WWW-Authenticate"]
    if ($wwwAuthHeader -match "Basic realm=.+")
    {
        $secretFile = ($wwwAuthHeader -split "Basic realm=")[1]
    }
}
Write-Host "Secret file path: " $secretFile`n
$secret = cat -Raw $secretFile
$response = Invoke-WebRequest -Method GET -Uri $endpoint -Headers @{Metadata='True'; Authorization="Basic $secret"} -UseBasicParsing
if ($response)
{
    $token = (ConvertFrom-Json -InputObject $response.Content).access_token
    Write-Host "Access token: " $token
}
```

The response is similar to the following example:

![A successful retrieval of the access token using PowerShell.](media/managed-identity-authentication/powershell-token-output-example.png)

For an Azure Arc-enabled Linux server, use Bash to invoke the web request that gets the token from the local host on the specific port. Specify the following request by using the IP address or the environmental variable **IDENTITY\_ENDPOINT**. To complete this step, you need an SSH client.

```bash
CHALLENGE_TOKEN_PATH=$(curl -s -D - -H Metadata:true "http://127.0.0.1:40342/metadata/identity/oauth2/token?api-version=2019-11-01&resource=https%3A%2F%2Fmanagement.azure.com" | grep Www-Authenticate | cut -d "=" -f 2 | tr -d "[:cntrl:]")
CHALLENGE_TOKEN=$(cat $CHALLENGE_TOKEN_PATH)
if [ $? -ne 0 ]; then
    echo "Could not retrieve challenge token, double check that this command is run with root privileges."
else
    curl -s -H Metadata:true -H "Authorization: Basic $CHALLENGE_TOKEN" "http://127.0.0.1:40342/metadata/identity/oauth2/token?api-version=2019-11-01&resource=https%3A%2F%2Fmanagement.azure.com"
fi
```

The response is similar to the following example:

![A successful retrieval of the access token using Bash.](media/managed-identity-authentication/bash-token-output-example.png)

Note

The preceding example requests an access token for use with ARM REST APIs when the resource variable is set to `https://management.azure.com`. If you need an access token for a different Azure service, replace the resource variable in the script with the correct resource value. To authenticate with Azure Storage, see [Microsoft Authentication Library (MSAL)](/en-us/azure/storage/blobs/authorize-access-azure-active-directory#microsoft-authentication-library-msal). To complete the configuration to authenticate to Azure Key Vault, see [Access Key Vault with Windows](/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-windows-vm-access-nonaad#access-data) or [Access Key Vault with Linux](/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-nonaad#access-data).