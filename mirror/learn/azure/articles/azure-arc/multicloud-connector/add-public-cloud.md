---
layout: Conceptual
title: Add a public cloud with the multicloud connector in the Azure portal - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/multicloud-connector/add-public-cloud
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
description: Learn how to add an AWS or GCP cloud by using the multicloud connector enabled by Azure Arc.
ms.topic: how-to
ms.date: 2026-11-10T00:00:00.0000000Z
locale: en-us
document_id: 59494af0-2a5d-37aa-aa72-6a0150a45716
document_version_independent_id: 7c1a2a1a-378c-0f90-89d5-44c7b73da9f3
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/multicloud-connector/add-public-cloud.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/multicloud-connector/add-public-cloud
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/multicloud-connector/add-public-cloud.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 6542295a-8747-c352-395e-139d0a48d44f
---

# Add a public cloud with the multicloud connector in the Azure portal - Azure Arc | Microsoft Learn

The multicloud connector enabled by Azure Arc lets you connect non-Azure public cloud resources to Azure by using the Azure portal. Currently, the multicloud connector provides support for connecting resources from these public clouds:

- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

## Prerequisites

To use the multicloud connector, you need the appropriate permissions in both your source cloud (AWS or GCP) and in Azure.

# [AWS](#tab/aws)
When you upload your CloudFormation template, more permissions are requested, based on the solutions that you selected:

- For **Inventory**, you can choose your permission:

    1. **Global Read**: Provides read-only access to all resources in the AWS account. When new services are introduced, the connector can scan for those resources without requiring an updated CloudFormation template.
    2. **Least Privilege Access**: Provides read access to only the resources under the selected services. If you choose to scan for more resources in the future, a new CloudFormation template must be uploaded.
- For **Arc EC2 Onboarding**, our service requires **EC2 Read & Write** access in order to install the [Azure Connected Machine agent](/en-us/azure/azure-arc/servers/agent-overview). You must also meet the [additional prerequisites for the](onboard-multicloud-vms-arc#prerequisites)**[Arc onboarding](onboard-multicloud-vms-arc#prerequisites)**[solution](onboard-multicloud-vms-arc#prerequisites).
- For **Arc EKS Onboarding**, our service requires **EKS Read & Write** access in order to install the [Arc-enabled Kubernetes agent](/en-us/azure/azure-arc/kubernetes/conceptual-agent-overview). You must also meet the [additional prerequisites for the](onboard-multicloud-vms-arc#prerequisites)**[Arc onboarding](onboard-multicloud-vms-arc#prerequisites)**[solution](onboard-multicloud-vms-arc#prerequisites).

# [GCP](#tab/gcp)
When you upload your Terraform template, more permissions are requested, based on the solutions that you selected.

- For **Inventory**, you can choose your permission:

    1. **Global Read**: Provides read-only access to all resources in the GCP project. When new services are introduced, the connector can scan for those resources without requiring an updated Terraform template.
    2. **Least Privilege Access**: Provides read access to only the resources under the selected services. If you choose to scan for more resources in the future, a new Terraform template must be uploaded.
- For **Arc Onboarding**, our service requires **OSPolicyAssignment Admin** access in order to install the [Azure Connected Machine agent](/en-us/azure/azure-arc/servers/agent-overview). You must also meet the [additional prerequisites for the **Arc onboarding** solution](onboard-multicloud-vms-arc#prerequisites).

---

### Azure prerequisites

To use the multicloud connector in an Azure subscription, you need the **Contributor** built-in role.

If this is the first time you're using the service, you need to [register these resource providers](/en-us/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider), which requires **Contributor** access on the subscription:

- Microsoft.HybridCompute
- Microsoft.HybridConnectivity
- Microsoft.AwsConnector
- Microsoft.Kubernetes

Note

The multicloud connector can work side-by-side with Defender for Cloud support for [AWS accounts](/en-us/azure/defender-for-cloud/quickstart-onboard-aws) and [GCP projects](/en-us/azure/defender-for-cloud/quickstart-onboard-gcp). If you choose, you can use these connectors together.

## Add your public cloud in the Azure portal

# [AWS](#tab/aws)
To add your AWS public cloud to Azure, use the Azure portal to enter details and generate a CloudFormation template.

1. In the Azure portal, navigate to **Azure Arc**.
2. Under **Management**, select **Multicloud connectors**.
3. In the **Connectors** pane, select **Create** and choose **Create AWS connector**.
4. On the **Basics** page:

    1. Select the subscription and resource group in which to create your connector resource.
    2. Enter a unique name for the connector and select a [supported region](overview#supported-regions).
    3. Provide the ID for the AWS account that you want to connect, and indicate whether it's a single account or an organization account.
    4. Select **Next**.
5. On the **Solutions** page, select which solutions you'd like to use with this connector and configure them. Select **Add** to enable **[Inventory](view-multicloud-inventory)**, **[Arc onboarding](onboard-multicloud-vms-arc)**, or **Storage - Data Management**.

    [![Screenshot showing the Solutions for the AWS connector in the Azure portal.](media/add-aws-connector-solutions.png)](media/add-aws-connector-solutions.png#lightbox)

    - For **Inventory**, you can modify the following options:

        1. Choose whether or not to enable **Add all supported AWS services.** By default, this option is enabled, so that all services (available now and services added in the future) are scanned.
        2. Choose the **AWS Services** for which you want to scan and import resources. By default, all available services are selected.
        3. Choose your permissions. If **Add all supported AWS services** is checked, you must have **Global read** access.
        4. Choose whether or not to enable periodic sync. By default, this option is enabled so that the connector scans your AWS account regularly. If you uncheck the box, your AWS account is scanned only once.
        5. If **Enable periodic sync** is checked, confirm or change the **Recur every** selection to specify how often your AWS account are scanned.
        6. Choose whether or not to enable **Include all supported AWS regions**. By selecting this option, all current and future AWS regions are scanned.
        7. Choose which regions to scan for resources in your AWS account. By default, all available regions are selected. If you selected **Include all supported AWS regions**, all regions must be selected.
        8. When you have finished making selections, select **Save** to return to the **Solutions** page.
    - For **Arc onboarding**:

        1. For connectivity, public endpoints will be used by default. You can optionally update your **Connectivity method** to use a proxy server or Arc gateway by providing those details.
        2. Choose whether or not to enable periodic sync. By default, this option is enabled so that the connector scans your AWS account regularly. If you uncheck the box, your AWS account is scanned only once.
        3. If **Enable periodic sync** is checked, confirm or change the **Recur every** selection to specify how often your AWS account is scanned.
        4. Choose whether or not to enable **Include all supported AWS regions**. By selecting this option, all current and future AWS regions are scanned.
        5. Choose which regions to scan for EC2 or EKS instances in your AWS account. By default, all available regions are selected. If you selected **Include all supported AWS regions**, all regions must be selected.
        6. Choose to filter for EC2 or EKS instances by AWS tag. If you enter a tag value here, only EC2 or EKS instances that contain that tag are onboarded to Arc. By leaving this value empty, all EC2 or EKS Instances discovered are onboarded to Arc.
    - For **Storage - Data management**, you must first add **Inventory** with the S3 service selected. No other settings are required.
6. On the **Authentication template** page, download the CloudFormation template that you'll upload to AWS. This template is created based on the information you provided in **Basics** and the solutions you selected. You can upload the template right away, or wait until you finish adding your public cloud.
7. On the **Tags** page, enter any tags you'd like to use.
8. On the **Review and create** page, confirm your information, then select **Create**.

If you didn't upload your template during this process, follow the steps in the next section to do so.

### Upload CloudFormation template to AWS

After you save the CloudFormation template generated in the previous section, you need to upload it to your AWS public cloud. If you upload the template before you finish connecting your AWS cloud in the Azure portal, your AWS resources are scanned immediately. If you complete the **Add public cloud** process in the Azure portal before uploading the template, it takes a bit longer to scan your AWS resources and make them available in Azure.

### Create stack

Follow these steps to create a stack and upload your template:

1. Open the AWS CloudFormation console and select **Create stack**.
2. Select **Template is ready**, then select **Upload a template file**. Select **Choose file** and browse to select your template. Then select **Next**.
3. In **Specify stack details**, enter a stack name.

    1. If you selected the **Arc Onboarding** solution, fill out the following details in the Stack parameters:

        1. **EC2SSMIAMRoleAutoAssignment**: Specifies whether IAM roles used for SSM tasks are automatically assigned to EC2 instances. By default this option is set to *true*, and all discovered EC2 machines will have the IAM role assigned. If you set this option to *false,* you must manually assign the IAM role to the EC2 instances that you want onboarded to Arc.
        2. **EC2SSMIAMRoleAutoAssignmentSchedule**: Specifies whether the EC2 IAM Role used for SSM tasks should be autoassigned periodically. By default, this option is set to *enable,* meaning that any EC2 machines discovered in the future will have the IAM role automatically assigned. If you set this option to *disable,* you must manually assign the IAM role to any newly deployed EC2 that you want onboarded to Azure Arc.
        3. **EC2SSMIAMRoleAutoAssignmentScheduleInterval**: Specifies the periodic interval for autoassignment of the EC2 IAM Role used for SSM tasks (for example, 15 minutes, 6 hours, or 1 day). If you set the **EC2SSMIAMRoleAutoAssignment** to *true* and **EC2SSMIAMRoleAutoAssignmentSchedule** to *enable*, you can choose how often you want to scan for new EC2 instances to be assigned the IAM role. The default interval is *1 day*.
        4. **EC2SSMIAMRolePolicyUpdateAllowed**: Specifies whether existing EC2 IAM roles used for SSM tasks are allowed to update with required permission policies if they're missing. By default, this option is set to *true*. If you choose to set to *false*, you must manually add this IAM role permission to the EC2 instance.
    2. Otherwise, leave the other options set to their default settings and select **Next**.
4. In **Configure stack options**, leave the options set to their default settings and select **Next**.
5. In **Review and create**, confirm that the information is correct, select the acknowledgment checkbox, and then select **Submit**.

### Create StackSet

If your AWS account is an organization account, you also need to create a StackSet and upload your template again. To do so:

1. Open the AWS CloudFormation console and select **StackSets**, then select **Create StackSet**.
2. Select **Template is ready**, then select **Upload a template file**. Select **Choose file** and browse to select your template. Then select **Next**.
3. In **Specify stack details**, enter `AzureArcMultiCloudStackset` as the StackSet name

    1. If you selected the **Arc Onboarding** solution, fill out the following details in the Stack parameters:

        1. **EC2SSMIAMRoleAutoAssignment**: Specifies whether IAM roles used for SSM tasks are automatically assigned to EC2 instances. By default this option is set to *true*, and all discovered EC2 machines will have the IAM role assigned. If you set this option to *false,* you must manually assign the IAM role to the EC2 instances that you want onboarded to Arc.
        2. **EC2SSMIAMRoleAutoAssignmentSchedule**: Specifies whether the EC2 IAM Role used for SSM tasks should be autoassigned periodically. By default, this option is set to *enable,* meaning that any EC2 machines discovered in the future will have the IAM role automatically assigned. If you set this option to *disable,* you must manually assign the IAM role to any newly deployed EC2 instance that you want onboarded to Arc.
        3. **EC2SSMIAMRoleAutoAssignmentScheduleInterval**: Specifies the periodic interval for autoassignment of the EC2 IAM Role used for SSM tasks (such as, 15 minutes, 6 hours, or 1 day). If you set the **EC2SSMIAMRoleAutoAssignment** to *true* and **EC2SSMIAMRoleAutoAssignmentSchedule** to *enable*, you can choose how often you want to scan for new EC2 instances to be assigned the IAM role. The default interval is *1 day*.
        4. **EC2SSMIAMRolePolicyUpdateAllowed**: Specifies whether existing EC2 IAM roles used for SSM tasks are allowed to update with required permission policies if they're missing. By default, this option is set to *true*. If you choose to set to *false*, you must manually add this IAM role permission to the EC2 instance.
    2. Otherwise, leave the other options set to their default settings and select **Next**.
4. In **Configure stack options**, leave the options set to their default settings and select **Next**.
5. In **Set deployment options**, enter the ID for the AWS account where the StackSet will be deployed, and select any AWS region to deploy the stack. Optionally, you can choose to **Deploy to organizational units (OUs)** in the **Deployment Targets** section if you prefer the connector to only scan accounts associated with specific OUs. Leave the other options set to their default settings and select **Next**.
6. In **Review**, confirm that the information is correct, select the acknowledgment checkbox, and then select **Submit**.

# [GCP](#tab/gcp)
To add your GCP public cloud to Azure, use the Azure portal to enter details and generate a Terraform template.

1. In the Azure portal, navigate to **Azure Arc**.
2. Under **Management**, select **Multicloud connectors**.
3. In the **Connectors** pane, select **Create** and choose **Create GCP connector**.
4. On the **Basics** page:

    1. Select the subscription and resource group in which to create your connector resource.
    2. Enter a unique name for the connector and select a [supported region](overview#supported-regions).
    3. Provide the **Project ID** and **Project Number** for the GCP project that you want to connect. If you connect an organization account, provide the **Organization ID**.
    4. Select **Next**.
5. On the **Solutions** page, select which solutions you'd like to use with this connector and configure them. Select **Add** to enable **[Inventory](view-multicloud-inventory)**, **[Arc onboarding](onboard-multicloud-vms-arc)**, or both.

    [![Screenshot showing the Solutions for the GCP connector in the Azure portal.](media/add-google-cloud-platform-solutions.png)](media/add-google-cloud-platform-solutions.png#lightbox)

    - For **Inventory**, you can modify the following options:

        1. Choose whether or not to enable **Onboard all supported GCP services.** By default, this option is enabled, so that all services (available now and services added in the future) are scanned.
        2. Choose the **GCP Services** for which you want to scan and import resources. By default, all available services are selected.
        3. Choose your permissions. If **Onboard all supported GCP services** is checked, you must have **Global read** access.
        4. Choose whether or not to enable periodic sync. By default, this option is enabled so that the connector scans your GCP project regularly. If you uncheck the box, your GCP project is scanned only once.
        5. If **Enable periodic sync** is checked, confirm or change the **Recur every** selection to specify how often your GCP project are scanned.
        6. Choose whether or not to enable **Include all supported GCP regions**. By selecting this option, all current and future GCP regions are scanned.
        7. Choose which regions to scan for resources in your GCP project. By default, all available regions are selected. If you selected **Include all supported GCP regions**, all regions must be selected.
        8. When you have finished making selections, select **Save** to return to the **Solutions** page.
    - For **Arc onboarding**:

        Note

        The **Arc onboarding** solution uses the VM manager on GCP to enforce policies on your VMs through the OS Config agent. A VM that has an active OS Config agent incurs a cost according to GCP. To see how this cost might affect your account, refer to the GCP technical documentation.

        1. For connectivity, public endpoints will be used by default. You can optionally update your **Connectivity method** to use a proxy server or gateway by providing those details.
        2. Choose whether or not to enable periodic sync. By default, this option is enabled so that the connector scans your GCP project regularly. If you uncheck the box, your GCP project is scanned only once.
        3. If **Enable periodic sync** is checked, confirm or change the **Recur every** selection to specify how often your GCP project is scanned.
        4. Choose whether or not to enable **Include all supported GCP regions**. By selecting this option, all current and future GCP regions are scanned.
        5. Choose which regions to scan for VM instances in your GCP project. By default, all available regions are selected. If you selected **Include all supported GCP regions**, all regions must be selected.
        6. Choose to filter for VM instances by GCP label. If you enter a label value here, only VM instances that contain that label are onboarded to Arc. By leaving this value empty, all VM instances discovered are onboarded to Arc.
        7. When you have finished making selections, select **Save** to return to the **Solutions** page.
6. On the **Configure Access** page, download the Terraform template that you'll upload to GCP. This template is created based on the information you provided in **Basics** and the solutions you selected. You can upload the template right away, or wait until you finish adding your public cloud.
7. On the **Tags** page, enter any tags you'd like to use.
8. On the **Review and create** page, confirm your information, then select **Create**.

If you didn't upload your template during this process, follow the steps in the next section to do so.

### Upload Terraform template to GCP

After you save the Terraform template generated in the previous section, you need to run the Terraform commands in your GCP environment. If you run the Terraform commands before you finish connecting your GCP cloud in the Azure portal, your GCP resources are scanned immediately. If you complete the **Add public cloud** process in the Azure portal before uploading the template, it takes a bit longer to scan your GCP resources and make them available in Azure.

### Configure GCP access

Follow these steps to run the Terraform template you downloaded:

1. Open the GCP Console and start Cloud Shell.
2. Navigate to any directory or folder and upload the saved Terraform template.
3. Execute the following commands:

    ```terraform
    terraform init
    terraform plan -out tf.plan
    terraform apply tf.plan
    ```

    Optionally, you can run these commands locally or in the Azure Cloud Shell. The additional requirement is to download the [gCloud CLI](https://cloud.google.com/sdk/gcloud/). You will need to authenticate with your GCP credentials.

For help with any issues related to access configuration, see [Troubleshoot multicloud connector enabled by Azure Arc](troubleshoot-multicloud-connector).

---

## Confirm deployment

After you complete the **Add public cloud** option in Azure and upload your template to AWS or GCP, your connector and selected solutions are created. On average, it takes about one hour for your AWS or GCP resources to become available in Azure. If you upload the template after creating the public cloud in Azure, it may take a bit more time before you see the resources.

Resources are stored in a resource group using the naming convention `<PublicCloud>_<AccountId>`, with permissions inherited from its subscription. Scans run regularly to update these resources, based on your **Enable periodic sync** selections.

## Clean up GCP connector resources

Use the Terraform configuration and state associated with your connector deployment to remove connector-specific resources from GCP. Confirm that you're using the correct GCP project, Terraform backend, and workspace before continuing. These steps address GCP-side Terraform resources; verify deletion of the Azure connector separately.

### Retain shared GCP APIs

Enable GCP APIs at the project level so workloads other than the multicloud connector can use them. Retain shared APIs when removing the connector, including:

- Kubernetes Engine API (`container.googleapis.com`)
- Identity and Access Management API (`iam.googleapis.com`)
- IAM Service Account Credentials API (`iamcredentials.googleapis.com`)

For the corresponding `google_project_service` resources in your Terraform configuration, explicitly set:

```hcl
disable_on_destroy         = false
disable_dependent_services = false
```

Make this change **before cleanup**, and review and apply the configuration update so Terraform records the retention setting in its state. Confirm that the update doesn't introduce unintended changes before applying it.

Then generate, review, and apply a destroy plan:

```sh
terraform plan -destroy -out=destroy.tfplan
terraform show destroy.tfplan
terraform apply "destroy.tfplan"
```

Warning

Don't set `disable_dependent_services = true` or forcibly disable dependent APIs to complete connector cleanup. Disabling shared APIs and their dependent services can disrupt unrelated workloads, including Google Kubernetes Engine (GKE) and Filestore.

### Recover from a partially successful destroy

Terraform destroy can delete connector-specific resources and then fail when attempting to disable an API that other enabled services depend on. A dependency error doesn't roll back resources that Terraform already deleted. However, don't assume that Terraform removed all connector resources. Inspect the remaining state and verify the actual resources.

1. In the original deployment directory, confirm the backend, workspace, and GCP project. Back up the current state:

    ```sh
    terraform state pull > terraform-state-backup.json
    ```

    Store the backup securely because Terraform state can contain sensitive information.
2. List the remaining resources and inspect each relevant entry:

    ```sh
    terraform state list
    terraform state show '<resource-address>'
    ```

    Replace `<resource-address>` with the exact address returned by `terraform state list`. Check the resource type, project, and service name. Distinguish shared API enablement entries (`google_project_service`) from remaining connector-specific resources.
3. For each shared API you intentionally want to retain, remove only its exact resource instance from Terraform state:

    ```sh
    terraform state rm -dry-run '<api-resource-address>'
    terraform state rm '<api-resource-address>'
    ```

    Replace `<api-resource-address>` with the exact API resource instance address verified in the previous step. These examples use Cloud Shell quoting.

    Removing an entry from state stops Terraform from managing it; it doesn't disable the API. Don't remove connector-specific resources from state as a substitute for deleting them, and don't remove the entire state file.
4. Generate and review a new destroy plan for any remaining connector resources:

    ```sh
    terraform plan -destroy -out=destroy-recovery.tfplan
    terraform show destroy-recovery.tfplan
    ```

    Apply the plan only after confirming that it targets the intended resources and doesn't disable shared APIs you want to retain:

    ```sh
    terraform apply "destroy-recovery.tfplan"
    ```

    Don't reuse the original saved plan after a partial apply or state change.

Important

Don't run a normal `terraform apply` against the original deployment configuration during recovery. It can recreate deleted connector resources or resume management of API entries removed from state.

### Verify cleanup

After recovery, complete the following checks:

1. Run `terraform state list` and generate a fresh destroy plan:

    ```sh
    terraform state list
    terraform plan -destroy
    ```

    For a state dedicated to the connector, no managed resources should remain and the destroy plan should report no changes.

    If the state also manages unrelated infrastructure, preserve those resources. Verify that connector-specific entries are absent, and don't apply a destroy plan that targets unrelated resources.
2. Verify in GCP that the connector-specific resources identified in the original configuration, such as service accounts, IAM bindings, and workload identity resources, are removed. An empty Terraform state alone doesn't prove that resources were deleted.
3. Confirm that intentionally retained APIs remain enabled:

    ```sh
    gcloud services list --enabled --project=PROJECT_ID
    ```

    Replace `PROJECT_ID` with your GCP project ID.
4. Verify separately that the Azure multicloud connector is deleted if you're removing the connection entirely.

Note

Intentionally retained GCP APIs don't indicate that connector resources remain. API enablement is project-wide and is separate from the connector-specific resources and permissions used to access your project.