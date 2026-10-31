---
layout: Conceptual
title: Windows 365 Support for MXC | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/process-isolation-on-cloud-pcs
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn what Microsoft Execution Containers (MXC) is, how process isolation works on a Windows 365 Cloud PC, what you need, and how to verify support.
ms.date: 2026-10-28T00:00:00.0000000Z
ms.topic: concept-article
ms.service: windows-365
ms.subservice: windows-365-enterprise
author: DelzeenMachhi
ms.author: dmachhi
ms.reviewer: 
locale: en-us
document_id: a14854fc-4097-c83f-5872-1a4e3de05a91
document_version_independent_id: a14854fc-4097-c83f-5872-1a4e3de05a91
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/process-isolation-on-cloud-pcs.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: process-isolation-on-cloud-pcs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/process-isolation-on-cloud-pcs.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 16981c2e-d427-5c48-bd82-dd45fecc00e1
---

# Windows 365 Support for MXC | Microsoft Learn

## What is MXC?

[Microsoft Execution Containers (MXC)](/en-us/windows/apps/develop/mxc/) is an open-source, policy-driven execution technology for running workloads with defined resource permissions. You use the .NET or TypeScript SDK in your app to select a workload, describe what it can access, and run it in a supported containment environment.

Apps, agents, and developer tools often run code that they didn't create or fully control, such as AI-generated commands, third-party tools, and user-provided scripts. Without containment, that code can inherit broad access to files, credentials, network services, and other resources. MXC limits that access to what the task requires.

MXC supports Windows, Linux, and macOS through platform-specific containment backends. A container doesn't necessarily mean a virtual machine or a container image. A workload can run in an operating-system process sandbox, a separate session, or a virtualized environment. For how these models compare, see [MXC architecture and containment models](/en-us/windows/apps/develop/mxc/architecture).

## Windows 365 support

A Cloud PC is a persistent Windows device in Azure. It runs the same operating system, the same applications, and the same management stack as a physical Windows device.

Because of that, MXC process isolation works on a Cloud PC the same way it works on a physical device. Windows 365 adds no isolation mechanism of its own, and nothing about a Cloud PC interferes with process isolation.

## What you need

| Requirement | Detail |
| --- | --- |
| Windows version | Windows 11, version 24H2 or later, with a supported `ProcessContainer` environment. |
| Cloud PC size | Any supported size. Process isolation doesn't require nested virtualization. |
| SDK (.NET) | .NET 8 SDK or later, and the `Microsoft.Mxc.Sdk` package from NuGet.org. |
| SDK (TypeScript) | Node.js 18 or later, and the `@microsoft/mxc-sdk` package from npm. |
| Host app | A trusted app or agent runtime that selects the policy and handles results. |

A supported Windows version doesn't guarantee that every optional feature is available. Check [MXC containment options and platform support](/en-us/windows/apps/develop/mxc/platform-support) and address any host-preparation requirements the SDK reports.

## Use process isolation on your Cloud PC

Follow these steps on the Cloud PC. They're the same steps as on a physical device.

### Step 1: Update Windows

1. On the Cloud PC, select **Start** &gt; **Settings** &gt; **Windows Update**.
2. Select **Check for updates**, install any available updates, and restart if you're prompted to.

By SKU:

- **Windows 365 Enterprise**: set the provisioning policy to a supported Windows version.
- **Windows 365 Business**, **Flex**, and **Reserve**: confirm the Cloud PC is on a supported version.

### Step 2: Confirm the backend is available

Query support before you launch a workload, and keep handling errors at launch, because availability can change.

| SDK | Discovery entry point |
| --- | --- |
| .NET | `MxcSandbox.GetPlatformSupport()` |
| TypeScript | `getPlatformSupport()` |

Check that the result reports support and that `ProcessContainer` appears in the available methods. Treat discovery as advisory, not as a complete policy validator. For details, see [Start with runtime discovery](/en-us/windows/apps/develop/mxc/platform-support#start-with-runtime-discovery).

### Step 3: Run a workload

Follow [Quickstart: Run a workload with the MXC SDK](/en-us/windows/apps/develop/mxc/quickstart). The quickstart creates a sample input, allows the workload to read it, grants write access to a separate output folder, and leaves network and UI permissions denied.

Run the quickstart's denied-write case as well. A permitted run that succeeds and a denied run that fails together confirm that the boundary is enforced on your Cloud PC.

### Step 4: Author your policy

Start with deny-by-default permissions and add only the resources the task requires. See [Author and validate an MXC policy](/en-us/windows/apps/develop/mxc/policy) and adapt the [MXC policy examples](/en-us/windows/apps/develop/mxc/examples).

To investigate missing access, use [Learning Mode](/en-us/windows/apps/develop/mxc/learning-mode), which is supported for Windows `ProcessContainer` workloads and therefore available on a Cloud PC. Learning Mode provides evidence, not an access decision. Review each observation, then remove all learning and audit settings and run a final enforcing test.

Important

Process isolation runs inside the user's session and doesn't require nested virtualization. Any MXC caller that selects a containment backend above process isolation — such as a session or virtualized environment — does require it. On a Cloud PC, nested virtualization has its own prerequisites. See [Set up virtualization-based workloads on your Windows 365 Cloud PC](/en-us/windows-365/enterprise/nested-virtualization).