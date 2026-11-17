---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set up Microsoft Copilot Managed Runtime for Lovable - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/configure-lovable?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Configure Microsoft Entra consent, app creation, external artifact deployment, environments, and network access so makers can publish Lovable apps to Microsoft Copilot Managed Runtime.
ms.topic: how-to
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ms.author: jordanchodak
manager: alaug
ms.reviewer: 
author: jordanchodakWork
ms.date: 2026-11-17T00:00:00.0000000Z
locale: en-us
document_id: 20872c21-5afa-a946-89c4-c6ae5cb6e3cc
document_version_independent_id: 20872c21-5afa-a946-89c4-c6ae5cb6e3cc
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/configure-lovable.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/configure-lovable
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/configure-lovable.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: e5f0ae53-e51c-e87d-f4a1-04e1d55a2670
---

# Set up Microsoft Copilot Managed Runtime for Lovable - Microsoft 365 admin | Microsoft Learn

Before makers can publish Lovable projects to Microsoft Copilot Managed Runtime, configure access to Lovable in Microsoft Entra. In each approved environment, you must allow app creation through the Copilot Managed Runtime command-line interface (CLI) setting and allow externally built artifacts. You should also decide where apps are created and validate network access.

This setup enables a third-party authoring and build service to deploy apps into your Microsoft tenant.

This article is for Microsoft tenant and Power Platform administrators. Makers should see [Publish a Lovable app to Microsoft Copilot Managed Runtime](../../../copilot-managed-runtime/publish-from-lovable).

Important

The Microsoft Copilot Managed Runtime integration is a third-party feature provided by Lovable. According to Lovable, the integration [requires a Lovable Business or Enterprise plan](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup) and is being released gradually. A Lovable workspace administrator must also [enable access to the connector](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup#set-up-your-lovable-workspace).

## How the integration works

The integration uses a Microsoft Entra enterprise application and delegated permissions to create and deploy apps on behalf of a signed-in maker. The integration doesn't grant Lovable an administrator role in your tenant. Actions are limited by the signed-in user's permissions and by the policies applied to the target environment.

Lovable builds the application artifact outside the Microsoft-managed build system. Copilot Managed Runtime then hosts the deployed app and applies Microsoft Entra authentication and your environment's governance policies.

The following content remains outside your Microsoft tenant:

- The Lovable project source
- Project chat history
- Lovable workspace and connection metadata

The published application, its Microsoft runtime identity, and its runtime connector activity are managed in your Microsoft tenant. Review [Lovable's tenant setup documentation](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup) for Lovable's current data handling and connection architecture.

## Prerequisites

To complete the Microsoft configuration, you need:

- A Microsoft Entra role that can grant tenant-wide admin consent for the permissions requested by the Lovable enterprise application. For role requirements, see [Grant tenant-wide admin consent to an application](/en-us/entra/identity/enterprise-apps/grant-admin-consent#prerequisites).
- A Manage role for Copilot Managed Runtime, to configure Copilot Managed Runtime and environment governance settings. For details, see [Roles and responsibilities](roles-responsibilities).
- Access to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
- A Lovable workspace administrator who can configure connector access in Lovable.

Before you grant consent, review the requested permissions, publisher information, terms of use, privacy statement, and your organization's third-party application requirements.

## 1. Add the Lovable enterprise application

Lovable documents its enterprise application with the display name **Lovable managed apps** and application (client) ID `2679639a-43b1-48b5-add7-85cedd49f1fc`.

Use Lovable's [tenant setup instructions](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup#step-1-add-the-lovable-application-and-grant-admin-consent) to initiate the consent request. On the Microsoft consent screen:

1. Confirm that the tenant is the tenant you intend to configure.
2. Confirm the application identity and publisher.
3. Review every requested permission.
4. Grant consent only if the permissions meet your organization's requirements.

After consent, verify the enterprise application:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Go to **Entra ID** &gt; **Enterprise apps** &gt; **All applications**.
3. Open **Lovable managed apps**.
4. Under **Security**, select **Permissions** and confirm the granted permissions.
5. Review sign-in logs and configure any assignment or Conditional Access requirements that your organization needs.

## 2. Allow app creation with the Copilot Managed Runtime CLI

To create Lovable apps, you need the **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** setting. Enable this setting for every environment or environment group where makers publish lovable apps.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. Go to **Copilot** &gt; **Settings** &gt; **Managed apps**.
3. Select **Allow app creation with the Copilot Managed Runtime command line interface (CLI)**.
4. Select **Environment groups** or **Environments**.
5. Select the group or environment where approved makers publish Lovable apps.
6. Enable the setting, and then save your changes.

For an environment group, you can instead go to **Manage** &gt; **Environment groups**, select the group, open **Rules**, and enable **Allow app creation with the Copilot Managed Runtime command line interface (CLI)**.

For more information, see [Control whether apps can be created using the CLI](governance#control-whether-apps-can-be-created-using-the-cli).

## 3. Allow external artifact deployment

External artifact deployment is disabled by default. Enable it only for environments where your organization allows artifacts built outside the Microsoft-managed build system.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. Go to **Copilot** &gt; **Settings** &gt; **Managed apps**.
3. Select **External artifacts in managed apps**.
4. Select **Environment groups** or **Environments**.
5. Select the group or environment where approved makers publish Lovable apps.
6. Enable the setting, and then save your changes.

For an environment group, you can instead go to **Manage** &gt; **Environment groups**, select the group, open **Rules**, and enable **External artifacts in managed apps**.

When you publish a rule at the environment-group level, it locks the corresponding setting for every environment in the group. Per-environment exceptions aren't supported. For more information, see [External artifact deployment](governance#external-artifact-deployment).

Important

Your organization is responsible for validating externally built artifacts, securing the build and authoring process, and confirming that artifacts meet your security, compliance, privacy, and software supply-chain requirements.

## 4. Choose the target environments

Decide whether makers can use automatically provisioned environments or must publish to environments that you designate.

### Use the default environment group

When a maker doesn't specify an environment ID, Lovable requests an environment under that maker's identity. Microsoft reuses that environment for the maker's later Lovable projects.

Automatically provisioned environments are placed in the [**Default environment group**](governance), where they inherit Microsoft-recommended governance settings that administrators can configure. To let makers create and publish Lovable-built apps in these environments, enable both **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** and **External artifacts in managed apps** for the **Default environment group**.

### Use designated environments

For more control over where apps are created, select approved environments and give each maker the applicable environment ID. The maker enters the ID when creating the Copilot Managed Runtime connection in Lovable.

Use separate environments or environment groups when teams, regions, or lifecycle stages require different policies. Confirm that each maker has permission to create and update apps in the assigned environment. For that environment or its environment group, enable both **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** and **External artifacts in managed apps**.

For environment-group design guidance, see [Environment groups](/en-us/power-platform/admin/environment-groups).

## 5. Configure network access

According to Lovable, builders and app users might need access to the following domains:

- `lovable.dev` and its subdomains
- `login.microsoftonline.com`
- `*.powerapps.com`
- `*.managedapps.cloud.microsoft`
- `*.lovable.app`
- `*.lovableproject.com`

Review the current [network requirements in Lovable's tenant setup documentation](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup#network-requirements) before you change a firewall, proxy, or browser policy.

The Lovable editor embeds the Copilot Managed Runtime preview. TLS inspection or policies that block embedded third-party content can prevent the preview from loading. Test with a pilot maker on your standard corporate network.

## 6. Configure the Lovable workspace

A Lovable workspace administrator controls who can create and use the Microsoft Copilot Managed Runtime connection. In Lovable, configure the connector for only the administrators and makers approved by your organization.

Lovable documents these workspace controls under [Set up your Lovable workspace](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup#set-up-your-lovable-workspace). Lovable controls and terminology can change independently of Microsoft, so use its documentation for the current procedure.

Connection sharing in Lovable controls who can use a connection in Lovable projects. It doesn't change the Microsoft identity that owns the connection or the permissions of that identity in your tenant.

## Revoke Lovable access

Revoking the Lovable integration prevents future access, but it doesn't automatically remove apps that were already deployed.

1. In the Microsoft Entra admin center, open **Entra ID** &gt; **Enterprise apps** &gt; **Lovable managed apps**.
2. Revoke consent or delete the enterprise application according to your incident-response and change-management process.
3. Have Lovable workspace administrators delete the corresponding Microsoft connections in Lovable.
4. In the Microsoft 365 admin center, go to **Apps** &gt; **All apps** and block or delete deployed apps as needed.
5. In the Power Platform admin center, review and remove environments or connections that are no longer required.
6. Disable CLI app creation and external artifact deployment if no approved workflow still requires them.

## Troubleshoot setup

| Issue | Resolution |
| --- | --- |
| Makers can't sign in from Lovable | Verify that the correct Lovable enterprise application exists in the tenant and has the required consent. Review the enterprise application's sign-in logs and Conditional Access results. |
| Makers can't find the connector | Ask the Lovable workspace administrator to verify plan availability and the workspace setting that controls who can create the connector. |
| App creation is rejected | Verify that **Allow app creation with the Copilot Managed Runtime command line interface (CLI)** is enabled for the target environment or its environment group. |
| Publishing is rejected | Verify that **External artifacts in managed apps** is enabled for the target environment or its environment group. |
| Runtime data requests fail | Review the app's connections, advanced connector policies, user permissions, and Conditional Access results. |
| The embedded preview is blank | Verify the required domains, proxy and TLS inspection behavior, and browser policies for embedded third-party content. |
| A revoked integration still has deployed apps | Revocation stops future Lovable access; block or delete existing apps separately from **Apps** &gt; **All apps** in the Microsoft 365 admin center. |

## Related information

- [Publish a Lovable app to Microsoft Copilot Managed Runtime](../../../copilot-managed-runtime/publish-from-lovable)
- [Lovable tenant setup for Microsoft Copilot Managed Runtime](https://docs.lovable.dev/integrations/microsoft-copilot-managed-runtime-tenant-setup)
- [Copilot Managed Runtime overview and key concepts for admins](./)
- [Copilot Managed Runtime default governance settings](governance)
- [Grant tenant-wide admin consent to an application](/en-us/entra/identity/enterprise-apps/grant-admin-consent)