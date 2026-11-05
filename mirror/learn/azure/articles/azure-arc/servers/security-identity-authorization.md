---
layout: Conceptual
title: Managed identity and access control - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/security-identity-authorization
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
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Identity and authorization for Azure Arc-enabled servers.
ms.topic: concept-article
ms.date: 2025-03-06T00:00:00.0000000Z
locale: en-us
document_id: 913a787c-b294-91aa-494e-6a5fa80c7d26
document_version_independent_id: 6e8ac557-99e4-61b9-e02e-e7dbff01bd6e
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/security-identity-authorization.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/security-identity-authorization
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/security-identity-authorization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 089ae8c6-7b27-18bc-e96b-cbb50974f547
---

# Managed identity and access control - Azure Arc | Microsoft Learn

This article describes the Microsoft Entra ID managed identity for Azure Arc-enabled servers, which is used for authentication when communicating with Azure, and details two useful Azure built-in roles.

## Microsoft Entra ID managed identity

Every Azure Arc-enabled server has a system-assigned Microsoft Entra ID managed identity associated with it. This identity is used by the agent to authenticate itself with Azure. It can also be used by extensions or other authorized apps on your system to access resources that understand OAuth tokens. The managed identity appears in the Microsoft Entra ID portal with the same name as the Azure Arc-enabled server resource. For example, if your Azure Arc-enabled server is named `prodsvr01`, an enterprise app in Microsoft Entra ID with the same name appears.

Each Microsoft Entra ID directory has a finite limit for the number of objects it can store. A managed identity counts as one object in the directory. If you're planning a large deployment of Azure Arc-enabled servers, check the available quota in your Microsoft Entra ID directory first, and submit a support request to increase your quota if needed. You can see the available and used quota in the [List Organizations API](/en-us/graph/api/intune-onboarding-organization-list) response under the `directorySizeLimit` section.

The managed identity is fully managed by the agent. As long as the agent stays connected to Azure, it handles rotating the credential automatically. The certificate backing the managed identity is valid for 90 days. The agent attempts to renew the certificate when it has 45 or fewer days of validity remaining. If the agent is offline long enough to expire, the agent becomes "expired" as well and won't connect to Azure. In this situation, automatic reconnection isn't possible and requires you to disconnect and reconnect the agent to Azure using an onboarding credential.

The managed identity certificate is stored on the local disk of the system. It’s important that you protect this file, because anyone in possession of this certificate can request a token from Microsoft Entra ID. The agent stores the certificate in `C:\ProgramData\AzureConnectedMachineAgent\Certs\` on Windows and `/var/opt/azcmagent/certs` on Linux. The agent automatically applies an access control list to this directory, restricting access to local administrators and the "himds" account. Don't modify access to the certificate files or modify the certificates on your own. If you think the credential for a system-assigned managed identity has been compromised, [disconnect](/en-us/azure/azure-arc/servers/azcmagent-disconnect) the agent from Azure and [connect](/en-us/azure/azure-arc/servers/azcmagent-connect) it again to generate a new identity and credential. Disconnecting the agent removes the resource in Azure, including its managed identity.

When an application on your system wants to get a token for the managed identity, it issues a request to the REST identity endpoint at `http://localhost:40342/identity`. There are slight differences in how Azure Arc handles this request compared to Azure VM. The first response from the API includes a path to a challenge token located on disk. The challenge token is stored in `C:\ProgramData\AzureConnectedMachineAgent\tokens` on Windows or `/var/opt/azcmagent/tokens` on Linux. The caller must prove they have access to this folder by reading the contents of the file and reissuing the request with this information in the authorization header. The tokens directory is configured to allow administrators and any identity belonging to the "Hybrid agent extension applications" (Windows) or the "himds" (Linux) group to read the challenge tokens. If you're authorizing a custom application to use the system-assigned managed identity, you should add its user account to the appropriate group to grant it access.

To learn more about using a managed identity with Arc-enabled servers to authenticate and access Azure resources, see the following video.

## RBAC roles

Azure role-based access control (Azure RBAC) has two [built-in roles](/en-us/azure/role-based-access-control/built-in-roles) that you can use to control access to an Arc-enabled server:

- **Azure Connected Machine Onboarding**, intended for accounts used to connect new machines to Azure Arc. This role allows accounts to see and create new Arc servers but disallows extension management.
- **Azure Connected Machine Resource Administrator**, intended for accounts that will manage servers once they’re connected. This role allows accounts to read, create, and delete Arc servers, VM extensions, licenses, and private link scopes.

Generic Azure built-in roles also apply to Azure Arc-enabled servers, including Reader, Contributor, and Owner.

## Identity and access control

[Azure RBAC](/en-us/azure/role-based-access-control/overview) is used to control which accounts can see and manage your Azure Arc-enabled server. From the [**Access Control (IAM)**](/en-us/azure/role-based-access-control/role-assignments-portal) page in the Azure portal, you can verify who has access to your Azure Arc-enabled server.

[![Screenshot of the Azure portal showing Azure Arc-enabled server access control.](media/security-identity-authorization/access-control-page.png)](media/security-identity-authorization/access-control-page.png#lightbox)

Users and applications granted the [Contributor](/en-us/azure/role-based-access-control/built-in-roles#contributor) or an administrator role to a resource can make changes to it, including deploying or deleting [extensions](manage-vm-extensions) on the machine. Extensions can include arbitrary scripts that run in a privileged context, so consider any contributor on the Azure resource to be an indirect administrator of the server.

The **Azure Connected Machine Onboarding** role is available for at-scale onboarding. This role only grants permission to read or create new Azure Arc-enabled servers in Azure. It doesn't grant permission to delete servers that were already registered, or to manage extensions. As a best practice, we recommend only assigning this role to the Microsoft Entra service principal used to onboard machines at scale.

Users who have the **Azure Connected Machine Resource Administrator** role can read, modify, reonboard, and delete a machine. This role is designed to support management of Azure Arc-enabled servers, but not other resources in the resource group or subscription.