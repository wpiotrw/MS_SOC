---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Export Monitor metrics with the Power Platform API - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/monitor-export-metrics?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Export Monitor metrics for Copilot Managed Runtime apps by using a simple REST call. Keep historical records, share insights, and combine data with other sources.
author: arjunmayur
manager: alaug
ms.author: arjunmayur
ms.reviewer: mkaur
contributors: joshuapartlow
ms.date: 2026-11-17T00:00:00.0000000Z
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: a6cfd4c8-dc2a-0d63-61df-67ec00e43b13
document_version_independent_id: a6cfd4c8-dc2a-0d63-61df-67ec00e43b13
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/monitor-export-metrics.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/monitor-export-metrics
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/monitor-export-metrics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 59ead6c8-0c5b-2ac5-23e7-178edc660939
---

# Export Monitor metrics with the Power Platform API - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

The Monitor metrics export API (preview) is a REST endpoint in the Power Platform API. Use this endpoint to retrieve daily metric aggregates for Copilot Managed Runtime apps in OpenTelemetry Protocol JSON (OTLP JSON) format. Store the exported data in a destination that you manage, then use it for historical reports, shared operational insights, or analysis alongside your other data.

The API supports all metrics for Copilot Managed Runtime apps in Monitor. Any script or client that can make authenticated REST requests can retrieve the data. You don't need a specific command-line interface (CLI) or connector.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

## Why export Monitor metrics?

Use exported aggregates to:

- Retain a historical record beyond Monitor's 30-day retention window in your own storage.
- Share insights with authorized IT and operations colleagues who don't have access to Monitor.
- Combine Monitor metrics with deployment history, service inventory, or other operational data to build custom views. This API is specifically for the metric aggregates that you see in Monitor.
- Use OpenTelemetry-compatible pipelines with tools such as Datadog or Splunk, subject to the destination's configuration and historical-data support.

This is a historical pull workflow; it isn't a real-time feed or a replacement for a live telemetry service. Build dashboards against your stored data, not continuous queries to the export API.

## Prerequisites

Before you start, ensure you have the following:

- Power Platform, Global, and AI admins can use the export API. Global Reader and AI Reader roles can't access this export API.
- The environment ID, the product (for example, Copilot Managed Runtime) and product type (for example, App), and an explicit list of 1–10 resource IDs for that environment and type.
- A historical start date and end date within the last 30 days of the export date. Only daily aggregates that are at least one day old are eligible; current-day data isn't available.
- An authenticated REST client and a bearer access token obtained through a supported authentication flow. The PowerShell example requires PowerShell 7.
- A protected storage location and a plan for scheduling, retrying, ingesting, retaining, and controlling access to the exports.
- To find the environment ID of your app:
    - Go to [Copilot Studio](https://copilotstudio.microsoft.com)
    - Use the environment selector on the bottom left of the screen. It's right above your profile photo or initials.
    - Select the environment the app or apps are located in. It's likely to be in the personal environment of the maker who made the app.
    - Once you select the environment, find the environment ID in the URL. For example, if the URL says `https://copilotstudio.microsoft.com/environments/00000000-0000-0000-0000-000000000000/apps`, `00000000-0000-0000-0000-000000000000` is the environment ID for that app.
- You can only export metric data for apps from a specific environment at a time. That means if you have two apps that live in two different environments, you need to create separate data exports for each.

This API is available through the Power Platform API. Before calling it, set up authentication as described in [Power Platform API authentication](/en-us/power-platform/admin/programmability-authentication-v2), and confirm the required permissions in the [Power Platform API permission reference](/en-us/power-platform/admin/programmability-permission-reference).

## Supported products and required inputs

The route supports all metrics in Monitor for Copilot Managed Runtime apps. The following list shows product labels and **API identifier spellings**.

| Product | Sub-product types in Monitor | Product API Identifier | Sub-product API Identifier |
| --- | --- | --- | --- |
| Copilot Managed Runtime | Apps | `MicrosoftApp` | `App` |

The following table provides the metric names that you should use for export requests.

| Sub-product type | Metric | `metricNames`value |
| --- | --- | --- |
| App | App open success rate | `microsoftapp.app_launch` |
| App | App session count | `microsoftapp.app_launch_count` |
| App | Data request success rate | `microsoftapp.data_requests` |
| App | Data request latency | `microsoftapp.data_requests_latency` |
| App | Time to interactive | `microsoftapp.time_to_interactive` |

The route uses `resourceType` and `resourceSubType` to identify the selected product and type. Use the values in the preceding tables when creating the export request.

| Input | Where to provide it | Requirement |
| --- | --- | --- |
| Environment ID | `{environmentId}` in the route | One environment per request. Copy the ID, not the display name. |
| Product identifier | `{resourceType}` in the route | Use the approved API identifier for the product. |
| Sub-product type identifier | `{resourceSubType}` in the route | Use the approved API identifier for the resource type. |
| Resource IDs | Root-level `resourceIds` array in the JSON body | Supply 1–10 distinct IDs. Every resource must belong to the selected environment. |
| Start date | `timeRange.startDate` in the JSON body | Use `YYYY-MM-DD`. Select a historical date within the available 30-day window. |
| End date | `timeRange.endDate` in the JSON body | Use `YYYY-MM-DD`, later than the start date. Exclude current-day data. |

For more than 10 resources, divide the explicit resource list into batches of at most 10. Use separate requests for different environments, and retrieve every page for each batch. If the request returns no data, it means there's no Monitor data for that app or the app doesn't exist in that environment.

## Export the metrics

### Calling Export Metrics via PPAPI and PowerShell

Save the following script as `Export-MonitorMetrics.ps1`. Before running the script, fill in the `environmentId`, `resourceType`, `resourceSubType`, `resourceIds`, and `metricsNames` fields. Use the approved values for `resourceType`, `resourceSubType`, and `metricsNames` as listed earlier in the article. Also, authenticate by using PAC CLI and create an authentication profile. When you run the script, it first asks for the name of the PAC authentication profile that you want to use to export metrics (for example, `ProfileName`). Then, it asks for the `startDate` and `endDate` of the time range you want to request metrics for.

Note

This PowerShell script assumes that you're using Windows PowerShell 7.6.x and a PAC CLI version of 2.13.x or greater. The PAC CLI version needs to have the token command available for this script to work.

The script checks input syntax, duplicate IDs, and the broad 30-day source-history window, not just the interval's length. These checks don't establish the service's exact minimum-age or completeness boundary, authorization, resource membership, or approved product identifiers. Confirm eligible complete days before you run it. The script accepts `{}` as a candidate empty envelope.

```powershell
#requires -Version 7.0
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string] $ProfileName,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string] $StartDate,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string] $EndDate,

    [ValidateNotNullOrEmpty()]
    [string] $OutputRoot = '.\monitor-exports'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Set these values for your environment before running the script.
$apiBaseUri = 'https://api.powerplatform.com'
$environmentId = 'INPUT ENVIRONMENT ID HERE'
$resourceType = 'MicrosoftApp'
$resourceSubType = 'App'
$resourceIds = @(
    'DELETE THIS LINE AND INPUT UP TO 10 RESOURCE IDS HERE'
    'resource-id-1',
    '...',
    'resource-id-10'
)
$metricNames = @(
    'DELETE THIS LINE AND INPUT METRIC NAMES HERE',
    'metric-name-1',
    '...',
    'metric-name-n'
)

if ($environmentId -notmatch '\A(?=.{1,100}\z)[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\z') {
    throw 'Set $environmentId to a valid environment ID before running the script.'
}
if ($resourceIds.Count -lt 1 -or $resourceIds.Count -gt 10) {
    throw 'Set up to 10 resource GUIDs in $resourceIds.'
}

$canonicalResourceIds = [System.Collections.Generic.List[string]]::new()
foreach ($resourceId in $resourceIds) {
    $parsedId = [Guid]::Empty
    if (-not [Guid]::TryParseExact($resourceId, 'D', [ref] $parsedId) -or
        $parsedId -eq [Guid]::Empty) {
        throw 'Every value in $resourceIds must be a non-empty GUID in D format.'
    }
    $canonicalResourceIds.Add($parsedId.ToString('D'))
}
if (@($canonicalResourceIds | Select-Object -Unique).Count -ne $canonicalResourceIds.Count) {
    throw 'Resource IDs in $resourceIds must be unique.'
}

$dateFormat = 'yyyy-MM-dd'
$dateStyles = [Globalization.DateTimeStyles]::AssumeUniversal -bor
    [Globalization.DateTimeStyles]::AdjustToUniversal
try {
    $start = [datetime]::ParseExact(
        $StartDate, $dateFormat, [Globalization.CultureInfo]::InvariantCulture, $dateStyles
    )
    $end = [datetime]::ParseExact(
        $EndDate, $dateFormat, [Globalization.CultureInfo]::InvariantCulture, $dateStyles
    )
}
catch {
    throw 'Use YYYY-MM-DD dates for StartDate and EndDate.'
}
if ($start -ge $end) {
    throw 'StartDate must be earlier than the exclusive EndDate.'
}
if (($end - $start).TotalDays -gt 30) {
    throw 'The requested range cannot exceed 30 days.'
}
if ($end -gt [datetime]::UtcNow.Date) {
    throw 'The exclusive EndDate cannot be later than today in UTC.'
}

$uri = '{0}/monitoringhub/environments/{1}/resourceType/{2}/resourceSubType/{3}/exports/metrics?api-version=1' -f `
    $apiBaseUri.TrimEnd('/'), [Uri]::EscapeDataString($environmentId), [Uri]::EscapeDataString($resourceType), [Uri]::EscapeDataString($resourceSubType)
$body = @{
    metricNames = $metricNames
    resourceIds = @($canonicalResourceIds)
    timeRange = @{
        startDate = $start.ToString($dateFormat, [Globalization.CultureInfo]::InvariantCulture)
        endDate = $end.ToString($dateFormat, [Globalization.CultureInfo]::InvariantCulture)
    }
} | ConvertTo-Json -Depth 5

$token = $null
$authOutput = $null
$headers = $null
$continuation = $null
$outputDirectory = $null
$exportComplete = $false
$seenContinuations = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)

try {
    & pac auth select --name $ProfileName *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "Could not select PAC profile '$ProfileName'. Check it with 'pac auth list'."
    }

    $authOutput = & pac auth token | Out-String
    if ($LASTEXITCODE -ne 0) {
        throw 'PAC token acquisition failed. Check the selected profile and sign in again if needed.'
    }
    $tokenMatch = [regex]::Match(
        $authOutput,
        '(?<![\w.-])eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+(?![\w.-])'
    )
    if (-not $tokenMatch.Success) {
        throw 'PAC did not return a recognizable access token.'
    }
    $token = $tokenMatch.Value
    $authOutput = $null
    $tokenMatch = $null

    $outputDirectory = (New-Item -ItemType Directory -Path $OutputRoot -Force).FullName
    $filePrefix = 'monitoringhub-canvas-export-{0}-{1}' -f `
        (Get-Date -Format 'yyyyMMdd-HHmmss'), ([Guid]::NewGuid().ToString('N'))
    $headers = @{
        Authorization = "Bearer $token"
        Accept = 'application/json'
    }
    $pageNumber = 0

    do {
        if ([string]::IsNullOrWhiteSpace($continuation)) {
            $null = $headers.Remove('x-ms-continuation')
        }
        else {
            $headers['x-ms-continuation'] = $continuation
        }
        $headers['x-ms-client-request-id'] = [Guid]::NewGuid().ToString()

        Write-Host "Requesting export page $($pageNumber + 1)..."
        $response = Invoke-WebRequest `
            -Uri $uri `
            -Method POST `
            -Headers $headers `
            -ContentType 'application/json' `
            -Body $body `
            -TimeoutSec 180 `
            -MaximumRedirection 0 `
            -ErrorAction Stop

        if ($response.StatusCode -ne 200) {
            throw "Unexpected HTTP status $($response.StatusCode)."
        }
        $page = $response.Content | ConvertFrom-Json -ErrorAction Stop
        if ($null -eq $page -or $null -eq $page.PSObject.Properties['resourceMetrics']) {
            throw 'The response is not an OTLP metrics export page.'
        }

        $pageNumber++
        $filePath = Join-Path $outputDirectory (
            '{0}-page-{1:D4}.json' -f $filePrefix, $pageNumber
        )
        [System.IO.File]::WriteAllText(
            $filePath, $response.Content, [System.Text.UTF8Encoding]::new($false)
        )
        Write-Host "Saved page $pageNumber to $filePath"

        $continuation = (@($response.Headers['x-ms-continuation']) -join '').Trim()
        if (-not [string]::IsNullOrWhiteSpace($continuation) -and
            -not $seenContinuations.Add($continuation)) {
            throw 'The service repeated a continuation token; export stopped.'
        }
    }
    while (-not [string]::IsNullOrWhiteSpace($continuation))

    $exportComplete = $true
    Write-Host "Export complete: $pageNumber page(s) saved in $outputDirectory"
}
finally {
    if (-not $exportComplete -and $null -ne $outputDirectory) {
        Write-Warning "Export is incomplete. Any pages already downloaded remain in $outputDirectory"
    }
    if ($null -ne $headers) {
        $headers.Clear()
    }
    $token = $null
    $authOutput = $null
    $continuation = $null
    $seenContinuations.Clear()
}
```

### Export metrics by using your preferred client

#### 1. Select a historical interval

Choose the daily aggregates you need, considering their minimum age and processing time. The following examples use UTC dates with an inclusive start and an exclusive end: `2026-10-20` through `2026-10-27` selects October 20–26, seven daily intervals.

This example assumes an export on **November 3, 2026**. Its selected days are within the preceding 30 days and are more than one day old. Replace the dates when you run an export; these fixed dates aren't a rolling lookback.

Note

Export returns only the metrics from a completed day. Allow for processing time and verify the latest complete interval before scheduling production exports.

#### 2. Prepare authentication and the request

Obtain a bearer token by using the supported Power Platform API authentication flow for an authorized Power Platform, Global, or AI admin. Supply the token securely to your REST client.

The current draft route template is:

```http
POST https://api.powerplatform.com/monitoringhub/environments/{environmentId}/resourceType/MicrosoftApp/resourceSubType/App/exports/metrics?api-version=1
Authorization: Bearer <access-token>
Content-Type: application/json
Accept: application/json
```

**Canvas example** The following URL combines the current global host, environment-scoped route with the canvas identifier pair.

Important

The GUIDs are placeholders; replace them with your own IDs.

```http
POST https://api.powerplatform.com/monitoringhub/environments/00000000-0000-0000-0000-000000000000/resourceType/MicrosoftApp/resourceSubType/App/exports/metrics?api-version=1
```

Send this JSON request body:

```json
{
  "metricNames": [
    "microsoftapp.app_launch",
    "microsoftapp.time_to_interactive"
  ],
  "resourceIds": [
    "<app-id-1>",
    "<app-id-2>"
  ],
  "timeRange": {
    "startDate": "2026-10-01",
    "endDate": "2026-10-31"
  }
}
```

The `resourceIds` array is at the root of the request, not inside a `scope` object. This example doesn't use relative lookback values. If you want all metrics for your export, you can omit the `metricNames` field.

#### 3. Retrieve every response page

The draft paging contract uses the `x-ms-continuation` HTTP header. Keep the route and JSON body unchanged throughout a paging sequence.

1. Send the first POST request without an `x-ms-continuation` request header.
2. Check that the response is successful and contains the expected JSON metrics envelope. Save it as a separate page in staging storage.
3. Read the response's `x-ms-continuation` header. If it contains a nonempty value, send that value in the same header on the next POST request.
4. Repeat until the response header is absent or empty. Only then mark page retrieval complete.

Don't modify, decode, log, or reuse the continuation token with a different request that has a different set of parameters.

Completion of pagination means that you retrieved the response pages for that request. It doesn't prove that every expected app or daily aggregate was available. Reconcile the returned coverage before you use the data.

## Inspect the OTLP metrics payload

A metrics page uses the OTLP JSON `ExportMetricsServiceRequest` structure. The following is a **structure-only illustration**, not a captured API response or an approved metric registry. `example.resource.id` and `example.metric` are placeholder names. The empty data-point array avoids implying an actual measurement.

```json
{
  "resourceMetrics": [
    {
      "resource": {
        "attributes": [
          {
            "key": "example.resource.id",
            "value": {
              "stringValue": "00000000-0000-0000-0000-000000000000"
            }
          }
        ]
      },
      "scopeMetrics": [
        {
          "scope": { "name": "example.scope" },
          "metrics": [
            {
              "name": "example.metric",
              "gauge": { "dataPoints": [] }
            }
          ]
        }
      ]
    }
  ]
}
```

| OTLP field | How to use it |
| --- | --- |
| `resourceMetrics` | Groups metrics by app. Preserve the resource identity and attributes. |
| `scopeMetrics` | Groups metrics by instrumentation scope. |
| `metrics` | Contains metric names, units when present, and the instrument-specific payload. Use the released metric definitions to interpret values. |
| `dataPoints` | Contains aggregate measurements, not individual app sessions, flow runs, or raw events. |
| `startTimeUnixNano`, `timeUnixNano` | Timestamp fields, when present. Preserve their decimal-string encoding and precision; don't replace historical timestamps with ingestion time. |
| `asInt` | A 64-bit integer value encoded as a decimal string in OTLP JSON. Don't convert it through a floating-point type. |
| `asDouble`, `attributes` | A numeric value and dimensions, when present. Preserve dimensions when identifying a time series. |

This metrics API doesn't export logs, recommendation text, or triggered-alert records.

## Store, ingest, and share the data

You own the storage, scheduler, retry policy, ingestion pipeline, downstream permissions, and retention policy. Monitor returns the data; it doesn't provision your destination or continuously deliver exports to it. Refer to OpenTelemetry documentation for setting up your collector and receiver and **ensure the destination accepts historical timestamps, metric types, units, and dimensions.** Check its retention and backfill limits before a large import.

OpenTelemetry supports interoperability with platforms such as Datadog and Splunk, but it doesn't guarantee automatic ingestion, universal native file import, or a configuration-free integration. A receiver, exporter, or transformation might be required for your chosen destination. An export endpoint that returns an OTLP payload isn't itself a configured ingestion pipeline.

### Export implementation tips

Monitor retains daily metric aggregates for 30 days. Also, daily aggregates are the only metrics that are available for export. If you export data for the same app(s) in the same day, you get the same metric data. Design your implementation such that you're exporting data at most once per day, for a given day.

Preserve aggregate semantics. Don't average daily P75 values to calculate a weekly P75, or average rates without the necessary denominators and an approved aggregation method. Daily aggregates aren't raw observations from which every statistic can be reconstructed.

### Control access to exported copies

Apply your organization's data classification, encryption, audit, and least-privilege access policies to export files and derived reports. Grant authorized colleagues access in your destination system. Sharing an exported copy doesn't grant access to the Power Platform admin center, Monitor, or the export API. Review destination access and retention independently of Power Platform roles, and delete stored copies when your policy requires it.

## Limitations

- Exports contain daily metric aggregates only. They don't contain real-time, hourly, or current-day data. Configuring hourly alerts doesn't enable hourly exports.
- Data must be at least one day old and within the last 30 days of the export date.
- Each request requires one environment, one product/type pair, and 1–10 explicit resource IDs. Environment-wide export and tenant-wide unfiltered requests aren't supported.
- Only Power Platform, Global, and AI admins can export. Global Reader and AI Reader roles aren't currently supported.
- This metrics API doesn't export logs, recommendation text, or triggered-alert records.
- Export doesn't create a datastore, schedule recurring calls, ingest data into a destination, or extend Monitor's own retention.

## Troubleshooting

The following guidance is symptom-based. It doesn't define a service error-code schema, throttle quota, continuation lifetime, or availability guarantee.

| Symptom | What to check or do |
| --- | --- |
| Authentication or access is rejected | See [Power Platform API authentication](/en-us/power-platform/admin/programmability-authentication-v2) and [Power Platform API permission reference](/en-us/power-platform/admin/programmability-permission-reference) |
| The request or resource selection is rejected | Check the validated route/version and product/type identifiers. Use an explicit root-level list of 1–10 distinct IDs from the same environment and type. Verify ID values, not display names. |
| The date range is rejected or recent days are missing | Use historical dates within the last 30 days, with start before end. Exclude today and allow for processing time. Verify the latest complete daily interval rather than assuming midnight availability. |
| The export has fewer resources or days than expected | Finish pagination, reconcile scope and returned coverage, and check whether those resources have Monitor data for the selected dates. Don't interpret absent points as zero. |
| The service throttles requests or fails temporarily | Try to reduce the number of calls by breaking up your requests, or waiting in between requests. |
| The destination shows no data or incorrect values | Check the receiver/exporter, credentials, historical timestamp limits, units, dimensions, and integer precision. Confirm that only completed exports were ingested. |

When escalating, include sanitized request scope, the interval, the HTTP status, the time of failure, and a correlation identifier if the service provides one. Don't include bearer tokens, continuation values, or unrestricted exported data.

## Frequently asked questions

### Do I need the Power Platform CLI or a connector?

No. Use any client that can call a REST API with the supported authentication. PowerShell is an example, not product dependency.

### Can I export data for every app in an environment?

Inventory the resources you need and submit explicit batches of up to 10 app IDs. Retrieve every page for every batch. Don't omit `resourceIds` to request an entire environment.

### Can an Operations colleague without Monitor access view the data?

Yes, if your organization authorizes access to the exported copy or report in your destination. That permission doesn't allow the colleague to call the export API or open Monitor in Microsoft 365 admin center.

### Can I recover data from more than 30 days ago?

Export doesn't restore data that ages out of Monitor's window.

### Does an hourly alert produce an hourly export?

No. Alert configuration doesn't change export granularity. The API exports eligible daily aggregates only.

### Does a successful export mean ingestion and coverage are complete?

No. Finish all pages, validate the returned coverage, and separately verify ingestion in your destination.