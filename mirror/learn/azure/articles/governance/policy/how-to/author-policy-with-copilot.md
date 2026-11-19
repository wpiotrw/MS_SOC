---
layout: Conceptual
title: Create and test Azure Policy definitions with Azure Copilot (preview) - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/how-to/author-policy-with-copilot
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
description: Learn how to generate an Azure Policy definition with Azure Copilot, review the policy rule, and simulate its behavior before assigning it.
ms.date: 2026-11-10T00:00:00.0000000Z
ms.topic: how-to
ms.collection: ce-skilling-ai-copilot
locale: en-us
document_id: 5b5b3f21-3923-ba3f-1ecc-51796bd86223
document_version_independent_id: 15b6f834-b35c-e861-7d35-e56660d51001
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/how-to/author-policy-with-copilot.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/how-to/author-policy-with-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/how-to/author-policy-with-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 31cd0a30-139a-178d-9148-f408a7faecc0
---

# Create and test Azure Policy definitions with Azure Copilot (preview) - Azure Policy | Microsoft Learn

Azure Copilot in Azure Policy helps you turn a plain-language requirement into a custom policy definition. You can review and refine the generated policy rule, then use policy simulation to check its behavior against specific resources before you assign it.

This article walks through generating an audit policy and testing it in the Azure portal.

Note

Policy authoring with Azure Copilot and policy simulation are preview features. You need access to the preview to follow these steps.

## Prerequisites

- An Azure account with an active subscription.
- Access to Azure Copilot. For more information, see [Manage access to Azure Copilot](/en-us/azure/copilot/manage-access).
- Permission to create policy definitions at the selected subscription or management group. For example, the [Resource Policy Contributor](/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#resource-policy-contributor) role provides this permission.
- Read access to the scope and resources you use for simulation.

Before creating a custom definition, check the [built-in policy samples](/en-us/azure/governance/policy/samples/built-in-policies) for a policy that already meets your needs.

## Generate a policy definition

1. Sign in to the [Azure portal](https://portal.azure.com). Search for and select **Policy**.
2. Under **Authoring**, select **Definitions**, and then select **+ Policy definition**.
3. Select **Generate with Copilot**. In **Policy target description**, describe the resource type and the condition you want to check. For example:

> 
> Audit storage accounts that allow HTTP traffic instead of requiring secure transfer.
4. Select **Generate**.
5. Review the generated JSON in **Policy rule**. Check the resource type, aliases, conditions, parameters, and effect against your requirement.

Important

AI-generated policy rules can be incorrect or incomplete. Review and test the rule before assigning it, especially when you use an effect that blocks or changes resources.

## Simulate the policy

1. In the policy-definition creation experience, open the **Simulate policy** tab.
2. Select up to five representative resources from the scope you chose for the definition. For the storage-account example, select a storage account whose secure-transfer setting you know.
3. Run the simulation. Review the compliance result, effect details, and evaluated expressions to understand why the resource matches or doesn't match the policy.
4. Repeat with resources that should pass and resources that should fail. Update the policy rule and rerun the simulation if the results don't match your intent.
5. Save the definition when you're satisfied with the results. Creating a definition doesn't enforce it. When you're ready to roll it out, [create a policy assignment](../assign-policy-portal) and follow [safe deployment practices](policy-safe-deployment-practices).

Simulation tests the resources you select, not every resource in the scope. It doesn't create an assignment or change the resources. You can also simulate an existing policy rule without generating it with Copilot.