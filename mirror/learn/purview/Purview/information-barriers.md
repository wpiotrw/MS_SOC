---
layout: Conceptual
title: Learn about Information Barriers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Information Barriers in Microsoft Purview. Information Barriers can help to avoid conflicts of interest and safeguard internal information between users and organizational areas.
keywords: Microsoft 365, Microsoft Purview, compliance, Information Barriers
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-information-barriers
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
f1.keywords:
- NOCSH
ms.custom: seo-marvel-apr2020
ai-usage: ai-assisted
locale: en-us
document_id: d314e4e1-d3d7-2b2d-9f7c-cf803daf7c14
document_version_independent_id: d314e4e1-d3d7-2b2d-9f7c-cf803daf7c14
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 6d06616f-058a-cf05-12ce-cce3cb585099
---

# Learn about Information Barriers | Microsoft Learn

Microsoft Purview Information Barriers (IB) is a compliance solution that restricts two-way communication and collaboration between groups and users in Microsoft Teams, SharePoint, and OneDrive. Often used in highly regulated industries, IB helps avoid conflicts of interest and safeguards internal information between users and organizational areas.

When you create IB policies, users who can't communicate or share files with other specific users can't find, select, chat, or call those users. IB policies automatically put checks in place to detect and prevent unauthorized communication and collaboration among defined groups and users. IB policies are independent from [compliance boundaries](ediscovery-set-up-compliance-boundaries) for eDiscovery investigations that control user content locations that eDiscovery managers can search.

IB policies can allow or prevent communication and collaboration between groups and users for the following example scenarios:

- Users in the *Day Trader* group can't communicate or share files with the *Marketing Team*.
- Instructors in one school can't communicate or share files with students in another school in the same school district.
- Finance personnel working on confidential company information can't communicate or share files with certain groups within their organization.
- An internal team with trade secret material can't call or chat online with users in certain groups within their organization.
- A research team can only call or chat online with a product development team.
- A SharePoint site for *Day Trader* group can't be shared or accessed by anyone outside of the *Day Trader* group.
- A lawyer's data obtained from one client can't be accessed by a lawyer at the same firm who represents a different client.
- Government information access and control are limited across departments and groups.
- A group of people in a company can only chat with a client or a specific customer via guest access during a customer engagement.

Important

Information Barriers **only supports** two-way communication and collaboration restrictions. For example, a scenario where Marketing can communicate and collaborate with Day Traders, but Day Traders can't communicate and collaborate with Marketing **isn't supported**.

Important

Information barrier (IB) policies can't restrict communication and collaboration between groups and users in email messages including Exchange Online. If your organization needs to define and control email communications, consider using [Exchange mail flow rules](/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Information Barriers and Microsoft Teams

In Microsoft Teams, IB policies determine and prevent the following kinds of unauthorized communication and collaboration:

- Searching for a user
- Adding a member to a team
- Starting a chat session with someone
- Starting a group chat
- Inviting someone to join a meeting
- Sharing a screen
- Placing a call
- Sharing a file with another user
- Accessing a file through a sharing link

If the users conducting these activities in Microsoft Teams are included in an IB policy to prevent the activity, they can't proceed. In addition, everyone included in an IB policy can be potentially blocked from communicating with other users in Microsoft Teams. When users affected by IB policies are part of the same team or group chat, they might be removed from those chat sessions and further communication with the group might not be allowed.

For more information, see [Information Barriers in Microsoft Teams](/en-us/MicrosoftTeams/information-barriers-in-teams).

## Information Barriers and SharePoint and OneDrive

In SharePoint and OneDrive, IB policies detect and prevent the following kinds of unauthorized collaboration:

- Adding a member to a site
- Accessing site or content by a user
- Sharing site or content with another user
- Searching a site

For more information, see [Information Barriers in SharePoint](/en-us/sharepoint/information-barriers?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) and [Information Barriers in OneDrive](/en-us/onedrive/information-barriers).

## Information Barriers and Microsoft Planner

As a work management tool, [Microsoft Planner](/en-us/planner/planner-for-admins) enables users to collaborate on plans and tasks. If your compliance admin configures IB policies to restrict communication and collaboration between user segments, Microsoft Planner supports these restrictions.

IB policies allow administrators to enable or disable search restrictions in the people picker. By using IB support in Planner, when a user searches for others in the people picker to share a plan or to assign a task, they don't see users from segments they're restricted from communicating with. This restriction prevents users from one segment from sharing plans or assigning tasks to users in another segment.

IB support in Microsoft Planner is available only for basic plans in the following applications:

- Planner Web
- Planner in Teams web
- Planner in Teams desktop
- Planner in Teams mobile app

### Policy behavior

When IB policy administrators create a new policy or modify an existing policy, users can still access existing plans shared with them or already assigned tasks. For any subsequent plan sharing or task assignment, an IB policy check is triggered and collaboration is permitted or restricted as defined by the policy.

## Information Barriers and Exchange Online

Information barrier (IB) policies can't restrict communication and collaboration between groups and users in email messages. If your organization needs to define and control email communications, consider using [Exchange mail flow rules](/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). **Enabling Information Barriers in environments without configured ABPs can result in the loss of Address List visibility between all users**.

The following table summarizes the key differences between IB modes for Exchange Online Address Book Policies (ABPs):

| Feature | Single and multi-segment modes | Legacy mode |
| --- | --- | --- |
| ABP management | Automatic; no reliance on existing ABPs | Automatic; existing ABPs must be removed first |
| ABP for unsegmented users | System creates ABP with empty address lists | Not applicable |
| Custom ABP changes | Allowed; keep consistent with IB segments | Not supported; IB controls all ABPs |
| Hierarchical address book | Available for users not in an IB segment | Available for users not in an IB segment |
| Key prerequisite | None for ABPs | Remove all existing ABPs before enabling IB |

### Information Barriers and Exchange for single and multi-segment modes

If your organization uses *[single](information-barriers-multi-segment#check-the-ib-mode-for-your-organization)*[or](information-barriers-multi-segment#check-the-ib-mode-for-your-organization)[multi-segment](information-barriers-multi-segment#check-the-ib-mode-for-your-organization)[mode](information-barriers-multi-segment#check-the-ib-mode-for-your-organization), Information Barriers no longer relies on Exchange Online Address Book Policies (ABPs). Information barrier (IB) policies can't restrict communication in email messages. If your organization needs to define and control email communications, consider using [Exchange mail flow rules](/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). Enabling Information Barriers doesn't affect organizations that use ABPs. If users don't have an ABP defined with associated IB segments and policies, the system **automatically creates an ABP with empty address lists for these users**. You can change these ABPs as needed, they are not automatically adjusted based on your IB Segmentation. Keep your ABPs consistent with the segments you configure in Information Barriers to avoid losing proper Address List visibility. Avoid user visibility differences between your existing ABPs and your new Information Barriers configuration.

### Information Barriers and Exchange for legacy mode

If your organization uses [*legacy* mode](information-barriers-multi-segment#check-the-ib-mode-for-your-organization), IB policies rely on [Exchange Online Address Book Policies (ABPs)](/en-us/exchange/address-books/address-book-policies/address-book-policies?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). ABPs let organizations virtually assign users into specific groups to provide customized views of the organization's global address list (GAL). When you create IB policies, the system automatically creates ABPs for the policies. As you add IB policies in your organization, the structure and behavior of your GAL changes to comply with IB policies.

Before you define and apply IB policies, remove all existing Exchange address book policies in your organization. IB policies rely on address book policies, and existing ABPs aren't compatible with the ABPs that IB creates. To remove your existing address book policies, see [Remove an address book policy in Exchange Online](/en-us/exchange/address-books/address-book-policies/remove-an-address-book-policy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). When you enable IB policies and enable hierarchical address book, all users not included in an IB segment see the [hierarchical address book](/en-us/exchange/address-books/hierarchical-address-books/hierarchical-address-books?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Exchange Online.

## Ready to get started?

- [Get started with Information Barriers](information-barriers-policies): Define segments and create your first IB policies.
- [Information Barriers attributes](information-barriers-attributes): Review the Microsoft Entra attributes available for defining user segments.
- [Use multi-segment support in Information Barriers](information-barriers-multi-segment): Assign users to multiple segments for complex organizational scenarios.