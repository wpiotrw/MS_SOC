---
layout: Conceptual
title: Group and view items in a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-view
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Choose how you group and view content in eDiscovery review sets, including specialized viewers to examine details about individual items.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
ms.custom: sfi-image-nochange, msecd-doc-authoring-1014
locale: en-us
document_id: 1343b5c4-dde2-d885-e165-5860682ec80e
document_version_independent_id: 1343b5c4-dde2-d885-e165-5860682ec80e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-view.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-view
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-view.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 4d4b60bc-4fd2-66ae-201d-a533ef23e91c
---

# Group and view items in a review set in eDiscovery | Microsoft Learn

eDiscovery review sets display content using different grouping options and include specialized viewers that you can use to examine details about individual items.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Grouping

Use the **Group** control in the command bar of a review set to view review content grouped by the following options:

### Option 1: Group items by Group ID and Thread ID

If you're new to eDiscovery or are an existing eDiscovery customer with a steady stream of new cases, group review set items by using [Group IDs and Thread IDs](edisc-ref-document-metadata-fields). This grouping option makes it easier to find and review related items in a review set by grouping them together in the list view. When the **Enable group** option is [enabled in the review set case settings](edisc-settings-review-sets), you see the following grouping options on the **Group** control in the command bar of a review set:

- **Group by families**: All items related to a specific file are grouped together by using the same Group ID. For example, if you have a PowerPoint file in the review set that includes embedded images or .zip files, these images and files are grouped with the PowerPoint file and shown as nested items with the file in the item list view. Microsoft 365 Copilot and Microsoft 365 Copilot Chat user prompts and responses are also grouped together by using the same Group ID when there are multiple prompts and responses associated with a file.
- **Group by conversations**: All email messages, Teams conversations, and Viva Engage conversations are grouped by using the same Thread ID and appear as nested items. Additionally, all associated content for these messages and conversations is also grouped together. For example, if you have an email conversation that includes several email messages, some of which include attachments and some that include embedded images, all of the email messages, attachments, and images are grouped together in the review set list view under an applicable item.

Note

For cases created before March 15, 2023, the **Enable group** toggle is disabled and the **Group by families** and **Group by conversations** options aren't available. Item grouping in review sets for these cases is based on *Family ID* and *Conversation ID* described in Option 2: Group items by Family ID and Conversation ID.

### Option 2: Group items by Family ID and Conversation ID

If you're an existing eDiscovery customer with a large number of existing cases or use existing internal or third-party automation to help process review set items, you might want to continue to group review set items by using [Family IDs and Conversation IDs](edisc-ref-document-metadata-fields). When the **Enable group** option is [disabled in the review set case settings](edisc-settings-review-sets), you see the following grouping options on the **Group** control in the command bar of a review set:

- **Group family attachments**: View review set content grouped by family. Each transcript file is displayed on a line in the list of review set items. Attachments are nested under the item.
- **Group Teams or Viva Engage conversations**: View Teams and Viva Engage content grouped by conversation. Each conversation is displayed on a line in the list of review set items. Transcript files and attachments are nested under the top-level conversation.

Note

[Cloud attachments](edisc-cloud-attachments) are grouped with the conversations they appear in. Grouping cloud attachments with their conversations is accomplished by assigning the same **GroupID** as the transcript file of the message the file was attached to and the same **ConversationId** as the conversation the message appeared in. This means multiple copies of cloud attachments might be added to the review set if they were attached to different conversations.

## Use source view

The **Source** viewer displays the richest view of a selected document. It supports hundreds of file types and is designed to display the truest to native experience possible. For Microsoft Office files, the viewer uses the web version of Office apps to display content such as document comments, Microsoft Teams chats, Excel formulas, hidden rows and columns, and PowerPoint notes.

![Screenshot of the review set source view displaying a selected item's content in its native format.](media/ediscovery-source-view.png)

The **Source** view doesn't support previewing video and audio files. To view these files, export them from the review set as described in [Export from a review set](edisc-review-set-export).

## Use plain text view

The **Plain text** viewer provides a view of the extracted text of a selected file. It ignores any embedded images and formatting but is useful if you want to understand the content quickly. The text view also includes these features:

- Line counter makes it easier to reference specific portions of a document
- Search hit highlighting that highlights terms within the document and in the scrollbar

![Screenshot of the plain text view showing extracted text content with line numbers and search hit highlighting.](media/ediscovery-plain-text-view.png)

## Use annotate view

The **Annotate** view provides features that let you apply markup on a selected document, including the ability to:

- **Select annotations**: Select annotations on a document to delete.
- **Select text**: Select text on the document to delete.
- **Area redactions**: Draw a box on the document to hide sensitive content.
- **Pencil**: Freehand draw in selectable colors on a document to bring attention to certain portions of a document.
- **Toggle annotation transparency**: Make annotations semi-transparent to view the content behind the annotation.
- **Previous page**: Go to the previous page.
- **Next page**: Go to the next page.
- **Go to page**: Enter a specific page number to go to.
- **Zoom**: Set the zoom level for annotate view.
- **Rotate**: Rotate the document clockwise.

![Screenshot of the review set annotate view showing markup and redaction tools for the selected item.](media/ediscovery-annotate-view.png)

### Commit redactions

When you apply annotations in the **Annotate** view (including area redactions, text deletion, and pencil markup), the annotations save with the document but don't change how the document appears in the review set, in search results, or in exports until you **commit** them. When you commit a redaction, it generates a redacted PDF (`{itemId}_burn.pdf`) that's persisted alongside the original item in the review set.

To include redacted PDFs in an export, select *Export redaction* when configuring the export. For details on how redacted items appear in the export package – including how individual documents, attachments, and conversations are handled – see [Export from a review set](edisc-review-set-export#choose-export-options-for-a-review-set).

## Use metadata view

You can toggle the panel in the **Metadata** view on or off to display various metadata associated with the selected document. Although you can customize the search results grid to display specific metadata, there are instances where scrolling horizontally can be difficult while reviewing data. The File metadata panel allows you to toggle on a view within the viewer.

![Screenshot of the review set metadata view showing file metadata details for the selected document.](media/ediscovery-metadata-view.png)

## Use Copilot activity view

The **Copilot activity** view displays the Microsoft 365 Copilot and Microsoft 365 Copilot Chat activity associated with the selected item. User prompts and Copilot responses display in the order they're generated.

![Screenshot of the review set Copilot activity view showing user prompts and Copilot responses for the selected item.](media/ediscovery-copilot-view.png)

## Summarize an item by using Microsoft Security Copilot

You can use [Security Copilot in Microsoft Purview](copilot-in-purview-overview) to provide a contextual summary of most items in a review set. The summary is based on the text included in a selected item. The contextual summary saves time for reviewers by quickly identifying information helpful when tagging or exporting items.

Security Copilot summarizes the entire item, including any documents, meetings transcripts, or attachments. Most common document file types are supported.

### Limitations

Security Copilot summarization in review sets has the following limitations:

- The *Plain text* view must be available for an item for Security Copilot availability. For more information about which file types support plain text views, see [Supported file types in eDiscovery](edisc-ref-supported-file-types).
- The item content must be at least 100 words and less than 15,000 words. If the item content is fewer than 100 words or more than 15,000 words, Security Copilot doesn't summarize it.
- Summarize items in various languages supported by Security Copilot. For more information, see [Supported languages in Microsoft Security Copilot](/en-us/copilot/security/supported-languages).
- Currently, only individual Teams messages can be summarized. For example. if you summarize an individual Teams message, Copilot doesn't pull in the surrounding conversation (family or conversation groups).

For more information about Microsoft Security Copilot and Microsoft's artificial intelligence (AI) responsibilities, see [Responsible AI FAQ](/en-us/security-copilot/rai-faqs-security-copilot).

### Prerequisites for using Security Copilot

To summarize an item in a review set in eDiscovery by using Security Copilot, you must:

- Have specific licenses and onboard your organization to Security Copilot. For more information, see [Learn more about Security Copilot licensing requirements and onboarding](/en-us/security-copilot/get-started-security-copilot).
- Have an admin assign you at least one of the required roles to access the Security Copilot portal. For more information about these required roles, see [Understand authentication in Security Copilot](/en-us/security-copilot/authentication#access-security-copilot-portal).

Note

Currently, eDiscovery only supports Security Copilot in the embedded experience (not the [Security Copilot stand-alone experience](/en-us/security-copilot/experiences-security-copilot)).

### Summarize an item in a review set

1. In eDiscovery, open a review set and filter the items as needed.
2. Select an item in the list. You can select a parent item or a child item.
3. In any item view, select **Summarize**. Selecting **Summarize** opens the **Copilot** panel on the right side of the screen and displays a summary of the item.

    Note

    If the plain text view isn't available for an item, **Summarize** isn't available to select.
4. To use Copilot to create the summary, select one of the suggested prompts at the bottom of the panel. For example, if the item is a legal contract in the Microsoft Word format, select the *Identify key participants*, *Identify key topics*, or *Identify action items* prompt.

    You can also enter an open-ended question in the *Ask questions and get insights about this item* field. Copilot responses are generated without using information from prior messages. For more information about prompts and promptbooks, see [Microsoft Copilot in Microsoft Purview prompts and promptbooks](copilot-in-purview-promptbooks).

    Note

    Only item content is summarized. If you ask a question relevant to the item content, Copilot provides a result. If the question isn't relevant to the item content, Copilot instructs you to ask a different question.
5. To provide feedback on the summarized content, select the drop-down arrow in the lower-right corner below the summary, and then enter your feedback.
6. After reviewing the summary, you can take other eDiscovery actions connected with review set items.

## Use viewer and management tools

For selected content, you get extra view and management tools that help you work with documents.

![Screenshot of the review set viewer showing additional tools for managing and working with selected content.](media/ediscovery-additional-viewer-tools.png)

You can select the following actions for selected content:

- **View or update notes**: Opens the **Notes** pane where you can view or add notes to the selected document. You can display the notes for the document in a column in the dashboard list by customizing your displayed columns.
- **Show in a new window**: Displays the selected document in a new browser window or tab.
- **Download PDF**: Downloads the selected document as a .pdf file.
- **Move up**: Selects the previous review set item and displays the item in the viewer.
- **Move down**: Selects the next review set item and displays the item in the viewer.
- **Maximize/Minimize**: Maximizes the viewer pane to full screen and minimizes the viewer pane.
- **Close**: Closes the selected item from the viewers.

Important

To download a PDF containing items from a review set, you must be assigned the *Export* role or be assigned to a role group that includes the *Export* role. For more information about eDiscovery permissions, see [Assign eDiscovery permissions](edisc-permissions#rbac-roles-related-to-ediscovery).