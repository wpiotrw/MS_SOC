---
layout: Conceptual
title: Connect Arc-enabled servers using TPM-backed identity - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/tpm-backed-identity
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
description: Learn how to connect Azure Arc-enabled servers using TPM-backed identity.
ms.topic: how-to
ms.date: 2026-10-18T00:00:00.0000000Z
ai-usage: ai-generated
locale: en-us
document_id: 541b9988-f159-c236-4142-fdaec34a7bfe
document_version_independent_id: b98179a6-1e17-d12d-0aea-fb7069dde5f7
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/tpm-backed-identity.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/tpm-backed-identity
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/tpm-backed-identity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: e3d05c18-386c-cd08-a101-d3af923bf0ff
---

# Connect Arc-enabled servers using TPM-backed identity - Azure Arc | Microsoft Learn

Trusted Platform Module (TPM)-backed identity provides extra protection for the managed identity credentials that Azure Arc-enabled servers use.

By default, the Azure Connected Machine agent stores the machine's managed identity credential material on the local disk, protected by operating system access controls. When you use TPM-backed identity, the agent uses the machine's physical TPM or virtual TPM (vTPM) as a hardware-backed root of trust. The TPM secures the managed identity credentials against exfiltration, including by privileged users.

In this article, you learn how to:

- Check whether a machine is ready to use TPM-backed Identity.
- Enable TPM or vTPM when required.
- Connect one or more machines to Azure Arc by using TPM-backed identity.
- Verify that TPM-backed identity is enabled.

## Supported scenarios

TPM-backed identity supports connecting one or more new machines to Azure Arc and securing their managed identity credentials by using the machine's TPM or vTPM.

Migrating an existing Arc-enabled server from file-based credential storage to TPM-backed credential storage while retaining the same system-assigned managed identity isn't currently supported.

## Prerequisites

Before you begin, ensure that:

- The machine has a TPM or vTPM that implements TPM 2.0, is enabled and operational, and has the storage and endorsement hierarchies enabled. Validate this condition by using the `azcmagent check` command described in the next section.
- Azure Connected Machine agent version 1.69 or later is installed.
- You have administrator or root permissions on the machine.

## Check TPM readiness

Before connecting the machine, run the following command from an elevated terminal:

```azurecli
azcmagent check tpm
```

The command reads the machine's TPM state and determines whether the TPM is ready for Azure Arc onboarding. It doesn't change the machine's TPM configuration.

A TPM is considered ready when it is:

- Present.
- Operational.
- Using TPM specification version 2.0.
- Configured with the storage hierarchy enabled.
- Configured with the endorsement hierarchy enabled.

The command also returns the TPM manufacturer and Endorsement Key certificate information. An Endorsement Key certificate isn't required for onboarding.

If the command returns `Ready`, continue to connect the machine using TPM-backed identity. If it returns `Not Ready`, enable or configure the TPM before continuing.

## Enable TPM or vTPM

The process of enabling TPM depends on where the machine is running. After completing the applicable procedure, restart the machine and run `azcmagent check tpm` again.

# [Windows and Linux physical machines](#tab/physical)
[Enable TPM 2.0](https://support.microsoft.com/en-us/windows/enable-tpm-2-0-on-your-pc-1fd5a332-360d-4f46-a1e7-ae6b0c90645c) in the machine's UEFI or BIOS configuration. The available settings and their names vary by hardware manufacturer.

# [Hyper-V virtual machines](#tab/hyper-v)
The Hyper-V virtual machine must be a Generation 2 virtual machine.

1. Shut down the virtual machine.
2. In Hyper-V Manager, open the virtual machine settings.
3. Select **Security**.
4. Enable **Secure Boot** if it isn't already enabled.
5. Enable **Trusted Platform Module**.
6. Start the virtual machine.

For more information about enabling vTPM on Hyper-V, see [Enable-VMTPM](/en-us/powershell/module/hyper-v/enable-vmtpm).

# [Google Cloud virtual machines](#tab/google-cloud)
1. Stop the virtual machine instance.
2. Open the virtual machine configuration and select **Edit**.
3. Under **Security and access**, locate **Shielded VM**.
4. Enable **Turn on vTPM**.
5. Save the configuration and start the virtual machine.

For more information about enabling vTPM on Google Cloud, see [Modifying Shielded VM options on a VM instance](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).

# [AWS virtual machines](#tab/aws)
Amazon EC2 automatically enables NitroTPM when you launch an instance with a supported Amazon Machine Image (AMI) and instance type. You can't enable NitroTPM on an existing instance.

Before you launch the instance, review the requirements for:

- Supported AMIs: See [Windows AMIs](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ami-windows-tpm.html#ami-windows-tpm-find) or [Linux AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-support-on-ami.html).
- Supported instance types: See [Requirements for using NitroTPM with Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-prerequisites.html#nitrotpm-instancetypes).

For more information, see [Enable or stop using NitroTPM on an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-instance.html).

# [VMware virtual machines](#tab/vmware)
Before you begin, configure a key provider in vSphere and make sure the virtual machine uses EFI firmware.

To enable vTPM when you create a virtual machine:

1. In the vSphere Client, start the **New Virtual Machine** wizard.
2. On the **Customize hardware** page, select **Add New Device** &gt; **Trusted Platform Module**.
3. Complete the wizard to create the virtual machine.

For more information, see [Create a Virtual Machine with a Virtual Trusted Platform Module](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security/securing-virtual-machines-with-virtual-trusted-platform-module/add-a-virtual-trusted-platform-module-to-a-virtual-machine.html).

To enable vTPM on an existing virtual machine:

1. Shut down the virtual machine.
2. In the vSphere Client, right-click the virtual machine and select **Edit Settings**.
3. On the **Virtual Hardware** tab, select **Add New Device** &gt; **Trusted Platform Module**.
4. Select **OK** to save the changes, and then start the virtual machine.

For more information, see [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security/securing-virtual-machines-with-virtual-trusted-platform-module/enable-vtpm-for-an-existing-virtual-machine.html).

---

## Connect the machine using TPM-backed identity

Use the `--identity-key-store` flag during onboarding to configure how the machine stores its managed identity credentials. The flag supports two values for TPM:

- **`tpm`**: Onboards the machine only by using TPM-backed identity. If a compatible TPM or vTPM isn't enabled and ready, onboarding fails.
- **`auto`**: Checks the machine for TPM readiness first, and if available, onboards with TPM. Otherwise, continues onboarding by using the file-based method.

```azurecli
--identity-key-store "tpm"
```

The examples in this section use `--identity-key-store tpm` to require TPM-backed identity.

If onboarding fails with a TPM-related error, see [Azure Connected Machine agent error codes](troubleshoot-agent-onboard#agent-error-codes) for troubleshooting steps.

### azcmagent CLI

Run the following command from an elevated terminal. Replace the placeholder values with your Azure subscription, resource group, tenant, and region:

```azurecli
azcmagent connect \
  --subscription-id "<subscription-id>" \
  --resource-group "<resource-group>" \
  --tenant-id "<tenant-id>" \
  --location "<region>" \
  --identity-key-store "tpm"
```

### Azure portal

You can enable TPM-backed identity when you generate an onboarding script in the Azure portal.

1. In the Azure portal, search for and select **Azure Arc**.
2. In the service menu, expand **Infrastructure**, and then select **Machines**.
3. Select **Onboard/Create**, and then select **Onboard existing machines**.
4. On the **Basics** tab, select your subscription, resource group, region, and operating system.
5. Under **TPM-backed Identity**, select the checkbox labeled **Onboard with a Trusted Platform Module (TPM) for additional security**.

    ![Screenshot of the Azure Arc onboarding page with the TPM-backed Identity option highlighted.](media/trusted-platform-module-identity/trusted-platform-module-identity-configuration.png)
6. Complete the remaining onboarding settings, and then download and run the generated script on the machine. For detailed instructions, see [Connect hybrid machines to Azure from the Azure portal](onboard-portal).

Note

To connect machines by using TPM-backed identity, you can also use any of the [at-scale onboarding methods](onboard-service-principal).

## Verify TPM-backed identity

After the connection finishes, confirm that the Arc-enabled server resource is connected. Then verify that TPM-backed identity is enabled by using one of the following methods.

# [Azure portal](#tab/azure-portal)
1. In the Azure portal, go to your Arc-enabled server.
2. Select **Properties**.

    ![Screenshot of the Arc-enabled server page with the Properties tab highlighted.](media/trusted-platform-module-identity/server-properties-tab.png)
3. Under **Agent status**, confirm that **Trusted Platform Module (TPM) backed Identity** is **Yes**.

    ![Screenshot of Agent status showing Trusted Platform Module (TPM) backed Identity set to Yes.](media/trusted-platform-module-identity/trusted-platform-module-identity-agent-status.png)

# [Azure Resource Graph](#tab/arg)
Use [Azure Resource Graph Explorer](/en-us/azure/governance/resource-graph/first-query-portal) in the Azure portal to find Arc-enabled servers that use TPM-backed identity across your selected subscriptions.

1. In the Azure portal, open **Resource Graph Explorer**.
2. Set the query scope to the subscriptions or resource groups that contain your Arc-enabled servers.
3. Run the following query:

    ```kusto
    resources
    | where type =~ 'microsoft.hybridcompute/machines'
    | where properties.identityKeyStore == 'Tpm'
    | project name, resourceGroup, subscriptionId, identityKeyStore = tostring(properties.identityKeyStore)
    | order by name asc
    ```
4. Confirm that your server appears in the results. The query returns only servers whose **identityKeyStore** value is **Tpm**.

# [Azure CLI](#tab/azure-cli)
Run the following command, replacing the placeholder values with your subscription ID, resource group, and machine name:

```azurecli
az resource show --ids "/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.HybridCompute/machines/<machine-name>" --query "properties.identityKeyStore" --output tsv
```

# [azcmagent CLI](#tab/azcmagent-cli)
On the machine, run the following command:

```azurecli
azcmagent show
```

---