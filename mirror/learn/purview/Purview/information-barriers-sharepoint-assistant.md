---
layout: Conceptual
title: Information Barriers compliance assistant (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-assistant
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the Information Barriers compliance assistant.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: purview
ms.subservice: purview-information-barriers
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.collection:
- purview-compliance
- M365-collaboration
ai-usage: ai-assisted
locale: en-us
document_id: 074a0502-8f79-c093-140c-4da5c88a0923
document_version_independent_id: 074a0502-8f79-c093-140c-4da5c88a0923
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-sharepoint-assistant.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-sharepoint-assistant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-sharepoint-assistant.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
2PlusCloud:
- Azure
- M365
__autotagging_hash:
- 57DFE987CE44D31CB0A9C046E19B09A31593B1E2B43BFE5CC1CAB17A81DAFC4E
platformId: 2bca5cc4-20cf-83fb-be0f-e4effaea040c
---

# Information Barriers compliance assistant (preview) | Microsoft Learn

This article explains how to enable the Information Barriers (IB) compliance assistant for group-connected SharePoint sites. These sites are sites that don't have an associated team in Microsoft Teams. When you enable the IB compliance assistant, it automatically removes users who don't match the segments specified on this site to ensure group membership honors configured IB policies. This configuration helps ensure your organization remains compliant with standards, policies, and compliance regulations.

## Prerequisites

1. Make sure you [define policies for Information Barriers](information-barriers-policies).
2. [Configure IB segments on a SharePoint Site.](information-barriers-sharepoint)
3. [Install the Azure PowerShell module](/en-us/powershell/azure/install-az-ps?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
4. [Install the Microsoft Graph PowerShell SDK](/en-us/powershell/microsoftgraph/installation?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
5. PowerShell account must have directory administrator access for the tenant.

## Enable the background compliance assistant

These steps create a new application in your organization's enterprise applications. For the compliance assistant to function properly, you must have explicitly added segments to a SharePoint site. Complete the following steps to enable the compliance assistant:

1. Run the following PowerShell cmdlets.

    ```PowerShell
    Connect-MgGraph
    Connect-AzAccount
    $appId="00001111-aaaa-2222-bbbb-3333cccc4444"
    $sp=Get-AzADServicePrincipal -ServicePrincipalName $appId
    if ($sp -eq $null) {New-AzADServicePrincipal -ApplicationId $appId}
    Start-Process "https://login.microsoftonline.com/common/adminconsent?client_id=$appId"
    ```
2. When prompted, sign in by using your Microsoft 365 work or school account.
3. In the **Permissions requested** dialog box, review the information, and select **Accept**. This action configures admin consent for the compliance assistant.

## Verify you created a new application

To verify you created a new application in your organization's enterprise applications, complete the following steps:

1. Sign in to portal.azure.com with directory administrator credentials.
2. Select **Manage Microsoft Entra ID**.
3. Select **Enterprise Applications** in the left navigation.
4. Search for the compliance assistant by using 'M365' as the search term.

    ![Search for IB compliance assistant app](media/info-barriers-compliance-assistant-search.png)
5. Select **M365-Group-Compliance-Assistant** from the list of search results.
6. On the **M365-Group-Compliance-Assistant overview** page, review the application properties.

    ![Overview page for IB compliance assistant app](media/info-barriers-compliance-assistant-overview.png)
7. Select **Permissions** in the left navigation to review the permissions that the application is authorized for.

    ![Permissions page for IB compliance assistant app](media/info-barriers-compliance-assistant-permissions.png)
8. In this example, the **M365-Group-Compliance-Assistant** is authorized to add or remove noncompliant IB users from your Microsoft 365 groups.

You can use [audit log search](audit-search) in the Microsoft Purview portal to search, review, and track audit log events for the M365-Group-Compliance-Assistant application. The audit activities associated with the compliance assistant are:

- **IB assistant removed group member**: The IB noncompliant group member was removed from the group by the compliance assistant.
- **IB assistant removed group owner**: The IB noncompliant owner was removed from the group by the compliance assistant.
- **Identified as IB non-compliant group**: The segments on the group are non-IB compliant with each other.

To search the audit log for Microsoft 365 Groups activities, see [Search the audit log](audit-search).

Note

The compliance assistant runs periodically (every 24 hours). The assistant runs on group-connected SharePoint sites that don't have an associated team in Microsoft Teams. To enable the compliance assistant for SharePoint sites connected to Microsoft Teams, follow the instructions in the [Define IB policies](information-barriers-policies) article.