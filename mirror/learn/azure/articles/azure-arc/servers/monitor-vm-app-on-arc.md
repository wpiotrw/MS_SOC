---
layout: Conceptual
title: Govern and monitor VM applications on Azure Arc-enabled servers (preview) - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/monitor-vm-app-on-arc
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
description: Learn how to monitor VM Applications on Azure Arc-enabled servers.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-generated
locale: en-us
document_id: f6c724df-c43c-3f54-aab3-62390ada41cf
document_version_independent_id: a13125a9-6bd5-6ecc-4af8-bfe9d2e005da
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/monitor-vm-app-on-arc.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/monitor-vm-app-on-arc
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/monitor-vm-app-on-arc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4a39416b-bebd-367d-a11e-d55391b7321b
---

# Govern and monitor VM applications on Azure Arc-enabled servers (preview) - Azure Arc | Microsoft Learn

Monitor and govern VM applications on Azure Arc-enabled servers to track deployments and assess compliance with your organization's application requirements. This article shows you how to use Azure Resource Graph to view deployment status across your environment and Azure Policy to audit and deploy required applications. You can also review application installation logs to troubleshoot deployment issues.

## Monitor deployed VM applications with Azure Resource Graph

Use Azure Resource Graph to monitor VM application deployments across your Arc-enabled servers. The following query provides an environment-wide view of deployed applications, including their provisioning state and package reference.

```kusto
resources
| where type =~ "microsoft.hybridcompute/machines/applications"
| project tenantId, subscriptionId, resourceGroup, location,
    machineName = tostring(split(id, "/")[8]),
    applicationName = name,
    provisioningState = tostring(properties.provisioningState),
    packageReferenceId = tostring(properties.packageReferenceId),
    id
```

## Govern required VM applications with Azure Policy

Use three Azure Policy effects to govern VM applications on Arc-enabled servers:

- `AuditIfNotExists`: Report servers that are missing a required application without changing resources.
- `DeployIfNotExists` (DINE): Deploy a required application to servers that don't have it.
- `Modify`: Enforce the version, install order, and failure-handling settings of an existing application. This effect doesn't deploy missing applications.

### Prerequisites and remediation

For DINE and Modify:

- Meet the [VM application deployment prerequisites](deploy-vm-app-on-arc#prerequisites), including agent version, network access, and gallery replication requirements.
- Configure a managed identity on the policy assignment's **Remediation** tab.
- Grant the identity the [Azure Connected Machine Resource Administrator](/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#azure-connected-machine-resource-administrator) role at the deployment or remediation scope and the **Reader** role on both the gallery and its resource group.

DINE deploys missing applications after successful server creation or update requests. Modify changes matching application settings during application resource creation or update. Compliance evaluation alone doesn't change existing resources. For either effect, create a [remediation task](/en-us/azure/governance/policy/how-to/remediate-resources) to correct existing noncompliant resources.

### Define and assign a policy

Select an effect for its policy definition and assignment steps.

# [AuditIfNotExists](#tab/audit-if-not-exists)
#### Create a custom policy definition

```json
{
  "properties": {
    "displayName": "Audit Azure Arc-enabled servers that do not have a VM application installed",
    "policyType": "Custom",
    "mode": "Indexed",
    "description": "Audits Azure Arc-enabled servers that match the target operating system and do not have the specified VM application installed.",
    "metadata": {
      "category": "Azure Arc",
      "version": "1.0.0"
    },
    "parameters": {
      "effect": {
        "type": "String",
        "metadata": {
          "displayName": "Effect",
          "description": "Enable or disable the execution of the policy."
        },
        "allowedValues": [
          "AuditIfNotExists",
          "Disabled"
        ],
        "defaultValue": "AuditIfNotExists"
      },
      "applicationName": {
        "type": "String",
        "metadata": {
          "displayName": "Application name",
          "description": "The name of the VM application to check for on Azure Arc-enabled servers."
        }
      },
      "osType": {
        "type": "String",
        "metadata": {
          "displayName": "Operating system type",
          "description": "The target operating system. Only Azure Arc-enabled servers with a matching operating system are audited."
        },
        "allowedValues": [
          "Windows",
          "Linux"
        ]
      }
    },
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.HybridCompute/machines"
          },
          {
            "field": "Microsoft.HybridCompute/machines/osName",
            "equals": "[parameters('osType')]"
          }
        ]
      },
      "then": {
        "effect": "[parameters('effect')]",
        "details": {
          "type": "Microsoft.HybridCompute/machines/applications",
          "existenceCondition": {
            "field": "name",
            "equals": "[parameters('applicationName')]"
          }
        }
      }
    }
  }
}
```

#### Assign the policy

Assign the custom policy to the scope you want to monitor, such as a subscription or resource group.

1. Set `applicationName` to the name of the required VM application.
2. Set `osType` to `Windows` or `Linux`, depending on the application's target operating system.
3. Set `effect` to `AuditIfNotExists` to report missing applications.

Create a separate assignment for each required application and target operating system. By using `AuditIfNotExists`, matching servers are noncompliant if the named application resource is missing.

# [DeployIfNotExists](#tab/deploy-if-not-exists)
#### Create a custom policy definition

```json
{
  "properties": {
    "displayName": "Deploy a VM application to Azure Arc-enabled servers",
    "policyType": "Custom",
    "mode": "Indexed",
    "description": "Deploys the specified VM application from an Azure Compute Gallery to Azure Arc-enabled servers that match the target operating system, if the application is not already installed.",
    "metadata": {
      "category": "Azure Arc",
      "version": "1.0.0"
    },
    "parameters": {
      "effect": {
        "type": "String",
        "metadata": {
          "displayName": "Effect",
          "description": "Enable or disable the execution of the policy."
        },
        "allowedValues": [
          "DeployIfNotExists",
          "Disabled"
        ],
        "defaultValue": "DeployIfNotExists"
      },
      "subscriptionId": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery subscription ID",
          "description": "The ID of the subscription that contains the Azure Compute Gallery."
        }
      },
      "resourceGroup": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery resource group",
          "description": "The name of the resource group that contains the Azure Compute Gallery."
        }
      },
      "galleryName": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery name",
          "description": "The name of the Azure Compute Gallery."
        }
      },
      "applicationName": {
        "type": "String",
        "metadata": {
          "displayName": "Application name",
          "description": "The name of the VM application definition in the gallery."
        }
      },
      "applicationVersion": {
        "type": "String",
        "metadata": {
          "displayName": "Application version",
          "description": "The version of the VM application to deploy. Use 'latest' to deploy the most recent version."
        },
        "defaultValue": "latest"
      },
      "osType": {
        "type": "String",
        "metadata": {
          "displayName": "Operating system type",
          "description": "The target operating system. The application is deployed only to Azure Arc-enabled servers with a matching operating system."
        },
        "allowedValues": [
          "Windows",
          "Linux"
        ]
      }
    },
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.HybridCompute/machines"
          },
          {
            "field": "Microsoft.HybridCompute/machines/osName",
            "equals": "[parameters('osType')]"
          }
        ]
      },
      "then": {
        "effect": "[parameters('effect')]",
        "details": {
          "type": "Microsoft.HybridCompute/machines/applications",
          "roleDefinitionIds": [
            "/providers/Microsoft.Authorization/roleDefinitions/cd570a14-e51a-42ad-bac8-bafd67325302"
          ],
          "existenceCondition": {
            "field": "Microsoft.HybridCompute/machines/applications/packageReferenceId",
            "contains": "[concat('/galleries/', parameters('galleryName'), '/applications/', parameters('applicationName'), '/')]"
          },
          "deployment": {
            "properties": {
              "mode": "incremental",
              "parameters": {
                "machineName": {
                  "value": "[field('name')]"
                },
                "location": {
                  "value": "[field('location')]"
                },
                "applicationName": {
                  "value": "[parameters('applicationName')]"
                },
                "packageReferenceId": {
                  "value": "[concat('/subscriptions/', parameters('subscriptionId'), '/resourceGroups/', parameters('resourceGroup'), '/providers/Microsoft.Compute/galleries/', parameters('galleryName'), '/applications/', parameters('applicationName'), '/versions/', parameters('applicationVersion'))]"
                }
              },
              "template": {
                "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
                "contentVersion": "1.0.0.0",
                "parameters": {
                  "machineName": {
                    "type": "string"
                  },
                  "location": {
                    "type": "string"
                  },
                  "applicationName": {
                    "type": "string"
                  },
                  "packageReferenceId": {
                    "type": "string"
                  }
                },
                "resources": [
                  {
                    "type": "Microsoft.HybridCompute/machines/applications",
                    "apiVersion": "2026-09-01",
                    "name": "[concat(parameters('machineName'), '/', parameters('applicationName'))]",
                    "location": "[parameters('location')]",
                    "properties": {
                      "packageReferenceId": "[parameters('packageReferenceId')]",
                      "order": 1,
                      "treatFailureAsDeploymentFailure": true
                    }
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
}
```

#### Assign the policy

Assign the custom policy to the subscription or resource group that contains the Arc-enabled servers where you want to deploy the application.

1. Set `subscriptionId`, `resourceGroup`, and `galleryName` to identify the Azure Compute Gallery that contains the application.
2. Set `applicationName` to the gallery application definition name.
3. Set `applicationVersion` to a specific version or leave the default value of `latest`.
4. Set `osType` to `Windows` or `Linux`, matching the application's target operating system.
5. Set `effect` to `DeployIfNotExists` to deploy missing applications.

Create a separate assignment for each required application and target operating system.

# [Modify](#tab/modify)
#### Create a custom policy definition

```json
{
  "properties": {
    "displayName": "Configure VM application settings on Azure Arc-enabled servers",
    "policyType": "Custom",
    "mode": "Indexed",
    "description": "Enforces the version, install order, and failure-handling settings of the specified VM application on Azure Arc-enabled servers. If a deployed application does not match these settings, the policy updates it.",
    "metadata": {
      "category": "Azure Arc",
      "version": "1.0.0"
    },
    "parameters": {
      "effect": {
        "type": "String",
        "metadata": {
          "displayName": "Effect",
          "description": "Enable or disable the execution of the policy."
        },
        "allowedValues": [
          "Modify",
          "Disabled"
        ],
        "defaultValue": "Modify"
      },
      "subscriptionId": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery subscription ID",
          "description": "The ID of the subscription that contains the Azure Compute Gallery."
        }
      },
      "resourceGroup": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery resource group",
          "description": "The name of the resource group that contains the Azure Compute Gallery."
        }
      },
      "galleryName": {
        "type": "String",
        "metadata": {
          "displayName": "Gallery name",
          "description": "The name of the Azure Compute Gallery."
        }
      },
      "applicationName": {
        "type": "String",
        "metadata": {
          "displayName": "Application name",
          "description": "The name of the VM application definition in the gallery."
        }
      },
      "applicationVersion": {
        "type": "String",
        "metadata": {
          "displayName": "Application version",
          "description": "The version of the VM application to enforce. Use a specific version, such as 1.0.1, or use 'latest' to enforce the most recent version."
        },
        "defaultValue": "latest"
      },
      "order": {
        "type": "Integer",
        "metadata": {
          "displayName": "Install order",
          "description": "The install order to enforce for the VM application."
        },
        "defaultValue": 1
      },
      "treatFailureAsDeploymentFailure": {
        "type": "Boolean",
        "metadata": {
          "displayName": "Treat failure as deployment failure",
          "description": "Specifies whether an application install failure is reported as a deployment failure."
        },
        "defaultValue": true
      }
    },
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.HybridCompute/machines/applications"
          },
          {
            "field": "Microsoft.HybridCompute/machines/applications/packageReferenceId",
            "contains": "[concat('/galleries/', parameters('galleryName'), '/applications/', parameters('applicationName'), '/')]"
          },
          {
            "anyOf": [
              {
                "field": "Microsoft.HybridCompute/machines/applications/packageReferenceId",
                "notEquals": "[concat('/subscriptions/', parameters('subscriptionId'), '/resourceGroups/', parameters('resourceGroup'), '/providers/Microsoft.Compute/galleries/', parameters('galleryName'), '/applications/', parameters('applicationName'), '/versions/', parameters('applicationVersion'))]"
              },
              {
                "field": "Microsoft.HybridCompute/machines/applications/order",
                "notEquals": "[parameters('order')]"
              },
              {
                "field": "Microsoft.HybridCompute/machines/applications/treatFailureAsDeploymentFailure",
                "notEquals": "[parameters('treatFailureAsDeploymentFailure')]"
              }
            ]
          }
        ]
      },
      "then": {
        "effect": "[parameters('effect')]",
        "details": {
          "roleDefinitionIds": [
            "/providers/Microsoft.Authorization/roleDefinitions/cd570a14-e51a-42ad-bac8-bafd67325302"
          ],
          "operations": [
            {
              "operation": "addOrReplace",
              "field": "Microsoft.HybridCompute/machines/applications/packageReferenceId",
              "value": "[concat('/subscriptions/', parameters('subscriptionId'), '/resourceGroups/', parameters('resourceGroup'), '/providers/Microsoft.Compute/galleries/', parameters('galleryName'), '/applications/', parameters('applicationName'), '/versions/', parameters('applicationVersion'))]"
            },
            {
              "operation": "addOrReplace",
              "field": "Microsoft.HybridCompute/machines/applications/order",
              "value": "[parameters('order')]"
            },
            {
              "operation": "addOrReplace",
              "field": "Microsoft.HybridCompute/machines/applications/treatFailureAsDeploymentFailure",
              "value": "[parameters('treatFailureAsDeploymentFailure')]"
            }
          ]
        }
      }
    }
  }
}
```

#### Assign the policy

Assign the custom policy to the subscription or resource group that contains the Arc-enabled servers whose application settings you want to enforce.

1. Set `subscriptionId`, `resourceGroup`, and `galleryName` to identify the Azure Compute Gallery.
2. Set `applicationName` to the gallery application definition name.
3. Set `applicationVersion` to the version to enforce, or leave the default value of `latest`.
4. Set `order` to the required install order.
5. Set `treatFailureAsDeploymentFailure` to `true` to report application installation failures as deployment failures, or `false` to disable this behavior.
6. Set `effect` to `Modify` to enforce the settings.

---

## Access VM application logs

Use installation logs to troubleshoot application installation issues, and use the Azure Activity log to review control-plane operations on VM application resources.

### Use Run command to review installation logs

Use Run command to read the installation logs on an Arc-enabled server. For instructions on creating and executing a Run command, see [Run command on Azure Arc-enabled servers (preview)](run-command).

Run the following script for your server's operating system. Replace `vm-application-name` with the VM application definition name and `1.0.0` with the application version.

#### Windows

Set `$extensionVersion` to the version of the VM Application Manager extension installed on the server. The following example uses `1.0.17`.

```powershell
$appName = "vm-application-name"
$appVersion = "1.0.0"
$extensionVersion = "1.0.17"
$logDirectory = "C:\Packages\Plugins\Microsoft.CPlat.Core.VMApplicationManagerWindows\$extensionVersion\Downloads\$appName\$appVersion"
$stdoutFilePath = Join-Path $logDirectory "stdout"
$stderrFilePath = Join-Path $logDirectory "stderr"

Write-Output "`n=== Contents of stdout ==="
Get-Content -Path $stdoutFilePath -ErrorAction Stop
Write-Output "`n=== Contents of stderr ==="
Get-Content -Path $stderrFilePath -ErrorAction Stop
```

#### Linux

Run the following Bash script to view standard output and standard error.

```bash
set -e

appName="vm-application-name"
appVersion="1.0.0"
logDirectory="/var/lib/waagent/Microsoft.CPlat.Core.VMApplicationManagerLinux/$appName/$appVersion"
stdoutFilePath="$logDirectory/stdout"
stderrFilePath="$logDirectory/stderr"

printf '\n=== Contents of stdout ===\n'
cat "$stdoutFilePath"
printf '\n=== Contents of stderr ===\n'
cat "$stderrFilePath"
```

### Use the Activity log to review resource operations

The Azure Activity log records control-plane operations on VM application resources, such as creating, updating, or deleting a deployment. These records are separate from the installation logs on the server.

1. In the Azure portal, go to the Arc-enabled server where the VM application is deployed.
2. Select **Activity log**.
3. Adjust the time range and filters to find the operation you want to review.
4. Select an event to view its details, and then select **JSON** for the full event record.

Use the following operation names to identify VM application events:

- Deployment creation or updates: `Microsoft.HybridCompute/machines/applications/write`.
- Deployment deletions: `Microsoft.HybridCompute/machines/applications/delete`.

### Collect full Azure Arc agent logs

To collect all available Azure Connected Machine agent and extension logs, rather than only the most recent logs, run the following command on the Arc-enabled server:

```console
azcmagent logs -f
```

The command saves the logs in a ZIP archive in the current directory. For more information, see [azcmagent logs](azcmagent-logs).