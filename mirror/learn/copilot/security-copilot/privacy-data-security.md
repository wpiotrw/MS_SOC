---
layout: Conceptual
title: Privacy and data security in Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/privacy-data-security
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about privacy and data security in Microsoft Security Copilot.
ms.date: 2026-04-08T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-privacy
- essentials-security
- essentials-compliance
locale: en-us
document_id: 7d671095-e125-883a-096e-fcc9d1926375
document_version_independent_id: 7d671095-e125-883a-096e-fcc9d1926375
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/privacy-data-security.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: privacy-data-security
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/privacy-data-security.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: 1cfaa989-ab74-f32e-1619-405ac4852341
---

# Privacy and data security in Microsoft Security Copilot | Microsoft Learn

Important

The privacy and data security settings described on this page apply to customers who are not using a Microsoft 365 E5 and E7 license. If you are a Microsoft 365 E5 and E7 customer, note that your default settings differ from those described here, but this page still includes important information about how those settings work. For more information, see [Auto provisioned for Microsoft 365 E5 and E7 customers](/en-us/copilot/security/auto-provisioning-security-copilot).

When you use [Microsoft Security Copilot](microsoft-security-copilot), Customer Data and system-generated logs are stored and processed as part of the service.

Data sharing is turned on by default. Global Administrators and Security Administrators with the Capacity Contributor role (for example, capacity write access) for the capacity linked to a Workspace, can configure Customer Data sharing settings. Administrators can do this during the first run experience and at any time afterward. For more information on roles, see [Security Copilot roles](authentication#security-copilot-roles).

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

This article compares Security Copilot's Customer Data to system-generated logs, describes data sharing options, and summarizes how data is protected.

## Customer Data and system-generated logs

As defined in the Microsoft Product Terms, *Customer Data* means all data, including all text, sound, video, or image files, and software, that are provided to Microsoft by, or on behalf of, the Customer through use of the Online Service. Customer Data doesn't include Professional Services Data or information used to configure resources in the Online Services such as technical settings and resource names.

Microsoft online services create *system-generated logs* as part of the regular operation of the services. System-generated logs continuously record system activity over time to allow Microsoft to monitor whether systems are operating as expected. "Logging" (the storage and processing of logs) is essential to identify, detect, respond to, and prevent operational problems, policy violations, and fraudulent activity. Logging is also essential to optimize system, network, and application performance, as well as to help with security investigations and resilience activities and to comply with laws and regulations.

The following table compares Security Copilot's Customer Data to system-generated logs.

| Customer Data | System-generated logs |
| --- | --- |
| - Prompts that users submit to Security Copilot.  - Information retrieved to generate responses. - Responses. - Content of pinned items.  - File uploads. | - Account information (tenant ID, account ID, licensing, and others). - Usage data. - Performance information. - Internal system behavior information. |

## Customer Data sharing preferences

Copilot owners can change data sharing settings for Customer Data during the first run experience, and at any time thereafter.

Enabling or disabling these Customer Data sharing preferences described in the following table won't affect Microsoft's rights or responsibilities under the Microsoft Products and Services Data Protection Addendum.

The following data sharing options are available:

| Setting | Description |
| --- | --- |
| **Allow Microsoft to capture data from Security Copilot to validate product performance using human review** | Such validations include but aren't limited to:  - Ability of Security Copilot to successfully provide responses to user requests and understand capability gaps that need to be addressed based on user prompts.- Understand the types of tasks customers are using Security Copilot for. - Produce metrics surrounding the usability and quality of responses and agents.  - Validate Security Copilot capabilities involving other Microsoft products purchased (including those products agents) and integrated by a customer. - Improve responses from plugins and agents accessing other Microsoft products. - Improve responses from Microsoft Security Copilot agents within Security Copilot, including agents accessing other Microsoft products.For more information, see Set up location for prompt evaluation and opt-in (or out of) data sharing. |
| **Allow Microsoft to capture and human review data from Security Copilot to build and validate Microsoft's security AI model** | Such validations include but aren't limited to: - Captured data\* is used to develop security specific models built on top of Azure OpenAI foundational model or Microsoft built models, which would power more intelligent and personalized capabilities for Security Copilot and other Microsoft products that it integrates with.  \*Captured data includes data from Microsoft plugins and Microsoft Security Copilot agents utilized by you while using Security Copilot.**NOTE:** Data isn't shared with OpenAI or used to train the Azure OpenAI foundational model. |

## Accessing data from Microsoft 365 services

Security Copilot seamless integrates with multiple Microsoft 365 and Microsoft security services that your organization has licensed. You have the option of allowing users to use those products to query information directly from those services in both the standalone and embedded experiences.

Note

Currently, Security Copilot only accesses Microsoft 365 services data processed by Microsoft Purview, and Customer Data generated by Microsoft Purview (for example, DLP alerts).  In Microsoft Purview, services such as data loss prevention (DLP), Insider Risk Management (IRM), or communication compliance are configured by the administrator to run on Microsoft 365 services data (or other data types). The data types that Security Copilot can access is dictated by what an administrator has configured for Microsoft Purview. 

The following table summarizes the Microsoft 365 services data accessed by Security Copilot.

| Microsoft Purview Product or Services | What is accessed by Security Copilot |
| --- | --- |
| Data Loss Prevention | DLP alert data associated with a DLP match |
| Microsoft Purview Information Protection | Activity logs associated with labeling activity |
| eDiscovery | Data captured within a review set of an eDiscovery search |
| Insider Risk Management | IRM alert data associated with an IRM policy alert |
| Communication Compliance | Data captured within a policy match of a Communication Compliance Policy |
| Data Security Posture Management | Activity and alerts data associated with MIP, DLP, IRM |

Microsoft 365 services data accessed by Security Copilot, including Customer Data generated by Microsoft Purview, is processed and stored according to the data processing activities described herein. This means, Microsoft 365 data accessed by Security Copilot will be processed and stored in location(s) described herein, regardless of the location in which the data was processed or stored pursuant to [EU Data Boundary Services](/en-us/privacy/eudb/eu-data-boundary-transfers-for-all-services) and the data residency commitments under the "Customer Data at Rest for Core Online Services" section of the Product Terms before the data was accessed by Security Copilot. This also means, Microsoft 365 data accessed by Security Copilot will be processed pursuant to the security practices and policies applicable to Security Copilot, regardless of the security practices and policies applicable to the data under "Security Practices and Policies for Core Online Services" section of the Product Terms before the Microsoft 365 data was accessed by Security Copilot.

To learn more about information captured, recorded, and retained by Microsoft Purview, see [Learn about auditing solutions in Microsoft Purview](/en-us/purview/audit-solutions-overview). For information about activities that are audited in Microsoft 365, [Audit log activities](/en-us/purview/audit-log-activities).

| Setting | Description |
| --- | --- |
| **Allow Security Copilot to access data from your Microsoft 365 services** | When turned on: - Security Copilot can retrieve your data from a Microsoft 365 service on your behalf if you're a customer of both Security Copilot and the Microsoft 365 service, and you allow Security Copilot access to your Microsoft 365 services. See the note in the prior section for more information about the Microsoft 365 services data accessed by Security Copilot. - All data, including Microsoft 365 data returned to answer your queries in Security Copilot is retained pursuant to Security Copilot's data retention policy. For more information, see Customer Data storage location. |

### Configuring Microsoft 365 services data access

Use the following steps to turn on or off Security Copilot's access to Microsoft 365 services.

1. In Security Copilot, go to **Settings** &gt; **Owner settings**.
2. Update your data sharing selection.

Warning

Turning off Microsoft 365 data access does not mean that any data retrieved from those Microsoft 365 services are deleted at that instant. Microsoft 365 data accessed up to that time will be deleted pursuant to Security Copilot's data retention policy. For more information, see Data retention and deletion.

## Customer Data storage location

Data is stored in the location you select during Workspace creation. This happens during the onboarding steps as you set up your first Workspace, or whenever a new Workspace is created. Whenever you create a Workspace, you can choose the new Workspace's data storage location to be the same or different from that of your other existing workspaces. Once you have created a Workspace, you cannot change its data storage location. For Government Community Cloud (GCC) customers adopting the Security Copilot Commercial SKU, their relevant Customer Data associated with, and feedback shared from GCC Product SKUs will be stored in the US Geo of the Azure Public Cloud.

When data sharing is opted in, Customer Data such as prompts and responses are shared with Microsoft to enhance product performance, improve accuracy, and address response latency. In this case, Customer Data (except uploaded files) may be stored outside of the tenant's chosen Workspace geo. While uploaded files are stored in the tenant's chosen Workspace, if content from uploaded files is part of information retrieved to generate responses during sessions, that retrieved content can be stored outside of the Workspace. For more information, see [Data, privacy, and security for Azure OpenAI Service](/en-us/legal/cognitive-services/openai/data-privacy?tabs=azure-portal).

Note

Communications initiated by skills through Microsoft Security Copilot agents that surface results through emails or Microsoft Teams may traverse global Microsoft network infrastructure during transit, and therefore may cross geographic boundaries, even when data at rest remains within the selected Workspace region.

### File upload storage and processing

While uploaded files are stored in the tenant's chosen Workspace, if content from uploaded files is part of information retrieved to generate responses during sessions, that retrieved content can be stored outside of the Workspace. Uploaded files are only available to the user account that uploaded them, and not available to other users within or outside the tenant.

When data sharing is opted in, Microsoft may only capture and human-review content from uploaded files when that content is part of information retrieved to generate responses.

## Data retention and deletion

Security Copilot stores Customer Data necessary for in-product functionality (such as your session data (for example your prompts and responses)) so long as you have an active subscription to Security Copilot.

Customer Data can be deleted in the following scenarios:

- **When you delete all provisioned capacity** Customer Data is deleted within 180 days of when you delete all provisioned capacity.
- **When a session is inactive for more than 180 days** Session data will be deleted after 180 days of inactivity.
- **When you request for your Customer Data to be deleted** You can also request that Security Copilot delete your Customer Data through the portal (https://securitycopilot.microsoft.com) or by requesting deletion through [customer support](support) . This Customer Data will be deleted within 30 days of that request.

When you opt-in to sharing your Customer Data with Security Copilot this Customer Data is only retained by Security Copilot for 90 days before being deleted by that team evaluating that Customer Data.

If you opt out of data sharing, Security Copilot deletes all Customer Data shared within 30 days. Customer Data is retained by you in your tenant so long as you have an active subscription to Security Copilot and have not requested it be deleted.

## Data Subject Requests (DSRs) under the GDPR

For DSRs, please contact the support team: [customer support](support). The Security Copilot team will then guide you through the next steps and process your request in accordance with GDPR guidelines. If you have any further questions or need additional assistance, feel free to [contact support](support).

## Location for prompt evaluation

With any Microsoft Copilot product, prompts refer to the text-based, natural language input you provide in the prompt bar that instructs Security Copilot to generate a response. Prompts are the primary input Copilot needs to generate answers that help you in your security-related tasks. Prompts are evaluated using GPU resources in Azure datacenters protected with Azure security and privacy controls.

You can choose to select where the prompts are evaluated from any of the following locations:

- Australia (ANZ)
- Europe (EU)
- United Kingdom (UK)
- United States (US)

You can opt in to having prompts evaluated anywhere in the world to mitigate potential disruptions in case your primary location experiences high activity.

Microsoft recommends having prompts evaluated anywhere with available GPU capacity, which enables the Copilot system to determine the optimal location based on load, latency, and responsiveness.

Note

Data is stored in the location you select during Workspace creation. For more information, see Customer Data storage location.

## Set up location for prompt evaluation and opt in (or out of) data sharing

During initial setup, Copilot owners are prompted to set data sharing and prompt evaluation options. For more information, see [Get started with Security Copilot](get-started-security-copilot). Copilot owners can change these settings during the first run experience, or at any time thereafter.

**Authorized role** You need to be a Copilot owner to change the data sharing options. For more information on roles, see [Understand authentication](authentication).

### Set up data sharing

During initial setup, a Copilot owner is provided with the following data sharing options:

| Setting | Description |
| --- | --- |
| **Allow Microsoft to capture data from Security Copilot to validate product performance using human review** | Such validations include but aren't limited to:  - Ability of Security Copilot to successfully provide responses to user requests and understand capability gaps that need to be addressed based on user prompts.- Understand the types of tasks customers are using Security Copilot for. - Produce metrics surrounding the usability and quality of responses.  - Validate Security Copilot capabilities involving other Microsoft products that a customer has purchased and integrated. - Improve responses from plugins accessing other Microsoft products. |
| **Allow Microsoft to capture and human review data from Security Copilot to build and validate Microsoft's security AI model** | Such validations include but aren't limited to: - Captured data is used to develop security specific models built on top of Azure OpenAI foundational model, which would power more intelligent and personalized capabilities for Security Copilot and other Microsoft products that it integrates with. **NOTE:** Data isn't shared with OpenAI or used to train the Azure OpenAI foundational model. |

- When you opt in to data sharing, your Customer Data is shared with Microsoft from that point forward.
- When you opt out of data sharing, no further Customer Data is shared. Customer Data that was shared previously is retained for not more than 180 days.

### Updating data sharing

1. In Security Copilot, go to **Settings** &gt; **Owner settings**.
2. Update your data sharing selection.

## How Microsoft protects your data

Microsoft uses comprehensive controls to protect your data. All Security Copilot data is handled according to Microsoft's commitments to privacy, security, compliance, and responsible AI practices. Access to the systems that house your data is governed by Microsoft's certified processes.

Security Copilot runs queries as the user, so it never has elevated privileges beyond what the user has.

If you opt in to share Customer Data, your data is:

- Not shared with OpenAI
- Not used for sales
- Not shared with third parties
- Not used to train Azure OpenAI foundational models

Security Copilot meets all Azure production data compliance standards.

All data stored in Azure is automatically encrypted at rest and uses AES-256 encryption. For more information, see [Data encryption](/en-us/azure/cosmos-db/database-encryption-at-rest) and [Encryption at rest](/en-us/azure/storage/common/storage-service-encryption).

## Microsoft security products data handling

Microsoft Security products purchased by you may share data, including Customer Data, as described in the product documentation. Customer Data shared with Security Copilot is governed by the Product Terms, Data Protection Addendum, and documentation applicable to Security Copilot. For Microsoft 365 services, an administrator needs to enable Security Copilot in the sharing preference option detailed in Accessing data from Microsoft 365 services and users will need to enable a plugin for those Microsoft 365 Services. For other Microsoft services, such plugins are enabled by default for users. Users can turn off plugins at any time. For more information, see [Manage plugins](manage-plugins).

## Feedback from Security Copilot users

Microsoft collects feedback on the response produced by Microsoft Security Copilot from users of the product. A Copilot owner can turn off feedback collection for their tenant by contacting Microsoft Support through a support ticket. For more information, see [Contact support](support).