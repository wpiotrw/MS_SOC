---
layout: Conceptual
title: Set up Double Key Encryption (DKE) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/double-key-encryption-setup
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Complete these tasks to deploy Microsoft Purview Double Key Encryption to secure your most sensitive data.
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-07-23T00:00:00.0000000Z
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-encryption
audience: Admin
ms.reviewer: esaggese
ms.collection:
- purview-compliance
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-ropc-nochange
locale: en-us
document_id: 116dec79-2492-65cf-8e5b-9918bb2a1efe
document_version_independent_id: 116dec79-2492-65cf-8e5b-9918bb2a1efe
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/double-key-encryption-setup.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: double-key-encryption-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/double-key-encryption-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/911a44a7-2f6c-477c-810f-dc8b7d425cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/9bdc1705-9b40-49d6-8377-caa0b71fda66
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/14f2b9d5-6f06-45a8-ac5f-313eaa351153
- https://authoring-docs-microsoft.poolparty.biz/devrel/686ed158-d915-41e9-9760-efa46ba88f6d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 6d099ff6-fd9f-f005-cf2d-675f368d111f
---

# Set up Double Key Encryption (DKE) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

> 
> *Service description for: [Microsoft Purview](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)*

Follow these general steps to set up DKE. Once you complete these steps, your end users can protect your highly sensitive data with Double Key Encryption.

1. Deploy the DKE service as described in this article. Ensure your environment meets the minimum system and licensing requirements. For more information, see [System and licensing requirements for DKE](double-key-encryption#system-and-licensing-requirements-for-dke).
2. Create a label with Double Key Encryption. In the Microsoft Purview portal, navigate to **Information protection** and create a new label with Double Key Encryption. See [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels).
3. Configure the registry on client devices so you can use Double Key Encryption labels. Next, protect your data by selecting the Double Key Encrypted label from the Sensitivity ribbon in Microsoft Office.

There are several ways you can complete some of the steps to deploy Double Key Encryption. This article provides detailed instructions so that less experienced admins successfully deploy the service. If you're comfortable doing so, you can choose to use your own methods.

## Deploy DKE

This article and the deployment video use Azure as the deployment destination for the DKE service. If you're deploying to another location, you need to provide your own values.

Follow these general steps to set up Double Key Encryption for your organization.

1. Install software prerequisites for the DKE service
2. Clone the Double Key Encryption GitHub repository
3. Modify application settings
4. Generate test keys
5. Build the project
6. Deploy the DKE service and publish the key store
7. Validate your deployment
8. Register your key store
9. Create sensitivity labels using DKE
10. Migrate protected files from HYOK labels to DKE labels

When you're done, you can encrypt documents and files using DKE. For information, see [Apply sensitivity labels to your files and email in Office](https://support.microsoft.com/office/2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9).

### Install software prerequisites for the DKE service

Install these prerequisites on the computer where you want to install the DKE service.

**.NET 8.0 SDK**. Download and install the SDK from [Download .NET 8.0](https://dotnet.microsoft.com/download/dotnet/8.0).

**Visual Studio Code**. Download Visual Studio Code from [https://code.visualstudio.com/](https://code.visualstudio.com). Once installed, run Visual Studio Code and select **View** &gt; **Extensions**. Install these extensions.

- C# for Visual Studio Code
- NuGet Package Manager

**Git resources**. Download and install one of the following.

- [Git](https://git-scm.com/downloads)
- [GitHub Desktop](https://desktop.github.com/)
- [GitHub Enterprise](https://github.com/enterprise)

**OpenSSL**. You must have [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) installed to generate test keys after you deploy DKE. Make sure you're invoking it correctly from your environment variables path. For example, see "Add the installation directory to PATH" at https://www.osradar.com/install-openssl-windows/ for details.

### Clone the DKE GitHub repository

Microsoft supplies the DKE source files in a GitHub repository. You clone the repository to build the project locally for your organization's use. The DKE GitHub repository is located at https://github.com/Azure-Samples/DoubleKeyEncryptionService.

The following instructions are intended for inexperienced git or Visual Studio Code users:

1. In your browser, go to: https://github.com/Azure-Samples/DoubleKeyEncryptionService.
2. Towards the right side of the screen, select **Code**. Your version of the UI might show a **Clone or download** button. Then, in the dropdown that appears, select the copy icon to copy the URL to your clipboard.

    For example:

    ![Clone the Double Key Encryption service repository from GitHub.](media/dke-clone.png)
3. In Visual Studio Code, select **View** &gt; **Command Palette** and select **Git: Clone**. To jump to the option in the list, start typing `git: clone` to filter the entries, and then select it from the drop-down. For example:

    ![Visual Studio Code GIT:Clone option.](media/dke-vscode-clone.png)
4. In the text box, paste the URL that you copied from Git and select **Clone from GitHub**.
5. In the **Select Folder** dialog that appears, browse to and select a location to store the repository. Select **Open**.

    The repository opens in Visual Studio Code, and displays the current Git branch at the bottom left. The branch should be **main**. For example:

    ![Screenshot of the DKE repository in Visual Studio Code displaying the main branch.](media/dke-vscode-main-branch.jpg)
6. If you're not on the main branch, select it. In Visual Studio Code, select the branch and choose **main** from the list of branches that displays.

    Important

    Selecting the main branch ensures that you have the correct files to build the project. If you don't choose the correct branch your deployment will fail.

You now have your DKE source repository set up locally. Next, modify application settings for your organization.

### Modify application settings

To deploy the DKE service, you must modify the following types of application settings:

- Key access settings
- Tenant and key settings

You modify application settings in the appsettings.json file. This file is located in the DoubleKeyEncryptionService repo you cloned locally under DoubleKeyEncryptionService\src\customer-key-store. For example, in Visual Studio Code, you can browse to the file as shown in the following picture.

![Locating the appsettings.json file for DKE.](media/dke-appsettingsjson.png)

#### Key access settings

Choose whether to use email or role authorization. DKE supports only one of these authentication methods at a time.

- **Email authorization**. Allows your organization to authorize access to keys based on email addresses only.
- **Role authorization**. Allows your organization to authorize access to keys based on Active Directory groups, and requires that the web service can query LDAP.

##### To set key access settings for DKE using email authorization

1. Open the **appsettings.json** file and locate the `AuthorizedEmailAddress` setting.
2. Add the email address or addresses that you want to authorize. Separate multiple email addresses with double quotes and commas. For example:

    ```json
    "AuthorizedEmailAddress": ["email1@company.com", "email2@company.com ", "email3@company.com"]
    ```
3. Locate the `LDAPPath` setting and remove the text `If you use role authorization (AuthorizedRoles) then this is the LDAP path.` between the double quotes. Leave the double quotes in place. When you're finished, the setting should look like this.

    ```json
    "LDAPPath": ""
    ```
4. Locate the `AuthorizedRoles` setting and delete the entire line.

This image shows the **appsettings.json** file correctly formatted for email authorization.

![The appsettings.json file showing email authorization method.](media/dke-email-accesssetting.png)

##### To set key access settings for DKE using role authorization

1. Open the **appsettings.json** file and locate the `AuthorizedRoles` setting.
2. Add the Active Directory group names you want to authorize. Separate multiple group names with double quotes and commas. For example:

    ```json
    "AuthorizedRoles": ["group1", "group2", "group3"]
    ```
3. Locate the `LDAPPath` setting and add the Active Directory domain. For example:

    ```json
    "LDAPPath": "contoso.com"
    ```
4. Locate the `AuthorizedEmailAddress` setting and delete the entire line.

This image shows the **appsettings.json** file correctly formatted for role authorization.

![appsettings.json file showing role authorization method.](media/dke-role-accesssetting.png)

#### Tenant and key settings

DKE tenant and key settings are located in the **appsettings.json** file.

##### To configure tenant and key settings for DKE

1. Open the **appsettings.json** file.
2. Locate the `ValidIssuers` setting and replace `<tenantid>` with your tenant ID, making sure you keep the slash at the end of the tenant ID. You can locate your tenant ID by going to the Azure portal and viewing the [tenant properties](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Properties). For example:

    ```json
    "ValidIssuers": [
    "https://sts.windows.net/9c99431e-b513-44be-a7d9-e7b500002d4b/"
    ]
    
    ```

Note

If you want to enable external B2B access to your key store, you will also need to include these external tenants as part of the valid issuers' list.

Locate the `JwtAudience`. Replace the placeholder value, `"https://dkeservice.contoso.com"` in the json with the hostname of the machine where you want to run the DKE service.

Important

The value for `JwtAudience` must match the name of your host *exactly*.

- `TestKeys:Name`. Enter a name for your key. For example: `TestKey1`
- `TestKeys:Id`. Create a GUID and enter it as the `TestKeys:ID` value. For example, `DCE1CC21-FF9B-4424-8FF4-9914BD19A1BE`. You can use a site like [Online GUID Generator](https://guidgenerator.com/) to randomly generate a GUID.
- `JwtAuthorization`. Replace `{tenant-id}` with your tenant id.

The following json shows the correct format for tenant and keys settings in **appsettings.json**. `LDAPPath` is configured for role authorization.

```json
{
  "TokenValidationParameters": {
    "ValidIssuers": [
      "https://sts.windows.net/9c99431e-b513-44be-a7d9-e7b50002d4b/"
    ]
  },
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  },
  "AllowedHosts": "*",
  "JwtAudience": "https://dkeservice.contoso.com/",
  "JwtAuthorization": "https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize",
  "RoleAuthorizer": {
    "LDAPPath": ""
  },
  "TestKeys": [
    {
      "Name": "TestKey1",
      "Id": "DCE1CC21-FF98-4424-8FF4-9914BD19A1BE"
    }
  ]
}
```

### Generate test keys

Once you have your application settings defined, you're ready to generate public and private test keys.

To generate keys:

1. From the Windows Start menu, run the OpenSSL Command Prompt.
2. Change to the folder where you want to save the test keys. The files you create by completing the steps in this task are stored in the same folder.
3. Generate the new test key.

    ```console
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
    ```
4. Generate the private key.

    If you installed OpenSSL version 3 or later, run the following command:

    ```console
    openssl rsa -in key.pem -out privkeynopass.pem -outform PEM -traditional
    ```

    Otherwise, run the following command:

    ```console
    openssl rsa -in key.pem -out privkeynopass.pem -outform PEM
    ```
5. Generate the public key.

    ```console
    openssl rsa -in key.pem -pubout > pubkeyonly.pem
    ```
6. In a text editor, open **pubkeyonly.pem**. Copy all of the content in the **pubkeyonly.pem** file, except the first and last lines, into the `PublicPem` section of the **appsettings.json** file.
7. In a text editor, open **privkeynopass.pem**. Copy all of the content in the **privkeynopass.pem** file, except the first and last lines, into the `PrivatePem` section of the **appsettings.json** file.
8. Remove all blank spaces and newlines in both the `PublicPem` and `PrivatePem` sections.

    Important

    When you copy this content, do not delete any of the PEM data.
9. In Visual Studio Code, browse to the **Startup.cs** file. This file is located in the DoubleKeyEncryptionService repo you cloned locally under DoubleKeyEncryptionService\src\customer-key-store.
10. Locate the following lines:

    ```csharp
    #if USE_TEST_KEYS
    #error !!!!!!!!!!!!!!!!!!!!!! Use of test keys is only supported for testing,
    DO NOT USE FOR PRODUCTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    services.AddSingleton<ippw.IKeyStore, ippw.TestKeyStore>();
    #endif
    ```
11. Replace these lines with the following text:

    ```csharp
    services.AddSingleton<ippw.IKeyStore, ippw.TestKeyStore>();
    ```

    The end results should look similar to the following.

    ![startup.cs file for public preview.](media/dke-startupcs-usetestkeys.png)

Now you're ready to build your DKE project.

### Build the project

Use the following instructions to build the DKE project locally:

1. In Visual Studio Code, in the DKE service repository, select **View** &gt; **Command Palette** and then type **build** at the prompt.
2. From the list, choose **Tasks: Run build task**.

    If there are no build tasks found, select **Configure Build Task** and create one for .NET core as follows.

    ![Configure missing build task for .NET.](media/dke-configurebuildtask.png)

    1. Choose **Create tasks.json from template**.

        ![Create tasks.json file from template for DKE.](media/dke-createtasksjsonfromtemplate.png)
    2. From the list of template types, select **.NET Core**.

        ![Select the correct template for DKE.](media/dke-tasksjsontemplate.png)
    3. In the build section, locate the path to the **customerkeystore.csproj** file. If it's not there, add the following line:

        ```json
        "${workspaceFolder}/src/customer-key-store/customerkeystore.csproj",
        ```
    4. Run the build again.
3. Verify that there are no red errors in the output window.

    If there are red errors, check the console output. Ensure that you completed all the previous steps correctly and the correct build versions are present.

Your setup is now complete. Before you publish the keystore, in appsettings.json, for the JwtAudience setting, ensure the value for hostname exactly matches your App Service host name.

### Deploy the DKE service and publish the key store

For production deployments, deploy the service either in a third-party cloud or [publish to an on-premises system](/en-us/aspnet/core/tutorials/publish-to-iis?preserve-view=true&amp;tabs=netcore-cli&amp;view=aspnetcore-3.1).

You may prefer other methods to deploy your keys. Select the method that works best for your organization.

For pilot deployments, you can deploy in Azure and get started right away.

#### To create an Azure Web App instance to host your DKE deployment

To publish the key store, create an Azure App Service instance to host your DKE deployment. Next, publish your generated keys to Azure.

1. In your browser, sign in to the [Microsoft Azure portal](https://ms.portal.azure.com), and go to **App Services** **&gt; Create &gt; Web App**.
2. Create a new or select an existing resource group.
3. Provide a name for the instance, e.g. contosodke1. This name does not match the name in the config file. The value you provide for the name is also the WebAppInstanceName.
4. In pricing plan, select a size that allows custom domains, e.g. Basic B1.
5. For **Publish**, select **code**, and for **Runtime stack**, select **.NET 8 (LTS)**.
6. Select **Review + create**

For example:

![Create Web App](media/double-key-encryption-setup/create-web-app.jpg)

1. In the newly created web app, go to “Settings”, “Custom domains”, select **Add custom domain**
2. In **Domain provider,** select **All other domain services**
3. In **Domain**, enter the hostname of the computer where you want to install the DKE service.

Important

Make sure the hostname is the same name as the one defined for the JwtAudience setting in the appsettings.json file.

1. In the public DNS, perform the suggested changes as indicated in the Domain validation section and select **Validate**.

For example:

![Add custom domain.](media/double-key-encryption-setup/customdomain.jpg)

1. Do the following to publish your generated keys:

    - Publish via ZipDeployUI
    - You can use other methods to upload your binaries to that app, such as FTP.

for example, ftp

#### Publish via ZipDeployUI

1. Go to `https://<WebAppInstanceName>.scm.<location>.azurewebsites.net/ZipDeployUI`.

    For example: `https://dkeservice-ctaugtfwh7d3c3c.scm.westcentralus-01.azurewebsites.net/ZipDeployUI`
2. Launch a PowerShell prompt.
3. In the codebase for the key store, go to the **customer-key-store\src\customer-key-store** folder, and verify that this folder contains the **customerkeystore.csproj** file.
4. Run: **dotnet publish**

    The output window displays the directory where the publish was deployed.

    For example: `customer-key-store\src\customer-key-store\bin\Debug\net8.0\publish\`
5. Send all files in the publish directory to a .zip file. When creating the .zip file, make sure that all files in the directory are at the root level of the .zip file.
6. Drag and drop the .zip file you created to the ZipDeployUI site you opened before.

DKE is deployed and you can browse to the test keys you created. Continue to Validate your deployment in this article.

### Validate your deployment

After deploying DKE using one of the methods described in this article, validate the deployment and the key store settings.

Run:

```powershell
src\customer-key-store\scripts\key_store_tester.ps1 dkeserviceurl/mykey
```

For example:

```powershell
key_store_tester.ps1 https://dkeservice.contoso.com/TestKey1
```

Ensure that no errors appear in the output. When you're ready, register your key store.

The key name is case-sensitive. Enter the key name as it appears in the appsettings.json file.

## Register your key store

The following steps enable you to register your DKE service. Registering your DKE service is the last step in deploying DKE before you can start creating labels.

To register the DKE service:

1. In your browser, open the [Microsoft Azure portal](https://ms.portal.azure.com/), and go to **All Services** &gt; **Identity** &gt; **App Registrations**.
2. Select **New registration**, and enter a meaningful name.
3. Select an account type from the options displayed.

    For example:

    ![New App Registration.](media/dke-app-registration.png)
4. At the bottom of the page, select **Register** to create the new App Registration.
5. In your new App Registration, in the left pane, under **Manage**, select **Authentication**.
6. Select **Add a platform**.
7. On the **Configure platforms** popup, select **Web**.
8. Under **Redirect URIs**, enter the URI of your double key encryption service. Enter the App Service URL, including both the hostname and domain.

    For example: `https://mydkeservicetest.com`

    - The URL you enter must match the hostname where your DKE service is deployed.
    - The domain must be a [verified domain](/en-us/azure/active-directory/develop/reference-breaking-changes#appid-uri-in-single-tenant-applications-will-require-use-of-default-scheme-or-verified-domains).
    - In all cases, the scheme must be **https**.

    Ensure the hostname exactly matches your App Service hostname.
9. Under **Implicit grant**, select the **ID tokens** checkbox.
10. Select **Save** to save your changes.
11. On the left pane, select **Expose an API**, next to Application ID URI, enter your App Service URL, including both hostname and domain, and then select **Set**.
12. Still on the **Expose an API** page, in the **Scopes defined by this API** area, select **Add a scope**. In the new scope:

    1. Define the scope name as **user\_impersonation**.
    2. Select the administrators and users who can consent.
    3. Define any remaining values required.
    4. Select **Add scope**.
    5. Select **Save** at the top to save your changes.
13. Still on the **Expose an API** page, in the **Authorized client applications** area, select **Add a client application**.

    In the new client application:

    1. Define the Client ID as `d3590ed6-52b3-4102-aeff-aad2292ab01c`. This value is the Microsoft Office client ID, and enables Office to obtain an access token for your key store.
    2. Under **Authorized scopes**, select the **user\_impersonation** scope.
    3. Select **Add application**.
    4. Select **Save** at the top to save your changes.
    5. Repeat these steps, but this time, define the client ID as `c00e9d32-3c8d-4a7d-832b-029040e7db99`. This value is the Purview Information Protection client ID.

Your DKE service is now registered. Continue by creating labels using DKE.

## Create sensitivity labels using DKE

In the Microsoft Purview portal, create a new sensitivity label and apply encryption as you would otherwise. Select **Use Double Key Encryption** and enter the endpoint URL for your key. You need to include the key name you provided in the "TestKeys" section of the appsettings.json file in the URL.

For example: `https://testingdke1.azurewebsites.net/KEYNAME`

![Select Use Double Key Encryption in the Microsoft Purview portal.](media/dke-use-dke.png)

Any DKE labels you add appear for users in the latest versions of Microsoft 365 Apps for enterprise.

Note

It may take up to 24 hours for the clients to refresh with the new labels.

## Migrate protected files from HYOK labels to DKE labels

If you want, once you finish setting up DKE, you can migrate content that you protected using HYOK labels to DKE labels. To migrate, use the Microsoft Purview Information Protection scanner. To get started using the scanner, see [Understand the information protection scanner](deploy-scanner).

If you don't migrate content, your HYOK protected content remains unaffected.

## Other deployment options

We realize that for some customers in highly regulated industries, this standard reference implementation using software-based keys might not be sufficient to meet their enhanced compliance obligations and needs. We partner with third-party hardware security module (HSM) vendors to support enhanced key management options in the DKE service, including:

- [Entrust](https://www.entrust.com/digital-security/hsm/services/packaged-services/double-key-encryption-integration#:%7E:text=Entrust%20Double%20Key%20Encryption%20for%20Microsoft%20AIP%2C%20offered,trust%20for%20the%20protection%20of%20sensitive%20cryptographic%20keys.)
- [Thales](https://cpl.thalesgroup.com/cloud-security/encryption/double-key-encryption)
- [Utimaco](https://utimaco.com/solutions/applications/double-key-encryption)

Reach out directly to these vendors for more information and guidance on their in-market DKE HSM solutions.

## Set up clients to apply DKE sensitivity labels

On each client device, complete this task.

1. Ensure the following registry values are defined on each client. Create registry keys that aren't already there:

    ```console
    [HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIPC\flighting]
    "DoubleKeyProtection"=dword:00000001
    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSIPC\flighting]
    "DoubleKeyProtection"=dword:00000001
    ```