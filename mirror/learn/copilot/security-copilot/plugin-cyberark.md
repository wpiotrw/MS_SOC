---
layout: Conceptual
title: CyberArk Privilege Cloud and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-cyberark
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the CyberArk plugin with Microsoft Security Copilot.
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
- sfi-image-nochange
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 83333198-e126-0aae-130b-f2929eb326d3
document_version_independent_id: 83333198-e126-0aae-130b-f2929eb326d3
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-cyberark.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-cyberark
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-cyberark.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: e658b1f0-3aad-dc22-9ebf-8ea79612ec86
---

# CyberArk Privilege Cloud and Microsoft Security Copilot | Microsoft Learn

CyberArk Privilege Cloud is a SaaS solution that provides a simplified path to securely store, rotate and isolate credentials, monitor sessions, and quickly deliver scalable risk reduction to the business. You can use the CyberArk plugin with Microsoft Security Copilot to:

- List privileged accounts in Security Copilot using natural language.
- Leverage Copilot generative AI abilities to interact with privileged accounts data.

Note

This article contains information about third-party plugins. This is provided to help complete integration scenarios. However, Microsoft doesn't provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

## Know before you begin

Integration with Security Copilot requires an OAuth service user account for authentication. You'll need to take the following steps before using the plugin.

1. Sign in to your CyberArk Identity Security Platform Shared Services (ISPSS) with a user account that has permissions to manage users in CyberArk Identity.
2. Configure a new OAuth service user account by following these steps:

    1. From the service picker, choose **Identity Administration**.

        ![Screenshot showing a section of the CyberArk identity portal with Identity Administration highlighted.](media/cyberark-identity-portal.png)
    2. Expand **Core Services**, and then select **Users**.
    3. In the **Users** screen, select **Add User**, and then fill in the required details.

        ![Screenshot showing the Create User screen with required field to fill in.](media/cyberark-create-user.png)
    4. Under **Status** mark the checkbox next to **Is OAuth confidential client**, and then select **Create User**.
    5. In the menu, select **Roles**, and then assign the new user account to a *Privilege Cloud Users* role.
3. Configure CyberArk Privilege Cloud to work with the Security Copilot plugin. Follow these steps:

    1. In the service picker, select **Privilege Cloud**.

        ![Sceenshot showing CyberArk menu with Privilege Cloud selected.](media/cyberark-priv-cloud.png)
    2. In the menu, expand **Policies**, select **Safes**, and then choose the safe you want to grant permissions for.
    3. In the **Safe** pane, select the **Members** tab. Select **Add members**, and select the user account you created earlier, and then select **Next**.
    4. Assign appropriate permissions, and then select **Add**.
4. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
5. Access **Manage Plugins** by selecting the **Plugin** button from the prompt bar.
6. Next to **CyberArk**, select the toggle to enable it.
7. Provide your CyberArk Privilege Cloud instance URL and user account information.
8. Save your changes.

## Sample CyberArk prompts

After the CyberArk plugin is configured, you can use it by typing `CyberArk` in your Security Copilot prompt bar, followed by an action. You can use the plugin to list privileged accounts and get account details. The following table lists some example prompts to try and their expected output:

| Prompt example | Expected output |
| --- | --- |
| `Find an account with the username test_user` | Get all account details about an account with the username “test\_user”. |
| `Get all account details about an account with the username “test_user”` | Get a positive or negative answer whether an account with the username “test\_user” and an address “10.0.1.103” is managed by CyberArk. |
| `Get all accounts and show the results in a table` | Get details about all accounts, displayed in a table format. |

## Provide feedback

To provide feedback, contact [CyberArk](https://www.cyberark.com/).