---
layout: Conceptual
title: 'Quickstart: Deploy a JBoss EAP cluster on Azure Virtual Machines (VMs) - Azure Virtual Machines | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/redhat/jboss-eap-azure-vm
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
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: jiangma
description: Shows you how to quickly stand up a JBoss EAP cluster on Azure Virtual Machines.
author: MarckK
ms.author: kdelamarck
ms.topic: quickstart
ms.date: 2026-03-26T00:00:00.0000000Z
ms.service: azure-virtual-machines
ms.custom:
- devx-track-java
- devx-track-extended-java
- devx-track-javaee
- devx-track-javaee-jbosseap
- devx-track-javaee-jbosseap-vm
- devx-track-azurecli
- linux-related-content
- sfi-image-nochange
locale: en-us
document_id: 9738a189-c6ff-1194-a392-efa86aeea22a
document_version_independent_id: 406db07f-6129-1de6-07cd-8886053d8422
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/workloads/redhat/jboss-eap-azure-vm.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/workloads/redhat/jboss-eap-azure-vm
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/workloads/redhat/jboss-eap-azure-vm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/982661b3-cc41-45b1-b21d-18b4b6937344
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bbee35d0-ba85-4062-b9c2-388c328eb4fa
platformId: c11d68c1-f61e-64dc-fff7-295c1d3e6518
---

# Quickstart: Deploy a JBoss EAP cluster on Azure Virtual Machines (VMs) - Azure Virtual Machines | Microsoft Learn

This article shows you how to quickly deploy a JBoss Enterprise Application Platform (EAP) cluster on Azure Virtual Machines (VMs) using the Azure portal.

This article uses the Azure Marketplace offer for JBoss EAP Cluster to accelerate your journey to Azure VMs. The offer automatically provisions a number of resources including Azure Red Hat Enterprise Linux (RHEL) VMs, JBoss EAP instances on each VM, Red Hat build of OpenJDK on each VM, a JBoss EAP management console, and optionally an Azure App Gateway instance. To see the offer, visit the solution [JBoss EAP Cluster on RHEL VMs](https://aka.ms/eap-vm-cluster-portal) using the Azure portal.

If you prefer manual step-by-step guidance for installing Red Hat JBoss EAP Cluster on Azure VMs that doesn't use the automation enabled by the Azure Marketplace offer, see [Tutorial: Install Red Hat JBoss EAP on Azure Virtual Machines manually](/en-us/azure/developer/java/migration/migrate-jboss-eap-to-azure-vm-manually).

If you're interested in providing feedback or working closely on your migration scenarios with the engineering team developing JBoss EAP on Azure solutions, fill out this short [survey on JBoss EAP migration](https://aka.ms/jboss-on-azure-survey) and include your contact information. The team of program managers, architects, and engineers will promptly get in touch with you to initiate close collaboration.

## Prerequisites

- An Azure subscription. If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- Ensure the Azure identity you use to sign in has either the [Contributor](/en-us/azure/role-based-access-control/built-in-roles#contributor) role or the [Owner](/en-us/azure/role-based-access-control/built-in-roles#owner) role in the current subscription. For an overview of Azure roles, see [What is Azure role-based access control (Azure RBAC)?](/en-us/azure/role-based-access-control/overview)
- A Java Development Kit (JDK), version 17. In this guide, we recommend the [Red Hat Build of OpenJDK](https://developers.redhat.com/products/openjdk/download). Ensure that your `JAVA_HOME` environment variable is set correctly in the shells in which you run the commands.
- [Git](https://git-scm.com/downloads). Use `git --version` to test whether `git` works. This tutorial was tested with version 2.34.1.
- [Maven](https://maven.apache.org/download.cgi). Use `mvn -version` to test whether `mvn` works. This tutorial was tested with version 3.8.6.

Note

The Azure Marketplace offer you're going to use in this article includes support for Red Hat Satellite for license management. Using Red Hat Satellite is beyond the scope of this quickstart. For an overview on Red Hat Satellite, see [Red Hat Satellite](https://aka.ms/red-hat-satellite). To learn more about moving your Red Hat JBoss EAP and Red Hat Enterprise Linux subscriptions to Azure, see [Red Hat Cloud Access program](https://aka.ms/red-hat-cloud-access-overview).

## Set up an Azure Database for PostgreSQL flexible server

The steps in this section direct you to deploy an Azure Database for PostgreSQL flexible server, which you use for configuring the database connection while setting up a JBoss EAP cluster in the next section.

First, use the following command to set up some environment variables.

```bash
export RG_NAME=<db-resource-group-name>
export SERVER_NAME=<database-server-name>
export ADMIN_PASSWORD=<postgresql-admin-password>
```

Replace the placeholders with the following values, which are used throughout the the article:

- `<db-resource-group-name>`: The name of the resource group to use for the PostgreSQL flexible server - for example, `ejb040323postgresrg`.
- `<database-server-name>`: The name of your PostgreSQL server, which should be unique across Azure - for example, `ejb040323postgresqlserver`.
- `<postgresql-admin-password>`: The password of your PostgreSQL server. That password must be at least eight characters and at most 128 characters. The characters should be from three of the following categories: English uppercase letters, English lowercase letters, numbers (0-9), and nonalphanumeric characters (!, $, #, %, and so on).

Note

Microsoft recommends using the most secure authentication flow available. The authentication flow described in this procedure, such as for databases, caches, messaging, or AI services, requires a very high degree of trust in the application and carries risks not present in other flows. Use this flow only when more secure options, like managed identities for passwordless or keyless connections, are not viable. For local machine operations, prefer user identities for passwordless or keyless connections.

Next, use the following steps to create an Azure Database for PostgreSQL flexible server:

1. Use the following command to create an Azure Database for PostgreSQL flexible server:

    ```azurecli
    az postgres flexible-server create \
        --resource-group ${RG_NAME} \
        --name ${SERVER_NAME} \
        --database-name testdb \
        --public-access 0.0.0.0  \
        --admin-user testuser \
        --admin-password ${ADMIN_PASSWORD} \
        --yes
    ```
2. Use the following command to get the host of the PostgreSQL server:

    ```azurecli
    export DB_HOST=$(az postgres flexible-server show \
        --resource-group ${RG_NAME} \
        --name ${SERVER_NAME} \
        --query "fullyQualifiedDomainName" \
        --output tsv)
    ```
3. Use the following command to get the Java Database Connectivity (JDBC) connection URL of the PostgreSQL server:

    ```azurecli
    echo jdbc:postgresql://${DB_HOST}:5432/testdb
    ```

    Note down the output, which you use as the data source connection string of the PostgreSQL server later in this article.

## Deploy a JBoss EAP cluster on Azure VMs

The steps in this section direct you to deploy a JBoss EAP cluster on Azure VMs.

Use the following steps to find the JBoss EAP Cluster on Azure VMs offer:

1. Sign in to the Azure portal by visiting https://aka.ms/publicportal.
2. In the search bar at the top of the Azure portal, enter *JBoss EAP*. In the search results, in the **Marketplace** section, select **JBoss EAP Cluster on VMs**.

    [![Screenshot of the Azure portal showing JBoss EAP Server on Azure VM in the search results.](media/jboss-eap-azure-vm/marketplace-search-results.png)](media/jboss-eap-azure-vm/marketplace-search-results.png#lightbox)
3. In the drop-down menu, ensure **PAYG** is selected.

Alternatively, you can also go directly to the [JBoss EAP Cluster on Azure VMs](https://aka.ms/eap-vm-cluster-portal) offer. In this case, the correct plan is already selected for you.

In either case, this offer deploys a JBoss EAP cluster on Azure VMs by providing your Red Hat subscription at deployment time. The offer runs the cluster on Red Hat Enterprise Linux using a pay-as-you-go payment configuration for the base VMs.

The following steps show you how to fill out the **Basics** pane shown in the following screenshot.

[![Screenshot of the Azure portal showing the JBoss EAP Cluster on VMs Basics pane.](media/jboss-eap-azure-vm/portal-basics.png)](media/jboss-eap-azure-vm/portal-basics.png#lightbox)

1. On the offer page, select **Create**.
2. On the **Basics** pane, ensure that the value shown in the **Subscription** field is the same one that has the roles listed in the prerequisites section.
3. In the **Resource group** field, select **Create new** and fill in a value for the resource group. Because resource groups must be unique within a subscription, pick a unique name. An easy way to have unique names is to use a combination of your initials, today's date, and some identifier. For example, *ejb040323jbosseapcluster*.
4. Under **Instance details**, select the region for the deployment.
5. Leave the default VM size for **Virtual machine size**.
6. Leave the default option **OpenJDK 17** for **JDK version**.
7. Leave the default value **jbossuser** for **Username**.
8. Leave the default option **Password** for **Authentication type**.
9. Provide a password for **Password**. Use the same value for **Confirm password**.
10. Use *3* for **Number of virtual machines to create**.
11. Under **Optional Basic Configuration**, leave the default option **Yes** for **Accept defaults for optional configuration**.
12. Scroll to the bottom of the **Basics** pane and notice the helpful links for **Report issues, get help, and share feedback**.
13. Select **Next: JBoss EAP Settings**.

The following steps show you how to fill out the **JBoss EAP Settings** pane shown in the following screenshot.

[![Screenshot of the Azure portal showing the JBoss EAP Cluster on VMs JBoss EAP Settings pane.](media/jboss-eap-azure-vm/portal-jboss-eap-settings.png)](media/jboss-eap-azure-vm/portal-jboss-eap-settings.png#lightbox)

1. Leave the default option **Managed domain** for **Use managed domain or standalone hosts to form a cluster**.
2. Leave the default value **jbossadmin** for **JBoss EAP Admin username**.
3. Provide a JBoss EAP password for **JBoss EAP password**. Use the same value for **Confirm password**. Save aside the value for later use.
4. Leave the default option **No** for **Connect to an existing Red Hat Satellite Server?**.
5. Select **Next: Azure Application Gateway**.

The following steps show you how to fill out the **Azure Application Gateway** pane shown in the following screenshot.

[![Screenshot of the Azure portal showing the JBoss EAP Cluster on VMs Azure Application Gateway pane.](media/jboss-eap-azure-vm/portal-azure-application-gateway.png)](media/jboss-eap-azure-vm/portal-azure-application-gateway.png#lightbox)

1. Select **Yes** for **Connect to Azure Application Gateway?**.
2. Select **Next: Networking**.

    This pane enables you to customize the virtual network and subnet into which the JBoss EAP cluster deploys. For information about virtual networks, see [Create, change, or delete a virtual network](/en-us/azure/virtual-network/manage-virtual-network). Accept the defaults on this pane.
3. Select **Next: Database**.

The following steps show you how to fill out the **Database** pane shown in the following screenshot, and start the deployment.

[![Screenshot of the Azure portal showing the JBoss EAP Cluster on VMs Database pane.](media/jboss-eap-azure-vm/portal-database.png)](media/jboss-eap-azure-vm/portal-database.png#lightbox)

1. Select **Yes** for **Connect to database?**.
2. Select **PostgreSQL** for **Choose database type**.
3. Fill in *java:jboss/datasources/JavaEECafeDB* for **JNDI name**.
4. Provide the JDBC connection URL of the PostgreSQL server, which you saved before, for **Data source connection string (jdbc:postgresql://&lt;host&gt;:&lt;port&gt;/&lt;database&gt;)**.
5. Fill in *testuser* for **Database username**.
6. Provide the value for the placeholder `<postgresql-admin-password>`, which you specified before, for **Database password**. Use the same value for **Confirm password**.
7. Select **Review + create**. Ensure that the green **Validation Passed** message appears at the top. If the message doesn't appear, fix any validation problems, then select **Review + create** again.
8. Select **Create**.
9. Track the progress of the deployment on the **Deployment is in progress** page.

Depending on network conditions and other activity in your selected region, the deployment may take up to 35 minutes to complete. After that, you should see the text **Your deployment is complete** displayed on the deployment page.

## Verify the functionality of the deployment

Use the following steps to verify the functionality of the deployment for a JBoss EAP cluster on Azure VMs from the **Red Hat JBoss Enterprise Application Platform** management console:

1. On the deployment page, select **Outputs**.
2. Select the copy icon next to **adminConsole**.

    [![Screenshot of the Azure portal showing the deployment outputs with the adminConsole URL highlighted.](media/jboss-eap-azure-vm/rg-deployments-outputs.png)](media/jboss-eap-azure-vm/rg-deployments-outputs.png#lightbox)
3. Paste the URL into an internet-connected web browser and press Enter. You should see the familiar **Red Hat JBoss Enterprise Application Platform** management console sign-in screen, as shown in the following screenshot.

    [![Screenshot of the JBoss EAP management console sign-in screen.](media/jboss-eap-azure-vm/jboss-eap-console-login.png)](media/jboss-eap-azure-vm/jboss-eap-console-login.png#lightbox)
4. Fill in *jbossadmin* for **JBoss EAP Admin username** Provide the value for **JBoss EAP password** that you specified before for **Password**, then select **Sign in**.
5. You should see the familiar **Red Hat JBoss Enterprise Application Platform** management console welcome page as shown in the following screenshot.

    [![Screenshot of JBoss EAP management console welcome page.](media/jboss-eap-azure-vm/jboss-eap-console-welcome.png)](media/jboss-eap-azure-vm/jboss-eap-console-welcome.png#lightbox)
6. Select the **Runtime** tab. In the navigation pane, select **Topology**. You should see that the cluster contains one domain controller **master** and two worker nodes, as shown in the following screenshot:

    [![Screenshot of the JBoss EAP management console Runtime topology.](media/jboss-eap-azure-vm/jboss-eap-console-runtime-topology.png)](media/jboss-eap-azure-vm/jboss-eap-console-runtime-topology.png#lightbox)
7. Select the **Configuration** tab. In the navigation pane, select **Profiles** &gt; **ha** &gt; **Datasources & Drivers** &gt; **Datasources**. You should see that the datasource **dataSource-postgresql** is listed, as shown in the following screenshot:

    [![Screenshot of the JBoss EAP management console Configuration tab with Datasources selected.](media/jboss-eap-azure-vm/jboss-eap-console-configuration-datasources.png)](media/jboss-eap-azure-vm/jboss-eap-console-configuration-datasources.png#lightbox)

Leave the management console open. You use it to deploy a sample app to the JBoss EAP cluster in the next section.

## Deploy the app to the JBoss EAP cluster

Use the following steps to deploy the Java EE Cafe sample application to the Red Hat JBoss EAP cluster:

1. Use the following steps to build the Java EE Cafe sample. These steps assume that you have a local environment with Git and Maven installed:

    1. Use the following command to clone the source code from GitHub and check out the tag corresponding to this version of the article:

        ```bash
        git clone https://github.com/Azure/rhel-jboss-templates.git --branch 20240904 --single-branch
        ```

        If you see an error message with the text `You are in 'detached HEAD' state`, you can safely ignore it.
    2. Use the following command to build the source code:

        ```bash
        mvn clean install --file rhel-jboss-templates/eap-coffee-app/pom.xml
        ```

        This command creates the file *rhel-jboss-templates/eap-coffee-app/target/javaee-cafe.war*. You'll upload this file in the next step.
2. Use the following steps in the **Red Hat JBoss Enterprise Application Platform** management console to upload the *javaee-cafe.war* to the **Content Repository**.

    1. From the **Deployments** tab of the Red Hat JBoss EAP management console, select **Content Repository** in the navigation panel.
    2. Select **Add** and then select **Upload Content**.

        [![Screenshot of the JBoss EAP management console Deployments tab with Upload Content menu item highlighted.](media/jboss-eap-azure-vm/jboss-eap-console-upload-content.png)](media/jboss-eap-azure-vm/jboss-eap-console-upload-content.png#lightbox)
    3. Use the browser file chooser to select the *javaee-cafe.war* file.
    4. Select **Next**.
    5. Accept the defaults on the next screen and then select **Finish**.
    6. Select **View content**.
3. Use the following steps to deploy an application to the `main-server-group`:

    1. From **Content Repository**, select *javaee-cafe.war*.
    2. Open the drop-down menu and select **Deploy**.
    3. Select **main-server-group** as the server group for deploying *javaee-cafe.war*.
    4. Select **Deploy** to start the deployment. You should see a notice similar to the following screenshot:

        [![Screenshot of the notice of successful deployment.](media/jboss-eap-azure-vm/jboss-eap-console-app-successfully-deployed.png)](media/jboss-eap-azure-vm/jboss-eap-console-app-successfully-deployed.png#lightbox)

You're now finished deploying the Java EE application. Use the following steps to access the application and validate all the settings:

1. Use the following command to get the public IP address of the Azure Application Gateway. Replace the placeholder `<resource-group-name>` with the name of the resource group where the JBoss EAP cluster is deployed.

    ```azurecli
    az network public-ip show \
        --resource-group <resource-group-name> \
        --name gwip \
        --query '[ipAddress]' \
        --output tsv
    ```
2. Copy the output, which is the public IP address of the Azure Application Gateway deployed.
3. Open an internet-connected web browser.
4. Navigate to the application with the URL `http://<gateway-public-ip-address>/javaee-cafe`. Replace the placeholder `<gateway-public-ip-address>` with the public IP address of the Azure Application Gateway you copied previously.
5. Try to add and remove coffees.

## Clean up resources

To avoid Azure charges, you should clean up unnecessary resources. When you no longer need the JBoss EAP cluster deployed on Azure VMs, unregister the JBoss EAP servers and remove the Azure resources.

Run the following command to unregister the JBoss EAP servers and VMs from Red Hat subscription management. Replace the placeholder `<resource-group-name>` with the name of the resource group where the JBoss EAP cluster is deployed.

```azurecli
# Unregister domain controller
az vm run-command invoke \
    --resource-group <resource-group-name> \
    --name jbosseapVm-adminVM \
    --command-id RunShellScript \
    --scripts "sudo subscription-manager unregister"

# Unregister host controllers
az vm run-command invoke \
    --resource-group <resource-group-name> \
    --name jbosseapVm1 \
    --command-id RunShellScript \
    --scripts "sudo subscription-manager unregister"
az vm run-command invoke \
    --resource-group <resource-group-name> \
    --name jbosseapVm1 \
    --command-id RunShellScript \
    --scripts "sudo subscription-manager unregister"
```

Run the following commands to remove the two resource groups where the JBoss EAP cluster and the Azure Database for PostgreSQL flexible server are deployed. Replace the placeholder `<resource-group-name>` with the name of the resource group where the JBoss EAP cluster is deployed. Ensure the environment variable `$RG_NAME` is set with the name of the resource group where the PostgreSQL flexible server is deployed.

```azurecli
az group delete --name <resource-group-name> --yes --no-wait
az group delete --name $RG_NAME --yes --no-wait
```