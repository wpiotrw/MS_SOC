---
layout: Conceptual
title: Discover modernization pattern by workload type - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/sizes-v6-v7-modernization-discover
breadcrumb_path: ../../../breadcrumb/azure-compute/toc.json
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
author: rod-reis
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: rosanto
ms.update-cycle: 1095-days
description: Discover which of seven modernization patterns each workload follows, and which phases of the v6 and v7 modernization journey apply to it.
ms.service: azure-virtual-machines
ms.topic: how-to
ms.date: 2026-09-25T00:00:00.0000000Z
ms.collection:
- migration
- v2-5-to-v6-7
ai-usage: ai-assisted
locale: en-us
document_id: 9b395484-4bbe-a6e6-3039-24872a51b7fd
document_version_independent_id: c4611499-9831-a2d4-de52-0abb140e9bab
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/sizes-v6-v7-modernization-discover.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/lifecycle/sizes-v6-v7-modernization-discover
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/sizes-v6-v7-modernization-discover.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d44a5346-5de4-439c-b804-7b2a536cbb55
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/31f0a52b-651f-4010-94e9-e671670147d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/da41a22b-b7a0-42d3-9c35-50da1c2b7b87
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/b3236d36-01a2-484b-8b87-88a599a6998d
platformId: a0630e02-9609-a80b-8c91-f43c0260bd5c
---

# Discover modernization pattern by workload type - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs

**Workload patterns:** ✔️ All patterns — start here

Before planning modernization waves, discover which pattern each workload follows. The starting VM generation determines **remediation effort**. However, how the workload deploys, stores state, and recovers from the replacement of an individual VM determines **modernization effort**.

The prerequisites in this article apply per image, not per VM. Workloads built from a shared, validated image can modernize by replacing the pool, while customer-managed applications, databases, infrastructure roles, and virtual appliances require application-aware replication, configuration migration, vendor certification, or a planned cutover.

Important

VM series availability varies by Azure service, region, zone, operating system, and application vendor. Managed services that let you select a VM size expose a curated size list. Databricks, HDInsight, Azure Data Explorer, and Batch each publish which sizes they support. Confirm the target v6 or v7 size appears in the service's list and the vendor's support matrix, not only in the region. Confirm quota as well: the v6 and v7 series use quota families separate from earlier generations, so existing headroom doesn't carry over.

## Workload modernization categories

| Category | Examples | Typical modernization approach | Expected effort |
| --- | --- | --- | --- |
| **A. Customer-replaceable compute pools** | • Azure Kubernetes Service (AKS) node pools• Azure Red Hat OpenShift machine sets• Azure Batch pools• Stateless Virtual Machine Scale Sets• Self-hosted CI agent pools (Azure DevOps, GitHub Actions)• Azure CycleCloud and HPC scheduler node arrays | Create a replacement pool on the target series from a platform-supplied or generic image — the workload deploys at runtime via containers, packages, or bootstrap. Redirect or reschedule work, drain the old pool, and remove it. | **Lowest** for stateless, declaratively deployed workloads |
| **B. Image-based desktop and application hosts** | **Non-persistent hosts only:**• Azure Virtual Desktop pooled host pools• Citrix DaaS random (pooled) catalogs• Omnissa Horizon floating instant-clone pools | Rebuild the customer-owned golden image with the workload baked in, deploy canary hosts on the target series, drain user sessions from old hosts, expand in rings, and remove old hosts as sessions end. | **Low to moderate** when profiles and application data are externalized |
| **C. Service-managed compute** | • Azure Databricks• Azure Data Explorer• Azure Synapse Spark pools• Azure-SSIS integration runtime• Azure Database for PostgreSQL and MySQL flexible server | Select a supported node type or SKU; the service restarts, recreates, or moves the underlying compute. | **Low**, but the replacement process is controlled by the service |
| **D. Cluster re-creation** | • Azure HDInsight• Azure Machine Learning compute clusters | Deploy a replacement cluster at the target size, reproduce configuration, redirect jobs, and migrate any state not held externally. | **Low to moderate**; lowest when storage and metastore are already external |
| **E. Customer-managed application and infrastructure VMs** | • Custom line-of-business applications• Web and application servers• DNS servers• Middleware• General-purpose ISV applications• File servers• License and activation servers• Jump boxes and management servers• **Persistent desktops:** Azure Virtual Desktop personal host pools, Citrix DaaS static (dedicated) catalogs, Omnissa Horizon dedicated assignments | Deploy a replacement VM from a current image, restore application and configuration, synchronize state, validate dependencies, redirect clients, and retire the old VM. | **Moderate**, decreasing with automation and externalized state |
| **F. Stateful and clustered workloads** | • Active Directory Domain Services domain controllers• SQL Server Always On availability groups• Failover clusters• Distributed databases• Splunk indexer clusters• Service Fabric managed clusters• SAP workloads• Oracle Database with Data Guard• Self-managed Cassandra, MongoDB, and Elasticsearch clusters• Kafka and Confluent Platform on VMs | Add replacement nodes or replicas on the target series, synchronize data, validate cluster health, perform an application-aware failover or role transfer, and remove old nodes. | **Moderate to high**, depending on data volume, replication, and quorum |
| **G. Certified ISV virtual appliances and "COTS" applications** | • Palo Alto Networks• Check Point• Fortinet• F5• Citrix ADC• Storage appliances• Cisco Catalyst 8000V• Backup proxies and media agents (Veeam, Commvault)• Other marketplace network and security appliances | Confirm vendor certification for the exact VM family, deploy parallel appliances, reproduce policy and routing, validate the datapath, shift traffic, and retire the old appliances. | **Moderate**, gated on vendor certification and network cutover |

Most workloads identify by example. If yours doesn't match any row, classify it by two questions: who owns the image, and what gets replaced — a pool, a cluster, or an individual VM. If the answer is still "an individual VM," treat it as pattern E.

## Which phases apply to your pattern

The modernization journey isn't uniform. Assess and Plan cover image and VM-level remediation, so they apply only where you own the image. Modernize replaces individual VMs, so it applies only where that's your unit of replacement. Use this table to find your route.

| Pattern | 1.Discover | 2.Assess | 3.Plan | 4.Modernize | 5.Validate | Where you finish |
| --- | --- | --- | --- | --- | --- | --- |
| A. Compute pools | ✔️ | ❌ | ❌ | ❌ | Platform checks | This article, then your respective Azure Service's docs |
| B. Image-based hosts | ✔️ | ✔️ | ✔️ | ❌ | ✔️ | Assess and Plan the image, then replace hosts by ring |
| C. Service-managed compute | ✔️ | ❌ | ❌ | ❌ | Platform checks | This article, then your service's docs |
| D. Cluster re-creation | ✔️ | ❌ | ❌ | ❌ | Platform checks | This article, then your service's docs |
| E. Customer-managed VMs | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | The full journey |
| F. Stateful and clustered | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | The full journey, plus cluster gates and validation |
| G. Certified appliances | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | Vendor certification first, then as for E |

### If your pattern finishes here (A, C, D)

When the platform or the Azure service supplies the node image, it already meets the Generation 2, NVMe, and MANA prerequisites. There's no image to rebuild, no device paths to remediate, and no per-VM cutover to plan, so the Assess, Plan, and Modernize phases have nothing to add.

Confirm the supported size, region, zone, and quota as described earlier, then replace the pool or cluster by using the steps for your pattern below together with your service's own documentation. For capacity assurance and family-scoped discount replanning, see [Region, zone, and capacity planning](sizes-v6-v7-modernization-plan#region-zone-and-capacity-planning) and [Commercial continuity](sizes-v6-v7-modernization-plan#commercial-continuity). When the new nodes are running, confirm the platform signals in [Validate and optimize](sizes-v6-v7-modernization-validate).

## A. Customer-replaceable compute pools

**Applies to:** ✔️ Azure Kubernetes Service (AKS) node pools ✔️ Azure Red Hat OpenShift machine sets ✔️ Azure Batch pools ✔️ Stateless Virtual Machine Scale Sets ✔️ Self-hosted CI agent pools (Azure DevOps, GitHub Actions) ✔️ Azure CycleCloud and HPC scheduler node arrays

Nodes are disposable, and workloads arrive through containers, images, packages, extensions, or automated bootstrap. This is the most direct path:

1. Create a replacement pool by using a supported v6 or v7 size and a current Generation 2, NVMe- and MANA-ready image.
2. Apply the required labels, taints, extensions, or agent configuration.
3. Deploy a representative workload and validate boot, storage, networking, and performance.
4. Move or reschedule workloads onto the replacement pool.
5. Drain the old pool and remove it after validation.

For Kubernetes-based services, confirm that disruption budgets, topology constraints, persistent volumes, daemon sets, and node selectors permit workloads to move to the new pool.

**References**

- [Resize node pools in Azure Kubernetes Service (AKS)](/en-us/azure/aks/resize-node-pool)
- [Supported VM sizes and generations for AKS node pools](/en-us/azure/aks/aks-virtual-machine-sizes)
- [Choose a VM size for compute nodes in an Azure Batch pool](/en-us/azure/batch/batch-pool-vm-sizes)
- [Nodes and pools in Azure Batch](/en-us/azure/batch/nodes-and-pools)

## B. Image-based desktop and application hosts

**Applies to:** ✔️ Azure Virtual Desktop pooled host pools ✔️ Citrix DaaS random (pooled) catalogs ✔️ Omnissa Horizon floating instant-clone pools

Important

**Only non-persistent hosts belong to this pattern.** What decides the pattern isn't whether the workload is a desktop or an application — it's whether a user is permanently assigned to a specific VM. Persistent desktops hold unique state on the OS disk, so they can't be drained and replaced, and they modernize as customer-managed VMs instead.

| Product | Non-persistent — this pattern | Persistent — pattern E |
| --- | --- | --- |
| Azure Virtual Desktop | Pooled host pools | Personal host pools |
| Citrix DaaS | Random (pooled) catalogs | Static (dedicated) catalogs |
| Omnissa Horizon | Floating instant-clone pools | Dedicated assignments |

Session hosts and application workers are created from a golden image, but user sessions add operational sequencing:

1. Update the image and required agents.
2. Deploy a small number of hosts on the target series and validate sign-in, profile attachment, application launch, and monitoring.
3. Place old hosts into drain or maintenance mode.
4. Expand replacement hosts in controlled rings and remove old hosts after active sessions end.

This pattern requires user profiles and application data to live outside the session host — through FSLogix profile containers, a persistent user-data disk, or an equivalent. If a host holds anything a user would miss, it isn't non-persistent, whatever the host pool is called.

**References**

- [Session host update for Azure Virtual Desktop](/en-us/azure/virtual-desktop/session-host-update)
- [Update session hosts using session host update](/en-us/azure/virtual-desktop/session-host-update-configure)
- [Host pool management approaches for Azure Virtual Desktop](/en-us/azure/virtual-desktop/host-pool-management-approaches)
- [Manage machine catalogs in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/install-configure/machine-catalogs-manage.html)
- [Instant-clone desktop pools in Omnissa Horizon](https://docs.omnissa.com/bundle/Desktops-and-Applications-in-HorizonV2406/page/InstantCloneDesktopPools.html)

## C. Service-managed compute

**Applies to:** ✔️ Azure Databricks ✔️ Azure Data Explorer ✔️ Azure Synapse Spark pools ✔️ Azure-SSIS integration runtime ✔️ Azure Database for PostgreSQL and MySQL flexible server

Select a supported compute configuration. The service manages the image and the replacement process. Check target-SKU availability in the service's supported list, quota, local temporary-disk requirements, and application performance on the new nodes.

**How to tell whether a service belongs here:** You can change the size on the existing resource, or swap a pool inside it, without rebuilding the resource. Some services need a restart or a stop-set-start sequence to apply the change — that's still pattern C. If the size is fixed at creation, it's pattern D instead.

**References**

- [Azure Databricks compute configuration reference](/en-us/azure/databricks/compute/configure)
- [Select a SKU for your Azure Data Explorer cluster](/en-us/azure/data-explorer/manage-cluster-choose-sku)
- [Manage cluster vertical scaling (scale up) in Azure Data Explorer](/en-us/azure/data-explorer/manage-cluster-vertical-scaling)
- [Apache Spark pool configurations in Azure Synapse Analytics](/en-us/azure/synapse-analytics/spark/apache-spark-pool-configurations)
- [Reconfigure the Azure-SSIS integration runtime](/en-us/azure/data-factory/manage-azure-ssis-integration-runtime)
- [Compute options in Azure Database for PostgreSQL flexible server](/en-us/azure/postgresql/flexible-server/concepts-compute)

## D. Cluster re-creation

**Applies to:** ✔️ Azure HDInsight ✔️ Azure Machine Learning compute clusters

**How to tell whether a service belongs here:** The service fixes the VM size when it creates the resource, so changing the size means deploying and moving to a replacement. If you can change the size in place, it's pattern C.

Some Azure services statically assign the VM size at cluster creation, so moving to a new series means deploying a replacement cluster rather than swapping a pool inside it. HDInsight is the primary example. The effort depends almost entirely on whether state already lives outside the cluster:

1. Confirm the target v6 or v7 size appears in the service's supported-size list for the cluster type.
2. Externalize anything still held inside the cluster — storage on Azure Data Lake Storage or a Storage Account, and an external metastore for Hive or Oozie metadata.
3. Capture the cluster configuration: script actions, network and security settings, autoscale rules, and installed components.
4. Deploy the replacement cluster at the target size and reapply the configuration, preferably through infrastructure as code so the rebuild is repeatable.
5. Redirect jobs, pipelines, and client connections to the new cluster and validate output parity and performance.
6. Retire the old cluster after the validation window closes.

When storage and metastore are already external, this approach is similar to pool-replacement effort. When they aren't, externalizing them is the modernization — do it first, and future size changes become routine.

**References**

- [Supported node configurations for Azure HDInsight](/en-us/azure/hdinsight/hdinsight-supported-node-configuration)
- [Select the right VM size for Azure HDInsight](/en-us/azure/hdinsight/hdinsight-selecting-vm-size)
- [Use external metadata stores in Azure HDInsight](/en-us/azure/hdinsight/hdinsight-use-external-metadata-stores)
- [Capacity planning for Azure HDInsight clusters](/en-us/azure/hdinsight/hdinsight-capacity-planning)
- [Create an Azure Machine Learning compute cluster](/en-us/azure/machine-learning/how-to-create-attach-compute-cluster)

## E. Customer-managed application and infrastructure VMs

**Applies to:** ✔️ Custom line-of-business applications ✔️ Web and application servers ✔️ DNS servers ✔️ Middleware ✔️ General-purpose ISV applications ✔️ File servers ✔️ License and activation servers ✔️ Jump boxes and management servers ✔️ Persistent desktops

Deploy a replacement VM from an updated image. The process depends on the role:

- **Stateless web and application servers:** Add replacement instances behind the load balancer, validate, remove old instances from rotation, and retire them.
- **File servers:** Deploy replacement capacity and use replication or migration tooling before redirecting clients.
- **Custom and ISV applications:** Rebuild from supported media, restore configuration and data, validate licensing and dependencies, and redirect traffic.
- **Persistent desktops:** Azure Virtual Desktop personal host pools, Citrix DaaS static (dedicated) catalogs, and Omnissa Horizon dedicated assignments belong here rather than in pattern B. A user is bound to a specific VM, so the desktop can't be drained and replaced. Treat each one as an individual VM modernization: capture what the user has on the OS disk, modernize per user or in small waves during agreed windows, and confirm reassignment after cutover.

Where the application is deployed through infrastructure as code or configuration management, the effort approaches pool-based workloads. Where it isn't, follow the standard [2. Assess](sizes-v6-v7-modernization-assess), [3. Plan](sizes-v6-v7-modernization-plan), [4. Modernize](sizes-v6-v7-modernization-modernize), and [5. Validate](sizes-v6-v7-modernization-validate) journey.

Note

Persistent desktops are the most common workload that arrives hibernated. Resume and deallocate before you modernize, and re-validate hibernation support on the target size — see [Resume hibernated VMs before you modernize](sizes-v6-v7-modernization-plan#resume-hibernated-vms-before-you-modernize).

**References**

- [Change the size of a virtual machine](/en-us/azure/virtual-machines/sizes/resize-vm)
- [Configure personal desktop assignment in Azure Virtual Desktop](/en-us/azure/virtual-desktop/configure-host-pool-personal-desktop-assignment-type)

## F. Stateful and clustered workloads

**Applies to:** ✔️ Active Directory Domain Services domain controllers ✔️ SQL Server Always On availability groups ✔️ Failover clusters ✔️ Distributed databases ✔️ Splunk indexer clusters ✔️ Service Fabric managed clusters ✔️ SAP workloads ✔️ Oracle Database with Data Guard ✔️ Self-managed Cassandra, MongoDB, and Elasticsearch clusters ✔️ Kafka and Confluent Platform on VMs

A workload is pattern F when the VM holds state that must be synchronized — a database, a directory, a quorum vote — and the application supports replicas, cluster nodes, or role transfer. These workloads modernize side by side: a new node joins the topology, state synchronizes, and the application moves the role. The VM is never cut over; the cluster absorbs the replacement. For the execution sequence, quorum rules, and rollback model, see [Stateful and clustered workloads in the modernization runbook](sizes-v6-v7-modernization-modernize#stateful-and-clustered-workloads-f).

**Active Directory Domain Services** follows this pattern natively — replication is multi-master, so a fresh domain controller on the target series populates itself. Never restore or clone a domain controller from an image or backup of another domain controller; the runbook covers the safe sequence.

Standalone stateful VMs that can't take a replica modernize as individual VMs with an application-consistent backup — the runbook's execution-method choice applies to them.

Note

For SAP workloads, treat SAP certification of the target VM size as a hard gate that precedes all other planning — not as a validation item. Only sizes on the SAP-certified list are supportable, regardless of platform readiness.

**References**

- [Install a replica Active Directory domain controller on an Azure VM](/en-us/windows-server/identity/ad-ds/deploy/virtual-dc/adds-on-azure-vm)
- [Always On availability groups on SQL Server on Azure VMs](/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview)
- [Scale up a Service Fabric cluster primary node type](/en-us/azure/service-fabric/service-fabric-scale-up-primary-node-type)
- [Modify the VM SKU for a Service Fabric managed cluster node type](/en-us/azure/service-fabric/how-to-managed-cluster-modify-node-type)
- [What SAP software is supported on Azure VMs](/en-us/azure/sap/workloads/supported-product-on-azure)

## G. Certified ISV virtual appliances

**Applies to:** ✔️ Palo Alto Networks ✔️ Check Point ✔️ Fortinet ✔️ F5 ✔️ Citrix ADC ✔️ Cisco Catalyst 8000V ✔️ Storage appliances ✔️ Backup proxies and media agents ✔️ Other marketplace network and security appliances

A workload is pattern G when the VM *is* the product: the marketplace image, NIC layout, drivers, and disk presentation are part of what the vendor certifies and supports. Don't assume an appliance can move because its operating system boots on the target family — certification is granted per VM family, and it's a hard gate that precedes all other planning.

The modernization is a parallel-pair cutover: new appliances deploy alongside the existing pair, policy and routing are reproduced and verified, and traffic shifts through a controlled network change. For the certification checklist, see [Confirm before you commit in Plan](sizes-v6-v7-modernization-plan#confirm-before-you-commit); for the cutover sequence, see [Cut over a certified appliance in the modernization runbook](sizes-v6-v7-modernization-modernize#cut-over-a-certified-appliance-g).

Note

Some products span categories, so classify the deployment rather than the product name. A Citrix estate can span three patterns at once: random (pooled) catalogs are image-based hosts, static (dedicated) catalogs are customer-managed VMs, and Citrix ADC appliances are certified ISV appliances. Splunk indexer clusters modernize as stateful clustered workloads, while vendor support for the VM family remains an ISV consideration. Virtual Machine Scale Sets are only pool-replaceable when instances hold no unique state or configuration.

**References**

- [Generation 2 VMs on Azure](/en-us/azure/virtual-machines/generation-2)
- [Trusted Launch for Azure VMs](/en-us/azure/virtual-machines/trusted-launch)
- [NVMe overview for Azure VMs](/en-us/azure/virtual-machines/nvme-overview)
- [Microsoft Azure Network Adapter (MANA) overview](/en-us/azure/virtual-network/accelerated-networking-mana-overview)
- [MANA support for Network Virtual Appliances (NVAs)](/en-us/azure/virtual-network/accelerated-networking-mana-network-virtual-appliance-opt-out)

## Exit criteria

- Every workload in scope is tagged with a pattern.
- Pool-replaced and service-managed workloads (A, C, D) have a confirmed supported size, region, zone, and quota, and are routed to their service's documentation.
- SAP workloads have a certified target size confirmed, not assumed.
- Appliance workloads (G) have a vendor certification check open with a named owner.
- Remaining workloads (B, E, F) are routed to [2. Assess Readiness](sizes-v6-v7-modernization-assess).