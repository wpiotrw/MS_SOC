---
layout: Conceptual
title: Implement your Zero Trust strategy for data protection by using Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/zero-trust-microsoft-purview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: esaggese
ms.service: purview
ms.date: 2025-12-15T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.collection:
- zerotrust-services
- highpri
description: Microsoft Purview contributes to a strong Zero Trust strategy and architecture for data protection.
locale: en-us
document_id: 1d98eeac-0662-1fd9-e226-56894b453b76
document_version_independent_id: 1d98eeac-0662-1fd9-e226-56894b453b76
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/zero-trust-microsoft-purview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: zero-trust-microsoft-purview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/zero-trust-microsoft-purview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e42a01cd-57ab-6b93-b3b5-13b9d2f0bee6
---

# Implement your Zero Trust strategy for data protection by using Microsoft Purview | Microsoft Learn

Microsoft Purview solutions can help you implement a [Zero Trust](/en-us/security/zero-trust/zero-trust-overview) security strategy that is based on the following security principles:

| Verify explicitly | Use least privilege access | Assume breach |
| --- | --- | --- |
| Always authenticate and authorize based on all available data points. | Limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection. | Minimize blast radius and segment access. Verify end-to-end encryption and use analytics to get visibility, drive threat detection, and improve defenses. |

Microsoft Purview is a primary component of the **Use least privilege access** principle by providing data protection solutions. Use Purview capabilities to help you safeguard your data across platforms, apps, and clouds.

## Zero Trust to protect data

Microsoft Purview provides the following capabilities and options for a data defense in depth strategy and a Zero Trust implementation for data protection:

- **Data classification**: So you can know your data

    Discover and detect sensitive data across your entire organization, so that you can better protect it. For more information, see [Classifiers overview](data-classification-overview) and [Reports](purview-reports).
- **Information protection**: So you can protect your data

    Apply sensitivity labels to integrate with Microsoft 365 Copilot and other apps and services to provide access control guardrails, and encryption with rights management for your most sensitive data. Content markings, such as footers and watermarks, can increase awareness and security policy compliance. While users create or update content, the highly visible labels and labeling recommendations support user education about sensitive data. For more information, see [Learn about sensitivity labels](sensitivity-labels).

    When you use sensitivity labels with [protection policies](data-gov-protection-policy), you can automatically enforce access restrictions across your data estate the moment sensitive information is detected.
- **Data loss prevention (DLP)**: So you can prevent data loss

    Users sometimes take risks with your organization’s sensitive data, which might result in a data security or compliance incident. Data loss prevention helps you monitor for and protect against risky oversharing of sensitive data. As with sensitivity labeling, policy tips support user education about sensitive data. For more information, see [Learn about data loss prevention](dlp-learn-about-dlp).
- **Insider Risk Management**: So you can identify and take action against risky security-related user activities and data activity patterns

    Correlate various signals to identify and take action on potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. For more information, see [Learn about Insider Risk Management](insider-risk-management).
- **Data lifecycle management**: So you can delete what you don't need, and safeguard important data

    Deploy policies to manage the lifecycle of sensitive data to reduce data exposure. Limit the number of copies or propagation of sensitive data by automatically and permanently deleting it when it's no longer needed. Or conversely, protect important data from malicious or accidental deletes by automatically retaining a copy in a secured location after a user deletes the data. For more information, see [Learn about data lifecycle management](data-lifecycle-management).

Supporting tools and technologies:

Note

Now in preview, use [Microsoft Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) to help you discover, protect, and investigate sensitive data risks across your digital estate. Unifying other Microsoft Purview solutions, DSPM provides visibility and control for both traditional applications and AI apps and agents, so you can monitor, assess, and remediate data risks regardless of where sensitive data resides.

- As you implement these capabilities, use appropriate [role-based permissions and administrative units](purview-permissions) to provide Just-Enough-Access and segment access. Augment these protective measures with [privileged access management](privileged-access-management) for Just-In-Time access.
- Consider your [encryption](encryption) requirements for specific scenarios, for example:

    - Microsoft 365 Copilot
    - Use your sensitivity labels to apply [Double Key Encryption](double-key-encryption) to selected documents and emails when only your organization and no cloud services should be able to decrypt them.
    - Use [Advanced Message Encryption](revoke-ome-encrypted-mail) if you need to keep sensitive content within your organization boundary, log external mail access, or revoke access to encrypted emails.
    - Use [Customer Key](customer-key-overview) if you need to control the root encryption keys for Microsoft 365 data at-rest.
    - If you use Conditional Access or cross-tenant access settings, these services need [specific configurations to support encrypted content](encryption-azure-ad-configuration).
- For high-value documents and emails, [records management](records-management) supports additional restrictions and a disposition review process.
- Consider using [information barriers](information-barriers) if you need to segment access between specific users by restricting two-way communication and collaboration between groups and users in Microsoft Teams, SharePoint, and OneDrive.
- Additional governance options:

    - [Access policies in the Microsoft Purview Unified Catalog](unified-catalog-data-product-access-policies) allow users to request access to data, but also give you the tools to ensure they only have access to the data they need, and only for as long as they need it.
    - Use the [data sharing app](concept-data-share) to minimize data duplication and instead, provide read-only access that you can time-limit or remove the access.
- Consider using [Compliance Manager](compliance-manager) to help drive the adoption of and monitor the implementation of security features and configurations. Easy-to-build assessments with automatic monitoring help you stay on track with requirements across your multicloud environment.
- Use [auditing solutions](audit-solutions-overview) to help you monitor Microsoft 365 data and respond to security events.
- Use [Customer Lockbox](customer-lockbox-requests) to ensure Microsoft service engineers must obtain approval before accessing any Microsoft 365 data you own during a support investigation.