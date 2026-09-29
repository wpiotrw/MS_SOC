---
layout: Conceptual
title: Steer an in-flight agent turn (preview) - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/steer-hosted-agent
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
description: Let a new input redirect a hosted agent's in-flight turn instead of racing or rejecting it, using steerable conversations and the steering queue.
ms.manager: mcleans
ms.date: 2026-08-05T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 7fde98f3-f106-8739-9d49-6e79ce99897a
document_version_independent_id: 2fc3184b-8ac9-ab6f-12e9-80489fc8e5dd
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/steer-hosted-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/steer-hosted-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/steer-hosted-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 1d268493-c2e8-9216-86a4-f94d3eaf9d05
---

# Steer an in-flight agent turn (preview) - Microsoft Foundry | Microsoft Learn

*Steering* lets you redirect a [long-running hosted agent](../concepts/long-running-agent-resilience) while it's still working. A new input queues behind the active turn and the running handler cooperatively winds down. This approach avoids rejecting the new turn or racing two turns at once.

Note

Long-running agents are in preview. APIs and package versions are subject to change.

## Turn on steering

### Responses protocol

Set `steerable_conversations=True` on `ResponsesServerOptions`:

```python
app = ResponsesAgentServerHost(
    options=ResponsesServerOptions(steerable_conversations=True),
)
```

A second turn that arrives on a busy conversation queues and the current handler cooperatively cancels. This approach avoids returning `409 conversation_locked`. Send the follow-up as a new response with `previous_response_id` set to the running response and the same `agent_session_id`.

### Invocations and task primitives

Pass `steerable=True` to `@multi_turn_task`:

```python
@multi_turn_task(name="conv", steerable=True)
async def conv(ctx: TaskContext[dict]) -> dict:
    return await llm(ctx.input)

# A .start() against an in-flight chain queues instead of raising.
r1 = asyncio.create_task(conv.start(task_id="c1", input={"msg": "Plan a trip to Rome"}))
await asyncio.sleep(0.05)
r2 = asyncio.create_task(conv.start(task_id="c1", input={"msg": "Actually, Paris"}))
# r1 resolves with turn 1's outcome; r2 resolves with turn 2's outcome.
```

Without `steerable=True`, a concurrent `.start()` on an in-flight chain raises `TaskConflictError`.

## Wind down the active turn

When something is queued, the framework signals the running handler through the cooperative cancel signal. A steerable handler should check for it at safe boundaries and return early so the queued turn can take over:

```python
@multi_turn_task(name="conv", steerable=True)
async def conv(ctx: TaskContext[dict]) -> dict:
    for step in plan:
        if ctx.cancel.is_set() and ctx.pending_input_count > 0:
            # A newer turn is waiting - stop at this boundary and let it run.
            return partial_result
        await do_step(step)
    return final_result
```

Steering observability on the context:

| Field | Meaning |
| --- | --- |
| `ctx.is_steered_turn` | `True` if this turn was promoted from the queue. |
| `ctx.pending_input_count` | How many newer turns are currently queued. |
| `ctx.cancel` | Cooperative cancel signal; set when a queued turn is waiting. |

## Order turns with a precondition

When a client reasons about message ordering, pass `if_last_input_id` so a stale caller can't append after another caller has advanced the chain. It's the input-queue equivalent of an HTTP `If-Match`:

```python
await conv.start(task_id="c1", input=new_msg, if_last_input_id=prev_input_id)
```

If the chain's last accepted input no longer matches, the call raises `LastInputIdPreconditionFailed`.

## Handle a full queue

The steering queue is bounded. When it's full, an enqueue raises `SteeringQueueFull`; surface a clear "please wait" signal to the user rather than dropping the input silently:

```python
try:
    run = await conv.start(task_id="c1", input=new_msg)
except SteeringQueueFull:
    return {"status": "busy", "detail": "Too many pending turns; try again shortly."}
```

Steerable conversations are sequential, not forked: newer input can queue behind or interrupt the active turn, but the conversation still has one latest turn and one ordered history.