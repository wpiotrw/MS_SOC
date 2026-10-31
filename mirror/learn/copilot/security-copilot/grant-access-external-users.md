---
layout: Conceptual
title: Grant MSSPs access to Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/grant-access-external-users
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about Managed Security Solution Provider access to Microsoft Security Copilot using Azure Lighthouse, GDAP, or B2B collaboration and understand which tenant's capacity is used for each option.
ms.date: 2026-05-22T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-manage
ms.custom: 
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 41f7eebb-7792-e6ed-01f8-fe14bf3560c5
document_version_independent_id: 41f7eebb-7792-e6ed-01f8-fe14bf3560c5
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/grant-access-external-users.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: grant-access-external-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/grant-access-external-users.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/d0989e16-62ed-4db0-8dd8-b1c704683638
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/677796fe-69f7-4468-8f9b-540e903c4f4e
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
platformId: 5e495a9c-b8b1-d2c8-e568-dad9d8b087b3
---

# Grant MSSPs access to Microsoft Security Copilot | Microsoft Learn

If you're working with a Microsoft Managed Security Solution Provider (MSSP), ensure they access your [Security Copilot](microsoft-security-copilot) capabilities only when you grant them access.

There are several ways to allow a partner to manage your Security Copilot.

1. Azure Lighthouse Approve your MSSP to gain Security Copilot permissions for your Microsoft Sentinel workspaces and other supported Azure resources. The capacity plan (SCUs) used are the partner tenant's capacity plan.
2. GDAP (recommended) Approve your MSSP to gain Security Copilot permissions for your tenant. They assign a security group the permissions needed using Granular Delegated Admin Privileges (GDAP). The capacity plan (SCUs) used are the customer's capacity plan.
3. B2B collaboration Set up guest accounts for individuals from your partner to log into your tenant. The capacity plan (SCUs) used are the customer tenant's capacity plan.

## Compare access methods

There are tradeoffs for these methods. Use the following table to help decide which method is best for your organization. It's possible to mix these methods for an overall partner strategy.

| Consideration | GDAP | B2B collaboration | Azure Lighthouse |
| --- | --- | --- | --- |
| How is **time-bound access** implemented? | Access is time-bound by default and built into the permission approval process. | Customers can implement Privileged Identity Management (PIM) with time-bound access, but they must maintain it themselves. | Privileged Identity Management (PIM) with time-bound access is possible for Azure role-based access control (Azure RBAC). |
| How is **least-privileged access** administered? | GDAP requires security groups. A list of least-privileged roles needed guides the setup. | Security groups are optional, and maintained by customer. | Azure Lighthouse requires Microsoft Entra security groups. For more information, see [Tenants, users, and roles in Azure Lighthouse scenarios](/en-us/azure/lighthouse/concepts/tenants-users-roles). |
| What **plugins are supported**? | A partial set of plugins are supported. | All plugins available for the customer are available to the partner. | Azure Lighthouse supports delegated access to Azure resources, which includes Microsoft Sentinel. For more information on supported workloads, see [What is Azure Lighthouse](/en-us/azure/lighthouse/overview). |
| What is the **standalone login** experience? | The MSSP uses **Service management** to seamlessly log into Security Copilot for the appropriate tenant. | Use the tenant switch selection from the Security Copilot setting. | The MSSP analyst, from their Security Copilot standalone portal, is able to prompt against any Microsoft Sentinel workspace that the analyst has permissions to access using the Azure Lighthouse delegated access. |
| What is the **embedded experience**? | Supported, with **Service management** links to facilitate access. | Supported normally. | Supported, with the Unified SecOps Platform integration between Microsoft Defender XDR and Microsoft Sentinel. Microsoft Sentinel incidents show under "Investigation & response" allowing for embedded Security Copilot experiences to be ran. For more information, see [Microsoft Defender XDR integration with Sentinel](/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration?tabs=azure-portal). |
| Who's Security Copilot capacity plan (SCUs) are used when performing prompts? | Customer tenant's capacity plan. | Customer tenant's capacity plan. | Partner tenant's capacity plan. |

## Grant partner access using Azure Lighthouse

Azure Lighthouse allows an MSSP to set up least-privileged and time-bound access explicitly granted by the Security Copilot customer for delegated access to Azure resources. When performing Security Copilot prompts within the partner's tenant against Microsoft Sentinel workspaces of the customer, the partner's capacity plan SCUs are used instead of the customer's capacity plan SCUs.

For more information, see [Introduction to Azure Lighthouse](/en-us/azure/lighthouse/overview).

Here's the current matrix of Security Copilot plugins that support Azure Lighthouse:

| Security Copilot plugin | Supports Azure Lighthouse |
| --- | --- |
| Microsoft Defender External Attack Surface Mgmt | No |
| Microsoft Defender Threat Intelligence | No |
| Microsoft Defender XDR | No |
| Microsoft Entra | No |
| Microsoft Intune | No |
| Microsoft Purview | No |
| Microsoft Sentinel | Yes |
| NL2KQL Defender | No |
| NL2KQL Sentinel | Yes |

### Onboard a customer to Azure Lighthouse

1. Gather tenant and subscription details

    - To onboard a customer's tenant, you must have an active Azure subscription, and you'll need the following information to create an Azure Resource Manager template.
        - MSSP's tenant ID
        - Customer's tenant ID
        - Azure Subscription IDs for each specific subscription in the customer's tenant that will be managed by the MSSP including the offering details.
        - For more information, see, [Onboard a customer to Azure Lighthouse](/en-us/azure/lighthouse/how-to/onboard-customer#gather-tenant-and-subscription-details).
        - For more information If you require publishing a private or public managed service offering to Azure Marketplace, see [Publish a Managed Service offer to Azure Marketplace](/en-us/azure/lighthouse/how-to/publish-managed-services-offers).
2. Define roles and permissions

    - As a service provider, you may want to perform multiple tasks for a single customer, requiring different access for different scopes. You can define as many authorizations as you need in order to assign the appropriate Azure built-in roles. To define authorizations in your template, you must include the ID values for each user, user group, or service principal in the managing tenant to which you want to grant access. You'll also need to include the role definition ID for each built-in role you want to assign. For more information, see, [Onboard a customer to Azure Lighthouse - Azure Lighthouse](/en-us/azure/lighthouse/how-to/onboard-customer#define-roles-and-permissions).
    - To use Microsoft Entra Privileged Identity Management (PIM) for just-in-time access, you need to create eligible authorizations. For more information, see [Create eligible authorizations](/en-us/azure/lighthouse/how-to/create-eligible-authorizations).
3. Create an Azure Resource Manager template

    - To onboard your customer, you need to create an Azure Resource Manager template for your offer with the following information. The mspOfferName and mspOfferDescription values are visible to the customer in the Service providers page of the Azure portal once the template is deployed in the customer's tenant. You can create this template in the Azure portal, or by manually modifying the templates provided in our [samples repo](https://github.com/Azure/Azure-Lighthouse-samples/). For more information, see, [Onboard a customer to Azure Lighthouse](/en-us/azure/lighthouse/how-to/onboard-customer#create-an-azure-resource-manager-template).
4. Deploy Azure Resource Manager template

    - Once you have created your template, a user in the customer's tenant must deploy it within their tenant. A separate deployment is needed for each subscription that you want to onboard (or for each subscription that contains resource groups that you want to onboard). The deployment may be done by using PowerShell, by using Azure CLI, or in the Azure portal. For more information, see, [Onboard a customer to Azure Lighthouse](/en-us/azure/lighthouse/how-to/onboard-customer#deploy-the-azure-resource-manager-template).
5. Confirm successful onboarding

    - When a customer subscription has successfully been onboarded to Azure Lighthouse, users in the service provider's tenant will be able to see the subscription and its resources. You can confirm this within the Azure portal, using PowerShell or by using Azure CLI. For more information, see, [Onboard a customer to Azure Lighthouse](/en-us/azure/lighthouse/how-to/onboard-customer#confirm-successful-onboarding).

## Grant partner access using GDAP

GDAP allows an MSSP to set up least-privileged and time-bound access explicitly granted by the Security Copilot customer. Only MSSPs registered as a Cloud Solution Partner (CSP) are allowed to manage Security Copilot. Access is assigned to an MSSP security group, which reduces the administrative burden for both the customer and the partner. An MSSP user is assigned the appropriate role and security group to manage the customer.

For more information, see [Introduction to GDAP](/en-us/partner-center/gdap-introduction).

Here's the current matrix of Security Copilot plugins that support GDAP:

| Security Copilot plugin | Supports GDAP |
| --- | --- |
| Defender External Attack Surface Management | No |
| Microsoft Entra | Overall, no, but a few capabilities work. |
| Intune | Yes |
| MDTI | No |
| Defender XDR | Yes |
| NL2KQL Defender | Yes |
| NL2KQL Sentinel | No |
| Purview | Yes |
| Microsoft Sentinel | No |

For more information, see [Workloads supported by GDAP](/en-us/partner-center/gdap-supported-workloads).

### GDAP relationship

1. The MSSP sends a GDAP request to their customer. Follow the instructions in this article, [Obtain permissions to manage customer](/en-us/partner-center/gdap-obtain-admin-permissions-to-manage-customer). For best results, the MSSP should request **Security reader** and **Security operator** roles to access Security Copilot platform and plugins. For more information, see [Understand authentication](authentication).
2. The customer approves the GDAP request from the partner. For more information, see [Customer approval](/en-us/partner-center/gdap-customer-approval).

### Security group permissions

1. The MSSP creates a security group and assigns it the approved permissions. For more information, see [Assign Microsoft Entra roles](/en-us/partner-center/gdap-assign-microsoft-entra-roles).
2. The customer adds the roles the MSSP requested to the appropriate Security Copilot role (Copilot owner or copilot contributor). For example, if the MSSP requested **Security operator** permissions, the customer adds that role to the **Copilot contributor** role within Security Copilot. For more information, see [Assigning Security Copilot roles](authentication#assign-roles).

### MSSP Security Copilot access

1. The MSSP user account needs membership to the partner security group assigned and an approved role to access the delegated Microsoft Sentinel workspace of the customer in the partner tenant.
2. The MSSP can access Security Copilot standalone portal and use the example prompts below:

    - "List all Sentinel workspaces" to see all available Sentinel workspaces within the partner tenant and the delegated customer Microsoft Sentinel workspaces.
    - "Summarize incident &lt;incident ID&gt; from workspace &lt;name of customer's Microsoft Sentinel workspace&gt;" to see a summarization of the Microsoft Sentinel incident from the customer's Microsoft Sentinel workspace.
3. The MSSP can access their Security Copilot's Usage Monitoring Dashboard in the standalone experience to see the SCU cost associated with the prompt performed against the customer's Microsoft Sentinel workspace. This can be validated by seeing the session ID in the Usage Monitoring Dashboard and the session ID in the browser URL when viewing the Security Copilot session.

## Grant partner access using B2B collaboration

B2B collaboration invites individual partner accounts as guests to the customer tenant to operate Security Copilot.

### Set up a guest account for your partner

Note

To perform the procedures described in this option, you must have an appropriate role, such as User Administrator, or Billing Administrator, assigned in Microsoft Entra.

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com) and sign in.
2. Go to **Identity** &gt; **Users** &gt; **All users**.
3. Select **New user** &gt; **Invite external user**, and then specify settings for the guest account.

    1. On the **Basics** tab, fill in the user's email address, display name, and a message if you want to include one. (You can optionally add a **Cc recipient** to receive a copy of the email invitation.)
    2. On the **Properties** tab, in the **Identity** section, fill in the user's first and last name. (You can optionally fill in any other fields you want to use.)
    3. On the **Assignments** tab, select **+ Add role**. Scroll down, and select either **Security Operator** or **Security Reader**.
    4. On the **Review + invite** tab, review your settings. When you're ready, select **Invite**.

        The partner receives an email with a link to accept the invitation to join your tenant as a guest.

Tip

To learn more about setting up a guest account, see [Invite an external user](/en-us/azure/active-directory/fundamentals/how-to-create-delete-users#invite-an-external-user).

### B2B access to Security Copilot

After you have set up a guest account for your partner, you're ready to notify them that they can now use your Security Copilot capabilities.

1. Tell your partner to look for an email notification from Microsoft. The email contains details about their user account and includes a link they must select to accept the invitation.
2. Your partner accesses Security Copilot by visiting https://securitycopilot.microsoft.com and signing in using their email account.
3. The partner uses the tenant switch feature to ensure they're accessing the appropriate customer. For example, the following image shows a partner from Fabrikam using their credentials to work in Security Copilot for their customer, Contoso.

    ![Screenshot showing tenant switch setting.](media/tenant-switch.png) Alternatively, set the tenant ID directly in the URL, for example,`https://securitycopilot.microsoft.com/?tenantId=aaaabbbb-0000-cccc-1111-dddd2222eeee`.
4. Share the following articles to help your MSSP get started using Security Copilot:

    - [Navigate Microsoft Security Copilot](navigating-security-copilot)
    - [Get started with Microsoft Security Copilot](get-started-security-copilot)
    - [Investigate an incident's malicious script](investigate-incident-malicious-script)

## Get technical support for partner access setup

Currently, if your MSSP or partner has questions and needs technical support for Security Copilot outside of the partner center, the customer organization should contact support on the MSSP's behalf.