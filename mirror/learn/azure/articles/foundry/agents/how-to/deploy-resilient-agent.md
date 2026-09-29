---
layout: Conceptual
title: Deploy a crash-resilient long-running agent (preview) - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-resilient-agent
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
description: Deploy a long-running hosted agent that keeps working with no client traffic, survives a container crash, and resumes from its last checkpoint.
ms.manager: mcleans
ms.date: 2026-08-20T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: references_regions, doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 6af65cb1-020a-d7d4-fc7f-30b795ebe3ed
document_version_independent_id: fb176302-7f70-1d2b-b938-9d249d6c8763
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/deploy-resilient-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/deploy-resilient-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/deploy-resilient-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: af76e441-ec6f-74f5-fc58-2aaed17a0ee7
---

# Deploy a crash-resilient long-running agent (preview) - Microsoft Foundry | Microsoft Learn

In this article, you deploy a [long-running hosted agent](../concepts/long-running-agent-resilience) that uses the Responses protocol and the resilient background response feature. You run a stored background response, crash the agent process on purpose, and watch it resume from the last checkpoint after restart.

The agent runs three simulated streamed stages: analyze, generate, and refine. Each completed stage is one checkpointed output item, so a recovered run repeats at most one stage.

Note

Long-running agents are in preview. APIs and package versions are subject to change.

## Prerequisites

- An Azure subscription with Microsoft Foundry access.
- [Python 3.13](https://www.python.org/downloads/).
- The [Azure Developer CLI (`azd`)](/en-us/azure/developer/azure-developer-cli/install-azd) with the Foundry agents extension (`azd extension install azure.ai.agents`), version `azd-ext-azure-ai-agents_1.0.0-beta.16` or later for the `--long-running` invoke flag and the `invocations` lifecycle commands.
- [`curl`](https://curl.se/) for the local crash-recovery step. The deployed agent is called with `azd`, which handles authentication for you.

## Get the sample

In an empty directory, initialize the resilient streaming agent from its `azure.yaml` manifest:

```bash
azd auth login
azd ai agent init -m https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/bring-your-own/responses/resilient-streaming/azure.yaml
```

The command downloads the sample source, adopts its `azure.yaml`, creates an azd environment, and connects it to the Foundry project you select.

The sample opts in to resilience when it creates the host:

```python
# src/resilient-streaming/main.py
options = ResponsesServerOptions(resilient_background=True)
app = ResponsesAgentServerHost(options=options)
```

Important

`resilient_background` defaults to `False`. Without it, a background response that crashes is marked `failed` instead of being recovered. See [Recover long-running work after a crash](recover-long-running-work).

## Run it locally

The resilient state store uses files when you run it locally, so your machine uses the same recovery code path. The local crash-recovery walkthrough drives the agent with `curl`, so every local run uses `azd ai agent run --no-client`, which installs the Python dependencies, injects the active azd environment, and starts the agent on `http://localhost:8088` without launching Agent Inspector.

## Test crash recovery locally

Use Linux, WSL2, or a container for this exercise so the operating system releases the file lock when the process exits.

Set `SIMULATE_CRASH_AFTER_STAGE` so the sample crashes after it checkpoints the first stage, and then start the agent:

```bash
SIMULATE_CRASH_AFTER_STAGE=0 azd ai agent run --no-client
```

Recovery needs a stored background response (`store: true` and `background: true`). In a second terminal, send the request inline with `curl`:

```bash
curl -sS -X POST http://localhost:8088/responses \
  -H "Content-Type: application/json" \
  -d '{"input": "renewable energy supply chains", "store": true, "background": true}'
```

The agent checkpoints the analyze stage and then exits. Restart it from the first terminal:

```bash
azd ai agent run --no-client
```

The framework reinvokes the handler with `context.is_recovery == True`. The handler restores `context.persisted_response`, skips the checkpointed analyze stage, and completes the generate and refine stages.

## Deploy to Foundry

Provision the project and deploy the agent. When prompted for a location, choose a [region that supports hosted agents](../concepts/hosted-agents#region-availability).

```bash
azd up
```

`azd up` prints the Responses endpoint and a playground link.

## Invoke the deployed agent

Create a stored background response with `--long-running`, and return as soon as the platform assigns its ID with `--no-wait`:

```bash
azd ai agent invoke --long-running --no-wait "renewable energy supply chains"
```

`--long-running` sends `store=true` and `background=true`, so the platform keeps the response running with no client traffic. `azd ai agent invoke` resolves the deployed endpoint, authenticates for you, and saves the returned response ID as the current invocation.

Check the response, or replay its output from the beginning, with the saved ID:

```bash
azd ai agent invocations show
azd ai agent invocations follow
```

Pass `--id <response-id>` to target a specific response. For the reconnect protocol and the `starting_after` cursor, see [Stream with reconnect](stream-with-reconnect).

## Clean up

```bash
azd down
```