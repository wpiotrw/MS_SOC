---
layout: Conceptual
title: Azure Virtual Desktop (classic) retirement - Azure | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/previous-versions/azure/virtual-desktop-classic/classic-retirement
breadcrumb_path: /previous-versions/azure/breadcrumb/toc.json
feedback_system: None
ROBOTS: NOINDEX,NOFOLLOW
is_archived: true
uhfHeaderId: MSDocsHeader-Archive
docs_archive: tool
recommendations: true
is_retired: false
ms.suite: office
recommendation_types:
- Learn
ms.service: artificial-intelligence
ms.topic: conceptual
permissioned-type: public
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
adobe-target: true
description: Information about the retirement of Azure Virtual Desktop (classic).
ms.date: 2023-09-27T00:00:00.0000000Z
locale: en-us
author: huypub
document_id: ccf5dabe-b41f-4a9c-7f52-393c987b8899
document_version_independent_id: e813fa6e-3ff0-d13f-943c-15213f50846d
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-archive-pr/blob/live/articles/virtual-desktop-classic/classic-retirement.md
site_name: Docs
depot_name: MSDN.Azure-docs-archive
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
asset_id: virtual-desktop-classic/classic-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-desktop-classic/classic-retirement.md
platformId: ae8df2f1-919b-aab3-4f6c-ef52b30e3b0b
---

# Azure Virtual Desktop (classic) retirement - Azure | Microsoft Learn

Important

This content applies to Azure Virtual Desktop (classic), which doesn't support Azure Resource Manager Azure Virtual Desktop objects.

Azure Virtual Desktop (classic) will retire on **September 30, 2026**. You should transition to Azure Virtual Desktop before that date.

[Azure Virtual Desktop](overview) replaces Azure Virtual Desktop (classic). Here are some of the benefits of using Azure Virtual Desktop instead of Azure Virtual Desktop (classic):

- Deployments via Azure Resource Manager (ARM)
- Unified resource management
- Improved networking and security
- Scaling and automation features
- Feature availability and updates

## Retirement timeline

Beginning **September 30, 2023**, you'll no longer be able to create new Azure Virtual Desktop (classic) tenants. Existing Azure Virtual Desktop (classic) resources can still be managed, migrated, and are supported through **September 30, 2026**.

Important

If you have more than 500 application groups or manage multi-tenant environments, you can request an exemption.

## Required action

To avoid service disruptions, migrate to Azure Virtual Desktop before September 30, 2026. Here are some articles to help you migrate:

- [Migrate manually from Azure Virtual Desktop (classic)](manual-migration)
- [Migrate automatically from Azure Virtual Desktop (classic)](automatic-migration)

## Exemption process

To be able to continue creating tenants in Azure Virtual Desktop (classic), you need to create an exemption. An exemption is available if you have more than 500 application groups or manage multitenant environments. To create an exemption:

1. Browse to [New support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest) in the Azure portal.
2. On the **Problem description** tab, complete the following information:

    | Parameter | Value/Description |
    | --- | --- |
    | Issue type | Select **Technical** from the drop-down list |
    | Subscription | Select a subscription containing Azure Virtual Desktop (classic) resources from the drop-down list. |
    | Service | Select **My services**. |
    | Service type | Select **Azure Virtual Desktop** from the drop-down list |
    | Resource | Select an Azure Virtual Desktop (classic) resource from the drop-down list. |
    | Summary | Enter a description of your issue. |
    | Problem type | Select **Issues configuring Azure Virtual Desktop (classic)** from the drop-down list. |
    | Problem subtype | Select **Tenant creation exemption request** from the drop-down list. |
3. Complete the remaining tabs and select **Create**.

## Help and support

If you have a support plan and you need technical help, see [Azure Virtual Desktop (classic) troubleshooting overview, feedback, and support](troubleshoot-set-up-overview-2019#create-a-support-request) for information on how to create a support request. You can also ask community experts questions at [Azure Virtual Desktop - Microsoft Q&A](/en-us/answers/tags/221/azure-virtual-desktop).