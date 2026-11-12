---
layout: Conceptual
title: Authoring and publishing Data owner policies (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-policies-data-owner-authoring-generic
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Step-by-step guide on authoring and publishing Data owner policies in Microsoft Purview so users or groups in your enterprise can read or modify data assets.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: sfi-image-nochange, msecd-doc-authoring-1030
locale: en-us
document_id: 052ea4bd-9405-9805-bf6e-a84fcd8a4441
document_version_independent_id: 052ea4bd-9405-9805-bf6e-a84fcd8a4441
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-policies-data-owner-authoring-generic.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-policies-data-owner-authoring-generic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-policies-data-owner-authoring-generic.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: cf8f8ad2-2517-da56-1877-3b7ed0e14904
---

# Authoring and publishing Data owner policies (preview) | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

[Data owner policies](../concept-policies-data-owner) are a type of Microsoft Purview access policies. They allow you to manage access to user data in sources that have been registered for *Data Policy Enforcement* in Microsoft Purview. These policies can be authored directly in the Microsoft Purview governance portal, and after publishing, they get enforced by the data source.

This guide describes how to create, update, and publish data owner policies in the Microsoft Purview governance portal.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A new or existing Microsoft Purview account. [Follow this quickstart guide to create one](../create-microsoft-purview-portal).

### Configuration

Before authoring policies in the Microsoft Purview policy portal, you'll need to configure Microsoft Purview and the data sources so that they can enforce those policies.

1. Follow any policy-specific prerequisites for your source. Check the [Microsoft Purview supported data sources table](../data-map-data-sources) and select the link in the **Access Policy** column for sources where access policies are available. Follow any steps listed in the Access policy or Prerequisites sections.
2. Register the data source in Microsoft Purview. Follow the **Prerequisites** and **Register** sections of the [source pages](../data-map-data-sources) for your resources.
3. Enable the Data policy enforcement option on the data source registration. Data Policy Enforcement needs certain permissions and can affect the security of your data, as it delegates to certain Microsoft Purview roles to manage access to the data sources. **Go through the secure practices related to Data Policy Enforcement in this guide**: [How to enable Data Policy Enforcement](../how-to-enable-data-policy-enforcement)

## Create a new policy

This section describes the steps to create a new policy in Microsoft Purview. Ensure you have the *Policy Author* permission as described [here](../how-to-enable-data-policy-enforcement#configure-microsoft-purview-permissions-to-create-update-or-delete-access-policies).

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.
3. Select the **New Policy** button in the policy page.

    ![Screenshot showing data owner can access the Policy functionality in Microsoft Purview when it wants to create policies.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-1.png)
4. The new policy page will appear. Enter the policy **Name** and **Description**.
5. To add a policy statement to the new policy, select the **New policy statement** button. This will bring up the policy statement builder.

    ![Screenshot showing data owner can create a new policy statement.](../media/how-to-policies-data-owner-authoring-generic/create-new-policy.png)
6. Select the **Effect** button and choose *Allow* from the drop-down list.
7. Select the **Action** button and choose *Read* or *Modify* from the drop-down list.
8. Select the **Data Resources** button to bring up the window to enter Data resource information, which will open to the right.
9. Under the **Data Resources** Panel do **one of two things** depending on the granularity of the policy:

    - To create a broad policy statement that covers an entire data source, resource group, or subscription that was previously registered, use the **Data sources** box and select its **Type**.
    - To create a fine-grained policy, use the **Assets** box instead. Enter the **Data Source Type** and the **Name** of a previously registered and scanned data source. See example in the image.

    ![Screenshot showing data owner can select a Data Resource when editing a policy statement.](../media/how-to-policies-data-owner-authoring-generic/select-data-source-type.png)
10. Select the **Continue** button and transverse the hierarchy to select and underlying data-object (for example: folder, file, etc.). Select **Recursive** to apply the policy from that point in the hierarchy down to any child data-objects. Then select the **Add** button. This will take you back to the policy editor.

    ![Screenshot showing data owner can select the asset when creating or editing a policy statement.](../media/how-to-policies-data-owner-authoring-generic/select-asset.png)
11. Select the **Subjects** button and enter the subject identity as a principal, group, or MSI. Note that Microsoft 365 groups are supported but updates to group membership take up to 1 hour to get reflected by Microsoft Entra ID. Then select the **OK** button. This will take you back to the policy editor.

    ![Screenshot showing data owner can select the subject when creating or editing a policy statement.](../media/how-to-policies-data-owner-authoring-generic/select-subject.png)
12. Select the **Save** button to save the policy.

Now that you have created your policy, you will need to publish it for it to become active.

## Publish a policy

A newly created policy is in the **draft** state. The process of publishing associates the new policy with one or more data sources under governance. This is called "binding" a policy to a data source.

Ensure you have the *Data Source Admin* permission as described [here](../how-to-enable-data-policy-enforcement#configure-microsoft-purview-permissions-for-publishing-data-owner-policies)

The steps to publish a policy are as follows:

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.

    ![Screenshot showing data owner can access the Policy functionality in Microsoft Purview when it wants to update a policy by selecting Data policies.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-2.png)
3. The Policy portal will present the list of existing policies in Microsoft Purview. Locate the policy that needs to be published. Select the **Publish** button on the right top corner of the page.

    ![Screenshot showing data owner can publish a policy.](../media/how-to-policies-data-owner-authoring-generic/publish-policy.png)
4. A list of data sources is displayed. You can enter a name to filter the list. Then, select each data source where this policy is to be published and then select the **Publish** button.

    ![Screenshot showing data owner can select the data source where the policy will be published.](../media/how-to-policies-data-owner-authoring-generic/select-data-sources-publish-policy.png)

Note

After making changes to a policy, there is no need to publish it again for it to take effect if the data source(s) continues to be the same.

## Unpublish a policy

Ensure you have the *Data Source Admin* permission as described [here](../how-to-enable-data-policy-enforcement#configure-microsoft-purview-permissions-for-publishing-data-owner-policies)

The steps to publish a policy are as follows:

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.

    ![Screenshot showing data owner can access the Policy functionality in Microsoft Purview when it wants to update a policy by selecting Data policies.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-2.png)
3. The Policy portal will present the list of existing policies in Microsoft Purview. Locate the policy that needs to be unpublished. Select the trash can icon.

![Screenshot shows how to unpublish a data owner policy.](../media/how-to-policies-data-owner-authoring-generic/unpublish-policy.png)

## Update or delete a policy

Steps to update or delete a policy in Microsoft Purview are as follows. Ensure you have the *Policy Author* permission as described [here](../how-to-enable-data-policy-enforcement#configure-microsoft-purview-permissions-to-create-update-or-delete-access-policies)

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.

    ![Screenshot showing data owner can access the Policy functionality in Microsoft Purview when it wants to update a policy.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-2.png)
3. The Policy portal will present the list of existing policies in Microsoft Purview. Select the policy that needs to be updated.
4. The policy details page will appear, including Edit and Delete options. Select the **Edit** button, which brings up the policy statement builder. Now, any parts of the statement in this policy can be updated. To delete the policy, use the **Delete** button.

    ![Screenshot showing data owner can edit or delete a policy statement.](../media/how-to-policies-data-owner-authoring-generic/edit-policy.png)