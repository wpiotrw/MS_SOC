---
layout: Conceptual
title: Install FSLogix Applications - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/how-to-install-fslogix
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Installation instructions for the FSLogix Apps (Core Product) and standalone Rule Editors.
author: msft-jasonparker
ms.topic: how-to
ms.date: 2026-03-09T00:00:00.0000000Z
ms.author: japarker
locale: en-us
document_id: 18388b81-2ca8-2da3-d9f4-cd369f50e541
document_version_independent_id: 18388b81-2ca8-2da3-d9f4-cd369f50e541
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/how-to-install-fslogix.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: how-to-install-fslogix
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/how-to-install-fslogix.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
platformId: 9a3f8fb4-e180-773d-dcb7-4eee8771c3de
---

# Install FSLogix Applications - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

This article describes how to download and install FSLogix Apps (Core Product), Rule Editor, and Java Rule Editor (retired).

All FSLogix installations use the same steps no matter if the installation is new or an upgrade.

## Prerequisites

- Review the [FSLogix prerequisites](overview-prerequisites).
- Review the [Installation FAQ](overview-faq#installation).
- Review the [Release Notes](overview-release-notes).

## Download FSLogix

We recommend that you upgrade to the [latest version](https://aka.ms/fslogix-latest) of FSLogix as quickly as your deployment process can allow. FSLogix provides hotfix releases to address current and potential bugs that affect customer deployments. To open a support case, you're required to have the latest version.

You can download FSLogix via direct download or through Microsoft Download Center.

### Direct download

If you integrate the download and installation of FSLogix as part of an automated build routine, you can obtain the latest version of FSLogix on [this website](https://aka.ms/fslogix_download).

### Microsoft Download Center

You can search and find previous versions^1^ of FSLogix on Microsoft Download Center.

^1 Microsoft Download Center provides only the last two feature and associated hotfix releases.^

## Install FSLogix Apps (Core Product)

1. Extract the downloaded .zip file.
2. Go to the directory where the files were extracted.
3. Double-click **x64 (64-bit)**.
4. Double-click **Release**.
5. Double-click **FSLogixAppsSetup.exe**.
6. Agree to the licensing terms, and select **Install**.

    ![Screenshot that shows the start of the licensing terms.](media/apps-click-through.png)

    Note

    You can install FSLogix Apps to an alternate location, but we don't recommend it.
7. Observe the FSLogix Apps installation progress.

    ![Screenshot that shows the progress screen.](media/install-progress.png)
8. Reboot.

## Install FSLogix Apps Rule Editor and Java Rule Editor (retired)

The Rule Editor and Java Rule Editor (retired) are intended for administrator workstations.

Be aware that:

- Both the Rule Editor and Java Rule Editor (retired) installation dialogs are identical to the screenshots and aren't provided here.
- You can install the editors to an alternate location, but we don't recommend it.

1. Extract the downloaded .zip file.
2. Go to the directory where the files were extracted.
3. Double-click **x64 (64-bit)**.
4. Double-click **Release**.
5. Double-click **FSLogixAppsRuleEditorSetup.exe**.
6. Agree to the licensing terms, and select **Install**.

## Unattended installation options

Each of the FSLogix installers supports unattended and silent installation for automated use cases. Installation commands and descriptions are described in the following table.

| Command switch | Description |
| --- | --- |
| `/install` | Default product installation. |
| `/repair` | Repairs a previous product installation. |
| `/uninstall` | Uninstalls a previous product installation. |
| `/layout` | Creates a local copy of the install bundle. |
| `/passive` | Displays minimal UI and no prompts. |
| `/quiet` | Displays no UI and no prompts. |
| `/norestart` | Suppresses any attempts to restart. By default, the UI prompts before restart. |
| `/log log.txt` | Logs installation to a specific path and file. Default log is in `%TEMP%`. |

## Verify product installation and version

Before you begin verification, make sure that:

- You manually installed FSLogix.
- It was installed as part of your golden image.
- It was preinstalled as part of the Windows 10 or Windows 11 Azure Marketplace image.

It doesn't matter how FSLogix was installed. Verifying the installation and version is a valuable step before configuration.

For the most recent release, see the [Release Notes](overview-release-notes).

### Installed apps

1. Sign in to the virtual machine as a local administrator or with an account that has administrative privileges.
2. Right-click the **Start** icon.
3. Select **Installed apps**.

    ![Screenshot that shows the Installed apps context menu.](media/fsl-installed-apps.jpg)
4. Locate **Microsoft FSLogix Apps**.

    ![Screenshot that shows the list of installed apps.](media/fslogix-installed-apps-list.jpg)

### Command line

1. Sign in to the virtual machine as a local administrator or with an account that has administrative privileges.
2. Select **Start** and enter **command prompt** in the **Start** menu search box.
3. Select **Command Prompt** on the **Start** menu.

    ![Screenshot that shows the Command Prompt Start menu.](media/fsl-command-prompt.jpg)
4. Change the directory to **C:\Program Files\FSLogix\Apps**.
5. Enter **frx version**.

    ![Screenshot that shows the command prompt frx utility.](media/fsl-cmd-frx-version.jpg)