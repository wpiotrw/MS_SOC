---
layout: Conceptual
title: Deploy an information protection solution with Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-protection-solution
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-03-31T00:00:00.0000000Z
audience: Admin
ms.topic: solution-overview
ms.service: purview
ms.subservice: purview-information-protection
search.appverid:
- MOE150
- MET150
ms.collection:
- m365solution-overview
- m365solution-mip
- zerotrust-solution
- highpri
description: Prescriptive guidance to deploy Microsoft Purview Information Protection for your organization.
locale: en-us
document_id: 9d025747-e7b7-0152-3d0a-922d5094c85f
document_version_independent_id: 9d025747-e7b7-0152-3d0a-922d5094c85f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-protection-solution.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-protection-solution
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-protection-solution.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 70cc433d-66f0-b28b-8780-780c9aed908b
---

# Deploy an information protection solution with Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Your information protection strategy is driven by your business needs. Many organizations must comply with regulations, laws, and business practices. Additionally, organizations need to protect proprietary information, such as data for specific projects.

Microsoft Purview Information Protection (formerly Microsoft Information Protection) provides a framework, process, and capabilities you can use to protect sensitive data across clouds, apps, and devices.

## Microsoft Purview Information Protection framework

Use Microsoft Purview Information Protection to help you discover, classify, protect, and govern sensitive information wherever it lives or travels.

![Microsoft Purview Information Protection solution overview](media/mip-solution-overview-extended.png)

For data governance, see [Deploy a data governance solution with Microsoft Purview](data-governance-solution).

Tip

Consider using the new version of [Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) to supplement the information on this page and jumpstart securing your data with Microsoft Purview Information Protection.

DSPM helps you discover, protect, and investigate sensitive data risks across your digital estate by unifying Microsoft Purview Information Protection with other Microsoft Purview solutions and capabilities. With a focus on data security objectives with guided workflows that offer default sensitivity labels, default policies, and more, DSPM helps you monitor, assess, and remediate data risks regardless of where sensitive data resides.

## Licensing

Microsoft Purview Information Protection capabilities are included with Microsoft Purview. The licensing requirements can vary even within capabilities, depending on configuration options. To identify licensing requirements and options, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

## Know your data

![Know your data for Microsoft Purview Information Protection solution overview](media/knowyourdata-mipsolution.png)

Knowing where your sensitive data resides is often the biggest challenge for many organizations. Microsoft Purview Information Protection data classification helps you to discover and accurately classify ever-increasing amounts of data that your organization creates. Graphical representations help you gain insights into this data so you can set up and monitor policies to protect and govern it.

| Step | Description | More information |
| --- | --- | --- |
| 1 | Describe the categories of sensitive information you want to protect.  You already have an idea of what types of information are most valuable to your org and what types aren't. Work with stakeholders to describe these categories that are your starting point. | [Learn about sensitive information types](sit-sensitive-information-type-learn-about)<br>[Learn about trainable classifiers](trainable-classifiers-learn-about) |
| 2 | Discover and classify sensitive data.  Sensitive data in items can be found by using many different methods that include default DLP policies, manual labeling by users, and automated pattern recognition using sensitive information types or machine learning. | [Classifiers overview](data-classification-overview) |
| 3 | View your sensitive items.  Use content explorer and activity explorer for a deeper analysis of sensitive items and the actions that users are taking on these items. | [Get started with content explorer](data-classification-content-explorer)<br>[Get started with activity explorer](data-classification-activity-explorer) |

## Protect your data

![Protect your data for Microsoft Purview Information Protection solution overview](media/protect-mipsolution.png)

Use the information from knowing where your sensitive data resides to help you more efficiently protect it. However, there's no need to wait—you can start to protect your data immediately with a combination of manual, default, and automatic labeling. Then, use [content explorer](data-classification-content-explorer) and [activity explorer](data-classification-activity-explorer) from the previous section to confirm what items are labeled and how your labels are being used.

| Step | Description | More information |
| --- | --- | --- |
| 1 | Define your [sensitivity labels](sensitivity-labels) and policies that will protect your organization's data. In addition to identifying the sensitivity of content, these labels can apply protection actions such as content markings (headers, footers, watermarks), encryption, and other access controls.[Example sensitivity labels](default-sensitivity-labels-policies#default-sensitivity-labels): **Personal** **Public** **General** - **Anyone (unrestricted)** - **All Employees (unrestricted)** **Confidential** - **Anyone (unrestricted)** - **All Employees** - **Trusted People** **Highly Confidential** - **All Employees** - **Specific People**[Example sensitivity label policy](default-sensitivity-labels-policies#default-sensitivity-label-policy): 1. Publish all labels to all users in the tenant  2. Default label of **General \ All Employees (unrestricted**) for items  3. Users must provide a [justification](media/sensitivity-label-justification-required.png) to remove a label or lower its classification | [Get started with sensitivity labels](get-started-with-sensitivity-labels)[Create and configure sensitivity labels and their policies](create-sensitivity-labels)[Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels) |
| 2 | Label and protect data for Microsoft 365 apps and services. Sensitivity labels are supported for Microsoft 365 Word, Excel, PowerPoint, Outlook, Teams meetings, and also containers that include SharePoint and OneDrive sites, and Microsoft 365 groups. Use a combination of labeling methods such as manual labeling, automatic labeling, a default label, and mandatory labeling. [Example configuration for client-side auto-labeling](default-sensitivity-labels-policies#client-side-auto-labeling):  1. Recommend **Confidential \ Anyone (unrestricted)** if 1-9 credit card numbers  2. Recommend **Confidential \ All Employees** if 10+ credit card numbers  -- [typical end user experience, and the user selects the button to show sensitive content (Word only)](media/sensitivity-label-recommended.png)[Example configuration for service-side auto-labeling](default-sensitivity-labels-policies#service-side-auto-labeling):  Apply to all locations (Exchange, SharePoint, OneDrive) 1. Apply **Confidential \ Anyone (unrestricted)** if 1-9 credit card numbers  2. Apply **Confidential \ All Employees** if 10+ credit card numbers  3. Apply **Confidential \ Anyone (unrestricted)** if 1-9 US personal data and full names  4. Apply **Confidential \ All Employees** if 10+ US personal data and full names | [Manage sensitivity labels in Office apps](sensitivity-labels-office-apps)[Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files)[Enable co-authoring for files encrypted with sensitivity labels](sensitivity-labels-coauthoring)[Configure a default sensitivity label for a SharePoint document library](sensitivity-labels-sharepoint-default-label)[Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically)[Use sensitivity labels to protect collaborative workspaces (groups and sites)](sensitivity-labels-teams-groups-sites)[Use sensitivity labels to protect calendar items, Teams meetings, and chat](sensitivity-labels-meetings)[Use sensitivity labels with Microsoft Loop](sensitivity-labels-loop)[Use sensitivity labels to set the default sharing link for sites and documents in SharePoint and OneDrive](sensitivity-labels-default-sharing-link)[Apply a sensitivity label to a model in Microsoft Syntex](/en-us/microsoft-365/contentunderstanding/apply-a-sensitivity-label-to-a-model)[Sensitivity labels in Power BI](/en-us/power-bi/admin/service-security-sensitivity-label-overview) |
| 3 | Discover, label, and protect sensitive items that reside in data stores in the cloud (Box, GSuite, SharePoint, and OneDrive) by using [Microsoft Defender for Cloud Apps](/en-us/cloud-app-security/what-is-cloud-app-security) with your sensitivity labels. [Example configuration for a file policy](/en-us/defender-cloud-apps/use-case-information-protection#prerequisites): Looks for credit card numbers in files stored in a Box account, and then applies a sensitivity label to identify the highly confidential info and encrypt it. | [Discover, classify, label, and protect regulated and sensitive data stored in the cloud](/en-us/cloud-app-security/best-practices#discover-classify-label-and-protect-regulated-and-sensitive-data-stored-in-the-cloud) |
| 4 | Discover, label, and protect sensitive items that reside in data stores on premises by deploying the [information protection scanner](deploy-scanner) with your sensitivity labels. | [Configuring and installing the information protection scanner](deploy-scanner-configure-install) |
| 5 | Auto-apply sensitivity labels in Microsoft Purview Data Map to discover and label items for Azure Blob Storage, Azure files, and Azure Data Lake Storage Gen2. | [Learn about sensitivity labels in Microsoft Purview Data Map](data-map-sensitivity-labels) |

If you're a developer who wants to extend sensitivity labels to line-of-business apps or third-party SaaS apps, see [Microsoft Information Protection (MIP) SDK setup and configuration](/en-us/information-protection/develop/setup-configure-mip).

### Additional protection capabilities

Microsoft Purview includes additional capabilities to help protect data. Not every customer needs these capabilities, and some might be superseded by more recent releases.

Refer to the [Protect your data with Microsoft Purview](information-protection) page for the full list of protection capabilities.

## Prevent data loss

![Prevent data loss for Microsoft Purview Information Protection solution overview](media/dlp-mipsolution.png)

Deploy Microsoft Purview Data Loss Prevention (DLP) policies to govern and prevent the inappropriate sharing, transfer, or use of sensitive data across apps and services. These policies help users make the right decisions and take the right actions when they're using sensitive data.

| Step | Description | More information |
| --- | --- | --- |
| 1 | Learn about DLP.  Organizations have sensitive information under their control, such as financial data, proprietary data, credit card numbers, health records, and social security numbers. To help protect this sensitive data and reduce risk, they need a way to prevent their users from inappropriately sharing it with people who shouldn't have it. This practice is called data loss prevention (DLP). | [Learn about data loss prevention](dlp-learn-about-dlp) |
| 2 | Plan your DLP implementation.  Every organization will plan for and implement data loss prevention (DLP) differently, because every organization's business needs, goals, resources, and situation are unique to them. However, there are elements that are common to all successful DLP implementations. | [Plan for data loss prevention](dlp-overview-plan-for-dlp) |
| 3 | Design and create a DLP policy.  Creating a data loss prevention (DLP) policy is quick and easy, but getting a policy to yield the intended results can be time consuming if you have to do a lot of tuning. Taking the time to design a policy before you implement it gets you to the desired results faster, and with fewer unintended issues, than tuning by trial and error alone. [Help prevent sharing credit card numbers through email](dlp-create-policy-cc-email#help-prevent-sharing-credit-card-numbers-through-email): Prevents emails being sent if they contain credit card numbers or the email has a specific sensitivity label that identities highly confidential info. | [Design a DLP policy](dlp-policy-design)<br>[DLP policy reference](dlp-policy-reference)<br><br>[Create and deploy data loss prevention policies](dlp-create-deploy-policy) |
| 4 | Tune your DLP policies.  After you deploy a DLP policy, you'll see how well it meets the intended purpose. Use that information to adjust your policy settings for better performance. | [Create and deploy data loss prevention policies](dlp-create-deploy-policy) |

## Deployment strategies

The credit card number examples are often helpful for initial testing and end user education. Even if your organization doesn't typically need to protect credit card numbers, the concept of these being sensitive items that need protection is easily understood by users. Many websites provide credit card numbers that are suitable for testing purposes only. You can also search for sites that provide credit card number generators so that you can paste the numbers into documents and emails.

When you're ready to move your automatic labeling and DLP policies into production, change to classifiers and configurations that are suitable for the type of data used by your organization. For example, you might need to use trainable classifiers for intellectual property and specific types of documents, or exact data match (EDM) sensitive information types for privacy data that's related to customers or employees.

Or, you might want to start by discovering and protecting IT-related information that is frequently the target of security attacks. Then, supplement this by checking for and preventing the sharing of passwords with DLP policies for email and Teams chat:

- Use the trainable classifiers **IT** and **IT Infra and Network Security Documents**
- Use the built-in sensitive info type **General Password** and create a custom sensitive info type for "password is" for the different languages used by your users

Deploying an information protection solution isn't a linear deployment but iterative, and often circular. The more you know your data, the more accurately you can label it, and prevent data leakage. The results of those applied labels and policies flow into the [Reports](purview-reports) and tools, which in turn makes more sensitive data visible for you to protect. Or, if you're already protecting that sensitive data, consider whether it requires additional protective actions.

You can start to manually label data as soon as you've defined sensitivity labels. The same classifiers that you use for DLP can be used to automatically find and label more data. You can even use sensitivity labels as a classifier, for example, block sharing items that are labeled highly confidential.

Most customers already have some solutions in place to protect their data. Your deployment strategy might be to build on what you already have, or focus on gaps that offer the most business value or addresses high risk areas.

To help you plan your unique deployment strategy, reference [Get started with sensitivity labels](get-started-with-sensitivity-labels) and [Plan for data loss prevention](dlp-overview-plan-for-dlp).

### Consider a phased deployment

You might prefer to deploy information protection by using a phased deployment that implements progressively restrictive controls. This approach gradually introduces new protection measures for users as you gain familiarity and confidence with the technology. For example:

- From default labels and no encryption, to recommending labels that apply encryption when sensitive data is found, and then automatically applying labels when sensitive data is found.
- DLP policies that progress from auditing oversharing actions, to more restrictive blocking with warning to educate users, and then blocking all sharing.

Details of such a phased deployment might look something like the following plan, where sensitivity labels and DLP policies become more integrated with each other to provide greater data protection than if they were used independently:

![Conceptual graphic for a phased deployment where sensitivity labels and DLP policies become more integrated and the controls more restricted.](media/information-protection-phased.png)

# [Phase 1](#tab/phase-one)
Sensitivity label configurations:

- **General\All Employees**: Default label for email. No encryption. If applied on emails, block users from over-sharing.
- **Confidential\All Employees**: Default label for documents. No encryption. If applied on emails, block users from over-sharing.
- **Highly Confidential\All Employees**: No encryption. If applied on emails, block users from over-sharing.

DLP policy A:

- If 1-2 instances of credit cards are found, block external sharing except if the item is labeled as **Personal** or **Confidential\Anyone (unrestricted)**. Use logging and reporting for analysis.

DLP policy B:

- If 3-9 instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives except if the item is labeled as **Confidential\Anyone (unrestricted)**. Use logging and reporting for analysis.

DLP policy C:

- If 10+ instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives with no exceptions. Use logging and reporting for analysis.

# [Phase 2](#tab/phase-two)
Sensitivity label configurations:

- **General\All Employees**: Default label for email. No encryption. If applied on emails, block users from over-sharing.
- **Confidential\All Employees**: Default label for documents. Encryption with Full Control to all employees. If applied on emails, block users from over-sharing.
- **Confidential\Trusted People**: Encryption that lets users assign permissions with Encrypt-Only for Outlook and prompts users in Word, PowerPoint, and Excel. If applied on emails, display DLP tooltip to warn users that unauthorized users won't be able to read the email.
- **Highly Confidential\All Employees**: Encryption with Full Control to all employees. If applied on emails, block users from over-sharing. Recommend the label if 3-9 instances of credit cards are found with high confidence, or 10+ instances of credit cards are found with low confidence.

DLP policy A:

- If 1-2 instances of credit cards are found, block external sharing except if the item is labeled as **Personal** or **Confidential\Anyone (unrestricted)**. Send an alert on repeat actions in a short period of time.

DLP policy B:

- If 3-9 instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives except if the item is labeled as **Confidential\Anyone (unrestricted)**. Send alert on repeat actions over time.

DLP policy C:

- If 10+ instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives with no exceptions. Report on each individual action.

# [Phase 3](#tab/phase-three)
Sensitivity label configurations:

- **General\All Employees**: Default label for email. No encryption. If applied on emails, block users from over-sharing.
- **Confidential\All Employees**: Default sublabel for the parent label or label group, **Confidential**. Encryption with all usage rights except Export and Full Control to all employees. Encryption with Full Control usage rights to managers. Recommend the label if 1-9 instances of credit cards are found with low confidence.
- **Confidential\Trusted People**: Encryption that lets users assign permissions with Encrypt-Only for Outlook and prompts users in Word, PowerPoint, and Excel. If applied on emails, display DLP tooltip to warn users that unauthorized users won't be able to read the email.
- **Highly Confidential\All Employees**: Encryption with all usage rights except Export and Full Control to all employees. Encryption with Full Control usage rights to managers. Recommend the label if 1-9 instances of credit cards are found with low confidence. If applied on emails, block users from over-sharing. Automatically apply the label if 3-9 instances of credit cards are found with high confidence, or 10+ instances of credit cards are found with low confidence.
- **Highly Confidential\Specific People**: Encryption that lets users assign permissions with Do Not Forward for Outlook and prompts users in Word, PowerPoint, and Excel. Exception for all DLP blocking rules.

DLP policy A:

- If 1-2 instances of credit cards are found, block external sharing except if the item is labeled as **Personal**, **Confidential\Trusted People**, or **Highly Confidential\Specific People**. Send an alert on repeat actions in a short period of time.

DLP policy B:

- If 3-9 instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives except if the item is labeled as **Confidential\Anyone (unrestricted)** or **Highly Confidential\Specific People**. Send alert on repeat actions over time.

DLP policy C:

- If 10+ instances of credit cards are found, block external sharing, cloud egress, and copy to removable drives with no exceptions. Report on each individual action.

DLP policy D:

- If sensitivity labels of either **General\All Employees**, **Confidential\All Employees**, or **Highly Confidential\All Employees** block external sharing with policy tip and no exceptions.

---

Configuration details for this example phased deployment:

- [Default sublabel for a parent label or label group](sensitivity-labels-office-apps#specify-a-default-sublabel-for-a-parent-label-or-label-group)
- [Data loss prevention Exchange conditions and actions reference](dlp-exchange-conditions-and-actions)
- [Confidence levels and other elements of a sensitivity type](sit-sensitive-information-type-learn-about#fundamental-parts-of-a-sensitive-information-type)
- [Use sensitivity labels as conditions in DLP policies](dlp-sensitivity-label-as-condition)
- [Encryption that lets users assign permissions](encryption-sensitivity-labels#let-users-assign-permissions)
- [Encryption for specific usage rights](encryption-sensitivity-labels#assign-permissions-to-specific-users-or-groups)
- [Configure and view alerts for data loss prevention policies](dlp-configure-view-alerts-policies)

For other deployment guidance that includes a phased deployment strategy, see [Secure by default with Microsoft Purview and protect against oversharing](/en-us/purview/deploymentmodels/depmod-secure-by-default-intro) from our Product Engineering team.

## Training resources

Interactive guides: [Microsoft Purview Information Protection](https://mslearn.cloudguides.com/guides/Protect%20sensitive%20data%20with%20Microsoft%20Purview%20Information%20Protection)

Learning modules for consultants and admins:

- [Introduction to information protection and data lifecycle management in Microsoft Purview](/en-us/training/modules/m365-compliance-information-governance)
- [Classify data for protection and governance](/en-us/training/modules/m365-compliance-information-classify-data)
- [Protect information in Microsoft Purview](/en-us/training/modules/m365-compliance-information-protect-information)
- [Prevent data loss in Microsoft Purview](/en-us/training/modules/m365-compliance-information-prevent-data-loss)

To help train your users to apply and use the sensitivity labels that you configure for them, see [End-user documentation for sensitivity labels](get-started-with-sensitivity-labels#end-user-documentation-for-sensitivity-labels).

When you deploy data loss prevention policies for Teams, you might find the following end-user guidance useful as an introduction to this technology. It includes some potential messages that users might see: [Teams messages about data loss prevention (DLP) and communication compliance policies](https://support.microsoft.com/office/teams-messages-about-data-loss-prevention-dlp-and-communication-compliance-policies-c5631c3f-f61b-4306-a6ac-6603d9fc5ff0).