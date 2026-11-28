---
layout: Conceptual
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
defaultMoniker: microsoft-fabric
versioningType: Ranged
title: project-by-names operator - Kusto | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/kusto/query/project-by-names-operator?view=microsoft-fabric
config_moniker_range: 'microsoft-fabric || azure-data-explorer || azure-monitor || microsoft-sentinel '
breadcrumb_path: /kusto/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Kusto
feedback_system: Standard
recommendations: true
author: spelluru
ms.author: oronkaiser
ms.service: kusto
services: kusto
description: Learn how to use the project-by-names operator to select a subset of columns from the input table by their names, dynamic arrays, or name patterns.
ms.reviewer: alexans
ms.topic: reference
ms.date: 2025-07-07T00:00:00.0000000Z
locale: en-us
document_id: ef867b2b-5760-d40e-ab19-eba7a8ea7c61
document_version_independent_id: ef867b2b-5760-d40e-ab19-eba7a8ea7c61
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/kusto/query/project-by-names-operator.md
default_moniker: microsoft-fabric
site_name: Docs
depot_name: Learn.kusto-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Learn.kusto-docs/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query/project-by-names-operator
moniker_range_name: f0081dc5071f32aee7689305c3508dfe
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
item_type: Content
source_path: data-explorer/kusto/query/project-by-names-operator.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
platformId: 9c6a5a2b-6776-ee06-19d4-2520ed6099cc
---

# project-by-names operator - Kusto | Microsoft Learn

> 
> Switch services using the **Version** drop-down list. [Learn more about navigation](../docs-navigation).  Applies to: ✅ Microsoft Fabric ✅ Azure Data Explorer ✅ Azure Monitor ✅ Microsoft Sentinel

Select and reorder a subset of columns from the input table by their names, dynamic arrays, or name patterns.

## Syntax

*T*`| project-by-names`*ColumnSpecifier* [`,` ...]

Learn more about [syntax conventions](/en-us/kusto/query/syntax-conventions).

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| *T* | `string` | ✔️ | The tabular input from which to remove columns. |
| *ColumnSpecifier* | `string` | ✔️ | The name of the column, dynamic array of column names, or column wildcard pattern to keep and reorder. |

Note

- Columns in the result are ordered based on the sequence in which they're specified or matched.
- Column names that don't match any existing column are safely ignored.
- Wildcard characters (\*) can be used to match multiple columns by name pattern.
- ColumnSpecifier can include the result of a [column_names_of(Table)](column-names-of-function) expression, which returns a dynamic array of column names from the specified table.
- Subqueries or scalar expressions like toscalar() aren't supported in the *ColumnSpecifier* parameter.
- For related functionality:
    - Use [`project-away`](project-away-operator) to exclude specific columns from the result.
    - Use [`project-keep`](project-keep-operator) to retain columns without changing their order.
    - Use [`project-rename`](project-rename-operator) to rename columns.

## Returns

A table containing only the columns specified in the *ColumnSpecifier* parameter, in the specified order. All unspecified columns are excluded from the result.

## Examples

The following examples demonstrate how to use the `project-by-names` operator to select and reorder columns from a table. The input table has four columns: `Name`, `Age`, `City`, and `Country`.

### Keep and reorder specific columns

Use the operator to keep only the `Name` and `City` columns.

```kusto
datatable(Name:string, Age:int, City:string, Country:string) 
['Peter', 39, 'New York', 'USA']
| project-by-names "Name", "City"
```

**Output**

| Name | City |
| --- | --- |
| Peter | New York |

### Keep columns using a dynamic array

Use the operator to select columns from the input table by providing a dynamic array of column names.

```kusto
datatable(Name:string, Age:int, City:string, Country:string) 
['Peter', 39, 'New York', 'USA']
| project-by-names dynamic(["Name", "Country"])
```

**Output**

| Name | Country |
| --- | --- |
| Peter | USA |

### Keep columns using column name patterns

Use the operator to select columns from the input table starting with `C`.

```kusto
datatable(Name:string, Age:int, City:string, Country:string) 
['Peter', 39, 'New York', 'USA']
| project-by-names "C*"
```

**Output**

| City | Country |
| --- | --- |
| New York | USA |

### Lookup and keeping lookup columns using a dynamic array

Use the operator to keep columns from a table after performing a lookup, specifying which columns to retain using a dynamic array.

```kusto
let LookupTable = 
    datatable(Name:string, Age:int, City:string, Country:string)
    ['Peter', 39, 'New York', 'USA']; 
let LookupColumns = (Source:(Name:string), lookup_columns: dynamic) { 
    Source 
    | lookup LookupTable on Name
    | project-by-names column_names_of(Source), lookup_columns
};
datatable(Name:string, Data:string)
['Peter', 'Source-data']
| invoke LookupColumns(dynamic(['Country']))
```

**Output**

| Name | Data | Country |
| --- | --- | --- |
| Peter | Source-data | USA |

### Ignore nonexisting columns

Use the operator to keep columns from a table after performing a lookup, specifying which columns to retain using a dynamic array that includes a nonexisting column name.

```kusto
let LookupTable = 
    datatable(Name:string, Age:int, City:string, Country:string)
    ['Peter', 39, 'New York', 'USA']; 
let LookupColumns = (Source:(Name:string), lookup_columns: dynamic) { 
    Source 
    | lookup LookupTable on Name
    | project-by-names column_names_of(Source), lookup_columns
};
datatable(Name:string, Data:string)
['Peter', 'Source-data']
| invoke LookupColumns(dynamic(['Country', 'NonExistent']))
```

**Output**

| Name | Data | Country |
| --- | --- | --- |
| Peter | Source-data | USA |