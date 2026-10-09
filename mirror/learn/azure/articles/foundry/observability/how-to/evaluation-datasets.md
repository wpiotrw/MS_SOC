---
layout: Conceptual
title: Evaluation datasets in Microsoft Foundry - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluation-datasets
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
author: lgayhardt
learn_banner_products:
- azure
manager: mcleans
ms.author: lagayhar
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Learn how evaluation datasets are structured, how to prepare them, and how Microsoft Foundry uses them in evaluation runs.
ms.reviewer: fishah
ms.date: 2026-08-26T00:00:00.0000000Z
ms.subservice: foundry-observability
ms.topic: concept-article
ai-usage: ai-assisted
locale: en-us
document_id: 43060365-de06-019a-4854-12875328d54e
document_version_independent_id: 81a68f22-e191-967a-2e24-351997760ed6
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/observability/how-to/evaluation-datasets.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/observability/how-to/evaluation-datasets
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/observability/how-to/evaluation-datasets.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4a569e72-46c5-6455-5230-8b4dc84736c2
---

# Evaluation datasets in Microsoft Foundry - Microsoft Foundry | Microsoft Learn

An evaluation dataset is a reusable collection of test cases for measuring model or agent quality. Evaluation datasets typically use JSONL, with one JSON object per line. This article explains when to use a reusable dataset, how evaluation data is organized, and the available ways to prepare it.

## Do you need an evaluation dataset?

Create a dataset when you want a stable test set that you can rerun against different model, prompt, or agent versions. Reusable datasets work well for regression testing, CI/CD quality gates, and comparisons across evaluation runs.

You don't always need a dataset. If your Foundry agent already has responses or your application emits traces to Application Insights, you can evaluate that data where it exists. See [Evaluate interactions by response ID](cloud-evaluation-deployed-interactions#evaluate-interactions-by-response-id) and [Evaluate traces](cloud-evaluation-deployed-interactions#evaluate-traces-preview).

## How Foundry uses evaluation data

In a JSONL dataset, the `messages` field represents model or agent interactions. Each message identifies a role and its content.

If your dataset contains completed responses, Foundry evaluates those responses directly. If you run the evaluation against a model or agent, Foundry generates a new response for each input and evaluates that response. Any response already stored in the dataset is ignored.

For example, consider a user who can't sign in. The agent asks which error appears, the user says their password is rejected, and the agent recommends a password reset. Turn-level evaluation scores an individual agent response, such as the password-reset guidance, by using preceding messages as context. Conversation-level evaluation scores the complete interaction.

The `evaluation_level` setting on the run controls the scoring granularity. The dataset and selected evaluators must support that level. For details, see [Choose an evaluation level](cloud-evaluation-conversations#choose-an-evaluation-level). For standard columns and examples, see [Evaluation dataset schema](evaluation-dataset-schema).

## Choose how to prepare evaluation data

| Situation | Recommended approach |
| --- | --- |
| **You have curated evaluation data** | Upload it as a versioned Foundry dataset or provide a small dataset inline. See [Prepare input data](cloud-evaluation-datasets#prepare-input-data). |
| **You want to review and reuse generated test cases before running an evaluation** | [Generate a synthetic evaluation dataset](evaluation-dataset-synthetic) from an agent definition, inline prompt, or reference file. |
| **You want a reusable dataset based on production traffic** | [Convert traces into a dataset](traces-to-dataset). |
| **You want to test simulated multi-turn scenarios** | [Generate a simulation seed dataset](evaluation-dataset-synthetic#generate-a-simulation-seed-dataset) or author test case scenarios as JSONL, and then [simulate conversations](cloud-evaluation-simulate-conversations). |
| **You have Foundry response IDs** | [Evaluate interactions by response ID](cloud-evaluation-deployed-interactions#evaluate-interactions-by-response-id) without creating a dataset. |
| **You want to evaluate existing Application Insights traces** | [Evaluate traces](cloud-evaluation-deployed-interactions#evaluate-traces-preview) without creating a dataset. |
| **You want to generate queries, invoke a target, and evaluate its responses in one workflow** | [Generate synthetic queries](cloud-evaluation-synthetic-data#generate-synthetic-queries) during the evaluation run. Foundry saves the generated queries as a dataset for reuse. |