---
layout: Conceptual
title: Restrict multitenant Microsoft Entra apps - Microsoft Entra ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/restrict-multitenant-apps
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/22920db1-ad25-ec11-b6e6-000d3a4f0789
author: omondiatieno
ms.author: jomondi
ms.service: entra-id
ms.subservice: enterprise-apps
manager: dougeby
description: Require multitenant apps to explicitly list the tenants they'll operate in for increased security
ms.reviewer: arcrowe
ms.date: 2026-11-24T00:00:00.0000000Z
ms.topic: how-to
ms.localizationpriority: medium
ms.collection: RestrictedMode
audience: admin
ai-usage: ai-assisted
locale: en-us
document_id: 775335ca-e98b-5527-8e69-a8775d6aca70
document_version_independent_id: 775335ca-e98b-5527-8e69-a8775d6aca70
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/identity/enterprise-apps/restrict-multitenant-apps.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity/enterprise-apps/restrict-multitenant-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/identity/enterprise-apps/restrict-multitenant-apps.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 044a25aa-187f-054b-33ff-08654b459188
---

# Restrict multitenant Microsoft Entra apps - Microsoft Entra ID | Microsoft Learn

Applications that accept tokens from any Microsoft Entra tenant significantly expand their attack surface. When an app doesn't explicitly restrict which tenants it can authenticate, any external tenant - including one controlled by a bad actor - can attempt to obtain tokens and interact with the app. Microsoft recommends that applications explicitly constrain the tenants they trust, limiting authentication to a defined set of known tenants. This reduces lateral movement risk and helps ensure apps are only accessed from environments they're designed to operate in.

Tenant administrators can require applications in their tenant to declare the tenants they're allowed to authenticate from. When this control is enabled, going forward, applications in the tenant must specify an allow list of tenant IDs they'll operate in. Over time, this drives a more secure-by-default posture as apps are created or updated, ensuring tenant boundaries are explicitly enforced. Existing applications aren't automatically restricted when the policy is applied; administrators can accelerate risk reduction by identifying unrestricted apps and updating them to declare their allowed tenants.

## Restrict app audience

Multitenant apps can be restricted in the Microsoft 365 admin center.

For required roles and access instructions, see [Baseline security mode settings](/en-us/microsoft-365/baseline-security-mode/baseline-security-mode-settings#before-you-begin).

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) and go to **Settings** &gt; **Org settings** &gt; **Security and Privacy**.
2. Select **Baseline Security Mode**, find the **New apps require assignment of the tenants allowed to access them** setting, and switch the toggle to **On**.

Apps can also be restricted using the [Microsoft Entra admin center](https://aka.ms/app-mgmt-policy-ux). For more information, see [Configure app management policies](configure-app-management-policies).

Enabling this setting blocks both new and existing apps from becoming multitenant without restrictions. You can gauge the impact of enabling this setting by identifying recent creations of multitenant apps. From the Microsoft 365 admin center:

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Security and Privacy**.
2. Select **Baseline Security Mode** and find the **New apps require assignment of the tenants allowed to access them** setting.
3. Select **download report** to view recent multitenant app creations in your organization.

## Restrict existing app audiences

Blocking creation of new unrestricted apps doesn't affect existing apps. Existing apps that already allow any tenant can be identified using the Microsoft 365 admin center.

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org settings** &gt; **Security and Privacy**.
2. Select **Baseline Security Mode** and find the **New apps require assignment of the tenants allowed to access them** setting.
3. Select **download report** to view existing unrestricted multitenant apps.

Identify the tenants where an existing multitenant app operates before adding them to its audience restrictions. Existing application audiences can be restricted using the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType%7E/null/sourceType/Microsoft_AAD_IAM), [Microsoft Graph PowerShell](/en-us/powershell/module/microsoft.graph.beta.applications/update-mgbetaapplication?view=graph-powershell-beta&amp;preserve-view=true), or the [Microsoft Graph API](/en-us/graph/api/resources/signinaudiencerestrictionsbase?view=graph-rest-beta&amp;preserve-view=true).