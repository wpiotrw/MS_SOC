---
layout: Conceptual
title: Plan and Deploy Azure Arc-Enabled Servers - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/plan-at-scale-deployment
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
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to enable a large number of machines to Azure Arc-enabled servers to simplify configuration of essential security, management, and monitoring capabilities in Azure.
ms.date: 2025-05-08T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: 297753ce-0861-7dbb-7eb2-1f7b8d29ac73
document_version_independent_id: fd645122-e5fb-0f61-9150-2bf8b02c316a
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/plan-at-scale-deployment.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/plan-at-scale-deployment
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/plan-at-scale-deployment.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 7c81cbdc-9e83-677e-ad28-81736bb41169
---

# Plan and Deploy Azure Arc-Enabled Servers - Azure Arc | Microsoft Learn

Deployment of an IT infrastructure service or business application is a challenge for any company. To execute it well and avoid any unwelcome surprises and unplanned costs, you need to thoroughly plan for it to ensure that you're as ready as possible. A plan for deploying Azure Arc-enabled servers at any scale should cover the design and deployment criteria that need to be met to complete the tasks successfully.

For the deployment to proceed smoothly, your plan should establish a clear understanding of:

- Roles and responsibilities.
- Inventory of physical servers or virtual machines (VMs) to verify that they meet network and system requirements.
- The skill set and training required to enable successful deployment and ongoing management.
- Acceptance criteria and how you track its success.
- Tools or methods to be used to automate the deployments.
- Identified risks and mitigation plans to avoid delays and disruptions.
- A plan to avoid disruption during deployment.
- The escalation path when a significant issue occurs.

This article helps you prepare for a successful deployment of Azure Arc-enabled servers across multiple production physical servers or VMs in your environment.

To learn more about our at-scale deployment recommendations, you can also refer to this video.

## Prerequisites

Consider the following basic requirements when you plan your deployment:

- To support your deployment, your machines must run a [supported operating system](prerequisites#supported-operating-systems) for the Azure Connected Machine agent.
- To connect your deployment, your machines must have connectivity from your on-premises network or other cloud environment to resources in Azure, either directly or through a proxy server.
- To install and configure the Connected Machine agent, you must have an account with elevated privileges (that is, an administrator or as root) on the machines.
- To onboard machines, you must have the Azure Connected Machine Onboarding built-in role.
- To read, modify, and delete a machine, you must have the Azure Connected Machine Resource Administrator built-in role.

For more information, see the [prerequisites](prerequisites) and [network requirements](network-requirements) for installing the Connected Machine agent.

### Azure subscription and service limits

There are no limits to the number of Azure Arc-enabled servers that you can register in any single resource group, subscription, or tenant.

Each Azure Arc-enabled server is associated with a Microsoft Entra object and counts against your directory quota. For information about the maximum number of objects you can have in a Microsoft Entra directory, see [Microsoft Entra service limits and restrictions](/en-us/azure/active-directory/enterprise-users/directory-service-limits-restrictions).

## Pilot

Before you deploy to all production machines, start by evaluating the deployment process before you adopt it broadly in your environment. For a pilot, identify a representative sampling of machines that aren't critical to your company's ability to conduct business. Be sure to allow enough time to run the pilot and assess its impact. We recommend a minimum of 30 days.

Establish a formal plan to describe the scope and details of the pilot. Your plan should generally include the following items:

- **Objectives**: Describes the business and technical drivers that led to the decision that a pilot is necessary.
- **Selection criteria**: Specifies the criteria used to select which aspects of the solution that the pilot demonstrates.
- **Scope**: Describes the scope of the pilot, which includes but isn't limited to solution components, anticipated schedule, duration of the pilot, and number of machines to target.
- **Success criteria and metrics**: Defines the pilot's success criteria and specific measures used to determine level of success.
- **Training plan**: Describes the plan for training system engineers, administrators, etc. who are new to Azure and its services during the pilot.
- **Transition plan**: Describes the strategy and criteria used to guide transition from pilot to production.
- **Rollback**: Describes the procedures for rolling back a pilot to predeployment state.
- **Risks**: Lists all identified risks for conducting the pilot and that are associated with production deployment.

## Phase 1: Build a foundation

In this phase, system engineers or administrators enable the core features in their organization's Azure subscription to start the foundation before they enable machines for management by Azure Arc-enabled servers and other Azure services.

| Task | Detail | Estimated duration |
| --- | --- | --- |
| [Create a resource group](/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups). | A dedicated resource group to include only Azure Arc-enabled servers and centralize management and monitoring of these resources. | One hour |
| Plan [Tags](/en-us/azure/azure-resource-manager/management/tag-resources) to help organize machines. | Evaluate and develop an IT-aligned [tagging strategy](/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/) that can help reduce the complexity of managing your Azure Arc-enabled servers and simplify making management decisions. | One day |
| Design and deploy [Azure Monitor Logs](/en-us/azure/azure-monitor/logs/data-platform-logs). | Evaluate [design and deployment considerations](/en-us/azure/azure-monitor/logs/workspace-design) to determine if your organization should use an existing Log Analytics workspace or implement another workspace to store collected log data from hybrid servers and machines. | One day |
| [Develop an Azure Policy](/en-us/azure/governance/policy/overview) governance plan. | Determine how you plan to implement governance of hybrid servers and machines at the subscription or resource group scope with Azure Policy. | One day |
| Configure [role-based access control](/en-us/azure/role-based-access-control/overview). | Develop an access plan to control who has access to manage Azure Arc-enabled servers and the ability to view their data from other Azure services and solutions. | One day |
| Identify machines with Azure Monitor Agent already installed. | Run the following log query in [Log Analytics](/en-us/azure/azure-monitor/logs/log-analytics-overview) to support conversion of existing Azure Monitor Agent deployments to extension-managed agent:`Heartbeat <br> &#124; summarize arg_max(TimeGenerated, OSType, ResourceId, ComputerEnvironment) by Computer <br> &#124; where ComputerEnvironment == "Non-Azure" and isempty(ResourceId) <br> &#124; project Computer, OSType` | One hour |

## Phase 2: Deploy Azure Arc-enabled servers

Next, we add to the foundation laid in Phase 1 by preparing for and [deploying the Connected Machine agent](deployment-options).

| Task | Detail | Estimated duration |
| --- | --- | --- |
| Download the predefined installation script. | Review and customize the predefined installation script for at-scale deployment of the Connected Machine agent to support your automated deployment requirements. Sample at-scale onboarding resources:<br>- [At-scale onboarding script via service principal for Linux and Windows](onboard-service-principal)<br><br><br>- [At-scale onboarding for Linux and Windows via the Azure portal](onboard-portal)<br><br><br>- [At-scale onboarding AWS](../multicloud-connector/onboard-multicloud-vms-arc) Linux and Windows machines by using [the multicloud connector](../multicloud-connector/connect-to-aws)<br><br><br>- [Connect machines at scale with Ansible](onboard-ansible-playbooks) using the Azure Arc onboarding role. | One or more days depending on the requirements, organizational processes (for example, Change and Release Management), and automation method used. |
| [Create service principal](onboard-service-principal#create-a-service-principal-for-onboarding-at-scale). | Create a service principal to connect machines noninteractively by using Azure PowerShell or from the Azure portal. | One hour. |
| Deploy the Connected Machine agent to your target servers and machines. | Use your automation tool to deploy the scripts to your servers and connect them to Azure. | One or more days depending on your release plan and if following a phased rollout. |

Note

You can view all available deployment options at [Azure Connected Machine agent deployment options](deployment-options).

## Phase 3: Manage and operate

Phase 3 is when administrators or system engineers can enable automation of manual tasks to manage and operate the Connected Machine agent and the machines during their lifecycle.

| Task | Detail | Estimated duration |
| --- | --- | --- |
| Create a Resource Health alert. | If a server stops sending heartbeats to Azure for longer than 15 minutes, it can mean that the server is offline, the network connection is blocked, or the agent isn't running. Develop a plan for how to respond and investigate these incidents and use [Resource Health alerts](/en-us/azure/service-health/resource-health-alert-monitor-guide) to get notified when they start. Specify the following items when you configure the alert:**Resource type** = **Azure Arc-enabled servers** **Current resource status** = **Unavailable** **Previous resource status** = **Available** | One hour |
| Create an Azure Advisor alert. | For the best experience and most recent security and bug fixes, we recommend that you keep the Connected Machine agent up to date. Out-of-date agents are identified with an [Azure Advisor alert](/en-us/azure/advisor/advisor-alerts-portal). Specify the following items when you configure the alert:**Recommendation type** = **Upgrade to the latest version of the Azure Connected Machine agent** | One hour |
| Update the Azure connected machine agent | Update the Arc agent as new versions are released. You can manually update the agent or [enable auto-update (public preview)](automatic-agent-upgrade). | 5-10 minutes |
| [Assign Azure policies](/en-us/azure/governance/policy/assign-policy-portal) to your subscription or resource group scope. | Assign the **Enable Azure Monitor for VMs**[policy](/en-us/azure/azure-monitor/vm/vminsights-enable-policy) (and others that meet your needs) to the subscription or resource group scope. With Azure Policy, you can assign policy definitions that install the required agents for VM insights across your environment. | Varies |
| Enable [Azure Update Manager](/en-us/azure/update-manager/) for your Azure Arc-enabled servers. | Configure Azure Update Manager on your Azure Arc-enabled servers to manage system updates for your Windows and Linux VMs. You can choose to [deploy updates on-demand](/en-us/azure/update-manager/deploy-updates?tabs=install-single-overview%2Cinstall-scale-overview) or [apply updates by using a custom schedule](/en-us/azure/update-manager/scheduled-patching?tabs=schedule-updates-single-machine%2Cschedule-updates-scale-overview%2Cwindows-maintenance). | 5 minutes |