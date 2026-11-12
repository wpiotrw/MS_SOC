---
layout: Conceptual
title: Disaster Recovery for Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-disaster-recovery
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-10-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.custom: msecd-doc-authoring-1030
ms.localizationpriority: medium
ms.collection:
- tier2
search.appverid:
- MET150
- MOE150
description: Learn how to configure a disaster recovery (BCDR) environment for Microsoft Purview Unified Catalog using manual methods and the governance REST APIs.
ai-usage: ai-assisted
locale: en-us
document_id: e8417816-d82f-e8a6-e81a-6ee4c5c339de
document_version_independent_id: e8417816-d82f-e8a6-e81a-6ee4c5c339de
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-disaster-recovery.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-disaster-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-disaster-recovery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 33e15ad6-a188-1abf-6eef-508073fb8c9c
---

# Disaster Recovery for Microsoft Purview Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article provides guidance on backup and recovery strategy when using [Microsoft Purview Unified Catalog](unified-catalog) in production deployment. The scope of this article is to cover manual business continuity and disaster recovery (BCDR) methods that you can set up using APIs.

## Features covered

The following areas are covered in this BCDR strategy:

- Unified Catalog foundation: Governance Domains, Glossary Terms, and Data Assets — the foundational catalog that organizes and describes an organization's data estate.
- Data products: Curated, business-ready data sets with ownership, documentation, terms of use, and audience metadata.
- Critical data elements: Regulated or high-value data elements (for example, personal data, financial identifiers) with lifecycle management (Draft → Published → Expired).
- Data quality: Quality rules and asset metadata that track data health and conformance across the estate.
- Data access: Access request workflows, multi-stage approval chains, policy sets, and permitted use-case definitions for governed data sharing.
- Data estate health: CDMC control templates and analytics schedules that continuously measure governance maturity and compliance posture.
- Workflows: Configurable multi-stage approval workflows including manager, privacy, and approver stages for data access governance.

## BCDR workflow

### Step 1. Create an Enterprise tier account

Create a Purview Data Governance account at the **Enterprise** tier. This serves as the **primary account** with full governance capabilities.

### Step 2. Request Classic Purview provisioning in a secondary region

Create a **support ticket** through the Customer Support channel requesting enablement of Classic Purview account provisioning in a **secondary (paired) region** for BCDR purposes.

### Step 3. Create a Classic Purview account

After Classic provisioning is enabled in the secondary region, create a **Classic Purview account**. This account serves as the **secondary (backup) account** with limited capabilities.

### Step 4. Copy data from the Enterprise account to the Classic account

Using the available BCDR APIs (described in the API details section), copy governance data from the **Enterprise account (primary)** to the **Classic account (secondary)**. This includes:

- Governance domains
- Data products
- Glossary terms
- Critical data elements
- Data assets
- Data Quality metadata
- Data estate health configuration
- Data access workflows and policies

### Step 5. Manage GUIDs during backup

You're responsible for **managing and mapping globally unique identifiers (GUIDs)** during the backup process. Because the secondary account generates new identifiers, you must maintain a mapping between primary and secondary GUIDs to ensure data consistency and traceability.

### Step 6. Validate the secondary account

Use the **GET APIs** for each feature area to validate that all governance data is replicated to the secondary account:

- `GET /catalog/businessdomains`
- `GET /catalog/dataProducts`
- `GET /catalog/terms`
- `GET /catalog/criticalDataElements`
- `GET /catalog/dataAssets`
- `GET /quality/bulk-asset-metadata`
- `GET /health/analytics/schedule`
- `GET /dataaccess/workflows`

### Step 7. Fail over during a disaster recovery (DR) event

When a disaster recovery event occurs, create a **support ticket** requesting:

1. **Promote** the Secondary (Classic) account to **Enterprise** tier
2. **Demote** the Primary (Enterprise) account to **Secondary**

This completes the failover, and the previously secondary account becomes the new primary with full Enterprise capabilities.

## API details

### 1. Account and provisioning

#### Get current policies

Verify the BCDR account is operational by listing the current user's policies.

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/policies
```

Note

Account provisioning is performed with **Is BCDR = true**. Acquire tokens by using standard [Microsoft Entra ID/OAuth flows](/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow) for Purview REST APIs.

### 2. Governance domains

#### Create governance domain

Create a governance domain:

```http
POST https://<accountName>.purview.azure.com/datagovernance/catalog/businessdomains
```

**Request body:**

```json
{
  "name": "BCDR - My Business Domain",
  "type": "DataDomain",
  "status": "Draft",
  "description": "Optional description up to 200k chars",
  "isStagingDomain": false,
  "managedAttributes": []
}
```

**Response body:**

```json
{
  "status": "Draft",
  "type": "DataDomain",
  "name": "BCDR - My Business Domain",
  "description": "Optional description up to 200k chars",
  "isRestricted": false,
  "isStagingDomain": false
}
```

#### Get governance domains

List the governance domains to confirm replication:

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/businessdomains
```

### 3. Data products

#### Create data product

Create a data product under a governance domain:

```http
POST https://<accountName>.purview.azure.com/datagovernance/catalog/dataProducts
```

**Request body:**

```json
{
  "name": "BCDR - Sales Analytics",
  "domain": "<businessDomainId>",
  "status": "Draft",
  "type": "Analytical",
  "endorsed": false,
  "contacts": {
    "owner": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ]
  },
  "description": "Aggregated sales data across regions",
  "businessUse": "Used for quarterly reporting",
  "audience": [
    "DataAnalyst",
    "BusinessUser"
  ],
  "updateFrequency": "Monthly",
  "termsOfUse": [
    {
      "name": "Data Policy",
      "url": "https://contoso.com/policy"
    }
  ],
  "documentation": [
    {
      "name": "User Guide",
      "url": "https://contoso.com/guide"
    }
  ]
}
```

**Response body:**

```json
{
  "status": "Draft",
  "type": "Analytical",
  "name": "BCDR - Sales Analytics",
  "description": "Aggregated sales data across regions",
  "businessUse": "Used for quarterly reporting",
  "updateFrequency": "Monthly",
  "endorsed": false
}
```

#### Get data products

List the data products:

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/dataProducts
```

### 4. Glossary terms

#### Create term

Create a glossary term under a governance domain:

```http
POST https://<accountName>.purview.azure.com/datagovernance/catalog/terms
```

**Request body:**

```json
{
  "name": "BCDR - Customer Revenue",
  "domain": "<businessDomainId>",
  "status": "Draft",
  "description": "Total revenue attributed to a customer",
  "acronyms": [
    "CR",
    "CustRev"
  ],
  "contacts": {
    "owner": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ],
    "expert": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ]
  },
  "resources": [
    {
      "name": "Wiki",
      "url": "https://contoso.com/wiki/customer-revenue"
    }
  ]
}
```

**Response body:**

```json
{
  "status": "Draft",
  "name": "BCDR - Customer Revenue",
  "description": "Total revenue attributed to a customer",
  "contacts": {
    "owner": [],
    "expert": []
  },
  "isMigrated": false
}
```

Note

The API response may return empty `contacts` arrays even when contacts are provided in the request. Contacts are linked asynchronously and will appear on subsequent GET calls.

#### Get terms

List the glossary terms:

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/terms
```

### 5. Critical data elements (CDE)

#### Create critical data element

Create a critical data element under a governance domain:

```http
POST https://<accountName>.purview.azure.com/datagovernance/catalog/criticalDataElements
```

**Request body:**

```json
{
  "name": "BCDR - Customer SSN",
  "domain": "<businessDomainId>",
  "status": "Draft",
  "dataType": "DateTime",
  "description": "Social Security Number — regulated PII element",
  "contacts": {
    "owner": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ],
    "expert": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ]
  }
}
```

**Response body:**

```json
{
  "status": "Draft",
  "dataType": "DateTime",
  "name": "BCDR - Customer SSN",
  "description": "Social Security Number - regulated PII element"
}
```

> 
> **CDE Data Types:** Boolean, DateTime, Number, Text **CDE Status Lifecycle:** Draft → Published → Expired

#### Get critical data elements

List the critical data elements:

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/criticalDataElements
```

### 6. Data assets

#### Create data asset

Create a data asset that references a source:

```http
POST https://<accountName>.purview.azure.com/datagovernance/catalog/dataAssets
```

**Request body:**

```json
{
  "name": "gold",
  "type": "ADLSGen2Path",
  "source": {
    "type": "PurviewDataMap",
    "accountName": "BCDRSecondary",
    "assetId": "<assetGuid>",
    "assetType": "azure_datalake_gen2_filesystem",
    "fqn": "https://<storageAccount>.dfs.core.windows.net/gold"
  },
  "typeProperties": {
    "serverEndpoint": "<storageAccount>.dfs.core.windows.net",
    "container": "gold"
  },
  "contacts": {
    "owner": [
      {
        "id": "<guidObjectId>",
        "info": "<email>"
      }
    ]
  }
}
```

**Response body:**

```json
{
  "name": "gold",
  "status": "ACTIVE",
  "displayText": "gold",
  "source": {
    "type": "PurviewDataMap",
    "assetId": "<assetGuid>"
  }
}
```

#### Get data assets

```http
GET https://<accountName>.purview.azure.com/datagovernance/catalog/dataAssets
```

### 7. Data estate health

#### CDMC control template

CDMC (Cloud Data Management Capabilities) control templates are **auto-created** when the BCDR account is provisioned. A global analytics schedule is enabled by default (daily frequency).

#### Create or update analytics schedule

Create or update the schedule that controls how often data estate health is measured:

```http
PUT https://<accountName>.purview.azure.com/datagovernance/health/analytics/schedule?api-version=2024-02-01-preview
```

**Request body:**

```json
{
  "frequency": "Hour",
  "interval": 6,
  "startTime": "2026-03-18T00:00:00Z",
  "status": "Enabled",
  "timeZone": "UTC"
}
```

**Response body:**

```json
{
  "frequency": "Hour",
  "interval": 6,
  "status": "Enabled",
  "timeZone": "UTC"
}
```

#### Get analytics schedule

Retrieve the current analytics schedule:

```http
GET https://<accountName>.purview.azure.com/datagovernance/health/analytics/schedule?api-version=2024-02-01-preview
```

### 8. Data access

#### Get default access request template

Retrieve the default data access request template:

```http
GET https://<accountName>.purview.azure.com/datagovernance/dataaccess/workflows/templates/dataAccessRequestTemplate
```

#### Create data access workflow

Create or update a data access workflow:

```http
PUT https://<accountName>.purview.azure.com/datagovernance/dataaccess/workflows/{workflowId}
```

The workflow request body is a **large JSON directed acyclic graph (DAG)** that defines multi-stage approvals including:

- `DataSubscriptionWebhook`: subscription trigger
- `DataAccessRequestSubmitted`: entry trigger
- **Manager approval** stage
- **Privacy / compliance approval** stage
- **Approver chain** stages
- **Approve / Reject** terminal actions

#### Apply policy sets to data product

Apply policy sets to a data product to govern access:

```http
PUT https://<accountName>.purview.azure.com/datagovernance/dataaccess/dataProducts/{dataProductId}/policySets/applied?api-version=2023-10-01-preview
```

**Request body:**

```json
{
  "policies": {
    "approvers": [
      {
        "identityType": "User",
        "objectId": "<userObjectId>",
        "tenantId": "<tenantId>"
      }
    ],
    "permittedUseCases": [
      {
        "title": "Assessing Fit",
        "description": "Use to determine if data is useful"
      },
      {
        "title": "Critical Reporting",
        "description": "Use to create high quality reports"
      },
      {
        "title": "Directional Insights",
        "description": "Use to gather directional insights"
      }
    ],
    "managerApprovalRequired": false,
    "privacyComplianceApprovalRequired": false,
    "dataCopyPermitted": false,
    "attestations": [],
    "skipWorkflow": false,
    "maximumAccessDuration": {
      "durationType": "Years",
      "length": 1
    }
  }
}
```

#### List workflows

List the data access workflows:

```http
GET https://<accountName>.purview.azure.com/datagovernance/dataaccess/workflows
```

#### Get approvals

Retrieve pending data access approvals:

```http
GET https://<accountName>.purview.azure.com/datagovernance/dataaccess/approvals?approvalStatus=Pending&api-version=2023-10-01-preview
```

#### Get workflow runs

Retrieve the data access workflow runs:

```http
GET https://<accountName>.purview.azure.com/datagovernance/dataaccess/workflowRuns?ignoreActionStatuses=true&api-version=2023-10-01-preview
```

### 9. Data Quality

#### Create bulk asset metadata

Create bulk asset metadata for data quality:

```http
PUT https://<accountName>.purview.azure.com/datagovernance/quality/bulk-asset-metadata
```

Note

The request body references an external JSON file (`BCDR-DQ-Create Metadata.json`). Contact your support representative for the complete payload.

#### Get bulk asset metadata

Retrieve the bulk asset metadata:

```http
GET https://<accountName>.purview.azure.com/datagovernance/quality/bulk-asset-metadata
```