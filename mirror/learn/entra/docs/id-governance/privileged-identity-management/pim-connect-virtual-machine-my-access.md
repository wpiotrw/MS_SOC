---
layout: Conceptual
title: Connect to an Azure Virtual Machine from the My Access portal - Microsoft Entra ID Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-connect-virtual-machine-my-access
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: tamimsangrar
ms.author: tamimsangrar
ms.service: entra-id-governance
ms.subservice: privileged-identity-management
manager: dougeby
description: Use the My Access portal to view Azure Virtual Machine access, activate eligible roles, and connect with Microsoft Entra ID authentication.
ms.topic: how-to
ms.date: 2026-11-17T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: e4419421-dcb2-7dda-75b6-19b1f7977e73
document_version_independent_id: e4419421-dcb2-7dda-75b6-19b1f7977e73
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/id-governance/privileged-identity-management/pim-connect-virtual-machine-my-access.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: id-governance/privileged-identity-management/pim-connect-virtual-machine-my-access
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/id-governance/privileged-identity-management/pim-connect-virtual-machine-my-access.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7c01134-b8f3-438c-822d-13471e513908
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/82fff6b2-939d-4e9a-8f9c-d1c41a59749b
platformId: 24f5fd9d-fd0a-bd86-17f1-20cd4f275f82
---

# Connect to an Azure Virtual Machine from the My Access portal - Microsoft Entra ID Governance | Microsoft Learn

Use the My Access portal to view your access to an Azure Virtual Machine, activate eligible role assignments when required, and connect to the Virtual Machine with Microsoft Entra ID authentication. An eligible role assignment lets you request temporary role access for your signed-in identity.

## Prerequisites

Before you begin, confirm your access and ask the resource administrator to verify the connection setup.

### Your access

- Microsoft Entra ID Governance licensing is required for **Resource Connections**. See [Microsoft Entra ID Governance licensing fundamentals](../licensing-fundamentals).
- You need an active or eligible **Virtual Machine Administrator Login** or **Virtual Machine User Login** role assignment for Microsoft Entra sign-in to the virtual machine. An Owner or Contributor **role assignment** alone will not grant the user the ability to sign-in.
- For Azure Bastion, you need read access to the virtual machine, its network interface, and the Bastion resource. You also need read access to the target virtual machine's virtual network when Bastion is deployed in a peered virtual network. Existing active role assignments can provide some of this access within their scopes. Ask your administrator to provide the required access where it is missing, for example through the **Reader** role. If this access isn't already active, you need existing eligible role assignments that cover the required resources and permissions.
- Use a client that meets the [Windows](../../identity/devices/howto-vm-sign-in-azure-ad-windows) or [Linux](../../identity/devices/howto-vm-sign-in-azure-ad-linux) sign-in requirements. Windows virtual machine connectivity doesn't support guest accounts.

### Administrator-managed setup

- The Azure Virtual Machine must be configured for Microsoft Entra sign-in. The resource administrator can follow the setup procedures for [Windows](../../identity/devices/howto-vm-sign-in-azure-ad-windows) or [Linux](../../identity/devices/howto-vm-sign-in-azure-ad-linux) virtual machines. For Azure Arc-enabled servers, this preview supports only Linux.
- For Azure Bastion connections, a Bastion host must have network connectivity to the virtual machine. Use [Deploy Azure Bastion](/en-us/azure/bastion/quickstart-host-portal) for deployment and [Microsoft Entra ID authentication with Azure Bastion](/en-us/azure/bastion/bastion-entra-id-authentication) for authentication setup and required resource access.
- An administrator manages the active or eligible role assignments. For role assignment setup, see [Assign Azure resource roles in PIM](pim-resource-roles-assign-roles).

## Find your Azure Virtual Machine

In the [My Access portal](../my-access-portal-overview), locate the virtual machine you want to connect to and view its role assignments. Eligible role assignments need to be activated before you can use their permissions. If the role assignments you need are already active, you don't need to activate them again.

1. Sign in to the [My Access portal](https://myaccess.microsoft.com) in the tenant where you have access.
2. Under **My Access**, select [**Resource Connections**](https://aka.ms/pim/resource-connections).
3. Select **Virtual Machine** to view Azure Virtual Machines, or **Azure Arc VM** for supported Azure Arc-enabled Linux servers.
4. Find the resource and view its active and eligible role assignments. Select the resource name to view its details. To view it in the Azure portal, select **Open in Azure** from the resource details.

[![Screenshot of My Access Resource Connections showing eligible role assignments and the Activate action for a virtual machine.](media/pim-connect-virtual-machine-my-access/my-access-resource-connections.png)](media/pim-connect-virtual-machine-my-access/my-access-resource-connections.png#lightbox)

## Activate the access you need

If you already have active access and **Connect** is available, continue to Connect to the Azure Virtual Machine. Otherwise, request role activation for the roles you need.

Dependent resources are resources used for the connection, such as the Azure Bastion host and the virtual machine's network interface. An existing eligible role assignment can cover dependent resources when it grants the required permissions at a scope that includes those resources. You don't need a separate eligible role assignment on every dependency. You can optionally select a lower-privileged role when the eligible role's policy allows it.

For example, if the virtual machine, network interface, Bastion host, and relevant virtual network are in the same resource group, the following eligible role assignments can provide the required access after activation:

| Existing eligible role assignment | Role assignment scope | Access after activation |
| --- | --- | --- |
| **Reader** | The resource group containing the resources. | Reader access to the virtual machine, network interface, Bastion host, and virtual network in that resource group. |
| **Virtual Machine User Login** | The virtual machine. | Microsoft Entra sign-in to the virtual machine as a regular user. |

Confirm the roles and scopes offered in the role activation dialog for your connection.

1. Select **Activate** at the Azure subscription, resource group, or resource scope where you need access. The scope you select is the activation scope.
2. In the role-selection dialog, select **Activate** for the eligible role assignment you need.

    [![Screenshot of available virtual machine sign-in role assignments and their Activate actions.](media/pim-connect-virtual-machine-my-access/resource-connection-role-selection.png)](media/pim-connect-virtual-machine-my-access/resource-connection-role-selection.png#lightbox)
3. Under **Choose a connection path**, select an available path, such as **Azure Bastion**. Review **Role assignments to activate**, including access to dependent resources such as the Azure Bastion host or network interface.

    The roles shown depend on your existing eligibility. Review the roles and resources listed before you submit the request.

    [![Screenshot of a connection path, dependent-resource role assignments, and the Activate access action.](media/pim-connect-virtual-machine-my-access/resource-connection-activation.png)](media/pim-connect-virtual-machine-my-access/resource-connection-activation.png#lightbox)
4. Review the **Duration** and enter a **Justification** for your task.
5. Optional: If **Allow least-privilege role activation** is enabled on the policy for the role you're eligible for, use **Change settings** in the activation dialog to select an available lower-privileged role. The eligible role's policy governs approval, authentication, justification, and activation maximum duration.
6. Complete the role activation requirements shown and select **Activate access**. Requirements depend on each eligible role's policy and can include approval or Conditional Access.
7. Select **Refresh** to check the request status. If the request is pending approval, wait for approval. Continue when access is **Active** and **Connect** is available.

[![Screenshot of a virtual machine with an active role assignment and the Connect action available.](media/pim-connect-virtual-machine-my-access/resource-connection-active-access.png)](media/pim-connect-virtual-machine-my-access/resource-connection-active-access.png#lightbox)

## Connect to the Azure Virtual Machine

Use a connection method offered for the selected resource. The available options depend on the resource configuration.

If your organization requires a recording, check [Azure Bastion recording support and limitations](azure-pim-resource-rbac#azure-bastion-recording-support) before selecting a method. Microsoft Entra ID RDP in the Azure portal and native-client connections don't support Bastion graphical session recording.

1. Select **Connect** for the Azure Virtual Machine or supported Azure Arc-enabled Linux server.
2. In the connection dialog, choose an available method:

    - For Azure Bastion in-browser access, select **Azure Bastion** under **Choose a connection path**. Select **Browser** under **Choose a connection option**, and then select **Connect**.
    - For Azure Cloud Shell, select the offered Cloud Shell connection option.
    - For a native RDP or SSH connection, follow the instructions in the connection dialog. Use the applicable [Windows](../../identity/devices/howto-vm-sign-in-azure-ad-windows) or [Linux](../../identity/devices/howto-vm-sign-in-azure-ad-linux) guide for client requirements.
3. Complete the connection instructions and sign in with your Microsoft Entra ID credentials.

[![Screenshot of the Azure Bastion connection path, Browser connection option, and Connect action.](media/pim-connect-virtual-machine-my-access/resource-connection-bastion-browser.png)](media/pim-connect-virtual-machine-my-access/resource-connection-bastion-browser.png#lightbox)

## Troubleshoot access and connection

Use the following checks when you can't connect. An administrator handles role assignment or activation issues. A resource administrator handles virtual machine and Bastion setup.

| Symptom | Next action |
| --- | --- |
| The virtual machine isn't listed. | Confirm that you're signed in to the tenant where you have access. Ask the administrator to verify your role assignment and its scope, and the resource administrator to verify the connection setup. |
| The required role assignment isn't listed for activation. | Ask the administrator to check whether you have an eligible role assignment with the required permissions and scope. My Access activation doesn't create eligibility. |
| Activation is pending approval. | Wait for approval before using the role. If you no longer need the request, [cancel it in My Access](pim-resource-roles-activate-your-roles?pivots=my-access#view-and-cancel-a-pending-request-in-my-access). |
| **Connect** is unavailable after activation. | Select **Refresh** and check the activation status in [**Resource Connections**](https://aka.ms/pim/resource-connections). If the request is pending approval, wait for approval. If the status is **Active** but **Connect** is still unavailable, ask your administrator to check the access and setup requirements in Prerequisites. |
| Sign-in fails after you start the connection. | Use the [Windows sign-in troubleshooting guide](../../identity/devices/howto-vm-sign-in-azure-ad-windows#troubleshoot-sign-in-problems) or [Linux sign-in troubleshooting guide](../../identity/devices/howto-vm-sign-in-azure-ad-linux#troubleshoot-sign-in-issues), with help from the resource administrator for configuration checks. |

## Finish your work

When you're finished, end your Azure Virtual Machine or Azure Arc-enabled server session and deactivate temporary access that you no longer need.

1. Sign out of the Azure Virtual Machine or Azure Arc-enabled server session.
2. In the [My Access portal](../my-access-portal-overview), review the active role assignment and select **Deactivate** where available.

Role deactivation removes the active role assignment. It isn't a procedure for disconnecting an existing Azure Virtual Machine or Azure Arc-enabled server session. For administrator session management in PIM, see [Monitor and disconnect Azure Bastion sessions](pim-manage-bastion-sessions). For session management on the Azure Bastion resource, see [Monitor active sessions](/en-us/azure/bastion/session-monitoring).