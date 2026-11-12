---
layout: Conceptual
title: Microsoft Purview metamodel | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-metamodel
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: The Microsoft Purview metamodel helps you represent a business perspective of your data, how it’s grouped into data domains, used in business processes, organized into systems, and more.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: evwhite
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-concept, msecd-doc-authoring-1030
locale: en-us
document_id: cb18450e-86ca-d501-946f-43faef7211d1
document_version_independent_id: cb18450e-86ca-d501-946f-43faef7211d1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-metamodel.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-metamodel
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-metamodel.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: dcdfb9d8-4808-eb8d-0a22-b1d961ed01eb
---

# Microsoft Purview metamodel | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Note

On April 22, 2024 asset types moved to be under the Microsoft Purview Data Catalog feature in the Microsoft Purview portal. Access instructions have been updated.

Metamodel is a feature in the Microsoft Purview Data Catalog that helps add rich business context to your data catalog. It tells a story about how your data is grouped in data domains, how it's used in business processes, what projects are impacted by the data, and ultimately how the data fits in the day to day of your business.

The context metamodel provides is important because business users, the people who are consuming the data, often have nontechnical questions about the data. Questions like: What department produces this dataset? Are there any projects that are using this dataset? Where does this report come from?

When you scan data into Microsoft Purview, the technical metadata can tell you what the data looks like, if the data has been classified, or if it has glossary terms assigned, but it can't tell you where and how that data is used. The metamodel gives your users that information. It can tell you what data is mission critical for a product launch or used by a high performing sales team to convert leads to prospects.

So the metamodel not only helps data consumers find the data they're looking for, but it also tells your data managers what data is critical and how healthy that critical data is, so you can better manage and govern it. For example: you could have different privacy obligations if you use personal information for marketing activities vs. analytics that improve a product or service, and metamodel can help you determine where data is being used.

## So what is the metamodel?

What does it look like? The metamodel is built from **assets** and the **relationships** between them.

For example, you might have a sales reporting team (asset) that consumes data (relationship) from some SQL tables (assets).

When you scan data sources into the data map, you already have the technical data assets like SQL tables available for your metamodel. But what about assets like a sales reporting team, or a marketing strategy that represent processes or people instead of a data source? Metamodel provides **asset types** that allow you to describe other important parts of your business.

An **asset type** is a template for important concepts like business processes, departments, lines of business, or even products. They're the building blocks you'll use to describe how data is used in your business. The **asset type** creates a template you can use over and over to describe specific assets. For example, you can define an asset type "department" and then create new department assets for each of your business departments. These new assets are stored in Microsoft Purview like any other data assets that were scanned in the data map, so you can search and browse for them in the data catalog.

Metamodel includes several [predefined asset types](../how-to-metamodel#predefined-asset-types) to help you get started, but you can also create your own.

Similarly a **relationship definition** is the template for the kinds of interactions between assets that you want to represent. For example, a department *manages* a business process. An organization *has* departments. The business process, organization, and departments are the assets, "manages" and "has" are the relationships between them.

For example, if we want to use Microsoft Purview to show how key data sets are used in our business processes, we can represent that information as a template:

![Diagram showing that a business process uses a dataset.](../media/concept-metamodel/process-dataset.png)

Which we can then use to describe how a specific business process uses a specific data set:

![Diagram mirroring previous diagram showing social media management using customer demographics.](../media/concept-metamodel/specific-example.png)

## Metamodel example

For a simple example of a metamodel, let's consider marketing campaign management in a business. This process is an asset that we'll add to our metamodel. It's not a data source we can scan, since it's a set of business processes, but during this process real data will be used and referenced. It's important to show what data is being used and how, so we can properly manage and govern it. We'll create an asset for the marketing campaign management from the asset type "Business Process".

We know there are two tables in SQL that the marketing campaign management team uses. These are assets too, but they were data source assets created when the SQL database was scanned into the Microsoft Purview Data Map.

The relationship between the marketing campaign management asset and the SQL table assets is that campaign management **consumes**, or uses, the SQL tables when developing campaigns. We can record that in our metamodel, so now anyone that looks at those SQL tables can see that they're being used to develop marketing campaigns. We'll also be able to see if there are any other teams that use this data, or maybe which department develops this data as well. So now, with metamodel, we know not only what the data is, but we have a story about how it's being used that helps us understand and manage it.

![Screenshot of a metamodel showing a marking email report asset connected to two SQL databases through 'consumes' relationships.](../media/concept-metamodel/simple-metamodel-example.png)

And now that marketing campaign management is an asset in your data catalog like any other asset, so you can find it in a search. A user could search for that process and quickly know what data it uses and produces, without needing to know anything about the data beforehand.