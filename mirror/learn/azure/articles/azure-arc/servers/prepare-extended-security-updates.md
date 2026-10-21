---
layout: Conceptual
title: Prepare to deliver Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/prepare-extended-security-updates
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
zone_pivot_group_filename: zone-pivots/azure-management/zone-pivot-groups.json
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to prepare to deliver Extended Security Updates for Windows Server 2012 and Windows Server 2016 through Azure Arc.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: how-to
zone_pivot_groups: extended-security-updates-windows-server
locale: en-us
document_id: 504906db-216f-5583-7e8c-ba3910e53661
document_version_independent_id: 1ed93905-fce0-29e6-d9d4-20ad36144135
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/prepare-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/prepare-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/prepare-extended-security-updates.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: bd1b369d-2b1e-ff9c-1c07-858f9ad44540
---

# Prepare to deliver Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn

By using Azure Arc-enabled servers, you can enroll your existing Windows Server machines in [Extended Security Updates (ESUs)](/en-us/windows-server/get-started/extended-security-updates-overview) after they reach end of support. Offering both cost flexibility and an enhanced delivery experience, Azure Arc better positions you to migrate to Azure. Select the version of Windows Server that you're enrolling to see version-specific guidance.

The purpose of this article is to help you understand the benefits and how to prepare to use Arc-enabled servers to enable delivery of ESUs.

::: zone pivot="windows-server-2012"

Windows Server 2012 and Windows Server 2012 R2 reached end of support on October 10, 2023. The three-year ESU period ends on October 13, 2026, and the October 13, 2026 security update is the final update provided through ESUs. At midnight Coordinated Universal Time (UTC) on October 14, 2026, Windows Server 2012 ESU licenses enabled by Azure Arc are deactivated and stop providing update eligibility. Plan to migrate your workloads or upgrade to a supported version of Windows Server before the ESU period ends. For more information, see [Overview of Extended Security Updates for Windows Server 2012 and Windows Server 2012 R2](/en-us/windows-server/get-started/extended-security-updates-overview).

Note

Azure VMware Solution (AVS) machines and virtual machines on Azure Local are eligible for free ESUs and shouldn't enroll in ESUs enabled through Azure Arc.

::: zone-end

::: zone pivot="windows-server-2016"

Windows Server 2016 reaches end of support on January 12, 2027. Extended Security Updates for Windows Server 2016 provide Critical and Important security updates for up to three years, through 2030. ESUs don't include new features, customer-requested nonsecurity hotfixes, or design change requests.

You can configure Windows Server 2016 ESUs in the Azure portal starting August 3, 2026. Billing for Windows Server 2016 ESUs enabled by Azure Arc begins January 13, 2027.

::: zone-end

## Key benefits

Delivering ESUs to your Windows Server machines provides the following key benefits:

- **Pay-as-you-go:** Flexibility to sign up for a monthly subscription service with the ability to migrate mid-year.
- **Azure billed:** You can draw down from your existing [Microsoft Azure Consumption Commitment (MACC)](/en-us/marketplace/azure-consumption-commitment-benefit) and analyze your costs using [Microsoft Cost Management and Billing](/en-us/azure/cost-management-billing/cost-management-billing-overview).
- **Built-in inventory:** The coverage and enrollment status of ESUs on eligible Arc-enabled servers are identified in the Azure portal, highlighting gaps and status changes.
- **Keyless delivery:** The enrollment of ESUs on Azure Arc-enabled machines doesn't require the acquisition or activation of keys.

## Access to Azure services

For Azure Arc-enabled servers enrolled in ESUs enabled by Azure Arc, free access is provided to these Azure services for enrolled servers:

- [Azure Update Manager](/en-us/azure/update-center/overview) - Unified management and governance of update compliance that includes not only Azure and hybrid machines, but also ESU update compliance for all your Windows Server machines. Enrollment in ESUs does not impact Azure Update Manager. After enrollment in ESUs through Azure Arc, the server becomes eligible for ESU patches. These patches can be delivered through Azure Update Manager or any other patching solution. You still need to configure updates from Microsoft Updates or Windows Server Update Services.
- [Change Tracking and Inventory](/en-us/azure/automation/change-tracking/overview-monitoring-agent?tabs=win-az-vm) - Track changes in virtual machines hosted in Azure, on-premises, and other cloud environments.
- [Azure Policy Guest Configuration](/en-us/azure/cloud-adoption-framework/manage/azure-server-management/guest-configuration-policy) - Audit the configuration settings in a virtual machine. Guest configuration supports Azure VMs natively and non-Azure physical and virtual servers through Azure Arc-enabled servers.

Other Azure services through Azure Arc-enabled servers are available as well, with offerings such as:

- [Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) - As part of the cloud security posture management (CSPM) pillar, it provides server protections through [Microsoft Defender for Servers](/en-us/azure/defender-for-cloud/plan-defender-for-servers) to help protect you from various cyber threats and vulnerabilities.
- [Microsoft Sentinel](scenario-onboard-azure-sentinel) - Collect security-related events and correlate them with other data sources.

## Prepare delivery of ESUs

::: zone pivot="windows-server-2012"

1. Plan and prepare to connect your machines to Azure Arc-enabled servers by installing the [Azure Connected Machine agent](agent-overview) to establish a connection to Azure. For Windows Server 2012 ESUs, use agent version 1.34 or higher.

    After establishing this connection, you can enroll your servers to receive Extended Security Updates (ESUs). Both Standard and Datacenter editions are supported. Deploy your machines to Azure Arc so that you have visibility into their ESU coverage and can enroll through the Azure portal or by using Azure Policy.
2. Download both the licensing package and servicing stack update (SSU) for the Azure Arc-enabled server as documented in the applicable Microsoft Knowledge Base article. For Windows Server 2012, see [KB5031043: Procedure to continue receiving security updates after extended support has ended on October 10, 2023](https://support.microsoft.com/topic/kb5031043-procedure-to-continue-receiving-security-updates-after-extended-support-has-ended-on-october-10-2023-c1a20132-e34c-402d-96ca-1e785ed51d45).

::: zone-end

::: zone pivot="windows-server-2016"

1. Plan and prepare to connect your machines to Azure Arc-enabled servers by installing the [Azure Connected Machine agent](agent-overview) to establish a connection to Azure. For Windows Server 2016 ESUs, use agent version 1.62 or higher.

    After establishing this connection, you can enroll your servers to receive Extended Security Updates (ESUs). Both Standard and Datacenter editions are supported. Deploy your machines to Azure Arc so that you have visibility into their ESU coverage and can enroll through the Azure portal or by using Azure Policy.

::: zone-end

Review the version-specific eligibility and licensing requirements before you enroll.

::: zone pivot="windows-server-2012"

Windows Server 2012 Extended Security Updates support Windows Server 2012 and 2012 R2 Standard and Datacenter editions. Windows Server 2012 Storage isn't supported. Billing for this service starts in October 2023 (that is, after Windows Server 2012 end of support).

Note

To purchase ESUs, you must have Software Assurance through Volume Licensing Programs such as an Enterprise Agreement (EA), Enterprise Agreement Subscription (EAS), Enrollment for Education Solutions (EES), Server and Cloud Enrollment (SCE), or through Microsoft Open Value Programs. Alternatively, if your Windows Server 2012/2012 R2 machines are licensed through SPLA or with a Server Subscription, Software Assurance isn't required to purchase ESUs.

::: zone-end

::: zone pivot="windows-server-2016"

Windows Server 2016 Extended Security Updates support Windows Server 2016 Standard and Datacenter editions. You can configure Windows Server 2016 ESUs in the Azure portal starting August 3, 2026, and billing begins January 13, 2027.

Note

To purchase ESUs, you must have Software Assurance through Volume Licensing Programs such as an Enterprise Agreement (EA), Enterprise Agreement Subscription (EAS), Enrollment for Education Solutions (EES), Server and Cloud Enrollment (SCE), or through Microsoft Open Value Programs. Alternatively, if your Windows Server 2016 machines are licensed through SPLA or with a Server Subscription, Software Assurance isn't required to purchase ESUs.

::: zone-end

### Deployment options

You can onboard Azure Arc-enabled servers at scale by using the following options:

- Run a [Custom Task Sequence](onboard-configuration-manager-custom-task) through Configuration Manager.
- Deploy a [Scheduled Task through Group Policy](onboard-group-policy-powershell).
- Use [VMware vCenter managed VMs](../vmware-vsphere/deliver-extended-security-updates-for-vmware-vms-through-arc) through Azure Arc.
- Use [SCVMM managed VMs](../system-center-virtual-machine-manager/deliver-esus-for-system-center-virtual-machine-manager-vms) through Azure Arc.

Note

Don't use Azure Arc to deliver ESUs to virtual machines running on Virtual Desktop Infrastructure (VDI). Use Multiple Activation Keys (MAK) to apply ESUs to VDI systems. To learn more, see [Access your Multiple Activation Key from the Microsoft 365 Admin Center](/en-us/windows-server/get-started/extended-security-updates-deploy).

### Networking

Ensure your machines have the necessary network connectivity to Azure Arc. Connectivity options include:

- Public endpoint
- Proxy server
- Private link or Azure Express Route.

Review the [networking prerequisites](network-requirements) to prepare non-Azure environments for deployment to Azure Arc.

If you use Azure Arc-enabled servers only for Extended Security Updates for one or more of the following products:

- Windows Server 2012
- Windows Server 2016
- SQL Server 2012

You can enable the following subset of endpoints.

# [Azure cloud platform](#tab/azure-cloud)
| Agent resource | Description | When required | Endpoint used with private link |
| --- | --- | --- | --- |
| `download.microsoft.com` | Used to download the Windows installation package. | Only at installation time.^1^ | Public. |
| `login.windows.net` | Microsoft Entra ID. | Always. | Public. |
| `login.microsoftonline.com` | Microsoft Entra ID. | Always. | Public. |
| `*.login.microsoft.com` | Microsoft Entra ID. | Always. | Public. |
| `management.azure.com` | Azure Resource Manager is used to create or delete the Azure Arc server resource. | Only when you connect or disconnect a server. | Public, unless a [resource management private link](/en-us/azure/azure-resource-manager/management/create-private-link-access-portal) is also configured. |
| `*.his.arc.azure.com` | Metadata and hybrid identity services. | Always. | Private. |
| `*.guestconfiguration.azure.com` | Extension management and guest configuration services. | Always. | Private. |
| `www.microsoft.com/pkiops/certs` | Intermediate certificate updates for Extended Security Updates (uses HTTP/TCP 80 and HTTPS/TCP 443). | Always for automatic updates or temporarily if you download certificates manually. | Public. |
| `*.<region>.arcdataservices.com` | Azure Arc data processing service and service telemetry. | SQL Server Extended Security Updates. | Public. |

^1^ Access to this URL is also needed when you perform updates automatically.

# [Azure Government](#tab/azure-government)
| Agent resource | Description | When required | Endpoint used with private link |
| --- | --- | --- | --- |
| `download.microsoft.com` | Used to download the Windows installation package. | Only at installation time.^1^ | Public. |
| `login.microsoftonline.us` | Microsoft Entra ID. | Always. | Public. |
| `management.usgovcloudapi.net` | Azure Resource Manager is used to create or delete the Azure Arc server resource. | Only when you connect or disconnect a server. | Public, unless a [resource management private link](/en-us/azure/azure-resource-manager/management/create-private-link-access-portal) is also configured. |
| `*.his.arc.azure.us` | Metadata and hybrid identity services. | Always. | Private. |
| `*.guestconfiguration.azure.us` | Extension management and guest configuration services. | Always. | Private. |
| `www.microsoft.com/pkiops/certs` | Intermediate certificate updates for Extended Security Updates (uses HTTP/TCP 80 and HTTPS/TCP 443). | Always for automatic updates or temporarily if you download certificates manually. | Public. |
| `*.blob.core.usgovcloudapi.net` | Download SQL Server Extension package. | SQL Server Extended Security Updates. | Not required if you use Azure Private Link. |

^1^ Access to this URL is also needed when you perform updates automatically.

# [Azure operated by 21Vianet](#tab/azure-china)
Note

Azure Arc-enabled servers used for Extended Security Updates for Windows Server 2012 and Windows Server 2016 aren't available in Microsoft Azure operated by 21Vianet regions at this time.

---

Tip

To take advantage of the full range of offerings for Arc-enabled servers, such as extensions and remote connectivity, ensure that you allow the additional URLs that apply to your scenario. For more information, see [Connected machine agent networking requirements](network-requirements).

## Required Certificate Authorities

The following [Certificate Authorities](/en-us/azure/security/fundamentals/azure-ca-details?tabs=root-and-subordinate-cas-list) are required for Extended Security Updates:

- [Microsoft Azure RSA TLS Issuing CA 03](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2003%20-%20xsign.crt)
- [Microsoft Azure RSA TLS Issuing CA 04](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2004%20-%20xsign.crt)
- [Microsoft Azure RSA TLS Issuing CA 07](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2007%20-%20xsign.crt)
- [Microsoft Azure RSA TLS Issuing CA 08](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2008%20-%20xsign.crt)

If necessary, you can [manually download and install](troubleshoot-extended-security-updates#option-2-manually-download-and-install-the-intermediate-ca-certificates) these Certificate Authorities.