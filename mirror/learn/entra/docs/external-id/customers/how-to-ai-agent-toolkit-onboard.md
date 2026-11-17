---
layout: Conceptual
title: Add authentication with the AI agent toolkit - Microsoft Entra External ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-ai-agent-toolkit-onboard
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/microsoftentraexternalid
author: csmulligan
ms.author: cmulligan
ms.service: entra-external-id
ms.subservice: external
manager: dougeby
description: Use the eeid-onboarding skill to choose an authentication experience, plan or implement app changes, and get manual tenant setup instructions.
ms.topic: how-to
ms.date: 2026-11-11T00:00:00.0000000Z
ai-usage: ai-generated
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 8c7d5d4a-4755-92e6-657d-c8fe165b765e
document_version_independent_id: 8c7d5d4a-4755-92e6-657d-c8fe165b765e
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/external-id/customers/how-to-ai-agent-toolkit-onboard.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: external-id/customers/how-to-ai-agent-toolkit-onboard
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/external-id/customers/how-to-ai-agent-toolkit-onboard.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 0611b6d7-37ab-4a3f-5cba-4916e96811e8
---

# Add authentication with the AI agent toolkit - Microsoft Entra External ID | Microsoft Learn

Use the `eeid-onboarding` skill to choose an authentication experience for your app, create an implementation plan or apply approved code changes, and get tenant configuration instructions. You make the authentication choices, approve application changes, and complete tenant setup manually.

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](../media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

## Prerequisites

- Completion of [Install the AI agent toolkit](how-to-install-ai-agent-toolkit).
- Your application's source code, available to your coding agent.
- A Microsoft Entra external tenant and its tenant ID. If you need a tenant, [create an external tenant](how-to-create-external-tenant-portal).
- An account with permission to complete the tenant configuration steps for your selected authentication experience.
- Your project's existing build and test tools, if you choose to implement code changes.

## Start the onboarding skill

Start in your app's source folder so that the agent can base its recommendations on your project.

1. Open the application's source folder in your coding agent.
2. Ask the agent to use the `eeid-onboarding` skill. For example, enter:

    ```text
    /eeid-onboarding Help me add Microsoft Entra External ID authentication to this app.
    ```
3. Choose **Hosted authentication (faster setup)** or **Custom authentication experience (more control)** when prompted. Select **Other / help me choose** to discuss the trade-offs before continuing.
4. Let the agent inspect your repository without changing it. Review its recommended authentication approach and confirm your choice.

The skill presents **Web authentication**, **Native authentication**, or **BYO UX** according to your selected experience and the repository findings. It asks for your choice before moving on.

## Select journeys, tenant details, and factors

Your choices determine the application changes and the manual tenant setup instructions.

1. Select the journeys you want to enable: **Sign in**, **Sign up**, **MFA**, or **Self-service password reset (SSPR)**.
2. Provide your tenant ID. The agent attempts to resolve the external-tenant subdomain from authenticated tenant metadata. If it can't resolve the subdomain, provide it when prompted.
3. Confirm the tenant details the agent presents.
4. Select the sign-in factors. Without MFA, choose **Email + password** or **Email one-time passcode**. With MFA, review and select the first-factor and second-factor combination the agent presents.

## Choose a plan or approved implementation

Choose whether you want a technical plan to review or application code changes. Tenant setup remains manual in either mode.

1. Review the selected authentication approach, journeys, tenant details, and factors with the agent.
2. Choose an implementation mode:

    - **Create a dry-run plan** produces a dependency-ordered technical plan without changing your repository or tenant. Review the proposed files, packages, configuration, routes, scopes, tests, tenant steps, and rollback guidance.
    - **Implement changes** prepares application code changes for your approval. Review the exact files and package changes, repository checkpoint information, and targeted rollback procedure before confirming.

The onboarding skill requires approval before changing code, installing packages, or replacing an existing authentication stack. For implementation, it records the Git branch, commit, and working-tree status. For dirty or non-Git projects, its checkpoint procedure copies the files it will change to a location outside the repository.

## Complete the manual tenant setup

Use the tailored instructions the agent provides for your chosen approach. The standard onboarding workflow doesn't run tenant automation scripts.

1. Review the generated Microsoft Entra admin center instructions. Each step should identify the action, its purpose, the expected result, and how to verify it.
2. Complete the applicable tenant configuration steps manually. Check that the application registration, platform, redirect URIs, scopes, and selected journeys match the application code or dry-run plan.
3. If you selected Web authentication and want branding, review the offered branding package and follow the generated upload and configuration instructions.

## Verify the result and review the handoff

Distinguish changes the agent completed from configuration and tests that you still need to perform.

1. If the agent implemented code changes, review the changed files and the results of your project's applicable format, lint, type, build, and test commands.
2. If you chose a dry run, confirm that the plan includes dependency-ordered implementation tasks, acceptance checks, tenant instructions, tests, and rollback guidance.
3. Complete the manual checks for your selected journeys and factors. Compare redirect URIs exactly and check the applicable authority, scopes, protected routes, and logout behavior.
4. Review the handoff for completed checks, remaining tenant steps, and blocked items. Don't treat a generated instruction as a completed tenant configuration step.