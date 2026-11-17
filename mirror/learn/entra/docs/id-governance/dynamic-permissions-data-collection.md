---
layout: Conceptual
title: Data collection for dynamic permissions - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/dynamic-permissions-data-collection
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: OWinfreyATL
ms.author: owinfrey
ms.service: entra-id-governance
manager: dougeby
description: Learn what Snowflake data Microsoft Entra ID Governance dynamic permissions collects, including identity, access, configuration, and activity metadata.
ms.topic: reference
ms.date: 2026-11-16T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: 68d8c5ff-d2c1-c860-0adc-941950572bb3
document_version_independent_id: 68d8c5ff-d2c1-c860-0adc-941950572bb3
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/dynamic-permissions-data-collection.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/dynamic-permissions-data-collection
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/dynamic-permissions-data-collection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
platformId: b6e2f74b-7b41-119a-92b2-a6648910d32e
---

# Data collection for dynamic permissions - Microsoft Entra ID Governance | Microsoft Learn

This reference describes data read by Microsoft Entra ID Governance dynamic permissions for permission remediation from the Snowflake application. This information is leveraged by Microsoft Entra for analyzing non-human identities and ensuring least privilege.

Dynamic permissions is in preview and capabilities are subject to change. Licensing requirements for dynamic permissions have not yet been announced. During preview, dynamic permissions for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite.

## Permissions required for dynamic permissions

Dynamic permissions relies on the effective privileges of the connection identity in each supported application to:

- **Detect excessive access:** Read the identity, role, permission, and activity metadata needed to evaluate agent access.
- **Remediate excessive access:** Revoke or adjust supported role assignments to right-size access, or disable supported identities.
- **Assign task-scoped permissions:** Grant and revoke supported access for an approved task.

The required privileges and supported operations depend on the application.

## Snowflake

When Microsoft Entra is integrated with Snowflake for dynamic permissions, then Microsoft Entra reads Snowflake metadata about users, roles, permissions, objects, security configuration, and activity. Collection depends on the connector's privileges, Snowflake visibility rules, and the features available in your account.

### Identity and configuration data

The following table summarizes the forms of metadata which may be collected.

| Category | Data collected |
| --- | --- |
| Users | User identifiers, names, email addresses, user types, account status, timestamps, session defaults, ownership, comments, and authentication-configuration indicators. |
| Roles and grants | Account, database, application, and instance roles; role properties; privilege grants; user and role assignments; role hierarchies; and grants to Snowflake Native Apps. Grant details include the privilege, object, recipient, grant option, grantor role, and timestamps. |
| Future grants | Definitions of privileges to apply automatically to new objects, including the recipient role, object type, and database or schema scope. These aren't grants on existing objects. |
| Objects and account information | Inventory and properties of database and data objects, compute resources, processing objects, functions, procedures, AI objects, applications, and security objects. Metadata can include names, identifiers, owners, comments, timestamps, object definitions, and service endpoint details. Account context includes organization, account, region, and Snowflake version. |
| Security configuration | Security integration properties exposed by Snowflake, including integration type and enabled status; the account setting for blocking privileged roles in External OAuth; and network and authentication policy inventory. Collection doesn't include every network or authentication policy's full definition. |
| Selected tags | Selected sensitivity, classification, criticality, environment, certification, privacy, and semantic tags. Collected data includes tag values and direct object or column associations, not every tag value or inherited association. |

User authentication indicators describe whether credentials or authentication methods are configured. They aren't password, private-key, or token values.

Role and grant records describe assignments and hierarchies, not a precomputed list of every user's effective privileges.

### Activity data

The default activity lookback is 90 days. This window applies to activity queries, not all metadata collection.

| Activity source | Data collected |
| --- | --- |
| [Login history](https://docs.snowflake.com/en/sql-reference/account-usage/login_history) | The latest successful login per identified user within the collection window, rather than all login attempts. Details include event time, user name, client IP address, client type, authentication factors, and connection information. |
| [Query history](https://docs.snowflake.com/en/sql-reference/account-usage/query_history) | Aggregated query activity by user, role, query type, execution status, errors, and warehouse. Summaries include query counts and first and last occurrence times. Both successful and unsuccessful activity can be represented. Executed SQL text isn't selected. |
| [Access history](https://docs.snowflake.com/en/sql-reference/account-usage/access_history) | Aggregated activity for directly referenced objects, underlying objects, and modified objects. Details include users, object identifiers and types, query counts, latest activity time, and accessed or modified column names. |

Access history collection doesn't include every field in the source view. Collected column names aren't a complete inventory of every column in every table.

### Data boundaries and limitations

This collection doesn't query business-data rows from Snowflake customer-defined tables or select executed SQL text from query history.