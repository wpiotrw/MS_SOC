---
layout: Conceptual
title: Get started with Service Groups - Azure Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/service-groups/overview
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
description: Learn how to use and manage resources with Service Groups.
ms.topic: overview
ms.date: 2025-05-19T00:00:00.0000000Z
ms.custom:
- build-2025
locale: en-us
document_id: c3b78314-12c8-5258-4127-fb0ca4a72ba0
document_version_independent_id: 13a5d5f3-2abc-31c5-31e4-4989e2224486
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/service-groups/overview.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/service-groups/overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/service-groups/overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: b84d6ffe-7c02-6669-e162-77af0345711b
---

# Get started with Service Groups - Azure Governance | Microsoft Learn

Azure Service Groups enable you to create flexible, custom groupings of Azure resources across subscriptions and resource groups without changing the existing resource hierarchy. Use them to build virtual folders of resources for specific teams, projects, or workloads, giving each group its own view with minimal permissions.

Service Groups are ideal for scenarios that require cross-boundary grouping, low privileged permissions, and aggregations of data across resources. By using these features, teams can create tailored resource collections that align with operational, organizational, or persona-based needs. This article provides an overview of Service Groups, scenarios for using them, and important facts.

Important

Azure Service Groups is currently in public preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

## Why use Service Groups?

Service Groups solve a common challenge: your Azure resource hierarchy (Management Groups → Subscriptions → Resource Groups) may not reflect how your teams actually work. For example:

- A **platform team** needs to see all networking resources across dozens of subscriptions.
- A **project lead** wants a single dashboard for resources spanning production, staging, and development environments.
- An **application engineer** needs to track a set of resources for lifecycle and management.

With Service Groups, you can create these views without reorganizing your subscriptions or requesting broad permissions. Resources can belong to **multiple** service groups simultaneously, and access on service groups doesn't grant access to the underlying resources.

### When to use Service Groups vs. other groupings

| Feature | Service Groups | Management Groups | Resource Groups | Tags |
| --- | --- | --- | --- | --- |
| **Purpose** | Flexible cross-boundary views and data aggregation | Governance hierarchy and policy inheritance | Resource lifecycle management | Resource level Metadata labeling |
| **Scope** | Resources, resource groups, and subscriptions | Subscriptions only | Within a singular subscription | Individual resources |
| **Multiple membership** | Yes — a resource can belong to many service groups | No — one parent only | No — one resource group only | Yes — multiple tags per resource |
| **Permission inheritance** | Only between parent/child service groups | Yes — to subscriptions and resources | Yes — to resources | No |

Use **Service Groups** when you need to create different topologies across multiple subscriptions without affecting governance or deployment. Use **Management Groups** for at-scale high privileged operations such as applying policies and RBAC across subscriptions. Use **Resource Groups** for managing the deployment and lifecycle of closely related resources. Use **Tags** for resource level metadata identification.

## Prerequisites

- An Azure account with an active subscription. [Create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Review the Role Based Access Controls section to understand which built-in roles are available.

## Key capabilities

- **Multiple Hierarchies**: Service Groups enable scenarios where the resources can be grouped in different topologies for multiple purposes.
- **Flexible Membership**: Service Groups allow resources from different subscriptions to be grouped together, providing a unified view and management capabilities. They also allow the grouping of subscriptions, resource groups, and resources. The same resources can be connected to many different service groups allowing different customer personas and scenarios to be created and used.
- **Low Privilege Management**: Service Groups are designed to operate with low privilege permissions, ensuring that users can manage resources without needing excessive access rights.

### Example Scenarios

Customers can create many different views that support how they organize their resources.

- Unified View of Resources

    - Organizations with multiple applications and environments can use Service Groups to create a centralized view of resource information across different environments. Member resources or resource containers from various environments within different management groups or subscriptions can be linked to a single Service Group, providing a unified reference point for resource details.
    - Since Service Groups don’t inherit permissions from their members, customers can apply least-privilege principles to assign permissions on the Service Groups that allow viewing of resource information. This capability enables scenarios where users can access and review the Service Group, but not access or alter the resources directly.
- Creating Inventory

    - Customers can connect resources to the Service Groups to get a consolidated view of all the resources of a particular type or function in the entire environment.
    - Showcase ownership and identification boundaries.

[![Diagram showing the Management Group and Service Group Hierarchies within the Microsoft Entra Tenant](media/side-by-side.png)](media/side-by-side.png#lightbox)

- Varying Personas
    - With Service Groups, organizations have the ability to manage multiple hierarchies over the same resources for different personas and their own individual views. Customers can use the same resources to be members of a Workload Service Group, a Department Service Group, and a Service Group with all Production resources.

[![Diagram that shows multiple service group branches.](media/multiple-service-group.png)](media/multiple-service-group.png#lightbox)

## How it works

Azure Service Groups are created at the tenant level to allow to span the complete hierarchy. The separation from Management Groups, Subscriptions, and Resource Groups allows Service Groups to be connected many times to different resources and resource containers without impacting the existing structures.

Information about Service Groups

- A Service Group is created within the Microsoft.Management Resource Provider.
- Service Groups allow self nesting to create up to 10 "levels" of grouping depth. Nesting can be managed via the 'parent' property within the Service Group resource.
- Role assignments on the Service Group can be inherited to the **child Service Groups only**. There's **no RBAC inheritance** through the memberships to the resources or resource containers.
- There's a limit of 2000 service group members per subscription.
- There's a limit of 10,000 Service Groups in a single tenant.
- Service Groups and Service Group Member IDs support up to 250 characters. They can be alphanumeric and special characters: - \_ ( ). ~
- Service Groups require a globally unique ID. Two Microsoft tenants can't have a Service Group with the same IDs.
- Membership to Service Groups are managed by the 'Microsoft.Relationship/ServiceGroupMember' on the desired member (a resource, resource group, or subscription) with reference to the desired Service Group.

## Azure Resource Manager Groupings

Azure offers a wide variety of resources containers that enable our customers to manage resources at many different scales. Service Groups is only the newest in a family of Azure Resource Manager (ARM) containers used to organize your environment.

This table shows a summary of the differences between the groups.

### Scenario comparison

| Scenario | [Resource Group](/en-us/azure/azure-resource-manager/management/overview#resource-groups) | [Subscription](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-subscription-limits) | [Management Group](https://www.learn.microsoft.com/azure/governance/management-groups/overview) | [Service Group](/en-us/azure/governance/service-groups/overview) | [Tags](/en-us/azure/azure-resource-manager/management/tag-resources) |
| --- | --- | --- | --- | --- | --- |
| Required inheritance from assignment on scope to each member/descendant resource | Supported | Supported | Supported | Not Supported | Not Supported |
| Consolidation of resources for reduction of Role Assignments/Policy Assignments | Supported | Supported | Supported | Not Supported | Not Supported\* |
| Grouping of resources that are shared across scope boundaries. Ex. Global Networking resources in one subscription/resource group that are shared across multiple applications that have their own subscriptions/resource groups. | Not Supported | Not Supported | Not Supported | Supported | Not Supported\*\* |

\*: Azure tags can be used as criteria within Azure Policy to apply policies to certain resources. Azure tags are subject to limitations.

\*\*: Tags can be applied across scopes and are added to resources individually. However, Tags do not serve as a first-class grouping.

## The Root Service Group

Service groups, like management groups, have one root service group. This root service group is the top parent of all service groups in the tenant. The root service group's ID is the same as its tenant ID.

Service Groups creates the Root Service Group on the first request received within the Tenant and users can't create or update the root service group. *"/providers/microsoft.management/servicegroups/[tenantId]"*

Access to the root has to be given from a user with "microsoft.authorization/roleassignments/write" permissions at the tenant level. For example, the Tenant's Global Administrator can elevate their access on the tenant to have these permissions. [Details on elevating Tenant Global Administrator Accesses](../../role-based-access-control/elevate-access-global-admin)

## Role Based Access Controls

There are three built-in roles definitions to support Service Groups in the preview.

Note

Custom Role Based Access Controls aren't supported during the Preview.

- [Service Group Administrator](../../role-based-access-control/built-in-roles/management-and-governance#service-group-administrator): This built-in role manages all aspects of Service Groups and Relationships and is the *default role* given to users when they create a Service Group.
- [Service Group Contributor](../../role-based-access-control/built-in-roles/management-and-governance#service-group-contributor): This built-in role should be given to users when they need to create or manage the lifecycle of a Service Group. This role allows for all actions except for Role Assignment capabilities.
- [Service Group Reader](../../role-based-access-control/built-in-roles/management-and-governance#service-group-reader): This built-in role provides read-only access to service group information and can be assigned to other resources in order to view the connected relationships.

Anyone with valid permissions within the tenant can create a service group under the root. The user who creates the service group becomes the **Service Group Administrator**. To edit the service group or create child service groups, a user must have **Service Group Contributor** at that service group. To add members, users must have **Service Group Contributor** on the service group and `Microsoft.Relationship/write` on the resource.