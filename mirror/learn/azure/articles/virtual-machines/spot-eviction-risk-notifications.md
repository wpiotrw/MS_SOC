---
layout: Conceptual
title: Spot Rebalance Recommendation signals (preview Spot Plus) - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/spot-eviction-risk-notifications
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: wwilliams
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn how to receive Spot Plus rebalance recommendations through in-VM Scheduled Events or out-of-VM Azure Event Grid notifications.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: concept-article
ai-usage: ai-assisted
locale: en-us
document_id: 8bc340bd-1668-604e-1b24-6c15bb238e4e
document_version_independent_id: 7e6d8c33-64ff-79ef-166d-f1b351391631
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/spot-eviction-risk-notifications.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/spot-eviction-risk-notifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/spot-eviction-risk-notifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/467aaae1-e916-4fcd-a463-5b27f9d4745c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fbd4eef5-2258-406b-95d3-2c68fa333b20
platformId: 50113cd6-6747-76d8-23b1-b38fff164422
---

# Spot Rebalance Recommendation signals (preview Spot Plus) - Azure Virtual Machines | Microsoft Learn

The Spot rebalance recommendation is a feature that provides an early alert when a Spot Instance faces a heightened risk of interruption. When you receive this recommendation, proactively save your state and shift your workload to another Spot Instance to mitigate potential disruptions. Scheduled events deliver rebalance recommendations. You can consume them in two ways: as an **in-VM notification** or as an **out-of-VM notification**.

To receive these notifications for Spot Plus, register `Microsoft.Compute/SpotPlus` by using [Feature Registration](/en-us/rest/api/resources/features/register?tabs=HTTP).

Note

This feature makes a best-effort attempt and doesn't always emit a signal before eviction.

## In-VM rebalance notifications

In-VM rebalance notifications are a scheduled event delivered to the virtual machine via the metadata service. The metadata service provides this information through a REST endpoint that you can access from inside the VM.

Important

This endpoint uses the same endpoint for preempt notifications, but it uses a different version.

Rebalance notifications are only advisory. Unlike preempt notifications, acknowledging them has no effect. To onboard to Scheduled Events and listen to these events, follow [Scheduled Events for Windows VMs in Azure](windows/scheduled-events) or [Scheduled Events for Linux VMs in Azure](linux/scheduled-events).

## Out-of-VM rebalance notifications

The following steps explain the onboarding experience for out-of-VM rebalance notifications.

### Create a system topic by using the Azure CLI

For the full command reference, see [az eventgrid system-topic](/en-us/cli/azure/eventgrid/system-topic).

1. Set the account to the Azure subscription where you want to create the system topic. Replace the placeholders in the commands with your values.

    ```azurecli
    az account set -s <subscription-id>
    ```
2. Create the system topic. For more information, see [az eventgrid system-topic](/en-us/cli/azure/eventgrid/system-topic).

    ```azurecli
    az eventgrid system-topic create --name spotRebalanceTopic --resource-group sampletestrg --source /subscriptions/<subscription-id> --topic-type microsoft.resourcenotifications.MaintenanceResources --location Global
    ```
3. Create the event subscription. For more information, see [az eventgrid system-topic event-subscription create](/en-us/cli/azure/eventgrid/system-topic/event-subscription#az-eventgrid-system-topic-event-subscription-create).

    ```azurecli
    az eventgrid system-topic event-subscription create --name firstEventSubscription --resource-group sampletestrg --system-topic-name spotRebalanceTopic --included-event-types Microsoft.ResourceNotifications.MaintenanceResources.ScheduledEventEmitted --endpoint <event-hub-endpoint> --endpoint-type eventhub
    ```

    Note

    If you don't specify `--included-event-types`, the command includes all event types by default. Ensure that the entity creating the event subscription has read permissions on the entire Azure subscription.
4. To delete the event subscription:

    ```azurecli
    az eventgrid system-topic event-subscription delete --name firstEventSubscription --resource-group sampletestrg --system-topic-name spotRebalanceTopic
    ```
5. To delete the system topic:

    ```azurecli
    az eventgrid system-topic delete --name spotRebalanceTopic --resource-group sampletestrg
    ```

### Create and validate system topics by using the Azure portal

After you create a system topic by using the Azure CLI or PowerShell, use the Azure portal to create event subscriptions and configure filters.

For more information, see [Create, view, and manage system topics](/en-us/azure/event-grid/create-view-manage-system-topics).

1. Follow the preceding steps to create the system topic by using the CLI.
2. In the portal, in the search box at the top, type **Event Grid System Topics**, and then press **ENTER**.

    [![Screenshot of the Azure portal search box with Event Grid System Topics entered.](media/spot-rebalance-recommendation-signals-onboarding-guide/search-event-grid-system-topics.png)](media/spot-rebalance-recommendation-signals-onboarding-guide/search-event-grid-system-topics.png#lightbox)
3. On the **Event Grid System Topics** page, view the list of system topics.

    [![Screenshot of the Event Grid System topics page listing the system topics.](media/spot-rebalance-recommendation-signals-onboarding-guide/event-grid-system-topics-list.png)](media/spot-rebalance-recommendation-signals-onboarding-guide/event-grid-system-topics-list.png#lightbox)
4. Select a **system topic** from the list to see details about it.

    ![Screenshot of the system topic details page.](media/spot-rebalance-recommendation-signals-onboarding-guide/event-grid-system-topic-overview.png)

    This page shows you details about the system topic, such as the following information:

    - **Source**: Name of the resource on which the system topic was created.
    - **Source type**: Type of the system topic resource. For example: microsoft.resourcenotifications.MaintenanceResources, Microsoft.ResourceNotifications.HealthResources, Microsoft.ResourceNotifications.Resources, Microsoft.Storage.StorageAccounts, Microsoft.EventHub.Namespaces, and Microsoft.Resources.ResourceGroups.
    - Any subscriptions created for the system topic.

    This page allows operations such as the following ones:

    - Create an event subscription: select **+ Event Subscription** on the toolbar.
    - Delete an event subscription: select **Delete** on the toolbar.
5. On the **Event Grid System Topic** page, select **+ Event Subscription** from the toolbar.

    ![Screenshot of the system topic page with the + Event Subscription button highlighted.](media/spot-rebalance-recommendation-signals-onboarding-guide/add-event-subscription.png)
6. Confirm that the **Topic Type**, **Source Resource**, and **Topic Name** are automatically populated. Enter a name for the event subscription, select the event types, and specify the endpoint details.

    ![Screenshot of the Create Event Subscription page showing the Basics tab.](media/spot-rebalance-recommendation-signals-onboarding-guide/create-event-subscription-basics.png)
7. Select the **Filters** tab to provide subject or advanced filtering for your scenario.

    ![Screenshot of the Filters tab on the Create Event Subscription page.](media/spot-rebalance-recommendation-signals-onboarding-guide/event-subscription-filters.png)

### Example scenario: Subscribe to rebalance signals for a particular resource group

#### Azure portal

Select **Enable subject filtering** under **Subject Filters**. For **Subject Begins With**, enter the value of the resource group in this format: `/subscriptions/{subscription-id}/resourceGroups/{resourceGroup-id}`.

For example, set **Subject Begins With** to `/subscriptions/<subscription-id>/resourceGroups/TestRG`.

![Screenshot of the event subscription Filters tab with subject filtering enabled for a resource group.](media/spot-rebalance-recommendation-signals-onboarding-guide/resource-group-subject-filter.png)

#### Azure CLI

```azurecli
az eventgrid system-topic event-subscription create --name firstEventSubForRebalance --resource-group sampletestrg --system-topic-name spotRebalanceTopic --included-event-types Microsoft.ResourceNotifications.MaintenanceResources.ScheduledEventEmitted --endpoint <event-hub-endpoint> --endpoint-type eventhub --subject-begins-with /subscriptions/<subscription-id>/resourceGroups/TestRG/
```