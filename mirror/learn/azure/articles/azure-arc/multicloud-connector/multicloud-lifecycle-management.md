---
layout: Conceptual
title: Manage the Power Cycle of AWS EC2s - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/multicloud-connector/multicloud-lifecycle-management
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
author: JalenMcG
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: jalenmcgee
ms.service: azure-arc
description: Learn how to start, stop, and restart AWS EC2s with the Azure Arc Multicloud Connector
ms.topic: feature-guide
ms.date: 2026-10-07T00:00:00.0000000Z
ms.subservice: servers-azure-arc
locale: en-us
document_id: ae05fe54-d62e-eed1-7d06-c06410ff2edd
document_version_independent_id: 1d3b2906-3626-ce4e-b94b-0ba6af8fca24
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/multicloud-connector/multicloud-lifecycle-management.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/multicloud-connector/multicloud-lifecycle-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/multicloud-connector/multicloud-lifecycle-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 38e4c8a0-e01f-2708-c98b-2a36c1f2b810
---

# Manage the Power Cycle of AWS EC2s - Azure Arc | Microsoft Learn

The **Power Cycle management** solution of the multicloud connector lets you operate your AWS resources from Azure, including start, stop, and restart actions on EC2 instances. This capability extends the connector beyond discovering and Azure Arc-enabling resources, so you can act on the machines you find without switching to the AWS console.

Important

The **Power Cycle management** solution is currently in preview. It currently supports Amazon Web Services (AWS) only. Google Cloud Platform (GCP) isn't supported.

## Supported actions

| Action | Applies to | Description |
| --- | --- | --- |
| Start | EC2 instances | Starts a stopped instance. |
| Stop | EC2 instances | Stops a running instance. Supports optional force and hibernate behavior. |
| Restart | EC2 instances | Reboots a running instance. |

Creating and deleting EC2 instances isn't supported through the multicloud connector.

## Prerequisites

In addition to the [general prerequisites for connecting a public cloud](add-public-cloud#prerequisites), meet these requirements.

### Solution dependency

The **Inventory** solution must be enabled on the same connector, with the **EC2** service included in the scanned services. **Power Cycle** actions read instance state from the inventory resource, so you can't add **Power Cycle management** to a connector that doesn't have **Inventory** with EC2.

### Resource provider registration

Register these resource providers in your Azure subscription:

- `Microsoft.AwsConnector`
- `Microsoft.HybridCompute`

### AWS permissions

Your CloudFormation template must grant the connector IAM role permission to run **Power Cycle** operations:

```json
{
  "Sid": "Ec2LifecycleManagement",
  "Effect": "Allow",
  "Action": [
    "ec2:StartInstances",
    "ec2:StopInstances",
    "ec2:RebootInstances"
  ],
  "Resource": "*"
}
```

If you enable **Power Cycle** **management** on an existing connector, upload a new CloudFormation template so these permissions are applied.

### Instance requirements

- The EC2 instance must be discovered and projected into Azure by an inventory sync.
- The instance must be in a supported AWS region.

## Add the solution

Add **Power Cycle** **management** when you [create a connector](add-public-cloud#add-your-public-cloud-in-the-azure-portal), or add it to an existing connector:

1. In the Azure portal, go to **Azure Arc**, and under **Management**, select **Multicloud connectors**.
2. Select your AWS connector, and then select **Solutions**.
3. In the **Power Cycle** **management (preview)** row, select **Add**.
4. Complete the **Authentication template** step to apply the updated CloudFormation template in AWS.

## How instance state is determined

Power cycle actions are enabled or disabled based on the most likely current state of the machine. The connector uses a dual-path model, because an Arc heartbeat is fresher than a periodic inventory sync.

### Arc-enabled machines

For machines onboarded to Azure Arc, the `Microsoft.HybridCompute/machines` resource `properties.status` value provides the state. This value reflects the Arc connected heartbeat.

| Arc status | Effective state | Start | Stop | Restart |
| --- | --- | --- | --- | --- |
| Connected | Running | Disabled | Enabled | Enabled |
| Disconnected | Stopped or unavailable | Enabled | Disabled | Disabled |
| Unknown | Unknown | Falls back to inventory state | Falls back to inventory state | Falls back to inventory state |

### Inventory-only machines

For machines that aren't Azure Arc–enabled, the inventory resource provides the state:

`Microsoft.AwsConnector/ec2Instances/default.properties.awsProperties.state.name.value`

| AWS EC2 state | Effective state | Start | Stop | Restart |
| --- | --- | --- | --- | --- |
| `running` | Running | Disabled | Enabled | Enabled |
| `stopped` | Stopped | Enabled | Disabled | Disabled |
| Transitional (`stopping`, `starting`) or unknown | Changing or unknown | Disabled | Disabled | Disabled |

Note

Inventory state depends on the periodic sync interval rather than a live signal, so it can be stale. Treat it as best effort. A shorter sync interval produces fresher state.

If the connector doesn't have the **Power Cycle** **management** solution enabled, the Start, Stop, and Restart actions are disabled and the portal shows a banner explaining how to enable the solution.

## Query instance power state

Use [Azure Resource Graph](/en-us/azure/governance/resource-graph/overview) to report on running and stopped instances across your connected AWS accounts.

```kusto
awsresources
| where type =~ "microsoft.awsconnector/ec2instances"
| extend state = tostring(properties.awsProperties.state.name.value)
| extend instanceType = tostring(properties.awsProperties.instanceType.value)
| project subscriptionId, resourceGroup, name, state, instanceType, location
| order by state asc
```