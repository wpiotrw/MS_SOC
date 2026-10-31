---
layout: Conceptual
title: Manage Information Barriers policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-edit-segments-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to edit or remove policies for Information Barriers.
keywords: Microsoft 365, Microsoft Purview, compliance, Information Barriers
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-barriers
ms.collection:
- purview-compliance
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: f1c4693f-cf44-5051-3b1c-e9355b0fe440
document_version_independent_id: f1c4693f-cf44-5051-3b1c-e9355b0fe440
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-edit-segments-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-edit-segments-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-edit-segments-policies.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
platformId: 892cd7d8-8f50-4e6e-2c08-4de111c5a342
---

# Manage Information Barriers policies | Microsoft Learn

After you [define Information Barriers (IB) policies](information-barriers-policies), you might need to change those policies or your user segments as part of [troubleshooting](/en-us/office365/troubleshoot/information-barriers/information-barriers-troubleshooting?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) or regular maintenance.

## Manage segments and policies

- **Edit user account attributes**: Fill in attributes in Microsoft Entra ID that you can use to define segments. Edit user account attributes when users aren't included in segments they should be, to change which segments users are in, or to define segments by using different attributes.
- **Edit a segment**: Edit segments when you want to change how you define a segment. For example, you might have originally defined segments by using *Department* and now want to use another attribute, such as *MemberOf*.
- **Edit a policy**: Edit an Information Barriers policy when you want to change how a policy works. For example, instead of blocking communications between two segments, you might decide you want to allow communications to occur only between certain segments.
- **Set a policy to inactive status**: Set a policy to inactive status when you want to make changes to a policy, or when you don't want a policy to be in effect.
- **Remove a policy**: Remove an Information Barriers policy when you no longer need a particular policy in place.
- **Remove a segment**: Remove an Information Barriers segment when you no longer need a particular segment.
- **Remove a policy and a segment**: Remove an Information Barriers policy and a segment at the same time.
- **Stop a policy application**: Stop the process of applying Information Barriers policies. Stopping a policy application isn't instant, and it doesn't undo policies that are already applied to users.
- **Enable or disable user discoverability**: Enable or disable if users are displayed in the people picker.
- **[Define policies for Information Barriers](information-barriers-policies)**: Define an Information Barriers policy when you don't already have such policies in place, and you must restrict or limit communications between specific groups of users.
- **[Resolve Information Barriers issues](/en-us/office365/troubleshoot/information-barriers/information-barriers-troubleshooting?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)**: Refer to this article when you run into unexpected issues with Information Barriers.

Important

To perform the tasks described in this article, you must be assigned an appropriate role, such as one of the following roles:

- Microsoft 365 Enterprise Global Administrator
- Global Administrator
- Compliance Administrator
- IB Compliance Management

For more information about prerequisites for Information Barriers, see [Prerequisites (for Information Barriers policies)](information-barriers-policies#step-1-make-sure-prerequisites-are-met).

Make sure to [connect to the Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Edit user account attributes

Complete the following steps to edit attributes that segment users. For example, if you're using a Department attribute and one or more user accounts don't currently have any values listed for Department, edit those user accounts to include Department information. Use user account attributes to define segments so you can assign Information Barriers policies.

1. Use the **Get-ExoInformationBarrierRelationship** cmdlet to view details for a specific user account, such as attribute values and assigned segments. Use Identity parameters in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). You can use any value that uniquely identifies each user, such as name, alias, distinguished name, canonical domain name, email address, or GUID.

    Syntax:

    ```powershell
    Get-ExoInformationBarrierRelationship -RecipientId1 <value> -RecipientId2 <value>
    ```

    Example:

    ```powershell
    Get-ExoInformationBarrierRelationship -Identity meganb -Identity2 alexw
    ```

    In this example, two user accounts are referenced: *meganb* for *Megan*, and *alexw* for *Alex*.
2. Decide which attribute to edit for your user account profiles. For more information, see [Attributes for Information Barriers policies](information-barriers-attributes).
3. Edit one or more user accounts to include values for the attribute you selected in the previous step. Use one of the following procedures:

    - To edit a single account, see [Add or update a user's profile information using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
    - To edit multiple accounts (or use PowerShell to edit a single account), see [Configure user account properties with Office 365 PowerShell](/en-us/microsoft-365/enterprise/configure-user-account-properties-with-microsoft-365-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Edit a segment

Complete the following steps to edit the definition of a user segment. For example, you might change the name of a segment or the filter that determines who is included in the segment.

1. Use the **Get-OrganizationSegment** cmdlet to view all existing segments.

    ```powershell
    Get-OrganizationSegment
    ```

    You see a list of segments and details for each segment, such as the segment type, its UserGroupFilter value, who created or last modified it, GUID, and more.

    Tip

    Print or save your list of segments for reference. For example, if you want to edit a segment, you need to know its name or identifying value (used with the Identity parameter).
2. Use the **Set-OrganizationSegment** cmdlet with the **Identity** parameter and relevant details to edit a segment.

    Syntax:

    ```powershell
    Set-OrganizationSegment -Identity GUID -UserGroupFilter "attribute -eq 'attributevalue'"
    ```

    Example:

    ```powershell
    Set-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd -UserGroupFilter "Department -eq 'HRDept'"
    ```

    In this example, you update the department name to *HRDept* for the segment with GUID *c96e0837-c232-4a8a-841e-ef45787d8fcd*.
3. When you finish editing segments for your organization, you can either [define](information-barriers-policies#step-3-create-ib-policies) or edit Information Barriers policies.

## Edit a policy

1. Use the **Get-InformationBarrierPolicy** cmdlet to view a list of current Information Barriers policies.

    ```powershell
    Get-InformationBarrierPolicy
    ```

    In the list of results, find the policy that you want to change. Note the policy's GUID and name.
2. Use the **Set-InformationBarrierPolicy** cmdlet with an **Identity** parameter, and specify the changes you want to make.

    Important

    You can only edit the segments assigned to a policy. You can't change a policy type from *block* to *allow* or from *allow* to *block*. To change the policy type, you must set the existing policy to inactive status and create a new policy with the desired type and segments.

    Example: Suppose you defined a policy to block the *Research* segment from communicating with the *Sales* and *Marketing* segments:

    ```powershell
    New-InformationBarrierPolicy -Name "Research-SalesMarketing" -AssignedSegment "Research" -SegmentsBlocked "Sales","Marketing"
    ```

    Suppose you want to change the policy so that users in the *Research* segment are blocked from communicating with the *HR* segment instead. To make this change:

    ```powershell
    Set-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c93772471 -SegmentsBlocked "HR"
    ```

    In this example, you change the blocked segments from *Sales* and *Marketing* to *HR*.
3. When you finish editing a policy, make sure to apply your changes. For more information, see [Apply Information Barriers policies](information-barriers-policies#step-4-apply-ib-policies).

## Set a policy to inactive status

1. Use the **Get-InformationBarrierPolicy** cmdlet to view a list of current Information Barriers policies.

    ```powershell
    Get-InformationBarrierPolicy
    ```

    In the list of results, find the policy that you want to change or remove. Note the policy's GUID and name.
2. Use the **Set-InformationBarrierPolicy** cmdlet with the *Identity* parameter and the *State* parameter set to *Inactive* to set the policy's status to inactive.

    Syntax:

    ```powershell
    Set-InformationBarrierPolicy -Identity GUID -State Inactive
    ```

    Example:

    ```powershell
    Set-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c9377247 -State Inactive
    ```

    In this example, the Information Barriers policy that has GUID *43c37853-ea10-4b90-a23d-ab8c9377247* is set to an inactive status.
3. Use the **Start-InformationBarrierPoliciesApplication** cmdlet to apply your changes.

    ```powershell
    Start-InformationBarrierPoliciesApplication
    ```

    Changes are applied user-by-user for your organization. If your organization is large, it can take 24 hours or more for this process to complete. As a general guideline, it takes about an hour to process 5,000 user accounts.
4. One or more Information Barriers policies are set to inactive status. From here, you can take any of the following actions:

    - Keep it as is (a policy set to inactive status has no effect on users)
    - Edit a policy
    - Remove a policy

## Remove a policy

1. Use the **Get-InformationBarrierPolicy** cmdlet to view a list of current Information Barriers policies.

    ```powershell
    Get-InformationBarrierPolicy
    ```

    In the list of results, find the policy that you want to remove. Note the policy's GUID and name.
2. Make sure the policy is set to inactive status. To set the policy's status to inactive, use the **Set-InformationBarrierPolicy** cmdlet with an Identity parameter and the State parameter set to Inactive.

    Syntax:

    ```powershell
    Set-InformationBarrierPolicy -Identity GUID -State Inactive
    ```

    Example:

    ```powershell
    Set-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c9377247 -State Inactive
    ```

    In this example, you set an Information Barriers policy that has GUID *43c37853-ea10-4b90-a23d-ab8c9377247* to an inactive status.
3. To apply your changes on the policy, use the **Start-InformationBarrierPoliciesApplication** cmdlet.

    ```powershell
    Start-InformationBarrierPoliciesApplication
    ```

    Changes are applied user-by-user for your organization. If your organization is large, it can take 24 hours or more for this process to complete. As a general guideline, it takes about an hour to process 5,000 user accounts.
4. Use the **Remove-InformationBarrierPolicy** cmdlet with an Identity parameter.

    Syntax:

    ```powershell
    Remove-InformationBarrierPolicy -Identity GUID
    ```

    Example:

    ```powershell
    Remove-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c93772471
    ```

    In this example, you remove the policy that has GUID *43c37853-ea10-4b90-a23d-ab8c93772471*.

    When prompted, confirm the change.

## Remove a segment

1. Use the **Get-OrganizationSegment** cmdlet to view all existing segments.

    ```powershell
    Get-OrganizationSegment
    ```

    You see a list of segments and details for each segment, such as the segment type, its UserGroupFilter value, who created or last modified it, GUID, and more.

    Tip

    Print or save your list of segments for reference later. For example, if you want to edit a segment, you need to know its name or identify value (this value works with the Identity parameter).
2. Identify the segment to remove and make sure you remove the IB policy associated with the segment. For more information, see the Remove a policy procedure.
3. Edit the segment to remove the relationship of users to that segment. This action updates the segment definition and removes all users from the segment. Use the UserGroupFilter parameter to disassociate users from the segment before removal.

    Use the **Set-OrganizationSegment** cmdlet with the *Identity* parameter and relevant details to edit a segment.

    Syntax:

    ```powershell
    Set-OrganizationSegment -Identity GUID -UserGroupFilter "attribute -eq 'attributevalue'"
    ```

    Example:

    ```powershell
    Set-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd -UserGroupFilter "Department -eq 'FakeDept'"
    ```

    In this example, for the segment that has the GUID c96e0837-c232-4a8a-841e-ef45787d8fcd, you define the department name as *FakeDept* to remove users from the segment. This example uses the *Department* attribute, but you can use other attributes as appropriate. The example uses *FakeDept* because this doesn't exist and is certain to not contain any users.
4. Use the **Start-InformationBarrierPoliciesApplication** cmdlet to apply your changes.

    ```powershell
    Start-InformationBarrierPoliciesApplication -CleanupGroupSegmentLink
    ```

    Note

    The *CleanupGroupSegmentLink* attribute removes group associations with the segment with no user associations.

    Changes are applied user-by-user for your organization. If your organization is large, it can take 24 hours or more for this process to complete. As a general guideline, it takes about an hour to process 5,000 user accounts.
5. Use the **Remove-OrganizationSegment** cmdlet with the *Identity* parameter and relevant details to remove a segment.

    Syntax:

    ```powershell
    Remove-OrganizationSegment -Identity GUID
    ```

    Example:

    ```powershell
    Remove-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd
    ```

    In this example, you remove the segment that has the GUID c96e0837-c232-4a8a-841e-ef45787d8fcd.

## Remove a policy and segment

1. Use the **Get-InformationBarrierPolicy** cmdlet to view a list of current Information Barriers policies.

    ```powershell
    Get-InformationBarrierPolicy
    ```

    In the list of results, find the policy that you want to remove. Note the policy's GUID and name.
2. Use the **Get-OrganizationSegment** cmdlet to view all existing segments.

    ```powershell
    Get-OrganizationSegment
    ```

    You see a list of segments and details for each, such as segment type, its *UserGroupFilter* parameter value, who created or last modified it, GUID, and so on.

    Tip

    Print or save your list of segments for reference later. For example, if you want to edit a segment, you need to know its name or identify value (this value works with the Identity parameter).
3. Set the policy to inactive status using the **Set-InformationBarrierPolicy** cmdlet.

    Syntax:

    ```powershell
    Set-InformationBarrierPolicy -Identity GUID -State Inactive
    ```

    Example:

    ```powershell
    Set-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c93772471 -State Inactive
    ```

    In this example, this command sets an Information Barriers policy that has GUID 43c37853-ea10-4b90-a23d-ab8c93772471 to an inactive status.
4. Edit the segment that you want to remove to remove the relationship of users to that segment. This action updates the segment definition and removes all users from the segment. Use the *UserGroupFilter* parameter to disassociate users from the segment before removal.

    Syntax:

    ```powershell
    Set-OrganizationSegment -Identity GUID -UserGroupFilter "attribute -eq 'attributevalue'"
    ```

    Example:

    ```powershell
    Set-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd -UserGroupFilter "Department -eq 'FakeDept'"
    ```

    In this example, for the segment that has the GUID c96e0837-c232-4a8a-841e-ef45787d8fcd, the department name is updated to *FakeDept* to remove users from the segment. This example uses the *Department* attribute, but you can use other attributes as appropriate. The example uses *FakeDept* because this doesn't exist and is certain to contain no users.
5. Use the **Start-InformationBarrierPoliciesApplication** cmdlet to apply your changes.

    ```powershell
    Start-InformationBarrierPoliciesApplication -CleanupGroupSegmentLink
    ```

    Note

    The *CleanupGroupSegmentLink* attribute removes group associations with the segment with no user associations.

    Changes are applied user-by-user for your organization. If your organization is large, it can take 24 hours or more for this process to complete. As a general guideline, it takes about an hour to process 5,000 user accounts.
6. Remove the policy using the **Remove-InformationBarrierPolicy** cmdlet.

    Syntax:

    ```powershell
    Remove-InformationBarrierPolicy -Identity GUID
    ```

    Example:

    ```powershell
    Remove-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c93772471
    ```

    In this example, the policy that has GUID *43c37853-ea10-4b90-a23d-ab8c93772471* is removed.

    When prompted, confirm the change.
7. Remove the segment using the **Remove-OrganizationSegment** cmdlet.

    Syntax:

    ```powershell
    Remove-OrganizationSegment -Identity GUID
    ```

    Example:

    ```powershell
    Remove-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd
    ```

    In this example, the segment with GUID c96e0837-c232-4a8a-841e-ef45787d8fcd was removed.

## Stop applying a policy

If you started applying Information Barriers policies and want to stop applying those policies, complete the following steps. It takes about 30 to 35 minutes for the process to start.

1. Use the **Get-InformationBarrierPoliciesApplicationStatus** cmdlet to view the status of the most recent Information Barriers policy application.

    ```powershell
    Get-InformationBarrierPoliciesApplicationStatus
    ```

    Note the application's GUID.
2. Use the **Stop-InformationBarrierPoliciesApplication** cmdlet with an Identity parameter.

    Syntax:

    ```powershell
    Stop-InformationBarrierPoliciesApplication -Identity GUID
    ```

    Example:

    ```powershell
    Stop-InformationBarrierPoliciesApplication -Identity 46237888-12ca-42e3-a541-3fcb7b5231d1
    ```

    In this example, you're stopping the application of Information Barriers policies.

## Enable or disable user discoverability

Important

Support for enabling or disabling search restrictions is only available when your organization isn't in *Legacy* mode. Organizations in *Legacy* mode can't enable or disable search restrictions. Enabling or disabling search restrictions requires additional actions to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment). Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

To enable the people picker search restriction by using PowerShell, complete the following steps:

1. Use the **Set-PolicyConfig** cmdlet to enable the people picker restriction:

```powershell
Set-PolicyConfig -InformationBarrierPeopleSearchRestriction 'Enabled'
```

To disable the people picker search restriction by using PowerShell, complete the following steps:

1. Use the **Set-PolicyConfig** cmdlet to disable the people picker restriction:

```powershell
Set-PolicyConfig -InformationBarrierPeopleSearchRestriction 'Disabled'
```