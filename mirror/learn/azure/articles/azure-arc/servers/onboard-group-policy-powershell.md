---
layout: Conceptual
title: Connect machines at scale using Group Policy with a PowerShell script - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/onboard-group-policy-powershell
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: schaffererin
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: schaffererin
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: In this article, you learn how to create a Group Policy Object to onboard Active Directory-joined Windows machines to Azure Arc-enabled servers.
ms.date: 2025-08-27T00:00:00.0000000Z
ms.topic: how-to
ms.custom: template-how-to
locale: en-us
document_id: 6ae288ed-d6fe-6337-482c-8e11cc5ec18b
document_version_independent_id: 5b1ec441-86a2-1040-28da-d6f249d1e01e
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/onboard-group-policy-powershell.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/onboard-group-policy-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/onboard-group-policy-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 224a566b-1665-7bce-9b16-bd0168f18c62
---

# Connect machines at scale using Group Policy with a PowerShell script - Azure Arc | Microsoft Learn

You can onboard Active Directory–joined Windows machines to [Azure Arc-enabled servers](overview) at scale using Group Policy.

First, you set up a remote share that hosts the Connected Machine agent, and then modify a script specifying the Arc-enabled server's landing zone within Azure. Next, you run a script that generates a Group Policy Object (GPO) to onboard a group of machines to Azure Arc-enabled servers. This Group Policy Object can be applied at the site, domain, or organizational level. The assignment can also use Access Control List (ACL) and other security filtering native to Group Policy. All machines in the scope of the Group Policy will be onboarded to Azure Arc-enabled servers, so scope your GPO to only include those machines that you want to onboard to Azure Arc.

Before you get started, ensure your environment meets the [Connected Machine Agent prerequisites](prerequisites) and the [networking requirements for deploying Azure Arc-enabled servers](network-requirements). For information about supported regions and other related considerations, see [supported Azure regions](overview#supported-regions). To understand more about design and deployment criteria, review our [at-scale planning guide](plan-at-scale-deployment).

Important

The `AllSigned` PowerShell execution policy isn't supported. Before connecting machines to Azure Arc, review the [PowerShell execution policy requirements](prerequisites#windows-powershell-execution-policy).

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Automatic connection for SQL Server

When you connect a Windows or Linux server to Azure Arc that also has Microsoft SQL Server installed, the SQL Server instances are automatically connected to Azure Arc as well. [SQL Server enabled by Azure Arc](/en-us/sql/sql-server/azure-arc/overview) provides a detailed inventory and additional management capabilities for your SQL Server instances and databases. As part of the connection process, an extension is deployed to your Azure Arc-enabled server, and [new roles](/en-us/sql/sql-server/azure-arc/permissions-granted-agent-extension) are applied to your SQL Server and databases. If you don't want to automatically connect your SQL Servers to Azure Arc, you can opt out by adding a tag to the Windows or Linux server with the name `ArcSQLServerExtensionDeployment` and value `Disabled` when connecting it to Azure Arc.

For more information, see [Manage automatic connection for SQL Server enabled by Azure Arc](/en-us/sql/sql-server/azure-arc/manage-autodeploy).

## Prepare a remote share and create a service principal

The Group Policy Object, which is used to onboard Azure Arc-enabled servers, requires a remote share with the Connected Machine agent.

1. Prepare a remote share to host the Azure Connected Machine agent package for Windows and the configuration file. You need to be able to add files to this remote share. The network share must be accessible by domain controllers and the domain machines. Domain computers should have Change permissions, and domain admins should have Full Control permissions.
2. Follow the steps to [create a service principal for onboarding at scale](onboard-service-principal#create-a-service-principal-for-onboarding-at-scale).

    - Assign the Azure Connected Machine Onboarding role to your service principal. Limit the scope of the role to the target Azure landing zone.
    - Make a note of the Service Principal Secret; you'll need this value later.
3. Download and unzip the folder **ArcEnabledServersGroupPolicy\_vX.X.X** from https://github.com/Azure/ArcEnabledServersGroupPolicy/releases/latest/. This folder contains the ArcGPO project structure with the scripts `EnableAzureArc.ps1`, `DeployGPO.ps1`, and `AzureArcDeployment.psm1`. These assets are used for onboarding the machine to Azure Arc-enabled servers.
4. Download the latest version of the [Azure Connected Machine agent Windows Installer package](https://aka.ms/AzureConnectedMachineAgent) from the Microsoft Download Center and save it to the remote share.
5. Execute the deployment script `DeployGPO.ps1` on the domain controller, modifying the run parameters for DomainFQDN, ReportServerFQDN, ArcRemoteShare, Service Principal secret, Service Principal Client ID, Subscription ID, Resource Group, Region, Tenant, and AgentProxy (if applicable). Details about these values can be found in the script comments.

    For example, the following command deploys the GPO to the contoso.com domain and copies the onboarding script `EnableAzureArc.ps1` to the remote share `AzureArcOnBoard` in the `Server.contoso.com` server:

    ```powershell
    .\DeployGPO.ps1 -DomainFQDN contoso.com -ReportServerFQDN Server.contoso.com -ArcRemoteShare AzureArcOnBoard -ServicePrincipalSecret $ServicePrincipalSecret -ServicePrincipalClientId $ServicePrincipalClientId -SubscriptionId $SubscriptionId -ResourceGroup $ResourceGroup -Location $Location -TenantId $TenantId [-AgentProxy $AgentProxy]
    ```

## Apply the Group Policy Object

On the Group Policy Management Console (GPMC), right-click on the desired Organizational Unit (OU) and link the GPO named **[MSFT] Azure Arc Servers (datetime)**. This GPO has a scheduled task to onboard the machines. Within 20 minutes, the GPO is replicated to the respective domain controllers. For more information about creating and managing group policy in Microsoft Entra Domain Services, see [Administer Group Policy in a Microsoft Entra Domain Services managed domain](/en-us/azure/active-directory-domain-services/manage-group-policy).

## Verify successful onboarding

After you install and configure the agent, verify that the servers in your OU were successfully connected to Azure Arc. You can do so by ensuring that they appear in the [Azure portal](https://aka.ms/hybridmachineportal) under **Azure Arc - Machines**.

Important

After confirming that your servers have successfully onboarded to Azure Arc, disable the Group Policy Object. Doing so prevents the PowerShell commands in the scheduled task from executing again when the system reboots or when the group policy is updated.