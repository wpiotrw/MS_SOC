---
layout: Conceptual
title: Learn about Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to help minimize risk in your organization with Insider Risk Management in Microsoft Purview.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
locale: en-us
document_id: 82b27e81-1adb-3ff6-63da-49fc1fe08fa5
document_version_independent_id: 82b27e81-1adb-3ff6-63da-49fc1fe08fa5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: a0d5f9d0-1d4b-0087-32c4-93612849ff59
---

# Learn about Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Microsoft Purview Insider Risk Management is a compliance solution that helps minimize internal risks by enabling you to detect, investigate, and act on malicious and inadvertent activities in your organization. With insider risk policies, you can define the types of risks to identify and detect in your organization. You can also set up processes for acting on cases and escalating cases to Microsoft eDiscovery (Premium) if needed. Risk analysts in your organization can quickly take appropriate actions to make sure users are compliant with your organization's compliance standards.

For more information and an overview of the planning process to address potentially risky activities in your organization that might lead to a security incident, see [Starting an Insider Risk Management program](https://download.microsoft.com/download/b/2/0/b208282a-2482-4986-ba07-15a9b9286df0/pwc-starting-an-insider-risk-management-program-with-pwc-and-microsoft.pdf).

Watch the following videos to learn how Insider Risk Management can help your organization prevent, detect, and contain risks while prioritizing your organization values, culture, and user experience:

**Insider Risk Management solution & development**:

**Insider Risk Management workflow**:

Check out the [Microsoft Mechanics video](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) on how Insider Risk Management and Communication Compliance work together to help minimize data risks from users in your organization.

Important

Insider Risk Management is currently available in tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that Insider Risk Management is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

## Modern risk pain points

Managing and minimizing risk in your organization starts with understanding the types of risks found in the modern workplace. Some risks come from external events and factors that you can't directly control. Other risks come from internal events and user actions that you can minimize and avoid. Some examples are risks from illegal, inappropriate, unauthorized, or unethical behavior and actions by users in your organization. These behaviors include a broad range of internal risks from users:

- Leaks of sensitive data and data spillage
- Confidentiality violations
- Intellectual property (IP) theft
- Fraud
- Insider trading
- Regulatory compliance violations

Users in the modern workplace can create, manage, and share data across a broad spectrum of platforms and services. In most cases, organizations have limited resources and tools to identify and mitigate organization-wide risks while also meeting user privacy standards.

Insider Risk Management uses the full breadth of service and third-party indicators to help you quickly identify, triage, and act on risk activity. By using logs from Microsoft 365 and Microsoft Graph, Insider Risk Management enables you to define specific policies to identify risk indicators. These policies help you identify risky activities and act to mitigate these risks.

Insider Risk Management centers around the following principles:

- **Transparency**: Balance user privacy versus organization risk with privacy-by-design architecture.
- **Configurable**: Configurable policies based on industry, geographical, and business groups.
- **Integrated**: Integrated workflow across Microsoft Purview solutions.
- **Actionable**: Provides insights to enable reviewer notifications, data investigations, and user investigations.

## Identifying potential risks with analytics

Insider risk analytics enables you to evaluate potential insider risks in your organization without configuring any insider risk policies. This evaluation can help your organization identify potential areas of higher user risk and help determine the type and scope of Insider Risk Management policies you might consider configuring. This evaluation can also help you determine needs for additional licensing or future optimization of existing insider risk policies.

For more information about insider risk analytics, see [Insider Risk Management settings: Analytics](insider-risk-management-settings-analytics).

## Get started with recommended actions

Whether you're setting up Insider Risk Management for the first time or getting started with creating new policies, the new [recommended actions](insider-risk-management-configure#recommended-actions) experience can help you get the most out of Insider Risk Management capabilities. Recommended actions include setting up permissions, choosing policy indicators, creating a policy, and more.

## Workflow

The Insider Risk Management workflow helps you identify, investigate, and take action to address internal risks in your organization. With focused policy templates, comprehensive activity signaling across the Microsoft 365 service, and alert and case management tools, you can use actionable insights to quickly identify and act on risky behavior.

Identifying and resolving internal risk activities and compliance issues with Insider Risk Management uses the following workflow:

![Insider Risk Management workflow.](media/insider-risk-workflow.png)

### Policies

You create [Insider Risk Management policies](insider-risk-management-policies) by using predefined templates and policy conditions that define which triggering events and risk indicators to examine in your organization. These conditions include how risk indicators are used for alerts, which users are included in the policy, which services are prioritized, and the detection time period.

To quickly get started with Insider Risk Management, select from the following policy templates:

- [Data theft by departing users](insider-risk-management-policy-templates#data-theft-by-departing-users)
- [Data leaks](insider-risk-management-policy-templates#data-leaks)
- [Data leaks by priority users](insider-risk-management-policy-templates#data-leaks-by-priority-users)
- [Data leaks by risky users](insider-risk-management-policy-templates#data-leaks-by-risky-users)
- [Patient data misuse (preview)](insider-risk-management-policy-templates#patient-data-misuse-preview)
- [Risky Agents](insider-risk-management-policy-templates#risky-agents-preview)
- [Risky AI usage](insider-risk-management-policy-templates#risky-ai-usage)
- [Risky browser usage (preview)](insider-risk-management-policy-templates#risky-browser-usage-preview)
- [Security policy violations](insider-risk-management-policy-templates#security-policy-violations)
- [Security policy violations by departing users](insider-risk-management-policy-templates#security-policy-violations-by-departing-users)
- [Security policy violations by risky users](insider-risk-management-policy-templates#security-policy-violations-by-risky-users)
- [Security policy violations by priority users](insider-risk-management-policy-templates#security-policy-violations-by-priority-users)

### Alerts

Risk indicators automatically generate alerts when they match policy conditions. You can see these alerts in the [Alerts dashboard](insider-risk-management-activities#standard-alert-dashboard) or the [Triage Agent dashboard](insider-risk-management-activities#triage-agent-in-insider-risk-management-dashboard). These dashboards provide a quick view of all alerts that need review, open alerts over time, and alert statistics for your organization. All policy alerts display the following information to help you quickly identify the status of existing alerts and new alerts that need action:

- ID
- Users
- Alert
- Status
- Alert severity
- Time detected
- Case
- Case status
- Risk factors

### Triage

New user activities that need investigation automatically generate alerts and assign them a *Needs review* status. Reviewers can quickly identify, review, evaluate, and triage these alerts.

Resolve alerts by opening a new case, assigning the alert to an existing case, or dismissing the alert. With alert filters, you can quickly identify alerts by status, severity, or time detected. As part of the triage process, reviewers can view alert details for the activities identified by the policy, view user activity associated with the policy match, see the severity of the alert, and review user profile information.

![Insider Risk Management triage.](media/insider-risk-triage.png)

### Investigate

Quickly investigate all risky activities for a selected user with [User activity reports (preview)](insider-risk-management-activities#review-the-user-activity-tab). These reports let investigators in your organization examine activities for specific users during a defined time period without temporarily or explicitly assigning them to an Insider Risk Management policy. After examining activities for a user, investigators can dismiss individual activities as benign, share or email a link to the report with other investigators, or choose to assign the user temporarily or explicitly to an Insider Risk Management policy.

[Cases](insider-risk-management-cases) are created for alerts that require deeper review and investigation of the activity details and circumstances around the policy match. The **Case dashboard** provides an all-up view of all active cases, open cases over time, and case statistics for your organization. Reviewers can quickly filter cases by status, the date the case was opened, and the date the case was last updated.

Selecting a case on the case dashboard opens the case for investigation and review. This step is the heart of the Insider Risk Management workflow. This area synthesizes risk activities, policy conditions, alert details, and user details into an integrated view for reviewers. The primary investigation tools in this area are:

- **User activity**: An interactive chart automatically displays user risk activity. It plots activities over time and by risk level for current or past risk activities. Reviewers can quickly filter and view the entire risk history for the user and drill into specific activities for more details.
- **Content explorer**: The Content explorer automatically captures and displays all data files and email messages associated with alert activities. Reviewers can filter and view files and messages by data source, file type, tags, conversation, and many more attributes.
- **Case notes**: Reviewers can provide notes for a case in the Case Notes section. This list consolidates all notes in a central view and includes reviewer and date submitted information.

![Insider Risk Management investigation.](media/insider-risk-investigate.png)

Additionally, the new [Audit log (preview)](insider-risk-management-audit-log) enables you to stay informed of the actions taken on Insider Risk Management features. This resource allows an independent review of the actions taken by users assigned to one or more Insider Risk Management role groups.

### Action

After investigating cases, reviewers can quickly act to resolve the case or collaborate with other risk stakeholders in your organization. If users accidentally or inadvertently violate policy conditions, reviewers can send a simple reminder notice to the user from notice templates you can customize for your organization. These notices might serve as simple reminders or might direct the user to refresher training or guidance to help prevent future risky behavior. For more information, see [Insider Risk Management notice templates](insider-risk-management-notices).

In more serious situations, you might need to share the Insider Risk Management case information with other reviewers or services in your organization. Insider Risk Management tightly integrates with other Microsoft Purview solutions to help you with end-to-end risk resolution.

- **eDiscovery (Premium)**: Escalating a case for investigation allows you to transfer data and management of the case to Microsoft Purview eDiscovery (Premium). eDiscovery (Premium) provides an end-to-end workflow to preserve, collect, review, analyze, and export content that's responsive to your organization's internal and external investigations. It allows legal teams to manage the entire legal hold notification workflow. To learn more about eDiscovery (Premium) cases, see [Overview of Microsoft Purview eDiscovery (Premium)](ediscovery-overview).
- **Office 365 Management APIs integration (preview)**: Insider Risk Management supports exporting alert information to security information and event management (SIEM) services via the Office 365 Management APIs. Having access to alert information in the platform that best fits your organization's risk processes gives you more flexibility in how to act on risk activities. To learn more about exporting alert information with Office 365 Management APIs, see [Export alerts](insider-risk-management-settings-alerts).

## Scenarios

Insider Risk Management can help you detect, investigate, and take action to mitigate internal risks in your organization in several common scenarios:

### Data theft by departing users

When users leave an organization, either voluntarily or as the result of termination, legitimate concerns often arise that company, customer, and user data are at risk. Users might innocently assume that project data isn't proprietary, or they might be tempted to take company data for personal gain and in violation of company policy and legal standards. Insider Risk Management policies that use the [Data theft by departing users](insider-risk-management-policy-templates#policy-templates) policy template automatically detect activities typically associated with this type of theft. With this policy, you automatically receive alerts for suspicious activities associated with data theft by departing users so you can take appropriate investigative actions. You need to configure a [Microsoft 365 HR connector](import-hr-data) for your organization for this policy template.

### Intentional or unintentional leak of sensitive or confidential information

In most cases, users try their best to properly handle sensitive or confidential information. But occasionally users make mistakes and information is accidentally shared outside your organization or in violation of your information protection policies. In other circumstances, users might intentionally leak or share sensitive and confidential information with malicious intent and for potential personal gain. Insider Risk Management policies created using the following policy templates automatically detect activities typically associated with sharing sensitive or confidential information:

- [Data leaks](insider-risk-management-policy-templates#data-leaks)
- [Data leaks by priority users](insider-risk-management-policy-templates#data-leaks-by-priority-users)
- [Data leaks by risky users](insider-risk-management-policy-templates#data-leaks-by-risky-users)
- [Risk AI usage](insider-risk-management-policy-templates#risky-ai-usage)

### Intentional or unintentional security policy violations (preview)

Users typically have a large degree of control when managing their devices in the modern workplace. This control might include permissions to install or uninstall applications needed in the performance of their duties or the ability to temporarily disable device security features. Whether this risk activity is inadvertent, accidental, or malicious, this conduct can pose risk to your organization and is important to identify and act to minimize. To help identify these risky security activities, the following Insider Risk Management security policy violation templates scores security risk indicators and use Microsoft Defender for Endpoint alerts to provide insights for security-related activities:

- [Security policy violations](insider-risk-management-policy-templates#security-policy-violations)
- [Security policy violations by departing users](insider-risk-management-policy-templates#security-policy-violations-by-departing-users)
- [Security policy violations by priority users](insider-risk-management-policy-templates#security-policy-violations-by-priority-users)
- [Security policy violations by risky users](insider-risk-management-policy-templates#security-policy-violations-by-risky-users)

### Policies for users based on position, access level, or risk history

Users in your organization might have different levels of risk depending on their position, level of access to sensitive information, or risk history. This structure might include members of your organization's executive leadership team, IT administrators that have extensive data and network access privileges, or users with a past history of risky activities. In these circumstances, closer inspection and more aggressive risk scoring are important to help surface alerts for investigation and quick action. To help identify risky activities for these types of users, you can create priority user groups and create policies from the following policy templates:

- [Security policy violations by priority users](insider-risk-management-policy-templates#security-policy-violations-by-priority-users)
- [Data leaks by priority users](insider-risk-management-policy-templates#data-leaks-by-priority-users)

### Healthcare (preview)

For organizations in the healthcare industry, recent studies found a very high rate of insider-related data breaches. Detecting misuse of patient data and health record information is a critical component of safeguarding patient privacy and complying with compliance regulation such as the Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act. Patient data misuse can range from accessing privileged patient records to accessing records of patients from family or neighbors with malicious intent. To help identify these types of risky activities, the following Insider Risk Management policy template uses the Microsoft 365 HR connector and a healthcare-specific data connector to start scoring risk indicators relating to behaviors that can occur within your electronic heath record (EHR) systems:

- [Patient data misuse (preview)](insider-risk-management-policy-templates#patient-data-misuse-preview)

### Actions and behaviors by risky users

Employment stressor events can impact user behavior in several ways that relate to insider risks. These stressors might be a poor performance review, a position demotion, or the user being placed on a performance review plan. Stressors might also result in potentially inappropriate behavior such as users sending potentially threatening, harassing, or discriminatory language in email and other messages. Though most users don't respond maliciously to these events, the stress of these actions can result in some users behaving in ways that they might not normally consider during normal circumstances. To help identify these types of potentially risky activities, the following Insider Risk Management policy templates can use the HR connector and/or integration with a [dedicated Communication Compliance policy](communication-compliance-policies#integrate-communication-compliance-with-microsoft-purview-insider-risk-management) to bring users into scope for Insider Risk Management policies and start scoring risk indicators relating to behaviors that might occur:

- [Data leaks by risky users](insider-risk-management-policy-templates#data-leaks-by-risky-users)
- [Risk AI usage](insider-risk-management-policy-templates#risky-ai-usage)
- [Risky browser usage (preview)](insider-risk-management-policy-templates#risky-browser-usage-preview)
- [Security policy violations by risky users](insider-risk-management-policy-templates#security-policy-violations-by-risky-users)

### Visual context for potentially risky user activities with forensic evidence

Having visual context is crucial for security teams during forensic investigations to get better insights into potentially risky user activities that might lead to a security incident. This insight might include visual capturing of these activities to help evaluate if they're indeed risky or taken out of context and not potentially risky. For activities that are determined to be risky, having forensic evidence captures can help investigators and your organization better mitigate, understand, and respond to these activities. To help with this scenario, [enable forensic evidence capturing](insider-risk-management-forensic-evidence) for online and offline devices in your organization.

## Ready to get started?

- See [Plan for Insider Risk Management](insider-risk-management-plan) to prepare for enabling Insider Risk Management policies in your organization.
- See [Get started with Insider Risk Management settings](insider-risk-management-settings) to configure global settings for insider risk policies.
- See [Get started with Insider Risk Management](insider-risk-management-configure) to configure prerequisites, create policies, and start receiving alerts.