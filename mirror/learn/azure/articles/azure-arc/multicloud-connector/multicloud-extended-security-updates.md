---
layout: Conceptual
title: Attach Windows Server Extended Security Updates licenses with the multicloud connector - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/multicloud-connector/multicloud-extended-security-updates
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
description: Learn how to use the Windows Server ESU solution of the multicloud connector enabled by Azure Arc to attach an ESU license to eligible Arc-enabled Windows Server machines in AWS and GCP.
ms.topic: how-to
ms.date: 2026-11-09T00:00:00.0000000Z
locale: en-us
document_id: ff9d76e3-9b61-02f3-70a2-7e391de042c0
document_version_independent_id: ed382f48-c831-45e0-90e5-285812e1062e
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/multicloud-connector/multicloud-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/multicloud-connector/multicloud-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/multicloud-connector/multicloud-extended-security-updates.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: a49090e9-1d3f-282f-45e3-0c6a07c5ef98
---

# Attach Windows Server Extended Security Updates licenses with the multicloud connector - Azure Arc | Microsoft Learn

The **Windows Server ESU** solution of the multicloud connector attaches an Extended Security Updates (ESU) license to eligible Azure Arc-enabled Windows Server machines. Instead of linking licenses machine by machine, you select a license once on the connector, and eligible machines that the connector onboards from AWS and GCP are covered as they're discovered.

## Prerequisites

In addition to the [general prerequisites for connecting a public cloud](add-public-cloud#prerequisites), meet these requirements.

### Solution dependency

The **AWS Arc EC2 onboarding** or **GCP Arc VM onboarding** solution must be enabled on the same connector. ESU is delivered through the Azure Connected Machine agent, so an AWS EC2 instance or GCP VM must be Arc-enabled before it can receive updates. You can't add **Windows Server ESU** to a connector that doesn't have **AWS Arc EC2 onboarding** or **GCP Arc VM onboarding**.

### Cloud permissions

This solution requires no additional AWS or GCP permissions. The default permission is **None**.

### License requirement

You must already have a Windows Server ESU license in Azure that meets all of these conditions:

| Attribute | Required value |
| --- | --- |
| Version | Windows Server 2016 |
| SKU | Standard |
| Core type | Virtual cores (vCore) |
| Activation status | Activated |

The solution attaches an existing license. It doesn't create one. To create a license, see [Deliver Extended Security Updates for Windows Server](../servers/deliver-extended-security-updates).

Note

Standard SKU with virtual cores is required because source-cloud VMs run on third-party hosts. Virtual core licensing requires a minimum of eight virtual cores per VM, and you select Standard even when the guest operating system is Datacenter edition. For details, see [License provisioning guidelines](../servers/license-extended-security-updates).

## Add the solution

1. In the Azure portal, go to **Azure Arc**, and under **Management**, select **Multicloud connectors**.
2. Select your AWS or GCP connector, and then select **Solutions**.
3. In the **Windows Server ESU** row, select **Add**.
4. In **Windows Server ESU settings**, select an existing, activated Standard SKU Windows Server 2016 vCore ESU license from the dropdown.
5. Select **Save**.

If the dropdown is empty, no license in the subscription meets all four conditions in the previous table. Create or activate a qualifying license first.

## Manage core coverage

You're responsible for managing your ESU license and all linked machines so that core counts are provisioned accurately. Insufficient core coverage can result in noncompliance.

Because the connector attaches the license as it onboards eligible machines, license consumption grows as your multicloud estate grows. Plan for this growth:

- Review the number of cores on the license against the number of eligible machines on a regular basis.
- Increase the core count on the license before onboarding a large batch of Windows Server 2016 instances.
- Reduce the core count or deactivate the license as machines are upgraded, migrated, or decommissioned. Billing follows the cores provisioned on an activated license and doesn't adjust on its own.

A single ESU license covers up to 10,000 cores. Split larger estates across multiple licenses.

## Find eligible machines

Use Azure Resource Graph to list eligible Arc-enabled Windows Server 2016 machines onboarded from AWS and GCP, along with their core counts and license assignment states.

```kusto
resources
| where type =~ 'microsoft.hybridcompute/machines'
| where resourceGroup startswith "AWS_" or resourceGroup startswith "GCP_"
| extend osSku = tolower(tostring(properties.osSku)), cores = toint(properties.detectedProperties.coreCount)
| extend licenseAssignmentState = tolower(tostring(properties.licenseProfile.esuProfile.licenseAssignmentState))
| extend esuKeyState = tolower(tostring(properties.licenseProfile.esuProfile.esuKeyState))
| extend esuEligibility = tolower(tostring(properties.licenseProfile.esuProfile.esuEligibility))
| extend agentVersion = tostring(properties.agentVersion)
| extend agentMajor = toint(split(agentVersion, '.')[0]), agentMinor = toint(split(agentVersion, '.')[1])
| where osSku contains '2016' and licenseAssignmentState != 'assigned' and esuKeyState != 'active' and esuEligibility == 'eligible' and (agentMajor > 1 or (agentMajor == 1 and agentMinor >= 62))
| project name, resourceGroup, osSku, cores, status = tostring(properties.status), licenseAssignmentState
```

## Install the updates

Attaching a license makes a machine eligible to receive ESU patches. The machine still needs a patching solution to install them. You can use Azure Update Manager, Windows Server Update Services, Microsoft Update, Microsoft Configuration Manager, or a third-party patch management solution.

To confirm enrollment on a machine, run `azcmagent show` and check that the **Extended Security Updates** section reports a status of **Active**.