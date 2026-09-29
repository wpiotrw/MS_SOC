---
layout: Conceptual
title: What is FSLogix - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/overview-what-is-fslogix
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: An overview of FSLogix Containers, Application Masking and Java Version Control
author: msft-jasonparker
ms.author: japarker
ms.topic: overview
ms.date: 2026-03-09T00:00:00.0000000Z
ms.custom: template-overview
locale: en-us
document_id: b34e3ae6-c7f4-7bb0-ab25-afe99fa9dda0
document_version_independent_id: b34e3ae6-c7f4-7bb0-ab25-afe99fa9dda0
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/overview-what-is-fslogix.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: overview-what-is-fslogix
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/overview-what-is-fslogix.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
platformId: 9ee763bb-2ade-8df6-7e70-518b6caf5ddd
---

# What is FSLogix - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

FSLogix enhances and enables a consistent experience for Windows user profiles in virtual desktop computing environments. FSLogix isn't limited to virtual desktop environments, but could be used on physical desktops where a more portable user experience is desired.

Here are a few things that FSLogix provides:

- Roam user data between remote computing session hosts.
- Minimize sign in times for virtual desktop environments.
- Optimize file I/O between host/client and remote profile store.
- Provide a local profile experience, eliminating the need for roaming profiles.
- Simplify the management of applications and 'Gold Images'.

FSLogix provides customers with both ease of configuration and various levels of flexibility. This can lead to limitless configuration options of which, can have unintended consequences. FSLogix can be a complex solution with various dependencies on other systems and infrastructure. We recommend that you engage with resources who have the following skill set or have these skills inherently:

- Identity and Authentication
- Storage design and architecture
- Active Directory, Azure Active Directory, or Azure Active Directory Domain Services
- Windows Deployment (Server or Desktop)
- Application Compatibility

Note

FSLogix provides unique integration and advantages when used in an [Azure Virtual Desktop](/en-us/azure/virtual-desktop/) environment.

## Key capabilities

- Redirect user profiles to a [storage provider](concepts-fslogix-terminology). Mounting and using the profile from a storage provider eliminates delays often associated with solutions that copy profiles to and from a network location.
- Redirect only the portion of the profile that contains Office^1^ data by using an [ODFC](concepts-fslogix-terminology)[container](concepts-fslogix-terminology). The ODFC container allows an organization already using an alternate profile solution^2^ to enable Microsoft 365 applications in multi-session desktop environments.
- Applications use the user's profile as if it were on the local disk. FSLogix uses a filter driver to virtualize and [redirect](concepts-fslogix-terminology) the profile at the file system level. Applications are unaware the profile is on the network. Obscuring the redirection is important because many applications can't work properly with a profile stored remotely.
- [Profile](concepts-fslogix-terminology) containers used with [Cloud Cache](concepts-fslogix-cloud-cache) to provide [high availability](concepts-container-high-availability) and [disaster recovery](concepts-container-recovery-business-continuity) profile solutions.
- [Application Rule Sets](tutorial-application-rule-sets) manage access to an application, font, printer, or other items. Access can be controlled using users, groups, IP Addresses, and other criteria. Application Rule Sets significantly decrease the complexity of managing large numbers of gold images.

^1 Office data includes, but is not limited to Microsoft 365 applications, OneDrive, Teams, SharePoint, and OneNote.^^2 Under most circumstances, ODFC containers are not used with Profile containers simultaneously.^