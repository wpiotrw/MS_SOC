---
layout: Conceptual
title: Deploy a steerable agent (preview) - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-steerable-agent
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
author: aahill
learn_banner_products:
- azure
manager: mcleans
ms.author: aahi
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Deploy a hosted agent that accepts a new instruction mid-run, cooperatively winding down the in-flight turn and continuing with the redirected input.
ms.manager: mcleans
ms.date: 2026-08-20T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: references_regions, doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 11931065-6b4b-ed04-a134-32b574ba72b5
document_version_independent_id: 5eb3601d-d9c7-5837-bce8-734e1bc6cd9b
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/deploy-steerable-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/deploy-steerable-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/deploy-steerable-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: 0b828dd0-3d5f-a969-dd26-38971f8a68b4
---

# Deploy a steerable agent (preview) - Microsoft Foundry | Microsoft Learn

In this article, you deploy a [long-running hosted agent](../concepts/long-running-agent-resilience) that supports *steering*: when a second turn arrives on the same conversation while the first turn is still running, the platform queues the new turn and cooperatively cancels the current one instead of rejecting it with `409 conversation_locked`.

The sample is a Responses protocol agent that turns on resilience and steering with two options. It uses a simulated model stream, so you can run it without model credentials.

Note

Long-running agents are in preview. APIs and package versions are subject to change.

## Prerequisites

- An Azure subscription with Microsoft Foundry access.
- [Python 3.13](https://www.python.org/downloads/).
- The [Azure Developer CLI (`azd`)](/en-us/azure/developer/azure-developer-cli/install-azd) with the Foundry agents extension (`azd extension install azure.ai.agents`), version `azd-ext-azure-ai-agents_1.0.0-beta.16` or later for the `--long-running` invoke flag and the `invocations` lifecycle commands. `azd` handles authentication when it calls the deployed agent.

## Get the sample

In an empty directory, initialize the resilient steering agent from its `azure.yaml` manifest:

```bash
azd auth login
azd ai agent init -m https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/bring-your-own/responses/resilient-steering/azure.yaml
```

The command downloads the sample source, adopts its `azure.yaml`, creates an azd environment, and connects it to the Foundry project you select.

The agent enables resilience and steering when it constructs the host:

```python
options = ResponsesServerOptions(
    resilient_background=True,
    steerable_conversations=True,
)
app = ResponsesAgentServerHost(options=options)
```

By using `steerable_conversations=True`, a second turn on a busy conversation is queued and the running handler is cooperatively cancelled, rather than returning `409 conversation_locked`.

## Provision and deploy

Provision the project and deploy the agent. When prompted for a location, choose a [region that supports hosted agents](../concepts/hosted-agents#region-availability).

```bash
azd up
```

`azd up` prints the Responses endpoint and a playground link.

## Steer the deployed agent

Steering redirects an in-flight turn, so the first turn must keep running while you send the second. Start the first turn as a long-running background response in a fresh conversation, and return immediately with `--no-wait`:

```bash
azd ai agent invoke --long-running --no-wait --new-session "Explain quantum computing in detail, including its history, principles, algorithms, hardware, error correction, and applications."
```

`--long-running` sends `store=true` and `background=true`, and `azd ai agent invoke` reuses that conversation on your next invocation by default. While the first turn is still running, send a new instruction to steer the in-flight turn. Omit `--no-wait` this time so the CLI stays attached and streams the steered turn through completion:

```bash
azd ai agent invoke --long-running "Instead, explain relativity and focus on practical examples."
```

The first turn observes the queued input and winds down at its next safe point. The queued turn then streams to completion in your terminal, so you can watch the handoff. To replay a specific response by ID instead, use `azd ai agent invocations follow --id <response-id>`.

## Clean up

```bash
azd down
```