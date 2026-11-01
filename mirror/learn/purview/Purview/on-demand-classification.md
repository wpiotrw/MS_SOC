---
layout: Conceptual
title: On-demand classification | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/on-demand-classification
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-10-14T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1030
search.appverid:
- MET150
description: Learn how to scan historical data using On-demand classification.
ai-usage: ai-assisted
locale: en-us
document_id: fe715167-244a-4fc1-571a-66431f3c3fd7
document_version_independent_id: fe715167-244a-4fc1-571a-66431f3c3fd7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/on-demand-classification.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: on-demand-classification
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/on-demand-classification.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: fd7d6017-b6e6-c445-139d-d435aca2e305
---

# On-demand classification | Microsoft Learn

Microsoft Purview on-demand classification identifies and classifies sensitive content in historical data stored in SharePoint, OneDrive, and endpoints. On-demand classification extends the classification capabilities to files that aren't classified or modified for a long time, files that are never classified, or files that need updated classification on previously classified files.

On-demand classification updates classification results; matching policies determine any resulting actions. For SharePoint and OneDrive, updated results can trigger active policies, including policies that apply or remove sensitivity labels. On-demand classification isn't an auto-labeling simulation.

To decide whether existing files need updated classification or only policy reevaluation, see [Auto-labeling classification and simulation concepts](auto-label-classification-simulation). Existing, correct classifications don't need to be refreshed for every auto-labeling policy change.

On-demand classification taken with [Information Protection’s continuous classification](information-protection) brings a two-pronged approach to keeping sensitive items aligned with your organization's latest security policies.

By using on-demand classification, organizations can:

- Extend protection to previously unclassified or inactive files, increasing overall coverage.
- Strengthen data protection across your environment without relying on end-user actions.
- Reduce the risk of AI tools surfacing unlabeled or unprotected information. Do it all natively, without exporting your data or relying on fragmented tools.

## SKU and subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## Billing

This feature uses pay-as-you-go billing or per-user licensing for Microsoft Purview capabilities or both. To help you understand and manage your usage, Microsoft Purview provides a **Usage center** in the Microsoft Purview portal. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage). To learn more about Purview billing, see [Purview billing models.](purview-billing-models).

Note

The actual billed amount may be lower than the estimated cost if some items or locations are skipped during the scan. Items can be skipped if they are empty files (excluded to avoid unnecessary billing), if the scan is canceled, or if the subscription expires before completion. Locations may be skipped if another scan is already running on the same location at the same time.

## Permissions

To run a scan, you must be a member of the following role group:

- Compliance Administrator

To view classification results, you must be a member of one of these role groups:

- Content Explorer Content Viewer
- Content Explorer List Viewer

## Create an on-demand classification scan

Before starting classification for SharePoint or OneDrive, review the scan scope, estimated charges, and active policies that might act on the updated results. Check that the file date range and selected classifiers cover the historical files you intend to classify. A policy you're testing can remain in simulation while other active policies act on those files.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Data loss prevention** &gt; **Classifiers** &gt; **On-demand classification** or **Information Protection** &gt; **Classifiers** &gt; **On-demand classification**.
3. Select **New scan**.
4. Follow the instructions in the wizard. During this process, you define the following settings:

    - Name and description
    - Scope and location - You can choose to scan all SharePoint sites and OneDrive accounts, only specific ones, or skip certain sites and accounts from the scan. For endpoint devices, you can scope the scan by users.
    - Classifiers to scan for
    - File last modified date range you want to scan
    - File extensions you want to scan

    After you complete the wizard, the estimation process begins. The estimation duration depends on the scope of the scan.

    Note

    By default, the scan includes all items created or modified within the past year, across all supported file extensions. It also includes every available classifier configured in your tenant. If you choose to scan for specific classifiers, you can select up to 50 at a time.
5. From the **On-demand classification** list view, select the scan you created.
6. Select **View estimation**.

    Note

    After reviewing the estimates, you can edit the scan to narrow or expand the scope. Select **Edit scan** and rerun the estimation scan.
7. Select **Start classification.**

## Analyze on-demand classification results

1. From **On-demand classification**, select a scan from the list.
2. Select **View estimation**.
3. On the **Estimation overview** tab, review scan results, including progress, items found, and estimated cost. To cancel in-progress scans, select **Cancel Scan**.
4. On the **Items for review** tab, review specific items found during the scan. You can filter and export the result.

Devices that don't respond are ones that don't send endpoint telemetry signals for over 72 hours. Devices with expired scan validity don't have a valid scan in the last 72 hours.

## Additional considerations

- Classification can start up to 30 days after estimation, but minimizing the gap ensures greater accuracy in final counts and costs.
- Tenants using EDM classifiers should be aware that On-Demand Classification scans (including estimation and classification) rescan previously classified files, which can increase overall scan costs. To mitigate this impact, tenants can exclude the EDM classifier from the scan scope.
- Impact of classifier selection on scan cost: The classifiers selected for an on‑demand scan influence how many files are identified for processing. Scan cost is determined by the total number of files scanned—not the number of classifiers. Selecting a broader set of classifiers may increase the number of files in scope and raise overall cost. However, this approach ensures files are assessed against all relevant classifiers in a single scan, reducing the risk of missed sensitive data and limiting the need for additional scans later.

Applies to SharePoint and OneDrive

- Each scan can process up to 150,000 locations and 100 million files. The system enforces these limits based on scan estimation results.

    Note

    In On-Demand Classification estimation scans (simulation), you see a difference between the number of matched locations and the number of users or accounts included in the scan scope. Simulation results are based on mailbox locations rather than unique users. A single user can have multiple mailboxes (for example, a primary mailbox along with archive or system mailboxes), and each mailbox is treated as a separate location during scanning. As a result, the total number of matched locations can exceed the number of users in scope, even when the scan is correctly applied at the user level.
- If you select specific classifiers during a scan, only those classifiers have their classification results updated for the scanned files. Other classifiers present in the files might remain unevaluated and might not trigger their associated policies.
- If a location is in scope of multiple active scans, only one scan processes it successfully and marks it skipped for others.
- Each file, once scanned, is evaluated against Data Loss Prevention (DLP), Information Protection (MIP), Data Lifecycle Management (DLM), and Insider Risk Management (IRM) policies, triggering appropriate actions as per matching policies.
- Content Explorer updates within seven days of scanning to reflect newly classified content.
- Adaptive scopes for SharePoint on-demand classification let administrators define scan scope dynamically based on site attributes (such as URL, name, or metadata) instead of selecting sites manually. The scan automatically includes all sites that match the criteria and updates as sites change, enabling scalable, accurate coverage with minimal manual maintenance. To learn more, see [Adaptive scopes](purview-adaptive-scopes).
- Administrative units (AUs) for SharePoint on-demand classification let organizations scope and manage scans within defined administrative boundaries, enabling delegated administration across large or distributed environments. Administrators can create and manage scans only for sites within their assigned AUs, and access to scan configuration and results is limited to AU-scoped admins. This supports least-privilege access, simplifies ownership across regions or departments, and ensures alignment with existing governance in Microsoft Purview. For more information, see [Administrative units in Microsoft Purview](purview-admin-units).

Applies to Windows 10/11 endpoints

- Ensure that the machine has a minimum four virtual processors and a minimum of 4,096 MB memory.
- Each device is limited to 2 GB of data discovery bandwidth per rolling 24-hour period (independent of DLP). Scanning pauses once the limit is reached and resumes after 24 hours.
- Only devices that successfully complete estimation are included in classification.
- In addition to DLP-excluded paths, certain system folders are automatically excluded from data discovery.

    `%WinDir%``%ProgramFiles%``%ProgramFiles(x86)%``%SystemDrive%\Windows.old``%SystemDrive%\Users\*(1)\Application Data``%SystemDrive%\Users\*(1)\AppData\Local\Application Data``%SystemDrive%\Users\*(1)\Local Settings\Application Data``%SystemDrive%\Documents and Settings\*(1)\Application Data``%SystemDrive%\Documents and Settings\*(1)\AppData\Local\Application Data``%SystemDrive%\Documents and Settings\*(1)\Local Settings\Application Data``%ProgramData%\Application Data``%ProgramData%\Microsoft\Windows\WER`\