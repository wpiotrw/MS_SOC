---
layout: Conceptual
title: Microsoft Foundry reasoning models - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-chat-reasoning
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
zone_pivot_group_filename: zone-pivots/azure-ai/zone-pivot-groups.json
author: msakande
learn_banner_products:
- azure
manager: mcleans
ms.author: mopeakande
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Reasoning models in Microsoft Foundry solve complex problems step by step. Learn to call Foundry reasoning Models with the Chat Completions API and stream results.
ms.reviewer: achand
reviewer: achandmsft
ms.subservice: foundry-models
ms.topic: how-to
ms.date: 2026-08-26T00:00:00.0000000Z
zone_pivot_groups: azure-ai-inference-samples
ai-usage: ai-assisted
locale: en-us
document_id: a9de4533-cebd-2a81-8af0-3f8c0d65c72a
document_version_independent_id: f46f3855-943f-a034-54ee-7ea4d72afaf2
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/foundry-models/how-to/use-chat-reasoning.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/foundry-models/how-to/use-chat-reasoning
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/foundry-models/how-to/use-chat-reasoning.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: 14a62cb6-a0be-c661-8d26-3e718538adb3
---

# Microsoft Foundry reasoning models - Microsoft Foundry | Microsoft Learn

Reasoning models use extra computation to solve complex problems before returning an answer. This article shows how to call a non-OpenAI reasoning model, `DeepSeek-V4-Pro`, by using the OpenAI Chat Completions API from a Foundry project.

## Prerequisites

- An Azure subscription.
- A Foundry project. This kind of project is managed under a Foundry resource. If you don't have a Foundry project, see [Create a project for Microsoft Foundry](../../how-to/create-projects).
- Your Foundry project's endpoint URL, which is of the form `https://YOUR-RESOURCE-NAME.services.ai.azure.com/api/projects/YOUR_PROJECT_NAME`.
- A deployed reasoning model. This article uses `DeepSeek-V4-Pro`; replace the model name with your deployment name when necessary.
- The SDK or command-line tools for the language you select. For C#, use the .NET 10 SDK. The C# examples are tested with the `OpenAI` 2.13.0 and `Azure.Identity` 1.21.0 packages.
- Permission to access the project and model deployment. For keyless authentication, sign in with an identity that has the required Foundry project access.

## Use the AI model starter kit

The examples in the [AI model starter kit](https://aka.ms/ai-model-start) use standard OpenAI clients with a Foundry project endpoint and the `/openai/v1` path. The starter kit includes a complete example for a DeepSeek reasoning model. Its current samples use the Responses API. The examples in this article use Chat Completions for deployments that expose that API.

## Set up the client

Use Microsoft Entra ID to authenticate the OpenAI client. The token scope for the Foundry project endpoint is `https://ai.azure.com/.default`. The endpoint must be the project endpoint, not the resource endpoint, and the client base URL must append `/openai/v1`.

::: zone pivot="programming-language-python"

1. Install `openai` and `azure-identity` libraries.

    ```bash
    pip install --upgrade openai azure-identity
    ```
2. Use the following code to configure the OpenAI client object in the project route.

    ```python
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from openai import OpenAI
    
    project_endpoint = "https://<resource>.services.ai.azure.com/api/projects/<project>"
    token_provider = get_bearer_token_provider(
                  DefaultAzureCredential(), "https://ai.azure.com/.default"
    )
    client = OpenAI(
                  base_url=project_endpoint.rstrip("/") + "/openai/v1",
                  api_key=token_provider,
    )
    ```

::: zone-end

::: zone pivot="programming-language-javascript"

1. Install `openai` and `@azure/identity`.

    ```bash
    npm install openai @azure/identity
    ```
2. Use the following code to configure the OpenAI client object in the project route:

    ```javascript
    import OpenAI from "openai";
    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
    
    const projectEndpoint = "https://<resource>.services.ai.azure.com/api/projects/<project>";
    const tokenProvider = getBearerTokenProvider(
           new DefaultAzureCredential(), "https://ai.azure.com/.default"
    );
    const client = new OpenAI({
           baseURL: `${projectEndpoint.replace(/\/+$/, "")}/openai/v1`,
           apiKey: tokenProvider,
    });
    ```

::: zone-end

::: zone pivot="programming-language-java"

Add `openai-java` and `azure-identity` to your project, then configure the OpenAI client object in the project route. The following client pattern uses the OpenAI Java SDK and the Entra token provider:

```java
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.credential.BearerTokenCredential;
import com.azure.identity.AuthenticationUtil;

String projectEndpoint = "https://<resource>.services.ai.azure.com/api/projects/<project>";
OpenAIClient client = OpenAIOkHttpClient.builder()
              .baseUrl(projectEndpoint.replaceAll("/+$", "") + "/openai/v1")
              .credential(BearerTokenCredential.create(AuthenticationUtil.getBearerTokenSupplier(
                            new DefaultAzureCredentialBuilder().build(), "https://ai.azure.com/.default")))
              .build();
```

::: zone-end

::: zone pivot="programming-language-csharp"

1. Install the `OpenAI` and `Azure.Identity` packages:

    ```bash
    dotnet add package OpenAI --version 2.13.0
    dotnet add package Azure.Identity --version 1.21.0
    ```
2. Use the following code to configure the OpenAI client object in the project route.

    ```csharp
    using Azure.Identity;
    using OpenAI;
    using OpenAI.Chat;
    using System.ClientModel.Primitives;
    
    #pragma warning disable OPENAI001
    
    BearerTokenPolicy tokenPolicy = new(
                  new DefaultAzureCredential(), "https://ai.azure.com/.default");
    ChatClient client = new(
                  model: "DeepSeek-V4-Pro", // Replace with your deployment name, not the model ID 
                  authenticationPolicy: tokenPolicy,
                  options: new OpenAIClientOptions { Endpoint = new Uri(
                                "https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1") });
    ```

::: zone-end

::: zone pivot="programming-language-rest"

Get an Entra token for the `https://ai.azure.com/.default` scope and send it as a bearer token. No `api-version` query parameter is required for `/openai/v1`.

```bash
export AZURE_AI_AUTH_TOKEN="<entra-token>"
```

::: zone-end

## Create a basic chat completion

Send a user message to the deployed reasoning model. The response contains the final answer in `message.content`. Depending on the model, the response can also contain reasoning content in `message.reasoning_content`.

::: zone pivot="programming-language-python"

```python
response = client.chat.completions.create(
              model="DeepSeek-V4-Pro", # Replace with your deployment name, not the model ID
              messages=[{"role": "user", "content": "How many languages are spoken worldwide?"}],
)
print(response.choices[0].message.content)
print(getattr(response.choices[0].message, "reasoning_content", None))
```

::: zone-end

::: zone pivot="programming-language-javascript"

```javascript
const response = await client.chat.completions.create({
       model: "DeepSeek-V4-Pro", // Replace with your deployment name, not the model ID
       messages: [{ role: "user", content: "How many languages are spoken worldwide?" }],
});
console.log(response.choices[0]?.message.content);
console.log(response.choices[0]?.message.reasoning_content);
```

::: zone-end

::: zone pivot="programming-language-java"

```java
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
              .model("DeepSeek-V4-Pro") // Replace with your deployment name, not the model ID
              .addUserMessage("How many languages are spoken worldwide?")
              .build();
ChatCompletion response = client.chat().completions().create(params);
System.out.println(response.choices().get(0).message().content().orElse(""));
```

::: zone-end

::: zone pivot="programming-language-csharp"

```csharp
ChatCompletion response = await client.CompleteChatAsync([
              new UserChatMessage("How many languages are spoken worldwide?")
]);
Console.WriteLine(response.Content[0].Text);
```

::: zone-end

::: zone pivot="programming-language-rest"

```bash
curl -X POST "https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1/chat/completions" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer $AZURE_AI_AUTH_TOKEN" \
       -d '{
              "model": "DeepSeek-V4-Pro",
              "messages": [{"role": "user", "content": "How many languages are spoken worldwide?"}]
       }'
```

::: zone-end

## Read reasoning content

Some non-OpenAI reasoning models return a `reasoning_content` field alongside the final `content`. Reasoning content can be lengthy and counts toward token usage. Don't add it to the message history for a multi-turn conversation unless the model documentation specifically requires it. Store or display it only when your application needs it, and treat it as model output rather than a verified explanation.

For models that don't return `reasoning_content`, use the final `content` value. The field is model-dependent and isn't available for every reasoning model.

## Stream a completion

Set `stream` to `true` to receive server-sent events as the model generates output. Reasoning content and final answer content can arrive in different delta fields. The following examples print final answer content as it arrives.

::: zone pivot="programming-language-python"

```python
stream = client.chat.completions.create(
              model="DeepSeek-V4-Pro",
              messages=[{"role": "user", "content": "Explain photosynthesis briefly."}],
              stream=True,
)
for event in stream:
              if event.choices:
                            content = event.choices[0].delta.content
                            if content:
                                          print(content, end="", flush=True)
```

::: zone-end

::: zone pivot="programming-language-javascript"

```javascript
const stream = await client.chat.completions.create({
       model: "DeepSeek-V4-Pro",
       messages: [{ role: "user", content: "Explain photosynthesis briefly." }],
       stream: true,
});
for await (const event of stream) {
       const content = event.choices[0]?.delta?.content;
       if (content) process.stdout.write(content);
}
```

::: zone-end

::: zone pivot="programming-language-java"

```java
ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
              .model("DeepSeek-V4-Pro")
              .addUserMessage("Explain photosynthesis briefly.")
              .build();
client.chat().completions().createStreaming(params).stream()
              .flatMap(chunk -> chunk.choices().stream())
              .flatMap(choice -> choice.delta().content().stream())
              .forEach(System.out::print);
```

::: zone-end

::: zone pivot="programming-language-csharp"

```csharp
var stream = client.CompleteChatStreamingAsync([
              new UserChatMessage("Explain photosynthesis briefly.")
]);
await foreach (StreamingChatCompletionUpdate update in stream)
{
              foreach (ChatMessageContentPart part in update.ContentUpdate)
              {
                            Console.Write(part.Text);
              }
}
```

::: zone-end

::: zone pivot="programming-language-rest"

```bash
curl -N -X POST "https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1/chat/completions" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer $AZURE_AI_AUTH_TOKEN" \
       -d '{"model":"DeepSeek-V4-Pro","messages":[{"role":"user","content":"Explain photosynthesis briefly."}],"stream":true}'
```

::: zone-end

## Choose parameters for reasoning models

Reasoning models often don't support parameters that are common for other chat completion models, including `temperature`, `top_p`, `presence_penalty`, and `frequency_penalty`. Check the model details in the Foundry model catalog before adding optional parameters. Set a sufficient `max_completion_tokens` value because reasoning tokens and final answer tokens both count toward the limit.

Use short, direct prompts. Avoid asking the model to reveal a chain of thought. For multi-turn conversations, append the final answer instead of the reasoning content when the model returns both.

## Handle content safety responses

Foundry applies content filtering to supported deployments. A request or response can be blocked when it violates a configured content safety policy. Handle the `content_filter` finish reason and HTTP 400 errors in your application, show a useful message to the user, and don't retry the same blocked prompt unchanged.

```json
{
       "error": {
              "code": "content_filter",
              "message": "The response was filtered due to the prompt triggering a content policy."
       }
}
```

For configuration and control options, see [Azure AI Content Safety](https://aka.ms/azureaicontentsafety).

## About reasoning models

Reasoning models reach higher levels of performance in domains like math, coding, science, strategy, and logistics. These models explicitly use a chain of thought to explore all possible paths before generating an answer. They verify their answers as they produce them, which helps them arrive at more accurate conclusions. As a result, reasoning models might require fewer context prompts to produce effective results.

Reasoning models produce two types of content as outputs:

- Reasoning completions
- Output completions

Both of these completions count towards content generated from the model. Therefore, they contribute to the token limits and costs associated with the model. Some models, like `DeepSeek-V4-Pro`, might respond with the reasoning content. Others, like `o1`, output only the completions.

### Prompt reasoning models

When building prompts for reasoning models, take the following into consideration:

- Use simple instructions and avoid using chain-of-thought techniques.
- Built-in reasoning capabilities make simple zero-shot prompts as effective as more complex methods.
- When providing additional context or documents, like in RAG scenarios, including only the most relevant information might help prevent the model from over-complicating its response.
- Reasoning models may support the use of system messages. However, they might not follow them as strictly as other non-reasoning models.
- When creating multi-turn applications, consider appending only the final answer from the model, without its reasoning content.

Notice that reasoning models can take longer times to generate responses. They use long reasoning chains of thought that enable deeper and more structured problem-solving. They also perform self-verification to cross-check their answers and correct their mistakes, thereby showcasing emergent self-reflective behaviors.