---
layout: Conceptual
title: Set up a Microsoft Foundry project in Visual Studio Code - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/set-up-foundry-project-visual-studio-code
breadcrumb_path: ../../../breadcrumb/azure-ai/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure-ai-foundry
ms.suite: office
author: bobtabor-msft
learn_banner_products:
- azure
manager: mcleans
ms.author: rotabor
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Sign in to Azure, select an existing Microsoft Foundry project, or create a project with Foundry Toolkit for Visual Studio Code.
ms.subservice: foundry-sdk
content_well_notification:
- AI-contribution
ai-usage: ai-assisted
ms.topic: how-to
ms.date: 2026-08-20T00:00:00.0000000Z
ms.reviewer: erichen
ms.custom:
- doc-kit-assisted
locale: en-us
document_id: 2851378a-294b-8142-8807-040d43319b10
document_version_independent_id: d6dd4d32-fb7e-2021-e90e-e71c7ae9a573
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/how-to/develop/set-up-foundry-project-visual-studio-code.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/how-to/develop/set-up-foundry-project-visual-studio-code
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/how-to/develop/set-up-foundry-project-visual-studio-code.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/911a44a7-2f6c-477c-810f-dc8b7d425cce
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/14f2b9d5-6f06-45a8-ac5f-313eaa351153
platformId: d2197edc-b2fe-27f7-b504-cd8a5c88bfaf
---

# Set up a Microsoft Foundry project in Visual Studio Code - Microsoft Foundry | Microsoft Learn

Sign in to Azure, and then select an existing Foundry project or create one with Microsoft Foundry Toolkit for Visual Studio Code. Foundry Toolkit uses the project you select as its default project for cloud models, agents, tools, and evaluations.

## Prerequisites

- [Install Microsoft Foundry Toolkit for Visual Studio Code](install-foundry-toolkit-visual-studio-code).
- An [Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- To select an existing project, access to that project. For more information, see [Role-based access control for Microsoft Foundry](../../concepts/rbac-foundry).
- To create a project, meet the [prerequisites to create a Foundry project](../create-projects#prerequisites).

## Sign in to Azure

Foundry Toolkit uses the account, tenant, and subscriptions available through the Azure Resources extension.

1. In the Activity Bar, select **Azure**.
2. In the **Azure Resources** view, select **Sign in to Azure**.
3. Complete the sign-in flow.
4. In **Accounts & Tenants**, confirm that the account and tenant for your Foundry resources are selected.
5. In **Resources**, confirm that the target subscription is visible.

## Select an existing project

Set an accessible project as the default project for Foundry Toolkit.

1. In the Activity Bar, select **Foundry Toolkit**.
2. Under **My Resources**, select **Set Foundry Project**.
3. Select **Switch project**.

    [![Screenshot of Foundry Toolkit showing Set Foundry Project and the choices to switch projects or create a project.](../../media/how-to/get-started-projects-vs-code/set-foundry-project.png)](../../media/how-to/get-started-projects-vs-code/set-foundry-project.png#lightbox)
4. Select the Azure subscription that contains the project.
5. Select the Foundry project.
6. Under **My Resources**, confirm that the project resources appear.

The selected project remains the default until you select another project, clear the default project, sign out, or lose access to the project.

## Create a project

Use Foundry Toolkit to create a Foundry account and project with basic default settings. For customized networking, security, naming, or Azure Policy requirements, use the [Foundry portal](https://ai.azure.com/) or an [infrastructure template](../create-resource-template).

1. In the Activity Bar, select **Foundry Toolkit**.
2. Under **My Resources**, select **Set Foundry Project**.
3. Select **Create project**.
4. Select your Azure subscription.
5. Select an existing resource group, or select **Create new resource group**.
6. If you create a resource group, enter the resource group name, and then select a location.
7. Enter a name for the Foundry project.
8. Monitor the notification for project creation progress.

    [![Screenshot of a Foundry Toolkit notification showing Foundry project creation progress.](../../media/how-to/get-started-projects-vs-code/project-creation-progress.png)](../../media/how-to/get-started-projects-vs-code/project-creation-progress.png#lightbox)
9. Wait for the notification that the project deployed successfully.
10. Under **My Resources**, confirm that the new project resources appear.

Foundry Toolkit creates a Foundry account named from the project, creates the project under that account, and sets the project as the Toolkit default.

## Switch the default project

Change the cloud project used by Foundry Toolkit without changing your Azure account.

1. Under **My Resources**, locate the current default project.
2. Select the gear icon next to the project.
3. Select **Switch Default Project**.

    [![Screenshot of the Foundry Toolkit project actions menu with Switch Default Project selected.](../../media/how-to/get-started-projects-vs-code/switch-default-project.png)](../../media/how-to/get-started-projects-vs-code/switch-default-project.png#lightbox)
4. Select **Switch project**.
5. Select the subscription and another accessible project.
6. Under **My Resources**, confirm that the selected project resources appear.

To work without a cloud project, run **Foundry Toolkit: Clear Default Project**.

## Clean up resources

Selecting an existing project doesn't create Azure resources. If you created a project in this article, its resources can incur charges.

- If you used a shared resource group, don't delete the resource group. Follow [Delete projects](../create-projects#delete-projects) to remove the project. Delete the Foundry account only if Toolkit created it for this procedure and it contains no other projects or resources.
- If you created a dedicated resource group and no longer need anything in it, open the [Azure portal](https://portal.azure.com), select the resource group, and select **Delete resource group**.

Warning

Deleting a resource group permanently deletes every resource in it. Review the resource list before you confirm deletion.