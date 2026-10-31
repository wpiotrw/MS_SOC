---
layout: Conceptual
title: Get started with sensitivity labels | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-04-16T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- highpri
- SPO_Content
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MOE150
- MET150
description: Prescriptive steps for admins, licensing requirements, and common scenarios that use sensitivity labels to help protect your organization's data.
locale: en-us
document_id: 992f56b8-4ca9-57ed-e651-38ca779ce082
document_version_independent_id: 992f56b8-4ca9-57ed-e651-38ca779ce082
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/get-started-with-sensitivity-labels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: get-started-with-sensitivity-labels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/get-started-with-sensitivity-labels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6bd23cb0-e7f1-b57a-542a-ca7bd53e6ed1
---

# Get started with sensitivity labels | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

For information about what sensitivity labels are and how they can help you protect your organization's data, see [Learn about sensitivity labels](sensitivity-labels).

When you're ready to start protecting your organization's data by using sensitivity labels:

1. **Create the labels.** Create and name your sensitivity labels according to your organization's classification taxonomy for different sensitivity levels of content. Use common names or terms that make sense to your users. If you don't already have an established taxonomy, consider starting with label names such as Personal, Public, General, Confidential, and Highly Confidential. You can then use sublabels to group similar labels by category.

    For each label, specify a tooltip to help users select the appropriate label and consider including specific examples. However, don't make the tooltip so long that users won't read it, and be aware that some apps might truncate long tooltips.

    Note

    For some recommended examples, see the label names and descriptions for the [default sensitivity labels](default-sensitivity-labels-policies#default-sensitivity-labels). For more guidance about defining a classification taxonomy, see [Data classification & sensitivity label taxonomy](/en-us/compliance/assurance/assurance-data-classification-and-labels).

    Always test and tailor your sensitivity label names and tooltips with the people who need to apply them.
2. **Define what each label can do.** Configure the protection settings you want associated with each label. For example, you might want lower sensitivity content (such as a "General" label) to have just a header or footer applied, while higher sensitivity content (such as a "Confidential" label) should have a watermark and encryption.
3. **Publish the labels.** After your sensitivity labels are configured, publish them by using a label policy. Decide which users and groups should have the labels and what policy settings to use. A single label is reusable—you define it once, and then you can include it in several label policies assigned to different users. So for example, you could pilot your sensitivity labels by assigning a label policy to just a few users. Then when you're ready to roll out the labels across your organization, you can create a new label policy for your labels and this time, specify all users.

Tip

You might be eligible for the automatic creation of default labels and a default label policy that takes care of steps 1-3 for you. For more information, see [Default labels and policies for Microsoft Purview Information Protection](default-sensitivity-labels-policies).

The basic flow for deploying and applying sensitivity labels is summarized in the following diagram. It identifies the roles and actions of admins, end users, and then Office or third-party apps or services that respectively create labels, apply them, and enforce the label settings.

![Flowchart explaining the sensitivity label flow: First, admins create and publish sensitivity labels to users and groups. Then, end users apply labels to emails and documents. Finally, Office or third-party apps/services enforce protection based on the applied labels.](media/sensitivity-label-flow.png)

## Licensing and billing requirements for sensitivity labels

A number of different per-user subscriptions support sensitivity labels for Microsoft 365 apps and services, and the licensing requirements for users depend on the features you use. Admins also need a license to manage sensitivity labels.

To see the options for licensing your users to benefit from Microsoft Purview features, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). For sensitivity labels, see the [Microsoft Purview Information Protection sensitivity labeling](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling) section and related [PDF download](https://go.microsoft.com/fwlink/?linkid=2139145) for feature-level licensing requirements.

Specific to non-Microsoft 365 data sources, applying sensitivity labels in the Data Map and using protection policies requires you to set up [pay-as-you-go billing](purview-billing-models) in your organization.

Tip

Because features for this solutions use pay-as-you-go billing or per-user licensing for Microsoft Purview, you might find it helpful to use the **Usage center** to help you understand and manage your usage. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage).

## Permissions required to create and manage sensitivity labels

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Members of your compliance team who will create and sensitivity labels need permissions to the [Microsoft Purview portal](purview-portal). You can use the following role groups:

- **Information Protection**
- **Information Protection Admins**
- **Information Protection Analysts**
- **Information Protection Investigators**
- **Information Protection Readers**

For an explanation of each one, and the roles that they contain, select a role group in the Microsoft Purview portal, and then review the description in the flyout pane. Or, see [Role groups in Microsoft Defender for Office 365 and Microsoft Purview compliance](/en-us/microsoft-365/security/office-365-security/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance).

Alternatively to using the default role groups, you can create a new role group and add the **Sensitivity Label Administrator** role to this group. For a read-only role, use **Sensitivity Label Reader**.

Another option is to add users to the **Compliance Data Administrator**, **Compliance Administrator**, or **Security Administrator** role group.

For configuration instructions, see [Permissions in the Microsoft Purview portal](purview-permissions).

These permissions are required only to create and configure sensitivity labels and their label policies. They are not required to apply the labels in apps or services. If additional permissions are needed for specific configurations that relate to sensitivity labels, those permissions will be listed in their respective documentation instructions.

## Support for administrative units

Sensitivity labels support [administrative units that have been configured in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units):

- You can assign administrative units to members of role groups that are used with Microsoft Purview Information Protection. Edit these role groups and select individual members, and then the **Assign admin units** option to select administrative units from Microsoft Entra ID. These administrators are now restricted to managing just the users in those administrative units.
- You can define the initial scope of sensitivity label policies and auto-labeling policies when you create or edit these policies. When you select administrative units for Exchange and OneDrive, only the users in those administrative units will be eligible for the policy. When you select administrative units for SharePoint, only the sites in those administrative units will be eligible for the policy.
- [Protection policies](create-sensitivity-labels#create-and-configure-protection-policies) don't support administrative units.

The configuration of administrative units and the accuracy of their membership is a Microsoft Entra ID dependency. Although the main purpose of administrative units is to ensure the security best practice of least privileges, using administrative units for your labeling policies can simplify their configuration and maintenance.

For example, your organization has configured administrative units for specific countries, and you need to publish a new sensitivity label just to users in France and assign specific policy settings to these users:

1. You sign in to the Microsoft Purview portal. Your account is a member of the **Information Protection Admins** role group, and your account in that role group has been assigned administrative units for France, Germany, and Spain.
2. When you create the sensitivity label policy, you see just three administrative units and select the one for France, keeping the default of all users and groups.

    This configuration automatically scopes the policy to all users in France. You don't need to worry about which groups to select or manually select users. You also don't need to worry about changing the policy when there are new users in France, because this change is handled by the administrative unit in Microsoft Entra.

For more information about how Microsoft Purview supports administrative units, see [Administrative units](purview-admin-units#permissions-for-administrative-units).

## Deployment strategy for sensitivity labels

A successful strategy to deploy sensitivity labels for an organization is to create a working virtual team that identifies and manages the business and technical requirements, proof of concept testing, internal checkpoints and approvals, and final deployment for the production environment.

Using the table in the next section, we recommend identifying your top one or two scenarios that map to your most impactful business requirements. After these scenarios are deployed, return to the list to identify the next one or two priorities for deployment.

Tip

To help accelerate your deployment, use the **Overview** page from **Information Protection** in the [Microsoft Purview portal](https://purview.microsoft.com/informationprotection/overview) to see labeling recommendations and reports specific to your organization, and more.

## Common scenarios for sensitivity labels

All scenarios require you to [Create and configure sensitivity labels and their policies](create-sensitivity-labels).

| I want to ... | Documentation |
| --- | --- |
| Manage sensitivity labels for Office apps so that content is labeled as it's created—includes support for manual labeling on all platforms | [Manage sensitivity labels in Office apps](sensitivity-labels-office-apps) |
| Extend labeling to Windows File Explorer and PowerShell | [Extend sensitivity labeling on Windows](information-protection-client) |
| Encrypt documents and emails with sensitivity labels and restrict who can access that content and how it can be used | [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels) |
| Ensure that documents from SharePoint sites retain their current permissions when files are downloaded, and protect them against move and copy | [Configure SharePoint with a sensitivity label to extend permissions to downloaded documents](sensitivity-labels-sharepoint-extend-permissions) |
| Protect Teams meetings, from meeting invites and responses, to protecting the meeting itself and related chat | [Use sensitivity labels to protect calendar items, Teams meetings and chat](sensitivity-labels-meetings) |
| Protect Teams voicemail messages | [Enable protected voicemail in your organization](/en-us/microsoftteams/set-up-phone-system-voicemail#enable-protected-voicemail-in-your-organization) |
| Enable sensitivity labels for Office for the web, with support for coauthoring, eDiscovery, data loss prevention, search—even when documents are encrypted | [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files) |
| Use sensitivity labels with Microsoft Loop to protect Loop content | [Use sensitivity labels with Microsoft Loop](sensitivity-labels-loop) |
| Files in SharePoint to be automatically labeled with a default sensitivity label | [Configure a default sensitivity label for a SharePoint document library](sensitivity-labels-sharepoint-default-label) |
| Use co-authoring and AutoSave in Office desktop apps when documents are encrypted | [Enable co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring) |
| Automatically apply sensitivity labels to documents and emails | [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically) |
| Use sensitivity labels to protect content in Teams, SharePoint, Viva Engage, and Loop | [Use sensitivity labels with containers (groups and sites)](sensitivity-labels-teams-groups-sites) |
| Use sensitivity labels to configure the default sharing link type for sites and individual documents in SharePoint and OneDrive | [Use sensitivity labels to set the default sharing link for sites and documents in SharePoint and OneDrive](sensitivity-labels-default-sharing-link) |
| Apply a sensitivity label to a document understanding model, so that identified documents in a SharePoint library are automatically classified and protected | [Apply a sensitivity label to a model in Microsoft Syntex](/en-us/microsoft-365/contentunderstanding/apply-a-sensitivity-label-to-a-model) |
| Prevent or warn users about sharing files or emails with a specific sensitivity label | [Use sensitivity labels as conditions in DLP policies](dlp-sensitivity-label-as-condition) |
| Apply a sensitivity label to a file when I receive an alert that content containing personal data is being shared and needs protection | [Investigate and remediate alerts in Privacy Risk Management](/en-us/privacy/priva/risk-management-alerts) |
| Apply a retention label to retain or delete files or emails that have a specific sensitivity label | [Automatically apply a retention label to retain or delete content](apply-retention-labels-automatically) |
| Discover, label, and protect files stored in data stores that are on premises | [Deploying the information protection scanner to automatically classify and protect files](deploy-scanner) |
| Discover, label, and protect files stored in data stores that are in the cloud | [Discover, classify, label, and protect regulated and sensitive data stored in the cloud](/en-us/cloud-app-security/best-practices#discover-classify-label-and-protect-regulated-and-sensitive-data-stored-in-the-cloud) |
| Label SQL database columns by using the same sensitivity labels as those used for files and emails so that the organization has a unified labeling solution that can continue to protect this structured data when it's exported | [Data Discovery & Classification for Azure SQL Database, Azure SQL Managed Instance, and Azure Synapse Analytics](/en-us/azure/azure-sql/database/data-discovery-and-classification-overview)[SQL Data Discovery and Classification for SQL Server on-premises](/en-us/sql/relational-databases/security/sql-data-discovery-and-classification) |
| Apply and view labels in Power BI, and protect data when it's saved outside the service | [Sensitivity labels in Power BI](/en-us/power-bi/admin/service-security-sensitivity-label-overview) |
| Label items in Microsoft Fabric, to restrict access and grant read-only or full control permissions to users | [Create and manage protection policies for Fabric](/en-us/fabric/governance/protection-policies-create) |
| Monitor and understand how sensitivity labels are being used in my organization | [Reports overview](purview-reports) Additionally, view the [information protection reports from the Microsoft Purview portal](https://purview.microsoft.com/informationprotection/purviewmipreports) |
| Audit sensitivity labeling in my organization | [Audit log activities - Sensitivity label activities](audit-log-activities#sensitivity-label-activities) |
| Identify content for eDiscovery cases based on applied sensitivity labels, such as Confidential and Highly Confidential | [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder) |
| Extend sensitivity labels to third-party apps and services | [Microsoft Information Protection SDK](/en-us/information-protection/develop/overview#microsoft-information-protection-sdk) |
| Extend sensitivity labels across content in my Microsoft Purview Data Map assets, such as Azure Blob Storage, Azure Files, Azure Data Lake Storage, and multi-cloud data sources | [Labeling in Microsoft Purview Data Map](data-map-sensitivity-labels) |

## End-user documentation for sensitivity labels

The most effective end-user documentation will be customized guidance and instructions you provide for the label names and configurations you choose. You can use the label policy setting **Provide users with a link to a custom help page** to specify an internal link for this documentation.

In Office apps, users can then easily access your customized help from the **Sensitivity** button, **Learn More** menu option. If you don't specify a link in the policy setting, users don't see this menu option in their apps.

From the Microsoft Purview Information Protection file labler in Windows File Explorer, users can access the same customized help from **Help and Feedback** &gt; **Tell Me More** in the file labeler dialog box.

You can use the following resources for basic instructions:

- [Apply sensitivity labels to your files](https://support.microsoft.com/en-us/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9)

    - [Custom permissions for files](https://support.microsoft.com/office/custom-permissions-for-files-5ffed537-ec78-4346-b68b-007209ae9e25)
- [Apply sensitivity labels to email messages in Outlook](https://support.microsoft.com/office/apply-sensitivity-labels-to-email-messages-in-outlook-ba9918f4-aace-42dc-8f0a-27d830de6eef)
- [Known issues with sensitivity labels in Office](https://support.microsoft.com/en-us/office/known-issues-with-sensitivity-labels-in-office-b169d687-2bbd-4e21-a440-7da1b2743edc)
- [Automatically apply or recommend sensitivity labels to your files and emails in Office](https://support.office.com/article/automatically-apply-or-recommend-sensitivity-labels-to-your-files-and-emails-in-office-622e0d9c-f38c-470a-bcdb-9e90b24d71a1)

    - [Known issues with automatically applying or recommending sensitivity labels](https://support.office.com/article/known-issues-with-automatically-applying-or-recommending-sensitivity-labels-451698ae-311b-4d28-83aa-a839a66f6efc)
- [Create protected PDFs from Office files](https://support.microsoft.com/topic/aba7e367-e482-49e7-b746-a385e48d01e4)
- [Sensitivity labels for Teams meetings](https://support.microsoft.com/office/sensitivity-labels-for-teams-meetings-2b244d1d-72d0-471e-8e58-c41079e190fb)
- [Apply sensitivity labels to your Outlook meetings](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-outlook-meetings-f3c960aa-e094-4447-9c88-6fd7c4b4d33c).
- [Sensitivity labels in Viva Engage](/en-us/viva/engage/manage-engage-communities/community-sensitivity-labeling)
- [Label and protect files in File Explorer in Windows](https://support.microsoft.com/topic/label-and-protect-files-in-file-explorer-in-windows-67829155-2d0e-4122-9677-7c53c8cba18a)

If your sensitivity labels apply encryption for PDF documents, these documents can be opened with Microsoft Edge on Windows or Mac. For more information, see [View protected PDFs using Microsoft Edge on Windows or Mac](https://support.microsoft.com/topic/view-protected-pdfs-using-microsoft-edge-on-windows-or-mac-643c3dbe-c4ed-477c-9acb-078398a7e2b5).