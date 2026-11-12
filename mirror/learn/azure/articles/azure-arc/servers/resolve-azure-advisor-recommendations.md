---
layout: Conceptual
title: Resolve Azure Advisor recommendations for Azure Arc-enabled servers - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/resolve-azure-advisor-recommendations
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
description: Learn how to resolve Azure Advisor reliability recommendations for disconnected and expired Azure Arc-enabled servers.
ms.date: 2026-11-09T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-assisted
locale: en-us
document_id: 45fc7827-4a14-9ccf-a48b-c26f1beceb80
document_version_independent_id: 24ccb3e5-0cca-eca1-95d8-a8bb9b3e16c5
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/resolve-azure-advisor-recommendations.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/resolve-azure-advisor-recommendations
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/resolve-azure-advisor-recommendations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/d9dfd2a0-aa13-46ef-a37d-ed697b490607
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/06404839-4766-4799-8cab-c0e1c3b55e48
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 5e5f6631-4623-2128-709d-250db75fa30e
---

# Resolve Azure Advisor recommendations for Azure Arc-enabled servers - Azure Arc | Microsoft Learn

Azure Advisor analyzes Azure Arc-enabled servers and recommends actions that can improve their reliability. Use this article to understand and resolve recommendations for disconnected or expired servers.

The following Azure Advisor recommendations are available for Azure Arc-enabled servers:

| Recommendation | Severity | Condition |
| --- | --- | --- |
| Restore connectivity for 30+ day disconnected Arc-enabled server | Medium | The server is disconnected for 30 through 44 days. |
| Reconnect Arc-enabled server before the managed identity certificate expires | High | The server is disconnected for at least 45 days and the certificate is still valid. |
| Re-onboard expired Arc-enabled server | High | The server's status is **Expired**, or its managed identity certificate is expired. |

## Restore connectivity for 30+ day disconnected Arc-enabled server

Azure shows this recommendation when a server remains disconnected for 30 through 44 days. Azure didn't receive a heartbeat from the server for an extended period. If you don't restore connectivity, the server's managed identity credential might expire, and Azure management capabilities might stop working.

To restore connectivity:

1. Sign in to the server.
2. Run the following command to [check the agent status and dependent services](azcmagent-show):

    ```console
    azcmagent show
    ```
3. Confirm that the agent services are running. If a service isn't running, start or restart it, and then run `azcmagent show` again.
4. Run the following command to [test connectivity to the required Azure Arc endpoints](azcmagent-check):

    ```console
    azcmagent check
    ```
5. Resolve any failed connectivity checks. Review the [network requirements](network-requirements) and, if the server uses a proxy, [verify the agent proxy configuration](manage-agent-proxy-settings).
6. If the problem continues, run the following command to [collect the full agent log bundle](azcmagent-logs):

    ```console
    azcmagent logs --full
    ```

    Use the logs to investigate the failure. For help with common errors, see [Troubleshoot Azure Connected Machine agent connection problems](troubleshoot-agent-onboard#agent-connection-issues-to-service).
7. In the Azure portal, confirm that the server's status returns to **Connected**.

To receive an alert when a server becomes disconnected, [create a Resource Health alert](troubleshoot-connectivity#disconnected-server-alerts).

## Reconnect Arc-enabled server before the managed identity certificate expires

Azure shows this recommendation when the server is disconnected for at least 45 days but the certificate is still valid.

Restore connectivity immediately so that the agent can renew its managed identity credential and avoid expiration. The certificate is valid for 90 days, and the agent attempts to renew it when 45 or fewer days of validity remain. For more information, see [Managed identity security overview](security-identity-authorization#microsoft-entra-id-managed-identity).

To reconnect the server before the certificate expires:

1. Sign in to the server.
2. Run the following command to [check the agent status and dependent services](azcmagent-show):

    ```console
    azcmagent show
    ```
3. Confirm that the agent services are running. If a service isn't running, start or restart it, and then run `azcmagent show` again.
4. Run the following command to [test connectivity to the required Azure Arc endpoints](azcmagent-check):

    ```console
    azcmagent check
    ```
5. Resolve any failed connectivity checks. Review the [network requirements](network-requirements) and, if the server uses a proxy, [verify the agent proxy configuration](manage-agent-proxy-settings).
6. If the problem continues, run the following command to [collect the full agent log bundle](azcmagent-logs):

    ```console
    azcmagent logs --full
    ```

    Use the logs to investigate the failure. For help with common errors, see [Troubleshoot Azure Connected Machine agent connection problems](troubleshoot-agent-onboard#agent-connection-issues-to-service).
7. In the Azure portal, confirm that the server's status returns to **Connected**.

## Re-onboard expired Arc-enabled server

Azure shows this recommendation when the server's status is **Expired** or its managed identity certificate has expired. An expired credential can't renew automatically, and Azure Arc management capabilities are unavailable until you recover the connection.

First, confirm whether the server should remain managed by Azure Arc.

- If the server should remain Arc-enabled and uses agent version 1.70 or later, use [`azcmagent reconnect`](azcmagent-reconnect) (preview) to recover its connection to the existing resource.
- For earlier agent versions, [disconnect the agent and reconnect the server by using an onboarding credential](security-identity-authorization#microsoft-entra-id-managed-identity). To generate and run a new onboarding script, see [Connect hybrid machines to Azure using a deployment script](onboard-portal).
- If the server is retired, [remove its stale Azure resource](uninstall-agent#remove-stale-server-resources). If you still have access to the server, [remove VM extensions, disconnect the server, and uninstall the agent](uninstall-agent).

After re-onboarding a server, confirm in the Azure portal that its status is **Connected**.