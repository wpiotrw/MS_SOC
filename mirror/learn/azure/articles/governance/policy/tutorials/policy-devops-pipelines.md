---
layout: Conceptual
title: 'Tutorial: Implement Azure Policy with Azure DevOps - Azure Policy | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/policy-devops-pipelines
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
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
author: kgremban
learn_banner_products:
- azure
ms.author: kgremban
ms.service: azure-policy
ms.reviewer: kgremban
description: In this tutorial, you implement an Azure Policy with an Azure DevOps release pipeline.
ms.date: 2025-03-04T00:00:00.0000000Z
ms.topic: tutorial
ms.custom:
- devops-pipelines-deploy
- sfi-image-nochange
locale: en-us
document_id: 04b85d1c-9aec-02bf-097d-a90103ab1490
document_version_independent_id: db855997-4017-d31e-4743-ff090b892d59
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/tutorials/policy-devops-pipelines.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/tutorials/policy-devops-pipelines
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/tutorials/policy-devops-pipelines.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/5bd2b3fa-c186-4b92-a3c8-09f22a249d37
- https://authoring-docs-microsoft.poolparty.biz/devrel/7960090f-b1c1-4f33-accd-7f42c377c619
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/7eba7926-b7b2-4a7a-bf89-e6ac53b3e7f6
- https://authoring-docs-microsoft.poolparty.biz/devrel/61f08768-d46a-4092-af3e-b449ce915a2b
platformId: 44db3101-639f-dbc9-12e9-0b6d868be12b
---

# Tutorial: Implement Azure Policy with Azure DevOps - Azure Policy | Microsoft Learn

**Azure DevOps Services**

Learn how to enforce compliance policies on your Azure resources before and after deployment with Azure Pipelines. Azure Pipelines lets you build, test, and deploy with continuous integration (CI) and continuous delivery (CD) using [Azure DevOps](/en-us/azure/devops/). One scenario for adding Azure Policy to a pipeline is when you want to ensure that resources are deployed only to authorized regions and are configured to send diagnostics logs to Azure Log Analytics.

You can use either the [classic pipeline](/en-us/azure/devops/pipelines/release/define-multistage-release-process) or [YAML pipeline](/en-us/azure/devops/pipelines/get-started/yaml-pipeline-editor) processes to implement Azure Policy in your CI/CD pipelines.

For more information, see [What is Azure Pipelines?](/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines) and [Create your first pipeline](/en-us/azure/devops/pipelines/create-first-pipeline).

## Prepare

1. Create an [Azure Policy](create-and-manage) in the Azure portal. There are several [predefined sample policies](/en-us/azure/governance/policy/samples/index) that can be applied to a management group, subscription, and resource group.
2. In Azure DevOps, create a release pipeline that contains at least one stage, or open an existing release pipeline.
3. Add a pre- or post-deployment condition that includes the **Check Azure Policy compliance** task as a gate. [More details](/en-us/azure/devops/pipelines/release/deploy-using-approvals#set-up-gates).

    ![Screenshot of Azure Policy Gate.](../media/devops-policy/azure-policy-gate.png)

If you're using a YAML pipeline definition, then use the [AzurePolicyCheckGate@0](/en-us/azure/devops/pipelines/tasks/reference/azure-policy-check-gate-v0) Azure Pipelines task.

## Validate for any violation(s) during a release

Note

Use the [AzurePolicyCheckGate](/en-us/azure/devops/pipelines/tasks/deploy/azure-policy) task to check for policy compliance in YAML. This task can only be used as a gate and not in a build or a release pipeline.

1. Navigate to your team project in Azure DevOps.
2. In the **Pipelines** section, open the **Releases** page and create a new release.
3. Choose the **In progress** link in the release view to open the live logs page.
4. When the release is in progress and attempts to perform an action disallowed by the defined policy, the deployment is marked as **Failed**. The error message contains a link to view the policy violations.

    ![Screenshot of Azure Policy failure message.](../media/devops-policy/azure-policy-02.png)
5. An error message is written to the logs and displayed in the stage status panel in the releases page of Azure Pipelines.

    ![Screenshot of Azure Policy failure in log.](../media/devops-policy/azure-policy-03.png)
6. When the policy compliance gate passes the release, a **Succeeded** status is displayed.

    ![Screenshot of Policy Gates.](../media/devops-policy/policy-compliance-gates.png)
7. Choose the successful deployment to view the detailed logs.

    ![Screenshot of Policy Logs.](../media/devops-policy/policy-logs.png)