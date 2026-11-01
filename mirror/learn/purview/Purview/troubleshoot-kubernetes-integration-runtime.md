---
layout: Conceptual
title: Troubleshoot a Kubernetes supported self-hosted integration runtime | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/troubleshoot-kubernetes-integration-runtime
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains the steps troubleshoot your Kubernetes-supported self-hosted integration runtime.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vamahtani
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-map
ms.custom: devx-track-extended-java
ms.date: 2024-10-08T00:00:00.0000000Z
locale: en-us
document_id: 235d40b9-40c3-eb93-bc39-6ab7058b521e
document_version_independent_id: 235d40b9-40c3-eb93-bc39-6ab7058b521e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/troubleshoot-kubernetes-integration-runtime.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: troubleshoot-kubernetes-integration-runtime
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/troubleshoot-kubernetes-integration-runtime.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: d0ba3a28-cd69-99c9-e3e1-8f2d77eddc0c
---

# Troubleshoot a Kubernetes supported self-hosted integration runtime | Microsoft Learn

This article covers the details for troubleshooting the new self-hosted integration runtime that is Kubernetes-based for Linux.

You can look up any errors you see in the error guide below. To get support and troubleshooting guidance for SHIR issues, you might need to generate a Log Upload ID and [reach out to Microsoft support.](https://azure.microsoft.com/support/create-ticket/)

## Gather Kubernetes self-hosted integration runtime logs

To generate the Log Upload ID for Microsoft Support:

1. Once a scan shows status Failed, navigate to the VM or machine where your [IRCTL](data-map-integration-runtime-kubernetes-irctl) tool is installed.
2. Use the `./irctl log upload`[command.](data-map-integration-runtime-kubernetes-irctl#log-upload)
3. When the logs are uploaded, keep a record of the Log Upload ID that's printed.
4. If the self-hosted integration runtime fails to register, use the guide below to download logs to local and send it to Microsoft support

To collect the self-hosted integration runtime log and scan run log to troubleshoot your SHIR, use the `./irctl log download`[command.](data-map-integration-runtime-kubernetes-irctl#log-download)

For example:

```bash
./irctl log download --destination "C:\Users\user\logs\"
```

Logs are downloaded to the destination path.

Note

The log is reserved for 14 days. Persist it by uploading it to Microsoft or downloading it to your local machine.

## IRCTL connectivity error to Kubernetes

You might get a Kubernetes context configuration from your Kubernetes administrator, and the registration could fail with one of the following error messages:

- `Error: invalid flag context [] .kube/config: no such file or directory`
- `[Warning] Failed to create kube client with context [] with error`

### Cause

When installing a self-hosted integration runtime, a correct Kubernetes config and a stable connectivity is required.

### Resolution

1. Make sure the Kubernetes context file is located in the correct path.
2. Make sure the IRCTL machine can reach the Kubernetes cluster API server.

## IRCTL permission error

When connecting you could see the following error messages:

- `[Error] Failed to list namespaces to get Running SHIR`
- `[Error] Failed to get configmap/ create job/ etc.`

### Cause

When installing a self-hosted integration runtime, sufficient permissions to multiple Kubernetes resources are required.

### Resolution

Regenerate the Kubernetes service-account-token with an Admin Role.

## IRCTL connectivity error to Microsoft Purview service endpoint

When you attempt to register the Kubernetes supported self-hosted integration runtime, the IRCTL create command could return the following errors:

- `[Error] Failed to register SHIR with error: Post “https://[REGION].compute.governance.azure.com/purviewAccounts/[]/integrationruntimes/[]/registerselfhostedintegrationruntime: []”`

### Cause

IRCTL can't connect to service backend. Such issue is usually caused by network settings or firewall.

### Resolution

Review the network topology of the IRCTL host machine. Refer to these sections of the [general integration runtime troubleshooting page](scanning-shir-troubleshooting#self-hosted-ir-connectivity-issues): Firewall, DNSServer, SSL cert trusts, and http proxy.

## Registration key isn't authorized

When you attempt to register the Kubernetes supported self-hosted integration runtime, the IRCTL create command could return the following errors:

- `[Error] failed to register SHIR with error: Request is not authorized.`

### Cause

They had expired or was manually revoked.

### Resolution

Regenerate the key from the integration runtime's page in the Microsoft Purview portal and register again.

## Kubernetes self-hosted IR creation timed out error

When you attempt to register the Kubernetes supported self-hosted integration runtime, the IRCTL create command could run long until it eventually times out.

![Screenshot of the command line after the creation times out.](media/kubernetes-integration-runtime/shir-time-out.png)

You can start with checking the status of Pods under the namespaces mentioned by the `irctl describe` command.

For example:

```bash
./irctl describe 

K8s SHIR Name:shir-demo 
Purview AccountName:   shirdemopurview 
Installation ID:       00000000-0000-0000-0000-000000000000 
Kubernetes Namespace:  shirdemopurview-shir-demo, compute-fleet-system(control-plane) 
K8s SHIR Version:      Unknown (Installation not completed) 
Status:                Initializing 
Healthiness:           Unhealthy

kubectl get pods --namespace shirdemopurview-shir-demo

NAME                                       READY   STATUS    RESTARTS   AGE 
batch-defaultspec-4pbwx                    0/1     Pending   0          10m 
batch-defaultspec-7t9bl                    0/1     Pending   0          10m 
dynamic-config-provider-778c686fdc-9mkjb   0/1     Pending   0          10m 
interactive-schemaprocess-bcrmf            0/1     Pending   0          10m 
interactive-schemaprocess-fn66x            0/1     Pending   0          10m 
logagent-ds-84jqn                          0/1     Pending   0          10m 
logagent-ds-k7vw8                          0/1     Pending   0          10m 
user-credential-proxy-579c899b64-d4q5v     0/1     Pending   0          10m 
```

There are a couple potential causes:

- Connectivity with the Microsoft Purview service endpoint
- Kubernetes node configuration error

### Cause - Connectivity with the Microsoft Purview service endpoint

Kubernetes can't connect to MCR (mcr.microsoft.com). This error is usually caused by network settings or a firewall.

If seeing the status as 'ImagePullBackOff', it means your Kubernetes can't connect to MCR (mcr.microsoft.com) to download Pod images. This error is usually caused by network settings or a firewall.

![Screenshot of the command line showing the ImagePullBackOff status.](media/kubernetes-integration-runtime/image-pull-back-off.png)

### Resolution - Connectivity with the Microsoft Purview service endpoint

Review the network topology for your Kubernetes cluster. For example, for Azure Kubernetes you should check:

- [DNS Resolution](/en-us/azure/aks/coredns-custom)
- [Egress outbound](/en-us/azure/aks/egress-outboundtype)
- [VNet/Firewall](/en-us/azure/firewall/protect-azure-kubernetes-service)

Note

The troubleshooting steps required are different for each Kubernetes provider. Deployment location and individual network details vary between networks. You need to review connectivity through your organization's network.

Review the network topology of the IRCTL host machine. Refer to these sections of the [general integration runtime troubleshooting page](scanning-shir-troubleshooting#self-hosted-ir-connectivity-issues): Firewall, DNSServer, SSL cert trusts, and http proxy.

### Cause - Kubernetes node configuration error

If the status of some of the Pods stuck in 'Pending', use the describe pod command to see details of the Pod.

For example:

```bash
kubectl describe pod batch-defaultspec-4pbwx  --namespace shirdemopurview-shir-demo

Events: 
  Type     Reason            Age                From               Message 

  ----     ------            ----               ----               ------- 

  Warning  FailedScheduling  13m                default-scheduler  0/5 nodes are available: 1 Too many pods. preemption: 0/5 nodes are available: 5 No preemption victims found for incoming pod.. 
```

The Events from the describe command can tell the reason why the Pod is pending. The FailedScheduling error with detailed message shows that the total number of Pods exceeds the maximum number of the Pod on a Node. A new Pod can't be scheduled to the selected Node.

Note

If there are no Events seen under the description, try to delete the Pod manually by `kubectl delete pod` command and track the newly created one.

### Resolution - Kubernetes node configuration error

Reserve 20 pod number for the kubernetes integration runtime to support normal utilization and upgrade scenarios.

## Kubernetes connectivity error with Microsoft Purview service endpoint

When you attempt to register the Kubernetes supported self-hosted integration runtime, the IRCTRL create command could run long until it eventually times out. Or, after a successful installation, the self-hosted integration runtime status shows as unhealthy or offline in the Microsoft Purview portal.

Check the logs using this command: `kubectl logs [podName] -n compute-fleet-system`

You could see one of these errors:

- `“TraceMessage”:”HttpRequestFailed”, “Host”: “fleet.[REGION].compute.governance.azure.com”`
- `Exception":"System.Net.Http.HttpRequestException: Connection refused fleet.[REGION].compute.governance.azure.com:443`
- `System.AggregateException: Failed to acquire identity token from https://fleet. [REGION].compute.governance.azure.com:443`

### Cause

Kubernetes can't connect to the service backend. This error is usually caused by network settings or a firewall.

### Resolution

Review the network topology for your Kubernetes cluster. For example, for Azure Kubernetes you should check:

- [DNS Resolution](/en-us/azure/aks/coredns-custom)
- [Egress outbound](/en-us/azure/aks/egress-outboundtype)
- [VNet/Firewall](/en-us/azure/firewall/protect-azure-kubernetes-service)

Note

The troubleshooting steps required are different for each Kubernetes provider. Deployment location and individual network details vary between networks. You need to review connectivity through your organization's network.

Review the network topology of the IRCTL host machine. Refer to these sections of the [general integration runtime troubleshooting page](scanning-shir-troubleshooting#self-hosted-ir-connectivity-issues): Firewall, DNSServer, SSL cert trusts, and http proxy.

## Unregister a runtime whose local resource is unavailable

If your local self-hosted integration runtime is accidentally deleted from the Kubernetes cluster, you can't delete it using the [`irctl delete` command](data-map-integration-runtime-kubernetes-irctl#delete) and you can't install it to another Kubernetes cluster.

### Cause

A self-hosted integration runtime can only be installed on one Kubernetes cluster. After it's registered, it can't be installed on another cluster before it's unregistered.

### Resolution

1. Check the self-hosted integration local status. You should see that no running self-hosted integration runtime is found.

    ```bash
    $./irctl describe
    ```
2. Check the self-hosted integration runtime in the Microsoft Purview portal. You should see an **Offline** status. (Though, there's a 1 hour latency for token expiration.)
3. Select **Unregister installation** next to the status and confirm the operation.
4. After the unregistration is complete, you can see the status shows as **Not registered**.
5. Select the integration runtime and get the registration key.
6. [Reinstall the integration runtime](data-map-integration-runtime-kubernetes#create-kubernetes-supported-self-hosted-integration-runtime).