---
layout: Conceptual
monikers:
- azure-data-explorer
- microsoft-fabric
defaultMoniker: microsoft-fabric
versioningType: Ranged
title: gql_request plugin - Kusto | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/kusto/query/gql-request-plugin?view=microsoft-fabric
config_moniker_range: 'microsoft-fabric || azure-data-explorer || azure-monitor || microsoft-sentinel '
breadcrumb_path: /kusto/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Kusto
feedback_system: Standard
recommendations: true
author: spelluru
ms.author: spelluru
ms.service: kusto
services: kusto
description: Run a GQL query against a Microsoft Fabric graph and process the returned table with Kusto Query Language operators.
ms.reviewer: gabil
ms.topic: reference
ms.date: 2026-10-18T00:00:00.0000000Z
locale: en-us
document_id: 491cb846-a44d-c2cb-d86c-6595066f4c84
document_version_independent_id: 491cb846-a44d-c2cb-d86c-6595066f4c84
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/kusto/query/gql-request-plugin.md
default_moniker: microsoft-fabric
site_name: Docs
depot_name: Learn.kusto-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Learn.kusto-docs/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query/gql-request-plugin
moniker_range_name: 20a40bd96f66fbdf33721192ccdcccff
monikers:
- azure-data-explorer
- microsoft-fabric
item_type: Content
source_path: data-explorer/kusto/query/gql-request-plugin.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: da7e0c49-f05a-671b-8e60-dc19a4f19b6e
---

# gql_request plugin - Kusto | Microsoft Learn

The `gql_request` plugin runs an [ISO Graph Query Language (GQL)](/en-us/fabric/graph/gql-language-guide) query against a graph in Microsoft Fabric and returns the results as a table. Process the returned table with standard Kusto Query Language (KQL) operators. Invoke the plugin with the [evaluate operator](evaluate-operator).

The plugin uses the Microsoft Fabric [GQL Query API](/en-us/fabric/graph/gql-query-api). You can optionally declare the expected output schema. Providing it avoids an additional GQL query during schema discovery.

Note

This plugin uses Graph Query Language (GQL) to query Fabric graphs, not GraphQL, the API query language.

Note

The `gql_request` plugin is in preview.

## Prerequisites

- A Microsoft Fabric graph that contains data. To create and load a sample graph, see [Graph quickstart](/en-us/fabric/graph/quickstart).
- Permission to query the graph in its Fabric workspace.
- The cluster callout policy must allow Fabric Graph GQL request callouts to `api.fabric.microsoft.com`. To change this policy, you need `AllDatabasesAdmin` or `Ops` permissions.

## Syntax

`evaluate``gql_request``(`*ConnectionString*`,`*GqlQuery*`)` [`:`*OutputSchema*]

Learn more about syntax conventions in the [Syntax conventions for reference documentation](syntax-conventions).

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ConnectionString | `string` | Yes | The Fabric graph-model URL followed by `;Impersonate`. For the supported format, see Connection string. |
| GqlQuery | `string` | Yes | The GQL query to run against the graph. |
| OutputSchema | - | - | The names and types of the expected output columns. Use the syntax `(`*ColumnName*`:`*ColumnType* [`,` ...]`)`. |

Note

Specifying *OutputSchema* is recommended particularly when the GQL query might return no rows. It lets Kusto determine the plugin’s output columns and types without running the query during schema discovery. The plugin returns an error if the returned schema is incompatible with the declared schema.

## Connection string

Specify the Fabric graph-model URL followed by the `;Impersonate` authentication directive:

`https://api.fabric.microsoft.com/v1/workspaces/<WorkspaceId>/GraphModels/<GraphModelId>;Impersonate`

`WorkspaceId` and `GraphModelId` must be valid GUIDs.

## Authentication and authorization

The plugin uses Microsoft Entra on-behalf-of authentication. The engine obtains a token for the requesting user and queries the graph in that user's security context. The user must have permissions on the graph.

Use `;Impersonate` as the authentication directive. Managed identity, service principal, and application key authentication aren't supported.

Important

Use an [obfuscated string literal](scalar-data-types/string) for any string that contains confidential information. Obfuscated values don't appear in Kusto tracing.

## Configure the callout policy

The plugin makes an external call to Microsoft Fabric. Because the default callout policy blocks Fabric Graph GQL request callouts, a cluster administrator must explicitly allow the Fabric endpoint.

The following command merges a restrictive Fabric Graph GQL request rule into the existing [cluster callout policy](../management/callout-policy):

```kusto
.alter-merge cluster policy callout @'[{
    "CalloutType": "gql", 
    "CalloutUriRegex": "api\\.fabric\\.microsoft\\.com/.*", 
    "CanCall": true
}]'
```

Verify the policy:

```kusto
.show cluster policy callout
```

## Returns

The plugin returns the GQL query result as a KQL table. If you specify *OutputSchema*, the returned columns must be compatible with the declared schema. For predictable results, project the properties you need in the GQL query rather than returning whole nodes, edges, or paths.

## Examples

### Return rows from a graph

This example assumes the graph contains `Person` nodes with `firstName` and `lastName` properties. It returns up to 100 names.

```kusto
evaluate gql_request(
  'https://api.fabric.microsoft.com/v1/workspaces/<workspace-id>/graphModels/<graph-model-id>;Impersonate',
  @'MATCH (p:Person)
    RETURN p.firstName AS firstName, p.lastName AS lastName
    LIMIT 100')
  : (firstName:string, lastName:string)
```

### Process GQL results with Kusto

The following example counts `Person` nodes with a `LIVES_IN` relationship to each `City`, then uses KQL to show cities with more than 10 people, ordered by count. It assumes the graph contains `Person` and `City` nodes connected by `LIVES_IN` relationships.

```kusto
evaluate gql_request(
  'https://api.fabric.microsoft.com/v1/workspaces/<workspace-id>/GraphModels/<graph-model-id>;Impersonate',
  @'MATCH (p:Person)-[:LIVES_IN]->(c:City)
    RETURN c.name AS city, count(DISTINCT p) AS PersonCount')
  : (city:string, PersonCount:long)
| where PersonCount > 10
| order by PersonCount desc
```

This counts distinct people per city name; cities sharing a name are grouped together.

Tip

Filter, project, and limit data in GQL when possible to reduce the amount of data returned to Kusto.

## Troubleshooting

The plugin distinguishes transport failures from GQL application errors. A GQL application error can arrive in an HTTP 200 response. The plugin evaluates the response status, includes available status codes, descriptions, and nested causes, and returns the failure as a query error.

The table below lists common errors returned by the plugin and their possible causes and resolutions.

| Error | Cause and resolution |
| --- | --- |
| Invalid connection string | Confirm that the connection string follows the supported format, the workspace and graph model IDs are valid GUIDs, and the string ends with `;Impersonate`. Don't include `/executeQuery` , query parameters, or a fragment in the URL. The plugin constructs the API endpoint internally. |
| Output schema mismatch | Confirm that the declared column names and KQL types are compatible with the GQL result columns and types. |
| Unsupported GQL result type | Project individual scalar properties in the GQL query. For complex values, consider using GQL `TO_JSON_STRING` to return a string representation. |
| Callout isn't permitted | Configure the cluster callout policy to allow Fabric Graph GQL request calls to `api.fabric.microsoft.com`. |
| Authentication or authorization error | Confirm that the caller identity can access the workspace and graph. |
| HTTP request error | Check Microsoft Fabric service availability, endpoint accessibility and throttling responses. |
| GQL query error | Review the query error details, including the GQL status description, diagnostics, and nested cause when available. |