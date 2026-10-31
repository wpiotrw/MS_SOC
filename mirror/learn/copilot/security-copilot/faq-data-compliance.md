---
layout: Conceptual
title: Microsoft Security Copilot Data and Compliance Frequently Asked Questions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/faq-data-compliance
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Microsoft Security Copilot Data and Compliance frequently asked questions.
ms.date: 2026-05-28T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: faq
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: lakram
search.audiencetype: Admin
locale: en-us
document_id: 5345e091-4b76-200e-7c07-6ca7f8cbddb9
document_version_independent_id: 5345e091-4b76-200e-7c07-6ca7f8cbddb9
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/faq-data-compliance.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: faq-data-compliance
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/faq-data-compliance.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 0b61ef24-d3bf-97f6-4cb8-dd74b4b0190e
---

# Microsoft Security Copilot Data and Compliance Frequently Asked Questions | Microsoft Learn

This article provides a reference for how Microsoft Security Copilot handles, stores, and protects Customer Data. It highlights key data residency behaviors, security and privacy commitments, eligibility considerations, retention practices, and how Security Copilot complies with Microsoft policies and industry regulations.

## FAQ

### What is Security Copilot's Microsoft 365 E5 and E7 data handling policies?

All existing Security Copilot customers' data storage and handling will continue in the location where their current workspace resides. For more information, see [Privacy and data security in Microsoft Security Copilot](privacy-data-security).

### Can my organization elect to disable Security Copilot at this time?

Existing customers can remove Security Copilot capacity. For more information, see [Delete capacity through Security Copilot](manage-usage#delete-capacity-from-the-owner-settings).

For customers who do not currently have access to Security Copilot through Microsoft 365 E5 and E7, details will be shared once it is included in their Microsoft 365 E5 and E7 license.

### Is Customer Data used to train Azure OpenAI Service foundation models?

No, Customer Data isn’t used to train Azure OpenAI Service foundation models, and this commitment is documented in our Product Terms. For more information on data sharing in the context of Security Copilot, see [Privacy and data security](privacy-data-security).

### What is the GDPR Guidance for EU Markets?

Microsoft complies with all laws and regulations applicable to its providing the Products and Service including security breach notification law and Data Protection Requirements (as defined in the Microsoft DPA). However, Microsoft isn’t responsible for compliance with any laws or regulations applicable to Customer or Customer’s industry that aren’t generally applicable to information technology service providers. Microsoft doesn’t determine whether Customer’s data includes information subject to any specific law or regulation. For more information, see [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA).

### Are US Government Cloud (GCC) customers eligible?

Currently, Security Copilot isn't designed for use by customers using US government clouds, including but not limited to GCC, GCC High, DoD, and Microsoft Azure Government. For more information, see with your Microsoft representative.

### Are US and Canada health care customers eligible?

US and Canada HLS customers are eligible to purchase Security Copilot. Microsoft Security Copilot is now listed and covered by Business Associate Agreement (“BAA”), which is important to healthcare providers who are subject to regulations under HIPAA. For additional information on compliance offerings currently covered for Microsoft Security Copilot can be found in the [Service Trust Portal](https://servicetrust.microsoft.com/DocumentPage/7adf2d9e-d7b5-4e71-bad8-713e6a183cf3).

### How do I export or delete data from Security Copilot?

You will need to contact support. For more information, see [Contact support](/en-us/copilot/security/support).

### Where can I find more information on Data Protection and Privacy?

You can learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center/privacy?rtc=1).

### The Azure OpenAI Service code of conduct includes “Responsible AI Mitigation Requirements”. How do those requirements apply to Security Copilot customers?

These requirements don’t apply to Security Copilot customers because Security Copilot implements these mitigations.

### Why does Microsoft Copilot transfer data to a Microsoft tenant?

Microsoft Copilot is a SaaS (Software as a Service) offering that runs in the Azure production tenant. Users enter prompts and Security Copilot provides responses based on the insights sourced from other products such as Microsoft Defender XDR, Microsoft Sentinel, and Microsoft Intune. Security Copilot stores past prompts and responses for a user. The user can use the in-product experience to access prompts and responses. Data from a customer is logically isolated from the data of other customers. This data doesn't leave the Azure production tenant and is stored until customers ask to delete them or offboard from the product.

### How is the transferred data secured in transit and at rest?

The data is encrypted both in transit and at rest as described in the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Professional-Services-Data-Protection-Addendum-DPA).

### How is the transferred data protected from unauthorized access and what testing was done for this scenario?

By default, no human users have access to the database and the network access is restricted to the private network where the Microsoft Copilot application is deployed. If a human needs access to respond to an incident, then the on-call engineer needs elevated access and network access approved by authorized Microsoft employees.

Apart from regular feature testing, Microsoft also completed penetration testing. Microsoft Security Copilot complies with all the Microsoft Privacy, security and compliance requirements.

### In "My Sessions" when an individual session is deleted, what happens to the session data?

Session data is stored for runtime purposes (to operate the service), and also in logs. In the runtime database, when a session is deleted via the in-product UX, all data associated with that session is marked as deleted and the time to live (TTL) is set to 30 days. After that TTL expires, queries can't access that data. A background process physically deletes the data after that time. In addition to the 'live' runtime database, there are periodic database backups. The backups will age out – these have short-lived retention periods (currently set to four days).

Logs, which contain session data aren't affected when a session is deleted via the in-product UX. These logs have a retention period of up to 90 days.

### What Product Terms apply to Security Copilot? Is Security Copilot a "Microsoft Generative AI Service" within the meaning of Microsoft's Product Terms?

The following Product Terms govern Security Copilot customers:

- Universal License Terms for Online Services terms in the Product Terms, which include the [Microsoft Generative AI Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) terms and the Customer Copyright Commitment.
- Privacy & Security Terms in the Microsoft Product Terms, which include the Data Protection Addendum.

Security Copilot is a Generative AI Service within the definition of the Product Terms. Additionally, Security Copilot is a "Covered Product" for purposes of the Customer Copyright Commitment. At this time, in the Product Terms there are no product-specific terms unique to Security Copilot. For more information, see [Microsoft Azure Legal Information](https://azure.microsoft.com/support/legal/).

In addition to the Product Terms, customers' MBSA/EA and MCA agreements, for example, govern the parties' relationship. If a customer has specific questions about its agreements with Microsoft, engage the CE, the deal manager, or the local CELA supporting the deal.

### What is the Microsoft Copilot Copyright Commitment?

The Microsoft Customer Copyright Commitment is a new commitment that extends Microsoft's existing intellectual property indemnity support to certain commercial Copilot services. The Customer Copyright Commitment applies to Security Copilot. If a third party sues a commercial customer for copyright infringement for using Microsoft's Copilots or the output they generate, Microsoft will defend the customer and pay the amount of any adverse judgments or settlements that result from the lawsuit, provided that the customer used the guardrails and content filters built into our products.

### Can Security Copilot customers opt out of Azure OpenAI Service abuse monitoring? Does Security Copilot engage in any content filtering or abuse monitoring?

Azure OpenAI abuse monitoring is currently disabled service-wide for all customers.

### Does Security Copilot make any location of data processing or data residency commitments?

For more information on Customer Data storage location and processing, see [Privacy and data security](/en-us/copilot/security/privacy-data-security).

### Is Security Copilot a Microsoft EU Data Boundary service?

At the time of GA, all Microsoft Security Services are out of scope for EU data residency requirements and Security Copilot won't be listed as an EUDB service.

### Where is EU Customer Data stored?

Security Copilot stores Customer Data and Personal Data such as user prompts and Microsoft Entra Object IDs in the tenant Geo. If a customer provisions their tenant in the EU and isn’t opted in to data sharing, all Customer Data and pseudonymized personal data are stored at rest within the EU. Processing of Customer Data and Personal Data prompts can occur in the designated Security GPU Geo. For more information on Security GPU geography selection, see [Get Started with Security Copilot](get-started-security-copilot). If a customer is opted in to data sharing, prompts can be stored outside of the EU Data Boundary. For more information on data sharing, see [Privacy and data security](/en-us/copilot/security/privacy-data-security)..

### Are customer prompts (such as input content from the customer) considered Customer Data within the terms of the DPA and the Product Terms?

Yes, customer prompts are considered Customer Data. Under the Product Terms, customer prompts are considered Inputs. Inputs are defined as "all Customer Data that Customer provides, designates, selects, or inputs for use by a generative artificial intelligence technology to generate or customize an output".

### Is "Output Content" considered Customer Data within the terms of the DPA and the Product Terms?

Yes, Output Content is Customer Data under the Product Terms.

### Is there a transparency note or transparency documentation for Security Copilot?

Yes, the Responsible AI transparency document can be found here: [Responsible AI FAQ](rai-faqs-security-copilot).

### What are the Compliance Offerings for Microsoft Security Copilot?

Microsoft Security Copilot is dedicated to upholding the highest standards of security, privacy, and operational excellence, as demonstrated by its extensive array of industry certifications. These include ISO 27001 for information security management, ISO 27018 for the protection of personal data in the cloud, ISO 27017 for cloud-specific security controls, and ISO 27701 for privacy information management.

Additionally, Security Copilot holds certifications for ISO 20000-1 in IT service management, ISO 9001 in quality management, and ISO 22301 in business continuity management. It also complies with SOC2 requirements for security, availability, and confidentiality, underscoring our commitment to delivering secure and reliable services. For healthcare-related services, Security Copilot is certified under the HiTrust CSF framework, further enhancing its security and compliance stance, and is covered by HIPAA Business Associate Agreements (BAA), ensuring adherence to healthcare regulations and the protection of sensitive health information.

For more information on compliance offerings currently covered for Microsoft Security Copilot see, the [Service Trust Portal](https://servicetrust.microsoft.com/DocumentPage/7adf2d9e-d7b5-4e71-bad8-713e6a183cf3).