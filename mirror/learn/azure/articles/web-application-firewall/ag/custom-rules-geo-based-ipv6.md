---
layout: Conceptual
title: IPv6 Geo-Based Custom Rules (Preview) - Azure Web Application Firewall | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/custom-rules-geo-based-ipv6
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/192/azure-web-application-firewall/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: halkazwini
learn_banner_products:
- azure
manager: kumud
ms.reviewer: halkazwini
description: Learn about IPv6 geo-based custom rules in Application Gateway WAF, including preview feature registration, dual-stack requirements, and validation behavior.
ms.author: halkazwini
ms.service: azure-web-application-firewall
ms.topic: concept-article
ms.date: 2026-09-17T00:00:00.0000000Z
locale: en-us
document_id: 90466417-ee89-5bd7-ca71-31811ca1c5c0
document_version_independent_id: dc8733eb-7e10-652f-299c-06ae1b581c7b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/web-application-firewall/ag/custom-rules-geo-based-ipv6.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
interactive_type: azurepowershell,azurecli
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: web-application-firewall/ag/custom-rules-geo-based-ipv6
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/web-application-firewall/ag/custom-rules-geo-based-ipv6.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e8fdebed-2921-4997-a75a-fa863723a535
- https://authoring-docs-microsoft.poolparty.biz/devrel/d4cf20b3-3e54-4ed9-8b09-370a52eee81b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf1e63a8-325f-42be-b60c-d84a95a42b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/9ecc2643-be13-4271-a1f4-87114737d63a
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: c4d857cc-034f-d97e-8d28-d70e35b70952
---

# IPv6 Geo-Based Custom Rules (Preview) - Azure Web Application Firewall | Microsoft Learn

**Applies to:** ✔️ Application Gateway v2

Important

The IPv6 geo-based custom rules feature for Azure Application Gateway Web Application Firewall (WAF) is currently in preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

[Geomatch custom rules](geomatch-custom-rules) let you restrict access to your web applications by country or region. The IPv6 geo-based custom rules feature for Azure Application Gateway WAF extends this protection to IPv6 traffic.

To use this feature, register `AllowAppGwWafIpv6Geo` in your Azure subscription. For more information, see [Set up preview features in Azure subscription](../../azure-resource-manager/management/preview-features).

## When feature registration is required

Register the `AllowAppGwWafIpv6Geo` feature **only** in the following scenario:

- You want to create or use geo-based custom rules that apply to IPv6 traffic in Application Gateway WAF.

You don't need to register the feature for:

- IPv6 inspection using managed rule sets
- Non-geo custom rules for IPv6, such as rules based on IPv6 addresses or ranges
- Logging, diagnostics, and monitoring of IPv6 traffic

## Requirements

To use IPv6 geo-based custom rules:

- The Application Gateway must support IPv6 and be deployed in a dual-stack configuration.
- Both public and private IP configurations must be dual-stack.
- To evaluate IPv6 traffic by using geo-based custom rules, you must associate the WAF policy with at least one IPv6-capable, dual-stack Application Gateway.

## Workflow for enabling IPv6 geo-based custom rules

To evaluate IPv6 traffic by using geo-based custom rules, complete the following steps:

1. Register the `AllowAppGwWafIpv6Geo` feature in your Azure subscription.
2. Deploy or update your Application Gateway to a dual-stack configuration that supports IPv6. You can't update or convert an existing IPv4-only Application Gateway to dual-stack. For more information, see [Configure Application Gateway with a frontend public IPv6 address](../../application-gateway/ipv6-application-gateway-portal).

    Note

    IPv6-only Application Gateways aren't supported.
3. Create or update a WAF policy with geo-based custom rules for IPv6 traffic. For more information, see [Geomatch custom rules](geomatch-custom-rules).
4. Associate the WAF policy with the IPv6-capable Application Gateway. For more information, see [Associate a WAF policy with an existing Application Gateway](associate-waf-policy-existing-gateway).
5. Validate enforcement by using WAF logs and diagnostics. For more information, see [Resource logs for Azure Web Application Firewall](web-application-firewall-logs).

## Enforcement behavior and validation

To prevent unsupported configurations, the platform blocks the following actions:

- **Associating a policy:** You **can't associate** a WAF policy that contains geo-based custom rules for IPv6 traffic with an incompatible dual-stack Application Gateway that doesn't support IPv6 geo evaluation.
- **Creating a rule:** You **can't create** geo-based custom rules in a WAF policy that is already associated with a dual-stack Application Gateway that doesn't support IPv6.

Note

IPv4-only Application Gateways aren't affected by this validation. Validation applies only when you associate dual-stack Application Gateways that participate in IPv6 traffic evaluation.

These checks remain in effect after you register the feature, which ensures predictable behavior during the preview.

## Register the feature

The following table lists the details you need to register the feature:

| Property | Value |
| --- | --- |
| Feature name | `AllowAppGwWafIpv6Geo` |
| Display name | Enable IPv6 Geo Custom Rules for WAF |
| Provider namespace | `Microsoft.Network` |
| Description | Enables geo-based custom rules with IPv6 traffic in Application Gateway WAF |

# [Portal](#tab/portal)
To register the feature, follow these steps:

1. In the search box at the top of the [Azure portal](https://portal.azure.com), enter *subscriptions* and select **Subscriptions**.
2. Select your subscription.
3. Under **Settings**, select **Preview features** to see a list of all available features and the current registration status.
4. On the **Preview features** page, use the search box to search for *AllowAppGwWafIpv6Geo*.
5. Select the feature and then select **Register**.

    ![Screenshot of the Preview features page in the Azure portal, showing the Enable IPv6 Geo Custom Rules for WAF feature selected and the Register button highlighted.](../media/custom-rules-geo-based-ipv6/preview-features-register.png)
6. In the confirmation message, select **OK** to register the feature in your subscription.

# [PowerShell](#tab/powershell)
Use the [Register-AzProviderFeature](/en-us/powershell/module/az.resources/register-azproviderfeature) cmdlet to register the feature.

```azurepowershell
Register-AzProviderFeature -FeatureName "AllowAppGwWafIpv6Geo" -ProviderNamespace "Microsoft.Network"
```

Use the [Get-AzProviderFeature](/en-us/powershell/module/az.resources/get-azproviderfeature) cmdlet to view the registration status of the feature.

```azurepowershell
Get-AzProviderFeature -FeatureName "AllowAppGwWafIpv6Geo" -ProviderNamespace "Microsoft.Network"
```

```
FeatureName          ProviderName      RegistrationState
-----------          ------------      -----------------
AllowAppGwWafIpv6Geo Microsoft.Network Registered
```

# [Azure CLI](#tab/cli)
Use the [az feature register](/en-us/cli/azure/feature#az-feature-register) command to register for the feature.

```azurecli
az feature register --name AllowAppGwWafIpv6Geo --namespace Microsoft.Network
```

Use the [az feature registration show](/en-us/cli/azure/feature/registration#az-feature-registration-show) command to view the registration status of the feature.

```azurecli
az feature registration show --name AllowAppGwWafIpv6Geo --provider-namespace Microsoft.Network --output table
```

```
Name                                    RegistrationState
--------------------------------------  -----------------
Microsoft.Network/AllowAppGwWafIpv6Geo   Registered
```

---

## Unregister the feature

# [Portal](#tab/portal)
To unregister the feature, follow these steps:

1. In the search box at the top of the [Azure portal](https://portal.azure.com), enter *subscriptions* and select **Subscriptions**.
2. Select your subscription.
3. Under **Settings**, select **Preview features** to see a list of all available features and the current registration status.
4. On the **Preview features** page, use the search box to search for *AllowAppGwWafIpv6Geo*.
5. Select the feature and then select **Unregister**.

    ![Screenshot of the Preview features page in the Azure portal, showing the registered Enable IPv6 Geo Custom Rules for WAF feature and the Unregister button highlighted.](../media/custom-rules-geo-based-ipv6/preview-features-unregister.png)
6. In the confirmation message, select **OK** to unregister the feature from your subscription.

# [PowerShell](#tab/powershell)
Use the [Unregister-AzProviderFeature](/en-us/powershell/module/az.resources/unregister-azproviderfeature) cmdlet to unregister from the feature.

```azurepowershell
Unregister-AzProviderFeature -FeatureName "AllowAppGwWafIpv6Geo" -ProviderNamespace "Microsoft.Network"
```

Use the [Get-AzProviderFeature](/en-us/powershell/module/az.resources/get-azproviderfeature) cmdlet to view the registration status of the feature.

```azurepowershell
Get-AzProviderFeature -FeatureName "AllowAppGwWafIpv6Geo" -ProviderNamespace "Microsoft.Network"
```

```
FeatureName          ProviderName      RegistrationState
-----------          ------------      -----------------
AllowAppGwWafIpv6Geo Microsoft.Network Unregistered
```

# [Azure CLI](#tab/cli)
Use the [az feature unregister](/en-us/cli/azure/feature#az-feature-unregister) command to unregister the feature.

```azurecli
az feature unregister --name AllowAppGwWafIpv6Geo --namespace Microsoft.Network
```

Use the [az feature registration show](/en-us/cli/azure/feature/registration#az-feature-registration-show) command to view the registration status of the feature.

```azurecli
az feature registration show --name AllowAppGwWafIpv6Geo --provider-namespace Microsoft.Network --output table
```

```
Name                                    RegistrationState
--------------------------------------  -----------------
Microsoft.Network/AllowAppGwWafIpv6Geo   Unregistered
```

---