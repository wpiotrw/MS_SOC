---
layout: Conceptual
title: Use DLP policies for non-Microsoft cloud apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: renukhar
author: Renukhar
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MET150
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
description: Learn how to scope Microsoft Purview DLP policies to non-Microsoft cloud app instances to monitor, detect, and protect sensitive items shared via connected apps like Box, Dropbox, and Google Workspace.
ai-usage: ai-assisted
locale: en-us
document_id: 469a4bd8-af10-82bf-c9d2-51cf66705af3
document_version_independent_id: 469a4bd8-af10-82bf-c9d2-51cf66705af3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-use-policies-non-microsoft-cloud-apps.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-use-policies-non-microsoft-cloud-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-use-policies-non-microsoft-cloud-apps.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e69816a-aaaa-474e-a36f-3ec7790fadc3
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ae012320-d2b3-47d8-abdc-898a64d069a9
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 881c9f55-0105-dafa-da0e-2eb988d04776
---

# Use DLP policies for non-Microsoft cloud apps | Microsoft Learn

Important

The Instances policy location in Microsoft Purview Data Loss Prevention (DLP) and policy creation experiences are being retired on January 6th, 2027, as part of the retirement of Microsoft Defender for Cloud Apps file policies. Recreate your policies in Purview using dedicated policy locations for supported non-Microsoft connected apps before this date. For more information, see [Migrate file policies to Microsoft Purview](/en-us/defender-cloud-apps/migrate-file-policies-to-purview).

You can scope DLP policies to **Instances** to monitor, detect, and take actions when sensitive items are used and shared via non-Microsoft cloud apps.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you begin

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of these role groups

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

### Prepare your Defender for Cloud Apps environment

Before you configure DLP policies scoped to **Instances**, you must prepare your Defender for Cloud Apps environment. For instructions, see [Quickstart: Get started with Microsoft Defender for Cloud Apps](/en-us/defender-cloud-apps/get-started).

### Connect a non-Microsoft cloud app

To use a DLP policy that's scoped to a specific non-Microsoft cloud app, the app must be connected to Defender for Cloud Apps. For information, see:

- [Connect Box](/en-us/defender-cloud-apps/connect-box)
- [Connect Dropbox](/en-us/defender-cloud-apps/connect-dropbox)
- [Connect Google Workspace](/en-us/defender-cloud-apps/connect-google-workspace)
- [Connect Salesforce](/en-us/defender-cloud-apps/connect-salesforce)
- [Connect Cisco Webex](/en-us/defender-cloud-apps/connect-webex)
- [Connect AWS](/en-us/defender-cloud-apps/protect-aws)
- [Connect ServiceNow](/en-us/defender-cloud-apps/protect-servicenow)

After you connect your cloud apps to Defender for Cloud Apps, you can create DLP policies for those apps.

## Create a DLP policy scoped to a non-Microsoft cloud app

Refer to [Create and Deploy data loss prevention policies](dlp-create-deploy-policy) for the procedures to create a DLP policy. Keep these points in mind as you configure your policy:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Custom** &gt; **Custom policy**.
4. Name the policy and add a description.
5. Set the **Admin units** scope as desired.
6. On the **Locations** page, toggle the **Instances** location to on.
7. To select a specific app or instance, select **Edit** &gt; **Specific instances** &gt; **+ Include instances** and then the instances (cloud apps) you want to include. If you don't select a instance, the policy will be scoped to all connected apps in your Microsoft Defender for Cloud Apps tenant.
8. **Create rule** with the desired settings. For more information on policy creation, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy).

    1. Under **Actions** select **Restrict Third Party Apps** and select any of the apps listed.

Note

When you create a DLP policy that is scoped to **Instances**, the same policy will be automatically created in Microsoft Defender for Cloud Apps.