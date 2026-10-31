---
layout: FAQ
title: Frequently Asked Questions About Microsoft Purview Data Governance Solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-faq
summary: ''
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article answers frequently asked questions about Microsoft Purview data governance solutions.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.service: purview
ms.subservice: purview-data-governance
ms.topic: faq
ms.date: 2024-05-16T00:00:00.0000000Z
locale: en-us
document_id: 9bf3f0b7-61d0-f57b-c243-a9d65d941271
document_version_independent_id: 9bf3f0b7-61d0-f57b-c243-a9d65d941271
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 52ba990f-ec6e-9b4e-5909-3834d521383b
---

# Frequently Asked Questions About Microsoft Purview Data Governance Solutions | Microsoft Learn

## Overview

Many organizations lack a holistic understanding of their data. It's challenging to understand what data exists, where data is located, and how to find and access relevant data. Data lacks context such as lineage, classification, and comprehensive metadata, making it difficult for business users to search for the right data and use that data appropriately. As a result, only a small fraction of collected data is used to inform business decisions. Finally, identifying data security issues and protecting sensitive data is inconsistent. It requires ongoing time and effort, especially while maintaining data agility.

Microsoft Purview data governance solutions help customers gain deep knowledge of all their data while maintaining control over its use. With our tools, organizations discover and curate data. They gain insights into their data estate and centrally govern access to data.

## Purpose of this FAQ

This FAQ answers common questions that customers and field teams often ask about Microsoft Purview data governance solutions: Microsoft Purview Data Map and Microsoft Purview Unified Catalog.

## Where can I submit feedback or feature requests?

If you have an issue with Microsoft Purview Data Map or Unified Catalog, [reach out to support](https://azure.microsoft.com/support/create-ticket/).

If you have feedback about the documentation, reach out using the feedback button at the bottom of every documentation page.

## What are the source types available for metadata scanning and classification?

There are many sources available, and we're adding more all the time. For a full list of sources and all their available capabilities, see our [supported data sources article](data-map-data-sources).

## Does the Microsoft Purview Data Map support scanning zipped files?

Currently, the Microsoft Purview Data Map supports scanning GZIP files that contain a single CSV. For more information, see [supported file types for scanning.](data-map-data-sources#file-types-supported-for-scanning)

## Do scans in the Microsoft Purview Data Map impact operational database performance?

It depends. The amount of load on a database will be dependent on the number of assets being scanned, and complexity of the table schema (like number of columns, etc.). The Microsoft Purview Data Map only samples a subset of the data to determine classification. For sampling related details, see the [supported data sources documentation](data-map-data-sources). It's recommended to schedule scans outside of normal business hours. For scanning best practices, see the [scanning best practices documentation](data-map-scanning-best-practices).

## Can I customize the number of rows scanned?

No. Number of rows scanned is determined by the data source being scanned. For more information, see [our sampling documentation.](data-map-data-sources#sampling-data-for-classification)

## What data systems/processors can we connect and get lineage?

Our lineage offering updates often. For a full list of systems, see our [lineage user guide](data-gov-classic-lineage-user-guide).

## How are Azure Unified Catalog (ADC) Gen 2, Azure Information Protection, and Microsoft Purview (formerly Azure Purview) related?

Microsoft Purview (formerly Azure Purview) originally began as ADC Gen 2 but has since broadened in scope. It now embraces the advanced catalog capabilities of ADC Gen 2 combined with the data classification, labeling, and compliance policy enforcement capabilities of Azure Information Protection. Microsoft Purview now houses compliance and data governance tools to manage your full data estate. For more information, see [our overview documentation.](purview)

## What happens to customers using ADC Gen 1?

Microsoft Purview is the focus of all product innovation in the catalog solution space for Microsoft. ADC Gen 1 is being retired in 2024.

## How do I migrate existing ADC Gen 1 data assets to Microsoft Purview?

Use the Microsoft Purview APIs to extract from ADC Gen 1 and ingest into Microsoft Purview. For the glossary, we support bulk tools based on CSV.

## How do I encrypt sensitive data for SQL tables using Microsoft Purview?

Data encryption is done at the data source level. Microsoft Purview stores only the metadata. It doesn't preview data.

## What's the difference between a glossary and classification?

A glossary uses a naming convention followed by non-technical/business users of the data, also known as data consumers. These types of people are business analysts or data scientists who use Microsoft Purview to search for certain types of data, based on business usage. For instance, supply chain analysts might need to search for the terms *SKU types* and *shipment details*. They search the glossary for these terms to find relevant data. Classification is a tag applied to a data asset at the table, column, or file level that identifies what data exists in the asset. Classification can be applied automatically or manually, based on the type of data found. Typically, you use classification tags to identify whether an asset contains sensitive data, and what type of sensitive data that might be.

## Can the Microsoft Purview Data Map scan and classify emails, PDFs etc. in my SharePoint and OneDrive?

Scanning for on-premises SharePoint sites and libraries is provided through the [Microsoft Purview Information Protection scanner](deploy-scanner). The scanner is available for use through a customer's Microsoft 365 subscription with the following SKUs: AIP P1, EMS E3, and Microsoft 365 E3. If you have any one of these SKUs, you should have the right entitlements to start using the Microsoft Purview Information Protection scanner. However, currently, the Microsoft Purview Data Map doesn't support scanning SharePoint and OneDrive into the [Microsoft Purview Unified Catalog](unified-catalog). Follow these links for [supported file types for the Microsoft Purview Information Protection scanner](information-protection-client#supported-file-types), and [supported file types for the Microsoft Purview Unified Catalog](data-map-data-sources).

## What is the compute used for the scan?

There's a Microsoft-managed scanning infrastructure. For most Azure/AWS resources that we support, you don't need to deploy a scanning infrastructure.

## Is there a way to create a Microsoft Purview account programatically? For example, using Azure Resource Manager (ARM) template / CLI / PowerShell?

Yes, [PowerShell commands](create-microsoft-purview-powershell), [a .NET script](create-microsoft-purview-dotnet), [a Python script](create-microsoft-purview-python), [an ARM template](data-gov-classic-instance-create-arm), and [a Bicep template](quickstart-bicep-create-microsoft-purview) are all available.

## I'm already using Atlas, can I easily move to Microsoft Purview?

Microsoft Purview is compatible with Atlas API. If you're migrating from Atlas, it's recommended to scan your data sources first using Microsoft Purview. Once the assets are available in your account, you can use similar Atlas APIs to integrate such as updating assets or adding custom lineage. Microsoft Purview modifies the Search API to use Azure Search so you should be able to use Advance Search.

## Can I register multiple tenants within a single Microsoft Purview account?

No, currently in order to scan another tenant's data source, you need to create a separate Microsoft Purview account in that tenant.

## Does Microsoft Purview support column level lineage?

Yes, Microsoft Purview supports column level lineage.

## Does Microsoft Purview support Soft-Delete?

Yes, Microsoft Purview supports Soft Delete for Azure subscription status management perspective. Microsoft Purview can read subscription states (disabled/warned etc.) and put the account in soft-delete state until the account is restored/deleted. All the data plane API calls will be blocked when the account is in soft delete state and only GET/DELETE control plane API calls will be allowed. You can find additional information in Azure subscription states page [Azure Subscription Status](/en-us/azure/cost-management-billing/manage/subscription-states).

## Does Microsoft Purview Data Map support data loss prevention (DLP) capabilities?

No, the data map doesn't currently provide the data loss prevention capabilities that are supported for Microsoft 365 apps and services.

Read about [Data Loss Prevention in Microsoft Purview Information Protection](information-protection#prevent-data-loss) if you're interested in data loss prevention for Microsoft 365 apps and services.

## Can I use the same self-hosted integration runtime (SHIR) for both Microsoft Purview and Azure Data Factory?

No. For more information about the SHIR, see our [self-hosted integration runtime documentation](data-map-integration-runtime-self-hosted).

## How do I use the REST API for Microsoft Purview?

You can follow our documentation for examples: [using the REST API to access the Unified Catalog](data-gov-api-rest-data-plane), and [using the REST API to manage access control](tutorial-metadata-policy-collections-apis). We also have a tutorial for using the [Python SDK](data-gov-python-sdk), and [Atlas 2.2 APIs](data-gov-api-atlas-2-2).

## What network, security, and firewall configurations are recommended for Microsoft Purview?

For network, security, and firewall configuration recommendations, see our [security best practices documentation.](data-gov-classic-security-best-practices)