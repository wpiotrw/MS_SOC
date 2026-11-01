---
layout: Conceptual
title: Privacy in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-privacy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview addresses privacy requirements, including data types collected, retention policies, data residency, and data subject request handling.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-04T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
search.appverid:
- MET150
ms.collection:
- purview-compliance
- essentials-privacy
- essentials-overview
ai-usage: ai-assisted
locale: en-us
document_id: 24b2ace4-ca01-6846-12d7-96cdff68bb98
document_version_independent_id: 24b2ace4-ca01-6846-12d7-96cdff68bb98
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-privacy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-privacy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-privacy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: ea9c8e12-d04e-faf5-4b0f-f15193a3fca6
---

# Privacy in Microsoft Purview | Microsoft Learn

Microsoft is committed to providing the information you need to manage privacy concerns in Microsoft Purview. All aspects of Microsoft Purview adhere to Microsoft's privacy governance model, which includes controls on data minimization, retention and deletion, location and transfer, sharing, and more.

For information about Microsoft’s privacy governance model, see [Privacy & data management overview - Microsoft Service Assurance](/en-us/compliance/assurance/assurance-privacy).

## Data security and privacy

Microsoft Purview processes and stores the following content types:

- Customer data
- End User Identifiable Information (EUII)
- Administrator data
- End User Pseudonymized Identifiers (EUPI)
- Feedback data

These types of data typically come from other Microsoft 365 services, such as Exchange, SharePoint, Microsoft Teams, and Copilot. Microsoft Purview also sources data when tenant admins configure policies and define data classification labels that can be applied to the organization’s assets. This data includes emails, files, chats, messages, or Copilot interactions. EUII, administrator data, and EUPI data come from Microsoft Purview tenant administrators or users. Tenant administrators can also bring data from third-party sources so that the solutions offered by Microsoft Purview can extend to these sets of organizational data.

### Customer data

You can categorize Microsoft Purview customer data as follows:

- Custom configuration settings.
- Search queries: In e-discovery, administrators can perform search and export results. This action could contain a portion of the data impacted by the user action, and the system retains it until the user deletes it. This category includes all Microsoft 365 user data, such as emails, files, Teams chat, and Copilot & AI interactions.
- Alerts
- Reports
- Tenant data that connectors ingest from third-party data sources.
- Data classification labels.

### End User Identifiable Information (EUII)

End User Identifiable Information (EUII) includes a user's email address, User Principal Name (UPN), end user's IP address, address book data, user name, and user display name. Tenant admins choose how to process EUII data and decide which solutions to apply to these end users' data.

### Administrator data

Administrator data includes the tenant admin's email address, UPN, IP address, user name, and display name. These types of data are specifically processed around tenant admin's activities when they perform administrative duties, such as:

- Set up policies, configurations, or connectors.
- Assign data classification label or policies to users.
- Put a user's data on legal hold.
- Assign compliance tasks to users.

### End user pseudonymized identifier (EUPI)

End User Pseudonymized Identifier (EUPI) data includes UserID, UserKey, and Mailbox GUID. EUPI and EUII are used for user activities, audit logs, eDiscovery search, and service logs.

### Feedback data

Feedback data is the feedback about the compliance solutions that a tenant administrator submitted through Unified Feedback Platform within Microsoft Purview.

### How are these content types processed?

In the solutions that Microsoft Purview provides, customer data, EUII, administrator data, EUPI, and feedback data are applied to data assets such as emails, files, chats, messages, or Copilot and AI app interactions. For users managed by tenant admins, Microsoft Purview data processing can include monitoring for risky activities, preserving accounts and data, assigning tasks, and more. Microsoft Purview solutions handle these data assets as follows:

| Data asset | Processing |
| --- | --- |
| Exchange emails and calendar items | Microsoft Purview solutions process this data to enable: - Data classification labels - Legal hold - Data Loss Prevention policies - Encryption with customer's own encryption key |
| SharePoint and OneDrive files |
| Messages from Teams, Skype for Business, and Viva Engage |
| Copilot and AI app interactions. |
| Email subject & metadata | Microsoft Purview solutions process this data for audit that tracks activities of tenant admins, analysts, and users. |
| Calendar item data |
| List, filename, & metadata from SharePoint and OneDrive. |

### Retention

Tenant administrators primarily control the retention of these types of data, except for the following cases:

- **eDiscovery:** Tenant administrators retain data that is in scope for eDiscovery case investigation until they delete the case when the legal investigation is complete, and the case is closed. A former employee's data isn't deleted until the investigation case is closed.
- **Audit:** User activity logs are retained for 180 days by default, 365 days for E5 licensed customers, and 10 years if customers purchase an additional license.
- **Communication policy hits:** Tenant administrators retain these as configured. The default policy retention is one year.
- **Configuration and policy data:** Tenant administrators retain this data until they delete configuration settings or policies.
- **Connector data:** Tenant administrators retain all data that is brought into the in-scope Microsoft Purview solutions through connectors until they remove the connectors and purge the data.
- **Administrator data:** Administrator data is retained until the person is no longer a tenant administrator.
- **Feedback data:** Feedback data is retained for 180 days.

When a user or the tenant leaves Microsoft 365 services, their data is retained for 90 days and no longer than 180 days to allow recovery or export of the data, except where specified by policy. For example, for eDiscovery, the data is retained until the tenant admin releases the user’s account from legal hold.

### Data residency

Customer data is stored based on where customer accounts are provisioned and in accordance with the commitments in the Online Service Terms. For more information, see [Where your Microsoft 365 customer data is stored](/en-us/microsoft-365/enterprise/o365-data-locations)

### Data sharing

Microsoft Purview solutions don't share data outside of Microsoft or across Microsoft without customer consent or authorization. Microsoft Purview compliance solutions share data with Microsoft Security Copilot as a plugin to Security Copilot. Microsoft Security Copilot processes the following data to provide the Purview Copilot capability:

- Microsoft 365 audit logs collected through the Microsoft Purview Audit pipeline
- eDiscovery and Communication Compliance data, which could include:
    - Emails
    - Teams conversations
    - Copilot and AI app interactions
    - Microsoft Purview alerts or insights generated by Data Loss Prevention (DLP) and Insider Risk Management (IRM)
    - Underlying data that led to such alerts or insights, such as audit logs and telemetry data collected by Microsoft Defender for Office related to emails and Teams, DLP, or IRM policies

For customers in the Government Community Cloud (GCC), data sharing between government and commercial cloud environments may occur, depending on the location of the service offering.

### Data Subject Requests

For information about how to find, access, and act on personal data that resides in Microsoft IT systems, see: [Introduction to DSRs](/en-us/compliance/regulatory/gdpr-dsr-prof-services#introduction-to-dsrs).

[Data privacy and protection – Respond to incidents and subject requests](/en-us/microsoft-365/solutions/data-privacy-protection-respond-requests)

## Regulatory compliance

As a product, Microsoft Purview provides solutions to help manage risk and compliance for your organization. For more information about these product capabilities, see: [Microsoft Purview risk and compliance solutions](purview-compliance).

As an online service, Microsoft Purview aligns to the Microsoft Security Policy (MSP). For more information, see: [Governance, risk, and compliance overview - Microsoft Service Assurance](/en-us/compliance/assurance/assurance-governance).

For more information about regulatory compliance in Microsoft Purview, see: [Regulatory & industry compliance](/en-us/compliance/).

## Resources

For more information about Microsoft privacy and compliance, see the following resources:

- [Microsoft Trust Center](https://www.microsoft.com/trust-center/privacy)
- [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement)
- [General Data Protection Regulation](/en-us/compliance/regulatory/gdpr)
- [The EU Data Boundary for the Microsoft Cloud](https://www.microsoft.com/trust-center/privacy/european-data-boundary-eudb)
- [Microsoft Privacy](/en-us/privacy)