---
layout: Conceptual
title: Search, review, and refine results in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to search, review, and refine results in Data Security Investigations, including audit search for activity-based content identification.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 27a8133b-690b-f6e3-cdca-8160d98f3e1f
document_version_independent_id: 27a8133b-690b-f6e3-cdca-8160d98f3e1f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 416c99e2-7149-beec-df07-f90787b30ddc
---

# Search, review, and refine results in Data Security Investigations | Microsoft Learn

Use search in Data Security Investigations to find Microsoft 365 content such as email, documents, and instant messaging conversations in your organization that are relevant to a security incident. Use search to find content in these cloud-based Microsoft 365 data sources:

| Data source | Content type searched | Risky content examples |
| --- | --- | --- |
| Endpoint Data Loss Prevention (DLP) | Files captured by endpoint DLP evidence collection | Files copied to USB, printed, uploaded to cloud, or accessed by unauthorized apps on onboarded devices. |
| Exchange Online | Emails and attachments in user mailboxes | Credentials or secrets sent in email, sensitive files shared externally. |
| Microsoft Copilot | AI prompts and responses | Sensitive data in Copilot or AI prompts. |
| Microsoft Teams | Chat messages (1:1 and group chats) and channel posts | Secrets included in chats, confidential information in Teams conversations. |
| OneDrive | User files | User files with secure access keys, export of databases, and more. |
| SharePoint | Documents and files in sites | Documents containing passwords, customer data, or confidential plans. |

Create and run different searches that are associated with an investigation. Use conditions such as keywords, file types, incidents, and more to build search queries that return search results with the data most relevant to the investigation. You can also:

- View search statistics that help you refine a search query to narrow results.
- Preview the search results to quickly verify whether you're finding the relevant data.
- Revise a query and rerun the search.
- Use audit search to identify content based on user activities recorded in the unified audit log.
- Use endpoint DLP evidence collection to query data captured by endpoint DLP policies on onboarded devices.

Consider the activities that triggered the investigation. For example, reported password sharing or leak, a suspicious file, work with an external development team, or an alert about data exfiltration or specific individuals or teams who may be involved. Use this information to help develop your initial search query. For example, if an administrator reported that passwords might be stored in plain text in SharePoint, start by searching for known password keywords or file names across SharePoint and OneDrive, or specific SharePoint sites managed by engineering teams.

When you're satisfied with the results of a search and ready to review and analyze the results, add them to an [investigation scope](data-security-investigations-scope) in the investigation. Adding copies of the original data to an investigation scope also facilitates the [AI analysis](data-security-investigations-ai) and review process by providing you with advanced categorization, examination, and vector search tools.

## Access search tools

Select **Summary** from the navigation options at the top of any page within a specific investigation to access search tools on the Identify page.

The Identify page is organized into the following tabs:

- **Search**: Create search queries to identify content relevant to the investigation. The **Search**tab includes three options:
    - **Query builder**: Search for content based on keywords, file types, dates, and other conditions.
    - **Audit**: Use audit search to identify content based on user activities recorded in the unified audit log.
    - **Endpoint DLP**: Use endpoint DLP evidence collection to query data captured by endpoint DLP policies on onboarded devices.
- **Review estimates**: Review scope and sample statistics for search results to refine your query before adding results to an investigation scope.

You can refine search query data sources and conditions at any time during the investigation and add the results to an investigation scope.

## Data sources

In Microsoft 365, data is stored across three platforms: Exchange, Teams, and SharePoint. These platforms serve as the backbone for organizing and managing data within Microsoft 365 applications.

Important

If you set a site status to *Locked* and set the site to *NoAccess*, Data Security Investigations doesn't return search results. For more information about managing site lock statuses, see [Lock and unlock sites](/en-us/sharepoint/manage-lock-status). In addition, if you restrict a document in the content store, the Data Security Investigations investigator must be a site admin, site owner, or the owner or last modifier of the restricted document to access it in Data Security Investigations. For more information about restricted content, see [Data Loss Prevention policy reference](dlp-policy-reference#actions).

Most Microsoft 365 apps store data in one or more of the following containers:

- **Users**: Data associated with individual users, such as their mail, 1:1 Teams messages, and OneDrive files.
- **Groups**: Data owned by the organization or a group of users within an organization. These groups are often referred to as Unified Groups or Teams.

In Data Security Investigations, the concept of *data sources* streamlines the process of identifying and managing data across Microsoft 365 platforms. Analysts select a user or group and scope searches to those data sources. Analysts can refine the scope by selecting or excluding specific locations.

Analysts can also use organization-wide sources to perform search across your organization. Organization-wide sources include:

- **All people and groups**: Includes all users and all groups in your organization.
- **All public folders**: Includes all content in Exchange [public folders](/en-us/exchange/collaboration-exo/public-folders/public-folders) mailboxes.

Important

If your organization has configured [compliance boundaries](edisc-compliance-boundaries) using search permissions filters, Data Security Investigations searches respect those boundaries. Investigators whose accounts are scoped by a compliance boundary only see search results for content locations within their permitted boundary. For more information about how compliance boundaries and search permissions filters work, see [Set up compliance boundaries in eDiscovery](edisc-compliance-boundaries) and [Configure search permissions filtering in eDiscovery](edisc-search-permission-filtering).

## Query builder

The **Query builder** option on the **Search** tab provides a visual filtering experience when you build search queries in Data Security Investigations. Since you'll use AI analysis tools to quickly identify applicable data in items returned by your search, one strategy is to broaden your search scope to include more sources of data. This approach helps reduce the chance of excluding any relevant content for review.

Use the query builder to construct complex queries with additional functionality, including AND, OR, and grouping of conditions. These features in the query builder help you build queries more effectively, provide a visual interface for grouping subqueries, and provide additional space for complex keyword queries to be constructed and reviewed.

### Use the query builder

To create a query and custom filtering for your search, use the following controls:

- **AND/OR**: These conditional logical operators help you choose the query condition that applies to specific filters and filter subgroups. Use these operators to include multiple filters or subgroups connected to a single filter in your query.
- **Select a filter**: Choose filters for the specific data sources and location content you select for the collection.
- **Add filter**: Add multiple filters to your query. This option becomes available after you define at least one query filter.
- **Select an operator**: Depending on the selected filter, choose from compatible operators. For example, if you select the *Date* filter, you can choose from *Before*, *After*, and *Between*. If you select the *Size (in bytes)* filter, you can choose from *Greater than*, *Greater or equal*, *Less than*, *Less or equal*, *Between*, and *Equal*.
- **Value**: Depending on the selected filter, enter compatible values. Some filters support multiple values, while others support a single specific value. For example, if you select the *Date* filter, enter date values. If you select the *Size (in bytes)* filter, enter a value for bytes.
- **Add subgroup**: After you define a filter, add a subgroup to refine the results returned by the filter. You can also add a subgroup to a subgroup for multilayered query refinement.
- **Remove a filter condition**: To remove an individual filter or subgroup, select the remove icon to the right of each filter line or subgroup.
- **Clear all**: To clear the entire query of all filters and subgroups, select **Clear all**.

### Scenario example

A Data Security Investigations analyst needs to create a query for any item that includes the keyword *confidential* used between January 1, 2025, and March 16, 2025\*. For this example, the analyst creates the following query using the query builder:

1. For the first filter, the analyst selects *Keyword*, then selects the *Equal* operator, then enters *confidential* in the **Value** control.
2. Next, the analyst selects **Add subgroup** and the **AND** operator, then the **Add filter**.
3. The analyst selects the *Date* filter, the *Between* operator, and start and ending dates for the *Value*.
4. The analyst selects **Save** to save the query, then **Review scope** to run the search query.

![Query builder example.](media/dsi-query-builder-example.png)

### Example search queries

You can use Keyword Query Language (KeyQL) syntax in the query builder to create targeted search queries for common investigation scenarios. Use these examples as starting points and adjust the date ranges, paths, and keywords to match your investigation.

Tip

Since you can use [AI analysis](data-security-investigations-ai) tools to quickly identify applicable data in items returned by your search, consider broadening your search scope to include more sources of data. This helps reduce the chance of excluding any relevant content for review.

#### Exchange Online

**Search for emails only**

To search mailboxes for email messages only and exclude other items such as calendar invites, tasks, and to-do items, use the `Kind` property. This example returns emails sent after a specified date.

*Data sources*: All people and groups

```text
(Kind=email) AND (Date>2025-01-01)
```

#### Microsoft Teams

**Search all Teams content**

To search for all Teams content, including chat messages, channel posts, meeting entries, and calls, use the `Kind=microsoftTeams` filter.

*Data sources*: All people and groups

```text
(Kind=microsoftTeams) AND (Date>2025-01-01)
```

**Search chat messages only**

To narrow your search to Teams chat messages only and exclude meetings and channel posts, use `Kind=IM`.

*Data sources*: All people and groups

```text
(Kind=IM)
```

#### SharePoint Online

**Search a specific SharePoint site**

To search all content in a specific SharePoint site, use the `Path` property.

```text
(Path="https://contoso.sharepoint.com/sites/ProjectAlpha")
```

**Search a site and exclude system-generated content**

To search a SharePoint site for documents created after a specified date while excluding system-generated content, use the `Author` property with the NOT (`-`) operator.

```text
((Date>2025-01-01) AND (Path="https://contoso.sharepoint.com/sites/EngineeringTeam/Shared Documents") AND ((-Author="System Account") AND (-Author="SHAREPOINT\System")))
```

**Search multiple sites for specific file names**

To search across multiple SharePoint sites for files with names that begin with a specific term, use the `OR` operator to combine paths and the `filename` property to filter by name.

```text
(((Path="https://contoso.sharepoint.com/sites/ProjectAlpha") OR (Path="https://contoso.sharepoint.com/sites/ProjectBeta")) AND (filename="proposal*"))
```

**Search for specific files**

To search for known files by their full path, use the `Identifier` property and the `OR` operator to combine multiple file paths.

```text
((Identifier="https://contoso.sharepoint.com/sites/EngineeringTeam/Docs/SecurityReport.docx") OR (Identifier="https://contoso.sharepoint.com/sites/EngineeringTeam/Docs/IncidentLog.xlsx"))
```

#### Microsoft Copilot

**Search Copilot prompts and responses**

Copilot interactions are stored in users' Exchange Online mailboxes. To search for Copilot prompts and responses after a specified date, use the `ItemClass` property with the Copilot item class value.

*Data sources*: All people and groups

```text
(ItemClass=IPM.SkypeTeams.Message.Copilot.*) AND (Date>2025-01-01)
```

For more information about Copilot item classes and searching for Copilot data, see [Search for and delete Copilot and other AI data in eDiscovery](edisc-search-copilot-data).

## Audit search

Use audit search in Data Security Investigations to identify and collect content based on user activities recorded in the [Microsoft Purview unified audit log](audit-log-activities). While the query builder searches Microsoft 365 content directly, audit search queries the unified audit log for specific user activities, such as accessing, copying, or downloading files, and pulls the associated content into your investigation. You can also filter audit search results by keywords, specific users, and file or site locations.

### Example scenario: Departing employee data exfiltration

A security team receives an alert that a departing employee might have exfiltrated sensitive files before their last day. Using audit search, the investigator queries for **Downloaded file** and **Sent email** activities scoped to that user over their final two weeks. Data Security Investigations pulls the associated content directly into the investigation scope - no manual file hunting required - so the team can quickly assess what data was accessed and whether anything was shared externally.

### Get started with Audit search

When you create an audit search, Data Security Investigations queries the unified audit log for the specified activities and adds the associated content directly to your [investigation scope](data-security-investigations-scope). Audit search uses the [permissions and role-based access control requirements](audit-get-started#step-2-assign-permissions-to-search-the-audit-log) from the unified audit log.

Audit search requires that your organization is configured for audit log and audit search. For more information about audit log requirements, see [Search the audit log](audit-search#before-you-search-the-audit-log).

### Supported activities

Audit search supports a curated set of content-associated activities from the unified audit log. You can only audit search activities that are associated with identifiable content items, such as files and emails. Audit search doesn't support activities that aren't associated with specific content, such as signing in to a solution.

The following activities are supported for audit search:

| Activity | Description |
| --- | --- |
| Accessed file | A user accessed a file in SharePoint or OneDrive. |
| Copied file | A user copied a file in SharePoint or OneDrive. |
| Deleted file | A user deleted a file from SharePoint or OneDrive. |
| Downloaded file | A user downloaded a file from SharePoint or OneDrive. |
| Moved file | A user moved a file between folders in SharePoint or OneDrive. |
| Renamed file | A user renamed a file in SharePoint or OneDrive. |
| Changed sensitivity label applied to file | A user changed the sensitivity label on a file. |
| Removed sensitivity label from file | A user removed a sensitivity label from a file. |
| Uploaded file | A user uploaded a file to SharePoint or OneDrive. |
| Sent email | A user sent an email message from Exchange Online. |

### Create an audit search

To create an audit search and add the associated content to your investigation scope, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and open an investigation.
2. Select **Summary** from the navigation options at the top of the page.
3. On the **Search** tab, select **Audit**.
4. Configure the search parameters:

    - **Date and time range (UTC)** (required): Specify a **Start** and **End** date and hour for the activity search.
    - **Activities - friendly names**: Select one or more supported activities by their display name from the activities list.
    - **Activities - operation names**: Select one or more supported activities by their operation name.
    - **Users**: Select users to search for activities performed by specific users.
    - **ObjectID (file, folder, or site)**: Enter a file, folder, or site path to narrow the search to activities associated with a specific location.
    - **Keyword search**: Enter keywords to search for in audit log entries.
5. Select **Search** to run the audit query. Data Security Investigations queries the unified audit log and displays the results in the results section at the bottom of the Audit page. Review the results to verify the query returns the expected data. To discard the search without adding results, select **Cancel**.
6. Select **Add to scope** to add the content associated with the search results to your investigation scope.

After you add to scope, Data Security Investigations starts processing the results. You can monitor the progress of audit search jobs on the [Activities](data-security-investigations-activity-history) page for the investigation. Previously submitted audit searches are also listed in the audit search history at the bottom of the Audit page.

Note

The **Review estimates** and **Save** buttons on the command bar are visible but unavailable when the **Audit** option is selected. These options are only available for the query builder. To preview audit search results before adding them to an investigation scope use the [Audit solution](audit-search) to test your queries separately.

### Audit search jobs and query chunking

Audit search uses *query chunking* to process results. This method creates multiple jobs to ingest data into the investigation scope. When you submit an audit search, the following jobs appear on the [Activities](data-security-investigations-activity-history) page:

- **One audit search job**: The primary job that queries the unified audit log for the specified activities.
- **Multiple add-to-scope jobs**: Additional jobs that process and add the associated content to your investigation scope. The number of add-to-scope jobs depends on the volume of data returned by the search.

After all jobs complete, the system automatically vectorizes the data for AI analysis. You can continue investigating the data after [Add to scope](data-security-investigations-scope#automatic-vectorization) completes.

Tip

After submitting an audit search, you see an *Audit Search* activity and multiple *Add to scope* activities on the **Activities** page. This result indicates that query chunking is processing the results.

### Audit search and the unified audit log

Audit searches you create in Data Security Investigations also appear in the search history of the [Microsoft Purview unified audit log](audit-solutions-overview). This behavior is expected because Data Security Investigations queries the unified audit log directly as the data source for audit searches.

Important

Data Security Investigations supports up to 10 concurrent audit searches per user. Audit searches that return more than approximately 3,000 items might not return complete results. The exact limit depends on the file names and paths of the returned items. For more information about limits, see [Limits in Data Security Investigations](data-security-investigations-ref-limits).

## Endpoint DLP evidence collection

You can use endpoint DLP evidence collection in Data Security Investigations to query data captured by [endpoint data loss prevention](endpoint-dlp-learn-about) policies on onboarded devices and add the associated content to your investigation scope. Instead of triaging individual endpoint DLP alerts one by one, investigators can aggregate endpoint events and analyze them collectively using Data Security Investigations AI tools.

Endpoint DLP evidence collection queries the data stored by the [evidence collection for file activities on devices](dlp-copy-matched-items-learn) feature. This data includes files that matched endpoint DLP policies when users attempted activities such as copying to USB, printing, uploading to cloud services, or accessing files with unauthorized apps.

### Prerequisites

Before you can use endpoint DLP evidence collection in Data Security Investigations, ensure the following requirements are met:

- Devices are [onboarded to Microsoft Purview](device-onboarding-overview).
- An [endpoint DLP policy](endpoint-dlp-learn-about) is configured and active in your organization.
- The endpoint DLP policy has [evidence collection for file activities on devices](dlp-copy-matched-items-get-started) enabled with the **Collect original file as evidence for all selected file activities on endpoint** option selected.
- [Microsoft-managed storage](dlp-copy-matched-items-get-started#enable-and-configure-evidence-collection-on-a-storage-account-managed-by-microsoft) is configured for evidence collection.

Note

In addition to the standard [Data Security Investigations permissions](data-security-investigations-permissions), you must also be a member of the Insider Risk Management role group and View-Only DLP Compliance Management role to query from endpoint evidence collection.

### Key considerations

Keep the following considerations in mind when using endpoint DLP evidence collection in Data Security Investigations:

- **Data availability depends on evidence collection retention**: If endpoint DLP evidence collection data is no longer available in the evidence store due to retention expiration, Data Security Investigations can't query it. The same query run at different times might yield different results based on the current state of the evidence store.
- **Data isn't immutable before ingestion**: Endpoint DLP evidence collection data can change in the evidence store before you add it to your investigation scope. After you add items to scope, the data is static within the investigation.
- **File content only**: Data Security Investigations ingests the file content associated with endpoint DLP events. Some contextual metadata from endpoint DLP, such as per-event device details, isn't preserved in the investigation scope. For detailed per-event context, use the [DLP Alerts dashboard](dlp-alerts-dashboard-get-started) or [Activity explorer](data-classification-activity-explorer).
- **Data availability latency**: Evidence collection data might not appear immediately after a policy match. Availability depends on device connectivity and upload timing.
- **Endpoint DLP only**: This feature queries data from endpoint DLP policies only. Browser DLP, network DLP, and non-endpoint DLP scenarios aren't supported for this search option.

### Create an endpoint DLP search

To query endpoint DLP evidence collection data and add the associated content to your investigation scope, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and open an investigation.
2. Select **Summary** from the navigation options at the top of the page.
3. On the **Search** tab, select **Endpoint DLP**.
4. Configure the search parameters:

    - **Date range** (required): Specify a start and end date for the endpoint DLP events to query.
    - **Users** (optional): Select one or more users to narrow the search to endpoint DLP events for specific users. If you don't select any users, the search returns results for all users in your organization.
5. Select **Search** to run the query. Data Security Investigations queries the endpoint DLP evidence collection data and displays the results.
6. Review the pre-ingestion estimate, which includes a summary of matched alerts, users, actions, and policies.
7. Select **Add to scope** to add the content associated with the search results to your investigation scope.

After you add items to scope, Data Security Investigations starts processing the results. You can monitor the progress on the [Activities](data-security-investigations-activity-history) page for the investigation.

Important

Endpoint DLP evidence collection searches that return more than approximately 3,000 items might not return complete results. To ensure complete coverage, narrow your search by using a shorter date range or by selecting specific users. For more information about limits, see [Limits in Data Security Investigations](data-security-investigations-ref-limits).

### Work with large audit search results

When an investigation involves a large volume of user activity, audit searches might exceed the approximately 3,000-item limit. To work with large result sets, use the [Audit solution](audit-search) to analyze the full scope of results. Then, split the data into smaller time-based slices that fit within the Data Security Investigations audit search limit.

#### Analyze audit results outside Data Security Investigations

The [Audit solution](audit-search) doesn't have the same per-search item limit as Data Security Investigations audit search. Use the Audit solution to run the full query first and determine the total volume of results before splitting it into smaller searches.

To analyze audit results, complete the following steps:

1. Go to [Audit](https://purview.microsoft.com/audit) in the Microsoft Purview portal.
2. Configure the same search parameters you plan to use in Data Security Investigations:

    - **Date and time range**: Specify the full date and time range for the investigation.
    - **Activities**: Select the same activities you need for the investigation.
    - **Users**: Specify the same users you plan to search.
3. Run the search and export the results to a CSV file.

#### Identify time slices for audit searches

After you export the audit results, use the CSV data to identify time periods that contain fewer than approximately 3,000 items each. These time periods become the individual audit searches you run in Data Security Investigations.

To identify time slices, complete the following steps:

1. Open the exported CSV file in Microsoft Excel.
2. Add helper columns to break the `CreationDate` timestamp into components for grouping:

    | Column name | Formula | Description |
    | --- | --- | --- |
    | Date | `=LEFT(B2,10)` | Extracts the date portion (YYYY-MM-DD). |
    | Hour | `=MID(B2,12,2)` | Extracts the hour (HH). |
    | Day-Hour | `=I2&" "&J2&":00"` | Combines date and hour for hourly grouping. |
    | Day-Hour-Minute | `=I2&" "&J2&":"&MID(B2,15,2)` | Combines date, hour, and minute for finer grouping. |

    Note

    Replace `B2` with the column reference for `CreationDate` in your export, and `I2`/`J2` with the column references for your Date and Hour helper columns. Adjust column references based on your export format.
3. Create a PivotTable to count records by user and time period:

    - Set **Rows** to the user column and the *Day-Hour* helper column.
    - Set **Values** to count of records.
    - Identify time groups that contain fewer than approximately 3,000 items.
4. For time groups that exceed approximately 3,000 items, apply finer grouping:

    - Break hourly groups into minute-level slices using the *Day-Hour-Minute* column.
    - Optionally, split by activity type if a single time period still exceeds the limit.

#### Run sliced audit searches in Data Security Investigations

After you identify the time slices, run separate audit searches in Data Security Investigations for each slice and add all results to the same investigation scope.

To run sliced audit searches, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and open an investigation.
2. Select **Summary** from the navigation options at the top of the page.
3. On the **Search** tab, select **Audit**.
4. Configure the search parameters for the first time slice:

    - **Date and time range (UTC)**: Enter the start and end times for the slice.
    - **Activities**: Select the same activities as the original query.
    - **Users**: Select the same users as the original query.
5. Select **Search** to run the audit query.
6. Select **Add to scope** to add the results to your investigation scope.
7. Repeat for each remaining time slice until all data is ingested into the investigation.

Tip

Data Security Investigations automatically deduplicates items across audit searches. If time slices overlap, duplicate items aren't added to the investigation scope more than once. You can also run up to 10 concurrent audit searches per user to speed up the ingestion process.

## Scope dashboard

The **Review estimates** tab displays statistics and metrics for the data results included in the search query. This view helps you determine if the search query results are ready for adding to the investigation scope or if you need to refine your query for broader or narrower results.

The search results for the **Scope** dashboard are included in the following sections:

- **Summary**: Shows the number of search hits, locations, data sources, and the total file size of partially indexed items.

    - **Total matches**: Displays the total search hit count and volume from all items matching the query criteria from locations searched.
    - **Locations**: Displays the fraction of locations with hits out of all locations searched. The numerator shows the locations with hits and denominator shows the number of locations searched. Locations with errors appear in red. To view full details on all the locations and associated hits and errors, select **Download report** to download the full .csv report.
    - **Data sources**: Displays the fraction of data sources with hits out of all data sources searched. The numerator shows the data sources with hits and denominator shows the number of data sources included in the search. This data source is consistent with the data source in the search design flow and should match the number of people or groups included in the search. A tenant-wide data source of *All people and all groups* counts as a single data source.
    - **Partially indexed items** or "Advanced indexed items hits": Displays the count and volume of partially and unindexed items returned as part of the search. The advanced indexed hit count comes from a statistic sample on the partially indexed items, actual hits might be more and you can confirm by using the *Add to a review set* and *Export search results* actions.
    - **Top data sources**: Displays the top five data sources that make up the most search hits matching your query. The names of these data sources (names of users, groups, or organization-wide locations) are listed with the hit count. These data sources should match what you selected in the data sources workflow when building the search query.
    - **Indexing status**: Breakdown of unindexed (including partially indexed) and fully indexed data items.
    - **Top location type**: Hit count by location type (mailbox versus site).

Select **Regenerate view** to rerun the query and to review the most current results. Select **Download report** to combine all **Scope** results into a single .csv file. When viewing the top 100 results for any trend area, select **Download report** for a .csv file of the top 100 results of the selected hit trend.

## Samples dashboard

Samples let you inspect a representative subset of individual items and details for each item returned for the search. The number of samples per location and the number of sample locations defined in the search determine the number of sample items and location representation in the sample items.

The search results for the **Samples** dashboard columns contain the following information for each item:

- **Subject/Title**: The subject or title of the items included in the sample.
- **Date**: The date the item was created or sent.
- **Sender/Author**: The sender or author of the item.

Select a sample item to view the [Source](data-security-investigations-scope-views#source-view) information for the item. If available for the item, this view displays a rich view of a selected item so that you can evaluate the relevancy of the item as it relates to the defined search data source and conditions.

Select **Download reports** to combine all **Sample** results into a single .csv file. Select **View settings** to view the settings applied to the sample view generation.