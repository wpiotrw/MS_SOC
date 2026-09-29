---
layout: Reference
title: Embed Token - Generate Token - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/generate-token
uid: api.powerbi.com.power-bi.embedtoken.generatetoken
breadcrumb_path: /rest/breadcrumb/toc.json
rest_product: Power BI
ms.service: powerbi
products:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
author: rloutlaw
ms.author: routlaw
ms.devlang: rest-api
ms.date: 2018-03-14T00:00:00.0000000Z
uhfHeaderId: MSDocsHeader-MSPowerBI
feedback_system: None
enable_rest_try_it: true
ms.topic: generated-reference
description: Generates an embed token for multiple reports, datasets, and target workspaces. Reports and datasets don't have to be related.
locale: en-us
document_id: ad05c0e4-9e80-5670-70f8-70f42881a5c2
document_version_independent_id: 8ae1d024-6358-232f-b049-11161bfc31aa
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Embed-Token/Generate-Token.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/embed-token/generate-token
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Embed-Token/Generate-Token.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 92907040-25e6-a80c-abd2-f06215d80552
---

# Embed Token - Generate Token

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Generates an embed token for multiple reports, datasets, and target workspaces.

- Reports and datasets don't have to be related.
- You can bind a report to a dataset during embedding.
- You can only create a report in workspaces specified by the `targetWorkspaces` parameter.

Important

This API call is only relevant to the [embed for your customers](/en-us/power-bi/developer/embed-sample-for-customers) scenario. To learn more about using this API, see [Considerations when generating an embed token](/en-us/power-bi/developer/embedded/generate-embed-token).

## Permissions

- When using a service principal for authentication, refer to [Embed Power BI content with service principal](/en-us/power-bi/developer/embed-service-principal) and [Considerations and limitations](/en-us/power-bi/developer/embedded/embed-service-principal#considerations-and-limitations).
- For Power BI reports with a paginated visual, include the paginated report ID in the API call. For more information, see [example](/en-us/rest/api/power-bi/embed-token/generate-token#examples).
- This API call can be called by a service principal profile. For more information see: [Service principal profiles in Power BI Embedded](/en-us/power-bi/developer/embedded/embed-multi-tenancy).

## Required Scope

All of the following, unless a requirement doesn't apply:

- Content.Create, required if a target workspace is specified in [GenerateTokenRequestV2](/en-us/rest/api/power-bi/embed-token/generate-token#generatetokenrequestv2).
- Report.ReadWrite.All or Report.Read.All, required if a report is specified in [GenerateTokenRequestV2](/en-us/rest/api/power-bi/embed-token/generate-token#generatetokenrequestv2).
- Report.ReadWrite.All, required if the `allowEdit` flag is specified for at least one report in [GenerateTokenRequestV2](/en-us/rest/api/power-bi/embed-token/generate-token#generatetokenrequestv2).
- Dataset.ReadWrite.All or Dataset.Read.All

## Limitations

- You can only create a report in workspaces specified by the `targetWorkspaces` parameter.
- All reports and datasets must reside in a **V2** workspace.
- All target workspaces must be **V2** workspaces.
- Maximum 50 reports.
- Maximum 50 datasets.
- Maximum 50 target workspaces.
- For Azure Analysis Services or Analysis Services on-premises live connection reports, generating an embed token with row-level security (RLS) might not work for several minutes after a [rebind](/en-us/rest/api/power-bi/reports/rebind-report).

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

## Request Body

| Name | Type | Description |
| --- | --- | --- |
| datasets | GenerateTokenRequestV2Dataset[] | A list of datasets |
| datasourceIdentities | DatasourceIdentity[] | List of identities to use when connecting to data sources with Single Sign-On (SSO) enabled. |
| identities | EffectiveIdentity[] | The list of identities to use for row-level security rules |
| lifetimeInMinutes | integer | The maximum lifetime of the token in minutes, starting from the time it was generated. Can be used to shorten the token's expiration time, but not to extend it. The value must be a positive integer. Zero (`0`) is equivalent to `null`, and will set the default expiration time. |
| reports | GenerateTokenRequestV2Report[] | A list of reports |
| targetWorkspaces | GenerateTokenRequestV2TargetWorkspace[] | The list of workspaces that the embed token will allow saving to |

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | EmbedToken | OK |

## Examples

| Example of generating an embed token for a dataset and two reports example. Only one of the reports can be edited. |
| --- |
| Example of generating an embed token for a paginated report which has a Power BI dataset as a datasource. The ID of the dataset must be specified in the request. The report and dataset can each have its own identity |
| Example of generating an embed token for a paginated report with a data source identity |
| Example of generating an embed token for a paginated report with multiple data source identities and a single identity blob |
| Example of generating an embed token for a paginated report with multiple data source identities and multiple identity blobs |
| Example of generating an embed token for a Power BI report with a dataset which is connected with DirectQuery to another Power BI dataset. All related dataset IDs must be specified in the request with 'xmlaPermissions' set to 'ReadOnly'. IdentityBlobs for all SSO-enabled data sources must be provided in the 'datasourceIdentities' array |
| Example of generating an embed token for a Power BI report with a paginated visual. The paginated report ID ('...4850') of the paginated visual must be included in the 'reports' section of the request. |
| Example of generating an embed token for two datasets with RLS identities and a single report with read-only permissions. The embed token lets you view the report, which is dynamically bound to two different datasets. |
| Example of generating an embed token that expires no later than ten minutes from the API call |

### Example of generating an embed token for a dataset and two reports example. Only one of the reports can be edited.

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    }
  ],
  "reports": [
    {
      "allowEdit": true,
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    },
    {
      "id": "759908bb-ead8-4a43-9645-7ffbf921c68d"
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2018-07-29T17:58:19Z"
}
```

### Example of generating an embed token for a paginated report which has a Power BI dataset as a datasource. The ID of the dataset must be specified in the request. The report and dataset can each have its own identity

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
      "xmlaPermissions": "ReadOnly"
    }
  ],
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "identities": [
    {
      "username": "john@contoso.com",
      "roles": [
        "sales"
      ],
      "datasets": [
        "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
      ]
    },
    {
      "username": "john@contoso.com",
      "reports": [
        "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
      ]
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2028-07-29T17:58:19Z"
}
```

### Example of generating an embed token for a paginated report with a data source identity

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "datasourceIdentities": [
    {
      "datasources": [
        {
          "datasourceType": "Sql",
          "connectionDetails": {
            "server": "New-Sql-Server",
            "database": "New-Sql-Database"
          }
        }
      ],
      "identityBlob": "eyJ0eX....AAA="
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2028-07-29T17:58:19Z"
}
```

### Example of generating an embed token for a paginated report with multiple data source identities and a single identity blob

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "datasourceIdentities": [
    {
      "datasources": [
        {
          "datasourceType": "Sql",
          "connectionDetails": {
            "server": "New-Sql-Server",
            "database": "New-Sql-Database"
          }
        },
        {
          "datasourceType": "MySql",
          "connectionDetails": {
            "server": "New-MySql-Server",
            "database": "New-MySql-Database"
          }
        }
      ],
      "identityBlob": "eyJ0eX....AAA="
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2028-07-29T17:58:19Z"
}
```

### Example of generating an embed token for a paginated report with multiple data source identities and multiple identity blobs

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "datasourceIdentities": [
    {
      "datasources": [
        {
          "datasourceType": "Sql",
          "connectionDetails": {
            "server": "New-Sql-Server",
            "database": "New-Sql-Database"
          }
        }
      ],
      "identityBlob": "eyJ0eX....AAA="
    },
    {
      "datasources": [
        {
          "datasourceType": "MySql",
          "connectionDetails": {
            "server": "New-MySql-Server",
            "database": "New-MySql-Database"
          }
        }
      ],
      "identityBlob": "eyJ0dW....AAA="
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2028-07-29T17:58:19Z"
}
```

### Example of generating an embed token for a Power BI report with a dataset which is connected with DirectQuery to another Power BI dataset. All related dataset IDs must be specified in the request with 'xmlaPermissions' set to 'ReadOnly'. IdentityBlobs for all SSO-enabled data sources must be provided in the 'datasourceIdentities' array

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd",
      "xmlaPermissions": "ReadOnly"
    },
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
      "xmlaPermissions": "ReadOnly"
    }
  ],
  "reports": [
    {
      "id": "f904e89a-7ebe-4aa0-8647-e409063b4850"
    }
  ],
  "datasourceIdentities": [
    {
      "datasources": [
        {
          "datasourceType": "Sql",
          "connectionDetails": {
            "server": "Best-Sql-Server",
            "database": "Database3"
          }
        }
      ],
      "identityBlob": "eyJ0eX....AAA="
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "ab4d49ae-c054-4c29-af52-93b5c80619ff",
  "expiration": "2022-06-10T12:41:11Z"
}
```

### Example of generating an embed token for a Power BI report with a paginated visual. The paginated report ID ('...4850') of the paginated visual must be included in the 'reports' section of the request.

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    }
  ],
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    },
    {
      "id": "f904e89a-7ebe-4aa0-8647-e409063b4850"
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "49ae3742-54c0-4c29-af52-619ff93b5c80",
  "expiration": "2018-07-29T17:58:19Z"
}
```

### Example of generating an embed token for two datasets with RLS identities and a single report with read-only permissions. The embed token lets you view the report, which is dynamically bound to two different datasets.

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    },
    {
      "id": "e75afc47-1150-45e0-aba7-4eb04e4876e5"
    }
  ],
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "identities": [
    {
      "username": "john@contoso.com",
      "roles": [
        "sales"
      ],
      "datasets": [
        "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
      ]
    },
    {
      "username": "iris@contoso.com",
      "roles": [
        "executive"
      ],
      "datasets": [
        "e75afc47-1150-45e0-aba7-4eb04e4876e5"
      ]
    }
  ]
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "4b76f5ed-5a06-4150-8d1b-60f8e4c186f4",
  "expiration": "2028-07-29T17:58:19Z"
}
```

### Example of generating an embed token that expires no later than ten minutes from the API call

#### Sample request

```http
POST https://api.powerbi.com/v1.0/myorg/GenerateToken
```

- Request Body

```json
{
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    }
  ],
  "reports": [
    {
      "id": "b2e49b01-2356-4456-bfb9-3f4c2bc4ddbd"
    }
  ],
  "identities": [
    {
      "username": "john@contoso.com",
      "roles": [
        "sales"
      ],
      "datasets": [
        "cfafbeb1-8037-4d0c-896e-a46fb27ff229"
      ]
    }
  ],
  "lifetimeInMinutes": 10
}
```

#### Sample response

- Status code:
    - 200

```json
{
  "token": "H4sI....AAA=",
  "tokenId": "4b76f5ed-5a06-4150-8d1b-60f8e4c186f4",
  "expiration": "2028-07-29T17:58:19Z"
}
```

## Definitions

| Name | Description |
| --- | --- |
| DatasourceConnectionDetails | The Power BI data source connection details. See examples in [Get Datasources](/en-us/rest/api/power-bi/datasets/get-datasources#examples) or [Get Datasources In Group](/en-us/rest/api/power-bi/datasets/get-datasources-in-group#examples). |
| DatasourceIdentity | Effective identity for connecting DirectQuery data sources with single sign-on (SSO) enabled. |
| DatasourceSelector | An object that uniquely identifies a single data source by its connection details. |
| EffectiveIdentity | Defines the user identity and roles. For more information, see [Row-level security with Power BI Embedded](/en-us/power-bi/developer/embedded/embedded-row-level-security). |
| EmbedToken | A Power BI embed token |
| GenerateTokenRequestV2 | Power BI Generate Token Request V2 |
| GenerateTokenRequestV2Dataset | A dataset object in GenerateTokenRequestV2 |
| GenerateTokenRequestV2Report | A report object in GenerateTokenRequestV2 |
| GenerateTokenRequestV2TargetWorkspace | A workspace object in GenerateTokenRequestV2 |
| IdentityBlob | A blob for specifying an identity. Only supported for datasets with a DirectQuery connection to Azure SQL |
| XmlaPermissions | XMLA Permissions |

### DatasourceConnectionDetails

Object

The Power BI data source connection details. See examples in [Get Datasources](/en-us/rest/api/power-bi/datasets/get-datasources#examples) or [Get Datasources In Group](/en-us/rest/api/power-bi/datasets/get-datasources-in-group#examples).

| Name | Type | Description |
| --- | --- | --- |
| account | string | The connection account |
| classInfo | string | The connection class information |
| database | string | The connection database |
| domain | string | The connection domain |
| emailAddress | string | The connection email address |
| kind | string | The connection kind |
| loginServer | string | The connection login server |
| path | string | The connection path |
| server | string | The connection server |
| url | string | The connection URL |

### DatasourceIdentity

Object

Effective identity for connecting DirectQuery data sources with single sign-on (SSO) enabled.

| Name | Type | Description |
| --- | --- | --- |
| datasources | DatasourceSelector[] | An array of data sources that this identity applies to. |
| identityBlob | string | A blob for specifying the identity. |

### DatasourceSelector

Object

An object that uniquely identifies a single data source by its connection details.

| Name | Type | Description |
| --- | --- | --- |
| connectionDetails | DatasourceConnectionDetails | The data source connection details. You can obtain the connection details using [Get Datasources for paginated reports](/en-us/rest/api/power-bi/reports/get-datasources-in-group) and [Get Datasources for powerbi reports](/en-us/rest/api/power-bi/datasets/get-datasources-in-group) APIs. |
| datasourceType | string | The type of the [data source](/en-us/power-bi/connect-data/power-bi-data-sources).<br><br><br>| API name for the data source | - | - |<br>| --- | --- | --- |<br>| ActiveDirectory | AdobeAnalytics | AdoDotNet |<br>| AnalysisServices | AzureBlobs | AzureDataLakeStorage |<br>| AzureMarketplace | AzureTables | BizTalk |<br>| CDPA | CustomConnector | CustomHttpApi |<br>| DB2 | Essbase | EventHub |<br>| Excel | Exchange | Extension |<br>| Facebook | File | Folder |<br>| GoogleAnalytics | Hdfs | HDInsight |<br>| Informix | MQ | MySql |<br>| OData | ODBC | OleDb |<br>| Oracle | PostgreSql | PowerQueryMashup |<br>| PubNub | Salesforce | SAPBW |<br>| SAPBWMessageServer | SapErp | SAPHana |<br>| SharePoint | SharePointDocLib | SharePointList |<br>| Sql | Sybase | Teradata |<br>| UIFlow | Web |  | |
| --- | --- | --- |

### EffectiveIdentity

Object

Defines the user identity and roles. For more information, see [Row-level security with Power BI Embedded](/en-us/power-bi/developer/embedded/embedded-row-level-security).

| Name | Type | Description |
| --- | --- | --- |
| auditableContext | string | The EffectiveIdentity auditable context. If this parameter is provided and isn't empty, it will enable auditing of the EffectiveIdentity and its value will be set to the username in the audit record. Otherwise, the EffectiveIdentity context will be omitted from the GenerateToken audit record. |
| customData | string | [Custom data](/en-us/power-bi/developer/embedded/embedded-row-level-security#using-the-customdata-feature) that's used to apply row-level security rules. Supported for live connection to Azure Analysis Services models and cloud models only. |
| datasets | string[] | An array of datasets for which this identity applies |
| identityBlob | IdentityBlob | A blob that specifies an [identity](/en-us/power-bi/developer/embedded/embedded-row-level-security#token-based-identity-sdk-additions). Only supported for datasets with a DirectQuery connection to Azure SQL. |
| reports | string[] | An array of reports for which this identity applies. Only supported for paginated reports. |
| roles | string[] | An array of row-level security (RLS) roles within a token that applies RLS rules. An identity can contain up to 50 roles. A role can contain any character except `,`, and its length must not exceed 50 characters. |
| username | string | The effective username within a token that applies row-level security rules. For an on-premises model, the username can contain alphanumeric or any of the following characters `.`, `-`, `_`, `!`, `#`, `^`, `~`, `\\`, `@`. For cloud models, the username can contain any ASCII character. For either model, the username length must not exceed 256 characters, and the username shouldn't contain spaces. |

### EmbedToken

Object

A Power BI embed token

| Name | Type | Description |
| --- | --- | --- |
| expiration | string (date-time) | The date and time (UTC) of token expiration |
| token | string | The embed token |
| tokenId | string (uuid) | The unique token ID. Through audit logs, the token ID can be used to correlate operations that use the token with the generate operation. |

### GenerateTokenRequestV2

Object

Power BI Generate Token Request V2

| Name | Type | Description |
| --- | --- | --- |
| datasets | GenerateTokenRequestV2Dataset[] | A list of datasets |
| datasourceIdentities | DatasourceIdentity[] | List of identities to use when connecting to data sources with Single Sign-On (SSO) enabled. |
| identities | EffectiveIdentity[] | The list of identities to use for row-level security rules |
| lifetimeInMinutes | integer | The maximum lifetime of the token in minutes, starting from the time it was generated. Can be used to shorten the token's expiration time, but not to extend it. The value must be a positive integer. Zero (`0`) is equivalent to `null`, and will set the default expiration time. |
| reports | GenerateTokenRequestV2Report[] | A list of reports |
| targetWorkspaces | GenerateTokenRequestV2TargetWorkspace[] | The list of workspaces that the embed token will allow saving to |

### GenerateTokenRequestV2Dataset

Object

A dataset object in GenerateTokenRequestV2

| Name | Type | Description |
| --- | --- | --- |
| id | string | The dataset ID |
| xmlaPermissions | XmlaPermissions | XMLA Permissions |

### GenerateTokenRequestV2Report

Object

A report object in GenerateTokenRequestV2

| Name | Type | Description |
| --- | --- | --- |
| allowEdit | boolean | Whether the generated embed token supports report editing |
| id | string (uuid) | The report ID |

### GenerateTokenRequestV2TargetWorkspace

Object

A workspace object in GenerateTokenRequestV2

| Name | Type | Description |
| --- | --- | --- |
| id | string (uuid) | The workspace ID |

### IdentityBlob

Object

A blob for specifying an identity. Only supported for datasets with a DirectQuery connection to Azure SQL

| Name | Type | Description |
| --- | --- | --- |
| value | string | An OAuth 2.0 access token for Azure SQL |

### XmlaPermissions

Enumeration

XMLA Permissions

| Value | Description |
| --- | --- |
| Off | Indicates that the generated embed token doesn't grant access permissions to the dataset's XMLA endpoint. |
| ReadOnly | Indicates that the generated embed token grants Read access permissions to the dataset's XMLA endpoint. |