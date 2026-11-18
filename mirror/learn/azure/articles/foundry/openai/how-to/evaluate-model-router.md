---
layout: Conceptual
title: Evaluate model router for your workload - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/evaluate-model-router
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
author: kosti-v
learn_banner_products:
- azure
manager: mcleans
ms.author: kostiv
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Compare model router with a single-model deployment on quality, latency, and estimated cost in the Foundry portal, with the SDK, or with the open-source toolkit.
ms.date: 2026-11-08T00:00:00.0000000Z
ms.subservice: foundry-model-inference
ms.topic: how-to
ms.custom:
- doc-kit-assisted
ms.reviewer: chrhoder
ai-usage: ai-assisted
locale: en-us
document_id: eecb2fb4-e5c0-2d68-2db8-72dd43f8b2bb
document_version_independent_id: 829a8165-9594-9773-18e9-5177d72f9667
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/openai/how-to/evaluate-model-router.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/openai/how-to/evaluate-model-router
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/openai/how-to/evaluate-model-router.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8f01073a-20aa-3abb-4059-627d39a2bfb0
---

# Evaluate model router for your workload - Microsoft Foundry | Microsoft Learn

Before you move production traffic, prove that model router in Microsoft Foundry meets your bar on your own prompts. Run model router and the model you'd otherwise use against the same dataset and evaluators, and then compare quality, latency, and estimated cost side by side. In this article, you run that comparison in the Foundry portal, with the SDK, or with the open-source toolkit, and then decide what to change next.

- Compare your model router deployment with a single-model baseline on the same prompts, evaluators, and settings.
- In the Foundry portal, each run reports P50 and P95 latency. For Global Standard deployments, it also reports estimated cost, with a breakdown by the models that model router selected.
- Model router can be the evaluation target only. It can't be the judge, the synthetic data generator, or the simulator.
- For automated, repeatable comparisons, use cloud evaluation in the SDK or the open-source Model Router Auto Evaluation toolkit.
- After you adopt model router, the **Monitor** tab compares the cost of your production traffic with single-model baselines.

Important

Features or capabilities marked (preview) in this article are in Public Preview and are subject to the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Previews are provided without a service-level agreement, and Microsoft doesn't recommend them for production workloads. Certain features might not be supported or might have constrained capabilities.

## Prerequisites

- A model router deployment. For estimated cost in evaluation results, use the Global Standard deployment type. To create a deployment, see [Deploy model router](model-router-configure#deploy-model-router).
- A baseline deployment: the model that serves your workload today, or the single model you'd deploy instead of model router.
- A dataset of representative prompts in CSV or JSONL format. Remove secrets, personal data, and other sensitive information first. In the Foundry portal, synthetic data generation is also available.
- A judge model deployment for AI-assisted evaluators. Model router can't be the judge. For the requirements, see [Run evaluations from the Microsoft Foundry portal](../../how-to/evaluate-generative-ai-app#prerequisites).
- The **Foundry User** role on the Foundry project. For every role that evaluation needs, see [Set up permissions for Microsoft Foundry evaluation workflows](../../observability/how-to/evaluation-permissions).

## Define the deployment decision

Start with the decision that the results must support. For example: replace a single-model deployment with model router, pick a routing mode, or choose which models to route to. Treat it like hill climbing: start from a baseline, change one lever, and keep the change only when it moves your workload closer to its goals.

Set acceptance criteria for each dimension before you run anything:

| Dimension | Acceptance criteria to set |
| --- | --- |
| **Quality** | The minimum evaluator score or pass rate, for the whole workload and for high-impact categories. Consider accuracy, completeness, clarity, and helpfulness. |
| **Cost** | The maximum estimated cost per request, or the minimum savings compared with the baseline. |
| **Latency** | The acceptable median (P50) and tail (P95) latency for your user experience. |
| **Policy** | The models, regions, and deployment types that your organization allows. |

The right tradeoff depends on the workload. A high-volume classification workload might accept a small quality difference for lower cost. A workload that makes high-impact recommendations might need equal or better quality before cost matters.

### Design a fair comparison

- **Test the configuration you'd run in production.** The **Balanced** routing mode and the full model pool are good starting points, unless policy, regional availability, or workload needs call for a model subset.
- **Use a meaningful baseline.** Compare with the model that serves the workload today, or the single-model deployment you'd otherwise adopt.
- **Represent your traffic mix.** Include common requests, hard edge cases, long inputs, and high-impact tasks. Group prompts by category so that an average doesn't hide a regression in one category.
- **Keep everything else the same.** Use the same prompts, system instructions, output limits, and evaluators for both runs. Otherwise, a configuration difference can look like a routing effect.
- **Plan for human review.** Automated scores are estimates. Have qualified reviewers check high-impact, regulated, domain-specific, and inconclusive results.
- **Watch sample sizes.** Add prompts when an important category has too few examples to support a conclusion.

## Evaluate in the Foundry portal

Run one evaluation with your model router deployment as the target and one with your baseline, using the same dataset and evaluators. Then compare the two runs.

1. In the [Foundry portal](https://ai.azure.com/?cid=learnDocs), select **Evaluation** &gt; **Create**. Or go to **Build** &gt; **Models**, select your model router deployment, select the **Evaluation** tab, and then select **Create**.
2. Choose **Model** as the target, and select your model router deployment.
3. Add your dataset as a CSV or JSONL file, or generate synthetic data by using a model other than model router.
4. Choose evaluators. For AI-assisted evaluators, select a judge model other than model router.
5. Review the settings, and start the run.
6. Repeat steps 1 through 5 by using your baseline deployment as the target. Use the same dataset and evaluators.
7. Select both runs, and compare them side by side. For the comparison view, see [Compare the evaluation results](../../how-to/evaluate-results#compare-the-evaluation-results).

Each model-target run reports:

- **Target latency**: P50 and P95 end-to-end latency.
- **Estimated target cost**: for Global Standard deployments, with a per-model cost breakdown for the models that model router selected. Estimated cost excludes evaluator costs and discounts.

To find these values in the run details, see [Review model-target latency and estimated cost](../../how-to/evaluate-results#review-model-target-latency-and-estimated-cost). For every option in the evaluation wizard, see [Run evaluations from the Microsoft Foundry portal](../../how-to/evaluate-generative-ai-app).

Important

Model router can only be the evaluation target. It can't be the judge (grader), the synthetic data generator, or the simulator. Choose another model deployment for those roles.

## Evaluate with the SDK

Cloud evaluation in the Microsoft Foundry SDK runs the same comparison from code, which makes it repeatable whenever your prompts or settings change. A model router deployment works as the target of a model-target evaluation.

1. Follow [Evaluate a model target](../../observability/how-to/cloud-evaluation-targets#evaluate-a-model-target). In the `azure_ai_target_completions` data source, set the `model` of the `azure_ai_model` target to your model router deployment name:

    ```python
    import os
    
    target = {
        "type": "azure_ai_model",
        "model": os.environ["MODEL_ROUTER_DEPLOYMENT"],  # Your model router deployment name
    }
    ```
2. Create a second run with your baseline deployment as the target, with the same data and evaluators.
3. When both runs finish, read `latency.target` and `estimated_cost.target` from each run. See [Review model-target latency and estimated cost](../../observability/how-to/cloud-evaluation-results#review-model-target-latency-and-estimated-cost).

For a model router target, each entry in `estimated_cost.target.model_costs` is a model that model router selected, with its estimated cost and token counts.

## Evaluate with the open-source toolkit

The [Model Router Auto Evaluation toolkit](https://github.com/microsoft-foundry/Model-Router-Auto-Evaluation) automates a side-by-side comparison of model router and a baseline model on quality, cost, and latency, and produces a report. It supports `/openai/v1` and Responses API endpoints. Use it when you want to run the comparison from your own environment, with a judge model and scoring setup that you control.

1. Follow the toolkit [quickstart](https://github.com/microsoft-foundry/Model-Router-Auto-Evaluation/blob/main/QUICKSTART.md). Explore the report with mock data first, and then connect your deployments.
2. Prepare your prompts. See [Create a custom evaluation dataset](https://github.com/microsoft-foundry/Model-Router-Auto-Evaluation/blob/main/docs/how-to-custom-dataset.md).
3. Run the comparison, and review the report. For the metrics, see [Interpret evaluation results](https://github.com/microsoft-foundry/Model-Router-Auto-Evaluation/blob/main/docs/how-to-interpret-results.md).

The repository is the source of truth for current commands, input formats, judging behavior, statistical methods, pricing calculations, and report fields. To understand how the toolkit calculates and aggregates its results, see the [evaluation methodology](https://github.com/microsoft-foundry/Model-Router-Auto-Evaluation/blob/main/docs/methodology.md).

## Read the results

Review quality, latency, and cost together, and compare them to the acceptance criteria you set. A lower cost doesn't justify a quality regression in an important category, and a good median latency can hide slow requests.

| Result | Where to find it | How to read it |
| --- | --- | --- |
| Evaluator scores | The run details and comparison view in the portal. In the SDK, the run's per-criteria results. | Compare with your quality criteria, for the whole workload and for each category. |
| Target latency | The run details in the portal. In the SDK, `latency.target.p50_ms` and `latency.target.p95_ms`. | Compare median and tail latency with the baseline. |
| Estimated target cost | The run details in the portal. In the SDK, `estimated_cost.target.estimated_cost`. | Compare cost with the baseline. Available for Global Standard deployments. Excludes evaluator costs and discounts. |
| Per-model cost breakdown | The run details in the portal. In the SDK, `estimated_cost.target.model_costs`. | See which models model router selected and what each cost. The model mix can help explain a change in quality, cost, or latency. |
| Cost completeness | In the SDK, `estimated_cost.target.completeness` and `unpriced_models`. | When `completeness` is `partial`, the estimate covers only the models that could be priced. Check it before you compare runs. |

When the portal's comparison view marks a difference as inconclusive, add representative prompts before you decide.

Record the context of each run so that you can reproduce it and attribute changes to the setting you tested:

- The baseline deployment.
- The model router version, routing mode, and model subset.
- The dataset and relevant application settings.
- The acceptance criteria you used to interpret the run.

## Choose what to try next

Use the results to choose one lever to change. You have four: the routing mode, the model subset, per-request controls, and a direct deployment for part of the workload. The following table lists common patterns, not universal rules.

| What you see | What to try next |
| --- | --- |
| Quality falls short of your criteria. | Switch to the **Quality** routing mode, or route to a model subset of stronger models. See [Choose a routing mode](model-router-configure#choose-a-routing-mode) and [Route to a subset of models](model-router-configure#route-to-a-subset-of-models). |
| Quality is acceptable, but savings are small. | Try the **Cost** routing mode, and recheck high-impact categories for regressions. |
| One category behaves differently from the rest. | Evaluate that category on its own. Then give its requests their own routing mode or model list with per-request controls (preview). See [Control model router routing per request](model-router-routing-controls). |
| One category needs the same model every time. | Keep a direct deployment of that model for that part of the workload, or pin those requests to one model with `routing_config.models` (preview). See [Limit a request to specific models](model-router-routing-controls#limit-a-request-to-specific-models). |
| The results depend on a model that you can't use. | Choose a model subset that's available in your region and allowed by your organization's policy. See [Supported regions](../concepts/model-router-models#supported-regions) and [Govern model router with Azure Policy](../../how-to/model-router-policy). |
| The results are inconclusive. | Add representative prompts, review the inconclusive items, and rerun the comparison. |
| Tail latency exceeds your requirement. | Validate under production-like traffic. On the **Monitor** tab, compare **Router overhead** with **Model processing**, and use the **By model** view to find slow models. See [Use the Monitor tab](monitor-model-router#use-the-monitor-tab). |

Change one lever at a time, and rerun the same prompts against the same baseline. That way, you know which change moved the results.

## Validate under production-like traffic

A controlled evaluation doesn't reproduce every production condition. Before you move all traffic, run a limited production test on your model router deployment, and watch these signals:

- **Cost**: on the **Monitor** tab, **Estimated cost: model router vs. single-model baselines** shows what the same production traffic would have cost on your baseline model. See [Compare cost with single-model baselines](monitor-model-router#compare-cost-with-single-model-baselines). Confirm billed amounts in [Cost Management](monitor-model-router#track-costs-in-cost-management).
- **Latency**: median and tail latency under expected concurrency, in **Request latency**.
- **Reliability**: errors and failover, in **Request success rate over time** and **Fallback rate over time**.
- **Model mix**: which models serve your traffic, in **Requests by model**.
- **Quality**: quality signals for important categories, plus feedback from qualified reviewers and users.

Treat the configuration you adopt as your new baseline. Rerun the evaluation when your traffic mix, routing mode, model subset, application, or pricing changes. Deployments that use the full model pool get new models automatically, so also rerun it after the pool changes listed in [What's new in model router](../../foundry-models/whats-new-model-router).