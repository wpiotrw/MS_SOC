---
layout: Conceptual
title: Manage holds in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-managing-holds
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to place holds on custodians and their data sources to preserve relevant content for your eDiscovery (Premium) case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- highpri
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-mar2020
- admindeeplinkMAC
locale: en-us
document_id: 206603ce-6495-2af5-edd8-4e6c7b7802e9
document_version_independent_id: 206603ce-6495-2af5-edd8-4e6c7b7802e9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-managing-holds.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-managing-holds
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-managing-holds.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0b3b2b80-3266-b94f-1c7e-a1965d272528
---

# Manage holds in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use a Microsoft Purview eDiscovery (Premium) case to create holds to preserve content that might be relevant to your case. Using the eDiscovery (Premium) hold capabilities, you can place holds on custodians and their data sources. Additionally, you can place a noncustodial hold on mailboxes and OneDrive for Business sites. You can also place a hold on the group mailbox, SharePoint site, and OneDrive for Business site for a Microsoft 365 group. Similarly, you can place a hold on the mailbox and site that are associated with Microsoft Teams. When you place content locations on hold, content is held until you release the custodian, remove a specific data location, or delete the hold policy entirely. After you create an eDiscovery hold, it may take up to 24 hours for the hold to be applied.

Important

For long term data retention not related to eDiscovery investigations, it is strongly advised to use retention policies and retention labels. For more information, see [Learn about retention policies and retention labels](retention#when-to-use-retention-policies-and-retention-labels-or-ediscovery-holds).

## View custodian-based holds

In some cases, you may have a set of custodians that you've identified and decided to preserve their data during the case. In eDiscovery (Premium), when these custodians are placed on hold, the user and their selected data sources are automatically added to a custodian hold policy.

Points to remember about hold policies:

- The best policy status is fetched when a location is viewed in a data source
- If the existing applied policy is deleted or released, the system replaces the hold policy status and name with next best applied or active policy.
- Only 1 policy per location is reported. However, there can be more than 1 policy impacting the location within the case. View the [hold report](ediscovery-hold-report) to determine all applicable policies.
- The status for a location is fetched only from the policies applicable to the case. A policy from another case won't be referred to highlight the Hold status of the location.
- The hold status of a location is displayed in the *Hold status* column in the [hold report](ediscovery-hold-report).

To view the custodian hold policy:

1. In the Microsoft Purview portal, select **eDiscovery &gt; Premium** to display the list of cases in your organization.
2. Go to the **Sources** tab to add custodians within your case. To learn how you can add and place custodians on hold within an eDiscovery (Premium) case, see [Add Custodians to a case](ediscovery-add-custodians-to-case). If you have already added custodians and placed them on hold, go to step 3.
3. Go to the **Holds** tab and select **CustodianHold(HoldId)** and ensure the hold is placed successfully.

The hold status shown for a custodian in the data source tab is the most restrictive status for all holds in the underlying locations within the custodian or noncustodial data source. For example, if a custodian is added and includes their mailbox, OneDrive, and several Teams channels, all these data sources are placed on hold. However, if the hold for OneDrive returns an error but hold on all other data sources is successful, the hold status for the custodian is *Not on Hold* because the most restrictive status also applies to all of the underlying holds.

For an individual location within a data source, the hold status of that location is determined using all the hold policies applied on that location and the distribution status. The hold status of any successfully applied hold is applied. For example, a location is part of three hold policies and two policies have a *Failed/error* hold status. If the third policy has a hold successfully applied, then the hold status of the location would be *On Hold* based on the success of the hold on the third policy.

## View noncustodial holds

In some cases, you may have a set of data that isn't tied to a specific custodian, but you need to identify the data as relevant to the case and preserve it. When these noncustodial sources are placed on hold in eDiscovery (Premium), the selected data sources are automatically added to a noncustodial hold policy.

To view a noncustodial hold for an eDiscovery (Premium) case:

1. In the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149), select **eDiscovery &gt; Premium** to display the list of cases in your organization.
2. Select the **Sources** tab to add noncustodial locations within your case. To learn how you can add and place noncustodial data on hold within an eDiscovery (Premium) case, see [Add noncustodial data sources to an eDiscovery (Premium) case](/en-us/purview/ediscovery-non-custodial-data-sources). If you've already added noncustodial location and placed them on hold, go to step 3.
3. Select the **Holds** tab and select **NCDSHold(HoldId)** and ensure hold is placed successfully.

The source policy for the noncustodial location is shown below the hold status. The hold status of that location is determined using all the hold policies applied to the location and the distribution status. The least restrictive hold status of all the statuses is applied.

## Placing custodial and noncustodial locations on hold

Placing custodial and noncustodial locations on hold preserves all the content in the locations. For steps to place query-based hold in eDiscovery (Premium), see [Create eDiscovery holds in an eDiscovery case](/en-us/purview/ediscovery-create-holds).

Note

When you create a query-based hold, all content from selected locations is initially placed on hold. After the timer job in either Exchange or SharePoint runs, any content that doesn't match the specified query is cleared from the hold. After the character count across all queries on a single location exceeds 10,000 characters, the entire location is placed on hold.

Note

If the SMTP address of the user changes after you place the user's mailbox on hold, the mailbox remains on hold. To use the new SMTP address to place hold, create a new hold.

## Place a hold on Microsoft Teams and Microsoft 365 groups

Microsoft Teams is built on Microsoft 365 groups. Therefore, placing them on hold in eDiscovery (Premium) is similar. Keep the following things in mind when placing Microsoft 365 groups and Microsoft Teams on hold:

- To place content located in Microsoft 365 groups and Microsoft Teams on hold, you have to specify the mailbox and SharePoint site that associated with a group or team.
- Run the **Get-UnifiedGroup** cmdlet in Exchange Online to view properties for a Microsoft 365 group or Microsoft Team. This method is a good way to get the URL for the site that's associated with a Microsoft 365 group or a Microsoft Team. For example, the following command displays selected properties for a Microsoft 365 group named Senior Leadership Team:

    ```console
    Get-UnifiedGroup "Senior Leadership Team" | FL DisplayName,Alias,PrimarySmtpAddress,SharePointSiteUrl
    DisplayName            : Senior Leadership Team
    Alias                  : seniorleadershipteam
    PrimarySmtpAddress     : seniorleadershipteam@contoso.onmicrosoft.com
    SharePointSiteUrl      : https://contoso.sharepoint.com/sites/seniorleadershipteam
    ```

    Note

    To run the Get-UnifiedGroup cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- When a user's mailbox is searched, any Microsoft 365 group or Microsoft Team that the user is a member of isn't searched. Similarly, when you place a Microsoft 365 group or Microsoft Team hold, only the group mailbox and group site are placed on hold; the mailboxes and OneDrive sites of group members aren't placed on hold unless you explicitly add them as custodians or place their data sources hold. Therefore, if you need to place a Microsoft 365 group or Microsoft Team on hold for a specific custodian, consider mapping the group site and group mailbox to the custodian (See Managing Custodians in eDiscovery (Premium)). If the Microsoft 365 group or Microsoft Team isn't attributable to a single custodian, consider adding the source to a noncustodial hold.
- To get a list of the members of a Microsoft 365 group or Microsoft Team, you can view the properties on the **Home** &gt; [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) page in the Microsoft 365 admin center. Alternatively, you can run the following command in Exchange Online PowerShell:

    ```powershell
    Get-UnifiedGroupLinks <group or team name> -LinkType Members | FL DisplayName,PrimarySmtpAddress
    ```

    Note

    To run the **Get-UnifiedGroupLinks** cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- Channel conversations that are part of a Microsoft Teams channel are stored in the mailbox that's associated with the Team. Similarly, files that team members share in a channel are stored on the team's SharePoint site. Therefore, you have to place the Microsoft Team mailbox and SharePoint site on hold to retain conversations and files in a channel.
- Alternatively, conversations that are part of the Chat list in Microsoft Teams are stored in the mailbox of the user's who participate in the chat. Files that a user shares in Chat conversations are stored in the OneDrive site of the user who shares the file. Therefore, you have to place the individual user mailboxes and OneDrive sites on hold to retain conversations and files in the Chat list.
- Every Microsoft Team or team channel contains a Wiki for note-taking and collaboration. The Wiki content is automatically saved as a .mht file. This file is stored in the Teams Wiki Data document library on the team's SharePoint site. You can place the content in the Wiki on hold by placing the team's SharePoint site on hold.

    Note

    The capability to retain Wiki content for a Microsoft Team or team channel (when you place the team's SharePoint site on hold) was released on June 22, 2017. If a team site is on hold, the Wiki content will be retained starting on that date. However, if a team site is on hold and the Wiki content was deleted before June 22, 2017, the Wiki content was not retained.

## Hold status

The following table lists the status of holds for items:

| Hold Status | Definition |
| --- | --- |
| Applied | A hold is applied on the location. Content is preserved based on the hold policy conditions. |
| Apply Failed | The hold policy trying to apply Hold on the location has failed. Check the distribution errors in the hold policy. |
| Applying | A hold is being applied on the location. The hold job is in progress. |
| Not on Hold | A hold isn't applied on the location. Content preservation isn't force. |
| Released | A hold is released on the location. Content preservation is disabled. |
| Release failed | The hold policy releasing a hold on the location failed. Check the distribution errors in the hold policy. |
| Releasing | A hold release for the location is in progress. |
| Unknown | The hold status is unknown for the location. Check hold policies, distribution status, and the hold report. This status may appear in cases where the system isn't able to map a hold policy to the location, indicating there isn't a hold present or applied on the location. |

## Manage hold status errors

You may encounter errors while placing a hold on custodial or noncustodial data sources. The following table lists the errors that you may encounter and the recommended resolution.

| **Hold error types** | **Description** | **Resolution** |
| --- | --- | --- |
| Policy deployment interrupted | A system error indicating a problem was encountered while applying the hold. | Select **Retry hold action** on the custodial/non-custodial data source flyout page command bar to retry the hold application. |
| Site inaccessible | Indicates the SharePoint location associated with the requested hold request isn't accessible and may be read only. | Contact your SharePoint site administrator to configure the site as writable and retry the hold with **Retry hold action** on the custodial/non-custodial data source flyout page command bar. |
| Site not found. | Indicates the SharePoint location associated with the requested hold may have been moved, deleted, or the site URL may not exist. | Check the site URL and confirm if the SharePoint site exists. Once confirmed, edit the custodial/non-custodial data source for the site and retry the hold action. |
| Mailbox not found | Indicates the mailbox associated with the requested hold isn't a valid mailbox. | Verify the email address and check that it's a valid Exchange Online mailbox. Once confirmed, edit the custodial/non-custodial data source for the mailbox and then retry the hold action. |
| Distribution group has too many members | Indicates the distribution group associated with the requested hold has more than 1,000 email addresses. Currently, a distribution group having more than 1,000 email addresses can't be expanded to be placed on hold. | Add the individual email addresses as custodial or noncustodial data sources or split the distribution group into groups with less than 1,000 email addresses and retry the hold action. |
| Invalid email address or URL | Indicates the location associated with the requested hold has an invalid email address or site URL. | Specify a valid email address or URL that exists within your organization. |