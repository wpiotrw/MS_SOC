---
layout: Conceptual
title: Automatically upgrade the Azure Connected Machine agent - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/automatic-agent-upgrade
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
ms.subservice: servers-azure-arc
description: Learn how to manage automatic upgrades for the Azure Connected Machine agent on Azure Arc-enabled servers.
ms.date: 2026-10-16T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-assisted
locale: en-us
document_id: 1f21a3b3-0963-1585-269d-1be7c75e54e6
document_version_independent_id: 9400128b-78af-b658-249b-ff974283a62c
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/automatic-agent-upgrade.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/automatic-agent-upgrade
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/automatic-agent-upgrade.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: ebfe9924-53e1-1bc1-cd0e-c234b19467fb
---

# Automatically upgrade the Azure Connected Machine agent - Azure Arc | Microsoft Learn

The Azure Connected Machine agent is updated regularly with bug fixes, stability improvements, and new functionality. Automatic agent upgrade helps keep Azure Arc-enabled servers up to date without requiring you to manually deploy each new agent version.

When you enable automatic agent upgrade, Microsoft automatically manages updates to the Azure Connected Machine agent. Machines are scheduled to upgrade to the latest agent version. Upgrades roll out in batches across regions and initiate during off-peak hours to help maintain stability and minimize disruption. If an upgrade doesn't complete successfully, the agent periodically retries the upgrade until it succeeds.

Installing or upgrading the Azure Connected Machine agent doesn't require a server restart. This feature is currently available only on Azure public cloud.

## Prerequisites

Before enabling automatic agent upgrade, ensure your machines meet the following requirements:

- **All Arc-enabled servers:** Azure Connected Machine agent version 1.67 or later is required.
- **Windows:** Set the PowerShell execution policy to RemoteSigned. Automatic agent upgrade isn't supported when the execution policy is set to Restricted.
- **Linux:** Ensure the cron service is installed and running. This service is required to schedule and perform automatic agent upgrades.

Important

If enabled on an agent version earlier than 1.67, use [one of the other methods](manage-agent#additional-agent-upgrade-methods) to upgrade the agent to a compatible version. Automatic Agent Upgrade can then manage all future upgrades.

## Enable automatic agent upgrade

You can enable automatic agent upgrade when connecting a new machine to Azure Arc or enable it later for an existing Arc-enabled server.

To enable automatic agent upgrade when connecting the machine, include the `--enable-automatic-upgrade` parameter with `azcmagent connect`.

```bash
azcmagent connect \
--subscription-id "<SUBSCRIPTION_ID>" \
--resource-group "<RESOURCE_GROUP>" \
--location "<LOCATION>" \
--enable-automatic-upgrade
```

Alternatively, enable automatic agent upgrade during the machine onboarding process in the Azure portal by following these steps:

1. In the [Azure portal](https://portal.azure.com/), search for and select **Azure Arc**.
2. In the service menu, expand **Infrastructure**, and then select **Machines**.
3. Select **Onboard/Create**, and then select **Onboard existing machines**.
4. On the **Basics** tab, enter the required details for your server.
5. Under **Automatic agent upgrade**, select **Automatically keep the Azure Connected Machine agent up to date**.
6. Complete the remaining onboarding steps, then download and run the generated script on your server.

### Enable automatic upgrade on an existing server

For an existing Arc-enabled server, enable automatic agent upgrade by setting the `enableAutomaticUpgrade` property to `true`. You can configure this property in multiple ways.

# [Azure portal](#tab/azure-portal)
1. In the Azure portal, go to your Arc-enabled server.
2. Select **Properties**.

    [![Screenshot of the Properties navigation option for an Azure Arc-enabled server.](media/automatic-agent-upgrade/server-properties.png)](media/automatic-agent-upgrade/server-properties.png#lightbox)
3. Under **Agent status**, select the current **Agent auto upgrade** status, such as **Not enabled**.

    ![Screenshot of the Agent auto upgrade status showing Not enabled.](media/automatic-agent-upgrade/automatic-upgrade-not-enabled.png)
4. Select **Enable automatic upgrades for the Arc connected machine agent**, and then select **Enable**.

    ![Screenshot of the option to enable automatic upgrades for the Azure Connected Machine agent.](media/automatic-agent-upgrade/enable-automatic-upgrade.png)

# [Azure CLI](#tab/azure-cli)
Set the target subscription:

```azurecli
az account set --subscription "<SUBSCRIPTION_ID>"
```

Enable automatic agent upgrade:

```azurecli
az rest \
--method PATCH \
--url "https://management.azure.com/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.HybridCompute/machines/<MACHINE_NAME>?api-version=2024-05-20-preview" \
--headers "Content-Type=application/json" \
--body '{"properties":{"agentUpgrade":{"enableAutomaticUpgrade":true}}}'
```

# [PowerShell](#tab/powershell)
Set the target subscription:

```azurepowershell
Set-AzContext -Subscription "<SUBSCRIPTION_ID>"
```

Enable automatic agent upgrade:

```azurepowershell
$params = @{
    ResourceGroupName     = "<RESOURCE_GROUP>"
    ResourceProviderName  = "Microsoft.HybridCompute"
    ResourceType          = "Machines"
    ApiVersion            = "2024-05-20-preview"
    Name                  = "<MACHINE_NAME>"
    Method                = "PATCH"
    Payload               = '{"properties":{"agentUpgrade":{"enableAutomaticUpgrade":true}}}'
}
Invoke-AzRestMethod @params
```

# [Azure Policy](#tab/azure-policy)
Use [Azure Policy](/en-us/azure/governance/policy/overview) to enable automatic agent upgrade across multiple Azure Arc-enabled servers.

Assign the [Configure Azure Arc-enabled Servers to enable automatic upgrades](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailAdaptor.ReactView/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2Ff9dfba6f-7430-4214-a666-342b3d3d0d62) policy to the appropriate scope. The policy enables automatic agent upgrade on Azure Arc-enabled servers covered by the assignment.

This method is particularly useful when you want to apply the automatic upgrade configuration consistently across your environment at scale.

---

## Verify automatic agent upgrade status

After you enable automatic agent upgrade, verify the current setting on the Arc-enabled server resource.

# [Azure portal](#tab/azure-portal-verify)
1. In the Azure portal, navigate to your Arc-enabled server.
2. Select **Properties**.

    [![Screenshot of the server Properties navigation option used to verify automatic agent upgrade.](media/automatic-agent-upgrade/server-properties.png)](media/automatic-agent-upgrade/server-properties.png#lightbox)
3. Under **Agent status**, check the current **Agent auto upgrade** status. In this example, the status is **Enabled**.

    ![Screenshot of the Agent auto upgrade status showing Enabled.](media/automatic-agent-upgrade/automatic-upgrade-enabled.png)

# [Azure Resource Graph](#tab/arg-verify)
Run the following query in [Azure Resource Graph Explorer](https://ms.portal.azure.com/#servicemenu/Microsoft_Azure_Resources/ResourceManager/resourcegraphexplorer) to list all Arc-enabled servers with automatic agent upgrade enabled in the selected scope:

```kusto
resources
| where type =~ 'microsoft.hybridcompute/machines'
| where properties.agentUpgrade.enableAutomaticUpgrade == true
| project name, resourceGroup, subscriptionId, location, id
| order by name asc
```

---

## Disable automatic agent upgrade

To opt out of automatic agent upgrade for an existing Azure Arc-enabled server, set the **enableAutomaticUpgrade** property to **false**.

Note

If Azure Policy is assigned to enable automatic upgrades at the machine's scope, update or remove the assignment before disabling the setting. Otherwise, the policy can enable automatic upgrades again.

### Block automatic agent upgrades locally

As an alternative to disabling the **enableAutomaticUpgrade** property on the Azure resource, you can block automatic agent upgrades locally on an individual machine. This option is useful when you want the Azure resource setting to remain enabled but don't want automatic upgrades to run on a specific machine. The **automaticupgrade.blocklocally** setting takes precedence over the **enableAutomaticUpgrade** property. When the local setting is **true**, automatic upgrades are blocked even if **enableAutomaticUpgrade** is set to **true**.

```bash
azcmagent config set automaticupgrade.blocklocally true
```

To verify the local block setting, run:

```bash
azcmagent config get automaticupgrade.blocklocally
```

To use automatic agent upgrades on the machine again, ensure that the local property is set to **false**:

```bash
azcmagent config set automaticupgrade.blocklocally false
```

To modify these settings at scale, it is recommended to use [Run Command](run-command?tabs=azure-powershell).