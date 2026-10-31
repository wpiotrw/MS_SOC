---
layout: Conceptual
title: Merge classic Microsoft Purview account into your tenant as a domain | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-domains-merge-account
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-08-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to merge an existing Microsoft Purview account into your Microsoft Purview tenant as a domain.
locale: en-us
document_id: 117d830b-c831-b2c8-4e55-86ff02a84023
document_version_independent_id: 117d830b-c831-b2c8-4e55-86ff02a84023
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-domains-merge-account.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-domains-merge-account
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-domains-merge-account.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 11e537af-1188-feeb-1714-6816fc31229e
---

# Merge classic Microsoft Purview account into your tenant as a domain | Microsoft Learn

This guide describes how to merge an existing classic Microsoft Purview account into your Microsoft Purview tenant account as a [domain](data-map-domains). Merge is a one-time process to *copy* the information in your secondary classic Microsoft Purview account into your tenant level account. All the information is incorporated into a new domain. Your existing classic account remains as-is, so you can migrate your managed identity and deactivate and remove the secondary account once you have validated the merge.

Throughout this document, we use the terms **primary account** and **secondary account**:

- **Primary account** - refers to your tenant-level Microsoft Purview instance.
- **Secondary account** - refers to the Microsoft Purview instance you're migrating into your primary account as a domain.

## Prerequisites

- Tenant with multiple Microsoft Purview accounts.
- Public network access enabled on your **secondary account** for the merging process.
- [A Microsoft Purview account upgraded to the new experience as a primary account](data-governance-purview-portal#multiple-microsoft-purview-accounts).

## Limitations

1. Secondary accounts can only be merged once. Any values added to your secondary account after merging will have to be manually added to your primary account. It's recommended you stop using your secondary account after merging and either deactivate or delete the account.
2. Any values or assets added to a secondary account during an active merge aren't guaranteed to be migrated to the primary account. It's recommended you stop update and scanning activities on your secondary account during a merge.

There are also some current limitations that could prevent you from merging your existing Microsoft Purview account as a domain. Review these limitations and the behavior changes to confirm that merging is the correct option for you. The limitations could be updated in the future.

| Category | Limitation | Potential resolution |
| --- | --- | --- |
|  | Primary account can only have five domains. | [Contact support](https://azure.microsoft.com/support/create-ticket/) to provide your business requirement and increase the domain number. |
|  | Either primary account or secondary account has more than 1,000,000 assets. | Remove assets to the allowed limit, choose to filter out the asset category, or [contact support](https://azure.microsoft.com/support/create-ticket/) to provide your business requirements. |
|  | Secondary account’s collection number + primary account’s collection number &gt; 400. | Remove or consolidate collections to the allowed limit. |
| Scan limitations | Secondary account has a user-assigned managed identity (UAMI) scan. | Remove all scheduled UAMI scans from any data sources or filter out the user assigned managed identity category during merge. |
|  | Scan run histories aren't migrated to the primary account. | No resolution. |
|  | Secondary account has private endpoints enabled. | Remove all private endpoints from secondary account or filter out the private endpoint category during merge. |
|  | Secondary account has a self-hosted integration runtimes. | [Remove all self-hosted integration runtimes from secondary account](data-map-integration-runtime-self-hosted#manage-a-self-hosted-integration-runtime) or filter out the self-hosted integration runtime category during merge. |
|  | Secondary account has managed virtual networks. | Remove all managed virtual networks from secondary account or filter out the managed virtual networks category during merge. |
|  | Secondary account has "bring your own Event Hubs" configured. | [Remove all Kafka configurations from secondary accounts.](data-map-kafa-notifications#remove-configured-event-hubs) |
|  | Secondary account has managed Event Hubs enabled and it's actively used in last 30 days. | Disable managed event hub. |
|  | Secondary account has a data factory connection. | Remove data factory connections. |
|  | Secondary account has a data share connection. | [Remove all data share connections.](how-to-share-data#delete-share) |
| Asset limitations | Secondary account has lineage scans. | Remove all lineage scans from any data sources. |
| Source limitations | Secondary account has a Website data source registered. | Unregister all Website data sources |

### Behavior changes

1. Any secondary accounts' scans that use the managed identity (MSI) to scan a data source will keep using the same MSI after migrating to the primary account. So, if the secondary account is deleted after merge, these migrated scans won't work unless you follow the managed identity switchover process after merging.
2. Any secondary accounts' key vault connections that use managed identity (MSI) to connect will keep using the same MSI after migrating to the primary account. So if the secondary account is deleted after merge, these migrated scans won't work unless you follow the managed identity switchover process after merging.
3. If secondary account has a glossary named *Glossary*, the migrated glossary is named *Glossary-{secondary account name}* in the primary account. This behavior could cause glossary conflicts during assessment:

    - Secondary account already has a glossary named *Glossary-{secondary account name}*
    - Primary account has a glossary named *Glossary-{secondary account name}*
4. If the secondary account was created before 7/12/2022 and the primary account was created after this date, after the merge, the scan will populate hierarchical schema types(parquet\_schema, json\_schema, xml\_schema, and delimited\_text\_schema) rather than tabular\_schema.

## Request account merge

You can request an account merge from your primary account or from the secondary account you want to merge.

Tip

It's recommended to assess your merge before requesting a full merge to check for any conflicts or limitations.

### Request account merge from the primary account

Important

To request account merge from the primary account, requestors need to be a member of the [**Purview Administrator** role group](data-governance-roles-permissions#tenant-level-role-groups).

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. To select an existing account to be mapped as a new domain in primary account. You can either:

    - Select the **Select account** button in the pop-up.

        ![Screenshot of the merge account menu in the Microsoft Purview portal.](media/merge-domain/select-account.png)
    - If you're using the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), open the Management center, navigate to the **Overview** in the General section. If you're using the [Microsoft Purview portal](https://purview.microsoft.com), open Settings solution card, select **Account** and then select **Select account** in the alert box.

        ![Screenshot of the merge account menu in the classic Microsoft Purview governance portal.](media/merge-domain/governance-portal-merge-menu.png)

    Note

    - If a merge is currently in progress within the tenant, then the **Submit request** pop-up and alert box won't appear.
    - If the logged-in user doesn't have the proper permissions to request a merge, the **Submit request** pop-up and alert box won't appear.
3. Select an account to merge. (It's recommended that you perform an assessment before you merge.)

    ![Screenshot of the select account menu in the Microsoft Purview portal.](media/merge-domain/select-account-to-merge.png)
4. Specify categories for the merge filter, and select whether you want to allow auto-resolve for conflicts in that category.
5. Select **Submit**.
6. An assessment runs to confirm if there are any conflicts or limitations, and if the assessment is successful, the merge process begins.
7. You can monitor the merge process from the report page.

Important

Failed merges start the cleanup process to revert everything back to its previous state.

### Request account merge from secondary account

Important

To request account merge from the secondary account, requestors need to be either be a [**Collection Admin**](catalog-permissions#roles) on the root collection or an **ARM Resource Owner**, and then they also need to be assigned one of these roles: [**Compliance Manager Administration, Role Management, Case Management**](catalog-permissions#roles) .

1. Open the secondary account's Microsoft Purview portal
2. To select this account to be mapped as a new domain in primary account, you can either:

    - Select **Submit merge request** in the pop-up.

        ![Screenshot of the submit merge pop-up on a secondary account.](media/merge-domain/secondary-submit-merge.png)
    - Or in the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), open the Management center, navigate to the **Overview** in the General section, then select the alert box.

        ![Screenshot of the merge account window in the classic Microsoft Purview governance portal.](media/merge-domain/actual-governance-portal-merge-menu.png)

    Note

    - If a merge is currently in progress within the tenant, then the **Submit request** pop-up and alert box won't appear.
    - If the logged-in user doesn't have the proper permissions to request a merge, the **Submit request** pop-up and alert box won't appear.
3. Specify categories for the merge filter, and select whether you want to allow auto-resolve for conflicts in that category.
4. Select **Submit**.
5. The request is sent through an approval process where a [Purview Administrator](data-governance-roles-permissions#tenant-level-role-groups) needs to approve the request.
6. After approval, an assessment will run to confirm if there are any conflicts or limitations, and if the assessment is successful, the merge process will begin.
7. You can monitor the merge process from the report page.

Important

Failed merges start the cleanup process to revert everything back to its previous state.

### Merge filter

Whenever you merge an account, you can select which objects to migrate and which objects to exclude. In many cases, the filter impacts objects in its own category. However, there are potential behavior changes when you unselect some objects that might apply to associated objects. Some of these categories and the associated behavior changes are listed below:

| Unselected category | Behavior change |
| --- | --- |
| Contact assignment | If unselected, contact assignments configured to glossary terms or assets are removed. |
| Credential | If unselected, scans that use credentials to scan data sources aren't migrated. |
| Custom classification rule | If unselected, scans that applied custom classification rules aren't migrated. |
| Custom scan rule set | If unselected, scans that use applied custom scan rule sets aren't migrated. |
| Custom type | If unselected: - All custom type assets aren't migrated- All relationships for custom types and affected assets aren't migrated.- All classification instances of custom types attached to glossary terms or assets aren't migrated. - Managed attributes attached to glossary terms or assets are removed. |
| Glossary | If unselected, workflows applied to glossary or glossary term aren't migrated, and assets won't have associated glossaries. |
| Key vault connection | If unselected, scans that use key vault credentials to scan data sources aren't migrated. |
| Managed virtual network | If unselected, scans that use managed virtual network to scan data sources aren't migrated. |
| Self-hosted integration runtime | If unselected, scans that use a self-hosted integration runtime to scan data sources aren't migrated. |
| User assigned managed identity | If unselected, scans that use a user assigned managed identity to scan data sources aren't migrated |
| Resource set rule | If unselected, future assets scanned will have no resource set rule applied util users configure new resource set rules in the primary account. |
| Contact assignment | If unselected, contact assignments configured to assets and glossary terms are removed. |

## Approval for account merges

If the merge is requested from the secondary account, it needs to be approved by a Purview Administrator before proceeding with the merge. [Purview Administrators](data-governance-roles-permissions#tenant-level-role-groups) receive an email notification to approve the merge request. Alternatively, the merge request can be approved within primary account's Microsoft Purview portal.

Important

If the outlook account and Microsoft Purview accounts are in different tenants, approving from the email might fail. In this case, use the Microsoft Purview portal to approve.

1. Open primary account's Microsoft Purview portal.
2. Depending on which portal you're using:

    - If you're using [**the Microsoft Purview governance portal**](https://web.purview.azure.com/resource/):
        1. Open the Management center
        2. Select **Request and approvals** in the Workflow section.
    - If you're using the [**Microsoft Purview portal**](https://purview.microsoft.com):
        1. open Workflows solution card
        2. select **Requests and approvals**.

    ![Screenshot of the requests and approvals page, showing a merge account request.](media/merge-domain/requests-and-approval.png)
3. Select the request.
4. Choose your response and select **Confirm**.

    ![Screenshot of the merge request response form.](media/merge-domain/request-response.png)

## Assess conflicts and limitations

Before you run a merge, Microsoft Purview will assess a secondary account to see if it meets the prerequisites for merging with the primary account. If conflicts/limitations are detected and validation fails, manual intervention is required to proceed with the merge. After assessment, you'll have a report of any conflicts, and you can use our conflicts and resolutions to help resolve them.

### Auto-resolve

During the Account Merge process, if the auto-resolve rule is set for a category, the system will automatically resolve any conflicts encountered according to the rule. Currently, only the **skip** rule is supported, which means the object causing the conflict is skipped and not moved from the secondary account to the primary account. Any other objects that depend on this object will also be skipped.

For example: If an auto-resolve rule is set for the **Glossary** category, and a Glossary term encounters a conflict, the system will automatically skip the merge of that term, and also skip the merge of any of that term's children.

Any conflicts encountered when auto-resolve is enabled won't be shown as errors in the assessment or merge process, because they'll be automatically resolved according to the rule.

### Assessment only

You can submit an account for a merge assessment without merging it, to check for any conflicts.

To run an assessment from your primary account:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. To assess an existing account for merging, if you're using the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), open the Management center, navigate to the **Overview** in the General section. If you're using the [Microsoft Purview portal](https://purview.microsoft.com), open Settings solution card, select **Account** and then select **Select account** in the alert box.

    ![Screenshot of the merge account menu in the classic Microsoft Purview governance portal with assess only selected.](media/merge-domain/governance-portal-merge-menu.png)
3. Select an account to assess.
4. Select the drop-down on the **Assess and merge** button and select **Assess only**. Only an assessment is run and the merge process won't start afterwards, regardless of the assessment result.

    ![Screenshot of assess and merge button dropdown showing the assess only option.](media/merge-domain/assess-only.png)

To run an assessment from your secondary account:

1. Select the dropdown in the pop-up and select **Submit assess only request**.

    ![Screenshot of the submit assess only option in the Microsoft Purview portal merge window.](media/merge-domain/submit-assess-only-request.png)

After assessment, you'll have a report of any conflicts, and you can use our conflicts and resolutions to help resolve them.

### Conflicts and resolutions

Tip

For many conflicts, three potential options to resolve the issue are:

1. Remove the conflicting asset from either the primary or secondary account.
2. Choose to filter out that asset category during merge.
3. Select auto-resolve to skip migration for conflicting assets.

Here's a table of conflicts and their possible resolutions:

| Conflict | Potential resolution |
| --- | --- |
| Asset with the same qualified name exists in both the primary and secondary accounts. | There are a few options:- Remove the conflicting asset from either primary or secondary account- Choose to filter out the assets category- Select auto-resolve to skip migration when initiating a merge. |
| Glossary with the same name exists in both the primary and secondary accounts. | [Remove the conflict glossary](how-to-create-manage-glossary#manage-or-delete-a-glossary) from either the primary or secondary account or filter out the glossary category during merge. |
| Glossary term with the same qualified name exists in both the primary and secondary accounts. | [Remove the conflict glossary term](how-to-create-manage-glossary-term) from either the primary or secondary account. |
| Term template with the same name exists in both the primary and secondary accounts. | [Remove the conflict term template](how-to-manage-term-templates) from either the primary or secondary account. |
| Classification rule with the same name exists in both the primary and secondary accounts. | [Remove the conflict classification rule](data-map-classification-custom#edit-or-delete-a-custom-classification) from either the primary or secondary account. |
| Workflow with the same name exists in both the primary and secondary account. | Remove the conflict workflow from either the primary or secondary account. |
| Key vault connection with the same name exists in both the primary and secondary accounts. | [Remove the conflict key vault connection](data-map-data-scan-credentials#manage-your-key-vault-connections) from either the primary or secondary account. |
| Credential with the same name exists in both the primary and secondary accounts. | Remove the conflict credential from either the primary or secondary account. |
| Data source with the same data source name registered in both the primary and secondary accounts. | Unregister the conflict data source from either the primary or secondary account. |
| The same data source registered in both the primary and secondary account. | Unregister the conflict data source from either the primary or secondary account. |
| Data policy with the same policy name exists in both the primary and secondary accounts. | Remove the conflict policy from either the primary or secondary account: [DevOps policy](how-to-policies-devops-authoring-generic#delete-a-devops-policy), [data owner policy](how-to-policies-data-owner-authoring-generic#update-or-delete-a-policy), [self-service policy](how-to-delete-self-service-data-access-policy). |
| Scan rule set with the same name exists in both the primary and secondary accounts. | Remove the conflict scan rule set from either the primary or secondary account. |
| The same contact assignment exists in both the primary and secondary accounts. | Remove the conflict contact assignment from either the primary or secondary account. |
| Secondary account has a glossary named 'Glossary' and another glossary named 'Glossary-{secondary account name}' | Remove either 'Glossary' or 'Glossary-{secondary account name}' from the secondary account. |
| Secondary account has a glossary named 'Glossary' and primary account has a glossary named 'Glossary-{secondary account name}' | Remove 'Glossary' from secondary account or remove 'Glossary-{secondary account name}' from the primary account. |
| Collections with the same name (not display name) exists in both the primary and secondary accounts. | Remove the conflicting collection from either the secondary account or the primary account. |

## View merge and assessment reports

You can track the merge progress in real time during the merging process. To view merge report, users need to be a member of [Purview Administrator](data-governance-roles-permissions#tenant-level-role-groups) role group.

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the Data Map and select **Monitoring**.
3. The merge reports are located on the **Account merging** tab.
4. Select any account name to see full information about its merge or assessment. Select the account name again to collapse its details and see the full account list.

On the report page, you can see the merge statistics summaries:

- Total accounts: Number of accounts that have attempted to merge
- Merging in progress: Accounts currently undergoing merging
- Completed merges: accounts that have successfully merged
- Failed merges: accounts that failed to merge

For any completed assessment, you can rerun an assessment, or rerun an assessment and merge, by selecting \*\*Rerun assessment the assessment details.

### Merge and assessment summary

On the account merging page, select an account, and you can view the merge or assessment summary and the detailed progress for that account.

- Assessment: the step that identifies conflicts and limitations between the primary and secondary accounts. 
    Note

    The discovered conflicts and limitations are blocking the merge from proceeding. You must resolve all of them before selecting **Rerun**.
- Migration: the step that copies the objects from the secondary account to the primary account 
    Note

    - Migrated objects in the primary account are invisible, and their associated functions are disabled during this step. For example, scan schedules are disabled in the primary account during migration and will be enabled before merge complete.
    - Since both the primary and secondary accounts remain operational during the merge, there might be new conflicts and limitations. In such cases, migration will fail and automatic cleanup be triggered to roll back the state of the primary account back to its state before the merge.
- Cleanup: the step that is automatically triggered to clean up migrated objects from the primary account in case the prior step **Migration** fails.
- PostMigration: the step involves preparation work before merge completes.

You can also view detailed merge progress at object category level under a step (Assessment/Migration/PostMigration/Cleanup).

![Screenshot of the detailed merge summary.](media/merge-domain/detailed-merge-progress.png)

Tip

Objects that were filtered to not be merged will show as **Skipped** in the report.

You can view issues details by selecting **View details**. It lists all conflicts and limitations detected during the assessment, as seen in this example:

![Screenshot of the details for the Assessment step during merge.](media/merge-domain/assessment-step-details.png)

Use filters to examine conflicts and limitations within selected categories.

### Download report

You can download all conflict details for any failed assessment.

1. Go to **Data Map** -&gt; **Monitoring** -&gt; **Account merging**.
2. Select the secondary account's assessment.
3. Select the link in the **Issues** column.
4. Select **Download all issues** to download the conflict detail report that has **Description**, **Object category**, **Resolution**, and **Type** columns.

Tip

Objects that were filtered to not be merged will show as **Skipped** in the report.

## After merge completion

After the merge has successfully completed, a new domain will appear in the primary account. It could take a few minutes before the domain appears. Its display name is the root collection's friendly name of the secondary account. This contains all the domain level data migrated from the secondary account.

Next, you should switch over your managed identity connections from your secondary to your primary account using the managed identity switchover process.

After merger completion, the merged account still incurs billing. To prevent billing through the merged account, you can either:

- Delete the account, or
- Deactivate the account.

### Hard deletion of merged secondary account

Hard delete the Purview account will also delete System Assigned Managed Identity associated with the secondary account. To ensure your scans and resources will connect after deletion of the secondary account, you can use the managed identity switchover process to migrate your resources to the primary account's managed identity.

1. Open the [Azure portal](https://portal.azure.com) and select your Microsoft Purview account.
2. Select the **Delete** button and confirm the request.
3. Wait for the deletion to successfully complete.

After hard deleting the account:

- Migrated scans that use secondary account's system assigned managed identity to access data source won't work in the Primary account.
- Migrated key vault connections that use secondary account's system assigned managed identity to access key vaults won't work in the Primary account.

### Deactivate merged secondary account

If you want to stop billing on your secondary account, or you want to use secondary account's system assigned managed identity to access data sources and key vaults in the primary account, you can choose to deactivate the secondary account after merge complete. After the account is deactivated, the data plane operations for this account will be blocked and billing will stop. To switch your sources and scans to the primary managed identity, use the managed identity switchover process.

Caution

Once an account is deactivated, it can't be reactivated.

1. Open secondary account's Microsoft Purview portal.
2. Open Data Map and select **Monitoring**.
3. Select the **Account merging** tab.
4. Select **Deactivate**.

![Screenshot of option to deactivate a merged account.](media/merge-domain/deactivate-secondary-account.png)

## Managed identity switchover

When a secondary account is merged into the tenant-level account, switching your managed identity to the new tenant account is a required step to use the self-hosted integration runtime (SHIR), and is still highly recommended even if you're not. Once the secondary account is deleted, any scans or key vaults that use its managed identity will fail.

To switch your scans and resources from your secondary accounts' managed identity to your primary account's managed identity, follow the steps below. Users must hold the [Domain admin role](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections) in order to perform these functions.

1. Ensure that your primary/tenant-level Microsoft Purview account's managed identity has access to the migrated sources and connections.
2. You can start the switchover from:
    1. The domain overview in your secondary account
        1. If your secondary account was using its own managed identity, on the domain overview page there's a **Switch managed identity button**. Select it.
        2. Select **Confirm**
        3. Once the switchover is completed, you receive a notification.
    2. On the create/edit scan page of your secondary account
        1. Once a merge has been completed, on the secondary account's scan pages there's a notification that asks you to confirm switching your managed identity.
        2. Select **Confirm**
        3. Once the switchover is completed, you receive a notification.
    3. On the create/edit key vault connection page in your secondary account
        1. Once a merge has been completed, on the secondary account's key vault connection page there's a notification that asks you to confirm switching your managed identity.
        2. Select **Confirm**
        3. Once the switchover is completed, you receive a notification.

## Billing

After merge completion, billing for the secondary account will be consolidated with the primary account and will be charged to the primary account's subscription. However, until you deactivate the secondary account, its billing will still be applicable to its subscription.

Tip

Once you've merged your secondary account, deactivate and then delete it to reduce billing.