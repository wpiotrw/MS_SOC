---
layout: Conceptual
title: Best practices for Azure Service Groups - Azure Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/service-groups/best-practices
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: kenieva
learn_banner_products:
- azure
ms.author: kenieva
ms.service: azure-policy
description: Learn recommended practices for adopting Azure Service Groups, including how to divide responsibilities between a central platform team and application teams, and the benefits of a shared service-centric model.
ms.topic: how-to
ms.date: 2026-11-04T00:00:00.0000000Z
locale: en-us
document_id: 519b062c-6c72-98c2-8ea7-4a5731b120b0
document_version_independent_id: 73bd1a57-4851-a2c5-b786-6643f840c6ea
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/service-groups/best-practices.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/service-groups/best-practices
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/service-groups/best-practices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 88c35e38-eb26-492e-255b-668e40b72a77
---

# Best practices for Azure Service Groups - Azure Governance | Microsoft Learn

As your organization grows in Azure, you might find that your org chart, deployment hierarchy, cost model, and operational views don't align. You might spread mission-critical resources across subscriptions, resource groups, regions, and ownership boundaries. This distribution can make it difficult to answer simple questions like "what makes up this application?" or "who owns this service?"

This article shares recommended practices for adopting [Azure Service Groups](overview). It covers how to divide responsibilities between a central platform team and application teams and a recommended path for adopting Service Groups at scale.

## Why a shared model matters

Different teams need different views of the same resources:

- A **platform or cloud operations team** needs a consistent hierarchy standard to keep inventory, security, and cost reporting accurate.
- A **security team** needs to understand boundaries and blast radius without being granted access to every resource.
- A **cost owner** needs an all-up view of spend for an application that might span dozens of subscriptions.
- An **application or workload team** needs to manage and monitor *their* service, regardless of how its resources are distributed across the resource hierarchy.

Azure Service Groups address this challenge by adding a flexible, service-centric lens on top of your existing hierarchy, without requiring you to redesign management groups, subscriptions, or resource groups. Because a resource can belong to **multiple service groups at the same time**, a central team's governance tree and an application team's "my service" tree can coexist over the same resources without conflict. This shared, non-exclusive membership model is the biggest difference from other Azure scopes where a resource can only have one parent.

## Define roles and responsibilities

Organizations that get the most value from Service Groups explicitly divide responsibilities between a central team and application teams, rather than leaving every team to model resources on its own.

### Central (platform) team responsibilities

The central, or platform, team owns the standards and automation that keep service groups consistent and trustworthy across the organization:

- **Define the standards.** Agree on a naming convention, a tiering model (for example, criticality tier), and the metadata every service group should carry, such as owner, environment, and cost center as tags.
- **Own the top of the hierarchy.** Manage the root and upper levels of the service group tree, and decide how broad or deep (up to 10 levels) the hierarchy should go.
- **Automate discovery and membership.** Use [Azure Policy to deploy service group membership automatically](manage-membership#using-azure-policy-for-automatic-membership) based on tags or naming conventions, and use [Azure Resource Graph queries](manage-membership#creating-memberships-based-on-a-resource-graph-query) to find and add resources in bulk, instead of relying on every team to tag and add members by hand.
- **Grant least-privilege access.** Use the [built-in roles](overview#role-based-access-controls) to give broad read access (Service Group Reader) for visibility, and reserve the Contributor or Administrator roles for teams that need to manage lifecycle or membership. Remember that access to a service group doesn't grant access to its members.
- **Report centrally, act locally.** Use the aggregated membership data in Azure Resource Graph to report such as Azure Policy compliance and operational readiness (such as zone resiliency, backup, and disaster recovery coverage).
- **Partner with application teams** to validate that ownership and tiering metadata reflects reality, and revisit the model as the organization changes.

### Application (workload) team responsibilities

Application teams get the most value when they treat their service group as the map of their own application, independent of how its resources happen to be deployed:

- **Model the application as it operates**, not as it's deployed. Create a service group, or a tree of service groups, that mirrors your components, tiers, and dependencies, even if the underlying resources span multiple subscriptions or resource groups.
- **Add resources as members** by following the central team's naming and tagging conventions so automated policies pick them up, or by [adding members directly](create-service-group-member-portal) when automation doesn't fit.
- **Keep membership current.** Update membership through code or CI/CD alongside deployments (see [Manage membership at scale](manage-membership)) instead of treating it as a one-time, manual exercise.
- **Use the service group as a single pane of glass** for [monitoring health, alerts, and dependencies](monitoring) across the application, rather than stitching together separate views per subscription.
- **Request only the access needed.** A Service Group Contributor role on the team's own group, plus the `Microsoft.Relationship/write` permission on its resources, is usually enough to manage membership — subscription-level access isn't required.

## Recommended adoption path

Instead of modeling every resource in the tenant on day one, organizations that successfully adopt Service Groups tend to follow a similar path:

1. **Start with a few critical services.** Choose one or two visible applications with known mission-critical resources and clear owners as a pilot.
2. **Standardize the tree.** Agree on a tiering model and naming convention with the pilot application teams before scaling further. Model tiers and membership without changing any existing deployment scopes.
3. **Automate membership.** Replace manual, one-off membership updates with [Azure Policy-based automation or Resource Graph-driven scripts](manage-membership) so new resources are enrolled automatically as teams tag or deploy them.
4. **Connect reporting and monitoring.** Layer in [Azure Resource Graph queries](resource-graph-samples) and [Azure Monitor](monitoring) so both the central team and application teams get value from the same membership data, instead of maintaining separate inventories.
5. **Review and expand.** Periodically review coverage, ownership, and access with application teams, then expand the model to more services once the pattern is proven.