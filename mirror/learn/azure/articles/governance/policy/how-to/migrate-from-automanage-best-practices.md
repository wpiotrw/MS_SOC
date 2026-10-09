---
layout: Conceptual
title: Azure Automanage Best Practices to Azure Policy migration planning - Azure Policy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/how-to/migrate-from-automanage-best-practices
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: kgremban
learn_banner_products:
- azure
ms.author: kgremban
ms.service: azure-policy
description: This article provides process and technical guidance for customers interested in moving from Azure Automanage Best Practices to Azure Policy.
ms.date: 2025-03-04T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: a37fd972-53d5-7323-5cd3-e58d1bfeab14
document_version_independent_id: 99f597fb-8e96-dea7-0199-5872b30bc52c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/how-to/migrate-from-automanage-best-practices.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/policy/how-to/migrate-from-automanage-best-practices
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/how-to/migrate-from-automanage-best-practices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 2f19ab5e-4f55-d3bc-d7c2-56a4515dadcf
---

# Azure Automanage Best Practices to Azure Policy migration planning - Azure Policy | Microsoft Learn

Caution

On September 30, 2027, the Azure Automanage Best Practices service will be retired. Migrate to Azure Policy before that date. For more information on migration, see the [Azure portal](https://portal.azure.com/). Learn how to [disable Azure Automanage](/en-us/azure/automanage/how-to-disable-automanage).

Caution

Starting February 1st 2025, Azure Automanage will begin rolling out changes to halt support and enforcement for all services dependent on the deprecated Microsoft Monitoring Agent (MMA). To continue using Change Tracking and Management, VM Insights, Update Management, and Azure Automation, [migrate to the new Azure Monitor Agent (AMA)](https://aka.ms/mma-to-ama/).

Azure Policy is a more robust cloud resource governance, enforcement, and compliance offering with full parity with the Azure Automanage Best Practices service. When possible, you should plan to move your content and machines to the new service. This article provides guidance on developing a migration strategy from Azure Automation to machine configuration. Azure Policy implements a robust array of features, including:

- **Granular control and flexibility:** Azure Policy allows for highly granular control over resources. You can create custom policies tailored to your specific regulatory and organizational compliance needs to ensure that every aspect of your infrastructure meets the required standards. This level of customization might not be as easy to achieve with the predefined configurations in Automanage.
- **Comprehensive compliance management:** Azure Policy offers comprehensive compliance management by continuously assessing and auditing your resources. Detailed reports and dashboards help you to track compliance status. These features help you to quickly detect and rectify noncompliance issues across your environment.
- **Scalability:** Azure Policy is built to manage large-scale environments efficiently. You can apply policies at different scopes, such as management group, subscription, and resource group levels. This capability helps you to enforce compliance across multiple resources and regions systematically.
- **Integration with Azure Security Center:** Azure Policy integrates seamlessly with Azure Security Center. You have the ability to manage security policies and ensure that your servers adhere to best practices. This integration provides more insights and recommendations, which further strengthen your security posture.

Before you begin, read the conceptual overview information on the [Azure Policy](../overview) webpage.

## Understand migration

The best approach to migration is to identify how to map services in an Automanage configuration profile to the respective Azure Policy content first. Then offboard your subscriptions from Automanage. This section outlines the expected steps for migration.

Automanage designers created an experience for Azure customers to onboard new and existing virtual machines (VMs) to a recommended set of Azure services to ensure compliance with Azure best practices. The capabilities include a configuration profile, a reusable template of management, monitoring, security, and resiliency services that customers can opt into. The profile is assigned to a set of VMs that are onboarded to those services, and customers then receive reports on the state of their machines.

This functionality is available in Azure Policy as an initiative with various configurable parameters, Azure services, regional availability, compliance states, and remediation actions. Configuration profiles are the main onboarding vehicle for Automanage customers. Just like Azure Policy initiatives, Automanage configuration profiles apply to VMs at the subscription and resource group level. They enable further specification of the zone of applicability. The following Automanage feature parities are available in Azure Policy.

### Azure Monitor Insights and analytics

[Azure Monitor](/en-us/azure/azure-monitor/overview) is a suite of tools designed to enhance the performance, reliability, and quality of your applications. It offers features like application performance management, monitoring alerts, metrics analysis, diagnostic settings, and logs. With Azure Monitor Insights, you can gain valuable insights into your application's behavior, troubleshoot issues, and optimize performance.

The Azure Monitor agent collects monitoring data from the guest operating system of Azure and hybrid VMs. The agent delivers the data to Azure Monitor for use by features, insights, and other services, such as Microsoft Sentinel and Microsoft Defender for Cloud. The Azure Monitor agent replaces all of the Azure Monitor legacy monitoring agents like the deprecated Microsoft Monitor Agent. The new Azure Monitor Agent is unsupported in Automanage but can be configured at-scale using Azure Policy. Visit [Azure Monitor Agent Built-In Policy](/en-us/azure/azure-monitor/policy-reference) to learn more.

### Azure Backup

[Azure Backup](/en-us/azure/backup/backup-overview) provides independent and isolated backups to guard against unintended destruction of the data on your VMs. Backups are stored in a Recovery Services vault with built-in management of recovery points. To back up Azure VMs, Backup installs an extension on the VM agent running on the machine. Visit [Azure Backup Built-In Policy](/en-us/azure/backup/policy-reference) to learn how to configure Backup at scale through Azure Policy. To configure Backup time and duration, create a custom Azure policy based on the properties of the Backup policy resource or by a REST API call. For more information, see [Create Recovery Services backup policies by using the REST API](../../../backup/backup-azure-arm-userestapi-createorupdatepolicy).

### Microsoft Antimalware for Azure

[Microsoft Antimalware](/en-us/azure/security/fundamentals/antimalware#antimalware-deployment-scenarios) for Azure Cloud Services and Virtual Machines offers free real-time protection that helps identify and remove viruses, spyware, and other malicious software. It generates alerts when known malicious or unwanted software tries to install itself or run on your Azure systems. The Azure Guest agent (or the Microsoft Fabric agent) opens the Microsoft Antimalware for Azure extension and applies the antimalware configuration settings that were supplied as input. This step enables the antimalware service with either default or custom configuration settings.

Deploy the following Microsoft Antimalware for Azure policies in Azure Policy:

- Configure Microsoft Antimalware for Azure to automatically update protection signatures.
- Deploy the Microsoft `IaaSAntimalware` extension on Windows servers.
- Deploy the default Microsoft `IaaSAntimalware` extension for Windows Server.

You can create a custom Azure policy based on the properties of the Azure `IaaSAntimalware` policy resource or by using an Azure Resource Manager template (ARM template). You can use the custom policy to:

- Configure excluded files, locations, file extensions, and processes.
- Enable real-time protection.
- Schedule a scan, and scan type, day, and time.

For more information, see [this webpage](/en-us/azure/virtual-machines/extensions/iaas-antimalware-windows).

### Change Tracking and Inventory

[Change Tracking and Inventory](/en-us/azure/automation/change-tracking/overview) is a feature within Automation that monitors changes in VMs across Azure, on-premises, and in other cloud environments. It tracks modifications to installed software, files, registry keys, and services on both Windows and Linux systems. Change Tracking and Inventory uses the Log Analytics agent to collect data and then forwards it to Azure Monitor Logs for analysis. It also integrates with Microsoft Defender for Cloud File Integrity Monitoring to enhance security and operational insights.

Enable change tracking on VMs by using the following policies:

- Assign built-in user-assigned managed identity to VMs.
- Configure Windows VMs to install the Azure Monitor agent for Change Tracking and Inventory with user-assigned managed identity.
- Configure Linux VMs to install the Azure Monitor agent for Change Tracking and Inventory with a user-assigned managed identity.
- Configure the Change Tracking and Inventory extension for Windows VMs.
- Configure the Change Tracking and Inventory extension for Linux VMs.
- Configure Windows VMs to associate with a data collection rule for Change Tracking and Inventory.

Configure the preceding Azure policies in bulk by using the following Azure Policy initiatives:

- [Preview]: Enable Change Tracking and Inventory for virtual machine scale sets.
- [Preview]: Enable Change Tracking and Inventory for VMs.
- [Preview]: Enable Change Tracking and Inventory for Azure Arc-enabled VMs.

### Microsoft Defender for Cloud

[Microsoft Defender for Cloud](/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) (MDC) provides unified security management and advanced threat protection across hybrid cloud workloads. Visit [Configure Defender for Cloud in Azure Policy](/en-us/azure/defender-for-cloud/policy-reference) to learn more about at-scale compliance and monitoring for MDC.

### Azure Update Manager

[Azure Update Manager](/en-us/azure/update-manager/overview) (AUM) is a service included as part of your Azure subscription. Use it to assess your update status across your environment and manage your Windows and Linux server patching from a single pane of glass, both for on-premises and Azure. It provides a unified solution to help you keep your systems up to date. Update Manager oversees update compliance, deploys critical updates, and offers flexible patching options. Visit [Azure Update Manager Built-In Policy](/en-us/azure/update-manager/periodic-assessment-at-scale) to learn how to configure AUM at scale through Azure Policy.

### Azure Automation account

[Azure Automation](/en-us/azure/automation/overview) is a cloud-based service that provides consistent management across your Azure and non-Azure environments. Use it to automate repetitive tasks, enforce configuration consistency, and manage updates for VMs. By using runbooks and shared assets, you can streamline operations and reduce operational costs. Visit [Azure Automation Built-In Policy](/en-us/azure/automation/policy-reference) to learn how to configure AUM at scale through Azure Policy.

### Boot diagnostics

Boot diagnostics is a debugging feature for Azure VMs that you can use to diagnose VM boot failures. The feature collects serial log information and screenshots so that you can observe the state of your VM as it boots up. After you enable the boot diagnostics feature, the Azure cloud platform can inspect the VM operating system for provisioning errors. The feature helps to provide deeper information on the root causes of startup failures. Boot diagnostics is enabled by default when you create a VM and is enforced by the **Boot Diagnostics should be enabled on virtual machines** policy.

### Windows Admin Center

You can now use Windows Admin Center in the Azure portal to manage the Windows operating system inside an Azure VM. You can also manage operating system functions from the Azure portal and work with files in the VM without using Remote Desktop or PowerShell. You can use an ARM template or a custom Azure Policy for configuration. For more information, see [Manage a Windows VM by using Windows Admin Center in Azure](/en-us/windows-server/manage/windows-admin-center/azure/manage-vm).

### Log Analytics workspace

Log Analytics is an Azure Monitor feature that monitors your cloud and on-premises resources and applications. Use it to collect and analyze data generated by resources in your cloud and on-premises environments. With Log Analytics, you can search, analyze, and visualize data to identify trends, troubleshoot issues, and monitor your systems.

On August 31, 2024, both Automation Update Management and the Log Analytics agent that it used were retired. You should have migrated to Azure Update Manager before that date. For guidance on how to migrate to Azure Update Manager, see [Overview of migration from Automation Update Management to Azure Update Manager](../../../update-manager/migration-overview). We advise you to migrate [now](https://portal.azure.com/) because this feature is no longer supported in Automanage.

## Pricing

Automanage Best Practices is a free service, so you don't receive a bill from Automanage. If you used Automanage to enable paid services like Azure Monitor Insights, you might incur usage charges. Those services bill you directly.

Read more about Automanage and pricing on the [Azure Automanage pricing webpage](https://azure.microsoft.com/pricing/details/azure-automanage/).