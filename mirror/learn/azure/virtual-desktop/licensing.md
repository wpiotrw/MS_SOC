---
layout: Conceptual
title: Licensing Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/licensing
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: cosmeao
manager: eliotgra
ms.author: cosmeochoa
ms.service: azure-virtual-desktop
description: An overview of licensing Azure Virtual Desktop for internal and external commercial purposes, including per-user access pricing.
ms.topic: overview
ms.date: 2025-01-17T00:00:00.0000000Z
locale: en-us
document_id: e6c70e5f-db91-9a6d-1358-51420c982d4c
document_version_independent_id: e6c70e5f-db91-9a6d-1358-51420c982d4c
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/licensing.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: licensing
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/licensing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: 83ebbcc4-17f6-1816-2ae8-72e7d6500639
---

# Licensing Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn

This article explains the licensing requirements for using Azure Virtual Desktop, whether you're providing desktops or applications to users in your organization, or to external users. This article shows you how licensing Azure Virtual Desktop for external commercial purposes is different than for internal purposes, how per-user access pricing works in detail, and how you can license other products you plan to use with Azure Virtual Desktop.

## Internal and external commercial purposes

In the context of providing virtualized infrastructure with Azure Virtual Desktop, *internal users* (for internal commercial purposes) refers to people who are members of your own organization, such as employees of a business or students of a school, including external vendors or contractors. *External users* (for external commercial purposes) aren't members of your organization, but your customers where you might provide a Software-as-a-Service (SaaS) application using Azure Virtual Desktop.

Note

Take care not to confuse external *users* with external *identities*. Azure Virtual Desktop supports external identities, including guest accounts or business-to-business (B2B) identities, such as for contractors. For more information, see [Recommendations for deploying Azure Virtual Desktop for internal or external commercial purposes](organization-internal-external-commercial-purposes-recommendations) and Licensing recommendations for working with external identities.

Licensing Azure Virtual Desktop works differently for internal and external commercial purposes. Consider the following examples:

- A manufacturing company called *Fabrikam, Inc*. might use Azure Virtual Desktop to provide Fabrikam's employees (internal users) with access to virtual workstations and line-of-business apps. Because Fabrikam is serving internal users, Fabrikam must purchase one of the eligible licenses listed in [Azure Virtual Desktop pricing](https://azure.microsoft.com/pricing/details/virtual-desktop/) for each of their employees that access Azure Virtual Desktop.
- A retail company called *Wingtip Toys* might use Azure Virtual Desktop to provide an external contractor company (external users) with access to line-of-business apps. Because these external users are serving internal purposes, Wingtip Toys must purchase one of the eligible licenses listed in [Azure Virtual Desktop pricing](https://azure.microsoft.com/pricing/details/virtual-desktop/) for each of their contractors that access Azure Virtual Desktop. Per-user access pricing isn't applicable in this scenario.
- A software vendor called *Contoso* might use Azure Virtual Desktop to sell remote access of Contoso's productivity app to Contoso's customers (external users). Because Contoso is serving external users for external commercial purposes, Contoso must enroll in Azure Virtual Desktop's per-user access pricing. This enables Contoso to pay for Azure Virtual Desktop access rights on behalf of those external users who connect to Contoso's deployment. The users don't need a separate license like Microsoft 365 to access Azure Virtual Desktop. Contoso still needs to create and manage identities for those external users.

Important

Per-user access pricing can only be used for external commercial purposes, not internal purposes. Per-user access pricing isn't a way to enable external guest user accounts with Azure Virtual Desktop. Check if your Azure Virtual Desktop solution is applicable for per-user access pricing by reviewing [our licensing documentation](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftAzure/EAEAS#Documents).

## Eligible licenses to use Azure Virtual Desktop

You must provide an eligible license for each user that accesses Azure Virtual Desktop. The license you need also depends on whether you're using a Windows client operating system or a Windows Server operating system for your session hosts, and whether it's for internal or external commercial purposes. The following table shows the eligible licensing methods for each scenario:

| Operating system(64-bit only) | Licensing method(Internal commercial purposes) | Licensing method(External commercial purposes) |
| --- | --- | --- |
| - [Windows 11 Enterprise multi-session](/en-us/lifecycle/products/windows-11-enterprise-and-education)<br>- [Windows 11 Enterprise](/en-us/lifecycle/products/windows-11-enterprise-and-education)<br>- [Windows 10 Enterprise multi-session](/en-us/lifecycle/products/windows-10-enterprise-and-education)<br>- [Windows 10 Enterprise](/en-us/lifecycle/products/windows-10-enterprise-and-education) | - Microsoft 365 E3, E5, A3, A5, F3, Business Premium, Student Use Benefit<br>- Windows Enterprise E3, E5<br>- Windows Education A3, A5<br>- Windows VDA per user | [Per-user access pricing](licensing#per-user-access-pricing-for-external-commercial-purposes-to-use-azure-virtual-desktop) by enrolling an Azure subscription. |
| - [Windows Server 2025](/en-us/lifecycle/products/windows-server-2025)<br>- [Windows Server 2022](/en-us/lifecycle/products/windows-server-2022)<br>- [Windows Server 2019](/en-us/lifecycle/products/windows-server-2019)<br>- [Windows Server 2016](/en-us/lifecycle/products/windows-server-2016) | - Remote Desktop Services (RDS) Client Access License (CAL) with Software Assurance (per-user or per-device)<br>- RDS User Subscription Licenses. | Not supported. [Per-user access pricing](licensing#per-user-access-pricing-for-external-commercial-purposes-to-use-azure-virtual-desktop) isn't available for Windows Server operating systems. |

### Per-user access pricing for external commercial purposes to use Azure Virtual Desktop

Per-user access pricing lets you pay for Azure Virtual Desktop access rights for external commercial purposes. You must enroll in per-user access pricing to build a compliant deployment for external users.

You pay for per-user access pricing through your enrolled Azure subscription or subscriptions on top of your charges for virtual machines, storage, and other Azure services. Each billing cycle, you only pay for users who actually used the service. Only users that connect at least once in that month to Azure Virtual Desktop incur an access charge.

There are two price tiers for Azure Virtual Desktop per-user access pricing. Charges are determined automatically each billing cycle based on the type of [application groups](terminology#application-groups) a user connected to. Each price tier has flat per-user access charges. For example, a user incurs the same charge to your subscription no matter when or how many hours they used the service during that billing cycle. If a user doesn't access a RemoteApp or desktop, then there's no charge.

| Price tier | Description |
| --- | --- |
| *Apps* | A flat price is charged for each user who accesses at least one published RemoteApp, but doesn't access a published full desktop. |
| *Desktops + apps* | A flat price is charged for each user who accesses at least one published full desktop. The user can also access published applications. |

For more information about prices, see [Azure Virtual Desktop pricing](https://azure.microsoft.com/pricing/details/virtual-desktop/).

Important

Azure Virtual Desktop also charges users with separate assigned licenses that otherwise entitle them to Azure Virtual Desktop access. If you have internal users you're purchasing eligible licenses for, we recommend you give them access to Azure Virtual Desktop through a separate subscription that isn't enrolled in per-user access pricing to avoid effectively paying twice for those users.

Azure Virtual Desktop issues at most one access charge for a given user in a given billing period. For example, if you grant the user Alice access to Azure Virtual Desktop resources across two different Azure subscriptions in the same tenant, only the first subscription accessed by Alice incurs a usage charge.

To learn how to enroll an Azure subscription for per-user access pricing, see [Enroll in per-user access pricing](enroll-per-user-access-pricing).

### Licensing other products and services for use with Azure Virtual Desktop

The Azure Virtual Desktop per-user access license isn't a full replacement for a Windows or Microsoft 365 license. Per-user licenses only grant access rights to Azure Virtual Desktop and don't include Microsoft Office, Microsoft Defender XDR, or Universal Print. This means that if you choose a per-user license, you need to separately license other products and services to grant your users access to them in your Azure Virtual Desktop environment.

There are a few ways to enable your external users to access Office:

- Users can sign in to Office with their own Office account.
- You can resell Office through your Cloud Service Provider (CSP).
- You can distribute Office by using a Service Provider Licensing Agreement (SPLA).

## Licensing recommendations for working with external identities

If you're deploying Azure Virtual Desktop for use with external identities, there may be special considerations for how you license Azure Virtual Desktop and other products and services from Microsoft.

### Licensing Azure Virtual Desktop for external collaborators

Anyone accessing Azure Virtual Desktop or any other Online Services must be licensed, unless specified otherwise in the Online Service-specific Terms. This includes external collaborators, such as contractors.

Licenses assigned to an external collaborator in their own home tenant generally do not confer entitlements to Azure Virtual Desktop or other products within your tenant. Therefore, we generally recommend purchasing the same sort of license as you purchase for internal users and assigning it to the external collaborator's identity object in your Entra ID tenant.

Below are our licensing recommendations for Azure Virtual Desktop and some of the products most commonly deployed alongside it:

| Product | Recommendation for licensing B2B collaborators |
| --- | --- |
| Azure Virtual Desktop | Purchase and assign any license for internal business purposes from the Eligible licenses to use Azure Virtual Desktop table.Example: A Microsoft 365 E3 license you've assigned to an external collaborator grants Azure Virtual Desktop access rights within your tenant. |
| Microsoft Entra ID | Purchase and assign standalone Entra ID licenses, or use the entitlements that are included as a benefit of another license like Microsoft 365. In both cases, those benefits can be applied to an external collaborator.Example: A Microsoft 365 E3 license you've assigned to an external collaborator grants Entra ID P1 entitlements within your tenant. |
| Microsoft 365 Apps | Purchase and assign standalone licenses via Microsoft 365 Apps for enterprise, or use the entitlements that are included as a benefit of another license like Microsoft 365. In both cases, those benefits can be applied to an external collaborator.Example: A Microsoft 365 E3 license you've assigned to an external collaborator grants M365 Apps entitlements within your tenant. |
| Microsoft Intune | Purchase and assign standalone Intune licenses, or use the entitlements that are included as a benefit of another license like Microsoft 365. In both cases, those benefits can be applied to an external collaborator.Example: A Microsoft 365 E3 license you've assigned to an external collaborator grants Intune Plan 1 entitlements within your tenant. |
| Microsoft Defender | Purchase and assign standalone Defender for Endpoint licenses, or use the entitlements that are included as a benefit of another license like Microsoft 365. In both cases, those benefits can be applied to an external collaborator.Example: A Microsoft 365 E3 license you've assigned to an external collaborator grants Defender for Endpoint Plan 1 entitlements within your tenant. |

### Licensing Azure Virtual Desktop for multitenant organizations

In a [multitenant organization scenario](/en-us/entra/identity/multi-tenant-organizations/overview), you may wish to license Azure Virtual Desktop and other services to users based in multiple Entra ID tenants. External identities can be helpful for managing access to Azure Virtual desktop in such a scenario.

Licenses assigned to a user in one tenant of a multitenant organization generally do not confer entitlements to Azure Virtual Desktop or other products within another tenant of that organization. Therefore, we generally recommend purchasing a license for each user in each tenant in which access rights are required.

For example, a Microsoft 365 E3 license assigned to a user identity in Tenant A of a multitenant organization does not confer Azure Virtual Desktop access rights in Tenant B.

An exception to this is Entra ID. Only one Microsoft Entra ID P1 license is required per employee per multitenant organization. For more information, see [Entra ID multitenant organization license requirements](/en-us/entra/identity/multi-tenant-organizations/multi-tenant-organization-overview#license-requirements).

## Comparing licensing options

Here's a summary of the two types of licenses for Azure Virtual Desktop you can choose from:

| Component | Eligible Windows, Microsoft 365, or Remote Desktop Services (RDS) license | Per-user access pricing |
| --- | --- | --- |
| Access rights | Internal purposes only. It doesn't grant permission for external commercial purposes, not even identities you create in your own Microsoft Entra tenant. | External commercial purposes only. It doesn't grant access to members of your own organization or contractors for internal business purposes. |
| Billing | Licensing channels. | Pay-as-you-go through an Azure meter, billed to an Azure subscription. |
| User behavior | Fixed cost per user each month regardless of user behavior. | Cost per user each month depends on user behavior. |
| Other products | Dependent on the license. | Only includes access rights to Azure Virtual Desktop and [FSlogix](/en-us/fslogix/overview-what-is-fslogix). |