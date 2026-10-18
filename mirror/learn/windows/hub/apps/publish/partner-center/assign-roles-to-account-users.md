---
layout: Conceptual
title: Assign roles to account users - Windows apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/apps/publish/partner-center/assign-roles-to-account-users
ms.service: windows-app-sdk
recommendations: true
ROBOTS: INDEX, FOLLOW
author: GrantMeStrength
ms.author: jken
Search.Product: eADQiWindows 10XVcnh
uhfHeaderId: MSDocsHeader-WinDevCenter
breadcrumb_path: /windows/breadcrumbs/toc.json
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_system: OpenSource
ms.subservice: apps
ms.update-cycle: 365-days
description: Learn how to assign standard roles when adding users to your Partner Center account.
ms.date: 2026-10-14T00:00:00.0000000Z
ms.topic: article
ms.localizationpriority: high
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 9e162eb7-c446-bd51-0af9-c9b1828ff4ad
document_version_independent_id: 9e162eb7-c446-bd51-0af9-c9b1828ff4ad
original_content_git_url: https://github.com/MicrosoftDocs/windows-dev-docs-pr/blob/live/hub/apps/publish/partner-center/assign-roles-to-account-users.md
site_name: Docs
depot_name: MSDN.windows-uwp-hub
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.windows-uwp-hub/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: apps/publish/partner-center/assign-roles-to-account-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: hub/apps/publish/partner-center/assign-roles-to-account-users.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: da7001e5-f634-fe81-2c78-869a8e26ebc4
---

# Assign roles to account users - Windows apps | Microsoft Learn

By default, a set of standard roles is presented for you to choose from when you add a user, group, or Microsoft Entra ID application to your Partner Center account. Each role has a specific set of permissions in order to perform certain functions within the account.

Unless you opt to define [custom permissions](overview-of-roles-and-permissions-for-account-users#custom-permissions) by selecting **Customize permissions**, each user, group, or Microsoft Entra ID application that you add to an account must be assigned at least one of the following standard roles.

Note

The **owner** of the account is the person who first created it with a Microsoft account (and not any user(s) added through Microsoft Entra ID). This account owner is the only person with complete access to the account, including the ability to delete apps, create and edit all account users, and change all financial and account settings.

| Role | Description |
| --- | --- |
| Manager | Has complete access to the account, except for changing tax and payout settings. This includes managing users in Partner Center, but note that the ability to create and delete users in the Microsoft Entra ID tenant is dependent on the account's permission in Microsoft Entra ID. That is, if a user is assigned the Manager role, but does not have global administrator permissions in the organization's Microsoft Entra ID, they will not be able to create new users or delete users from the directory (though they can change a user's Partner Center role). **Note:** if the Partner Center account is associated with more than one Microsoft Entra ID tenant, a Manager can’t see complete details for a user (including first name, last name, password recovery email, and whether they are a Microsoft Entra ID global administrator) unless they are signed in to the same tenant as that user with an account that has global administrator permissions for that tenant. However, they can add and remove users in any tenant that is associated with the Partner Center account. |
| Developer | Can upload packages and submit apps and add-ons, and can view the [Usage report](/en-us/partner-center/usage-report) for telemetry details. Can access [Cross-Device Experiences](https://developer.microsoft.com/windows/project-rome) functionality. Can’t view financial info or account settings. |
| Business Contributor | Can view [Health](/en-us/partner-center/health-report) and [Usage](/en-us/partner-center/usage-report) reports. Can't create or submit products, change account settings, or view financial info. |
| Finance Contributor | Can view [payout reports](/en-us/partner-center/payout-statement), financial info, and acquisition reports. Can’t make any changes to apps, add-ons, or account settings. |
| Marketer | Can view non-financial [analytic reports](/en-us/partner-center/analyze-app-performance). Can’t make any changes to apps, add-ons, or account settings. |

The table below shows some of the specific features available to each of these roles (and to the account owner).

| - | Account owner | Manager | Developer | Business Contributor | Finance Contributor | Marketer |
| --- | --- | --- | --- | --- | --- | --- |
| **Acquisition report (including Near Real Time data)** | Can view | Can view | No access | No access | Can view | No access |
| **Feedback report/responses** | Can view and send feedback | Can view and send feedback | Can view and send feedback | No access | No access | Can view and send feedback |
| **Health report (including Near Real Time data)** | Can view | Can view | Can view | Can view | No access | No access |
| **Usage report** | Can view | Can view | Can view | Can view | No access | No access |
| **Payout account** | Can update | No access | No access | No access | Can update | No access |
| **Tax profile** | Can update | No access | No access | No access | Can update | No access |
| **Payout summary** | Can view | No access | No access | No access | Can view | No access |
| **Self serve sales** | Can update | No access | No access | No access | No access | Can update |

If none of the standard roles are appropriate, or you wish to limit access to specific apps and/or add-ons, you can grant custom permissions to the user by selecting **Customize permissions**, as described in the next page.