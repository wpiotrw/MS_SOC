---
layout: Conceptual
title: Generate synthetic data with the Microsoft Foundry SDK - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cloud-evaluation-synthetic-data
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
description: Learn how to use the Microsoft Foundry SDK to generate synthetic evaluation queries for model and agent targets.
ms.subservice: foundry-observability
ms.custom:
- references_regions
ms.topic: how-to
ms.date: 2026-08-31T00:00:00.0000000Z
ms.reviewer: dlozier
ai-usage: ai-assisted
locale: en-us
document_id: cde64afd-2532-e252-2af9-87381c75ffb6
document_version_independent_id: 07d2d0ce-e4c4-7663-9c76-33303d6105cb
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/observability/how-to/cloud-evaluation-synthetic-data.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/observability/how-to/cloud-evaluation-synthetic-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/observability/how-to/cloud-evaluation-synthetic-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/954f73a6-f63f-4ee4-82b7-50903bc7735d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a5690ca4-dbe1-40cd-8b54-527e1da6d88c
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: cb379e60-721d-ba93-d22d-7aa6f0a56a19
---

# Generate synthetic data with the Microsoft Foundry SDK - Microsoft Foundry | Microsoft Learn

Important

Items marked preview in this article are currently in preview. This preview is provided without a service-level agreement, and Microsoft doesn't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Generate individual test queries, send them to a model or agent target, and evaluate the target responses.

## Prerequisites

- Complete the [cloud evaluation prerequisites](cloud-evaluation#prerequisites) and [client setup](cloud-evaluation#set-up-the-sdk-client).
- A model deployment that supports the Responses API for query generation.
- A model or agent target to evaluate.

The examples use the SDK client configured in [Set up the SDK client](cloud-evaluation#set-up-the-sdk-client).

## Generate synthetic queries

Use the `azure_ai_synthetic_data_gen_preview` data source type to generate synthetic test queries, send them to a deployed model or Foundry agent, and evaluate the responses. Use this scenario when you don't have a test dataset. The service generates queries based on a prompt you provide (and/or from the agent's instructions), runs them against your target, and evaluates the responses.

Important

Before you begin, complete [client setup](cloud-evaluation#set-up-the-sdk-client).

### How synthetic data evaluation works

1. The service generates synthetic queries based on your `prompt` and optional seed data files.
2. Each query is sent to the specified target (model or agent) to generate a response.
3. Evaluators score each response using the generated query and response.
4. The generated queries are stored as a dataset in your project for reuse.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `samples_count` | Yes | Number of synthetic test queries to generate. Specify a value from 15 through 1,000, inclusive. |
| `model_deployment_name` | Yes | Model deployment to use for generating synthetic queries. Only models with Responses API capability are supported. For availability, see [Responses API region availability](https://aka.ms/aoai/responsesapi/availability). The [model router](../../openai/concepts/model-router) isn't supported here; it can only be used as the evaluation target. |
| `prompt` | No | Instructions describing the type of queries to generate. Optional when the agent target has instructions configured. |
| `output_dataset_name` | No | Name for the output dataset where generated queries are stored. If you don't provide a name, the service generates one automatically. |
| `sources` | No | Seed data files (by file ID) to improve relevance of generated queries. Currently only one file is supported. |

### Set up evaluators and data mappings

For target evaluations, map every required evaluator input explicitly. In this synthetic-data example, generated queries are available as `{{item.query}}`, and target responses are available as `{{sample.output_text}}`.

```python
from azure.ai.projects.models import TestingCriterionAzureAIEvaluator

data_source_config = {"type": "azure_ai_source", "scenario": "synthetic_data_gen_preview"}

testing_criteria = [
    TestingCriterionAzureAIEvaluator(
        type="azure_ai_evaluator",
        name="coherence",
        evaluator_name="builtin.coherence",
        initialization_parameters={"model": model_deployment_name},
        data_mapping={
            "query": "{{item.query}}",
            "response": "{{sample.output_text}}",
        },
    ),
    TestingCriterionAzureAIEvaluator(
        type="azure_ai_evaluator",
        name="violence",
        evaluator_name="builtin.violence",
        data_mapping={
            "query": "{{item.query}}",
            "response": "{{sample.output_text}}",
        },
    ),
]
```

### Create evaluation and run

# [Python](#tab/python)
#### Model target

Generate synthetic queries and evaluate a model:

```python
eval_object = openai_client.evals.create(
    name="Synthetic Data Evaluation",
    data_source_config=data_source_config,
    testing_criteria=testing_criteria,
)

data_source = {
    "type": "azure_ai_synthetic_data_gen_preview",
    "item_generation_params": {
        "type": "synthetic_data_gen_preview",
        "samples_count": 15,
        "prompt": "Generate customer service questions about returning defective products",
        "model_deployment_name": model_deployment_name,
        "output_dataset_name": "my-synthetic-dataset",
    },
    "target": {
        "type": "azure_ai_model",
        "model": model_deployment_name,
    },
}

eval_run = openai_client.evals.runs.create(
    eval_id=eval_object.id,
    name="synthetic-data-evaluation",
    data_source=data_source,
)
```

You can optionally add a system prompt to shape the target model's behavior. When you use `input_messages` with synthetic data generation, include only `system` role messages - the service provides the generated queries as user messages automatically.

```python
data_source = {
    "type": "azure_ai_synthetic_data_gen_preview",
    "item_generation_params": {
        "type": "synthetic_data_gen_preview",
        "samples_count": 15,
        "prompt": "Generate customer service questions about returning defective products",
        "model_deployment_name": model_deployment_name,
    },
    "target": {
        "type": "azure_ai_model",
        "model": model_deployment_name,
    },
    "input_messages": {
        "type": "template",
        "template": [
            {
                "type": "message",
                "role": "system",
                "content": {
                    "type": "input_text",
                    "text": "You are a helpful customer service agent. Be empathetic and solution-oriented."
                }
            }
        ]
    },
}
```

#### Agent target

Generate synthetic queries and evaluate a Foundry agent:

```python
data_source = {
    "type": "azure_ai_synthetic_data_gen_preview",
    "item_generation_params": {
        "type": "synthetic_data_gen_preview",
        "samples_count": 15,
        "prompt": "Generate questions about returning defective products",
        "model_deployment_name": model_deployment_name,
    },
    "target": {
        "type": "azure_ai_agent",
        "name": agent_name,
        "version": agent_version,
    },
}

eval_run = openai_client.evals.runs.create(
    eval_id=eval_object.id,
    name="synthetic-agent-evaluation",
    data_source=data_source,
)
```

# [C#](#tab/csharp)
The .NET client uses its protocol methods for this preview data source.

```csharp
object[] testingCriteria =
[
  new
  {
    type = "azure_ai_evaluator",
    name = "coherence",
    evaluator_name = "builtin.coherence",
    initialization_parameters = new { model = modelDeploymentName },
    data_mapping = new
    {
      query = "{{item.query}}",
      response = "{{sample.output_text}}"
    }
  },
  new
  {
    type = "azure_ai_evaluator",
    name = "violence",
    evaluator_name = "builtin.violence",
    data_mapping = new
    {
      query = "{{item.query}}",
      response = "{{sample.output_text}}"
    }
  }
];
BinaryData evaluationData = BinaryData.FromObjectAsJson(new
{
  name = "Synthetic Data Evaluation",
  data_source_config = new
  {
    type = "azure_ai_source",
    scenario = "synthetic_data_gen_preview"
  },
  testing_criteria = testingCriteria
});
using BinaryContent evaluationContent = BinaryContent.Create(evaluationData);
ClientResult evaluation = await evaluationClient.CreateEvaluationAsync(
  evaluationContent);
string evaluationId = GetString(evaluation, "id");

BinaryData runData = BinaryData.FromObjectAsJson(new
{
  name = "synthetic-data-evaluation",
  data_source = new
  {
    type = "azure_ai_synthetic_data_gen_preview",
    item_generation_params = new
    {
      type = "synthetic_data_gen_preview",
      samples_count = 15,
      prompt = "Generate customer service questions about returning defective products",
      model_deployment_name = modelDeploymentName,
      output_dataset_name = "my-synthetic-dataset"
    },
    target = new
    {
      type = "azure_ai_model",
      model = modelDeploymentName
    }
  }
});
using BinaryContent runContent = BinaryContent.Create(runData);
ClientResult evaluationRun = await evaluationClient.CreateEvaluationRunAsync(
  evaluationId: evaluationId,
  content: runContent);
Console.WriteLine($"Evaluation run created: {GetString(evaluationRun, "id")}");
```

To evaluate an agent instead, set `target.type` to `azure_ai_agent` and provide its `name` and `version`.

Reference: [`EvaluationClient` protocol methods](https://github.com/openai/openai-dotnet/blob/main/OpenAI/src/Custom/Evals/EvaluationClient.Protocol.cs)

# [JavaScript/TypeScript](#tab/javascript)
The current JavaScript/TypeScript SDK samples don't demonstrate synthetic data evaluation. Use the Python or cURL tab for this flow.

# [cURL](#tab/curl)
```bash
# Step 1: Create the evaluation
curl --request POST \
  --url "https://${ACCOUNT}.services.ai.azure.com/api/projects/${PROJECT}/openai/evals?api-version=v1" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "Synthetic Data Evaluation",
    "data_source_config": {
      "type": "azure_ai_source",
      "scenario": "synthetic_data_gen_preview"
    },
    "testing_criteria": [
      {
        "type": "azure_ai_evaluator",
        "name": "coherence",
        "evaluator_name": "builtin.coherence",
        "initialization_parameters": {
          "model": "gpt-5-mini"
        },
        "data_mapping": {
          "query": "{{item.query}}",
          "response": "{{sample.output_text}}"
        }
      },
      {
        "type": "azure_ai_evaluator",
        "name": "violence",
        "evaluator_name": "builtin.violence",
        "data_mapping": {
          "query": "{{item.query}}",
          "response": "{{sample.output_text}}"
        }
      }
    ]
  }'

# Step 2: Create a run with synthetic data generation
curl --request POST \
  --url "https://${ACCOUNT}.services.ai.azure.com/api/projects/${PROJECT}/openai/evals/${EVAL_ID}/runs?api-version=v1" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "synthetic-data-evaluation",
    "data_source": {
      "type": "azure_ai_synthetic_data_gen_preview",
      "item_generation_params": {
        "type": "synthetic_data_gen_preview",
        "samples_count": 15,
        "prompt": "Generate customer service questions about returning defective products",
        "model_deployment_name": "gpt-5-mini",
        "output_dataset_name": "my-synthetic-dataset"
      },
      "target": {
        "type": "azure_ai_model",
        "model": "gpt-5-mini"
      }
    }
  }'
```

---