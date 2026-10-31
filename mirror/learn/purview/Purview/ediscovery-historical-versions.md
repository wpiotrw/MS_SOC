---
layout: Conceptual
title: Set up historical versions in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-historical-versions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use historical versions in eDiscovery (Premium) to collect content from all versions of documents stored in SharePoint and OneDrive.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 0834464e-34a9-0896-a555-9618bd8a328b
document_version_independent_id: 0834464e-34a9-0896-a555-9618bd8a328b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-historical-versions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-historical-versions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-historical-versions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 5e00feed-7b9a-d738-00d7-3000497eccf2
---

# Set up historical versions in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The historical versions feature in eDiscovery (Premium) lets eDiscovery managers in your organization search for and collect content from all versions of documents stored in SharePoint Online and OneDrive for Business. Then you can add that content to a review set for analysis and review. This helps you find and review content from a specific version of a document that may be relevant to a case or investigation, even if the latest version of the same document doesn't contain the relevant information.

To support the historical versions capability in eDiscovery (Premium), SharePoint administrators must enable versioning for sites in their organization. Then, when users modify documents in SharePoint or OneDrive, implicit regular versions are created when document is saved (or autosaved). SharePoint versioning allows for tracking of the activity performed on SharePoint items (including documents, events, and tasks). This versioning capability leaves an audit trail that can provide evidence in legal investigations. These older versions of a document are available to the organization, who may be required to share such versions that have sensitive or relevant content during court discovery in a legal matter.

After an eDiscovery administrator turns on historical versions for the organization and then activates it for specific SharePoint sites, the SharePoint content push service crawls all major and minor versions of documents on the activated sites and then sends those versions for indexing. After the crawling and indexing process is complete, documents and their versions are available for eDiscovery search. As long as a specific version can be accessed (by version history), then that version will be discoverable in an eDiscovery (Premium) collection search.

## Set up historical versions

To enable historical versions in eDiscovery (Premium), your organization has to turn it on and then activate specific sites so that all versions of documents stored on those sites are indexed for search. Before you set up eDiscovery (Premium) for historical versions, you have to enable versioning support in SharePoint.

### Step 1: Turn on versioning in SharePoint

The first step is to turn on versioning in SharePoint Online so that all versions of a document are preserved. For instructions, see [Versioning in SharePoint](/en-us/microsoft-365/community/versioning-basics-best-practices).

Important

Adding SharePoint sites to historical versions isn't currently supported in multi-geo environments. Only the primary domain of your organization is enabled for historical versions.

### Step 2: Turn on historical versions

The next step is to turn on historical versions in eDiscovery (Premium). To turn on historical versions for your organization, a person must be a global administrator or an eDiscovery Administrator (a member of the eDiscovery Administrator subgroup in the eDiscovery Manager role group). After historical versions is turned on, it will apply to your entire organization.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Important

After you turn on historical versions, you won't be able to turn it off during the public preview. You will be able to turn it off after historical versions is released for general availability.

1. In the Microsoft Purview portal, go to [eDiscovery (Premium)](https://go.microsoft.com/fwlink/p/?linkid=2173764), and then select **eDiscovery (Premium) settings**.

    ![Select eDiscovery (Premium) settings](media/historicalversions1.png)
2. On the **Settings** page, select the **Historical versions (preview)** tab, and then switch the **Historical versions tenant control** toggle to on.

    ![Switch on the toggle to enable historical versions](media/historicalversions2.png)

    A warning is displayed that says you won't be able to turn off historical versions. As previously stated, you won't be able to turn off historical versions until the feature is released for general availability.
3. Select **Yes** to turn on historical versions.

### Step 3: Activate SharePoint sites

After you turn on historical versions for your organization, the last step is to activate SharePoint sites to support historical versions. When you activate a site (by adding it to a list of sites on the **Historical versions** tab), the site is recrawled and all versions of documents stored on that site are indexed for search.

Note

There is a limit of 100 site activations per organization during the public preview of historical versions. An activation is counted against this limit whenever you enable or disable a site for historical versions. If you enable multiple sites, each site is counted as a single activation. The total number of activations is displayed on the **Historical versions** tab.

1. On the **Historical versions** tab on the eDiscovery (Premium) **Settings** page, select **Enable** to activate sites for historical versions.

    ![Select Enable to activate sites for historical versions](media/historicalversions3.png)

    A flyout out page is displayed that contains a list of all SharePoint sites in your organization.
2. Select a site to activate, and then select **Enable** to activate it for historical versions. You can use the search box to search for a specific site.

    A warning is displayed that says document versions on the site will be indexed and this indexing process will take some time before the versions will be ready to be searched. The warning also states that you won't be able to disable historical versions for the selected site for 30 days.
3. Select **Yes** to activate the site for historical versions.

    ![The activated site and the number of site activations are displayed](media/historicalversions4.png)

    The site is added to the list of activated sites. The counter showing the number of site activations is also updated.
4. Repeat the previous steps for each site that you want to activate for historical versions.

## Frequently asked questions

**How are historical versions different that the option to "collect all versions" when you commit a collection estimate to a review set?**

Currently, only the latest version of documents is indexed for search. That means when you run a collection estimate, only the latest versions of documents are searched. If a document matches the keyword query for the collection, it is returned in the collection results. However, if the latest version of a document doesn't match a search query, the document won't be returned event if older versions of the document contain the keyword. To help mitigate this situation, eDiscovery (Premium) gives you the ability to collect all versions of the document when you [commit a collection to a review set](ediscovery-commit-draft-collection#commit-a-collection-estimate-to-a-review-set). That means any older version that may contain the keyword will be added to the review set.

Historical versions are different and more efficient than "collecting all versions" because when you activate a site, all versions of a document (and not just the last version) are indexed for search. The result is that if an older version of a document contains a keyword that matches the search query, it will be returned by the collection.

**When historical versions is enabled for a site, does it impact the performance of the site?**

No. Once historical versions is enabled for a site, the performance for the site will the same as it was before the site was enabled. The crawling and indexing processes that are performed on the site after it's enabled will occur at a slower rate and be performed during off-peak hours. Enabling historical versions for a site will kick off a backfill process, which finds all the versions of documents on the site and then sends those versions to the index. Depending on the number of document versions for site, this backfill process might impact service health. We have mitigated this potential impact in the following ways:

- We make the best effort to process these versions during off-peak hours.
- We process document versions in our lowest priority queues, which allows most service resources to be delegated to user changes.

**How long do I have to wait after a site is activated until all historical versions of documents on that site are all indexed and available for eDiscovery search?**

Based on the number of documents for a site and the average number of versions per document, we try to estimate the total number of files per site. Based on this, an estimate of how long it may take to index is as follows:

`Number of versions / (Processing rate of 100,000 files per day ) + .5 days = Total number of days to process a site`

The half-day is added as a buffer since indexing of versions on site is optimized to run during off-peak hours.

For example, if the total number of documents and all versions for a site is 150,000 then it will take at least two days to process the site for historical versions:

`150,000 files/100,000 files per day + .5 days = 2 days`

**Why is it not recommended to frequently activate or deactivate sites for historical versions?**

When you deactivate a previously activated site, a clean-up process is triggered. This process will take time to complete. If that same site is activated again, the backfill process of reindexing the site has to be rerun. Both the clean-up and backfill processes are time- and resource-intensive. Therefore we recommended that you carefully consider and plan which sites you want to activate for historical version so you can avoid repeatedly activating and deactivating historical versions for a site.