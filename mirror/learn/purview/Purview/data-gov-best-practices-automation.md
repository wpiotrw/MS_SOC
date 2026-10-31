---
layout: Conceptual
title: Microsoft Purview automation best practices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-automation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article provides an overview of Microsoft Purview automation tools and guidance on what to use when.
locale: en-us
document_id: ec623dd2-0620-279f-6740-1351a1d00319
document_version_independent_id: ec623dd2-0620-279f-6740-1351a1d00319
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-automation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-automation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-automation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/43093068-2dda-408b-b3fe-dfd705c84f78
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 929261a6-436d-73b5-7a65-7facec2c948a
---

# Microsoft Purview automation best practices | Microsoft Learn

While [Microsoft Purview governance solutions](/en-us/purview/purview#microsoft-purview-unified-data-governance-solutions) provide an out of the box user experience with the Microsoft Purview governance portal, not all tasks are suited to the point-and-click nature of the graphical user experience.

For example:

- Triggering a scan to run as part of an automated process.
- Monitoring for metadata changes in real time.
- Building your own custom user experience.

Microsoft Purview provides several tools in which we can use to interact with the underlying platform, in an automated, and programmatic fashion. Because of the open nature of the Microsoft Purview service, we can automate different aspects, from the control plane, made accessible via Azure Resource Manager, to Microsoft Purview's multiple data planes (catalog, scanning, administration, and more).

This article provides a summary of the options available, and guidance on what to use when.

## Tools

| Tool Type | Tool | Scenario | Management | Catalog | Scanning | Logs |
| --- | --- | --- | --- | --- | --- | --- |
| **Resource Management** | - [ARM Templates](/en-us/azure/templates/microsoft.purview/accounts)<br>- [Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/purview_account) | Infrastructure as Code | ✓ |  |  |  |
| **Command Line** | - [Azure CLI](/en-us/cli/azure/service-page/azure%20purview) | Interactive | ✓ |  |  |  |
| **Command Line** | - [Azure PowerShell](/en-us/powershell/module/az.purview) | Interactive | ✓ | ✓ |  |  |
| **API** | - [REST API](/en-us/rest/api/purview/) | On-Demand | ✓ | ✓ | ✓ |  |
| **Streaming** (Apache Atlas) | - [Event Hubs](/en-us/azure/purview/manage-kafka-dotnet) | Real-Time |  | ✓ |  |  |
| **Monitoring** | - [Azure Monitor](/en-us/azure/azure-monitor/essentials/diagnostic-settings?tabs=CMD#destinations) | Monitoring |  |  |  | ✓ |
| **SDK** | - [.NET](/en-us/dotnet/api/overview/azure/purview)<br>- [Java](/en-us/java/api/overview/azure/purview)<br>- [JavaScript](/en-us/javascript/api/overview/azure/purview)<br>- [Python](/en-us/python/api/overview/azure/purview) | Custom Development | ✓ | ✓ | ✓ |  |

## Command Line

Azure CLI and Azure PowerShell are command-line tools that enable you to manage Azure resources such as Microsoft Purview. While the list of commands will grow over time, only a subset of Microsoft Purview control plane operations is currently available. For an up-to-date list of commands currently available, check out the documentation ([Azure CLI](/en-us/cli/azure/purview) | [Azure PowerShell](/en-us/powershell/module/az.purview)).

- **Azure CLI** - A cross-platform tool that allows the execution of commands through a terminal using interactive command-line prompts or a script. Azure CLI has a **purview extension** that allows for the management of Microsoft Purview accounts. For example, `az purview account`.
- **Azure PowerShell** - A cross-platform task automation program, consisting of a set of cmdlets for managing Azure resources. Azure PowerShell has a module called **Az.Purview** that allows for the management of Microsoft Purview accounts. For example, `Get-AzPurviewAccount`.

When to use?

- Best suited for ad-hoc tasks and quick exploratory operations.

## API

REST APIs are HTTP endpoints that surface different methods (`POST`, `GET`, `PUT`, `DELETE`), triggering actions such as create, read, update, or delete (CRUD). Microsoft Purview exposes a large portion of the Microsoft Purview platform via multiple [service endpoints](/en-us/rest/api/purview/).

When to use?

- Required operations not available via Azure CLI, Azure PowerShell, or native client libraries.
- Custom application development or process automation.

## Streaming (Apache Atlas)

Each Microsoft Purview account can configure Event Hubs that are accessible via their Atlas Kafka endpoint.

[You can follow these steps to configure the Event Hubs namespaces.](data-map-kafa-notifications)

Note

Enabling this Event Hubs namespace does incur a cost for the namespace. For specific details, see [the pricing page](https://azure.microsoft.com/pricing/details/event-hubs/).

Once the namespace is enabled, Microsoft Purview events can be monitored by consuming messages from the event hub. External systems can also use the event hub to publish events to Microsoft Purview as they occur.

- **Consume Events** - Microsoft Purview will send notifications about metadata changes to Kafka topic **ATLAS\_ENTITIES**. Applications interested in metadata changes can monitor for these notifications. Supported operations include: `ENTITY_CREATE`, `ENTITY_UPDATE`, `ENTITY_DELETE`, `CLASSIFICATION_ADD`, `CLASSIFICATION_UPDATE`, `CLASSIFICATION_DELETE`.
- **Publish Events** - Microsoft Purview can be notified of metadata changes via notifications to Kafka topic **ATLAS\_HOOK**. Supported operations include: `ENTITY_CREATE_V2`, `ENTITY_PARTIAL_UPDATE_V2`, `ENTITY_FULL_UPDATE_V2`, `ENTITY_DELETE_V2`.

When to use?

- Applications or processes that need to publish or consume Apache Atlas events in real time.

## Monitoring

Microsoft Purview can send platform logs and metrics via "Diagnostic settings" to one or more destinations (Log Analytics Workspace, Storage Account, or Azure Event Hubs). [Available metrics](data-gov-classic-azure-monitor#available-metrics) include `Data Map Capacity Units`, `Data Map Storage Size`, `Scan Canceled`, `Scan Completed`, `Scan Failed`, and `Scan Time Taken`.

Once configured, Microsoft Purview automatically sends these events to the destination as a JSON payload. From there, application subscribers that need to consume and act on these events can do so with the option of orchestrating downstream logic.

When to use?

- Applications or processes that need to consume diagnostic events.

## SDK

Microsoft provides Azure SDKs to programmatically manage and interact with Azure services. Microsoft Purview client libraries are available in several languages (.NET, Java, JavaScript, and Python), designed to be consistent, approachable, and idiomatic.

- [.NET](/en-us/dotnet/api/overview/azure/purview)
- [Java](/en-us/java/api/overview/azure/purview)
- [JavaScript](/en-us/javascript/api/overview/azure/purview)
- [Python](/en-us/python/api/overview/azure/purview)

When to use?

- Recommended over the REST API as the native client libraries (where available) will follow standard programming language conventions in line with the target language that will feel natural to the developer.