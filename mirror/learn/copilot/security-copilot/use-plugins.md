---
layout: Conceptual
title: Use plugins in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/use-plugins
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use plugins, the different plugin categories, and the ways to configure the plugins in Security Copilot.
ms.date: 2026-06-01T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: ee8e709c-c4dc-3b55-5131-b5574d9a6057
document_version_independent_id: ee8e709c-c4dc-3b55-5131-b5574d9a6057
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/use-plugins.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: use-plugins
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/use-plugins.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: cb38b28e-c864-c342-e2de-4b301dc21105
---

# Use plugins in Microsoft Security Copilot | Microsoft Learn

Security Copilot includes many preinstalled plugins for Microsoft security services and other commonly used services and websites. Additionally, depending on how your administrator has configured plugins, you might be able to to add, delete, update, and manage both preinstalled and custom plugins.

Note

Microsoft processes and stores data from these plugins according to our [Privacy and Data](privacy-data-security) policies.

Watch the following video to learn more about plugins:

## Control plugins

To personalize the way Security Copilot interacts with you, there are two ways to configure the plugins on your list:

- Turn any plugin on or off
- Apply filters
- Personalize plugin settings

### Enable or disable plugins

Copilot uses on-behalf-of authentication to access security-related data through active Microsoft plugins. If a plugin requires its own authentication setup though, the plugin determines the authentication instead of on-behalf-of. For more information, see [Understand authentication](authentication#access-the-capabilities-of-microsoft-plugins).

Plugin sources are separated into these plugin categories:

- **Microsoft**
- **Non-Microsoft**
- **Websites**
- **Custom**

Select which plugins Security Copilot uses as a data source by turning service toggles on or off.

1. Select the **Security Copilot sources** icon.
2. Select the plugin you'd like to use by turning the toggle on or off. Custom plugins you don't have access to won't appear. Preinstalled plugins you don't have access to will indicate they're *Restricted*.

    [![Screenshot that shows Turn on or off toggles for plugins.](media/manage-plugin-toggles-update-small.png)](media/manage-plugin-toggles-update.png#lightbox)

### Apply filters

You can apply filters to improve discoverability and quickly find the plugin that suits your needs. By applying filters, you can narrow down plugins based on **state**, such as active or inactive, and by **category**. You can also apply multiple filters to better refine your search, helping you see the most relevant plugins for your workflow. For example, you can select all active custom plugins.

[![Screenshot plugin filters.](media/plugin-filters.png)](media/plugin-filters.png#lightbox)

### Personalize plugin settings

Personalize Security Copilot plugin experiences by configuring the plugin setting. For example, a user who wants the Microsoft Sentinel plugin to use a particular workspace that they designate as the default, personalizes the settings to specify the workspace.

Currently personalization settings are available for the following Microsoft plugins:

- Microsoft Sentinel
- Microsoft Defender External Attack Surface Management

1. Select the **Security Copilot sources** icon.
2. Select the gear icon.

    [![Screenshot that shows Personalize plugin settings.](media/personalize-gear-update-small.png)](media/personalize-gear-update.png#lightbox)
3. Provide setting details, then select **Save**.