---
layout: Conceptual
title: CLI reference for azcmagent reconnect (preview) - Azure Connected Machine agent | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/azcmagent-reconnect
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
description: Restore a server's connection to its existing Azure Arc resource with azcmagent reconnect, using TPM-backed recovery or a managed identity reset.
ms.topic: reference
ms.date: 2026-11-10T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: a6c4decb-0ad0-90f3-5d23-5a1c4df407db
document_version_independent_id: 3e17c2e9-29fe-4046-e948-6baee8b80827
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/azcmagent-reconnect.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/azcmagent-reconnect
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/azcmagent-reconnect.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 6bbb379a-5a44-4d43-60a1-60c7a8a5b754
---

# CLI reference for azcmagent reconnect (preview) - Azure Connected Machine agent | Microsoft Learn

Restores the server's connection to its existing Azure Arc-enabled server resource without deleting and recreating the resource. This command is available in preview on Windows and Linux with Azure Connected Machine agent version 1.70 or later.

For servers that use Trusted Platform Module (TPM)-backed identity, the command restores connection while preserving Azure managed identities and their role assignments.

For servers that use file-based credential storage, use `--reset-identity`. **This replaces the server's system-assigned managed identity.** The new identity doesn't inherit the previous identity's role assignments. Record the role assignments before resetting. Afterward, grant the new identity the required access.

## Prerequisites

- Run the command from an elevated terminal on Windows or as root on Linux.
- Ensure that the Hybrid Instance Metadata Service (HIMDS) is running and that the server can reach the [required Azure Arc endpoints](network-requirements).
- Confirm that the Azure Arc-enabled server resource still exists. If it was deleted, use [`azcmagent connect`](azcmagent-connect) instead.
- If Azure sign-in is required, use an account or service principal with the **[Azure Connected Machine Resource Administrator](security-identity-authorization#rbac-roles)** role on the existing server resource, or equivalent permissions.

## Usage

First, check which credential storage the server uses. In the Azure portal, open the existing Azure Arc-enabled server resource and select **JSON View**. Alternatively, send a GET request for the resource through the Azure Resource Manager API. Check `properties.identityKeyStore` in the resource JSON:

- `Tpm` (case-insensitive): Use TPM-backed identity.
- `Default` (case-insensitive), an empty string, `null`, or an absent property: Use File-based credentials.

Any resource details you supply must match the saved agent configuration, if present, and the existing Azure resource.

### TPM-backed identity

When saved agent configuration is available, no Azure sign-in or resource details are required:

```console
azcmagent reconnect [flags]
```

If the agent configuration is missing, supply the existing resource details and Azure authentication:

```console
azcmagent reconnect [authentication] --tenant-id <tenant-id> --subscription-id <subscription-id> --resource-group <resource-group> --resource-name <resource-name> --location <region> [flags]
```

Don't use `--reset-identity` for TPM-backed identity.

### File-based credentials

**This replaces the server's system-assigned managed identity.** Record its role assignments before running the command, and grant the new identity the required access afterward.

Use `--reset-identity` and supply the existing resource details and Azure authentication, even when saved agent configuration is available:

```console
azcmagent reconnect --reset-identity [authentication] --tenant-id <tenant-id> --subscription-id <subscription-id> --resource-group <resource-group> --resource-name <resource-name> --location <region> [flags]
```

Caution

`azcmagent reconnect --reset-identity` can fail after modifying the Azure resource's identity. Rerunning the command generates another key pair and replaces the identity again; it doesn't resume the previous attempt. Verify the resulting identity before restoring role assignments.

## Examples

Reconnect a TPM-backed server using its saved configuration:

```console
azcmagent reconnect
```

Reconnect a TPM-backed server without saved configuration, using device code authentication. Replace the sample values with the existing resource's details:

```console
azcmagent reconnect --tenant-id "bbbbbbbb-cccc-dddd-eeee-ffffffffffff" --subscription-id "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee" --resource-group "HybridServers" --resource-name "Server01" --location "eastus" --use-device-code
```

Reconnect a server with file-based credentials, using device code authentication. Replace the sample values with the existing resource's details:

```console
azcmagent reconnect --reset-identity --tenant-id "bbbbbbbb-cccc-dddd-eeee-ffffffffffff" --subscription-id "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee" --resource-group "HybridServers" --resource-name "Server01" --location "eastus" --use-device-code
```

After recovery, run [`azcmagent show`](azcmagent-show) and confirm that the server returns to **Connected**.

## Authentication options

TPM-backed recovery doesn't require Azure sign-in when saved agent configuration is available.

If the configuration is missing, or you use `--reset-identity`, choose a sign-in method and its flags from [Authenticate the azcmagent CLI](azcmagent-authentication). Use credentials with the permissions described in Prerequisites.

## Flags

This command supports [Common flags](azcmagent#common-flags), [Authentication flags](azcmagent-authentication#authentication-flags), and the flags listed in this section.

The `--tenant-id`, `--subscription-id`, `--resource-group`, `--resource-name`, and `--location` flags are required for an identity reset or TPM-backed recovery without saved configuration.

`--reset-identity`

Required for servers that use file-based credentials. Resets the server's system-assigned managed identity and requires Azure authentication, even when saved configuration is present.

`--cloud`

Specifies the Azure cloud instance: `AzureCloud`, `AzureUSGovernment`, or `AzureChinaCloud`. With saved TPM-backed configuration, the command uses the saved cloud, and any value you supply must match. Otherwise, the default is `AzureCloud`.

`-l`, `--location`

Specifies the existing resource's Azure region. Must match the resource's location.

`-t`, `--tenant-id`

Specifies the tenant ID for the subscription containing the existing resource. Must be a GUID.

`-s`, `--subscription-id`

Specifies the ID of the subscription containing the existing resource. Must be a GUID, not a subscription name.

`-g`, `--resource-group`

Specifies the resource group containing the existing server resource.

`-n`, `--resource-name`

Specifies the name of the existing server resource.