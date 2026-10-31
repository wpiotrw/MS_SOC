---
layout: Conceptual
title: Windows 365 cloud-native and Zero Trust deployment guidance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-365-deployment-guidance
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Recommended Windows 365 deployment decisions for a simpler, faster, and more secure Cloud PC deployment, with improved reliability and supportability at scale.
ms.service: windows-365
ms.topic: overview
ms.date: 2026-08-27T00:00:00.0000000Z
author: Mauvlans
ms.author: adnich
locale: en-us
document_id: 572d2f2d-2b64-efd5-cdde-7f78a5c43cb7
document_version_independent_id: 572d2f2d-2b64-efd5-cdde-7f78a5c43cb7
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-365-deployment-guidance.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-365-deployment-guidance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-365-deployment-guidance.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 8b42c4ce-122c-2a11-1bb3-f79bb5296c70
---

# Windows 365 cloud-native and Zero Trust deployment guidance | Microsoft Learn

Recommended guidance for a simpler, faster, and more secure Cloud PC deployment, with improved reliability and supportability at scale.

These articles present recommended approaches for each deployment decision, the considerations behind them, and a practical path to adoption.

## How this guidance fits with the planning guide

Use the [Windows 365 planning guide](planning-guide) to define objectives, inventory your environment, determine licensing, create a rollout plan, and prepare communications and support. Use this deployment guidance to make the architecture and operating-model decisions that shape that plan.

This guidance doesn't replace planning. It gives you a recommended starting point for the major deployment choices: identity, network, images, updates, management, user data, clients, and supportability. Start with the recommended option for each area, then document any exception that a business, technical, regulatory, security, application, networking, or operational requirement makes necessary.

## Cloud-native and Zero Trust principles

These articles recommend deployment choices that align to modern cloud-native and Zero Trust operating models.

Microsoft's Zero Trust guidance is defined as a security strategy. It isn't a product or a service, but an approach to designing and implementing the following set of security principles: *verify explicitly*, *use least privilege access*, and *assume breach*. Rather than relying on implicit trust based on network location, these models prioritize identity, device health, application access, and data protection controls to verify access continuously and reduce security risk.

For more information, see [Zero Trust overview](/en-us/security/zero-trust/zero-trust-overview).

## Deployment guidance structure

These articles consolidate Microsoft's recommended Windows 365 deployment decisions across these critical pillars: identity, network, images, updates, management, user data, clients, and supportability. By bringing these elements together, the guide provides a unified, cloud-native, and Zero Trust-aligned blueprint for successful deployments.

This deployment model is the preferred starting point for most organizations because it aligns with cloud-native and Zero Trust principles, and reduces operational complexity. Organizations should validate this approach against their specific requirements and adopt alternative models only where a documented business or technical dependency exists.

## Comparative deployment pillars

For each pillar, these articles contrast the recommended option with its traditional alternative. They also outline a practical adoption path, helping IT and platform technical decision-makers transition with clarity and confidence.

The recommended model requires less configuration and fewer customer-managed components to deploy and operate Windows 365 Cloud PCs. By prioritizing cloud-based identity, Microsoft Hosted Network, Intune management, and cloud data locations, this approach reduces on-premises dependencies, which shortens provisioning time and removes the need to build additional infrastructure.

[![Diagram comparing the recommended cloud-native Windows 365 deployment model with the traditional alternative across the identity, network, images, updates, management, and user data pillars.](windows-365-deployment-guidance-image.svg)](windows-365-deployment-guidance-image.svg#lightbox)

## Recommended deployment decisions at a glance

For each pillar, start by evaluating the recommended option against your organization's requirements. Use a traditional alternative only where a documented dependency exists and can't be met by the cloud-native approach (for example, technical, regulatory, compliance, security, application, networking, or operational).

Note

Cloud-native deployment options can still provide access to on-premises resources when required. In this context, cloud-native doesn't mean cloud-only.

| Deployment decision | Recommended option | Traditional alternative |
| --- | --- | --- |
| Identity and device join | Microsoft Entra join | Microsoft Entra hybrid join |
| Network | Microsoft Hosted Network (MHN) | Azure Network Connection (ANC) |
| Images | Gallery images | Custom images |
| Updates | Windows Autopatch | Configuration Manager / WSUS |
| Management | Intune management | Configuration Manager (co-management) / Group Policy |
| User data | Cloud data (OneDrive, Teams, SharePoint, Edge profiles) | Home drives, file shares, folder redirection |
| Clients | Windows App, Windows 365 Link, Windows 365 Boot, Windows 365 Switch | Thin clients and Remote Desktop clients |

Important

Where an alternative may be required, aim to limit its scope only to the affected users or scenarios. The decision should be documented along with the affected users or workloads, the business or technical requirement being addressed, the associated trade-offs, and any future opportunities to move toward the recommended cloud-native model.

Organizations should seek to minimize the scope of exceptions wherever possible. This ensures that the broader deployment can retain the benefits of a cloud-native, Zero Trust approach.

## Benefits of the recommended model

- **Less configuration** — each recommended default requires minimal or no configuration. You can run a cloud-native pilot without an Azure network, an image pipeline, or a directory-sync dependency.
- **Fewer on-premises dependencies** — removing Microsoft Entra Connect sync, custom-image capture, and network configuration shortens both provisioning time and sign-in time.
- **Reduced operational scope** — Microsoft manages the network, the base image, patch orchestration, and the underlying infrastructure. Your team manages policy and apps in Intune rather than servers, file shares, and image pipelines.
- **Identity-based access control** — access is based on identity, device posture, workload, and data signals rather than a trusted network location.
- **Scaling without infrastructure changes** — Microsoft-managed capacity, service-managed gallery images, and cloud-stored user data let you add or move large numbers of Cloud PCs without first expanding infrastructure.
- **Fewer components to troubleshoot** — a deployment built on managed services has fewer customer-owned components in the failure path, which narrows the scope of most troubleshooting.