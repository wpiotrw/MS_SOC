---
layout: Conceptual
title: Troubleshoot Microsoft Purview policies for SQL data sources | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/troubleshoot-policy-sql
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Check how to see if SQL data sources are receiving policies from Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: tutorial
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: afc23b75-cce7-0ba9-fd78-d1eaf3b7eb5d
document_version_independent_id: afc23b75-cce7-0ba9-fd78-d1eaf3b7eb5d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/troubleshoot-policy-sql.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/troubleshoot-policy-sql
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/troubleshoot-policy-sql.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: 9aa3a32a-2aa7-f300-73fe-5839609fb4ca
---

# Troubleshoot Microsoft Purview policies for SQL data sources | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

In this tutorial, you learn how issue SQL commands to inspect the Microsoft Purview policies that have been communicated to the SQL instance, where they'll be enforced. You'll also learn how to force a download of the policies to the SQL instance. These commands are only used for troubleshooting and aren't required during the normal operation of Microsoft Purview policies. These commands require a higher level of privileges in the SQL instance.

For more information about Microsoft Purview policies, see the concept guides listed in the Next steps section.

## Prerequisites

- An Azure subscription. If you don't already have one, [create a free subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A Microsoft Purview account. If you don't have one, see the [quickstart for creating a Microsoft Purview account](../create-microsoft-purview-portal).
- Register a data source, enable *Data policy enforcement*, and create a policy. To do so, use one of the Microsoft Purview policy guides. To follow along with the examples in this tutorial, you can [create a DevOps policy for Azure SQL Database](../how-to-policies-devops-azure-sql-db).

## Test the policy

Once you create a policy, the Microsoft Entra principals referenced in the Subject of the policy should be able to connect to any database in the server to which the policies are published.

### Force policy download

It's possible to force an immediate download of the latest published policies to the current SQL database by running the following command. The minimal permission required to run it's membership in ##MS\_ServerStateManager##-server role.

```sql
-- Force immediate download of latest published policies
exec sp_external_policy_refresh reload
```

### Analyze downloaded policy state from SQL

The following DMVs can be used to analyze which policies have been downloaded and are currently assigned to Microsoft Entra principals. The minimal permission required to run them is VIEW DATABASE SECURITY STATE - or assigned Action Group *SQL Security Auditor*.

```sql

-- Lists generally supported actions
SELECT * FROM sys.dm_server_external_policy_actions

-- Lists the roles that are part of a policy published to this server
SELECT * FROM sys.dm_server_external_policy_roles

-- Lists the links between the roles and actions, could be used to join the two
SELECT * FROM sys.dm_server_external_policy_role_actions

-- Lists all Microsoft Entra ID principals that were given connect permissions  
SELECT * FROM sys.dm_server_external_policy_principals

-- Lists Microsoft Entra ID principals assigned to a given role on a given resource scope
SELECT * FROM sys.dm_server_external_policy_role_members

-- Lists Microsoft Entra ID principals, joined with roles, joined with their data actions
SELECT * FROM sys.dm_server_external_policy_principal_assigned_actions
```