---
layout: Conceptual
title: Microsoft Purview Auto-Labeling Concepts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/auto-label-classification-simulation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview classification, simulation, and enforcement differ for existing SharePoint and OneDrive files, and when to refresh classification.
author: nickjrobinson
ms.author: nickrob
manager: laurawi
audience: Admin
ms.service: purview
ms.subservice: purview-information-protection
ms.topic: concept-article
ms.date: 2026-10-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1030
ai-usage: ai-generated
locale: en-us
document_id: f0253c12-eaba-acf1-9df3-0acf37709f96
document_version_independent_id: f0253c12-eaba-acf1-9df3-0acf37709f96
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/auto-label-classification-simulation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: auto-label-classification-simulation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/auto-label-classification-simulation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 63d927b2-75bb-52bc-e909-e2460c7ad150
---

# Microsoft Purview Auto-Labeling Concepts | Microsoft Learn

In Microsoft Purview, service-side auto-labeling is a policy-based capability that applies or removes sensitivity labels. For existing files in SharePoint and OneDrive, classification, policy evaluation, and label enforcement are distinct stages. These distinctions help you interpret unexpected matches and decide whether to change a policy, update classification, or investigate a labeling failure.

This article focuses on policies that use sensitive information types (SITs). A new or changed policy can evaluate existing files using available classification results. Changing a custom SIT or restarting simulation doesn't, by itself, refresh classification for unchanged historical files.

## Classification, policy evaluation, and enforcement

Each stage answers a different question. A policy match isn't evidence that the content was freshly classified or that a label was successfully applied.

| Stage | What it does | What the result means |
| --- | --- | --- |
| **Classification** | Identifies sensitive content and records classification results, such as the SIT, match count, and confidence. | The results describe what classification detected when it processed the file. |
| **Policy evaluation and simulation** | Evaluates the policy's scope and conditions using available classification results for SIT conditions. Simulation reports matches without applying or removing labels. | The file matched the evaluated policy. The match doesn't prove that classification used the latest SIT definition. |
| **Enforcement** | Applies or removes a label according to the active policies, file eligibility, and applicable label rules. | The actual labeling outcome must be checked separately from the simulation match. |

## Policy changes aren't classifier changes

Changing the conditions that a policy evaluates isn't the same as changing how a SIT detects sensitive content.

| Change or action | Effect on existing SharePoint and OneDrive files |
| --- | --- |
| **Create or change an auto-labeling policy or rule** | Can evaluate existing in-scope files using available classification results. Existing, correct classifications don't need to be refreshed for every policy change. |
| **Change a custom SIT definition** | Doesn't by itself reclassify unchanged historical files. Available results can still reflect the earlier definition. |
| **Restart auto-labeling simulation** | Reevaluates policy matches. It doesn't itself reclassify the underlying content. |
| **Run on-demand classification** | Classifies files within the scan scope. If you select specific classifiers, only those classifiers have their results updated for the scanned files. |

Creating a policy that references a new SIT isn't proof that all historical files have been classified with that SIT. Review classification coverage rather than assuming that either the policy creation date or the SIT creation date establishes coverage.

## Why an older file can appear in simulation

Supported files can be eligible for auto-labeling whether they existed before or after the policy was created. An older file can match a new policy because classification results are already available for it. The file's last-modified date alone doesn't establish when it was last classified.

For example, a file already has classification results for a SIT. You create a policy that uses that SIT, or change the policy's required match count. The file can match the policy without being edited or freshly classified.

In a different example, you narrow a custom SIT definition after a file was classified. If the file's classification hasn't been refreshed, simulation can still match using the earlier results. This is one possible explanation for a discrepancy, not a diagnosis for every unexpected match.

## Uploaded-file tests and policy simulation answer different questions

The SIT **Test** function evaluates an uploaded file against the SIT. Auto-labeling simulation evaluates the policy's scope and conditions using available classification results for existing SharePoint and OneDrive files. A successful uploaded-file test doesn't establish that historical files have the same classification results.

Use [Test sensitive information types](sit-test-a-sit) with representative positive and negative examples to validate your custom detector. Your organization is responsible for deciding whether a custom SIT meets its detection requirements and obligations. A successful test or simulation doesn't certify regulatory coverage.

When a direct test and simulation disagree, consider the SIT definition used for classification as well as the policy's conditions and scope. Don't assume that restarting simulation refreshes classification.

## When historical files need updated classification

Use [on-demand classification](on-demand-classification) when relevant historical files haven't been classified or need updated classification, such as after a custom SIT change. Scope the scan to the relevant locations, file date range, file types, and classifiers. Check that the date range includes the historical files you intend to evaluate. Review estimates and charges before starting classification.

Important

On-demand classification isn't an auto-labeling simulation. Updated classification can trigger actions from other active matching policies, including labeling, label removal, and other protection or lifecycle actions. Review active policies before starting the scan, even if the auto-labeling policy you're testing is still in simulation.

After classification completes, review [auto-labeling simulation results](auto-label-simulation-results) before deciding whether to turn on the policy you're testing. Refreshing classification doesn't itself undo existing labels; label changes depend on the applicable policies or an authorized labeling action.

## Simulation doesn't guarantee enforcement

Simulation evaluates one policy. When policies are active, competing policies and [label replacement rules](apply-sensitivity-label-automatically#will-an-existing-label-be-overridden) can affect the outcome. File eligibility, protection, and labeling failures can also prevent a matching file from being labeled.

Use [policy-level labeling activity](apply-sensitivity-label-automatically#policy-level-labeling-activity-for-sharepoint-and-onedrive) to review actual outcomes and failures. [Coverage by simulation context](apply-sensitivity-label-automatically#review-coverage-by-simulation-context) helps compare those outcomes with the latest simulation; it isn't an exact reconciliation or an all-time policy total.

These distinctions don't explain a stalled simulation, a source view that fails to open, or results that remain inconsistent after the relevant checks. Use the [auto-labeling troubleshooting guidance](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/troubleshoot-auto-labeling-policies) and contact Microsoft Support if the issue persists.