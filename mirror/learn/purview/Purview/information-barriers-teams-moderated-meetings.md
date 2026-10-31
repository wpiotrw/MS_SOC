---
layout: Conceptual
title: Information Barriers and moderated meetings | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-teams-moderated-meetings
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains how Information Barriers support in Microsoft Teams with moderated meetings.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.date: 2026-04-09T00:00:00.0000000Z
ms.topic: article
ms.service: purview
ms.subservice: purview-information-barriers
audience: Admin
ms.collection:
- purview-compliance
- M365-collaboration
- information-barriers
search.appverid: MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: a82382e9-f7a8-33b8-ca34-c74790fc1eed
document_version_independent_id: a82382e9-f7a8-33b8-ca34-c74790fc1eed
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-teams-moderated-meetings.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-teams-moderated-meetings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-teams-moderated-meetings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8a03c098-1055-ead3-cc72-2552b00a42c9
---

# Information Barriers and moderated meetings | Microsoft Learn

Moderated meetings in [Information Barriers (IB)](information-barriers) enable controlled interactions between users who can't communicate because of IB [policies](information-barriers-policies). This feature ensures that meetings occur with the presence of a designated moderator, such as a compliance admin, who oversees the interaction and ensures compliance with IB policies.

Moderated meetings in IB provide the following benefits:

- **Granular control**: Selectively allow meetings with IB-incompatible users, such as town halls or new hire orientations.
- **Moderator role**: Designated moderators facilitate the meeting, ensuring that all interactions comply with IB policies.
- **Flexible user discovery**: Users can look up and invite participants on either side of the IB during scheduling.
- **Compliance and security**: Adheres to regulatory requirements and provides a secure environment for sensitive discussions.

Important

Your organization must use the IBv2 architecture to use moderated meetings in IB and must be in MultiSegment mode. The IBv2 architecture supports flexible people discovery and the creation of a separate moderator segment. This support is required for necessary compliance and security measures in moderated interactions.

## Set up moderators, segments, and policies

Setting up moderators and associated segments and policies is crucial for conducting moderated meetings where attendees from segments blocked from communicating with each other attend a common meeting.

To configure these settings, you must be assigned one of the following roles in your organization:

- Microsoft 365 global administrator
- Office 365 global administrator
- Compliance administrator
- IB Compliance Management

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Additionally, all users included in Moderated Meeting must meet the following prerequisites:

- All users and the admin must have a Microsoft 365 E5 license
- All users scheduling a Moderated Meeting in Teams must have a Microsoft Teams Premium license.

### Step 1: Define a moderators group in Microsoft Entra

Complete the following steps to define a moderators group in Microsoft Entra:

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/), select **Expand groups**, select **Select all groups**, and then select **Add new group**.
2. For **Group type**, select *Microsoft 365*.
3. Enter a name for the group in the **Group name** field.
4. Enter *moderator* in the **Group email address** field. If you delete the moderators’ group or this group name isn't available, use one of the following address names:

    - moderators1@&lt;domain&gt;.com
    - moderators2@&lt;domain&gt;.com

    Important

    The name of the group email ID must contain the keyword *moderator* and be in stated format.
5. Enter a description for the group in the **Group description** field.
6. Select **No** for **Microsoft Entra roles can be assigned to this group**.
7. Select *Assigned* for **Membership type**.
8. Add owners and moderators to this group.
9. Select **Create**.

You use the *Object ID* of the moderator group in the next step for the creation of a moderators segment in Microsoft Purview portal.

### Step 2: Define the moderators segment

After you configure a Microsoft Entra group with all the needed moderators, use this group to configure a new moderator segment.

Complete the following steps to define a moderators group in the Microsoft Purview portal:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and navigate to **Information Barriers** &gt; **Segments**.
2. Select **New segment**.
3. On the **Provide a segment name** page, enter a name for the segment and select **Next**.
4. On the **Add user group filter** page, select **Add**.
5. Select the *MemberOf* filter.
6. Copy the *Object ID* of the group you created in Step 1 in Microsoft Entra and paste it in the **Member of** condition field with the *Equal* operator. Select **Next**.
7. Review the segment details and select **Submit** to create the segment.

When you create the segment, add or remove owners and moderators by updating the Microsoft Entra group. This segment updates automatically if there are any membership changes in the Microsoft Entra group.

### Step 3: Create a policy for the moderator segment

Create an *Allow* policy for the moderator segment. This policy enables moderators to facilitate meetings for participants from all segments, even if existing IB policies block those participants.

To create a policy for the moderator segment in the Microsoft Purview portal, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and navigate to **Information Barriers** &gt; **Policies** &gt; **Policies**.
2. Select **Create policy**.
3. On the **Provide a policy name** page, enter a name for the policy and select **Next**.
4. On the **Add assigned segment details** page, select **Choose segment**.
5. Select the segment you created in Step 2, and then select **Add** and **Next**.
6. On the **Configure communication and collaboration details** page, select **Allowed**.
7. Select the **Allow moderation** checkbox.
8. Add all the segments in your organization that should participate in a moderated meeting. Add all segments in your organization, including the moderators segment you created in Step 2.
9. Select **Add** and **Next**.
10. On the **Policy status** page, enable **Set your policy to active status** and select **Next**.
11. Review the policy details and select **Submit** to create the policy.

To verify that the policy is applied in your organization, go to **Information Barriers** &gt; **Policies** &gt; **Policy applications** and select **Apply all policies**.

Note

When you select **Apply all policies**, the system evaluates all existing and new policies. You might see some validation errors. Update policies to correct any errors as needed and rerun the evaluation. Applying all policies might take several hours, depending on the size of your organization.

### Step 4: Setting policy configuration

Important

Before you begin, make sure you have the following PowerShell modules installed:

- [Exchange Online Management module](/en-us/powershell/exchange/exchange-online-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) (`ExchangeOnlineManagement`)
- [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) (for `Connect-IPPSSession`)

Complete the following steps to change your IB mode to multi-segment and to disable the IB *InformationBarrierPeopleSearchRestriction* property.

1. Start PowerShell in admin mode and use the following command to change your IB mode to multi-segment:

    ```PowerShell
    Connect-IPPSSession -UserPrincipalName <compliance admin email id>
    Import-Module ExchangeOnlineManagement
    Get-PolicyConfig | fl "Information*"
    Set-PolicyConfig -InformationBarrierMode 'MultiSegment'
    ```

    Note

    If you configure any Block policies in your organization, multi-segment doesn't work. For multi-segment IBv2 to work, configure your organization with Allow policies only. All segments that aren't set to allow are blocked.
2. Use the following cmdlet to disable the *InformationBarrierPeopleSearchRestriction* property:

    ```powershell
     Set-PolicyConfig -InformationBarrierPeopleSearchRestriction 'Disabled'
    ```

To verify that you configured multi-segment support and disabled the *InformationBarrierPeopleSearchRestriction* property, use the following cmdlet:

```powershell
Get-PolicyConfig | fl "Information*"
```

### Step 5: Apply policies

To apply the changes in Step 4, you must apply the policy changes again in your organization. To apply these changes in your organization, go to **Information Barriers** &gt; **Policies** &gt; **Policy applications** and select **Apply all policies**.

Note

When you select **Apply all policies**, the system evaluates all existing and new policies. You might see some validation errors. Update policies to correct any errors as needed and rerun the evaluation. Applying all policies might take several hours, depending on the size of your organization.