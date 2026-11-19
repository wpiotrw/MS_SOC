---
layout: Conceptual
title: Azure Monitor Logs reference - AzureActivity - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azureactivity
breadcrumb_path: ../../../breadcrumb/azure-monitor/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/20/azure-monitor/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/3887dc70-2025-ec11-b6e6-000d3a4f09d0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: austinmccollum
learn_banner_products:
- azure
manager: tedhudek
ms.author: austinmc
ms.service: azure-monitor
description: Reference for AzureActivity table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-07-27T00:00:00.0000000Z
locale: en-us
document_id: 60121cc0-21a6-6266-30f9-9b55b7964f01
document_version_independent_id: 6dbc0923-2986-81f9-28ac-5f2852178637
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/azureactivity.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/azureactivity
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/azureactivity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
platformId: e0df4e42-5914-590e-f9c4-6f57870f248f
---

# Azure Monitor Logs reference - AzureActivity - Azure Monitor | Microsoft Learn

Entries from the Azure Activity log that provides insight into any subscription-level or management group level events that have occurred in Azure.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | microsoft.aad/domainservices,microsoft.azureadgraph/tenants,microsoft.containerservice/managedclusters,microsoft.apimanagement/service,microsoft.appconfiguration/configurationstores,microsoft.network/applicationgateways,microsoft.servicenetworking/trafficcontrollers,microsoft.web/sites,microsoft.kubernetes/connectedclusters,microsoft.toolchainorchestrator/diagnostics,microsoft.attestation/attestationproviders,microsoft.cache/redis,microsoft.cdn/profiles,microsoft.hardwaresecuritymodules/cloudhsmclusters,microsoft.communication/communicationservices,microsoft.documentdb/databaseaccounts,microsoft.datacollaboration/workspaces,microsoft.digitaltwins/digitaltwinsinstances,microsoft.network/dnsresolverpolicies,microsoft.eventgrid/namespaces,microsoft.eventgrid/topics,microsoft.eventhub/namespaces,microsoft.network/azurefirewalls,microsoft.dashboard/grafana,microsoft.keyvault/vaults,microsoft.loadtestservice/loadtests,microsoft.managednetworkfabric/networkdevices,microsoft.documentdb/cassandraclusters,microsoft.documentdb/mongoclusters,microsoft.dashboard/dashboard,microsoft.networkcloud/baremetalmachines,microsoft.networkcloud/clustermanagers,microsoft.networkcloud/clusters,microsoft.networkcloud/storageappliances,microsoft.network/loadbalancers,microsoft.purview/accounts,microsoft.quantum/provideraccounts,microsoft.quantum/workspaces,microsoft.recoveryservices/vaults,microsoft.relay/namespaces,microsoft.servicebus/namespaces,microsoft.sql/servers,microsoft.networkfunction/azuretrafficcollectors,microsoft.network/networkmanagers,microsoft.botservice/botservices,microsoft.chaos/experiments,microsoft.cognitiveservices/accounts,microsoft.connectedcache/cachenodes,microsoft.connectedvehicle/platformaccounts,microsoft.network/networkwatchers/connectionmonitors,microsoft.app/managedenvironments,microsoft.d365customerinsights/instances,microsoft.databricks/workspaces,microsoft.dbformysql/flexibleservers,microsoft.dbforpostgresql/flexibleservers,microsoft.devcenter/devcenters,microsoft.devopsinfrastructure/pools,microsoft.discovery/bookshelves,microsoft.discovery/supercomputers,microsoft.discovery/workspaces,microsoft.durabletask/schedulers,microsoft.experimentation/experimentworkspaces,microsoft.hdinsight/clusters,microsoft.compute/virtualmachines,microsoft.logic/integrationaccounts,microsoft.machinelearningservices/workspaces,microsoft.machinelearningservices/registries,microsoft.media/mediaservices,microsoft.azureplaywrightservice/accounts,microsoft.graph/tenants,microsoft.networkanalytics/dataproducts,microsoft.network/networkvirtualappliances,microsoft.onlineexperimentation/workspaces,microsoft.storage/storageaccounts,microsoft.storagecache/amlfilesytems,microsoft.storagemover/storagemovers,microsoft.synapse/workspaces,microsoft.edge/diagnostics,microsoft.desktopvirtualization/hostpools,microsoft.zerotrustsegmentation/segmentationmanagers,default,subscription,resourcegroup,microsoft.signalrservice/webpubsub,microsoft.insights/components,microsoft.desktopvirtualization/applicationgroups,microsoft.desktopvirtualization/workspaces,microsoft.timeseriesinsights/environments,microsoft.workloadmonitor/monitors,microsoft.analysisservices/servers,microsoft.batch/batchaccounts,microsoft.appplatform/spring,microsoft.signalrservice/signalr,microsoft.containerregistry/registries,microsoft.kusto/clusters,microsoft.blockchain/blockchainmembers,microsoft.eventgrid/domains,microsoft.eventgrid/partnernamespaces,microsoft.eventgrid/partnertopics,microsoft.eventgrid/systemtopics,microsoft.conenctedvmwarevsphere/virtualmachines,microsoft.azurestackhci/virtualmachines,microsoft.scvmm/virtualmachines,microsoft.compute/virtualmachinescalesets,microsoft.hybridcontainerservice/provisionedclusters,microsoft.insights/autoscalesettings,microsoft.devices/iothubs,microsoft.servicefabric/clusters,microsoft.logic/workflows,microsoft.automation/automationaccounts,microsoft.datafactory/factories,microsoft.datalakestore/accounts,microsoft.datalakeanalytics/accounts,microsoft.powerbidedicated/capacities,microsoft.datashare/accounts,microsoft.sql/managedinstances,microsoft.sql/servers/databases,microsoft.dbformysql/servers,microsoft.dbforpostgresql/servers,microsoft.dbforpostgresql/serversv2,microsoft.dbformariadb/servers,microsoft.devices/provisioningservices,microsoft.network/expressroutecircuits,microsoft.network/frontdoors,microsoft.network/networkinterfaces,microsoft.network/networksecuritygroups,microsoft.network/publicipaddresses,microsoft.network/trafficmanagerprofiles,microsoft.network/virtualnetworkgateways,microsoft.network/vpngateways,microsoft.network/virtualnetworks,microsoft.search/searchservices,microsoft.streamanalytics/streamingjobs,microsoft.network/bastionhosts,microsoft.healthcareapis/services |
| **Categories** | Azure Resources, Audit, Security |
| **Solutions** | LogManagement |
| **Basic** table support | No |
| **Auxiliary / Lake** table support | No |
| **DCR workspace transformation** support | No |
| **Ingestion API** support | No |
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/azureactivity) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ActivityStatus | string |  |
| ActivityStatusValue | string | Status of the operation in display-friendly format. Common values include Started, In Progress, Succeeded, Failed, Active, Resolved. |
| ActivitySubstatus | string |  |
| ActivitySubstatusValue | string | Substatus of the operation in display-friendly format. E.g. OK (HTTP Status Code: 200). |
| Authorization | string | Blob of RBAC properties of the event. Usually includes the "action", "role" and "scope" properties. Stored as string. The use of Authorization\_d should be preferred going forward. |
| Authorization\_d | dynamic | Blob of RBAC properties of the event. Usually includes the "action", "role" and "scope" properties. Stored as dynamic column. |
| \_BilledSize | real | The record size in bytes |
| Caller | string | GUID of the caller. |
| CallerIpAddress | string | IP address of the user who has performed the operation UPN claim or SPN claim based on availability. |
| Category | string |  |
| CategoryValue | string | Category of the activity log e.g. Administrative, Policy, Security. |
| Claims | string | The JWT token used by Active Directory to authenticate the user or application to perform this operation in Resource Manager. The use of claims\_d should be preferred going forward. |
| Claims\_d | dynamic | The JWT token used by Active Directory to authenticate the user or application to perform this operation in Resource Manager. |
| CorrelationId | string | Usually a GUID in the string format. Events that share a correlationId belong to the same uber action. |
| EventDataId | string | Unique identifier of an event. |
| EventSubmissionTimestamp | datetime | Timestamp when the event became available for querying. |
| Hierarchy | string | Management group hierarchy of the management group or subscription that event belongs to. |
| HTTPRequest | string | Blob describing the Http Request. Usually includes the "clientRequestId", "clientIpAddress" and "method" (HTTP method. For example, PUT). |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| Level | string | Level of the event. One of the following values: Critical, Error, Warning, Informational and Verbose. |
| OperationId | string | GUID of the operation |
| OperationName | string |  |
| OperationNameValue | string | Identifier of the operation e.g. Microsoft.Storage/storageAccounts/listAccountSas/action. |
| Properties | string | Set of &lt;Key Value&gt; pairs (i.e. Dictionary) describing the details of the event. Stored as string. Usage of Properties\_d is recommended instead. |
| Properties\_d | dynamic | Set of &lt;Key Value&gt; pairs (i.e. Dictionary) describing the details of the event. Stored as dynamic column. |
| Resource | string |  |
| ResourceGroup | string | Resource group name of the impacted resource. |
| ResourceId | string |  |
| \_ResourceId | string | A unique identifier for the resource that the record is associated with |
| ResourceProvider | string |  |
| ResourceProviderValue | string | Id of the resource provider for the impacted resource - e.g. Microsoft.Storage. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| SubscriptionId | string | Subscription ID of the impacted resource. |
| \_SubscriptionId | string | A unique identifier for the subscription that the record is associated with |
| TenantId | string | The Log Analytics workspace ID |
| TimeGenerated | datetime | Timestamp when the event was generated by the Azure service processing the request corresponding the event. |
| Type | string | The name of the table |