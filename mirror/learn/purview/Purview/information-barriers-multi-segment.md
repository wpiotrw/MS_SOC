---
layout: Conceptual
title: Use multi-segment support in Information Barriers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use multi-segment support with Information Barriers in Microsoft Purview.
keywords: Microsoft 365, Microsoft Purview, compliance, Information Barriers
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-barriers
ms.collection:
- highpri
- purview-compliance
- m365solution-mip
- m365initiative-compliance
f1.keywords:
- NOCSH
ms.custom: seo-marvel-apr2020
ai-usage: ai-assisted
locale: en-us
document_id: a29665ed-5f33-2524-e6f6-f6a95120fe59
document_version_independent_id: a29665ed-5f33-2524-e6f6-f6a95120fe59
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-multi-segment.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-multi-segment
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-multi-segment.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 8e988d94-cfe8-de35-dfc1-be4266223514
---

# Use multi-segment support in Information Barriers | Microsoft Learn

Important

Support for 5,000 segments and assigning users to multiple segments is only available when your organization isn't in *Legacy* mode. Assigning users to multiple segments requires extra steps to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

For organizations in *Legacy* mode, the maximum number of segments supported is 250, and users are restricted to being assigned to only one segment. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

By using the multi-segment mode, you can assign users in your organization to up to 10 segments in Information Barriers instead of being limited to just one segment. This support for more diverse communication rules between individuals and groups supports more complex organizational and operational scenarios. For organizations using multi-segment support, define all Information Barriers policies with an allow list.

When you configure multi-segment support, user compatibility depends on each user's assignment to a shared segment. If users share assignment to the same segment, they're compatible. For example, the following table shows that User A and User B aren't compatible because they don't share an assigned segment. However, User A is compatible with User C and User B is compatible with User C because they each have an assigned segment in common.

| User | Assigned segments |
| --- | --- |
| User A | Segment 1, Segment 2 |
| User B | Segment 3, Segment 4 |
| User C | Segment 2, Segment 4 |

## Multi-segment example: North School District's schools, segments, and policies

The North School District has two schools, School 1 and School 2. The district policy is to allow students and teachers to communicate with each other only if they're both in the same school. For example, a student and teacher that are both in School 1 can communicate, but a student in School 1 can't communicate with a teacher in School 2. For this scenario, configure multiple segments to support the following district policy scenarios:

### North School District's schools and plan

North School District has two schools:

| Segment | Allowed communication | Prevented communication |
| --- | --- | --- |
| School 1 | Students and teachers in School 1 | Students and teachers in School 2 |
| School 2 | Students and teachers in School 2 | Students and teachers in School 1 |

For this structure, North School District's plan includes three IB policies:

1. An IB policy that enables students and teachers in School 1 to communicate with each other.
2. An IB policy that enables students and teachers in School 2 to communicate with each other.
3. An IB policy that allows teachers in School 1 and School 2 to communicate with each other.

### North School District's defined segments

North School District uses the *Department* attribute in Microsoft Entra ID to define segments, as follows:

**School1 segment**:

```powershell
New-OrganizationSegment -Name "School1" -UserGroupFilter "Department -eq 'School1'"
```

**School2 segment**:

```powershell
New-OrganizationSegment -Name "School2" -UserGroupFilter "Department -eq 'School2'"
```

**AllTeachers segment**:

```powershell
New-OrganizationSegment -Name "AllTeachers" -UserGroupFilter "MemberOfGroup -eq 'AllTeachersgroup@northschoolsdistrict.com'"
```

After defining the segments, North School District defines the IB policies.

### North School District's IB policies

North School District defines three IB policies:

**Policy 1**: Students and teachers in School 1 can communicate with each other.

```powershell
New-InformationBarrierPolicy -Name School1Policy -SegmentsAllowed 'School1' -AssignedSegment 'School1' -State Active
```

When you activate and apply this policy, students and teachers in School 1 can communicate with each other. This policy is a one-way policy; it doesn't prevent students and teachers in School 1 from communicating with School 2. For that, Policy 2 is needed.

**Policy 2**: Students and teachers in School 2 can communicate with each other.

```powershell
New-InformationBarrierPolicy -Name School2Policy -SegmentsAllowed 'School2' -AssignedSegment 'School2' -State Active
```

When you activate and apply this policy, students and teachers in School 2 can communicate with each other.

**Policy 3**: Teachers in different schools can communicate with each other.

```powershell
New-InformationBarrierPolicy -Name AllTeachersPolicy -SegmentsAllowed 'AllTeachers' -AssignedSegment 'AllTeachers' -State Active
```

When you activate and apply this policy, teachers in School 1 and School 2 can communicate with each other.

After defining segments and policies, North School District runs the **Start-InformationBarrierPoliciesApplication** cmdlet to apply the policies. When the cmdlet finishes, North School District implements its communication policy for students and teachers.

## Check the IB mode for your organization

To support assigning users to multiple segments, verify that your IB organization supports multiple segments. Run the following cmdlet to verify your IB mode in the [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json):

```powershell
Get-PolicyConfig
```

If the value of the `InformationBarrierMode` property is *SingleSegment*, enable multi-segment support by following the guidance in the Enable multiple segment support for users section in this article. If the value of the `InformationBarrierMode` property is *MultiSegment*, you can skip enabling support for multi-segment because it's already enabled for your organization.

If the value of the `InformationBarrierMode` property is *Legacy*, enabling multi-segment isn't supported for your organization. *Legacy* organizations are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

## Enable multiple segment support for users

To enable multiple segment support for organizations in *SingleSegment* mode, make sure that you don't currently have any IB segments or policies defined for your organization. Run the following cmdlet to enable multiple segment support in your organization:

```powershell
Set-PolicyConfig -InformationBarrierMode 'MultiSegment'
```

Important

If you enable multiple segments and configure IB in your organization, don't revert to single segment support.

## Multi-segment support for users in OneDrive

When you configure OneDrive for Information Barriers to support multiple segments, the following behavior applies:

- A multi-segment user's OneDrive is automatically set to *Owner Moderated* mode.
- In *Explicit* or *Mixed* mode, a multi-segment user can access a OneDrive if they belong to at least one of its segments and have site access permission. All other modes use the same access experience as single segment support.
- Sharing behavior follows the IB mode set for OneDrive. In *Explicit* mode, users can share with others who have the same segment. In *Open* or *Owner Moderated* mode, users can share with compatible users per IB policies.

For more information, see [Use Information Barriers with OneDrive](information-barriers-onedrive).

## Multi-segment support for users in SharePoint Online

When you configure SharePoint for Information Barriers to support multiple segments, the following behavior applies:

- A user with multiple segments who creates a SharePoint site (either a Microsoft 365 group connected site or a non-group site) automatically uses *Owner Moderated* mode.
- In *Explicit* mode, users get access if they have at least one segment that matches the site's segment and they have site access permission. All other modes use the same access experience as single segment support.
- Sharing behavior follows the IB mode of the site. In *Explicit* mode, users can share with others who match the site's segment. In *Implicit* or *Owner Moderated* mode, users can share with existing members of the connected Microsoft 365 group. In *Open* mode, users can share with compatible users per IB policy.

For more information, see [Use Information Barriers with SharePoint](information-barriers-sharepoint).

## Multi-segment support for users in Microsoft Teams

When you configure Teams for Information Barriers to support multiple segments, the following behavior applies:

- A user with multiple segments who creates a team automatically uses *Implicit* mode.
- All users in the team must have one segment that is compatible with all other users.

For more information, see [Use Information Barriers with Microsoft Teams](/en-us/microsoftteams/information-barriers-in-teams?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).