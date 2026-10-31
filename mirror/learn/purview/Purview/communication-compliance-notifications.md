---
layout: Conceptual
title: Use notification templates in Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-notifications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn more about using notification templates in Communication Compliance.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-04-07T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
- microsoft-365-copilot
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: cedd652e-b7ba-e535-e5b5-e0628302aa23
document_version_independent_id: cedd652e-b7ba-e535-e5b5-e0628302aa23
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-notifications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-notifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-notifications.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/37da4cc9-0cfc-42a9-ba5e-805706b01ef8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3661fb96-d414-4a4e-b7ad-9370637790dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
platformId: 05ea0a9d-a797-fd6b-ec4a-10dec2517609
---

# Use notification templates in Communication Compliance | Microsoft Learn

Create notification templates when you want to send users an email reminder for policy matches as part of the issue resolution process. You can only send notifications to the user email address associated with the policy match that generates the specific alert for remediation. When selecting a notification template to apply to a policy violation as part of the remediation workflow, you can choose to accept the field values defined in the template or overwrite the fields as needed.

Notice templates are custom email templates where you define the following message fields in the **Communication Compliance settings** area:

| Field | Required | Details |
| --- | --- | --- |
| **Template name** | Yes | Friendly name for the notice template that you select in the notify workflow during remediation, supports text characters. |
| **Sender address** | Yes | Address of one or more users or groups that send the message to the user with a policy match, selected from the Active Directory for your subscription. |
| **CC and BCC addresses** | No | Optional users or groups to be notified of the policy match, selected from the Active Directory for your subscription. |
| **Subject** | Yes | Information that appears in the subject line of the message, supports text characters. |
| **Message body** | Yes | Information that appears in the message body, supports text or HTML values. |

#### HTML for notices

If you want to create more than a simple text-based email message for notifications, you can create a more detailed message by using HTML in the message body field of a notice template. The following example provides the message body format for a basic HTML-based email notification template:

```HTML
<!DOCTYPE html>
<html>
    <body>
        <h2>Action Required: Contoso Employee Code of Conduct Policy Training</h2>
        <p>A recent message you've sent has generated a policy alert for the Contoso Employee <a href='https://www.contoso.com'>Code of Conduct Policy</a>.</p>
        <p>You are required to attend the Contoso Employee Code of Conduct <a href='https://www.contoso.com'>training</a> within the next 14 days. Please contact <a href='mailto:hr@contoso.com'>Human Resources</a> with any questions about this training request.</p>
        <p>Thank you,</p>
        <p><em>Human Resources</em></p>
    </body>
</html>
```

Note

In Communication Compliance notification templates, the HTML href attribute implementation currently supports only single quotation marks instead of double quotation marks for URL references.