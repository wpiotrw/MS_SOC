---
layout: Conceptual
title: Remove a retention hold from an unlicensed OneDrive site | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/remove-retention-hold-unlicensed-onedrive-site
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use Security & Compliance PowerShell to remove a blocking retention hold from an unlicensed OneDrive for Business site and allow its deletion.
author: prateekbhamri
ms.author: pbhamri
manager: rasrivas
ms.date: 2026-08-17T00:00:00.0000000Z
ai-usage: ai-generated
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1023
locale: en-us
document_id: 91296eae-24d9-f90a-58b4-8dc9f6496980
document_version_independent_id: 91296eae-24d9-f90a-58b4-8dc9f6496980
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/remove-retention-hold-unlicensed-onedrive-site.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: remove-retention-hold-unlicensed-onedrive-site
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/remove-retention-hold-unlicensed-onedrive-site.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 3e1320df-f303-64c8-5009-4d51ea0ee486
---

# Remove a retention hold from an unlicensed OneDrive site | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

This article is for Microsoft Purview administrators who manage unlicensed OneDrive for Business sites. Use the `Fix-PurviewConfig` cmdlet in Security & Compliance PowerShell to force-exclude a specified retention hold from an unlicensed, archived site. Removing the blocking hold allows the site to be deleted when no other non-force-excluded holds apply.

Before you begin, review the account, site, and policy requirements in Prerequisites.

## Prerequisites

Before you begin, make sure you have:

- An account that can connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
- The URL of the unlicensed OneDrive for Business site.
- The GUID of the retention or hold policy to remove. The policy must exist in EOP and apply to the specified site.
- Confirmation that the site owner is unlicensed and the OneDrive site is archived. For more information, see [Manage unlicensed OneDrive user accounts](/en-us/sharepoint/unlicensed-onedrive-accounts).

## Remove the retention hold

The `RemoveHoldFromUnlicencedODBSite` scenario removes the specified hold from the site. Review your organization's retention and legal requirements before you run the cmdlet because removing the blocking hold can allow site deletion.

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Confirm the values that you will use for `SiteUrl` and `PolicyId`.
3. Run the `Fix-PurviewConfig` cmdlet with the following syntax:

    ```text
    Fix-PurviewConfig -Scenario RemoveHoldFromUnlicencedODBSite
        -SiteUrl <String>
        -PolicyId <String>
    ```

    For example:

    ```powershell
    Fix-PurviewConfig -Scenario RemoveHoldFromUnlicencedODBSite `
      -SiteUrl "https://<tenant>-my.sharepoint.com/personal/<user>" `
      -PolicyId "430b7b03-88b7-4ec5-9ae1-736f27bac9c3"
    ```
4. Review the result. A successful operation returns the following fields:

    ```text
    ScenarioName  : DLM_ODB_Remove_Hold_For_Unlicenced_Site
    Description   : Remove hold from unlicenced ODB site.
    Status        : Success
    Comments      : {Successfully removed hold(s) from unlicenced ODB site.}
    CorrelationId : 00000000-0000-0000-0000-000000000000
    ```

    After successful execution, the specified hold is force-excluded. If no other non-force-excluded holds apply, site deletion is allowed.

You can run the command again without changing the result. If the hold is already excluded, the cmdlet reports that the hold has already been removed.

## Resolve validation errors

Use the following table to resolve validation errors returned by the cmdlet.

| Validation error | Action |
| --- | --- |
| `SiteUrl` isn't provided. | Provide the URL of the unlicensed OneDrive for Business site. |
| `SiteUrl` isn't a valid OneDrive for Business URL. | Correct the URL format and run the command again. |
| The specified site isn't present in OneDrive for Business. | Confirm that the site exists and that you entered the correct URL. |
| `PolicyId` isn't provided. | Provide the retention or hold policy GUID. |
| `PolicyId` doesn't exist in EOP. | Confirm the policy ID and run the command again. |
| `PolicyId` isn't a valid GUID. | Provide a valid policy GUID. |
| The hold doesn't apply to the site. | Confirm that the policy applies to the specified site. |
| The site owner is licensed. | Remove the hold only after the site owner is unlicensed. |

## Review validation screenshots

The following screenshots show the validation outcomes from the approved test run. Tenant URLs, user aliases, local file paths, policy identifiers, browser property values, and exception internals are redacted. The cmdlet results and status messages are unchanged.

### Validate the site URL

**Site URL isn't provided**

![Screenshot of the cmdlet result showing that the SiteUrl parameter is required.](media/remove-retention-hold-unlicensed-onedrive-site/site-url-required.png)

**Site URL isn't in a valid OneDrive for Business format**

![Screenshot of the cmdlet result showing that the OneDrive for Business site URL format is invalid.](media/remove-retention-hold-unlicensed-onedrive-site/site-url-invalid.png)

**Site URL isn't present in OneDrive for Business**

![Screenshot of the validation result showing that the specified OneDrive for Business site wasn't found.](media/remove-retention-hold-unlicensed-onedrive-site/site-url-not-found.png)

### Validate the policy ID

**Policy ID isn't provided**

![Screenshot of the cmdlet result showing that the PolicyId parameter is required.](media/remove-retention-hold-unlicensed-onedrive-site/policy-id-required.png)

**Policy ID doesn't exist in EOP**

![Screenshot of the cmdlet result showing that the specified policy ID doesn't exist in EOP.](media/remove-retention-hold-unlicensed-onedrive-site/policy-id-not-found.png)

**Policy ID isn't a valid GUID**

![Screenshot of the cmdlet result showing that the policy ID isn't a valid GUID.](media/remove-retention-hold-unlicensed-onedrive-site/policy-id-invalid.png)

### Validate hold applicability and licensing

**Hold isn't applicable to the site**

![Screenshot of the cmdlet result showing that the specified hold doesn't apply to the site.](media/remove-retention-hold-unlicensed-onedrive-site/hold-not-applicable.png)

**Site owner is licensed**

![Screenshot of the cmdlet result showing that hold removal is skipped for a licensed site owner.](media/remove-retention-hold-unlicensed-onedrive-site/site-owner-licensed.png)

### Verify site-level hold removal

**Before cmdlet execution**

![Screenshot of the site properties before execution showing that a site-level hold is present.](media/remove-retention-hold-unlicensed-onedrive-site/site-level-hold-before.png)

**Successful cmdlet execution**

![Screenshot of the successful cmdlet result for removing a site-level hold from an unlicensed OneDrive site.](media/remove-retention-hold-unlicensed-onedrive-site/site-level-hold-command-success.png)

**After cmdlet execution**

![Screenshot of the site properties after execution showing that the site-level hold is excluded.](media/remove-retention-hold-unlicensed-onedrive-site/site-level-hold-after.png)

### Verify tenant-level hold removal

**Before cmdlet execution**

![Screenshot of the site properties before execution showing that the tenant-level hold isn't stamped in AllWebHolds.](media/remove-retention-hold-unlicensed-onedrive-site/tenant-level-hold-before.png)

**Successful cmdlet execution**

![Screenshot of the successful cmdlet result for removing a tenant-level hold from an unlicensed OneDrive site.](media/remove-retention-hold-unlicensed-onedrive-site/tenant-level-hold-command-success.png)

**After cmdlet execution**

![Screenshot of the site properties after execution showing that the tenant-level hold is excluded.](media/remove-retention-hold-unlicensed-onedrive-site/tenant-level-hold-after.png)

### Verify repeated execution

**Hold is already excluded**

![Screenshot of repeated cmdlet execution showing success followed by a message that the hold no longer applies.](media/remove-retention-hold-unlicensed-onedrive-site/hold-already-excluded.png)