---
layout: Conceptual
title: Tag items in a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-tagging
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about tagging items in a review set with eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: aec10535-5bf3-0c7d-a13e-bab168818e77
document_version_independent_id: aec10535-5bf3-0c7d-a13e-bab168818e77
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-tagging.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-tagging
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-tagging.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a7c576ba-d962-0fe4-e97a-854bcefbb520
---

# Tag items in a review set in eDiscovery | Microsoft Learn

Organizing content in a review set is important to complete various workflows in the eDiscovery process. The review-set organization workflow includes:

- Culling unnecessary content
- Identifying relevant content
- Identifying content that must be reviewed by an expert or attorney

When experts, attorneys, or other users review content in a review set, they can capture their opinions related to the content by using tags. For example, if the intent is to cull unnecessary content, a user can tag documents with a tag such as "nonresponsive". After content is reviewed and tagged, you can create a review set search to exclude any content tagged as "nonresponsive". Excluding tagged nonresponsive content from the review set search eliminates that content from the next steps in the eDiscovery workflow.

You can use *tag templates* to define tags and review workflow across all cases and review sets in your organization. Using tag templates is the recommended approach and helps provide structure and standardization for tagging to ensure searches identify similar content across your organization. You can also use the tagging panel in an individual review set to customize tags for each case when tag templates don't meet your needs, but tags created here are specifically for the individual case and review set.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Tag types

eDiscovery has two types of tags:

- **Single-select tags**: Restricts reviewers to selecting a single tag within a tag group. These types of tags can be useful to ensure that reviewers don't select conflicting tags such as "responsive" and "nonresponsive". Single choice tags appear as radio buttons.
- **Multi-select tags**: Allow reviewers to select multiple tags within a tag group. These types of tags appear as checkboxes.

## Tag groups

In addition to the tag types, the structure of how tag groups are organized in the tag panel can make tagging documents more intuitive. Tags are organized in tag groups. Review set search supports the ability to search by tag and by tag groups. Because review set search supports both levels, you can create a review set search to retrieve documents tagged with any tag in a group or the group itself.

For example, if you need to identify and tag privileged content, grouping can be used to make it clear that a reviewer can tag a document as *Privileged* (the tag group) and select *Attorney work product* (specific tag) as the type of privilege within the tag group.

![Nested tags within a tag section in the tagging panel.](media/nestingtags.png)

## Tag templates (preview)

Use tag templates to define and standardize tags and the review workflow across all cases and review sets in your organization. Each tag template contains tag groups where you can create a grouping structure for individual tags. You can create tag templates in the **Tag templates** tab in **eDiscovery settings**.

### Create tag templates

To create a new tag template, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **Settings** solution card, then select **eDiscovery**.
3. Select **Tag templates**.
4. On **Manage tag templates**, select **Create**.
5. On **New tag template**, enter a name and description for the tag template.
6. In the initial tag group, enter a tag group name and use the dropdown to define this as a **Multi-select** or **Single-select** tag group.
7. Enter at least one tag name in the tag group. Select **Add tag** to add more tags to the tag group.
8. If needed, select **Add tag group** to add more tag groups and tags to the tag template.
9. Preview the tag template group and tag structure in the **Preview** pane on the right side of **New tag template**.
10. When complete, select **Save**.

The tag template is now available for use in all cases and review sets in your organization.

### Manage tag templates

After you create a tag template, you can edit or delete it. You can also view information about the tag template, including the dates when you created or last modified it.

To edit a tag template, select the tag template name on **Manage tag templates** and select **Edit**. On **Edit tag template**, you can edit the tag template name, description, and tag groups and tags. When you're done, select **Save**.

To delete a tag template, select the tag template name on **Manage tag templates** and select **Delete**. Select **Yes** to confirm the deletion or **No** to cancel the deletion.

## Apply tag templates to a case and review sets

After you create a tag template, you can apply it to a review set. You can apply a tag template when you create a new review set or when you edit an existing review set.

To apply a tag template to a new review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Review sets** tab.
4. Select a review set, then select the **All items** tab.
5. On the review set command bar, select **Manage** &gt; **Tags**.
6. On **Manage tags**, delete the blank tag group, then select **Import tag templates**.
7. On **Import tag templates**, select the tag template that you want to apply to the review set and then select **Import**.
8. If needed, edit the tag template as it applies to the case and review set.
9. Select **Save** to apply the tag templates to the case and review set.

The applied tag template is now available for use in the case and all included review sets.

## Create tags for a specific case or review set

If you don't want to use tag templates for a specific case or review set, you can create tags directly in the review set. This approach is useful when you need tags that are specific to a case or review set. However, these tags are unique to the case or review set and can't be used in other cases or review sets.

Before you apply tags to items in a review set, you need to create a tag structure.

1. Open a review set. On the review set command bar, select **Manage** &gt; **Tags**.
2. On **Manage tags**, enter a *Tag group name* and select either **Multi-select** or **Single-select** for the tag group.
3. Enter one or more tags in the tag group. Select **Add tag** to add more tags to the tag group.
4. Select **Add tag group** if you need more tag groups and tags.
5. Preview the tag template group and tag structure in the **Preview** pane on the right side of **New tag template**.
6. Select **Save** to apply the tag group and tags to the case and review set.

## Apply tags

With the tag structure from tag templates or custom tagging in place, reviewers can apply tags to items in a review set by configuring tagging settings.

1. In the review set command bar, select **Tag files** to display the **Tag files** flyout page (also called the *tagging panel*).
2. On the **Tag files** flyout page, set the following options to configure how to tag items displayed in the review set. The filters or filter queries currently applied to the review set determine which items are displayed and therefore the items that you can apply tags to. For more information, see [Search content in a review set in eDiscovery](edisc-review-set-search).

    - **Choose selection**. Choose one the following options to determine the scope of items to apply tags to.

        - **Tag selected items**: Applies tags to the items that you select. You can select items before or after launching the tagging panel. The **Tag selected items** option displays (in real time) the number of selected items that are tagged.
        - **Tag all items in list**: Applies tags to all items displayed in the review set. The **Tag all items in list** option displays the total number of items that are tagged.
    - **Expand selection**: Use the following options to tag additional items that are related to tagged items in the review set. Depending on the **Enable group** option [enabled in the review set settings](edisc-settings-review-sets), you see the following options:

        **With *Enable group* in settings disabled**:

        - **None**: The **None** option doesn't apply tags to associated family items or associated conversation items. It only applies tags to the items that are selected or to all items in the review set list.
        - **Include family groups**: The **Include family groups** option applies the same tag to the associated family items of items that are tagged. *Family items* are items that share the same **FamilyId** metadata property value. For example, a document that's attached to an email message shares the same **FamilyId** as the email message. So if this option is selected for this example, the email message and the document are tagged, even though the document might not be included in the list of review set items.
        - **Include conversation groups**: The **Include conversation groups** option applies the same tag to all items that are in the same Teams or Viva Engage conversation as the items that are tagged. *Conversation items* are items that share the same **ConversationId** metadata property value. All messages, posts, and corresponding transcript file of a conversation share the same **ConversationId**. If this option is selected, then all items in the same conversation (and transcript file) are tagged, even though some of those conversation items might not be included in the list of review set items.

        Note

        Including family or conversation groups doesn't change the count of items shown in the **Tag selected items** or **Tag all items in list** options. In other words, the number of grouped items that are tagged isn't displayed.

        **With *Enable group* in settings enabled**:

        - **None**: The **None** option doesn't apply tags to family group items or conversation group items. It only applies tags to the items that are selected or to all items in the review set list.
        - **Include family groups**: The **Include family groups** option applies the same tag to the associated family items of items that are tagged. *Family group* items are items that share the same **GroupId** metadata property value. For example, a document that's attached to a PowerPoint file shares the same **GroupId** as the document. So if this option is selected for this example, the document and the PowerPoint file are both tagged. Both are grouped together in the list of review set items.
        - **Include conversation groups**: The **Include conversation groups** option applies the same tag to all items that are in the same email, Teams, or Viva Engage conversation as the items that are tagged. *Conversation group* items are items that share the same **ThreadId** metadata property value. All messages, posts, and corresponding transcript files of a conversation share the same **ThreadId**. If this option is selected, then all items in the same conversation (and transcript file) are tagged. All items are grouped together in the list of review set items.
    - **Assign tags**: This section displays the tags (organized by tag groups) that you can apply to documents. These tags are either the tag groups and tags assigned using tag templates or custom tag groups and tags that you create for this case. You can only apply one single-choice tag (identified by a radio button) per tag group. However, you can apply multiple multichoice tags (identified by a checkbox).
3. Select **Apply tags** to apply the tags based on your settings.

    The **Applying tags** status message is displayed for each tag group on the tagging panel to indicate a tagging process has started. Tags for each tag group in the **Assign tags** section are greyed out until the process completes.

Tip

If you're in the process of configuring the settings on the tagging panel, but want to start over, select **Reset tag assignment** to clear the current setting. This control doesn't apply to items that are already tagged, and it doesn't change or remove tags from previously tagged items.

## Set up smart tags

Machine learning (ML) capabilities in eDiscovery can help you make the decision process more efficient when reviewing case documents in a review set. Smart tags bring the ML capabilities to where you record decisions: when tagging documents during review. When you create a smart tag group, the decisions that result from the ML model you associate with the smart tag group display in-line with the tags in the tag group. Displaying model decisions inline with the tag group helps you see the ML results information in-line when you're reviewing specific documents.

### How to set up a smart tag group

To create a smart tag group, complete the following steps:

1. In a review set, select **Manage review set** and then select **Manage tags**.
2. Select **Add tag group** and then select **Add smart tag group**.
3. Select the ML model that you want to associate to the tag group.

    Selecting an ML model creates a tag group and *N* child tags, where *N* is the number of possible outputs of the model. For example, the [attorney-client privilege detection model](edisc-settings-analytics) has two possible outputs:

    - **Positive**: Use to tag documents that contain attorney-client privileged content.
    - **Negative**: Use to tag documents that don't contain attorney-client privileged content.

    If you select this model, you create a tag group with two child tags (one child tag named **Positive** and the other named **Negative**) for the review set. In this example, each child tag corresponds to one of the possible outputs from the attorney-client privilege detection model.
4. Optionally, rename the tag group and the child tags. For example, you could rename the **Positive** tag to **Privileged** and the **Negative** tag to **Not privileged**.

### How to use smart tags

When reviewing a document, the model's results display next to the appropriate child tag. For example, if you have a smart tag group for attorney-client privilege detection and you review a document that is potentially privileged, the reason for that conclusion displays next to the appropriate tag. The tag isn't automatically applied to the document. The reviewer makes the decision about how to tag the document.

## Monitor tagging jobs

When you tag a large number of items or select the **Tag all items in list** option, a **Tagging documents** job is created. You can view the status of this job on the **Jobs** tab in the case. The **Jobs** tab helps you track large tagging jobs that might take a long time to complete. In some cases, a tagging job might be complete, but the **Applying tags** status message in the tagging panel still displays. To update the status of tagging jobs, select **Refresh** in the review set command bar.

## Remove tags

You can remove tags from items in a review set. However, you can't remove a single-choice tag that you applied to a review set item. You can only change a single-choice tag to another single-choice tag within the same tag group.

To remove a tag:

1. Select the items that you want to remove the tag from.
2. Select **Tag files** to display the tagging panel.
3. Under **Assign tags**, clear the tag, then select **Apply tags**.

You can also use the previous procedure to change the tag applied to selected items. After clearing the current tag, you can select a different one.