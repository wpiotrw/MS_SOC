---
layout: Conceptual
monikers:
- vs-2022
- visualstudio
defaultMoniker: visualstudio
versioningType: Ranged
title: Administrative Templates (ADMX) - Visual Studio (Windows) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/visualstudio/install/administrative-templates?view=visualstudio
config_moniker_range: '>= vs-2022'
feedback_system: Standard
feedback_help_link_url: https://developercommunity.microsoft.com/VisualStudio
feedback_help_link_type: ask-the-community
feedback_product_url: https://developercommunity.visualstudio.com/VisualStudio/suggest
breadcrumb_path: /visualstudio/_breadcrumb/toc.json
ms.manager: nitinme
author: madskristensen
ms.author: madsk
audience: developer
ms.service: visual-studio-windows
uhfHeaderId: MSDocsHeader-VisualStudio
toc_preview: true
archive_url: /previous-versions/visualstudio
recommendations: true
description: Configure and deploy group policy settings to the client machines in the Visual Studio ADMX Template and control Visual Studio behavior.
ms.date: 2025-11-04T00:00:00.0000000Z
ms.topic: concept-article
ms.custom: vs-acquisition
ms.subservice: installation
locale: en-us
document_id: feb00ee2-4e24-a9cf-5f19-1d7715f79c76
document_version_independent_id: feb00ee2-4e24-a9cf-5f19-1d7715f79c76
original_content_git_url: https://github.com/MicrosoftDocs/visualstudio-docs-pr/blob/live/docs/install/administrative-templates.md
default_moniker: visualstudio
site_name: Docs
depot_name: VS.docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/VS.docs/{branchName}{pdfName}
asset_id: install/administrative-templates
moniker_range_name: f22a899ea89b53168e6a2ccb9c507f5c
monikers:
- vs-2022
- visualstudio
item_type: Content
source_path: docs/install/administrative-templates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/4628cbd9-6f47-4ae1-b371-d34636609eaf
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/be21deb8-8c64-44b0-b71f-2dc56ca7364f
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 5f7b9b11-3f50-b11b-e34b-527ea8537db2
---

# Administrative Templates (ADMX) - Visual Studio (Windows) | Microsoft Learn

IT Administrators in organizations may want to control certain aspects of Visual Studio behavior to achieve consistency, compliance, or compatibility across their client machines. An easy way to accomplish this level of control is to configure and then deploy group policy settings to the client machines. The Visual Studio policies are consolidated in the [Visual Studio ADMX Template](https://aka.ms/vs/admx/details) into different categories, making them easily understandable and discoverable.

The recommended approach to discover and configure Visual Studio policies across your organization is to use the [Microsoft Intune settings catalog](/en-us/mem/intune/configuration/settings-catalog). Alternative approaches are described below.

The Visual Studio group policy settings contained in the ADMX file are machine-wide for all users, meaning they intend to cover all applicable installed instances, versions, and SKUs of Visual Studio. Sometimes a policy is particular to a specific version of Visual Studio, and the template clearly calls this out.

## Visual Studio policy categories

The following are the main categories of Visual Studio policies that are included in the Visual Studio Administrative Templates (ADMX):

- [**Copilot**](../ide/visual-studio-github-copilot-admin#disable-copilot-skus) - controls Copilot SKUs and agent mode
- [**Dev Tunnels**](https://aka.ms/devtunnels/vs/admx) - controls test functionality
- [**Feedback**](feedback-survey-policies) - controls behavior of feedback and survey avenues.
- [**Install and Update**](configure-policies-for-enterprise-deployments) - controls product acquisition behavior.
- [**Live Share**](https://aka.ms/vsls-policies) - controls user and hosts settings.
- **Privacy** - controls [Intellicode](/en-us/visualstudio/intellicode/intellicode-privacy) and [Customer Experience Improvement Program](https://aka.ms/vs/admx/telemetry) settings.

## Acquiring the Visual Studio Administrative Template (ADMX)

The [Visual Studio Administrative Template (ADMX)](https://aka.ms/vs/admx/details) can be downloaded from the Microsoft Download Center. The default installation path is `C:\Windows\PolicyDefinitions`, a location that makes them instantly visible to the Group Policy Editor (gpedit.exe) tool, but you can install them anywhere. The templates are updated periodically, so if you use them we recommend that you check back periodically to get the latest updates.

## Deploying the policies

For cloud connected environments managed by Microsoft Intune, you have two choices for configuring and deploying Visual Studio policies.

1. You can access Visual Studio policies through the [settings catalog](/en-us/mem/intune/configuration/settings-catalog).
2. You can also [import the Visual Studio Administrative Templates (ADMX)](/en-us/mem/intune/configuration/administrative-templates-import-custom#add-the-admx-and-adml-files) into your **Devices** &gt; **Configuration profiles**, and then [create a customized **Configuration profile**](/en-us/mem/intune/configuration/administrative-templates-import-custom#create-a-profile-using-your-imported-files) based on the imported ADMX files. The Visual Studio Administrative Templates (ADMX) depend on the [Windows administrative template (Windows.admx)](/en-us/mem/intune/configuration/administrative-templates-windows), so make sure you manually import that one in too.

For machines within a corporate network, you can use the [Group Policy editor](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265982%28v=ws.11%29) or [Microsoft Endpoint Manager (SCCM)](/en-us/mem/configmgr/core/understand/introduction) to deploy Visual Studio policies.

## Support or troubleshooting

Sometimes, things can go wrong. If your Visual Studio installation fails, see [Troubleshoot Visual Studio installation and upgrade issues](troubleshooting-installation-issues) for step-by-step guidance.

Here are a few more support options:

- Use the [installation chat](https://visualstudio.microsoft.com/vs/support/#talktous) (English only) support option for installation-related issues.
- Report product issues to us by using the [Report a Problem](../ide/how-to-report-a-problem-with-visual-studio) tool that appears both in the Visual Studio Installer and in the Visual Studio IDE. If you're an IT Administrator and don't have Visual Studio installed, you can submit [IT Admin feedback](https://aka.ms/vs/admin/feedback).
- Suggest a feature, track product issues, and find answers in the [Visual Studio Developer Community](https://aka.ms/feedback/suggest?space=8).