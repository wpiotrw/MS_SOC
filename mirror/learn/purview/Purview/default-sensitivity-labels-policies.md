---
layout: Conceptual
title: Learn about the default sensitivity labels and policies to protect your data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- m365copilot
description: Learn about the default sensitivity labels and policies for Microsoft Purview Information Protection to classify and protect sensitive data.
locale: en-us
document_id: 41b71426-1fb7-365b-9cea-37ea176ab9d2
document_version_independent_id: 41b71426-1fb7-365b-9cea-37ea176ab9d2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/default-sensitivity-labels-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: default-sensitivity-labels-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/default-sensitivity-labels-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 1e7447af-c195-5820-861f-b7cd999835a4
---

# Learn about the default sensitivity labels and policies to protect your data | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When you use [Data Security Posture Management](data-security-posture-management) or [Data Security Posture Management for AI](ai-microsoft-purview) (classic), you can activate some default [sensitivity labels](sensitivity-labels) and their policies for [Microsoft Purview Information Protection](information-protection-solution):

- Sensitivity labels and a sensitivity label publishing policy
- Client-side auto-labeling
- Service-side auto-labeling

Note

The default labels and policies are now automatically created for new customers who have an eligible license for Microsoft Purview.

These default configurations get you up and running quickly with Microsoft Purview Information Protection to help you protect your data in Microsoft 365. You can use them as-is, make just a few changes, or fully customize them to better suit your business requirements. Then, extend the labels beyond Microsoft 365, to protect data in other sources, such as Microsoft Azure and Microsoft Foundry.

If you're an existing customer who wasn't eligible for the automatic creation of the default labels and policies, you can activate the default configurations that are supported by your licenses if you haven't yet configured an equivalent:

| Default configuration | Equivalent |
| --- | --- |
| Sensitivity labels and a sensitivity label policy | Published sensitivity labels |
| Client-side auto-labeling | One or more sensitivity labels configured to automatically apply (or recommend to users) in Office apps |
| Service-side auto-labeling | At least one auto-labeling policy that's turned on |

## Activate the default labels and policies

If the default labels and polices aren't automatically created for you, you can activate them:

- From the current version of [Data Security Posture Management](data-security-posture-management-learn-about#how-to-use-data-security-posture-management) &gt; **Actions** &gt; **Setup tasks**, select **Protect your data with sensitivity labels**
- From [Data Security Posture Management for AI](dspm-for-ai#how-to-use-data-security-posture-management-for-ai) (classic) &gt; **Recommendations**, select **Protect your data with sensitivity labels**

After the labels and policies are created, you'll need to enable sensitivity labels for SharePoint and OneDrive. This one-time, manual step is a prerequisite to use sensitivity labels in Office for the web, and auto-labeling policies for SharePoint and OneDrive.

To do this step, use the following banner at the top of the **Information Protection** &gt; **Overview** page, and select **Turn on now**. If you don't see this banner, sensitivity labels for SharePoint and OneDrive have already been enabled for your tenant.

![Enable sensitivity labels for SharePoint and OneDrive banner.](media/turn-on-mip-labels.png)

For more information about this capability, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

## Default sensitivity labels

When you don't have sensitivity labels that are published, we'll create the following labels for you:

| Label name | Label description for users | Settings |
| --- | --- | --- |
| Personal | Non-business data, for personal use only. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Public | Business data that is specifically prepared and approved for public consumption. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| General | Business data that is not intended for public consumption. However, this can be shared with external partners, as required. Examples include a company internal telephone directory, organizational charts, internal standards, and most internal communication. | **Scope**: Files & other data assets, Emails **Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| General  \ Anyone (unrestricted) | Organization data that isn’t intended for public consumption but can be shared with external partners if appropriate. Examples include customer conversations that don’t include sensitive info or released marketing materials. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| General  \ All Employees (unrestricted) | Organization data that isn’t intended for public consumption. If you need to share this content with external partners, confirm with other data owners that it's OK to share and then change the label to General \ Anyone (unrestricted) . Examples include a company internal telephone directory, organizational charts, internal standards, and most internal communication. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Confidential | Sensitive business data that could cause damage to the business if shared with unauthorized people. Examples include contracts, security reports, forecast summaries, and sales account data. | **Scope**: Files & other data assets, Emails **Content marking**: No**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Confidential  \ Anyone (unrestricted) | Confidential data that doesn’t need to be encrypted. Use this option with care and appropriate business justification. | This label is selected for client-side auto-labeling and service-side auto-labeling.**Scope**: Files & other data assets, Emails, Meetings^\*^**Content marking**: Footer: Classified as Confidential**Auto-labeling**: Recommend that users apply the label **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Confidential  \ All Employees | Confidential data that requires protection, which allows all employees full permissions. Data owners can track and revoke content. | This label is selected for client-side auto-labeling and service-side auto-labeling.**Scope**: Files & other data assets, Emails, Meetings^\*^**Encryption**: All users and groups in the org: Co-Author**Content marking**: Footer: Classified as Confidential**Auto-labeling**: Recommend that users apply the label **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Confidential  \ Trusted People | Confidential data that can be shared with trusted people inside and outside your organization. These people can also reshare the data as needed. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Encryption**: Let users assign permissions:  - Encrypt-Only for Outlook - Prompt users in Word, PowerPoint, and Excel**Content marking**: Footer: Classified as Confidential**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Highly Confidential | Very sensitive business data that would cause damage to the business if it was shared with unauthorized people. Examples include employee and customer information, passwords, source code, and pre-announced financial reports. | **Scope**: Files & other data assets, Emails **Content marking**: Watermark: HIGHLY CONFIDENTIAL**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Highly Confidential  \ All Employees | Highly confidential data that allows all employees view, edit, and reply permissions to this content. Data owners can track and revoke content. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Encryption**: All users and groups in the org: Co-Author**Content marking**: Footer: Classified as Highly Confidential**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |
| Highly Confidential  \ Specific People | Highly confidential data that requires protection and can be viewed only by people you specify and with the permission level you choose. | **Scope**: Files & other data assets, Emails, Meetings^\*^**Encryption**: Let users assign permissions: - Do Not Forward for Outlook - Prompt users in Word, PowerPoint, and Excel**Content marking**: Footer: Classified as Highly Confidential**Auto-labeling**: No **Group settings**: No**Site settings**: No **Auto-labeling for database columns**: None |

^\*^ The **Meetings** scope is included for customers starting October 2024 if the tenant has [licenses to manually apply a label for scheduled meetings](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling). Additionally:

- The sensitivity label policy includes a default Teams meeting label.
- If the tenant has licenses to manually apply the label to Teams meetings, some of the sensitivity labels also have settings configured to protect these meetings.

Note

The label names and descriptions are automatically available for the following locales: US English, Chinese Simplified and Traditional, French, German, Italian, Japanese, Korean, Portuguese Brazilian, Russian, and Spanish.

If you need additional languages, you can specify your translations [by using PowerShell](create-sensitivity-labels#example-configuration-to-configure-a-sensitivity-label-for-different-languages).

For more information about these configuration settings and what sensitivity labels can do, see [What sensitivity labels can do](sensitivity-labels#what-sensitivity-labels-can-do).

If you need to edit these default sensitivity labels, see [Create and configure sensitivity labels](create-sensitivity-labels#create-and-configure-sensitivity-labels).

## Default sensitivity label policy

The default sensitivity label policy makes the labels available for users to start labeling their documents and emails with sensitivity labels. It has the following configuration:

- Publish the default labels to all users in your tenant
- Default label of **General** \ **All Employees (unrestricted)** for unlabeled documents, email, and meetings
- Users must provide a justification to remove a label or lower its classification

For more information about these policy settings, and other policy settings that are available, see [What label policies can do](sensitivity-labels#what-label-policies-can-do).

If you need to edit these default policy settings, see [Publish sensitivity labels by creating a label policy](create-sensitivity-labels#publish-sensitivity-labels-by-creating-a-label-policy).

When you use these labels in Office apps on Windows, macOS, iOS, and Android, users see new labels within four hours, and within one hour for Word, Excel, and PowerPoint on the web when you refresh the browser. However, you might need to allow up to 24 hours for changes to replicate to all apps and services.

## Client-side auto-labeling

The default client-side auto-labeling configuration automatically recommends users apply a sensitivity label when we detect credit card numbers in documents or emails they’re working with. As a recommendation rather than automatically applied, this configuration serves as a good first step for highlighting concerning content and introduces users to the practice of labeling their documents and emails.

Client-side auto-labeling only works for documents and emails in use by the Office apps Word, Excel, PowerPoint, and Outlook.

The default client-side auto-labeling has the following configuration:

- If there are 1-9 instances of credit card numbers found in a document or email, recommend the user applies the sensitivity label **Confidential** \ **Anyone (unrestricted)**
- If there are 10 or more instances of credit card numbers found in a document or email, recommend the user applies the sensitivity label **Confidential** \ **All Employees**

Note

If we detected you have your own sensitivity labels published, we'll prompt you to select one of your own labels for auto-labeling and configure it for you.

If you want to edit the client-side auto-labeling configuration, see [How to configure auto-labeling for Office apps](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-for-office-apps).

## Service-side auto-labeling

Service-side auto-labeling helps label sensitive documents at rest, and emails in transit. The default service-side auto-labeling policy creates policies that run in simulation mode for documents stored in all SharePoint or OneDrive sites, and all emails that are sent via Exchange Online.

In simulation mode, items aren't actually labeled until the policy is turned on. You can manually turn on the policy. Alternatively, if you don't change the default setting, the policy will be automatically turned on for you if there aren't any changes to the policy within a set number of days from when the simulation completes.

In most cases, the number of days before an unedited policy is automatically turned on is 7. However, specific to new customers from June 23, 2022, the initial number of days is 25, and then 7 after the policy is edited.

Simulation mode allows you to preview what items would get labeled when the policy is turned on, so you can have confidence in the labeling feature before you deploy the policy to your tenant for actual labeling.

The default service-side auto-labeling policies have the following configuration: For all customers:

- If there are 1-9 instances of credit card numbers found in a document or email, apply the sensitivity label **Confidential** \ **Anyone (unrestricted)**
- If there are 10 or more instances of credit card numbers found in a document or email, apply the sensitivity label **Confidential** \ **All Employees**

Note

If we detected you have your own sensitivity labels published, we'll prompt you to select one of your own labels for your auto-labeling policy.

There are two auto-labeling policies for each setting. One policy is for the Exchange location, and the other for the SharePoint and OneDrive locations. Although the policies are created at the same time, simulation isn't immediately turned on for SharePoint and OneDrive:

- Exchange location: The auto-labeling policy is created and immediately starts simulation.
- SharePoint and OneDrive locations: The auto-labeling policy is created but waits 25 days before it automatically starts simulation. This delay ensures that there is time for files to be created and saved to these locations.

When the simulation is complete, review the results. If you are happy with them, turn on the policies.

For more information about simulation mode, see [Learn about simulation mode](apply-sensitivity-label-automatically#learn-about-simulation-mode).

If you want to edit the service-side auto-labeling policy, see [How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange).