---
layout: Conceptual
title: Microsoft Foundry Toolkit for Visual Studio Code overview - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/get-started-projects-visual-studio-code
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
description: Learn how Microsoft Foundry Toolkit helps you discover models and build, test, deploy, evaluate, and monitor AI apps and agents in Visual Studio Code.
ms.subservice: foundry-sdk
content_well_notification:
- AI-contribution
ai-usage: ai-assisted
ms.topic: concept-article
ms.date: 2026-09-10T00:00:00.0000000Z
ms.reviewer: erichen
ms.custom:
- classic-and-new
- doc-kit-assisted
locale: en-us
document_id: 14b10af0-47f8-bfbd-009d-63a15c3102c0
document_version_independent_id: 1541c389-f8ca-6194-5e32-bbe5efa35943
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/how-to/develop/get-started-projects-visual-studio-code.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/how-to/develop/get-started-projects-visual-studio-code
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/how-to/develop/get-started-projects-visual-studio-code.md
platformId: 1805e140-e522-0cfb-0a9e-acfa5d5fd354
---

# Microsoft Foundry Toolkit for Visual Studio Code overview - Microsoft Foundry | Microsoft Learn

Microsoft Foundry Toolkit for Visual Studio Code is an extension for building, testing, deploying, evaluating, and monitoring AI apps and agents. Use it locally or connect to Microsoft Foundry to manage your AI development workflow without leaving Visual Studio Code.

Foundry Toolkit is the new name for AI Toolkit. It also includes the capabilities previously provided by the separate Microsoft Foundry extension, so you can work with local resources and Foundry resources in one extension.

## Who should use Foundry Toolkit

Foundry Toolkit supports different roles and levels of AI development experience:

- **Application developers** can add generative AI features to web, desktop, and mobile apps.
- **AI and machine learning engineers** can compare, customize, optimize, and deploy models and agents.
- **Data scientists and researchers** can experiment with prompts, models, datasets, and evaluation criteria.
- **Educators and students** can explore generative AI concepts through interactive playgrounds and local models.

## How the Toolkit workspace is organized

Foundry Toolkit separates resources that you have from actions that you can take. The extension has three main sections.

[![Screenshot of Foundry Toolkit in Visual Studio Code with My Resources, Developer Tools, and Help and Feedback sections.](../../media/how-to/get-started-projects-vs-code/foundry-toolkit-overview.png)](../../media/how-to/get-started-projects-vs-code/foundry-toolkit-overview.png#lightbox)

| Section | Purpose |
| --- | --- |
| **My Resources** | View models, agents, tools, knowledge sources, evaluations, recent resources, local resources, and resources in your Foundry project. |
| **Developer Tools** | Discover models and tools. Build, debug, deploy, test, evaluate, and monitor AI apps and agents. |
| **Help And Feedback** | Ask Copilot, get started, open documentation and release information, report issues, or join the community. |

The exact tools and resource types can change as the extension evolves. Use the Toolkit view to see the features in your installed version.

## Work with models

Foundry Toolkit provides an end-to-end model development workflow:

- Use the **Model Catalog** to discover models from Foundry and external providers, or use local models through ONNX, Ollama, and Foundry Local.
- Compare models and test prompts, parameters, images, and attachments in the **Model Playground**.
- Convert, quantize, optimize, and evaluate supported models for local Windows deployment.
- Fine-tune supported models locally with a GPU or remotely with Azure Container Apps.
- Profile CPU, GPU, and NPU usage for supported Windows machine learning workloads.

## Build and operate agents

Foundry Toolkit supports prompt agents and code-based hosted agents. Start with [Create an agent](create-agent-visual-studio-code) to compare Agent Builder, hosted-agent samples, and Copilot-assisted coding.

| Task | Guide |
| --- | --- |
| Configure a model, instructions, and tools without a hosted-agent code project. | [Create a prompt agent](create-prompt-agent-visual-studio-code). |
| Develop, inspect, and deploy code-based orchestration with Microsoft Agent Framework. | [Create hosted agents](vs-code-agents-workflow-pro-code). |
| Maintain an existing declarative workflow and prepare its migration. | [Use and migrate declarative agent workflows](vs-code-agents-workflow-low-code). |

Agent Builder also supports locally stored prompts. Their tools, structured output, and dataset evaluation options differ from those of Foundry prompt agents. Local storage doesn't mean that model inference runs on your machine. See [Work with local prompts](create-prompt-agent-visual-studio-code#work-with-local-prompts).

During development, you can:

- Use **Agent Builder** to test conversations, save prompt-agent versions, and generate client code that calls a saved Foundry agent.
- Use the **Tool Catalog** to discover Foundry tools, Model Context Protocol (MCP) servers, and toolboxes, and then add them to agents.
- Use **Agent Inspector** to debug local agents, inspect streaming responses and tool calls, and visualize workflow execution.
- Deploy hosted agents to Foundry Agent Service from source code or a container image.
- Test deployed agents in the **Hosted Agent Playground**, inspect logs and traces, and manage versions.
- Evaluate models, prompts, and agents with datasets, built-in evaluators, or custom criteria.

Important

Declarative workflows in Microsoft Foundry retire on December 1, 2026. Use Microsoft Agent Framework for new workflow development. This retirement doesn't affect code-based orchestration in hosted agents. See the [workflow migration guide](../../agents/concepts/workflow#migration-guide).

Some Toolkit experiences are available in preview. Review the [Foundry Toolkit release notes](https://github.com/microsoft/foundry-dev-tools/blob/main/WHATS_NEW.md) for release details.

## Manage Foundry resources

Sign in to Azure and set a Foundry project to manage cloud resources from Visual Studio Code. You can:

- Browse Foundry projects and the resources available to your account.
- Discover and deploy models from the Foundry model catalog.
- View model endpoints and authentication information.
- Create and version prompt agents, and deploy and test hosted agents.
- Inspect and test existing declarative workflows before migration.
- Browse tools and knowledge sources used by your agents.
- Open evaluations, conversations, logs, and traces during development.

For broader resource administration, use the [Foundry portal](https://ai.azure.com/). To automate a workflow in application code, use the [Microsoft Foundry SDKs](sdk-overview).