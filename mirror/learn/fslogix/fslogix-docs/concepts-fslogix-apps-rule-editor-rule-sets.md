---
layout: Conceptual
title: FSLogix Apps RuleEditor and Rule Sets- FSLogix - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/concepts-fslogix-apps-rule-editor-rule-sets
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Provides technical details for Application Rule Sets.
author: msft-jasonparker
ms.author: japarker
ms.topic: article
ms.date: 2025-02-10T00:00:00.0000000Z
ms.custom: template-concept
locale: en-us
document_id: a96dd836-c324-3e58-74de-4fcdedc267bb
document_version_independent_id: a96dd836-c324-3e58-74de-4fcdedc267bb
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/concepts-fslogix-apps-rule-editor-rule-sets.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: concepts-fslogix-apps-rule-editor-rule-sets
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/concepts-fslogix-apps-rule-editor-rule-sets.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
2PlusCloud:
- Power
- Azure
- M365
__autotagging_hash:
- 008935950791053BF80B213815A6CC0145C813E14CB199B683510F6D9FEE04A1
platformId: 6662bd5c-df5f-5159-d945-31d25fe325da
---

# FSLogix Apps RuleEditor and Rule Sets- FSLogix - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

The FSLogix Apps RuleEditor is a standalone application that creates FSLogix Rule Set files. FSLogix Apps Services (`frxsvc`) processes Rule Set files and can perform various actions that manage the end-user experience in virtual desktop environments. Rule Set files are a collection of rules that show, hide, redirect, or customize specific aspects of the registry, file system, applications or printers. A single Rule Set file can support any number of rules of varying types. In most cases, keeping the Rule Set files contained to a specific type of customization makes them easier to maintain and troubleshoot.

## Types of rules

You can create four types of rules:

- Hiding rule
- Redirection rule
- Specify value rule

Caution

Hiding and redirection rules manipulate the file system at very fundamental level. These types of rules can be very powerful, and creating or changing them can have unexpected consequences. Always test and validate Rule Sets before deploying them in a production environment.

### Hiding rule

A hiding rule hides specific items from a user or group of users. Hiding rules can apply to files, folders, registry keys, registry values, printers, or fonts.

### Redirection rule

Redirection rules allow IT administrators to redirect non-profile or other specific data into the user profile container so it's available on subsequent sign-ins regardless of which virtual machine they sign into.

### App container (VHD) rule (retired)

Note

App container rules have been retired as of February 11, 2025 and are no longer supported. Please review the [**feature deprecation**](troubleshooting-feature-deprecation) page for additional information.

### Specify value rule

The specify value rule will, at sign-in, set a registry value for a specific user or group of users. This rule is most commonly used when users need HKLM-based registry key values to change based on which users are signing in.

## Rule Assignments

Important

FSLogix Apps Rule Set assignments don't support Microsoft Entra ID cloud-only accounts. To use the assignment functionality, you must sync the users and groups from an Active Directory domain controller. Additionally, the virtual machines must have line-of-sight to a domain controller to resolve SIDs.

Application Rule Sets are assigned to users, groups, and other entities using the RuleEditor. Newly created rules automatically have the Everyone group assigned with the Applies setting configured to No.

### Assignment order

The ordering of assignments affects how the Rule Set is applied. When the assignment file is processed, the Rule Set is applied from top to bottom. Assignment ordering is managed using the `Move Up` and `Move Down` buttons.

![rule set assignment everyone at top](media/fsl-ruleset-assignment-everyone-top.jpg)

^Figure 1: Everyone group processed at top^

**Result:** Rule Set applies to `CONTOSO\Domain Users` only.

![rule set assignment everyone at bottom](media/fsl-ruleset-assignment-everyone-bottom.jpg)

^Figure 2: Everyone group processed at bottom^

**Result:** Rule Set **does not** apply to any user or group.

### Assignment types

You can assign Rule Sets to the following entities:

- User
- Group
- Process
- Network Location (IP Address)
- Computer
- Directory container (distinguished name)
- Environment variable

Note

Any environment variable present at user sign in can be used as part of an assignment.

### Assignment template

You can save the assignments and assignment order as a template for later use. This template becomes the default assignment configuration for any new Rule Sets you create on the same machine.

![assignment template warning](media/fsl-ruleset-assignment-template-warning.jpg)

^Figure 3: Save as Template warning dialog^

## Active Directory (AD) Reporting

Note

Active Directory reporting has been deprecated as of August 22, 2023. Please review the [**feature deprecation**](troubleshooting-feature-deprecation) page for additional information.

Administrators use the AD Reporting feature to validate whether the Rule Set file applies to the expected user or users. The report only shows user accounts affected by the assignment and doesn't display groups.

![A D reporting](media/fsl-ruleset-ad-report.jpg)

^Figure 4: AD Reporting window^