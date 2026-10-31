---
layout: Conceptual
title: Plan for Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-plan
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to plan for using Insider Risk Management policies in your organization.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: 27c7796a-c42c-8c5b-4431-259ae59fc0ee
document_version_independent_id: 27c7796a-c42c-8c5b-4431-259ae59fc0ee
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-plan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b674f1ce-5e11-afec-00ed-5c79c188d688
---

# Plan for Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Before you get started with [Insider Risk Management](insider-risk-management) in your organization, review important planning activities and considerations with your information technology and compliance management teams. Thoroughly understanding and planning for deployment in the following areas helps ensure that your implementation and use of Insider Risk Management features goes smoothly and aligns with best practices.

For more information and an overview of the planning process to address risky activities in your organization, see [Starting an Insider Risk Management program](https://download.microsoft.com/download/b/2/0/b208282a-2482-4986-ba07-15a9b9286df0/pwc-starting-an-insider-risk-management-program-with-pwc-and-microsoft.pdf).

To learn how the Insider Risk Management workflow can help your organization prevent, detect, and contain risks while prioritizing your organization values, culture, and user experience, watch the following video:

Check out the [Microsoft Mechanics video](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) on how Insider Risk Management and Communication Compliance work together to help minimize data risks from users in your organization.

## Work with stakeholders in your organization

Identify the appropriate stakeholders in your organization to collaborate for taking actions on Insider Risk Management alerts and cases. Consider including the following areas of your organization in initial planning and the end-to-end [Insider Risk Management workflow](insider-risk-management#workflow):

- Information technology
- Compliance
- Privacy
- Security
- Human resources
- Legal

## Determine regional compliance requirements

Different geographic and organizational areas might have compliance and privacy requirements that differ from other areas of your organization. Work with the stakeholders in these areas to ensure they understand the compliance and privacy controls in Insider Risk Management and how to use them across different areas of your organization. In some scenarios, compliance and privacy requirements might require policies that designate or restrict some stakeholders from investigations and cases based on the case for a user or regulatory or policy requirements for the area.

If you have requirements for specific stakeholders to be involved in case investigations that involve users in certain regions, roles, or divisions, consider implementing separate (even if identical) [Insider Risk Management policies](insider-risk-management-policies) that target the different regions and populations. This configuration makes it easier for the right stakeholders to triage and manage cases that are relevant to their roles and regions. Consider creating processes and policies for regions where investigators and reviewers speak the same language as the users. This approach can help streamline the escalation process for Insider Risk Management alerts and cases.

## Plan permissions to support the review and investigation workflow

Depending on how you want to manage Insider Risk Management policies and alerts, assign users to specific role groups to manage different sets of Insider Risk Management features. You can assign users with different compliance responsibilities to specific role groups to manage different areas of Insider Risk Management features. Or, assign all user accounts for designated administrators, analysts, investigators, and viewers to the *Insider Risk Management* role group. For more information, see [Assign Insider Risk Management permissions](insider-risk-management-permissions).

## Understand requirements and dependencies

Depending on how you plan to implement Insider Risk Management policies, you need the proper Microsoft 365 licensing subscriptions. You also need to understand and plan for some solution prerequisites.

**Licensing:** Microsoft offers Insider Risk Management as part of a wide selection of Microsoft 365 licensing subscriptions. For details, see the [Getting started with Insider Risk Management](insider-risk-management-configure#subscriptions-and-licensing) article.

Important

Microsoft currently offers Insider Risk Management in tenants hosted in geographical country/regions supported by Azure service dependencies. To verify that Microsoft supports Insider Risk Management for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

If you don't have an existing Microsoft 365 Enterprise E5 plan and want to try Insider Risk Management, you can [add Microsoft 365](/en-us/microsoft-365/commerce/try-or-buy-microsoft-365) to your existing subscription or [sign up for a trial](https://www.microsoft.com/microsoft-365/enterprise) of Microsoft 365 Enterprise E5.

**Policy template requirements:** Depending on the policy template you choose, understand the following requirements and plan accordingly prior to configuring Insider Risk Management in your organization:

- For the **Data theft by departing users** template, configure a Microsoft 365 HR connector to periodically import resignation and termination date information for users in your organization. For step-by-step guidance to configure the Microsoft 365 HR connector, see the [Import data with the HR connector](import-hr-data) article.
- For the **Data leaks** template, configure at least one Microsoft Purview Data Loss Prevention (DLP) policy to define sensitive information in your organization and to receive insider risk alerts for High Severity DLP policy alerts. For step-by-step guidance to configure DLP policies, see the [Create and Deploy data loss prevention policies](dlp-create-deploy-policy) article.
- For the **Security policy violation** template, enable Microsoft Defender for Endpoint for Insider Risk Management integration in the Defender Security Center to import security violation alerts. For step-by-step guidance to enable Defender for Endpoint integration with Insider Risk Management, see [Configure advanced features in Microsoft Defender for Endpoint](/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-features).
- For the **Risky user** template, configure a Microsoft 365 HR connector to periodically import performance or demotion status information for users in your organization. For step-by-step guidance to configure the Microsoft 365 HR connector, see the [Import data with the HR connector](import-hr-data) article.

## Test with a small group of users in a production environment

Before enabling this solution broadly in your production environment, consider testing the policies with a small set of production users so you can complete the necessary compliance, privacy, and legal reviews in your organization. Evaluating Insider Risk Management in a test environment requires that you generate simulated user actions and other signals to create alerts for triage and cases for processing. This approach might not be practical for many organizations, so we recommend that you test Insider Risk Management with a small group of users in a production environment.

Keep the anonymization feature in policy settings enabled to anonymize user display names in the Insider Risk Management console during this testing to maintain privacy within the tool. This setting helps protect the privacy of users that have policy matches and can help promote objectivity in data investigation and analysis reviews for insider risk alerts.

If you don't see any alerts immediately after configuring an Insider Risk Management policy, it might mean the minimum risk threshold isn't met yet. Check the **Users** page to verify that the policy is triggered and working as expected and to see if users are in-scope for the policy.

## Migrating between Microsoft 365 US Government Cloud and the commercial cloud

If you migrate your organization from the Microsoft 365 US Government Cloud to the worldwide commercial cloud or from the worldwide commercial cloud to the Government Cloud, active cases and alerts don't migrate. Close any alerts and cases before starting the migration.

## Resources for stakeholders

Share Insider Risk Management documentation with the stakeholders in your organization that are included in your management and remediation workflow:

- [Create and manage insider risk policies](insider-risk-management-policies)
- [Investigate insider risk activities](insider-risk-management-activities)
- [Take action on insider risk cases](insider-risk-management-cases)
- [Review case data with the insider risk Content explorer](insider-risk-management-content-explorer)
- [Create insider risk notice templates](insider-risk-management-notices)

## Ready to get started?

Ready to configure Insider Risk Management for your organization? We recommend that you review the following articles:

- [Get started with Insider Risk Management settings](insider-risk-management-settings) to configure global policy settings.
- [Get started with Insider Risk Management](insider-risk-management-configure) to configure prerequisites, create policies, and start receiving alerts.
- [Get started with Insider Risk Management forensic evidence](insider-risk-management-forensic-evidence-configure) for step-by-step guidance to configure forensic evidence capturing in your organization.