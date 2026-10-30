---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Migrate Google files to Microsoft 365 for business - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/moveto-microsoft-365/migrate-files-migration-manager?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: heidip
author: MicrosoftHeidi
manager: dansimp
ms.date: 2026-09-25T00:00:00.0000000Z
audience: Admin
ms.topic: upgrade-and-migration-article
ms.service: m365-core
ms.subservice: migration
ms.localizationpriority: medium
ms.collection:
- Tier1
- highpri
- M365-subscription-management
- Adm_O365
- must-keep
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- adminvideo
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to migrate Google files to Microsoft 365 for business by using the SharePoint Migration Manager.
ai-usage: ai-assisted
locale: en-us
document_id: 4a52c60e-e617-f204-187b-25bfdb413975
document_version_independent_id: 4a52c60e-e617-f204-187b-25bfdb413975
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/moveto-microsoft-365/migrate-files-migration-manager.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/moveto-microsoft-365/migrate-files-migration-manager
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/moveto-microsoft-365/migrate-files-migration-manager.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 99ac974a-155b-56c3-9d38-3a4af34912de
---

# Migrate Google files to Microsoft 365 for business - Microsoft 365 admin | Microsoft Learn

Note

When you move from Google Workspace to Microsoft 365 for business, use Migration Manager to copy files from personal and shared Google drives. This article provides an overview. For complete instructions, see [Migrate Google Workspace to Microsoft 365 with Migration Manager](/en-us/sharepointmigration/mm-google-overview).

## Watch: Migrate Google files to Microsoft 365 for business

Watch this video and find more on the [Microsoft 365 small business YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198217).

The video uses a SharePoint admin center entry point. Follow the Microsoft 365 admin center steps in this article for this procedure.

Note

Migration Manager copies files to Microsoft 365 for business. The original files remain in Google Drive. Google-native files are exported to Microsoft Office or other supported formats. Review [unsupported files](/en-us/sharepointmigration/mm-unsupported-files) and migration reports to identify content that wasn't copied.

## Before you start

For standard Migration Manager projects that use OneDrive destinations, make sure each user's OneDrive exists before assigning destinations. If it doesn't, [pre-provision OneDrive for users in your organization](/en-us/sharepoint/pre-provision-accounts). Migration Manager Lite can provision OneDrive automatically for eligible projects. If automatic provisioning isn't available or doesn't succeed, use the linked procedure before migration.

Before starting a migration:

- Review [permission settings](/en-us/sharepointmigration/mm-project-settings-permissions) and identity mappings. File-level permissions aren't migrated by default; files inherit destination-folder permissions. Choose the required settings and validate destination access with representative users.
- Review [version settings](/en-us/sharepointmigration/file-versions). By default, only the most recent file version is copied. Select the supported version-history option you need before migrating, and verify the resulting history.
- Check Google Drive for unorganized or orphaned files and decide how to preserve any that you need. These files aren't scanned, migrated, or listed in migration reports. See [unsupported files](/en-us/sharepointmigration/mm-unsupported-files).

Note

Google migration is supported in GCC, but not in GCC High or DoD. See [Specialty environments support](/en-us/sharepointmigration/mm-specialty-environments-support).

## Install the Microsoft 365 Migration app

Use the following steps to install the Microsoft 365 Migration app in your Google Workspace environment.

1. In the Microsoft 365 admin center, go to **Setup** &gt; **Migration resources**.
2. Under **Self-service migration and import tools**, select **Explore migration & imports tools**.
3. Select **Google Workspace** to open the Google Workspace migration page.
4. Select **Connect to Google Workspace**.
5. On the **Install the migration app** page, select **Install and authorize**.
6. On the **Google Workspace Marketplace** page, sign in with a Google Workspace super administrator account.
7. Select the organization-wide installation option shown by Google Workspace Marketplace, such as **Admin install** or **Domain install**.
8. Select **Continue**.
9. Select the checkbox, then select **Finish**.
10. When the installation completes, select **Done**.
11. Return to the **Install the migration app** page, and select **Next**.
12. Select **Sign in to Google Workspace**, and then enter your Google Workspace admin credentials.
13. Select **Finish**.

## Select and scan drives

In standard Migration Manager, select and scan the drives you want to migrate before copying them to the migrations list. Migration Manager Lite guides eligible tenants through task selection, destination assignment, identity mapping, settings, and migration without the separate scan and copy steps.

1. On the **Drives** tab, select the Google drives you want to copy to Microsoft 365.
2. Select **Scan**. When the scan completes, the drives show a scan status of **Ready to migrate**.
3. Select **Copy to Drive migrations**.

## Start the migration

After selecting and scanning the drives you want to migrate, use the following steps to migrate them.

1. On the **Drive migrations** tab, verify the destination paths of the drives you want to migrate. Edit them if needed.
2. Select the drives you want to migrate, and then select **Migrate**.
3. When migration completes successfully, each drive shows a **Migration status** of **Completed**.

    A task can show **Completed** when unsupported items weren't migrated. Download and review both the migration summary and detailed reports, and resolve or account for failures and exclusions.

After resolving migration errors and preserving excluded content, continue with [canceling Google Workspace](cancel-google).