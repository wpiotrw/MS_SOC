---
layout: Conceptual
title: Microsoft Security Copilot agent error messages | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/agents-error-messages
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Microsoft Security Copilot agent error messages
ms.date: 2026-01-16T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: partner-contribution
ms.reviewer: shivanpatel
locale: en-us
document_id: 9e5b0a8d-8b61-17be-24c1-6ecebdf94a89
document_version_independent_id: 9e5b0a8d-8b61-17be-24c1-6ecebdf94a89
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/agents-error-messages.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agents-error-messages
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/agents-error-messages.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: fb2f20a8-0c8c-f8fd-ea71-c64bd382216e
---

# Microsoft Security Copilot agent error messages | Microsoft Learn

Learn about the error messages that you might encounter when using agents.

| Error message | Messages returned | Issue | Resolution |
| --- | --- | --- | --- |
| CapacityNotFound | Capacity not found. Check your capacity configuration. | Possible causes of this could include: 1. Disassociating capacity from the active workspace. 2. Not attaching a capacity to the workspace. | Ensure capacity is provisioned correctly. For more information, see [Manage usage](manage-usage). |
| CapacityNotValid | Capacity isn't valid. Check your capacity configuration. | Possible causes of this could include: 1. Disassociating capacity from the active workspace. 2. Not attaching a capacity to the workspace. | Ensure capacity has been provisioned correctly. For more information, see [Manage usage](manage-usage). |
| FailedToCompleteInAllottedTime | Run failed to complete in allotted time. | Agents might have gone over the maximum time required to complete the run. The current maximum time is set to 30 minutes in the system. This issue can happen in situations such as a high load or where certain processes within the agent are taking longer than expected. | Try again and if it persists, contact the agent owner. |
| FailedToParseFetchSkillResult | Failed to parse fetch skill result. Fetch skill must return valid JSON. | Agent returns an unexpected invalid output. | Contact the agent owner. |
| FailedToRetrieveFetchSkillResult | Failed to get results of fetch skill. | Agent returns an unexpected invalid output. | Contact the agent owner. |
| FailedToStartExecution | Failed to start fetch skill. | Transient failure due to interprocess communication. | Try again and if it persists, [contact support](support). |
| FailedToStartRun | Run failed to start. | Transient failure due to interprocess communication. | Try again and if it persists, [contact support](support). |
| FetchSkillEvaluationFailed | Fetch skill evaluation resulted in error. | Agent underlying skill had an issue. | Contact the agent owner. |
| ForbiddenIdentityConfiguration | Received 403 Forbidden invoking skill. Update your identity configuration. | An internal error occurred during an interprocess communication during a prompt/evaluation using the identity associated with the agent. It wasn't able to communicate with the service due to insufficient permissions. Each tenant/service logs should be able to identify if an identity was blocked from accessing the service. | Check with your sign-in logs administrator whether any access is preventing the agent from using the identity. Other steps: 1. Go to the agent. 2. Edit the agent. 3. Try to sign in with the identity into the services that the permissions identified in the agent manifest. OR  4. Try choosing another identity that has full access to all the permissions listed in the manifest. |
| InternalServerError | An error occurred while processing your request. | Transient failure due to interprocess communication or a service outage. | Try again and if it persists, [contact support](support). |
| InvalidIdentityConfiguration | The identity configuration is invalid. | Failed to get a token from underlying services in Security Copilot. While rare, this issue can occur when one of the identity services doesn't complete the request or when it is under high load. | Try again and if it persists, [contact support](support). |
| MissingIdentityConfiguration | IdentityId is missing. | A required identity wasn't configured for the agent to run. | Steps: 1. Go to the agent.  2. Edit the agent. 3. Set up an identity that has full access to all the permissions listed in the manifest. |
| ProcessSkillEvaluationFailed | Process skill evaluation resulted in error. | Agent underlying skill had an issue. | Contact the agent owner. |
| SecurityCopilotEvaluationError | An error occurred in a child evaluation. | Agent underlying skill had an issue. | Contact the agent owner. |
| Throttled | Skill invocation is throttled due to capacity limits. Try again later. | Possible causes of this error could include: 1. Provisioned capacity exceeded. 2. During a high load situation, the system might be throttling the process. | Review your provisioned capacity and its current usage and adjust if needed. For more information, see [Manage usage](manage-usage).  If the provisioned capacity and usage are looking normal, retry again. If the issues persists, [contact support](support). |
| TriggerNotEnabled | N/A | An agent won't run because a trigger is misconfigured. | Try to have the workspace owner reinstall the agent or get help from the agent owner |
| TriggerNotFound | N/A | An agent won't run because a trigger is missing. | Try to have the workspace owner reinstall the agent or get help from the agent owner. |
| UnauthorizedIdentityConfiguration | Unauthorized identity configuration. Update your identity configuration. | An internal error happened during an interprocess communication during a prompt/evaluation using the identity associated with the agent. It wasn't able to communicate with the service due to an invalid token. Each tenant/service logs should be able to identify if an identity was blocked from accessing the service. | Check with your sign-in logs administrator whether any access is preventing the agent from using the identity. Other steps: 1. Go to the agent. 2. Edit the agent. 3. Try to sign in with the identity into the services that the permissions identified in the agent manifest. OR 4. Try choosing another identity that has full access to all the permissions listed in the manifest. |