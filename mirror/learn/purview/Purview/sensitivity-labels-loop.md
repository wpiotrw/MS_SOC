---
layout: Conceptual
title: Use sensitivity labels with Microsoft Loop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sensitivity-labels-loop
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
ms.reviewer: taminecm
manager: laurawi
audience: Admin
ms.topic: article
ms.date: 2026-03-31T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Learn how Microsoft Loop supports sensitivity labels to protect Loop components, pages, and workspaces.
locale: en-us
document_id: e75745bc-e0f0-16f1-84ee-66100f2e0a63
document_version_independent_id: e75745bc-e0f0-16f1-84ee-66100f2e0a63
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sensitivity-labels-loop.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sensitivity-labels-loop
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sensitivity-labels-loop.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/0850fefd-e402-4507-ae98-46cfdfc2e16c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/6ecf98a5-97c7-4249-b209-a9d9e42633a0
platformId: 0facc739-c58b-2295-b531-530c0182d116
---

# Use sensitivity labels with Microsoft Loop | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use your [sensitivity labels](sensitivity-labels) with Microsoft Loop to add an extra layer of protection to the Loop-related data that users create with this app. This protection [extends to Microsoft 365 Copilot](ai-microsoft-purview#microsoft-purview-strengthens-information-protection-for-ai-apps).

Loop supports sensitivity labels at the file level, to help protect components and pages:

- Users can manually apply sensitivity labels that are published to them with the **Files & other data assets** label scope, including sensitivity labels that apply encryption configured to [apply permissions now](encryption-sensitivity-labels#assign-permissions-now).
- Watermarks as a label setting are supported but not variables in the text string.
- Mandatory labeling and a default document label are supported as settings from a label publishing policy.
- Other policy settings supported:
    - Justification to remove a label or lower its priority
    - The "Learn more" link

Example Loop component that's currently labeled with the **Confidential** \ **All Employees** sensitivity label that applies encryption, displaying other available labels:

![Microsoft Loop component displaying sensitivity labels to protect the data in the component.](media/labeled-loop-component.png)

Loop supports sensitivity labels at the container level, to help protect access to workspaces:

- This functionality is supported for tenant-owned workspaces on the web version of the Loop app.
- You can apply a sensitivity label when you create a new workspace, or apply or change a sensitivity label as a More (**...**) workspace configuration.
- Using the SharePoint admin center with the [SharePoint Embedded administrator role](/en-us/sharepoint/dev/embedded/concepts/admin-exp/adminrole), you can see and change applied sensitivity labels from **Containers** &gt; **Active containers**.

![Microsoft Loop workspace creation displaying sensitivity labels to protect access to the data in the workspace.](media/label-loop-workspace.png)

See the following sections for more details about requirements, supported scenarios, and limitations when you use sensitivity labels with Loop.

For information where Loop-related content is stored, see [Overview of Loop storage](/en-us/microsoft-365/loop/loop-storage).

## Sensitivity labels to protect Loop components and pages

The ability to apply sensitivity labels to Loop components and pages requires that [SharePoint and OneDrive is enabled for sensitivity labels](sensitivity-labels-sharepoint-onedrive-files#how-to-enable-sensitivity-labels-for-sharepoint-and-onedrive-opt-in). Then, you can apply sensitivity labels to loop components and pages in the following apps:

- The [Loop app](https://support.microsoft.com/en-us/office/get-started-with-microsoft-loop-9f4d8d4f-dfc6-4518-9ef6-069408c21f0c) (web and mobile)
- Loop in Outlook (desktop, mobile, web)
- Microsoft 365 Copilot Chat in Microsoft Copilot Pages

When Loop components and pages are encrypted by sensitivity labels, [Microsoft 365 Copilot honors the EXTRACT usage right](ai-microsoft-purview-considerations#copilot-honors-existing-protection-with-the-extract-usage-right). Microsoft 365 Copilot won't summarize this Loop data unless the user is granted this usage right.

As with sensitivity labels that are applied to documents in SharePoint and OneDrive, the following [auditing events](sensitivity-labels-office-apps#auditing-labeling-activities) are supported:

- **Applied sensitivity label to file**
- **Changed sensitivity label applied to file**
- **Removed sensitivity label from file**

### Sensitivity label inheritance for components and pages

Any unlabeled Loop components on the page inherit the sensitivity label applied to the page. That label is retained if you move it to another Loop page.

A Loop page can inherit a [higher priority sensitivity label](sensitivity-labels#label-priority-order-matters) from Copilot in the Loop app when referenced files are labeled. If more than one file is referenced and labeled, the page inherits the label with the highest priority.

### Limitations for Loop components and pages

The following labeling capabilities aren't supported:

- Label names and descriptions for [other languages](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell)
- Headers and footers
- Variables in watermarks and dynamic watermarks
- Automatic and recommended labeling
- Sensitivity labels that are configured for any of the following [encryption settings](encryption-sensitivity-labels#configure-encryption-settings):
    - **Let users assign permissions**, sometimes known as "user-defined permissions"
    - **User access to content expires** is set to a value other than **Never**
    - **Double Key Encryption** is selected

Because the task management tools in Microsoft Planner and Microsoft To Do don't support encryption, they stop synchronizing a Loop component or page that's encrypted by a sensitivity label.

## Sensitivity labels to protect Loop workspaces

The ability to apply sensitivity labels to Loop workspaces at the tenant-level requires that [sensitivity labels are enabled for containers](sensitivity-labels-teams-groups-sites#how-to-enable-sensitivity-labels-for-containers-and-synchronize-labels) and that the label scope includes **Groups & sites**. Then, you can apply sensitivity labels to Loop workspaces in the Loop web app so that content in those workspaces is protected by the following label settings documented in [Use sensitivity labels to protect collaborative workspaces (groups and sites)](sensitivity-labels-teams-groups-sites):

- External user access
- External sharing from SharePoint sites
- Access from unmanaged devices
- Authentication contexts
- Default sharing link for a SharePoint site (PowerShell-only configuration)
- Site sharing settings (PowerShell-only configuration)

Although Loop workspaces are stored in SharePoint Embedded containers rather than SharePoint sites, the listed sensitivity label settings for sites are functionally the same.

### Limitations for Loop workspaces

As with sensitivity labels that you apply to Loop components and pages, sensitivity labels for Loop workspaces don't support label colors or label names and descriptions for [other languages](create-sensitivity-labels#additional-label-settings-with-security--compliance-powershell).

The following Loop content isn't protected by the container label settings:

- Linked files
- Files uploaded to a workspace because these files are stored in the user's OneDrive
- Videos that are created in a workspace because these files are stored in the user's OneDrive