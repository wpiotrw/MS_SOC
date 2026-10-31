---
layout: Conceptual
title: Working with improvement actions in Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to implement and test controls by working with improvement actions in Microsoft Purview Compliance Manager. Automate testing, store documentation, and export reports.
locale: en-us
document_id: 7636d042-99e2-ba59-25e0-d59a2117fa9e
document_version_independent_id: 7636d042-99e2-ba59-25e0-d59a2117fa9e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-improvement-actions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-improvement-actions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-improvement-actions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
- https://authoring-docs-microsoft.poolparty.biz/devrel/8e3fdb08-a059-4277-98f6-c0e21e940707
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
- https://authoring-docs-microsoft.poolparty.biz/devrel/88291526-9c74-4f87-878c-de0a82134421
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: fc1a6a0c-357c-f54e-f728-63e5e1507dfc
---

# Working with improvement actions in Microsoft Purview Compliance Manager | Microsoft Learn

## Overview

Improvement actions help centralize your compliance activities. Each improvement action recommends an action to take, with detailed guidance intended to help you align with data protection regulations and standards. Improvement actions can be assigned to users in your organization to perform implementation and testing work. You can also store evidence, add notes, and record status updates within the action. Many improvement actions come with automatic testing and monitoring.

Compliance Manager works within a shared responsibility model where some actions are completed by you and others are completed automatically by Microsoft in order to meet the requirements of a regulation, standard, or certification. The actions listed on the Improvement actions tab in Compliance Manager are the ones that your organization is responsible for completing.

Tip

Visit the [Compliance Manager glossary](compliance-manager-glossary) for helpful definitions of many of the terms on this page.

## Automated testing and monitoring

While some improvement actions must be manually tested by your organization, many actions can be automatically tested and monitored for you. Compliance Manager automatically identifies settings in your Microsoft 365 environment and your multicloud environment that help determine when certain configurations meet improvement action implementation requirements. Compliance Manager utilizes four types of automation, explained below.

#### Built-in automation

Compliance Manager has built-in functionality to receive signals from other Microsoft solutions and non-Microsoft services. Compliance Manager detects signals from other Microsoft Purview solutions that your organization may subscribe to, including Data Lifecycle Management, Information Protection, Data Loss Prevention, Communication Compliance, and Insider Risk Management. Compliance Manager also detects signals from Microsoft Priva (this capability is in preview). The automation applies specifically to the solution and isn’t scoped to cloud services. Learn more about [automatic testing settings](compliance-manager-setup#testing-source-for-automated-testing).

#### Microsoft Secure Score automation

Compliance Manager detects signals from complementary improvement actions that are monitored by Microsoft Secure Score. Through these signals, Compliance Manager can automatically test certain improvement actions in order to provide continuous control assessment. When an improvement action is successfully tested and implemented, you receive the maximum possible points for that action, which gets credited to your overall compliance score.

#### Microsoft Defender for Cloud automation

Integration with Defender for Cloud allows Compliance Manager to facilitate improvement actions and provide continuous monitoring across multiple Microsoft and non-Microsoft cloud services, such as Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). The cloud infrastructure of this monitoring means that action status can be evaluated and graded at the subscription level of the intended service. You can see specific implementation and testing results for each improvement action within each subscription of your service. The overall score you receive for the improvement action is an aggregate of the individual scores of each subscription within that service. Learn more about [multicloud support](compliance-manager-multicloud) and [scoring](compliance-manager-scoring).

#### Connectors

We're rolling out a selection of connectors built specifically for Compliance Manager to support other non-Microsoft services. Connectors for Salesforce and Zoom are available now, with more connectors releasing soon. Learn more at [Working with connectors in Compliance Manager](compliance-manager-connectors).

Note

An improvement action that is set to automatic testing can be changed to manual testing, unless that action is implemented through Microsoft Defender for Cloud.

## Testing type

Compliance Manager provides options for how to test improvement actions. On the improvement action’s details page, the **Testing type** status in the top information bar shows how the action is tested. From here you can choose how you want the action to be tested: **Manual** or **Automatic**.

Note

Testing source can’t be changed on actions for services supported by Defender for Cloud. If you don’t agree with an automated testing result, you can go to the related assessment in Defender for Cloud to alter the testing logic and scope.

#### Manual

Improvement actions set for manual testing are actions that you manually test and implement. You set the necessary implementation and test status states, and upload any evidence files on the **Evidence** tab. For some actions, this is the only available method for testing improvement actions.

#### Automatic

Certain improvement actions can be automatically tested by Compliance Manager. [Get details](compliance-manager-setup#testing-source-for-automated-testing) on which improvement actions can and can't be tested automatically.

For those improvement actions that can be automatically tested, you'll see the **Automatic** option for **Testing type**. Compliance Manager detects signals from other compliance solutions and cloud services. When signals indicate that an improvement action has been successfully implemented, you automatically receive the eligible points for that action, which factor into scores for related controls and assessments. Learn more about [scoring](compliance-manager-scoring).

Automatic testing is on by default for all eligible improvement actions. You can adjust these settings to automatically test only certain improvement actions, or you can turn off automatic testing for all actions. Learn more about how automated testing works and how to adjust your settings at [Set up automated testing](compliance-manager-setup#manage-automated-testing-settings).

## Improvement actions page

All of the improvement actions managed by your organization are listed on the **Improvement actions** page in Compliance Manager. The list of improvement actions displays basic information related to each action, such as the regulations they correspond to, testing status and source, owner, and action type. See below for descriptions of some of the columns. Filter the columns to customize your view.

##### Points achieved

Each improvement action is worth a number of points that contribute to your overall compliance score. This column shows how many points have been earned out of the total available to achieve.

##### Service

The service is the data source, such as Microsoft Azure or Amazon Web Services, that the improvement action assesses and impacts.

##### Group

This column shows the assessment groups that the improvement action is associated with. Learn more about [assessment groups](compliance-manager-assessments#groups-for-assessments).

##### Solutions

The solutions are the location where you perform the recommended action; for example, in Microsoft Communication Compliance, Microsoft Priva, or Microsoft Defender for Cloud.

##### Categories

Compliance Manager groups improvement actions into general categories to help you understand which areas need attention in order to bolster your overall compliance posture. The categories are: Control Access, Discover and Respond, Govern Information, Infrastructure Cloud, Manage Compliance, Manage Devices, Manage Internal Risks, Privacy Management, Protect Against Threats, and Protect Information.

##### Action type

Improvement actions can be technical or nontechnical in nature:

- **Technical actions** are implemented by interacting with the technology of a solution (for example, changing a configuration).
- **Nontechnical actions** are managed by your organization and implemented in ways other than working with the technology of a solution. There are two types of nontechnical actions: **documentation** and **operational**.

Learn how action type affects [scoring for improvement actions](compliance-manager-scoring).

## Improvement action details page

Select an improvement action from the list on the **Improvement actions** page to view the action's details page. The details page provides detailed implementation guidance and a link to launch you into the appropriate solution or service. Here’s what you can do from an improvement actions details page:

- Get basic status quickly from the top information bar.
- Assign an owner, who is responsible for performing the work.
- Review implementation guidance on the **Details** tab. Follow a direct link into the recommended solution to start implementation work and add implementation notes.
- Review the action’s status within your cloud services’ subscriptions from the **Details** tab and drill into subscription-level details.
- Upload and store evidence files and links on the **Evidence** tab.
- Check the **Related controls** tab to see all the controls that include the improvement action. You can filter the control list by regulation.

## Implementation and testing

### Assign an owner

To begin implementation work on an improvement action, you can do the work yourself or assign it to another user as an owner. The owner could be a business policy owner, an IT implementer, or another employee with responsibility to perform the task. Once you identify the appropriate assignee, be sure they hold a sufficient [Compliance Manager role](compliance-manager-setup#set-user-permissions-and-assign-roles) to perform the work.

To assign an owner to an improvement action, open the improvement action’s details page. In the **Owner** box in the information bar at the top of the page, begin typing a user’s name and select the name when it appears. The assigned user receives an email explaining that the improvement action has been assigned to them, with a direct link to the improvement action.

Note

US Government Community (GCC) High and Department of Defense (DoD) customers won't receive an email when improvement actions are assigned to them.

##### Assign multiple improvement actions to a single user

You can assign multiple improvement actions to one user by following these steps:

1. In Compliance Manager, go to the **Improvement actions** page.
2. Select the checkbox to the left of the improvement actions you want to assign.
3. Select **Assign to user** at the top of the improvement actions table. The **Assign improvement actions** flyout pane appears.
4. Enter a user’s name in the search bar to search for the user, or select a name from the list of suggested people. After choosing the user, select **Assign**.

You arrive back at your **Improvement actions** page with the new owner listed in the **Assigned to** column for the actions you assigned.

### Implementation work

Implementation guidance varies depending on whether you go to Microsoft Defender for Cloud to perform the work to complete the action. Learn more about [multicloud support](compliance-manager-multicloud). Instructions for each action type’s implementation are below.

##### Actions that you implement in Defender for Cloud

On an improvement action’s details page, view the **Testing source** on the top information bar. If the testing source is **Defender for Cloud**, then the action pertains to cloud services such as Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP), and the action is implemented and monitored using Compliance Manager’s integration with Defender for Cloud. These actions belong to the category of **infrastructure cloud**. Whether they can be automatically tested or not depends on the action type:

- Technical actions are automatically tested and monitored.
- Non-technical actions must be manually tested.

View the implementation instructions for each action type below.

**Subscription monitoring**

For actions implemented in Defender for Cloud, the **Subscription monitoring** section on the **Details** tab shows a list of all related subscriptions ([view glossary](compliance-manager-glossary)). This view provides a more granular view into the action’s status across each service’s subscriptions. Select a subscription name to view a flyout pane with implementation details, virtual resources status, and the related assessments.

**Implementation for manual actions**:

- On the improvement action details page, review the **How to implement** guidance and perform the necessary steps. This may involve non-technical work that takes place offline.
- Each subscription listed under **Subscription monitoring** needs to have its status updated. Each subscription contains a single virtual resource, which represents the subscription itself. Select the subscription name to bring up a flyout pane for that subscription. Select the appropriate status, date, and enter notes.
- When you’re done, select **Save**.

Note

Manual actions don’t synchronize status between Compliance Manager and Defender for Cloud. You can update the status in either location, however the statuses won't synch.

**Implementation for automatic actions**:

- Select each subscription, one at a time, listed under **Subscription monitoring**.
- If a subscription shows that there are virtual resources that aren't complete, select the subscription and on the flyout pane, select the **Virtual resources** tab.
- Inspect the status of each resource to determine which require ones require remediation.
- For the resources needing remediation, review the **How to implement** guidance. Then select **Go to Defender for Cloud** to make the necessary changes.

Updates to the improvement action’s status show within 24 hours.

##### Actions that you don't implement in Defender for Cloud

The implementation guidance on the **Details** tab provides instructions and a link into the solution where you go to perform the implementation work. To perform and record your implementation work:

1. Review the **How to implement** guidance and follow the link into the related solution to perform the necessary work. This may involve non-technical work that takes place offline.
2. After performing implementation work, select one of the following status options from the **Implementation status** dropdown menu in the top information bar:

    - **Not implemented**
    - **Implemented**
    - **Alternative implementation** - select this option if you used other non-Microsoft tools or took other actions not included in Microsoft recommendations
    - **Planned**
    - **Out of scope** - not relevant to your organization and doesn’t contribute to your score
3. You then need to record the date for the implementation status change. Select **Edit notes** above the action's information bar. The **Edit action details** flyout pane opens to the **Implementation** tab. You can also edit the implementation status here.
4. At the **Implementation date** field, select an implementation date.
5. In the notes field, enter optional implementation notes (learn more about notes).
6. Select **Save** on the flyout pane to close the pane.
7. Select **Save** or **Save and close** above the action's information bar to save the changes you made.

Common actions synchronize across groups. When two different assessments in the same group share improvement actions that are managed by you, any updates you make to an action's implementation details or status will automatically synchronize to the same action in any other assessment in the group. This synchronization allows you to implement one improvement action and meet several requirements across multiple regulations.

### Testing work

The test status of an improvement action is displayed in the **Test status** field on the action’s details page. After an improvement action has been implemented, you can update the test status for manually tested actions by following the instructions below. A user with editing permissions can adjust the action status.

1. On the improvement action details page, you can select one of the following status options from the **Test status** dropdown menu in the top information bar:

    - **None** - no work has started on the action
    - **Not assessed** - action hasn’t been tested
    - **Passed** - implementation has been verified by an assessor
    - **Failed low risk**
    - **Failed medium risk**
    - **Failed high risk**
    - **Out of scope** - the action is out of scope for the assessment and doesn’t contribute to your score
    - **To be determined**
    - **Could not be determined**
    - **Partially tested**
    - **In progress**
2. You then need to record the test date. Select **Edit notes** above the action's information bar. The **Edit action details** flyout pane appears.
3. On the **Test and verification** tab, select a test date. You can also edit the test status here.
4. In the notes field, enter optional testing notes (learn more about notes).
5. Select **Save** on the flyout pane to close the pane.
6. Select **Save** or **Save and close** above the action's information bar to save the changes you made.

For manually tested actions that are implemented in Defender for Cloud, refer to the implementation instructions for how to set test status within subscriptions.

Note

If the action is manually tested, you can edit test status, test date, and notes. You can’t edit test status and notes for automatically tested actions.

Automatically tested actions may show a status of **Out of scope** when automatic monitoring through Defender for Cloud is first set up. This is because it can take up to 24 hours to process the signals from Defender for Cloud. Improvement action statuses refresh every 24 hours.

Automatically tested actions may also show one of the following test statuses:

- **To be detected** - awaiting signals that indicate test status
- **Could not be detected** - couldn't detect a test status; will be automatically checked again
- **Partially tested** - action has been partially tested; neither passes nor fails

#### Exporting testing history

You can export a report that shows you a history of all changes in test status for an improvement action. These reports are especially helpful for monitoring progress on actions that are automatically tested, since such actions are regularly or frequently updated based on your tenant's data.

On an improvement action's details page, select **Export testing history** above the top information bar. The report downloads as an Excel file.

## Enter and view notes

You can enter notes for internal reference about your implementation or testing work. These notes can be added or edited by any user with editing permissions, not just by the action's assigned owner.

The notes don't display on the improvement action's details page. To view notes, or to add notes, you need to select the **Edit notes** command in the upper right of the improvement action's details page. When you select **Edit notes**, the **Edit action details** flyout pane appears. A text field for notes appears on both the **Implementation** and **Test and verification** tabs of the flyout pane (this is also where you can select status and dates for implementation and testing work.)

After adding notes, select **Save** on the flyout pane. The pane closes. Then select **Save** or **Save and close** above the action's information bar to save your notes.

Note

Testing notes can't be manually edited for automatically tested improvement actions. Compliance Manager updates notes for you.

## Storing evidence

You can upload evidence related to implementation and testing work, in the form of files or links, directly to the **Evidence** tab of an improvement action’s details page. This environment is a secure, centralized repository to help you demonstrate satisfaction of controls to meet compliance standards and regulations. Any user with read-only access can read content in this section. Only users with editing rights can upload, download, and delete evidence.

#### Upload evidence

- On the improvement action’s details page, go to the **Evidence** tab.
- Select **Add evidence** and select either **Document** or **Link**.
- For a document, browse to select the file you want to upload, then select **Done**. Accepted file types are:
    - Documents (.doc, .xls, .ppt, .txt, .pdf)
    - Images (.jpg, .png)
    - Video (.mkv)
    - Compressed files (.zip, .rar)
- For a link, enter a name for the link and its URL, then select **Done**.

#### Delete evidence

You can delete evidence when the improvement action hasn't yet reached a pass or fail status. To delete evidence files or links, select the action menu (the three dots) to the right of the item's name and select **Delete**. Confirm the deletion when prompted.

When an improvement action has a test status of **Passed,** **Failed**, or **Out of scope**, evidence files and links can no longer be deleted.

## Assign improvement action to assessor for completion

After you complete the work, conduct testing, and upload evidence, the next step is to assign the improvement action to an assessor for validation. The assessor validates the work, examines the evidence, and selects the appropriate test status.

- **If action status is set to “Pass”**: The action is complete and receives the total number of points.
- **If action status is set to “Fail”**: The action doesn’t meet the requirements, and the assessor can assign it back to the appropriate user for more work.

A **Compliance Manager Assessor** role allows a user to perform this work, without the full rights to create assessments. Learn [how to set permissions](compliance-manager-setup#set-user-permissions-and-assign-roles) and [how to grant role-based access to assessments and regulations](compliance-manager-setup#role-based-access-to-assessments-and-regulations).

## Accepting updates to improvement actions

When an update is available for an improvement action, you see a notification next to its name. You can either accept the update or defer it for a later time.

##### What causes an update

An update occurs when there are changes related to scoring, automation, or scope. Changes may involve new guidance for improvement actions based on regulatory changes, or could be because of product changes. Only the improvement actions managed by your organizations receive update notifications.

##### Where you see assessment update notifications

When an improvement action is updated, you see a **Pending update** label next to its name on the improvement actions page, and on the details page of its related assessments.

Go to the improvement action’s details page, and select the **Review update** button in the top banner to review details about the changes and accept or defer the update.

##### Review update to accept or defer

When you select **Review update** from the improvement action details page, a flyout pane appears on the right side of your screen. The flyout pane provides key details about the update, such as the assessments impacted and changes in score and scope.

Select **Accept update** to accept all the changes to the improvement action. **Accepted changes are permanent**.

Note

When you accept an update to an action, you’re also accepting updates to any other versions or instances of this action. Updates will propagate tenant-wide for technical actions, and will propagate group-wide for non-technical actions.

If you select **Cancel**, the update won’t be applied to the improvement action. However, you continue to see the **Pending update** notification until you accept the update.

- **Why we recommend accepting updates**: Accepting updates helps ensure you have the most updated guidance on using solutions and taking appropriate improvement actions to help you meet the requirements of the certification at hand.
- **Why you might want to defer an update**: If you’re in the middle of completing an assessment that includes the improvement action, you may want to ensure you’ve finished work on it before you accept the update. You can defer the update for a later time by selecting **Cancel** on the review update flyout pane.

##### Accept all updates at once

If you have multiple updates and want to accept them all at one time, select the **Accept all updates** link at the top of your improvement actions table. A flyout pane appears which lists the number of actions to be updated. Select the **Accept updates** button to apply all updates.

When you return to your improvement actions page, you may see a message across the top of the page asking you to refresh the page for the updates to be completed.

## Set up alerts for improvement action changes

You can set up alerts to notify you immediately when certain changes to improvement actions occur, such as a change in implementation or test status, or an increase or decrease in score. Getting quick notifications of such changes can help you stay on top of possible compliance risks. Visit [Compliance Manager alerts and alert policies](compliance-manager-alert-policies) to learn how to set up alerts.

## Export a report of all improvement actions

On the improvement actions page, select **Export actions** above the list of actions. An Excel file downloads. The file contains all your improvement actions and the filter categories shown on the improvement actions page. This is the same file to use for updating multiple improvement actions at once. Get details about how to work with the file in order to [update multiple improvement actions](compliance-manager-update-actions).