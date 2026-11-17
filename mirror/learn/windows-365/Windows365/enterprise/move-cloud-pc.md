---
layout: Conceptual
title: Cloud PC Move | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/move-cloud-pc
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to move Windows 365 Cloud PCs to a different region or network by using the Move device action or a provisioning policy.
keywords: 
author: ErikjeMS
ms.author: ashleyvarma
manager: dougeby
ms.date: 2026-11-10T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: mattsha
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: c5ae470a-3468-2f55-f302-47111eb94936
document_version_independent_id: c5ae470a-3468-2f55-f302-47111eb94936
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/move-cloud-pc.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/move-cloud-pc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/move-cloud-pc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c450d479-44e5-4a9c-9b93-e6f9b69dd42d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e273b0-a43e-4cc8-9bf9-67d4d6a1e869
platformId: 8a5a15d0-4c7a-d0a5-0e4b-3bfa32ab113b
---

# Cloud PC Move | Microsoft Learn

Note

The Move device action (preview) is rolling out gradually, beginning at Microsoft Ignite 2026. It might not be available to everyone right away, even after this article is published.

You can move existing Windows 365 Cloud PCs to a different region or network without [reprovisioning](reprovision-cloud-pc) them. A move preserves the Cloud PC, including its apps, settings, and user data. You can move Cloud PCs from:

- One region to another single region.
- One [Azure network connection (ANC)](azure-network-connections) to another ANC.
- A Microsoft hosted network to an ANC and vice versa.

There are two ways to move Cloud PCs:

- **Move device action (preview):** Move one or more selected Windows 365 Enterprise Cloud PCs without changing their [provisioning policy](edit-provisioning-policy).
- **Provisioning policy:** Change the region or ANC in a provisioning policy, and then apply the change to existing Cloud PCs. This method supports Windows 365 Enterprise and [Windows 365 Flex](introduction-windows-365-flex) dedicated Cloud PCs.

Moving Cloud PCs doesn't result in reprovisioning.

Important

A Cloud PC is unavailable while it's being moved, and connected users can be disconnected. Users aren't notified automatically, so tell them in advance to save their work and sign out. After a Cloud PC is moved to a new region or ANC, its [restore points](restore-overview) in the previous region or ANC are deleted and no longer accessible.

## Choose how to move Cloud PCs

| To move | Use |
| --- | --- |
| One Windows 365 Enterprise Cloud PC | The **Move** device action (preview) from the Cloud PC's page. See Move a single Cloud PC. |
| Selected Windows 365 Enterprise Cloud PCs in a provisioning policy | The **Move** device action (preview) from the policy's **Devices** tab. See Move Cloud PCs from a provisioning policy's Devices tab. |
| Multiple Windows 365 Enterprise Cloud PCs, up to 100 at a time | The **Move** device action (preview) from **Bulk device actions**. See Move multiple Cloud PCs by using bulk device actions. |
| All Cloud PCs in a provisioning policy (Enterprise or Flex dedicated) | Edit the provisioning policy and apply the change to all devices. See Bulk move all Cloud PCs in a policy. |
| Selected Windows 365 Flex dedicated Cloud PCs | Edit the provisioning policy and apply the change to select devices. See Move a subset of Cloud PCs. |

Use the Move device action when you want to move selected Enterprise Cloud PCs without changing their provisioning policy. Use the provisioning policy method when you want to change the region or network that a policy uses and apply that change to its existing Cloud PCs.

Note

Editing a provisioning policy remains available for both Windows 365 Enterprise and Windows 365 Flex dedicated Cloud PCs. The Move device action (preview) doesn't replace it, and it supports only Windows 365 Enterprise Cloud PCs. To move Windows 365 Flex dedicated Cloud PCs, edit the provisioning policy.

## Supported Cloud PC move scenarios

These combinations apply to both methods. Move doesn't change a Cloud PC's join type. For example, you can't move a Microsoft Entra hybrid joined Cloud PC to a Microsoft-hosted network.

| Join type | To/from | To/from | Supported? |
| --- | --- | --- | --- |
| Microsoft Entra join &lt;-&gt; Microsoft Entra join | Microsoft-hosted network region or region group | Another Microsoft-hosted network region or region group | Yes |
| Microsoft Entra join &lt;-&gt; Microsoft Entra join | ANC | Another ANC | Yes |
| Microsoft Entra join &lt;-&gt; Microsoft Entra join | Microsoft-hosted network region or region group | ANC | Yes |
| Microsoft Entra join &lt;-&gt; Microsoft Entra join | ANC | Microsoft-hosted network region or region group | Yes |
| Microsoft Entra hybrid join &lt;-&gt; Microsoft Entra hybrid join | ANC | Another ANC | Yes |
| Microsoft Entra hybrid join &lt;-&gt; Microsoft Entra join | ANC (Microsoft Entra hybrid join) | Microsoft-hosted network region or region group | No |
| Microsoft Entra hybrid join &lt;-&gt; Microsoft Entra join | ANC (Microsoft Entra hybrid join) | Another ANC (Microsoft Entra join) | No |

## What happens during a move

When a move starts:

- The Cloud PC is shut down and unavailable until the move finishes. A move can take several hours.
- Connected users can be disconnected, and unsaved work might be lost.
- Users aren't notified automatically.
- Other Cloud PC actions are blocked while the move is in progress.
- The Cloud PC keeps its join type. Its data, apps, and settings are preserved.

When the move finishes, restore points from the previous region or ANC are deleted and no longer accessible. For more information, see Move and disaster recovery.

## Bulk move all Cloud PCs in a policy

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Windows 365** (under **Provisioning**) &gt; **Provisioning policies** &gt; select a policy.
2. Under **General**, select **Edit**.
3. Under **Join type details**, make changes depending on the original type:

    - For **Hybrid Microsoft Entra Join**, change the ANC\*.
    - For **Microsoft Entra Join**:

        - You can change **Network** type from ANC to Microsoft hosted network, or vice versa.
        - If a **Microsoft hosted network** is used, change the **Geography** and/or **Region**.
        - If an **Azure network connection** is used, change the ANC\*.
4. Select **Next** &gt; **Update**.
5. When ready to move the existing Cloud PCs, select **Apply this configuration**.
6. In the **Apply this configuration to existing Cloud PCs** box, select **Region or Azure network connections for all devices** &gt; **Apply**.

\* The domain defined in the new ANC must match that of the Cloud PCs that you want to move. The domain used in the original ANC must be reachable from the new ANC.

Any new Cloud PCs provisioned after updating the policy configuration follow the updated policy configuration and are created in the new region or ANC.

## Move a subset of Cloud PCs

Tip

For Windows 365 Enterprise Cloud PCs, we recommend the Move device action (preview). Use the steps in this section to move Windows 365 Flex dedicated Cloud PCs.

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), select **Devices** &gt; **Windows 365** (under **Provisioning**) &gt; **Provisioning policies** &gt; select a policy.
2. Under **General**, select **Edit**.
3. Under **Join type details**, make changes depending on the original type:

    - For **Hybrid Microsoft Entra Join**, change the ANC\*.
    - For **Microsoft Entra Join**:

        - You can change **Network** type from ANC to Microsoft hosted network, or vice versa.
        - If a **Microsoft hosted network** is used, change the **Geography** and/or **Region**.
        - If an **Azure network connection** is used, change the ANC\*.
4. Select **Next** &gt; **Update**.
5. When ready to move the existing Cloud PCs, select **Apply this configuration**.
6. In the **Apply this configuration to existing Cloud PCs** box, select **Region or Azure network connections for select devices** &gt; **Apply**.
7. Under **Select devices**, select the devices that you want to move. You can move up to 100 devices at a time.
8. Choose **Select** &gt; **Continue**.

## Move Enterprise Cloud PCs by using the Move device action (preview)

Important

The Move device action is in public preview. Preview features might change before general availability.

Use the **Move** device action to move one or more selected Windows 365 Enterprise Cloud PCs to a different region or network without changing their provisioning policy or affecting other Cloud PCs in the policy. Moved Cloud PCs stay in their current provisioning policy.

The Move device action supports only Windows 365 Enterprise Cloud PCs. To move Windows 365 Flex dedicated Cloud PCs, see Move a subset of Cloud PCs.

You can start a move from:

- A Cloud PC's page.
- **Bulk device actions**.
- The **Devices** tab of a provisioning policy.

### Requirements

You must have an Intune role that includes the **Cloud PCs** &gt; **Relocate** permission. For more information, see [Windows 365 role-based access](role-based-access).

Each Cloud PC that you move must:

- Be a Windows 365 Enterprise Cloud PC with a **Provisioned** status.
- Not be [GPU-enabled](gpu-cloud-pc).
- Not have another Cloud PC action in progress.
- Not have a third-party agent that Move doesn't support.

If you move Cloud PCs to an ANC, the ANC must be healthy and compatible with the join type of the Cloud PCs.

### Move a single Cloud PC

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), and select **Devices** &gt; **All Cloud PCs**.
2. Select the Cloud PC that you want to move.
3. Select **Move**.
4. Select the destination region and network.
5. Review the information, and then submit the move.

After the move completes, the Cloud PC's page shows its new region and network.

### Move multiple Cloud PCs by using bulk device actions

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), and select **Devices** &gt; **All devices** &gt; **Bulk device actions**.
2. For **OS**, select **Windows**. For **Device type**, select **Cloud PCs**. For **Device action**, select **Move**.
3. Read the guidance on the page, and then select **Next**.
4. Select the Cloud PCs that you want to move. You must select at least two Cloud PCs, and you can select up to 100 in one bulk move. Move doesn't change join type, so a selection that mixes Microsoft Entra join and Microsoft Entra hybrid join Cloud PCs can fail for some of them. When possible, select Cloud PCs that have the same join type.
5. Select the destination region and network.
6. On the **Review + create** page, review your selections, and then select **Create**.

### Move Cloud PCs from a provisioning policy's Devices tab

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431), and select **Devices** &gt; **Provision Cloud PCs**.
2. Select a provisioning policy, and then select the **Devices** tab.
3. Select one or more Cloud PCs.
4. Select **Move**, and then select the destination region and network.
5. Review the information, and then submit the move.

### Monitor a move

Track the status of a move in the [Cloud PC actions report](report-cloud-pc-actions). Select **Devices** &gt; **Monitor** &gt; **Cloud PC actions**. Single-device moves appear on the **Devices** tab, and bulk moves appear on the **Bulk batches** tab. To see the action status for the Cloud PCs in one policy, select the policy, and then select the **Action status** tab.

### After a move

- The provisioning policy and the settings it uses for new Cloud PCs don't change. A Cloud PC that you move can have a different region or network than its provisioning policy specifies.
- If you [reprovision](reprovision-cloud-pc) a Cloud PC after you move it, the Cloud PC is reprovisioned based on the region and network in its provisioning policy, so it can return to its previous location. Review the policy before you reprovision a Cloud PC that you moved. To change a Cloud PC's region or network, use Move.
- A move can show as completed before the Cloud PC is connectable. Before you tell users that the move is finished, confirm that the Cloud PC is available and that a user can connect.
- Users might need to refresh their workspace in [Windows App](/en-us/windows-app/overview) to reconnect to the Cloud PC after a move.

### Considerations

- Move doesn't change a Cloud PC's join type or provisioning policy.
- Move doesn't support scheduling or maintenance windows.
- To move Cloud PCs to a different virtual network or subnet, create an ANC that uses that network or subnet, and then move the Cloud PCs to the ANC.

### Troubleshooting

| Issue | What to do |
| --- | --- |
| **Move** isn't available | Confirm that you have the **Cloud PCs** &gt; **Relocate** permission, that the Cloud PC is an Enterprise Cloud PC with a **Provisioned** status, that it isn't GPU-enabled, and that it doesn't have another action in progress. Cloud PCs that have an unsupported third-party agent can't be moved. |
| No destination ANC appears | Confirm that a healthy and compatible ANC exists for the join type of the Cloud PC. |
| Validation prevents you from submitting the move | Review the message, remove unsupported Cloud PCs from your selection, or select a compatible destination. For example, you can't move a Microsoft Entra hybrid joined Cloud PC to a Microsoft-hosted network. |
| The move failed | Open the action details. If **Retry** is available, correct the reported condition, and then retry the action. |
| The move stays pending or doesn't complete | Network settings on the Cloud PC, such as a VPN, proxy, or secure web gateway, can block the connectivity that Windows 365 needs. Confirm that these settings allow access to the required endpoints. See [Network requirements for Windows 365](requirements-network). If the move still doesn't progress, contact Microsoft Support. |
| The move completed, but the Cloud PC isn't available | Wait for the connection status to update, and review the action details. If users connect by using Windows App, ask them to refresh their workspace. If the Cloud PC stays unavailable, contact Microsoft Support. |
| A Cloud PC returns to its previous location after you reprovision it | Reprovisioning uses the region and network in the provisioning policy. To change the location of a Cloud PC, use Move. |

## Move and resiliency

Move gives you a planned way to change where Cloud PCs run without reprovisioning them or losing user data. For example, you can use Move to:

- Respond to capacity constraints in a region by moving Cloud PCs to another supported region.
- Move Cloud PCs off a network that you're retiring or migrating, by moving them to a different ANC or to a Microsoft hosted network.
- Place Cloud PCs closer to users when users relocate or when latency is a concern.

Move is an administrator-initiated action. It doesn't automatically fail over Cloud PCs when a region has an outage. To help protect against unplanned regional outages, use [cross region disaster recovery](cross-region-disaster-recovery) or [disaster recovery plus](disaster-recovery-plus).

To reduce the impact of a move on your users, see Best practices.

## Move and disaster recovery

Move and disaster recovery serve different purposes. Use Move for planned changes, such as permanently relocating Cloud PCs. Use [cross region disaster recovery](cross-region-disaster-recovery) or [disaster recovery plus](disaster-recovery-plus) to keep users productive during an unplanned regional outage. Cross region disaster recovery isn't intended for planned or permanent region changes. For an overview of your options, see [Microsoft Business Continuity and Disaster Recovery (BCDR) with Windows 365](business-continuity-disaster-recovery).

Moving a Cloud PC doesn't conflict with disaster recovery, but a move affects the recovery points for that Cloud PC:

- **Restore points:**[Restore points](restore-overview) stored in the Cloud PC's previous region or ANC are deleted after the move. You can't restore the Cloud PC to a point in time before the move.
- **Disaster recovery snapshots:** While a Cloud PC is being moved, a scheduled disaster recovery snapshot of that Cloud PC might be missed. If you need to recover the Cloud PC during that time, the most recent recovery point might be older than usual.
- **Other actions:** Other Cloud PC actions are blocked while a move is in progress, and you can't move a Cloud PC while another action is in progress. Wait for a restore or disaster recovery operation to finish before you start a move.

## Best practices

The best time to perform moves is over a maintenance window or general period of down time to make sure the impact to users is minimized. Cloud PCs are shut down and inaccessible for up to several hours during the move process. You should notify your users before the move so that they can save their work and sign out.

When moving many devices to a new region, start with a few noncritical Cloud PCs and check for success before moving the critical Cloud PCs.

You can track the status of moving Cloud PCs with the [Cloud PC actions report](report-cloud-pc-actions).

New Cloud PCs created by the edited provisioning policy are assigned to the new region or ANC.

## Other move operations

Cloud PCs can't be moved from one provisioning policy to another.

You can't move some Cloud PCs to one region and other Cloud PCs to another region in the same policy edit operation.

You can't move Cloud PCs from one virtual network or subnet to another using the edit provisioning policy method. To make VNet/subnet changes, create a new ANC with the updated vNet/subnet and then move the Cloud PCs to the new ANC.