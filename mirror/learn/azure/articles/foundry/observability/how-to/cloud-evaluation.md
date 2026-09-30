---
layout: Conceptual
title: Introduction to cloud evaluation with Microsoft Foundry SDK - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cloud-evaluation
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
description: Set up the Microsoft Foundry SDK and choose a cloud evaluation workflow for datasets, targets, interactions, conversations, or synthetic data.
ms.subservice: foundry-observability
ms.custom:
- classic-and-new
- references_regions
ms.topic: how-to
ms.date: 2026-09-25T00:00:00.0000000Z
ms.reviewer: dlozier
ai-usage: ai-assisted
locale: en-us
document_id: 0afb084c-6c63-7308-3646-32345de3bf5c
document_version_independent_id: 5ebc49c6-078c-ab36-b9b4-5bd0ac564d8f
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/observability/how-to/cloud-evaluation.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/observability/how-to/cloud-evaluation
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/observability/how-to/cloud-evaluation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/954f73a6-f63f-4ee4-82b7-50903bc7735d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a5690ca4-dbe1-40cd-8b54-527e1da6d88c
platformId: f8e8a2e2-052d-de83-2f9e-51d7cdfc01d0
---

# Introduction to cloud evaluation with Microsoft Foundry SDK - Microsoft Foundry | Microsoft Learn

Use cloud evaluations to test generative AI applications at scale without managing local compute. This article sets up the shared SDK client and helps you choose a workflow for predeployment or production evaluation.

## Prerequisites

- A [Foundry project](../../how-to/create-projects).
- An Azure OpenAI deployment with a GPT model that supports chat completion, such as `gpt-5-mini`.
- The **Foundry User** role on the Foundry project.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- For all evaluation role requirements, see [Set up permissions for evaluation workflows](evaluation-permissions).
- Optionally, [your own storage account](../../concepts/evaluation-regions-limits-virtual-network#bring-your-own-storage) for evaluation data.

Some evaluation features have regional restrictions. Review the [supported regions](../../concepts/evaluation-evaluators/risk-safety-evaluators#foundry-project-configuration-and-region-support) before you begin.

## Set up the SDK client

Install the SDK for your language. Set these shared environment variables:

- `AZURE_AI_PROJECT_ENDPOINT`: Your Foundry project endpoint, for example, `https://<account_name>.services.ai.azure.com/api/projects/<project_name>`.
- `AZURE_AI_MODEL_DEPLOYMENT_NAME`: The model deployment used by AI-assisted evaluators.
- `DATASET_NAME` and `DATASET_VERSION`: Optional values for reusable datasets.

Authenticate with `DefaultAzureCredential`, create the project client, and get the OpenAI client used by the evaluation API.

# [Python](#tab/python)
```bash
pip install "azure-ai-projects>=2.2.0"
```

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import TestingCriterionAzureAIEvaluator
from openai.types.eval_create_params import DataSourceConfigCustom
from openai.types.evals.create_eval_jsonl_run_data_source_param import (
    CreateEvalJSONLRunDataSourceParam,
    SourceFileContent,
    SourceFileContentContent,
    SourceFileID,
)

endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
model_deployment_name = os.environ.get(
    "AZURE_AI_MODEL_DEPLOYMENT_NAME", ""
)
dataset_name = os.environ.get("DATASET_NAME", "")
dataset_version = os.environ.get("DATASET_VERSION", "1")

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)
openai_client = project_client.get_openai_client()
```

Reference: [`AIProjectClient`](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient), [`DefaultAzureCredential`](/en-us/python/api/azure-identity/azure.identity.defaultazurecredential)

# [C#](#tab/csharp)
```dotnetcli
dotnet add package Azure.AI.Projects --prerelease
dotnet add package Azure.Identity
```

```csharp
using System.ClientModel;
using System.Collections.Generic;
using System.Text.Json;
using Azure.AI.Extensions.OpenAI;
using Azure.AI.Projects;
using Azure.Identity;
using OpenAI.Evals;
using OpenAI.Responses;

#pragma warning disable OPENAI001

static string GetString(ClientResult result, string propertyName)
{
  using JsonDocument document = JsonDocument.Parse(
    result.GetRawResponse().Content.ToMemory());
  return document.RootElement.GetProperty(propertyName).GetString()
    ?? throw new InvalidOperationException(
      $"The response doesn't contain {propertyName}.");
}

var projectEndpoint = Environment.GetEnvironmentVariable(
  "AZURE_AI_PROJECT_ENDPOINT")
  ?? throw new InvalidOperationException(
    "AZURE_AI_PROJECT_ENDPOINT isn't set.");
var modelDeploymentName = Environment.GetEnvironmentVariable(
  "AZURE_AI_MODEL_DEPLOYMENT_NAME")
  ?? throw new InvalidOperationException(
    "AZURE_AI_MODEL_DEPLOYMENT_NAME isn't set.");
var datasetName = Environment.GetEnvironmentVariable("DATASET_NAME")
  ?? "evaluation-data";
var datasetVersion = Environment.GetEnvironmentVariable("DATASET_VERSION")
  ?? "1";

AIProjectClient projectClient = new(
  endpoint: new Uri(projectEndpoint),
  tokenProvider: new DefaultAzureCredential());
EvaluationClient evaluationClient = projectClient.ProjectOpenAIClient
  .GetEvaluationClient();
```

Reference: [`AIProjectClient`](/en-us/dotnet/api/azure.ai.projects.aiprojectclient), [`DefaultAzureCredential`](/en-us/dotnet/api/azure.identity.defaultazurecredential), and [`EvaluationClient`](https://github.com/openai/openai-dotnet/blob/main/OpenAI/src/Custom/Evals/EvaluationClient.Protocol.cs)

# [JavaScript/TypeScript](#tab/javascript)
```bash
npm install @azure/ai-projects @azure/identity dotenv
```

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";
import "dotenv/config";

const projectEndpoint = process.env["AZURE_AI_PROJECT_ENDPOINT"] || "";
const modelDeploymentName =
  process.env["AZURE_AI_MODEL_DEPLOYMENT_NAME"] || "";
const datasetName = process.env["DATASET_NAME"] || "";
const datasetVersion = process.env["DATASET_VERSION"] || "1";

const projectClient = new AIProjectClient(
  projectEndpoint,
  new DefaultAzureCredential(),
);
const openaiClient = projectClient.getOpenAIClient();
```

Reference: [AIProjectClient class](/en-us/javascript/api/@azure/ai-projects/aiprojectclient)

---

To use a model connected through admin connections as a target, judge model, or conversation simulator, see [Use admin-connected models in cloud evaluations](evaluate-admin-connected-models).

## Understand the evaluation workflow

A cloud evaluation has three steps:

1. Define the data shape and the evaluators that score it.
2. Create the evaluation with the evaluation client.
3. Start a run, poll until it completes, and retrieve the scored results.

Cloud evaluation results are stored in your Foundry project. You can retrieve them through the SDK, review them in the portal, or route them to Application Insights when it's connected.

## Choose evaluators

Evaluators bind to fields in your data through column mappings. Dataset workflows expose item fields, while target-generated workflows also expose the model or agent output through the sample schema.

Review the [built-in evaluators](../../concepts/built-in-evaluators) and [custom evaluators](../../concepts/evaluation-evaluators/custom-evaluators) before you configure testing criteria.

## Choose your starting point

| Evaluation unit | Starting point | Workflow |
| --- | --- | --- |
| Individual turn | You have JSONL or CSV test data with a query and response. | [Evaluate query-response datasets](cloud-evaluation-datasets) |
| Individual turn | You have queries and want a model or agent to generate responses. | [Evaluate model and agent responses](cloud-evaluation-targets) |
| Individual turn | You have stored responses or traces from individual interactions with a deployed model or agent. | [Evaluate deployed model and agent interactions](cloud-evaluation-deployed-interactions) |
| Individual turn | You need to generate synthetic queries. | [Generate synthetic queries](cloud-evaluation-synthetic-data#generate-synthetic-queries) |
| Complete conversation | You have a dataset of complete conversations. | [Evaluate conversation datasets](cloud-evaluation-conversations) |
| Complete conversation | You have traces that capture complete conversations with a deployed model or agent. | [Evaluate deployed model and agent conversations](cloud-evaluation-deployed-conversations) |
| Complete conversation | You need to generate and evaluate simulated agent conversations. | [Simulate agent conversations](cloud-evaluation-simulate-conversations) |
| Any evaluation unit | You need to poll, interpret, cancel, or troubleshoot a run. | [Get evaluation results](cloud-evaluation-results) |

For adversarial safety testing, use [AI red teaming](../../how-to/develop/run-ai-red-teaming-cloud). To create a standalone dataset, see [Generate a synthetic evaluation dataset](evaluation-dataset-synthetic).