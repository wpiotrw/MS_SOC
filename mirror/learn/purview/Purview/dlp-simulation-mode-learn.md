---
layout: Conceptual
title: Learn about data loss prevention simulation mode | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-03-27T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
search.appverid:
- MET150
description: Learn about the foundational concepts of Microsoft Purview Data Loss Prevention policy simulation mode
locale: en-us
document_id: 7dcdb47d-63a1-7750-6158-12fd7a3666b6
document_version_independent_id: 7dcdb47d-63a1-7750-6158-12fd7a3666b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-simulation-mode-learn.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-simulation-mode-learn
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-simulation-mode-learn.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: f344b297-6eed-b551-82b2-2041fcbff23a
---

# Learn about data loss prevention simulation mode | Microsoft Learn

**Run the policy in simulation mode**, otherwise known as simulation mode, for Microsoft Purview Data Loss Prevention (DLP) policies replaces the **Test** and **Test with policy tips** policy states. When a policy is in simulation mode, it's run as if it were being enforced, without any actual enforcement. Unlike the **Test** modes, all matched items and alerts are reported in a separate dashboard. This makes it easy to see the impact of the policy before you enforce it by keeping all the simulation results separate from the results of policies that are being enforced.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

Simulation mode provides:

- An isolated experience to run and assess policies.
- A summary dashboard that gives you visibility into the impact of the policies across different locations and shows which items were matched.
- A flat list of matched items at a policy level.

Simulation mode for DLP policies is a tool you can use for [tuning your data loss prevention policies](dlp-test-dlp-policies) at any time. You should incorporate it into your [policy creation and deployment](dlp-create-deploy-policy) process. Using simulation mode to tune a policy reduces false positives without impact to your users or business processes. Use it as part of your deployment process for new policies, use it to test changes to existing policies before enforcing those changes in production.

For example:

DLP policy *Protect Credit Cards v1* is in production, but is throwing too many false positives. You think you know what is wrong, but you don't want to experiment with changes to it in production to find out. You can make a copy of policy *Protect Credit Cards v1*, call it *Protect Credit Cards v2*, make tuning changes, and then run *v2* in simulation mode. If it the changes have the desired result, then you can turn off *v1* and set *v2* to enforce mode.

Important

Simulations can run for up to 15 days so the results are not a point in time snapshot. For SharePoint Online and OneDrive for Business locations, all existing and new/changed items are evaluated. For Exchange, Teams, Devices locations only items that are new during simulation are evaluated. Fabric items that are updated or refreshed after a simulation starts are evaluated. Data from a simulation run is kept for 30 days.

## Placing a policy in simulation mode

See [Get started with the data loss prevention simulation mode](dlp-simulation-mode-get-started) for the procedures to manage simulation mode for a policy.

## Simulation results

See [Get started with the data loss prevention simulation mode](dlp-simulation-mode-get-started) for the steps to access simulation results. Simulation results are presented across three pages.

### Simulation overview

The **Simulation overview** tab gives you basic information on:

- the status of the policy simulation (complete, in progress or expired)
- status of scanning per location
- total items scanned
- total matches found
- matched items for each location
- links to the matched items

and other information.

![a screenshot of the simulation overview tab. It shows the progress of the simulation, total items scanned, and total matches and presents other controls](media/dlp-sim-mode-sim-overview.png)

## Items for review

The **Items for review** tab shows a flat list of the items that matched the policy in simulation and lets you read the source item along with item metadata much like [Content explorer](data-classification-content-explorer).

![a screenshot of the items to review tab. It shows a flat list of items that matched the policy in simulation and lets you read the source item along with item metadata](media/dlp-sim-mode-sim-items.png)

## Alerts

The simulation mode alerts tab shows a flat list of all the alerts that were generated when an item matched the policy in simulation. It has the same format as the [DLP alerts console](dlp-alerts-dashboard-get-started).

![a screenshot of the simulation alerts tab. It shows a flat list of all the alerts that were generated when an item matched the policy in simulation. It has the same format as the DLP alerts console](media/dlp-sim-mode-sim-alerts.png)

Important

While a policy is in simulation mode, all simulation alerts are only surfaced in the simulation alerts tab. They don't show up in the DLP alerts console and they don't flow into the Microsoft Defender portal.