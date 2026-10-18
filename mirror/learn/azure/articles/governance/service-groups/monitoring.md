---
layout: Conceptual
title: Monitoring Service Groups with Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/service-groups/monitoring
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
description: Learn how to monitor the health and performance of Azure Service Groups using Azure Monitor within the Azure portal.
ms.topic: how-to
ms.date: 2026-06-04T00:00:00.0000000Z
locale: en-us
document_id: 91c2bb68-67fd-c371-fcbd-235e8987a09f
document_version_independent_id: 10bcee6d-48fc-1b02-6276-e851d1b1b8d6
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/service-groups/monitoring.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/service-groups/monitoring
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/service-groups/monitoring.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d93b08ab-099b-fe10-fce4-cf24474bc59d
---

# Monitoring Service Groups with Azure Monitor | Microsoft Learn

Important

These Azure Monitor features for Azure Service Groups are currently in PREVIEW. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

[Azure Monitor](/en-us/azure/governance/service-groups/overview) provides a set of experiences and tools to monitor the health and performance of workloads in Azure Service Groups. You can view Azure Monitor insights for resources in your service group directly from the Azure portal. You can also explore relevant signals to help your workload perform as expected.

## Access service group monitoring

The monitoring experience is available under Service Groups in the [Azure portal](https://portal.azure.com).

You must also have an existing service group to monitor. For more information, see the quickstart to [create a service group in the Azure portal](create-service-group-portal).

1. Sign in to the [Azure portal](https://portal.azure.com) and search for **Service groups**.
2. On the **Service groups** page, select the resource that you want to monitor.
3. In the sidebar menu for the resource, select **Monitor** then **Monitoring**.

On the **Monitoring** page for your resource, the **Overview** tab is shown. This tab has the following tiles:

- **Issues in the last day (trend)** to see and investigate active issues and trends.
- **Application Map** to view your application map.
- **Availability tests** to run availability tests
- **Service Level Indicators and Objectives (SLIs and SLOs)** to measure and maintain service reliability

The monitoring experience only shows insights for resources in the selected service group. Insights from child and/or nested service groups aren't included.

If you want to provide feedback, you can also select the **Feedback** button at the top of the **Monitoring** page.

## Find and investigate issues

To see a breakdown of issues for a service group, go to the **Overview** tab on the **Monitoring** page for the service group. In the **Issues in the last day (trend)** tile, there's a trendline of created issues and counts of active issues. If there are no issues, no trendline is shown. The tile also shows **Total alerts**.

You can select one of the following issue types for more information, or select the button **See all issues**.

- **Total issues**
- **Critical**
- **Error**
- **Warning**
- **Informational**
- **Verbose**

[Azure Monitor issues and investigations](/en-us/azure/azure-monitor/aiops/aiops-issue-and-investigation-how-to), which are [Artificial Intelligence for IT Operations (AIOps)](/en-us/azure/azure-monitor/aiops/aiops-machine-learning) capabilities, provides details about the issues. The AI-based investigation automates the troubleshooting processes for Azure monitor alerts on resources. You get a summary of the problem, evidence, and next steps to fix each issue. 

## View alerts

To see [Azure Monitor alerts](/en-us/azure/azure-monitor/alerts/alerts-overview) alerts for resources in your service group, go to the **Overview** tab on the **Monitoring** page for the service group. In the **Issues in the last day (trend)** tile, select **Total alerts** to open the alerts pane. This view shows a list of active alerts that you can search or filter.

There's a count by severity of active alerts fired on the service group or its members. You can select an alert to view more details. You can then trigger an investigation on an alert and automatically create an issue.

## View application maps

An [application map](/en-us/azure/azure-monitor/app/app-map) shows performance bottlenecks or failure hotspots in your service groups, such as dependencies, roles, or other Application Insights resources in your service group. You can also turn on the [**Intelligent view** feature](/en-us/azure/azure-monitor/app/app-map#explore-intelligent-view) to show probable causes for service failures using machine learning to identify patterns and anomalies. You can also scope your map by using filters to see only relevant nodes and edges.

To use application maps, you must have an Application Insights resource in your service group. You can use an existing resource or create a new one.

To view the application map for resources in your service group, go to the **Overview** tab on the **Monitoring** page for the service group. In the **Application Map** tile, select **View App Map**.

If your application runs on an Azure Kubernetes Service (AKS) cluster or virtual machine, the application map shows compute details.

## Run availability tests

You can use the [availability tests](/en-us/azure/azure-monitor/app/availability) to monitor resources in your service group for responsiveness and uptime. Synthetic HTTP requests are sent at regular intervals from Azure datacenters to your application endpoints. This monitoring can help you detect failures and performance for a reliable experience across your services. You can configure test frequency, locations, and alerts based on critical paths and user locations.

To run availability tests, you must have an Application Insights resource in your service group. You can use an existing resource or create a new one. Then, configure availability tests through Application Insights in the Azure portal.

To see availability tests with your service group, go to the **Overview** tab on the **Monitoring** page for the service group. In the **Availability tests** tile, you can see the percent of successful tests over the last day, and how many tests are running.

Select **View details** to get more information on the availability tests for your resource.

## Monitoring coverage and recommendations

There are two types of monitoring available for service groups:

- **Basic monitoring** is the standard monitoring setting, which is enabled by default when you create a resource.
- **Enhanced monitoring** is the monitoring setting recommended by Microsoft. This setting might result in extra costs.

Currently, only Azure Virtual Machines and AKS resources are supported for service group monitoring coverage and recommendations.

To see coverage and recommendations for monitoring your service group, go to the **Coverage + recommendations** tab in the **Monitoring** page for the service group.

The **Monitoring coverage across all resources** tile helps you spot potential gaps in your monitoring. The chart shows the number and percentage of resources in your service group that have basic monitoring and enhanced monitoring. For more information, select **View monitoring details**.

The **Monitoring coverage by resource type** tile shows what type of monitoring is applied to resources. The chart shows the number of each resource type with enhanced monitoring and basic monitoring. For more information, select **View monitoring details**.

The **Monitoring recommendations** tile shows which monitoring enhancements you can apply at scale to close coverage gaps. If there are no supported resources in the service group, no recommendations are displayed.

The table shows a description of each recommendation, which you can select for more details. The number and type of impacted resources are also listed along with the severity level. You can select the **Apply** button next to each recommendation to apply the suggested change automatically.

## SLIs and SLOs

Today, Azure customers have a large amount of telemetry in Azure Monitor that tracks their applications and infrastructure health and performance already, these applications need to be continuously monitored to ensure their business growth and end user satisfaction. You can monitor their application’s health and measure the impact of infrastructure disruptions to their application using service level indicators (SLIs) in a standard and industry accepted way. For more information, see [Service level indicators in Azure Monitor](/en-us/azure/azure-monitor/fundamentals/service-level-indicators-create).

Key capabilities:

- Author your application SLIs and add a baseline service level objective (SLO) to SLIs.
- Deep dive into a specific SLI and track the SLI trends, error budget as well as burn rate through trend charts.
- Create burn rate-based alerts.

You can author SLIs, set targets, and track trends for your Service Group through the SLI experience in Azure Monitor. This helps you measure and maintain service reliability.

## Costs

If you use Azure Monitor with Service Groups, there might be extra costs for enhanced monitoring, data collection, and storage depending on your configuration and data volume. For more information, see [Azure Monitor pricing](https://azure.microsoft.com/pricing/details/monitor/).