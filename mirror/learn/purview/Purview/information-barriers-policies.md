---
layout: Conceptual
title: Get started with Information Barriers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to get started with Information Barriers in Microsoft Purview.
keywords: Microsoft 365, Microsoft Purview, compliance, Information Barriers
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-22T00:00:00.0000000Z
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
ms.custom:
- seo-marvel-apr2020
- sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 83cd494e-f221-abf7-a59b-64f68779b52c
document_version_independent_id: 83cd494e-f221-abf7-a59b-64f68779b52c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 665e61f9-e617-566d-08b3-fd8acf4efcab
---

# Get started with Information Barriers | Microsoft Learn

This article describes how to configure Information Barriers (IB) policies in your organization. Several steps are involved, so review the entire process before you begin configuring IB policies.

Use the [Microsoft Purview portal](purview-portal) or [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) to configure IB in your organization. For organizations configuring IB for the first time, use the **Information Barriers** solution in the Microsoft Purview portal. If you're managing an existing IB configuration and you're comfortable using PowerShell, you can still use that option.

For more information about IB scenarios and features, see [Learn about Information Barriers](information-barriers).

Tip

To help you prepare your plan, this article includes an example scenario.

## Required subscriptions and permissions

Before you get started with IB, confirm your Microsoft 365 subscription and any add-ons. To access and use IB, your organization must have supporting subscriptions or add-ons. For more information, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Information Barriers.

To [manage IB policies](information-barriers-edit-segments-policies), you must be assigned one of the following roles:

- Microsoft 365 global administrator
- Office 365 global administrator
- Compliance administrator
- IB Compliance Management

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Configuration concepts

When you configure IB, you work with several objects and concepts.

- **User account attributes**: Microsoft Entra ID (or Exchange Online) defines these attributes. These attributes can include department, job title, location, team name, and other job profile details. You assign users or groups to segments by using these attributes.
- **Segments**: You define these sets of groups or users in the Microsoft Purview portal or by using PowerShell. They use selected group or user account attributes.

    Your organization can have up to 5,000 segments, and users can be assigned to a maximum of 10 segments. See the list of [IB supported attributes](information-barriers-attributes) for details.

    Important

    Support for 5,000 segments and assigning users to multiple segments is only available when your organization isn't in *Legacy* mode. Assigning users to multiple segments requires extra steps to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

    For organizations in *Legacy* mode, the maximum number of segments supported is 250, and users are restricted to being assigned to only one segment. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).
- **IB policies**: These policies determine communication limits or restrictions. When you define IB policies, you choose from two kinds of policies:

    - *Block* policies prevent one segment from communicating with another segment.
    - *Allow* policies allow one segment to communicate with only certain other segments.

        Note

        **For organizations in *Legacy* mode**: Non-IB groups and users **aren't visible** to users included in IB segments and policies for *allow* policies. If you need non-IB groups and users to be visible to users included in IB segments and policies, you must use *block* policies. **For organizations in *SingleSegment* or *MultiSegment* mode**: Non-IB groups and users are visible to users included in IB segments and policies.  To verify your IB mode, see [Check the IB mode for your organization](information-barriers-multi-segment#check-the-ib-mode-for-your-organization).
- **Policy application**: You apply all IB policies after you define them.
- **Visibility of non-IB users and groups**: Non-IB users and groups are users and groups excluded from IB segments and policies. Depending on when you configure IB policies in your organization and the type of IB policies (block or allow), the behavior for these users and groups differs in Microsoft Teams, SharePoint, OneDrive, and in your global address list.

    - **For organizations in *Legacy* mode**: For users defined in *allow* policies, non-IB groups and users aren't visible to users included in IB segments and policies. For users defined in *block* policies, non-IB groups and users are visible to users included in IB segments and policies.
    - **For organizations in *SingleSegment* or *MultiSegment* mode**: Non-IB groups and users are visible to users included in IB segments and policies.
- **Group support**: IB currently supports only Microsoft 365 Groups. Distribution Lists and Security Groups are treated as non-IB groups.
- **Hidden or disabled user and guest accounts**: For hidden or disabled user and guest accounts in your organization, the *HiddenFromAddressListEnabled* parameter is automatically set to *True* when you hide or disable user accounts, or when you create a guest. When the organization mode is *Legacy* for IB-enabled organizations, IB policies aren't enforced for these accounts in Microsoft Teams. Administrators can change this behavior by manually setting the *HiddenFromAddressListEnabled* parameter to *False*, which allows IB policy enforcement for these users. When the organization is in *SingleSegment* or *MultiSegment* mode, IB policies are enforced for hidden users.

## Configuration overview

- **Step 1: Make sure prerequisites are met**: Verify required subscriptions, permissions, directory data for segmenting users, audit logging, IB mode, and Exchange address book policy configuration.
- **Step 2: Segment users in your organization**: Determine what policies you need, identify attributes to use, and define segments in terms of policy filters.
- **Step 3: Create Information Barriers policies**: Create your policies (don't apply them yet) and select from two kinds (block or allow).
- **Step 4: Apply Information Barriers policies**: Set policies to active status, run the policy application, and view policy status.
- **Step 5: Configure Information Barriers on SharePoint and OneDrive (optional)**: Configure IB for SharePoint and OneDrive.
- **Step 6: Information Barriers modes (optional)**: Update IB modes if applicable.
- **Step 7: Configure user discoverability (optional)**: Enable or restrict user discoverability in the people picker if applicable.

## Step 1: Make sure prerequisites are met

In addition to the required subscriptions and permissions, make sure that you meet the following requirements before configuring IB:

- **Directory data**: Make sure that your organization's structure is reflected in directory data. To take this action, make sure that user account attributes (such as group membership, department name, and other attributes) are populated correctly in Microsoft Entra ID or Exchange Online. For more information, see the following resources:

    - [Attributes for Information Barriers policies](information-barriers-attributes)
    - [Add or update a user's profile information using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)
    - [Configure user account properties with Office 365 PowerShell](/en-us/microsoft-365/enterprise/configure-user-account-properties-with-microsoft-365-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)
- **Scoped directory search**: Before you define your organization's first IB policy, you must [enable scoped directory search in Microsoft Teams](/en-us/MicrosoftTeams/teams-scoped-directory-search). Wait at least 24 hours after enabling scoped directory search before you set up or define IB policies.
- **Verify audit logging is enabled**: To look up the status of an IB policy application, audit logging must be turned on. Auditing is enabled for Microsoft 365 organizations by default. Some organizations might disable auditing for specific reasons. If auditing is disabled for your organization, it might be because another administrator turned it off. Confirm that it's OK to turn auditing back on when completing this step. For more information, see [Turn the audit log search on or off](audit-log-enable-disable).
- **Check the IB mode for your organization**: Support for multiple segments, people discoverability options, Exchange ABPs, and other features is determined by the IB mode for your organization. To verify the IB mode for your organization, see [Check the IB mode for your organization](information-barriers-multi-segment#check-the-ib-mode-for-your-organization).
- **Remove existing Exchange Online address book policies (optional)**:

    - **For organizations in *Legacy* mode**: Before you define and apply IB policies, remove all existing Exchange Online address book policies in your organization. IB policies are based on address book policies and existing ABPs aren't compatible with the ABPs created by IB. To remove your existing address book policies, see [Remove an address book policy in Exchange Online](/en-us/exchange/address-books/address-book-policies/remove-an-address-book-policy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). For more information about IB policies and Exchange Online, see [Information Barriers and Exchange Online](information-barriers#information-barriers-and-exchange-online).
    - **For organizations in *SingleSegment* or *MultiSegment* mode**: Information Barriers no longer uses Exchange Online Address Book Policies (ABPs). Enabling Information Barriers doesn't affect existing ABPs.
- **Manage using PowerShell (optional)**: You can define and manage IB segments and policies in the Microsoft Purview portal, or you can use Security & Compliance PowerShell if preferred or needed. Although several examples are provided in this article, you need to be familiar with PowerShell cmdlets and parameters if you choose to use PowerShell to configure and manage IB segments and policies. You also need the following modules depending on your configuration:

    | Module | Used for | Installation |
    | --- | --- | --- |
    | Security & Compliance PowerShell | Segments, policies, and organization settings | [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) |
    | Microsoft Graph PowerShell SDK | User and group management | [Install the Microsoft Graph PowerShell SDK](/en-us/powershell/microsoftgraph/installation?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) |
    | SharePoint Online Management Shell | SharePoint and OneDrive IB configuration | [Get started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) |

When you meet all the prerequisites, proceed to the next step.

## Step 2: Segment users in your organization

In this step, you determine what IB policies you need, make a list of segments to define, and define your segments. Defining segments doesn't affect users; it just sets the stage for defining and applying IB policies.

### Determine what policies you need

Consider the needs of your organization and determine the groups within your organization that need IB policies. Ask yourself the following questions:

- Are there internal, legal, or industry regulations that require the restriction of communication and collaboration between groups and users in your organization?
- Are there any groups or users you should prevent from communicating with another group of users?
- Are there any groups or users you should allow to communicate only with one or two other groups of users?

Think about the policies you need as belonging to one of two types:

- *Block* policies prevent one group from communicating with another group.
- *Allow* policies allow a group to communicate with only specific groups.

When you have your initial list of needed groups and policies, proceed to identify the segments you need for the IB policies.

### Identify segments

In addition to your initial list of policies, make a list of segments for your organization. Users included in IB policies should belong to at least one segment. Users can be assigned to multiple segments if needed. You can have up to 5,000 segments in your organization, and each segment can have only one IB policy applied.

Important

For organizations in *Legacy* or *SingleSegment* modes, a user can belong to only one segment. To verify your IB mode, see [Check the IB mode for your organization](information-barriers-multi-segment#check-the-ib-mode-for-your-organization).

Determine which attributes in your organization's directory data you'll use to define segments. You can use *Department*, *MemberOf*, or any of the supported IB attributes. Make sure that you have values in the attribute you select for users. For more information, see the [supported attributes for IB](information-barriers-attributes).

Important

**Before you proceed to the next section, make sure your directory data has values for attributes that you can use to define segments**. If your directory data doesn't have values for the attributes you want to use, update the user accounts to include that information before you proceed with configuring IB. For help, see the following resources: - [Configure user account properties with Office 365 PowerShell](/en-us/microsoft-365/enterprise/configure-user-account-properties-with-microsoft-365-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)- [Add or update a user's profile information using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)

### Enable multiple segment support for users (optional)

Support for assigning users to multiple segments is available only when your organization isn't in *Legacy* mode. To support assigning users to multiple segments, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

Users can be assigned to only one segment for organizations in *Legacy* mode. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

### Define segments using the portals

Complete the following steps to define segments:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your organization.
2. Select the **Information Barriers** solution card. If you don't see the **Information Barriers** solution card, select **View all solutions** and then select **Information Barriers** from the **Risk & Compliance** section.
3. Select **Segments**.
4. On the **Segments** page, select **New segment** to create and configure a new segment.
5. On the **Name** page, enter a name for the segment. You can't rename a segment after you create it.
6. Select **Next**.
7. On the **User group filter** page, select **Add** to configure the group and user attributes for the segment. Choose an attribute for the segment from the list of available attributes.
8. For the selected attribute, select either *Equal* or *Not equal* and then enter the value for the attribute. For example, if you select *Department* as the attribute and *Equals*, you could enter *Marketing* as the defined *Department* for this segment condition. Select **Add condition** to add extra conditions for an attribute. To delete an attribute or attribute condition, select the delete icon for the attribute or condition.
9. Add extra attributes as needed on the **User group filter** page, then select **Next**.
10. On the **Review your settings** page, review the settings you chose for the segment and any suggestions or warnings for your selections. Select **Edit** to change any of the segment attributes and conditions or select **Submit** to create the segment.

### Define segments using PowerShell

To define segments by using PowerShell, complete the following steps:

1. Use the **New-OrganizationSegment** cmdlet with the **UserGroupFilter** parameter that corresponds to the [attribute](information-barriers-attributes) you want to use.

    **Syntax**:

    ```powershell
    New-OrganizationSegment -Name "segmentname" -UserGroupFilter "attribute -eq 'attributevalue'"
    ```

    **Example**:

    ```powershell
    New-OrganizationSegment -Name "HR" -UserGroupFilter "Department -eq 'HR'"
    ```

    In this example, you define a segment named *HR* by using *HR*, a value in the *Department* attribute. The **-eq** operator refers to "equals." (Alternately, you can use **-ne** to mean "not equals". See PowerShell reference: "Equals" and "not equals" in segment definitions.)

    After you run each cmdlet, you see a list of details about the new segment. Details include the segment's type, who created or last modified it, and so on.
2. Repeat this process for each segment you want to define.

After you define your segments, go to Step 3: Create IB policies.

## Step 3: Create IB policies

When you create your IB policies, decide whether to prevent communications between certain segments or limit communications to certain segments. Use the minimum number of IB policies to ensure your organization complies with internal, legal, and industry requirements. Use the Microsoft Purview portal or PowerShell to create and apply IB policies.

Tip

For user experience consistency, use *Block* policies for most scenarios.

With your list of user segments and the IB policies you want to define, select a scenario and follow the steps.

- Scenario 1: Block communications between segments
- Scenario 2: Allow a segment to communicate only with one other segment

Important

**Don't assign more than one policy to a segment**. For example, if you define one policy for a segment called *Sales*, don't define an additional policy for the *Sales* segment. As you define IB policies, set those policies to inactive status until you're ready to apply them. Defining (or editing) policies doesn't affect users until you set those policies to active status and then apply them.

### Scenario 1: Block communications between segments

When you want to block segments from communicating with each other, define two policies: one for each direction. Each policy blocks communication in one direction only.

For example, suppose you want to block communications between Segment A and Segment B. Define two policies:

- One policy preventing Segment A from communicating with Segment B
- A second policy to prevent Segment B from communicating with Segment A

#### Create policies using the portals for Scenario 1

Complete the following steps to create policies:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your organization.
2. Select the **Information Barriers** solution card. If you don't see the **Information Barriers** solution card, select **View all solutions** and then select **Information Barriers** from the **Risk & Compliance** section.
3. Select **Policies**.
4. On **Policies**, select **Create policy** to create and configure a new IB policy.
5. On **Name**, enter a name for the policy, and then select **Next**.
6. On **Assigned segment**, select **Choose segment**. Use the search box to search for a segment by name or scroll to select the segment from the displayed list. Select **Add** to add the selected segment to the policy. You can only select one segment.
7. Select **Next**.
8. On **Communication and collaboration**, select the policy type in the **Communication and collaboration** field. The policy options are either *Allowed* or *Blocked*. In this example scenario, select *Blocked* for the first policy.

    Important

    You can't change the Allowed and Blocked status for segments after creating a policy. To change the status, delete the policy and create a new one.
9. Select **Choose segment** to define the actions for the target segment. You can assign more than one segment in this step. For example, if you want to block users in a segment called *Sales* from communicating with users in a segment called *Research*, define the *Sales* segment in Step 5 and assign *Research* in the **Choose segment** option in this step.
10. Select **Next**.
11. On **Policy status**, toggle the active policy status to **On**. Select **Next** to continue.
12. On **Review your settings**, review the settings you choose for the policy and any suggestions or warnings for your selections. Select **Edit** to change any of the policy segments and status or select **Submit** to create the policy.

In this example, repeat the previous steps to create a second *Block* policy to restrict users in a segment called *Research* from communicating with users in a segment called *Sales*. Define the *Research* segment in Step 5 and assign *Sales* (or multiple segments) in the **Choose segment** option.

#### Create policies using PowerShell for Scenario 1

To define policies by using PowerShell, complete the following steps:

1. To define your first blocking policy, use the **New-InformationBarrierPolicy** cmdlet with the **SegmentsBlocked** parameter.

    **Syntax**:

    ```powershell
    New-InformationBarrierPolicy -Name "policyname" -AssignedSegment "segmentAname" -SegmentsBlocked "segmentBname"
    ```

    **Example**:

    ```powershell
    New-InformationBarrierPolicy -Name "Sales-Research" -AssignedSegment "Sales" -SegmentsBlocked "Research" -State Inactive
    ```

    In this example, you define a policy called *Sales-Research* for a segment called *Sales*. When active and applied, this policy prevents users in *Sales* from communicating with users in a segment called *Research*.
2. To define your second blocking segment, use the **New-InformationBarrierPolicy** cmdlet with the **SegmentsBlocked** parameter again, this time with the segments reversed.

    **Example**:

    ```powershell
    New-InformationBarrierPolicy -Name "Research-Sales" -AssignedSegment "Research" -SegmentsBlocked "Sales" -State Inactive
    ```

    In this example, you define a policy called *Research-Sales* to prevent *Research* from communicating with *Sales*.
3. Proceed to one of the following actions:

    - (If needed) Define a policy to allow a segment to communicate only with one other segment
    - (After all your policies are defined) Apply IB policies

### Scenario 2: Allow a segment to communicate only with one other segment

When you want to allow a segment to communicate with only one other segment, define two policies: one for each direction. Each policy allows communication in one direction only.

In this example, define two policies:

- One policy that allows Segment A to communicate with Segment B
- A second policy that allows Segment B to communicate with Segment A

#### Create policies using the portals for Scenario 2

Complete the following steps to create policies:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your organization.
2. Select the **Information Barriers** solution card. If you don't see the **Information Barriers** solution card, select **View all solutions** and then select **Information Barriers** from the **Risk & Compliance** section.
3. On **Policies**, select **Create policy** to create and configure a new IB policy.
4. On **Name**, enter a name for the policy, and then select **Next**.
5. On **Assigned segment**, select **Choose segment**. Use the search box to search for a segment by name or scroll to select the segment from the displayed list. Select **Add** to add the selected segment to the policy. You can only select one segment.
6. Select **Next**.
7. On the **Communication and collaboration** page, select the policy type in the **Communication and collaboration** field. The policy options are either *Allowed* or *Blocked*. In this example scenario, select *Allowed* for the policy.

    Important

    You can't change the Allowed and Blocked status for segments after creating a policy. To change the status, delete the policy and create a new one.
8. Select **Choose segment** to define the actions for the target segment. You can assign more than one segment in this step. For example, if you want to allow users in a segment called *Manufacturing* to communicate with users in a segment called *HR*, define the *Manufacturing* segment in Step 5 and assign *HR* in the **Choose segment** option in this step.
9. Select **Next**.
10. On **Policy status**, toggle the active policy status to **On**. Select **Next** to continue.
11. On **Review your settings**, review the settings you choose for the policy and any suggestions or warnings for your selections. Select **Edit** to change any of the policy segments and status or select **Submit** to create the policy.
12. Repeat the previous steps to create a second *Allow policy* to allow users in a segment called *Research* to communicate with users in a segment called *Sales*. Define the *Research* segment in **Step 5** and assign *Sales* (or multiple segments) in the **Choose segment** option.

#### Create a policy using PowerShell for Scenario 2

To define policies by using PowerShell, complete the following steps:

1. To allow one segment to communicate with the other segment, use the **New-InformationBarrierPolicy** cmdlet with the **SegmentsAllowed** parameter.

    **Syntax**:

    ```powershell
    New-InformationBarrierPolicy -Name "policyname" -AssignedSegment "segmentAname" -SegmentsAllowed "segmentBname","segmentAname"
    ```

    **Example**:

    ```powershell
    New-InformationBarrierPolicy -Name "Manufacturing-HR" -AssignedSegment "Manufacturing" -SegmentsAllowed "HR","Manufacturing" -State Inactive
    ```

    In this example, you define a policy called *Manufacturing-HR* for a segment called *Manufacturing*. When active and applied, this policy allows users in *Manufacturing* to communicate only with users in a segment called *HR*. In this case, *Manufacturing* can't communicate with users who aren't part of *HR*.

    **If needed, you can specify multiple segments by using this cmdlet, as shown in the following example.**

    **Syntax**:

    ```powershell
    New-InformationBarrierPolicy -Name "policyname" -AssignedSegment "segmentAname" -SegmentsAllowed "segmentBname","segmentCname","segmentDname"
    ```

    **Example**:

    ```powershell
    New-InformationBarrierPolicy -Name "Research-HRManufacturing" -AssignedSegment "Research" -SegmentsAllowed "HR","Manufacturing","Research" -State Inactive
    ```

    In this example, you define a policy that allows the *Research* segment to communicate with only *HR* and *Manufacturing*.

    Repeat this step for each policy you want to define to allow specific segments to communicate with only certain other specific segments.
2. To define your second allowing segment, use the **New-InformationBarrierPolicy** cmdlet with the **SegmentsAllowed** parameter again, this time with the segments reversed.

    **Example**:

    ```powershell
    New-InformationBarrierPolicy -Name "Research-Sales" -AssignedSegment "Research" -SegmentsAllowed "Sales" -State Inactive
    ```

    In this example, you define a policy called *Research-Sales* to allow *Research* to communicate with *Sales*.
3. Proceed to one of the following actions:

    - (If needed) Define a policy to block communications between segments
    - (After all your policies are defined) Apply IB policies

## Step 4: Apply IB policies

IB policies take effect when you set them to active status and apply the policies.

### Apply policies using the portals

Complete the following steps to apply policies:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your organization.
2. Select the **Information Barriers** solution card. If you don't see the **Information Barriers** solution card, select **View all solutions** and then select **Information Barriers** from the **Risk & Compliance** section.
3. Select **Policy application**.
4. On the **Policies application** page, select **Apply all policies** to apply all IB policies in your organization.

    Note

    Allow 30 minutes for the system to start applying the policies. The system applies policies user by user and processes about 5,000 user accounts per hour.

### Apply policies using PowerShell

To apply policies by using PowerShell, complete the following steps:

1. Use the **Get-InformationBarrierPolicy** cmdlet to see a list of defined policies. Note the status and identity (GUID) of each policy.

    ```powershell
    Get-InformationBarrierPolicy
    ```
2. Use the **Set-InformationBarrierPolicy** cmdlet with the **Identity** parameter and the **State** parameter set to **Active** to set a policy to active status.

    **Syntax**:

    ```powershell
    Set-InformationBarrierPolicy -Identity GUID -State Active
    ```

    **Example**:

    ```powershell
    Set-InformationBarrierPolicy -Identity 43c37853-ea10-4b90-a23d-ab8c93772471 -State Active
    ```

    In this example, you set an IB policy that has the GUID *43c37853-ea10-4b90-a23d-ab8c93772471* to active status.

    Repeat this step for each policy.
3. When you finish setting your IB policies to active status, use the **Start-InformationBarrierPoliciesApplication** cmdlet in Security & Compliance PowerShell.

    ```powershell
    Start-InformationBarrierPoliciesApplication
    ```

    After you run `Start-InformationBarrierPoliciesApplication`, allow 30 minutes for the system to start applying the policies. The system applies policies user by user and processes about 5,000 user accounts per hour.

### View status of user accounts, segments, policies, or policy application

By using PowerShell, you can view the status of user accounts, segments, policies, and policy application.

#### View user account IB relationships

Use the [Get-ExoInformationBarrierRelationship](/en-us/powershell/module/exchange/get-exoinformationbarrierrelationship?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) cmdlet with RecipientId parameters. You can use any value that uniquely identifies each user, such as name, alias, distinguished name, canonical domain name, email address, or GUID.

```powershell
Get-ExoInformationBarrierRelationship -RecipientId1 meganb -RecipientId2 alexw
```

In this example, you refer to two user accounts: *meganb* for *Megan*, and *alexw* for *Alex*. This cmdlet returns information about users, such as attribute values and any IB policies that are applied.

#### View all segments

```powershell
Get-OrganizationSegment
```

This cmdlet displays a list of all segments defined for your organization.

#### View all IB policies

```powershell
Get-InformationBarrierPolicy
```

This cmdlet displays a list of IB policies that you defined, and their status.

#### View the most recent IB policy application

```powershell
Get-InformationBarrierPoliciesApplicationStatus
```

This cmdlet displays information about whether policy application completed, failed, or is in progress.

#### View all IB policy applications

```powershell
Get-InformationBarrierPoliciesApplicationStatus -All
```

This cmdlet displays information about whether policy application completed, failed, or is in progress.

### What if I need to remove or change policies?

You can find resources to help you manage your IB policies.

- To edit, stop, or remove IB policies, see [Manage Information Barriers policies](information-barriers-edit-segments-policies).
- If something goes wrong with IB, see [Resolve Information Barriers issues](/en-us/office365/troubleshoot/information-barriers/information-barriers-troubleshooting?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Step 5: Configure Information Barriers on SharePoint and OneDrive

If you configure IB for SharePoint and OneDrive, you need to enable IB on these services. You also need to enable IB on these services if you configure IB for Microsoft Teams. When you create a team in Microsoft Teams, you automatically create and associate a SharePoint site with Microsoft Teams for the files experience. By default, IB policies don't apply to this new SharePoint site and files.

To enable IB in SharePoint and OneDrive, follow the guidance and steps in the [Use Information Barriers with SharePoint](information-barriers-sharepoint) article.

## Step 6: Information Barriers modes (optional)

Modes help strengthen access, sharing, and membership of a Microsoft 365 resource based on the resource's IB mode. Microsoft 365 Groups, Microsoft Teams, OneDrive, and SharePoint sites support modes. Your new or existing IB configuration automatically enables modes.

The following IB modes support Microsoft 365 resources:

| Mode | Description | Example |
| --- | --- | --- |
| **Open** | The Microsoft 365 resource has no IB policies or segments associated with it. Anyone can be invited to be a member of the resource. | A team site created for a picnic event for your organization. |
| **Owner Moderated** | The resource owner's IB policy determines the IB policy of the Microsoft 365 resource. The resource owners can invite any user to the resource based on their IB policies. This mode is useful when your company wants to allow collaboration among incompatible segment users that the owner moderates. Only the resource owner can add new members per their IB policy. | The VP of HR wants to collaborate with the VPs of Sales and Research. A new SharePoint site that is set with IB mode *Owner Moderated* to add both Sales and Research segment users to the same site. It's the responsibility of the owner to ensure appropriate members are added to the resource. |
| **Implicit** | The resource members' IB policy determines the IB policy or segments of the Microsoft 365 resource. The owner can add members as long as they're compatible with the existing members of the resource. This mode is the default IB mode for Microsoft Teams. | The Sales segment user creates a Microsoft Teams team to collaborate with other compatible segments in the organization. |
| **Explicit** | The segments associated with the resource determine the IB policy of the Microsoft 365 resource. The resource owner or SharePoint administrator can manage the segments on the resource. | A site created only for Sales segment members to collaborate by associating the Sales segment with the site. |
| **Mixed** | Only applicable to OneDrive. The segments associated with the OneDrive determine the IB policy of the OneDrive. The resource owner or OneDrive administrator can manage the segments on the resource. | A OneDrive created for Sales segment members to collaborate is allowed to be shared with unsegmented users. |

### Implicit mode updates

Depending on when you enabled IB in your organization, your organization is in either *Legacy*, *SingleSegment*, or *MultiSegment* organization mode. To verify your mode, see [Check the IB mode for your organization](information-barriers-multi-segment#check-the-ib-mode-for-your-organization).

If your organization is in *SingleSegment* or *MultiSegment* mode and the Information Barriers mode of the Teams group is *Implicit*, the Teams-connected groups and sites don't have any segments associated with them.

For more information about IB modes and how to configure them across services, see the following articles:

- [Information Barriers modes and Microsoft Teams](/en-us/microsoftteams/information-barriers-in-teams?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)
- [Information Barriers modes and OneDrive](information-barriers-onedrive)
- [Information Barriers modes and SharePoint](information-barriers-sharepoint)

## Step 7: Configure user discoverability for Information Barriers (optional)

By using Information Barriers policies, administrators can enable or disable search restrictions in the people picker. By default, the people picker restriction is enabled for IB policies. For example, IB policies that block two specific users from communication can also restrict the users from seeing each other when using the people picker.

Important

Support for enabling or disabling search restrictions is only available when your organization isn't in *Legacy* mode. Organizations in *Legacy* mode can't enable or disable search restrictions. Enabling or disabling search restrictions requires additional actions to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment). Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

To disable the people picker search restriction by using PowerShell, complete the following steps:

1. Use the **Set-PolicyConfig** cmdlet to disable the people picker restriction:

```powershell
Set-PolicyConfig -InformationBarrierPeopleSearchRestriction 'Disabled'
```

## Example scenario: Contoso's departments, segments, and policies

To see how an organization might approach defining segments and block-based policies, consider the following example scenario.

Tip

For an example of allow-based policies with multi-segment support, see the North School District example in [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

### Contoso's departments and plan

Contoso has five departments: *HR*, *Sales*, *Marketing*, *Research*, and *Manufacturing*. To comply with industry regulations, users in some departments can't communicate with other departments, as shown in the following table:

| Segment | Can communicate with | Can't communicate with |
| --- | --- | --- |
| HR | Everyone | (no restrictions) |
| Sales | HR, Marketing, Manufacturing | Research |
| Marketing | Everyone | (no restrictions) |
| Research | HR, Marketing, Manufacturing | Sales |
| Manufacturing | HR, Marketing | Anyone other than HR or Marketing |

For this structure, Contoso's plan includes three IB policies:

1. An IB policy that prevents Sales from communicating with Research.
2. An IB policy that prevents Research from communicating with Sales.
3. An IB policy that allows Manufacturing to communicate with HR and Marketing only.

For this scenario, you don't need to define IB policies for *HR* or *Marketing*.

### Contoso's defined segments

Contoso uses the Department attribute in Microsoft Entra ID to define segments, as follows:

**HR segment**:

```powershell
New-OrganizationSegment -Name "HR" -UserGroupFilter "Department -eq 'HR'"
```

**Sales segment**:

```powershell
New-OrganizationSegment -Name "Sales" -UserGroupFilter "Department -eq 'Sales'"
```

**Marketing segment**:

```powershell
New-OrganizationSegment -Name "Marketing" -UserGroupFilter "Department -eq 'Marketing'"
```

**Research segment**:

```powershell
New-OrganizationSegment -Name "Research" -UserGroupFilter "Department -eq 'Research'"
```

**Manufacturing segment**:

```powershell
New-OrganizationSegment -Name "Manufacturing" -UserGroupFilter "Department -eq 'Manufacturing'"
```

After defining the segments, Contoso defines the IB policies.

### Contoso's IB policies

Contoso defines three IB policies:

**Policy 1**: Prevent Sales from communicating with Research.

```powershell
New-InformationBarrierPolicy -Name "Sales-Research" -AssignedSegment "Sales" -SegmentsBlocked "Research" -State Inactive
```

In this example, the IB policy is called *Sales-Research*. When you activate and apply this policy, it prevents users in the Sales segment from communicating with users in the Research segment. This policy is a one-way policy; it doesn't prevent Research from communicating with Sales. For that, Policy 2 is needed.

**Policy 2**: Prevent Research from communicating with Sales.

```powershell
New-InformationBarrierPolicy -Name "Research-Sales" -AssignedSegment "Research" -SegmentsBlocked "Sales" -State Inactive
```

In this example, the IB policy is called *Research-Sales*. When you activate and apply this policy, it prevents users in the Research segment from communicating with users in the Sales segment.

**Policy 3**: Allow Manufacturing to communicate with HR and Marketing only.

```powershell
New-InformationBarrierPolicy -Name "Manufacturing-HRMarketing" -AssignedSegment "Manufacturing" -SegmentsAllowed "HR","Marketing","Manufacturing" -State Inactive
```

In this case, the IB policy is called *Manufacturing-HRMarketing*. When you activate and apply this policy, Manufacturing can communicate only with HR and Marketing. HR and Marketing aren't restricted from communicating with other segments.

After defining the segments and policies, Contoso applies the policies by running the **Start-InformationBarrierPoliciesApplication** cmdlet.

When the cmdlet finishes, Contoso complies with industry requirements.

## PowerShell reference: "Equals" and "not equals" in segment definitions

When you define segments by using PowerShell, use "equals" (`-eq`) and "not equals" (`-ne`) parameters. Also, use logical *AND* and *OR* operators for complex group filters.

**Basic "equals" example**:

```powershell
New-OrganizationSegment -Name "HR" -UserGroupFilter "Department -eq 'HR'"
```

Defines a segment named *HR* by using *HR*, a value in the *Department* attribute. The **-eq** portion of the cmdlet refers to "equals".

**Basic "not equals" example**:

```powershell
New-OrganizationSegment -Name "NotSales" -UserGroupFilter "Department -ne 'Sales'"
```

Defines a segment called *NotSales* that includes everyone who isn't in *Sales*. The **-ne** portion of the cmdlet refers to "not equals".

**Using "AND" operators**:

```powershell
New-OrganizationSegment -Name "LocalFTE" -UserGroupFilter "Location -eq 'Local'" -and "Position -ne 'Temporary'"
```

Defines a segment called *LocalFTE* that includes users who are located locally and whose positions aren't listed as *Temporary*.

**Using "AND" with MemberOf**:

```powershell
New-OrganizationSegment -Name "Segment1" -UserGroupFilter "MemberOf -eq 'group1@contoso.com'' -and MemberOf -ne 'group3@contoso.com'"
```

Defines a segment called *Segment1* that includes users who are members of group1@contoso.com and not members of group3@contoso.com.

**Using "OR" with MemberOf**:

```powershell
New-OrganizationSegment -Name "Segment2" -UserGroupFilter "MemberOf -eq 'group2@contoso.com' -or MemberOf -ne 'group3@contoso.com'"
```

Defines a segment called *Segment2* that includes users who are members of group2@contoso.com and not members of group3@contoso.com.

**Combining "OR" and "AND" operators**:

```powershell
New-OrganizationSegment -Name "Segment1and2" -UserGroupFilter "(MemberOf -eq 'group1@contoso.com' -or MemberOf -eq 'group2@contoso.com') -and MemberOf -ne 'group3@contoso.com'"
```

Defines a segment called *Segment1and2* that includes users in group1@contoso.com and group2@contoso.com and not members of group3@contoso.com.

Tip

If possible, use segment definitions that include `-eq` or `-ne`. Avoid defining complex segment definitions.

## PowerShell cmdlet quick reference

The following table lists the PowerShell cmdlets you can use to manage Information Barriers segments and policies.

| Cmdlet | Module | Purpose |
| --- | --- | --- |
| [New-OrganizationSegment](/en-us/powershell/module/exchange/new-organizationsegment?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Create a new segment |
| [Get-OrganizationSegment](/en-us/powershell/module/exchange/get-organizationsegment?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | View all defined segments |
| [Set-OrganizationSegment](/en-us/powershell/module/exchange/set-organizationsegment?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Edit a segment definition |
| [Remove-OrganizationSegment](/en-us/powershell/module/exchange/remove-organizationsegment?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Remove a segment |
| [New-InformationBarrierPolicy](/en-us/powershell/module/exchange/new-informationbarrierpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Create a new IB policy |
| [Get-InformationBarrierPolicy](/en-us/powershell/module/exchange/get-informationbarrierpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | View IB policies and their status |
| [Set-InformationBarrierPolicy](/en-us/powershell/module/exchange/set-informationbarrierpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Edit or activate a policy |
| [Remove-InformationBarrierPolicy](/en-us/powershell/module/exchange/remove-informationbarrierpolicy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Remove a policy |
| [Start-InformationBarrierPoliciesApplication](/en-us/powershell/module/exchange/start-informationbarrierpoliciesapplication?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Apply all active IB policies |
| [Stop-InformationBarrierPoliciesApplication](/en-us/powershell/module/exchange/stop-informationbarrierpoliciesapplication?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Stop applying IB policies |
| [Get-InformationBarrierPoliciesApplicationStatus](/en-us/powershell/module/exchange/get-informationbarrierpoliciesapplicationstatus?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | View policy application status |
| [Get-ExoInformationBarrierRelationship](/en-us/powershell/module/exchange/get-exoinformationbarrierrelationship?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | View IB relationship between users |
| [Get-PolicyConfig](/en-us/powershell/module/exchange/get-policyconfig?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | View IB organization mode |
| [Set-PolicyConfig](/en-us/powershell/module/exchange/set-policyconfig?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) | Security & Compliance PowerShell | Configure IB organization settings |

For managing Information Barriers in SharePoint and OneDrive, see the [SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) cmdlets documented in [Use Information Barriers with SharePoint](information-barriers-sharepoint) and [Use Information Barriers with OneDrive](information-barriers-onedrive).