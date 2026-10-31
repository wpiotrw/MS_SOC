---
layout: Conceptual
title: Upgrade the Microsoft Purview Information Protection scanner | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/upgrade-scanner-migrate
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: 
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-06-28T00:00:00.0000000Z
audience: Admin
ms.topic: upgrade-and-migration-article
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
description: How to upgrade the Microsoft Purview Information Protection scanner from 2.x (Azure Information Protection client) or 3.x (information protection client)
locale: en-us
document_id: ba22e22e-2eaf-8816-a812-2fe0f2a0382e
document_version_independent_id: ba22e22e-2eaf-8816-a812-2fe0f2a0382e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/upgrade-scanner-migrate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: upgrade-scanner-migrate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/upgrade-scanner-migrate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/c900d0ba-7127-44a2-8ba8-afc4f786377d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/179dea74-32c0-4804-9e75-383800f5d15e
platformId: 85856712-90da-3b9d-dad0-505e0c18bed2
---

# Upgrade the Microsoft Purview Information Protection scanner | Microsoft Learn

Use the following instructions to upgrade the [information protection scanner](deploy-scanner) to the latest version from the [Microsoft Purview Information Protection client](information-protection-client):

- From the Azure Information Protection unified labeling client (2.x)
- From a previous version of the scanner from the [Microsoft Purview Information Protection client](information-protection-client) (3.x)

For the latest release information and support timelines for each version, see [Microsoft Purview Information Protection client - Release management and supportability](information-protection-client).

## Upgrade the scanner from the Azure Information Protection client (version 2.x)

Important

Upgrading the Microsoft Purview Information Protection scanner from client version 2.x to version 3.x requires additional and specific steps because service names and other components are renamed.

To avoid misconfigurations that can result in the scanner no longer working, make sure you follow each step that follows.

1. On any scanner node in the cluster, run the following command and make a note of the SQL database name and cluster:

    ```PowerShell
    Get-AIPScannerConfiguration
    ```
2. Get ready to install the new version of the scanner on each node in the cluster by stopping the scanner service:

    ```PowerShell
    Net Stop AIPScanner
    ```
3. Uninstall the existing scanner service:

    ```PowerShell
    Uninstall-AIPScanner
    ```
4. Restart the Windows server computer to completely remove the service.
5. Uninstall version 2.x of the Azure Information Protection unified labeling client.
6. [Install version 3.x of the Microsoft Purview Information Protection client](information-protection-client#install-or-upgrade-the-information-protection-client)
7. Install the scanner from the information protection client:

    ```PowerShell
    Install-Scanner -SqlServerInstance  <SQL\InstanceName>  -Cluster <cluster-name>
    ```

    For example, to upgrade the scanner that uses the SQL Server instance named SCANNER that runs on the server named SQLSERVER1 and uses the cluster name of EU as the database for the scanner configuration:

    ```PowerShell
    Install-Scanner -SqlServerInstance SQLSERVER1\SCANNER -Cluster EU
    ```

    For more details and other examples that include using the SQL Server default instance and SQL Server Express, see the examples from [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner#examples).
8. Stop the scanner service:

    ```PowerShell
    Net Stop MIPScanner 
    ```
9. Update the scanner database: On one scanner node, run the following command:

    ```PowerShell
    Update-ScannerDatabase
    ```
10. Start the scanner service on the Windows server computer.
11. For each node in the cluster, start the scanner service:

    ```PowerShell
    Net Start MIPScanner
    ```

The scanner is now upgraded for the Microsoft Purview Information Protection client and ready to resume any scanning jobs that are configured.

## Upgrade a previous version of the scanner from the information protection client (version 3.x)

Use the following instructions to upgrade the scanner from an earlier version from the Microsoft Purview Information Protection client (version 3.x).

For example, you're upgrading from a preview version of the Microsoft Purview Information Protection client to a general availability (GA) version. Or, you're upgrading from a GA version of the Microsoft Purview Information Protection client to the latest version of this client.

1. Get ready to install the new version of the scanner on each node in the cluster by stopping the scanner service:

    ```PowerShell
    Net Stop MIPScanner
    ```
2. [Install the latest version of the Microsoft Purview Information Protection client](information-protection-client#install-or-upgrade-the-information-protection-client).
3. Update the scanner database: On one scanner node, run the following command:

    ```PowerShell
    Update-ScannerDatabase
    ```
4. Start the scanner service on the Windows server computer.
5. For each node in the cluster, start the scanner service:

    ```PowerShell
    Net Start MIPScanner
    ```

The scanner is now upgraded to the latest version from the Microsoft Purview Information Protection client and ready to resume any scanning jobs that are configured.