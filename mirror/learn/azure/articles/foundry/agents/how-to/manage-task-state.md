---
layout: Conceptual
title: Manage state for long-running agents (preview) - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-task-state
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
description: Keep durable progress for a hosted agent by storing progress markers, checkpoints, and framework recovery state in the Foundry state store.
ms.manager: mcleans
ms.date: 2026-09-04T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 3f4fb674-6462-c497-3681-01a36cbc5984
document_version_independent_id: 06c6abf6-6968-46a0-aae8-1076162ad70c
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/manage-task-state.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/manage-task-state
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/manage-task-state.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/062d60c9-ee0f-402e-a046-b4e67c3572d6
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/17d3b3f6-a66e-4c69-9774-14a73c38e669
platformId: 726bad1f-22ae-9cf4-f89c-eb9e6c6268bb
---

# Manage state for long-running agents (preview) - Microsoft Foundry | Microsoft Learn

A [long-running hosted agent](../concepts/long-running-agent-resilience) recovers from crashes only if its progress is durable. This article shows how to keep progress markers and checkpoints in the Foundry state store, and how to back a framework checkpointer so framework-level recovery survives restarts.

Note

Long-running agents are in preview. APIs and package versions are subject to change.

## Store progress and checkpoints

`FoundryStateStore` is a durable, server-backed key-value store for state that must survive crashes and idle eviction. Keep progress markers and checkpoints in separate items so a recovered attempt can identify both the next step and the results already written.

| Item | What it holds | Write pattern |
| --- | --- | --- |
| Progress marker | The next workflow step or another small resume position. | Update a stable key with the ETag from the last read. |
| Checkpoint | A completed step result, generated artifact, or serialized framework state. | Create an item with a deterministic, append-only key. |

A store is bound to one caller-chosen name. Encode the workflow, session, thread, or run scope in that name. For the full store surface, see [Durable state store for hosted agents](../concepts/agent-state-store).

```python
from azure.ai.agentserver.core.storage import FoundryStateStore

async def save_step(task_id: str, step: int, result: dict) -> None:
    store = await FoundryStateStore.get_or_create(f"workflows/{task_id}")
    async with store:
        progress = await store.get_item("progress")
        if progress and int(progress.value["workflow_step"]) > step:
            return

        checkpoint_key = f"checkpoints/{step}"
        checkpoint = await store.get_item(checkpoint_key)
        if checkpoint is None:
            await store.create_item(f"checkpoints/{step}", result)
        elif checkpoint.value != result:
            raise RuntimeError("The checkpoint contains a different result.")

        next_progress = {"workflow_step": step + 1}
        if progress is None:
            await store.create_item("progress", next_progress)
        else:
            await store.set_item(
                "progress", next_progress, if_match=progress.etag
            )
```

Write the checkpoint before you advance the progress marker. If the process fails between those writes, the deterministic checkpoint key lets the recovered attempt detect the completed write. On a `409 Conflict` or `412 Precondition Failed` response, reread the items and reconcile the existing checkpoint before you retry.

Key behaviors:

- **`get_or_create()`** fetches or creates the store in one call. It applies `user_isolation` and `item_ttl_seconds` only on first creation.
- **Store name = scope.** Names can contain `/`; use it as a hierarchy separator and choose a stable scheme up front.
- **Optimistic concurrency.** Use `if_match=item.etag` for mutable items such as progress markers. Use `create_item()` for append-only checkpoints so a competing write doesn't overwrite an existing value.
- **Limits.** An item value can contain up to 1 MB of serialized JSON. A store name can contain 1 through 128 characters, and an item can have up to 16 tags.

## Back a framework checkpointer

Point a LangGraph or Microsoft Agent Framework (MAF) checkpointer at `FoundryStateStore` and the framework's own recovery becomes durable across crashes - no custom recovery code.

| Framework concept | FoundryStateStore |
| --- | --- |
| Thread / scope | Store name (encode the ID into it) |
| Checkpoint ID | Item key |
| Serialized checkpoint | Item value (JSON `dict`) |
| "latest" / history / filtering | Tags + `list_keys(order="desc")` |
| Per-user safety | `user_isolation=True` |

Checkpoints are append-only - each save uses a fresh ID, so there's no write contention and you never need `if_match` on the checkpoint path.

```python
# LangGraph: one thread = one store
async def _store(thread_id: str) -> FoundryStateStore:
    return await FoundryStateStore.get_or_create(
        f"langGraphCheckpoints/{thread_id}", user_isolation=True
    )
```

Warning

For the MAF adapter, always set `user_isolation=True`. MAF's only grouping is `workflow_name` - a definition name shared across users - so without user isolation, `get_latest` / `list_checkpoints` would return other callers' checkpoints.

## Keep inputs small

Task inputs are persisted before the handler runs (that's what recovery rests on), so keep them small - the per-input limit is about 10 MiB after JSON serialization, and larger inputs raise `InputTooLarge` before any network call. Externalize big payloads to blob storage and pass a reference.