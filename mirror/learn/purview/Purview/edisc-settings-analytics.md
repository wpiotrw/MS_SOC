---
layout: Conceptual
title: Configure analytics settings in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-analytics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure the attorney-client privilege detection setting in eDiscovery organization settings in the Microsoft Purview portal.
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
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: dda49f43-d80a-63a9-536d-ee4c344a1551
document_version_independent_id: dda49f43-d80a-63a9-536d-ee4c344a1551
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 34ea131c-cdfd-c080-1d9d-c7de3bb55356
---

# Configure analytics settings in eDiscovery | Microsoft Learn

This article explains how to configure organization-level analytics settings for eDiscovery in the Microsoft Purview portal. eDiscovery administrators can use these settings to enable machine learning-based detection of privileged content across all eDiscovery cases in the organization.

Note

The **Attorney-client privilege detection** feature is the only analytics setting currently available in eDiscovery organization settings. You configure additional case level search and analytics settings in the case settings for individual cases.

## Configure attorney-client privilege detection

A major and costly aspect of the review phase of any eDiscovery process is reviewing documents for privileged content. eDiscovery provides machine learning-based detection of privileged content to make this process more efficient. This feature is called *attorney-client privilege detection*.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

### How attorney-client privilege detection works

When you enable attorney-client privilege detection, the model processes all documents in a review set when you [analyze the data](edisc-review-set-analytics) in the review set. The model looks for two things:

- **Privileged content**: The model uses machine learning to determine the likelihood that the document contains content that is legal in nature.
- **Participants**: As part of setting up attorney-client privilege detection, you submit a list of attorneys for your organization. The model then compares the participants of the document with the attorney list to determine if a document has at least one attorney participant.

The model produces the following three properties for every document:

- **AttorneyClientPrivilegeScore**: The likelihood the document is legal in nature; the values for the score are between *0* and *1*.
- **HasAttorney**: This property is set to *true* if one of the document participants is listed in the attorney list; otherwise the value is *false*. The value is also set to *false* if your organization didn't upload an attorney list.
- **IsPrivilege**: This property is set to *true* if the value for **AttorneyClientPrivilegeScore** is over the threshold *or* if the document has an attorney participant; otherwise the value is set to *false*.

These properties (and their corresponding values) are added to the file metadata of the documents in a review set and are searchable within a review set:

![Screenshot of file metadata showing attorney-client privilege properties, including AttorneyClientPrivilegeScore, HasAttorney, and IsPrivilege values.](media/aedattorneyclientprivilegemetadata.png)

### Set up the attorney-client privilege detection model

To enable the attorney-client privilege detection model, your organization needs to turn it on and (optionally) upload an attorney list.

#### Step 1: Turn on attorney-client privilege detection

An eDiscovery Administrator in your organization (a member of the eDiscovery Administrator subgroup in the eDiscovery Manager role group) must make the model available in your eDiscovery cases.

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Settings** &gt; **eDiscovery** &gt; **Analytics**.
2. Toggle **Attorney-client privilege detection** to *On*.
3. Select **Save** to save the change.

#### Step 2: Upload a list of attorneys (optional)

To take full advantage of the attorney-client privilege detection model and use the results of the **Has Attorney** or **Potentially Privileged** detection, upload a list of email addresses for the lawyers and legal personnel who work for your organization.

To upload an attorney list for the attorney-client privilege detection model:

1. Create a .csv file (without a header row) and add the email address for each appropriate person on a separate line. Save this file to your local computer.
2. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Settings** &gt; **eDiscovery** &gt; **Analytics**.
3. Select **Choose file**, then find and select the .csv file that you created in step 1.
4. Select **Save** to upload the attorney list.

### Use the attorney-client privilege detection model

Complete the following steps to use attorney-client privilege detection for documents in a review set.

#### Step 1: Create a smart tag group with attorney-client privilege detection model

One of the primary ways to see the results of attorney-client privilege detection in your review process is by using a smart tag group. A smart tag group shows the results of the attorney-client privilege detection in-line next to the tags. This setup lets you quickly identify potentially privileged documents during document review. You can also use the tags in the smart tag group to tag documents as privileged or nonprivileged. For more information about smart tags, see [Set up smart tags](edisc-review-set-tagging#set-up-smart-tags).

1. In the review set that contains documents you previously analyzed, select **Manage review set** and then select **Manage tags**.
2. Under **Tags**, select the pull-down next to **Add group** and then select **Add smart tag group**.
3. On the **Choose a model for your smart tag** page, select **Select** next to **Attorney-client privilege**.

    A tag group named **Attorney-client privilege** appears. It contains two child tags named **Positive** and **Negative**, which correspond to the possible results produced by the model.
4. Rename the tag group and tags as appropriate for your review. For example, you can rename **Positive** to **Privileged** and **Negative** to **Not privileged**.

#### Step 2: Analyze a review set

When you analyze the documents in a review set, the attorney-client privilege detection model also runs and adds the **AttorneyClientPrivilegeScore**, **HasAttorney**, and **IsPrivilege** properties (described in How attorney-client privilege detection works) to every document in the review set. For more information about analyzing data in review set, see [Analyze data in a review set in eDiscovery](edisc-review-set-analytics).

#### Step 3: Use the smart tag group for review of privileged content

After analyzing the review set and setting up smart tags, the next step is to review the documents. If the model determines the document is potentially privileged, the corresponding smart tag in the **Tagging panel** indicates the following results produced by the attorney-client privilege detection:

- If the document has content that might be legal in nature, the label **Legal content** appears next to the corresponding smart tag (which in this case is the default **Positive** tag).
- If the document has a participant who is found in your organization's attorney list, the label **Attorney** appears next to the corresponding smart tag (which in this case is also the default **Positive** tag).
- If the document has content that might be legal in nature *and* has a participant found in the attorney list, both the **Legal content** and **Attorney** labels appear.

If the model determines that a document doesn't contain content that is legal in nature or doesn't contain a participant from the attorney list, then neither label appears in the tagging panel.

After you review a document to see if it contains privileged content, you can tag the document with the appropriate tag.