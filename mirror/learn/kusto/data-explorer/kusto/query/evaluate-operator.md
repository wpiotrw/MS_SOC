---
layout: Conceptual
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
defaultMoniker: microsoft-fabric
versioningType: Ranged
title: evaluate plugin operator - Kusto | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/kusto/query/evaluate-operator?view=microsoft-fabric
config_moniker_range: 'microsoft-fabric || azure-data-explorer || azure-monitor || microsoft-sentinel '
breadcrumb_path: /kusto/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Kusto
feedback_system: Standard
recommendations: true
author: spelluru
ms.author: spelluru
ms.service: kusto
services: kusto
description: Learn how to use the evaluate plugin operator to invoke plugins.
ms.reviewer: alexans
ms.topic: reference
ms.date: 2026-10-14T00:00:00.0000000Z
locale: en-us
document_id: 5688286a-8b20-5799-c5aa-e0f0c57bc350
document_version_independent_id: 5688286a-8b20-5799-c5aa-e0f0c57bc350
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/kusto/query/evaluate-operator.md
default_moniker: microsoft-fabric
site_name: Docs
depot_name: Learn.kusto-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Learn.kusto-docs/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query/evaluate-operator
moniker_range_name: f0081dc5071f32aee7689305c3508dfe
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
item_type: Content
source_path: data-explorer/kusto/query/evaluate-operator.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
platformId: 0caaf572-21d4-8183-5606-8b3c43a9137f
---

# evaluate plugin operator - Kusto | Microsoft Learn

> 
> Switch services using the **Version** drop-down list. [Learn more about navigation](../docs-navigation).  Applies to: ✅ Microsoft Fabric ✅ Azure Data Explorer

Invokes a service-side query extension (plugin).

The `evaluate` operator is a tabular operator that allows you to invoke query language extensions known as **plugins**. Unlike other language constructs, plugins can be enabled or disabled. Plugins aren't "bound" by the relational nature of the language. In other words, they may not have a predefined, statically determined, output schema.

Note

- Syntactically, `evaluate` behaves similarly to the [invoke operator](invoke-operator), which invokes tabular functions.
- Plugins provided through the evaluate operator aren't bound by the regular rules of query execution or argument evaluation.
- Specific plugins may have specific restrictions. For example, plugins whose output schema depends on the data. For example, [bag_unpack plugin](bag-unpack-plugin) and [pivot plugin](pivot-plugin) can't be used when performing cross-cluster queries.

## Syntax

[*T*`|`] `evaluate` [ *evaluateParameters* ] *PluginName*`(`[ *PluginArgs* ]`)`

Learn more about [syntax conventions](/en-us/kusto/query/syntax-conventions).

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| *T* | `string` |  | A tabular input to the plugin. Some plugins don't take any input and act as a tabular data source. |
| *evaluateParameters* | `string` |  | Zero or more space-separated evaluate parameters in the form of *Name*`=`*Value* that control the behavior of the evaluate operation and execution plan. Each plugin may decide differently how to handle each parameter. Refer to each plugin's documentation for specific behavior. |
| *PluginName* | `string` | ✔️ | The mandatory name of the plugin being invoked. |
| *PluginArgs* | `string` |  | Zero or more comma-separated arguments to provide to the plugin. |

### Evaluate parameters

The following parameters are supported:

| Name | Values | Description |
| --- | --- | --- |
| `hint.distribution` | `single`, `per_node`, `per_shard` | Distribution hints |
| `hint.pass_filters` | `true`, `false` | Allow `evaluate` operator to passthrough any matching filters before the plugin. Filter is considered as 'matched' if it refers to a column existing before the `evaluate` operator. Default: `false` |
| `hint.pass_filters_column` | *column\_name* | Allow plugin operator to passthrough filters referring to *column\_name* before the plugin. Parameter can be used multiple times with different column names. |

## Plugins

The following plugins are supported:

- [autocluster plugin](autocluster-plugin)
- [azure-digital-twins-query-request plugin](azure-digital-twins-query-request-plugin)
- [bag-unpack plugin](bag-unpack-plugin)
- [basket plugin](basket-plugin)
- [cosmosdb-sql-request plugin](cosmosdb-plugin)
- [dax_request plugin](dax-request-plugin)
- [gql_request plugin](gql-request-plugin)
- [dcount-intersect plugin](dcount-intersect-plugin)
- [diffpatterns plugin](diffpatterns-plugin)
- [diffpatterns-text plugin](diffpatterns-text-plugin)
- [infer-storage-schema plugin](infer-storage-schema-plugin)
- [ipv4-lookup plugin](ipv4-lookup-plugin)
- [ipv6-lookup plugin](ipv6-lookup-plugin)
- [mysql-request-plugin](mysql-request-plugin)
- [narrow plugin](narrow-plugin)
- [pivot plugin](pivot-plugin)
- [preview plugin](preview-plugin)
- [R plugin](r-plugin)
- [rolling-percentile plugin](rolling-percentile-plugin)
- [rows-near plugin](rows-near-plugin)
- [schema-merge plugin](schema-merge-plugin)
- [sql-request plugin](sql-request-plugin)
- [sequence-detect plugin](sequence-detect-plugin)

## Distribution hints

Distribution hints specify how the plugin execution will be distributed across multiple cluster nodes. Each plugin may implement a different support for the distribution. The plugin's documentation specifies the distribution options supported by the plugin.

Possible values:

- `single`: A single instance of the plugin will run over the entire query data.
- `per_node`: If the query before the plugin call is distributed across nodes, then an instance of the plugin will run on each node over the data that it contains.
- `per_shard`: If the data before the plugin call is distributed across shards, then an instance of the plugin will run over each shard of the data.