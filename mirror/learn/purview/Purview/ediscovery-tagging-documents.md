---
layout: Conceptual
title: Tag documents in a review set | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-tagging-documents
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Tagging documents in a review set helps remove unnecessary content and identify relevant content in an eDiscovery (Premium) case.
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
document_id: 82a80ed2-bc38-b0bc-77cb-834254ea2010
document_version_independent_id: 82a80ed2-bc38-b0bc-77cb-834254ea2010
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-tagging-documents.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-tagging-documents
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-tagging-documents.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6691f6f9-8b96-c83e-632d-ab587fd4c9e9
---

# Tag documents in a review set | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Organizing content in a review set is important to complete various workflows in the eDiscovery process. This workflow includes:

- Culling unnecessary content
- Identifying relevant content
- Identifying content that must be reviewed by an expert or attorney

When experts, attorneys, or other users review content in a review set, their opinions related to the content can be captured by using tags. For example, if the intent is to cull unnecessary content, a user can tag documents with a tag such as "non-responsive". After content has been reviewed and tagged, a review set search can be created to exclude any content tagged as "non-responsive". This process eliminates the non-responsive content from the next steps in the eDiscovery workflow.

You can use *tag templates* to define tags and review workflow across all cases and review sets in your organization. This method is the recommeded approach and helps provide structure and standardization for tagging to ensure searches identify similar content across your organization. You can also use the tagging panel in an individual review set to customized tags for each case when tag templates don't meet your needs, but tags created here are specifically for the individual case and review set.

## Tag types

eDiscovery (Premium) provides two types of tags:

- **Single-select tags**: Restricts reviewers to selecting a single tag within a tag group. These types of tags can be useful to ensure that reviewers don't select conflicting tags such as "responsive" and "non-responsive". Single choice tags appear as radio buttons.
- **Multi-select tags**: Allow reviews to select multiple tags within a tag group. These types of tags appear as checkboxes.

## Tag groups

In addition to the tag types, the structure of how tags groups are organized in the tag panel can be used to make tagging documents more intuitive. Tags are organized in tag groups. Review set search supports the ability to search by tag and by tag groups. This means you can create a review set search to retrieve documents tagged with any tag in a group or the group itself.

For example, if you need to identify and tag privileged content, grouping can be used to make it clear that a reviewer can tag a document as *Privileged* (the tag group) and select *Attorney work product* (specific tag) as the type of privilege within the tag group.

![Nested tags within a tag section.](media/nestingtags.png)

## Tag templates (preview)

Tag templates are used to define and standardize tags and the review workflow across all cases and review sets in your organization. Each tag template contains tag groups where you can create a grouping structure for individual tags. You can create tag templates in the **Tag templates** section in **eDiscovery (Premium) settings**.

### Create tag templates

To create a new tag template, complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), select **eDiscovery** &gt; **Premium** and then select **eDiscovery (Premium) settings**.
2. Select **Tag templates**.
3. On the **Manage tag templates** page, select **Create**.
4. On the **New tag template** page, enter a name and description for the tag template.
5. In the initial tag group, enter a tag group name and use the dropdown to define if this as a **Multi-select** or **Single-elect** tag group.
6. Enter at least one tag name in the tag group. Select **Add tag** to add additional tags to the tag group.
7. If needed, select **Add tag group** to add additional tag groups and tags to the tag template.
8. Preview the tag template group and tag structure in the **Preview** pane on the right side of the **New tag template** page.
9. When complete, select **Save**.

The tag template is now available for use in all cases and review sets in your organization.

### Manage tag templates

After you create a tag template, you can edit or delete it. You can also view information about the tag template, including the dates when it was created or last modified.

To edit a tag template, select the tag template name on the **Manage tag templates** page and select **Edit**. On the **Edit tag template** page, you can edit the tag template name, description, and tag groups and tags. When you're done, select **Save**.

To delete a tag template, select the tag template name on the **Manage tag templates** page and select **Delete**. Select **Yes** to confirm the deletion or **No** to cancel the deletion.

## Apply tag templates to a case and review sets

After you've created a tag template, you can apply it to a review set. You can apply a tag template when you create a new review set or when you edit an existing review set.

To apply a tag template to a new review set, complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), select **eDiscovery** &gt; **Premium**.
2. Select the **Cases** tab and select a case.
3. In the case, select **Review sets**, select a review set, and then select **Open review set**.
4. On the review set command bar, select **Manage** &gt; **Tags**.
5. On the **Manage tags** page, delete the blank tag group then select **Import tag templates**.
6. On the **Import tag templates** flyout page, select the tag template that you want to apply to the review set and then select **Import**.
7. If needed, you can edit the tag template as it applies to the case and review set.
8. Select **Save** to apply the tag templates to the case and review set.

The applied tag template is now available for use in the case and all included review sets.

## Create tags for a specific case or review set

If you choose not to use tag templates for a specific case or review set, you can create tags directly in the review set. This is useful when you need to create tags that are specific to a case or review set. However, these tags are unique to the case or review set and can't be used in other cases or review sets.

Before applying tags to items in a review set, you need to create a tag structure.

1. Open a review set and on the review set command bar, select **Manage** &gt; **Tags**.
2. On the **Manage tags** flyout page, enter a *Tag group name* and select either **Multi-select** or **Single-select** for the tag group.
3. Enter one or more tags in the tag group. Select **Add tag** to add additional tags to the tag group.
4. Select **Add tag group** if more tag groups and tags are needed.
5. Preview the tag template group and tag structure in the **Preview** pane on the right side of the **New tag template** page.
6. Select **Save** to apply the tag group and tags to the case and review set.

## Apply tags

With the tag structure from tag templates or custom tagging in place, reviewers can apply tags to items in a review set by configuring tagging settings.

1. In the review set command bar, select **Tag files** to display the **Tag files** flyout page (also called the *tagging panel*).
2. On the **Tag files** flyout page, you can set the following options to configure how to tag items displayed in the review set. The filters or filter queries currently applied to the review set determine which items are displayed and therefore the items that you can apply tags to. For more information, see [Query and filter content in a review set](ediscovery-review-set-search).

    - **Choose selection**. Choose one the following options to determine the scope of items to apply tags to.

        - **Tag selected items**: This option applies tags to the items that you select. You can select items before or after launching the tagging panel. This option displays (in real time) the number of selected items that are tagged.
        - **Tag all items in list**: This option applies tags to all items displayed in the review set. This option displays the total number of items that are tagged.
    - **Expand selection**: Use the following options to tag additional items that are related to tagged items in the review set. Depending on the **Enable group** option [enabled in the case settings](ediscovery-configure-review-set-settings), you'll see the following options:

        **With *Enable group* in settings disabled**:

        - **None**: This option doesn't apply tags to associated family items or associated conversation items. It only applies tags to the items that are selected or to all items in the review set list.
        - **Include family groups**: This option applies the same tag to the associated family items of items that are tagged. *Family items* are items that share the same **FamilyId** metadata property value. For example, a document that's attached to an email message shares the same **FamilyId** as the email message. So if this option is selected for this example, the email message and the document are tagged, even though the document might not be included in the list of review set items.
        - **Include conversation groups**: This option applies the same tag to all items that are in the same Teams or Viva Engage conversation as the items that are tagged. *Conversation items* are items that share the same **ConversationId** metadata property value. All messages, posts, and corresponding transcript file of a conversation share the same **ConversationId**. If this option is selected, then all items in the same conversation (and transcript file) are tagged, even though some of those conversation items might not be included in the list of review set items. For more information about conversation items, see the "Grouping" section in [eDiscovery (Premium) workflow for content in Microsoft Teams](ediscovery-teams-workflow#grouping).

        Note

        Including family or conversation groups doesn't change the count of items shown in the **Tag selected items** or **Tag all items in list** options. In other words, the number of grouped items that are tagged is not displayed.

        **With *Enable group* in settings enabled**:

        - **None**: This option doesn't apply tags to family group items or conversation group items. It only applies tags to the items that are selected or to all items in the review set list.
        - **Include family groups**: This option applies the same tag to the associated family items of items that are tagged. *Family group* items are items that share the same **GroupId** metadata property value. For example, a document that's attached to an PowerPoint file shares the same **GroupId** as the document. So if this option is selected for this example, the document and the PowerPoint file are both tagged. Both are grouped together in the list of review set items.
        - **Include conversation groups**: This option applies the same tag to all items that are in the same email, Teams, or Viva Engage conversation as the items that are tagged. *Conversation group* items are items that share the same **ThreadId** metadata property value. All messages, posts, and corresponding transcript files of a conversation share the same **ThreadId**. If this option is selected, then all items in the same conversation (and transcript file) are tagged. All items are grouped together in the list of review set items.
    - **Assign tags**: This section displays the tags (organized by tag groups) that you can apply to documents. These are either the tag groups and tags assigned using tag templates or custom tag groups and tags that you've created for this case. You can only apply one single-choice tag (identified by a radio button) per tag group. However, you can apply multiple multi-choice tags (identified by a checkbox).
3. Select **Apply tags** to apply the tags based on your settings.

    The **Applying tags** status message is displayed for each tag group on the tagging panel to indicate a tagging job has been started. Tags for each tag group in the **Assign tags** section are greyed out until the job is completed.

Tip

If you're in the process of configuring the settings on the tagging panel, but want to start over, select **Reset tag assignment** to clear the current setting. This control doesn't apply to items that are already tagged, and it doesn't change or remove tags from previously tagged items.

## Monitor tagging jobs

When you tag a large number of items (or select the **Tag all items in list**) option, a **Tagging documents** job is created. You view the status of this job on the **Jobs** tab in the case. This view helps you track large tagging jobs that may take a long time to complete. In some cases, a tagging job might be complete, but the **Applying tags** status message in the tagging panel is still displayed. To update the status of tagging jobs, select **Refresh** in the review set command bar.

## Removing tags

You can remove tags from items in a review set. However, you can't remove a single-choice tag that's been applied to a review set item. You can only change a single-choice tag to another single-choice tag within the same tag group.

To remove a tag:

1. Select the items that you want to remove the tag from.
2. Select **Tag files** to display the tagging panel.
3. Under **Assign tags**, unselect the tag, and then select **Apply tags**.

You can also use the previous procedure to change the tag applied to selected items. After unselecting the current tag, you can select a different one.