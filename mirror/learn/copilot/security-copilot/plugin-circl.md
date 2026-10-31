---
layout: Conceptual
title: CIRCL Hash Lookup and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-circl
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the CIRCL Hash Lookup plugin you can use with Microsoft Security Copilot.
ms.date: 2025-08-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 97a1fdff-a552-1c26-2683-ab958f90981a
document_version_independent_id: 97a1fdff-a552-1c26-2683-ab958f90981a
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-circl.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-circl
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-circl.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: df014b73-4c14-ebfd-e4df-e6921a1b3503
---

# CIRCL Hash Lookup and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

The Computer Incident Response Center Luxembourg ([CIRCL](https://www.circl.lu)) is a government-driven initiative designed to provide a systematic response facility to computer security threats and incidents. CIRCL Hash Lookup integration enables you to validate suspicious files in the form of hashes, either MD5, SHA-1, or SHA-256, in Security Copilot. You can use this plugin to get information about a file and verify whether it's allowlisted or blocklisted by trusted security platforms.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

You don't have to sign up for an account to use CIRCL Hash Lookup. You also don't need an API key. You'll need to take the following steps before using the plugin.

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
3. Verify that **CIRCL Hash Lookup** is turned on.

## Sample CIRCL Hash Lookup prompts

Try one or more of the capabilities listed in the following table:

| Capability | Example prompts |
| --- | --- |
| `lookupMD5HashCIRCL` This endpoint allows you to lookup information on CIRCL about a specific MD5 hash  Required input: hash | - `lookup this MD5 hash using CIRCL`- `lookup information on this MD5 hash using CIRCL` |
| `lookupSHA1HashCIRCL`This endpoint allows you to lookup information on CIRCL about a specific SHA-1 hash  Required input: hash | - `lookup this SHA-1 hash using CIRCL`- `lookup information on this SHA-1 hash using CIRCL` |
| `lookupSHA256HashCIRCL` This endpoint allows you to lookup information on CIRCL about a specific SHA-256 hash Required input: hash | - `lookup this SHA-256 hash using CIRCL`- `lookup information on this SHA-256 hash using CIRCL`Alternatively, you can type the name of a specific capability, like `lookupMD5HashCIRCL` in the prompt bar, instead of using one of the example prompts. |

## Troubleshoot the CIRCL Hash Lookup plugin

### Errors occur

If you get errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts are not invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. For example, if you're using multiple sources that provide hash information like CIRCL, there might be conflicts. You can either use the product name `CIRCL` in your prompts, or type the name of a specific capability, like `lookupMD5HashCIRCL` instead.

## Provide feedback

To provide feedback, contact [CIRCL](https://www.circl.lu).