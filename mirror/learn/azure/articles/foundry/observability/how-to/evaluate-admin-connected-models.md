---
layout: Conceptual
title: Use admin-connected models in cloud evaluations - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-admin-connected-models
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
description: Learn how to use models connected through an enterprise AI gateway as evaluators, targets, and simulators in Microsoft Foundry cloud evaluations.
ms.subservice: foundry-observability
ms.custom:
- classic-and-new
- references_regions
ms.topic: how-to
ms.date: 2026-09-25T00:00:00.0000000Z
ms.reviewer: dlozier
ai-usage: ai-assisted
locale: en-us
document_id: 6c1c318c-0f2a-aceb-2ca3-fe6390fcdbe6
document_version_independent_id: ab64bc93-c9c2-6ccc-0adc-f59fcd3841cc
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/observability/how-to/evaluate-admin-connected-models.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/observability/how-to/evaluate-admin-connected-models
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/observability/how-to/evaluate-admin-connected-models.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/bf4dbf7f-261c-4ae9-9fee-5989668a780a
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/1c4b5d48-3f26-4bd8-9592-816d9c1a3420
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 91e6c5ea-0e7c-fdd3-716f-f9355e23b15c
---

# Use admin-connected models in cloud evaluations - Microsoft Foundry | Microsoft Learn

Admin-connected models are models hosted behind an enterprise AI gateway, such as [Azure API Management](../../agents/how-to/ai-gateway) or a non-Azure AI model gateway, that an administrator connects to your Foundry project. You can use an admin-connected model for cloud evaluation scenarios that accept a model deployment.

Foundry resolves the connection endpoint and authentication, including API key, managed identity, or OAuth 2.0 authentication. Your evaluation request simply references the connection and deployment and the service manages resolving the gateway endpoint resolution and authentication.

Important

Admin-connected models require the connected deployment to expose the OpenAI **Chat Completions API**.

Note

Admin-connected model support in cloud evaluation is in preview and might not be available in all regions.

## Prerequisites

- A [Foundry project](../../how-to/create-projects).
- **Foundry User** role on the Foundry project.
- For all evaluation role requirements, see [Set up permissions for evaluation workflows](evaluation-permissions).
- An administrator has created an Azure API Management or non-Azure AI model gateway connection on your Foundry resource and added the model on the **Manage** &gt; **Resource details** &gt; **Admin-connected models** tab. For setup instructions, see [Bring your own model to Foundry Agent Service](../../agents/how-to/ai-gateway).
- The connection name and deployment name for a model that supports the OpenAI Chat Completions API.

## Reference an admin-connected model

Use the following format anywhere a supported evaluation scenario accepts a model deployment:

```text
<connection-name>/<deployment-name>
```

The following table shows common evaluation surfaces and the field that accepts the reference:

| Scenario | Field |
| --- | --- |
| AI-assisted evaluator (judge) | `initialization_parameters.model` |
| Model target | `target.model` |
| Conversation simulation | `item_generation_params.model` |

## Use an admin-connected model as an evaluator judge model

Set `initialization_parameters.model` when you configure an AI-assisted evaluator. This example uses the admin-connected model as the judge for the coherence evaluator:

# [Python](#tab/python)
```python
from azure.ai.projects.models import TestingCriterionAzureAIEvaluator

admin_connected_model = "my-apim-connection/my-model-name"

testing_criteria = [
    TestingCriterionAzureAIEvaluator(
        type="azure_ai_evaluator",
        name="coherence",
        evaluator_name="builtin.coherence",
        initialization_parameters={"model": admin_connected_model},
        data_mapping={
            "query": "{{item.query}}",
            "response": "{{item.response}}",
        },
    ),
]
```

# [C#](#tab/csharp)
```csharp
string adminConnectedModel = "my-apim-connection/gpt-4o";

object[] testingCriteria =
[
    new
    {
        type = "azure_ai_evaluator",
        name = "coherence",
        evaluator_name = "builtin.coherence",
        initialization_parameters = new { model = adminConnectedModel },
        data_mapping = new
        {
            query = "{{item.query}}",
            response = "{{item.response}}"
        }
    }
];
```

# [JavaScript/TypeScript](#tab/javascript)
```typescript
const adminConnectedModel = "my-apim-connection/gpt-4o";

const testingCriteria = [
    {
        type: "azure_ai_evaluator",
        name: "coherence",
        evaluator_name: "builtin.coherence",
        initialization_parameters: { model: adminConnectedModel },
        data_mapping: {
            query: "{{item.query}}",
            response: "{{item.response}}",
        },
    },
];
```

---

- Reference: [`TestingCriterionAzureAIEvaluator`](/en-us/python/api/azure-ai-projects/azure.ai.projects.models.testingcriterionazureaievaluator) (Python)
- Reference: [OpenAI Evals API](https://platform.openai.com/docs/api-reference/evals) (`testing_criteria`, all languages)

## Use an admin-connected model as a target

Set `target.model` to send each evaluation input to the admin-connected model:

# [Python](#tab/python)
```python
admin_connected_model = "my-apim-connection/my-model-name"

target = {
    "type": "azure_ai_model",
    "model": admin_connected_model,
    "sampling_params": {
        "top_p": 1.0,
        "max_completion_tokens": 2048,
    },
}
```

# [C#](#tab/csharp)
```csharp
string adminConnectedModel = "my-apim-connection/gpt-4o";

object target = new
{
    type = "azure_ai_model",
    model = adminConnectedModel,
    sampling_params = new
    {
        top_p = 1.0f,
        max_completion_tokens = 2048
    }
};
```

# [JavaScript/TypeScript](#tab/javascript)
```typescript
const adminConnectedModel = "my-apim-connection/gpt-4o";

const target = {
    type: "azure_ai_model",
    model: adminConnectedModel,
    sampling_params: {
        top_p: 1.0,
        max_completion_tokens: 2048,
    },
};
```

---

- Reference: [OpenAI Evals API](https://platform.openai.com/docs/api-reference/evals) (`data_source.target`, all languages)

Use this target with the [model target evaluation flow described in Run evaluations in the cloud](cloud-evaluation-targets#evaluate-a-model-target).

## Use other evaluation scenarios

Other model-based scenarios in [Run evaluations in the cloud by using the Microsoft Foundry SDK](cloud-evaluation) work similarly with admin-connected models. Wherever the scenario accepts a supported model deployment, replace the deployment name with `<connection-name>/<deployment-name>`. For example, conversation simulation accepts this reference in `item_generation_params.model`.

Keep the Foundry project endpoint unchanged, and don't add the gateway endpoint or credentials to the evaluation request. Foundry resolves those values from the admin-connected model connection.

Note

Admin-connected model isn't available for synthetic data generation.