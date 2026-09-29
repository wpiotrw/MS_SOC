---
layout: Conceptual
title: Use AI analysis in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-ai-analysis
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use AI analysis in Microsoft Purview to categorize, search, and examine data for security risks and sensitive information in your investigations.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
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
document_id: e9a9abce-7e97-8439-b214-832b5ca1e3af
document_version_independent_id: e9a9abce-7e97-8439-b214-832b5ca1e3af
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-ai-analysis.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-ai-analysis
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-ai-analysis.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: fcc0741a-0cc6-e13d-8a8f-67b4bf5d84e9
---

# Use AI analysis in Data Security Investigations | Microsoft Learn

After [automatic vectorization](data-security-investigations-scope#automatic-vectorization) completes for your investigation scope, you're ready to review and use AI analytics tools for the data in the investigation. Generative AI processing conducts a deep content analysis of selected items and can uncover key security and sensitive data risks within impacted data.

To get started with AI analysis in an investigation, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis** on the navigation bar.

Tip

Consider increasing the default item display from 50 to 1,000 items for easier selection of multiple items to exclude from the investigation scope.

## Use categorization

### Categorization considerations

Keep the following considerations in mind when configuring categorization and reviewing the results:

- **Not all items may appear in results**: Categorization uses relevance scoring to prioritize content. Items that score below the relevance threshold for a category aren't included in the results for that category, even if the items exist in the investigation scope.
- **Results may change when categories are updated**: When you add new categories or change existing categories between Standard and Advanced processing, the system reprocesses those categories. Because relevance is evaluated per category, results may differ based on the categories you select.
- **Large documents may be more strongly represented**: Documents with extensive content may contribute more content segments to categorization results, which can affect the distribution of results across documents.
- **Use examination for comprehensive analysis**: If your investigation requires analysis of all items in scope rather than a prioritized subset, use examination tools to perform item-level analysis on selected data items.

### Configure categorization

When you first open the **Analysis** page, items aren't categorized. Configure categorization first because it's helpful to start your triage by grouping items by risk.

Categorization takes time to complete. The completion time depends on the data volume and consumes AI capacity (compute units). To get an initial understanding of incident severity, use AI to categorize impacted data and narrow the focus to high-risk assets. Data Security Investigations sorts data into default, custom, or AI-generated categories, including by subject matter and risk.

Note

Investigations auto-created by [proactive AI insights from Data Security Posture Management (DSPM)](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm) arrive pre-categorized with five fixed risk categories. You can run additional categorization with default, suggested, or custom categories on these investigations.

To categorize data items in the investigation scope, complete the following steps.

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can configure categorization.

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis**.
4. Select **Categorize**.
5. Select the **Standard** or **Advanced** categorization option.

    - **Standard**: AI groups your scope into the selected categories. This option can significantly reduce the time it takes to complete processing and the amount of Data Security Investigations Compute Units (compute unit) needed for categorization.
    - **Advanced**: AI further groups your scope into various topics within each category. This grouping takes additional time and compute units to process.

    Important

    Categorization prioritizes the most relevant content for each selected category rather than analyzing every item in the investigation scope. Results represent the highest-confidence content segments for each category. If your investigation requires comprehensive analysis of all items, use examination tools instead of or in addition to categorization. For more information, see [How categorization processes data](data-security-investigations-ai#how-categorization-processes-data).
6. In the **Categorize with AI** dialog, complete the following areas to customize your categories as applicable:

    - **Default categories**: Select one or more default categories.
    - **Suggested categories**: Select one or more AI suggested categories. Suggested categories are generated based on the most recent vector search. If searches aren't run, no categories are suggested.
    - **Custom categories**: Select **Create category** and enter a theme or area to include. Select **Save** for the custom category.
7. After configuring your categorization settings, select **Save**.

Categorization processing can take some time depending on data volume. If you need to cancel an in-progress categorization job, select **Cancel** on the **Analysis** tab. You still pay for any compute units consumed before the cancellation. For more information, see [Billing in Data Security Investigations](data-security-investigations-billing).

After categorization processing completes, select categorization areas or individual subject areas within a category to filter data items for review. Examining the categories helps you quickly identify incident severity and scope.

When you select a specific subject area, a summary for the subject area displays with the following information:

- **Topic name**: The name of the subject area in the category.
- **Topic description**: The description of the subject area generated from AI processing.
- **Topic impact score**: The impact score related to potential risk generated from AI processing.
- **Total documents in sample**: The total number of data items that match the subject area in the investigation scope.

### Add or update categories

After the initial categorization run finishes, you can add new categories or update existing categories without reprocessing the entire categorization job. When you add categories, the system processes only the new categories, and you pay only for the compute units needed to process those newly added categories. The system preserves previously categorized data unless you select an existing category in a new categorization run. Selecting existing categories in a new run reprocesses the category.

You can also change existing categories from **Standard** to **Advanced** or from **Advanced** to **Standard**. When you change the categorization option for existing categories, the system reprocesses those categories with the new option.

To add or update categories for an existing categorization, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis**.
4. Select **Categorize**.
5. Add new categories or update existing categories as applicable:

    - To add new default, suggested, or custom categories, select the categories you want to add to the existing categorization.
    - To change the categorization option for existing categories, select **Standard** or **Advanced** to update the processing level.
6. Select **Save**.

Tip

Adding categories incrementally helps you manage compute unit costs effectively. Start with a focused set of categories and expand as your investigation progresses, rather than selecting all categories upfront.

### Categorization and compute units

For example, you might see the following categories in your investigation:

- **Credentials (712 items)**: This category identifies documents or emails containing passwords or API keys.
- **Operational Information (356 items)**: This category identifies items that contain app credentials in a SharePoint site used by a team in your organization.
- **Internal Communications (122 items)**: This category identifies chat logs or emails that include shared credentials.

From an incident response perspective in this example, exposed credentials are typically the highest risk and the priority to triage, then the other areas for follow-up investigation.

Using categorization in Data Security Investigations might require a significant number of compute units, even for smaller amounts of data included in an investigation scope. The compute unit requirements are directly proportional to the number of categories selected, not the size of the data. When you add new categories to an existing categorization, you pay only for the compute units needed to process the new categories. Previously processed categories don't incur additional compute unit costs.

For more information about compute unit capacity and billing, see [Billing models in Data Security Investigations](data-security-investigations-billing).

## Use vector search

Use vector search to describe what you're looking for in the vectorized data items in the investigation scope. Vector-based semantic search enables similarity-based information retrieval and understands user intent beyond literal words. You can query your impacted data to find all assets related to a particular subject, even if keywords are missing. For example, a pharmaceutical company might use vector search to find all emails, documents, Copilot prompts and responses, and Microsoft Teams messages related to vaccine trials to identify relevant assets that don't mention the words *vaccine* or *trial* but remain pertinent to the investigation.

Vector search also includes content from image-based items that were processed through [Optical Character Recognition (OCR)](data-security-investigations-scope#automatic-vectorization). You can find text from screenshots and scanned documents alongside text-based content.

Additionally, Data Security Investigations supports searching and returning results across multiple languages. You can create a vector search in one language, and vector search can also identify items with the same terms in other languages. For example, if you search for *shared passwords* in English, vector search might identify content in French containing *mot de passe* or content in Spanish containing *contrasena*.

Use natural language to ask a question or enter phrases with specific focus to narrow down items for review. Vector search queries don't add any extra compute unit related capacity costs because the system already processes these scoped items.

To create a vector search, complete the following steps:

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can use vector search.

1. In an investigation, select the **Analyze** card or the **Analysis** tab.
2. Select **Standard** mode.
3. Describe what you're looking for in the search field or select one of the suggested searches.
4. Select the search arrow or press **Enter**.

The vector or suggested search starts and lists data items associated with your query in the items area. Each item includes a search relevance score. The results are listed from high to low by default, with the most relevant items listed first. The search relevance measures how closely each result matches the terms of the search that you provided. The search relevance score indicates the confidence level of the connection and helps give you a sense of confidence about how well each result fits your search. The score applies only to the current vector search, and item scores can change based on the search performed.

Search relevance scores are as follows:

- **High**: Strong connection signals, highly relevant vector search results.
- **Medium**: Moderate connection signals, likely relevant vector search results.
- **Low**: Weak connection signals, possibly less relevant vector search results.

Important

Search relevance scores show only when vector search items are returned.

### Vector search and compute units

Using vector search in Data Security Investigations doesn't require many compute units, even for larger amounts of data included in an investigation scope.

For more information about compute unit capacity and billing, see [Billing models in Data Security Investigations](data-security-investigations-billing).

Tip

Consider adding [context to the investigation](data-security-investigations-investigation#ai-context-for-investigations) to help focus categories on specific areas or issues.

## Use Search with AI (preview)

Use Search with AI (preview) to ask natural language questions or enter keywords with a specific focus to narrow down items for review. Search with AI (preview) supplements vector search and extends AI capabilities when analyzing your data. Search with AI (preview) now includes metadata for data items, which helps you narrow down relevant items based on item file types, sizes, versions, and more.

In addition to relevant items, search results also include a high-level summary of all results. This summary helps you quickly determine if the search items are relevant to your search question or keywords. The summary includes citations to specific items returned by the search and relevance scores for each item.

To use Search with AI (preview), complete the following steps:

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can use Search with AI (preview).

1. In an investigation, select the **Analyze** card or the **Analysis** tab.
2. Select **Ask AI (preview)** mode.
3. In the **Search with AI (preview)** pane, enter your question about the data or enter keywords.
4. After the search completes, review the search summary, item results, and item AI search details.

The item detail pane displays all items matching the context related to your AI search. Use filters to help focus the results by document and sender or author. Select **Document** to view a list of cited items included in the results to automatically filter by relevant items. Use actions on the command bar to examine, categorize, or add one or more items to your mitigation plan.

Select an item in the results and select the **AI summary** view to review the relevance categorization score and a snippet with an extracted example that matches the intent of the search.

## Use examination tools

Tip

Consider adding [context to the investigation](data-security-investigations-investigation#ai-context-for-investigations) to help focus examination results on specific areas or issues.

Use examination to run deep content analysis with AI on selected data items. This examination helps you find security risks buried within impacted data. By examining impacted data for security risks, you can find credentials, network risks, or evidence of threat actor discussion. After you identify security risks, you can scan for sensitive data, like [personal data](data-security-investigations-personal-data), financial, or health information.

In addition to summarizing risks, Data Security Investigations provides mitigation steps and the thought process to explain the assessment. From here, you can add open issues to the mitigation plan, connecting analysis to mitigation. This analysis helps you identify data relevant to your investigation and quickly take action to minimize the impact.

You can choose examination processing for the following focus areas:

- **Credentials**: [Credentials processing](data-security-investigations-credentials) examines and extracts credentials and access assets included in selected data items.
- **Risks**: [Risks processing](data-security-investigations-risks) analyzes and scores selected data items for active risks.
- **Mitigation**: [Mitigation processing](data-security-investigations-mitigation) identifies specific threats and recommends mitigation steps for selected data items.
- **Personal data**: [Personal data processing](data-security-investigations-personal-data) identifies and extracts personal data from selected data items, including names, email addresses, employee IDs, IP addresses, and other PII.
- **Custom**: Define a custom examination focus area using a natural language prompt to describe what you want AI to analyze. Custom examinations produce the same structured results as built-in focus areas. For more information about creating and using custom examinations, see Create a custom examination.

Examination processing can take some time depending on data volume and the focus area you select. If you need to cancel an in-progress examination job, select **Cancel** on the **Analysis** tab. You still pay for any compute units consumed before the cancellation. For more information, see [Billing in Data Security Investigations](data-security-investigations-billing).

When the examination process completes for a focus area, select **Probing history** from the command bar on the right side of the investigation scope page. In the **Probing history** pane, select **View details** for a specific examination process.

### Create a custom examination

In addition to the built-in focus areas, you can create a custom examination to analyze data items for specific scenarios unique to your investigation. Custom examinations use a natural language prompt that you define to instruct the AI on what to look for.

Complete the following steps to create a custom examination:

1. On the investigation scope page, select one or more data items.
2. Select **Examine** from the command bar.
3. Select **Custom** as the examination type.
4. In the prompt field, enter a natural language description of what you want the AI to analyze. Prompts can be up to 2,000 characters.
5. Select **Verify prompt**.
6. Verify the prompt is understood with the same intent.
7. Select **Examine** to start the examination.

After the examination completes, results appear in **Probing history** with the same structured output as built-in focus areas, including findings, severity, surrounding snippets, and thought process explanations.

To edit and re-run a custom examination prompt, select the previously created custom examination type and select **Edit**.

#### Example prompts

The following examples illustrate custom examination prompts for common investigation scenarios:

- **Protected Health Information (PHI)**: "Identify any Protected Health Information (PHI) including patient names, medical record numbers, diagnosis codes, treatment information, and insurance identifiers."
- **Insider trading**: "Identify references to specific stock tickers, trade volumes, non-public earnings data, or language suggesting intent to trade on insider information."
- **IP exfiltration**: "Identify references to project codenames, patent application numbers, unreleased product specifications, or proprietary algorithms."

### Examination and compute units

Using examination in Data Security Investigations might require a significant number of compute units, even for smaller amounts of data included in an investigation scope. The compute unit requirements are directly proportional to the size of the data categorized and each examination option you select.

For more information about compute unit capacity and billing, see [Billing models in Data Security Investigations](data-security-investigations-billing).

### Examination process information

Select **Probing history** from the far-right command bar to display a list of the examination activities for the investigation scope.

The list shows the following summary information for each examination process:

- **Name**: The name of the examination.
- **Created by**: The user principal name (UPN) of the user that created the examination process.
- **Probe**: The probing area selected for the examination.
- **Scope**: The number of items selected for examination.
- **Date**: The creation date of the examination process.
- **Status**: The process status. Values include *In progress*, *Successful*, *Failed*, or *Cancelled*.

Select **View details** when the process finishes to view the examination report and recommendations.