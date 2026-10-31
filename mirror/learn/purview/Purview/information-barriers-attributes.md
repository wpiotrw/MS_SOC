---
layout: Conceptual
title: Information Barriers attributes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-attributes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article is a reference for the Microsoft Entra user account attributes that you can use to define Information Barriers segments.
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
f1.keywords:
- NOCSH
ms.custom: seo-marvel-apr2020
ai-usage: ai-assisted
locale: en-us
document_id: 7833ee0c-ab84-eaab-eb22-39307bbc2bc0
document_version_independent_id: 7833ee0c-ab84-eaab-eb22-39307bbc2bc0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-attributes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-attributes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-attributes.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 6eb1d24d-8730-1f23-e614-a4c6b7bd36c1
---

# Information Barriers attributes | Microsoft Learn

You can use certain attributes in Microsoft Entra ID to segment users in Information Barriers (IB). After you define segments, use them as filters for IB policies. For example, you might use **Department** to define segments of users by department within your organization (assuming no single user works for two departments at the same time).

This article describes how to use attributes with Information Barriers and provides a list of attributes you can use. For more information about Information Barriers, see the following resources:

- [Information Barriers](information-barriers)
- [Define policies for Information Barriers in Microsoft Teams](information-barriers-policies)
- [Edit (or remove) IB policies](information-barriers-edit-segments-policies)

## How to use attributes in IB policies

Use the attributes listed in this article to define or edit segments of users. Your defined segments serve as parameters (called *UserGroupFilter* values) in [IB policies](information-barriers-policies).

1. Decide which attribute you want to use to define segments. (See the Reference section in this article.)
2. Make sure the user accounts have values filled in for the attribute(s) you selected in Step 1. View user account details, and if necessary, edit user accounts to include attribute values.

    - To edit multiple accounts or use PowerShell to edit a single account, see [Configure user account properties with Office 365 PowerShell](/en-us/microsoft-365/enterprise/configure-user-account-properties-with-microsoft-365-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
    - To edit a single account, see [Add or update a user's profile information using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
3. [Define segments using PowerShell](information-barriers-policies#define-segments-using-powershell), similar to the following examples. Before running these cmdlets, [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

    Tip

    You can also define segments using the Microsoft Purview portal. For more information, see [Define segments using the portals](information-barriers-policies#define-segments-using-the-portals).

    **Define a segment using the Department attribute**:

    ```powershell
    New-OrganizationSegment -Name "Segment1" -UserGroupFilter "Department -eq 'Department1'"
    ```

    **Define a segment using the MemberOf attribute** (suppose this attribute contains group names, such as "BlueGroup"):

    ```powershell
    New-OrganizationSegment -Name "SegmentA" -UserGroupFilter "MemberOf -eq 'BlueGroup'"
    ```

    **Define a segment using ExtensionAttribute1** (suppose this attribute contains job titles, such as "DayTrader"):

    ```powershell
    New-OrganizationSegment -Name "DayTraders" -UserGroupFilter "ExtensionAttribute1 -eq 'DayTrader'"
    ```

    Tip

    When you define segments, use the same attribute for all your segments. For example, if you define some segments using *Department*, define all of the segments using *Department*. Don't define some segments using *Department* and others using *MemberOf*. Make sure your segments don't overlap; each user belongs to exactly one segment.

## Reference

The following table lists the attributes that you can use with Information Barriers.

Tip

The most commonly used attributes for defining segments are **Department**, **MemberOf**, **Company**, and **ExtensionAttribute1–15**. For more information about defining segments, see [Get started with Information Barriers](information-barriers-policies).

| Microsoft Entra property name(LDAP display name) | Exchange property name |
| --- | --- |
| Co | Co |
| Company | Company |
| Department | Department |
| Description | Description |
| ExtensionAttribute1 | CustomAttribute1 |
| ExtensionAttribute2 | CustomAttribute2 |
| ExtensionAttribute3 | CustomAttribute3 |
| ExtensionAttribute4 | CustomAttribute4 |
| ExtensionAttribute5 | CustomAttribute5 |
| ExtensionAttribute6 | CustomAttribute6 |
| ExtensionAttribute7 | CustomAttribute7 |
| ExtensionAttribute8 | CustomAttribute8 |
| ExtensionAttribute9 | CustomAttribute9 |
| ExtensionAttribute10 | CustomAttribute10 |
| ExtensionAttribute11 | CustomAttribute11 |
| ExtensionAttribute12 | CustomAttribute12 |
| ExtensionAttribute13 | CustomAttribute13 |
| ExtensionAttribute14 | CustomAttribute14 |
| ExtensionAttribute15 | CustomAttribute15 |
| Mail | WindowsEmailAddress |
| MailNickname | Alias |
| MemberOf | MemberOfGroup |
| MSExchExtensionCustomAttribute1 | ExtensionCustomAttribute1 |
| MSExchExtensionCustomAttribute2 | ExtensionCustomAttribute2 |
| MSExchExtensionCustomAttribute3 | ExtensionCustomAttribute3 |
| MSExchExtensionCustomAttribute4 | ExtensionCustomAttribute4 |
| MSExchExtensionCustomAttribute5 | ExtensionCustomAttribute5 |
| PhysicalDeliveryOfficeName | Office |
| PostalCode | PostalCode |
| ProxyAddresses | EmailAddresses |
| StreetAddress | StreetAddress |
| TargetAddress | ExternalEmailAddress |
| UsageLocation | UsageLocation |
| UserPrincipalName | UserPrincipalName |