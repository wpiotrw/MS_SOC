---
layout: Conceptual
title: Create a search for a case in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-query
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to create and run a search for a Microsoft Purview eDiscovery case, select data sources, build queries, and review search results.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom:
- msecd-doc-authoring-1028
locale: en-us
document_id: 8665a433-e076-6aef-98ba-dfe57a9a0ac7
document_version_independent_id: 8665a433-e076-6aef-98ba-dfe57a9a0ac7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-query.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-query
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-query.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 809384f0-3094-fad0-4184-51ac80d42253
---

# Create a search for a case in eDiscovery | Microsoft Learn

Use search in eDiscovery to find in-place content such as email, documents, and instant messaging conversations in your organization that are relevant to a case. Use search to find content in these cloud-based Microsoft 365 data sources:

- Exchange Online mailboxes
- SharePoint sites
- OneDrive accounts
- Microsoft Teams
- Microsoft 365 Groups
- Viva Engage

You can create and run different searches that are associated with the case. Use conditions, such as keywords, to build search queries that return search results with the data that's most likely relevant to the case. You can also:

- View search statistics that might help you refine a search query to narrow the results.
- Preview the search results to quickly verify whether the relevant data is being found.
- Revise a query and rerun the search.

After you search for and find data that's relevant to your investigation, you can send the results to a review set for further investigation or export it for review by people outside of the investigation team.

Note

For organizations that have EU General Data Protection Regulation (GDPR) requirements to protect and enable individuals' privacy rights inside the European Union (EU), you can also manage investigations in response to Data Subject Requests (DSRs) submitted by a person in your organization. The User Data Search case tool is retired, and its functionality is merged with eDiscovery. You can now use search to find content to support DSRs in all locations supported by eDiscovery searches.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Search query tips for eDiscovery cases

Use the following tips when creating and running searches in eDiscovery.

- The time zone for all searches is Coordinated Universal Time (UTC). You can't change the time zone for your organization. Time zone display settings in the search view only apply to values in the *Data* column and don't affect time stamps on collected items.
- Keyword searches are **always case-insensitive**, with no per-query or per-term opt-out. For example, **cat** and **CAT** return the same results, and `subject:"Apple"` matches both **Apple** and **apple**. This rule applies to keyword text and `property:value` syntax across all eDiscovery search surfaces (search, query-based holds, and review set search). The only case-sensitive tokens in KeyQL are the Boolean operators themselves - **AND**, **OR**, **NOT**, and **NEAR** must be uppercase to be parsed as operators.

    Note

    **Case-sensitive matching isn't supported in eDiscovery search.** If your scenario requires distinguishing **Apple** (the company) from **apple** (the fruit), or differentiating identifiers like **ID** from **id**, use the following pattern: (1) run a deliberately broad case-insensitive collection, (2) add the items to a review set, (3) export the review set or its text and metadata, and (4) apply case-sensitive filtering post-export by using external tooling (for example, PowerShell `Select-String -CaseSensitive`, regular expressions, or a third-party review platform).
- **An empty keyword condition returns all content in the selected data sources, not no content.** If you don't enter any keywords or conditions, the search returns every item in every selected mailbox, site, and group across the entire date range.

    Important

    For broad-scope cases, an empty keyword condition can return millions of items, exceed result limits, and significantly delay the search. To preserve a defined search scope, enter at least one keyword or condition before you run the search. To intentionally collect all content in a scope (for example, for a custodial preservation snapshot), confirm the scope size by running **Generate statistics** first.
- The Boolean operators **AND**, **OR**, **NOT**, and **NEAR** must be uppercase.

    Important

    Use these operators in the *KeyQL* condition field. The search doesn't support these operators in the *Keyword* condition field. The search treats these operators as literal keywords.
- Using quotes stops wild cards and any operations inside the quotes.
- A space between two keywords or two `property:value` expressions is the same as using **OR**. For example, `from:"Sara Davis" subject:reorganization` returns all messages sent by Sara Davis or messages that contain the word reorganization in the subject line. However, using a mix of spaces and **OR** conditionals in a single query might lead to unexpected results. Use either spaces or **OR** in a single query.
- Use syntax that matches the `property:value` format. Values aren't case-sensitive, and they can't have a space after the operator. If there's a space, your intended value is a full-text search. For example `to: pilarp` searches for "pilarp" as a keyword, rather than for messages sent to pilarp.
- When searching a recipient property, such as To, From, Cc, or Recipients, you can use an SMTP address, alias, or display name to denote a recipient. For example, you can use pilarp@contoso.com, pilarp, or "Pilar Pinilla."
- You can use only prefix searches; for example, **cat\*** or **set\***. Suffix searches (**\*cat**), infix searches (**c\*t**), and substring searches (**\*cat\***) aren't supported.
- When searching a property, use double quotation marks (" ") if the search value consists of multiple words. For example, `subject:budget Q1` returns messages that contain **budget** in the subject line and that contain **Q1** anywhere in the message or in any of the message properties. Using `subject:"budget Q1"` returns all messages that contain **budget Q1** anywhere in the subject line.
- To exclude content marked with a certain property value from your search results, place a minus sign (-) before the name of the property. For example, `-from:"Sara Davis"` excludes any messages sent by Sara Davis.
- You can export items based on message type. For example, to export Skype conversations and chats in Microsoft Teams, use the syntax `kind:im`. To return only email messages, use `kind:email`. To return chats, meetings, and calls in Microsoft Teams, use `kind:microsoftteams`.
- When searching sites, you have to add the trailing `/` to the end of the URL when using the `path` property to return only items in a specified site. If you don't include the trailing `/`, items from a site with a similar path name are also returned. For example, if you use `path:sites/HelloWorld` then items from sites named `sites/HelloWorld_East` or `sites/HelloWorld_West` are also returned. To return items only from the HelloWorld site, you have to use `path:sites/HelloWorld/`.
- You can define the **Query language-country/region** in your search query before collecting content. Query language that is Chinese, Japanese, or Korean might require special treatment such as breaking a phrase or sentence into individual words or characters for more accurate test results. For more information, see [Double-byte character language support in eDiscovery](edisc-cjk-support#search-for-items-containing-cjk-characters).
- When searching the **Sent** folders for emails, the search doesn't support using the SMTP address for the sender. Items in the **Sent** folder contain only display names.
- When searching data sources for content, optical character recognition (OCR) capabilities use [tenant-level OCR scanning](ocr-learn-about). Once data is collected in an eDiscovery review set, the OCR capability uses [eDiscovery OCR scanning](edisc-settings-search-analytics#optical-character-recognition-ocr).
- The search-time *Include partially indexed items* choice affects statistics and preview only. Whether partially indexed items appear in a later export is set independently at export time. If you need them in the export, select the partial-index option on the export dialog as well. For details, see [Search-time and export-time settings are independent](edisc-ref-partially-indexed-items#search-time-and-export-time-settings-are-independent).

## Create a search query

Tip

Do you prefer an interactive configuration guide experience? Check out the [Design a search](https://mslearn.cloudguides.com/guides/Design%20a%20search%20with%20Microsoft%20Purview%20eDiscovery) guide.

When you create a new case, you're automatically directed to the **Searches** tab in the case and you're ready to create a search for the case. You can also create a new search in the Content Search case in your organization. Searches help you find the items you want to collect for the case.

SharePoint Embedded container support in eDiscovery (preview) includes container discovery and application filtering when you add a user as a data source. You can also add a supported container directly by using its URL.

1. Select **Create a search** in a case or Content Search case. If this new case doesn't have any previous searches, you can also select **Create a search** in the main pane under **Start searching for relevant data**.
2. On the **Enter details to get started** page, complete the following fields:

    - **Search name**: give the search a name (required). The search name must be unique in your organization.
    - **Search description**: Add an optional description to help others understand this search.
3. Select **Create** to create the new search and start your queries to find relevant data for the case.
4. On the **Query** tab, add data sources for the search. For complete guidance and limitations, see [Data sources in eDiscovery](edisc-data-sources#sharepoint-embedded-application-content).

    For SharePoint Embedded container support in eDiscovery (preview), select a user to discover relevant supported user-owned and tenant-owned containers, or enter a known supported container URL as a site location.
5. Select **Manage** to review the mailbox and site locations associated with the selected sources. Otherwise, select **Save and close**.

    If you added a user as a data source, use **Filter by app** as needed, and then select or clear the supported SharePoint Embedded containers relevant to the investigation.
6. Review your selections and confirm the included resources for each data source. Select **Save**. You scoped the data sources that your search queries examine.
7. In the **Data sources** section, select the ellipse menu for any data source for management options for the data source.

    For management options, select from the following options:

    - **Manage data source**: Manage data sources for the selected user or site.
    - **Disable mailboxes**: Disable mailboxes for the selected user or site. Select this option again to enable the mailbox for the user or site.
    - **Disable sites**: Disable the site for the selected user or site. Select this option again to enable the site for the user or site.
    - **Frequent collaborators**: Select associated mailboxes and sites for users that frequently collaborate with the selected user.
    - **Manager**: Select associated mailboxes and sites of the user's manager.
    - **Direct reports**: Select associated mailboxes and sites of the user's direct reports.
    - **Groups the user owns**: Select associated mailboxes and sites of groups the user is an owner of.
    - **Groups the user is in**: Select associated mailboxes and sites of groups the user is a member of.

    For group sources, select from the following options:

    - **Members**: Select associated mailboxes and sites of people who are members of the group.
8. Use the **Data sources** command bar controls to add, update, sync, and search for other data sources for the search as needed.

    - **Search and add**: Select the + icon to add data sources.
    - **Manage**: Select the pencil icon to manage assigned data sources.
    - **Sync**: Select the sync icon to synchronize data sources and update the data sources with the most recent data sources in your organization.
    - **Search**: Select the search icon to search the data sources currently included in the search query.
9. To define the parameters of your search query, choose from the following options on the **Query** tab:

    - **Condition builder**: The [condition builder](edisc-condition-builder) option in search provides an easy-to-user search experience when you build search queries in eDiscovery. Use keywords or custom conditions to focus the scope of your search queries. Additionally, you can use the [Keyword Query Language (KeyQL) query condition option](edisc-keyword-query-language) in search that provides guidance and lets you quickly paste long, complex queries directly into the editor. It also helps you build search queries from scratch and identifies potential errors and displays hints about how to resolve issues.

        You can also quickly build KeyQL queries for your search using Microsoft Security Copilot. For guidance, see Create a KeyQL search query with Microsoft Copilot (preview).
10. Select **Run query**. If you want to save the query parameters you defined and run the query later, select **Save as draft**.

## Create a KeyQL search query with Microsoft Copilot (preview)

The Natural Language Query (preview) KeyQL builder option in search lets you use natural language and [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot) to quickly generate a Keyword Query Language (KeyQL) statement. Use the builder to construct complex queries with extra functionality, including AND, OR, and grouping of conditions, all while using natural language prompts.

This feature helps you build queries more easily by using predefined prompts for example scenarios. It also lets you refine and enhance custom prompts for more accurate search queries. You can also choose to use prompt suggestions as a starting point to create and refine KeyQL queries for common or custom search scenarios.

To create a search query with Copilot, complete the following steps:

1. After you select data sources for your query, select **Draft a query with Copilot**.
2. In the **Natural language prompt**pane, choose one of the following options:
    - Enter your search query question. You can include user, data source, and other content details as applicable.
    - Select **View prompts**to select one of the following prompt suggestions:
        - *Find all emails containing the words budget and finance and have attachments*
        - *Search all chats in the month of January 2020 that contain the word 'financial year'*
        - *Search for files of type .docx that contain the words confidential and budget*
3. Review the natural language prompt. To refine the prompt with Copilot, select **Refine**.
4. When the prompt is finalized, select **Generate KeyQL**.
5. Review the KeyQL query in the **Keyword Query Language (KeyQL) result** pane. If you need to refine the KeyQL query results, you can update the prompt in the **Natural language prompt** pane and select **Generate KeyQL** again. 1. When the KeyQL results are finalized, select **Copy KeyQL**.
6. Paste the KeyQL results in the query field on the **Keyword query language (KeyQL)** tab. You can close **Draft a query with Copilot**.
7. Select **Run query**. If you want to save the query parameters you defined and run the query later, select **Save as draft**.

## Run a search query

After you create a search query manually or by using Security Copilot, run the query to generate search results.

To run a search query, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case. On the **Searches** tab, select a saved search.
4. Select **Run query**.
5. After you select **Run query**, you see the **Choose search results** flyout pane. Choose the view you want to generate for the query and its settings. You can choose either the **Statistics** or **Sample** view:

    - **Statistics**: This view generates a summary of collected data estimates arranged by top indicators. Choose one or more of the following options:
    - **Include categories**: Refine your view to include people, sensitive information types, item types, and errors.
    - **Include query keywords report**: Assess keyword relevance for different parts of your search query.
    - **Investigate partially indexed items**: Partially indexed items typically account for approximately 1% of content in data sources by count. Selecting this option (and only this option) generates summary information (item count and location) about partially indexed items included in the selected data sources for the search. No partially indexed items are reindexed or processed. For more information about how to calculate the ratio of partially indexed items in your organization, see [Assess partially indexed items in your organization](edisc-ref-partially-indexed-items#assess-partially-indexed-items-in-your-organization). To further process partially indexed items in scoped data sources, consider the following advanced indexing options:

        - **Exclude partially indexed items in locations without search hits**: Choosing this option reduces the scope of partially indexed items (or advanced indexing if that option is selected) by limiting the inclusion of partially indexed items to only the data sources that include items relevant to your search. This exclusion removes partially indexed items from data sources that don't include any items relevant to your search.

            For example, you select multiple mailboxes, SharePoint sites, and OneDrive sites as data sources for your search. When the search runs, only a few of the mailboxes and sites have indexed items relevant to the search conditions. The rest of the mailboxes and sites don't contain any indexed items relevant to your search conditions. If you select this option, the partially indexed items in the mailboxes and sites that contain indexed items relevant to the search are included in the search statistics results. The partially indexed items in the mailboxes and sites that don't contain any indexed items relevant to the search are ignored and not reported in the search statistics results.
        - **Perform advanced indexing on partially indexed items**: The scope of where advanced indexing runs depends on if you select the **Exclude partially indexed items in locations without search hits** option. The advanced indexing process runs a statistical sample of partially indexed items in scope and determines if these items match the query or not:

            - Selected *with* the **Exclude partially indexed items in locations without search hits** option: This setting applies to partially indexed items only to data sources with fully indexed items matching the search query. These items are sampled, indexed, and the items matching the search query are displayed in search statistics (as applicable).
            - Selected *without* the **Exclude partially indexed items in locations without search hits** option: This setting applies to all partially indexed items in all data sources included in the search. All items are sampled, indexed, and the items matching the search query are displayed in search statistics (as applicable).

            Important

            This feature isn't available for [limited format](edisc-cases-manage#limited-format-cases) cases.
    - **Sample**: This view generates a representative selection of the full search results. Define the parameters for the following options:

        - **Select the number of sample items to generate per location**: Choose either *1*, *10*, or *100*.
        - **Select the number of locations to get samples from**: Choose *10*, *100*, *1000*, or *10000*.
6. **Tenant-wide source configuration** options in eDiscovery let you include additional data sources during organization-wide searches. Adding more data sources might cause searches to take longer than usual.

    Configure the organization-wide source "All people and groups" to include one or more user or content types:

    - **"All people and groups" should include unlicensed and on-premises users**
    - **"All people and groups" should include guest users**
    - **"All people and groups" should include shared Teams channels**
    - **"All people and groups" should include departed users**

    Important

    For large organizations, tenant-wide searches across all Exchange mailboxes and SharePoint sites are long-running processes. Service throttling can affect the number of mailboxes and sites to search. Before running these tenant-wide searches, review scale limits and throughput guidance in [Limits in eDiscovery](edisc-ref-limits#search-limits) and plan to conduct searches in batches as applicable. To improve performance and operability, break the search into scoped runs using [compliance boundaries](edisc-compliance-boundaries) (for example, by region, business unit, or department) so each search targets a subset of mailboxes and sites.
7. Select **Run query** to immediately run the query.

Depending on the query view options you selected, you're automatically directed to the **Statistics** or **Sample** tab. The search query assessment starts and the time remaining to process the query is calculated. For more information about evaluating and fine-tuning your search results, see [Review and evaluate search results](edisc-search-results).

## Create a new search from an existing search

In some scenarios, it might be helpful to create a new search based on an existing search. This approach maintains the original data sources and search while making modifications to get new search statistics without changing the original search. When you create a duplicate search, you keep all the data sources and the search from the original search in the new search. This approach preserves the integrity of the original search and enables you to explore new insights.

To create a new search from an existing search, complete the following steps:

1. Select a case. On the **Searches** tab, open a search.
2. Select **Duplicate**.
3. A new search is automatically created in the same case.

The new search name includes the source search title with *Copy of* prefixed to the title and the timestamp appended. For example, if the source search title is *Search for budget emails*, the new search title is *Copy of Search for budget emails + the timestamp*. To edit the new search title, select the edit control next to the title text.

## Create a new search from an existing hold

In some scenarios, it might be helpful to create a new search based on an existing hold. This approach allows you to use the original data sources and search used for the hold to run a new search. When you create a search from an existing hold, you keep all the data sources and the search from the hold in the new search.

Note

To create a search from an existing hold, you must be assigned the *Compliance Search* role. For information about adding users to a role group, see [Assign eDiscovery permissions](edisc-permissions).

To create a new search from an existing hold, complete the following steps:

1. Select a case. On the **Hold policies** tab, select and open a hold policy.
2. Select **Create search**.
3. A new search is automatically created and you're automatically redirected to the new search.

The new search name includes the source hold policy name with *Copy of* prefixed to the title and timestamp. For example, if the source hold policy title is *Hold to preserve Contoso project*, the new search title is *Copy of Hold to preserve Contoso project + the timestamp*. To edit the new search title, select the edit control next to the title text.

## Delete a search

To reduce the number of previous searches associated with a case, delete specific searches in eDiscovery. If the search has associated exports and review sets, the history of these exports and review sets remains available in the [Process Manager](edisc-process-managers) and [audit logs](audit-log-activities#ediscovery-activities).

To delete an existing search in a case, complete the following steps:

1. Select a case and select the search to delete.
2. Select the ellipsis (...) in the upper right of the search page, and then select **Delete search**.
3. Select **Yes** on the **Delete search** dialog to delete the search from the case.

Note

You can't delete a search while [processes](edisc-process-managers) are in progress. Wait for all processes to finish before deleting a search.