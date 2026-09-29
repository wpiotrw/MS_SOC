---
layout: Conceptual
title: Microsoft Purview extensibility | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-extensibility
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about extending Microsoft Purview solutions by using third-party data connectors and Microsoft Graph APIs.
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
ms.date: 2026-02-20T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-connectors
ms.collection:
- purview-compliance
- data-connectors
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
locale: en-us
document_id: 43082dd6-bf35-36cb-64fa-e7bae33dae8b
document_version_independent_id: 43082dd6-bf35-36cb-64fa-e7bae33dae8b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-extensibility.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-extensibility
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-extensibility.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: dffac354-4ee8-4582-7f8f-2a2ec23dd12e
---

# Microsoft Purview extensibility | Microsoft Learn

Microsoft Purview solutions help organizations intelligently assess their compliance risks, govern and protect sensitive data, and effectively respond to regulatory requirements. Microsoft Purview offers many extensibility scenarios and enables organizations to adapt, extend, integrate, accelerate, and support their compliance solutions.

Three key building blocks support extensibility in Microsoft Purview:

- **Data connectors**. Use these connectors to import and archive non-Microsoft data so you can apply Microsoft 365 protection and governance capabilities to third-party data.
- **APIs**. APIs enable programmatic access to Microsoft Purview capabilities.
- **Software Developer Partner Integrations:** Microsoft Purview enables software development companies to embed advanced data security capabilities directly into their applications.

## Data connectors

Microsoft provides third-party data connectors that you can configure in the Microsoft Purview portal. For a list of data connectors provided by Microsoft, see the [Third-party data connectors](archive-third-party-data#third-party-data-connectors) table. The table of third-party data connectors also summarizes the compliance solutions that you can apply to third-party data after you import and archive data in Microsoft 365, and links to the step-by-step instructions for each connector.

### Prerequisites for data connectors

Many of the data connectors available in the Microsoft Purview portal allow you to import and archive third-party data but require you to prepare and perform configuration tasks in the third-party data source. The documentation details these prerequisites for each third-party data connector.

For data connectors in the Microsoft Purview portal or the Microsoft Purview portal provided by one of Microsoft's partners, your organization needs a business relationship with the partner before you can deploy a connector.

For guidance and requirements for third-party data connectors, see the "Data connectors" section in [Microsoft 365 guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

## APIs

Microsoft Purview and Microsoft Priva APIs are available in the [Microsoft Information Protection SDK](/en-us/information-protection/develop/overview), [Microsoft Graph API](/en-us/graph/overview), and the [Office 365 Management Activity API](/en-us/office/office-365-management-api/). Some compliance APIs are part of a new set of security and compliance APIs that enable developers for Microsoft 365 customers, independent software publishers, system integrators, and managed security service providers to build high-value security and compliance solutions.

To learn more about how to access Graph APIs, see [Overview of Microsoft Graph](/en-us/graph/overview).

### Microsoft Information Protection (MIP) SDK

The MIP SDK exposes the labeling and encryption services from the Microsoft Purview portal to third-party applications and services. Developers can use the SDK to build native support for applying labels and protection to files. Developers can determine which actions to take when specific labels are detected, and reason over MIP-encrypted information.

High-level MIP SDK use cases include:

- A line-of-business application that applies classification labels to files on export.
- A CAD/CAM design application that provides native support for sensitivity labels.
- A cloud access security broker or data loss prevention solution that can encrypt data with rights management.

For more information about the MIP SDK, prerequisites, additional scenarios, and samples, see [MIP SDK Overview](/en-us/information-protection/develop/overview).

### Microsoft Graph API for Teams DLP

[Data loss prevention (DLP)](dlp-microsoft-teams) capabilities are widely used in Microsoft Teams, particularly as organizations shift to remote work. Recently, we [announced the general availability](https://devblogs.microsoft.com/microsoft365dev/change-notifications-for-microsoft-teams-messages-now-generally-available/) of the Microsoft Graph Change Notification API for messages in Teams. This API enables developers to build apps that can listen to Microsoft Teams messages in near-real time and then implement DLP scenarios for both customers and partners. Additionally, Microsoft Graph Patch API lets you apply DLP actions to Teams messages.

These two APIs form the Microsoft Graph API for Teams DLP. You can get started by trying out the [sample app](https://github.com/microsoftgraph/aspnetcore-webhooks-sample). For more information about Microsoft Teams messaging webhooks, see the [documentation](/en-us/graph/api/subscription-post-subscriptions).

For the licensing requirements for Teams DLP, see [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

### Microsoft Graph API for eDiscovery

With [eDiscovery](edisc), organizations can discover data where it lives and manage more end-to-end eDiscovery workflows with intelligent machine learning and analytics capabilities to reduce data to the relevant set – all while the data stays within the Microsoft 365 security and compliance boundary.

You can use Graph APIs for eDiscovery to create and manage cases, review sets, and review set queries in a scalable and repeatable manner. This approach enables customers and partners to create apps and workflows to automate common and repetitive processes such as creating cases and managing custodians and legal holds.

For the licensing requirements for eDiscovery and the API, see the "eDiscovery" section in the [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#ediscovery).

### Microsoft Graph API for Teams Export

Enterprise Information Archiving (EIA) for Microsoft Teams is a key scenario for our customers as it allows them to solve for regulatory requirements. In addition to our built-in capabilities for archiving content in Microsoft Teams, customers and partners can now use Teams Export APIs to solve for custom application and integration scenarios. The Teams Export APIs support bulk-export (up to 200 requests per second/per app/per tenant) of Teams messages and message attachments. Deleted messages are also accessible by the API for up to 30 days after they're deleted. For more information about these Teams Export APIs and how to use them in your applications, see [Export content with the Microsoft Teams Export APIs](/en-us/microsoftteams/export-teams-content).

For the licensing requirements for the use of the Teams Export APIs, see [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

### Microsoft Graph Connector APIs (preview)

With [Microsoft Graph connectors](/en-us/microsoftsearch/connectors-overview), organizations can index third-party data so it appears in Microsoft Search results. This feature expands the types of content sources that are searchable in your Microsoft 365 productivity apps and the broader Microsoft ecosystem. The third-party data can be hosted on-premises or in public or private clouds. Starting with eDiscovery (Premium), we're enabling developer preview of built-in compliance value of Microsoft 365 connected apps. This capability enables compliance for apps integrating into the Microsoft 365 ecosystem to empower users with seamless compliance experiences. To learn more about how to incorporate Microsoft Graph Connector APIs in your apps, see [Create, update, and delete connections in the Microsoft Graph](/en-us/graph/connecting-external-content-connectors-api-overview).

### Microsoft Graph API for records management

Organizations of all types need a records management solution to manage critical records across their data. [Microsoft Purview Records Management](records-management) helps an organization manage its legal obligations, provides the ability to demonstrate compliance with regulations, and increases efficiency with regular disposition of items that are no longer required.

Organizations use the records management solution to protect, label, retain, or delete their data. The Microsoft Graph APIs for records management help organizations manage retention labels and their associated actions more efficiently, automate repetitive tasks, and equip customers with flexibility in options.

The first release of Graph APIs for records management supports the management of retention labels and event-based retention. Example scenarios include:

- **Managing retention labels**

    Record management admins and developers need to maintain their record management systems with labels that they periodically create, update, and delete.

    Developers and compliance admins use the Graph APIs for records management to perform CRUD operations on the label entity to maintain their systems.
- **Triggering an event for an existing label**

    When an employee leaves an organization, the information is updated in the HR management system. From the date of leaving, confidential documents need to be retained for seven years. These documents already have the retention label "Employee\_departure" applied to them.

    Developers and compliance admins use the Graph APIs for records management to read the label “Employee\_departure” and look up the associated event type "Event-employee\_departure".

    They then use the Graph APIs for records management to create an event for the associated event type. The retention period for the confidential documents starts after this event is created.

For more information about the Graph APIs for records management, see [Use the Microsoft Graph Records Management API](/en-us/graph/api/resources/security-recordsmanagement-overview).

For licensing requirements to use these APIs, see the records management information from the Microsoft 365 guidance for security & compliance, [Microsoft Purview Data Lifecycle Management & Microsoft Purview Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#microsoft-purview-data-lifecycle-management--microsoft-purview-records-management) section.

### Microsoft Graph API for retention labels in SharePoint and OneDrive for Business

Retention labels are part of the Microsoft Purview Data Lifecycle Management solution and apply governance at the driveitem level. Retention labels support more capabilities than retention policies and can handle exceptions within a location. For more information on retention labels, see [Create retention labels for exceptions to your retention policies](/en-us/purview/create-retention-labels-data-lifecycle-management).

With the Microsoft Graph APIs for retention labels, organizations can programmatically apply and manage these labels on items in SharePoint and OneDrive for Business to automate their processes.

These Graph APIs support the following tasks:

- **[Apply a retention label to an item](/en-us/graph/api/driveitem-setretentionlabel)**
- **[Remove a retention label from an item](/en-us/graph/api/driveitem-removeretentionlabel)**
- **[Get metadata information on the retention label applied to an item](/en-us/graph/api/driveitem-getretentionlabel)**
- **[Lock or unlock the record label applied to an item](/en-us/graph/api/driveitem-getretentionlabel)**

For licensing requirements to use these APIs, see the records management information from the Microsoft 365 guidance for security & compliance, [Microsoft Purview Data Lifecycle Management & Microsoft Purview Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#microsoft-purview-data-lifecycle-management--microsoft-purview-records-management) section.

## Software Developer Partner Integrations

Microsoft Purview enables software development companies to embed advanced data security capabilities directly into their applications. Using available SDKs and APIs, developers can build solutions that apply classification, labeling, protection, and retention policies natively within their workflows. These integrations enable automation, consistent policy enforcement, and unified governance across diverse environments—helping companies meet regulatory requirements and streamline compliance processes at scale.

### Network Data Security

[Microsoft Purview Network Data Security](/en-us/purview/dlp-network-data-security-learn) enables real-time protection by intercepting and inspecting network traffic using the Purview DLP engine. Through deep integration with SASE and next-generation firewall platforms, it extends Purview classification and policy enforcement capabilities to the network layer based on customer-defined data loss prevention and collection policies. This enables:

- Granular control over sensitive data flows across both sanctioned and unsanctioned applications.
- Blocking exfiltration and unauthorized sharing with generative AI tools, cloud services, storage platforms, and social media.
- Deep integration with Purview insights and solutions, including Data Security Posture Management (DSPM) and Insider Risk Management (IRM).
- Stronger compliance for AI interactions through content capture that supports eDiscovery, retention, deletion, and related regulatory workflows.

The following list of partners have successfully built a Network Data Security integration:

| Partner | Partner documentation | Description |
| --- | --- | --- |
| iboss | [iboss deployment guide](https://www.iboss.com/microsoft-integrations/purview-inline-data-discovery) | iboss Zero Trust Integrates with Purview DLP for secure access and network data classification. |
| Netskope | [Netskope deployment guide](https://docs.netskope.com/en/netskope-one-for-microsoft-purview-dlp) | Netskope One Integrates with Purview DLP to inspect and classify network traffic for data protection. |

For more information on building integrations with Microsoft Purview, see [Use Microsoft Purview APIs to support data security and governance in your apps](/en-us/purview/developer/use-the-api). To get listed in the above table of integration partners, register your interest using the following form: [Microsoft Purview Network Data Security partner integration checklist](https://aka.ms/PurviewNetworkPartnerOnboardRequest).

### Microsoft Purview for Generative AI Apps integration

As generative AI tools become embedded in business processes, Microsoft Purview enables security, compliance, and data teams to discover and monitor AI usage, safeguard sensitive information in prompts and outputs, and enforce organizational policies—helping organizations innovate responsibly while reducing risk and meeting regulatory requirements. Developers can use the Microsoft Purview SDK to integrate these protections directly into their AI solutions, extending Purview’s coverage across the enterprise AI ecosystem. Visit the following documentation for guidance on building this integration: [Use the Microsoft Purview SDK with Agent Framework](/en-us/agent-framework/tutorials/plugins/use-purview-with-agent-framework-sdk).

The following partner has successfully built a Microsoft Purview for Generative AI App integration.

| Partner | Partner documentation |
| --- | --- |
| Miro | [Miro deployment guide](https://help.miro.com/hc/en-us/articles/28698434922386-Set-up-Microsoft-Purview-DSPM-for-Miro-AI) |

To get listed in the above table of integration partners, register your interest using the following form: [Microsoft Purview for Generative AI apps partner integration checklist](https://forms.office.com/r/ekg1sxKhkP).

### Microsoft Information Protection (MIP)

Many vendors integrate with Purview Information Protection to unify classification and protection across platforms. For a comprehensive list of MIP development partners, visit [Microsoft Intelligent Security Association](https://www.microsoft.com/misapartnercatalog?IntegratedProducts=MicrosoftPurviewInformationProtection).

For information on building with Microsoft Information Protection see the [Microsoft Information Protection SDK documentation](/en-us/information-protection/develop/).