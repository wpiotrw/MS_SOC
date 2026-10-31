---
layout: Conceptual
title: Onboarding to Microsoft Security Copilot for non-Microsoft 365 E5 and E7 customers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/manual-onboarding
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about manual onboarding to get started with Microsoft Security Copilot.
ms.date: 2026-03-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
locale: en-us
document_id: 12a9bc15-f0d5-e4e1-a125-1bc2bbedf18f
document_version_independent_id: 12a9bc15-f0d5-e4e1-a125-1bc2bbedf18f
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/manual-onboarding.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manual-onboarding
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/manual-onboarding.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 9d327b9a-292a-2f48-7ef4-3573fd37e42f
---

# Onboarding to Microsoft Security Copilot for non-Microsoft 365 E5 and E7 customers | Microsoft Learn

Note

The following steps are only applicable for customers who are **NOT** Microsoft 365 E5 and E7 customers.  If you're a Microsoft 365 E5 and E7 included customer and have been notified that you're eligible to use Security Copilot these steps don't apply to you. Microsoft will automatically provision and onboard you, so that you can immediately get started with Security Copilot. For more information, see [Understand how Security Copilot is auto provisioned for Microsoft 365 E5 and E7 customers](auto-provisioning-security-copilot).

If Security Copilot isn't included in your license, you need to provision SCUs.

You can choose from the following options to provision capacity:

- Option 1 (Recommended): Provision capacity within Security Copilot
- Option 2: Provision capacity through Azure

Note

Regardless of the method you choose, you'll need to purchase a minimum of 1 provisioned SCU. You can purchase up to a maximum of 100 SCUs. The recommended number of units to conduct an introductory exploration of Security Copilot is 3 units with overage set to unlimited overage. You can use the usage monitoring dashboard to keep track of usage and adjust capacity based on workload. For more information, see [Manage usage](manage-usage).

## Minimum requirements

- **Azure subscription**: Required to purchase SCUs. [Create your free Azure account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- **Supported roles**: Anyone with the supported [Microsoft Entra or Microsoft Purview roles](manual-onboarding#microsoft-entra-and-microsoft-purview-roles) can complete onboarding steps. For more information, see [Security Copilot roles](authentication#security-copilot-roles).

### Microsoft Entra and Microsoft Purview roles

The following Microsoft Entra and Microsoft Purview roles automatically inherit **Copilot owner** access, ensuring Security Copilot always has at least two owners.

**Microsoft Entra roles:**

- Billing Administrator
- Entra Compliance Administrator
- Global Administrator
- Intune Administrator
- Security Administrator

For more information on continuity in Microsoft Entra, see [Manage emergency access accounts](/en-us/entra/identity/role-based-access-control/security-emergency-access).

**Microsoft Purview roles:**

- Purview Compliance Administrator
- Purview Data Governance Administrator
- Purview Organization Management

As part of the Security Copilot inclusion in the Microsoft 365 E5 and E7 license, the Compliance pack is automatically added.

**For capacity provisioning**

- Azure Contributor or Owner role on subscription/resource group
- Security Administrator or higher in the tenant you're onboarding Security Copilot.

These roles are needed to attach the provision of SCU capacities to the Security Copilot workspace.

Note

Whoever sets up the default environment (including any other owner roles that that person holds) will be designated as the default owner. For example, if the person setting up Security Copilot has an Microsoft Entra Compliance Administrator role and Purview Organization Management role, then both of those roles are added as owners by default.

### Option 1 (Recommended): Provision capacity through Security Copilot

When you first open Security Copilot (https://securitycopilot.microsoft.com), you're guided through the steps in setting up capacity for your organization.

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com).
2. Select **Get started**.

    [![Screenshot of get started.](media/get-started.png)](media/get-started.png#lightbox)
3. Set up a workspace. A workspace is a scoped, tenant-bound environment where users, automations, and agents operate. Enter a workspace name following the workspace naming convention, then select **Continue**. For more information, see [Naming rules and restrictions for Azure resources](/en-us/azure/azure-resource-manager/management/resource-name-rules).

    ![Screenshot of Workspace info.](media/workspace-info-fre.png)
4. Set up your security capacity:  Select the Azure subscription, associate capacity to a resource group, add a name to the capacity, select the prompt evaluation location, and specify the number of Security Compute Units (SCUs). You can also specify the number of overage units. These units offer the flexibility to have additional security compute units available when the initially provisioned SCUs are depleted during usage spikes.

    [![Screenshot of set-up your security capacity.](media/set-up-capacity.png)](media/set-up-capacity.png#lightbox)

    Note

    The number of SCUs is provisioned on an hourly basis, and the estimated monthly cost is displayed.

    If your selected geo location is too busy, you can also evaluate the prompts anywhere in the world. This can be done by selecting the appropriate option in the capacity creation screen.
5. Select among the data sharing options. Select **Continue**. For more information on data sharing, see [Privacy and data security](privacy-data-security).
6. Confirm that you acknowledge and agree to the terms and conditions, then select **Continue**.

    After you've created the capacity, it will take a few minutes to deploy the Azure resource on the backend.

    [![Screenshot of setting up your security capacity.](media/setting-up-capacity.png)](media/setting-up-capacity.png#lightbox)
7. Select if you want Security Copilot to capture and store administrator actions, user actions, and system responses. Select **Continue**. For more information, see [Accessing data from Microsoft 365 services](privacy-data-security#accessing-data-from-microsoft-365-services).

    Note

    Microsoft Purview will store your Customer Data in the region where your Microsoft 365 data is stored. For more information, see [Privacy and data security](privacy-data-security#accessing-data-from-microsoft-365-services).
8. Review the roles that can access Security Copilot. You can choose to select other recommended owner roles or add contributors. Select **Continue**.

    [![Screenshot of Copilot access roles.](media/copilot-access-roles.png)](media/copilot-access-roles.png#lightbox)
9. A confirmation page is displayed. Select **Finish**.

    [![Screenshot of Copilot all set.](media/all-set.png)](media/all-set.png#lightbox)

### Option 2: Provision capacity in Azure

The initial setup in this method starts in the Azure portal. Then, you need to complete the setup in the Security Copilot portal.

Note

Billing begins as soon as capacity is created, regardless of whether the SCU is attached to an environment.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for Security compute in the list of services, then select **Microsoft Security compute capacities**.
3. Select **Resource groups**.
4. Under **Plan**, select **Microsoft Security Copilot**. Then select **Create**.
5. Select a subscription and resource group, add a name to the capacity, select the prompt evaluation location and select the number of Security Compute Units (SCUs). You can also specify the number of overage units. These units offer the flexibility to have additional security compute units available when the initially provisioned SCUs are depleted during usage spikes. Data is always stored in your home tenant geo.

    Note

    The number of SCUs is provisioned on an hourly basis, and the estimated monthly cost is displayed.

    If your selected geo location is too busy, you can also evaluate the prompts anywhere in the world. This can be done by selecting the appropriate option in the capacity creation screen.
6. Confirm that you acknowledge and have read the terms and conditions, then select **Review + create**.
7. Verify that all the information is correct, then select **Create**. A confirmation page is displayed.
8. Select **Finish setup in the Security Copilot portal**.

## Recommended next steps

- [Assign roles to users](authentication#assign-roles)
- [Try out standalone and embedded experiences](experiences-security-copilot)
- [Learn about integrations](manage-plugins)
- [Check out primary use cases](https://adoption.microsoft.com/en-us/security-copilot/)
- [Join the Microsoft Security Copilot Customer Connection Program (CCP)](https://aka.ms/JoinCCP)