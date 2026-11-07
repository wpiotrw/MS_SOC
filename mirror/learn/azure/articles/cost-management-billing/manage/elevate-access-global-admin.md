---
layout: Conceptual
title: Elevate access to manage billing accounts - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/elevate-access-global-admin
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ebeaa30a-2425-ec11-b6e6-000d3a4f0f84
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Describes how to elevate access for a Global Administrator to manage billing accounts using the Azure portal or REST API.
author: jkinma39
ms.reviewer: jkinma
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-06-25T00:00:00.0000000Z
ms.author: jkinma
ms.custom:
- sfi-image-nochange
- sfi-ga-nochange
service.tree.id: 95459a4b-434c-4f83-879b-aa5f509fc7fa
locale: en-us
document_id: 6f1fd6d5-78ea-23d2-e754-97c9e164f27a
document_version_independent_id: 6dd6a53c-7d72-ea3a-fc53-b28185e810c5
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/elevate-access-global-admin.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/elevate-access-global-admin
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/elevate-access-global-admin.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 574bab8b-875f-89f3-34a0-ae38014ae8c8
---

# Elevate access to manage billing accounts - Microsoft Cost Management | Microsoft Learn

As a Global Administrator in Microsoft Entra ID, you might not have access to all billing accounts in your directory. This article describes the ways that you can elevate your access to all billing accounts.

Elevating your access to manage all billing accounts gives you the ability to view and manage cost and billing for your accounts. You can view invoices, charges, products that are purchased, and the users that have access to the billing accounts. If you want to elevate your access to manage subscriptions, management groups, and resources, see [Elevate access to manage all Azure subscriptions and management groups](../../role-based-access-control/elevate-access-global-admin#elevate-access-to-manage-all-azure-subscriptions-and-management-groups).

Note

Elevated access only works for Microsoft Customer Agreement (MCA) and Microsoft Partner Agreement (MPA) billing account types. As a Global Administrator you can't elevate your access to manage billing accounts for Enterprise Agreement (EA) and Microsoft Online Service Program (MOSP) types. To learn more about billing accounts, see [Billing accounts and scopes in the Azure portal](view-all-accounts).

## Why elevate your access?

If you’re a Global Administrator, there might be times when you want to do the following actions:

- See all users who have created individual billing accounts in your organization.
- View invoices and charges for all individual billing accounts created in your organization.
- Regain access to a billing account when a user has lost access.
- Perform billing administration for an account when other administrators aren't available.

## How does elevated access work?

All Global Administrators in Microsoft Entra ID get read-only access to all Microsoft Customer Agreement (MCA) and Microsoft Partner Agreement (MPA) billing accounts in their Microsoft Entra ID. They can view all billing accounts and the corresponding cost and billing information. Along with a read-only view, they get permission to manage role assignments on the billing accounts. They can add themselves as owners of the billing accounts to elevate themselves.

## Elevate access to manage billing accounts

# [Azure portal](#tab/portal)
1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for **Cost Management + Billing**.![Screenshot that shows Search in the Azure portal for Cost Management + Billing.](media/elevate-access-global-admin/billing-search-cost-management-billing.png)
3. Select **Billing scopes** on the left side of the page.
4. On the Billing scopes page, select the box to view all billing accounts.[![Screenshot that shows global admins selecting the box to view all accounts.](media/elevate-access-global-admin/global-admin-view-all-accounts.png)](media/elevate-access-global-admin/global-admin-view-all-accounts.png#lightbox)
    Note

    The billing scopes page shows only 200 scopes. However, you can use the search box in the page to search for accounts that are not part of the list.
5. Select a Microsoft Customer Agreement or a Microsoft Partner Agreement billing account from the list. As a Global administrator, you have read access to the billing account. To elevate yourself to perform write operations, follow steps 6 to 8.
6. Select **Access Control (IAM)** on the left side of the page.
7. Select **Add** at the top of the page.[![Screenshot showing global admins selecting Add.](media/elevate-access-global-admin/role-assignment-list.png)](media/elevate-access-global-admin/role-assignment-list.png#lightbox)
8. In the Add permission window, in the **Role** list, select **Billing account owner**. Under the **Select** area, select your user name, and then select **Add** at the bottom of the window.

# [REST API](#tab/rest)
You can use the [Azure Billing](/en-us/rest/api/billing/) APIs to programmatically elevate yourself to manage all billing accounts in your directory.

### Find all billing accounts in your directory

```json
GET https://management.azure.com/providers/Microsoft.Billing/billingAccounts?includeAllOrgs=true&api-version=2020-05-01
```

The API response returns a list of billing accounts in your directory.

```json
{
  "value": [
    {
            "id": "/providers/Microsoft.Billing/billingAccounts/6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "name": "6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "properties": {
                "accountStatus": "Active",
                "accountType": "Individual",
                "agreementType": "MicrosoftCustomerAgreement",
                "billingProfiles": {
                    "hasMoreResults": false
                },
                "displayName": "Connie Wilson",
                "hasReadAccess": true
            },
            "type": "Microsoft.Billing/billingAccounts"
        },
        {
            "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "name": "5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "properties": {
                "accountStatus": "Active",
                "accountType": "Enterprise",
                "agreementType": "MicrosoftCustomerAgreement",
                "billingProfiles": {
                    "hasMoreResults": false
                },
                "displayName": "Contoso",
                "hasReadAccess": true
            },
            "type": "Microsoft.Billing/billingAccounts"
        },
        {
            "id": "/providers/Microsoft.Billing/billingAccounts/4e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "name": "4e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
            "properties": {
                "accountStatus": "Active",
                "accountType": "Individual",
                "agreementType": "MicrosoftCustomerAgreement",
                "billingProfiles": {
                    "hasMoreResults": false
                },
                "displayName": "Tomas Wilson",
                "hasReadAccess": true
            },
            "type": "Microsoft.Billing/billingAccounts"
        }
  ]
}
```

Use the `displayName` property of the billing account to identify the billing account for which you want to elevate your access. Copy the `name` of the billing account. For example, if you want to elevate yourself as owner on the **Connie Wilson** billing account, you'd copy `6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx`. Paste the value somewhere so that you can use it in the next step.

### Get definitions of roles available for your billing account

Make the following request, replacing `<billingAccountName>` with the `name` copied in the first step (`6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx`).

```json
GET https://management.azure.com/providers/Microsoft.Billing/billingAccounts/<billingAccountName>/billingRoleDefinitions?api-version=2020-05-01
```

The API response returns list of roles available to your billing account.

```json
{
    "value": [
        {
            "id": "/providers/Microsoft.Billing/billingAccounts/6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingRoleDefinitions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
            "name": "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
            "properties": {
                "description": "The Owner role gives the user all permissions including access management on a billing account.",
                "permissions": [
                    {
                        "actions": [
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1"
                        ]
                    }
                ],
                "roleName": "Billing account owner"
            },
            "type": "Microsoft.Billing/billingAccounts/billingRoleDefinitions"
        },
        {
            "id": "/providers/Microsoft.Billing/billingAccounts/6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingRoleDefinitions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
            "name": "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
            "properties": {
                "description": "The Contributor role gives the user all permissions except access management on a billing account.",
                "permissions": [
                    {
                        "actions": [
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                        ]
                    }
                ],
                "roleName": "Billing account contributor"
            },
            "type": "Microsoft.Billing/billingAccounts/billingRoleDefinitions"
        },
        {
            "id": "/providers/Microsoft.Billing/billingAccounts/6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingRoleDefinitions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
            "name": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
            "properties": {
                "description": "The Reader role gives the user read permissions to a billing account.",
                "permissions": [
                    {
                        "actions": [
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                            "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",
                        ]
                    }
                ],
                "roleName": "Billing account reader"
            },
            "type": "Microsoft.Billing/billingAccounts/billingRoleDefinitions"
        }
    ]
}
```

Use the `roleName` property to identify the owner role definition. Copy the `name` of the role definition. For example, from the preceding API response, you'd copy `aaaabbbb-0000-cccc-1111-dddd2222eeee`. Paste this value somewhere so that you can use it in the next step.

### Add yourself as an owner

Make the following request, replacing `<billingAccountName>` with the `name` copied in the first step (`6e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx`).

```json
PUT  https://management.azure.com/providers/Microsoft.Billing/billingAccounts/<billingAccountName>/createBillingRoleAssignment?api-version=2020-05-01
```

#### Request body

To add yourself as an owner, you need to get your object ID. You can find the object ID either in the Users page of the Microsoft Entra ID section in the Azure portal or your can use the [Microsoft Graph API](/en-us/graph/api/resources/users?view=graph-rest-1.0&amp;preserve-view=true) to get the object ID.

In the request body, replace `<roleDefinitionName>` with the `name` copied from Step 2. Replace `<principalId>` with the object ID that you got either from the Azure portal or through the Microsoft Graph API.

```json
{    "principalId": "<principalId>",    "roleDefinitionId": "<roleDefinitionName>"
}
```

---

## Need help? contact support

If you need help, [contact support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade) to get your issue resolved quickly.