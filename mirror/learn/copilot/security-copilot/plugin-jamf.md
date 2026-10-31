---
layout: Conceptual
title: Jamf and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-jamf
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the Jamf plugin with Microsoft Security Copilot.
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
document_id: 39eae303-a4bf-2106-d8c5-215e05f968ff
document_version_independent_id: 39eae303-a4bf-2106-d8c5-215e05f968ff
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-jamf.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-jamf
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-jamf.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: f943946d-e1cf-0eae-ae65-c31caf4621a1
---

# Jamf and Microsoft Security Copilot | Microsoft Learn

Jamf Pro provides comprehensive MDM data. You can use the Jamf plugin with Microsoft Security Copilot to streamline how your security analysts access data, simplify the process of gathering crucial information, and facilitate seamless collaboration between IT and Security teams.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires an API Key. You must have the *Analyst Viewer* or *Admin* role assigned in Jamf to get your API key. You'll need to take the following steps before using the plugin.

1. Sign into your Jamf Pro instance.
2. Create your API client. See [Jamf Pro Documentation 11.4.0: API Roles and Clients](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html).
3. Assign an API role to the client that has the *Read Computers* privilege.

    ![Screenshot showing how to assign an API role to a client with Read Computers permissions.](media/jamf-api-role.png)
4. Securely copy the client ID, client secret, and required scopes (scope number).
5. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
6. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
7. Next to **"Inventory Insights by Jamf**, select the toggle to enable it.
8. Provide the following information:

    - Jamf Pro Instance URL: `https://your-instance.jamfcloud.com`
    - ClientId: (Paste the copied client ID)
    - ClientSecret: (Paste the copied client secret)
    - TokenEndpoint: `https://your-instance.jamfcloud.com/api/oauth/token`
    - Scopes: `api-role:2` (whatever API scope number is associated with the role you created)
    - AuthorizationContentType: `application/x-www-form-urlencoded`

    ![Sceenshot sowing Jamf settings to fill in for the Security Copilot plugin.](media/jamf-settings.png)
9. Save your changes.

## Sample Jamf prompts

After the Jamf plugin is configured, you can use it by typing `Jamf` in your Security Copilot prompt bar, followed by an action.

Here are some examples to try:

`Does the mac H2WFP7BPF6NV have any suspicious applications installed?`

`What are all the user accounts on mac H2WFP7BPF6NV and what are their privilege levels?`

`Get complete inventory details for mac serial number H2WFP7BPF6NV.`

`Show hardware and security configuration for the mac with serial number H2WFP7BPF6NV.`

`List all installed applications on mac H2WFP7BPR6NV.`

`Check Filevault status for mac H2WFP7BPF6NV.`

`What are the firewall settings on mac H2WFP7BPQ6FV?`

## Provide feedback

To provide feedback, contact [Jamf](https://www.jamf.com/).