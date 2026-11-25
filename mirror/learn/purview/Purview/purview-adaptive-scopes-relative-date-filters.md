---
layout: Conceptual
title: Use relative date filters in adaptive scopes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes-relative-date-filters
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: amuralidhara
author: anirudhbharadwaj
ms.date: 2026-11-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-adaptive-scopes
ms.collection:
- purview-compliance
ai-usage: ai-assisted
description: Use relative date filters in Microsoft Purview adaptive scopes to target users, Microsoft 365 groups, and SharePoint sites with rolling date ranges.
locale: en-us
document_id: 52541f54-4bfc-7ed6-2321-350212902a82
document_version_independent_id: 52541f54-4bfc-7ed6-2321-350212902a82
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-adaptive-scopes-relative-date-filters.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-adaptive-scopes-relative-date-filters
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-adaptive-scopes-relative-date-filters.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: f6cedf59-57a9-d9a6-687f-c1e91411e4fd
---

# Use relative date filters in adaptive scopes | Microsoft Learn

Relative date filters let you define [adaptive scope](purview-adaptive-scopes) membership by a date relative to the time of evaluation. For example, you can target recently created mailboxes, groups that are more than a year old, or sites whose project completion date falls within the past six months.

Unlike a fixed date, a relative date moves forward without requiring you to edit the query. Use a relative date when you need a rolling range. Keep a fixed date when you need a cohort tied to a specific event, such as all sites created before a migration.

Important

Relative date filters determine which users, groups, or sites belong to a scope. They don't filter individual messages or documents by age, set a retention period, or change when retention starts. Configure those settings separately in the policy that uses the scope.

## Before you begin

You need the permissions and prerequisites for [configuring adaptive scopes](purview-adaptive-scopes#how-to-configure-an-adaptive-scope).

Use the **Advanced query builder** to enter relative date filters. Use OPATH syntax for **Users** and **Microsoft 365 Groups**, and Keyword Query Language (KeyQL) syntax for **SharePoint sites**.

For a custom SharePoint date property, work with your SharePoint administrator to populate the site metadata and map its crawled property to a supported date managed property. The property must represent a date for the site, not a date on an individual document. For background on custom site properties, see [Using Custom SharePoint Site Properties to Apply Microsoft 365 Retention with Adaptive Policy Scopes](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/using-custom-sharepoint-site-properties-to-apply-microsoft-365/ba-p/3133970).

## Supported date properties

### Users and Microsoft 365 Groups

| Property | Date used by the filter |
| --- | --- |
| `WhenCreated` | Creation date of the recipient object. |
| `WhenCreatedUTC` | Creation date of the recipient object, expressed in UTC. |
| `WhenMailboxCreated` | Creation date of the mailbox. This can differ from the creation date of the recipient object. |
| `WhenChanged` | Last modification date of the recipient object. |
| `WhenChangedUTC` | Last modification date of the recipient object, expressed in UTC. |
| `WhenSoftDeleted` | Date the recipient was soft-deleted, when that value is present. |

`WhenChanged` and `WhenChangedUTC` describe changes to the recipient object. They aren't measures of a person's last sign-in or mailbox activity.

A filter on `WhenSoftDeleted` doesn't by itself make a deleted recipient eligible for scope membership. The recipient must also meet the scope's other membership requirements.

For information about recipient properties, see [Filterable properties for recipient filters](/en-us/powershell/exchange/recipientfilter-properties).

### SharePoint sites

| Property | Date used by the filter |
| --- | --- |
| `Created` | Site creation date. |
| `RefinableDate00` through `RefinableDate19` | Custom site dates mapped to these date managed properties, such as a project completion date. |

Use the managed property name in the query, such as `RefinableDate00`. A date stored as text in a property such as `RefinableString00` isn't a supported relative date property.

## Specify a relative date

Use a date-only ISO 8601 duration. The value starts with an uppercase `P`, followed by a whole number and a unit:

| Unit | Meaning | Example |
| --- | --- | --- |
| `Y` | Calendar years | `P1Y`: one year before evaluation. |
| `M` | Calendar months | `P6M`: six months before evaluation. |
| `W` | Weeks of seven days | `P2W`: 14 days before evaluation. |
| `D` | Days | `P30D`: 30 days before evaluation. |

You can combine years, months, and days in that order. For example, `P1Y6M` means one year and six months before evaluation, and `P1Y2M3D` means one year, two months, and three days before evaluation. Use weeks on their own, such as `P2W`, not `P1W3D`.

`P0D` represents the evaluation time. It can provide an upper bound when you want to exclude future dates.

Use uppercase letters and whole, nonnegative numbers. Time components, such as `PT2H` or `P1DT12H`, fractional values, negative values, and expressions such as `30 days` aren't supported.

### How the cutoff date is calculated

The cutoff date moves forward every day, so the scope continues to use the same rolling date range without you changing the query. For example, if the current date is November 1, 2026, `P30D` represents October 2, 2026. On November 2, 2026, it represents October 3, 2026. Scope membership changes dynamically as users, groups, or sites fall inside or outside the query's date range.

Relative dates use UTC. These examples show dates only, but the cutoff includes a time of day rather than always starting at midnight.

Months and years follow the calendar, rather than fixed numbers of days. For example, `P1M` isn't always equivalent to `P30D`. When a target month doesn't have the original day, the cutoff falls on the last valid day of that month.

### Choose a comparison operator

The comparison applies to the property's date, not to its age:

| Meaning | OPATH operator | KeyQL operator |
| --- | --- | --- |
| Later than the cutoff, more recent | `-gt` | `>` |
| On or after the cutoff | `-ge` | `>=` |
| Earlier than the cutoff, older | `-lt` | `<` |
| On or before the cutoff | `-le` | `<=` |

For example, `WhenMailboxCreated -ge 'P30D'` matches creation dates on or after the rolling 30-day cutoff. To match mailboxes older than 30 days, use `WhenMailboxCreated -lt 'P30D'`.

Don't use equality or inequality operators with relative dates: OPATH `-eq` and `-ne`, or KeyQL `=`, `:`, and `<>`. To express a range, combine two comparisons with `-and` in OPATH or `AND` in KeyQL. Relative date ranges using KeyQL `..` syntax aren't supported.

Enclose OPATH duration values in single or double quotes. For KeyQL, use double quotes, as in `Created>="P30D"`, or leave the duration unquoted, as in `Created>=P30D`. The following examples use quoted values.

## Create an adaptive scope with a relative date filter

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), go to **Settings** &gt; **Roles and scopes** &gt; **Adaptive scopes**, and select **+ Create scope**.
2. Follow the prompts to name the scope and select an administrative unit or **Full directory**. SharePoint site scopes require **Full directory**.
3. Select **Users**, **Microsoft 365 Groups**, or **SharePoint sites**.
4. Select **Advanced query builder** and enter a query that uses the appropriate syntax and a supported date property. Use the examples in the next section as starting points.
5. Review and create the scope. Allow time for evaluation, then check its membership before adding it to a policy.

You can also pass the query to the **RawQuery** parameter of [New-AdaptiveScope](/en-us/powershell/module/exchangepowershell/new-adaptivescope) or [Set-AdaptiveScope](/en-us/powershell/module/exchangepowershell/set-adaptivescope) in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

## Examples

These examples define scope membership only. Choose the policy settings separately for your organization's requirements.

### Recently created mailboxes

To create a **Users** scope for mailboxes created on or after the rolling 30-day cutoff:

```text
WhenMailboxCreated -ge 'P30D'
```

You can combine the date filter with other supported conditions. For example, to restrict the same scope to recipients in the Finance department:

```text
(Department -eq 'Finance') -and (WhenMailboxCreated -ge 'P30D')
```

As the cutoff moves forward, mailboxes older than the cutoff no longer match.

### Groups older than one year

To create a **Microsoft 365 Groups** scope for groups whose recipient objects were created more than one year before evaluation:

```text
WhenCreatedUTC -lt 'P1Y'
```

This is an age-based scope. It doesn't identify groups that have been unused for a year.

### Recipient objects between one and two years old

To create a **Users** scope for recipient objects created on or after the two-year cutoff but before the one-year cutoff:

```text
(WhenCreatedUTC -ge 'P2Y') -and (WhenCreatedUTC -lt 'P1Y')
```

The older cutoff is the lower date bound. Reversing these comparisons would produce an empty range.

### SharePoint sites older than two years

To create a **SharePoint sites** scope for sites created more than two years before evaluation:

```text
Created<"P2Y"
```

You can also combine a relative date with other site conditions. For example, to include only modern communication sites created after the six-month cutoff:

```text
SiteTemplate=SITEPAGEPUBLISHING AND Created>"P6M"
```

### Project sites completed within the past six months

Suppose your SharePoint administrator has mapped each project's completion date to `RefinableDate00`. To create a **SharePoint sites** scope for completion dates from six months before evaluation through the evaluation time:

```text
RefinableDate00>="P6M" AND RefinableDate00<="P0D"
```

The upper bound excludes planned completion dates in the future. Verify the mapping and populated values before using this query.

## Validate relative date filters

After creating or updating a scope, use [View adaptive scope membership details](purview-adaptive-scopes#view-adaptive-scope-membership-details) to review added and removed members. You can also use [Get-AdaptiveScopeMembers](/en-us/powershell/module/exchangepowershell/get-adaptivescopemembers).

Adaptive scopes are evaluated periodically, not continuously. Initial membership and membership changes can take up to five days to appear. A recipient or site doesn't enter or leave the displayed member list immediately when it crosses a date cutoff.

### Test a query outside adaptive scopes

Exchange PowerShell filters and SharePoint search don't perform the adaptive scope conversion of ISO 8601 duration values. To [validate an advanced query independently](purview-adaptive-scopes#validate-advanced-queries), replace each duration with an absolute UTC date calculated from one reference time.

For example, after [connecting to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell), you can check the user mailbox portion of the recently created mailboxes example:

```powershell
$referenceTime = [DateTime]::UtcNow
$cutoff = $referenceTime.AddDays(-30).ToString("yyyy-MM-ddTHH:mm:ssZ", [Globalization.CultureInfo]::InvariantCulture)
Get-Mailbox -RecipientTypeDetails UserMailbox -Filter "WhenMailboxCreated -ge '$cutoff'" -ResultSize Unlimited
```

For SharePoint search, use the same approach. For example, at reference time `2026-11-23T12:00:00Z`, test `Created<"P2Y"` by using `Created<"2024-11-23T12:00:00Z"`.

These checks test the property values and query at the chosen time. They don't force an adaptive scope evaluation or guarantee identical membership results. The adaptive scope can evaluate later, and its other membership requirements still apply.

### Troubleshoot unexpected results

| Symptom | What to check |
| --- | --- |
| The query isn't accepted. | Check the scope type, property name, duration format, and comparison operator. Use the advanced query builder, quote OPATH values, and avoid time components and equality operators. |
| Recent objects match when you expected older objects, or the reverse. | Use `<` or `-lt` for dates older than the cutoff, and `>` or `-gt` for dates more recent than the cutoff. Use the inclusive forms when required. |
| A custom site date doesn't produce the expected matches. | Confirm that the site metadata is populated and mapped to the intended `RefinableDate` managed property. |
| A mailbox doesn't match a recipient creation-date filter. | Compare `WhenCreated` or `WhenCreatedUTC` with `WhenMailboxCreated`. Recipient and mailbox creation dates can differ. |
| Membership hasn't changed after a date boundary passes. | Allow time for the next evaluation and for membership details to update. |