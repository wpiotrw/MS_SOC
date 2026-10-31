---
layout: Conceptual
title: Manage plugins in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/manage-plugins
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to manage plugins to enable access to security intelligence, threat intelligence, and organizational context.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 0c12c69e-39e7-4427-637b-eaa63a89f18e
document_version_independent_id: 0c12c69e-39e7-4427-637b-eaa63a89f18e
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/manage-plugins.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manage-plugins
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/manage-plugins.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: cb8505cd-aa7a-c3c0-e2c0-9d9bc747cd25
---

# Manage plugins in Microsoft Security Copilot | Microsoft Learn

The plugin settings page helps owners control the functionality of plugins in Security Copilot.

## Manage custom plugins

The following custom plugin options are configurable:

- Control whether contributors can add custom plugins for their sessions
- Control whether contributors can publish custom plugins for everyone in the organization

Owners must set the permissions for adding custom plugins before they can be accessed. By default, only owners can add and manage their own custom plugins. In addition, owners are able to specify who has the ability to add and manage custom plugins for everyone in their organization.

Plugins added by owners can be set to be available only to them or to anyone in the organization.

Plugins added by owners and set to be available to anyone in the organization can be accessed, turned on or off, and used by all Security Copilot users. However, only owners can make modifications to the plugin.

For instructions on creating your own plugins, see [Custom plugins](custom-plugins).

### Options for managing plugins

To manage plugins as an owner:

1. On the left navigation, navigate to Owner. Select **Plugin settings**.

    ![Screenshot showing plugin settings menu.](media/plugin-settings-menu.png)
2. Choose who can add and manage their own custom plugins. Select **Owners only** or **Contributors and Owners**.

    ![Screenshot of plugin control options.](media/plugin-control-options-update.png)

    - **Owners only**:

        When an owner sets this configuration value, only owners can add and manage custom plugins for themselves (user scope).
    - **Owners and Contributors:**

        When an owner sets this configuration value, owners and contributors can add and manage custom plugins for themselves (user scope). This option enables the second permission, "Who can add and manage custom plugins for everyone in the organization?".
3. Choose who can add and manage custom plugins for users in this workspace.

    - **Owners only**:

        When an owner sets this configuration value, only owners can add and manage custom plugins for the organization (tenant scope).
    - **Owners and Contributors**:

        When an owner sets this configuration value, owners and contributors can add and manage custom plugins for the organization (tenant scope).
4. Choose to manage preinstalled plugin availability and restrict access.

    As an administrator, you have full control over which plugins are available across your organization. You can choose to make specific plugins accessible to everyone or restrict them to owners only. These settings apply to both standalone and embedded Security Copilot experiences.

    When you set up a Security Copilot agent the required plugins for that agent is automatically enabled. These plugins are activated solely for that agent and will not change the status of the plugins that you have made available or restricted to your organization. You can disable the agent at any time, giving you complete control over its operation.

## Manage preinstalled plugins

By default, all Owners and Contributors have access to preinstalled Microsoft and non-Microsoft plugins. When an owner toggles plugin availability and restricts access, there are two options for plugin availability:

- All users
- Owners only

Once access is restricted, new preinstalled plugins are made available to Owners only until configured otherwise.

Warning

Restricting access is an immediate change impacting all users of Security Copilot and embedded experiences. Exercise caution and notify users prior to impact.

Restricted plugins affect embedded experiences. Consider the example where an analyst has access to Security Copilot and Microsoft Defender XDR, but the plugins for Microsoft Defender XDR and Natural Language to KQL are restricted. The analyst experience for Copilot in Defender looks like this:

![Screenshot showing Copilot in Defender embedded experience when the plugin is restricted.](media/restricted-plugin-embedded-experience.png)

Preinstalled plugins, like **Microsoft Sentinel** and **Azure AI Search**, require more setup. Any plugin with the gear ![](media/gear-setup.png) or **Set up** button is configured per user. All users who have access to the plugin configure that plugin's setup for themselves.

## Manage accessing data from Microsoft 365 services

Allow users to query information from Microsoft 365 services that your organization has licensed. For more information, see [Accessing data from Microsoft 365 services](privacy-data-security#accessing-data-from-microsoft-365-services).

## Add custom plugins

Adding custom plugins extends the capabilities of Security Copilot.

Important

You must take precaution and ensure that plugins you create or make available in your organization adhere to responsible AI practices. For more information, see [Microsoft AI principles](https://www.microsoft.com/en-us/ai/responsible-ai?rtc=1).

You must also ensure that custom plugins you make available to your organization are fully vetted. It is good practice to vet custom plugins at a user level first, before making plugins available to the entire organization.

Note

This option is only available if an Owner has configured Security Copilot to allow Owners and Contributors to add and manage custom plugins for everyone in the organization.

The steps to add a custom plugin are as follows:

1. Select the **Security Copilot sources** icon.
2. In **Manage plugins**, scroll down to the **Custom** section.
3. Select, **Upload plugin**.

    ![Screenshot of Custom section of plugin.](media/manage-plugin-custom.png)
4. From the drop-down options, specify if you want to make the plugin available to just yourself or anyone in the organization. Then choose between adding a Security Copilot plugin or an OpenAI plugin.

    ![Screenshot that shows adding a plugin as an owner.](media/add-plugin-admin.png)

    Note

    If you choose to make a plugin available to just yourself, a private tag is added to the plugin. If you choose the option of making it available to anyone in the organization, then the plugin will be available to all Security Copilot users.
5. Depending on the plugin you'd like to add, follow the corresponding steps:

# [Security Copilot plugin](#tab/securitycopilotplugin)
1. Select **Security Copilot plugin**.
    2. You can choose to upload a file or upload as a link.

        - To upload a file:

            1. Select the **Upload file** section.
            2. Select the file to upload, then select **Add**.
        - To upload a link:

            1. Turn on **Upload as a link** toggle.
            2. Paste a link to a .yaml or .json file.
            3. Specify the file type.
            4. Select **Add**.

# [OpenAI plugin](#tab/openaiplugin)
1. Select **Open AI plugin**.
    2. Add a link to the OpenAI plugin.
    3. Select **Add**.

---
6. After the plugin is successfully added, some plugins might need to be set up. You can also choose to set up the plugin later.
7. Provide the appropriate values for the settings fields, then select **Setup**.

    After completing the setup steps, your plugin will be visible in the Custom section. You can turn the toggle on or off.

Note

You need to complete the setup steps for the plugin to be available for use and appear in the **Custom** section.

## Update a custom plugin

Depending on how owners manage custom plugins, you may be able to update your own custom plugins.

Custom plugins created by owners aren't editable by contributors.

If you need to make changes to the plugin that you added, you can edit the plugin file as follows:

1. Select the **Security Copilot plugin** icon.
2. In the **Custom** section, select the gear icon beside the plugin that you want to update.
3. Select **Edit file** and make the appropriate updates.
4. Select **Save** and confirm that you want to proceed.

## Delete a custom plugin

Depending on how owners manage custom plugins, you may be able to delete custom plugins you added as follows:

1. Select the **Security Copilot plugin** icon.
2. In the **Custom** section, select the gear icon beside the plugin that you want to delete.
3. Select **Delete** and confirm that you want to proceed.