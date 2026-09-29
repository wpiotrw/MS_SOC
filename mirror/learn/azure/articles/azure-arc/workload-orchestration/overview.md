---
layout: Conceptual
title: What Is Workload Orchestration? - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/workload-orchestration/overview
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: sethmanheim
learn_banner_products:
- azure
manager: lizross
ms.author: sethm
ms.service: azure-arc
ms.subservice: workload-orchestration
description: Workload orchestration is a cross-platform orchestrator for managing edge workloads using an Azure control plane.
ms.topic: overview
ms.date: 2025-06-22T00:00:00.0000000Z
ms.custom:
- build-2025
locale: en-us
document_id: e9225ed4-897c-1520-f576-5847dc7502f7
document_version_independent_id: 946782b9-1ec3-b9a3-0d5e-b46cd6984cc8
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/workload-orchestration/overview.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/workload-orchestration/overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/workload-orchestration/overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 02d6a312-05c9-70a1-367b-603efd17423f
---

# What Is Workload Orchestration? - Azure Arc | Microsoft Learn

Workload orchestration is a centralized approach to deploying, configuring, and managing application workloads across distributed environments—including cloud, on-premises, and edge. It enables teams to define the desired state of their applications, such as the Helm chart, version, configuration parameters, and target environments, and ensures that state is consistently achieved and maintained at scale.

## Key features of workload orchestration

- **Centralized deployment:** Deploy applications across multiple clusters from a single control plane, eliminating manual on-site operations.
- **Configuration management:** Apply environment-specific configurations while maintaining a consistent deployment blueprint.
- **Lifecycle management:** Handle upgrades, rollbacks, and version control seamlessly for all deployments.
- **Scalability:** Rapidly scale application rollouts across thousands of sites with minimal operational overhead.
- **Observability:** Monitor deployment status, workload health, and compliance from a [centralized dashboard](https://portal.digitaloperations.configmanager.azure.com).

## Operation model

Workload orchestration operates in two key steps:

1. Setup: It is a one-time operation that prepares your environment for workload deployments. It involves initializing workload orchestration on your existing Kubernetes infrastructure and provisioning targets that map to particular namespaces within the clusters where the applications are to be deployed.
2. Deploy: With setup in place, you can begin deploying applications consistently across your targets. This involves creating a blueprint (or template) for the application to be deployed, and leveraging the same consistently across all relevant targets.

To get started with workload orchestration, refer to the [setup guide](set-up-workload-orchestration).

## Contact support

For feedback, submit your comments through the [WOFeedback form](https://aka.ms/WOFeedback).

To report issues, use the [WOReportIssues form](https://aka.ms/WOReportingIssues).