---
layout: Conceptual
title: Manage Data Product Access Policies in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-product-access-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure and manage access policies for data products in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 61fa377d-2d2d-1b9b-8f18-c02aab58f036
document_version_independent_id: 61fa377d-2d2d-1b9b-8f18-c02aab58f036
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-product-access-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-product-access-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-product-access-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 833c4075-0340-4904-b3b4-6f2f071306bd
---

# Manage Data Product Access Policies in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

This article explains how to set access policies on business concepts including governance domains, data products, critical data elements, and glossary terms, and how to manage access requests. If you need to request access for yourself, see [Request access to data products](unified-catalog-data-product-access-requests).

Access to a data product in Microsoft Purview Unified Catalog grants users permissions to the data product and permissions to the data assets within the data product. This article explains how you can manage access to your data products and set up a system to provide access to users who request it.

This article explains:

- How to set up a data product access policy.
- How to manage and approve access to data products.

## Permissions

- To view and manage policies at the governance domain level, you need [governance domain owner permissions](data-governance-roles-permissions).
- To view and manage policies at the data product level, you need [data product owner permissions](data-governance-roles-permissions).
- To view and manage policies in critical data elements or glossary terms, you need [data steward permissions](data-governance-roles-permissions).
- Unified Catalog readers can view and request access to data products.
- Managers and privacy approvers of access requests also need to have a minimum of a catalog reader to be able to use the Unified Catalog and approve requests as part of the tiered approval.

## Considerations

In this experience, request approvers must provide access to the individual data assets manually as part of the approval process, or specify an access provider to do so.

The product doesn't enforce policies such as attestations (including the no copy attestation). The data consumer attests that they'll follow these policies while requesting access.

## Skip the access policies and workflow setup

If you use an external solution for access management or don't want to have access requests on a data product, you can disable this feature during data product curation. When you disable access management on the data product, no access policies from business concepts, workflows, or the request access button apply to that data product.

To disable the access process on a data product:

1. Select the data product in a draft state.
2. Select the **Manage policies** tab.
3. Scroll down to the workflows section of the tab to the checkbox **Disable Access Management** and make sure it's checked.

## Set up data product access policies

To build access policies, you usually need data product owner or data steward permissions.

Tip

Your data product needs to be in an unpublished state to manage access policies.

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open Unified Catalog.
2. Under **Catalog management**, select **Data products**, then select a data product.
3. On the data product's details page, select **Manage policies**. Here you can view and edit the default values assigned to the default set of data product access policies. The selected values affect what the data consumers see on their access request form and actions they need to take.
4. Under **Permitted access**, add your usage purposes, which are the authorized purposes for accessing and using the data product. Three purposes are provided by default. You can add more purposes and their descriptions, which the consumer can select in the request access form.
5. At **Approval requirements**, determine if manager approval or a privacy and compliance review is required.

    Note

    If you select these options, the access request form shows that a manager approver or a privacy and compliance review is required. The consumer’s manager in Microsoft Entra ID is notified for the first tier of approval. The privacy reviewer named by the consumer in the request form is notified for their approval. The request is first reviewed by manager, followed by the privacy reviewer, and then by the access request approvers for approval and granting of access. The optional access provider tier is last, if selected. The request status is final only when all configured levels of approval are complete.
6. Under the **Approval requirements** dropdown, in **Access request approvers**, select the users that need to approve the access request. The first approver to take action approves the request and proceeds to grant access to the data assets manually, records the status of access provisioned at each asset, and specifies data access instructions or comments to the data consumer. By default, data product owners are populated and you can add more approvers. You can also add Microsoft Entra ID groups or security groups as approvers. Approvers can see detailed status in the request view.
7. An optional tier called **Access provider** can be set explicitly to grant access to the data assets manually, record the status of access provisioned at each asset, and specify data access instructions or comments to the data consumer. This practice ensures the data consumer is aware of the next steps they can take to access and use the data.

    Note

    You can select a role group to grant approver status to all the users in a group at once. However, users who belong to nested groups within the role group aren't supported at this time.
8. Under **Attestations**, determine if copies of the data are permitted. The attestations are reflected on the access request form for the consumer to attest to.
9. If terms of use are present on a data product, those terms are also reflected on the access request form for the consumer to attest to.
10. Add any more attestations by selecting **Add attestation** and adding a display name and the file location. These attestations are reflected on the request access form for the consumer to attest to.
11. If there are policies inherited from the governance domain, critical data element, or glossary term, you can see them in the **Inherited policies** tab. See the following section in this document for details: Policies on governance domains and glossary terms (inherited policies).
12. Select **Preview request form** to see what users see when they request access.
13. Select **Save changes** to save the access policy for the governance domain.

## Policies on governance domains, glossary terms, and critical data elements (inherited policies)

You can set policies on governance domains, glossary terms, and critical data elements. Data products in the governance domain, or data products that have glossary terms or critical data elements applied, inherit and aggregate these policies.

You can see the inherited policies in the data product manage policies view, in a separate tab called **Inherited policies**. You can see the aggregated view by selecting the **Preview** button. Your data consumers see this aggregated view when they request access.

For example, if you set a manager approval policy on a glossary term applied to the data product, the data product also requires manager approval. Any attestation set on a business concept (governance domain, data product, glossary term, or critical data element) is aggregated on the data product, and the data consumer attests to all required attestations when requesting access.

To build access policies on governance domains, glossary terms, or critical data elements, you need governance domain owner or data steward permissions.

1. [In the Microsoft Purview portal](https://purview.microsoft.com/), open Unified Catalog.
2. Select the **Catalog management** dropdown and select **Governance domains**.
3. Select a governance domain.
4. On the governance domain page, select **Manage policies**.
5. Alternately on a glossary term or critical data element page, select **Manage policies**.
6. From the Policy configuration window, you're able to create and manage relevant access policies.

### Configure inherited policies

In the **Manage policies** window, you can view and manage the default set of access policies on each business concept. The selected values affect what the data consumers see on their access request form and actions they need to take.

1. Determine if manager approval is required. The data consumer’s manager, configured in Microsoft Entra ID, is notified as first tier of approval. If the request is approved, the request proceeds to the next tier.
2. Determine if copies of the data are permitted. This selection is reflected on the access request form for the consumer to attest to.
3. Add any more attestations you want by selecting **Add attestation** and adding a display name and the file location. These attestations are reflected on the request access form for the consumer to attest to.

## View and manage access requests

Important

The **Requests** page in **Catalog management** shows only the access requests from the existing published data products before the [new workflow feature](unified-catalog-workflows) became available on 11/12/2025. All access requests and other approvals moving forward are in the **Requests and approvals** tab under the **Waiting for my response** screen. The process and approvals are the same.

To view access requests in Unified Catalog, follow these steps. When you select an access request, the **Access Request** flyout pane opens. It contains details about the request and its status. You see only requests for which you're an approver.

1. In Unified Catalog, select **Catalog management**, then select **Requests**.
2. In the status column of the governance domain table, sort by any domains that have open access requests.
3. Select the governance domain that you want to manage access requests for.
4. On the access requests tab, you see a list of the most recent access requests.
5. Select the access request you want to respond to.
6. View the details submitted by the consumer.
7. Select **Approve** or **Deny**.
8. If you're the last approver in the sequence of approvers (a data product access request approver or an explicit access provider), record the status of access provisioned at each asset and specify data access instructions or comments to the data consumer. This practice ensures the data consumer is aware of the next steps they can take to access and use the data.
9. The data consumer is notified once you respond to the request.
10. The requestor is notified via email and can also view the status on the Microsoft Purview Unified Catalog **Discovery** drop-down, **Data products** page, in the **My data access tab**.

#### Request statuses

- **Pending**: The request is sent to an approver for review.
- **Declined**: The request is denied by the approver.
- **Approved**: The request is approved, but provisioning work isn't yet completed to grant access to the requestor.
- **Completed**: The data asset is provisioned to grant access for the requestor. This request is now fully complete.

## Respond to access requests through email notification

1. In the email you receive as a request to approve an access request, select the **Approval** request link.
2. You're brought to the request detail view in **Requests** page in **Catalog management** .
3. View the details submitted by the consumer.
4. Select **Approve** or **Deny**.
5. If you're the last approver in the sequence of approvers, a data product access request approver, or an explicit access provider, record the status of access provisioned at each asset and specify data access instructions or comments to the data consumer. This step ensures the data consumer is aware of the next steps they can take to access and use the data.
6. If you're the last approver in the sequence of approvers, and there are multiple data assets in the data product, you can record the status and save intermittently and mark the request as complete only when you're done with all the data assets.
7. The data consumer is notified once the request is responded to and in its final state.
8. The requestor is notified via email and can also view the status on the Microsoft Purview Unified Catalog **Data product search** page, in the **My data access** tab.

## Sequential or tiered approvals and request statuses

As noted in the section to manage policies on data product, depending on the approver selections you make, a sequential or tiered approval is in effect. The following sequence is maintained for data product access request approvals.

1. If you select manager approval, the consumer’s manager in Microsoft Entra is notified for the first tier of approval.
2. Only after the manager approves the request, the privacy reviewer if selected is notified for their approval or can take action.
3. Once approved by the privacy reviewer, the access request approver is notified for approval and provisioning of access to the data assets in the data product. This tier approves and completes the request if there's no access provider specified, else they only approve.
4. If there's a last tier of access provider specified, then that tier provisions access to the data assets and records the status and instructions for data consumer. They complete the request. Complete is the final status.
5. The workflow proceeds until the last approval and completion occurs or the first denial occurs.
6. The data consumer is only notified after all approvers take their respective actions.
7. At any point the data consumer can see the status of the request in the Microsoft Purview Unified Catalog **Discovery** drop-down, **Data products** page, in the **My data access** tab.
8. A request status can go from pending to declined or pending to approved and then to completed.

## Delete access requests

To revoke a user's access to a data product and the data assets within the data product, the request approver needs to complete both of the steps listed below.

Note

The only request approver who can remove access to a data product and delete an access request is the owner of that same data product. This data owner must also hold the [Data Product Owner role](data-governance-roles-permissions#unified-catalog-roles).

1. Return to the individual data asset (such as in Azure Data Lake, Microsoft Fabric, or SQL) and manually remove the provisioning for the user.
2. Delete the request in Unified Catalog by following these steps:

    1. In Unified Catalog, select **Catalog management**, then select **Requests**.
    2. Select a governance domain, then select the name of the request you want to delete.
    3. On the **Access Request** flyout pane, select **Delete**.

If you remove the provisioning on the asset but don't delete the access request in Unified Catalog, the data product shows that the user's access is removed, but the user still has access to the underlying data assets.