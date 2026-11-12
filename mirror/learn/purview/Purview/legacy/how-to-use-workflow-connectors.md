---
layout: Conceptual
title: Workflow connectors and actions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-use-workflow-connectors
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to use connectors and actions in Microsoft Purview workflows.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom:
- template-how-to
- sfi-image-nochange
- msecd-doc-authoring-1030
locale: en-us
document_id: c5dec19e-ab35-beb5-b8f7-5e1e55f0baaa
document_version_independent_id: c5dec19e-ab35-beb5-b8f7-5e1e55f0baaa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-use-workflow-connectors.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-use-workflow-connectors
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-use-workflow-connectors.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 52d96893-e420-b94a-3dea-15c54011d9ab
---

# Workflow connectors and actions | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

You can use [workflows](../concept-workflow) to automate some business processes through Microsoft Purview. A Connector in a workflow provides a way to connect to different systems and apply a set of prebuilt actions and triggers.

## Current workflow connectors and actions

Currently the following connectors and actions are available for a workflow in Microsoft Purview:

| Connector Type | Functionality | Parameters | Customizable | Workflow templates |
| --- | --- | --- | --- | --- |
| Apply to each | Apply an action or set of actions to all returned values in an output. | -Output to process  -Actions | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Check data source registration for data use governance | Validate if data source has been registered with Data policy enforcement enabled. | None | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | Data access request |
| Condition | Evaluate a value to true or false. Based on the evaluation the workflow will be redirected to different branches | - Add row  - Title  - Add group | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Create Glossary Term | Create a new glossary term | None | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | Create glossary term template |
| Create task and wait for task completion | Creates, assigns, and tracks a task to a user or Microsoft Entra group as part of a workflow.  - Reminder settings - You can set reminders to periodically remind the task owner until they complete the task.  - Expiry settings - You can set an expiration or deadline for the task activity. Also, you can set who needs to be notified (user/AAD group) after the expiry.  - Email aggregation available | - Assigned to  - Task title  - Task body | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Delay | Delay the next action until a specified number of units has passed. | -Count: Number of units that need to pass until the delay resolves-Unit: Month, Week, Day, Hour, Minute, Second | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Delete glossary term | Delete an existing glossary term | None | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | Delete glossary term |
| Grant access | Create an access policy to grant access to the requested user. | None | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | Data access request |
| Http | Integrate with external applications through http or https call.  For more information, see [Workflows HTTP connector](../how-to-use-workflow-http-connector) | - Host  - Method  - Path  - Headers  - Queries  - Body  - Authentication | - Renamable: Yes  - Deletable: Yes  - Settings: Secured Input and Secure outputs (Enabled by default)  - Multiple per workflow | All workflows templates |
| Import glossary terms | Import one or more glossary terms | None | - Renamable: Yes  - Deletable: No  - Multiple per workflow | Import terms |
| Parse JSON | Parse an incoming JSON to extract parameters | - Content  - Schema | - Renamable: Yes  - Deletable: No  - Multiple per workflow | All workflows templates |
| Send email notification | Send email notification to one or more recipients | - Subject  - Message body  - Recipient | - Renamable: Yes  - Deletable: Yes  - Settings: Secured Input and Secure outputs (Enabled by default), Single or aggregated emails - Multiple per workflow | All workflows templates |
| [ServiceNow actions](../how-to-use-servicenow-workflows) | Connect to an instance of ServiceNow and complete one of these actions:  -Create record  -Delete record  -Get record  -Get record types  -List records  -Update record | Depending. See [ServiceNow in workflows](../how-to-use-servicenow-workflows) for more information. | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Start and wait for an approval | Generates approval requests and assigns the requests to individual users or Microsoft Entra groups. There are two approval types:  - First to Respond – First approver's outcome (Approve/Reject) is considered final.  - Everyone must approve – This implies everyone identified as an approver must approve. If one approver rejects the request, the request is rejected.  - Email aggregation available | - Approval Type  - Title  - Assigned To | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Switch | Evaluates a dynamic content expression and chooses the case that matches the result, running specific actions for only that case. **Currently up to 15 cases are supported.** | - On: Dynamic content to evaluate. (string, integer)  - Equals: Value to evaluate 'on' against. When matched, the workflow diverts to this case. (string, integer) | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Until | Repeat actions within the until control until the and/or condition is satisfied, or the count or time out limits have been reached. | -Actions: Actions to repeat  -Count: Default 60, Minimum 1, Maximum 1000 The number of cycles that an Until loop can have during a workflow run. -Time-out: Default PT1H(1 hour), Maximum PT1H(1 hour) The amount of time that the Until loop can run before exiting and is specified in ISO 8601 format. If cumulative time counted for all actions and iterations within Until action takes longer than the time-out limit, the current cycle doesn't stop. However, the next cycle doesn't start because the limit condition isn't met. | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Update glossary term | Update an existing glossary term | None | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | Update glossary term |
| Variable actions | Define and update custom variables with these actions:  -Initialize variable  -Set variable  -Increment variable  -Decrement variable  -Append array to variable  -Append string to variable | Depending. See the variable actions section for more information. | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| When term creation request is submitted | Triggers a workflow with all term details when a new term request is submitted | None | - Renamable: Yes  - Deletable: No  - Only one per workflow | Create glossary term template |
| When term deletion request is submitted | Triggers a workflow with all term details when a request to delete an existing term is submitted | None | - Renamable: Yes  - Deletable: No  - Only one per workflow | Delete glossary term |
| When term Import request is submitted | Triggers a workflow with all term details in a csv file, when a request to import terms is submitted | None | - Renamable: Yes  - Deletable: No  - Only one per workflow | Import terms |
| When term update request is submitted | Triggers a workflow with all term details when a request to update an existing term is submitted | None | - Renamable: Yes  - Deletable: No  - Only one per workflow | Update glossary term |

## Start and wait for an approval

The start and wait for an approval connector generates approval requests and assigns the requests to individual users or Microsoft Entra groups.

Currently, the connector supports two types of approval types:

- **First to Respond** – This implies that the first approver's outcome (Approve/Reject) is considered final.
- **Everyone must approve** – This implies everyone identified as an approver must approve the request for the request to be considered approved. If one approver rejects the request, regardless of other approvers, the request is rejected.

You can also set reminders to periodically remind the approver until they approve or reject, or set an expiration or deadline for the approval activity. When the request expires, you can choose who will receive a notification about the expiration.

### Approval requests

Approval requests are sent as emails to the groups or users specified in the approval connector. There are two types of possible approval emails depending on whether your workflow and your email client meet some requirements.

- **Actionable messages** - if your workflow and email client meet the requirements, your approvers can receive single and aggregated actionable approval emails where they can leave comments and reject or approve requests within outlook. For more information, the approver can also select the approval item in the message to be taken to request details in the Microsoft Purview portal.

    ![Sample actionable message from Microsoft Purview with the title. Approval and rejection buttons are available in the email.](../media/how-to-workflow-manage-requests-approval/actionable-message.png)

    Important

    If your workflow or email client don't meet the requirements, your users might receive 400/401/403 errors when using actionable messages.
- **Standard messages** - if your workflow and email client don't meet the requirements, your approvers receive single and aggregated approval emails that direct them to the [approval experience in the Microsoft Purview portal](../how-to-workflow-manage-requests-approvals#approvals).

    ![Sample email from Microsoft Azure with the title 'Action required: Approve or reject the Microsoft Purview request.' Approval and rejection buttons are available in the email.](../media/how-to-workflow-manage-requests-approval/approval-email.png)

### Actionable approval requirements

For your approvers to use actionable messages in Outlook, your Microsoft Purview, workflow, and email client must meet these requirements:

- Your Microsoft Purview account must have public network access enabled.
- When the user submits an approval from the actionable email, they need to be logged into the same tenant where the Microsoft Purview account resides.
- The **Assigned to** configured in the Start and Wait for approval Connector must be an individual not a group.
- The **Assigned to** configured in the Start and Wait for approval Connector must have a mailbox on Outlook.com or Exchange Online in Office 365.
- The email client used to open the approval request email must be Outlook with these versions: [Outlook version requirements for actionable messages.](/en-us/outlook/actionable-messages#outlook-version-requirements-for-actionable-messages)
- The Microsoft Purview account isn't in an [Azure Government and Azure China 21Vianet region](../feature-availability).

Tip

If users receive a 403 message when attempting to approve an item from an actionable email, your Microsoft Purview account likely has network settings that are rejecting the request.

## Send email notification

When you send an email notification in a workflow, either using the send email activity or another activity, by default individual emails are sent to each user specified. However, for some activities there's also an option to aggregate emails to be sent to batches of users. This can greatly reduce the number of emails sent from activities.

These activities are available to aggregate emails:

- Start and wait for an approval
- Send email notification
- Create task and wait for task completion

### How to aggregate emails

When you're using one of the available activities and want to aggregate your emails, follow these steps.

1. Open your activity settings by selecting the ellipsis button in the activity, and then the **Settings** option.

    ![Screenshot of a start and wait for approval activity with the settings button highlighted.](../media/how-to-use-workflow-connectors/select-activity-settings.png)
2. Select the **Aggregate emails** toggle to switch it to **On**.

    ![Screenshot of the aggregate emails setting in a workflow activity.](../media/how-to-use-workflow-connectors/select-aggregate-emails-toggle.png)
3. Select **Done**
4. Finish making any other edits needed to your workflow, and then select **Save** to save the changes to your workflow.

### Aggregation information

When you enable aggregation, the emails sent during this action are sent immediately. Instead the individual emails would be aggregated into one email and sent to receivers. The aggregation causes a slight delay in email delivery, between 0-3 minutes.

Aggregated emails are batched in groups of at most, 20. That is, if there are 110 emails that need to be aggregated, in the end 6 emails would be sent.

## Variable actions

Create, update, and reference custom variables that you can reference in workflows in any places that support dynamic content. You can create variables of these data types:

- Integer
- Float
- Boolean
- Array
- String
- Object

![Screenshot of the variable actions available, shown under the Variables tab in the Choose an action menu.](../media/how-to-use-workflow-connectors/variable-actions.png)

Here are all the actions available and their parameters and descriptions:

| Action | Functionality | Parameters |
| --- | --- | --- |
| Initialize variable | Create a new variable of one of the available types | -Name-Type-Value: Appropriate value based on variable type |
| Set variable | Update variable to specified value | -Name: Variable name selected from drop-down -Value: New value for variable |
| Increment variable | Increase integer and float variables by a specified value | -Name: Variable name selected from drop-down -Value: Amount to increment variable |
| Decrement variable | Reduce integer and float variables by a specified value | -Name: Variable name selected from drop-down -Value: Amount to decrement variable |
| Append to array variable | Append specified value to array variable | -Name: Variable name selected from drop-down -Value: New value to append |
| Append to string variable | Append specified value to array variable | -Name: Variable name selected from drop-down -Value: New value to append |

### Variable limitations

- 50 variables per workflow
- Numeric variable range is [-(2^53^-1), 2^53^-1]
- names are limited to 46 characters
- Self-references aren't allowed in actions that update variable values: set, increment, decrement, append to array, append to string
- Initialize variable can't be used in local scope actions like "apply to each," "condition," or "until."
- Set variable can't be used in "apply to each" actions.