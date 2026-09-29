---
layout: Conceptual
title: Customer-Managed Key Encryption in Microsoft Foundry - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/concepts/customer-managed-keys
breadcrumb_path: ../../breadcrumb/azure-ai/toc.json
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
author: s-polly
learn_banner_products:
- azure
manager: mcleans
ms.author: scottpolly
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Learn how customer-managed keys (CMKs) encrypt your data in Microsoft Foundry, which capabilities and compute layers they cover, and the effect of key revocation.
ms.reviewer: deeikele
ms.date: 2026-08-24T00:00:00.0000000Z
ms.topic: concept-article
ms.custom:
- doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 52bce9d1-a43c-2cbd-3ec6-510bb5d3cd61
document_version_independent_id: 490e9e67-0f17-5412-c658-52cb41f44558
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/concepts/customer-managed-keys.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../toc.json
asset_id: foundry/concepts/customer-managed-keys
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/concepts/customer-managed-keys.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 34f36788-a09d-5881-5260-09ef1d495371
---

# Customer-Managed Key Encryption in Microsoft Foundry - Microsoft Foundry | Microsoft Learn

Microsoft Foundry automatically encrypts your data when it persists to the cloud. To add an extra layer of control, Foundry supports customer-managed keys (CMKs) that use keys stored in Azure Key Vault or Azure Managed HSM. CMKs provide an extra encryption layer that gives you control over key lifecycle operations such as rotation, revocation, and auditing.

To configure CMK encryption for your resource, see [Configure customer-managed keys for Microsoft Foundry](encryption-keys-portal).

Note

Due to capacity constraints in the underlying Azure AI Search infrastructure, CMK encryption is currently available only in select regions. For the list of supported regions, see [Azure AI Search regional availability](/en-us/azure/search/search-region-support#americas).

## About Microsoft Foundry encryption

Microsoft Foundry data is encrypted and decrypted by using [FIPS 140-2](https://en.wikipedia.org/wiki/FIPS_140-2) compliant [256-bit AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) encryption. Encryption and decryption are transparent, which means encryption and access are managed for you. Your data is secure by default, and you don't need to modify your code or applications to take advantage of encryption.

Important

CMK enforcement is subject to limitations. The following sections outline supported scenarios, exceptions, and configuration-specific considerations.

## How CMK applies in Microsoft Foundry

By default, the service stores data and resource state in Microsoft-managed service infrastructure and encrypts it by using Microsoft-managed keys. When you configure CMKs, the service encrypts eligible service data that it stores by using keys that you control.

Examples of encrypted data include:

- Project assets, such as agents, prompts, datasets, and evaluations.
- Uploaded files, such as files uploaded for a fine-tuning training job as a dataset or through OpenAI Files APIs.
- User state, such as conversation history, system prompts, and fine-tuned models.
- Indexed representations of the preceding data that enable in-product querying.

Important

Depending on your Foundry resource configuration, the service might store service state on managed storage that's part of the Foundry resource or on storage that you manage. Support differs by Foundry capability. Some capabilities don't support customer-managed key encryption unless you bring your own storage. For details, see CMK coverage by Foundry capability.

## CMK coverage by Foundry capability

| Foundry capability | CMK on Foundry-managed storage | CMK on customer-managed storage | Notes |
| --- | --- | --- | --- |
| Prompt Agents | ❌ Not supported | ✅ Supported | Basic setup uses Microsoft-managed keys. For CMK, use bring-your-own resources and configure CMK separately on Azure Cosmos DB, Storage, and AI Search. |
| Hosted Agents | ❌ Not supported | ◐ Partial | Basic setup uses Microsoft-managed keys. For CMK, use bring-your-own resources and configure CMK separately on Azure Cosmos DB, Storage, and AI Search. Hosted-agent sandbox compute is ephemeral, but each session has a persistent $HOME filesystem. $HOME is backed by platform-managed storage, and isn't encrypted using CMK, and can't currently be disabled. For more information, see: CMK coverage across the compute stack. |
| Fine-tuning | ✅ Supported | **N/A** (no bring-your-own storage support) | Uploaded files and trained fine-tuned models are CMK-encrypted on Microsoft-managed storage accounts. Trained models are logically isolated by their Azure subscription. Model weights are CMK-unwrapped to instantiate model deployments. For details about the compute stack and training runtime, see CMK coverage across the compute stack. |
| Batch jobs | ✅ Supported | ✅ Supported | Uploaded files are CMK-encrypted at rest on Microsoft-managed storage accounts. During the scoring job, this storage account is virtually mounted on the compute nodes for processing. For details about the compute stack used for batch job execution, see CMK coverage across the compute stack. |
| Evaluations | ✅ Supported | ✅ Supported | Evaluation assets and uploaded files stored by Foundry are CMK-protected. For details about the compute stack used for evaluation jobs, see CMK coverage across the compute stack. |
| Hugging Face models deployed on managed compute | **N/A** (weights are stored on Microsoft-managed public registries) | **N/A** (weights can't be stored on your own storage) | For Hugging Face models available through Foundry, [model weights are stored on Azure Storage](../foundry-models/how-to/hugging-face-models) managed by Microsoft. For details about the compute stack and hosting runtime, see CMK coverage across the compute stack. |
| Speech | ❌ Not supported | ✅ Supported | Covers uploaded training and test data that uses Azure AI Speech, batch transcriptions, real-time transcription with audio and result logging, and custom speech. Trace data is covered only if tracing is enabled for the custom endpoint. |
| Language | ✅ Supported | ✅ Supported | Data and model weights are stored with Microsoft-managed or Customer-Managed keys for cases where you don't bring your own storage account. |
| Content Understanding | **N/A** | ✅ Supported | Bring your own storage is required to use the Content Understanding capability. |
| OpenAI Assistants (deprecated) | ❌ Not supported | **N/A** | This feature is deprecated and didn't support CMK in preview. |
| Connected services, including Azure AI Search, Azure Logic Apps, and Azure Functions | **N/A** | **N/A** | Configure encryption keys separately from your Foundry resource. Every connected resource follows its own lifecycle for encryption management. |

## CMK coverage across the compute stack

Customer-managed keys protect customer data that Microsoft Foundry persists at rest. Foundry capabilities rely on managed compute infrastructure for model hosting, inference processing, fine-tuning, batch inference, and other runtime operations.

It's important to distinguish between:

- **Persistent data stores**, where customer content is stored and CMK is enforced at rest.
- **Runtime compute infrastructure**, which runs AI workloads for processing. Data is CMK-unwrapped for processing and CMK-wrapped when it's written back to persistent data storage.

Compute resources used for inference, model hosting, training, and batch processing are *ephemeral by design*. Job containers and temporary storage are provisioned only for the duration required to run a workload, and they aren't intended as long-term storage locations for customer data. Memory and disk space are cleaned up after compute job execution completes. When compute pods are terminated, all ephemeral state is cleaned.

Microsoft Foundry workloads run in logically isolated environments associated with a specific Foundry resource. Customer code, agent execution, and workload runtimes don't share execution containers with other tenants. Runtime caching that improves performance is isolated at the tenant or resource boundary and isn't shared across customers.

As a result, CMK coverage focuses on protecting customer data that's persisted in storage services and platform-managed data stores. Runtime compute infrastructure is protected through Microsoft's platform-managed encryption, workload isolation, and tenant-isolation controls.

| Layer | Examples | Ephemeral | Data lifecycle | CMK enforced |
| --- | --- | --- | --- | --- |
| Persistent data stores | Foundry-managed storage or Azure Storage accounts that you manage | No | Retained until deleted by you, a retention policy, or resource deletion | ✅ Yes |
| Foundry artifacts | Project assets, user state, service metadata | No | Persist until deleted by you or the associated resource | ✅ Yes |
| Fine-tuning model hosting infrastructure | Model-serving clusters, containers, endpoint infrastructure | Yes | CMKs protect files and model artifacts at rest in storage. During deployment, model weights are unwrapped and loaded into Microsoft-managed serving infrastructure for inference, and then removed when the deployment is deleted. | ◐ Partial |
| Managed compute model hosting infrastructure | Model-serving clusters, containers, endpoint infrastructure | Yes | Model weights are stored in Foundry-managed storage and instantiated into memory when model-serving instances are provisioned. The in-memory copies are transient and tied to the lifecycle of the serving infrastructure. Compute cache isn't encrypted and is tied to the node lifecycle. | ◐ Partial |
| Inference and agent execution runtime | Prompt execution, token generation, tool calls, runtime memory, temporary execution state, caches | Partial | Stateless in the context of inference request processing. Workloads run in logically isolated environments associated with a Foundry resource and aren't used as durable storage locations. Agent response outputs, such as conversations, can be CMK-encrypted at rest if you bring your own storage. | ◐ Partial (when you bring your own storage) |
| Hosted agent execution runtime | Per-session sandbox root disk, `$HOME` data volume, session state | Partial | Each compute node has an ephemeral root disk for the sandbox, which lasts up to 24 hours, and a `$HOME` data volume backed up by Microsoft-managed storage. The lifetime of `$HOME` is tied to the session: the platform deletes the sandbox after the idle timeout but retains `$HOME` state for 30 days unless you delete the session. CMK and bring-your-own storage aren't currently supported, and `$HOME` folder can't be disabled. | ❌ No |
| Fine-tuning training runtime | Fine-tuning compute, GPUs, temporary working directories | Yes | Training data is encrypted with CMK while stored in Foundry-managed storage. During training, data is mounted from CMK-protected Azure Storage, and checkpoints and final model artifacts are written back to CMK-protected storage. Training creates temporary, job-local working files and caches that aren't CMK-encrypted and remain only for the duration of the job. | ◐ Partial |

## Data retention and deletion

In addition to encryption controls, you retain control over the lifecycle of data managed by Microsoft Foundry. You can delete training, validation, and training results data uploaded through the Files API at any time. Similarly, you can permanently delete fine-tuned models and deployments when you no longer need them, which ensures that service-managed assets don't remain stored beyond their intended use. You can delete this data at any time through the appropriate DELETE API operations.

## Implications of revoking a customer-managed key

You can revoke access to a customer-managed key at any time, for example by removing permissions to the key, disabling the key, or deleting the key. When you revoke access to an active customer-managed key while CMK remains enabled, you can no longer access data encrypted with that key. As a result, operations that require access to encrypted fine-tuning assets fail, including downloading training data or training results, creating new fine-tuned models, and deploying fine-tuned models.

Previously deployed fine-tuned models continue to serve inference traffic because model artifacts are loaded into the hosting infrastructure at deployment time. These deployments remain operational until they're deleted, after which they can't be recreated unless you restore access to the customer-managed key.