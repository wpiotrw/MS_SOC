---
layout: Conceptual
title: Linux distributions endorsed on Azure - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/endorsed-distros
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
author: vamckMS
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: vakavuru
ms.update-cycle: 365-days
description: Learn about Linux on Azure-endorsed distributions, including information about Ubuntu, Rocky, Alma, Oracle, Flatcar, Debian, Red Hat, and SUSE.
services: virtual-machines
ms.service: azure-virtual-machines
ms.collection: linux
ms.topic: concept-article
ms.date: 2024-11-14T00:00:00.0000000Z
ms.custom: engagement-fy23, linux-related-content
locale: en-us
document_id: 6ea02d36-fca1-a329-f539-90e22b698977
document_version_independent_id: 35d1f897-0d81-98b8-1c28-af1528f1e135
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/endorsed-distros.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/linux/endorsed-distros
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/endorsed-distros.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d56bfe0c-ecd5-4d90-854f-35482bbb1314
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/02e99b71-5808-477b-9387-4c6efa24e46b
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 561bd2c1-f9a9-9669-d233-6a1537ff694a
---

# Linux distributions endorsed on Azure - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

In this article, we'll cover the following:

- Types of Images
- Partners
- Image Update Cadence
- Azure-tuned Kernels

There are several different sources of Linux Virtual Machine (VM) images for Azure. Each source provides a different expectation for quality, utility, and support. This document summarizes each source (marketplace images, platform images, custom images, and community gallery images) and gives you more details about platform images, which are images provided in partnership between Microsoft and several mainstream Linux publishers such as Red Hat, Canonical, and SUSE.

Microsoft’s Linux distribution partners provide a multitude of Linux images in the Azure Marketplace. For distributions that aren't available from the Marketplace, you can always provide a custom built Linux image by following the guidelines found in [Create and upload a virtual hard disk that contains the Linux operating system](create-upload-generic). For older versions, see [Linux Kernel Requirements](create-upload-generic#linux-kernel-requirements).

The Azure Linux Agent is already preinstalled on Azure Marketplace images and is typically available from the distribution package repository. Source code can be found on [GitHub](https://github.com/azure/walinuxagent).

For more information on support by distribution, see [Support for Linux images in Microsoft Azure](https://support.microsoft.com/help/2941892/support-for-linux-and-open-source-technology-in-azure).

For more information about running Azure workloads on Linux, see the following video:

## Types of Images

Azure Linux images can be grouped into three categories:

### Marketplace Images

Images published and maintained by either Microsoft or partners. There are a large variety of images from multiple publishers for various use cases (security hardened, full database / application stack, etc.), and can be available free, pay-as-you-go, or BYOL (bring your own license/subscription).

Platform images are a type of Marketplace image for which Microsoft partnered with several mainstream publishers (see the following table about partners) to create a set of platform images that undergo additional testing and receive predictable updates (see section on Image Update Cadence). Use these platform images to build your own custom images and solution stacks. Endorsed Linux distribution partners such as Canonical (Ubuntu), Red Hat (RHEL), SUSE (SLES), CIQ (Rocky/RLC), Oracle (OL), and Credativ (Debian) publish these images.

Microsoft provides commercially reasonable customer support for these images. Additionally, Red Hat, Canonical, and SUSE offer integrated vendor support capabilities for their platform images.

### Custom Images

These images are created and maintained by the customer, often based on platform images. These images can also be created from scratch and uploaded to Azure - [learn how to create custom images](tutorial-custom-images). Customers can host these images in [Azure Compute Gallery](../azure-compute-gallery) and they can share these images with others in their organization.

Microsoft provides commercially reasonable customer support for custom images.

### Community Gallery Images

These images are created and provided by open source projects, communities, and teams. These images are provided using licensing terms set out by the publisher, often under an open source license. They don't appear as traditional marketplace listings, however, they do appear in the portal and via command line tools. More information on community galleries can be found here: [Azure Compute Gallery](../azure-compute-gallery#community-gallery).

Microsoft provides commercially reasonable support for Community Gallery images.

## Platform Image Partners

| Linux Publisher / Distribution | Images (Offers) | Microsoft Support Policy | Description |
| --- | --- | --- | --- |
| **AlmaLinux** | [AlmaLinux OS (x86_64/AMD64)](https://azuremarketplace.microsoft.com/marketplace/apps/almalinux.almalinux-x86_64?tab=Overview)[AlmaLinux OS (AArch64/ARM64)](https://azuremarketplace.microsoft.com/marketplace/apps/almalinux.almalinux-arm?tab=Overview)[AlmaLinux OS (x86_64/AMD64) HPC](https://azuremarketplace.microsoft.com/marketplace/apps/almalinux.almalinux-hpc?tab=Overview) | Microsoft CSS provides commercially reasonable support for these images. | AlmaLinux OS is a 100% community owned and governed, open source and forever free enterprise-grade Linux distribution. With long-term stability and providing a robust production-grade platform, AlmaLinux OS is 1:1 compatible with RHEL/CentOS. |
| **Canonical / Ubuntu** | [Ubuntu 22.04 LTS (including Pro)](https://azuremarketplace.microsoft.com/marketplace/apps/canonical.ubuntu-22_04-lts?tab=Overview)[Ubuntu 24.04 LTS (including Pro)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/canonical.ubuntu-24_04-lts?tab=Overview)[Ubuntu 26.04 LTS (including Pro)](https://azuremarketplace.microsoft.com/marketplace/apps/canonical.ubuntu-26_04-lts?tab=Overview) | Microsoft CSS provides commercially reasonable support for these images. | Canonical produces official Ubuntu images for Microsoft Azure and continuously tracks and delivers updates to these images, ensuring security and stability from the moment your virtual machines launch.  Canonical works closely with Microsoft to optimize Ubuntu images on Azure and ensure Ubuntu supports the latest cloud features as they're released. Ubuntu powers more mission-critical workloads on Azure than any other operating system. https://ubuntu.com/azure |
| **Credativ / Debian** | [Debian 11 "Bullseye"](https://azuremarketplace.microsoft.com/marketplace/apps/debian.debian-11?tab=Overview)[Debian 12 "Bookworm"](https://azuremarketplace.microsoft.com/marketplace/apps/debian.debian-12?tab=Overview) | Microsoft CSS provides commercially reasonable support for these images. | Credativ is an independent consulting and services company that specializes in the development and implementation of professional solutions by using free software. As leading open-source specialists, Credativ has international recognition with many IT departments that use their support. In conjunction with Microsoft, Credativ is preparing Debian images. The images are specially designed to run on Azure and can be easily managed via the platform. credativ will also support the long-term maintenance and updating of the Debian images for Azure through its Open Source Support Centers. https://www.credativ.de/portfolio/support/open-source-support-center |
| **Kinvolk / Flatcar** | [Flatcar Container Linux](https://azuremarketplace.microsoft.com/marketplace/apps/kinvolk.flatcar-container-linux-free)[Flatcar Container Linux (BYOL)](https://azuremarketplace.microsoft.com/marketplace/apps/kinvolk.flatcar-container-linux)[Flatcar Container Linux ARM64](https://azuremarketplace.microsoft.com/marketplace/apps/kinvolk.flatcar-container-linux-corevm) | Microsoft CSS provides commercially reasonable support for these images. | Flatcar Container Linux is a minimal, immutable, and auto-updating operating system for containerized applications. Originally developed by Kinvolk, it's now 100% community governed as a Cloud Native Computing Foundation (CNCF) project. Flatcar is a minimal distro, containing just those packages required for deploying containers. Its immutable file system guarantees consistency and security, while its auto-update capabilities enable you to be always up-to-date with the latest security fixes. Kinvolk was acquired by Microsoft in April 2021 and, post-acquisition, continues its mission within Microsoft to support the Flatcar community.https://www.flatcar.org |
| **Oracle Linux** | [Oracle Linux](https://azuremarketplace.microsoft.com/marketplace/apps/oracle.oracle-linux) | Microsoft CSS provides commercially reasonable support for these images. | Oracle's strategy is to offer a broad portfolio of solutions for public and private clouds. The strategy gives customers choice and flexibility in how they deploy Oracle software in Oracle clouds and other clouds. Oracle's partnership with Microsoft enables customers to deploy Oracle software to Microsoft public and private clouds with the confidence of certification and support from Oracle. Oracle's commitment and investment in Oracle public and private cloud solutions is unchanged. https://www.oracle.com/cloud/azure |
| **Red Hat / Red Hat Enterprise Linux (RHEL)** | [Red Hat Enterprise Linux](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-20190605)[Red Hat Enterprise Linux RAW](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-raw)[Red Hat Enterprise Linux ARM64](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-arm64)[Red Hat Enterprise Linux for SAP Apps](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-sap-apps)[Red Hat Enterprise Linux for SAP, HA, Updated Services](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-sap-ha)[Red Hat Enterprise Linux with HA add-on](https://azuremarketplace.microsoft.com/marketplace/apps/redhat.rhel-ha) | Microsoft CSS provides commercially reasonable support for these images. | The world's leading provider of open-source solutions, Red Hat helps more than 90% of Fortune 500 companies solve business challenges, align their IT and business strategies, and prepare for the future of technology. Red Hat achieves this by providing secure solutions through an open business model and an affordable, predictable subscription model. https://www.redhat.com/partners/microsoft |
| **CIQ / Rocky Linux** | [Rocky Linux from CIQ](https://azuremarketplace.microsoft.com/marketplace/apps?search=ciq&amp;page=1) | Microsoft CSS provides commercially reasonable support for these images. | Rocky Linux, developed by the Rocky Enterprise Software Foundation (RESF), is an open-source Enterprise Linux operating system designed for the community. As the founding sponsor of RESF, CIQ enhances and supports Rocky Linux on Microsoft Azure, delivering a secure, compliant, high-performance, and user-friendly platform for both development and production workloads.https://ciq.com/partners/cloud/azure/ |
| **SUSE / SUSE Linux Enterprise Server (SLES)** | [SUSE Linux Enterprise Server 12 SP5](https://marketplace.microsoft.com/marketplace/apps?search=sles-12-sp5)[SUSE Linux Enterprise Server 15 SP5](https://marketplace.microsoft.com/marketplace/apps?search=sles-15-sp5)[SUSE Linux Enterprise Server 15 SP6](https://marketplace.microsoft.com/marketplace/apps?search=sles-15-sp6)[SUSE Linux Enterprise Server 15 SP7](https://marketplace.microsoft.com/marketplace/apps?search=sles-15-sp7)[SUSE Linux Enterprise Server 16](https://marketplace.microsoft.com/marketplace/apps?search=sles-16-0) | Microsoft CSS provides commercially reasonable support for these images. | SUSE Linux Enterprise Server on Azure is a proven platform that provides superior reliability and security for cloud computing. SUSE's versatile Linux platform seamlessly integrates with Azure cloud services to deliver an easily manageable cloud environment. With more than 9,200 certified applications from more than 1,800 independent software vendors for SUSE Linux Enterprise Server, SUSE ensures that workloads running supported in the data center can be confidently deployed on Azure. Each Marketplace page provides access to all supported service packs and variants, including:  • +24x7 Support • Patching-only • BYOS (Bring Your Own Subscription) • SLES for SAP Applications  • Arm64 • Hardened images https://www.suse.com/partners/alliance/microsoft |

## Image Update Cadence

Azure requires that the publishers of the endorsed Linux distributions regularly update their platform images in Azure Marketplace with the latest patches and security fixes, at a quarterly or faster cadence. Updated images in the Marketplace are available automatically to customers as new versions of an image SKU. More information about how to find Linux images: [Find Azure Marketplace image information using the Azure CLI](cli-ps-findimage).

## Azure-tuned Kernels

Azure works closely with various endorsed Linux distributions to optimize the images that they published to Azure Marketplace. One aspect of this collaboration is the development of "tuned" Linux kernels that are optimized for the Azure platform and delivered as fully supported components of the Linux distribution. The Azure-Tuned kernels incorporate new features and performance improvements, and at a faster (typically quarterly) cadence compared to the default or generic kernels that are available from the distribution.

In most cases, you'll find these kernels preinstalled on the default images in Azure Marketplace so customers will immediately get the benefit of these optimized kernels. More information about these Azure-Tuned kernels can be found in the following links:

- [Debian Cloud Kernel - Available with the Debian 10 and Debian 9 "backports" image on Azure](https://wiki.debian.org/Cloud/MicrosoftAzure)
- [SLES Azure-Tuned Kernel](https://www.suse.com/c/a-different-builtin-kernel-for-azure-on-demand-images)
- [Ubuntu Azure-Tuned Kernel](https://blog.ubuntu.com/2017/09/21/microsoft-and-canonical-increase-velocity-with-azure-tailored-kernel)
- [Flatcar Container Linux](https://azuremarketplace.microsoft.com/marketplace/apps/kinvolk.flatcar-container-linux-corevm-amd64)