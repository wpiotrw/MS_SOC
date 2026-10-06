---
layout: Conceptual
title: Deliver Extended Security Updates for Windows Server - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/deliver-extended-security-updates
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
zone_pivot_group_filename: zone-pivots/azure-management/zone-pivot-groups.json
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to deliver Extended Security Updates for Windows Server 2012 and Windows Server 2016.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
zone_pivot_groups: extended-security-updates-windows-server
locale: en-us
document_id: 4930f6d0-7f79-d462-f505-c29be51ef1cb
document_version_independent_id: a8855b38-d1cd-aeef-6361-69fa2103fdea
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/deliver-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/deliver-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/deliver-extended-security-updates.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 4cebf3c2-5deb-2734-ca0e-0d394ff2f557
---

# Deliver Extended Security Updates for Windows Server - Azure Arc | Microsoft Learn

This article provides steps to enable delivery of Extended Security Updates (ESUs) to Windows Server machines onboarded to Arc-enabled servers. You can enable ESUs to these machines individually or at scale. The steps apply to Windows Server 2012/2012 R2 and Windows Server 2016. Use the selector at the top of the article to choose the operating system version you're licensing.

## Before you begin

Plan and prepare to onboard your machines to Azure Arc-enabled servers. To learn more, see [Prepare to deliver Extended Security Updates for Windows Server](prepare-extended-security-updates).

You also need the [Contributor](/en-us/azure/role-based-access-control/built-in-roles#contributor) role in [Azure RBAC](/en-us/azure/role-based-access-control/overview) to create and assign ESUs to Arc-enabled servers.

## Manage ESU licenses

::: zone pivot="windows-server-2012"

Important

The Windows Server 2012 and Windows Server 2012 R2 ESU period ends on October 13, 2026. The October 13, 2026 security update is the final update provided through ESUs. At midnight Coordinated Universal Time (UTC) on October 14, 2026, ESU licenses enabled by Azure Arc deactivate. The license resources remain available to view in Azure, but servers linked to them aren't eligible for security updates released after October 13, 2026. Migrate your workloads or upgrade to a supported version of Windows Server before the ESU period ends.

1. From your browser, sign in to the [Azure portal](https://portal.azure.com).
2. In the service menu, under **Licenses**, select **Windows Server ESU licenses**.

    [![Screenshot of main ESU window showing licenses tab and eligible resources tab.](media/deliver-extended-security-updates/extended-security-updates-2012-main-window.png)](media/deliver-extended-security-updates/extended-security-updates-2012-main-window.png#lightbox)

    From here, you can view and create ESU **Licenses** and view **Eligible resources** for ESUs.

::: zone-end

::: zone pivot="windows-server-2016"

1. From your browser, sign in to the [Azure portal](https://portal.azure.com).
2. Go to the **Azure Arc** page, and in the service menu, under **Licenses**, select the **Windows Server 2016 ESU licenses** offering.

    [![Screenshot of main ESU window showing licenses tab and eligible resources tab.](media/deliver-extended-security-updates/extended-security-updates-2016-main-window.png)](media/deliver-extended-security-updates/extended-security-updates-2016-main-window.png#lightbox)

    From here, you can view and create ESU **Licenses** and view **Eligible resources** for ESUs.

::: zone-end

## Create Azure Arc Windows Server licenses

First, provision Extended Security Update licenses from Azure Arc. Link these licenses to one or more Arc-enabled servers that you select in the next section.

Note

To provision ESU licenses, you must attest to their SA or SPLA coverage.

::: zone pivot="windows-server-2012"

After you provision an ESU license, specify the SKU (Standard or Datacenter), type of cores (Physical or vCore), and number of cores. You can also provision an Extended Security Update license in a deactivated state so that it doesn't initiate billing or be functional on creation. You can modify the cores associated with the license after provisioning.

The **Licenses** tab displays Azure Arc Windows Server licenses that are available. From here, you can select an existing license to apply or create a new license.

![Screenshot showing existing licenses and the option to create a new one.](media/deliver-extended-security-updates/extended-security-updates-licenses.png)

1. To create a new Windows Server license, select **Create**, and then provide the information required to configure the license on the page.

    For details on how to complete this step, see [License provisioning guidelines for Extended Security Updates for Windows Server](license-extended-security-updates).
2. Review the information provided, and then select **Create**.

    The license you created appears in the list. You can link it to one or more Arc-enabled servers by following the steps in the next section.

::: zone-end

::: zone pivot="windows-server-2016"

For Windows Server 2016, specify the SKU (Standard or Datacenter) and the number of cores when you create the license. Unlike Windows Server 2012, you select the core type (physical or virtual) later, when you enable ESUs on your machines. You can also provision the license in a deactivated state so that it doesn't initiate billing or be functional on creation.

1. On the license page, select **Create**.
2. On the license creation page, provide the following information:

    - **Resource group**: Select the resource group for the license.
    - **License name**: Enter a name for the license.
    - **Activation status**: Select the activation status.
    - **Region**: Select your region.
    - **SKU**: Select **Windows Server 2016 Standard** or **Windows Server 2016 Datacenter**.
    - **Number of cores**: Enter the number of cores that the license supports.

    For details on how to complete this step, see [License provisioning guidelines for Extended Security Updates for Windows Server](license-extended-security-updates).
3. Select **Next**, confirm that your Windows Server licenses have Software Assurance, and then select **Create**.

    The license you created appears in the list. You can link it to one or more Arc-enabled servers by following the steps in the next section.

::: zone-end

## Link ESU licenses to Arc-enabled servers

Select one or more Arc-enabled servers to link to an Extended Security Update license. After you link a server to an activated ESU license, the server can receive Windows Server ESUs.

Note

You have the flexibility to configure your patching solution of choice to receive these updates – whether that's [Update Manager](/en-us/azure/update-center/overview), [Windows Server Update Services](/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus), Microsoft Updates, [Microsoft Endpoint Configuration Manager](/en-us/mem/configmgr/core/understand/introduction), or a third-party patch management solution.

::: zone pivot="windows-server-2012"

1. Select the **Eligible resources** tab to view a list of all your Arc-enabled servers running Windows Server 2012 and 2012 R2.

    [![Screenshot of eligible resources tab showing servers eligible to receive ESUs.](media/deliver-extended-security-updates/extended-security-updates-eligible-resources.png)](media/deliver-extended-security-updates/extended-security-updates-eligible-resources.png#lightbox)

    The **ESUs status** column indicates whether the machine is enabled for ESUs.
2. To enable ESUs for one or more machines, select them in the list, and then select **Enable ESUs**.

::: zone-end

::: zone pivot="windows-server-2016"

1. Select the **Eligible resources** tab to view a list of all your Azure Arc-enabled servers running Windows Server 2016.

    [![Screenshot of eligible resources tab showing servers eligible to receive ESUs.](media/deliver-extended-security-updates/extended-security-updates-2016-eligible-resources.png)](media/deliver-extended-security-updates/extended-security-updates-2016-eligible-resources.png#lightbox)

    The **ESUs status** column indicates whether the machine is enabled for ESUs.
2. To enable ESUs for one or more machines, select them in the list, and then select **Enable ESUs**.

::: zone-end

::: zone pivot="windows-server-2012"

On the **Enable Extended Security Updates** pane, it shows the number of machines selected to enable ESU and the Windows Server licenses available to apply. Select a license to link to the selected machines and then select **Enable**.

![Screenshot of options to select the license to apply to previously chosen machines.](media/deliver-extended-security-updates/extended-security-updates-select-license.png)

Note

You can create a license from this page, rather than choosing an existing one, by selecting **Create an ESUs license**.

::: zone-end

::: zone pivot="windows-server-2016"

In the **Enable ESUs** dialog:

1. Select the **Core type**: **Physical cores** or **Virtual cores**.
2. Select the ESU license that you created.
3. Select **Enable**.

::: zone-end

When you return to the **Eligible resources** tab, you see the status of the selected machines shows **Enabled**.

::: zone pivot="windows-server-2016"

To verify enrollment on the server, run `azcmagent show` and confirm that the **Extended Security Updates** section shows a status of **Active**.

::: zone-end

If problems occur during the enablement process, see [Troubleshoot delivery of Extended Security Updates for Windows Server](troubleshoot-extended-security-updates) for assistance.

::: zone pivot="windows-server-2012"

## Enable ESUs at scale by using Azure Policy

To link servers at scale to an Azure Arc Extended Security Update license and lock down license modification or creation, consider using the following built-in Azure policies:

- [Enable Extended Security Updates (ESUs) license to keep Windows 2012 machines protected after their support lifecycle has ended (preview)](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F4864134f-d306-4ff5-94d8-ea4553b18c97)
- [Deny Extended Security Updates (ESUs) license creation or modification (preview)](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F4c660f31-eafb-408d-a2b3-6ed2260bd26c)

Specify Azure policies to a targeted subscription or resource group for both auditing and management scenarios.

## Additional scenarios

You might be eligible to receive Extended Security Updates patches at no extra cost in some scenarios. Two of these scenarios supported by Azure Arc are [Dev/Test (Visual Studio)](license-extended-security-updates#visual-studio-subscription-benefit-for-devtest-scenarios) and [Disaster Recovery (Entitled benefit DR instances from Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-by-benefits) or subscription only. Both scenarios require that you're already using Windows Server 2012/R2 ESUs enabled by Azure Arc for billable, production machines.

Warning

Don't create a Windows Server 2012/R2 ESU License for only Dev/Test or Disaster Recovery workloads. Don't provision an ESU License only for nonbillable workloads. You pay for all of the cores provisioned with an ESU license. You don't pay for dev/test cores on the license if you tag them according to the following qualifications.

To qualify for these scenarios, you must already have:

- **Billable ESU License.** You must already have provisioned and activated a WS2012 Arc ESU License to link to regular Azure Arc-enabled servers running in production environments (such as normally billed ESU scenarios). Provision this license only for billable cores, not for cores that are eligible for free Extended Security Updates, such as dev/test cores.
- **Arc-enabled servers.** Onboard your Windows Server 2012 and Windows Server 2012 R2 machines to Azure Arc-enabled servers for Dev/Test with Visual Studio subscriptions or Disaster Recovery.

To enroll Azure Arc-enabled servers eligible for ESUs at no extra cost, follow these steps to tag and link:

1. Tag both the WS2012 Arc ESU License (created for the production environment with cores for only the production environment servers) and the nonproduction Azure Arc-enabled servers with one of the following name-value pairs, corresponding to the appropriate exception:

    1. Name: "ESU Usage"; Value: "WS2012 VISUAL STUDIO DEV TEST"
    2. Name: "ESU Usage"; Value: "WS2012 DISASTER RECOVERY"

    If you're using the ESU License for multiple exception scenarios, mark the license with the tag: Name: "ESU Usage"; Value: "WS2012 MULTIPURPOSE"
2. Link the tagged license (created for the production environment with cores only for the production environment servers) to your tagged nonproduction Azure Arc-enabled Windows Server 2012 and Windows Server 2012 R2 machines. **Don't license cores for these servers or create a new ESU license for only these servers.**

This linking doesn't trigger a compliance violation or enforcement block, so you can extend the application of a license beyond its provisioned cores. The expectation is that the license only includes cores for production and billed servers. Any additional cores result in overbilling.

Important

Adding these tags to your license doesn't make the license free or reduce the number of license cores that are chargeable. By using these tags, you can link your Azure machines to existing licenses that are already configured with payable cores without needing to create any new licenses or add more cores to your free machines.

**Example:**

- You have eight Windows Server 2012 R2 Standard instances, each with eight physical cores. Six of these Windows Server 2012 R2 Standard machines are for production, and two of these Windows Server 2012 R2 Standard machines are eligible for free ESUs because the operating system was licensed through a Visual Studio Dev Test subscription.
    - First, provision and activate a regular ESU License for Windows Server 2012/R2 that's Standard edition and has 48 physical cores to cover the six production machines. Link this regular, production ESU license to your six production servers.
    - Next, reuse this existing license, don't add any more cores or provision a separate license, and link this license to your two nonproduction Windows Server 2012 R2 standard machines. Tag the ESU license and the two nonproduction Windows Server 2012 R2 Standard machines with Name: "ESU Usage" and Value: "WS2012 VISUAL STUDIO DEV TEST".
    - This results in an ESU license for 48 cores, and you pay for those 48 cores. You don't pay for the extra 16 cores of the dev test servers that you added to this license, as long as you tag the ESU license and the dev test server resources appropriately.

Note

You need a regular production license to start with, and you pay only for the production cores.

## Upgrading from Windows Server 2012/2012 R2

When upgrading a Windows Server 2012/2012R machine to Windows Server 2016 or above, it's not necessary to remove the Connected Machine agent from the machine. The new operating system will be visible for the machine in Azure within a few minutes of upgrade completion. Upgraded machines no longer require ESUs and are no longer eligible for them. Any ESU license associated with the machine isn't automatically unlinked from the machine. See [Unlink a license](api-extended-security-updates#unlink-a-license) for instructions on doing so manually.

## Assess WS2012 ESU patch Status

To detect whether your Azure Arc-enabled servers are patched with the most recent Windows Server 2012/R2 Extended Security Updates, you can use the Azure Policy [Extended Security Updates should be installed on Windows Server 2012 Arc machines](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetail.ReactView/id/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F14b4e776-9fab-44b0-b53f-38d2458ea8be/version%7E/null/scopes%7E/%5B%22%2Fsubscriptions%2F4fabcc63-0ec0-4708-8a98-04b990085bf8%22%5D). This policy definition, powered by Machine Configuration, identifies if the server has received the most recent ESU Patches. This is observable from the Guest Assignment and Azure Policy Compliance views built into the Azure portal.

::: zone-end