---
layout: Conceptual
monikers:
- fabric
- azure-sqldw-latest
- azuresqldb-current
- azuresqldb-mi-current
- aps-pdw-2016
- aps-pdw-2016-au7
- sql-server-linux-2017
- sql-server-linux-ver15
- sql-server-linux-ver16
- sql-server-linux-ver17
- sql-server-2017
- sql-server-ver15
- sql-server-ver16
- sql-server-ver17
defaultMoniker: sql-server-ver17
versioningType: Ranged
title: What's Happening with Azure Data Studio - SQL Server | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/sql/tools/whats-happening-azure-data-studio?view=sql-server-ver17
config_moniker_range: =azuresqldb-current || =azuresqldb-mi-current || =azure-sqldw-latest || >=aps-pdw-2016 || >=sql-server-2017 || >=sql-server-linux-2017 || =fabric || =fabric-sqldb
uhfHeaderId: MSDocsHeader-DocsSQL
toc_preview: true
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/04fe6ee0-3b25-ec11-b6e6-000d3a4f0da0
feedback_help_link_url: https://learn.microsoft.com/answers/tags/191/sql-server
feedback_help_link_type: get-help-at-qna
recommendations: true
breadcrumb_path: ../breadcrumb/toc.json
ms.update-cycle: 365-days
description: Learn about the Azure Data Studio retirement, and the recommended replacement options.
author: rwestMSFT
ms.author: randolphwest
ms.reviewer: tsiddique, roblescarlos
ms.date: 2026-06-09T00:00:00.0000000Z
ms.service: sql
ms.subservice: tools-other
ms.topic: concept-article
ms.collection:
- data-tools
ms.custom:
- deprecation-announcement
locale: en-us
document_id: 14f22414-a55d-dfe3-e040-f947eb468a99
document_version_independent_id: 14f22414-a55d-dfe3-e040-f947eb468a99
original_content_git_url: https://github.com/MicrosoftDocs/sql-docs-pr/blob/live/docs/tools/whats-happening-azure-data-studio.md
default_moniker: sql-server-ver17
site_name: Docs
depot_name: SQL.sql-content
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/SQL.sql-content/{branchName}{pdfName}
asset_id: tools/whats-happening-azure-data-studio
moniker_range_name: bd2b65f370697851c2e4ddc67964ee6b
monikers:
- fabric
- azure-sqldw-latest
- azuresqldb-current
- azuresqldb-mi-current
- aps-pdw-2016
- aps-pdw-2016-au7
- sql-server-linux-2017
- sql-server-linux-ver15
- sql-server-linux-ver16
- sql-server-linux-ver17
- sql-server-2017
- sql-server-ver15
- sql-server-ver16
- sql-server-ver17
item_type: Content
source_path: docs/tools/whats-happening-azure-data-studio.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/911a44a7-2f6c-477c-810f-dc8b7d425cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/539ea068-ca2a-4180-a7b4-63c6319d3620
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/14f2b9d5-6f06-45a8-ac5f-313eaa351153
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03568a16-192d-46df-8ce4-4c75767d9e43
platformId: 16c52a85-fffd-4c2c-aba0-0e251cb39077
---

# What's Happening with Azure Data Studio - SQL Server | Microsoft Learn

Azure Data Studio is retired as of **February 28, 2026** and no longer receives updates or security fixes. Migrate to [Visual Studio Code](https://code.visualstudio.com/download) with the [MSSQL extension](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code) for continued support. Your existing queries, scripts, and database projects work in Visual Studio Code without conversion.

The MSSQL extension for Visual Studio Code includes schema management, query execution, AI-powered assistance, and integrations for source control and CI/CD workflows. For a complete list of features, see [MSSQL extension features](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code#features).

## Replacement options

The following replacement options are available for Azure Data Studio.

# [App / SQL developer](#tab/dev)
Use the [MSSQL extension for Visual Studio Code](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code) for daily work. Queries, scripts, and SQL database projects work without requiring conversion.

- Visual Studio Code includes schema design tools, IntelliSense, built-in Git integration, and CI/CD workflows.
- Continue storing SQL database projects in source control. Open them directly in Visual Studio Code with the MSSQL extension, or in Visual Studio with SSDT.
- [Schema Compare](visual-studio-code-extensions/mssql/mssql-schema-compare), [Schema Designer](visual-studio-code-extensions/mssql/mssql-schema-designer), and [GitHub Copilot integration](visual-studio-code-extensions/github-copilot/overview) are available in the MSSQL extension for Visual Studio Code.

For a full list of features, see [MSSQL extension features](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code#features).

# [Database administrator (DBA)](#tab/dba)
The MSSQL extension for Visual Studio Code includes:

- [Database operations](visual-studio-code-extensions/mssql/mssql-database-operations): Create, [back up and restore](visual-studio-code-extensions/mssql/mssql-database-operations#backup-database) databases, rename, and drop databases. Search database objects, and [import flat files](visual-studio-code-extensions/mssql/mssql-database-operations#import-flat-file).
- [Query Profiler](visual-studio-code-extensions/mssql/mssql-query-profiler): Capture real-time database activity using Extended Events.
- [Data-tier Application (DACPAC and BACPAC) import and export](visual-studio-code-extensions/mssql/mssql-data-tier-application): Deploy, extract, import, and export DACPAC and BACPAC files. Also available via [SqlPackage](sqlpackage/sqlpackage) CLI.
- [Schema Compare](visual-studio-code-extensions/mssql/mssql-schema-compare): Compare and synchronize schemas between databases, DACPACs, or SQL projects.
- [SQL Notebooks](visual-studio-code-extensions/mssql/mssql-sql-notebooks): Jupyter-based SQL notebooks for documenting runbooks, troubleshooting steps, and operational procedures.

Keep job scheduling and classic administration tasks in [SQL Server Management Studio (SSMS)](/en-us/ssms), which remains the supported home for SQL Server Agent and general administration.

For migration assessment, use [SQL Server enabled by Azure Arc migration assessment](../sql-server/azure-arc/migration-assessment).

For a full list of features, see [MSSQL extension features](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code#features).

# [Cross-database developer](#tab/xplat)
Replace Azure Data Studio extensions with their Visual Studio Code equivalents:

- **PostgreSQL**: [PostgreSQL extension for Visual Studio Code](/en-us/azure/postgresql/extensions/vs-code-extension/overview)
- **Azure Cosmos DB**: [Azure Databases for Visual Studio Code](/en-us/azure/cosmos-db/visual-studio-code-extension) (Mongo API)
- **MySQL**: Watch Azure Marketplace for a forthcoming MySQL extension

---

### Migration options

Use the dedicated migration tooling for your target: Azure SQL Managed Instance, SQL Server on Azure VMs, or Azure SQL Database. These tools replace the Azure SQL migration extension in Azure Data Studio.

## Migrate to Visual Studio Code

Like Azure Data Studio, Visual Studio Code runs on **Windows**, **macOS**, and **Linux**. It also supports real-time collaboration with [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) and integrates with source control and CI/CD workflows.

Note

Visual Studio Code with the MSSQL extension primarily supports SQL Server, Azure SQL Database, Azure SQL Managed Instance, and SQL database in Fabric.

1. **Install Visual Studio Code and the MSSQL extension**:

    - Download and install [Visual Studio Code](https://code.visualstudio.com/download).
    - Install the [MSSQL extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql) from the Visual Studio Code Marketplace.
2. **Open your existing work**:

    - Open SQL database projects directly in Visual Studio Code. No conversion is needed.
    - Use the same queries and scripts from Azure Data Studio.
3. **Replace Azure Data Studio extensions**: See the following tables for equivalent tools.

### Recommended alternatives for SQL Server capabilities

| Azure Data Studio extension | Description | Replacement |
| --- | --- | --- |
| SQL Server Agent | Manage and automate SQL Server Agent jobs. | [SQL Server Management Studio (SSMS)](/en-us/ssms/sql-server-management-studio-ssms). |
| SQL Server Profiler | Trace and monitor SQL Server activity. | [Query Profiler](visual-studio-code-extensions/mssql/mssql-query-profiler) in the MSSQL extension for Visual Studio Code, and [XEvent Profiler](../relational-databases/extended-events/use-the-ssms-xe-profiler) in SSMS. |
| Database administration | Tools for managing databases on Windows. | [Database operations](visual-studio-code-extensions/mssql/mssql-database-operations) in the MSSQL extension for Visual Studio Code (create, back up, restore, rename, drop, search, and scripting). [SQL Server Management Studio (SSMS)](/en-us/ssms/sql-server-management-studio-ssms) for full administration. |
| Schema management | Compare and synchronize database schemas. | [Schema Compare](visual-studio-code-extensions/mssql/mssql-schema-compare), [Schema Designer](visual-studio-code-extensions/mssql/mssql-schema-designer), and [GitHub Copilot integration in Schema Designer](visual-studio-code-extensions/mssql/mssql-schema-designer-copilot) in the MSSQL extension for Visual Studio Code. Also available in [SQL Database Projects extension](visual-studio-code-extensions/sql-database-projects/sql-database-projects-extension) and SQL Server Data Tools (SSDT). |
| Flat-file import | Import `.txt` and `.csv` files into databases. | [Import flat file](visual-studio-code-extensions/mssql/mssql-database-operations#import-flat-file) in the MSSQL extension for Visual Studio Code. Bulk insert and PowerShell are also available. |
| DACPAC import/export | Deploy and extract DACPAC files. | [Data-tier Application (DACPAC and BACPAC) import and export](visual-studio-code-extensions/mssql/mssql-data-tier-application) in the MSSQL extension for Visual Studio Code, and SqlPackage CLI from the command line. |
| SQL Server assessment | Assess an existing SQL Server data estate to prepare for migration. | [Assess migration readiness with SQL Server enabled by Azure Arc](../sql-server/azure-arc/migration-assessment). |
| Azure SQL migration | Migrate SQL Server to Azure SQL. | Alternative migration tools for [Azure SQL Managed Instance](/en-us/data-migration/sql-server/managed-instance/overview#migration-tools), [SQL Server on Azure VMs](/en-us/data-migration/sql-server/virtual-machines/overview#migrate), and [Azure SQL Database](/en-us/data-migration/sql-server/database/overview#migration-tools). |
| SQL database projects | Create, manage, and deploy SQL database projects. | Fully supported in the [SQL Database Projects extension](visual-studio-code-extensions/sql-database-projects/sql-database-projects-extension) and Visual Studio. |

### Alternatives for non-SQL Server capabilities

| Azure Data Studio extension | Description | Replacement |
| --- | --- | --- |
| **PostgreSQL** | Manage PostgreSQL databases. | [PostgreSQL extension for Visual Studio Code](/en-us/azure/postgresql/extensions/vs-code-extension/overview) |
| **MySQL** | Manage MySQL databases. | Pending announcement |
| **Azure Cosmos DB** | Manage Azure Cosmos DB API for MongoDB. | [Azure Databases for Visual Studio Code](/en-us/azure/cosmos-db/visual-studio-code-extension) |
| **Azure Cosmos DB Migration for MongoDB** | Migrate MongoDB to Azure Cosmos DB. | Pending announcement |

## Why retire Azure Data Studio?

Retiring Azure Data Studio consolidates SQL development tools into Visual Studio Code and other supported tools like [SQL Server Management Studio (SSMS)](/en-us/ssms/sql-server-management-studio-ssms). This allows the product team to focus investment on fewer, more capable tools.

## Resources

| Resource | Description |
| --- | --- |
| [MSSQL extension documentation](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code) | Tutorials and guides for the MSSQL extension for Visual Studio Code. |
| [Community support](https://stackoverflow.com/questions/tagged/visual-studio-code) | Visual Studio Code community and Stack Overflow. |
| [GitHub issues](https://github.com/microsoft/vscode-mssql/issues) | Submit feature requests or report bugs for the MSSQL extension. |

## Frequently asked questions (FAQ)

Here are answers to questions about the Azure Data Studio deprecation and migration to Visual Studio Code.

### What happens to Azure Data Studio after retirement?

Azure Data Studio retired on **February 28, 2026** and is no longer supported. It no longer receives updates, security patches, or maintenance. Migrate to Visual Studio Code with the [MSSQL extension](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code) for continued support.

### Can my queries, scripts, and database projects work in Visual Studio Code?

Yes. Open SQL database projects, queries, and scripts in Visual Studio Code without conversion.

### What about extensions not yet available in Visual Studio Code?

Refer to the alternatives table for replacements. For SQL Server Agent and full administration, use [SQL Server Management Studio (SSMS)](/en-us/ssms/sql-server-management-studio-ssms).

### How do I install the MSSQL extension for Visual Studio Code?

Install it from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql). Detailed steps are available in the [MSSQL extension documentation](visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code#install-the-mssql-extension-in-visual-studio-code).