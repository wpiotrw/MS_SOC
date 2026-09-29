---
layout: Conceptual
title: Install Microsoft Foundry Toolkit for Visual Studio Code - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/install-foundry-toolkit-visual-studio-code
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
description: Install and verify Microsoft Foundry Toolkit for Visual Studio Code from the Visual Studio Marketplace or the Extensions view.
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
document_id: dcd97cf9-61b2-9432-b1d4-d55f0f5d4ba8
document_version_independent_id: b2199145-a3ba-f88e-8e6d-0725e9d0faf0
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/how-to/develop/install-foundry-toolkit-visual-studio-code.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/how-to/develop/install-foundry-toolkit-visual-studio-code
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/how-to/develop/install-foundry-toolkit-visual-studio-code.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/911a44a7-2f6c-477c-810f-dc8b7d425cce
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/4628cbd9-6f47-4ae1-b371-d34636609eaf
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/14f2b9d5-6f06-45a8-ac5f-313eaa351153
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/be21deb8-8c64-44b0-b71f-2dc56ca7364f
platformId: 97729a34-836e-535d-4b22-82a8d45982d9
---

# Install Microsoft Foundry Toolkit for Visual Studio Code - Microsoft Foundry | Microsoft Learn

Install Microsoft Foundry Toolkit for Visual Studio Code from the Visual Studio Marketplace or the Extensions view. When you finish, the Foundry Toolkit view is available in Visual Studio Code.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/Download).
- The [.NET Runtime](/en-us/dotnet/core/install/). Foundry Toolkit depends on this runtime.

For a complete Foundry development environment, install [Foundry DevPack](install-cli-sdk#install-foundry-devpack) instead of installing Foundry Toolkit by itself. DevPack installs Foundry Toolkit, `azd` and `azd ai`, Foundry Canvas, and Microsoft Foundry Skill to provide a smoother workflow across your editor, terminal, and coding agent. For the full setup, see [Prepare your development environment](install-cli-sdk).

## Install Foundry Toolkit

Install the extension from the Visual Studio Marketplace or from within Visual Studio Code.

### Install from the Visual Studio Marketplace

1. Open the [Microsoft Foundry Toolkit for Visual Studio Code extension](https://aka.ms/foundrytk) page.
2. Select **Install**, and follow the prompt to open Visual Studio Code.
3. In Visual Studio Code, complete the installation. Reload the window if prompted.
4. Confirm that the **Foundry Toolkit** icon appears in the Activity Bar.

### Install manually from Visual Studio Code

Use the Extensions view to find and install the extension without leaving Visual Studio Code.

[![Screenshot of the Visual Studio Code Extensions Marketplace showing the Foundry Toolkit for VS Code extension details.](../../media/how-to/get-started-projects-vs-code/install-foundry-toolkit-marketplace.png)](../../media/how-to/get-started-projects-vs-code/install-foundry-toolkit-marketplace.png#lightbox)

1. In the Activity Bar, select **Extensions**.
2. Search for **Foundry Toolkit for VS Code**.
3. In the search results, select the extension published by Microsoft.
4. Select **Install**.
5. Reload the window if prompted.
6. Confirm that the **Foundry Toolkit** icon appears in the Activity Bar.

After installation, open **What's New** under **Help And Feedback** in Foundry Toolkit to review the features and changes in the installed version.

## Confirm the installation

Confirm that the extension activated successfully.

1. Select **Foundry Toolkit** in the Activity Bar.
2. Confirm that **My Resources**, **Developer Tools**, and **Help And Feedback** appear in the Foundry Toolkit view.

## Clean up

This procedure doesn't create Azure resources. If you installed Foundry Toolkit only to evaluate it, open **Extensions**, find **Foundry Toolkit for Visual Studio Code**, and select **Uninstall**. Uninstalling the extension doesn't delete any Azure resources.