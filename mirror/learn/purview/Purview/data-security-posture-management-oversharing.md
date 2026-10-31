---
layout: Conceptual
title: Prevent oversharing with data risk assessments from Microsoft Purview Data Security Posture Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: Li.Jenny
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.localizationpriority: high
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Learn how data risk assessments from Microsoft Purview Data Security Posture Management helps prevent oversharing of sensitive data.
locale: en-us
document_id: f0710c40-59fe-6c89-355b-6e2ff263be8e
document_version_independent_id: f0710c40-59fe-6c89-355b-6e2ff263be8e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-oversharing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-oversharing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-oversharing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 071bc122-937f-de6c-33e3-f3d63c9f8afa
---

# Prevent oversharing with data risk assessments from Microsoft Purview Data Security Posture Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This documentation is for the **current** version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

Most new features will be added to this version only but you can still access the previous versions and their documentation:

- [DSPM for AI (classic)](dspm-for-ai)
- [DSPM (classic)](data-security-posture-management)

Data risk assessments from [Data Security Posture Management](data-security-posture-management-learn-about) help you identify and fix potential data oversharing risks in your organization. Because of the power and speed AI can proactively surface content that might be obsolete, over-permissioned, or lack governance controls, generative AI amplifies the problem of oversharing data. Use data risk assessments to both identify and remediate issues.

You can access data risk assessments from the Microsoft Purview portal &gt; **DSPM** &gt; **Discover** &gt; **Data risk assessments**, and insights from these assessments are surfaced from the [security objective](data-security-posture-management-learn-about#data-security-objectives)**Prevent oversharing of sensitive data**.

## Default data risk assessments

For oversharing insights in SharePoint and OneDrive, use the **Microsoft 365** tab, and the **Fabric** tab for items in Fabric workspaces.

# [Microsoft 365](#tab/m365)
A default data risk assessment automatically runs weekly for the top 100 SharePoint sites based on usage in your organization, and you might have already run a custom assessment as one of the recommendations. However, come back regularly to this option to check the latest weekly results of the default assessment and run custom assessments when you want to check for different users or specific sites. After a custom assessment has run, wait at least 48 hours to see the results that don't update again. You'll need a new assessment to see any changes in the results.

The **Default assessment** displays at the top of the page with a quick summary, such as the total number of items found, the number of sensitive data detected, and the number of links sharing data with anyone. The first time the default assessment is created there's a 4-day delay before results are displayed.

After you select **View details** for more in-depth information, from the list, select each site to access the flyout pane that has tabs for **Overview**, **Identify**, **Protect**, and **Monitor**. Use the information on each tab to learn more, and take recommended actions. For example:

Use the **Identify** tab to identify how much data has been scanned or not scanned for sensitive information types, with an option to initiate an [on-demand classification scan](on-demand-classification) as needed.

Use the **Protect** tab to select options to remediate oversharing, which include:

- **Restrict access by label**: Use Microsoft Purview Data Loss Prevention to create a DLP policy that prevents Microsoft 365 Copilot and agents from summarizing data when it has sensitivity labels that you select. For more information about how this works and supported scenarios, see [Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat](dlp-microsoft365-copilot-location-learn-about).
- **Restrict all items**: Use SharePoint Restricted Content Discovery to list the SharePoint sites to be exempt from Microsoft 365 Copilot. For more information, see [Restrict discovery of SharePoint sites and content](/en-us/sharepoint/restricted-content-discovery).
- **Create an auto-labeling policy**: When sensitive information is found for unlabeled files, use Microsoft Purview Information Protection to create an auto-labeling policy to automatically apply a sensitivity label for sensitive data. For more information about how to create this policy, see [How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange).
- **Create retention policies**: When content hasn't been accessed for at least 3 years, use Microsoft Purview Data Lifecycle Management to automatically delete it. For more information about how to create the retention policy, see [Create and configure retention policies](create-retention-policies).

Use the **Monitor** tab to view the number of items in the site shared with anyone, shared with everyone in the organization, shared with specific people, and shared externally. Select **Start a SharePoint site access review** for information [how to use the SharePoint data access governance reports](/en-us/sharepoint/site-access-review).

# [Fabric](#tab/fabric)
Important

Before you can see data risk assessments for Fabric, there's a one-time setup process that requires an app registered in Entra, which is a member of a security group that you specify with the Admin API settings in the Fabric admin portal. For instructions and how to specify the authentication values required to run data risk assessments for Fabric, see [Prerequisites for Fabric data risk assessments](dspm-for-ai-considerations#prerequisites-for-fabric-data-risk-assessments).

Only when these prerequisites are in place and you know the authentication values to specify, select **Set config** for Fabric data risk assessments. In the **Configure Fabric Settings** box, enter the authentication values using **Federated Credentials** (recommended, more secure) or **Client Secret**. Select **Test connection**, and if successful, select **Save**. The default assessment starts scanning.

Once set up, the default data risk assessment automatically runs weekly for the top 100 Fabric workspaces based on usage in your organization. Come back regularly to this option to check the latest weekly results of the default assessment and run custom assessments when you want to check for different users or specific workspaces. After a data risk assessment has run, wait at least 48 hours to see the results that don't update again. You'll need a new assessment to see any changes in the results.

**Supported Fabric item types for scanning**: Dashboard, Report, DataExploration, DataPipeline, KQLQuerySet, Lakehouse, Notebook, SQLAnalyticsEndpoint, and Warehouse

The **Fabric default assessment** displays at the top of the page with a quick summary that includes the sensitive information types found, the total number of items that have and don't have [sensitivity labels to protect them](/en-us/fabric/governance/information-protection), and to whom they are accessible (users, the organization, externally, and groups).

For more in-depth information, from the list, select each workspace to access the flyout pane that has tabs for **Overview**, **Protect**, and **Monitor**. Use the information on each tab to learn more about the scanned data for that workspace.

Use the **Protect** tab to see recommended actions you can take to prevent oversharing by creating a [data loss prevention (DLP) policy](dlp-powerbi-get-started) and apply a [default sensitivity label to new and edited items](/en-us/fabric/governance/sensitivity-label-default-label-policy). Examples of a DLP policy that you can configure for Fabric:

- When specific sensitive information types are found, block access to people who have this access as a result of the "Anyone with the link" option
- When specific sensitive information types are found, apply a specific sensitivity label
- When items with a specific sensitivity label are accessed, attach a policy tip to the item and register an alert in the Microsoft Purview portal

Use the **Monitor** tab to see breakdown numbers of how access is configured: Accessible to specific people, accessible externally, accessible to everybody in your organization, and accessible to a group. Choose the option to run an access review in Microsoft Entra. For more information about this option, see [What are access reviews?](/en-us/entra/id-governance/access-reviews-overview)

---

## Custom data risk assessments

To create your own custom data risk assessment, select **Create custom assessment** to identify potential oversharing issues for all or selected users, the data sources to scan, and run the assessment.

Note

Microsoft 365 custom assessments optionally support item-level scanning with remediation actions when you complete a one-time authentication process. To specify the required settings, you must have a registered Entra application. For more information about the Entra application, see [Prerequisites for Microsoft 365 item-level scanning for data risk assessments](dspm-for-ai-considerations#prerequisites-for-microsoft-365-item-level-scanning-for-data-risk-assessments).

Select **Item-level** on the **Scan level** page, and then **Authenticate** to specify the Entra application information.

This data risk assessment is created in the **Custom assessments** category. Wait for the status of your assessment to display **Completed**, and select it to view details. To rerun a custom data risk assessment, and to see results after the 30-day expiration, use the duplicate option to create a new assessment with the same selections. Item-level scanning and remediation for items that are potentially overshared is applicable to Microsoft 365 only, and currently restricted to SharePoint sites. This scan identifies items as potentially overshared if they have a sharing link for external or anonymous users, and also shows any applied sensitivity label and the owner of each item. When the scan is complete, open the custom assessment and view item-level insights from the **Potentially overshared items** tab or the **View items** button from the **Potentially overshared items** banner. The following remediation actions can be taken on the identified potentially overshared items:

- **Resolve**, for example if you decide the item isn't at risk of oversharing.
- **Apply sensitivity label** for items that are identified as currently unlabeled or should have a different sensitivity label.
- **Notify** the site owner with an email notification (not customizable).
- **Remove sharing link** to remove the existing sharing link so it can no longer be used to access the item. This is an action to be used sparingly because it could prevent people from accessing the item legitimately. In this scenario, the site owner or item owner must then set a less permissive sharing link type for authorized users. If you haven't already, consider [configuring sensitivity labels for a default sharing link](sensitivity-labels-default-sharing-link).

The email notification contains information and instructions about the potentially overshared items in the site. It also contains options for them to go to the SharePoint site to manage access to the items from there, or to the Microsoft Purview portal for a read-only view of the item-level scan results that only show items and sites that they own.

Tip

Both the default and custom data risk assessments provide an **Export** option that let you save and customize the data into a choice of file formats (Excel, CSV, JSON, TSV).

Limits for Microsoft 365:

- A maximum of 200,000 items per location, which applies to both a custom data risk assessment and a default data risk assessment. The count of files reported might not be accurate when there are more than 100,000 files per location.
- OneDrive currently isn't supported for item-level scanning.
- A current maximum of 10 SharePoint sites for item-level scanning.