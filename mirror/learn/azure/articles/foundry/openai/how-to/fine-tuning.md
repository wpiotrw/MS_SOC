---
layout: Conceptual
title: Fine-tune a model with supervised fine-tuning in Microsoft Foundry - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning
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
author: ssalgadodev
learn_banner_products:
- azure
manager: mcleans
ms.author: ssalgado
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Prepare supervised data, create and monitor an SFT job with the portal, SDK, REST, or Azure Developer CLI, and evaluate the resulting model.
ms.subservice: foundry-openai
ms.custom:
- build-2023, build-2023-dataai, devx-track-python, references_regions
- classic-and-new
- doc-kit-assisted
- dev-focus
ms.topic: how-to
ms.date: 2026-10-05T00:00:00.0000000Z
zone_pivot_groups: foundry-fine-tuning
ai-usage: ai-assisted
locale: en-us
document_id: cdec4712-107b-dace-9ce5-369f2e7e6ee1
document_version_independent_id: e76e8fd6-67be-5042-bc42-09e38d2dfe30
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/openai/how-to/fine-tuning.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/openai/how-to/fine-tuning
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/openai/how-to/fine-tuning.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/86a4b315-a9f1-4577-b985-6fb0e0e67420
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/96ac410d-d052-4707-8007-df31dd0fe041
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
platformId: 293c189d-2a2b-32d9-2855-a8567688e271
---

# Fine-tune a model with supervised fine-tuning in Microsoft Foundry - Microsoft Foundry | Microsoft Learn

Prepare your data and create a supervised fine-tuning (SFT) job in Microsoft Foundry. For method comparisons and training concepts, see the [fine-tuning overview](../../fine-tuning/overview).

## Prerequisites

- A Foundry resource or project with an [SFT-supported model and training region](../../fine-tuning/overview#supported-models).
- The **Foundry User** role for training, or the **Foundry Owner** role if you also deploy the fine-tuned model.

::: zone pivot="programming-language-python"

- The client packages and credentials described in the Python procedure.

::: zone-end

::: zone pivot="rest-api"

- Your resource endpoint and credentials, and a Bash-compatible shell for the REST examples.

::: zone-end

::: zone pivot="azd"

- [Azure Developer CLI](/en-us/azure/developer/azure-developer-cli/install-azd) version 1.22.1 or later.

::: zone-end

Important

The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.

## Prepare your data

Start with the [text-only GSM8K sample dataset on GitHub](https://github.com/microsoft-foundry/fine-tuning/tree/main/Sample_Datasets/Supervised_Fine_Tuning/Text-GSM8K), or prepare your own data.

Save separate `training.jsonl` and `validation.jsonl` files with one conversation per line. Include the prompt and the desired assistant response in each example:

```json
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the biggest city in France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}
```

Reference: [Chat Completions message format](chatgpt).

Check the data-format, file-size, and minimum-example requirements for your selected model. Keep validation and final test examples out of the training set.

For specialized data formats, see [vision fine-tuning](fine-tuning-vision) or [tool calling](fine-tuning-functions).

::: zone pivot="programming-language-studio"

## Create an SFT job in the portal

Use your prepared datasets to create the job:

1. Sign in to the [Foundry portal](https://ai.azure.com) and select your project.
2. Go to **Build** &gt; **Fine-tune**, and select **Fine-tune**.
3. Select a supported base model and **Supervised fine-tuning**.
4. Select a [training type](../../fine-tuning/overview#training-types) supported by your model and resource.
5. Select **Existing dataset** or **Upload new dataset** for the training and validation files. Inspect the preview and resolve validation errors.
6. Configure the available hyperparameters, such as **Batch size**, **Learning rate multiplier**, and **Number of epochs**. Keep your model's defaults for your first job. See the hyperparameter descriptions below.

### Configure hyperparameters

Hyperparameters control how the job updates the model during training. Available settings and accepted values depend on your selected model. Start with its defaults, and compare validation results before changing a setting.

::: zone pivot="programming-language-studio"

Review these common settings in the job configuration:

| Setting | Description |
| --- | --- |
| **Batch size** | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| **Learning rate multiplier** | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| **Number of epochs** | The number of complete passes through the training dataset. More passes give the model more opportunities to learn, but can increase overfitting. |

::: zone-end

::: zone pivot="programming-language-python,rest-api"

Set supported values under `method.supervised.hyperparameters` in the job body:

| Hyperparameter | Value | Description |
| --- | --- | --- |
| `batch_size` | Integer or `auto` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Number or `auto` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `n_epochs` | Integer or `auto` | The number of complete passes through the training dataset. More passes can improve learning, but can increase overfitting. |

The v1 examples use `auto` for service-selected values. If your model doesn't accept `auto`, use values supported by that model.

For the request schema, see the [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

::: zone-end

::: zone pivot="azd"

Configure supported settings in your SFT YAML file. The [CLI SFT sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/supervised/sample_finetuning_supervised.yaml) uses these names:

| Hyperparameter | Description |
| --- | --- |
| `batch_size` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `epochs` | The number of complete passes through the training dataset. This CLI configuration uses `epochs`, rather than the v1 API's `n_epochs`. |

Use the configuration sample for your selected model rather than copying settings from another model.

::: zone-end

Optionally, set a suffix to identify the resulting model. Review the configuration and select **Submit**. Retain the job ID.

::: zone-end

::: zone pivot="programming-language-python"

## Create an SFT job with Python

Initialize the client with the Microsoft Foundry SDK for your project, or use the OpenAI SDK with a resource endpoint. Both clients use the same upload and job commands below.

# [Foundry SDK](#tab/foundry-sdk)
Install `azure-ai-projects`, `azure-identity`, and `openai`. Sign in with a credential supported by `DefaultAzureCredential`, and set `FOUNDRY_PROJECT_ENDPOINT` to your project endpoint:

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
client = project.get_openai_client()
```

Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient) and [DefaultAzureCredential](/en-us/python/api/azure-identity/azure.identity.defaultazurecredential).

# [OpenAI SDK](#tab/oai-sdk)
Install `openai` and set `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` for your resource:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
```

Reference: [Azure OpenAI client configuration](../api-version-lifecycle#code-changes).

---

Set `FINE_TUNING_MODEL` to an identifier from [supported model IDs and versions](../../fine-tuning/overview#supported-models) that supports SFT with this API.

Set `FINE_TUNING_TRAINING_TYPE` to the API value for a supported [training type](../../fine-tuning/overview#training-types). For example, Global training uses `GlobalStandard`.

### Configure hyperparameters

Hyperparameters control how the job updates the model during training. Available settings and accepted values depend on your selected model. Start with its defaults, and compare validation results before changing a setting.

::: zone pivot="programming-language-studio"

Review these common settings in the job configuration:

| Setting | Description |
| --- | --- |
| **Batch size** | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| **Learning rate multiplier** | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| **Number of epochs** | The number of complete passes through the training dataset. More passes give the model more opportunities to learn, but can increase overfitting. |

::: zone-end

::: zone pivot="programming-language-python,rest-api"

Set supported values under `method.supervised.hyperparameters` in the job body:

| Hyperparameter | Value | Description |
| --- | --- | --- |
| `batch_size` | Integer or `auto` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Number or `auto` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `n_epochs` | Integer or `auto` | The number of complete passes through the training dataset. More passes can improve learning, but can increase overfitting. |

The v1 examples use `auto` for service-selected values. If your model doesn't accept `auto`, use values supported by that model.

For the request schema, see the [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

::: zone-end

::: zone pivot="azd"

Configure supported settings in your SFT YAML file. The [CLI SFT sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/supervised/sample_finetuning_supervised.yaml) uses these names:

| Hyperparameter | Description |
| --- | --- |
| `batch_size` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `epochs` | The number of complete passes through the training dataset. This CLI configuration uses `epochs`, rather than the v1 API's `n_epochs`. |

Use the configuration sample for your selected model rather than copying settings from another model.

::: zone-end

Upload `training.jsonl` and `validation.jsonl`, then submit the job. The example includes hyperparameters in the job body and uses `auto` to request service-selected values:

```python
import os

with open("training.jsonl", "rb") as training:
    training_file = client.files.create(file=training, purpose="fine-tune")
with open("validation.jsonl", "rb") as validation:
    validation_file = client.files.create(
        file=validation, purpose="fine-tune"
    )
client.files.wait_for_processing(training_file.id)
client.files.wait_for_processing(validation_file.id)

job = client.fine_tuning.jobs.create(
    model=os.environ["FINE_TUNING_MODEL"],
    training_file=training_file.id,
    validation_file=validation_file.id,
    suffix="my-model",
    method={
        "type": "supervised",
        "supervised": {
            "hyperparameters": {
                "batch_size": "auto",
                "learning_rate_multiplier": "auto",
                "n_epochs": "auto",
            }
        },
    },
    extra_body={
        "trainingType": os.environ["FINE_TUNING_TRAINING_TYPE"],
    },
)
print(job.id, job.status)
```

Reference: [Files API](/en-us/rest/api/azureopenai/files) and [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

Retain the returned job ID and continue to monitor the job.

::: zone-end

::: zone pivot="rest-api"

## Create an SFT job with REST

Set `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` for your resource. Run these commands in a Bash-compatible shell.

Upload each dataset with `purpose=fine-tune`, and retain the distinct file IDs:

```bash
curl -X POST "$AZURE_OPENAI_ENDPOINT/openai/v1/files" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -F "purpose=fine-tune" -F "file=@training.jsonl"

curl -X POST "$AZURE_OPENAI_ENDPOINT/openai/v1/files" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -F "purpose=fine-tune" -F "file=@validation.jsonl"
```

Reference: [Files API](/en-us/rest/api/azureopenai/files).

Replace `<SUPPORTED_MODEL_ID>` with an identifier from [supported model IDs and versions](../../fine-tuning/overview#supported-models) that supports SFT with this API.

Replace `<SUPPORTED_TRAINING_TYPE>` with the API value for a supported [training type](../../fine-tuning/overview#training-types). For example, Global training uses `GlobalStandard`.

### Configure hyperparameters

Hyperparameters control how the job updates the model during training. Available settings and accepted values depend on your selected model. Start with its defaults, and compare validation results before changing a setting.

::: zone pivot="programming-language-studio"

Review these common settings in the job configuration:

| Setting | Description |
| --- | --- |
| **Batch size** | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| **Learning rate multiplier** | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| **Number of epochs** | The number of complete passes through the training dataset. More passes give the model more opportunities to learn, but can increase overfitting. |

::: zone-end

::: zone pivot="programming-language-python,rest-api"

Set supported values under `method.supervised.hyperparameters` in the job body:

| Hyperparameter | Value | Description |
| --- | --- | --- |
| `batch_size` | Integer or `auto` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Number or `auto` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `n_epochs` | Integer or `auto` | The number of complete passes through the training dataset. More passes can improve learning, but can increase overfitting. |

The v1 examples use `auto` for service-selected values. If your model doesn't accept `auto`, use values supported by that model.

For the request schema, see the [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

::: zone-end

::: zone pivot="azd"

Configure supported settings in your SFT YAML file. The [CLI SFT sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/supervised/sample_finetuning_supervised.yaml) uses these names:

| Hyperparameter | Description |
| --- | --- |
| `batch_size` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `epochs` | The number of complete passes through the training dataset. This CLI configuration uses `epochs`, rather than the v1 API's `n_epochs`. |

Use the configuration sample for your selected model rather than copying settings from another model.

::: zone-end

Replace the file IDs and submit the job. The request includes hyperparameters in the job body and uses `auto` to request service-selected values:

```bash
curl -X POST "$AZURE_OPENAI_ENDPOINT/openai/v1/fine_tuning/jobs" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{
    "model": "<SUPPORTED_MODEL_ID>",
    "training_file": "<TRAINING_FILE_ID>",
    "validation_file": "<VALIDATION_FILE_ID>",
    "trainingType": "<SUPPORTED_TRAINING_TYPE>",
    "method": {
      "type": "supervised",
      "supervised": {
        "hyperparameters": {
          "batch_size": "auto",
          "learning_rate_multiplier": "auto",
          "n_epochs": "auto"
        }
      }
    },
    "suffix": "my-model"
  }'
```

Reference: [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

Retain the returned job ID and continue to monitor the job.

::: zone-end

::: zone pivot="azd"

## Create an SFT job with the Azure Developer CLI

Install [Azure Developer CLI](/en-us/azure/developer/azure-developer-cli/install-azd) version 1.22.1 or later, then install the fine-tuning extension and sign in:

```bash
azd ext install azure.ai.finetune
azd auth login
```

Reference: [Azure Developer CLI](/en-us/azure/developer/azure-developer-cli/).

Download an [SFT configuration sample and its data files](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/cli/finetuning/supervised) for your model. Set the model from [supported model IDs and versions](../../fine-tuning/overview#supported-models), and review the data paths and supported [training type](../../fine-tuning/overview#training-types).

### Configure hyperparameters

Hyperparameters control how the job updates the model during training. Available settings and accepted values depend on your selected model. Start with its defaults, and compare validation results before changing a setting.

::: zone pivot="programming-language-studio"

Review these common settings in the job configuration:

| Setting | Description |
| --- | --- |
| **Batch size** | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| **Learning rate multiplier** | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| **Number of epochs** | The number of complete passes through the training dataset. More passes give the model more opportunities to learn, but can increase overfitting. |

::: zone-end

::: zone pivot="programming-language-python,rest-api"

Set supported values under `method.supervised.hyperparameters` in the job body:

| Hyperparameter | Value | Description |
| --- | --- | --- |
| `batch_size` | Integer or `auto` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Number or `auto` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `n_epochs` | Integer or `auto` | The number of complete passes through the training dataset. More passes can improve learning, but can increase overfitting. |

The v1 examples use `auto` for service-selected values. If your model doesn't accept `auto`, use values supported by that model.

For the request schema, see the [v1 fine-tuning API](/en-us/rest/api/microsoft-foundry/azureopenai/fine-tuning).

::: zone-end

::: zone pivot="azd"

Configure supported settings in your SFT YAML file. The [CLI SFT sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/supervised/sample_finetuning_supervised.yaml) uses these names:

| Hyperparameter | Description |
| --- | --- |
| `batch_size` | The number of training examples processed together in one forward and backward pass. Larger batches produce less frequent updates with lower variance. |
| `learning_rate_multiplier` | Scales the training learning rate. A smaller multiplier can help reduce overfitting. |
| `epochs` | The number of complete passes through the training dataset. This CLI configuration uses `epochs`, rather than the v1 API's `n_epochs`. |

Use the configuration sample for your selected model rather than copying settings from another model.

::: zone-end

The following excerpt shows how to include hyperparameters in the job configuration. It uses values from the official CLI sample, not defaults for every model. Keep the rest of your model's configuration and adjust these values to its supported settings.

```yaml
model: <SUPPORTED_MODEL_ID>
method:
  type: supervised
  supervised:
    hyperparameters:
      epochs: 4
      batch_size: 8
      learning_rate_multiplier: 0.1
```

Reference: [SFT CLI configuration](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/supervised/sample_finetuning_supervised.yaml).

Replace `<SUPPORTED_MODEL_ID>` with your selected model ID. From the configuration directory, initialize the project, submit the complete job configuration, and inspect its status:

```bash
azd ai finetuning init -e <project-endpoint>
azd ai finetuning jobs submit -f <path-to-job-yaml>
azd ai finetuning jobs show -i <job-id>
```

Use a project endpoint in the form `https://<account>.services.ai.azure.com/api/projects/<project>`. Replace `<job-id>` with the ID returned by submission.

Reference: [Fine-tuning CLI samples and commands](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/README.md).

### Pause, resume, or cancel

Run lifecycle commands only when your model, method, and job state support them. Pause and resume aren't available for every model or method.

```bash
azd ai finetuning jobs pause -i <job-id>
azd ai finetuning jobs resume -i <job-id>
azd ai finetuning jobs cancel -i <job-id>
```

Reference: [Fine-tuning CLI commands](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/README.md).

::: zone-end

## Review training metrics

SFT measures how well the model predicts the target responses in your examples. Compare training and validation results rather than judging the model on training performance alone.

Metric availability depends on your model. Use the metrics reported for your job:

| Metrics | What to look for |
| --- | --- |
| Training loss. | Loss on the current training batch. Look for a decreasing trend. |
| Full validation loss. | Loss across the validation set at the end of an epoch. If training loss falls but validation loss rises, inspect failing validation examples. |
| Training mean token accuracy. | The fraction of target tokens correctly predicted in the training batch. Look for an increasing trend. |
| Full validation mean token accuracy. | Token accuracy across the validation set at the end of an epoch. Confirm that improvements also help your task. |

::: zone pivot="programming-language-python,rest-api"

The corresponding metric names are `train_loss`, `full_valid_loss`, `train_mean_token_accuracy`, and `full_valid_mean_token_accuracy`. Batch validation metrics, when reported, aren't the same as full-validation metrics.

::: zone-end

Compare the available checkpoints using validation metrics and held-out task results. Checkpoint creation and retention depend on the model and training workflow.

For explanations of overfitting and evaluation risks, see [challenges and limitations](../../fine-tuning/overview#challenges-and-limitations).

## Monitor the job and select a checkpoint

Inspect training progress before choosing a model or checkpoint to deploy.

::: zone pivot="programming-language-studio"

In the portal, open the job details:

1. Check the **Status** and event logs. Jobs can queue before training starts; inspect error details if a job fails.
2. Open **Monitor** to compare training and validation metrics using the guidance above.
3. Open **Checkpoints** to inspect available model versions and their metrics. Compare candidates on held-out tasks before choosing one to deploy.

::: zone-end

::: zone pivot="programming-language-python"

### Inspect logs and checkpoints with Python

Use the Python `client` from your submission example. Replace `<JOB_ID>` with your job ID. Repeat the status check until the job finishes; don't resubmit a queued job.

Retrieve the status, event logs, available checkpoints, and result-file IDs:

```python
job = client.fine_tuning.jobs.retrieve("<JOB_ID>")
print("Status:", job.status)
print("Error:", job.error)
print("Model:", job.fine_tuned_model)
print("Result files:", job.result_files)

for event in client.fine_tuning.jobs.list_events(job.id).data:
    print(event.created_at, event.message)

checkpoints = client.fine_tuning.jobs.checkpoints.list(job.id)
print(checkpoints.model_dump_json(indent=2))
```

Reference: [Fine-tuning API](/en-us/rest/api/azureopenai/fine-tuning).

After completion, if the job returns a CSV metrics file, replace `<RESULT_FILE_ID>` with its ID and download it:

```python
with open("results.csv", "wb") as result_file:
    result_file.write(client.files.content("<RESULT_FILE_ID>").read())
```

Reference: [Files API](/en-us/rest/api/azureopenai/files).

::: zone-end

::: zone pivot="rest-api"

### Inspect logs and checkpoints with REST

Use the resource endpoint and key for REST. Replace `<JOB_ID>` with your job ID. Repeat the status check until the job finishes; don't resubmit a queued job.

Retrieve the job, event logs, and available checkpoints:

```bash
JOB_URL="$AZURE_OPENAI_ENDPOINT/openai/v1/fine_tuning/jobs/<JOB_ID>"
curl "$JOB_URL" -H "api-key: $AZURE_OPENAI_API_KEY"
curl "$JOB_URL/events" -H "api-key: $AZURE_OPENAI_API_KEY"
curl "$JOB_URL/checkpoints" -H "api-key: $AZURE_OPENAI_API_KEY"
```

Reference: [Fine-tuning API](/en-us/rest/api/azureopenai/fine-tuning).

After completion, inspect `result_files` in the job response. If it includes a CSV metrics file, replace `<RESULT_FILE_ID>` with its ID and download it:

```bash
curl "$AZURE_OPENAI_ENDPOINT/openai/v1/files/<RESULT_FILE_ID>/content" \
  -H "api-key: $AZURE_OPENAI_API_KEY" --output results.csv
```

Reference: [Files API](/en-us/rest/api/azureopenai/files).

::: zone-end

::: zone pivot="azd"

Use the Azure Developer CLI job workflow to inspect the job status.

::: zone-end

Checkpoints appear as training progresses; a queued job might have none. Inspect the returned checkpoint identifiers and metrics rather than assuming the latest version performs best.

When training succeeds, retain the trained model or your chosen checkpoint. Compare candidates on held-out tasks before selecting one for deployment.

## Deploy the model

Use the Foundry portal to deploy the model, regardless of how you submit the training job. Follow [Deploy fine-tuned models](../../fine-tuning/deploy-fine-tuned-models) for your model's supported serving option and inference procedure.

::: zone pivot="programming-language-studio"

After deployment, use [Run evaluations from the Foundry portal](../../how-to/evaluate-generative-ai-app) to compare candidates on held-out tasks.

::: zone-end

::: zone pivot="programming-language-python"

For SDK evaluation, see [Cloud evaluation with the Microsoft Foundry SDK](../../observability/how-to/cloud-evaluation).

::: zone-end

## Stop training and clean up

::: zone pivot="programming-language-studio"

Cancel an unneeded job from its portal view. Delete uploaded files separately through the portal when you no longer need them.

::: zone-end

::: zone pivot="programming-language-python"

Cancel an unneeded job with `client.fine_tuning.jobs.cancel("<JOB_ID>")`. Delete unused uploaded files separately with `client.files.delete("<FILE_ID>")`.

Reference: [Job cancellation](/en-us/rest/api/azureopenai/fine-tuning/cancel) and [file deletion](/en-us/rest/api/azureopenai/files/delete).

::: zone-end

::: zone pivot="rest-api"

Cancel an unneeded job with the [fine-tuning cancellation API](/en-us/rest/api/azureopenai/fine-tuning/cancel). Delete unused uploaded files separately with the [Files API](/en-us/rest/api/azureopenai/files/delete).

::: zone-end

::: zone pivot="azd"

Cancel an unneeded job with the CLI commands above. For available cleanup operations, see the [fine-tuning CLI reference](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/cli/finetuning/README.md).

::: zone-end

Delete unused deployments with the [deployment cleanup procedure](../../fine-tuning/deploy-fine-tuned-models#clean-up-your-deployment). Cancelling training doesn't delete deployments or stop their charges.

Retain any data and job records you need to reproduce the experiment.