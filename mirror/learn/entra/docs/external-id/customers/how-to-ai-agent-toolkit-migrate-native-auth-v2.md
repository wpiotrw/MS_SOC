---
layout: Conceptual
title: Migrate native authentication with the AI agent toolkit - Microsoft Entra External ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-ai-agent-toolkit-migrate-native-auth-v2
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/microsoftentraexternalid
author: csmulligan
ms.author: cmulligan
ms.service: entra-external-id
ms.subservice: external
manager: dougeby
description: Use the eeid-native-auth-migrate-v2 skill to plan, approve, apply, and validate a native authentication V1-to-V2 migration in your app.
ms.topic: how-to
ms.date: 2026-11-11T00:00:00.0000000Z
ai-usage: ai-generated
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 72b982ef-7cc3-2100-e81b-7159f3f1568f
document_version_independent_id: 72b982ef-7cc3-2100-e81b-7159f3f1568f
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/external-id/customers/how-to-ai-agent-toolkit-migrate-native-auth-v2.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: external-id/customers/how-to-ai-agent-toolkit-migrate-native-auth-v2
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/external-id/customers/how-to-ai-agent-toolkit-migrate-native-auth-v2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/5f286262-a4cb-47f4-92d3-dc24f172492b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e31b9be-b6e9-4221-a20b-d1460dbd5dfa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/90571f66-8410-4272-8117-79ce87fc2dcc
- https://authoring-docs-microsoft.poolparty.biz/devrel/8d63a4c4-4889-43b4-a98e-8e50dbfdb083
platformId: ee2be035-bc6f-7896-c8f2-de0ba80ef51a
---

# Migrate native authentication with the AI agent toolkit - Microsoft Entra External ID | Microsoft Learn

Use the `eeid-native-auth-migrate-v2` skill to migrate an existing app's native authentication from V1 to V2. The skill inventories your code, creates a reviewable plan, applies approved changes, reviews those changes for security, and reports validation results.

You can migrate sign-in, sign-up, and self-service password reset together or one flow at a time. Multifactor authentication and strong authentication method registration move with the flow they belong to.

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](../media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

## Prerequisites

- Completion of [Install the AI agent toolkit](how-to-install-ai-agent-toolkit).
- An existing app that uses native authentication V1, with source code the agent can inspect and change.

Build and unit test tools are recommended for validation, but they aren't required to use the skill. If you choose to run validation commands, make sure your project's tools are available.

Use the skill with one of these integration approaches:

- An app that calls the native authentication API directly.
- A JavaScript single-page app that uses MSAL native authentication.
- An Android app that uses MSAL native authentication.
- An iOS or macOS app that uses MSAL native authentication.

The direct API approach isn't limited to the SDK platforms listed here. The skill needs access to the app-owned HTTP calls and flow code. It isn't a guide for adding authentication to a new app, upgrading an MSAL package on its own, or changing browser-redirect authentication.

## Start the migration and choose its scope

Start in the app you want to migrate. The skill inspects V1 usage before proposing code changes.

1. Open your app's source folder in your coding agent. If the workspace contains several apps, identify the app to migrate.
2. Ask the agent to use `eeid-native-auth-migrate-v2`. Choose the request that matches your intended scope:

    - To migrate all flows, enter `Migrate my app's native auth from V1 to V2`.
    - To migrate sign-in only, enter `Migrate only sign-in to native auth V2 and keep the other flows on V1`.
3. Review the agent's inventory and any questions about the integration approach or scope.

If the skill doesn't start, name it explicitly in your request. In coding agents that support it, you can enter `/eeid-native-auth-migrate-v2`.

The skill writes `.native-auth-v2-migration/plan.md` in your app's root folder. It doesn't change application code before you approve the plan.

## Review and revise the migration plan

The plan records what changes, what stays on V1, what users will notice, and how the migration is validated.

1. Open `.native-auth-v2-migration/plan.md`.
2. Confirm the selected flows and deferred flows. Check that changes to shared code preserve the flows that remain on V1.
3. Review the proposed behavior changes, implementation tasks, and open decisions.
4. Review any planned validation commands and their baseline and post-change runs. Adjust the plan's validation settings with the agent if needed.
5. Answer open decisions and request revisions until the scope is correct. For example, enter `Remove password reset from the migration plan`.

Different flows can use different versions, but a single flow can't mix V1 and V2. This boundary includes MFA and method registration that occur within the flow.

Each plan change needs approval of the new revision. Resolve open decisions before approving.

## Approve and apply the plan

Approval authorizes the current plan revision, including its validation commands. Review the plan before giving that approval.

1. Confirm that the plan matches your intended scope and has no unresolved decisions.
2. Approve the plan in chat. For example, enter:

    ```text
    The plan looks good. Approved, go ahead.
    ```
3. Let the agent perform its pre-apply check and any planned baseline validation. If files changed since planning or an in-scope file has uncommitted changes, resolve the conflict and review any revised plan before continuing.
4. Let the agent apply the approved changes, update the applicable tests, review its changes for security, and run any planned validation commands.

The `eeid-native-auth-migrate-v2` workflow doesn't commit, push, or create branches. It leaves changes in your working tree for you to review.

## Check the report and test the app

The migration report records the outcome rather than assuming every check passed.

1. Open `.native-auth-v2-migration/report.md`.
2. Review the outcome, deviations from the plan, security review findings, and baseline and post-change validation results. Check the reasons for any failed or not-run checks.
3. Review the application changes in your working tree.
4. Perform the manual tests listed in the report for the migrated flows and any deferred flows that share code.

Keep unresolved findings and manual tests visible when deciding whether the migration is ready for your own commit and release.

## Continue a migration or migrate deferred flows

The migration folder records progress so that the skill can determine the next step.

1. To resume an interrupted migration, ask the agent to use the skill and enter `Continue my native auth migration`.
2. After a phase is reported, review the outcome before starting deferred flows. To continue with the remaining flows, enter `Start the next phase and migrate the remaining flows to V2`.

An unfinished plan created by a different version of the skill can't be continued as-is. The skill requires its version-change restart procedure instead.