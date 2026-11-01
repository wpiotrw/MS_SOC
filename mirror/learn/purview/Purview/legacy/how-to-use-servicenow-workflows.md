---
layout: Conceptual
title: Connect to ServiceNow in workflows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-use-servicenow-workflows
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to connect to your ServiceNow instance in Microsoft Purview workflows to manage records.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2025-02-24T00:00:00.0000000Z
ms.custom: template-how-to
locale: en-us
document_id: 52a6fe05-6107-2d7a-50a7-21f2d69459ef
document_version_independent_id: 52a6fe05-6107-2d7a-50a7-21f2d69459ef
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-use-servicenow-workflows.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-use-servicenow-workflows
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-use-servicenow-workflows.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
platformId: 957286fe-fa17-0c32-ac64-52f2fe70bfd6
---

# Connect to ServiceNow in workflows | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

You can use ServiceNow actions in Microsoft Purview workflows to manage and update your ServiceNow records during your data catalog and data governance workflows.

For a list of all available workflow actions, see our [workflow actions page](../how-to-use-workflow-connectors). To connect to your ServiceNow instance, follow the instructions below.

## Set up authentication

Microsoft Purview uses Azure Key Vault to securely store the credentials it uses to connect to other services. Before we can connect to ServiceNow we need to create our ServiceNow credential in the Azure Key vault. Follow these steps:

1. If you don't have an Azure Key Vault, [you can follow this documentation to create one](/en-us/azure/key-vault/general/quick-create-portal).
2. [Create a secret in your key vault](/en-us/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault). The value will be your ServiceNow basic authentication password.
3. [Grant Microsoft Purview access to your Azure Key Vault](../data-map-data-scan-credentials#grant-microsoft-purview-access-to-your-azure-key-vault).
4. [Create a connection in Microsoft Purview to your Azure Key Vault](../data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
5. [Create a new basic authentication credential in Microsoft Purview](../data-map-data-scan-credentials#create-a-new-credential), providing your ServiceNow username and your key vault secret.

Now we have all the authentication pieces in place to connect to your ServiceNow instance.

## Connect to ServiceNow

To access to your ServiceNow instance from Microsoft Purview workflows, first we'll create a connection. This allows Microsoft Purview to authenticate with ServiceNow.

Microsoft Purview uses basic auth credentials to connect to ServiceNow.

1. In the Microsoft Purview governance portal, select the **Management** menu, and then select **Connections**.

    ![Screenshot of connections button in the management menu.](../media/how-to-use-servicenow-workflows/select-connections.png)
2. Select the **+ New** button to create a new connection.
3. Select the **ServiceNow** data source.
4. Name your connection, select the credential you created when you set up authentication, and provide your ServiceNow instance in this format:

    `<instance>.service-now.com`

    ![Screenshot of a new ServiceNow connection with the instance and credential provided.](../media/how-to-use-servicenow-workflows/new-connection.png)
5. Select **Save**

## Create ServiceNow action

When you're authoring any workflow (for example an [approval workflow for business terms](../how-to-workflow-business-terms-approval)), you can add a ServiceNow action by following these steps.

1. Add an action to your workflow by selecting the **+** button on the arrow between actions, select the **Add an action** button, or the **+ New Step** button at the end of the flow. Where you add the action is where it will be executed in the workflow.

    [![Screenshot of a workflow, highlighting the various buttons that can be used to add an action.](../media/how-to-use-servicenow-workflows/add-action.png)](../media/how-to-use-servicenow-workflows/add-action.png#lightbox)
2. In the **Choose an action** menu, select **ServiceNow**.

    ![Screenshot of the choose an action menu, with the ServiceNow tab selected.](../media/how-to-use-servicenow-workflows/select-servicenow.png)
3. Select the ServiceNow action you'd like to use, and fill out the parameters. For more information about each action, see the available ServiceNow actions list.
4. Select **Save** to save your additions to the workflow.

## Available actions

| Connector Type | Functionality | Parameters | Customizable | Workflow templates |
| --- | --- | --- | --- | --- |
| Create record | Create a record for a ServiceNow object type. | -Connection (your ServiceNow connection)  -Record type  -Record body  -Display system references toggle  -Exclude reference links toggle | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Delete record | Delete a record for a ServiceNow object type. | -Connection (your ServiceNow connection)  -Record type  -System ID | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Get record | Get a record for a ServiceNow object type. | -Connection (your ServiceNow connection)  -Record type  -System ID  -Display system references toggle  -Exclude reference links toggle | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Get record types | List available record types. | -Connection (your ServiceNow connection) | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| List records | Get records of a ServiceNow object type. | -Connection (your ServiceNow connection)  -Record type  -Display system references toggle  -Exclude reference links toggle  -Query  -Limit (default is 10000)  -Offset | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |
| Update record | Updates a record for a ServiceNow object type. | -Connection (your ServiceNow connection)  -Record type  -System ID -Record body  -Display system references toggle  -Exclude reference links toggle | - Renamable: Yes  - Deletable: Yes  - Multiple per workflow | All workflows templates |