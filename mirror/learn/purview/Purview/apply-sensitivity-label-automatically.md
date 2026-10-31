---
layout: Conceptual
title: Automatically apply a sensitivity label to Microsoft 365 data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
audience: Admin
ms.service: purview
ms.subservice: purview-information-protection
ms.date: 2026-10-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
ms.topic: article
ms.custom:
- admindeeplinkMAC
- sfi-ga-nochange
- msecd-doc-authoring-1030
ai-usage: ai-assisted
search.appverid:
- MOE150
- MET150
description: When you create a sensitivity label, you can automatically assign a label to data stored in Microsoft 365, or you can prompt users to select the label that you recommend.
locale: en-us
document_id: d7ac1791-f1d7-f2f3-2218-65ba0ec9ab16
document_version_independent_id: d7ac1791-f1d7-f2f3-2218-65ba0ec9ab16
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/apply-sensitivity-label-automatically.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: apply-sensitivity-label-automatically
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/apply-sensitivity-label-automatically.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 764d8ea0-012f-aef1-8f86-096674cdc62d
---

# Automatically apply a sensitivity label to Microsoft 365 data | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

For information about automatically applying a sensitivity label to data stored outside Microsoft 365 and in the data map, see [Labeling in Microsoft Purview Data Map](data-map-sensitivity-labels).

Tip

**Start here — pick your task**

- **I'm setting up my first auto-labeling policy.** Review the Prerequisites for auto-labeling policies first, then follow Creating an auto-labeling policy.
- **I want to label Exchange email based on the subject, sender, or recipient.** See Example: Apply a label to Exchange email based on the subject.
- **I'm deciding between labeling in Office apps and an auto-labeling policy.** See Compare auto-labeling for Office apps with auto-labeling policies.
- **My simulation results look wrong or incomplete.** See [Auto-labeling classification and simulation concepts](auto-label-classification-simulation) to distinguish available classification, policy matches, and actual labeling. For simulation requirements and workflow, see Learn about simulation mode.
- **I turned on a policy after simulation and want to review coverage.** See Review coverage by simulation context.
- **I want SharePoint default library labels to apply to existing files.** See Apply default sensitivity labels from SharePoint document libraries to existing files.
- **A file wasn't labeled, or has an unexpected label.** Start with Why was — or wasn't — a specific file labeled? to choose the checks for your file. For a reported failure, see [Resolve auto-labeling failures in SharePoint and OneDrive files](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/auto-labeling-failures-sharepoint-onedrive).
- **My active policy has stopped matching Exchange email.** See Policy rule fails to load.
- **I'm hitting a limit** (500,000 files/day, 100 policies, 1,000 explicitly selected SharePoint sites, or 20,000,000 matched files per policy simulation). See How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange, and Use PowerShell for auto-labeling policies to target SharePoint sites by using an adaptive scope.
- **Auto-labeling isn't available in my region.** The **Auto-labeling** page isn't visible in unsupported regions. See the regional availability prerequisite.
- **I want to set a default label for Teams meetings, sites, groups, or Microsoft 365 Copilot.** This article covers files and emails. For container-level default labels (including Teams instant meetings and Meet Now), see [Use sensitivity labels with Microsoft Teams, Microsoft 365 groups, and SharePoint sites](sensitivity-labels-teams-groups-sites). For Copilot default labels, see [Considerations for Microsoft 365 Copilot](ai-m365-copilot-considerations).

When you create a sensitivity label, you can automatically assign that label to Microsoft 365 items such as files and emails when the data matches conditions that you specify.

This ability to apply sensitivity labels to content automatically is important because:

- You don't need to train your users when to use each of your classifications.
- You don't need to rely on users to classify all content correctly.
- Users no longer need to know about your policies—they can instead focus on their work.

There are two different methods for automatically applying a sensitivity label to content in Microsoft 365:

- **Client-side labeling when users edit documents or compose (also reply or forward) emails**: Use a label that's configured for auto-labeling for files and emails (includes Word, Excel, PowerPoint, and Outlook).

    This method supports recommending a label to users, as well as automatically applying a label. But in both cases, the user decides whether to accept or reject the label, to help ensure the correct labeling of content. This client-side labeling has minimal delay for documents because the label can be applied even before the document is saved. However, [not all client apps support auto-labeling](sensitivity-labels-office-apps#support-for-sensitivity-label-capabilities-in-apps).

    For configuration instructions, see How to configure auto-labeling for Office apps on this page.
- **Service-side labeling when content is already saved (in SharePoint or OneDrive) or emailed (processed by Exchange Online)**: Use an auto-labeling policy.

    You might also hear this method referred to as auto-labeling for data at rest (documents in SharePoint and OneDrive) and data in transit (email that is sent or received by Exchange). For Exchange, it doesn't include emails at rest (mailboxes).

    Auto-labeling policies run in the service, so they don't depend on which app version a user has installed. They're available across your organization from the moment you turn a policy on, which makes them suitable for labeling at scale. Because the user doesn't interact with the labeling process, auto-labeling policies don't support *recommended* labeling — instead, run the policy in simulation before you turn it on to help ensure correct labeling.

    For configuration instructions, see How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange on this page.

#### Auto-labeling for SharePoint and OneDrive

    - [PDF documents](sensitivity-labels-office-apps#pdf-support)and Office files for Word (.docx), PowerPoint (.pptx), and Excel (.xlsx) are supported.
        - These files can be auto-labeled at rest before or after the auto-labeling policies are created. Files can't be auto-labeled if they're part of an open session (the file is open).
        - Currently, attachments to list items aren't supported and won't be auto-labeled.

        Important

        PDF labeling must be enabled for your tenant before an auto-labeling policy can process PDFs in SharePoint and OneDrive. Enable it by selecting the **Protect PDFs with Auto-labeling** banner in the Microsoft Purview portal, or by using PowerShell. If PDF labeling isn't enabled, PDFs are skipped entirely: PDFs aren't evaluated or sent for labeling, and no label is applied. For instructions, see [Adding support for PDF](sensitivity-labels-sharepoint-onedrive-files#adding-support-for-pdf).
    - Maximum of 500,000 automatically labeled files in your tenant per day.
    - Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 1,000 explicitly included or excluded SharePoint sites, or up to 100 explicitly included or excluded OneDrive individual users or groups. If you keep the default configuration of **All**, this configuration is exempt from these maximums.
    - For SharePoint, an auto-labeling policy can use an adaptive scope to target sites. For configuration instructions, see Use PowerShell for auto-labeling policies.
    - Existing values for modified, modified by, and the date aren't changed as a result of auto-labeling policies—for both simulation mode and when labels are applied.
    - When the label applies encryption, the [Rights Management issuer and Rights Management owner](rights-management-usage-rights#rights-management-issuer-and-rights-management-owner) is the account that last modified the file.
    - To apply default sensitivity labels from SharePoint document libraries to existing files, see Apply default sensitivity labels from SharePoint document libraries to existing files.

#### Auto-labeling for Exchange

    - PDF attachments and Office attachments are scanned for the conditions you specify in your auto-labeling policy. When there's a match, the email is labeled but not the attachment.
        - For PDF files, if the label applies encryption, these files are encrypted by using [Message encryption](ome) when your tenant is [enabled for PDF attachments](ome-faq#what-file-types-are-supported-as-attachments-in-protected-emails--do-attachments-inherit-the-protection-policies-and-permissions-associated-with-protected-emails--what-about-pdf-).
        - For these Office files, Word, PowerPoint, and Excel are supported. If the label applies encryption and these files are unencrypted, they're now encrypted by using [Message encryption](ome). The encryption settings are inherited from the email.
    - To label and protect emails that contain Teams voicemail messages, see the configuration instructions in [Enable protected voicemail in your organization](/en-us/microsoftteams/set-up-phone-system-voicemail#enable-protected-voicemail-in-your-organization).
    - If you have Exchange mail flow rules or Microsoft Purview Data Loss Prevention (DLP) policies that apply IRM encryption: When content is identified by these rules or policies and an auto-labeling policy, the label is applied. If that label applies encryption, the IRM settings from the Exchange mail flow rules or DLP policies are ignored. However, if that label doesn't apply encryption, the IRM settings from the mail flow rules or DLP policies are applied in addition to the label.
    - Email that has IRM encryption with no label will be replaced by a label with any encryption settings when there's a match by using auto-labeling.
    - Incoming email is labeled when there's a match with your auto-labeling conditions. For this outcome to apply to senders outside your organization, the Exchange location must be set to **All** included and **None** excluded. If the label is configured for [encryption](encryption-sensitivity-labels):
        - That encryption is always applied when the sender is from your organization.
        - By default, that encryption isn't applied when the sender is outside your organization but can be applied by configuring **Additional settings for email** and specifying a Rights Management owner.
    - When the label applies encryption, the [Rights Management issuer and Rights Management owner](rights-management-usage-rights#rights-management-issuer-and-rights-management-owner) is the person who sends the email when the sender is from your own organization. When the sender is outside your organization, you can specify a Rights Management owner for incoming email that's labeled and encrypted by your policy.
    - If the label is configured to apply [content markings with variables](sensitivity-labels-office-apps#content-markings-with-variables), be aware that for incoming email, this configuration can result in displaying the names of people outside your organization.

Note

For some new customers, we're offering the automatic configuration of default auto-labeling settings for both client-side labeling and service-side labeling. Even if you're not eligible for this automatic configuration, you might find it useful to reference their configuration. For example, you can manually configure existing labels and create your own auto-labeling policies with the same settings to help accelerate your labeling deployment.

For more information, see [Default labels and policies for Microsoft Purview Information Protection](default-sensitivity-labels-policies).

## Compare auto-labeling for Office apps with auto-labeling policies

Use the following table to help you identify the differences in behavior for the two complementary automatic labeling methods:

| Feature or behavior | Label setting: Auto-labeling for files and emails | Policy: Auto-labeling |
| --- | --- | --- |
| App dependency | Yes ([minimum versions](sensitivity-labels-office-apps#support-for-sensitivity-label-capabilities-in-apps)) | No \* |
| Restrict by location | No | Yes |
| Conditions: Sharing options and additional options for email | No | Yes |
| Conditions: Exceptions | No | Yes |
| Conditions: Nested rule logic (AND/OR/NOT) | No | Yes |
| Support for PDF files | No | Yes |
| Support for images | No | [Yes](ocr-learn-about) |
| Recommendations, policy tooltip, and user overrides | Yes | No |
| Simulation mode | No | Yes |
| Exchange attachments checked for conditions | No | Yes |
| Apply visual markings | Yes | Yes (email only) |
| Override IRM encryption applied without a label | Yes if the user has the minimum usage right of Export | Yes (email only) |
| Label incoming email | No | Yes |
| Assign a Rights Management owner for emails sent from another organization | No | Yes |
| Replace manually applied label that has lower priority | No | Yes (configurable) |
| Remove existing label in SharePoint or OneDrive | No | Yes |

\* Auto-labeling isn't currently available in all regions because of a backend Azure dependency. If your tenant can't support this functionality, the **Auto-labeling** page isn't visible in the Microsoft Purview portal. For more information, see [Azure dependency availability by country](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

### Licensing and where to find each surface

Auto-labeling is gated by license, and the two surfaces (client-side and service-side) appear in different places in the portal. If you expect to see auto-labeling and it isn't there, verify the license first.

| Surface | Configured in | Included with |
| --- | --- | --- |
| Client-side auto-labeling (Office apps) | Sensitivity label configuration → **Auto-labeling for files and emails** page | Microsoft 365 E5, Microsoft 365 E5 Compliance, Microsoft 365 E5 Information Protection & Governance, Azure Information Protection Premium P2 (standalone) |
| Service-side auto-labeling (SharePoint, OneDrive, Exchange) | Microsoft Purview portal → **Information Protection** → **Policies** → **Auto-labeling policies** | Same E5 / P2-tier SKUs as above |
| Container-level default labels (Teams, groups, sites) | Documented in [Use sensitivity labels with Microsoft Teams, Microsoft 365 groups, and SharePoint sites](sensitivity-labels-teams-groups-sites) | Not covered on this page |

For the authoritative, per-SKU feature matrix (including current entitlements for Microsoft 365 Business Premium, Frontline, Education, and Government clouds), see [Microsoft 365 licensing guidance for security and compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection-microsoft-purview-information-protection).

Common licensing symptoms:

- **You have E3 or Business Premium.** Auto-labeling of files and emails isn't included at this SKU. Sensitivity labels and manual labeling are — auto-labeling requires an E5 / P2-tier add-on.
- **You have E5 but don't see auto-labeling policies in the portal.** Confirm you're in the [Microsoft Purview portal](https://purview.microsoft.com/) (not the legacy Compliance Center), that your role includes **Compliance Administrator** or **Compliance Data Administrator**, and that your region supports auto-labeling ([Azure dependency availability by country](/en-us/troubleshoot/azure/general/dependency-availability-by-country)).
- **You have E5 and see the page, but saving a new policy fails with "No matching database is available."** This is a known transient backend condition. Retry the save; if it fails repeatedly over 24 hours, open a support case with the policy configuration.

## How multiple conditions are evaluated when they apply to more than one label

The labels are ordered for evaluation according to their position that you specify in the Microsoft Purview portal: The label positioned first has the lowest position (least sensitive, so lowest priority) and the label positioned last has the highest position (most sensitive, so highest priority). The label with the highest order number is selected.

This behavior is also true for service-side auto-labeling (auto-labeling policies) when sublabels share the same parent label: If after evaluation and ordering, more than one sublabel from the same parent label meets the auto-labeling conditions, the sublabel with the highest order number is selected and applied.

However, the behavior is a little different for client-side auto-labeling (auto-labeling settings in the label). If multiple sublabels from the same parent label match the conditions:

- If a file is not already labeled, the highest order sublabel that's configured for automatic labeling is always selected, rather than the highest order sublabel that's configured for recommended labeling. If none of these sublabels are configured for automatic labeling but only recommended labeling, the highest order sublabel is selected and recommended.
- If a file is already labeled with a sublabel from the same parent, no action is taken and the existing sublabel remains. This behavior applies even if the existing sublabel was a default label or automatically applied.

For more information about label priority, see [Label priority (order matters)](sensitivity-labels#label-priority-order-matters).

## Considerations for label configurations

The following considerations apply to both client-side labeling and service-side labeling.

### Don't configure a parent label to be applied automatically or recommended

If you're using parent labels with sublabels, rather than label groups: You can't apply a parent label (a label with sublabels) to content. Make sure that you don't configure a parent label to be auto-applied or recommended in Office apps, and don't select a parent label for an auto-labeling policy. If you do, the parent label won't be applied to content.

To use automatic labeling with sublabels that have parent labels, make sure you publish both the parent label and the sublabel.

For more information about parent labels, label groups, and sublabels, see [Sublabels that use parent labels or label groups](sensitivity-labels#sublabels-that-use-parent-labels-or-label-groups).

### Label scoping that excludes files or emails

To automatically apply a sensitivity label to content, the [label's scope](sensitivity-labels#label-scopes) must include **Files & other data assets** to automatically apply a label to documents, and **Emails** to automatically apply a label to emails.

For more information when you select just one of these label scopes, see [Scope labels to just files or emails](sensitivity-labels-office-apps#scope-labels-to-just-files-or-emails).

## Will an existing label be overridden?

An auto-labeling policy that applies a sensitivity label won't remove an existing sensitivity label to leave content unlabeled. However, for SharePoint and OneDrive, an auto-labeling policy configured to automatically remove a label can remove the selected label, including when the label was manually applied, and leave the content unlabeled.

Default behavior whether automatic labeling will override an existing label:

- When content has been manually labeled, that label won't be replaced by automatic labeling.
- Automatic labeling will replace a [lower priority sensitivity label](sensitivity-labels#label-priority-order-matters) that was automatically applied, but not a higher priority label.

    Tip

    For example, the sensitivity label at the top of the list in the Microsoft Purview portal is named **Public** with an order number (priority) of 0, and the sensitivity label at the bottom of the list is named **Highly Confidential** with an order number (priority of 4). The **Highly Confidential** label can override the **Public** label but not the other way around.

For auto-labeling policies that apply a sensitivity label, you can select a setting to override a manually applied label that has lower priority. This setting isn't required for an auto-labeling policy configured to automatically remove a label.

| Existing label | Override with label setting: Auto-labeling for files and emails | Override with policy: Auto-labeling |
| --- | --- | --- |
| Manually applied, lower priority | No | No by default, but configurable |
| Manually applied, higher priority | No | No |
| Automatically applied or default label, lower priority | Yes \* | Yes |
| Automatically applied or default label, higher priority | No | No |

\* There's an exception for sublabels that share the same parent label

The configurable setting for auto-labeling policies is on the **Additional label settings** page.

## How to configure auto-labeling for Office apps

Tip

Looking for **auto-labeling policies for SharePoint, OneDrive, or Exchange** (service-side auto-labeling for files at rest and emails in transit)? Skip ahead to How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange. The section on this page is for client-side auto-labeling in Word, Excel, PowerPoint, and Outlook.

Check the [minimum versions required](sensitivity-labels-office-apps#support-for-sensitivity-label-capabilities-in-apps) for automatic labeling in Office apps.

The auto-labeling settings for Office apps are available when you [create or edit a sensitivity label](create-sensitivity-labels). Make sure the label scope **Files & other data assets** is selected to auto-label documents, and **Emails** is selected to auto-label emails. For example:

![Sensitivity label scope options for Items that include Files and Email.](media/filesandemails-scope-options-sensitivity-label.png)

As you move through the configuration, you see the **Auto-labeling for files and emails** page where you can choose from a list of sensitive info types or trainable classifiers:

![Label conditions for auto-labeling in Office apps.](media/sensitivity-labels-conditions.png)

When this sensitivity label is automatically applied, the user sees a notification in their Office app. For example:

![Notification that a document had a label applied automatically.](media/sensitivity-label-automatically-applied.png)

Because of a timing issue, auto-labeling for Office apps might not trigger if you also use mandatory labeling. For details, see the additional information for configuring the policy setting [Require users to apply a label to their email and documents](sensitivity-labels-office-apps#labeling-timing-issues).

### Configuring sensitive info types for a label

When you select the **Sensitive info types** option, you see the same list of [sensitive information types](sit-sensitive-information-type-learn-about) as when you create a data loss prevention (DLP) policy. So you can, for example, automatically apply a Highly Confidential label to any content that contains customers' personal information, such as credit card numbers, social security numbers, or passport numbers:

![Sensitive info types for auto-labeling in Office apps.](media/sensitivity-labels-sensitive-info-types.png)

Similarly to when you configure DLP policies, you can then refine your condition by changing the instance count and match accuracy. For example:

![Options for match accuracy and instance count.](media/sit-confidence-level.png)

You can learn more about confidence levels from the DLP documentation: [More on confidence levels](sit-sensitive-information-type-learn-about#more-on-confidence-levels)

Important

Sensitive information types have two different ways of defining the max unique instance count parameters. To learn more, see [Instance count supported values for SIT](sit-limits#instance-count-supported-values-for-sit).

Also similarly to DLP policy configuration, you can choose whether a condition must detect all sensitive information types, or just one of them. And to make your conditions more flexible or complex, you can add [groups and use logical operators between the groups](dlp-policy-design#complex-rule-design).

#### Custom sensitive information types with Exact Data Match

You can configure a sensitivity label to use [exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types) for custom sensitive information types. However, currently, you must also specify at least one sensitive information type that doesn't use EDM. For example, one of the built-in sensitive information types, such as **Credit card number**.

If you configure a sensitivity label with only EDM for your sensitive information type conditions, the auto-labeling setting is automatically turned off for the label.

### Configuring trainable classifiers for a label

If you use this option with Microsoft 365 Apps for Windows version 2106 or lower, or Microsoft 365 Apps for Mac version 16.50 or lower, make sure you've published in your tenant at least one other sensitivity label that's configured for auto-labeling and the sensitive info types option. This requirement isn't necessary when you use later versions on these platforms.

When you select the **Trainable classifiers** option, select one or more of the pretrained or custom trainable classifiers:

![Options for trainable classifiers and sensitivity labels.](media/sensitivity-labels-classifers.png)

The available pretrained classifiers are often updated, so there might be more entries to select than the ones displayed in this screenshot.

For more information about these classifiers, see [Learn about trainable classifiers](trainable-classifiers-learn-about).

### Recommend that the user applies a sensitivity label

If you prefer, you can recommend to your users that they apply the label. With this option, your users can accept the classification and any associated protection, or dismiss the recommendation if the label isn't suitable for their content.

![Option for recommending a sensitivity label to users.](media/sensitivity-labels-recommended-label-option.png)

When you use built-in labeling with the desktop versions of Word, users have an additional option to **Show sensitive content** with the recommended label prompt. When they select this button, the Editor pane steps the user through each detection. The user can then remove the sensitive data or leave it with a better understanding of why the sensitivity label was recommended. When they have this extra information, users have more confidence to select the **Apply sensitivity** button. For example:

![Prompt to apply a recommended label and show sensitive content.](media/sensitivity-label-recommended.png)

This example shows the default recommended label prompt, but as with automatic labeling, you can customize this text to be more meaningful or specific for your users. For example, include your organization's name or reference your IT department to increase visibility and give users more confidence that this isn't a generic message that might not be applicable to them.

Tip

Although recommending a sensitivity label interrupts a user's workflow, it's a very efficient way to educate users in the moment about sensitive data that they work with. To see this in action, watch the video: [Automatically Classify & Protect Documents & Data](https://www.youtube.com/watch?v=v8LqmzBUaOo)

Recommended labeling is particularly powerful when it's coupled with this option to step the users through each instance of sensitive content that's detected. It can lead to more accurate labeling, not just for the immediate item, but also for future items that require manual labeling, or for modified items that might now need relabeling.

### When automatic or recommended labels are applied

Not all Office apps support automatic and recommended labeling. For more information, see [Support for sensitivity label capabilities in apps](sensitivity-labels-office-apps#support-for-sensitivity-label-capabilities-in-apps).

Other considerations:

- You can't use automatic labeling for documents and emails that were previously manually labeled, or previously automatically labeled with a higher sensitivity. Remember, you can only apply a single sensitivity label to a document or email (in addition to a single retention label).
- You can't use recommended labeling for documents or emails that were previously labeled with a higher sensitivity. When the content's already labeled with a higher sensitivity, the user won't see the prompt with the recommendation and policy tip.
- For recommended labels in the desktop versions of Word, the sensitive content that triggered the recommendation is flagged so that users can review and remove the sensitive content instead of applying the recommended sensitivity label.

For details about how these labels are applied in Office apps, example screenshots, and how sensitive information is detected, see [Automatically apply or recommend sensitivity labels to your files and emails in Office](https://support.microsoft.com/office/automatically-apply-or-recommend-sensitivity-labels-to-your-files-and-emails-in-office-622e0d9c-f38c-470a-bcdb-9e90b24d71a1).

### Convert your label settings into an auto-labeling policy

If the label includes sensitive info types for the configured conditions, you'll see an option at the end of the label creation or editing process to automatically create an auto-labeling policy that's based on the same auto-labeling settings.

However, if the label contains trainable classifiers as a label condition:

- When the label conditions contain just trainable classifiers, you won't see the option to automatically create an auto-labeling policy.
- When the label conditions contain trainable classifiers and sensitivity info types, an auto-labeling policy will be created for just the sensitive info types.

Although an auto-labeling policy is automatically created for you by auto-populating the values that you would have to select manually if you created the policy from scratch, you can still view and edit the values before they are saved.

By default, all locations for SharePoint, OneDrive, and Exchange are included in the auto-label policy, and when the policy is saved, it runs in simulation mode. There's no check that you've [enabled sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files), which is one of the prerequisites for auto-labeling to apply to content in SharePoint and OneDrive.

## How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange

Note

Don't use Exchange auto-labeling policies to send encrypted emails for mass mailing distributions. These policies aren't designed for this purpose and can result in sending failures and non-delivery receipts. For this scenario, the label setting to automatically send emails is more suitable.

Make sure you're aware of the prerequisites before you configure auto-labeling policies. Use the Pre-flight checklist to confirm each one in a single scan, then review the full Prerequisites for auto-labeling policies below for details.

### Pre-flight checklist

Before you create an auto-labeling policy, confirm each item below. Missing any one of them typically causes the policy to run without labeling any files, with no error surfaced in the portal. Each item links to the full guidance further down this article.

- [ ] **Auditing is turned on for Microsoft 365.** Required for simulation. See [Turn audit log search on or off](audit-log-enable-disable).
- [ ] **Sensitivity labels are enabled for Office files in SharePoint and OneDrive.** Required before any label can be applied to files in those locations. See [Enable sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).
- [ ] **Auto-labeling is available in your region.** If the **Auto-labeling** page isn't visible in the Microsoft Purview portal, your tenant is in an unsupported region. See [Azure dependency availability by country](/en-us/troubleshoot/azure/general/dependency-availability-by-country).
- [ ] **The label you plan to apply is not a parent label.** Parent labels (labels that have sublabels) can't be applied to content. If you select one, the policy will run but nothing will be labeled. See Don't configure a parent label to be applied automatically or recommended.
- [ ] **The label's scope matches your target content.** To label files, the label scope must include **Files & other data assets**. To label emails, it must include **Emails**. See Label scoping that excludes files or emails.
- [ ] **If the label applies encryption to SharePoint or OneDrive content:** the label is configured with **Assign permissions now**, and **User access to content expires** is set to **Never**. See the encryption details in Prerequisites for auto-labeling policies.
- [ ] **Classification covers the sensitive information types you intend to use.** Policies can evaluate existing files using available classification results, but changing a custom SIT doesn't by itself refresh those results for unchanged files. Review [when historical files need updated classification](auto-label-classification-simulation#when-historical-files-need-updated-classification), including the effects of on-demand classification on active policies.
- [ ] **You have the roles required to review simulation results.** Viewing file contents in the source view requires the **Data Classification Content Viewer** role (included in the Content Explorer Content Viewer, Information Protection, and Information Protection Investigators role groups). Global admins don't have this role by default.
- [ ] **You have the roles required to turn the policy on after simulation.** Turning a policy from **Ready to turn on** to **On** requires **Compliance Administrator** or **Compliance Data Administrator**. Without one of these roles, the **Turn on policy** button appears greyed out even after a successful simulation.

When every item is confirmed, continue to Prerequisites for auto-labeling policies for the full details, then to Creating an auto-labeling policy.

### Prerequisites — detailed reference

Every prerequisite for an auto-labeling policy is listed below. Confirm each item before you configure a policy — missing any one typically causes the policy to run without labeling any files, with no in-portal error surfaced.

- Simulation mode:

    - Auditing for Microsoft 365 must be turned on. If you need to turn on auditing or you're not sure whether auditing is already on, see [Turn audit log search on or off](audit-log-enable-disable).
    - To view file or email contents in the source view, you must have the **Data Classification Content Viewer** role, which is included in the **Content Explorer Content Viewer** role group, or **Information Protection** and **Information Protection Investigators** role groups. Without the required role, you don't see the preview pane when you select an item from the **Items to review** tab. Global admins don't have this role by default.
- To auto-label files in SharePoint and OneDrive:

    - You have [enabled sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).
    - If you want the policy to process PDFs, you have [enabled PDF support](sensitivity-labels-sharepoint-onedrive-files#adding-support-for-pdf) by using the portal banner or PowerShell. Otherwise, PDFs are skipped without being evaluated or sent for labeling.
    - For OneDrive, the OneDrive account must be associated with the corresponding user account. A OneDrive account that isn't associated with its user account (sometimes called a detached OneDrive account) isn't supported for auto-labeling or simulation. Use a properly associated OneDrive account, or move the content to a supported SharePoint or OneDrive location, and then rerun simulation.
    - At the time the auto-labeling policy runs, the file mustn't be open by another process or user. A file that's checked out for editing falls into this category, and similarly, all files in a library that's configured to [require documents to be checked out](https://support.microsoft.com/office/set-up-a-library-to-require-check-out-of-files-0c73792b-f727-4e19-a1f9-3173899e695b).
    - If historical files haven't been classified or need updated classification, use [on-demand classification](on-demand-classification). This isn't required for every policy change. Review scan scope, estimates, and active-policy effects before starting classification.
    - If you plan to use [sensitive information types](sit-sensitive-information-type-learn-about):

        - Policy evaluation uses available classification results for existing SharePoint and OneDrive files. Changing a custom SIT definition doesn't by itself reclassify unchanged historical files, and a file's last-modified date alone doesn't establish its classification time. See [Policy changes aren't classifier changes](auto-label-classification-simulation#policy-changes-arent-classifier-changes).
        - Validate custom SITs with representative matching and nonmatching files by using [Test sensitive information types](sit-test-a-sit). Then review policy simulation separately; a direct SIT test doesn't establish classification coverage for existing files.
    - If you plan to use document properties as a condition (**Document property is**), this option uses SharePoint managed properties in the same way as they are used for DLP policies. Use exact string matches; regex patterns aren't supported. For more information about managed properties as a search method, see [Manage the search schema in SharePoint](/en-us/sharepoint/manage-search-schema).

        Important

        When a document property is mapped to a SharePoint managed property, such as `RefinableString11`, values containing an ampersand (`&`) might not match an auto-labeling rule that uses **Document property is**. For example, documents with the mapped value `Billing & payment document` might remain unlabeled. Plan around this known limitation rather than relying on a future fix. Consider using a classification value without ampersands, keeping the document metadata and rule value consistent. Before deploying broadly, review simulation results and confirm actual label application in a limited scope.
    - If you have an auto-labeling policy configured to replace a manually applied label but another active auto-labeling policy is configured to apply a label without this option, the label won't be replaced. Because simulation shows the result of one policy, simulation results for the replace label policy show the label as replaced but the conflict is resolved when all policies run.
    - If you have an auto-labeling policy configured to remove a label but another active auto-labeling policy is configured to apply a label and the conditions are matched, the label will be applied rather than removed. This behavior applies even when the apply-label policy applies a different label than the label selected for removal. Because simulation shows the result of one policy, simulation results for the label removal policy show the label as removed but the conflict is resolved when all policies run.
    - If you choose to remove a label that applies encryption, encryption is automatically removed with the label.
- One or more sensitivity labels [created and published](create-sensitivity-labels) (to at least one user) that you can select for your auto-labeling policies. For these labels:

    - It doesn't matter if the auto-labeling in Office apps label setting is turned on or off, because that label setting supplements auto-labeling policies, as explained in the introduction.
    - If the labels you select are configured to use visual markings (headers, footers, watermarks), these markings aren't applied to documents when you use auto-labeling.
    - If the labels apply [encryption](encryption-sensitivity-labels):
        - When the auto-labeling policy includes locations for SharePoint or OneDrive, the label must be configured for the **Assign permissions now** setting, and **User access to content expires** must be set to **Never**.
        - When the auto-labeling policy is just for Exchange, the label can be configured for either **Assign permissions now** or **Let users assign permissions** (for the Do Not Forward or Encrypt-Only options). You can't auto-apply a label that's [configured to apply S/MIME protection](sensitivity-labels-office-apps#configure-a-label-to-apply-smime-protection-in-outlook).

### Scoping a policy with users and groups

Scope options differ by workload. For supported selections and Exchange sender-scope behavior, see **Choose locations** in Creating an auto-labeling policy.

### Learn about simulation mode

Simulation mode is supported for auto-labeling policies and woven into the workflow. You can't automatically label documents and emails, or remove labels, until your policy has run at least one simulation.

For existing SharePoint and OneDrive files, simulation evaluates policy matches using available classification results. Restarting simulation doesn't itself reclassify the content. See [Auto-labeling classification and simulation concepts](auto-label-classification-simulation) for when to change a policy and when to refresh classification.

Important

**What "simulation mode" does — and doesn't — do**

Simulation is designed to evaluate and log matches without applying (or removing) labels. It is not a fully silent dry run. Before you run a simulation, know these behaviors that customers frequently misdiagnose as bugs:

- **Simulation still generates activity alerts.** If a Microsoft Purview alert policy is configured on auto-labeling or sensitive-information-type activity, matches surfaced during simulation trigger those alerts. To avoid mass alert email while validating a policy, temporarily scope or disable the alert policy for the simulation window.
- **Policy actions depend on status and permissions.** If **Turn on policy**, **Edit**, or **Delete** is unavailable, check the current policy status and your permissions. For **Turn on policy**, also check the simulation status. Review any displayed error before retrying.
- **A duplicated policy lands in simulation by default and doesn't notify you.** Duplicating an existing policy creates a new policy in simulation regardless of the source policy's state. If you expect the duplicate to inherit the source's active state, it won't.
- **Simulation and DLP share the same test-mode surface.** Some **Items to review** views can mix auto-labeling and DLP results and can fail to load if either signal is under load. If a view returns an error, retry a few hours later before you open a support case.
- **Simulation limits are documented separately.** The following guidance covers item caps (100 per site displayed, 50,000-record CSV export ceiling, and 20,000,000 matched files per policy simulation), the 12-hour target completion time, and stall detection.

Simulation mode supports up to 20,000,000 matched files. If more than this number of files are matched from an auto-labeling policy, you can't turn on the policy to apply the labels. In this case, you must reconfigure the auto-labeling policy so that fewer files are matched, and rerun simulation. This maximum of 20,000,000 matched files applies to simulation mode only and not to an auto-labeling policy that's already turned on to apply sensitivity labels.

Note

Simulation results can differ from what happens when the policy is turned on:

- Simulation shows the result of a *single* policy. When more than one auto-labeling policy applies to the same content (for example, one policy replaces an existing label and another applies a label without that option), the conflict is resolved only when *all* policies run—so the enforced result can differ from any single policy's simulation.
- Classification results or file contents can change after simulation. A simulation match doesn't prove that classification used the latest SIT definition or that enforcement will successfully label the file. See [Classification, policy evaluation, and enforcement](auto-label-classification-simulation#classification-policy-evaluation-and-enforcement).
- For Exchange, simulation evaluates email that's sent and received during the run, so email results aren't consistent unless the same messages are sent and received again.

Workflow for an auto-labeling policy:

Important

Before you edit an auto-labeling policy or run simulation again, export any available results that you need for later comparison. See [Preserve results before editing or rerunning](auto-label-simulation-results#preserve-results-before-editing-or-rerunning).

1. Create and configure an auto-labeling policy.
2. Run the policy in simulation mode, which can take 12 hours to complete. The completed simulation triggers an email notification that's sent to the user configured to receive [activity alerts](/en-us/defender-xdr/alert-policies).
3. Review the results, and if necessary, refine your policy. For example, you might need to edit the policy rules to reduce false positives, or remove some sites so that the number of matched files doesn't exceed 20,000,000. Rerun simulation mode and wait for it to complete again.
4. Repeat step 3 as needed.
5. Deploy in production.

The simulated deployment runs like the WhatIf parameter for PowerShell, for a specific point in time. You see results reported as if the auto-labeling policy had applied your selected label, using the rules that you defined. You can then refine your rules for accuracy if needed, and rerun the simulation. However, because auto-labeling for Exchange applies to emails that are sent and received, rather than emails stored in mailboxes, don't expect results for email in a simulation to be consistent unless you can send and receive the exact same email messages.

Simulation mode also lets you gradually increase the scope of your auto-labeling policy before deployment. For example, you might start with a single location, such as a SharePoint site, with a single document library. Then, with iterative changes, increase the scope to multiple sites, and then to another location, such as OneDrive.

For details about the newer simulation overview, see [Review simulation results for auto-labeling policies](auto-label-simulation-results). **Sample items**, when displayed, shows the sampled item count. **Contextual summary** is available in supported portal experiences; viewing matched content requires the **Data Classification Content Viewer** role.

Finally, you can use simulation mode to provide an approximation of the time needed to run your auto-labeling policy, to help you plan and schedule when to run it without simulation mode.

Note

If simulation doesn't include expected files, check the policy's scope and conditions, whether files changed after the run, and whether classification reflects the SIT definitions you intend to use. Rerun simulation to review updated policy matches. Rerunning doesn't refresh classification or confirm successful labeling; see [When historical files need updated classification](auto-label-classification-simulation#when-historical-files-need-updated-classification).

### Apply default sensitivity labels from SharePoint document libraries to existing files

SharePoint document libraries can be configured with a default sensitivity label. SharePoint applies this label to new files and to files that users edit in the library. Files that already existed in the library before the default label was configured might remain unlabeled.

To extend your default library label deployment to existing files, create an auto-labeling policy that applies the default sensitivity label from each selected SharePoint document library to eligible existing files at rest. This policy type doesn't inspect file content to choose a label. The label comes from the SharePoint document library's default sensitivity label setting.

Use this configuration when:

- You already use default sensitivity labels for SharePoint document libraries.
- You want the default library label to apply to files that already exist in those libraries.
- You want service-side labeling for files at rest, instead of relying on users to open or edit each file.
- You want to apply the label selected by the SharePoint library configuration, rather than build separate sensitive information type or classifier conditions.

Before you create this type of policy, confirm these requirements:

- Sensitivity labels are enabled for Office files in SharePoint and OneDrive. For more information, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).
- The sensitivity labels that can be used as default library labels are created and published to the appropriate users or groups.
- One or more SharePoint document libraries in your target sites have a default sensitivity label configured.
- You have permissions to create and manage auto-labeling policies.
- You have permission to read the SharePoint site and document library metadata required to identify libraries with default sensitivity labels. For the currently supported configuration path, use Compliance Administrator or an existing SharePoint or Microsoft Entra role with this access, such as SharePoint Administrator.

When you create the policy, select the option to apply default sensitivity labels from SharePoint document libraries to existing files. Select specific SharePoint sites rather than **All**. This policy type doesn't support administrative-unit scoping, so the simplified wizard doesn't include the **Assign admin units** step.

In portal experiences that validate default library labels, each selected SharePoint site needs at least one library with a default sensitivity label. If a site can't be added, use the displayed error to choose your next step:

- **No default library label is configured:** Choose another site, or configure a default sensitivity label for a document library in that site, then try again.
- **Default labels couldn't be verified:** Check your access to the site and its library metadata, then try again. This message doesn't mean that the site has no default library label.

For example:

1. A SharePoint document library has the default sensitivity label **Confidential**.
2. The library contains files that were uploaded before **Confidential** was configured as the library default.
3. You create an auto-labeling policy that uses the default SharePoint document library label configuration.
4. The policy evaluates existing files in that library.
5. Eligible files are labeled **Confidential** by the policy.

For this policy type, simulation identifies files in document libraries that have a default sensitivity label configured. Review the simulation results before you turn on the policy to confirm that the expected SharePoint sites, document libraries, default library labels, and files are included.

If the simulation results don't include files you expected, confirm that the document library has a default sensitivity label configured, the SharePoint site is included in the policy scope, and sensitivity labels are enabled for Office files in SharePoint and OneDrive.

Currently, you can create one auto-labeling policy of this type per tenant, and include up to 10 SharePoint sites in the policy. The policy evaluates only SharePoint document libraries that have a default sensitivity label configured, and applies labels only to eligible supported files. Files might not be labeled if they're open, checked out, locked, unsupported, encrypted in an unsupported way, or otherwise unavailable when the policy evaluates them.

If you need to label existing files across more than 10 SharePoint sites, create the policy for up to 10 sites first. After labeling for those sites is complete and you've reviewed the results, edit the policy to replace the site selection with the next batch of up to 10 sites.

### Creating an auto-labeling policy

To create a policy, follow these steps. Page order and available settings can vary by portal experience; follow the settings shown in your wizard.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**.

    Note

    If you don't see the option for auto-labeling, this functionality isn't currently available in your region because of a backend Azure dependency. For more information, see [Azure dependency availability by country](/en-us/troubleshoot/azure/general/dependency-availability-by-country).
2. Select **+ Create auto-labeling policy**. Choose whether you want to apply a sensitivity label, or remove a label. Then follow the instructions according to the option you chose.

# [Automatically apply label only](#tab/apply-label)
1. For the page **Choose info you want this label applied to**: Select one of the categories, such as **Financial**, and then select a corresponding regulation, such as **Canadian Financial Data**. You can refine your search by using the template search or dropdown box for countries or regions. Or, select **Custom** &gt; **Custom policy** if the templates don't meet your requirements. Select **Next**.
2. For the page **Name your auto-labeling policy**: Provide a unique name, and optionally a description to help identify the automatically applied label, locations, and conditions that identify the content to label.
3. For the **Choose a label to auto-apply** page: Select **+ Choose a label**, select and add a label from the **Choose a sensitivity label** pane, and then select **Next**.
4. For the page **Assign admin units**: If your organization is using [administrative units in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units), auto-labeling policies for Exchange and OneDrive can be automatically restricted to specific users and auto-labeling policies for SharePoint can be automatically restricted to the specific sites configured for the selected administrative units. If your account has been [assigned administrative units](purview-admin-units#permissions-for-administrative-units), you must select one or more administrative units.

    If you don't want to restrict the policy by using administrative units, or your organization hasn't configured administrative units, keep the default of **Full directory**.

    Note

    If you are editing an existing policy and change the administrative units, you must now reconfigure the locations in the next step.
5. For the page **Choose locations where you want to apply the label**: Select and specify locations for Exchange, SharePoint, and OneDrive. If you don't want to keep the default of **All** included for your chosen locations, select the link to choose specific instances to include, or select the link to choose specific instances to exclude. Then select **Next**.

    ![Choose locations page for auto-labeling configuration.](media/locations-auto-labeling-wizard.png)

    Note

    For organizations that are using administrative units and selected in the policy:

    - For SharePoint, you can't use the **Included** or **Excluded** options and must use the **All** default selection.
    - For Exchange and OneDrive, you can use the **Included** or **Excluded** options, but see and can select only users from the administrative units selected in the previous step.

    If you use the **Included** or **Excluded** options:

    - For the **Exchange** location, the policy is applied according to the sender address of the recipients specified. Most of the time, you'll want to keep the default of **All** included with **None** excluded. This configuration is suitable even if you're testing for a subset of users. Instead of specifying your subset of users here, use the advanced rules in the next step to configure conditions to include or exclude recipients in your organization. Otherwise, when you change the default settings here:

        - If you change the default of **All** included and instead, choose specific users or groups, email sent from outside your organization will be exempt from the policy.
        - If you keep the default of **All** included but specify users or groups to exclude, email that these excluded users send will be exempt from the policy, but not email that they receive.
    - For the OneDrive location, you must specify users or groups. Previously, you had to specify sites by URLs. Any existing OneDrive URL sites in auto-labeling policies will continue to work but before you can specify new OneDrive locations, or for restricted admins, you must first delete any existing site URLs. Groups supported: distribution groups, Microsoft 365 groups, mail-enabled security groups, and security groups.
    - For the SharePoint location, you can explicitly select up to 1,000 individual sites. To dynamically target sites, use a [SharePoint adaptive scope](purview-adaptive-scopes). For example, an adaptive scope can use the `SiteTemplate` property to include or exclude communication sites, group-connected sites, Teams private channel sites, classic team sites, or OneDrive sites. For instructions to associate an adaptive scope with an auto-labeling policy, see Use PowerShell for auto-labeling policies.
6. For the **Set up common or advanced rules** page: Keep the default of **Common rules** to define rules that identify content to label across all your selected locations. If you need different rules per location, including some rules that are only available for Exchange, or SharePoint sites and OneDrive accounts, select **Advanced rules**. Then select **Next**.

    The rules use conditions that include [sensitive information types](sit-sensitive-information-type-learn-about), [trainable classifiers](trainable-classifiers-learn-about), sharing options, and other conditions:

    - To select a sensitive information type or trainable classifier as a condition, under **Content contains**, select **Add**, and then choose **Sensitive info types** or **Trainable classifiers**.
    - To select sharing options as a condition, under **Content is shared**, choose either **only with people inside my organization** or **with people outside my organization**.
    - Other conditions that you can select:
        - Attachment or file extension is
        - Attachment or document name matches words or phrases
        - Attachment or document property is
        - Attachment or document size equals or is greater than

    In **Advanced rules**, the name condition is **Attachment name matches words or phrases** for Exchange, or **Document name contains words or phrases** for SharePoint and OneDrive.

    If your location is **Exchange** and you selected **Advanced rules**, there are additional conditions that you can select:

    - Sender IP address is
    - Recipient domain is
    - Recipient is
    - Attachment is password protected
    - Any email attachment's content could not be scanned
    - Any email attachment's content didn't complete scanning
    - Header matches patterns
    - Subject matches patterns
    - Recipient address contains words
    - Recipient address matches patterns
    - Sender address matches patterns
    - Sender domain is
    - Recipient is a member of
    - Sender is

    If your location is **SharePoint sites** or **OneDrive accounts** and you selected **Advanced rules**, there is one other condition that you can select:

    - Document created by
7. Depending on your previous choices, you'll now have an opportunity to create new rules by using conditions and exceptions.

    The configuration options for sensitive information types are the same as those you select for auto-labeling for Office apps. If you need more information, see Configuring sensitive info types for a label.

    When you've defined the rules and confirmed their status is on, select **Next** and complete the remaining settings shown by the wizard.
8. Specify optional configurations on the **Additional label settings** page:

    - **Emails only**: Applicable for both incoming and outgoing emails. When you select this setting, an existing sensitivity label will always be overriden for emails if the sensitivity label you chose for the policy has a [higher priority](sensitivity-labels#label-priority-order-matters). Use this setting to override manually labeled emails with a higher priority label when sensitive content is detected.
    - **All locations**: Applicable for emails and for files in SharePoint and OneDrive. When you select this setting, an existing sensitivity label will always be overriden if the sensitivity label you chose for the policy has a [higher priority](sensitivity-labels#label-priority-order-matters). Use this setting to override manually labeled emails and files with a higher priority label when sensitive content is detected.
    - **Apply encryption to email received from outside your organization**: This option is visible only when the selected sensitivity label applies encryption. If you then select this option to apply encryption to email received from outside your organization, you must assign a [Rights Management owner](rights-management-usage-rights#rights-management-issuer-and-rights-management-owner). This configuration ensures that an authorized person in your organization has Full Control [usage rights](rights-management-usage-rights#usage-rights-and-descriptions) for these emails sent from your outside your organization and now encrypted. This role might be needed to later remove the encryption, or assign different usage rights for users in your organization.

        For **Assign a Rights Management owner**, specify a single user by an email address that's owned by your organization. Don't specify a mail contact, a shared mailbox, or any group type, because these aren't supported for this role.
9. For the **Decide if you want to test out the policy now or later** page: Select **Run policy in simulation mode** if you're ready to run the auto-labeling policy now, in simulation mode. Then decide whether to automatically turn on the policy if it's not edited for 7 days:

    ![Test out the configured auto-labeling policy.](media/simulation-mode-auto-labeling-wizard.png)

    If you're not ready to run simulation, select **Leave policy turned off**.
10. For the **Summary** page: Review the configuration of your auto-labeling policy and make any changes that you need, and complete the configuration.

# [Automatically remove label only](#tab/remove-label)
1. For the **Name your policy for auto-removing label** page: Provide a unique name, and optionally a description to help identify the label to automatically remove, the locations, and conditions that identify the content to unlabel. Select **Next**.
2. For the **Choose a label to auto-remove** page: Select **+ Choose a label**, select and add a label from the **Choose a sensitivity label** pane, and then select **Next**.

Note

If you choose a label that's configured to apply encryption, that encryption is removed in addition to the label. Unlike when you manually remove a sensitivity label that applies encryption, the person who creates the policy doesn't need the Export or Full Control permissions to successfully remove the encryption with an auto-labeling policy.

1. For the page **Assign admin units**: If your organization is using [administrative units in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units), auto-labeling policies for Exchange and OneDrive can be automatically restricted to specific users and auto-labeling policies for SharePoint can be automatically restricted to the specific sites configured for the selected administrative units. If your account has been [assigned administrative units](purview-admin-units#permissions-for-administrative-units), you must select one or more administrative units.

    If you don't want to restrict the policy by using administrative units, or your organization hasn't configured administrative units, keep the default of **Full directory**.

    Note

    If you are editing an existing policy and change the administrative units, you must now reconfigure the locations in the next step.
2. For the **Choose locations where you want to remove the label** page: Select and specify locations for SharePoint and OneDrive. If you don't want to keep the default of **All** included for your chosen locations, select the link to choose specific instances to include, or select the link to choose specific instances to exclude. Then select **Next**.

    Note

    For organizations that are using administrative units and selected in the policy:

    - For SharePoint, you can't use the **Included** or **Excluded** options and must use the **All** default selection.
    - For OneDrive, you can use the **Included** or **Excluded** options, but see and can select only users from the administrative units selected in the previous step.
3. For the **Set up common or advanced rules** page: Keep the default of **Common rules** to define rules that identify content to label across your selected locations. If you need different rules per location, including some rules that are only available for SharePoint sites and OneDrive accounts, select **Advanced rules**. Then select **Next**.

    The rules use conditions that include [sensitive information types](sit-sensitive-information-type-learn-about), [trainable classifiers](trainable-classifiers-learn-about), sharing options, and other conditions:

    - To select a sensitive information type or trainable classifier as a condition, under **Content contains**, select **Add**, and then choose **Sensitive info types** or **Trainable classifiers**.
    - To select sharing options as a condition, under **Content is shared**, choose either **only with people inside my organization** or **with people outside my organization**.
    - Other conditions that you can select:
        - Attachment or file extension is
        - Attachment or document name matches words or phrases
        - Attachment or document property is
        - Attachment or document size equals or is greater than

    In **Advanced rules**, the name condition is **Document name contains words or phrases** for SharePoint and OneDrive.

    If you selected **Advanced rules**, there is one other condition that you can select:

    - Document created by
4. Depending on your previous choices, you'll now have an opportunity to create new rules by using conditions and exceptions.

    The configuration options for sensitive information types are the same as those you select for auto-labeling for Office apps. If you need more information, see Configuring sensitive info types for a label.

    When you've defined all the rules you need, and confirmed their status is on, select **Next**.
5. For the **Decide if you want to test out the policy now or later** page: Select **Run policy in simulation mode** if you're ready to run the auto-labeling policy now, in simulation mode. Then decide whether to automatically turn on the policy if it's not edited for 7 days.

    If you're not ready to run simulation, select **Leave policy turned off**.
6. For the **Summary** page: Review the configuration of your auto-labeling policy and make any changes that you need, and complete the configuration.

---

#### Example: Apply a label to Exchange email based on the subject

In this example, an auto-labeling policy applies the **High Confidence** sensitivity label when an email subject matches the fictional project codename `Project Atlas`.

1. Make sure the **High Confidence** sensitivity label is published to at least one user and its scope includes **Emails**.
2. Follow the preceding steps to create a policy that automatically applies a label. Select **Custom** &gt; **Custom policy**, and then select the **High Confidence** label.
3. On the **Choose locations where you want to apply the label** page, select **Exchange**. Keep the default of **All** included and **None** excluded if the policy must evaluate incoming email from outside your organization.
4. On the **Set up common or advanced rules** page, select **Advanced rules**. Create a rule for Exchange, add the **Subject matches patterns** condition, and enter a regular expression that matches `Project Atlas` in the subject. For information about regular expressions for this condition, see [SubjectMatchesPatterns](/en-us/powershell/module/exchangepowershell/new-autosensitivitylabelrule#-subjectmatchespatterns).
5. Run the policy in simulation mode and send representative test messages while simulation is running. Review the matching messages on the **Items to review** tab, and then turn on the policy.

Note

You don't need an Exchange mail flow rule or a data loss prevention (DLP) policy for this configuration. Exchange auto-labeling policies evaluate messages in transit as they're sent or received; they don't evaluate existing messages stored in mailboxes. Similarly, simulation evaluates messages sent or received while the simulation is running.

Now on the **Information protection** &gt; **Auto-labeling** page, you see your auto-labeling policy in the **Simulation** or **Off** section, depending on whether you chose to run it in simulation mode or not. Select your policy to see the details of the configuration and status (for example, **Policy simulation is still running**). For policies in simulation mode, select the **Items to review** tab to see which emails or documents matched the rules that you specified.

Before selecting **Edit policy**, [preserve simulation results you need for comparison](auto-label-simulation-results#preserve-results-before-editing-or-rerunning). You can modify your policy directly from this interface:

- For a policy in the **Off** section, select the **Edit policy** button.
- For policy in the **Simulation** section, select the **Edit policy** option at the top of the page, from either tab.

    ![Edit auto-labeling policy option.](media/auto-labeling-edit.png)

    When you're ready to run the policy without simulation, select the **Turn on policy** option.

    Note

    Files with no content (i.e. zero bytes in size) may not be labeled.

Auto-labeling policies run continuously until they're deleted. For example, new and modified files will be included with the current policy settings.

### Removing or downgrading sensitivity labels with an auto-labeling policy

An auto-labeling policy can also be used to **remove** a sensitivity label from files that match its conditions — for example, to strip an encryption-enforcing label before content is migrated, shared externally, or reclassified. This mode is powerful, and it also has documented behaviors that customers frequently misdiagnose as a bug when a large removal run appears to do nothing after activation.

**Before you turn on a removal or downgrade policy, know these behaviors:**

- **A simulation match doesn't guarantee successful label removal.** Review actual removal results and failures after the policy is turned on. See Learn about simulation mode for reasons simulation and enforcement results can differ.
- **A removal policy can remove a label that applies Microsoft Purview encryption.** The associated encryption is also removed. Password-protected files and files protected with external or non-Microsoft encryption aren't supported and might report `EncryptedFileNotSupported`. Simulation confirms that files match the policy conditions, but doesn't guarantee that enforcement can successfully modify them.
- **After cross-tenant migration, the source-tenant label often isn't recognized in the target tenant.** The label's tenant-scoped identity moves with the file's metadata but the target tenant's label set doesn't include it, so a target-tenant removal policy can't find the label to strip. Republish the label in the target tenant (or use PowerShell to strip metadata directly) before you run a removal policy.
- **A conflicting active policy that applies a label wins.** If another auto-labeling policy has conditions that match the same files and applies a label, the label-apply wins over the label-remove even when the policy applies a different label than the label selected for removal. The label removal policy might show these files as removed in simulation because simulation evaluates one policy at a time, but after all active policies run, matching files stay labeled instead of becoming unlabeled. See the Prerequisites — detailed reference note beginning "If you have an auto-labeling policy configured to remove a label" for the full conflict-resolution behavior.
- **Removing a label that applies encryption also removes the encryption.** This is intentional but frequently surprising to admins who expected the file to become "unlabeled but still protected." If you need to retain the existing label-applied encryption, don't remove that label with an auto-labeling policy.

To create a removal policy, use the **Automatically remove label only** tab in Creating an auto-labeling policy above.

### Monitoring your auto-labeling policy

After your auto-labeling policy is turned on, you can view the labeling progress for files in your chosen SharePoint and OneDrive locations. Emails aren't included in the labeling progress because they're automatically labeled as they're sent.

Note

Exchange email isn't included in policy-level labeling progress, **Insights** enforcement metrics, or the **Labeled items** view. These views report on files in SharePoint and OneDrive.

To verify labeling for an Exchange email, use [Activity explorer](data-classification-activity-explorer) and filter for the **Sensitivity label applied** activity. Narrow the results by date, sensitivity label, location, and item details, and review **How applied** to verify that the label was applied automatically. Allow [60 to 90 minutes for the activity to appear](data-classification-activity-explorer#when-activities-appear). Activity explorer identifies the resulting label and how it was applied, but doesn't identify the specific auto-labeling policy or rule that applied the label to an Exchange message.

The labeling progress includes the files to be labeled or unlabeled by the policy, the affected files for the last seven days, and the total files affected. A maximum of 500,000 SharePoint and OneDrive files can be automatically labeled per tenant per day, across all auto-labeling policies. Use this progress information to see how many files your policy still needs to label.

When you first turn on your policy, you initially see a value of 0 for files to be labeled until the latest data is retrieved. This progress information updates every 48 hours, so you can expect to see the most current data about every other day. In the earlier policy flyout experience, selecting a policy shows labeling progress by the top 10 sites. The newer full **Overview** page shows **Top 15 sites** instead. The information on the flyout pane might be more current than the aggregated policy information displayed on the **Auto-labeling** main page. To have visibility on all auto-labeling policy progress, use activity explorer for the most up to date information for files and emails that were auto-labeled.

You can also see the results of your auto-labeling policy by using [content explorer](data-classification-content-explorer) when you have the appropriate [permissions](data-classification-content-explorer#permissions):

- **Content Explorer List Viewer** role group lets you see a file's label but not the file's contents.
- **Content Explorer Content Viewer** role group, and **Information Protection** and **Information Protection Investigators** role groups let you see the file's contents.

Content explorer provides a current snapshot of labeled items and doesn't identify the auto-labeling policy that applied a label. Counts can take up to seven days to update, so use Activity explorer instead for recent labeling activity.

However currently, restricted admins won't be able to see labeling activities for OneDrive in activity explorer.

Tip

You can also use content explorer to identify locations that have documents with sensitive information, but are unlabeled. Using this information, consider adding these locations to your auto-labeling policy, and include the identified sensitive information types as rules.

#### Policy-level labeling activity for SharePoint and OneDrive

For auto-labeling policies that are turned on and target SharePoint and OneDrive, you can monitor them right from the main **Auto-labeling** page and use the per-policy review pages. Use these pages to monitor day-to-day labeling activity, spot-check labeled files, and investigate labeling failures.

To view the review pages, you need one of the following roles:

- Compliance Administrator
- Compliance Data Administrator
- Information Protection Admin
- Information Protection Analyst

**Contextual summary** is available in supported portal experiences. To view matched text inside a file, you also need the **Data Classification Content Viewer** role.

To open the newer review pages, go to **Solutions** &gt; **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**. Select a policy, then select **View details** in the policy details panel. Earlier portal experiences might open Activity explorer instead. Most data on the review pages reflects activity from the last 30 days.

The newer review page has separate **Overview**, **Labeled items**, and **Labeling failures** tabs. For policies that remove labels, the item tabs are **Label removed items** and **Label removal failures**.

The **Overview** tab shows labeled and failed file counts and **Top 15 sites**. Its **Labeling activity overview** chart has separate successful and failed series for the last 30 days. For removal policies, the chart is **Label removal activity overview**. The **Configuration details** section shows the policy's locations, exclusions, and rule summary.

The policy details panel's **Insights** tab summarizes the sensitive information types detected in labeled files. A **Labeling failures** card shows the total failure count and the top three failure reasons. For details, see [Use the Insights tab to analyze auto-labeling policies](auto-label-insights-tab).

Use **Labeled items** to review successfully labeled files. Use **Labeling failures**, or **Review items** on the **Labeling failures** card, to investigate failures. Select a file and review its failure reason. In experiences with a **Details** tab, open that tab to find **Failure reason**. File previews and contextual summaries depend on the portal experience and your permissions.

Review the failure reason even when few files fail. Transient infrastructure failures are retried automatically, but file format, protection, or label configuration failures might require action regardless of volume. Some unsupported files require no action. Follow the reason-specific guidance in [Resolve auto-labeling failures in SharePoint and OneDrive files](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/auto-labeling-failures-sharepoint-onedrive).

#### Review coverage by simulation context

In supported portal experiences, **Coverage by simulation context** (preview) reports on SharePoint and OneDrive files. Run the policy in simulation mode, then turn it on before reviewing coverage. The coverage report helps you see which files were labeled, pending, or not labeled, and whether those files were found in the latest simulation run.

**View coverage** can be hidden if the policy isn't turned on or simulation completion information is missing. If the entry is greyed out, point to it or move keyboard focus to it to read the tooltip. The tooltip distinguishes an expired simulation from an unsupported Exchange-only policy. Rerunning an Exchange-only policy in simulation doesn't enable file coverage.

Use this report to:

- Review how labeling activity is distributed after the latest simulation run.
- Identify files that were found in simulation and then labeled during enforcement.
- Review files that are pending, not yet attempted, or failed to apply a label.
- Investigate files that don't have a match in the latest simulation run.

Coverage is based on labeling activity after the latest simulation run and is available for 30 days. After 30 days, **View coverage** is unavailable for that simulation run. To view coverage again, run the policy in simulation mode again and then review the updated coverage report.

The coverage report isn't an all-time policy total and isn't intended to be an exact reconciliation between simulation and enforcement. All-time labeled totals can include activity from before or after the coverage window, so they might not match the counts shown in the coverage report.

To open the coverage report:

1. In the Microsoft Purview portal, go to **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**.
2. Select an auto-labeling policy that includes SharePoint or OneDrive, has completed simulation, and is turned on.
3. In the **Coverage** column, select **View coverage**.

The report groups files by labeling outcome and simulation context.

| Area | What it means |
| --- | --- |
| **Observed files** | Files included in this report because they were found during simulation, enforcement, or both. |
| **Labeled during enforcement** | Files that had a label applied during enforcement. |
| **Not labeled during enforcement** | Files that don't have a successful label application in this report. |
| **Found in simulation** | Files that were found in the latest simulation run. |
| **No simulation match found** | Files that weren't matched to the latest simulation run. |
| **Pending** | Files that don't have a final enforcement outcome yet. |
| **Not yet attempted** | Files that enforcement hasn't attempted to label yet. |
| **Failed to apply label** | Files that enforcement attempted to label, but the attempt failed. |

Select a bucket in the chart to open an item list for that bucket. Depending on the bucket, item details can include the file name, location, workload, label, last activity time, status, and failure reason when available.

Files under **No simulation match found** can be files that were created, changed, or classified after the latest simulation run completed. They can also appear when the report doesn't have enough information to identify a more specific reason. Files under **Failed to apply label** were attempted during enforcement, but the label wasn't applied. Open the item list and review the failure reason when available.

#### Why was — or wasn't — a specific file labeled?

For files in SharePoint and OneDrive, first check what the policy reports. Select the policy, then **View details** in the policy details panel. In the newer experience, use **Labeled items** to review successful labeling or **Labeling failures** to investigate a failure. Earlier portal experiences might open Activity explorer instead.

A simulation match doesn't confirm that a label was applied. A file missing from **Labeling failures** isn't proof of success either. Choose the guidance that matches what you see:

- **The policy is on, but the file isn't labeled.** Check the policy's locations and conditions, then the file's eligibility. Follow [Policy is on but files aren't labeled](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/troubleshoot-auto-labeling-policies#policy-is-on-but-files-arent-labeled).
- **The file has an unexpected label or protection.** Review the policy's conditions and exceptions, label replacement rules, and other matching policies before changing anything. Follow [Existing label or protection isn't what you expect](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/troubleshoot-auto-labeling-policies#existing-label-or-protection-isnt-what-you-expect).
- **The reports show different numbers.** Check which time period and locations each report covers. SharePoint and OneDrive file views don't include Exchange email. Follow [Numbers don't agree or Exchange activity is missing](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/troubleshoot-auto-labeling-policies#numbers-dont-agree-or-exchange-activity-is-missing).

If the file reports a failure, review **Failure reason** (on the **Details** tab, if present). For reason-specific actions, see [Resolve auto-labeling failures in SharePoint and OneDrive files](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/auto-labeling-failures-sharepoint-onedrive).

A new or changed policy can evaluate existing files using available classification. Changing a custom sensitive information type doesn't by itself reclassify unchanged files. A file's last-modified date doesn't establish its classification time. For classification refresh and policy evaluation checks, see [Auto-labeling classification and simulation concepts](auto-label-classification-simulation).

If your rule uses **Document property is** with a mapped SharePoint managed property, check whether the value contains an ampersand (`&`). See the mapped-property limitation in Prerequisites — detailed reference.

### Monitoring your daily labeling volume

Use the main **Auto-labeling** page to review labeling activity across your policies. Depending on your portal experience, you might see **Files Labeled Today** or the newer **Files labeled in the last 30 days** chart. The chart shows daily counts and an average calculated over all 30 days.

These views count label-applied and label-changed activity for SharePoint and OneDrive files associated with your auto-labeling policies. They don't include Exchange email. Use them to spot activity trends, not to measure remaining daily capacity or the number of unique files currently labeled or protected.

### Policy rule fails to load

In rare cases, a malformed rule in an auto-labeling policy can prevent the policy from loading correctly. The most common symptom is that Exchange messages stop matching an otherwise enabled auto-labeling policy, and there might not be any item-level labeling failure to review because the rule never loaded in the first place.

This is different from the SharePoint and OneDrive item-level labeling failures described earlier in this section. Those failures mean a specific file was evaluated against the policy but couldn't be labeled (for example, because of file format or existing protection). A rule-load failure means the policy's rule couldn't be compiled or loaded at all, so *no* content is evaluated against that rule until the problem is fixed.

If you suspect a policy has stopped matching content and there's no corresponding item-level failure, contact Microsoft Support. Support can check whether a rule failed to load and, if so, identify which specific rule is affected.

Important

Only delete and recreate a rule after Microsoft Support has identified the specific rule that failed to load. Don't delete rules from a policy as a general troubleshooting step, because this removes their enforcement.

If Support confirms that a specific rule needs to be recreated, use the following sequence:

1. Record the current configuration of the affected rule before you delete it, including the policy name, rule name, target label, workload/scope, conditions, exceptions, priority, and enabled state. You can use [Get-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/get-autosensitivitylabelrule) to retrieve and save these details.
2. Delete only the rule that Microsoft Support identified, using [Remove-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/remove-autosensitivitylabelrule). Don't delete other rules in the policy.
3. Recreate the rule with the same configuration you recorded, using [New-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/new-autosensitivitylabelrule).
4. Run the policy in simulation mode to confirm the recreated rule matches content as expected.
5. For Exchange, validate the rule by using newly sent or received messages, because auto-labeling for Exchange doesn't apply to messages already at rest in a mailbox.
6. Turn on the policy and confirm that matching activity resumes as expected.

Warning

After you delete the affected rule, enforcement from that rule is paused until it's recreated and the change propagates. Plan for a change window and expect a delay before the recreated rule is fully in effect.

### Exchange auto-labeling rule limits

When you configure an Exchange auto-labeling rule in the Microsoft Purview portal, the **Sender domain is** condition accepts up to **600 domain entries**. If you exceed this limit, saving the policy fails with an error that identifies the maximum of 600.

This limit describes the domain entries in the condition. It doesn't establish a combined domain limit across all rules in a policy.

For Exchange auto-labeling policies, check the parameter-specific limits in [New-AutoSensitivityLabelRule](/en-us/powershell/module/exchangepowershell/new-autosensitivitylabelrule) and [Set-AutoSensitivityLabelRule](/en-us/powershell/module/exchangepowershell/set-autosensitivitylabelrule). These limits are separate from the number of policies or locations that you can configure.

For example, the [FromAddressMatchesPatterns parameter](/en-us/powershell/module/exchangepowershell/new-autosensitivitylabelrule#-fromaddressmatchespatterns) documentation specifies a maximum of 10 regular expressions, with up to 128 characters per expression. These figures describe the values for that parameter, not a combined limit for all conditions in a policy.

Support for multiple values doesn't mean an unlimited number of values. If the parameter reference doesn't specify a maximum for your configuration, contact Microsoft Support for guidance.

### Use PowerShell for auto-labeling policies

You can use [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to create and configure auto-labeling policies. This means you can fully script the creation and maintenance of your auto-labeling policies, which also provides a more efficient method of specifying multiple locations for SharePoint and OneDrive.

To target more than 1,000 SharePoint sites, associate an existing SharePoint adaptive scope with the policy by using the `-SharePointAdaptiveScopes` parameter (or `-SharePointAdaptiveScopesException` for exclusions) with [New-AutoSensitivityLabelPolicy](/en-us/powershell/module/exchange/new-autosensitivitylabelpolicy). This doesn't increase the portal limit; instead, it replaces static site enumeration with dynamic adaptive-scope membership.

Before rerunning simulation, [preserve simulation results you need for comparison](auto-label-simulation-results#preserve-results-before-editing-or-rerunning).

Before you run the commands in PowerShell, you must first [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell). To use PowerShell to start or rerun an auto-labeling policy simulation, connect by using [Connect-IPPSSession](/en-us/powershell/module/exchangepowershell/connect-ippssession) with the *EnableSearchOnlySession* switch:

```powershell
Connect-IPPSSession -EnableSearchOnlySession -UserPrincipalName <admin-UPN>
```

The *EnableSearchOnlySession* switch is required so that the simulation job can be submitted correctly. If a simulation started from PowerShell remains in progress, reconnect in a new PowerShell session with this switch and rerun the simulation, or use the Microsoft Purview portal.

To create a new auto-labeling policy:

```powershell
New-AutoSensitivityLabelPolicy -Name <AutoLabelingPolicyName> -SharePointLocation "<SharePointSiteLocation>" -ApplySensitivityLabel <Label> -Mode TestWithoutNotifications
```

This command creates an auto-labeling policy for a SharePoint site that you specify. For a OneDrive location, use the *OneDriveLocation* parameter, instead.

To add more sites to an existing auto-labeling policy:

```powershell
$spoLocations = @("<SharePointSiteLocation1>","<SharePointSiteLocation2>")
Set-AutoSensitivityLabelPolicy -Identity <AutoLabelingPolicyName> -AddSharePointLocation $spoLocations -ApplySensitivityLabel <Label> -Mode TestWithoutNotifications
```

This command specifies the new SharePoint URLs in a variable that is then added to an existing auto-labeling policy. To add OneDrive locations instead, use the *AddOneDriveLocation* parameter with a different variable, such as *$OneDriveLocations*.

To create a new auto-labeling policy rule:

```powershell
New-AutoSensitivityLabelRule -Policy <AutoLabelingPolicyName> -Name <AutoLabelingRuleName> -ContentContainsSensitiveInformation @{"name"= "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"; "mincount" = "2"} -Workload SharePoint
```

For an existing auto-labeling policy, this command creates a new policy rule to detect the sensitive information type of **U.S. social security number (SSN)**, which has an entity ID of 00aa00aa-bb11-cc22-dd33-44ee44ee44ee. To find the entity IDs for other sensitive information types, refer to [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions).

For more information about the PowerShell cmdlets that support auto-labeling policies, their available parameters and some examples, see the following cmdlet help:

- [Get-AutoSensitivityLabelPolicy](/en-us/powershell/module/exchange/get-autosensitivitylabelpolicy)
- [New-AutoSensitivityLabelPolicy](/en-us/powershell/module/exchange/new-autosensitivitylabelpolicy)
- [New-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/new-autosensitivitylabelrule)
- [Remove-AutoSensitivityLabelPolicy](/en-us/powershell/module/exchange/remove-autosensitivitylabelpolicy)
- [Remove-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/remove-autosensitivitylabelrule)
- [Set-AutoSensitivityLabelPolicy](/en-us/powershell/module/exchange/set-autosensitivitylabelpolicy)
- [Set-AutoSensitivityLabelRule](/en-us/powershell/module/exchange/set-autosensitivitylabelrule)

## Tips to increase labeling reach

Although auto-labeling is one of the most efficient ways to classify, label, and protect Office and PDF files that your organization owns, check whether you can supplement it with any of the following methods to increase your labeling reach:

- For SharePoint document libraries, you can apply a default sensitivity label for new and edited files. To extend the same default label to existing files, use an auto-labeling policy that applies default sensitivity labels from SharePoint document libraries to existing files. For more information, see [Configure a default sensitivity label for a SharePoint document library](sensitivity-labels-sharepoint-default-label).
- With Microsoft Syntex, you can [apply a sensitivity label to a document understanding model](/en-us/microsoft-365/contentunderstanding/apply-a-sensitivity-label-to-a-model), so that identified documents in a SharePoint document library are automatically labeled.
- For Outlook messages, you can [apply a sensitivity label based on attachments that are labeled](sensitivity-labels-office-apps#configure-label-inheritance-from-email-attachments).
- When you use the [Microsoft Purview Information Protection client](information-protection-client):

    - For files in on-premises data stores, such as network shares and SharePoint Server libraries: Use the [scanner](deploy-scanner) to discover sensitive information in these files and label them appropriately. If you're planning to migrate or upload these files to SharePoint in Microsoft 365, use the scanner to label the files before you move them to the cloud.
- Encourage [manual labeling](https://support.microsoft.com/office/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9) after providing users with training which sensitivity labels to apply. When you're confident that users understand which label to apply, consider configuring a default label and mandatory labeling as [policy settings](sensitivity-labels#what-label-policies-can-do).

Additionally, consider [marking new files as sensitive by default](/en-us/sharepoint/sensitive-by-default) in SharePoint to prevent guests from accessing newly added files until at least one DLP policy scans the content of the file.