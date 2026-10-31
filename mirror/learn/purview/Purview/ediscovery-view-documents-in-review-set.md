---
layout: Conceptual
title: Group and view documents in a review set in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-view-documents-in-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Choose how you group and view content in eDiscovery (Premium) review sets, including specialized viewers to examine details about individual items.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 704023c7-0616-2188-4077-3e06e0ddb9a5
document_version_independent_id: 704023c7-0616-2188-4077-3e06e0ddb9a5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-view-documents-in-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-view-documents-in-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-view-documents-in-review-set.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 02e6f0a0-88b4-e69d-39b2-a2b3c36fc94c
---

# Group and view documents in a review set in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

eDiscovery (Premium) review sets display content using different grouping options and include specialized viewers that you can use to examine details about individual items.

## Grouping

Use the **Group** control in the command bar of a review set to view review content grouped by the following options:

### Option 1: Group items with Group ID and Thread ID

If you're new to eDiscovery or are an existing eDiscovery customer with a steady stream of new cases, grouping review set items using [Group IDs and Thread IDs](ediscovery-document-metadata-fields) is the recommended option. This grouping option makes it easier to find and review related items in a review set by grouping them together in the list view. With the **Enable group** option [enabled in the case settings](ediscovery-configure-review-set-settings), you'll see the following grouping options on the **Group** control in the command bar of a review set:

- **Group by families**: All items related to a specific file are grouped together using the same Group ID. For example, if you have a PowerPoint file in the review set that includes imbedded images or .zip files, these images and files are grouped with the PowerPoint file and shown as nested items with the file in the item list view. Microsoft 365 Copilot and Microsoft 365 Copilot Chat user prompts and responses are also grouped together using the same Group ID when there are multiple prompts and responses associated with a file.
- **Group by conversations**: All email messages, Teams conversations, and Viva Engage conversations are grouped using the same Thread ID and appear as nested items. Additionally, all associated content for these messages and conversations is also grouped together. For example, if you have an email conversation that includes several email messages, some of which include attachments and some that include embedded images, all of the email messages, attachments, and images are grouped together in the review set list view under an applicable item.

Note

For cases created before March 15, 2023, the **Enable group** toggle is disabled and these grouping options aren't available. Item grouping in review sets for these cases is based on *Family ID* and *Conversation ID* described in Option 2.

### Option 2: Group items with Family ID and Conversation ID

If you're an existing eDiscovery with a large number of existing cases or use existing internal or third-party automation to help process review set items, you may want to continue to group review set items with [Family IDs and Conversation IDs](ediscovery-document-metadata-fields). With the **Enable group** option [disabled in the case settings](ediscovery-configure-review-set-settings), you'll see the following grouping options on the **Group** control in the command bar of a review set:

- **Group family attachments**: View review set content grouped by family. Each transcript file is displayed on a line in the list of review set items. Attachments are nested under the item.
- **Group Teams or Viva Engage conversations**: View Teams and Viva Engage content grouped by conversation. Each conversation is displayed on a line in the list of review set items. Transcript files and attachments are nested under the top-level conversation.

Note

Cloud attachments are grouped with the conversations they appear in. This grouping is accomplished by assigning the same **FamilyId** as the transcript file of the message the file was attached to and the same **ConversationId** as the conversation the message appeared in. This means multiple copies of cloud attachments may be added to the review set if they were attached to different conversations.

## Source view

The **Source** viewer displays the richest view of a selected document. It supports hundreds of file types and is meant to display the truest to native experience possible. For Microsoft Office files, the viewer uses the web version of Office apps to display content such as document comments, Microsoft Teams chats, Excel formulas, hidden rows/columns, and PowerPoint notes.

![Review set source view](media/ediscovery-source-view.png)

## Plain text view

The **Plain text** viewer provides a view of the extracted text of a selected file. It ignores any embedded images and formatting but is useful if you're trying to understand the content quickly. Text view also includes these features:

- Line counter makes it easier to reference specific portions of a document
- Search hit highlighting that highlights terms within the document and in the scrollbar

![Review set plain text view.](media/ediscovery-plain-text-view.png)

## Annotate view

The **Annotate** view provides features that allow users to apply markup on a selected document including:

- **Select annotations**: Select annotations on a document to delete.
- **Select text**: Select text on the document to delete.
- **Area redactions**: Draw a box on the document to hide sensitive content.
- **Pencil**: Free-hand draw in selectable colors on a document in order to bring attention to certain portions of a document.
- **Toggle annotation transparency**: Make annotations semi-transparent in order to view the content behind the annotation.
- **Previous page**: Navigates to previous page.
- **Next page**: Navigates to the next page.
- **Go to page**: Enter a specific page number to navigate to.
- **Zoom**: Set the zoom level for annotate view.
- **Rotate**: Rotate the document clockwise.

![Review set annotate view.](media/ediscovery-annotate-view.png)

## Metadata view

The panel in the **Metadata** view can be toggled on/off to display various metadata associated with the selected document. Although the search results grid can be customized to display specific metadata, there are instances where scrolling horizontally can be difficult while reviewing data. The File metadata panel allows a user to toggle on a view within the viewer.

![Review set metadata view](media/ediscovery-metadata-view.png)

## Copilot activity view

The **Copilot activity** view displays the Microsoft 365 Copilot and Microsoft 365 Copilot Chat activity associated with the selected item. User prompts and Copilot responses are displayed in the order they were generated.

![Review set Copilot view](media/ediscovery-copilot-view.png)

## Summarize an item by using Microsoft Security Copilot

You can use [Security Copilot in Microsoft Purview](copilot-in-purview-overview) to provide a contextual summary of most items in a review set. The summary provided is in the context of text included in a selected item. This summary can save time for reviewers by quickly identifying information helpful when tagging or exporting items.

Security Copilot summarizes the entire item, including any documents, meetings transcripts, or attachments. Most all of the common document file types are supported.

### Limitations

- The *Plain text* view must be available for an item for Security Copilot availability. For more information on which file types support plain text views, see [Supported file types in eDiscovery (Premium)](ediscovery-supported-file-types).
- The item content must be at least 100 words and fewer than 15,000 words. If the item content is fewer than 100 words or more than 15,000 words, Security Copilot doesn't summarize it.
- Currently, only English language messages are supported for summarization.
- Currently, only individual Teams messages can be summarized. For example. if you summarize an individual Teams message, Copilot doesn't pull in the surrounding conversation (family or conversation groups).

For more information about Microsoft Security Copilot and Microsoft's artificial intelligence (AI) responsibilities, see [Responsible AI FAQ](/en-us/security-copilot/rai-faqs-security-copilot).

### Prerequisites for using Security Copilot

To summarize an item in a review set in eDiscovery using Security Copilot, you must have:

- Specific licenses and you must onboard your organization to Security Copilot. For more information, see [Learn more about Security Copilot licensing requirements and onboarding](/en-us/security-copilot/get-started-security-copilot).
- Your admin assigned at least one of the required roles to access the Security Copilot portal. For more information about these required roles, see [Understand authentication in Security Copilot](/en-us/security-copilot/authentication#access-security-copilot-portal).

Note

Currently, eDiscovery only supports Security Copilot in the embedded experience (not the [stand-alone experience](/en-us/security-copilot/experiences-security-copilot)).

### Summarize an item in a review set

1. In eDiscovery, open a review set and filter the items as needed.
2. Select an item in the list. You can select a parent item or a child item.
3. In an item in any item view, then select **Summarize**. This opens the **Copilot** panel on the right side of the screen and displays a summary of the item.

    Note

    If the plain text view isn't available for an item, **Summarize** won't be available to select.
4. To use Copilot to create the summary, select one of the suggested prompts at the bottom of the panel. For example, if the item is a legal contract in the Microsoft Word format, select the *Identify key participants*, *Identify key topics*, or *Identify action items* prompt.

    You can also enter an open-ended question in the *Ask questions and get insights about this item* field. Copilot responses are generated without using information from prior messages. For more information about prompts and promptbooks, see [Microsoft Copilot in Microsoft Purview prompts and promptbooks](copilot-in-purview-promptbooks).

    Note

    Only item content is summarized. If you ask a question relevant to the item content, Copilot provides a result. If the question isn't relevant to the item content, Copilot instructs you to ask a different question.
5. If you want to provide feedback on the summarized content, select the drop-down arrow in the lower-right corner below the summary, and then enter your feedback.
6. After reviewing the summary, you can take other eDiscovery actions connected with review set items.

## Viewer and management tools

For selected content, there are additional view and management tools to help you work with documents.

![Review set additional viewer tools](media/ediscovery-additional-viewer-tools.png)

You can select the following actions for selected content:

- **View or update notes**: Opens the **Notes** pane where you can view or add notes to the selected document. You can display the notes for the document in a column in the dashboard list by customizing your displayed columns.
- **Show in a new window**: Displays the selected document in a new browser window/tab.
- **Download PDF**: Downloads the selected document as a .pdf file.
- **Move up**: Selects the previous review set item and displays the item in the viewer.
- **Move down**: Selects the next review set item and displays the item in the viewer.
- **Maximize/Minimize**: Maximizes the viewer pane to full screen and minimizes the viewer pane.
- **Close**: Closes the selected item from the viewers.

Important

To download a PDF containing items from a review set, you must be assigned the *Export* role or be assigned to a role group that includes the *Export* role. For more information about eDiscovery permissions, see [Assign eDiscovery permissions in the Microsoft Purview portal](ediscovery-assign-permissions#rbac-roles-related-to-ediscovery).