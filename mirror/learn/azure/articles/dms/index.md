---
layout: Landing
title: Azure Database Migration Service documentation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/dms/
summary: Azure Database Migration Service enables seamless migrations from multiple database sources to Azure Data platforms with minimal downtime. The service uses the Azure Arc migration readiness assessment to generate assessment reports that provide recommendations to guide you through the changes required before performing a migration. When you're ready to begin the migration process, Azure Database Migration Service performs all the required steps.
breadcrumb_path: ../breadcrumb/azure-databases/toc.json
feedback_help_link_url: /answers/tags/37/azure-database-migration/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
description: Learn how to enable seamless migrations from multiple database sources to Azure Data platforms with minimal downtime by using Azure Database Migration Service.
keywords: azure database migration services, dms service, azure data migration, data migration service, database migration service
author: rwestMSFT
ms.author: randolphwest
ms.reviewer: abhishekum
ms.date: 2026-08-12T00:00:00.0000000Z
ms.service: azure-database-migration-service
ms.topic: landing-page
ms.custom: seo-azure-migrate
locale: en-us
document_id: a63dd0ff-0ba6-5180-bae9-7da94ff500c1
document_version_independent_id: fb2d3cae-0b44-f505-51f0-6990e1304566
original_content_git_url: https://github.com/MicrosoftDocs/azure-databases-docs-pr/blob/live/articles/dms/index.yml
site_name: Docs
depot_name: Learn.azure-databases
page_type: landing
toc_rel: toc.json
asset_id: dms/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/dms/index.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7ce09da1-faab-41d3-88ef-a0ca3bd78eb7
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/216f2a55-66c2-40db-8770-b34875556df7
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: a98e571c-d605-add9-4752-dca0e1cf8c9f
---

# Azure Database Migration Service documentation

Azure Database Migration Service enables seamless migrations from multiple database sources to Azure Data platforms with minimal downtime. The service uses the Azure Arc migration readiness assessment to generate assessment reports that provide recommendations to guide you through the changes required before performing a migration. When you're ready to begin the migration process, Azure Database Migration Service performs all the required steps.

## About Azure Database Migration Service

### Overview

- [What is Azure Database Migration Service?](dms-overview)

### Get started

- [Migrate databases at scale using automation](migration-dms-powershell-cli)
- [Database migration scenario status](resource-scenario-status)

### Quickstart

- [SQL Server migration one-click PoC](http://aka.ms/SQLMigrationPoC)

### video

- [Introduction to Azure Data Migration Service](https://learn-video.azurefd.net/vod/player?id=58ca75ec-3688-4a84-bbf4-cf0265e9ab0d)
- [Cloud Migration Strategies and Phases in Migration Journey](https://learn-video.azurefd.net/vod/player?show=data-exposed&amp;ep=migrating-to-sql-cloud-migration-strategies-and-phases-in-migration-journey-ep-1)
- [Discover and Assess SQL Server Data Estate Migrating to Azure SQL](https://learn-video.azurefd.net/vod/player?show=data-exposed&amp;ep=migrating-to-sql-discover-and-assess-sql-server-data-estate-migrating-to-azure-sql-ep2)
- [Get Started with the New Database Migration Guides to Migrate Your Databases to Azure](https://learn-video.azurefd.net/vod/player?show=data-exposed&amp;ep=get-started-with-the-new-database-migration-guides-to-migrate-your-databases-to-azure)

### What's new

- [Check out our blog](https://techcommunity.microsoft.com/t5/Microsoft-Data-Migration/bg-p/MicrosoftDataMigration)

## Migrate SQL Server to Azure SQL

### Tutorial

- [Migrate to Azure SQL Database (offline)](/en-us/data-migration/sql-server/database/database-migration-service)
- [Migrate to Azure SQL Managed Instance](/en-us/sql/sql-server/azure-arc/migrate-to-azure-sql-managed-instance)
- [Migrate to SQL Server on Azure Virtual Machines (online)](/en-us/data-migration/sql-server/virtual-machines/database-migration-service-online)
- [Migrate to SQL Server on Azure Virtual Machines (offline)](/en-us/data-migration/sql-server/virtual-machines/database-migration-service-offline)

### Reference

- [Custom roles for migrations from SQL Server to Azure SQL Database](/en-us/data-migration/sql-server/database/custom-roles)
- [Custom roles for migrations from SQL Server to Azure SQL Managed Instance](/en-us/data-migration/sql-server/managed-instance/custom-roles)
- [Custom roles for migrations from SQL Server to SQL Server on Azure VMs](/en-us/data-migration/sql-server/virtual-machines/custom-roles)

## Migrate open-source databases to Azure

### Tutorial

- [Migrate to Azure DB for PostgreSQL online via the portal](tutorial-postgresql-azure-postgresql-online-portal)
- [Migrate to Azure DB for PostgreSQL online via the CLI](tutorial-postgresql-azure-postgresql-online)
- [Migrate RDS PostgreSQL to Azure DB for PostgreSQL](tutorial-rds-postgresql-server-azure-db-for-postgresql-online)
- [Migrate between Azure DB for PostgreSQL instances online via the portal](tutorial-azure-postgresql-to-azure-postgresql-online-portal)
- [Migrate to Azure DB for MySQL - offline](tutorial-mysql-azure-mysql-offline-portal)
- [Migrate to Azure DB for MySQL - online](tutorial-mysql-azure-external-to-flex-online-portal)
- [Migrate to Azure DB for MySQL - physical data files](tutorial-mysql-azure-external-online-portal-physical)
- [Migrate MongoDB to Azure DocumentDB](/en-us/azure/documentdb/how-to-migrate-vs-code-extension)
- [Migrate to Azure Cosmos DB for MongoDB - online](tutorial-mongodb-cosmos-db-online)

### Reference

- [Known issues - Online migration to Azure DB for PostgreSQL](known-issues-azure-postgresql-online)
- [Known issues - Migration from MongoDB to Azure Cosmos DB](known-issues-mongo-cosmos-db)

## Tools and guidance

### Reference

- [Services and tools available for data migration scenarios](dms-tools-matrix)
- [Azure Database Migration Guide](/en-us/data-migration/)
- [Azure Migrate](/en-us/azure/migrate/migrate-services-overview)
- [SQL Database Projects](/en-us/sql/tools/visual-studio-code-extensions/sql-database-projects/sql-database-projects-extension)
- [SQL Server Migration Assistant](/en-us/sql/ssma/sql-server-migration-assistant)