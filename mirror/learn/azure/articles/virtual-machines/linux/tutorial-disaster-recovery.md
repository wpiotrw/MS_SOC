---
layout: Conceptual
title: Tutorial - Set up disaster recovery for Linux VMs with Azure Site Recovery - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-disaster-recovery
breadcrumb_path: ../../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: rayne-wiselman
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: raynew
ms.update-cycle: 365-days
description: Learn how to set up disaster recovery for Linux VMs to a different Azure region, using the Azure Site Recovery service.
ms.service: azure-site-recovery
ms.collection: linux
ms.topic: tutorial
ms.date: 2023-01-25T00:00:00.0000000Z
ms.custom:
- mvc
- linux-related-content
- sfi-image-nochange
locale: en-us
document_id: 30f82099-c0eb-05eb-b152-bbb67fc711e2
document_version_independent_id: 1ee9495e-7ae3-f185-56b9-6422cc60779d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/tutorial-disaster-recovery.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/linux/tutorial-disaster-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/tutorial-disaster-recovery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bba62c59-6b53-4be4-8b9d-6624f9184c22
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f3a81ffb-ee36-4ec7-b54a-01b6681aff65
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 68bf78e4-6e6b-00e6-09fc-b5b239b56340
---

# Tutorial - Set up disaster recovery for Linux VMs with Azure Site Recovery - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Flexible scale sets

This tutorial shows you how to set up disaster recovery for Azure VMs running Linux. In this article, learn how to:

- Enable disaster recovery for a Linux VM
- Run a disaster recovery drill to check it works as expected
- Stop replicating the VM after the drill

When you enable replication for a VM, the Site Recovery Mobility service extension installs on the VM, and registers it with [Azure Site Recovery](/en-us/azure/site-recovery/site-recovery-overview). During replication, VM disk writes are sent to a cache storage account in the source VM region. Data is sent from there to the target region, and recovery points are generated from the data. When you fail a VM over to another region during disaster recovery, a recovery point is used to create a VM in the target region.

For a separate, same-region recovery option that retains an eligible existing VM resource, see [zone resilience for Azure VMs (Preview)](../zone-resilience). It isn't a Site Recovery workflow or a replacement for regional disaster recovery.

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Review the [preview limitations](../zone-resilience#limitations) before enabling the feature.

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Prerequisites

1. Check that your Azure subscription allows you to create a VM in the target region. If you just created your free Azure account, you're the administrator of the subscription, and you have the permissions you need.
2. If you're not the subscription administrator, work with the administrator to assign you:

    - Either the Virtual Machine Contributor built-in role, or specific permissions to:
        - Create a VM in the selected virtual network.
        - Write to an Azure storage account.
        - Write to an Azure managed disk.
    - The Site Recovery Contributor built-in role, to manage Site Recovery operations in the vault.
3. Check that the Linux VM is running a [supported operating system](/en-us/azure/site-recovery/azure-to-azure-support-matrix#linux).
4. If VM outbound connections use a URL-based proxy, make sure it can access these URLs. Using an authenticated proxy isn't supported.

    | **Name** | **Public cloud** | **Government cloud** | **Details** |
    | --- | --- | --- | --- |
    | Storage | `*.blob.core.windows.net` | `*.blob.core.usgovcloudapi.net` | Write data from the VM to the cache storage account in the source region. |
    | Microsoft Entra ID | `login.microsoftonline.com` | `login.microsoftonline.us` | Authorize and authenticate to Site Recovery service URLs. |
    | Replication | `*.hypervrecoverymanager.windowsazure.com` | `*.hypervrecoverymanager.windowsazure.com` | VM communication with the Site Recovery service. |
    | Service Bus | `*.servicebus.windows.net` | `*.servicebus.usgovcloudapi.net` | VM writes to Site Recovery for monitoring and diagnostic data. |
5. If you're using network security groups (NSGs) to limit network traffic for VMs, create NSG rules that allow outbound connectivity (HTTPS 443) for the VM using these service tags (groups of IP addresses). Try out the rules on a test NSG first.

    | **Tag** | **Allow** |
    | --- | --- |
    | Storage tag | Allows data to be written from the VM to the cache storage account. |
    | Microsoft Entra ID tag | Allows access to all IP addresses that correspond to Microsoft Entra ID. |
    | Events Hub tag | Allows access to Site Recovery monitoring. |
    | Azure Site Recovery tag | Allows access to the Site Recovery service in any region. |
    | GuestAndHybridManagement | Use if you want to automatically upgrade the Site Recovery Mobility agent that's running on VMs enabled for replication. |
6. Make sure VMs have the latest root certificates. On Linux VMs, follow the guidance provided by your Linux distributor, to get the latest trusted root certificates and certificate revocation list on the VM.

## Create a VM and enable disaster recovery

You can optionally enable disaster recovery when you create a VM.

1. [Create a Linux VM](quick-create-portal).
2. On the **Management** tab, under **Site Recovery** select **Enable disaster recovery**.
3. In **Secondary region**, select the target region to which you want to replicate the VM for disaster recovery.
4. In **Secondary subscription**, select the target subscription in which the target VM will be created. The target VM is created when you fail over the source VM from the source region to the target region.
5. In **Recovery Services vault**, select the vault you want to use for the replication. If you don't have a vault, select **Create new**. Select a resource group in which to place the vault, and a vault name.
6. In **Site Recovery policy**, leave the default policy, or select **Create new** to set custom values.

    - Recovery points are created from snapshots of VM disks taken at a specific point in time. When you fail over a VM, you use a recovery point to restore the VM in the target region.
    - A crash-consistent recovery point is created every five minutes. This setting can't be modified. A crash-consistent snapshot captures data that was on the disk when the snapshot was taken. It doesn't include anything in memory.
    - By default Site Recovery keeps crash-consistent recovery points for 24 hours. You can set a custom value between 0 and 72 hours.
    - An app-consistent snapshot is taken every 4 hours.
    - By default Site Recovery stores recovery points for 24 hours.
7. In **Availability options**, specify whether the VM will deploy as standalone, in an availability zone, or in an availability set.

    ![Enable replication on the VM management properties page.](media/tutorial-disaster-recovery/create-vm.png)
8. Finish creating the VM.

## Enable disaster recovery for an existing VM

If you want to enable disaster recovery on an existing VM, use this procedure.

1. In the Azure portal, open the VM properties page.
2. In **Operations**, select **Disaster recovery**.

    ![Open disaster recovery options for an existing VM.](media/tutorial-disaster-recovery/existing-vm.png)
3. In **Basics**, if the VM is deployed in an availability zone, you can select disaster recovery between availability zones.
4. In **Target region**, select the region to which you want to replicate the VM. The source and target regions must be in the same Microsoft Entra tenant.

    ![Set the basic disaster recovery options for a VM.](media/tutorial-disaster-recovery/basics.png)
5. Select **Next: Advanced settings**.
6. In **Advanced settings**, you can review settings, and modify values to custom settings. By default, Site Recovery mirrors the source settings to create target resources.

    - **Target subscription**. The subscription in which the target VM is created after failover.
    - **Target VM resource group**. The resource group in which the target VM is created after failover.
    - **Target virtual network**. The Azure virtual network in which the target VM is located when it's created after failover.
    - **Target availability**. When the target VM is created as a single instance, in an availability set, or availability zone.
    - **Proximity placement**. If applicable, select the proximity placement group in which the target VM is located after failover.
    - **Storage settings-Cache storage account**. Recovery uses a storage account in the source region as a temporary data store. Source VM changes are cached in this account, before being replicated to the target location.
        - By default one cache storage account is created per vault and reused.
        - You can select a different storage account if you want to customize the cache account for the VM.
    - **Storage settings-Replica managed disk**. By default, Site Recovery creates replica managed disks in the target region.
        - By default the target managed disk mirror the source VM managed disks, using the same storage type (Standard HDD/SSD, or Premium SSD).
        - You can customize the storage type as needed.
    - **Replication settings**. Shows the vault in which the VM is located, and the replication policy used for the VM. By default, recovery points created by Site Recovery for the VM are kept for 24 hours.
    - **Extension settings**. Indicates that Site Recovery manages updates to the Site Recovery Mobility Service extension that's installed on VMs you replicate.
        - The indicated Azure Automation account manages the update process.
        - You can customize the automation account.

    ![Page showing summary of target and replication settings.](media/tutorial-disaster-recovery/settings-summary.png)
7. Select **Review + Start replication**.
8. Select **Start replication**. Deployment starts, and Site Recovery starts creating target resources. You can monitor replication progress in the notifications.

    ![Notification for replication progress.](media/tutorial-disaster-recovery/notifications.png)

## Check VM status

After the replication job finishes, you can check the VM replication status.

1. Open the VM properties page.
2. In **Operations**, select **Disaster recovery**.
3. Expand the **Essentials** section to review defaults about the vault, replication policy, and target settings.
4. In **Health and status**, get information about replication state for the VM, the agent version, failover readiness, and the latest recovery points.

    ![Essentials view for VM disaster recovery.](media/tutorial-disaster-recovery/essentials.png)
5. In **Infrastructure view**, get a visual overview of source and target VMs, managed disks, and the cache storage account.

    ![infrastructure visual map for VM disaster recovery.](media/tutorial-disaster-recovery/infrastructure.png)

## Run a drill

Run a drill to make sure disaster recovery works as expected. When you run a test failover, it creates a copy of the VM, with no impact on ongoing replication, or on your production environment.

1. In the VM disaster recovery page, select **Test failover**.
2. In **Test failover**, leave the default **Latest processed (low RPO)** setting for the recovery point.

    This option provides the lowest recovery point objective (RPO), and generally spins up the VM most quickly in the target region. It first processes all the data that has been sent to Site Recovery service, to create a recovery point for each VM, before failing over to it. This recovery point has all the data replicated to Site Recovery when the failover was triggered.
3. Select the virtual network in which the VM will be located after failover.

    ![Page to set test failover options.](media/tutorial-disaster-recovery/test-failover-settings.png)
4. The test failover process begins. You can monitor the progress in notifications.

    ![Test failover notifications.](media/tutorial-disaster-recovery/test-failover-notification.png)

    After the test failover completes, the VM is in the *Cleanup test failover pending* state on the **Essentials** page.

## Clean up resources

The VM is automatically cleaned up by Site Recovery after the drill.

1. To begin automatic cleanup, select **Cleanup test failover**.

    ![Start cleanup on the Essentials page.](media/tutorial-disaster-recovery/start-cleanup.png)
2. In **Test failover cleanup**, type in any notes you want to record for the failover, and then select **Testing is complete. Delete test failover virtual machine**. Then select **OK**.

    ![Page to record notes and delete test VM.](media/tutorial-disaster-recovery/delete-test.png)
3. The delete process begins. You can monitor progress in notifications.

    ![Notifications to monitor delete test VM.](media/tutorial-disaster-recovery/delete-test-notification.png)

### Stop replicating the VM

After completing a disaster recovery drill, we suggest you continue to try out a full failover. If you don't want to do a full failover, you can disable replication. Disabling replication will:

- Remove the VM from the Site Recovery list of replicated machines.
- Stop Site Recovery billing for the VM.
- Automatically clean up source replication settings.

Stop replication as follows:

1. In the VM disaster recovery page, select **Disable Replication**.
2. In **Disable Replication**, select the reasons that you want to disable replication. Then select **OK**.

    ![Page to disable replication and provide a reason.](media/tutorial-disaster-recovery/disable-replication.png)

The Site Recovery extension installed on the VM during replication isn't removed automatically. If you disable replication for the VM, and you don't want to replicate it again at a later time, you can remove the Site Recovery extension manually, as follows:

1. Go to the VM &gt; **Settings** &gt; **Extensions**.
2. In the **Extensions** page, select each *Microsoft.Azure.RecoveryServices* entry for Linux.
3. In the properties page for the extension, select **Uninstall**.