---
layout: Conceptual
title: Configure Arguments for Built-In Lifecycle Workflow Tasks - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/identitygovernance-lifecycleworkflows-task-arguments
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: rogulati
ms.author: rogulati
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Learn how to configure arguments for built-in Lifecycle Workflow tasks in Microsoft Graph to automate user lifecycle processes.
ms.reviewer: alexander.filipin
ms.localizationpriority: medium
ms.date: 2025-04-25T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1026
locale: en-us
document_id: 58354ac3-716c-836a-7bbf-ec078f415a98
document_version_independent_id: 58354ac3-716c-836a-7bbf-ec078f415a98
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/identitygovernance-lifecycleworkflows-task-arguments.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identitygovernance-lifecycleworkflows-task-arguments
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/identitygovernance-lifecycleworkflows-task-arguments.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: c6e1e3d8-a5a3-1d28-fcb6-4f78d8db23b7
---

# Configure Arguments for Built-In Lifecycle Workflow Tasks - Microsoft Graph | Microsoft Learn

Microsoft Graph Lifecycle Workflows APIs let you automate user lifecycle processes at the joiner, leaver, and mover levels.

Core to the workflows are [tasks](/en-us/graph/api/resources/identitygovernance-task) that represent specific actions that run automatically when a workflow is triggered. [Built-in tasks](/en-us/graph/api/resources/identitygovernance-task) are available to support creating custom workflows. These tasks are configured on the **arguments** property of a task definition.

This article explains how to configure the arguments property for built-in tasks to streamline automation.

## Configure arguments for tasks

| Task display name | taskDefinitionId | arguments |
| --- | --- | --- |
| Send welcome email to new hire | 70b29d51-b59a-4773-9280-8841dfd3f2ea | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. This argument doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send onboarding reminder email | 3C860712-2D37-42A4-928F-5C93935D26A1 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. This argument doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Generate Temporary Access Pass and send via email to user's manager | 1b555e50-7f65-41d5-b514-5894a026d10d | **name**: `tapLifetimeMinutes`**value**: `10` up to `43000`**name**: `tapIsUsableOnce`**value**: `true` or `false`**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument.**Prerequisites**:<br>1. The user must be assigned a manager.<br>2. The user's manager must have their mail enabled.<br>3. The temporary access pass (TAP) policy must be enabled in the tenant and the user enabled to use the TAP authentication method. For more information, see [temporaryAccessPassAuthenticationMethodConfiguration resource type](/en-us/graph/api/resources/temporaryaccesspassauthenticationmethodconfiguration). |
| Select verification profile for identity verification (Preview) | 9ed82537-8442-467a-8eef-9351fb7a1f9c | Available only in `/beta`. `verifiedIdProfileId` is required. For optional arguments and recipient defaults, see Configure identity-verification onboarding tasks (beta). |
| Select verification for Verified ID presentation (Preview) | 8314685b-de26-4c90-b086-bfa0e7a263f3 | Available only in `/beta`. `verifiedIdProfileId` is required. For optional arguments and recipient defaults, see Configure identity-verification onboarding tasks (beta). |
| Send manager verification status email (Preview) | c7a1f3e5-4b2d-4e8a-9f6c-3d5a7b1e2c4f | Available only in `/beta`. `verifiedIdProfileId` is required. For optional arguments and recipient defaults, see Configure identity-verification onboarding tasks (beta). |
| Add user to groups | 22085229-5809-45e8-97fd-270d28d66910 | **name**: `groupID`**value**: A valid group ID or a comma-separated list of groups to which the user is added as a member. For example, `"06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"`. |
| Add user to teams | e440ed8d-25a1-4618-84ce-091ed5be5594 | **name**: `teamID`**value**: A valid group ID or a comma-separated list of teams to which the user is added as a member. For example, `"06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"`. |
| Update user attributes (Preview) | 2c8f4a1b-7d3e-4f9c-8a5b-6e1d2c3f4a5b | **name**: `attributeUpdates`**value**: A JSON string specifying up to 10 user attributes to update or clear. The attributes can include built-in, on-premises extensions, directory extensions, and employee org data. |
| Enable user account | 6fc52c9d-398b-4305-9763-15f42c1676fc | **name**: `enableOnPremisesAccount`**value**: A Boolean value that indicates whether the task enables synced on-premises user accounts. |
| Run a custom task extension | 4262b724-8dba-4fad-afc3-43fcbb497a0e | **name**: `CustomTaskExtensionID`**value**: The ID of the custom task extension. |
| Assign licenses to users (Preview) | 683c87a4-2ad4-420b-97d4-220d90afcd24 | **name**: `licenses`**value**: The ID of the license you want to assign. |
| Remove selected license assignments from user (Preview) | 5fc402a8-daaf-4b7b-9203-da868b05fc5f | **name**: `licenses`**value**: The ID of the license you want to assign. |
| Revoke all refresh tokens for user | 509589a4-0466-4471-829e-49c5e502bdee | None. |
| Send email to manager about sponsorship changes | b8c4e1f9-3a7d-4b2e-9c5f-8d6a9b1c2e3f | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. This argument doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send email to co-sponsors about sponsor changes | ad3b85cd-75b1-43e7-b4b9-0e52faba3944 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. This argument doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Transfer agent identity sponsorships to manager | b8f4c3d5-9e7a-4b1c-8f2d-6a5e8b9c7f4a | None.**Prerequisites**:<br>1. The user must be assigned a manager. |
| Disable user account | 1dfdfcc7-52fa-4c2e-bf3a-e3919cc12950 | **name**: `disableOnPremisesAccount`**value**: A Boolean value that indicates whether the task disables synced on-premises user accounts. |
| Remove user from selected group | 1953a66c-751c-45e5-8bfe-01462c70da3c | **name**: `groupID`**value**: A valid group ID or a comma-separated list of groups that the user is a member of. For example, `"06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"`. |
| Remove users from all groups | b3a31406-2a15-4c9a-b25b-a658fa5f07fc | None |
| Remove user from teams | 06aa7acb-01af-4824-8899-b14e5ed788d6 | **name**: `teamID`**value**: A comma-separated list of teams that the user is a member of. For example, `"06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"`. |
| Remove user from all teams | 81f7b200-2816-4b3b-8c5d-dc556f07b024 | None |
| Remove all license assignments from user | 8fa97d28-3e52-4985-b3a9-a1126f9b8b4e | None |
| Delete user | 8d18588d-9ad3-4c0f-99d0-ec215f0e3dff | **name**: `deleteOnPremisesAccount`**value**: A Boolean value that indicates whether the task deletes synced on-premises user accounts. |
| Send email to notify manager of user move | aab41899-9972-422a-9d97-f626014578b7 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. Doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send email to manager before user last day | 52853a3e-f4e5-4eb8-bb24-1ac09a1da935 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. Doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send email on user's last day | 9c0a1eaf-5bda-4392-9d9e-6e155bb57411 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. Doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send offboarding email to user's manager after their last day | 6f22ddd4-b3a5-47a4-a846-0d7c201a49ce | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. Doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Send email about user inactivity | 92f74cb4-f1b6-4ec0-b766-96210f56edc2 | **name**: `cc`**value**: A valid user ID (String) for the user you want to cc in the email.**name**: `customSubject`**value**: A custom subject header for the email being sent.**name**: `customBody`**value**: The body of the customized email.**name**: `locale`**value**: Language value that overrides the email recipient's language settings. This argument doesn't customize the custom text of the email, and should be set in the same language as the custom text.**name**: `to`**value**: `User`, `Managers`, `Sponsors`, or the string of a specific `userID`. If `Sponsors` is selected, you're not able to add another user in the `cc` argument. |
| Request user access package assignment | c1ec1e76-f374-4375-aaa6-0bb6bd4c60be | **name**: `assignmentPolicyId`**value**: A valid assignment policy ID (String) for the access package you want to assign the user.**name**: `accessPackageId`**value**: A valid access package ID for the access package you want to assign to the user. |
| Remove access package assignment for user | 4a0b64f2-c7ec-46ba-b117-18f262946c50 | **name**: `accessPackageId`**value**: A valid access package ID for the access package you want to unassign from the user. |
| Remove all access package assignments for user | 42ae2956-193d-4f39-be06-691b8ac4fa1d | None |
| Cancel pending access package assignment requests for user | 498770d9-bab7-4e4c-b73d-5ded82a1d0b3 | **name**: `daysUntilExpiration`**value**: A valid string of the days until the access package assignment for the user expires. |

## Examples

### Example 1: Send a welcome email to a new hire

```json
{
  "category": "joiner",
  "continueOnError": false,
  "description": "Send welcome email to new hire",
  "displayName": "Send Welcome Email",
  "isEnabled": true,
  "taskDefinitionId": "70b29d51-b59a-4773-9280-8841dfd3f2ea",
  "arguments": [
    {
      "name": "cc",
      "value": "e94ad2cd-d590-4b39-8e46-bb4f8e293f85,ac17d108-60cd-4eb2-a4b4-084cacda33f2"
    },
    {
      "name": "customSubject",
      "value": "Welcome to the organization {{userDisplayName}}!"
    },
    {
      "name": "customBody",
      "value": "Welcome to our organization {{userGivenName}} {{userSurname}}.\n\nFor more information, reach out to your manager {{managerDisplayName}} at {{managerEmail}}."
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 2: Generate a Temporary Access Pass (TAP) and send it to the user's manager

```json
{
  "category": "joiner",
  "continueOnError": false,
  "description": "Generate Temporary Access Pass and send via email to user's manager",
  "displayName": "Generate TAP and Send Email",
  "isEnabled": true,
  "taskDefinitionId": "1b555e50-7f65-41d5-b514-5894a026d10d",
  "arguments": [
    {
      "name": "tapLifetimeMinutes",
      "value": "480"
    },
    {
      "name": "tapIsUsableOnce",
      "value": "false"
    },
    {
      "name": "cc",
      "value": "068fa0c1-fa00-4f4f-8411-e968d921c3e7,9d208c40-7eb6-46ff-bebd-f30148c39b47"
    },
    {
      "name": "customSubject",
      "value": "Temporary access pass for your new employee {{userDisplayName}}"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nPlease find the temporary access pass for your new employee {{userDisplayName}} below:\n\n{{temporaryAccessPass}}\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 3: Add a user to groups

```json
{
  "category": "joiner,leaver",
  "description": "Add user to groups",
  "displayName": "AddUserToGroup",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "22085229-5809-45e8-97fd-270d28d66910",
  "arguments": [
    {
      "name": "groupID",
      "value": "06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"
    }
  ]
}
```

### Example 4: Add a user to teams

```json
{
  "category": "joiner,leaver",
  "description": "Add user to team",
  "displayName": "AddUserToTeam",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "e440ed8d-25a1-4618-84ce-091ed5be5594",
  "arguments": [
    {
      "name": "teamID",
      "value": "06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"
    }
  ]
}
```

### Example 5: Update user attributes (Preview)

```json
{
  "category": "joiner",
  "continueOnError": false,
  "description": "Update or clear user attribute values including custom attributes",
  "displayName": "Update user attributes",
  "isEnabled": true,
  "taskDefinitionId": "2c8f4a1b-7d3e-4f9c-8a5b-6e1d2c3f4a5b",
  "arguments": [
    {
      "name": "attributeUpdates",
      "value": "[{\"attribute\":\"department\",\"value\":\"Sales\"},{\"attribute\":\"jobTitle\",\"value\":\"Account Executive\"}]"
    }
  ]
}
```

### Example 6: Enable a user account

```json
{
  "category": "joiner,leaver",
  "description": "Enable user account",
  "displayName": "EnableUserAccount",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "6fc52c9d-398b-4305-9763-15f42c1676fc",
  "arguments": []
}
```

### Example 7: Run a custom task extension

```json
{
  "category": "joiner,leaver",
  "description": "Run a Custom Task Extension to call-out to an external system.",
  "displayName": "Run a Custom Task Extension",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "d79d1fcc-16be-490c-a865-f4533b1639ee",
  "arguments": [
    {
      "name": "customTaskExtensionID",
      "value": "<ID of your Custom Task Extension>"
    }
  ]
}
```

### Example 8: Disable a user account

```json
{
  "category": "joiner,leaver",
  "description": "Disable user account",
  "displayName": "DisableUserAccount",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "1dfdfcc7-52fa-4c2e-bf3a-e3919cc12950",
  "arguments": []
}
```

### Example 9: Remove a user from selected groups

```json
{
  "category": "leaver",
  "displayName": "Remove user from selected groups",
  "description": "Remove user from membership of selected Azure AD groups",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "1953a66c-751c-45e5-8bfe-01462c70da3c",
  "arguments": [
    {
      "name": "groupID",
      "value": "06269010-2d8e-48e4-8f0e-33580720c9e1, 06bba22c-775e-42d8-b451-4221af061af0, 182f68db-6513-4e79-9ec2-a7e89a460e7f"
    }
  ]
}
```

### Example 10: Remove a user from all groups

```json
{
  "category": "leaver",
  "continueOnError": true,
  "displayName": "Remove user from all groups",
  "description": "Remove user from all Azure AD groups memberships",
  "isEnabled": true,
  "taskDefinitionId": "b3a31406-2a15-4c9a-b25b-a658fa5f07fc",
  "arguments": []
}
```

### Example 11: Remove a user from selected teams

```json
{
  "category": "joiner,leaver",
  "continueOnError": true,
  "displayName": "Remove user from selected Teams",
  "description": "Remove user from membership of selected Teams",
  "isEnabled": true,
  "taskDefinitionId": "06aa7acb-01af-4824-8899-b14e5ed788d6",
  "arguments": [
    {
      "name": "teamID",
      "value": "TeamId1, TeamId2, TeamId3, ..."
    }
  ]
}
```

### Example 12: Remove a user from all teams

```json
{
  "category": "leaver",
  "continueOnError": true,
  "description": "Remove user from all Teams",
  "displayName": "Remove user from all Teams memberships",
  "isEnabled": true,
  "taskDefinitionId": "81f7b200-2816-4b3b-8c5d-dc556f07b024",
  "arguments": []
}
```

### Example 13: Remove all license assignments from a user

```json
{
  "category": "leaver",
  "continueOnError": true,
  "displayName": "Remove all licenses for user",
  "description": "Remove all licenses assigned to the user",
  "isEnabled": true,
  "taskDefinitionId": "8fa97d28-3e52-4985-b3a9-a1126f9b8b4e",
  "arguments": []
}
```

### Example 14: Delete a user

```json
{
  "category": "leaver",
  "continueOnError": true,
  "displayName": "Delete user account",
  "description": "Delete user account in Azure AD",
  "isEnabled": true,
  "taskDefinitionId": "8d18588d-9ad3-4c0f-99d0-ec215f0e3dff",
  "arguments": []
}
```

### Example 15: Send an email to notify a manager of a user move

```json
{
  "category": "mover",
  "continueOnError": false,
  "description": "Send email to notify user\u2019s manager of user move",
  "displayName": "Send email to notify manager of user move",
  "isEnabled": true,
  "taskDefinitionId": "aab41899-9972-422a-9d97-f626014578b7",
  "arguments": [
    {
      "name": "cc",
      "value": "ac17d108-60cd-4eb2-a4b4-084cacda33f2,7d3ee937-edcc-46b0-9e2c-f832e01231ea"
    },
    {
      "name": "customSubject",
      "value": "{{userDisplayName}} has moved"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nwe are reaching out to let you know {{userDisplayName}} has moved in the organization.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 16: Send an email to a manager before a user's last day

```json
{
  "category": "leaver",
  "continueOnError": false,
  "description": "Send offboarding email to user's manager before the last day of work",
  "displayName": "Send email before user's last day",
  "isEnabled": true,
  "taskDefinitionId": "52853a3e-f4e5-4eb8-bb24-1ac09a1da935",
  "arguments": [
    {
      "name": "cc",
      "value": "068fa0c1-fa00-4f4f-8411-e968d921c3e7,e94ad2cd-d590-4b39-8e46-bb4f8e293f85"
    },
    {
      "name": "customSubject",
      "value": "Reminder that {{userDisplayName}}'s last day is coming up"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nthis is a reminder that {{userDisplayName}}'s last day is coming up.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 17: Send an email on a user's last day

```json
{
  "category": "leaver",
  "continueOnError": false,
  "description": "Send offboarding email to user's manager on the last day of work",
  "displayName": "Send email on user's last day",
  "isEnabled": true,
  "taskDefinitionId": "9c0a1eaf-5bda-4392-9d9e-6e155bb57411",
  "arguments": [
    {
      "name": "cc",
      "value": "068fa0c1-fa00-4f4f-8411-e968d921c3e7,e94ad2cd-d590-4b39-8e46-bb4f8e293f85"
    },
    {
      "name": "customSubject",
      "value": "{{userDisplayName}}'s last day"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nthis is a reminder that {{userDisplayName}}'s last day is today and their access will be revoked.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 18: Send the offboarding email to a user's manager after the user's last day of work

```json
{
  "category": "leaver",
  "continueOnError": true,
  "displayName": "Send offboarding email to user's manager after the last day of work",
  "description": "Send email after user's last day",
  "isEnabled": true,
  "continueOnError": true,
  "taskDefinitionId": "6f22ddd4-b3a5-47a4-a846-0d7c201a49ce",
  "arguments": []
}
```

### Example 19: Request user access package assignment

```json
{
  "category": "joiner,mover",
  "continueOnError": false,
  "description": "Request user assignment to selected access package",
  "displayName": "Request user access package assignment",
  "isEnabled": true,
  "taskDefinitionId": "c1ec1e76-f374-4375-aaa6-0bb6bd4c60be",
  "arguments": [
    {
      "name": "assignmentPolicyId",
      "value": "00d6fd25-6695-4f4a-8186-e4c6f901d2c1"
    },
    {
      "name": "accessPackageId",
      "value": "2ae5d6e5-6cbe-4710-82f2-09ef6ffff0d0"
    }
  ]
}
```

### Example 20: Remove access package assignment for a user

```json
{
  "category": "leaver,mover",
  "continueOnError": false,
  "description": "Remove user assignment of selected access package",
  "displayName": "Remove access package assignment for user",
  "isEnabled": true,
  "taskDefinitionId": "4a0b64f2-c7ec-46ba-b117-18f262946c50",
  "arguments": [
    {
      "name": "accessPackageId",
      "value": "2ae5d6e5-6cbe-4710-82f2-09ef6ffff0d0"
    }
  ]
}
```

### Example 21: Remove all access package assignments for a user

```json
{
  "category": "leaver",
    "continueOnError": false,
    "description": "Remove all access packages assigned to the user",
    "displayName": "Remove all access package assignments for user",
    "isEnabled": true,
    "taskDefinitionId": "42ae2956-193d-4f39-be06-691b8ac4fa1d",
    "arguments": [
        {
             "description": "Remove all access packages assigned to the user",
            "displayName": "Remove all access package assignments for user",
            "id": "42ae2956-193d-4f39-be06-691b8ac4fa1d",
            "version": 1,
            "parameters": [
                {
                    "name": "daysUntilExpiration",
                    "values": [],
                    "valueType": "string"
                }
            ]
        }
    ]
}
```

### Example 22: Cancel pending access package assignment requests for a user

```json
{
  "category": "leaver",
  "continueOnError": false,
  "description": "Cancel all access package assignment requests pending for the user",
  "displayName": "Cancel all pending access package assignment requests for user",
  "isEnabled": true,
  "taskDefinitionId": "498770d9-bab7-4e4c-b73d-5ded82a1d0b3",
  "arguments": []
}
```

### Example 23: Send onboarding reminder email

```json
{
  "category": "joiner",
  "continueOnError": false,
  "description": "Send onboarding reminder email to user\u2019s manager",
  "displayName": "Send onboarding reminder email",
  "isEnabled": true,
  "taskDefinitionId": "3C860712-2D37-42A4-928F-5C93935D26A1",
  "arguments": [
    {
      "name": "cc",
      "value": "e94ad2cd-d590-4b39-8e46-bb4f8e293f85,068fa0c1-fa00-4f4f-8411-e968d921c3e7"
    },
    {
      "name": "customSubject",
      "value": "Reminder: {{userDisplayName}} is starting soon"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nthis is a reminder that {{userDisplayName}} is starting soon.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 24: Revoke all refresh tokens for user

```json
{
  "category": "leaver, mover",
  "continueOnError": false,
  "description": "Revoke all refresh tokens for user",
  "displayName": "Revoke all refresh tokens for user",
  "isEnabled": true,
  "taskDefinitionId": "509589a4-0466-4471-829e-49c5e502bdee",
  "arguments": []
}
```

### Example 25: Send email to manager about sponsorship changes

```json
{
  "category": "mover",
  "continueOnError": false,
  "description": "Notify sponsor's manager about agent identity sponsorship transfer.",
  "displayName": "Send email to manager about sponsorship transfer",
  "isEnabled": true,
  "taskDefinitionId": "b8c4e1f9-3a7d-4b2e-9c5f-8d6a9b1c2e3f",
  "arguments": [
    {
      "name": "cc",
      "value": "ac17d108-60cd-4eb2-a4b4-084cacda33f2,7d3ee937-edcc-46b0-9e2c-f832e01231ea"
    },
    {
      "name": "customSubject",
      "value": "{{userDisplayName}} has moved"
    },
    {
      "name": "customBody",
      "value": "Hello {{managerDisplayName}}\n\nwe are reaching out to let you know {{userDisplayName}} has moved in the organization and you have taken over their agent ID sponsorships.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 26: Send email to co-sponsors about sponsor changes

```json
{
  "category": "mover",
  "continueOnError": false,
  "description": "Notify co-sponsors about agent identity sponsorship changes.",
  "displayName": "Send email to co-sponsors about sponsor changes",
  "isEnabled": true,
  "taskDefinitionId": "ad3b85cd-75b1-43e7-b4b9-0e52faba3944",
  "arguments": [
    {
      "name": "cc",
      "value": "ac17d108-60cd-4eb2-a4b4-084cacda33f2,7d3ee937-edcc-46b0-9e2c-f832e01231ea"
    },
    {
      "name": "customSubject",
      "value": "{{userDisplayName}} has moved"
    },
    {
      "name": "customBody",
      "value": "We are reaching out to let you know {{userDisplayName}} has moved in the organization and will no longer have sponsorship authority over agent IDs they previously sponsored with you.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

### Example 27: Transfer agent identity sponsorships to manager

```json
{
  "category": "mover",
  "continueOnError": false,
  "description": "Transfer all agent identities sponsored by user to manager.",
  "displayName": "Transfer agent identity sponsorships to manager",
  "isEnabled": true,
  "taskDefinitionId": "b8f4c3d5-9e7a-4b1c-8f2d-6a5e8b9c7f4a",
  "arguments": []
}
```

### Example 28: Send email about user inactivity

```json
{
  "category": "leaver",
  "continueOnError": false,
  "description": "Notify manager that user has been inactive",
  "displayName": "Send email about user inactivity",
  "isEnabled": true,
  "taskDefinitionId": "92f74cb4-f1b6-4ec0-b766-96210f56edc2",
  "arguments": [
    {
      "name": "cc",
      "value": "1bda0458-cb4b-473d-baf5-61125c86a6d3,7f552c25-e0f6-40b6-b4e0-36bb40ba7fb6"
    },
    {
      "name": "customSubject",
      "value": "{{UserDisplayName}}'s account has been inactive for {{NumberofDays}} days."
    },
    {
      "name": "customBody",
      "value": "We're notifying you that a recent sign-in for {{UserDisplayName}}'s user account has not been detected, and the account is considered inactive. The last sign in was {{LastSigninDate}}. To maintain a secure environment, your organization may have already started the process to disable or delete this user account.\n\nPlease check your organization's policies and take appropriate action if this user account is still needed.\n\nRegards\nYour IT department"
    },
    {
      "name": "locale",
      "value": "en-us"
    }
  ]
}
```

## Configure identity-verification onboarding tasks (beta)

The three identity-verification onboarding tasks are Joiner tasks available only through the Microsoft Graph `/beta` endpoint, not `/v1.0`. Use an ID verification profile configured for onboarding.

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Use [List task definitions](/en-us/graph/api/identitygovernance-lifecycleworkflowscontainer-list-taskdefinitions?view=graph-rest-beta&amp;preserve-view=true) to retrieve the task definitions. Their task-definition **version** is `0`, which isn't a Microsoft Graph API version.

All three tasks support the following arguments. Argument values are strings.

| Argument | Required | Behavior |
| --- | --- | --- |
| `cc` | No | A user ID or comma-separated list of user IDs to copy on the email. If omitted, no CC recipients are added. |
| `customBody` | No | A custom email body. If omitted, the standard body is used. For the two verification-link tasks, a nonempty custom body must include `{{verificationLink}}`. |
| `customSubject` | No | A custom email subject. If omitted, the standard subject is used. |
| `locale` | No | A language value that overrides the recipient's language setting. If omitted, the notification service resolves the locale using recipient preferences. |
| `to` | No | The recipient selector. Supported values and defaults depend on the task, as described in the recipient table. |
| `verifiedIdProfileId` | Yes | The ID of the ID verification profile selected for the workflow. There's no default. The manager verification-status email task uses this ID to identify which profile's verification status to report. |

The `to` argument has the following task-specific behavior. Populate the user's **otherMails** property for verification-link delivery. For delivery to `Manager`, populate both the user's **manager** relationship and the manager's **mail** property.

| Task | Supported`to`values | Default when`to`is omitted |
| --- | --- | --- |
| Select verification profile for identity verification (Preview) | `User/otherMails` only | `User/otherMails` |
| Select verification for Verified ID presentation (Preview) | `User/otherMails` only | `User/otherMails` |
| Send manager verification status email (Preview) | `User`, `Manager`, `Sponsors`, or a specific user's ID | `Manager` |

The following examples show task objects, not complete HTTP request bodies. Include the objects in the **tasks** collection when you [create a workflow](/en-us/graph/api/identitygovernance-lifecycleworkflowscontainer-post-workflows?view=graph-rest-beta&amp;preserve-view=true) with `POST https://graph.microsoft.com/beta/identityGovernance/lifecycleWorkflows/workflows`. For an existing workflow, [create a new version](/en-us/graph/api/identitygovernance-workflow-createnewversion?view=graph-rest-beta&amp;preserve-view=true) to change its task configuration.

Replace `<id-verification-profile-id>` in each example with the ID of the profile selected for the workflow.

### Send an identity-verification link

This task sends the user a link to complete identity verification with the selected profile. The example explicitly selects `User/otherMails` and includes the required verification-link placeholder in the custom body.

```json
{
  "category": "joiner",
  "continueOnError": false,
  "displayName": "Select verification profile for identity verification (Preview)",
  "isEnabled": true,
  "taskDefinitionId": "9ed82537-8442-467a-8eef-9351fb7a1f9c",
  "arguments": [
    {
      "name": "verifiedIdProfileId",
      "value": "<id-verification-profile-id>"
    },
    {
      "name": "to",
      "value": "User/otherMails"
    },
    {
      "name": "customSubject",
      "value": "Complete your identity verification"
    },
    {
      "name": "customBody",
      "value": "Complete identity verification: {{verificationLink}}"
    }
  ]
}
```

### Send a Verified ID presentation link

This task sends the user a link to present a Verified ID for the selected profile. The example omits `to`, so delivery defaults to `User/otherMails`. The custom body includes the required verification-link placeholder.

```json
{
  "category": "joiner",
  "continueOnError": false,
  "displayName": "Select verification for Verified ID presentation (Preview)",
  "isEnabled": true,
  "taskDefinitionId": "8314685b-de26-4c90-b086-bfa0e7a263f3",
  "arguments": [
    {
      "name": "verifiedIdProfileId",
      "value": "<id-verification-profile-id>"
    },
    {
      "name": "customBody",
      "value": "Present your Verified ID: {{verificationLink}}"
    }
  ]
}
```

### Send a manager verification-status email

This task reports the verification status for the selected profile. The example supplies the required profile ID and omits all optional arguments. Delivery defaults to `Manager`, with no CC recipients and standard email content. The notification service resolves the locale using recipient preferences.

```json
{
  "category": "joiner",
  "continueOnError": false,
  "displayName": "Send manager verification status email (Preview)",
  "isEnabled": true,
  "taskDefinitionId": "c7a1f3e5-4b2d-4e8a-9f6c-3d5a7b1e2c4f",
  "arguments": [
    {
      "name": "verifiedIdProfileId",
      "value": "<id-verification-profile-id>"
    }
  ]
}
```