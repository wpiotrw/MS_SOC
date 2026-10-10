---
layout: Conceptual
title: Create zonal VMs with the Azure portal - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/create-portal-availability-zone
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
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
author: mimckitt
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: mimckitt
ms.update-cycle: 180-days
ms.service: azure-virtual-machines
description: Create VMs in an availability zone with the Azure portal
ms.topic: how-to
ms.date: 2024-06-06T00:00:00.0000000Z
ms.custom: references_regions, portal
locale: en-us
document_id: 0662764d-dc84-9a95-f25b-ca254fe725b1
document_version_independent_id: 9b6dda82-0732-e40f-adc1-19bfbc6650ed
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/create-portal-availability-zone.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/create-portal-availability-zone
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/create-portal-availability-zone.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f98c9a19-e481-4f15-8047-76b641e6ed57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f5685781-a4fd-40f1-8126-59abde4643bf
platformId: d4d1bf7b-c28e-df04-cbcd-dd2ea0482287
---

# Create zonal VMs with the Azure portal - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs

This article steps through using the Azure portal to create highly resilient virtual machines in [availability zones](/en-us/azure/reliability/availability-zones-overview). Azure availability zones are physically separate locations within each Azure region that are tolerant to local failures. Use availability zones to protect your applications and data against unlikely datacenter failures.

To use availability zones, create your virtual machines in a [supported Azure region](/en-us/azure/reliability/availability-zones-region-support).

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Click **Create a resource** &gt; **Compute** &gt; **Virtual machine**.
3. In the **Virtual machines** page, select **Create** and then **Virtual machine**. The **Create a virtual machine** page opens.
4. In the **Basics** tab, under **Project details**, make sure the correct subscription is selected and then choose a resource group or create a new one.
5. Under **Instance details**, type a name for the **Virtual machine name**.
6. For **Availability options**, leave the default of **Availability zone**.
7. For **Availability zone**, the drop-down defaults to *Zone 1*. If you choose multiple zones, a new VM is created in each zone. For example, if you select all three zones, then three VMs are created. The VM names are the original name you entered, with **-1**, **-2**, and **-3** appended to the name based on number of zones selected. If you want, you can edit each of the default VM names.

    ![Screenshot showing that there are now 3 virtual machines that are created.](media/zones/3-vm-names.png)
8. Complete the rest of the page as usual. If you want to create a load balancer, go to the **Networking** tab &gt; **Load Balancing** &gt; **Load balancing options**. You can choose either an Azure load balancer or an Application gateway.

    For an **Azure load balancer**:

    1. You can select an existing load balancer or select **Create a load balancer**.
    2. To create a new load balancer, for **Load balancer name** type a load balancer name.
    3. Select the **Type** of load balancer, either *Public* or *Internal*.
    4. Select the **Protocol**, either **TCP** or **UDP**.
    5. You can leave the default **Port** and **Backend port**, or change them if needed. The backend port you select will be opened up on the Network Security Group (NSG) of the VM.
    6. When you're done, select **Create**.

    For an **Application Gateway**:

    1. Select either an existing application gateway or **Create an application gateway**.
    2. To create a new gateway, type the name for the application gateway. The Application Gateway can load balance multiple applications. Consider naming the Application Gateway according to the workloads you wish to load balance, rather than specific to the virtual machine name.
    3. In **Routing rule**, type a rule name. The rule name should describe the workload you are load balancing.
    4. For HTTP load balancing, you can leave the defaults and then select **Create**. For HTTPS load balancing, you have two options:

    - Upload a certificate and add the password (application gateway manages certificate storage). For certificate name, type a friendly name for the certificate.
    - Use a key vault (application gateway will pull a defined certificate from a defined key vault). Select your **Managed identity**, **Key Vault**, and **Certificate**.

    Important

    After the VMs and application gateway are deployed, log in to the VMs to ensure that either the application gateway certificate is uploaded onto the VMs or the domain name of the VM certificate matches with the domain name of the application gateway.

    Note

    A separate subnet will be defined for Application Gateway upon creation. For more information, see [Application Gateway infrastructure configuration](/en-us/azure/application-gateway/configuration-infrastructure).
9. Leave the remaining defaults and then select the **Review + create** button at the bottom of the page.
10. On the **Create a virtual machine** page, you can see the details about the VM you are about to create. When you're ready, select **Create**.
11. If you are creating a Linux VM and the **Generate new key pair** window opens, select **Download private key and create resource**. Your key file will download as **myKey.pem**.
12. When the deployment is finished, select **Go to resource**.