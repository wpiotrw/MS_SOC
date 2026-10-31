---
layout: Conceptual
title: Configure Event Hubs with Microsoft Purview for Atlas Kafka Topics | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-kafa-notifications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2023-02-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure Event Hubs to send and receive events to and from Microsoft Purview's Apache Atlas Kafka topics.
locale: en-us
document_id: 5f698b1e-8601-e1ee-db09-00d66f2307be
document_version_independent_id: 5f698b1e-8601-e1ee-db09-00d66f2307be
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-kafa-notifications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-kafa-notifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-kafa-notifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f0234678-3067-4edc-abf7-8142d54bb7d2
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b0f4f6b9-28ed-4892-be4e-517310289c68
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: ea5d7fbd-bce9-74b0-6d83-a14509608027
---

# Configure Event Hubs with Microsoft Purview for Atlas Kafka Topics | Microsoft Learn

This article explains how to configure Microsoft Purview to be able to send and receive *Atlas Kafka* topics events with Azure Event Hubs.

If you have already configured your environment, learn how to [get started with the **Azure.Messaging.EventHubs** .NET library to send and receive messages](data-map-kafta-send-receive-events).

## Prerequisites

To configure your environment, you need certain prerequisites in place:

- **A Microsoft Azure subscription**. To use Azure services, including Event Hubs, you need an Azure subscription. If you don't have an Azure account, you can sign up for a [free trial](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) or use your MSDN subscriber benefits when you [create an account](https://azure.microsoft.com).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

## Configure Event Hubs

To send or receive Atlas Kafka topics messages, you'll need to configure at least one Event Hubs namespace. You can either:

- Create your own Azure Event Hubs namespace and configure it to work with Microsoft Purview
- Use the REST API to create a managed namespace

Note

If your Microsoft Purview account was created before December 15, 2022, you might have a managed Event Hubs resource already associated with your account. You can check in **Managed Resources** under settings on your Microsoft Purview account page in the [Azure portal](https://portal.azure.com). ![Screenshot showing the Event Hubs namespace toggle highlighted on the Managed resources page of the Microsoft Purview account page in the Azure portal.](media/configure-event-hubs-for-kafka/enable-disable-event-hubs.png)

- If you don't see this resource, or it's **disabled**, follow the steps below to configure your Event Hubs.
- If it's **enabled**, you can continue to use this managed Event Hubs namespace if you prefer. (There's associated cost. See see [the pricing page](https://azure.microsoft.com/pricing/details/purview/).) If you want to manage your own Event Hubs account, you must first **disable** this feature and follow the steps below. **To keep the Event Hub's supported TLS version updated, we recommend using BYO Event Hub.** **If you disable the managed Event Hubs resource you won't be able to re-enable a managed Event Hub resource. You will only be able to configure your own Event Hubs**.

## Bring your own Event Hubs namespace

You can configure an existing Azure Event Hubs namespace with an Event Hubs or [create a new one](/en-us/azure/event-hubs/event-hubs-create) to connect with Microsoft Purview.

### Event Hubs permissions

To authenticate with your Event Hubs, you can either use:

- Microsoft Purview managed identity(Recommended)
- [User assigned managed identity](data-map-data-scan-credentials#create-a-user-assigned-managed-identity) - only available when configuring namespaces after account creation **and** if using Event Hubs with an open network.

These identities need **at least contributor permissions on your Event Hubs** to be able to configure them to use with Microsoft Purview.

### Event Hubs networking

1. If your Microsoft Purview account is using private endpoints, [set up an ingestion private endpoint to connect to Event Hubs.](data-gov-classic-private-link#microsoft-purview-private-endpoint-deployment-scenarios)
2. Your Event Hubs workspace network needs to be configured in one of two ways:

    - *Public network access* set to **Selected networks** or **Disabled**, *Allow trusted Microsoft services to bypass this firewall* set to **Yes**, and using the Microsoft Purview managed identity to authenticate.
    - *Public network access* set to **All networks** and using the Microsoft Purview managed identity or a user assigned managed identity to authenticate.

    Microsoft Purview's status as a trusted service means that, as long as *Allow trusted Microsoft services to bypass this firewall* is set to **Yes** on your Event Hubs resource, your hooks can still receive messages from Event Hubs.

![Flow chart of Event Hubs networking, showing the success path through either all networks or enabling trusted services.](media/catalog-private-link/event-hubs-networking-chart.png)

For more information about networking for Event Hubs, see the [Azure Event Hubs documentation.](/en-us/azure/event-hubs/private-link-service)

### Configure Event Hubs to publish messages to Microsoft Purview

1. Navigate to **Kafka configuration** under settings on your Microsoft Purview account page in the [Azure portal](https://portal.azure.com).

    ![Screenshot showing the Kafka configuration option in the Microsoft Purview menu in the Azure portal.](media/configure-event-hubs-for-kafka/select-kafka-configuration.png)
2. Select **Add configuration** and **Hook configuration**.

    Note

    You can add as many hook configurations as you need.

    ![Screenshot showing the Kafka configuration page with add configuration and hook configuration highlighted.](media/configure-event-hubs-for-kafka/add-hook-configuration.png)
3. Give a name to your hook configuration, select your subscription, an existing Event Hubs namespace, an existing Event Hubs to send the notifications to, the consumer group you want to use, and the kind of authentication you would like to use.

    Tip

    You can use the same Event Hubs namespace more than once, but each configuration will need its own Event Hubs.

    ![Screenshot showing the hook configuration page, with all values filled in.](media/configure-event-hubs-for-kafka/configure-hook-event-hub.png)
4. Select **Save**. It takes a couple minutes for your configuration to complete.
5. Once configuration is complete, you can begin the steps to [publish messages to Microsoft Purview](data-map-kafta-send-receive-events#publish-messages-to-microsoft-purview).

### Configure Event Hubs to receive messages from Microsoft Purview

1. Navigate to **Kafka configuration** under settings on your Microsoft Purview account page in the [Azure portal](https://portal.azure.com).

    ![Screenshot showing the Kafka configuration option in the Microsoft Purview menu in the Azure portal.](media/configure-event-hubs-for-kafka/select-kafka-configuration.png)
2. If there's a configuration already listed as type **Notification**, Event Hubs is already configured, and you can begin the steps to [receive Microsoft Purview messages](data-map-kafta-send-receive-events#receive-microsoft-purview-messages).

    Note

    Only one *Notification* Event Hubs can be configured at a time.

    ![Screenshot showing the Kafka configuration option with a notification type configuration ready.](media/configure-event-hubs-for-kafka/type-notification.png)
3. If there isn't a **Notification** configuration already listed, select **Add configuration** and **Notification configuration**.

    ![Screenshot showing the Kafka configuration page with add configuration and notification configuration highlighted.](media/configure-event-hubs-for-kafka/add-notification-configuration.png)
4. Give a name to your notification configuration, select your subscription, an existing Event Hubs namespace, an existing Event Hubs to send the notifications to, the partitions you want to use, and the kind of authentication you would like to use.

    Tip

    You can use the same Event Hubs namespace more than once, but each configuration will need its own Event Hubs.

    ![Screenshot showing the notification hub configuration page, with all values filled in.](media/configure-event-hubs-for-kafka/configure-notification-event-hub.png)
5. Select **Save**. It takes a couple minutes for your configuration to complete.
6. Once configuration is complete, you can begin the steps to [receive Microsoft Purview messages](data-map-kafta-send-receive-events#receive-microsoft-purview-messages).

## Remove configured Event Hubs

To remove configured Event Hubs namespaces, you can follow these steps:

1. Search for and open your Microsoft Purview account in the [Azure portal](https://portal.azure.com).
2. Select **Kafka configuration** under settings on your Microsoft Purview account page in the Azure portal.
3. Select the Event Hubs you want to disable. (Hook hubs send messages to Microsoft Purview. Notification hubs receive notifications.)
4. Select **Remove** to save the choice and begin the disablement process. This can take several minutes to complete.

    ![Screenshot showing the Kafka configuration page of the Microsoft Purview account page in the Azure portal with the remove button highlighted.](media/configure-event-hubs-for-kafka/select-remove.png)

## Create a managed namespace

If you prefer to have a managed Event Hubs namespace, you need to use the REST API to configure your account.

You can use below script (set apiVersion = 2021-12-01) to update an account and this way will only affect the event hub configuration:

```
$body = @{"properties" = @{ "managedEventHubState" = "Enabled" }; "location" = $($location); "identity" = @{ "type"= $($type) } } | ConvertTo-Json
$Token=Get-AzAccessToken
$Headers = @{ "Authorization" = "Bearer $($Token.Token)" }
$Uri = "https://management.azure.com/subscriptions/$($subscription)/resourceGroups/$($rg)/providers/Microsoft.Purview/accounts/$($accountName)?api-version=$($apiVersion)"

Invoke-WebRequest -URI $Uri -Method Put -Body $body -Headers $Headers -ContentType "application/json"
```