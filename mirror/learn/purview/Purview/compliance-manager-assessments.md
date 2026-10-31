---
layout: Conceptual
title: Build and manage assessments in Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-assessments
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Build assessments from regulatory templates to evaluate and manage compliance requirements in Microsoft Purview Compliance Manager.
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 8bc1bc8c-fb8e-7bd1-c125-b9ec02463730
document_version_independent_id: 8bc1bc8c-fb8e-7bd1-c125-b9ec02463730
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-assessments.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-assessments
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-assessments.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 068677c2-8ddc-cefa-ad5a-ea8ccf97b90f
---

# Build and manage assessments in Microsoft Purview Compliance Manager | Microsoft Learn

Compliance Manager assessments help your organization evaluate its compliance with industry and regional regulations. Setting up the most relevant assessments for your organization can help you implement policies and operational procedures to limit your compliance risk. Ready-to-use regulatory templates for over 360 regulations contain the necessary controls and improvement actions for completing the assessment.

Tip

Get a comprehensive compliance overview before you deploy Microsoft services in your organization. Learn more about [predeployment compliance with Compliance Manager (preview)](compliance-manager-predeployment-compliance).

## Assessments page

All of your assessments are listed on the **Assessments** page Compliance Manager. You can create one assessment that covers multiple services. For example, you can create a single EU GDPR assessment that covers Microsoft 365, Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). The assessment details page shows a breakdown of control progress by service to help you evaluate how you’re doing across all your services. Learn more about monitoring assessment progress from the assessment details page.

Important

The regulations that are available for your organization's use by default depend on your licensing agreement. [Review licensing details](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).

The **Free regulation licenses used/Purchased regulation licenses used** counter near the top of the page shows the number of regulations currently in use out of the total number available for your organization to use. Learn more about [regulation availability](compliance-manager-regulations#regulation-availability-and-licensing).

### Assessment status and details

The assessments page summarizes key information about each assessment:

- **Assessment**: Name of the assessment.
- **Status**: See status types below.
    - **Complete**: All controls have a status of “Passed,” or at least one is passed and the rest are “Out of scope.”
    - **Incomplete**: At least one control has a status of “Failed." Review the failed controls and, within those controls, review both your improvement actions and Microsoft actions to see which have a "Failed" status.
    - **None**: Not all controls have been tested.
    - **In progress**: Improvement actions have a status of “In progress,” “Partial credit,” or “Undetected."
- **Progress**: The percentage of the work done toward completion, as measured by the number of controls successfully tested.
- **Your improvement actions**: The number of completed actions to satisfy implementation of your controls.
- **Microsoft actions**: The number of completed actions to satisfy implementation of Microsoft controls.
- **Group**: The name of the group to which the assessment belongs.
- **Service**: The services covered by the assessment, such as Microsoft 365, Microsoft Azure, or other cloud services.
- **Regulation**: The regulatory template serving as the basis for the assessment.

To filter your view of assessments, follow these steps:

1. Select **Filter** at the top-left corner of your assessments list.
2. On the **Filters** flyout pane, check your desired criteria.
3. Select the **Apply** button. The filter pane closes and you see your filtered view.

You can also modify your view to see assessments by group, product, or regulation by selecting the type of grouping from the **Group** drop-down menu above your assessments list.

## Data protection baseline default assessment

To get you started, Microsoft provides a default **Data Protection Baseline** assessment that's included at all subscription levels. This baseline assessment has a set of controls for key regulations and standards for data protection and general data governance. The Data Protection Baseline assessment draws elements primarily from NIST CSF (National Institute of Standards and Technology Cybersecurity Framework) and ISO (International Organization for Standardization), as well as from FedRAMP (Federal Risk and Authorization Management Program) and GDPR (General Data Protection Regulation of the European Union).

The default Data Protection Baseline assessment is used to calculate your initial compliance score the first time you come to Compliance Manager, before you configure any other assessments. Compliance Manager collects initial signals from your Microsoft 365 solutions. You see at a glance how your organization is performing relative to key data protection standards and regulations, and see suggested improvement actions to take. Compliance Manager becomes more helpful as you build and manage your own assessments to meet your organization's particular needs.

## Assessments for AI regulations

Compliance Manager provides four premium [regulatory templates](compliance-manager-regulations) to help your organization assess, implement, and strengthen its compliance against AI regulations. These templates are applicable to [all generative AI apps that Microsoft Purview supports for AI interactions](ai-microsoft-purview), such as Microsoft 365 Copilot, Security Copilot, ChatGPT Enterprise, Microsoft Foundry, Gemini and DeepSeek.

The AI regulations listed below align with compliance requirements such as monitoring AI interactions and preventing data loss in AI applications:

- EU Artificial Intelligence Act
- ISO/IEC 23894:2023
- ISO/IEC 42001:2023
- NIST AI Risk Management Framework (RMF) 1.0

##### Where to find AI regulation templates

On the **Regulations** page in Compliance Manager, the AI regulations are listed under the **Premium AI templates** header. All other premium regulations are listed under the **Premium templates** header. Using an AI regulation counts toward your purchased premium licenses. Learn more about [regulation availability and licensing](compliance-manager-regulations#regulation-availability-and-licensing).

##### How to use AI regulation templates

The **Recommendations** section from [Data Security Posture Management for AI](dspm-for-ai) provides guided assistance on working with AI regulations. This solution displays recent interactions with sensitive data and recommends actions to take to help you stay compliant with AI regulations.

## Automatic Assessments for AI Apps and Agents in Compliance Manager

Compliance Manager integrates with Azure AI Foundry to automate compliance evaluations for AI models and agents. The Compliance Manager integration with Azure AI Foundry syncs evaluation results directly into Compliance Manager, reducing manual effort and improving regulatory alignment. Organizations benefit from built-in assessments for key AI regulations—including the EU AI Act, NIST AI RMF, and ISO/IEC standards—provided free for six months with Copilot or Agent licenses. The automated compliance evaluation capability enables quick compliance checks without additional purchases, streamlining governance for AI deployments.

### Prerequisites

Before using automatic assessments for AI apps and agents, make sure the following prerequisites are met:

- The admin account must have either the Azure AI Project Manager or Azure AI User RBAC role assigned to the relevant AI Foundry accounts.
- The Azure AI Project Manager or Azure AI User RBAC role access is required to add Agents during assessment creation for the AI Foundry service in Compliance Manager.

### Key Features

- **Scoped Assessments** – Users define the assessment scope directly in Compliance Manager.
- **Comprehensive Action Set** – AI Foundry provides 75 actions, including 15 automated evaluation actions for metrics like reliability, BLEU score, coherence, and fluency.
- **Automated Sync** – Compliance Manager regularly syncs these 15 evaluation actions from AI Foundry, displaying real-time pass/fail status and detailed metrics.
- **Flexible Action Management** – Users can convert automated actions to manual actions through Compliance Manager settings.
- **Manual Update Support** – Allows manual updates for organizations without AI Foundry access.
- **Effort Reduction** – Eliminates repetitive tasks by automatically syncing evaluation results.
- **Detailed Insights** – Provides granular evaluation metrics alongside compliance status for transparency.

## Baseline Assessment for Microsoft 365 Copilot and Copilot Chat

Microsoft Purview Compliance Manager provides a baseline assessment for Microsoft Copilot for Microsoft 365 and Copilot Chat. The baseline assessment for Microsoft Copilot for Microsoft 365 and Copilot Chat is derived from the global AI regulations and includes recommended controls to help organizations maintain compliance and reduce risk.

When a Microsoft Copilot for Microsoft 365 or Copilot Chat license is purchased, the baseline assessment is automatically provisioned in the Microsoft 365 admin center. Administrators can view completed actions and pending tasks within the portal to track compliance progress and implement required controls.

## Initial steps before creating assessments

Listed below are details about steps and information that will help you prepare for creating an assessment:

- Plan a grouping strategy for your assessments.
- Understand [regulatory templates](compliance-manager-regulations), which contain the controls and action recommendations for assessments.
- Set up connectors if you're assessing non-Microsoft services.

## Groups for assessments

When you create an assessment, you must assign it to a group. Groups are containers that allow you to organize assessments in a way that is logical to you, such as by year or regulation, or based on your organization's divisions or geographies. Because groups determine how assessments are organized, we recommend planning a grouping strategy before you create assessments. Below are examples of two groups and their underlying assessments:

- **FFIEC IS assessment 2020**
    - FFIEC IS
- **Data security and privacy assessments**
    - ISO 27001:2013
    - ISO 27018:2014

Different assessments within a group or groups can share improvement actions. Improvement actions can be changes you make within technical solutions mapped to your tenant, like turning on two-factor authentication, or to nontechnical actions you perform outside the system, like instituting a new workplace policy. Any updates in details or status that you make to a technical improvement action will be picked up by assessments across all groups. Nontechnical improvement action updates will be recognized by assessments within the group where you apply them. Shared improvement actions across assessments and groups allow you to implement one improvement action and meet several requirements simultaneously.

#### What to know when working with groups

- You can create a group during the process of creating an assessment.
- Groups can't be standalone entities. A group must contain at least one assessment.
- Group names must be unique within your organization.
- Groups don't have security properties. All permissions are associated with assessments.
- Once you add an assessment to a group, the grouping can't be changed.
- If you add a new assessment to an existing group, common information from assessments in that group are copied to the new assessment.
- Related assessment controls in different assessments within the same group automatically update when completed.
- Groups can contain assessments for the same certification or regulation, but each group can only contain one assessment for a specific product-certification pair. For example, a group can't contain two assessments for Office 365 and NIST CSF. A group can contain multiple assessments for the same product only if the corresponding certification or regulation for each one is different.
- Deleting an assessment breaks the relationship between that assessment and the group.
- Groups can't be deleted.

## Set up connectors

Compliance Manager has an integrated set of connectors to build assessments that cover non-Microsoft services like Salesforce and Zoom. Visit [Working with connectors](compliance-manager-connectors) to learn more and start the setup process.

## Create assessments

To create and modify an assessment, a user must hold a role of Compliance Manager Administration, Compliance Manager Assessor, or Global Administrator. Learn more about [roles and permissions](compliance-manager-setup#set-user-permissions-and-assign-roles).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Before starting to create an assessment, be sure you know which group you'll assign it to, or be prepared to create a new group for this assessment. Read details in the Groups for assessments section. To create an assessment, you use a guided process to select a regulation and designate services.

#### Build a custom assessment

You can modify a regulatory template by adding controls and improvement actions to create a customized assessment. Visit [Build custom assessments (preview)](compliance-manager-assessments-custom) for instructions.

#### Create an assessment using a guided process

1. From your **Assessments** page, select **Add assessment** to begin the assessment creation wizard.
2. On the **Base your assessment on a regulation** page, select **Select regulation** to choose the regulatory template for the assessment. The **Select regulation** flyout page opens.
3. Use the search box to find your desired regulation, then select the check bubble to the left of the regulation name. Select **Save**, confirm your selection, then select **Next**.
4. On the **Add name and group** page, enter values in the following fields:

    - **Assessment name**: Assessment names must be unique. If the name matches another assessment in any group, you receive an error asking you to create a different name.
    - **Assessment group**: Assign your assessment to a group in one of two ways:
        - **Use existing group** to assign it to a group you created; or
        - **Create new group** to which you'll assign the assessment. Enter a name for this group. You can also **Copy data from an existing group**, such as implementation and testing details and documents, by selecting the appropriate boxes.

    When finished, select **Next**.
5. On the **Select services** page, designate which services this assessment applies to (learn more about [multicloud support](compliance-manager-multicloud)) using the **Select services** command. The flyout pane shows which services are available for your chosen regulation. Place a check next to your desired services, then select **Add**. Then select **Next**.

    - If your desired service isn't listed, you can add it as a new service. When you add a new service, the [universal version of the underlying regulation](compliance-manager-regulations#regulations-overview)is used, and you perform manual implementation and testing work. To add a new service:
        - On the **Select services** page, select **Add new service**.
        - Enter a name and description for the service.
        - Select **Add**. The service is listed on the **Service** section of the assessment's details page.
6. If you selected a service that has more than one subscription covered by Microsoft Defender for Cloud, you arrive at a substep for **Select service subscriptions**. Select **Manage subscriptions**. On the flyout pane, a tab for each service displays a list of all subscriptions within that service. All subscriptions are selected by default, but you can remove any by selecting the **X** next to the name. On the **Select services** page, select **Next**.
7. **Review and finish:** Review all your selections and make any necessary edits. When you're satisfied with the settings, select **Create assessment**.

The next screen confirms the assessment was created. When you select **Done**, you're taken to your new assessment's details page. If you see an **Assessment failed** screen after selecting **Create assessment**, select **Try again** to re-create your assessment.

#### Edit an assessment

After creating an assessment, you can edit it to update its name and add or remove services and subscriptions. To update an assessment:

1. From the assessment details page, select the ellipses in the upper right corner and select **Edit assessment**. The assessment update wizard opens.
2. You can update the assessment name on the **Update assessment name** page, or leave it as-is, then select **Next**.
3. On the **Select services** page, add or remove services, then select **Next**.
4. On the **Select service subscriptions** page, select **Manage subscriptions** to make any changes to your subscriptions. Then select **Next**.
5. Review your updates, then select **Modify assessment** to save your changes.

## Monitor assessment progress and controls

Each assessment has a details page that gives an at-a-glance view of your progress in completing the assessment. The page shows how your services are performing, and the status of controls and improvement actions. Expand the **Overview** section at the left side of the page to see basic details about the assessment, including its group, regulation, associated services, completion status, and a description.

The **Progress** tab shows the percentage of progress toward assessment completion. The progress bar displays a breakdown showing the number of points achieved within each service covered by the assessment. Get details on each service in the Assessment progress by service section. See all controls within the assessment and their current status on the Controls tab. Quickly access the status of all your improvement actions for the assessment the Your improvement actions tab. The actions handled by Microsoft for the assessment are listed on the Microsoft actions tab.

#### Assessment progress by service

The **Service** section on the assessment’s **Progress** tab helps you understand how you’re doing with respect to a regulation with each of your services individually, even at the subscription level, and collectively across your organization. The assessment gets its data on available subscriptions and improvement action status from Microsoft Defender for Cloud. Any errors associated with subscription accessibility should be addressed in your Defender for Cloud. See [Configure cloud settings](compliance-manager-cloud-settings) for more information.

Select the **View service details** command, located next to or under the **Assessment progress** bar graph or in the upper-right command bar, to view a flyout pane with more details. The **View service details** flyout pane lists each service and its progress toward completing the assessment. Selecting **View** next to a service name displays another pane that lists each subscription within the service and its status.

On a service's details panel, you see the list of subscriptions within the service that are covered by the assessment. The **Service progress** counter indicates the number of points achieved so far by improvement actions pertaining to the service for the assessment out of the total number of achievable points.

You can add more subscriptions to the service that you want the assessment to cover by editing the assessment.

#### Controls tab

The **Controls** tab displays detailed information for each control in the assessment. The **Control status breakdown** chart shows the status of controls by family (for example, Configuration Management and Incident Response) so you can see at a glance which groupings of controls need attention. The table underneath the breakdown chart lists all controls. You can filter the list by control family, status, and service. The table shows the following details about each control:

- **Control title**
- **Status**: The test status of the improvement actions within the control:
    - **Passed**: All improvement actions have a test status of "passed," or at least one is passed and the rest are "out of scope."
    - **Failed** At least one improvement action has a test status of "failed."
    - **None**: All improvement actions haven't been tested.
    - **Out of scope**: All improvement actions are out of scope for this assessment.
    - **In progress**: Improvement actions have a status other than the ones listed above, which could include "in progress," "partial credit," or "undetected."
- **Control ID**: The control's identification number, assigned by its corresponding regulation, standard, or policy.
- **Points achieved**: The number of points earned by completing actions, out of the total number achievable.
- **Your improvement actions**: The number of your actions completed out of the total number to be done.
- **Microsoft actions**: The number of actions completed by Microsoft.

Select a control from the list to view its details page. A graph indicates the test status of the improvement actions within the control. A table below the graph lists the improvement actions for that control. Select an improvement action from the list to drill into the improvement action's details page, from where you can manage implementation and testing. Get details about [working with improvement actions](compliance-manager-improvement-actions).

#### Your improvement actions tab

The **Improvement actions** tab on the assessment details page lists all your improvement actions for the control. The status bar chart details the aggregated test status of your improvement actions in the assessment so you can quickly gauge what has been tested and what still needs to be done. Hover over or select a test status label to highlight only that status on the bar.

Beneath the bar, a table lists all the actions and key details, including: service, test status, the number of potential and earned points, associated regulations and standards, applicable solution, action type, and control family.

Filter by **Service** to view actions related to a service and their progress. From the table, select an improvement action to go to its details page, from where you can manage implementation and testing. Get details about [working with improvement actions](compliance-manager-improvement-actions).

#### Microsoft actions tab

The Microsoft actions tab appears for assessments based on templates that support Microsoft products. It lists all the actions in the assessment that are managed by Microsoft. The list shows key action details, including: service, test status, points that contribute to your overall compliance score, associated regulations and standards, applicable solution, action type, and control family. Select an improvement action to view its details page.

## Grant user access to individual assessments

When you assign users a Compliance Manager role in the Microsoft Purview portal, they can view or edit data within all assessments by default (review the [Compliance Manager role types](compliance-manager-setup#role-types)). You can restrict user access to only certain assessments by managing user roles from within an assessment. Restricting access in this way can help ensure that users who play a role in overseeing compliance with particular regulations or standards have access only to the data and information they need to perform their duties. (You can also set [user access for regulations](compliance-manager-regulations#grant-user-access-to-regulations), which allows users to access all assessments created for that regulation.)

External users who need access for auditing or other purposes can also be assigned a role for viewing assessments and editing test data. You provide access to external individual by assigning them a Microsoft Entra role. Learn more about [assigning roles](compliance-manager-setup#set-user-permissions-and-assign-roles).

#### Steps for granting access

Follow the steps to grant user access to an assessment.

1. From your **Assessments** page, find the assessment you want to grant access to. Select it to open its details page.
2. In the upper-right corner, select **Manage user access**.
3. A **Manage user access** flyout pane appears. It has three tabs, one for each role of Readers, Assessors, and Contributors. Navigate to the tab for the role you want your user to hold for this assessment. Users who currently have access to the assessment will have a blue box with a check mark to the left of their name.
4. Select the **+ Add** command for the role tab you're on: **Add reader**, or **Add assessor** or **Add contributor**.
5. Another flyout pane appears which lists all the users in your organization. You can select the checkbox next to the username you want to add, or you can enter their name in the search bar and select the user from there. You can select multiple users at once.
6. After making all your selections, select **Add**.

    Note

    If you assign a role to someone who already has an existing role, the new role assignment you choose will override their existing role. In this case, you'll see a confirmation box asking you to confirm the change in role.
7. The flyout pane closes and you arrive back at your assessment details page. A confirmation message at the top confirms the new role assignment for that assessment.

#### Steps for removing access

You can remove a user's access to individual assessments by following the steps below:

1. On the assessment's details page, select **Manage user access**.
2. On the **Manage user access** flyout pane, go the tab corresponding to the user's role you want to remove.
3. Find the user whose role you want to remove. Check the circle to the left of their name, then select the **Remove** command just below the role tab. To remove all users at once, select the **Remove all** command without checking the circle next to every user's name.
4. A **Remove access?** dialog appears, asking you to confirm the removal. Select **Remove access** to confirm the role removal.
5. Select **Save** on the flyout pane. The users' roles will now be removed from the assessment.

Learn how to get a broad [view of all users with access to assessments](compliance-manager-setup#user-access).

##### Note about multiple roles

- A user can have one role that applies to an assessment, while also holding another role that applies broadly to overall Compliance Manager access.

    - For example, if you assigned a user a **Compliance Manager Reader** role, you can also assign that user a **Compliance Manager Assessor** role for a specific assessment. In effect, the user holds the two roles at the same time, but their ability to edit data is limited to the assessment to which they've been assigned the **Assessor** role.
    - Removing an assessment-based role won't remove the user's overall Compliance Manager role if they have one. If you want to change a user's overall role, you have to change it the Microsoft Purview portal. Learn more about [assigning roles and permissions](purview-permissions).
- For an individual assessment, one user can only hold one assessment-based role at a time.

    - For example, if a user holds a reader role for a GDPR assessment and you want to change them to a contributor role, you'll first need to remove their reader role, and then reassign them the reader role.

Note

Admins whose permissions for Compliance Manager were set in Microsoft Entra ID won't appear on the **Manage user access** flyout pane. This means that if a user has access to one or more assessments, and their role is Global Administrator, Compliance Administrator, Compliance Data Administrator, or Security Administrator, they won't appear on this pane. Learn more about [setting Compliance Manager permissions and roles](compliance-manager-setup#set-user-permissions-and-assign-roles).

## Accept updates to assessments

When an update is available for an assessment, you see a notification and have the option to accept the update or defer it for a later time. Updates are available for assessments based on the regulatory templates provided in Compliance Manager. If your organization is using universal templates for assessing other products, inheritance might not be supported.

### What causes an update

An assessment update occurs when there are underlying template changes that impact scoring. Changes might involve adjusting control mapping or other guidance based on regulatory changes or product changes. Assessment updates can originate from your organization and from Microsoft.

If Microsoft updates a Compliance Manager template that you extended, your assessment inherits those updates once you accept them. Your assessment retains the other attributes you applied to the assessment when you extended it.

Custom assessments that you create don't receive any template updates from Microsoft. Custom assessments can receive improvement action updates, but any Microsoft updates to control mapping between assessments and improvement actions don't apply to custom templates.

Note

Updates to assessments apply only at the group level. If you have two assessments built from the same template that exist in two different groups, each assessment will have a pending update notification, and you'll need to accept the update to each assessment in its respective group individually.

#### Where you see assessment update notifications

The assessment details page also shows a **Pending update** label next to the assessment with an update. Select that assessment to get to its details page.

A message near the top of the assessment details page shows that an update is available for that assessment. Select the **Review update** button in the banner to review the specific changes and accept or defer the update.

The assessment details page might also list improvement actions that have a **Pending update** label next to them. Those updates are for specific changes to the improvement actions themselves and need to be accepted separately. Visit [Accepting updates to improvement actions](compliance-manager-improvement-actions#accepting-updates-to-improvement-actions) to learn more.

#### Review update to accept or defer

When you select **Review update** from the assessment details page, a flyout pane appears on the right side of your screen. The flyout pane provides the key details below about the pending update:

- The template title
- Source of the update (Microsoft, your organization, or a specific user)
- The date the update was created
- An overview explaining the update
- Specific details about the changes, including the impact to your compliance score, the amount of progress toward completion of the assessment, and the specific number of changes to improvement actions and controls.

Selecting the **Updated template** command downloads an Excel file containing control data for the version of the template with the pending updates. Selecting the **Current template** command downloads a file of the existing template without the updates.

To accept the update and make the changes to your assessment, select **Accept update**. Accepted changes are permanent.

If you select **Cancel**, the update won't be applied to the assessment. However, you continue to see the **Pending update** notification until you accept the update.

- **Why we recommend accepting updates**: Accepting updates helps ensure you have the most updated guidance on using solutions and taking appropriate improvement actions to help you meet the requirements of the certification at hand.
- **Why you might want to defer an update**: If you're in the middle of completing an assessment, you might want to ensure you finished work on it before you accept an update to the assessment that could disrupt control mapping. You can defer the update for a later time by selecting **Cancel** on the review update flyout pane.

## Export an assessment report

You can export an assessment to an Excel file for compliance stakeholders in your organization or for external auditors and regulators. On the assessment details page, select the **Export actions** in the top right corner of the page, which creates an Excel file you can save and share. The report is a snapshot of the assessment as of the date and time of the export. It contains the details for controls managed by both you and Microsoft, including implementation status, test date, and test results.

## Delete an assessment

Deleting an assessment removes it from the list on your assessments page. Note these important points about deleting assessments:

- **Deleting an assessment is permanent; you cannot get it back.** If you want to use the same assessment again, you need to re-create it.
- If the improvement actions in the assessment don't appear in any other assessment, they're deleted when the assessment is deleted.
- We recommend exporting a report of the assessment before you permanently delete it.

To delete an assessment, follow the steps below:

1. From the **Assessments** page, select the assessment you wish to delete.
2. On the assessment's details page, select **Delete assessment** in the upper-right corner of your screen. If you don't see this option, select the ellipsis (...) in the upper-right corner, then select **Delete assessment** from the list.
3. A window appears asking you to confirm that you want to permanently delete the assessment. Select **Delete assessment** to close the window. You get a confirmation window that your assessment was deleted from Compliance Manager.

Note

You can't delete all of your assessments. Organizations need at least one assessment for Compliance Manager to function properly. If the assessment you want to delete is the only one, add another assessment before deleting the other assessment.