---
layout: Conceptual
title: Microsoft Purview Insider Risk Management and Communication Compliance privacy guide | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview Insider Risk Management and Microsoft Purview Communication Compliance are built with privacy by design, and how the solutions balance user privacy with tools that help detect and mitigate organizational risks.
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-18T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
- m365solution-insiderrisk
- m365solution-overview
- highpri
ms.custom: sfi-ga-nochange
locale: en-us
document_id: fa75f828-58dd-b923-2ae2-c882c5ef4429
document_version_independent_id: fa75f828-58dd-b923-2ae2-c882c5ef4429
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-solution-privacy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-solution-privacy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-solution-privacy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 39ae770b-1a53-9f40-ebd1-6d4cc036d3a9
---

# Microsoft Purview Insider Risk Management and Communication Compliance privacy guide | Microsoft Learn

Microsoft Purview insider risk solutions give organizations the tools to help detect and reduce potential risks and policy violations. The Microsoft Purview insider risk solutions include:

- **Microsoft Purview Insider Risk Management** uses different signals to find potential malicious or accidental insider risks, such as intellectual property theft, data leakage, and security violations. Insider risk management lets customers create policies to manage security and compliance.
- **Microsoft Purview Communication Compliance** provides tools to help organizations detect potential regulatory compliance issues (for example SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content.

Insider risk management and communication compliance are built with privacy by design and balance user privacy with tools that help detect and reduce organizational risks. We're committed to protecting user trust and maintaining user-level privacy through our core privacy principles:

- Pseudonymization
- Role-based access controls
- Admin explicit opt-in
- Audit logs

## Pseudonymization

Pseudonymization helps protect end-user privacy by removing identifiable user details like user name or email address. Pseudonymization also helps prevent potential bias and conflicts of interest by removing identifiable user details (name, email) and personal data (title, department, or location) exposed in the solution. For example, a user named John Smith is pseudonymized into a nonpersonal identifier such as ANON2340. Pseudonyms are on by default for specific roles such as *Insider Risk Management Analysts* and *Insider Risk Management Investigators* (review alerts and take action respectively) and *Communication Compliance Analysts* (review policy alerts).

## Role-based access controls

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

We recommend using stringent role-based access controls so only authorized insider risk management and communication compliance roles can use and access alerts and insights into potential policy violations. By default, global administrators don't have access to insider risk management and communication compliance features. This default setting helps ensure that only the appropriate stakeholders can access the solution and details specific to their role permissions. Organizations can assign users to specific role groups to manage different sets of features based on their responsibilities. For example, insider risk management and communication compliance admins can create, configure, and delete policies but can't access or investigate alerts or cases. On the other hand, insider risk management and communication compliance investigators can access and investigate alerts and cases but can't configure policies.

Note

Insider risk management admins can allow investigators and analysts to make edits to policy indicators and thresholds by using the [inline alert customization setting](insider-risk-management-settings-inline-alert-customization).

Whether your organization chooses a single role group or multiple role groups to fit your organization's compliance and privacy requirements, both insider risk management and communication compliance allow admins to choose from predefined role group options within each solution.

Learn more about role group options for each solution:

- [Get started with insider risk management](insider-risk-management-permissions)
- [Get started with communication compliance](communication-compliance-permissions)

## Admin explicit opt-in

Insider risk management and communication compliance policies detect risky activities and communications and potential policy violations that could result in a security incident. An admin with the right permissions can explicitly scope employees into a policy.

Additionally, by default, insider risk management and communication compliance indicators that help detect risky activities and communications that might lead to potential data security incidents are disabled. For example, indicators like "downloading content from OneDrive", "sharing SharePoint files with people outside the organization", or "sending sensitive information or harassing messages" are off by default. Insider risk management and communication compliance don't detect those activities without an admin's explicit opt-in. Admins with the right permissions must explicitly select and opt in to one or more indicators in settings before a policy can detect those activities.

Admin explicit opt-in controls help safeguard end-user privacy by ensuring the solutions only flag alerts and policy violations for users and indicators specified in the policies.

## Audit logs

Microsoft Purview insider risk solutions audit logs record all admin actions. With these logs, organizations can stay informed about all actions taken within Microsoft Purview insider risk solutions, including when an admin creates or edits a policy, adds a user, views user activity insights, or adds indicators.

Audit logs are enabled by default for all Microsoft 365 organizations. With these logs, organizations can audit privileged admins' actions and meet compliance and privacy requirements.

For more information about audit logs capabilities for each solution, see:

- [Review activities with the insider risk management audit log](insider-risk-management-audit-log)
- [Use communication compliance reports and audits](communication-compliance-reports-audits#audit)

## Protect user trust and build a holistic insider risk program

User privacy and trust are essential for organizations to establish a holistic insider risk program. The right set of tools can help you address risks in a way that meets security needs. Learn how to [build a holistic insider risk management program](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE59jhs) with five elements that help companies have stronger data protection while ensuring user trust.