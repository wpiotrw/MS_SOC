---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Reassign app owners in Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/reassign-app-owners?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how administrators can reassign app ownership, add another owner, or remove an owner by using the Copilot Managed Runtime CLI.
ms.topic: how-to
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ms.author: jordanchodak
manager: alaug
ms.reviewer: 
author: jordanchodak
ms.date: 2026-11-19T00:00:00.0000000Z
locale: en-us
document_id: 294647f0-952c-4464-173b-c43ebe3a3867
document_version_independent_id: 294647f0-952c-4464-173b-c43ebe3a3867
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/reassign-app-owners.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/reassign-app-owners
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/reassign-app-owners.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: f6a30273-ef2c-c17f-cc7a-1a2d501ea7a7
---

# Reassign app owners in Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn

Reassign app ownership so your team can continue to maintain an app when its creator leaves, changes roles, or hands responsibility to IT. Use the [Copilot Managed Runtime CLI (`ms` command)](../../../copilot-managed-runtime/developer/apps/quickstart-managed-apps-cli#install-the-copilot-managed-runtime-cli) to add the new owner, verify their access, and then remove the former owner if they no longer need owner access.

This article describes the administrator workflow. Find the app in the Microsoft 365 admin center first and then, use the CLI to update its owners.

Important

These commands are currently available only for apps that use a platform-managed Git repository.

## What changes when you update app owners

Adding an app owner grants owner access without replacing or demoting existing owners. The platform manages this access through owner assignments on the app's platform-managed Git repository.

Removing an owner removes that owner assignment; it doesn't automatically assign a lesser role. The person might retain access through other roles assigned separately. Additionally, changing app ownership doesn't transfer ownership of the app's connections or change their credentials. As part of a handoff, review the new owner's data-source permissions and any connections that depend on the departing owner's account.

## Prerequisites

Before you begin, make sure you have:

- The [Copilot Managed Runtime CLI](../../../copilot-managed-runtime/developer/apps/quickstart-managed-apps-cli#install-the-copilot-managed-runtime-cli) installed.
- An account with the Power Platform Administrator or Global Administrator role in the tenant that contains the app.
- The app's **App ID**, which is a GUID.
- The email address or Microsoft Entra object ID of each owner you want to add or remove.

## Find the app ID

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com).
2. Go to **Apps** &gt; **All apps**, and select the **Copilot Managed Runtime** tab.
3. Search for the app. You can filter by **Owner** to find apps associated with a departing employee.
4. Select the app to open its details pane, then copy the **App ID**.

For more information about the inventory, see [View and oversee apps across your tenant](inventory).

## Sign in to the CLI

Open a terminal and use [`ms auth login`](../../../copilot-managed-runtime/developer/apps/ms-cli-command-reference#ms-auth-login) to sign in with the account authorized to manage app ownership:

```bash
ms auth login
```

Make sure you're signed in to the tenant that contains the app.

## Add an owner

Use [`ms admin add owner`](../../../copilot-managed-runtime/developer/apps/ms-cli-command-reference#ms-admin-add-owner) to add an app owner. Replace `<app-id>` with the GUID you copied and `newowner@contoso.com` with the new owner's email address:

```bash
ms admin add owner newowner@contoso.com --app <app-id>
```

The command prompts for confirmation. Review the app ID, environment ID, and owner before you continue. Adding an owner preserves existing owners and other role assignments.

To add more than one owner, separate their email addresses or object IDs with spaces:

```bash
ms admin add owner newowner@contoso.com backupowner@contoso.com --app <app-id>
```

You can use a Microsoft Entra object ID instead of an email address. For a service principal, use its object ID.

## Verify the new owner's access

Since the **Owner** field doesn't update with due to known issue, ask the new owner to sign in with their own account and verify that they can perform the app maintenance tasks they need, including accessing the app's source code. For guidance on accessing source code, see [Collaborate on a Copilot Managed Runtime app](../../../copilot-managed-runtime/developer/apps/collaborate-on-app).

Also verify that the new owner has the data-source permissions and connections needed to maintain the app. Connections remain tied to their existing credentials. If the app depends on the former owner's personal connections, the new owner might need to create their own connections.

## Remove an owner

Use [`ms admin remove owner`](../../../copilot-managed-runtime/developer/apps/ms-cli-command-reference#ms-admin-remove-owner) to remove an existing app owner. Replace `<app-id>` with the app's GUID and `formerowner@contoso.com` with the email address of the owner to remove. If you're reassigning ownership, verify the replacement owner's access first.

```bash
ms admin remove owner formerowner@contoso.com --app <app-id>
```

The command prompts for confirmation unless you pass `--force`. Check the person and app before you confirm.

Read the result to confirm that an owner assignment was removed. If no matching owner assignment is found, retry using the person's Microsoft Entra object ID.

The platform prevents you from removing the app's last owner so the app always has at least one owner.

## Resolve ownership changes that fail

| Issue | What to check |
| --- | --- |
| You don't have sufficient permission. | Confirm the signed-in account, tenant, and admin permissions. |
| The CLI can't find the app. | Verify that `--app` contains the correct GUID and that the signed-in account can access the app in its tenant. |
| The repository association isn't supported. | Confirm that the app has a platform-managed repository. For external GitHub repositories, manage access in GitHub. |
| The inventory still shows the app's creator. | This is a known issue. The **Owner** field doesn't currently reflect ownership changes made through the CLI. Verify the person's access to confirm the change. |

## Known issues

- Updating app owners through the CLI doesn't currently update the **Owner** field on the **All apps** page. This field continues to show the app's creator rather than its current owner. Verify new owner's access after you update an app owner manually instead of using the **Owner** field.