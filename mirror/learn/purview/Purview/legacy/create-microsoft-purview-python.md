---
layout: Conceptual
title: 'Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using Python | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/create-microsoft-purview-python
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article will guide you through creating a Microsoft Purview (formerly Azure Purview) account using Python.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.devlang: python
ms.topic: quickstart
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: mode-api, devx-track-python, msecd-doc-authoring-1030
locale: en-us
document_id: ca1c5876-8ff1-548a-e61b-0cdf11ef05c9
document_version_independent_id: ca1c5876-8ff1-548a-e61b-0cdf11ef05c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/create-microsoft-purview-python.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/create-microsoft-purview-python
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/create-microsoft-purview-python.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 392ec56d-873d-2ca3-9439-7c3721cd4c21
---

# Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using Python | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](../classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

In this quickstart, you’ll create a Microsoft Purview (formerly Azure Purview) account programatically using Python. [The Python reference for Microsoft Purview](/en-us/python/api/azure-mgmt-purview/) is available, but this article will take you through all the steps needed to create an account with Python.

The Microsoft Purview governance portal surfaces tools like the Microsoft Purview Data Map and Microsoft Purview Data Catalog that help you manage and govern your data landscape. By connecting to data across your on-premises, multi-cloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your information. It identifies and classifies sensitive data, and provides end-to-end linage. Data consumers are able to discover data across your organization, and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the classic governance capabilities of Microsoft Purview, [see our governance solutions overview page](../governance-solutions-overview).

## Prerequisites

- If you don't have an Azure subscription, create a [free subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- A [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant) associated with your subscription.
- The user account that you use to sign in to Azure must be a member of the *contributor* or *owner* role, or an *administrator* of the Azure subscription. To view the permissions that you have in the subscription, follow these steps:

    1. Go to the [Azure portal](https://portal.azure.com)
    2. Select your username in the upper-right corner.
    3. Select the ellipsis button ("**...**") for more options.
    4. Then select **My permissions**.
    5. If you have access to multiple subscriptions, select the appropriate subscription.

## Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com) with your Azure account.

## Install the Python package

1. Open a terminal or command prompt with administrator privileges.
2. First, install the Python package for Azure management resources:

    ```python
    pip install azure-mgmt-resource
    ```
3. To install the Python package for Microsoft Purview, run the following command:

    ```python
    pip install azure-mgmt-purview
    ```

    The [Python SDK for Microsoft Purview](https://github.com/Azure/azure-sdk-for-python) supports Python 2.7, 3.3, 3.4, 3.5, 3.6 and 3.7.
4. To install the Python package for Azure Identity authentication, run the following command:

    ```python
    pip install azure-identity
    ```

    Note

    The "azure-identity" package might have conflicts with "azure-cli" on some common dependencies. If you meet any authentication issue, remove "azure-cli" and its dependencies, or use a clean machine without installing "azure-cli" package.

## Create a purview client

1. Create a file named **purview.py**. Add the following statements to add references to namespaces.

    ```python
    from azure.identity import ClientSecretCredential 
     from azure.mgmt.resource import ResourceManagementClient
     from azure.mgmt.purview import PurviewManagementClient
     from azure.mgmt.purview.models import *
     from datetime import datetime, timedelta
     import time
    ```
2. Add the following code to the **Main** method that creates an instance of PurviewManagementClient class. You'll use this object to create a purview account, delete purview accounts, check name availability, and other resource provider operations.

    ```python
    def main():
    
    # Azure subscription ID
    subscription_id = '<subscription ID>'
    
     # This program creates this resource group. If it's an existing resource group, comment out the code that creates the resource group
    rg_name = '<resource group>'
    
    # The purview name. It must be globally unique.
    purview_name = '<purview account name>'
    
    # Location name, where Microsoft Purview account must be created.
    location = '<location name>'    
    
    # Specify your Active Directory client ID, client secret, and tenant ID
    credentials = ClientSecretCredential(client_id='<service principal ID>', client_secret='<service principal key>', tenant_id='<tenant ID>') 
    # resource_client = ResourceManagementClient(credentials, subscription_id)
    purview_client = PurviewManagementClient(credentials, subscription_id)
    ```

## Create a purview account

1. Add the following code to the **Main** method that creates a **purview account**. If your resource group already exists, comment out the first `create_or_update` statement.

    ```python
     # create the resource group
     # comment out if the resource group already exits
     resource_client.resource_groups.create_or_update(rg_name, rg_params)
    
     #Create a purview
     identity = Identity(type= "SystemAssigned")
     sku = AccountSku(name= 'Standard', capacity= 4)
     purview_resource = Account(identity=identity,sku=sku,location =location )
    
     try:
         pa = (purview_client.accounts.begin_create_or_update(rg_name, purview_name, purview_resource)).result()
         print("location:", pa.location, " Microsoft Purview Account Name: ", pa.name, " Id: " , pa.id ," tags: " , pa.tags)  
     except:
         print("Error")
         print_item(pa)
    
     while (getattr(pa,'provisioning_state')) != "Succeeded" :
         pa = (purview_client.accounts.get(rg_name, purview_name))  
         print(getattr(pa,'provisioning_state'))
         if getattr(pa,'provisioning_state') == "Failed" :
             print("Error in creating Microsoft Purview account")
             break
         time.sleep(30)      
    ```
2. Now, add the following statement to invoke the **main** method when the program is run:

    ```python
    # Start the main method
    main()
    ```

## Full script

Here’s the full Python code:

```python
	
from azure.identity import ClientSecretCredential 
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.purview import PurviewManagementClient
from azure.mgmt.purview.models import *
from datetime import datetime, timedelta
import time

def main():

    # Azure subscription ID
    subscription_id = '<subscription ID>'
    # This program creates this resource group. If it's an existing resource group, comment out the code that creates the resource group
    rg_name = '<resource group>'

    # The purview name. It must be globally unique.
    purview_name = '<purview account name>'

    # Location for your resource group and your Microsoft Purview account.
    location ="<location>" 

    # Specify your Active Directory client ID, client secret, and tenant ID
    credentials = ClientSecretCredential(client_id='<service principal ID>', client_secret='<service principal key>', tenant_id='<tenant ID>') 
    resource_client = ResourceManagementClient(credentials, subscription_id)
    purview_client = PurviewManagementClient(credentials, subscription_id)
    # create the resource group
    # comment out if the resource group already exits
    resource_client.resource_groups.create_or_update(rg_name, {"location": location})

    #Create a purview
    identity = Identity(type= "SystemAssigned")
    sku = AccountSku(name= 'Standard', capacity= 4)
    purview_resource = Account(identity=identity,sku=sku,location =location)
       
    try:
        pa = (purview_client.accounts.begin_create_or_update(rg_name, purview_name, purview_resource)).result()
        print("location:", pa.location, " Microsoft Purview Account Name: ", purview_name, " Id: " , pa.id ," tags: " , pa.tags) 
    except:
        print("Error in submitting job to create account")
        print_item(pa)
 
    while (getattr(pa,'provisioning_state')) != "Succeeded" :
        pa = (purview_client.accounts.get(rg_name, purview_name))  
        print(getattr(pa,'provisioning_state'))
        if getattr(pa,'provisioning_state') == "Failed" :
            print("Error in creating Microsoft Purview account")
            break
        time.sleep(30)    

# Start the main method
main()
```

## Run the code

Build and start the application. The console prints the progress of Microsoft Purview account creation. Wait until it’s completed. Here’s the sample output:

```console
location: southcentralus  Microsoft Purview Account Name:  purviewpython7  Id:  /subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/Demo_Catalog/providers/Microsoft.Purview/accounts/purviewpython7  tags:  None
Creating
Creating
Succeeded
```

## Verify the output

Go to the **Microsoft Purview accounts** page in the Azure portal and verify the account created using the above code.

## Delete Microsoft Purview account

To delete purview account, add the following code to the program, then run:

```python
pa = purview_client.accounts.begin_delete(rg_name, purview_name).result()
```