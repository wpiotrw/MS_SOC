---
layout: Conceptual
title: Add a human-in-the-loop approval step (preview) - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-human-in-the-loop
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
description: Pause a long-running hosted agent indefinitely for human approval or input, then resume the conversation from where it left off.
ms.manager: mcleans
ms.date: 2026-08-05T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 0e36173d-492b-a5a9-b278-851ec7175679
document_version_independent_id: 2f6bbf81-e6cc-f2be-55b4-a5a20d6b814d
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/add-human-in-the-loop.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/add-human-in-the-loop
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/add-human-in-the-loop.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/0850fefd-e402-4507-ae98-46cfdfc2e16c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/6ecf98a5-97c7-4249-b209-a9d9e42633a0
platformId: b084ab00-d3d0-3152-14df-ac9d9dab5d0f
---

# Add a human-in-the-loop approval step (preview) - Microsoft Foundry | Microsoft Learn

Some agent workflows must stop and wait for a person - to approve an action, answer a question, or provide missing input - and then continue. A [long-running hosted agent](../concepts/long-running-agent-resilience) can pause indefinitely for that reply without holding a request open or losing its place, because a multi-turn chain persists between turns.

Note

Long-running agents are in preview. APIs and package versions are subject to change.

## How pause-and-resume works

A `@multi_turn_task` chain doesn't end when a turn returns - it moves to the `suspended` state and stays alive under one `task_id`. The next input on the same `task_id` reenters the same handler with `ctx.entry_mode == "resumed"`. That is the natural shape for a human-in-the-loop pause:

1. The agent does work until it needs a human decision.
2. It returns a turn that asks for the decision (the chain suspends).
3. A person replies; your app starts a new turn on the same `task_id`.
4. The handler resumes and continues with the human's answer.

Because the chain is durable, the wait can be arbitrarily long - minutes, hours, or days - and survives container restarts.

## Implement the approval turn

```python
from azure.ai.agentserver.core.tasks import multi_turn_task, TaskContext

@multi_turn_task(name="expense-approval")
async def approve(ctx: TaskContext[dict]) -> dict:
    if ctx.entry_mode == "resumed":
        # We're back with the human's decision.
        decision = ctx.input["decision"]
        if decision == "approved":
            await submit_expense(ctx.metadata["expense_id"])
            return {"status": "submitted"}
        return {"status": "rejected"}

    # First turn: prepare the request and ask for a decision.
    expense = await build_expense(ctx.input)
    ctx.metadata["expense_id"] = expense.id          # small watermark, survives the pause
    return {"status": "awaiting_approval", "summary": expense.summary}
```

Drive it from your application:

```python
# Turn 1 - agent produces an approval request, then the chain suspends.
r1 = await approve.run(task_id="exp-42", input={"amount": 1200, "category": "travel"})
# ... show r1["summary"] to a human and wait for their reply (could be much later) ...

# Turn 2 - same task_id resumes the suspended chain.
r2 = await approve.run(task_id="exp-42", input={"decision": "approved"})
```

Tip

Keep only small references in `ctx.metadata` (an expense ID, a step number). Store the full request, history, or generated artifacts in your own storage or a framework checkpoint. See [Manage state for long-running agents](manage-task-state).

## Use a framework interrupt with Responses

If you build on an agent framework (for example, LangGraph or Microsoft Agent Framework) over a background response, use the framework's own interrupt and approval mechanism. Keep the response resilient so the pause survives a restart. Set `resilient_background=True` and persist the framework's checkpoint at the interrupt point. On resume, rebuild from that checkpoint. See [Recover long-running work after a crash](recover-long-running-work).

## Clean up a finished chain

You delete a suspended chain only when you delete it explicitly. The system automatically cleans up one-shot `@task` records when they complete.

```python
await approve.delete("exp-42")
```