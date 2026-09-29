---
layout: Conceptual
title: Evaluation dataset schema in Microsoft Foundry - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluation-dataset-schema
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
description: Learn the standard fields and supported shapes for turn-level, conversation-level, agent, and simulation seed evaluation datasets.
ms.reviewer: fishah
ms.date: 2026-08-26T00:00:00.0000000Z
ms.subservice: foundry-observability
ms.topic: concept-article
ai-usage: ai-assisted
locale: en-us
document_id: 10d1a638-2881-90fd-0ce5-94d749a7abb6
document_version_independent_id: 4af94145-96df-02d4-c29f-a8c6f35c4c0c
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/observability/how-to/evaluation-dataset-schema.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/observability/how-to/evaluation-dataset-schema
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/observability/how-to/evaluation-dataset-schema.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 2548e594-1d0a-66c6-ffae-cd2e9d66275f
---

# Evaluation dataset schema in Microsoft Foundry - Microsoft Foundry | Microsoft Learn

Each line in an evaluation JSONL file contains one evaluation test case. The evaluation scenario determines its primary required column, while the selected evaluators can require supporting columns.

| Evaluation scenario | Primary required column | Additional columns depend on |
| --- | --- | --- |
| **Evaluate an existing interaction** | `messages` | The selected evaluators. |
| **Evaluate a stored separate input and output** | `query`, `response` | The selected evaluators. |
| **Evaluate a model or agent target** | Input captured in the `messages` or `query` column; Foundry generates the response | The selected evaluators. |
| **Evaluate simulated conversations** | `test_case_description` | Optional simulation guidance, such as `desired_num_turns`. |

Additional requirements depend on the selected evaluators. For example, a textual similarity evaluator can require `ground_truth`, groundedness can require `context` when `query` and `response` are strings, and an agent evaluator can require `tool_definitions`. For evaluator requirements, see [Built-in evaluators](../../concepts/built-in-evaluators).

Evaluations based on existing traces, response IDs, or [generated synthetic queries](cloud-evaluation-synthetic-data#generate-synthetic-queries) don't require an input dataset.

## Standard columns

The standard columns depend on whether the evaluation uses model or agent interaction data or conversation simulation.

### Model and agent evaluation columns

Use one interaction format for each test case: either the `messages` column or the separate `query` and `response` columns.

| Column | Required when | What it contains |
| --- | --- | --- |
| **`messages`** | Using the `messages` format for a stored interaction or model or agent target input | For stored interactions, input and output messages. For a model or agent target, input messages that Foundry sends to the target to generate a response. Messages can include system instructions, conversation history, typed text content, tool calls, and tool results. |
| **`query`** | Using the separate query and response format | The input and any interaction history, provided as a string or message array, used as context when scoring `response`. |
| **`response`** | Evaluating a stored response; not required for a model or agent target | The response being evaluated. |
| **`ground_truth`** | An evaluator compares the output with a reference answer | The expected or reference response. |
| **`tool_definitions`** | An evaluator requires the schemas of tools available to the agent | Tool names, descriptions, and parameter schemas. This column is optional for most evaluations. |
| **`context`** | A specific evaluator requires separate supporting context | Supporting information used mainly with string `query` and `response` values when the needed context isn't already represented in messages. |

### Conversation simulation columns

| Column | Required | What it contains |
| --- | --- | --- |
| **`test_case_description`** | Yes | The user's situation, goal, constraints, and behavior that the simulator should act out. |
| **`desired_num_turns`** | No | Guidance for the expected length of the simulated conversation. |

## Messages format

The `messages` column is an array. Each message identifies a role and its content. A row can contain one exchange or a complete multi-turn conversation.

The following running example contains a short account-support interaction:

```json
{
  "messages": [
    {"role": "system", "content": "You are an account support assistant."},
    {"role": "user", "content": "I can't sign in to my account."},
    {"role": "assistant", "content": "What error message do you see?"},
    {"role": "user", "content": "It says my password is incorrect."},
    {"role": "assistant", "content": "Use the password-reset link on the sign-in page. If the reset email doesn't arrive, check your spam folder or contact account support."}
  ]
}
```

This example includes a stored agent response, so the final message has the `assistant` role. For a model or agent target, end the `messages` array with a `user` message. Foundry sends the messages to the target, generates the next assistant response, and evaluates that response.

For turn-level evaluation, earlier messages provide context for the response being scored. In this example, an evaluator can score the final password-reset guidance by using the preceding messages as context. For conversation-level evaluation, an evaluator scores the complete interaction. The `evaluation_level` setting on the run selects the scoring level; the `messages` row stays the same.

For more information, see [Choose an evaluation level](cloud-evaluation-conversations#choose-an-evaluation-level).

### Message structure

Each message has a `role` and `content`. The `content` value can be a string or an array of typed content items. Tool-result messages also use `tool_call_id` to identify the corresponding tool call.

Text messages align with the [OpenAI Responses message structure](https://developers.openai.com/api/reference/resources/responses/methods/create). Input messages can use `input_text`, and assistant output can use `output_text`. Foundry evaluation also supports the `text` shorthand and normalized `tool_call` and `tool_result` content items shown in this article.

```text
[
  {
    "role": "developer" | "system" | "user" | "assistant" | "tool",
    "tool_call_id": "string",              // For role "tool"
    "content": "string" | [                // String or content-item array
      {
        "type": "text" | "input_text" | "output_text" | "tool_call" | "tool_result",
        "text": "string",                  // For text content
        "tool_call_id": "string",          // When type is tool_call
        "name": "string",                  // Tool name for tool_call
        "arguments": { ... },              // Tool arguments for tool_call
        "tool_result": { ... }             // Result for tool_result
      }
    ]
  }
]
```

| Role | Description |
| --- | --- |
| **`developer`** | Application instructions that take precedence over user messages. |
| **`system`** | Agent instructions. |
| **`user`** | User messages and requests. |
| **`assistant`** | Agent responses, including tool calls. |
| **`tool`** | Tool execution results. |

### Messages with content arrays

The `content` value can also be an array of typed content items instead of a string. This example uses the Responses API `input_text` and `output_text` types:

```json
{
  "messages": [
    {
      "role": "developer",
      "content": [
        {"type": "input_text", "text": "You are an account support assistant."}
      ]
    },
    {
      "role": "user",
      "content": [
        {"type": "input_text", "text": "I can't sign in to my account."}
      ]
    },
    {
      "role": "assistant",
      "content": [
        {"type": "output_text", "text": "What error message do you see?"}
      ]
    }
  ]
}
```

### Messages with tool calls

This variation of the running example includes a tool call and its result:

```json
{
  "messages": [
    {"role": "system", "content": "You are an account support assistant."},
    {"role": "user", "content": "I can't sign in to my account."},
    {"role": "assistant", "content": [{"type": "tool_call", "tool_call_id": "call_123", "name": "get_sign_in_guidance", "arguments": {"error": "incorrect password"}}]},
    {"role": "tool", "tool_call_id": "call_123", "content": [{"type": "tool_result", "tool_result": {"recommended_action": "password reset"}}]},
    {"role": "assistant", "content": [{"type": "text", "text": "Use the password-reset link on the sign-in page. If the reset email doesn't arrive, check your spam folder or contact account support."}]}
  ]
}
```

## Evaluator-specific columns

Most evaluations need only the primary interaction column. Add supporting columns when a selected evaluator requires them.

### Ground truth

`ground_truth` is a string containing the expected or reference answer. Include it when an evaluator compares the model or agent output with a known answer.

```json
{
  "messages": [
    {"role": "user", "content": "I can't sign in to my account."},
    {"role": "assistant", "content": "Use the password-reset link on the sign-in page."}
  ],
  "ground_truth": "Direct the user to reset their password from the sign-in page."
}
```

### Tool definitions

`tool_definitions` describes the tools available to the agent. The `messages` array shows what the agent called. `tool_definitions` supplies the names, descriptions, and parameter schemas of all tools that the agent could use.

Include this column when an evaluator needs to compare tool behavior with the tools that were available.

```json
{
  "messages": [
    {"role": "user", "content": "I can't sign in to my account."},
    {"role": "assistant", "content": [{"type": "tool_call", "tool_call_id": "call_123", "name": "get_sign_in_guidance", "arguments": {"error": "incorrect password"}}]},
    {"role": "tool", "tool_call_id": "call_123", "content": [{"type": "tool_result", "tool_result": {"recommended_action": "password reset"}}]},
    {"role": "assistant", "content": "Use the password-reset link on the sign-in page."}
  ],
  "tool_definitions": [
    {
      "name": "get_sign_in_guidance",
      "description": "Get troubleshooting guidance for a sign-in error.",
      "parameters": {
        "type": "object",
        "properties": {
          "error": {"type": "string"}
        },
        "required": ["error"]
      }
    }
  ]
}
```

For the full schema, see [Tool definitions format](../../concepts/evaluation-evaluators/agent-evaluators#tool-definitions-format).

### Context

`context` contains supporting information used to evaluate a response. This column is mainly useful with string `query` and `response` values when the needed information isn't already represented in message history. For details about this representation, see Separate query and response format.

For example, a groundedness evaluator can use `context` as the source material that should support the response:

```json
{
  "query": "How can I reset my password?",
  "response": "Use the password-reset link on the sign-in page.",
  "context": "Users can reset their password from the sign-in page."
}
```

## Conversation simulation

A simulation seed, also called a test case scenario, describes a situation that the simulator should act out as the user. `test_case_description` is the only required column. `desired_num_turns` is optional simulation guidance.

The following seed continues the account sign-in example:

```json
{
  "test_case_description": "Act as a user who can't sign in and initially provides little detail. After the agent asks a clarifying question, explain that your password is being rejected. Continue until the agent gives clear password-reset guidance.",
  "desired_num_turns": 4
}
```

Foundry uses a simulator to play the user's role and interact with the target agent. Conversation-level evaluators then score the simulated conversation, not the seed row.

For the simulation procedure, see [Simulate conversations](cloud-evaluation-simulate-conversations). To generate seed rows instead of authoring them, see [Generate a simulation seed dataset](evaluation-dataset-synthetic#generate-a-simulation-seed-dataset-sdk).

## Separate query and response format

Some evaluators and workflows use separate `query` and `response` columns. This format remains supported. Both columns can contain strings or message arrays that use the same structure as `messages`.

Use string values for a simple single-turn test case that doesn't need conversation history or tool-call details:

```json
{"query":"I can't sign in to my account.","response":"Use the password-reset link on the sign-in page."}
```

If `query` is a message array, it can include system instructions, previous turns, tool calls, and tool results. Evaluators use this history as context when scoring `response`.

```json
{
  "query": [
    {"role": "system", "content": "You are an account support assistant."},
    {"role": "user", "content": "I can't sign in."},
    {"role": "assistant", "content": "What error do you see?"},
    {"role": "user", "content": "It says my password is incorrect."}
  ],
  "response": [
    {"role": "assistant", "content": "Use the password-reset link on the sign-in page."}
  ]
}
```

When string `query` and `response` values need separate supporting information, add a `context` column.

If an evaluation run calls a model or agent target, Foundry generates a new response for each input. Any `response` already stored in the row is ignored.

CSV is also supported for simple string-based `query` and `response` rows. See [Evaluate a CSV dataset](cloud-evaluation-datasets#evaluate-a-csv-dataset).

## When you need a data mapping

You can omit `data_mapping` when a compatible evaluator uses the standard columns in your dataset. Add a mapping in the following cases:

- Your dataset uses a different name, such as `question` instead of `query`.
- A model or agent target generates text at run time and the evaluator requires a text response. For example, Coherence requires the response to map from `{{sample.output_text}}`.
- An agent target generates structured output and the evaluator requires tool calls or other structured items. For example, Task Adherence requires the response to map from `{{sample.output_items}}`.
- A CSV file uses nonstandard column headers.

For `{{item.*}}` and `{{sample.*}}` mapping syntax with runnable examples, see [Set up evaluators and data mappings](cloud-evaluation-targets#set-up-evaluators-and-data-mappings). To choose an overall workflow, see [Run evaluations from the SDK](cloud-evaluation).