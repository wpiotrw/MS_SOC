---
layout: Conceptual
title: Troubleshoot Power BI tenant scans in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-power-bi-tenant-troubleshoot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2025-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to troubleshoot Power BI tenant scans in Microsoft Purview.
locale: en-us
document_id: 3e052391-2cae-2675-836e-74caebfad199
document_version_independent_id: 3e052391-2cae-2675-836e-74caebfad199
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-power-bi-tenant-troubleshoot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-power-bi-tenant-troubleshoot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-power-bi-tenant-troubleshoot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f2ab218a-5d6f-c747-560b-53299cc8d5a4
---

# Troubleshoot Power BI tenant scans in Microsoft Purview | Microsoft Learn

This article explores common troubleshooting methods for scanning Power BI tenants in [Microsoft Purview](purview).

## Supported scenarios for Power BI scans

### Same-tenant

| **Scenarios** | **Microsoft Purview public access allowed/denied** | **Power BI public access allowed /denied** | **Runtime option** | **Authentication option** | **Deployment checklist** |
| --- | --- | --- | --- | --- | --- |
| Public access with Azure IR | Allowed | Allowed | Azure Runtime | Microsoft Purview Managed Identity | [Review deployment checklist](register-scan-power-bi-tenant#deployment-checklist) |
| Public access with self-hosted IR | Allowed | Allowed | Self-hosted runtime | Delegated authentication / Service principal | [Review deployment checklist](register-scan-power-bi-tenant#deployment-checklist) |
| Private access | Allowed | Denied | Self-hosted runtime | Delegated authentication / Service principal | [Review deployment checklist](register-scan-power-bi-tenant#deployment-checklist) |
| Private access | Denied | Allowed | Self-hosted runtime | Delegated authentication / Service principal | [Review deployment checklist](register-scan-power-bi-tenant#deployment-checklist) |
| Private access | Denied | Denied | Self-hosted runtime | Delegated authentication / Service principal | [Review deployment checklist](register-scan-power-bi-tenant#deployment-checklist) |

### Cross-tenant

| **Scenarios** | **Microsoft Purview public access allowed/denied** | **Power BI public access allowed /denied** | **Runtime option** | **Authentication option** | **Deployment checklist** |
| --- | --- | --- | --- | --- | --- |
| Public access with Azure IR | Allowed | Allowed | Azure runtime | Delegated Authentication | [Deployment checklist](register-scan-power-bi-tenant-cross-tenant#deployment-checklist) |
| Public access with Self-hosted IR | Allowed | Allowed | Self-hosted runtime | Delegated authentication / Service principal | [Deployment checklist](register-scan-power-bi-tenant-cross-tenant#deployment-checklist) |

## Troubleshooting tips

If delegated auth is used:

- Check your key vault. Make sure there are no typos in the password.
- Assign proper [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) to Power BI administrator user.
- Validate if user is assigned to Power BI Administrator role.
- If user is recently created, make sure password is reset successfully and user can successfully initiate the session.

## My schema is not showing up after scanning

It can take some time for schema to finish the scanning and ingestion process, depending on the size of your Power BI Tenant. Currently if you have a large PowerBI tenant, this process could take a few hours.

## Error code: Test connection failed - AASDST50079

- **Message**: `Failed to get access token with given credential to access Power BI tenant. Authentication type PowerBIDelegated Message: AASDST50079 Due to a configuration change made by your administrator or because you moved to a new location, you must enroll in multi-factor authentication.`
- **Cause**: Authentication is interrupted, due multi-factor authentication requirement for the Power BI admin user.
- **Recommendation**: Disable multi-factor authentication requirement and exclude user from conditional access policies. Login with the user to Power BI dashboard to validate if user can successfully login to the application.

## Error code: Test connection failed - AASTS70002

- **Message**: `Failed to access token with given credential to access Power BI tenant. Authentication type: PowerBiDelegated Message AASTS70002: The request body must contain the following parameter: 'client_assertion' or 'client_secret'.`
- **Cause**: If Delegated Authentication is used, the problem could be a misconfiguration on the app registration.
- **Recommendation**: Review Power BI deployment checklist based on your scenario.

## Error code: Test connection failed - Detailed metadata

- **Message**: `Failed to enable the PowerBI administrator API to fetch basic metadata and lineage.`
- **Cause**: **Allow service principals to use read-only Power BI admin APIs** is disabled.
- **Recommendation**: Under Power BI Admin portal, enable **Allow service principals to use read-only Power BI admin APIs**.

## Issue: Test Connection succeeded. No assets discovered.

- **Message**: N/A
- **Cause**: This problem can occur in same-tenant or cross-tenant scenarios, due problem with networking or authentication issues.
- **Recommendation**:

    - If Delegated Authentication is used, validate Power BI Admin user sign in logs in Microsoft Entra logs to make sure user sign in is successful. Login with the user to Power BI dashboard to validate if user can successfully login to the application.
    - Review your network configurations. Private endpoint is required for **both** Power BI tenant and Purview account, if one of these services (Power BI tenant or Microsoft Purview) is configured to block public access.