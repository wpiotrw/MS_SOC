---
layout: Conceptual
title: Configure guest user settings in eDiscovery (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-guest-users
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure guest access for eDiscovery cases in Microsoft Purview using Azure B2B collaboration. Learn which external users can be added and the current role limitations for guest reviewers.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-18T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: b404f508-e950-f8ec-1fb5-9b6dfbcd34ae
document_version_independent_id: b404f508-e950-f8ec-1fb5-9b6dfbcd34ae
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-guest-users.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-guest-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-guest-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 81f60086-0023-ea76-8abe-f0cb0f810fa8
---

# Configure guest user settings in eDiscovery (preview) | Microsoft Learn

With guest access, you can provide access to eDiscovery cases to people outside your organization. You can invite guest users to eDiscovery cases just like you can invite guests into your Teams environment.

A guest is someone who doesn't have a work or school account with your organization. For example, guests can include external partners, vendors, suppliers, or consultants. Anyone who isn't part of your organization can be added as a guest for an eDiscovery case. This access means that anyone with a Microsoft Entra account or personal email account (Outlook, Gmail, or others) can participate as a guest in eDiscovery and have access to specific eDiscovery cases.

Guest access in eDiscovery uses [Azure B2B technology](/en-us/azure/active-directory/external-identities/what-is-b2b), which depends on an organization-wide Azure collaboration setting. When you invite a guest to eDiscovery, a guest account is created for them in Microsoft Entra ID. They're covered by the same compliance and auditing protection as other Microsoft 365 users. Guest access is subject to Microsoft Entra ID and Microsoft 365 service limits.

Note

eDiscovery guests are currently limited to *Reviewer* role group permission only. The *Reviewer* role allows guests to access review sets and review case data, but it doesn't include the *Manage review set tags* role. As a result, guest users can't create, edit, delete, or apply review set tags. Review set tagging requires both the *Review* and *Manage review set tags* roles. For more information about the reviewer role, see [Assign eDiscovery permissions in the Microsoft Purview portal](edisc-permissions#rbac-roles-related-to-ediscovery).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Set up guest access

Setting up guest access in eDiscovery requires configuring other settings in Microsoft Entra ID. To enable access to invite guests to eDiscovery cases, complete the following steps:

1. Check the [B2B external collaboration settings](/en-us/microsoft-365/solutions/collaborate-as-team?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#azure-external-collaboration-settings) to ensure that collaboration with guests isn't blocked. If the **Guest invite settings** is set to *No one in the organization can invite guests including admins* then inviting guests into eDiscovery is disabled. Contact your system administrator to ensure [the B2B external collaboration settings are properly configured](/en-us/azure/active-directory/external-identities/external-collaboration-settings-configure). You can view and update the collaboration setting using the [Microsoft Graph authorizationPolicy resource](/en-us/graph/api/resources/authorizationpolicy).
2. Depending on the specific configuration in Step 1, eDiscovery administrators might or might not need additional roles to approve a guest access request submitted from the eDiscovery user.

    - If the *Anyone in the organization can invite guest including guests and nonadmins (most inclusive)* or *Member users and users assigned to specific admin roles can invite guests including guests with member permission* options are selected, then eDiscovery administrators can approve invitation requests without extra roles.
    - If *Only users assigned to specific admin roles can invite guests* is selected, then the eDiscovery administrator who approves the invitation request requires the *Invite guest* role to approve and trigger the invitation email to the guest. See the [Assign Microsoft Entra roles to users](/en-us/azure/active-directory/roles/manage-roles-portal) article for guidance on how to add the *Guest Inviter* role to users. If you prefer to use PowerShell to add this role, see [Assign the Guest Inviter role to a user](/en-us/azure/active-directory/external-identities/external-collaboration-settings-configure#assign-the-guest-inviter-role-to-a-user).
3. To enable collaboration with guest reviewers from other Microsoft 365 cloud environments, including if you're a Microsoft Azure Government organization, both your organization and the guest’s organization must enable specific connection settings. For detailed configuration guidance, see [Collaborate with guests from other Microsoft 365 cloud environments](/en-us/microsoft-365/solutions/collaborate-guests-cross-cloud?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

## Enable guest access in eDiscovery

eDiscovery admins must enable guest access in eDiscovery before they can invite users as guests.

To enable guest access for guests, complete the following steps:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Settings** &gt; **eDiscovery** &gt; **Guest users**.
2. Set **Guest access** to *On*.

Now eDiscovery managers and admins can start the guest invitation process within any eDiscovery case. To configure guest access to specific cases, see [Learn about access and permission settings in eDiscovery cases](edisc-settings-access-permissions#guest-access-in-ediscovery).