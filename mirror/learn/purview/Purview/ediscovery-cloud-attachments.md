---
layout: Conceptual
title: Collect cloud attachments in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-cloud-attachments
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use collections in Microsoft Purview eDiscovery (Premium) to collect cloud attachments for review in an investigation or case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.reviewer: nickrob
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: be643c1a-230f-f24e-ecbc-fbffda318d81
document_version_independent_id: be643c1a-230f-f24e-ecbc-fbffda318d81
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-cloud-attachments.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-cloud-attachments
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-cloud-attachments.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: d85c345b-bb01-9f1c-b140-149e47972a0a
---

# Collect cloud attachments in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Cloud attachments are links to documents that are typically stored in SharePoint site and OneDrive. So instead of attaching an actual copy of a document in an email message or a Teams chat conversation, you have the option of sharing a link to the file. Cloud attachments are an effective way to share documents and collaborate with other people in your organization. But cloud attachments present challenges during the eDiscovery workflow because only the cloud attachment link and not the actual content in the shared document are returned in an eDiscovery search. To address this challenge, eDiscovery (Premium) provides two solutions for collecting cloud attachments:

- Collecting the live version of a document that is linked to in a cloud attachment.
- Collecting the version of the document at the time it was shared in a cloud attachment.

## Collecting cloud attachments

When you create a collection estimate and the search results contain items that include cloud attachments, you have to the option of collecting the target of the cloud attachment when you commit the collection estimate to a review set. When you select this option, eDiscovery (Premium) adds the documents that are linked to in the cloud attachment to the review set. This option allows you to review the target documents and determine if the document is relevant to your case or investigation.

The following screenshot shows the option to include the targets of cloud attachments when you commit a collection to a review set.

![The option to include cloud attachments when committing a collection to a review set](media/collectcloudattachments1.png)

Note

You have the option to include all versions (in addition to the version that was shared) of cloud attachments in the review set.

When working with collections and cloud attachments, the following applies:

- Cloud attachments aren't represented or included in collection estimates. Only direct hits are included in a collection.
- If cloud attachments are moved or no longer available at the location from where it was shared, it isn't included in a collection.
- If the cloud attachment is under retention of legal hold policy, the cloud attachment is included in collections even if deleted by a user.
- For cloud attachments that have been renamed or moved to a different container, it may or may not be included in a collection depending on how it was shared. If the cloud attachment was shared via a link and the link is still active, it's retrieved and included in the collection. If the sharing link to the location for the cloud attachment isn't available, the cloud attachment isn't retrieved or included in the collection.
- For cloud attachments with parent items placed on hold, the hold applies to cloud attachment in certain situations. This depends on the source location of the cloud attachment and the hold policy applied to that location. The policies applicable to the cloud attachment recipient won't necessarily apply to the location of the shared cloud attachment.

For instructions committing a collection to a review set, see [Commit a collection estimate to a review set](ediscovery-commit-draft-collection).

## Collecting the version shared in a cloud attachment (preview)

The eDiscovery (Premium) workflow for collecting cloud attachments only includes adding the most current version of a cloud attachment to a review set. This means the version that's collected and added to a review set could be different than the version that was originally shared in the cloud attachment. So it's possible that content that was present in the cloud attachment at the time it was shared might have been removed and doesn't exist in the current version that's added to the review set.

Organizations can use Microsoft Purview retention labels to preserve the version of a document at the time when it was shared as a cloud attachment. To do this, your organization can create a retention label, choose the option apply the label to cloud attachments, and then automatically apply the label to documents stored in SharePoint and OneDrive. After you set up this configuration, a copy of a document is created at the time when the file is shared. Also, if the document is modified and shared again as a cloud attachment, the modified version is also preserved. If the file is modified and shared again, a new copy of the file as a new version is preserved.

Preserving the shared versions of cloud attachments can help your organization scope the preservation and collection of potentially relevant content to the specific version of the document that was shared rather than the current live version. After you implement this retention solution, both the current live version of a cloud attachment and the version that was shared in the cloud attachment are collected and added to a review set.

For instructions on setting up a retention label and automatically applying it to cloud attachments, see [Auto-apply labels to cloud attachments](apply-retention-labels-automatically#auto-apply-labels-to-cloud-attachments).

The following screenshot shows a cloud attachment document, named *XYZ Research.docx*, that was added to a review set. The document was shared as a cloud attachment in a Teams chat conversation. The review set also contains the version that was originally shared in the cloud attachment. Notice the name of this version of the cloud attachment is generated by the system and the author is identified as **SharePoint**.

![The version of a cloud attachment that was shared displayed in a review set](media/collectcloudattachments2.png)

Additionally, the current live version and the version that was shared have the same **FamilyId** property value, which is the same as the **FamilyId** for the parent object (such as an email message or a Teams chat conversation). This lets you group cloud attachments with the item in which they were shared.

After you've implemented the retention label and auto-apply the label to SharePoint documents, you still select the option to collect cloud attachments when committing a collection estimate to a review set. When the cloud attachments are collected, both the current live version and the version that was originally shared are added to the review set.