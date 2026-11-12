---
layout: Conceptual
title: Authenticate the azcmagent CLI - Azure Connected Machine agent | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/azcmagent-authentication
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
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Choose an Azure sign-in method for azcmagent commands, including interactive login, service principals, access tokens, and Azure CLI credentials.
ms.topic: how-to
ms.date: 2026-11-10T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 5a17e71e-f42d-bd7e-f5e2-f897e62ce73f
document_version_independent_id: e8f8dc6a-1e63-f4bd-5e55-98bb8e5f11ec
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/azcmagent-authentication.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/azcmagent-authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/azcmagent-authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: be0b9b16-42b2-f37f-a8a8-40776bf74126
---

# Authenticate the azcmagent CLI - Azure Connected Machine agent | Microsoft Learn

This article describes the authentication methods and flags available for signing in to Azure with the `azcmagent` CLI. The following commands support these options:

- [`azcmagent connect`](azcmagent-connect#authentication-options).
- [`azcmagent reconnect`](azcmagent-reconnect#authentication-options).
- [`azcmagent disconnect`](azcmagent-disconnect#authentication-options).

Each command reference explains when authentication is required and which Azure permissions you need.

## Choose an authentication method

Choose any authentication method supported by your environment and use its flags in the `[authentication]` portion of the command's usage syntax. The following table suggests common uses for each method.

| Method | Suggested use |
| --- | --- |
| Interactive browser login | Sign in interactively on Windows with a desktop experience. |
| Device code authentication | Sign in by using a browser on another device, including for servers without a desktop. |
| Service principal with secret | Authenticate noninteractively for scripted operations by using a client secret. |
| Service principal with certificate | Authenticate noninteractively for scripted operations by using a certificate instead of a client secret. |
| Access token | Authenticate noninteractively by using a short-lived token obtained by another tool or automation process. |
| Azure CLI credentials | Reuse an existing Azure CLI session on the server. |

For any authentication method, provide the tenant information required by the command, as described in its command reference.

### Interactive browser login (Windows only)

Interactive browser authentication is the default on Windows with a desktop experience. You don't need to specify an authentication flag. The sign-in page opens in your default browser. Complete browser authentication within five minutes. If browser authentication fails or times out, the agent falls back to device code authentication.

### Device code authentication

Device code authentication is the default interactive sign-in method on Linux. On Windows, use `--use-device-code` to select this method. This option lets you sign in through a browser on another device. The agent displays a URL and code. Open the URL on an internet-connected device, enter the code, and complete sign-in within five minutes.

### Service principal with secret

Use `--service-principal-id <application-id>` with `--service-principal-secret <secret>`.

Microsoft recommends supplying secrets through a configuration file rather than command-line arguments.

### Service principal with certificate

Use `--service-principal-id <application-id>` with `--service-principal-cert <path>`.

The agent accepts PKCS #12 (.PFX) files and ASCII-encoded files, such as .PEM, containing both the certificate and its private key. Password-protected PFX files and encrypted PEM files aren't supported.

On Windows, you can instead use `--service-principal-cert-thumbprint <thumbprint>` to select a certificate from a Windows certificate store. The agent searches the following stores under Current User and Local Machine:

- Personal (`MY`).
- Intermediate Certification Authorities (`CA`).
- Trusted Publishers (`TrustedPublisher`).
- Third-Party Root Certification Authorities (`AuthRoot`).

Exportable and nonexportable certificates are supported.

For information about creating the service principal, see [Use an Azure service principal with certificate-based authentication](/en-us/cli/azure/azure-cli-sp-tutorial-3).

### Access token

Use `--access-token <token>` to authenticate with a Microsoft Entra ID access token issued for the Azure Resource Manager API. You must obtain a valid token before running the command. The agent doesn't renew a token supplied through this flag.

You can obtain an Azure Resource Manager access token with Azure CLI ([`az account get-access-token`](/en-us/cli/azure/account#az-account-get-access-token)) or Azure PowerShell ([`Get-AzAccessToken`](/en-us/powershell/module/az.accounts/get-azaccesstoken)).

### Azure CLI credentials

Use `--use-azcli` to authenticate with an existing Azure CLI session on the server. This method requires Azure Connected Machine agent version 1.59 or later and [Azure CLI installed on the server](/en-us/cli/azure/install-azure-cli).

If you aren't already signed in, run:

```azurecli
az login
```

Then run the required `azcmagent` command with `--use-azcli`.

## Authentication flags

These flags are shared by the commands listed in this article. Resource flags, including command-specific requirements for `--tenant-id`, remain documented in each command reference.

| Flag | Description |
| --- | --- |
| `--access-token` | Supplies a Microsoft Entra access token. See Access token. |
| `-i`, `--service-principal-id` | Specifies the service principal's application ID. Use with a secret, certificate file, or certificate thumbprint. Follow the command reference's tenant requirements. |
| `-p`, `--service-principal-secret` | Specifies the service principal secret. Requires `--service-principal-id`. See Service principal with secret. |
| `--service-principal-cert` | Specifies the path to a certificate file containing the private key. Requires `--service-principal-id`. See Service principal with certificate. |
| `--service-principal-cert-thumbprint` | Specifies a certificate thumbprint on Windows. Requires `--service-principal-id`. See Service principal with certificate. |
| `-c`, `--use-device-code` | Uses device code authentication. |
| `--use-azcli` | Uses credentials from an Azure CLI session on the server. Requires agent version 1.59 or later. |
| `--user-tenant-id` | Specifies the tenant used for authentication, which can differ from the resource tenant, such as for a guest account or [Azure Lighthouse](/en-us/azure/lighthouse). Must be a GUID. |

## Protect credentials

To follow the principle of least privilege, use a service principal dedicated to agent operations and grant it only the permissions needed for the command. Permission to connect a new server doesn't necessarily include permission to disconnect or reset an existing server's identity.

Don't include secrets, access tokens, or private certificate material in logs or source control. For service principal secrets, use a JSON or YAML configuration file instead of command-line arguments. For example:

```json
{
  "service-principal-id": "<application-id>",
  "service-principal-secret": "<secret>"
}
```

Pass the file to the command with `--config <path>`, along with any required resource and tenant flags. Restrict access to the file and remove it when it's no longer needed. For configuration file syntax and command-line precedence, see [Common flags](azcmagent#common-flags).