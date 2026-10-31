---
layout: Conceptual
title: Case study - Contoso configures a Communication Compliance policy to identify potentially inappropriate text | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-case-study
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: A case study for Contoso and how they quickly configure a Communication Compliance policy to detect potentially inappropriate text in Microsoft Teams, Exchange Online, and Viva Engage communications.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.custom:
- admindeeplinkMAC
- admindeeplinkCOMPLIANCE
- admindeeplinkEXCHANGE
- sfi-image-nochange
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: 1f194208-6185-f76c-afb5-015de379e561
document_version_independent_id: 1f194208-6185-f76c-afb5-015de379e561
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-case-study.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-case-study
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-case-study.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: f7d0ba72-a7e2-42d2-5f46-664f9aa86c37
---

# Case study - Contoso configures a Communication Compliance policy to identify potentially inappropriate text | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

[Microsoft Purview Communication Compliance](communication-compliance) helps you minimize communication risks by helping you detect, capture, and act on messages with potentially inappropriate text in your organization. Potentially inappropriate text might include profanity, threats, harassment, and adult content. Predefined and custom [policies](communication-compliance-policies) allow you to review internal and external communications for policy matches, so designated reviewers can examine them. Reviewers can [investigate alerts](communication-compliance-investigate-remediate#investigate-and-remediate-communication-compliance-alerts) for email, Microsoft Teams, Viva Engage, or third-party communications throughout your organization and take appropriate [remediation actions](communication-compliance-investigate-remediate#investigate-and-remediate-communication-compliance-alerts) to make sure they're compliant with your organization's message standards.

The Contoso Corporation is a fictional organization that needs to quickly configure a policy to detect potentially inappropriate text. They use Microsoft 365 primarily for email, Microsoft Teams, and Viva Engage support for their users, but have new requirements to enforce company policy around workplace harassment. Contoso IT administrators and compliance specialists have a basic understanding of the fundamentals of working with Microsoft 365 and are looking for end-to-end guidance for how to quickly get started with Communication Compliance.

This case study covers the basics for quickly configuring a Communication Compliance policy to detect potentially inappropriate text. This guidance includes:

- Step 1: Planning for Communication Compliance
- Step 2: Accessing Communication Compliance
- Step 3: Configuring prerequisites and creating a Communication Compliance policy
- Step 4: Investigate and remediate alerts

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Step 1: Planning for Communication Compliance

Contoso IT administrators and compliance specialists attend online webinars about compliance solutions in Microsoft Purview and decide that Communication Compliance policies can help them meet the updated corporate policy requirements for reducing workplace harassment. Working together, they develop a plan to create and enable a Communication Compliance policy to detect potentially inappropriate messages. This configuration includes detecting text for chats sent in Microsoft Teams, private messages and community conversations in Viva Engage, and in email messages sent in Exchange Online.

Their plan includes identifying the:

- IT administrators who need access to Communication Compliance features.
- Compliance specialists who need to create and manage Communication Compliance policies.
- Compliance specialists and other colleague in other departments (Human Resources, Legal, etc.) who need to investigate and remediate Communication Compliance alerts.
- Users who are in-scope for the Communication Compliance potentially inappropriate text policy.

### Licensing

First, confirm whether Contoso's Microsoft 365 licensing includes support for the Communication Compliance solution. To access and use Communication Compliance, Contoso IT administrators need to verify Contoso has a supported subscription and assigned the appropriate licenses to users. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Communication Compliance.

Contoso IT administrators take the following steps to verify the licensing support for Contoso:

1. IT administrators sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) and go to Microsoft 365 admin center &gt; **Billing** &gt; [**Licenses**](https://go.microsoft.com/fwlink/p/?linkid=842264).
2. They confirm that they have one of the [license options](communication-compliance-configure#subscriptions-and-billing) that includes support for Communication Compliance.

![Communication Compliance licensing.](media/communication-compliance-case-licenses.png)

### Permissions for Communication Compliance

Five [role groups used to configure permissions](communication-compliance-permissions) manage Communication Compliance features. To make **Communication Compliance** available as a menu option in Microsoft Purview portal and to continue with these configuration steps, assign Contoso administrators the *Communication Compliance Admins* role.

Contoso decides to use the *Communication Compliance* role group and assign all the Communication Compliance administrators, analysts, investigators, and viewers to the group. This role group configuration makes it easier for Contoso to get started quickly and best fits their compliance management requirements.

Use the [Microsoft Purview portal](purview-portal) to select the *Communication Compliance* role group.

1. Contoso IT admins sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in their Microsoft 365 organization.
2. The administrators select **Settings** in the upper-right corner of the page, then select **Role groups** in the left navigation pane.
3. The administrators select the *Communication Compliance* role group, then select **Edit**.
4. The administrators select **Choose users**, then select the checkboxes for all the Contoso users who manage Communication Compliance and investigate and review alerts.
5. The administrators choose **Select**, then choose **Next** to review the role group changes.
6. They select **Save** to add Contoso users to the role group.

## Step 2: Accessing Communication Compliance

After configuring the permissions for Communication Compliance, Contoso IT administrators and compliance specialists assigned to the Communication Compliance role group can access the Communication Compliance solution in Microsoft Purview. Contoso IT administrators and compliance specialists have a couple of ways to access Communication Compliance and get started creating a new policy:

- Starting from the Microsoft Purview portal
- Starting directly from the Communication Compliance solution

### Starting from the Microsoft Purview portal

Admins and compliance specialists can sign in to the [Microsoft Purview portal](purview-portal) and then go to the Communication Compliance solution.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select the **Communication Compliance** solution.

### Starting directly from the Communication Compliance solution

To quickly access the solution, sign in directly. Sign directly into Communication Compliance in the [Microsoft Purview portal](https://df.purview.microsoft.com/cc).

When they select one of these links, Contoso IT administrators and compliance specialists go to the Communication Compliance page where they can quickly review the status of alerts and create new policies from the predefined templates.

![Communication Compliance home.](media/communication-compliance-home.png)

## Step 3: Configuring prerequisites and creating a Communication Compliance policy

To get started with a Communication Compliance policy, Contoso IT administrators need to configure several prerequisites before setting up the new policy to detect potentially inappropriate text. After completing these prerequisites, Contoso IT administrators and compliance specialists can configure the new policy. Compliance specialists can start investigating and remediating any generated alerts.

### Enabling auditing in Microsoft 365

Communication Compliance requires audit logs to show alerts and track remediation actions that reviewers take. The audit logs summarize all activities associated with a defined organizational policy or anytime there's a change to a Communication Compliance policy.

Contoso IT administrators review and complete the [step-by-step instructions](audit-search) to turn on auditing. After they turn on auditing, a message displays that says the audit log is being prepared and that they can run a search in a couple of hours after the preparation is complete. The Contoso IT administrators only need to perform this action once.

### Configuring Viva Engage tenant for Native Mode

Communication Compliance requires that the Viva Engage tenant for an organization is in Native Mode to detect potentially inappropriate text in private messages and public community conversations.

Contoso IT administrators make sure they review the information in the [Overview of Viva Engage Native Mode in Microsoft 365 article](/en-us/viva/engage/overview-native-mode) and follow the steps for running the migration tool in the [Configure your Viva Engage network for Native Mode for Microsoft 365](/en-us/viva/engage/automatic-migration-native-mode) article.

### Setting up a group to add users to the policy

Contoso compliance specialists want to add all users to the communication policy that detects potentially inappropriate text. They could decide to add each user account to the policy separately, but they decide it's easier and saves time to use an **All Users** distribution group for the users for this policy.

They need to create a new group to include all Contoso users, so they take the following steps:

1. Contoso IT administrators sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) and go to Microsoft 365 admin center &gt; **Groups** &gt; [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. They select **Add a group** and complete the workflow to create a new *Microsoft 365 group* or *Distribution group*.

    ![Groups.](media/communication-compliance-case-all-employees.png)
3. After they create the new group, they add all Contoso users to the new group. They open the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) and navigate to **Exchange admin center** &gt; **recipients** &gt; [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2183233). The Contoso IT administrators select the Membership area and the new *All Employees* group they created and select the **Edit** control to add all Contoso users to the new group in the workflow.

    ![Exchange admin center.](media/communication-compliance-case-eac.png)

### Creating the policy to detect potentially inappropriate text

After completing all the prerequisites, the IT administrators and compliance specialists for Contoso are ready to configure the Communication Compliance policy to detect potentially inappropriate text. By using the text policy template, you can quickly and easily configure this new policy.

1. Contoso IT admins sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in their Microsoft 365 organization.
2. They go to the **Communication Compliance** solution. This step opens a dashboard with quick links to Communication Compliance policy templates.
3. They choose **Policies** in the left navigation, select **Create policy**, and then select **Detect inappropriate text** to open the *Detect communications for inappropriate text* template.
4. In the policy template workflow, the Contoso IT administrators and compliance specialists work together to complete the three required fields: **Policy name**, **Users or groups in scope**, and **Reviewers**.
5. Since the policy workflow already suggests a name for the policy, the IT administrators and compliance specialists decide to keep the suggested name and focus on the remaining fields. They select the *All users* group for the **Users or groups in scope** field and select the compliance specialists who should investigate and remediate policy alerts for the **Reviewers** field. To finish configuring the policy and start gathering alert information, they select **Create policy**.

## Step 4: Investigate and remediate alerts

After configuring the Communication Compliance policy to detect potentially inappropriate text, the Contoso compliance specialists investigate and remediate any alerts the policy generates. It can take up to an hour for the policy to fully process communications in all the communication source channels and for alerts to show up in the **Alert dashboard**.

When alerts are generated, Contoso compliance specialists follow the [workflow instructions](communication-compliance-investigate-remediate) to investigate and remediate potentially inappropriate text issues.