---
layout: Conceptual
title: Microsoft Security Copilot Security Compute Units and capacity | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about what Security Copilot Security Compute Units are and how capacity works
ms.date: 2026-04-28T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 9be99ebc-acda-307f-0580-b632b4dc9a78
document_version_independent_id: 9be99ebc-acda-307f-0580-b632b4dc9a78
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/security-compute-units-capacity.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: security-compute-units-capacity
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/security-compute-units-capacity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: c18785e8-1ef4-953d-fa84-926efcee522d
---

# Microsoft Security Copilot Security Compute Units and capacity | Microsoft Learn

Security Compute Units (SCUs) are the compute resources that power Microsoft Security Copilot experiences. This article explains how SCU capacity works, compares provisioned, overage, and Microsoft 365 E5 and E7 inclusion models, and covers billing and monitoring so you can choose the right setup for your organization.

## Security compute units

Security Compute Units (SCUs) represent the compute capacity required to run Security Copilot workloads. SCUs are the units of compute resources needed to deliver dependable and consistent performance across Security Copilot experiences.

You consume SCUs in the following scenarios:

- Using the Security Copilot standalone portal
- Running embedded Security Copilot experiences
- Invoking Security Copilot through Microsoft‑developed agents
- Invoking Security Copilot through partner‑developed agents
- Running other Security Copilot features and capabilities

Depending on your scenario and licenses, you might need to provision or purchase SCUs to use Security Copilot.

For eligible and onboarded Microsoft 365 E5 customers, Security Copilot is auto provisioned with a default capacity. Non-Microsoft 365 E5 customers need to purchase SCUs by provisioning them.

## Capacity

Capacity in Security Copilot refers to the computational resources provisioned to run the service, measured in SCUs. You can scale capacity up or down and monitor usage over time to ensure you have the right level of SCUs for your organization’s needs. For more information, see [Managing usage](manage-usage).

### Non-Microsoft 365 E5 and E7 customers

Provisioned capacity is the baseline allocation of SCUs that you set up to support your organization’s ongoing use of Security Copilot. You must provision this capacity before you can use Security Copilot.

Overage capacity provides additional SCUs when your usage exceeds your provisioned capacity, such as during peak investigation periods. You can add overage capacity on top of your provisioned capacity to maintain uninterrupted access when demand increases.

The following section provides information about provisioned and overage capacity.

#### Provisioned capacity

**Key characteristics**

- SCUs are provisioned in advance (minimum of one SCU)
- Capacity refreshes every full billing hour (for example, 9:00–10:00)
- Unused SCUs expire at the end of the hour and don't roll over
    - Example: If you set up a capacity plan with three SCUs, you get three SCUs each full hour. Refresh happens on fixed clock-hour blocks (9:00–10:00, 10:00–11:00), not rolling blocks (11:05–12:05).
- If provisioned SCUs run out, Security Copilot requests stop unless another capacity type is available

Provisioned capacity is billed per hour and is best for steady, predictable usage.

For more information, see How provisioned and overage SCUs are billed.

#### Overage capacity

**Key characteristics**

- SCUs are consumed as used
- Capacity is consumed as Security Copilot activity occurs
- Can be configured with a maximum limit or set to unlimited

Overage capacity helps absorb unexpected usage spikes without requiring extra hourly provisioning.

For more information, see How provisioned and overage SCUs are billed.

### Microsoft 365 E5 and E7 customers

**Default Security Copilot Capacity** is the automatically created inclusion capacity that appears in your tenant when Security Copilot inclusion is enabled through Microsoft 365 E5 and E7. For more information, see [Understand how Security Copilot is auto provisioned for Microsoft 365 E5 and E7 customers](auto-provisioning-security-copilot).

## How provisioned and overage SCUs are billed

Security Copilot operates on a provisioned and overage capacity. Provisioned capacity is billed by the hour while the overage capacity is billed on usage.

You can flexibly provision Security Compute Units (SCUs) to accommodate regular workloads and adjust them anytime without long-term commitments.

To manage unexpected demand spikes, you can set an overage amount to ensure that extra SCUs are available when initially provisioned units are depleted during unexpected workload spikes. Overage units are billed on-demand and can be set as unlimited or a maximum amount. This approach enables predictable billing while providing the flexibility to handle both regular and unexpected usage.

### Provisioned capacity billing

Billing is calculated on hourly blocks based on provisioned capacity rather than by 60-minute increments and has a minimum of one hour. Any usage consumed within the same hour is billed as a full SCU for provisioned capacity, regardless of start or end times within that hour.

For more information, see [Microsoft Security Copilot pricing](https://aka.ms/CopilotforSecurity_Pricing) and the [Pricing calculator](https://azure.microsoft.com/pricing/calculator/?service=microsoft-copilot-for-security) page.

### Overage capacity billing

For overage units, SCUs are billed up to one decimal increments for the exact consumed units. Consumed units aren't rounded up to whole numbers. This means that you're charged precisely based on your usage (to one decimal place).

For instance, if you provision an SCU at 9:05 a.m., then deprovision it at 9:35 am, and then provision another SCU at 9:45 am, you are charged for two units within the 9:00 a.m. to 10:00 a.m. hour. To maximize usage, make SCU provisioning changes at the beginning of the hour. For more information, see [Manage usage](manage-usage).

For more information, see [Microsoft Security Copilot pricing](https://aka.ms/CopilotforSecurity_Pricing) and the [Pricing calculator](https://azure.microsoft.com/pricing/calculator/?service=microsoft-copilot-for-security) page.

### Example billing scenarios for overages

This section provides some scenarios to illustrate how overages are billed.

An enterprise company provisioned four SCUs and set an overage limit of six SCUs to stay within the monthly budget.

- **Scenario 1**:

    - A user runs a prompt consuming 3 SCUs and uses the incident summarization in Defender consuming 0.5 SCU.
    - The total consumption is calculated as 3.5 SCUs. However, the charge for that hour will be based on four provisioned SCUs.

    | Activity | SCU consumed |
    | --- | --- |
    | Runs a prompt | 3.0 SCUs |
    | Uses incident feature | 0.5 SCU |
    | **Total Consumption** | 3.5 SCUs |
- **Scenario 2**:

    - Building on Scenario 1, a user also runs a promptbook consuming an additional 3.7 SCUs, bringing the total to 7.2 SCUs for the hour.
    - The charge for that hour will now be based on four provisioned SCUs, and 3.2 overage SCUs.

    | Activity | SCU consumed |
    | --- | --- |
    | Runs a prompt | 3.0 SCUs |
    | Uses incident feature | 0.5 SCU |
    | Runs a promptbook | 3.7 SCUs |
    | **Total Consumption** | 7.2 SCUs |

## Managing and monitoring capacity

You can manage Security Copilot capacity by increasing or decreasing provisioned SCUs through the Azure portal or the Security Copilot portal. Security Copilot also provides a usage monitoring dashboard for tracking consumption over time.

For more information, see [Managing usage](manage-usage).