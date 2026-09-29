---
layout: Conceptual
title: Migrate from legacy alerts to the alerts and incidents API - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: FaithOmbongi
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: security
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: upgrade-and-migration-article
description: Learn how to migrate your apps from the deprecated Microsoft Graph security alerts v1 API to the new alerts and incidents API in Microsoft 365 Defender.
ms.reviewer: Austin.Beauchamp,fengzhu
ms.localizationpriority: medium
doc_type: conceptualPageType
ms.date: 2026-05-14T00:00:00.0000000Z
locale: en-us
document_id: 02c067a7-a15c-9668-bbae-e1a9323afdfe
document_version_independent_id: 02c067a7-a15c-9668-bbae-e1a9323afdfe
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/alertsv1-alertsv2-migration.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: alertsv1-alertsv2-migration
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/alertsv1-alertsv2-migration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
platformId: f6b4c5c6-c3b9-ddbc-8277-0470ee14c71e
---

# Migrate from legacy alerts to the alerts and incidents API - Microsoft Graph | Microsoft Learn

The legacy Microsoft Graph security alerts API available through the `/security/alerts` endpoint is deprecated and will be retired on **October 15, 2026**. If your app currently uses the legacy alerts API to retrieve, monitor, or manage security alerts, you should migrate to the new [alerts and incidents API](/en-us/graph/api/resources/security-alert) in Microsoft 365 Defender, available through the `/security/alerts_v2` endpoint.

This article describes the key differences between the two APIs, provides a field mapping reference, and outlines the steps to migrate your app.

Important

- After October 15, 2026, the legacy `/security/alerts` endpoint will stop returning data. Migrate your apps before this deadline to avoid disruption to your security operations workflows.
- The new alerts and incidents API is **not** a direct, one-to-one replacement for the legacy alerts API. It surfaces alerts that are part of the Microsoft 365 Defender ecosystem. Alerts from sources that aren't integrated with Microsoft 365 Defender—such as a Microsoft Sentinel workspace that isn't connected to the Microsoft Defender portal, or standalone and tuned alerts—aren't returned by the new API. Review the known differences and limitations section before you begin your migration.

## Before you begin

Before you start your migration, complete the following tasks:

- Identify all integrations, scripts, connectors, and downstream processes that call `/security/alerts`.
- If you use Microsoft Sentinel, verify whether your workspace is connected to the Microsoft Defender portal. Sentinel-generated alerts aren't available through the v2 API until you complete that onboarding. In the interim, use the [Sentinel REST API](/en-us/rest/api/loganalytics/) to retrieve Sentinel alerts. Standalone Sentinel alerts aren't supported in the v2 API, and the Sentinel REST API will be retired in the future.
- Review the known differences and limitations to identify any supplemental data sources your workflows may require.

## Why migrate?

The new alerts and incidents API offers significant improvements over the legacy alerts API:

- **Automatic correlation**: Alerts from multiple signals—identity, endpoint, email, and cloud—are automatically grouped into incidents, giving analysts a broader view of an attack.
- **Richer evidence**: Legacy state collections (`userStates`, `hostStates`, `fileStates`) are replaced by over 40 strongly typed evidence objects, such as `userEvidence`, `azureResourceEvidence`, `aiAgentEvidence`, and `analyzedMessageEvidence` which are easier to work with programmatically.
- **Incident-centric model**: The new API introduces a first-class [incident](/en-us/graph/api/resources/security-incident) object that represents the full attack story, enabling more effective investigation and response.
- **Expanded threat coverage**: The unified API includes additional sources such as Microsoft Purview Data Loss Prevention and Insider Risk Management.
- **Richer threat context**: Alerts and incidents include MITRE ATT&CK techniques, detection sources, and threat classification.

## API differences

### Endpoints

The following table lists the endpoint changes.

| Operation | Legacy endpoint | New endpoint |
| --- | --- | --- |
| List alerts | `GET /v1.0/security/alerts` | `GET /v1.0/security/alerts_v2` |
| Get alert by ID | `GET /v1.0/security/alerts/{id}` | `GET /v1.0/security/alerts_v2/{id}` |
| Update alert | `PATCH /v1.0/security/alerts/{id}` | `PATCH /v1.0/security/alerts_v2/{id}` |
| List incidents | Not available | `GET /v1.0/security/incidents` |
| Get incident by ID | Not available | `GET /v1.0/security/incidents/{id}` |

### Permissions

Your app registration must be updated with new Microsoft Graph permission scopes.

| Scenario | Legacy permission | New permission |
| --- | --- | --- |
| Read alerts | `SecurityEvents.Read.All` | `SecurityAlert.Read.All` |
| Read and write alerts | `SecurityEvents.ReadWrite.All` | `SecurityAlert.ReadWrite.All` |
| Read incidents | API not available | `SecurityIncident.Read.All` |
| Read and write incidents | API not available | `SecurityIncident.ReadWrite.All` |

After you add the new permissions to your app registration, an admin must grant consent before the app can use them in production.

For more information about these permissions, see [Microsoft Graph permissions reference](/en-us/graph/permissions-reference).

### Field mapping

The following table maps legacy [alerts v1](/en-us/graph/api/resources/alert) fields to their [alerts v2](/en-us/graph/api/resources/security-alert) equivalents. This mapping only covers fields that exist in v1 and have a direct or approximate counterpart in v2. The new API includes many additional fields that provide richer context about alerts and incidents.

| v1 field | v2 field | Notes |
| --- | --- | --- |
| azureTenantId | tenantId | Same meaning, renamed property. |
| lastModifiedDateTime | lastUpdateDateTime | Tracks the latest update time. |
| closedDateTime | resolvedDateTime | Represents when the alert was resolved. |
| activityGroupName | actorDisplayName | Renamed field for actor context. |
| feedback | classification + determination | v2 separates disposition from attack-type determination. |
| vendorInformation.provider | serviceSource + productName | Provider metadata is split into an enum and a display name. |
| sourceMaterials[] | alertWebUrl + incidentWebUrl | Portal links now point to the unified Defender experience. |
| eventDateTime | firstActivityDateTime + lastActivityDateTime | Single timestamp becomes a time range. |
| incidentIds[] | incidentId | Each alert now belongs to exactly one incident. |
| userStates[].userPrincipalName | evidence(userEvidence).userAccount.userPrincipalName | User entities move into typed evidence objects. |
| hostStates[].fqdn | evidence(deviceEvidence).deviceDnsName | Host information moves into device evidence. |
| fileStates[].name / fileHash.hashValue | evidence(fileEvidence).fileName / fileDetails.sha256 | File metadata and hashes move into file evidence. |
| networkConnections[].destinationUrl | evidence(urlEvidence).url | Network artifacts decompose into separate evidence types. |
| networkConnections[].destinationAddress | evidence(ipEvidence).ipAddress | IP addresses move into IP evidence. |
| confidence | No direct replacement | Use evidence-level verdict values such as suspicious or malicious instead of a numeric score. |

## Migrate your app

Use these steps to migrate from the legacy alerts API to the new alerts and incidents API.

### Step 1: Identify dependencies

Before you change any code, identify all integrations, scripts, connectors, and downstream processes that currently call `/security/alerts`.

### Step 2: Connect Microsoft Sentinel for unified visibility

If you use Microsoft Sentinel, connect your workspace to the Microsoft Defender portal and confirm that relevant detections are promoted into incidents. Without this integration, Sentinel-generated alerts don't appear in the v2 API.

While you prepare for onboarding, use the [Sentinel REST API](/en-us/rest/api/loganalytics/) to retrieve Sentinel alerts. Be aware that standalone Sentinel alerts aren't supported in the new API model, and the Sentinel REST API will be retired in the future. Prioritize Defender portal onboarding ahead of the October 15, 2026 deadline.

For more information, see [Connect Microsoft Sentinel to the Microsoft Defender portal](/en-us/unified-secops/microsoft-sentinel-onboard) and [Transition your Microsoft Sentinel environment to the Defender portal](/en-us/azure/sentinel/move-to-defender).

### Step 3: Update API endpoints and permissions

For each integration:

1. Replace calls to `/security/alerts` with `/security/alerts_v2` or `/security/incidents` as appropriate for your workflow.
2. Update app registration permissions and obtain admin consent.
3. Document any authentication gaps and resolve them before the retirement deadline.

### Step 4: Update your data model and query logic

The v2 migration requires more than a field-for-field swap. Plan for the following changes:

- **Treat incidents as first-class objects**: In v2, alerts belong to incidents. Consider building your workflow around incidents to get the full attack story.
- **Update parsing and enrichment logic**: Replace references to `userStates`, `hostStates`, `fileStates`, and `networkConnections` with the corresponding typed evidence objects.
- **Rewrite OData filters**: Update query filters to use the new property names and the `evidence/any()` function for evidence-based filtering.

The following examples show common filter rewrites.

**Filter by product or source**

```http
# Legacy
GET /v1.0/security/alerts?$filter=vendorInformation/provider eq 'Microsoft Defender ATP'

# New - alerts v2
GET /v1.0/security/alerts_v2?$filter=serviceSource eq 'microsoftDefenderForEndpoint'
```

**Filter by involved user**

```http
# Legacy: No direct OData filter on userStates sub-properties; required client-side filtering.

# New - alerts v2
GET /v1.0/security/alerts_v2?$filter=evidence/any(e: e/microsoft.graph.security.userEvidence/userAccount/userPrincipalName eq 'alice@contoso.com')
```

**Filter by involved device**

```http
# Legacy
GET /v1.0/security/alerts?$filter=hostStates/any(h: h/fqdn eq 'pc123.contoso.com')

# New
GET /v1.0/security/alerts_v2?$filter=evidence/any(e: e/microsoft.graph.security.deviceEvidence/deviceDnsName eq 'pc123.contoso.com')
```

**Incident-centric queries (new capability)**

```http
# Get all active, high-severity incidents
GET /v1.0/security/incidents?$filter=status eq 'active' and severity eq 'high'

# Get all alerts for a specific incident
GET /v1.0/security/incidents/{incidentId}/alerts
```

### Step 5: Validate coverage and downstream workflows

Before you retire your legacy integration:

1. Confirm that expected alerts and incidents are returned by the new API.
2. Verify that downstream workflows—such as automation, reporting, and SIEM ingestion—work correctly after the migration.
3. Review known coverage differences and identify any supplemental data sources you still need.

Use an API testing tool like [Graph Explorer](https://aka.ms/ge) to validate your queries and inspect the new data model.

## Known differences and limitations

- **Microsoft Sentinel coverage**: Sentinel-generated alerts aren't returned by the v2 API unless your Microsoft Sentinel workspace is connected to the Microsoft Defender portal. In the interim, use the [Sentinel REST API](/en-us/rest/api/loganalytics/) to retrieve these alerts.
- **Standalone alerts**: Alerts that exist outside of the Microsoft 365 Defender incident model, including standalone detections not promoted to an incident, aren't returned by the v2 API. Retrieve alerts through the originating product's API or data source.
- **Tuned alerts**: Alerts suppressed by alert-tuning rules aren't returned through the alerts\_v2 endpoint. Review the relevant alert-tuning configuration and use the originating product's API or data source if needed.
- **Low-signal Exchange Online events**: Certain low-signal Exchange Online events, such as mailbox rule creation and message delays, aren't included in alerts\_v2. Retrieve these through audit logs or other relevant Exchange Online data sources, such as [Microsoft Purview Audit](/en-us/purview/audit-search) for mailbox-rule activity and [Exchange Online Message Trace](/en-us/exchange/monitoring/trace-an-email-message/message-trace-modern-eac) for message-delivery and delay investigations.
- **Intune-originated alerts**: Intune-originated alerts aren't available through alerts\_v2. Retrieve the relevant data through the Microsoft Graph Intune APIs that correspond to your specific scenario. See [Working with Intune in Microsoft Graph](/en-us/graph/api/resources/intune-graph-overview) and [Intune devices and apps API overview](/en-us/graph/intune-concept-overview).