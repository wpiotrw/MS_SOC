---
layout: Conceptual
title: Use record versioning in SharePoint or OneDrive | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/record-versioning
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-03-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Learn about records to help you implement a records management solution in Microsoft 365.
ms.custom: sfi-image-nochange
locale: en-us
document_id: ee69f33b-a703-9675-5281-8305ec389d09
document_version_independent_id: ee69f33b-a703-9675-5281-8305ec389d09
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/record-versioning.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: record-versioning
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/record-versioning.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6c3507a7-573f-491d-0659-b32474d9b4ce
---

# Use record versioning in SharePoint or OneDrive | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

Because regulatory records block editing, record versioning is not available for regulatory records.

You can also prevent record versioning for your tenant, even if you're not using regulatory records. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Settings**&gt; **Records Management** &gt; **Retention Labels** &gt; **Configure record versioning** and then for **Configure record versioning**, turn off the setting for **Enable record versioning**.

The ability to mark a document as a [record](records-management#records) and restrict actions that can be performed on the record is an essential goal for any records management solution. However, collaboration might also be needed for people to create subsequent versions.

For example, you might mark a sales contract as a record, but then need to update the contract with new terms and mark the latest version as a new record while still retaining the previous record version. For these types of scenarios, SharePoint and OneDrive support *record versioning*. OneNote notebook folders don't support record versioning.

To use record versioning, you first label the document with a [retention label that's configured to mark items as a record](declare-records). At this point, a document property, called *Record status* is displayed next to the retention label. Depending on whether the label is configured to unlock the record by default, the initial record status is either **Locked** or **Unlocked**.

You can now do the following things:

- **Continually edit and retain individual versions of the document as records, by unlocking and locking the Record status property.** Only when the **Record status** property is set to **Locked** is a new version of the record retained. This toggle of locked and unlocked reduces the risk of retaining unnecessary versions and copies of the document.

    Note

    If the label is configured to unlock the record by default, but versioning is not enabled by the admin, or prevented by the records management setting, users will not be able to unlock the document after they lock it.
- **Have the records automatically stored in an in-place records repository located with the site.** Each site in SharePoint and OneDrive preserves content in its Preservation Hold library. Record versions are stored in the Records folder in this library as individual files. For more information about how the Preservation Hold library works, see [How retention works for SharePoint and OneDrive](retention-policies-sharepoint#how-retention-works-for-sharepoint-and-onedrive).
- **Maintain an evergreen document that contains all versions.** By default, each SharePoint and OneDrive document has a version history available on the item menu. In this version history, you can easily see which versions are records and view those documents.

Tip

When you use record versioning with a retention label that has a delete action, consider configuring the retention setting **Start the retention period based on:** to be **When items were labeled**. With this label setting, the start of the retention period is reset for each new record version, which ensures that older versions will be deleted before newer versions.

If the retention label is configured for [disposition review](disposition) at the end of the retention period, each version undergoes its own disposition review.

By default, record versioning is automatically available for any document that has a retention label applied that marks the item as a record, and that label is [published to the site](create-apply-retention-labels). When a user views the document properties by using the details pane, they can toggle the **Record status** between **Locked** and **Unlocked**. A padlock icon might also be displayed for the document, to help identify when the file is locked.

While the document is unlocked, any user with standard edit permissions can edit the file. However, users can't delete the file, because it's still a record. When editing is complete, a user can then toggle the **Record status** from **Unlocked** to **Locked**, which prevents further edits while in this status. 

[![Record status property on document tagged as a record.](media/recordversioning8.png)](media/recordversioning8.png#lightbox)

For more information about what user actions are allowed when a record is locked or unlocked, see [Compare restrictions for what actions are allowed or blocked](records-management#compare-restrictions-for-what-actions-are-allowed-or-blocked).

## Locking and unlocking a record

After a retention label that marks content as a record is applied to a document, any user with Contribute permissions or a narrower permission level can unlock a record or lock an unlocked record. 

[![Record status shows record document is unlocked.](media/recordversioning9.png)](media/recordversioning9.png#lightbox)

When a record is unlocked, the following actions occur:

1. If the current site doesn't have a Preservation Hold library, one is created.
2. If the Preservation Hold library doesn't have a Records folder, one is created.
3. A **Copy to** action copies the latest version of the document to the Records folder. The **Copy to** action includes only the latest version and no prior versions. This copied document is now considered a record version of the document, and its file name has the format: [Title GUID Version#]
4. The copy created in the Records folder is added to the version history of the original document, and this version shows the word **Record** in the comments field.
5. The original document is a new version that can be edited, but not deleted. The document library column **Item is a Record** still shows the **Yes** value because the document is still a record, even if it can now be edited.

When a user locks a record, the original document again can't be edited. But it is the action of unlocking a record that copies a version to the Records folder in the Preservation Hold library.

## Record versions

Each time a record is unlocked, the latest version is copied to the Preservation Hold library, and that version contains the value of **Record** in the **Comments** field of the version history. 

[![Record shown in the Preservation Hold library.](media/recordversioning10.png)](media/recordversioning10.png#lightbox)

To view the version history, select a document in the document library and then click **Version history** in the item menu.

## Searching the audit log for record versioning events

The actions of locking and unlocking records are logged in the audit log. From **File and page activities**, select **Changed record status to locked** and **Changed record status to unlocked**.

For more information about searching for these events, see [Audit log activities](audit-log-activities).