---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure authentication for Microsoft 365 support integration with ServiceNow - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-authentication?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: integration
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
ROBOTS: NOINDEX, NOFOLLOW
search.appverid:
- MET150
description: Scoped Certified application installation and configuration guide for ServiceNow.
locale: en-us
document_id: 0f2fdff5-c796-998b-9e60-41509c44336e
document_version_independent_id: 0f2fdff5-c796-998b-9e60-41509c44336e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/servicenow-authentication.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/servicenow-authentication
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/servicenow-authentication.md
platformId: e5263f74-59f8-6a97-5dc8-036097f4eb68
---

# Configure authentication for Microsoft 365 support integration with ServiceNow - Microsoft 365 admin | Microsoft Learn

Important

Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

## Prerequisites

These prerequisite steps are required to set up Microsoft 365 support integration.

### Microsoft Entra administrator

1. [Microsoft Entra Admin] Create Microsoft Entra Application for Outbound under your Microsoft 365 tenant.

    1. Log on to the Azure Portal with your Microsoft 365 tenant credentials and go to the [App registrations page](https://portal.azure.com/?Microsoft_AAD_RegisteredApps=true#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) to create a new application.
    2. Select **Accounts in this organizational directory only ({Microsoft-365-tenant-name} only - Single tenant)** and select **Register**.

        [![Select Register.](../../media/servicenow-guide/servicenow-guide-image3.png)](../../media/servicenow-guide/servicenow-guide-image3.png#lightbox)
2. Go to **Authentication** and select **Add a platform**. Select the **Web** option and enter the redirect URL: `https://{your-servicenow-instance``}.service-now.com/oauth_redirect.do`

    [![Select Add a platform and the redirect URL.](../../media/servicenow-guide/servicenow-guide-image4.png)](../../media/servicenow-guide/servicenow-guide-image4.png#lightbox)
3. Get the **Application Client ID** and create a Client secret and get that value.
4. [ServiceNow Admin] Set up the Outbound OAuth Provider in ServiceNow.

    If the scope is not set to **Global**, go to **Settings** &gt; **Developer** &gt; **Applications** and switch to **Global**.

    [![Switch to Global.](../../media/servicenow-guide/servicenow-guide-image5.png)](../../media/servicenow-guide/servicenow-guide-image5.png#lightbox)
5. Go to **System OAuth** &gt; **Application Registry**.
6. Create a new application by using the **Connect to a third party OAuth Provider** option and entering these values:

    - Client ID: This is the Client ID of the application created in step #1.
    - Client Secret: This is the Client Secret value of the application created in step #3.
    - Default Grant type: Client Credentials
    - Token URL: `https://login.microsoftonline.com/{microsoft-365-tenant-name}/oauth2/token`
    - Redirect URL: `https://{service-now-instance-name``}.service-now.com/auth_redirect.do`

### [OPTIONAL] Allow the service's IP addresses to Microsoft 365 support integration

If your company is limiting internet access with your own policies, enable network access for the service of Microsoft 365 support integration by allowing the IP addresses below for both inbound and outbound API access:

- 52.149.152.32
- 40.83.232.243
- 40.83.114.39
- 13.76.138.31
- 13.79.229.170
- 20.105.151.142

Note

This terminal command lists all active IPs of the service for Microsoft 365 support integration: `nslookup`` connector.rave.microsoft.com`

## Configure the Microsoft 365 support integration application

These steps are required to set up the integration between your ServiceNow instance and Microsoft 365 support.

To open the Microsoft 365 support integration setup wizard, type **Microsoft 365** in the ServiceNow navigator and select **Setup**.

### Steps performed by a ServiceNow administrator

1. Switch the scope to Microsoft 365 support integration.

    [![Switch the Application to Microsoft 365 support integration.](../../media/servicenow-guide/servicenow-guide-image9.png)](../../media/servicenow-guide/servicenow-guide-image9.png#lightbox)
2. Go to Microsoft 365 Support &gt; **Setup** to open the integration workflow.

    Note

    If you see the error "Read operation against 'oauth\_entity' from scope 'x\_mioms\_m365\_assis' has been refused due to the table's cross-scope access policy," it was caused by your table access policy. You must make sure **All application scopes &gt; Can read** is checked for the table oauth\_entity.

    [![Make sure All application scopes is selected.](../../media/servicenow-guide/servicenow-guide-image10.png)](../../media/servicenow-guide/servicenow-guide-image10.png#lightbox)
3. Select **Agree** to continue.

    [![Select Agree.](../../media/servicenow-guide/servicenow-updates-agree.png)](../../media/servicenow-guide/servicenow-updates-agree.png#lightbox)
4. Configure the environment and start the setup.

    If this installation is on a test environment, select the option **This is a test environment**. You can disable this option after the setup and your tests are completed later.

    [![Start setup.](../../media/servicenow-guide/servicenow-wizard-start-setup.png)](../../media/servicenow-guide/servicenow-wizard-start-setup.png#lightbox)
5. Enter your Microsoft 365 tenant domain.

    [![Enter tenant domain.](../../media/servicenow-guide/servicenow-updates-enterdomain.png)](../../media/servicenow-guide/servicenow-updates-enterdomain.png#lightbox)
6. Configure authentication settings.

    1. Register the Microsoft Entra app.
    2. After completing the instructions in the prerequisites section, select **Done**. Otherwise, follow the instructions in the wizard to create the necessary application registration in Microsoft Entra ID.

        [![Register the Microsoft Entra app.](../../media/servicenow-guide/servicenow-updates-configureauthsettings.png)](../../media/servicenow-guide/servicenow-updates-configureauthsettings.png#lightbox)
    3. Register the ServiceNow OAuth app.
    4. After completing the instructions in the prerequisites section, select the newly created OAuth application registration and select **Next**. Otherwise, follow the instructions to create the entity in ServiceNow, and then select the new application registration.

        [![Register the ServiceNow OAuth app.](../../media/servicenow-guide/servicenow-updates-authsettingsnext.png)](../../media/servicenow-guide/servicenow-updates-authsettingsnext.png#lightbox)

### Steps performed by a Microsoft 365 administrator in the Microsoft 365 admin portal

Note

Do not select **Test setup** before the Microsoft 365 administrator finishes performing the next steps.

Verify that the following information is correct.

[![Verify that the information in this screenshot is correct.](../../media/servicenow-guide/servicenow-updates-verifyinfo.png)](../../media/servicenow-guide/servicenow-updates-verifyinfo.png#lightbox)

Note

The following steps configure the Microsoft 365 support integration for ServiceNow application version 2.0.0 and later. If you've installed version 1.0.11 or earlier, you can't configure a new installation of the application.

1. Configure the support integration settings:

    Select the **Basic information** tab &gt; **Internal support tool** &gt; **ServiceNow**, and enter the **Outbound App ID** value in the **Application ID to issue Auth Token** field. This **Outbound App ID** is on Step 6 - Complete the Integration, which was created in Prerequisite step #1.

    [![Configure support integration settings.](../../media/servicenow-guide/servicenow-guide-image18.png)](../../media/servicenow-guide/servicenow-guide-image18.png#lightbox)

    - On the **Repositories** tab, select **New repository** and update it with the following settings:

        If you have version 1.0.11 or earlier installed, you must upgrade the application to version 2.0.0 or later.

        [![Update the new repository.](../../media/servicenow-guide/servicenow-updates-editrepository.png)](../../media/servicenow-guide/servicenow-updates-editrepository.png#lightbox)
    - Repository: The **Repository ID** value from Step 6 - Complete the Integration, which was created in Prerequisite step #1. Endpoint: The **Endpoint** value from Step 6 - Complete the Integration, which was created in Prerequisite step #1.

        [![Complete the integration by setting Repository and Endpoint.](../../media/servicenow-guide/servicenow-updates-addlsettings.png)](../../media/servicenow-guide/servicenow-updates-addlsettings.png#lightbox)
2. Select **Save**.

### Steps performed in ServiceNow by a ServiceNow administrator.

A ServiceNow administrator tests the connection and completes the setup.

- To complete the setup, go back to your ServiceNow instance and select **Test setup**.

## Test setup

The Microsoft 365 support integration app executes tests to make sure the integration is working. If there's a problem with the configuration, an error message explains what needs to be fixed. Otherwise, the application is ready.

[![Setup validation successful.](../../media/servicenow-guide/servicenow-updates-ready.png)](../../media/servicenow-guide/servicenow-updates-ready.png#lightbox)

## Enable Microsoft support integration for an existing user

Microsoft 365 support integration is enabled for the user with one of these roles:

- **x\_mioms\_m365\_assis.insights\_user**-This role is required to view the **Recommended Solutions & Articles** and **Microsoft Service Health** features in the ServiceNow incident view.
- **x\_mioms\_m365\_assis.administrator**-This role is required to escalate ServiceNow incidents to Microsoft support using a linked Microsoft 365 admin account. Follow the next section to link your admin account in the app's settings and finalize the steps to create Microsoft support cases.

In order for every member of your organization to be able to escalate ServiceNow incidents as support cases to Microsoft, each member must have the x\_mioms\_m365\_assis.administrator role applied. The x\_mioms\_m365\_assis.insights\_user role is required to gain access to the Recommended Solutions & Articles and Microsoft Service Health information in the ServiceNow incident view; it is not required to create Microsoft support cases.

### Link Microsoft 365 Admin account

Continue with these instructions if you are looking to escalate your ServiceNow incidents to Microsoft support from your ServiceNow instance via the app.

If any users are provisioned with the role **x\_mioms\_m365\_assis.administrator** and are using different Microsoft 365 accounts to manage a Microsoft 365 support case, they must set up their Microsoft 365 admin email account by navigating to **Microsoft 365 support** &gt; **Link Account**. Each member is not required to link their Microsoft 365 tenant email account. You are only required to enter a single valid Microsoft 365 admin email account that has ticket creation permissions. The app will only maintain a single admin account for this purpose.

[![Graphical user interface, text, application, chat or text message Description automatically generated.](../../media/servicenow-guide/servicenow-guide-image21.png)](../../media/servicenow-guide/servicenow-guide-image21.png#lightbox)