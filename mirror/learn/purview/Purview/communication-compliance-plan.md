---
layout: Conceptual
title: Plan for Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-plan
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about planning for using Communication Compliance in your organization.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-08-12T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: d1932321-23c2-8669-7cb8-73b2bcd364e1
document_version_independent_id: d1932321-23c2-8669-7cb8-73b2bcd364e1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-plan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
platformId: 7b0ddc9d-36e8-9c80-0ca7-8f8d859cdd7c
---

# Plan for Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

Before you get started with [Communication Compliance](communication-compliance) in your organization, your information technology and compliance management teams should review important planning activities and considerations. Thoroughly understanding and planning for deployment in the following areas helps ensure that your implementation and use of Communication Compliance features goes smoothly and aligns with the best practices for the solution.

To learn how to fulfill regulatory compliance requirements with Communication Compliance, watch the following video: 

For more information and an overview of the planning process to address compliance and risky activities in your organization, see [Starting an Insider Risk Management program](https://download.microsoft.com/download/b/2/0/b208282a-2482-4986-ba07-15a9b9286df0/pwc-starting-an-insider-risk-management-program-with-pwc-and-microsoft.pdf).

To see how Insider Risk Management and Communication Compliance work together to help minimize data risks from users in your organization, watch the [Microsoft Mechanics video](https://www.youtube.com/watch?v=Ynkfu8OF0wQ).

Important

Communication Compliance is currently available in tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that Communication Compliance is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

## Work with stakeholders in your organization

Identify the appropriate stakeholders in your organization to collaborate for taking actions on Communication Compliance alerts. Consider including the following stakeholders in your initial planning and the end-to-end [Communication Compliance workflow](communication-compliance#workflow):

- Information technology
- Compliance
- Privacy
- Security
- Human resources
- Legal

## Plan for the investigation and remediation workflow

Select dedicated stakeholders to investigate and review the alerts and cases on a regular cadence in the [Microsoft Purview portal](https://purview.microsoft.com). Make sure you understand how you assign users and stakeholders to different Communication Compliance role groups in your organization.

Important

After configuring your role groups, it might take up to 30 minutes for the role group permissions to apply to assigned users across your organization.

### Configure permissions

Six role groups configure initial permissions to manage Communication Compliance features. To make **Communication Compliance** available as a menu option in Microsoft Purview portal and to continue with these configuration steps, you must be assigned to one those groups. For more information, see [Assign permissions in Communication Compliance](communication-compliance-permissions).

### Scoped users

Before you start using Communication Compliance, determine who needs their communications reviewed. In the policy, user email addresses identify individuals or groups of people to apply the policy to. Some examples of these groups are Microsoft 365 Groups, Exchange-based distribution lists, Viva Engage communities, and Microsoft Teams channels. You can also exclude specific users or groups from checking with a specific exclusion group or a list of groups. For more information about groups types supported in Communication Compliance policies, see [Get started with Communication Compliance](communication-compliance-configure#step-3-optional-set-up-groups-for-communication-compliance).

Important

Users covered by Communication Compliance policies must have either a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) license, an Office 365 Enterprise E3 license with the Advanced Compliance add-on, or be included in an Office 365 Enterprise E5 subscription. If you don't have an existing Enterprise E5 plan and want to try Communication Compliance, you can [sign up for a trial of Office 365 Enterprise E5](https://go.microsoft.com/fwlink/p/?LinkID=698279).

### Reviewers

When you create a Communication Compliance policy, you decide who reviews the messages from the scoped users. In the policy, user email addresses identify individuals or groups of people who review scoped communications. All reviewers must have mailboxes hosted on Exchange Online, be assigned to either the *Communication Compliance Analysts* or *Communication Compliance Investigators* role groups, and be assigned in the policy they need to investigate. When you add reviewers to a policy, they automatically receive an email message that notifies them of the assignment to the policy and provides links to information about the review process.

### Groups for scoped users and reviewers

To simplify your setup, we recommend creating groups for people who need their communications reviewed and groups for people who review those communications. If you use groups, you might need several. For example, you might want to identify communications between two distinct groups of people, or you might want to specify a group that isn't in scope. When you assign a Distribution group in the policy, the policy detects all emails from each user in the Distribution group. When you assign a Microsoft 365 group in the policy, the policy detects all emails sent to that group, not the individual emails received by each group member.

Note

Before you create a policy, decide whether you want to apply an **adaptive scope** for users or groups. For more information, see [Adaptive policy scopes for compliance solutions](purview-adaptive-scopes#advantages-of-using-adaptive-scopes).

Adding groups and distribution lists to Communication Compliance policies are part of the overall conditions and rules set, so the maximum number of groups and distribution lists that a policy supports varies depending on the number of conditions you also add to the policy. Each policy supports approximately 20 groups or distribution lists, depending on the number of additional conditions present in the policy.

The following chart can help you configure groups in your organization for Communication Compliance policies:

| Policy Member | Supported Groups | Unsupported Groups |
| --- | --- | --- |
| Scoped users  Excluded users | Distribution groups  Microsoft 365 Groups | Dynamic distribution groups  Nested distribution groups  Mail-enabled security groups  Microsoft 365 groups with dynamic membership |
| Reviewers | None | Distribution groups  Dynamic distribution groups  Nested distribution groups  Mail-enabled security groups |

### Privacy

Protecting the privacy of users that have policy matches is important and can help promote objectivity in data investigation and analysis reviews for Communication Compliance alerts. This setting applies only to user names displayed the Communication Compliance solution. It doesn't affect how names are displayed in other compliance solutions or admin center.

For users with a Communication Compliance match, you can choose one of the following settings in **Communication Compliance settings**:

- **Show anonymized versions of usernames**: User names are anonymized to prevent users in *Communication Compliance Analysts* role group from seeing who is associated with policy alerts. Users in the *Communication Compliance Investigators* role group always see user names, not the anonymized versions. For example, a user 'Grace Taylor' appears with a randomized pseudonym such as 'AnonIS8-988' in all areas of the Communication Compliance experience. Choosing this setting anonymizes all users with current and past policy matches and applies to all policies. User profile information in the Communication Compliance alert details isn't available when you choose this option. However, user names are displayed when adding new users to existing policies or when assigning users to new policies. If you turn off this setting, user names are displayed for all users that have current or past policy matches.
- **Do not show anonymized versions of usernames**: User names are displayed for all current and past policy matches for Communication Compliance alerts. User profile information (the name, title, alias, and organization or department) is displayed for the user for all Communication Compliance alerts.

## Plan for Communication Compliance policies

Creating Communication Compliance policies is quick and easy with the [predefined templates](communication-compliance-policies#policy-templates) for analyzing potentially inappropriate content, sensitive information, and regulatory compliance issues. Custom Communication Compliance policies give you the flexibility to detect and investigate issues specific to your organization and requirements.

When planning for Communication Compliance policies, consider the following areas:

- Consider adding all users in your organization as in-scope for your Communication Compliance policies. Identifying specific users as in-scope for individual policies can be useful in some circumstances. However, most organizations should include all users in Communication Compliance policies optimized for harassment or discrimination detection.
- Decide whether you want to apply an adaptive scope to your Communication Compliance policy. For more information, see [Adaptive policy scopes for retention](purview-adaptive-scopes#advantages-of-using-adaptive-scopes). Creating multiple policies can result in higher administrative overhead.
- Configure the percentage of communications to review at 100% to ensure that policies catch all issues of concern in communications for your organization.
- You can analyze communications from [non-Microsoft sources](communication-compliance-channels#non-microsoft-sources) for data imported into mailboxes in your Microsoft 365 organization. To include review of communications in these platforms, you need to configure a third-party connector to these services before messages meeting policy conditions are detected by a communication policy.
- Policies can support detecting languages other than English in custom Communication Compliance policies. Build a [custom keyword dictionary](communication-compliance-policies#custom-keyword-dictionaries) of offensive words in the language of your choice or build your own machine learning model by using [trainable classifiers](trainable-classifiers-get-started-with) in Microsoft 365.
- All organizations have different communication standards and policy needs. Detect specific keywords by using Communication Compliance [policy conditions](communication-compliance-policies#choose-conditions-for-your-policies) or detect specific types of information with [custom sensitive information types](sit-create-a-custom-sensitive-information-type).

## Migrating between Microsoft 365 US Government Cloud and the commercial cloud

If you migrate your organization from the Microsoft 365 US Government Cloud to the worldwide commercial cloud or from the worldwide commercial cloud to the Government Cloud, active cases and alerts aren't migrated. Close any alerts and cases before starting the migration.

## Create a Communication Compliance policy walkthrough

Want to see an in-depth walkthrough of setting up a new Communication Compliance policy and remediating an alert? Check out the following 15-minute video to see a demonstration of how Communication Compliance policies can help you detect potentially inappropriate messages, investigate potential violations, and remediate compliance issues. 

## Ready to get started?

To configure Communication Compliance for your Microsoft 365 organization, see [Configure Communication Compliance](communication-compliance-configure) or check out the [case study for Contoso](communication-compliance-case-study) and how they quickly configured a Communication Compliance policy to detect potentially inappropriate content in Microsoft Teams, Exchange Online, and Viva Engage communications.