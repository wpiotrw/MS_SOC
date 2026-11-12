---
layout: Conceptual
title: azcmagent CLI reference - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/azcmagent
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
description: Reference documentation for the Azure Connected Machine agent command line tool
ms.topic: reference
ms.date: 2026-03-02T00:00:00.0000000Z
ms.custom:
- build-2025
locale: en-us
document_id: 78d7f898-b61c-d750-6c1b-875037b4166d
document_version_independent_id: b6591a03-29ae-b92c-50cb-b6c328f9beec
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/azcmagent.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/azcmagent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/azcmagent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4f4fd000-91e0-9a90-d288-9eaace79654a
---

# azcmagent CLI reference - Azure Arc | Microsoft Learn

The Azure Connected Machine agent command line tool, `azcmagent`, helps you configure, manage, and troubleshoot a server's connection with Azure Arc. The `azcmagent` CLI is installed with the Azure Connected Machine agent and controls actions specific to the server where it's running. Once the server is connected to Azure Arc, you can use the [Azure CLI](/en-us/cli/azure/connectedmachine) or [Azure PowerShell](/en-us/powershell/module/az.connectedmachine/) module to enable extensions, manage tags, and perform other operations on the server resource.

Unless otherwise specified, the command syntax and flags represent available options in the most recent release of the Azure Connected Machine agent. For more information, see [What's new with the Azure Connected Machine agent](agent-release-notes).

To get details about the individual commands available in the `azcmagent` CLI, run `azcmagent COMMANDNAME --help` or see the following reference pages:

For sign-in methods and shared authentication flags, see [Authenticate the azcmagent CLI](azcmagent-authentication).

## Commands

| Command | Purpose |
| --- | --- |
| [`azcmagent check`](azcmagent-check) | Run network connectivity checks for Azure Arc endpoints |
| [`azcmagent config`](azcmagent-config) | Manage agent settings. |
| [`azcmagent connect`](azcmagent-connect) | Connect the server to Azure Arc. |
| [`azcmagent disconnect`](azcmagent-disconnect) | Disconnect the server from Azure Arc. |
| [`azcmagent genkey`](azcmagent-genkey) | Generate a public-private key pair for asynchronous onboarding. |
| [`azcmagent help`](azcmagent-help) | Get help for commands. |
| [`azcmagent license`](azcmagent-license) | Display the end-user license agreement. |
| [`azcmagent logs`](azcmagent-logs) | Collect logs to troubleshoot agent issues. |
| [`azcmagent reconnect`](azcmagent-reconnect) | Restore the server's connection to its existing Azure Arc resource (preview). |
| [`azcmagent show`](azcmagent-show) | Display the agent status. |
| [`azmagent upgrade`](azcmagent-upgrade) | Upgrade the agent to the latest version. |
| [`azcmagent version`](azcmagent-version) | Display the agent version. |
| `azcmagent partnerconfig` | Reserved for internal use. |

## Common flags

All `azcmagent` commands support the following flags. To see if a command supports other flags, check its reference page.

`--config`

Takes in a path to a JSON or YAML file containing inputs to the command. The configuration file should contain a series of key-value pairs where the key matches an available command line option. For example, to pass in the `--verbose` flag, the configuration file would look like:

```json
{
    "verbose": true
}
```

If a command line option is found in both the command invocation and a configuration file, the value specified on the command line will take precedence.

`-h`, `--help`

Get help for the current command, including its syntax and command line options.

`-j`, `--json`

Output the command result in the JSON format.

`--log-stderr`

Redirect error and verbose messages to the standard error (stderr) stream. By default, all output is sent to the standard output (stdout) stream.

`--no-color`

Disable color output for terminals that do not support ANSI colors.

`-v`, `--verbose`

Show more detailed logging information while the command executes. Useful for troubleshooting issues when running a command.

## Frequently asked questions

### How can I install the azcmagent CLI?

The `azcmagent` CLI is bundled with the Azure Connected Machine agent. To learn about methods to install and configure the agent, see [Azure Connected Machine agent deployment options](deployment-options).

### Where is the CLI installed?

On Windows operating systems, the CLI is installed at `%PROGRAMFILES%\AzureConnectedMachineAgent\azcmagent.exe`. This path is automatically added to the system PATH variable during the installation process. You may need to close and reopen your console to refresh the PATH variable and be able to run `azcmagent` without specifying the full path.

On Linux operating systems, the CLI is installed at `/opt/azcmagent/bin/azcmagent`.

### What's the difference between the `azcmagent` CLI and the Azure CLI for Azure Arc-enabled servers?

The `azcmagent` CLI is used to configure the local agent. It's responsible for connecting the agent to Azure, disconnecting it, and configuring local settings like proxy URLs and security features.

The Azure CLI and other management experiences are used to interact with the Azure Arc resource in Azure once the agent is connected. These tools help you manage extensions, move the resource to another subscription or resource group, and change certain settings of the Arc server remotely.