---
layout: Conceptual
title: Deliver ESUs for VMware VMs through Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/deliver-extended-security-updates-for-vmware-vms-through-arc
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
author: Jeronika-MS
learn_banner_products:
- azure
ms.author: v-gajeronika
ms.service: azure-arc
description: Deliver ESUs for VMware VMs through Azure Arc.
ms.date: 2026-10-06T00:00:00.0000000Z
ms.topic: how-to
ms.services: azure-arc
ms.subservice: vmware-vsphere-azure-arc
ms.reviewer: v-gajeronika
keywords: VMware, Arc, Azure
locale: en-us
document_id: c7416fd5-50b7-2e6d-9ee4-3bcd39e4d8da
document_version_independent_id: 995749c5-b44e-da64-f5b2-7287122f4ff0
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/vmware-vsphere/deliver-extended-security-updates-for-vmware-vms-through-arc.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/vmware-vsphere/deliver-extended-security-updates-for-vmware-vms-through-arc
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/vmware-vsphere/deliver-extended-security-updates-for-vmware-vms-through-arc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8e23d947-35a1-c0b9-9029-d598db62ae8b
---

# Deliver ESUs for VMware VMs through Arc - Azure Arc | Microsoft Learn

By using Azure Arc-enabled VMware vSphere, you can enroll all the Windows Server 2016 VMs that your vCenter manages in [Extended Security Updates (ESUs)](/en-us/windows-server/get-started/extended-security-updates-overview) at scale. By using Arc ESUs, you get cost flexibility through pay-as-you-go Azure billing and an enhanced delivery experience with built-in inventory and keyless delivery. This article provides the steps to procure and deliver ESUs to WS 2016 VMware VMs that you onboard to Azure Arc-enabled VMware vSphere.

Note

To purchase ESUs, you must have Software Assurance through Volume Licensing Programs such as an Enterprise Agreement (EA), Enterprise Agreement Subscription (EAS), Enrollment for Education Solutions (EES), or Server and Cloud Enrollment (SCE). Alternatively, if your Windows Server 2016 machines are licensed through SPLA or with a Server Subscription, you don't need Software Assurance to purchase ESUs.

## Prerequisites

- The user account must have an Owner or Contributor role in a Resource Group in Azure to create and assign ESUs to VMware VMs.
- The vCenter managing the WS 2016 VMs, for which the ESUs are to be applied, should be [onboarded to Azure Arc](quick-start-connect-vcenter-to-arc-using-script).
- The WS 2016 VMs, for which the ESUs are to be applied, should be [onboarded to Azure Arc with the Arc agent installed](enable-vcenter-resources-in-azure).

## Manage ESU licenses

1. From your browser, sign in to the [Azure portal](https://portal.azure.com).
2. Go to the **Azure Arc** page, and in the service menu, under **Licenses**, select the **Windows Server 2016 ESU licenses** offering.

    [![Screenshot of main ESU window showing licenses tab and eligible resources tab.](/en-us/azure/azure-arc/servers/media/deliver-extended-security-updates/extended-security-updates-2016-main-window.png)](/en-us/azure/azure-arc/servers/media/deliver-extended-security-updates/extended-security-updates-2016-main-window.png#lightbox)

    From here, you can view and create ESU **Licenses** and view **Eligible resources** for ESUs.

## Create Azure Arc ESUs

First, provision Extended Security Update licenses from Azure Arc. Link these licenses to one or more Arc-enabled servers that you select in the next section.

Note

To provision ESU licenses, you must attest to their SA or SPLA coverage.

For Windows Server 2016, specify the SKU (Standard or Datacenter) and the number of cores when you create the license. Unlike Windows Server 2012, you select the core type (physical or virtual) later, when you enable ESUs on your machines. You can also provision the license in a deactivated state so that it doesn't initiate billing or be functional on creation.

1. On the license page, select **Create**.
2. On the license creation page, provide the following information:

    - **Resource group**: Select the resource group for the license.
    - **License name**: Enter a name for the license.
    - **Activation status**: Select the activation status.
    - **Region**: Select your region.
    - **SKU**: Select **Windows Server 2016 Standard** or **Windows Server 2016 Datacenter**.
    - **Number of cores**: Enter the number of cores that the license supports.

    For details on how to complete this step, see [License provisioning guidelines for Extended Security Updates for Windows Server](../servers/license-extended-security-updates).
3. Select **Next**, confirm that your Windows Server licenses have Software Assurance, and then select **Create**.

    The license you created appears in the list. You can link it to one or more Arc-enabled VMware vSphere VMs by following the steps in the next section.

## Link ESU licenses to Arc-enabled VMware vSphere VMs

Select one or more Arc-enabled VMware vSphere VMs to link to an ESU license. After you link a VM to an activated ESU license, the VM can receive Windows Server 2016 ESUs.

Note

You have the flexibility to configure your patching solution of choice to receive these updates – whether that's [Update Manager](/en-us/azure/update-center/overview), [Windows Server Update Services](/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus), Microsoft Updates, [Microsoft Endpoint Configuration Manager](/en-us/mem/configmgr/core/understand/introduction), or a third-party patch management solution.

1. Select the **Eligible Resources** tab to view a list of all your Arc-enabled machines running Windows Server 2016, including VMware vSphere VMs that have the Arc agent installed. The **ESUs status** column indicates whether the machine is enabled for ESUs.

    [![Screenshot of eligible resources tab showing servers eligible to receive ESUs.](/en-us/azure/azure-arc/servers/media/deliver-extended-security-updates/extended-security-updates-2016-eligible-resources.png)](/en-us/azure/azure-arc/servers/media/deliver-extended-security-updates/extended-security-updates-2016-eligible-resources.png#lightbox)
2. To enable ESUs for one or more machines, select them in the list, and then select **Enable ESUs**.

    In the **Enable ESUs** dialog:

    - Select the **Core type**: **Physical cores** or **Virtual cores**.
    - Select the ESU license that you created.
    - Select **Enable**.

    When you return to the **Eligible resources** tab, you see the status of the selected machines shows **Enabled**.

To verify enrollment on the server, run `azcmagent show` and confirm that the **Extended Security Updates** section shows a status of **Active**.

If problems occur during the enablement process, see [Troubleshoot delivery of Extended Security Updates for Windows Server](../servers/troubleshoot-extended-security-updates) for assistance.