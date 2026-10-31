---
layout: Conceptual
title: Create and manage inactive mailboxes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/create-and-manage-inactive-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-08-05T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.assetid: 296a02bd-ebde-4022-900e-547acf38ddd7
ms.custom:
- seo-marvel-apr2020
- admindeeplinkMAC
description: Create and manage inactive mailboxes that retain the contents of deleted mailboxes in Microsoft 365.
locale: en-us
document_id: d34127f0-a48d-9995-785a-64e8764e3ee5
document_version_independent_id: d34127f0-a48d-9995-785a-64e8764e3ee5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/create-and-manage-inactive-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: create-and-manage-inactive-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/create-and-manage-inactive-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: bc90ac7d-870c-da6c-c4d2-e1996aeb9b1a
---

# Create and manage inactive mailboxes | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Inactive mailboxes let you retain former employees' email after they leave your organization and can be accessed by authorized people who have been granted [eDiscovery permissions](ediscovery-assign-permissions) for compliance or legal reasons. For example, administrators, compliance officers, and records managers who can then use Content Search to search and export the contents of an inactive mailbox. Inactive mailboxes can't receive email and aren't displayed in your organization's shared address book or other lists.

For more information about inactive mailboxes, see [Learn about inactive mailboxes](inactive-mailboxes-in-office-365).

## Create an inactive mailbox

Making a mailbox inactive requires a hold on the mailbox, and then deleting the mailbox or corresponding user account.

To make a mailbox inactive, it must be [licensed correctly](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#email-archiving) so that a hold can be applied to the mailbox before it's deleted. After the user account is deleted, any Exchange Online license associated with the user account will be available to assign to a new user.

We recommend you use Microsoft 365 retention to apply the hold on the mailbox. Other methods are covered in [Learn about inactive mailboxes](inactive-mailboxes-in-office-365).

The best way to delete a mailbox is to delete the corresponding user account in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For information about deleting user accounts, see [Delete a user from your organization](/en-us/microsoft-365/admin/add-users/delete-a-user). However, you can also delete the mailbox by using the **Remove-Mailbox** cmdlet in Exchange Online PowerShell. For more information, see [Delete or restore user mailboxes in Exchange Online](/en-us/exchange/recipients-in-exchange-online/delete-or-restore-mailboxes).

The following table summarizes the process of making an inactive mailbox for different retention scenarios.

| To... | Do this... | Result |
| --- | --- | --- |
| Retain mailbox content indefinitely after an employee leaves the organization | 1. Apply Microsoft 365 retention settings with retain actions for the mailbox (a retention policy) or specific email items (one or more retention labels).  2. Wait for the retention settings to be applied.  3. Remove the user's Microsoft 365 account. | All content in the inactive mailbox that has retention settings applied, including items in the Recoverable Items folder, is retained indefinitely. |
| Retain all mailbox content for a specific period after an employee leaves the organization and then delete the mailbox | 1. Apply a Microsoft 365 retention policy to the mailbox with retention settings that retain and then delete items when the retention period expires.  2. Wait for the retention settings to be applied.  3. Remove the user's Microsoft 365 account. | When the retention period for a mailbox item expires, the item is moved to the Recoverable Items folder and then it's permanently deleted (purged) from the inactive mailbox when the deleted item retention period (for Exchange mailboxes) expires. The retention period of the Microsoft 365 retention policy is always based on the original date a mailbox item was received or created. |

Note

If Microsoft 365 retention settings that are configured to retain, or retain and then delete content, is already applied to the mailbox or mailbox items, or a Litigation hold is already placed on a mailbox, or then all you have to do to create an inactive mailbox is delete the corresponding user account.

## View a list of inactive mailboxes

You can use the Microsoft Purview portal to view a list of the inactive mailboxes in your organization.

Note

The portals are limited to displaying up to 5,000 inactive mailboxes. To view more than 5,000 inactive mailboxes, you must use Exchange Online PowerShell as described after the step instructions.

For this configuration, use the [Microsoft Purview portal](purview-portal) and a Compliance administrator account for your organization.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Policies** &gt; **Retention policies**.
2. Select the **Inactive mailbox** option. For example, from the Microsoft Purview portal:

    ![Inactive mailbox option on the Retention policies page from data lifecycle management.](media/inactive-mailbox-option.png)
3. The **Inactive mailboxes** page displays a list of inactive mailboxes. Select one to see details about that inactive mailbox. Details include the Exchange identifier for the mailbox and whether it's on [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds).

    You won't see other types of holds in the details pane, for example a Microsoft 365 retention policy or eDiscovery hold. To find this information, see [How to identify the type of hold placed on an Exchange Online mailbox](ediscovery-identify-a-hold-on-an-exchange-online-mailbox).

If you have many inactive mailboxes, you might find it easier to search and sort a CSV file for the details you see in the list: On the **Inactive mailboxes** page, select ![](media/47205c65-babd-4b3a-bd7b-98dfd92883ba.png)**Export**.

Alternatively, you can run the following command in Exchange Online PowerShell to display the list of inactive mailboxes:

```powershell
 Get-Mailbox -InactiveMailboxOnly -ResultSize Unlimited | FT DisplayName,PrimarySMTPAddress,WhenSoftDeleted
```

You can also run the following command to export the list of inactive mailboxes and other information to a CSV file. In this example, the CSV file is created in the current directory.

```powershell
Get-Mailbox -InactiveMailboxOnly -ResultSize Unlimited | Select Displayname,PrimarySMTPAddress,DistinguishedName,ExchangeGuid,WhenSoftDeleted | Export-Csv InactiveMailboxes.csv -NoTypeInformation
```

Note

It's possible that an inactive mailbox might have the same SMTP address as an active user mailbox. In this case, the value of the **DistinguishedName** or **ExchangeGuid** property can be used to uniquely identify an inactive mailbox.

## Search and export the contents of an inactive mailbox

You can access the contents of the inactive mailbox by using the Content Search tool in the Microsoft Purview portal. For more information, see the [Feature reference for Content search](ediscovery-content-search-reference#searching-inactive-mailboxes) article.

## Change the hold duration for an inactive mailbox

After a mailbox is made inactive, you might be able to change the duration of the hold applied to the inactive mailbox.

For step-by-step procedures, see [Change the hold duration for an inactive mailbox](change-the-hold-duration-for-an-inactive-mailbox).

## Recover an inactive mailbox

If a former employee returns to your organization, or if a new employee is hired to take on the job responsibilities of the former employee, you can recover the contents of the inactive mailbox.

When you recover an inactive mailbox, the mailbox is converted to a new mailbox, the contents and folder structure of the inactive mailbox are retained, and the mailbox is linked to a new user account. After it's recovered, the inactive mailbox no longer exists.

For step-by-step procedures and more information about happens when you recover an inactive mailbox, see [Recover an inactive mailbox](recover-an-inactive-mailbox).

## Restore the contents of an inactive mailbox to another mailbox

If another employee takes on the job responsibilities of a former employee, or if another person needs access to the contents of the inactive mailbox, you can restore (or merge) the contents of the inactive mailbox to an existing mailbox.

When you restore an inactive mailbox, the contents are copied to another mailbox. The inactive mailbox is retained and remains an inactive mailbox. The inactive mailbox can still be searched using eDiscovery, its contents can be restored to another mailbox, or it can be recovered or deleted at a later date.

For step-by-step procedures, see [Restore an inactive mailbox](restore-an-inactive-mailbox).

## Delete an inactive mailbox

If you no longer need to retain the contents of an inactive mailbox, you can permanently delete the inactive mailbox by removing the hold applied to the inactive mailbox.

For more details and step-by-step procedures, see [Delete an inactive mailbox](delete-an-inactive-mailbox).

Note

If a mailbox is still listed as inactive after you remove the last hold, check whether a delay hold is applied. A delay hold is applied automatically after another hold is removed, and it keeps the mailbox inactive until the delay hold is removed or expires. For instructions, see [Remove a delay hold from an inactive mailbox](delete-an-inactive-mailbox#remove-a-delay-hold-from-an-inactive-mailbox).