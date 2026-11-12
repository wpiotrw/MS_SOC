---
layout: Conceptual
title: CLI reference for `azcmagent disconnect` - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/azcmagent-disconnect
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
description: Syntax for the `azcmagent disconnect` command line tool
ms.topic: reference
ms.date: 2026-11-10T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: eac983cc-74ee-f703-4153-0d287f36ef3c
document_version_independent_id: f971d12a-7007-10da-61fe-19a2cbe10243
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/azcmagent-disconnect.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/azcmagent-disconnect
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/azcmagent-disconnect.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/289b8734-3abd-4162-bc19-e661c3f4c940
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/6a94795e-9024-410d-b38e-b67941440893
platformId: 89170b87-0ed8-ebb1-334e-1fa7f2c7c562
---

# CLI reference for `azcmagent disconnect` - Azure Arc | Microsoft Learn

Deletes the Azure Arc-enabled server resource in the cloud and resets the configuration of the local agent. For detailed information on removing extensions and disconnecting and uninstalling the agent, see [Uninstall the Azure Connected Machine agent from Arc-enabled servers](uninstall-agent).

Caution

When disconnecting the agent from Azure Local VMs enabled by Azure Arc, use only the `azcmagent disconnect --force-local-only` command. Using the command without the `--force-local-only` flag can cause your Azure Local VM to be deleted both from Azure and on-premises.

## Usage

```
azcmagent disconnect [authentication] [flags]
```

## Examples

Disconnect a server using the default login method (interactive browser or device code):

```
azcmagent disconnect
```

Disconnect a server using a service principal:

```
azcmagent disconnect --service-principal-id "ID" --service-principal-secret "SECRET"
```

Disconnect a server using Azure CLI credentials (requires Azure Connected Machine agent version 1.59 or later):

```
azcmagent disconnect --use-azcli
```

Disconnect a server if the corresponding resource in Azure has already been deleted.

```
azcmagent disconnect --force-local-only
```

## Authentication options

Choose a sign-in method and its flags from [Authenticate the azcmagent CLI](azcmagent-authentication). Use an account or service principal with the **[Azure Connected Machine Resource Administrator](security-identity-authorization#rbac-roles)** role on the existing server resource, or equivalent permission to delete it.

## Flags

This command supports [Common flags](azcmagent#common-flags), [Authentication flags](azcmagent-authentication#authentication-flags), and the flag listed in this section.

`-f`, `--force-local-only`

Disconnects the server without deleting the resource in Azure. Primarily used if the Azure resource was deleted and the local agent configuration needs to be cleaned up.