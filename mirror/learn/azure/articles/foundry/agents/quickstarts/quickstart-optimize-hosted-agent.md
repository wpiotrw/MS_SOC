---
layout: Conceptual
title: 'Quickstart: Optimize a hosted agent - Microsoft Foundry | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-optimize-hosted-agent
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
author: aahill
learn_banner_products:
- azure
manager: mcleans
ms.author: aahi
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Deploy and optimize a hosted agent by using the Azure Developer CLI, Python SDK, VS Code, or the Microsoft Foundry Skill.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: quickstart
ms.subservice: foundry-agent-service
ms.custom: mode-other, dev-focus, doc-kit-assisted
ai-usage: ai-assisted
zone_pivot_groups: hosted-agent-optimize-quickstart-method
locale: en-us
document_id: c0ecfd40-cd48-ea7e-b458-95b9fc9b77af
document_version_independent_id: 1f79dfab-59c8-52b6-c2bb-474438fc7d2c
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/quickstarts/quickstart-optimize-hosted-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/quickstarts/quickstart-optimize-hosted-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/quickstarts/quickstart-optimize-hosted-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/911a44a7-2f6c-477c-810f-dc8b7d425cce
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/14f2b9d5-6f06-45a8-ac5f-313eaa351153
platformId: c997525c-f713-939d-fe74-b3c4d0ec7a94
---

# Quickstart: Optimize a hosted agent - Microsoft Foundry | Microsoft Learn

In this quickstart, you deploy the optimization sample agent, run the agent optimizer to improve its instructions, deploy the winning candidate, and verify the result with an independent evaluation.

For the concepts behind each step and the full end-to-end path, see the [optimization workflow](../concepts/agent-optimizer-overview#the-optimization-workflow).

## Prerequisites

Before you begin, you need:

- An Azure subscription--[Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

::: zone pivot="azd"

- [azd CLI](https://aka.ms/azd) (Azure Developer CLI) version 1.37.0 or later.
- [Azure CLI](/en-us/cli/azure/install-azure-cli) for authentication.
- The `microsoft.foundry` extension for azd. It includes the `azd ai agent` commands, such as `azd ai agent optimize`, but not the `azd ai eval` commands:

    ```bash
    azd ext install microsoft.foundry
    ```

    If already installed, upgrade:

    ```bash
    azd ext upgrade microsoft.foundry
    ```
- The `azure.ai.evaluations` extension for azd, which provides the `azd ai eval` commands. It requires azd 1.33.0 or later:

    ```bash
    azd ext install azure.ai.evaluations
    ```

    If already installed, upgrade:

    ```bash
    azd ext upgrade azure.ai.evaluations
    ```

::: zone-end

::: zone pivot="python"

- [Azure CLI](/en-us/cli/azure/install-azure-cli) for authentication.
- Python 3.10 or later.
- The Python packages used in this path:

    ```bash
    pip install "azure-ai-projects>=2.5.0" azure-ai-agentserver-optimization python-dotenv
    ```
- An existing Foundry project that already contains the hosted agent, registered dataset, and evaluator you want to use for optimization.

::: zone-end

::: zone pivot="csharp"

- [Azure CLI](/en-us/cli/azure/install-azure-cli) for authentication.
- [.NET 10 SDK or later](https://dotnet.microsoft.com/download/dotnet/10.0).
- The .NET packages used in this path.

    ```dotnetcli
    dotnet add package Azure.AI.Projects --prerelease
    dotnet add package Azure.Identity
    ```
- An existing Foundry project that already contains the hosted agent, registered dataset, and evaluator you want to use for optimization.

::: zone-end

::: zone pivot="vscode"

- [Visual Studio Code](https://code.visualstudio.com/).
- [Microsoft Foundry Toolkit for Visual Studio Code](https://aka.ms/foundrytk) version 1.6.4 or later, signed in to Azure. Foundry Toolkit installs and updates the [Microsoft Foundry Skill](../../how-to/develop/use-microsoft-foundry-skill) used by this workflow.
- [GitHub Copilot in Visual Studio Code](https://code.visualstudio.com/docs/copilot/setup) with access to agent mode. Foundry Toolkit sends the Agent Optimizer request to GitHub Copilot after you select the agent workspace.
- [Azure CLI](/en-us/cli/azure/install-azure-cli) and [Azure Developer CLI (AZD)](/en-us/azure/developer/azure-developer-cli/install-azd) version 1.37.0 or later, installed and authenticated:

    ```bash
    az login
    azd auth login
    ```
- The `azure.ai.evaluations` extension for AZD, if you want to generate evaluation assets with `azd ai eval generate`. It requires AZD 1.33.0 or later:

    ```bash
    azd ext install azure.ai.evaluations
    ```

Tip

If you don't have Foundry Toolkit, [install it from the Visual Studio Code Marketplace](https://aka.ms/foundrytk). Foundry Toolkit brings your Foundry resources, model catalog, hosted-agent deployment and playgrounds, and Agent Optimization into Visual Studio Code. Reload Visual Studio Code if prompted, and then sign in to Azure. For a tour of the extension, see [Work with the Microsoft Foundry Toolkit for Visual Studio Code extension](../../how-to/develop/get-started-projects-visual-studio-code).

::: zone-end

::: zone pivot="foundry-skills"

- A coding agent host with the [Microsoft Foundry Skill](../../how-to/develop/use-microsoft-foundry-skill) installed.
- [Azure CLI](/en-us/cli/azure/install-azure-cli) and [Azure Developer CLI (AZD)](/en-us/azure/developer/azure-developer-cli/install-azd) version 1.37.0 or later, installed and authenticated:

    ```bash
    az login
    azd auth login
    ```
- The `microsoft.foundry` extension for AZD. It doesn't include the `azd ai eval` commands. Install it before you start the workflow:

    ```bash
    azd ext install microsoft.foundry
    ```

    If it's already installed, upgrade it.

    ```bash
    azd ext upgrade microsoft.foundry
    ```
- The `azure.ai.evaluations` extension for AZD, which provides the `azd ai eval` commands that the workflow uses. It requires AZD 1.33.0 or later:

    ```bash
    azd ext install azure.ai.evaluations
    ```

    If it's already installed, upgrade it.

    ```bash
    azd ext upgrade azure.ai.evaluations
    ```

::: zone-end

- Your Azure subscription must be on the allow list for the agent optimizer. Contact your Microsoft representative to request access.

::: zone pivot="azd"

## Step 1: Create the project

Initialize a new project from the optimization sample template:

```bash
mkdir my-agent && cd my-agent
azd ai agent init -t https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/bring-your-own/responses/optimization-customer-support/azure.yaml .
```

This template imports the [Optimization Customer Support sample](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/bring-your-own/responses/optimization-customer-support), an optimization-ready Python hosted agent that uses the bring-your-own approach and the Responses protocol. It represents a consumer electronics support agent that handles order inquiries, returns, warranty claims, troubleshooting, complaints, recommendations, and escalation. The deliberately minimal baseline instruction makes the improvements from instruction optimization and skill discovery easy to compare.

The sample calls `load_config()` to load baseline or candidate configuration and includes `.agent_configs/baseline/`, full and quick evaluation datasets, container configuration, and the Foundry deployment manifest. The interactive flow imports these files and prompts for your Azure subscription, region, and model deployment settings.

Tip

If you already have an existing agent project, see [Make your agent optimizer-ready](../how-to/make-agent-optimizer-ready) to add optimization support.

If you already have a Foundry project, add `-p <project-resource-id>` to target existing resources.

To optimize an already deployed agent without running `azd ai agent init` or creating `azure.yaml` and `.azure` files, skip this project-creation step and follow [Optimize an existing agent without AZD project files](../how-to/optimize-agent-targets#optimize-an-existing-agent-without-azd-project-files).

## Step 2: Provision and deploy

Authenticate and provision the Azure resources:

```bash
az login
azd auth login
azd provision
```

Provisioning takes approximately two minutes and creates a Foundry account, project, Azure Container Registry, and model deployments.

Deploy the agent:

```bash
azd deploy
```

Test the deployment:

```bash
azd ai agent invoke "What is 2+2?"
```

Tip

The sample agent reads its model deployment name from the `MODEL_DEPLOYMENT_NAME` environment variable and defaults to `gpt-5.4-mini`. If you target an existing Foundry project that has no deployment with that name, `azd ai agent invoke` fails with a generic `agent error`. Add `MODEL_DEPLOYMENT_NAME` to the `env` section of the agent service in `azure.yaml`, set it to a chat model deployment in your project, and run `azd deploy` again.

## Step 3: Generate evaluation assets

The optimizer scores candidates by using a dataset and evaluators that you provide. To create a measure that reflects how you judge your own agent, generate a dataset and a rubric evaluator by using the `azd ai eval` commands. Use the name of your deployed agent as the target. It's the `name` of the agent service in `azure.yaml`.

In the following commands, replace `<generation-deployment>`, `<judge-deployment>`, `<eval-deployment>`, and `<optimization-deployment>` with names of model deployments in your Foundry project. Set each role explicitly.

```bash
azd ai eval generate \
  --target <agent-name> \
  --from prompt \
  --generation-model <generation-deployment> \
  --dataset-name support-tests \
  --evaluator-name support-rubric \
  --max-samples 15 \
  --agent-instruction "A customer support agent for a consumer electronics company. It handles order inquiries, returns and refunds, warranty claims, device troubleshooting, complaints, product recommendations, and escalation to a human agent."
```

The command generates the dataset and the evaluator in your Foundry project, downloads them to `evals/datasets/support-tests.jsonl` and `evals/evaluators/support-rubric.json`, and registers both in `evals/azure.eval.yaml`.

Note

The `--from` option applies only to the dataset. This step uses `--from prompt`, which generates the rows from the instruction that you pass with `--agent-instruction`. In version 1.0.0-beta.2 of the evaluations extension, `--from agent` can fail in the service with a data generation system error. If that happens in an interactive run, `generate` offers to submit another job that uses the prompt source only, and the default answer is No. By using `--no-prompt` or `-o json`, it doesn't retry. It ends with an error that tells you to rerun by using `--from prompt`. By using `--no-wait` and `--from agent`, it drops the agent source and submits the instruction alone, because it can't retry after it returns.

Tip

The sample's baseline instruction is deliberately a single sentence. By default, `generate` reads the baseline instructions in `.agent_configs/baseline/metadata.yaml`, so the rows it creates are generic. Pass `--agent-instruction` or `--agent-instruction-file` to describe what the agent should do. An explicit instruction takes precedence.

Open the generated files and review them before you continue. If `generate` prints an input-quality warning, review the generated files with extra care. Edit rows or criteria that don't match how you want the agent to behave.

## Step 4: Measure the baseline

Set up an evaluation that scores the deployed agent, so that you can compare the optimized agent against the same measure later. The `generate` command prints the matching `init` command. The optimizer reuses this evaluation in Step 5. Add a judge model and a name:

```bash
azd ai eval init \
  --target <agent-name> \
  --source dataset \
  --dataset support-tests \
  --evaluation-level turn \
  --evaluator builtin.task_completion \
  --evaluator support-rubric \
  --path ./evals \
  --judge-model <judge-deployment> \
  --name optimize-check

azd ai eval create optimize-check
azd ai eval run start --eval optimize-check --name baseline --wait
```

The `init` command adds an evaluation service to `azure.yaml`. The `create` command registers the evaluation in your Foundry project. The run prints the pass rate and a per-evaluator summary:

```output
TEST CASE RESULTS
Total        15
Passed        <n>
Failed        <n>
Errored       <n>
Skipped       <n>
Pass rate  <percent> (<n> passed / 15 total test cases)

EVALUATOR RESULTS
EVALUATOR       PASS  FAIL  SKIP  ERROR   SCORED  PASS RATE  MEAN SCORE
...
```

Important

A run scores the agent version that is current when the run starts, and the run output doesn't show which version that was. Run the baseline before you deploy an optimized candidate, and give each run a descriptive `--name`.

## Step 5: Run the optimizer

Run the optimizer with the evaluation that you set up in Step 4:

```bash
azd ai agent optimize \
  --eval optimize-check \
  --max-candidates 2 \
  --eval-model <eval-deployment> \
  --optimize-model <optimization-deployment>
```

The `--eval` option reuses the `optimize-check` evaluation that `azd ai eval init` added to your project. The optimizer takes the dataset and the evaluators from that evaluation, so you don't pass `--dataset` or `--evaluator`. It reuses only an evaluation that targets an agent and runs at the turn level on a dataset, as the Step 4 evaluation does.

If you omit `--eval`, the CLI uses the evaluation in your project that targets the agent. If more than one evaluation targets the agent, the CLI prompts you to select one. With `--no-prompt`, it fails, so pass `--eval`. To select the evaluation from a configuration file, pass `--eval-config` with the path to the file, such as `evals/azure.eval.yaml`.

To score candidates on a different dataset, pass `--dataset` with the path to a local JSONL file or with a registered dataset as `name:version`. To add evaluators, pass `--evaluator` once for each evaluator.

Note

The `azd ai agent optimize` command doesn't support the legacy agent `eval.yaml` file. The `azd ai agent eval` commands only print guidance for moving to `azd ai eval`. Create evaluation assets with `azd ai eval generate` and `azd ai eval init`.

If you omit `--optimize-model`, the CLI prompts you to select a model. In unattended runs, pass `--eval-model` and `--optimize-model`. The CLI detects your agent from `azure.yaml`. A job with two candidates can take 15 to 20 minutes. The CLI shows progress as the job runs:

```output
  Note: Optimization creates candidate agents as draft versions.
  Your live agent versions are not affected until you explicitly deploy a candidate.

Optimizing agent "customer-support-py"...
  Config: <evaluation-service>/optimize-check
  Baseline saved to .agent_configs/baseline/metadata.yaml
  Job ID: opt_162bd0f09....
  Status: queued
  Portal: <OPTIMIZATION-JOB-URL>
```

Use the portal URL to monitor your job in the Foundry portal. The `Config` line shows the source and the name of the evaluation that the optimizer reuses. The source is the evaluation service, or the configuration file when you pass `--eval-config`. To check the job from the terminal, run `azd ai agent optimize status <job-id>`.

The *eval model* scores each response (any chat-completion model works). The *optimization model* (`--optimize-model`) generates improved candidates and must be from the [supported list](../concepts/agent-optimizer-overview#models) (gpt-5 family or DeepSeek).

Tip

The optimizer can improve an agent only when the baseline leaves room to improve. If the baseline already scores close to the maximum on your dataset, add harder cases, such as ambiguous requests, policy edge cases, and multistep problems, and run the job again.

## Step 6: Deploy the winner

The star (★) in the output indicates the best candidate.

Important

The `apply` command, and the `azd deploy` command that follows it, use the optimization job that your azd environment records for the agent. That's the job you started last for the agent. If you started another job after the one that produced your winning candidate, `apply` fails with a not-found error. Before you apply a candidate, check the recorded job:

```bash
azd env get-values
```

In the output, find `AGENT_<service-key>_OPTIMIZATION_JOB_ID`. To build `<service-key>`, take the agent service name from `azure.yaml`, convert it to uppercase, and replace hyphens and spaces with underscores. For example, the service name `optimization-customer-support-python-responses` becomes `OPTIMIZATION_CUSTOMER_SUPPORT_PYTHON_RESPONSES`.

If the value isn't the ID of the job that produced your winning candidate, set it. The job ID appears in the output when you submit the job:

```bash
azd env set AGENT_<service-key>_OPTIMIZATION_JOB_ID <job-id>
```

This per-agent value takes precedence over `OPTIMIZE_LAST_OPERATION_ID`.

Apply the optimized config locally, then deploy:

```bash
azd ai agent optimize apply --candidate <candidate-id>
azd deploy
```

The `apply` command downloads the optimized configuration into `.agent_configs/<candidate_id>/`, adds `OPTIMIZATION_CANDIDATE_ID` to your `azure.yaml` service environment, and prints a diff of the instructions. The `deploy` command pushes the optimized agent live using code deploy.

Note

The `azd ai eval init` command in Step 4 added an evaluation service to `azure.yaml`, so `azd deploy` also deploys that service. It registers a new version of a dataset or evaluator when its local file changed.

Invoke your agent to check the new behavior:

```bash
azd ai agent invoke "What is your return policy?"
```

## Step 7: Verify with an independent evaluation

The optimizer scores candidates with its own evaluators on its own run. Confirm that the deployed agent improved by running the same evaluation that you ran in Step 4:

```bash
azd ai eval run start --eval optimize-check --name optimized --wait
```

Compare the pass rate and each evaluator's results with the baseline run. To see why rows failed, run the `azd ai eval run output list ... --failed-only` command that the run prints under **Investigate**.

An optimizer score gain doesn't guarantee a gain on an independent evaluation. If the optimized agent doesn't improve on the baseline, don't keep it. Review the failing rows, adjust the dataset or rubric, and run the optimizer again.

To check the pass rate in a pipeline, add `--fail-on pass-rate=<0..1>` to `azd ai eval run start`. The command exits with code 1 when the run's pass rate is below that fraction. The check doesn't compare against the baseline run.

::: zone-end

::: zone pivot="python"

## Python SDK path

Use the following steps if you want to run the optimizer from Python instead of the Azure Developer CLI workflow described earlier.

This path assumes you already have the following resources in an existing Foundry project:

- A hosted agent to optimize.
- A registered training dataset.
- A registered evaluator.

Note

The `azd ai eval` commands keep their assets in `evals/azure.eval.yaml`, in the `datasets`, `evaluators`, and `evals` sections. The `azd ai agent optimize` command reuses an evaluation from that configuration by using `--eval` or `--eval-config`. This SDK path doesn't read it. It uses the registered dataset and evaluator that you reference in the code.

Unlike the Azure Developer CLI flow described earlier, the Python SDK path doesn't scaffold a project or generate a dataset or evaluators for you. If you want to create those assets by using the Azure Developer CLI, install the `azure.ai.evaluations` extension with `azd ext install azure.ai.evaluations` (it requires azd 1.33.0 or later), and then run `azd ai eval generate`.

### 1. Create a `.env` file

Create a working folder, and then add a `.env` file with these values:

```text
FOUNDRY_PROJECT_ENDPOINT=<your-project-endpoint>
FOUNDRY_AGENT_NAME=<your-hosted-agent-name>
DATASET_NAME=<your-registered-dataset-name>
EVALUATOR_NAME=<your-registered-evaluator-name>
DATASET_VERSION=1
POLL_INTERVAL_SECONDS=10
EVAL_MODEL=<your-eval-model-deployment-name>
OPTIMIZATION_MODEL=<your-optimization-model-deployment-name>
```

Run the script from this same working folder so `load_dotenv()` can load the `.env` file automatically. If you prefer to run it from another directory, set the same values in your shell environment first.

Use the exact project endpoint from your Foundry project's **Overview** page. The Python script sends its first request immediately. If `FOUNDRY_PROJECT_ENDPOINT` is only a placeholder or points to the wrong project, the run fails with `ResourceNotFound: The project does not exist`.

Set `EVAL_MODEL` and `OPTIMIZATION_MODEL` to deployment names that already exist in your Foundry project, not just model family names. For example, if your project deployment is named `gpt-4.1-mini` or `DeepSeek-V3.2`, use that exact deployment name in `.env`.

### 2. Run the optimization job

Create a file named `optimize_hosted_agent.py` in the same folder as `.env`:

```python

"""
DESCRIPTION:
    Create an optimization job for a hosted agent using the latest agent
    optimization API, poll the job to completion, and list its candidates.

USAGE:
    python optimize_hosted_agent_v3.py

    Before running the sample:

    pip install azure-ai-projects azure-ai-agentserver-optimization python-dotenv

    Set these environment variables with your own values:
    1) FOUNDRY_PROJECT_ENDPOINT - Required. The Microsoft Foundry project endpoint.
    2) FOUNDRY_AGENT_NAME       - Required. The hosted agent name.
    3) DATASET_NAME             - Required. The registered training dataset name.
    4) EVALUATOR_NAME           - Required. The registered evaluator name.
    5) DATASET_VERSION          - Optional. The dataset version. Defaults to "1".
    6) EVAL_MODEL               - Optional. The evaluation model. Defaults to "gpt-4o".
    7) OPTIMIZATION_MODEL       - Optional. The optimization model. Defaults to "gpt-5".
    8) POLL_INTERVAL_SECONDS    - Optional. Seconds between status polls. Defaults to 10.
    9) OPTIMIZATION_JOB_ID      - Optional. An existing job ID to resume instead of creating a job.
   10) OPTIMIZATION_LOCAL_DIR   - Optional. Path to the local .agent_configs directory.
   11) CREDENTIAL_PROCESS_TIMEOUT_SECONDS
                                - Optional. Credential subprocess timeout. Defaults to 60.
"""

import os
import time
from pathlib import Path

from azure.ai.agentserver.optimization import load_config, load_skills_from_dir
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    AgentOptimizationBaselineAgentConfiguration,
    AgentOptimizationCandidateExpand,
    AgentOptimizationCandidateSearchConfiguration,
    AgentOptimizationConfiguration,
    AgentOptimizationEvaluationConfiguration,
    AgentOptimizationEvaluator,
    AgentOptimizationFoundryAgentTargetConfiguration,
    AgentOptimizationJob,
    AgentOptimizationModelConfiguration,
    AgentOptimizationSkill,
    AgentOptimizationSpace,
    AgentOptimizationTargetCompletionDatasetReferenceDataSource,
    AgentOptimizationTargetCompletionEvaluationSet,
    EvaluationModelConfiguration,
    JobStatus,
    TargetAttribute,
)
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_AGENT_NAME"]
dataset_name = os.environ["DATASET_NAME"]
evaluator_name = os.environ["EVALUATOR_NAME"]
dataset_version = os.environ.get("DATASET_VERSION", "1")
eval_model = os.environ.get("EVAL_MODEL", "gpt-4o")
optimization_model = os.environ.get("OPTIMIZATION_MODEL", "gpt-5")
poll_interval_seconds = int(os.environ.get("POLL_INTERVAL_SECONDS", "10"))
existing_job_id = os.environ.get("OPTIMIZATION_JOB_ID")
credential_process_timeout_seconds = int(
    os.environ.get("CREDENTIAL_PROCESS_TIMEOUT_SECONDS", "60")
)

# Reads the hosted agent's baseline config from .agent_configs/baseline/metadata.yaml.
optimization_config = load_config()

target_attributes = [TargetAttribute.INSTRUCTIONS]
baseline_configuration = None
if optimization_config:
    loaded_skills = optimization_config.skills
    if not loaded_skills and optimization_config.skills_dir:
        loaded_skills = load_skills_from_dir(Path(optimization_config.skills_dir))

    skills = [
        AgentOptimizationSkill(
            name=skill.name,
            description=skill.description,
            body=skill.body or None,
        )
        for skill in loaded_skills
    ]

    if skills:
        target_attributes.append(TargetAttribute.SKILLS)
    if optimization_config.tool_definitions:
        target_attributes.append(TargetAttribute.TOOLS)

    baseline_configuration = AgentOptimizationBaselineAgentConfiguration(
        system_prompt=optimization_config.instructions,
        current_model=optimization_config.model,
        skills=skills or None,
        tools=optimization_config.tool_definitions or None,
    )

with (
    DefaultAzureCredential(
        process_timeout=credential_process_timeout_seconds
    ) as credential,
    AIProjectClient(endpoint=endpoint, credential=credential) as project_client,
):
    job_request = AgentOptimizationJob(
        target_configuration=AgentOptimizationFoundryAgentTargetConfiguration(
            name=agent_name
        ),
        optimization_model_configuration=AgentOptimizationModelConfiguration(
            model=optimization_model
        ),
        optimization_configuration=AgentOptimizationConfiguration(
            evaluation_configuration=AgentOptimizationEvaluationConfiguration(
                training_set=AgentOptimizationTargetCompletionEvaluationSet(
                    source=AgentOptimizationTargetCompletionDatasetReferenceDataSource(
                        name=dataset_name,
                        version=dataset_version,
                    )
                ),
                evaluators=[AgentOptimizationEvaluator(name=evaluator_name)],
                evaluation_model=EvaluationModelConfiguration(model=eval_model),
            ),
            candidate_search_configuration=AgentOptimizationCandidateSearchConfiguration(
                max_candidates=2
            ),
            baseline_agent_configuration=baseline_configuration,
            agent_optimization_space=AgentOptimizationSpace(
                target_attributes=target_attributes
            ),
        ),
    )

    if existing_job_id:
        job_id = existing_job_id
    else:
        poller = project_client.agents.begin_create_optimization_job(
            job=job_request,
            polling=False,
        )
        job_id = poller.details.get("job_id")
        if not isinstance(job_id, str):
            raise RuntimeError(
                "The create operation did not return an optimization job ID."
            )

    print(f"Optimization job ID: {job_id}")

    terminal_statuses = {
        JobStatus.SUCCEEDED,
        JobStatus.FAILED,
        JobStatus.CANCELLED,
    }
    job = project_client.agents.get_optimization_job(job_id=job_id)
    print("Optimization job started, waiting for completion...")
    while job.status not in terminal_statuses:
        print(f"\tstatus=`{job.status}`")
        time.sleep(poll_interval_seconds)
        job = project_client.agents.get_optimization_job(job_id=job_id)
    print(f"\tstatus=`{job.status}`")

    for warning in job.warnings or []:
        print(f"[WARNING] {warning}")

    if job.status == JobStatus.FAILED:
        message = job.error.message if job.error else "<no error message>"
        raise RuntimeError(f"Optimization job `{job.id}` failed: {message}")
    if job.status == JobStatus.CANCELLED:
        raise RuntimeError(f"Optimization job `{job.id}` was cancelled.")
    if job.result is None:
        raise RuntimeError(f"Optimization job `{job.id}` completed without a result.")

    result = job.result
    summary = result.candidate_summary
    if summary:
        print(f"Baseline candidate: {summary.baseline_id}")
        print(f"Best candidate: {summary.best_id}")
        print(f"Completed optimized candidates: {summary.completed_candidate_count}")
        if summary.baseline_score is not None:
            print(f"Baseline score: {summary.baseline_score:.4f}")
        if summary.best_score is not None:
            print(f"Best score: {summary.best_score:.4f}")
    if result.termination_reason:
        print(f"Termination reason: {result.termination_reason}")

    for candidate in project_client.agents.list_optimization_candidates(
        job_id=job_id,
        expand=[AgentOptimizationCandidateExpand.MUTATIONS],
    ):
        details = [
            f"{candidate.name}: candidate_id={candidate.candidate_id}",
            f"status={candidate.status}",
        ]
        if candidate.evaluation:
            if candidate.evaluation.score is not None:
                details.append(f"score={candidate.evaluation.score:.4f}")
            if candidate.evaluation.avg_tokens is not None:
                details.append(f"avg_tokens={candidate.evaluation.avg_tokens:.0f}")
        print(", ".join(details))

```

Run the script:

```bash
python optimize_hosted_agent.py
```

The optimization job ID prints immediately after submission; use it to monitor progress in the Foundry portal.

When the job succeeds, the script prints the winning candidate and its `candidate_id`.

Unlike `azd ai agent optimize`, the Python SDK flow doesn't create a local `.agent_configs/baseline/metadata.yaml` file. The optimization job metadata stays in the returned `job` object and in the Foundry service response, including the baseline candidate, best candidate, and scored candidate list.

### 3. Apply the winning candidate

If you're also working from the local `azd` project used in the CLI flow above, apply the winning candidate by using the `candidate_id` returned by the Python script:

```bash
azd ai agent optimize apply --candidate <candidate-id>
azd deploy
```

If you only need to inspect the result, use the candidate scores and evaluation identifiers printed by the script to review the winning configuration in Foundry before promoting it.

::: zone-end

::: zone pivot="csharp"

## C# SDK path

Use the following steps if you want to run the optimizer from .NET instead of using the Azure Developer CLI workflow described earlier.

This path assumes you already have the following resources in an existing Foundry project:

- A hosted agent to optimize.
- A registered training dataset.
- A registered evaluator, such as the built-in `builtin.task_adherence` evaluator.

Note

The `azd ai eval` commands keep their assets in `evals/azure.eval.yaml`, in the `datasets`, `evaluators`, and `evals` sections. The `azd ai agent optimize` command reuses an evaluation from that configuration by using `--eval` or `--eval-config`. This SDK path doesn't read it. It uses the registered dataset and evaluator that you reference in the code.

Unlike the Azure Developer CLI flow described earlier, the .NET SDK path doesn't scaffold a project or generate a dataset or evaluators for you. If you want to create those assets by using the Azure Developer CLI, install the `azure.ai.evaluations` extension with `azd ext install azure.ai.evaluations` (it requires azd 1.33.0 or later), and then run `azd ai eval generate`.

### 1. Set your environment variables

Create a console app, and then set these values in your shell before you run it:

```text
FOUNDRY_PROJECT_ENDPOINT=<your-project-endpoint>
FOUNDRY_AGENT_NAME=<your-hosted-agent-name>
DATASET_NAME=<your-registered-dataset-name>
DATASET_VERSION=1
EVALUATOR_NAME=builtin.task_adherence
EVAL_MODEL=<your-eval-model-deployment-name>
OPTIMIZATION_MODEL=<your-optimization-model-deployment-name>
```

Use the exact project endpoint from your Foundry project's **Overview** page.

Set `EVAL_MODEL` and `OPTIMIZATION_MODEL` to deployment names that already exist in your Foundry project, not just model family names. The optimization model must be a reasoning model that the optimizer supports. If you pick an unsupported deployment, the service returns an error that lists the allowed models.

### 2. Run the optimization job

Replace `Program.cs` with the following code.

Agent optimization requires the `AgentsOptimization=V2Preview` feature header on every request. The `FoundryFeaturesPolicy` class in this example adds that header to every request the client sends:

```csharp
using System.ClientModel.Primitives;
using Azure.AI.Projects;
using Azure.AI.Projects.Agents;
using Azure.Identity;

#pragma warning disable AAIP001

// Adds the feature header that agent optimization requires.
public sealed class FoundryFeaturesPolicy(string features) : PipelinePolicy
{
    public override void Process(PipelineMessage message, IReadOnlyList<PipelinePolicy> pipeline, int index)
    {
        message.Request.Headers.Set("Foundry-Features", features);
        ProcessNext(message, pipeline, index);
    }

    public override ValueTask ProcessAsync(PipelineMessage message, IReadOnlyList<PipelinePolicy> pipeline, int index)
    {
        message.Request.Headers.Set("Foundry-Features", features);
        return ProcessNextAsync(message, pipeline, index);
    }
}

public static class Program
{
    public static void Main()
    {
        var endpoint = Environment.GetEnvironmentVariable("FOUNDRY_PROJECT_ENDPOINT")!;
        var agentName = Environment.GetEnvironmentVariable("FOUNDRY_AGENT_NAME")!;
        var datasetName = Environment.GetEnvironmentVariable("DATASET_NAME")!;
        var datasetVersion = Environment.GetEnvironmentVariable("DATASET_VERSION") ?? "1";
        var evaluatorName = Environment.GetEnvironmentVariable("EVALUATOR_NAME") ?? "builtin.task_adherence";
        var evalModel = Environment.GetEnvironmentVariable("EVAL_MODEL")!;
        var optimizationModel = Environment.GetEnvironmentVariable("OPTIMIZATION_MODEL")!;

        var options = new AIProjectClientOptions();
        options.AddPolicy(new FoundryFeaturesPolicy("AgentsOptimization=V2Preview"), PipelinePosition.PerCall);

        AIProjectClient projectClient = new(new Uri(endpoint), new DefaultAzureCredential(), options);
        AgentOptimizationJobs optimizationJobs = projectClient.AgentAdministrationClient.GetAgentOptimizationJobs();

        OptimizationJob job = new()
        {
            Inputs = new OptimizationJobInputs(
                new OptimizationAgentIdentifier(agentName),
                new OptimizationReferenceDatasetInput(datasetName) { Version = datasetVersion },
                new[] { new OptimizationEvaluatorRef(evaluatorName) })
            {
                Options = new OptimizationOptions
                {
                    MaxCandidates = 2,
                    EvalModel = evalModel,
                    OptimizationModel = optimizationModel,
                    // The optimizer needs at least one optimizable target, such as the
                    // baseline system prompt, the tool definitions, or skills.
                    OptimizationConfig =
                    {
                        ["system_prompt"] = BinaryData.FromObjectAsJson(
                            "You are a helpful assistant that answers user requests accurately and concisely."),
                    },
                },
            },
        };

        OptimizationJob created = optimizationJobs.Create(job);
        Console.WriteLine($"Optimization job started: {created.Id}");

        OptimizationJob current = created;
        while (current.Status != AgentsJobStatus.Succeeded
            && current.Status != AgentsJobStatus.Failed
            && current.Status != AgentsJobStatus.Cancelled)
        {
            Thread.Sleep(TimeSpan.FromSeconds(20));
            current = optimizationJobs.Get(created.Id);
            Console.WriteLine($"\tstatus=`{current.Status}`");
        }

        Console.WriteLine($"Final status: {current.Status}");

        if (current.Result is not null)
        {
            Console.WriteLine($"Baseline candidate: {current.Result.Baseline}");
            Console.WriteLine($"Best candidate: {current.Result.Best}");

            foreach (OptimizationCandidate candidate in current.Result.Candidates)
            {
                Console.WriteLine(
                    $"{candidate.Name}: candidate_id={candidate.CandidateId}, " +
                    $"avg_score={candidate.AvgScore:F4}, " +
                    $"avg_tokens={candidate.AvgTokens:F0}");
            }
        }
    }
}
```

Run the app:

```dotnetcli
dotnet run
```

When the job succeeds, the app prints the winning candidate and its `candidate_id`:

```output
Optimization job started: opt_<job-id>
        status=`in_progress`
        status=`succeeded`
Final status: succeeded
Baseline candidate: cand_opt_<job-id>_0000
Best candidate: cand_opt_<job-id>_0000
baseline: candidate_id=cand_opt_<job-id>_0000, avg_score=1.0000, avg_tokens=0
```

Unlike `azd ai agent optimize`, the .NET SDK flow doesn't create a local `.agent_configs/baseline/metadata.yaml` file. The optimization job metadata stays in the returned job object and in the Foundry service response, including the baseline candidate, best candidate, and scored candidate list.

### 3. Apply the winning candidate

If you're also working from the local `azd` project used in the CLI flow, apply the winning candidate by using the `candidate_id` returned by the app:

```bash
azd ai agent optimize apply --candidate <candidate-id>
azd deploy
```

If you only need to inspect the result, use the candidate scores and evaluation identifiers printed by the app to review the winning configuration in Foundry before promoting it.

::: zone-end

::: zone pivot="vscode"

## Run the optimization in VS Code

Foundry Toolkit includes a native Agent Optimization experience for deployed hosted agents. From the agent playground, you can start an optimization run, compare candidates with the baseline, inspect configuration changes, and deploy the best candidate.

### Step 1: Select a deployed hosted agent

1. Select **Foundry Toolkit** in the Activity Bar.
2. Under **My Resources**, select **Agents**.
3. If you have a deployed hosted agent, select it to open the hosted agent playground.
4. If you don't have a deployed hosted agent, complete the VS Code path in [Quickstart: Deploy your first hosted agent](quickstart-hosted-agent?pivots=vscode). After deployment finishes, return to **Agents** and select the new hosted agent.

### Step 2: Start an optimization run

1. Select the **Optimize** tab.

[![Screenshot of a hosted agent in Foundry Toolkit with the Optimize tab selected and the New Optimization button available.](../media/quickstart/optimize-hosted-agent-vscode-optimize-tab.png)](../media/quickstart/optimize-hosted-agent-vscode-optimize-tab.png#lightbox)

1. Select **New Optimization**.
2. In **Select Workspace**, choose the workspace that contains the selected hosted agent's code:

    - Select **Current workspace** if the current workspace contains the agent code and its `azure.yaml` file.
    - Select **Browse...** to open the workspace that contains the agent code.

    Foundry Toolkit uses the workspace files to prepare the optimization and to apply a candidate to the matching `azure.ai.agent` service.

[![Screenshot of the Select Workspace prompt in Foundry Toolkit showing Current workspace and Browse options for locating the hosted agent code.](../media/quickstart/optimize-hosted-agent-vscode-select-workspace.png)](../media/quickstart/optimize-hosted-agent-vscode-select-workspace.png#lightbox)

1. Foundry Toolkit opens GitHub Copilot Chat and sends an Agent Optimizer request populated with the selected agent's kind, name, and Foundry project endpoint.
2. Answer the four optimization questions in Copilot Chat:

    | Input | What to provide |
    | --- | --- |
    | Evaluation metrics | Enter the metrics or evaluators to use. If you don't have them, choose whether to generate them with `azd ai eval generate` (use `--from prompt` for the dataset). |
    | Dataset | Select the optimization dataset. If you don't have one, choose whether to generate one with `azd ai eval generate` (use `--from prompt`). |
    | Maximum candidates | Enter the maximum number of candidates to generate, such as `2`. |
    | Optimization model | Select an existing deployment from the [supported optimization models](../concepts/agent-optimizer-overview#models). |

GitHub Copilot waits for these inputs before it starts optimization. The generated request directs Copilot to use the Microsoft Foundry Skill's Agent Optimizer workflow and Azure Developer CLI commands exclusively. It doesn't use Foundry MCP tools. Copilot:

- Inspects the agent code in the selected workspace.
- Initializes an AZD environment from existing `azure.yaml` and `.env` values if the project doesn't already have one.
- Wires the agent for optimization and deploys the updated hosted agent.
- Starts the optimization after you review and approve the proposed file changes and commands.

After Copilot submits the job, return to the **Optimize** tab. The run appears under **Optimization runs**. The table shows its run ID, status, candidate count, baseline score, best score, and creation time.

### Step 3: Compare and deploy the best candidate

1. When the run succeeds, select it under **Optimization runs**.
2. Compare the **Baseline** and **Best** scores. Review **Score details** for each candidate, and select **View changes** to inspect its configuration changes.
3. If the best candidate improves on the baseline, select **Deploy best candidate** to update the current agent. To deploy it as a new agent or change deployment settings, select **Custom deploy** instead.

Note

If every candidate scores lower than the baseline, don't deploy a candidate. Keep the current agent and revise the dataset or optimization settings before you run the optimizer again.

[![Screenshot of a completed optimization run in Foundry Toolkit comparing the baseline and generated candidates, with scores, configuration changes, and deployment options.](../media/quickstart/optimize-hosted-agent-vscode-results.png)](../media/quickstart/optimize-hosted-agent-vscode-results.png#lightbox)

::: zone-end

::: zone pivot="foundry-skills"

## Run the optimization with the Microsoft Foundry Skill

Use this path in any coding agent host that supports the Microsoft Foundry Skill, such as GitHub Copilot in Visual Studio Code, Copilot CLI, or Claude Code. The skill resolves the agent context from `azure.yaml`, loads its Agent Optimizer workflow, and keeps candidate application and deployment behind review gates.

Note

The dedicated `azd ai eval` commands keep evaluation assets in `evals/azure.eval.yaml`, in `datasets`, `evaluators`, and `evals` sections. The `azd ai agent optimize` command doesn't support the legacy agent `eval.yaml` file. It reuses an evaluation from that configuration by using `--eval` or `--eval-config`. For guidance on datasets and evaluators, see [Create an evaluation dataset and evaluators](../how-to/create-optimizer-dataset).

### Step 1: Open the agent workspace

Open an empty folder in your coding agent host. Confirm that the `microsoft-foundry` skill is available. If the skill isn't available, follow [Use the Microsoft Foundry Skill in coding agents](../../how-to/develop/use-microsoft-foundry-skill).

### Step 2: Ask the skill to run Agent Optimizer

Submit this prompt to your coding agent:

```text
Use the Microsoft Foundry Skill to run the Agent Optimizer workflow for a
Python hosted agent. If this workspace doesn't contain an agent, initialize the
customer support optimization sample from this template:
https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/bring-your-own/responses/optimization-customer-support/azure.yaml
Resolve the AZD environment and hosted-agent service, verify that the agent is
optimizer-ready, and deploy and invoke the baseline. If the azd ai eval
commands aren't available, run azd ext install azure.ai.evaluations first (it
requires azd 1.33.0 or later). Generate the evaluation
dataset and evaluators by using azd ai eval generate, with --from prompt for the
dataset, and show me them. Set up the evaluation by using azd ai eval init and
azd ai eval create, and run a baseline evaluation by using azd ai eval run
start. Verify that the project has a supported optimization model deployment,
then run Agent Optimizer with two candidates by reusing that evaluation with
azd ai agent optimize --eval. Stop after reporting the operation ID,
portal URL, candidate IDs, and scores. Don't apply or deploy a candidate yet.
```

The coding agent might ask you to select a subscription, region, Foundry project, agent service, evaluation model, or optimization model when it can't resolve those values from the workspace. Review generated files and cost-bearing resources before you approve any changes or commands.

### Step 3: Apply and deploy an approved candidate

After you review the optimization results, submit this follow-up prompt:

```text
Recommend the best optimization candidate and explain the score improvement.
Summarize the candidate changes before applying anything. After I approve the
candidate, apply it locally, show the source diff, and stop again before
deployment. After I approve deployment, run azd deploy, invoke the agent with
"What is your return policy?", and rerun the same azd ai eval evaluation with a
new run name. Compare it with the baseline run to confirm the improvement.
```

The skill uses `azd ai agent optimize apply --candidate <candidate-id>` so you can review the optimized configuration locally. It deploys only after your approval, then invokes the updated hosted agent and reruns the evaluation.

::: zone-end

## Clean up resources

If your workflow created resources through the AZD project, delete the provisioned resources when you finish experimenting:

```bash
azd down --force --purge
```

Tip

**Why `--purge`?** Foundry accounts use soft-delete by default. Without `--purge`, the resource name stays reserved for 48 hours, and reprovisioning with the same name fails.

## Troubleshooting

| Problem | Cause | Fix |
| --- | --- | --- |
| `azd ai agent optimize` command not found | Agent extension is missing or outdated. | Run `azd ext install microsoft.foundry`, or `azd ext upgrade azure.ai.agents` if the agent extension is already installed. The agent extension requires azd 1.37.0 or later. Inspect `azd ai agent optimize --help`. |
| `azd ai eval` command not found | The evaluations extension isn't installed. The `microsoft.foundry` extension doesn't include it. | Run `azd ext install azure.ai.evaluations`, or `azd ext upgrade azure.ai.evaluations` if it's already installed. The extension requires azd 1.33.0 or later. |
| `azd ai agent invoke` fails with `agent error` and `An internal server error occurred` | The agent's model deployment doesn't exist in your project. The agent logs show `DeploymentNotFound`. | Run `azd ai agent monitor` to read the logs. Set `MODEL_DEPLOYMENT_NAME` in the agent service's `env` section in `azure.yaml` to an existing deployment, and run `azd deploy` again. |
| `azd ai agent eval` prints that the legacy agent evaluation workflow was removed | The `azd ai agent eval` commands are deprecated and only print migration guidance. | Run `azd ext install azure.ai.evaluations`, and then use the `azd ai eval` commands, such as `azd ai eval generate`, `azd ai eval init`, and `azd ai eval run start`. |
| `azd ai agent optimize` fails with `--dataset requires name:version for a registered dataset, or a local JSONL file` | You passed a registered dataset name without a version to `--dataset`. | Pass the registered dataset as `name:version`, or pass the path to a local JSONL file. |
| `azd ai agent optimize` fails with `no evaluation matches the selected eval and agent` | The evaluation that `--eval` or `--eval-config` selects doesn't exist, or it doesn't target your agent. | Pass the name of an evaluation that targets the agent, such as the one that you create with `azd ai eval init --target <agent-name>`. |
| `azd ai agent optimize apply` returns not found for a candidate | The candidate belongs to an earlier job, and `apply` uses the most recent job in the azd environment | Apply a candidate from the job you started last. |
| `optimization_model is required` | Running in non-interactive mode without a model configured | Add `--optimize-model gpt-5` to the command, or set `optimization_model_configuration.model` in the optimization request file that you pass with `--config`. In interactive mode, the CLI prompts for model selection. |
| Python script fails with `KeyError: 'DATASET_NAME'` or another missing variable | The script didn't load your `.env` file, or the variable is missing | Run the script from the same folder as `.env`, or export the required values in your shell before running `python optimize_hosted_agent.py`. |
| Python script fails with `ResourceNotFound: The project does not exist` | `FOUNDRY_PROJECT_ENDPOINT` doesn't point to an existing Foundry project | Copy the project endpoint from the Foundry project's **Overview** page and update `FOUNDRY_PROJECT_ENDPOINT` in `.env`. |
| Python script fails with `Optimization model deployment '<name>' not found` | `OPTIMIZATION_MODEL` is not the name of a deployed model in your Foundry project | Use the exact deployment name from **Build** &gt; **Deployments**, such as an existing `gpt-5` family or DeepSeek deployment in your project. |
| The job request fails with `evaluators is required and cannot be empty` | The `Foundry-Features` header is missing from the request | Add the `AgentsOptimization=V2Preview` header, as the `FoundryFeaturesPolicy` class in the C# path shows. |
| The job fails with `No optimizable element found for the hosted agent` | The request doesn't include an optimizable target | Supply at least one target in `optimization_config`, such as the baseline `system_prompt`, the tool definitions, or skills. |
| The job fails with `AllEvaluatorsFailedError` | The evaluator is misconfigured, so every row fails to score | Open the evaluation run link in the error, and confirm the evaluator scores your agent's responses. Start with a built-in evaluator such as `builtin.task_adherence`. |
| The **Optimize** section doesn't appear for a hosted agent | Foundry Toolkit is older than version 1.6.4, or the selected agent isn't a deployed hosted agent | Update [Foundry Toolkit](https://aka.ms/foundrytk), reload Visual Studio Code, and reopen the deployed agent from the **Agents** tab. |
| GitHub Copilot Chat doesn't open after you select the workspace | GitHub Copilot isn't installed, isn't available for your account, or agent mode is disabled | Set up [GitHub Copilot in Visual Studio Code](https://code.visualstudio.com/docs/copilot/setup), enable agent mode, and then select **New Optimization** again. |
| Foundry Toolkit can't apply the best candidate to the current workspace | The workspace doesn't contain an `azure.yaml` service whose name matches the deployed hosted agent | Open the workspace that contains the selected agent's code and matching `azure.ai.agent` service, then try again. |
| Coding agent can't find the hosted agent | The wrong folder is open, or `azure.yaml` doesn't define an `azure.ai.agent` service | Open the AZD project folder that contains `azure.yaml`, then ask the coding agent to resolve the hosted-agent service again. |
| Coding agent stops before applying or deploying a candidate | The Agent Optimizer skill requires review before source changes and deployment | Review the candidate scores and local diff, then explicitly approve the apply or deployment step. |
| Optimization score is 0 or very low | Evaluation has many errored rows | Open the **Eval** link in the results. Fix response generation or evaluator errors, then rerun. |
| `azd provision` fails with quota error | Subscription lacks capacity | Try a different region or request a quota increase. |

## What you learned

In this quickstart, you:

- Deployed the optimization sample agent by using the customer-support template.
- Ran the agent optimizer by using the Azure Developer CLI, Python SDK, .NET SDK, Visual Studio Code, or the Microsoft Foundry Skill.
- Generated an evaluation dataset and rubric evaluator by using `azd ai eval`.
- Deployed the winning candidate and verified it with an independent evaluation that you can compare against the baseline.