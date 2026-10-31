---
layout: Conceptual
title: Manage hold notifications | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-manage-hold-notifications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the communications workflow in eDiscovery (Premium) to track the status of your legal hold notifications and if necessary update and resend them.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 621f28e8-a02a-aab3-5725-98dfdac0b7b6
document_version_independent_id: 621f28e8-a02a-aab3-5725-98dfdac0b7b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-manage-hold-notifications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-manage-hold-notifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-manage-hold-notifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 61fb44a4-dd5a-13db-6c2d-9115524e3cc4
---

# Manage hold notifications | Microsoft Learn

Important

Legal hold communications with custodians was permanently **retired on August 31, 2025**, this functionality isn't available in the new [eDiscovery experience](edisc).

After you've initiated your legal hold notification workflow, you can use the communications workflow in Microsoft Purview eDiscovery (Premium) to track the status of your communications. The Communications tab contains a list of all notifications within your eDiscovery (Premium) case. You can see details such as the number of custodians that have been assigned or have acknowledged the notice.

## Monitor acknowledgments

After you select a communication from the **Communications** tab, you can view a list of custodians that have acknowledged a hold notice.

1. In the Microsoft Purview portal, go to **eDiscovery &gt; eDiscovery (Premium)**.
2. Select a case and then select the **Communications** tab.
3. Select a communication to display the **Custodian communication** flyout page.

A list of custodians associated with the selected communication is displayed on the communication flyout page. This page also displays insights and about how many acknowledgments were received and how many are outstanding. The page also shows which custodians have sent an acknowledgment that they received the hold notification.

## Resend a hold notice

Occasionally, custodians lose track of email messages in their day-to-day work. Or for a long-running litigation case, a custodian may contact you or others and request that you resend a notice. As you manage the communications workflow for legal hold notices, you may need to resend a notice to bring it back to the "top of a user's mailbox".

To resend a hold notice to a custodian:

1. In eDiscovery (Premium), select a case and then select the **Communications** tab.
2. Select a communication to display the **Custodian communication** flyout page.
3. Select **More &gt; Re-send hold notice**.
4. On the **Re-send hold notice** flyout page, select the custodians that you what to resend the notice and type an optional reason.
5. Select **Re-send** to send the notice to the selected custodians.

If a custodian hasn't acknowledged the hold notification, the reminder and escalation workflow is restarted. If a custodian has acknowledged the hold notice, the custodian will receive a copy of the original hold notice.

Note

You can only resend a legal hold notification to custodians that are assigned to the communication.

## Update preservation requirements

As the case progresses, custodians may be required to preserve additional or less data than was previously instructed. In eDiscovery terms, you need to reissue the hold notice with updated content.

To update the contents of the initial hold notice:

1. In eDiscovery (Premium), select a case and then select the **Communications** tab.
2. Select the hold notice that you want to update and select **Edit** on the **Custodian communication** flyout page.
3. In the **Edit Communication** workflow, select **Define Portal Content** in the left pane of the workflow, and update the contents of the notice.
4. Select **Save**.

The reissuance notice will be sent to all the custodians assigned to the legal hold notification. In addition, if the Reminder or Escalation notice is enabled, then the workflows for those types of notices will restart.

## Update legal hold notifications and settings

When you update the content or settings of the Issuance, Release, Reissue, Reminder, or Escalation notice, these changes will apply to all future communications generated by the workflow.

## More information

- [Add custodians to a case](ediscovery-add-custodians-to-case)
- [Create a legal hold notice](ediscovery-create-hold-notification)
- [Acknowledge a hold notification](ediscovery-acknowledge-hold-notification)