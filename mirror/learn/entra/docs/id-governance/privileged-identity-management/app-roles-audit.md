---
layout: Conceptual
title: View app role audit history in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/app-roles-audit
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: kenwith
ms.author: kenwith
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Learn how to view application-level and personal app role audit history in Microsoft Entra Privileged Identity Management during preview.
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.custom: pim, msecd-doc-authoring-1031
ai-usage: ai-generated
locale: en-us
document_id: 546fae84-a77c-5112-c346-5f924a124ed9
document_version_independent_id: 546fae84-a77c-5112-c346-5f924a124ed9
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/app-roles-audit.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/app-roles-audit
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/app-roles-audit.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 6ce68787-8214-463e-45a7-b09bc82912e6
---

# View app role audit history in PIM (preview) - Microsoft Entra ID Governance | Microsoft Learn

Microsoft Entra Privileged Identity Management (PIM) for app roles is in preview. Use resource and personal audit history to investigate app role assignment changes, activation activity, and role-setting changes.

## Prerequisites

PIM for app roles (preview) requires Microsoft Entra ID Governance licenses.

To view **Resource audit**, you must own the target service principal or have one of the administrative roles listed in [Role assignment conditions](app-roles-assign#permissions).

## View resource audit history

Use **Resource audit** to investigate the app role activity recorded for the selected application.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**.
3. Select the application you want to view audit history for.
4. Expand **Activity**, and then select **Resource audit**.
5. Use **Time span**, **Audit type**, **Original requestor**, and **Subject type** to narrow the results.
6. Use **Search by requestor, resource, primary target or subject** to find relevant entries.
7. Review the **Time**, **Requestor**, **Action**, **Resource name**, **Primary target**, **Subject**, and **Status** columns.
8. Select an entry to open **Audit details**. Review its **Action**, **Status**, and **Status Reason**, together with the other available details.
9. Select **Close** to return to the list. Use **Refresh** to reload the audit view.

**Audit details** includes **Date**, **Requestor**, **Action**, **Resource**, **Scope**, **Primary target**, **Subject**, **Type**, **Reason**, **Ticket system**, **Ticket number**, **Status**, **Status Reason**, and **Correlation ID**. Some fields can be empty or show a dash for a particular event.

## View my audit

Use **My audit** to review app role activity associated with your account for the selected application.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **ID Governance** &gt; **Privileged Identity Management** &gt; **App Roles (Preview)**.
3. Select the application you want to view audit history for.
4. Expand **Activity**, and then select **My audit**.
5. Set **Time span** to **Last day**, **Last week**, **Last month**, or **Custom**.
6. Use **Audit type** to choose **All**, **Eligible**, **Assigned**, **Activated**, or **Active (Assigned + Activated)**.
7. Use **Subject type** and **Search by requestor, resource, primary target or subject** to narrow the results.
8. Select an entry to inspect **Audit details**. Review the recorded action, status, and other available fields, and select **Close** when you finish.

## Export audit history

The audit toolbar provides **Export**. The following steps describe the **Export Audits** dialog shown from **My audit**.

1. Open **My audit**, and select **Export**.
2. Under **Select the format of file**, choose **CSV** or **JSON**.
3. Enter **Name of the file**.
4. Select **Start** to begin the export.